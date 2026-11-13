# NOTES (coa2): Companies Act 2006, ss 53 to 111 (lines 564-1413 of `ukpga-2006-46.txt`)

Parts 5 (a company's name), 6 (registered office and email address) and 7 (re-registration as a means of altering a company's status).
Part agent `coa2`, run `dst-coa2`, encoded for the stable `l4` 1.6.110 (main, e51181d), compared against 1.6.109 (main, 4c887e0).

**Status, and how each claim below was checked (read this first).**

- Every count below was read from a program's output at the end of the session, not from memory: the assertion counts and the "same on main" column from `check.sh` (its full output is under "What `check.sh` prints"), the source-locator result from `srcrefs.py check --refs` and `--strict`, the trace result from `coa2-tracecheck.py`, the coverage counts from the coverage generator, and the FALSE-kind and NOTHING-kind quotations from a script that looks each quoted fragment up in the raw text.
- **Expected values were written from the text of the section the test names, before the encoding was run.** A test that agreed with the encoding on its first run was not trusted on that account: the NOT-precedence defect (finding in "What the stable binary does not accept") was found by a hand-written expectation that the encoding failed.
- Nothing in this folder is a legal opinion. The two readings the brief marks "for a lawyer" are taken as the status quo and listed in "Marginal readings for a lawyer".
- **About the text.** `ukpga-2006-46.txt` is a plain-text rendering of the Act made by a converter script. It is not the official text, and nothing here is "verified against the official text". Where the rendering looks damaged (two fine wordings run together, paragraphs shown as dots, `...` left in a sentence) the row says so and the encoding does not guess.
- **Where `PLAN.md` and the brief differ, the brief governs.** The one difference that mattered: `PLAN.md` records that both supplied builds check and run `REFUSE`, `#ASSERT REFUSED` and `YMD`; the brief forbids them, so none is used (a "not covered" case is `NOTHING`, and dates are `Date day month year`).

## Files

Layer 1 (the law, objectively; each imports the keel's read-only `coa-core.l4` and `prelude`/`daydate`):

| module | sections | tests |
| --- | --- | --- |
| `coa2-ch1-prohibited-names.l4` | ss 53 to 57C | `coa2-tests-ch1.l4` |
| `coa2-ch2-company-type.l4` | ss 58 to 65 | `coa2-tests-ch2.l4` |
| `coa2-ch3-similarity.l4` | ss 66 to 74 | `coa2-tests-ch3.l4` |
| `coa2-ch4-other-powers.l4` | ss 75 to 76E | `coa2-tests-ch4.l4` |
| `coa2-ch5-ch6-name-change-disclosure.l4` | ss 77 to 85 | `coa2-tests-ch5-ch6.l4` |
| `coa2-part6-registered-office.l4` | ss 86 to 88B | `coa2-tests-part6.l4` |
| `coa2-part7-private-to-public.l4` | ss 89 to 96 | `coa2-tests-part7a.l4` |
| `coa2-part7-other-routes.l4` | ss 97 to 111 | `coa2-tests-part7b.l4` |

Layer 2 (the seat): `coa2-seat.l4` and `coa2-cases-seat.l4`.
Also here: `coa2-tracecheck.py` (checks the `#TRACE` results, which `l4 run` prints but cannot assert), `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md`.
The scripts that built the coverage table and expanded the source quotations live in `../../work/` next to this folder, outside the deposit, and are not shipped.
Every module quotes the text with `-- src:N | ...` lines and a `@ref ... (src:a-b)` above each declaration; both `srcrefs.py` modes report 0 problems.

## Coverage (coa2)

One row per text unit of lines 564-1413 (every Part, Chapter and cross-heading, section, subsection, paragraph, sub-paragraph, defined term and unlabelled body paragraph), built by a script that reads the raw text, plus one row per term defined inside a subsection.
Each row has exactly one disposition: `encoded`, `fork N` (see the fork register), `inert (reason 1, 2 or 3)`, or `repealed or blank in this text`.
The L4 name column lists the layer-1 functions whose quotation covers the unit (at most four shown); a section row lists its principal function and says its subsections follow.

**Audit counts.** Text units counted by the script: **801** (317 subsection, 312 para, 71 section, 61 subpara, 32 heading, 5 body, 3 defterm). Non-blank lines in the range: **850**; lines in no unit: **0**. Rows before adding the defined-term rows: **801**; rows after (23 defined terms defined inside a subsection): **824**.

**Counts per disposition (all 824 rows).** encoded 631; fork 67 (fork 1: 2, fork 10: 5, fork 11: 3, fork 12: 1, fork 13: 3, fork 14: 3, fork 15: 1, fork 16: 3, fork 17: 3, fork 2: 2, fork 2, 18: 1, fork 2, 19: 1, fork 2, 20: 1, fork 2, 21: 1, fork 3: 7, fork 4: 4, fork 5: 6, fork 6: 2, fork 7: 15, fork 8: 2, fork 9: 1); inert reason 1 32; inert reason 2 92; inert reason 3 0; repealed or blank in this text 2.

**Inert rows and their reasons.** Reason 1 (not operative): the 32 headings (Parts 5 to 7, the Chapters, and the cross-headings). Reason 2 (machinery): regulation-making and rule-making powers and the procedure that governs the regulations (ss 54(3), 55(2), 56(1), 57(1), 57(2), 57(4), 60(4), 65(1), 65(2), 65(5), 66(2) to (5), 67(2) to (5), 82(1) to (3), 82(5), 84(1), 84(2)); the transitional provisions on articles that stopped having effect at commencement (s 63(4), s 63(5)); the appointment, terms and staffing of company names adjudicators (s 70) and their rules of procedure (s 71). Reason 3: none (the two blank paragraphs are their own disposition).

**Fork rows.** The entries of the fork register are numbered in "Fork register (coa2)"; the row names the entry and the function that encodes the reading taken.

| unit | lines | text | disposition | L4 name (layer 1), or the reason |
| --- | --- | --- | --- | --- |
| heading@564 | 564 | Part 5 — A company's name | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| heading@565 | 565 | Chapter 1 — General requirements | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| heading@566 | 566 | Prohibited names | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 53 | 567 | Prohibited names | encoded | `s 53 the company may be registered by the name` (see the rows of its subsections) |
| s 53 text | 568 | A company must not be registered under this Act by a name if | encoded | `s 53 the company may be registered by the name` |
| s 53(a) | 569 | (a) its use by the company would constitute an offence, or | encoded | `s 53 the company may be registered by the name` |
| s 53(b) | 570 | (b) it is offensive. | encoded | `s 53 the company may be registered by the name` |
| s 53A | 571 | Names for criminal purposes | encoded | `s 53A the company may be registered by the name` (see the rows of its subsections) |
| s 53A text | 572 | A company must not be registered under this Act by a name if | encoded | `s 53A the company may be registered by the name` |
| s 53A(a) | 573 | (a) the commission of an offence involving dishonesty or dec | encoded | `s 53A the company may be registered by the name` |
| s 53A(b) | 574 | (b) the carrying out of conduct that, if carried out in any  | encoded | `s 53A the company may be registered by the name` |
| heading@575 | 575 | Sensitive words and expressions | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 54 | 576 | Names suggesting connection with government or public author | encoded | `s 54(2) the body is a local authority`; `s 54(2) the person or body is a public authority`; +1 more (see the rows of its subsections) |
| s 54(1) | 577 | (1) The approval of the Secretary of State is required for a | encoded | `s 54(1) the approval of the Secretary of State is required` |
| s 54(1)(a) | 578 | (a) Her Majesty's Government, any part of the Scottish admin | encoded | `s 54(1) the approval of the Secretary of State is required` |
| s 54(1)(b) | 579 | (b) a local authority, or | encoded | `s 54(1) the approval of the Secretary of State is required` |
| s 54(1)(c) | 580 | (c) any public authority specified for the purposes of this  | encoded | `s 54(1) the approval of the Secretary of State is required` |
| s 54(2) | 581 | (2) For the purposes of this section— | encoded | `s 54(2) the body is a local authority`; `s 54(2) the person or body is a public authority` |
| term "local authority" @582 | 582 | “local authority” means— | encoded | `s 54(2) the body is a local authority` |
| s 54(2)(a) | 583 | (a) a local authority within the meaning of the Local Govern | encoded | `s 54(2) the body is a local authority` |
| s 54(2)(b) | 584 | (b) a council constituted under section 2 of the Local Gover | encoded | `s 54(2) the body is a local authority` |
| s 54(2)(c) | 585 | (c) a district council in Northern Ireland; | encoded | `s 54(2) the body is a local authority` |
| term "public authority" @586 | 586 | “public authority” includes any person or body having functi | encoded | `s 54(2) the person or body is a public authority` |
| s 54(3) | 587 | (3) Regulations under this section are subject to affirmativ | inert (reason 2) | machinery: regulations subject to affirmative resolution procedure |
| s 55 | 588 | Other sensitive words or expressions | encoded | `s 55(1) the approval of the Secretary of State is required` (see the rows of its subsections) |
| s 55(1) | 589 | (1) The approval of the Secretary of State is required for a | encoded | `s 55(1) the approval of the Secretary of State is required` |
| s 55(2) | 590 | (2) Regulations under this section are subject to approval a | inert (reason 2) | machinery: regulations subject to approval after being made |
| s 56 | 591 | Duty to seek comments of government department or other spec | encoded | `s 56(5) the department or body is specified`; `s 56(2) the applicant must request the specified department or body in writing to indicate whether and why it has any objections`; +4 more (see the rows of its subsections) |
| s 56(1) | 592 | (1) The Secretary of State may by regulations under— | inert (reason 2) | machinery: power to make regulations (who must seek the view of a department) |
| s 56(1)(a) | 593 | (a) section 54 (name suggesting connection with government o | inert (reason 2) | machinery: power to make regulations (who must seek the view of a department) |
| s 56(1)(b) | 594-595 | (b) section 55 (other sensitive words or expressions), | inert (reason 2) | machinery: power to make regulations (who must seek the view of a department) |
| s 56(2) | 596 | (2) Where such a requirement applies, the applicant must req | encoded | `s 56(2) the applicant must request the specified department or body in writing to indicate whether and why it has any objections` |
| s 56(3) | 597 | (3) Where a request under this section is made in connection | encoded | `s 56(3)(a) the application must include a statement that a request under this section has been made`; `s 56(3)(b) the application must be accompanied by a copy of the response received` |
| s 56(3)(a) | 598 | (a) include a statement that a request under this section ha | encoded | `s 56(3)(a) the application must include a statement that a request under this section has been made` |
| s 56(3)(b) | 599 | (b) be accompanied by a copy of any response received. | encoded | `s 56(3)(b) the application must be accompanied by a copy of the response received` |
| s 56(4) | 600 | (4) Where a request under this section is made in connection | encoded | `s 56(4)(a) the notice of the change must be accompanied by a statement by a director or secretary that a request has been made`; `s 56(4)(b) the notice of the change must be accompanied by a copy of the response received` |
| s 56(4)(a) | 601 | (a) a statement by a director or secretary of the company th | encoded | `s 56(4)(a) the notice of the change must be accompanied by a statement by a director or secretary that a request has been made` |
| s 56(4)(b) | 602 | (b) a copy of any response received. | encoded | `s 56(4)(b) the notice of the change must be accompanied by a copy of the response received` |
| s 56(5) | 603 | (5) In this section “specified” means specified in the regul | encoded | `s 56(5) the department or body is specified` |
| s 56A | 604 | Names suggesting connection with foreign governments etc | encoded | `s 56A the company may be registered by the name` (see the rows of its subsections) |
| s 56A text | 605 | A company must not be registered under this Act by a name th | encoded | `s 56A the company may be registered by the name` |
| s 56A(a) | 606 | (a) a foreign government or an agency or authority of a fore | encoded | `s 56A the company may be registered by the name` |
| s 56A(b) | 607 | (b) an international organisation whose members include two  | encoded | `s 56A the company may be registered by the name` |
| heading@608 | 608 | Permitted characters etc | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 57 | 609 | Permitted characters etc | encoded | `s 57(3) the company may be registered by the name`; `s 57(5) the character, sign, symbol, position or style is specified` (see the rows of its subsections) |
| s 57(1) | 610 | (1) The Secretary of State may make provision by regulations | inert (reason 2) | machinery: power to make regulations (permitted letters and characters, standard style) |
| s 57(1)(a) | 611 | (a) as to the letters or other characters, signs or symbols  | inert (reason 2) | machinery: power to make regulations (permitted letters and characters, standard style) |
| s 57(1)(b) | 612 | (b) specifying a standard style or format for the name of a  | inert (reason 2) | machinery: power to make regulations (permitted letters and characters, standard style) |
| s 57(2) | 613 | (2) The regulations may prohibit the use of specified charac | inert (reason 2) | machinery: power to make regulations (prohibited characters) |
| s 57(3) | 614 | (3) A company may not be registered under this Act by a name | encoded | `s 57(3) the company may be registered by the name` |
| s 57(4) | 615 | (4) Regulations under this section are subject to negative r | inert (reason 2) | machinery: regulations subject to negative resolution procedure |
| s 57(5) | 616 | (5) In this section “specified” means specified in the regul | encoded | `s 57(5) the character, sign, symbol, position or style is specified` |
| heading@617 | 617 | Computer code | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 57A | 618 | Names containing computer code | encoded | `s 57A the company may be registered by the name` (see the rows of its subsections) |
| s 57A text | 619 | A company must not be registered under this Act by a name th | encoded | `s 57A the company may be registered by the name` |
| heading@620 | 620 | Prohibitions where a company has been required to change a n | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 57B | 621 | Prohibition on re-registering name following direction | encoded | `s 57B(3)(a) the name is treated as changed following a direction`; `s 57B(3)(b) the name is treated as changed following an order`; +2 more (see the rows of its subsections) |
| s 57B(1) | 622 | (1) Where a company’s name has at any time been changed foll | encoded | `s 57B(1) the company may be registered by the name` |
| s 57B(2) | 623 | (2) But subsection (1) does not prevent the registration of  | encoded | `s 57B(2) subsection (1) does not prevent registration of the company by the name` |
| s 57B(3) | 624 | (3) In subsection (1)— | encoded | `s 57B(3)(a) the name is treated as changed following a direction`; `s 57B(3)(b) the name is treated as changed following an order` |
| s 57B(3)(a) | 625 | (a) the reference to the name of a company being changed fol | encoded | `s 57B(3)(a) the name is treated as changed following a direction` |
| s 57B(3)(b) | 626 | (b) the reference to the name of a company being changed fol | encoded | `s 57B(3)(b) the name is treated as changed following an order` |
| s 57C | 627 | Name that another company has been directed to change | encoded | `s 57C(4) the person has a relevant relationship with the company`; `s 57C(3) it matters whether the relationships coincided in time`; +4 more (see the rows of its subsections) |
| s 57C(1) | 628 | (1) Where a company has at any time been directed under sect | encoded | `s 57C(1) the other company may be registered by the name` |
| s 57C(1)(a) | 629 | (a) that company is an existing company and there is a perso | encoded | `s 57C(1) the other company may be registered by the name` |
| s 57C(1)(b) | 630 | (b) an application has been made for the registration of tha | encoded | `s 57C(1) the other company may be registered by the name` |
| s 57C(2) | 631 | (2) But subsection (1) does not prevent the registration of  | encoded | `s 57C(2) subsection (1) does not prevent registration of the company by the name` |
| s 57C(3) | 632 | (3) For the purposes of subsection (1) it is irrelevant whet | encoded | `s 57C(3) it matters whether the relationships coincided in time` |
| s 57C(4) | 633 | (4) For the purposes of this section a person has a “relevan | encoded | `s 57C(4) the person has a relevant relationship with the company` |
| s 57C(4)(a) | 634 | (a) an officer, or | encoded | `s 57C(4) the person has a relevant relationship with the company` |
| s 57C(4)(b) | 635 | (b) a member or former member. | encoded | `s 57C(4) the person has a relevant relationship with the company` |
| s 57C(5) | 636 | (5) In subsection (1)— | encoded | `s 57C(5)(a) the company is treated as directed to change its name`; `s 57C(5)(b) the company is treated as ordered to change its name` |
| s 57C(5)(a) | 637 | (a) the reference to the name of a company being changed fol | encoded | `s 57C(5)(a) the company is treated as directed to change its name` |
| s 57C(5)(b) | 638 | (b) the reference to the name of a company being changed fol | encoded | `s 57C(5)(b) the company is treated as ordered to change its name` |
| heading@639 | 639 | Chapter 2 — Indications of company type or legal form | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| heading@640 | 640 | Required indications for limited companies | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 58 | 641 | Public limited companies | encoded | `s 58(1) the name of the company must end with public limited company or p.l.c.`; `s 58(1) the name of the company ends as the section requires` (see the rows of its subsections) |
| s 58(1) | 642 | (1) The name of a limited company that is a public company m | encoded | `s 58(1) the name of the company must end with public limited company or p.l.c.`; `s 58(1) the name of the company ends as the section requires` |
| s 58(2) | 643 | (2) In the case of a Welsh company, its name may instead end | encoded | `s 58(1) the name of the company must end with public limited company or p.l.c.`; `s 58(1) the name of the company ends as the section requires` |
| s 58(3) | 644 | (3) This section does not apply to community interest compan | encoded | `s 58(1) the name of the company must end with public limited company or p.l.c.` |
| s 59 | 645 | Private limited companies | encoded | `s 59(1) the name of the company must end with limited or ltd.`; `s 59(1) the name of the company ends as the section requires` (see the rows of its subsections) |
| s 59(1) | 646 | (1) The name of a limited company that is a private company  | encoded | `s 59(1) the name of the company must end with limited or ltd.`; `s 59(1) the name of the company ends as the section requires` |
| s 59(2) | 647 | (2) In the case of a Welsh company, its name may instead end | encoded | `s 59(1) the name of the company must end with limited or ltd.`; `s 59(1) the name of the company ends as the section requires` |
| s 59(3) | 648 | (3) Certain companies are exempt from this requirement (see  | encoded | `s 59(1) the name of the company must end with limited or ltd.` |
| s 59(4) | 649 | (4) This section does not apply to community interest compan | encoded | `s 59(1) the name of the company must end with limited or ltd.` |
| s 60 | 650 | Exemption from requirement as to use of “limited” | encoded | `s 60(1) the private company is exempt from section 59`; `s 60(2) the registrar may refuse to register the company by the name`; +1 more (see the rows of its subsections) |
| s 60(1) | 651 | (1) A private company is exempt from section 59 (requirement | encoded | `s 60(1) the private company is exempt from section 59` |
| s 60(1)(a) | 652 | (a) it is a charity, | encoded | `s 60(1) the private company is exempt from section 59` |
| s 60(1)(b) | 653 | (b) it is exempted from the requirement of that section by r | encoded | `s 60(1) the private company is exempt from section 59` |
| s 60(1)(c) | 654-656 | (c) it meets the conditions specified in— | encoded | `s 60(1) the private company is exempt from section 59` |
| s 60(2) | 657 | (2) The registrar may refuse to register a private limited c | fork 5 | `s 60(2) the registrar may refuse to register the company by the name` |
| s 60(3) | 658 | (3) The registrar may accept the statement as sufficient evi | encoded | `s 60(3) the registrar may accept the statement as sufficient evidence of the matters stated in it` |
| s 60(4) | 659 | (4) Regulations under this section are subject to negative r | inert (reason 2) | machinery: regulations subject to negative resolution procedure |
| s 61 | 660 | Continuation of existing exemption: companies limited by sha | encoded | `s 61(1) the section applies to the company`; `s 61(1)(a) the date on which the company must have been registered in Great Britain`; +4 more (see the rows of its subsections) |
| s 61(1) | 661 | (1) This section applies to a private company limited by sha | encoded | `s 61(1) the section applies to the company`; `s 61(1)(a) the date on which the company must have been registered in Great Britain`; `s 61(1)(b) the date on which the company must have been registered in Northern Ireland` |
| s 61(1)(a) | 662 | (a) that on 25th February 1982— | encoded | `s 61(1)(a) the date on which the company must have been registered in Great Britain` |
| s 61(1)(a)(i) | 663 | (i) was registered in Great Britain, and | encoded | `s 61(1) the section applies to the company` |
| s 61(1)(a)(ii) | 664 | (ii) had a name that, by virtue of a licence under section 1 | encoded | `s 61(1) the section applies to the company` |
| s 61(1)(b) | 665 | (b) that on 30th June 1983— | encoded | `s 61(1)(b) the date on which the company must have been registered in Northern Ireland` |
| s 61(1)(b)(i) | 666 | (i) was registered in Northern Ireland, and | encoded | `s 61(1) the section applies to the company` |
| s 61(1)(b)(ii) | 667 | (ii) had a name that, by virtue of a licence under section 1 | encoded | `s 61(1) the section applies to the company` |
| s 61(2) | 668 | (2) A company to which this section applies is exempt from s | encoded | `s 61(2) the company is exempt from section 59` |
| s 61(2)(a) | 669 | (a) it continues to meet the following two conditions, and | encoded | `s 61(2) the company is exempt from section 59` |
| s 61(2)(b) | 670 | (b) it does not change its name. | encoded | `s 61(2) the company is exempt from section 59` |
| s 61(3) | 671 | (3) The first condition is that the objects of the company a | encoded | `s 61(3) the first condition is met` |
| s 61(4) | 672 | (4) The second condition is that the company's articles— | encoded | `s 61(4) the second condition is met` |
| s 61(4)(a) | 673 | (a) require its income to be applied in promoting its object | encoded | `s 61(4) the second condition is met` |
| s 61(4)(b) | 674 | (b) prohibit the payment of dividends, or any return of capi | encoded | `s 61(4) the second condition is met` |
| s 61(4)(c) | 675 | (c) require all the assets that would otherwise be available | encoded | `s 61(4) the second condition is met` |
| s 61(4)(c)(i) | 676 | (i) to another body with objects similar to its own, or | encoded | `s 61(4) the second condition is met` |
| s 61(4)(c)(ii) | 677-678 | (ii) to another body the objects of which are the promotion  | encoded | `s 61(4) the second condition is met` |
| s 62 | 679 | Continuation of existing exemption: companies limited by gua | encoded | `s 62(2) the first condition is met`; `s 62(3) the second condition is met`; +1 more (see the rows of its subsections) |
| s 62(1) | 680 | (1) A private company limited by guarantee that immediately  | encoded | `s 62(1) the company is exempt from section 59` |
| s 62(1)(a) | 681 | (a) was exempt by virtue of section 30 of the Companies Act  | encoded | `s 62(1) the company is exempt from section 59` |
| s 62(1)(b) | 682-683 | (b) had a name that did not include the word “limited” or an | encoded | `s 62(1) the company is exempt from section 59` |
| s 62(2) | 684 | (2) The first condition is that the objects of the company a | encoded | `s 62(2) the first condition is met` |
| s 62(3) | 685 | (3) The second condition is that the company's articles— | encoded | `s 62(3) the second condition is met` |
| s 62(3)(a) | 686 | (a) require its income to be applied in promoting its object | encoded | `s 62(3) the second condition is met` |
| s 62(3)(b) | 687 | (b) prohibit the payment of dividends to its members, and | encoded | `s 62(3) the second condition is met` |
| s 62(3)(c) | 688 | (c) require all the assets that would otherwise be available | encoded | `s 62(3) the second condition is met` |
| s 62(3)(c)(i) | 689 | (i) to another body with objects similar to its own, or | encoded | `s 62(3) the second condition is met` |
| s 62(3)(c)(ii) | 690-691 | (ii) to another body the objects of which are the promotion  | encoded | `s 62(3) the second condition is met` |
| s 63 | 692 | Exempt company: restriction on amendment of articles | encoded | `s 63(1) the company may amend its articles as proposed`; `s 63(1) the company's duty not to amend its articles`; +4 more (see the rows of its subsections) |
| s 63(1) | 693 | (1) A private company— | encoded | `s 63(1) the company may amend its articles as proposed`; `s 63(1) the company's duty not to amend its articles` |
| s 63(1)(a) | 694 | (a) that is exempt under section 61 or 62 from the requireme | encoded | `s 63(1) the company may amend its articles as proposed`; `s 63(1) the company's duty not to amend its articles` |
| s 63(1)(b) | 695-696 | (b) whose name does not include “limited” or any of the perm | encoded | `s 63(1) the company may amend its articles as proposed`; `s 63(1) the company's duty not to amend its articles` |
| s 63(2) | 697 | (2) If subsection (1) above is contravened an offence is com | encoded | `s 63(2) the person commits an offence` |
| s 63(2)(a) | 698 | (a) the company, and | encoded | `s 63(2) the person commits an offence` |
| s 63(2)(b) | 699-700 | (b) every officer of the company who is in default. | encoded | `s 63(2) the person commits an offence` |
| s 63(3) | 701 | (3) A person guilty of an offence under this section is liab | fork 1 | `s 63(3) the penalty on summary conviction`; `s 63(3) the daily default fine in pounds on the first wording`; `s 63(3) the daily default fine in pounds on the second wording` |
| s 63(4) | 702 | (4) Where immediately before the commencement of this sectio | inert (reason 2) | machinery: transitional: provisions in articles that stopped having effect at commencement (2008) |
| s 63(4)(a) | 703 | (a) a company was exempt by virtue of section 30 of the Comp | inert (reason 2) | machinery: transitional: provisions in articles that stopped having effect at commencement (2008) |
| s 63(4)(b) | 704 | (b) the company's memorandum or articles contained provision | inert (reason 2) | machinery: transitional: provisions in articles that stopped having effect at commencement (2008) |
| s 63(4)(b)(i) | 705 | (i) the Board of Trade or a Northern Ireland department (or  | inert (reason 2) | machinery: transitional: provisions in articles that stopped having effect at commencement (2008) |
| s 63(4)(b)(ii) | 706-708 | (ii) the Charity Commission, | inert (reason 2) | machinery: transitional: provisions in articles that stopped having effect at commencement (2008) |
| s 63(5) | 709 | (5) It is hereby declared that any such provision as is ment | inert (reason 2) | machinery: transitional declaration about provisions of memoranda formerly in force |
| s 64 | 710 | Power to direct change of name in case of company ceasing to | encoded | `s 64(1) the Secretary of State may direct the company to change its name`; `s 64(2) the direction meets the requirements of subsection (2)`; +12 more (see the rows of its subsections) |
| s 64(1) | 711 | (1) If it appears to the Secretary of State that a company w | fork 10 | `s 64(1) the Secretary of State may direct the company to change its name` |
| s 64(1)(a) | 712 | (a) has ceased to be entitled to exemption under section 60( | fork 10 | `s 64(1) the Secretary of State may direct the company to change its name` |
| s 64(1)(b) | 713 | (b) in the case of a company within section 61 or 62 (which  | fork 10 | `s 64(1) the Secretary of State may direct the company to change its name` |
| s 64(1)(b)(i) | 714 | (i) has carried on any business other than the promotion of  | fork 10 | `s 64(1) the Secretary of State may direct the company to change its name` |
| s 64(1)(b)(ii) | 715-716 | (ii) has acted inconsistently with the provision required by | fork 10 | `s 64(1) the Secretary of State may direct the company to change its name` |
| s 64(2) | 717 | (2) The direction must be in writing and must specify the pe | encoded | `s 64(2) the direction meets the requirements of subsection (2)` |
| s 64(2A) | 718 | (2A) The period must be a period of at least 28 days beginni | encoded | `s 64(2A) the period meets the requirement of subsection (2A)` |
| s 64(2B) | 719-720 | (2B) The Secretary of State may by further direction in writ | fork 2, 18 | `s 64(2B) the Secretary of State may give a further direction extending the period` |
| s 64(3) | 721-722 | (3) A change of name in order to comply with a direction und | encoded | `s 64(3) the company may change its name by resolution of the directors`; `s 64(3) the resolution method does not prejudice another method of changing the name` |
| s 64(4) | 723-724 | (4) Where a resolution of the directors is passed in accorda | encoded | `s 64(4) the company must give notice to the registrar of the change` |
| s 64(5) | 725 | (5) If the company fails to comply with a direction under th | fork 7 | `s 64(5) the company's duty to change its name as directed`; `s 64(5) the person commits an offence` |
| s 64(5)(a) | 726 | (a) the company, and | fork 7 | `s 64(5) the company's duty to change its name as directed`; `s 64(5) the person commits an offence` |
| s 64(5)(b) | 727 | (b) every officer of the company who is in default. | fork 7 | `s 64(5) the company's duty to change its name as directed`; `s 64(5) the person commits an offence` |
| s 64(6) | 728 | (6) A person guilty of an offence under this section is liab | fork 1 | `s 64(6) the penalty on summary conviction`; `s 64(6) the daily default fine in pounds on the first wording`; `s 64(6) the daily default fine in pounds on the second wording` |
| s 64(6A) | 729 | (6A) Where a direction is given under subsection (1), the re | encoded | `s 64(6A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 64(7) | 730-731 | (7) A company that has been directed to change its name unde | encoded | `s 64(7) the approval of the Secretary of State is required for the change of name` |
| heading@732 | 732 | Inappropriate use of indications of company type or legal fo | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 65 | 733 | Inappropriate use of indications of company type or legal fo | encoded | `s 65(3) the company may be registered by the name`; `s 65(4) the word, expression, indication, part of the name or accompanying word is specified` (see the rows of its subsections) |
| s 65(1) | 734 | (1) The Secretary of State may make provision by regulations | inert (reason 2) | machinery: power to make regulations (indications of company type) |
| s 65(1)(a) | 735 | (a) that are associated with a particular type of company or | inert (reason 2) | machinery: power to make regulations (indications of company type) |
| s 65(1)(b) | 736 | (b) that are similar to words, expressions or other indicati | inert (reason 2) | machinery: power to make regulations (indications of company type) |
| s 65(2) | 737 | (2) The regulations may prohibit the use of words, expressio | inert (reason 2) | machinery: power to make regulations (where such words may be used) |
| s 65(2)(a) | 738 | (a) in a specified part, or otherwise than in a specified pa | inert (reason 2) | machinery: power to make regulations (where such words may be used) |
| s 65(2)(b) | 739 | (b) in conjunction with, or otherwise than in conjunction wi | inert (reason 2) | machinery: power to make regulations (where such words may be used) |
| s 65(3) | 740 | (3) A company must not be registered under this Act by a nam | encoded | `s 65(3) the company may be registered by the name` |
| s 65(4) | 741 | (4) In this section “specified” means specified in the regul | encoded | `s 65(4) the word, expression, indication, part of the name or accompanying word is specified` |
| s 65(5) | 742 | (5) Regulations under this section are subject to negative r | inert (reason 2) | machinery: regulations subject to negative resolution procedure |
| heading@743 | 743 | Chapter 3 — Similarity to other names | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| heading@744 | 744 | Similarity to other name on registrar's index | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 66 | 745 | Name not to be the same as another in the index | encoded | `s 66(1) the company may be registered by the name`; `s 66(6) the circumstances or consent are specified` (see the rows of its subsections) |
| s 66(1) | 746 | (1) A company must not be registered under this Act by a nam | fork 9 | `s 66(1) the company may be registered by the name` |
| s 66(2) | 747 | (2) The Secretary of State may make provision by regulations | inert (reason 2) | machinery: power to make regulations (what counts as the same name) |
| s 66(3) | 748 | (3) The regulations may make provision— | inert (reason 2) | machinery: power to make regulations (what is disregarded) |
| s 66(3)(a) | 749 | (a) as to matters that are to be disregarded, and | inert (reason 2) | machinery: power to make regulations (what is disregarded) |
| s 66(3)(b) | 750-751 | (b) as to words, expressions, signs or symbols that are, or  | inert (reason 2) | machinery: power to make regulations (what is disregarded) |
| s 66(4) | 752 | (4) The regulations may provide— | inert (reason 2) | machinery: power to make regulations (circumstances or consent that permit registration) |
| s 66(4)(a) | 753 | (a) that registration by a name that would otherwise be proh | inert (reason 2) | machinery: power to make regulations (circumstances or consent that permit registration) |
| s 66(4)(a)(i) | 754 | (i) in specified circumstances, or | inert (reason 2) | machinery: power to make regulations (circumstances or consent that permit registration) |
| s 66(4)(a)(ii) | 755 | (ii) with specified consent, and | inert (reason 2) | machinery: power to make regulations (circumstances or consent that permit registration) |
| s 66(4)(b) | 756 | (b) that if those circumstances obtain or that consent is gi | inert (reason 2) | machinery: power to make regulations (circumstances or consent that permit registration) |
| s 66(5) | 757 | (5) Regulations under this section are subject to negative r | inert (reason 2) | machinery: regulations subject to negative resolution procedure |
| s 66(6) | 758 | (6) In this section “specified” means specified in the regul | encoded | `s 66(6) the circumstances or consent are specified` |
| s 67 | 759 | Power to direct change of name in case of similarity to exis | encoded | `s 67(1) the Secretary of State may direct the company to change its name`; `s 67(1A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates`; +1 more (see the rows of its subsections) |
| s 67(1) | 760 | (1) The Secretary of State may direct a company to change it | fork 11 | `s 67(1) the Secretary of State may direct the company to change its name` |
| s 67(1)(a) | 761 | (a) a name appearing at the time of the registration in the  | fork 11 | `s 67(1) the Secretary of State may direct the company to change its name` |
| s 67(1)(b) | 762 | (b) a name that should have appeared in that index at that t | fork 11 | `s 67(1) the Secretary of State may direct the company to change its name` |
| s 67(1A) | 763 | (1A) Where a direction is given under subsection (1), the re | encoded | `s 67(1A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 67(2) | 764 | (2) The Secretary of State may make provision by regulations | inert (reason 2) | machinery: power to make regulations (what counts as too like another name) |
| s 67(3) | 765 | (3) The regulations may make provision— | inert (reason 2) | machinery: power to make regulations (what is disregarded) |
| s 67(3)(a) | 766 | (a) as to matters that are to be disregarded, and | inert (reason 2) | machinery: power to make regulations (what is disregarded) |
| s 67(3)(b) | 767-768 | (b) as to words, expressions, signs or symbols that are, or  | inert (reason 2) | machinery: power to make regulations (what is disregarded) |
| s 67(4) | 769 | (4) The regulations may provide— | inert (reason 2) | machinery: power to make regulations (circumstances or consent that bar a direction) |
| s 67(4)(a) | 770 | (a) that no direction is to be given under this section in r | inert (reason 2) | machinery: power to make regulations (circumstances or consent that bar a direction) |
| s 67(4)(a)(i) | 771 | (i) in specified circumstances, or | inert (reason 2) | machinery: power to make regulations (circumstances or consent that bar a direction) |
| s 67(4)(a)(ii) | 772 | (ii) if specified consent is given, and | inert (reason 2) | machinery: power to make regulations (circumstances or consent that bar a direction) |
| s 67(4)(b) | 773 | (b) that a subsequent change of circumstances or withdrawal  | inert (reason 2) | machinery: power to make regulations (circumstances or consent that bar a direction) |
| s 67(5) | 774 | (5) Regulations under this section are subject to negative r | inert (reason 2) | machinery: regulations subject to negative resolution procedure |
| s 67(6) | 775 | (6) In this section “specified” means specified in the regul | encoded | `s 67(6) the circumstances or consent are specified` |
| s 68 | 776 | Direction to change name: supplementary provisions | encoded | `s 68(2)(a) the direction is given within twelve months of the company's registration by the name`; `s 68(2)(b) the direction specifies the period`; +6 more (see the rows of its subsections) |
| s 68(1) | 777 | (1) The following provisions have effect in relation to a di | encoded | `s 68(2)(a) the direction is given within twelve months of the company's registration by the name` |
| s 68(2) | 778 | (2) Any such direction— | encoded | `s 68(2)(a) the direction is given within twelve months of the company's registration by the name`; `s 68(2)(b) the direction specifies the period` |
| s 68(2)(a) | 779 | (a) must be given within twelve months of the company's regi | fork 3 | `s 68(2)(a) the direction is given within twelve months of the company's registration by the name` |
| s 68(2)(b) | 780 | (b) must specify the period within which the company is to c | encoded | `s 68(2)(b) the direction specifies the period` |
| s 68(2A) | 781 | (2A) The period must be a period of at least 28 days beginni | encoded | `s 68(2A) the period meets the requirement of subsection (2A)` |
| s 68(3) | 782-783 | (3) The Secretary of State may by a further direction extend | fork 2 | `s 68(3) the Secretary of State may give a further direction extending the period` |
| s 68(4) | 784 | (4) A direction under section 67 or this section must be in  | encoded | `s 68(4) the direction meets the requirement of being in writing` |
| s 68(5) | 785 | (5) If a company fails to comply with the direction, an offe | encoded | `s 68(5) the company's duty to change its name as directed`; `s 68(5) the person commits an offence` |
| s 68(5)(a) | 786 | (a) the company, and | encoded | `s 68(5) the company's duty to change its name as directed`; `s 68(5) the person commits an offence` |
| s 68(5)(b) | 787-788 | (b) every officer of the company who is in default. | encoded | `s 68(5) the company's duty to change its name as directed`; `s 68(5) the person commits an offence` |
| s 68(6) | 789 | (6) A person guilty of an offence under this section is liab | encoded | `s 68(6) the penalty on summary conviction` |
| heading@790 | 790 | Similarity to other name in which person has goodwill | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 69 | 791 | Objection to company's registered name | encoded | `s 69(1) the applicant may object to the company's registered name`; `s 69(7) the interest is goodwill`; +6 more (see the rows of its subsections) |
| s 69(1) | 792 | (1) A person (“the applicant”) may object to a company's reg | encoded | `s 69(1) the applicant may object to the company's registered name` |
| s 69(1)(a) | 793 | (a) that it is the same as a name associated with the applic | encoded | `s 69(1) the applicant may object to the company's registered name` |
| s 69(1)(b) | 794 | (b) that it is sufficiently similar to such a name that its  | encoded | `s 69(1) the applicant may object to the company's registered name` |
| s 69(2) | 795 | (2) The objection must be made by application to a company n | encoded | `s 69(2) the objection is made as the subsection requires` |
| s 69(3) | 796-797 | (3) The company concerned shall be the primary respondent to | encoded | `s 69(3) the person is the primary respondent to the application`; `s 69(3) the person may be joined as a respondent` |
| s 69(3)(a) | 798 | (a) any member or person who was a member at the time at whi | encoded | `s 69(3) the person may be joined as a respondent` |
| s 69(3)(b) | 799 | (b) any director or person who was a director at the time at | encoded | `s 69(3) the person may be joined as a respondent` |
| s 69(4) | 800 | (4) If the ground specified in subsection (1)(a) or (b) is e | encoded | `s 69(4) the objection is upheld under subsection (4)` |
| s 69(4)(a) | 801 | (a) that the name was registered before the commencement of  | encoded | `s 69(4) the objection is upheld under subsection (4)` |
| s 69(4)(b) | 802 | (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | repealed or blank in this text | the text shows "(b) . . . ." (omitted; the other paragraphs of s 69(4) keep their letters) |
| s 69(4)(c) | 803 | (c) that the name was registered in the ordinary course of a | encoded | `s 69(4) the objection is upheld under subsection (4)` |
| s 69(4)(d) | 804 | (d) that the name was adopted in good faith; or | encoded | `s 69(4) the objection is upheld under subsection (4)` |
| s 69(4)(e) | 805-806 | (e) that the interests of the applicant are not adversely af | encoded | `s 69(4) the objection is upheld under subsection (4)` |
| s 69(5) | 807 | (5) If the facts mentioned in subsection (4)(a) ... or (c) a | encoded | `s 69(5) the objection is nevertheless upheld` |
| s 69(6) | 808 | (6) If the objection is not upheld under subsection (4) or ( | encoded | `s 69(6) the objection is dismissed` |
| s 69(7) | 809 | (7) In this section “goodwill” includes reputation of any de | encoded | `s 69(7) the interest is goodwill` |
| s 70 | 810 | Company names adjudicators | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(1) | 811 | (1) The Secretary of State shall appoint persons to be compa | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(2) | 812 | (2) The persons appointed must have such legal or other expe | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(3) | 813 | (3) An adjudicator— | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(3)(a) | 814 | (a) holds office in accordance with the terms of his appoint | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(3)(b) | 815 | (b) is eligible for re-appointment when his term of office e | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(3)(c) | 816 | (c) may resign at any time by notice in writing given to the | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(3)(d) | 817 | (d) may be dismissed by the Secretary of State on the ground | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(4) | 818-819 | (4) One of the adjudicators shall be appointed Chief Adjudic | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(5) | 820 | (5) The other adjudicators shall undertake such duties as th | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(6) | 821 | (6) The Secretary of State may— | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(6)(a) | 822 | (a) appoint staff for the adjudicators; | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(6)(b) | 823 | (b) pay remuneration and expenses to the adjudicators and th | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(6)(c) | 824 | (c) defray other costs arising in relation to the performanc | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 70(6)(d) | 825 | (d) compensate persons for ceasing to be adjudicators. | inert (reason 2) | machinery: appointment, terms and staffing of company names adjudicators |
| s 71 | 826 | Procedural rules | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(1) | 827 | (1) The Secretary of State may make rules about proceedings  | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2) | 828 | (2) The rules may, in particular, make provision— | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(a) | 829 | (a) as to how an application is to be made and the form and  | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(b) | 830 | (b) for fees to be charged; | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(c) | 831 | (c) about the service of documents and the consequences of f | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(d) | 832 | (d) as to the form and manner in which evidence is to be giv | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(e) | 833 | (e) for circumstances in which hearings are required and tho | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(f) | 834 | (f) for cases to be heard by more than one adjudicator; | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(g) | 835 | (g) setting time limits for anything required to be done in  | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(h) | 836 | (h) enabling the adjudicator to strike out an application, o | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(h)(i) | 837 | (i) on the ground that it is vexatious, has no reasonable pr | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(h)(ii) | 838 | (ii) for failure to comply with the requirements of the rule | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(i) | 839 | (i) conferring power to order security for costs (in Scotlan | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(j) | 840 | (j) as to how far proceedings are to be held in public; | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(2)(k) | 841 | (k) requiring one party to bear the costs (in Scotland, expe | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(3) | 842 | (3) The rules may confer on the Chief Adjudicator power to d | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 71(4) | 843 | (4) Rules under this section shall be made by statutory inst | inert (reason 2) | machinery: power to make rules of procedure for adjudicators |
| s 72 | 844 | Decision of adjudicator to be made available to public | encoded | `s 72(1) the adjudicator's duty to make the decision available`; `s 72(1) the decision was made available within 90 days of the determination`; +1 more (see the rows of its subsections) |
| s 72(1) | 845 | (1) A company names adjudicator must, within 90 days of dete | encoded | `s 72(1) the adjudicator's duty to make the decision available`; `s 72(1) the decision was made available within 90 days of the determination` |
| s 72(2) | 846 | (2) He may do so by means of a website or by such other mean | encoded | `s 72(2) the adjudicator may make the decision available by the means` |
| s 73 | 847 | Order requiring name to be changed | encoded | `s 73(2) the name is an offending name`; `s 73(1) the adjudicator must make an order`; +8 more (see the rows of its subsections) |
| s 73(1) | 848 | (1) If an application under section 69 is upheld, the adjudi | encoded | `s 73(1) the adjudicator must make an order`; `s 73(1)(a) the order requires the person to change its name to one that is not an offending name`; `s 73(1)(b) the order requires the person to take the steps and not to cause or permit steps towards another offending name` |
| s 73(1)(a) | 849 | (a) requiring the respondent company to change its name to o | encoded | `s 73(1)(a) the order requires the person to change its name to one that is not an offending name` |
| s 73(1)(b) | 850 | (b) requiring all the respondents— | encoded | `s 73(1)(b) the order requires the person to take the steps and not to cause or permit steps towards another offending name` |
| s 73(1)(b)(i) | 851 | (i) to take all such steps as are within their power to make | encoded | `s 73(1)(b) the order requires the person to take the steps and not to cause or permit steps towards another offending name` |
| s 73(1)(b)(ii) | 852 | (ii) not to cause or permit any steps to be taken calculated | encoded | `s 73(1)(b) the order requires the person to take the steps and not to cause or permit steps towards another offending name` |
| s 73(2) | 853 | (2) An “offending name” means a name that, by reason of its  | encoded | `s 73(2) the name is an offending name` |
| s 73(2)(a) | 854 | (a) to be the subject of a direction under section 67 (power | encoded | `s 73(2) the name is an offending name` |
| s 73(2)(b) | 855 | (b) to give rise to a further application under section 69. | encoded | `s 73(2) the name is an offending name` |
| s 73(3) | 856 | (3) The order must specify a date by which the respondent co | encoded | `s 73(3) the order meets the requirement to specify a date`; `s 73(3) the order may be enforced` |
| s 73(3)(a) | 857 | (a) in England and Wales or Northern Ireland, in the same wa | encoded | `s 73(3) the order may be enforced` |
| s 73(3)(b) | 858 | (b) in Scotland, in the same way as a decree of the Court of | encoded | `s 73(3) the order may be enforced` |
| s 73(4) | 859 | (4) If the respondent company's name is not changed in accor | fork 12 | `s 73(4) the adjudicator may determine a new name for the company` |
| s 73(5) | 860 | (5) If the adjudicator determines a new name for the respond | encoded | `s 73(5) the adjudicator must give notice of his determination to the recipient` |
| s 73(5)(a) | 861 | (a) to the applicant, | encoded | `s 73(5) the adjudicator must give notice of his determination to the recipient` |
| s 73(5)(b) | 862 | (b) to the respondents, and | encoded | `s 73(5) the adjudicator must give notice of his determination to the recipient` |
| s 73(5)(c) | 863 | (c) to the registrar. | encoded | `s 73(5) the adjudicator must give notice of his determination to the recipient` |
| s 73(6) | 864 | (6) For the purposes of this section a company's name is cha | encoded | `s 73(6) the name is changed in accordance with the order by the specified date` |
| s 73(7) | 865 | (7) Where an order is made under subsection (1), the registr | encoded | `s 73(7) the registrar may omit from the register material available for public inspection any mention of the name to which the order relates` |
| s 74 | 866 | Appeal from adjudicator's decision | encoded | `s 74(1) an appeal lies to the court from the decision`; `s 74(2) notice of appeal is given in time`; +3 more (see the rows of its subsections) |
| s 74(1) | 867 | (1) An appeal lies to the court from any decision of a compa | encoded | `s 74(1) an appeal lies to the court from the decision` |
| s 74(2) | 868 | (2) Notice of appeal against a decision upholding an applica | encoded | `s 74(2) notice of appeal is given in time` |
| s 74(3) | 869 | (3) If notice of appeal is given against a decision upholdin | encoded | `s 74(3) the effect of the adjudicator's order is suspended` |
| s 74(4) | 870 | (4) If on appeal the court— | fork 13 | `s 74(4) the court may specify the date, remit the matter or make any order or determination that the adjudicator might have made` |
| s 74(4)(a) | 871 | (a) affirms the decision of the adjudicator to uphold the ap | fork 13 | `s 74(4) the court may specify the date, remit the matter or make any order or determination that the adjudicator might have made` |
| s 74(4)(b) | 872-873 | (b) reverses the decision of the adjudicator to dismiss the  | fork 13 | `s 74(4) the court may specify the date, remit the matter or make any order or determination that the adjudicator might have made` |
| s 74(5) | 874 | (5) If the court determines a new name for the company it mu | encoded | `s 74(5) the court must give notice of the determination to the recipient` |
| s 74(5)(a) | 875 | (a) to the parties to the appeal, and | encoded | `s 74(5) the court must give notice of the determination to the recipient` |
| s 74(5)(b) | 876 | (b) to the registrar. | encoded | `s 74(5) the court must give notice of the determination to the recipient` |
| heading@877 | 877 | Chapter 4 — Other powers of the Secretary of State and the r | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| heading@878 | 878 | Provision of misleading information | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 75 | 879 | Provision of misleading information etc | encoded | `s 75(1) the Secretary of State may direct the company to change its name`; `s 75(2)(a) the direction is given within five years of the company's registration by that name`; +8 more (see the rows of its subsections) |
| s 75(1) | 880 | (1) If it appears to the Secretary of State— | fork 14 | `s 75(1) the Secretary of State may direct the company to change its name` |
| s 75(1)(a) | 881 | (a) that misleading information has been given for the purpo | fork 14 | `s 75(1) the Secretary of State may direct the company to change its name` |
| s 75(1)(b) | 882-883 | (b) that an undertaking or assurance has been given for that | fork 14 | `s 75(1) the Secretary of State may direct the company to change its name` |
| s 75(2) | 884 | (2) Any such direction— | encoded | `s 75(2)(a) the direction is given within five years of the company's registration by that name`; `s 75(2)(b) the direction specifies the period` |
| s 75(2)(a) | 885 | (a) must be given within five years of the company's registr | fork 3 | `s 75(2)(a) the direction is given within five years of the company's registration by that name` |
| s 75(2)(b) | 886 | (b) must specify the period within which the company is to c | encoded | `s 75(2)(b) the direction specifies the period` |
| s 75(2A) | 887 | (2A) The period must be at least 28 days beginning with the  | encoded | `s 75(2A) the period meets the requirement of subsection (2A)` |
| s 75(3) | 888-889 | (3) The Secretary of State may by a further direction extend | fork 2 | `s 75(3) the Secretary of State may give a further direction extending the period` |
| s 75(4) | 890 | (4) A direction under this section must be in writing. | encoded | `s 75(4) the direction meets the requirement of being in writing` |
| s 75(4A) | 891 | (4A) Where a direction is given under subsection (1), the re | encoded | `s 75(4A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 75(5) | 892 | (5) If a company fails to comply with a direction under this | encoded | `s 75(5) the company's duty to change its name as directed`; `s 75(5) the person commits an offence` |
| s 75(5)(a) | 893 | (a) the company, and | encoded | `s 75(5) the company's duty to change its name as directed`; `s 75(5) the person commits an offence` |
| s 75(5)(b) | 894-895 | (b) every officer of the company who is in default. | encoded | `s 75(5) the company's duty to change its name as directed`; `s 75(5) the person commits an offence` |
| s 75(6) | 896 | (6) A person guilty of an offence under this section is liab | encoded | `s 75(6) the penalty on summary conviction` |
| heading@897 | 897 | Misleading indication of activities and names used for crimi | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 76 | 898 | Misleading indication of activities | encoded | `s 76(1) the Secretary of State may direct the company to change its name`; `s 76(2) the direction meets the requirements of subsection (2)`; +11 more (see the rows of its subsections) |
| s 76(1) | 899 | (1) If in the opinion of the Secretary of State the name by  | fork 15 | `s 76(1) the Secretary of State may direct the company to change its name` |
| s 76(2) | 900 | (2) The direction must be in writing and must specify the pe | encoded | `s 76(2) the direction meets the requirements of subsection (2)` |
| s 76(3) | 901 | (3) The period must be a period of at least 28 days beginnin | encoded | `s 76(3) the period meets the requirement of subsection (3)` |
| s 76(3A) | 902-903 | (3A) The Secretary of State may by further direction in writ | fork 2, 19 | `s 76(3A) the Secretary of State may give a further direction extending the period` |
| s 76(4) | 904 | (4) A company may apply to the court to set aside a directio | encoded | `s 76(4) the company may apply to the court to set the direction aside` |
| s 76(4A) | 905 | (4A) Any application under subsection (4) must be made withi | encoded | `s 76(4A) the application is made in time` |
| s 76(5) | 906-907 | (5) The court may set the direction aside or confirm it. | encoded | `s 76(5) the court may set the direction aside or confirm it`; `s 76(5) the court must specify the period within which the direction is to be complied with` |
| s 76(5A) | 908 | (5A) If a company applies to the court under subsection (4)  | encoded | `s 76(5A) the company is not required to comply with the direction while the proceedings are ongoing` |
| s 76(5B) | 909 | (5B) Where a direction is given under subsection (1), the re | encoded | `s 76(5B) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 76(6) | 910 | (6) If a company fails to comply with a direction under subs | encoded | `s 76(6) the company's duty to change its name as directed`; `s 76(6) the person commits an offence` |
| s 76(6)(a) | 911 | (a) the company, and | encoded | `s 76(6) the company's duty to change its name as directed`; `s 76(6) the person commits an offence` |
| s 76(6)(b) | 912-913 | (b) every officer of the company who is in default. | encoded | `s 76(6) the company's duty to change its name as directed`; `s 76(6) the person commits an offence` |
| s 76(7) | 914 | (7) A person guilty of an offence under this section is liab | encoded | `s 76(7) the penalty on summary conviction` |
| s 76A | 915 | Power to direct change of name used for criminal purposes | encoded | `s 76A(1) the Secretary of State may direct the company to change its name`; `s 76A(2) the direction meets the requirements of subsection (2)`; +11 more (see the rows of its subsections) |
| s 76A(1) | 916 | (1) The Secretary of State may direct a company to change it | fork 16 | `s 76A(1) the Secretary of State may direct the company to change its name` |
| s 76A(1)(a) | 917 | (a) the commission of an offence involving dishonesty or dec | fork 16 | `s 76A(1) the Secretary of State may direct the company to change its name` |
| s 76A(1)(b) | 918 | (b) the carrying out of conduct that, if carried out in any  | fork 16 | `s 76A(1) the Secretary of State may direct the company to change its name` |
| s 76A(2) | 919 | (2) The direction must be in writing and must specify the pe | encoded | `s 76A(2) the direction meets the requirements of subsection (2)` |
| s 76A(3) | 920 | (3) The period must be a period of at least 28 days beginnin | encoded | `s 76A(3) the period meets the requirement of subsection (3)` |
| s 76A(4) | 921-922 | (4) The Secretary of State may by further direction in writi | fork 2, 20 | `s 76A(4) the Secretary of State may give a further direction extending the period` |
| s 76A(5) | 923 | (5) A company may apply to the court to set aside a directio | encoded | `s 76A(5) the company may apply to the court to set the direction aside` |
| s 76A(6) | 924 | (6) Any application under subsection (5) must be made within | encoded | `s 76A(6) the application is made in time` |
| s 76A(7) | 925 | (7) On an application under subsection (5) the court may set | encoded | `s 76A(7) the court may set the direction aside or confirm it` |
| s 76A(8) | 926 | (8) If on an application under subsection (5) the direction  | encoded | `s 76A(8) the court must specify the period within which the direction is to be complied with` |
| s 76A(9) | 927 | (9) Where a direction is given under subsection (1), the reg | encoded | `s 76A(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 76A(10) | 928 | (10) If a company applies to the court under subsection (5)  | encoded | `s 76A(10) the company is not required to comply with the direction while the proceedings are ongoing` |
| s 76A(11) | 929 | (11) If a company fails to comply with a direction under sub | encoded | `s 76A(11) the company's duty to change its name as directed`; `s 76A(11) the person commits an offence` |
| s 76A(11)(a) | 930 | (a) the company, and | encoded | `s 76A(11) the company's duty to change its name as directed`; `s 76A(11) the person commits an offence` |
| s 76A(11)(b) | 931-932 | (b) every officer of the company who is in default. | encoded | `s 76A(11) the company's duty to change its name as directed`; `s 76A(11) the person commits an offence` |
| s 76A(12) | 933 | (12) A person guilty of an offence under this section is lia | encoded | `s 76A(12) the penalty on summary conviction` |
| heading@934 | 934 | Direction to change name wrongly registered | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 76B | 935 | Direction to change name wrongly registered | encoded | `s 76B(1) the Secretary of State may direct the company to change its name`; `s 76B(2) the direction meets the requirements of subsection (2)`; +11 more (see the rows of its subsections) |
| s 76B(1) | 936 | (1) The Secretary of State may direct a company to change it | fork 17 | `s 76B(1) the Secretary of State may direct the company to change its name` |
| s 76B(1)(a) | 937 | (a) it appears to the Secretary of State that the company’s  | fork 17 | `s 76B(1) the Secretary of State may direct the company to change its name` |
| s 76B(1)(b) | 938 | (b) the Secretary of State did not, at the time at which the | fork 17 | `s 76B(1) the Secretary of State may direct the company to change its name` |
| s 76B(2) | 939 | (2) The direction must be in writing and must specify the pe | encoded | `s 76B(2) the direction meets the requirements of subsection (2)` |
| s 76B(3) | 940 | (3) The period must be a period of at least 28 days beginnin | encoded | `s 76B(3) the period meets the requirement of subsection (3)` |
| s 76B(4) | 941-942 | (4) The Secretary of State may by further direction in writi | fork 2, 21 | `s 76B(4) the Secretary of State may give a further direction extending the period` |
| s 76B(5) | 943 | (5) A company may apply to the court to set aside a directio | encoded | `s 76B(5) the company may apply to the court to set the direction aside` |
| s 76B(6) | 944 | (6) Any application under subsection (5) must be made within | encoded | `s 76B(6) the application is made in time` |
| s 76B(7) | 945 | (7) On an application under subsection (5) the court may set | encoded | `s 76B(7) the court may set the direction aside or confirm it` |
| s 76B(8) | 946 | (8) If on an application under subsection (5) the direction  | encoded | `s 76B(8) the court must specify the period within which the direction is to be complied with` |
| s 76B(9) | 947 | (9) Where a direction is given under subsection (1), the reg | encoded | `s 76B(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 76B(10) | 948 | (10) If a company applies to the court under subsection (5)  | encoded | `s 76B(10) the company is not required to comply with the direction while the proceedings are ongoing` |
| s 76B(11) | 949 | (11) If a company fails to comply with a direction under sub | encoded | `s 76B(11) the company's duty to change its name as directed`; `s 76B(11) the person commits an offence` |
| s 76B(11)(a) | 950 | (a) the company, and | encoded | `s 76B(11) the company's duty to change its name as directed`; `s 76B(11) the person commits an offence` |
| s 76B(11)(b) | 951-952 | (b) every officer of the company who is in default. | encoded | `s 76B(11) the company's duty to change its name as directed`; `s 76B(11) the person commits an offence` |
| s 76B(12) | 953 | (12) A person guilty of an offence under this section is lia | encoded | `s 76B(12) the penalty on summary conviction` |
| heading@954 | 954 | Registrar’s powers to change names | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 76C | 955 | Registrar’s power to change name containing computer code | encoded | `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register`; `s 76C(2)(a) the registrar must give the company notice of the determination`; +3 more (see the rows of its subsections) |
| s 76C(1) | 956 | (1) Where, in the opinion of the registrar, a company’s regi | encoded | `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register` |
| s 76C(1)(a) | 957 | (a) determine a new name for the company, and | encoded | `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register` |
| s 76C(1)(b) | 958 | (b) remove from the register any reference to the company’s  | encoded | `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register` |
| s 76C(2) | 959 | (2) If the registrar determines a new name for a company und | encoded | `s 76C(2)(a) the registrar must give the company notice of the determination`; `s 76C(2)(b) the registrar must place a note of the determination in the register` |
| s 76C(2)(a) | 960 | (a) give the company notice of the determination, and | encoded | `s 76C(2)(a) the registrar must give the company notice of the determination` |
| s 76C(2)(b) | 961 | (b) place a note of the determination in the register. | encoded | `s 76C(2)(b) the registrar must place a note of the determination in the register` |
| s 76C(3) | 962 | (3) Where a company is given a direction under section 76B t | encoded | `s 76C(3)(a) the direction does not affect the registrar's power to act under subsection (1)`; `s 76C(3)(b) the direction lapses` |
| s 76C(3)(a) | 963 | (a) that does not affect the registrar’s power to act under  | encoded | `s 76C(3)(a) the direction does not affect the registrar's power to act under subsection (1)` |
| s 76C(3)(b) | 964 | (b) if the registrar does so, the direction lapses. | encoded | `s 76C(3)(b) the direction lapses` |
| s 76D | 965 | Registrar’s power to change name for failure to comply with  | encoded | `s 76D(2) the direction is one referred to in subsection (1)`; `s 76D(1) the registrar may determine a new name for the company`; +2 more (see the rows of its subsections) |
| s 76D(1) | 966 | (1) Where a company fails to comply with a direction to chan | encoded | `s 76D(1) the registrar may determine a new name for the company` |
| s 76D(2) | 967 | (2) The reference in subsection (1) to a direction to change | encoded | `s 76D(2) the direction is one referred to in subsection (1)` |
| s 76D(3) | 968 | (3) If the registrar determines a new name for a company und | encoded | `s 76D(3)(a) the registrar must give the company notice of the determination`; `s 76D(3)(b) the registrar must place a note of the determination in the register` |
| s 76D(3)(a) | 969 | (a) give the company notice of the determination, and | encoded | `s 76D(3)(a) the registrar must give the company notice of the determination` |
| s 76D(3)(b) | 970 | (b) place a note of the determination in the register. | encoded | `s 76D(3)(b) the registrar must place a note of the determination in the register` |
| heading@971 | 971 | CHAPTER 4A — Exceptions | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 76E | 972 | Exceptions based on national security etc | encoded | `s 76E(2)(a) the conduct is crime`; `s 76E(2)(b) the crime is serious`; +1 more (see the rows of its subsections) |
| s 76E(1) | 973 | (1) Nothing in this Part prevents the registration of a comp | encoded | `s 76E(1) Part 5 does not prevent the registration of the company by the name` |
| s 76E(1)(a) | 974 | (a) in the interests of national security, or | encoded | `s 76E(1) Part 5 does not prevent the registration of the company by the name` |
| s 76E(1)(b) | 975 | (b) for the purposes of preventing or detecting serious crim | encoded | `s 76E(1) Part 5 does not prevent the registration of the company by the name` |
| s 76E(2) | 976 | (2) For the purposes of subsection (1)(b)— | encoded | `s 76E(2)(a) the conduct is crime`; `s 76E(2)(b) the crime is serious` |
| s 76E(2)(a) | 977 | (a) “crime” means conduct which— | encoded | `s 76E(2)(a) the conduct is crime` |
| s 76E(2)(a)(i) | 978 | (i) constitutes a criminal offence, or | encoded | `s 76E(2)(a) the conduct is crime` |
| s 76E(2)(a)(ii) | 979 | (ii) is, or corresponds to, any conduct which, if it all too | encoded | `s 76E(2)(a) the conduct is crime` |
| s 76E(2)(b) | 980 | (b) crime is “serious” if— | encoded | `s 76E(2)(b) the crime is serious` |
| s 76E(2)(b)(i) | 981 | (i) the offence which is or would be constituted by the cond | encoded | `s 76E(2)(b) the crime is serious` |
| s 76E(2)(b)(ii) | 982 | (ii) the conduct involves the use of violence, results in su | encoded | `s 76E(2)(b) the crime is serious` |
| heading@983 | 983 | Chapter 5 — Change of name | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 77 | 984 | Change of name | encoded | `s 77(1) the company may change its name in that way`; `s 77(2) the name of the company may also be changed in that way` (see the rows of its subsections) |
| s 77(1) | 985 | (1) A company may change its name— | encoded | `s 77(1) the company may change its name in that way` |
| s 77(1)(a) | 986 | (a) by special resolution (see section 78), or | encoded | `s 77(1) the company may change its name in that way` |
| s 77(1)(b) | 987 | (b) by other means provided for by the company's articles (s | encoded | `s 77(1) the company may change its name in that way` |
| s 77(2) | 988 | (2) The name of a company may also be changed— | encoded | `s 77(2) the name of the company may also be changed in that way` |
| s 77(2)(a) | 989 | (a) by resolution of the directors acting under section 64 ( | encoded | `s 77(2) the name of the company may also be changed in that way` |
| s 77(2)(b) | 990 | (b) on the determination of a new name by a company names ad | encoded | `s 77(2) the name of the company may also be changed in that way` |
| s 77(2)(c) | 991 | (c) on the determination of a new name by the court under se | encoded | `s 77(2) the name of the company may also be changed in that way` |
| s 77(2)(d) | 992 | (d) under section 1033 (company's name on restoration to the | encoded | `s 77(2) the name of the company may also be changed in that way` |
| s 77(2)(e) | 993 | (e) by resolution of the directors acting under section 45(3 | encoded | `s 77(2) the name of the company may also be changed in that way` |
| s 78 | 994 | Change of name by special resolution | encoded | `s 78(1) the company must give notice to the registrar`; `s 78(2)(a) the notice must specify that the change is conditional`; +4 more (see the rows of its subsections) |
| s 78(1) | 995-996 | (1) Where a change of name has been agreed to by a company b | encoded | `s 78(1) the company must give notice to the registrar` |
| s 78(2) | 997 | (2) Where a change of name by special resolution is conditio | encoded | `s 78(2)(a) the notice must specify that the change is conditional`; `s 78(2)(b) the notice must state whether the event has occurred` |
| s 78(2)(a) | 998 | (a) specify that the change is conditional, and | encoded | `s 78(2)(a) the notice must specify that the change is conditional` |
| s 78(2)(b) | 999 | (b) state whether the event has occurred. | encoded | `s 78(2)(b) the notice must state whether the event has occurred` |
| s 78(3) | 1000 | (3) If the notice states that the event has not occurred— | encoded | `s 78(3)(a) the registrar is not required to act under section 80 until further notice`; `s 78(3)(b) the company must give notice to the registrar stating that the event has occurred`; `s 78(3)(c) the registrar may rely on the statement as sufficient evidence of the matters stated in it` |
| s 78(3)(a) | 1001 | (a) the registrar is not required to act under section 80 (r | encoded | `s 78(3)(a) the registrar is not required to act under section 80 until further notice` |
| s 78(3)(b) | 1002 | (b) when the event occurs, the company must give notice to t | encoded | `s 78(3)(b) the company must give notice to the registrar stating that the event has occurred` |
| s 78(3)(c) | 1003 | (c) the registrar may rely on the statement as sufficient ev | encoded | `s 78(3)(c) the registrar may rely on the statement as sufficient evidence of the matters stated in it` |
| s 79 | 1004 | Change of name by means provided for in company's articles | encoded | `s 79(1)(a) the company must give notice to the registrar`; `s 79(1)(b) the notice must be accompanied by a statement that the change of name has been made by means provided for by the company's articles`; +1 more (see the rows of its subsections) |
| s 79(1) | 1005 | (1) Where a change of a company's name has been made by othe | encoded | `s 79(1)(a) the company must give notice to the registrar`; `s 79(1)(b) the notice must be accompanied by a statement that the change of name has been made by means provided for by the company's articles` |
| s 79(1)(a) | 1006 | (a) the company must give notice to the registrar, and | encoded | `s 79(1)(a) the company must give notice to the registrar` |
| s 79(1)(b) | 1007 | (b) the notice must be accompanied by a statement that the c | encoded | `s 79(1)(b) the notice must be accompanied by a statement that the change of name has been made by means provided for by the company's articles` |
| s 79(2) | 1008 | (2) The registrar may rely on the statement as sufficient ev | encoded | `s 79(2) the registrar may rely on the statement as sufficient evidence of the matters stated in it` |
| s 80 | 1009 | Change of name: registration and issue of new certificate of | encoded | `s 80(1) this section applies`; `s 80(2) the registrar must enter the new name on the register in place of the former name`; +1 more (see the rows of its subsections) |
| s 80(1) | 1010 | (1) This section applies where— | encoded | `s 80(1) this section applies` |
| s 80(1)(a) | 1011 | (a) the registrar receives notice of a change of a company’s | encoded | `s 80(1) this section applies` |
| s 80(1)(a)(i) | 1012 | (i) that the new name complies with the requirements of this | encoded | `s 80(1) this section applies` |
| s 80(1)(a)(ii) | 1013 | (ii) that the requirements of the Companies Acts, and any re | encoded | `s 80(1) this section applies` |
| s 80(1)(b) | 1014 | (b) the registrar determines a new name for a company under  | encoded | `s 80(1) this section applies` |
| s 80(2) | 1015 | (2) The registrar must enter the new name on the register in | encoded | `s 80(2) the registrar must enter the new name on the register in place of the former name` |
| s 80(3) | 1016 | (3) On the registration of the new name, the registrar must  | encoded | `s 80(3) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` |
| s 81 | 1017 | Change of name: effect | encoded | `s 81(1) the change of name has effect on the day`; `s 81(2) the change of name affects the right, the obligation or the proceedings`; +1 more (see the rows of its subsections) |
| s 81(1) | 1018 | (1) A change of a company's name has effect from the date on | encoded | `s 81(1) the change of name has effect on the day` |
| s 81(2) | 1019 | (2) The change does not affect any rights or obligations of  | encoded | `s 81(2) the change of name affects the right, the obligation or the proceedings` |
| s 81(3) | 1020 | (3) Any legal proceedings that might have been continued or  | encoded | `s 81(3) the proceedings may be continued or commenced against the company by its new name` |
| heading@1021 | 1021 | Chapter 6 — Trading disclosures | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 82 | 1022 | Requirement to disclose company name etc | encoded | `s 82(4) the information, location, description of document or communication is specified` (see the rows of its subsections) |
| s 82(1) | 1023 | (1) The Secretary of State may by regulations make provision | inert (reason 2) | machinery: power to make regulations (trading disclosures) |
| s 82(1)(a) | 1024 | (a) to display specified information in specified locations, | inert (reason 2) | machinery: power to make regulations (trading disclosures) |
| s 82(1)(b) | 1025 | (b) to state specified information in specified descriptions | inert (reason 2) | machinery: power to make regulations (trading disclosures) |
| s 82(1)(c) | 1026 | (c) to provide specified information on request to those the | inert (reason 2) | machinery: power to make regulations (trading disclosures) |
| s 82(2) | 1027 | (2) The regulations— | inert (reason 2) | machinery: power to make regulations (content of the disclosure regulations) |
| s 82(2)(a) | 1028 | (a) must in every case require disclosure of the name of the | inert (reason 2) | machinery: power to make regulations (content of the disclosure regulations) |
| s 82(2)(b) | 1029 | (b) may make provision as to the manner in which any specifi | inert (reason 2) | machinery: power to make regulations (content of the disclosure regulations) |
| s 82(3) | 1030 | (3) The regulations may provide that, for the purposes of an | inert (reason 2) | machinery: power to make regulations (abbreviations) |
| s 82(4) | 1031 | (4) In this section “specified” means specified in the regul | encoded | `s 82(4) the information, location, description of document or communication is specified` |
| s 82(5) | 1032 | (5) Regulations under this section are subject to affirmativ | inert (reason 2) | machinery: regulations subject to affirmative resolution procedure |
| s 83 | 1033 | Civil consequences of failure to make required disclosure | encoded | `s 83(1) this section applies to the proceedings`; `s 83(2) the proceedings shall be dismissed`; +1 more (see the rows of its subsections) |
| s 83(1) | 1034 | (1) This section applies to any legal proceedings brought by | encoded | `s 83(1) this section applies to the proceedings` |
| s 83(2) | 1035 | (2) The proceedings shall be dismissed if the defendant (in  | encoded | `s 83(2) the proceedings shall be dismissed` |
| s 83(2)(a) | 1036 | (a) that he has a claim against the claimant (pursuer) arisi | encoded | `s 83(2) the proceedings shall be dismissed` |
| s 83(2)(b) | 1037-1038 | (b) that he has suffered some financial loss in connection w | encoded | `s 83(2) the proceedings shall be dismissed` |
| s 83(3) | 1039 | (3) This section does not affect the right of any person to  | encoded | `s 83(3) the section affects the person's right to enforce his rights against another person` |
| s 84 | 1040 | Criminal consequences of failure to make required disclosure | encoded | `s 84(3) the requirement is specified` (see the rows of its subsections) |
| s 84(1) | 1041 | (1) Regulations under section 82 may provide— | inert (reason 2) | machinery: power to make regulations (offences and penalty for breach of the disclosure regulations) |
| s 84(1)(a) | 1042 | (a) that where a company fails, without reasonable excuse, t | inert (reason 2) | machinery: power to make regulations (offences and penalty for breach of the disclosure regulations) |
| s 84(1)(a)(i) | 1043 | (i) the company, and | inert (reason 2) | machinery: power to make regulations (offences and penalty for breach of the disclosure regulations) |
| s 84(1)(a)(ii) | 1044 | (ii) every officer of the company who is in default; | inert (reason 2) | machinery: power to make regulations (offences and penalty for breach of the disclosure regulations) |
| s 84(1)(b) | 1045 | (b) that a person guilty of such an offence is liable on sum | inert (reason 2) | machinery: power to make regulations (offences and penalty for breach of the disclosure regulations) |
| s 84(2) | 1046 | (2) The regulations may provide that, for the purposes of an | inert (reason 2) | machinery: power to make regulations (shadow director treated as officer) |
| s 84(3) | 1047 | (3) In subsection (1)(a) “specified” means specified in the  | encoded | `s 84(3) the requirement is specified` |
| s 85 | 1048 | Minor variations in form of name to be left out of account | encoded | `s 85(1) no account is taken of the difference`; `s 85(2) subsection (1) affects the operation of the regulations` (see the rows of its subsections) |
| s 85(1) | 1049 | (1) For the purposes of this Chapter, in considering a compa | encoded | `s 85(1) no account is taken of the difference` |
| s 85(1)(a) | 1050 | (a) whether upper or lower case characters (or a combination | encoded | `s 85(1) no account is taken of the difference` |
| s 85(1)(b) | 1051 | (b) whether diacritical marks or punctuation are present or  | encoded | `s 85(1) no account is taken of the difference` |
| s 85(1)(c) | 1052-1053 | (c) whether the name is in the same format or style as is sp | encoded | `s 85(1) no account is taken of the difference` |
| s 85(2) | 1054 | (2) This does not affect the operation of regulations under  | encoded | `s 85(2) subsection (1) affects the operation of the regulations` |
| heading@1055 | 1055 | Part 6 — A company's registered office and email address | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| heading@1056 | 1056 | General | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 86 | 1057 | Duty to ensure registered office at appropriate address | encoded | `s 86 the company has its registered office at the address`; `s 86(2) the address is an appropriate address`; +3 more (see the rows of its subsections) |
| s 86(1) | 1058 | (1) A company must ensure that its registered office is at a | encoded | `s 86(1) the company must ensure that its registered office is at an appropriate address` |
| s 86(2) | 1059 | (2) An address is an “appropriate address” if, in the ordina | encoded | `s 86(2) the address is an appropriate address` |
| s 86(2)(a) | 1060 | (a) a document addressed to the company, and delivered there | encoded | `s 86(2) the address is an appropriate address` |
| s 86(2)(b) | 1061 | (b) the delivery of documents there is capable of being reco | encoded | `s 86(2) the address is an appropriate address` |
| s 86(3) | 1062 | (3) If a company fails, without reasonable excuse, to comply | fork 7 | `s 86(3) the person commits an offence` |
| s 86(3)(a) | 1063 | (a) the company, and | fork 7 | `s 86(3) the person commits an offence` |
| s 86(3)(b) | 1064 | (b) every officer of the company who is in default. | fork 7 | `s 86(3) the person commits an offence` |
| s 86(4) | 1065 | (4) A person guilty of an offence under this section is liab | encoded | `s 86(4) the penalty on summary conviction` |
| s 86(4)(a) | 1066 | (a) in England and Wales, to a fine; | encoded | `s 86(4) the penalty on summary conviction` |
| s 86(4)(b) | 1067 | (b) in Scotland or Northern Ireland, to a fine not exceeding | encoded | `s 86(4) the penalty on summary conviction` |
| s 86(5) | 1068 | (5) Subsection (1) does not apply in relation to a company d | encoded | `s 86(1) the company must ensure that its registered office is at an appropriate address` |
| s 87 | 1069 | Change of address of registered office | encoded | `s 87(1) the company may change the address of its registered office`; `s 87(1A) the notice must include a statement that the new address is an appropriate address within the meaning given by section 86(2)`; +4 more (see the rows of its subsections) |
| s 87(1) | 1070 | (1) A company may change the address of its registered offic | encoded | `s 87(1) the company may change the address of its registered office` |
| s 87(1A) | 1071 | (1A) The notice must include a statement that the new addres | encoded | `s 87(1A) the notice must include a statement that the new address is an appropriate address within the meaning given by section 86(2)` |
| s 87(2) | 1072 | (2) The change takes effect upon the notice being registered | encoded | `s 87(2) the change takes effect on the day`; `s 87(2) a person may validly serve a document on the company at the address previously registered on the day` |
| s 87(3) | 1073 | (3) For the purposes of any duty of a company— | encoded | `s 87(3) the company may act on the change as from that date` |
| s 87(3)(a) | 1074 | (a) to keep available for inspection at its registered offic | encoded | `s 87(3) the company may act on the change as from that date` |
| s 87(3)(b) | 1075-1076 | (b) to mention the address of its registered office in any d | encoded | `s 87(3) the company may act on the change as from that date` |
| s 87(4) | 1077 | (4) Where a company unavoidably ceases to perform at its reg | encoded | `s 87(4) the company is protected from being treated as having failed to comply with the duty` |
| s 87(4)(a) | 1078 | (a) resumes performance of that duty at other premises as so | encoded | `s 87(4) the company is protected from being treated as having failed to comply with the duty` |
| s 87(4)(b) | 1079-1080 | (b) gives notice accordingly to the registrar of a change in | encoded | `s 87(4) the company is protected from being treated as having failed to comply with the duty` |
| heading@1081 | 1081 | Welsh companies | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 88 | 1082 | Welsh companies | encoded | `s 88(1) the company is a Welsh company`; `s 88(2) the company may by special resolution require the register to state that its registered office is to be situated in Wales`; +4 more (see the rows of its subsections) |
| s 88(1) | 1083 | (1) In the Companies Acts a “Welsh company” means a company  | encoded | `s 88(1) the company is a Welsh company` |
| s 88(2) | 1084 | (2) A company— | encoded | `s 88(2) the company may by special resolution require the register to state that its registered office is to be situated in Wales` |
| s 88(2)(a) | 1085 | (a) whose registered office is in Wales, and | encoded | `s 88(2) the company may by special resolution require the register to state that its registered office is to be situated in Wales` |
| s 88(2)(b) | 1086-1087 | (b) as to which it is stated in the register that its regist | encoded | `s 88(2) the company may by special resolution require the register to state that its registered office is to be situated in Wales` |
| s 88(3) | 1088 | (3) A company— | encoded | `s 88(3) the company may by special resolution require the register to state that its registered office is to be situated in England and Wales` |
| s 88(3)(a) | 1089 | (a) whose registered office is in Wales, and | encoded | `s 88(3) the company may by special resolution require the register to state that its registered office is to be situated in England and Wales` |
| s 88(3)(b) | 1090-1091 | (b) as to which it is stated in the register that its regist | encoded | `s 88(3) the company may by special resolution require the register to state that its registered office is to be situated in England and Wales` |
| s 88(4) | 1092 | (4) Where a company passes a resolution under this section i | encoded | `s 88(4) the company must give notice to the registrar`; `s 88(4)(a) the registrar must amend the register accordingly`; `s 88(4)(b) the registrar must issue a new certificate of incorporation altered to meet the circumstances of the case` |
| s 88(4)(a) | 1093 | (a) amend the register accordingly, and | encoded | `s 88(4)(a) the registrar must amend the register accordingly` |
| s 88(4)(b) | 1094 | (b) issue a new certificate of incorporation altered to meet | encoded | `s 88(4)(b) the registrar must issue a new certificate of incorporation altered to meet the circumstances of the case` |
| heading@1095 | 1095 | Registered email address | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 88A | 1096 | Duty to maintain a registered email address | encoded | `s 88A(2) the email address is an appropriate email address`; `s 88A(1) the company must ensure that its registered email address is an appropriate email address`; +2 more (see the rows of its subsections) |
| s 88A(1) | 1097 | (1) A company must ensure that its registered email address  | encoded | `s 88A(1) the company must ensure that its registered email address is an appropriate email address` |
| s 88A(2) | 1098 | (2) An email address is an “appropriate email address” if, i | encoded | `s 88A(2) the email address is an appropriate email address` |
| s 88A(3) | 1099 | (3) If a company fails, without reasonable excuse, to comply | fork 7 | `s 88A(3) the person commits an offence` |
| s 88A(3)(a) | 1100 | (a) the company, and | fork 7 | `s 88A(3) the person commits an offence` |
| s 88A(3)(b) | 1101 | (b) every officer of the company who is in default. | fork 7 | `s 88A(3) the person commits an offence` |
| s 88A(4) | 1102 | (4) A person guilty of an offence under this section is liab | encoded | `s 88A(4) the penalty on summary conviction` |
| s 88A(4)(a) | 1103 | (a) in England and Wales, to a fine; | encoded | `s 88A(4) the penalty on summary conviction` |
| s 88A(4)(b) | 1104 | (b) in Scotland or Northern Ireland, to a fine not exceeding | encoded | `s 88A(4) the penalty on summary conviction` |
| s 88B | 1105 | Change of registered email address | encoded | `s 88B(1) the company may change its registered email address`; `s 88B(2) the notice must include a statement that the new address is an appropriate email address within the meaning given by section 88A(2)`; +1 more (see the rows of its subsections) |
| s 88B(1) | 1106 | (1) A company may change its registered email address by giv | encoded | `s 88B(1) the company may change its registered email address` |
| s 88B(2) | 1107 | (2) The notice must include a statement that the new address | encoded | `s 88B(2) the notice must include a statement that the new address is an appropriate email address within the meaning given by section 88A(2)` |
| s 88B(3) | 1108 | (3) The change takes effect upon the notice being registered | encoded | `s 88B(3) the change takes effect on the day` |
| heading@1109 | 1109 | Part 7 — Re-registration as a means of altering a company's  | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| heading@1110 | 1110 | Introductory | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 89 | 1111 | Alteration of status by re-registration | encoded | `s 89 the company may by re-registration under Part 7 alter its status in that way` (see the rows of its subsections) |
| s 89 text | 1112 | A company may by re-registration under this Part alter its s | encoded | `s 89 the company may by re-registration under Part 7 alter its status in that way` |
| s 89(a) | 1113 | (a) from a private company to a public company (see sections | encoded | `s 89 the company may by re-registration under Part 7 alter its status in that way` |
| s 89(b) | 1114 | (b) from a public company to a private company (see sections | encoded | `s 89 the company may by re-registration under Part 7 alter its status in that way` |
| s 89(c) | 1115 | (c) from a private limited company to an unlimited company ( | encoded | `s 89 the company may by re-registration under Part 7 alter its status in that way` |
| s 89(d) | 1116 | (d) from an unlimited private company to a limited company ( | encoded | `s 89 the company may by re-registration under Part 7 alter its status in that way` |
| s 89(e) | 1117 | (e) from a public company to an unlimited private company (s | encoded | `s 89 the company may by re-registration under Part 7 alter its status in that way` |
| heading@1118 | 1118 | Private company becoming public | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 90 | 1119 | Re-registration of private company as public | encoded | `s 90(1) all of the answers hold`; `s 90(2) the conditions are met`; +4 more (see the rows of its subsections) |
| s 90(1) | 1120 | (1) A private company (whether limited or unlimited) may be  | encoded | `s 90(1) all of the answers hold`; `s 90(1) the private company may be re-registered as a public company limited by shares` |
| s 90(1)(a) | 1121 | (a) a special resolution that it should be so re-registered  | encoded | `s 90(1) all of the answers hold`; `s 90(1) the private company may be re-registered as a public company limited by shares` |
| s 90(1)(b) | 1122 | (b) the conditions specified below are met, and | encoded | `s 90(1) all of the answers hold`; `s 90(1) the private company may be re-registered as a public company limited by shares` |
| s 90(1)(c) | 1123 | (c) an application for re-registration is delivered to the r | encoded | `s 90(1) all of the answers hold`; `s 90(1) the private company may be re-registered as a public company limited by shares` |
| s 90(1)(c)(i) | 1124 | (i) the other documents required by that section, and | encoded | `s 90(1) all of the answers hold`; `s 90(1) the private company may be re-registered as a public company limited by shares` |
| s 90(1)(c)(ii) | 1125 | (ii) a statement of compliance. | encoded | `s 90(1) all of the answers hold`; `s 90(1) the private company may be re-registered as a public company limited by shares` |
| s 90(2) | 1126 | (2) The conditions are— | encoded | `s 90(2) the conditions are met` |
| s 90(2)(a) | 1127 | (a) that the company has a share capital; | encoded | `s 90(2) the conditions are met` |
| s 90(2)(b) | 1128 | (b) that the requirements of section 91 are met as regards i | encoded | `s 90(2) the conditions are met` |
| s 90(2)(c) | 1129 | (c) that the requirements of section 92 are met as regards i | encoded | `s 90(2) the conditions are met` |
| s 90(2)(d) | 1130 | (d) if section 93 applies (recent allotment of shares for no | encoded | `s 90(2) the conditions are met` |
| s 90(2)(e) | 1131 | (e) that the company has not previously been re-registered a | encoded | `s 90(2) the conditions are met` |
| s 90(3) | 1132 | (3) The company must make such changes— | encoded | `s 90(3)(a) the company must make such changes in its name as are necessary in connection with its becoming a public company`; `s 90(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming a public company` |
| s 90(3)(a) | 1133 | (a) in its name, and | encoded | `s 90(3)(a) the company must make such changes in its name as are necessary in connection with its becoming a public company` |
| s 90(3)(b) | 1134-1135 | (b) in its articles, | encoded | `s 90(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming a public company` |
| s 90(4) | 1136 | (4) If the company is unlimited it must also make such chang | encoded | `s 90(4) the company must also make such changes in its articles as are necessary in connection with its becoming a company limited by shares` |
| s 91 | 1137 | Requirements as to share capital | encoded | `s 91(1)(a) the nominal value of the allotted share capital is not less than the authorised minimum`; `s 91(1)(b) the allotment is paid up as the paragraph requires`; +8 more (see the rows of its subsections) |
| s 91(1) | 1138 | (1) The following requirements must be met at the time the s | encoded | `s 91(1)(a) the nominal value of the allotted share capital is not less than the authorised minimum`; `s 91(1)(b) the allotment is paid up as the paragraph requires`; `s 91(1)(c) the allotment meets the paragraph`; `s 91(1)(d) the allotment meets the paragraph`; +1 more |
| s 91(1)(a) | 1139 | (a) the nominal value of the company's allotted share capita | encoded | `s 91(1)(a) the nominal value of the allotted share capital is not less than the authorised minimum` |
| s 91(1)(b) | 1140 | (b) each of the company's allotted shares must be paid up at | encoded | `s 91(1)(b) the allotment is paid up as the paragraph requires` |
| s 91(1)(c) | 1141 | (c) if any shares in the company or any premium on them have | fork 4 | `s 91(1)(c) the allotment meets the paragraph` |
| s 91(1)(d) | 1142 | (d) if shares have been allotted as fully or partly paid up  | fork 4 | `s 91(1)(d) the allotment meets the paragraph` |
| s 91(1)(d)(i) | 1143 | (i) the undertaking must have been performed or otherwise di | fork 4 | `s 91(1)(d) the allotment meets the paragraph` |
| s 91(1)(d)(ii) | 1144 | (ii) there must be a contract between the company and some p | fork 4 | `s 91(1)(d) the allotment meets the paragraph` |
| s 91(2) | 1145 | (2) For the purpose of determining whether the requirements  | encoded | `s 91(2)(a) the allotment may be disregarded`; `s 91(2)(b) the allotment may be disregarded` |
| s 91(2)(a) | 1146 | (a) shares allotted— | encoded | `s 91(2)(a) the allotment may be disregarded` |
| s 91(2)(a)(i) | 1147 | (i) before 22nd June 1982 in the case of a company then regi | encoded | `s 91(2)(a) the allotment may be disregarded` |
| s 91(2)(a)(ii) | 1148 | (ii) before 31st December 1984 in the case of a company then | encoded | `s 91(2)(a) the allotment may be disregarded` |
| s 91(2)(b) | 1149 | (b) shares allotted in pursuance of an employees' share sche | encoded | `s 91(2)(b) the allotment may be disregarded` |
| s 91(3) | 1150-1151 | (3) No more than one-tenth of the nominal value of the compa | encoded | `s 91(3) the disregard under subsection (2)(a) is within the limit` |
| s 91(4) | 1152 | (4) Shares disregarded under subsection (2) are treated as n | encoded | `s 91(4) the nominal value of the allotted share capital for paragraph (a)` |
| s 91(5) | 1153 | (5) A company must not be re-registered as a public company  | encoded | `s 91(5) the company may be re-registered as a public company` |
| s 91(5)(a) | 1154 | (a) the company has resolved to reduce its share capital, | encoded | `s 91(5) the company may be re-registered as a public company` |
| s 91(5)(b) | 1155 | (b) the reduction— | encoded | `s 91(5) the company may be re-registered as a public company` |
| s 91(5)(b)(i) | 1156 | (i) is made under section 626 (reduction in connection with  | encoded | `s 91(5) the company may be re-registered as a public company` |
| s 91(5)(b)(ii) | 1157 | (ii) is supported by a solvency statement in accordance with | encoded | `s 91(5) the company may be re-registered as a public company` |
| s 91(5)(b)(iii) | 1158 | (iii) has been confirmed by an order of the court under sect | encoded | `s 91(5) the company may be re-registered as a public company` |
| s 91(5)(c) | 1159 | (c) the effect of the reduction is, or will be, that the nom | encoded | `s 91(5) the company may be re-registered as a public company` |
| s 92 | 1160 | Requirements as to net assets | encoded | `s 92(1)(a) the balance sheet is prepared as at a date not more than seven months before the application is delivered`; `s 92(5) a qualification is material`; +8 more (see the rows of its subsections) |
| s 92(1) | 1161 | (1) A company applying to re-register as a public company mu | encoded | `s 92(1)(a) the balance sheet is prepared as at a date not more than seven months before the application is delivered`; `s 92(1)(b) the company has obtained an unqualified report by its auditor on the balance sheet`; `s 92(1)(c) the aggregate of the company's called-up share capital and undistributable reserves`; `s 92(1)(c) the company has obtained the auditor's written statement` |
| s 92(1)(a) | 1162 | (a) a balance sheet prepared as at a date not more than seve | fork 3 | `s 92(1)(a) the balance sheet is prepared as at a date not more than seven months before the application is delivered` |
| s 92(1)(b) | 1163 | (b) an unqualified report by the company's auditor on that b | encoded | `s 92(1)(b) the company has obtained an unqualified report by its auditor on the balance sheet` |
| s 92(1)(c) | 1164 | (c) a written statement by the company's auditor that in his | encoded | `s 92(1)(c) the aggregate of the company's called-up share capital and undistributable reserves`; `s 92(1)(c) the company has obtained the auditor's written statement` |
| s 92(2) | 1165 | (2) Between the balance sheet date and the date on which the | encoded | `s 92(2) there is no change in the company's financial position of the kind the subsection excludes` |
| s 92(3) | 1166 | (3) In subsection (1)(b) an “unqualified report” means— | encoded | `s 92(3) the report is an unqualified report` |
| s 92(3)(a) | 1167 | (a) if the balance sheet was prepared for a financial year o | encoded | `s 92(3) the report is an unqualified report` |
| s 92(3)(b) | 1168 | (b) if the balance sheet was not prepared for a financial ye | encoded | `s 92(3) the report is an unqualified report` |
| s 92(4) | 1169 | (4) For the purposes of an auditor's report on a balance she | encoded | `s 92(4) the provisions of this Act apply to the auditor's report with such modifications as are necessary` |
| s 92(5) | 1170 | (5) For the purposes of subsection (3) a qualification is ma | encoded | `s 92(5) a qualification is material` |
| s 92(6) | 1171 | (6) In this Part “net assets” and “undistributable reserves” | encoded | `s 92(6) the amount of the company's net assets or undistributable reserves` |
| s 93 | 1172 | Recent allotment of shares for non-cash consideration | encoded | `s 93(1) section 93 applies (recent allotment of shares for non-cash consideration)`; `s 93(7)(b) the thing is an arrangement`; +7 more (see the rows of its subsections) |
| s 93(1) | 1173 | (1) This section applies where— | encoded | `s 93(1) section 93 applies (recent allotment of shares for non-cash consideration)` |
| s 93(1)(a) | 1174 | (a) shares are allotted by the company in the period between | encoded | `s 93(1) section 93 applies (recent allotment of shares for non-cash consideration)` |
| s 93(1)(b) | 1175 | (b) the shares are allotted as fully or partly paid up as to | encoded | `s 93(1) section 93 applies (recent allotment of shares for non-cash consideration)` |
| s 93(2) | 1176 | (2) The registrar shall not entertain an application by the  | fork 5 | `s 93(2) the registrar may entertain the application for re-registration` |
| s 93(2)(a) | 1177 | (a) the requirements of section 593(1)(a) and (b) have been  | fork 5 | `s 93(2) the registrar may entertain the application for re-registration` |
| s 93(2)(b) | 1178 | (b) the allotment is in connection with— | fork 5 | `s 93(2) the registrar may entertain the application for re-registration` |
| s 93(2)(b)(i) | 1179 | (i) a share exchange (see subsections (3) to (5) below), or | fork 5 | `s 93(2) the registrar may entertain the application for re-registration` |
| s 93(2)(b)(ii) | 1180 | (ii) a proposed merger with another company (see subsection  | fork 5 | `s 93(2) the registrar may entertain the application for re-registration` |
| s 93(3) | 1181 | (3) An allotment is in connection with a share exchange if— | encoded | `s 93(3) the allotment is in connection with a share exchange` |
| s 93(3)(a) | 1182 | (a) the shares are allotted in connection with an arrangemen | encoded | `s 93(3) the allotment is in connection with a share exchange` |
| s 93(3)(a)(i) | 1183 | (i) the transfer to the company allotting the shares of shar | encoded | `s 93(3) the allotment is in connection with a share exchange` |
| s 93(3)(a)(ii) | 1184 | (ii) the cancellation of shares (or shares of a particular c | encoded | `s 93(3) the allotment is in connection with a share exchange` |
| s 93(3)(b) | 1185 | (b) the allotment is open to all the holders of the shares o | encoded | `s 93(3) the allotment is in connection with a share exchange` |
| s 93(4) | 1186 | (4) In determining whether a person is a holder of shares fo | encoded | `s 93(4) the shares are disregarded in determining whether a person is a holder of shares` |
| s 93(4)(a) | 1187 | (a) shares held by, or by a nominee of, the company allottin | encoded | `s 93(4) the shares are disregarded in determining whether a person is a holder of shares` |
| s 93(4)(b) | 1188 | (b) shares held by, or by a nominee of— | encoded | `s 93(4) the shares are disregarded in determining whether a person is a holder of shares` |
| s 93(4)(b)(i) | 1189 | (i) the holding company of the company allotting the shares, | encoded | `s 93(4) the shares are disregarded in determining whether a person is a holder of shares` |
| s 93(4)(b)(ii) | 1190 | (ii) a subsidiary of the company allotting the shares, or | encoded | `s 93(4) the shares are disregarded in determining whether a person is a holder of shares` |
| s 93(4)(b)(iii) | 1191 | (iii) a subsidiary of the holding company of the company all | encoded | `s 93(4) the shares are disregarded in determining whether a person is a holder of shares` |
| s 93(5) | 1192 | (5) It is immaterial, for the purposes of deciding whether a | encoded | `s 93(5) it matters whether the arrangement involves an issue of shares in the other company` |
| s 93(6) | 1193 | (6) There is a proposed merger with another company if one o | encoded | `s 93(6) there is a proposed merger with another company`; `s 93(6) the body is another company` |
| term "Another company" @1194 | 1194 | “Another company” includes any body corporate. | encoded | `s 93(6) the body is another company` |
| s 93(7) | 1195 | (7) For the purposes of this section— | encoded | `s 93(7)(b) the thing is an arrangement`; `s 93(7)(a) the amount counts as consideration for the allotment` |
| s 93(7)(a) | 1196 | (a) the consideration for an allotment does not include any  | encoded | `s 93(7)(a) the amount counts as consideration for the allotment` |
| s 93(7)(b) | 1197 | (b) “arrangement” means any agreement, scheme or arrangement | encoded | `s 93(7)(b) the thing is an arrangement` |
| s 93(7)(b)(i) | 1198 | (i) Part 26 or 26A of this Act (arrangements and reconstruct | encoded | `s 93(7)(b) the thing is an arrangement` |
| s 93(7)(b)(ii) | 1199 | (ii) section 110 of the Insolvency Act 1986 (c. 45) or Artic | encoded | `s 93(7)(b) the thing is an arrangement` |
| s 94 | 1200 | Application and accompanying documents | encoded | `s 94(1) the application contains what the subsection requires`; `s 94(2) the application is accompanied by what the subsection requires`; +2 more (see the rows of its subsections) |
| s 94(1) | 1201 | (1) An application for re-registration as a public company m | encoded | `s 94(1) the application contains what the subsection requires` |
| s 94(1)(a) | 1202 | (a) a statement of the company's proposed name on re-registr | encoded | `s 94(1) the application contains what the subsection requires` |
| s 94(1)(b) | 1203 | (b) in the case of a company without a secretary, a statemen | encoded | `s 94(1) the application contains what the subsection requires` |
| s 94(2) | 1204 | (2) The application must be accompanied by— | encoded | `s 94(2) the application is accompanied by what the subsection requires` |
| s 94(2)(a) | 1205 | (a) a copy of the special resolution that the company should | encoded | `s 94(2) the application is accompanied by what the subsection requires` |
| s 94(2)(b) | 1206 | (b) a copy of the company's articles as proposed to be amend | encoded | `s 94(2) the application is accompanied by what the subsection requires` |
| s 94(2)(c) | 1207 | (c) a copy of the balance sheet and other documents referred | encoded | `s 94(2) the application is accompanied by what the subsection requires` |
| s 94(2)(d) | 1208 | (d) if section 93 applies (recent allotment of shares for no | encoded | `s 94(2) the application is accompanied by what the subsection requires` |
| s 94(2)(e) | 1209 | (e) a statement of the aggregate amount paid up on the share | encoded | `s 94(2) the application is accompanied by what the subsection requires` |
| s 94(3) | 1210 | (3) The statement of compliance required to be delivered tog | encoded | `s 94(3) the statement meets the description of the statement of compliance` |
| s 94(4) | 1211 | (4) The registrar may accept the statement of compliance as  | encoded | `s 94(4) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as a public company` |
| s 95 | 1212 | Statement of proposed secretary | encoded | `s 95(1) the statement of the company's proposed secretary contains the required information`; `s 95(3) the statement of the proposed secretary includes the company's statement of consent`; +1 more (see the rows of its subsections) |
| s 95(1) | 1213 | (1) The statement of the company's proposed secretary must c | encoded | `s 95(1) the statement of the company's proposed secretary contains the required information` |
| s 95(2) | 1214 | (2) For the required information in relation to proposed sec | encoded | `s 95(1) the statement of the company's proposed secretary contains the required information` |
| s 95(3) | 1215-1216 | (3) The statement must also include a statement by the compa | encoded | `s 95(3) the statement of the proposed secretary includes the company's statement of consent`; `s 95(3) consent may be given by one partner on behalf of all of them` |
| s 96 | 1217 | Issue of certificate of incorporation on re-registration | encoded | `s 96(1) the company shall be re-registered as a public company`; `s 96(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +5 more (see the rows of its subsections) |
| s 96(1) | 1218 | (1) If on an application for re-registration as a public com | encoded | `s 96(1) the company shall be re-registered as a public company` |
| s 96(2) | 1219 | (2) The registrar must issue a certificate of incorporation  | encoded | `s 96(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` |
| s 96(3) | 1220 | (3) The certificate must state that it is issued on re-regis | encoded | `s 96(3) the certificate meets the requirement of subsection (3)` |
| s 96(4) | 1221 | (4) On the issue of the certificate— | encoded | `s 96(4)(a) the company is a public company on the day`; `s 96(4)(b) the changes in the company's name and articles have taken effect on the day`; `s 96(4)(c) the person named in the statement as secretary is deemed to have been appointed on the day` |
| s 96(4)(a) | 1222 | (a) the company by virtue of the issue of the certificate be | encoded | `s 96(4)(a) the company is a public company on the day` |
| s 96(4)(b) | 1223 | (b) the changes in the company's name and articles take effe | encoded | `s 96(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 96(4)(c) | 1224 | (c) where the application contained a statement under sectio | encoded | `s 96(4)(c) the person named in the statement as secretary is deemed to have been appointed on the day` |
| s 96(5) | 1225 | (5) The certificate is conclusive evidence that the requirem | encoded | `s 96(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` |
| heading@1226 | 1226 | Public company becoming private | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 97 | 1227 | Re-registration of public company as private limited company | encoded | `s 97(1) all of the answers hold`; `s 97(2) the conditions are met`; +3 more (see the rows of its subsections) |
| s 97(1) | 1228 | (1) A public company may be re-registered as a private limit | encoded | `s 97(1) all of the answers hold`; `s 97(1) the public company may be re-registered as a private limited company` |
| s 97(1)(a) | 1229 | (a) a special resolution that it should be so re-registered  | encoded | `s 97(1) all of the answers hold`; `s 97(1) the public company may be re-registered as a private limited company` |
| s 97(1)(b) | 1230 | (b) the conditions specified below are met, and | encoded | `s 97(1) all of the answers hold`; `s 97(1) the public company may be re-registered as a private limited company` |
| s 97(1)(c) | 1231 | (c) an application for re-registration is delivered to the r | encoded | `s 97(1) all of the answers hold`; `s 97(1) the public company may be re-registered as a private limited company` |
| s 97(1)(c)(i) | 1232 | (i) the other documents required by that section, and | encoded | `s 97(1) all of the answers hold`; `s 97(1) the public company may be re-registered as a private limited company` |
| s 97(1)(c)(ii) | 1233 | (ii) a statement of compliance. | encoded | `s 97(1) all of the answers hold`; `s 97(1) the public company may be re-registered as a private limited company` |
| s 97(2) | 1234 | (2) The conditions are that— | encoded | `s 97(2) the conditions are met` |
| s 97(2)(a) | 1235 | (a) where no application under section 98 for cancellation o | encoded | `s 97(2) the conditions are met` |
| s 97(2)(a)(i) | 1236 | (i) having regard to the number of members who consented to  | encoded | `s 97(2) the conditions are met` |
| s 97(2)(a)(ii) | 1237 | (ii) the period within which such an application could be ma | encoded | `s 97(2) the conditions are met` |
| s 97(2)(b) | 1238 | (b) where such an application has been made— | encoded | `s 97(2) the conditions are met` |
| s 97(2)(b)(i) | 1239 | (i) the application has been withdrawn, or | encoded | `s 97(2) the conditions are met` |
| s 97(2)(b)(ii) | 1240 | (ii) an order has been made confirming the resolution and a  | encoded | `s 97(2) the conditions are met` |
| s 97(3) | 1241 | (3) The company must make such changes— | encoded | `s 97(3)(a) the company must make such changes in its name as are necessary in connection with its becoming a private company limited by shares or by guarantee`; `s 97(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming a private company limited by shares or by guarantee` |
| s 97(3)(a) | 1242 | (a) in its name, and | encoded | `s 97(3)(a) the company must make such changes in its name as are necessary in connection with its becoming a private company limited by shares or by guarantee` |
| s 97(3)(b) | 1243-1244 | (b) in its articles, | encoded | `s 97(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming a private company limited by shares or by guarantee` |
| s 98 | 1245 | Application to court to cancel resolution | encoded | `s 98(1) the applicants may apply to the court for the cancellation of the resolution`; `s 98(2) the application is made within 28 days after the passing of the resolution`; +7 more (see the rows of its subsections) |
| s 98(1) | 1246 | (1) Where a special resolution by a public company to be re- | encoded | `s 98(1) the applicants may apply to the court for the cancellation of the resolution` |
| s 98(1)(a) | 1247 | (a) by the holders of not less in the aggregate than 5% in n | encoded | `s 98(1) the applicants may apply to the court for the cancellation of the resolution` |
| s 98(1)(b) | 1248 | (b) if the company is not limited by shares, by not less tha | encoded | `s 98(1) the applicants may apply to the court for the cancellation of the resolution` |
| s 98(1)(c) | 1249-1250 | (c) by not less than 50 of the company's members; | encoded | `s 98(1) the applicants may apply to the court for the cancellation of the resolution` |
| s 98(2) | 1251 | (2) The application must be made within 28 days after the pa | encoded | `s 98(2) the application is made within 28 days after the passing of the resolution`; `s 98(2) the members' permission to apply to the court`; `s 98(2) the application may be made on behalf of the persons entitled to make it` |
| s 98(3) | 1252 | (3) On the hearing of the application the court shall make a | encoded | `s 98(3) the court shall make an order either cancelling or confirming the resolution` |
| s 98(4) | 1253 | (4) The court may— | encoded | `s 98(4) the court may make the order on terms, adjourn for the purchase of dissentient members' interests, and give directions` |
| s 98(4)(a) | 1254 | (a) make that order on such terms and conditions as it think | encoded | `s 98(4) the court may make the order on terms, adjourn for the purchase of dissentient members' interests, and give directions` |
| s 98(4)(b) | 1255 | (b) if it thinks fit adjourn the proceedings in order that a | encoded | `s 98(4) the court may make the order on terms, adjourn for the purchase of dissentient members' interests, and give directions` |
| s 98(4)(c) | 1256 | (c) give such directions, and make such orders, as it thinks | encoded | `s 98(4) the court may make the order on terms, adjourn for the purchase of dissentient members' interests, and give directions` |
| s 98(5) | 1257 | (5) The court's order may, if the court thinks fit— | encoded | `s 98(5) the court's order may provide for the purchase by the company of members' shares and alter the articles` |
| s 98(5)(a) | 1258 | (a) provide for the purchase by the company of the shares of | encoded | `s 98(5) the court's order may provide for the purchase by the company of members' shares and alter the articles` |
| s 98(5)(b) | 1259 | (b) make such alteration in the company's articles as may be | encoded | `s 98(5) the court's order may provide for the purchase by the company of members' shares and alter the articles` |
| s 98(6) | 1260 | (6) The court's order may, if the court thinks fit, require  | encoded | `s 98(6) the court's order may require the company not to amend its articles without the leave of the court` |
| s 98(7) | 1261 | (7) In this section and section 99(3) “the court”, in Englan | fork 6 | `s 98(7) the court is the High Court` |
| s 99 | 1262 | Notice to registrar of court application or order | encoded | `s 99(1) the applicants must immediately give notice to the registrar`; `s 99(2) the company must immediately give notice to the registrar`; +5 more (see the rows of its subsections) |
| s 99(1) | 1263-1264 | (1) On making an application under section 98 (application t | fork 8 | `s 99(1) the applicants must immediately give notice to the registrar` |
| s 99(2) | 1265 | (2) On being served with notice of any such application, the | fork 8 | `s 99(2) the company must immediately give notice to the registrar` |
| s 99(3) | 1266 | (3) Within 15 days of the making of the court's order on the | encoded | `s 99(3) the number of days allowed for delivering a copy of the order`; `s 99(3) the copy of the order is delivered within the time allowed`; `s 99(3) the company's duty to deliver a copy of the order` |
| s 99(4) | 1267 | (4) If a company fails to comply with subsection (2) or (3)  | fork 7 | `s 99(4) the person commits an offence` |
| s 99(4)(a) | 1268 | (a) the company, and | fork 7 | `s 99(4) the person commits an offence` |
| s 99(4)(b) | 1269 | (b) every officer of the company who is in default. | fork 7 | `s 99(4) the person commits an offence` |
| s 99(5) | 1270 | (5) A person guilty of an offence under this section is liab | encoded | `s 99(5) the penalty on summary conviction` |
| s 100 | 1271 | Application and accompanying documents | encoded | `s 100(1) the application contains what the subsection requires`; `s 100(2) the application is accompanied by what the subsection requires`; +2 more (see the rows of its subsections) |
| s 100(1) | 1272 | (1) An application for re-registration as a private limited  | encoded | `s 100(1) the application contains what the subsection requires` |
| s 100(2) | 1273 | (2) The application must be accompanied by— | encoded | `s 100(2) the application is accompanied by what the subsection requires` |
| s 100(2)(a) | 1274 | (a) a copy of the resolution that the company should re-regi | encoded | `s 100(2) the application is accompanied by what the subsection requires` |
| s 100(2)(b) | 1275 | (b) a copy of the company's articles as proposed to be amend | encoded | `s 100(2) the application is accompanied by what the subsection requires` |
| s 100(3) | 1276 | (3) The statement of compliance required to be delivered tog | encoded | `s 100(3) the statement meets the description of the statement of compliance` |
| s 100(4) | 1277 | (4) The registrar may accept the statement of compliance as  | encoded | `s 100(4) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as a private limited company` |
| s 101 | 1278 | Issue of certificate of incorporation on re-registration | encoded | `s 101(1) the company shall be re-registered as a private limited company`; `s 101(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more (see the rows of its subsections) |
| s 101(1) | 1279 | (1) If on an application for re-registration as a private li | encoded | `s 101(1) the company shall be re-registered as a private limited company` |
| s 101(2) | 1280 | (2) The registrar must issue a certificate of incorporation  | encoded | `s 101(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` |
| s 101(3) | 1281 | (3) The certificate must state that it is issued on re-regis | encoded | `s 101(3) the certificate meets the requirement of subsection (3)` |
| s 101(4) | 1282 | (4) On the issue of the certificate— | encoded | `s 101(4)(a) the company is a private limited company on the day`; `s 101(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 101(4)(a) | 1283 | (a) the company by virtue of the issue of the certificate be | encoded | `s 101(4)(a) the company is a private limited company on the day` |
| s 101(4)(b) | 1284 | (b) the changes in the company's name and articles take effe | encoded | `s 101(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 101(5) | 1285 | (5) The certificate is conclusive evidence that the requirem | encoded | `s 101(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` |
| heading@1286 | 1286 | Private limited company becoming unlimited | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 102 | 1287 | Re-registration of private limited company as unlimited | encoded | `s 102(1) all of the answers hold`; `s 102(5) the person is a trustee in bankruptcy of a member of the company`; +6 more (see the rows of its subsections) |
| s 102(1) | 1288 | (1) A private limited company may be re-registered as an unl | encoded | `s 102(1) all of the answers hold`; `s 102(1)(a) all the members of the company have assented`; `s 102(1) the private limited company may be re-registered as an unlimited company` |
| s 102(1)(a) | 1289 | (a) all the members of the company have assented to its bein | encoded | `s 102(1)(a) all the members of the company have assented` |
| s 102(1)(b) | 1290 | (b) the condition specified below is met, and | encoded | `s 102(1) all of the answers hold`; `s 102(1) the private limited company may be re-registered as an unlimited company` |
| s 102(1)(c) | 1291 | (c) an application for re-registration is delivered to the r | encoded | `s 102(1) all of the answers hold`; `s 102(1) the private limited company may be re-registered as an unlimited company` |
| s 102(1)(c)(i) | 1292 | (i) the other documents required by that section, and | encoded | `s 102(1) all of the answers hold`; `s 102(1) the private limited company may be re-registered as an unlimited company` |
| s 102(1)(c)(ii) | 1293 | (ii) a statement of compliance. | encoded | `s 102(1) all of the answers hold`; `s 102(1) the private limited company may be re-registered as an unlimited company` |
| s 102(2) | 1294 | (2) The condition is that the company has not previously bee | encoded | `s 102(2) the condition is met` |
| s 102(3) | 1295 | (3) The company must make such changes in its name and its a | encoded | `s 102(3)(a) the company must make such changes in its name and its articles as are necessary in connection with its becoming an unlimited company`; `s 102(3)(b) the company must make such further changes as are necessary in connection with its becoming an unlimited company having a share capital` |
| s 102(3)(a) | 1296 | (a) as are necessary in connection with its becoming an unli | encoded | `s 102(3)(a) the company must make such changes in its name and its articles as are necessary in connection with its becoming an unlimited company` |
| s 102(3)(b) | 1297 | (b) if it is to have a share capital, as are necessary in co | encoded | `s 102(3)(b) the company must make such further changes as are necessary in connection with its becoming an unlimited company having a share capital` |
| s 102(4) | 1298 | (4) For the purposes of this section— | encoded | `s 102(4) the member's assent is given` |
| s 102(4)(a) | 1299 | (a) a trustee in bankruptcy of a member of the company is en | encoded | `s 102(4) the member's assent is given` |
| s 102(4)(b) | 1300 | (b) the personal representative of a deceased member of the  | encoded | `s 102(4) the member's assent is given` |
| s 102(5) | 1301 | (5) In subsection (4)(a), “a trustee in bankruptcy of a memb | encoded | `s 102(5) the person is a trustee in bankruptcy of a member of the company` |
| s 102(5)(a) | 1302 | (a) a trustee or interim trustee in the sequestration under  | encoded | `s 102(5) the person is a trustee in bankruptcy of a member of the company` |
| s 102(5)(b) | 1303 | (b) a trustee under a protected trustee deed (within the mea | encoded | `s 102(5) the person is a trustee in bankruptcy of a member of the company` |
| s 103 | 1304 | Application and accompanying documents | encoded | `s 103(1) the application contains what the subsection requires`; `s 103(2) the application is accompanied by what the subsection requires`; +3 more (see the rows of its subsections) |
| s 103(1) | 1305 | (1) An application for re-registration as an unlimited compa | encoded | `s 103(1) the application contains what the subsection requires` |
| s 103(2) | 1306 | (2) The application must be accompanied by— | encoded | `s 103(2) the application is accompanied by what the subsection requires` |
| s 103(2)(a) | 1307 | (a) the prescribed form of assent to the company's being reg | encoded | `s 103(2) the application is accompanied by what the subsection requires` |
| s 103(2)(b) | 1308 | (b) a copy of the company's articles as proposed to be amend | encoded | `s 103(2) the application is accompanied by what the subsection requires` |
| s 103(3) | 1309 | (3) The statement of compliance required to be delivered tog | encoded | `s 103(3) the statement meets the description of the statement of compliance` |
| s 103(4) | 1310 | (4) The statement must contain a statement by the directors  | encoded | `s 103(4) the statement of compliance contains the directors' statement` |
| s 103(4)(a) | 1311 | (a) that the persons by whom or on whose behalf the form of  | encoded | `s 103(4) the statement of compliance contains the directors' statement` |
| s 103(4)(b) | 1312 | (b) if any of the members have not authenticated that form t | encoded | `s 103(4) the statement of compliance contains the directors' statement` |
| s 103(5) | 1313 | (5) The registrar may accept the statement of compliance as  | encoded | `s 103(5) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as an unlimited company` |
| s 104 | 1314 | Issue of certificate of incorporation on re-registration | encoded | `s 104(1) the company shall be re-registered as an unlimited company`; `s 104(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more (see the rows of its subsections) |
| s 104(1) | 1315 | (1) If on an application for re-registration of a private li | encoded | `s 104(1) the company shall be re-registered as an unlimited company` |
| s 104(2) | 1316 | (2) The registrar must issue a certificate of incorporation  | encoded | `s 104(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` |
| s 104(3) | 1317 | (3) The certificate must state that it is issued on re-regis | encoded | `s 104(3) the certificate meets the requirement of subsection (3)` |
| s 104(4) | 1318 | (4) On the issue of the certificate— | encoded | `s 104(4)(a) the company is an unlimited company on the day`; `s 104(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 104(4)(a) | 1319 | (a) the company by virtue of the issue of the certificate be | encoded | `s 104(4)(a) the company is an unlimited company on the day` |
| s 104(4)(b) | 1320 | (b) the changes in the company's name and articles take effe | encoded | `s 104(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 104(5) | 1321 | (5) The certificate is conclusive evidence that the requirem | encoded | `s 104(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` |
| heading@1322 | 1322 | Unlimited private company becoming limited | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 105 | 1323 | Re-registration of unlimited company as limited | encoded | `s 105(2) the condition is met`; `s 105(1) the unlimited company may be re-registered as a private limited company`; +3 more (see the rows of its subsections) |
| s 105(1) | 1324 | (1) An unlimited company may be re-registered as a private l | encoded | `s 105(1) the unlimited company may be re-registered as a private limited company` |
| s 105(1)(a) | 1325 | (a) a special resolution that it should be so re-registered  | encoded | `s 105(1) the unlimited company may be re-registered as a private limited company` |
| s 105(1)(b) | 1326 | (b) the condition specified below is met, and | encoded | `s 105(1) the unlimited company may be re-registered as a private limited company` |
| s 105(1)(c) | 1327 | (c) an application for re-registration is delivered to the r | encoded | `s 105(1) the unlimited company may be re-registered as a private limited company` |
| s 105(1)(c)(i) | 1328 | (i) the other documents required by that section, and | encoded | `s 105(1) the unlimited company may be re-registered as a private limited company` |
| s 105(1)(c)(ii) | 1329 | (ii) a statement of compliance. | encoded | `s 105(1) the unlimited company may be re-registered as a private limited company` |
| s 105(2) | 1330 | (2) The condition is that the company has not previously bee | encoded | `s 105(2) the condition is met` |
| s 105(3) | 1331 | (3) The special resolution must state whether the company is | encoded | `s 105(3) the special resolution meets the requirement of subsection (3)` |
| s 105(4) | 1332 | (4) The company must make such changes— | encoded | `s 105(4)(a) the company must make such changes in its name as are necessary in connection with its becoming a company limited by shares or by guarantee`; `s 105(4)(b) the company must make such changes in its articles as are necessary in connection with its becoming a company limited by shares or by guarantee` |
| s 105(4)(a) | 1333 | (a) in its name, and | encoded | `s 105(4)(a) the company must make such changes in its name as are necessary in connection with its becoming a company limited by shares or by guarantee` |
| s 105(4)(b) | 1334-1335 | (b) in its articles, | encoded | `s 105(4)(b) the company must make such changes in its articles as are necessary in connection with its becoming a company limited by shares or by guarantee` |
| s 106 | 1336 | Application and accompanying documents | encoded | `s 106(1) the application contains what the subsection requires`; `s 106(2) the application is accompanied by what the subsection requires`; +4 more (see the rows of its subsections) |
| s 106(1) | 1337 | (1) An application for re-registration as a limited company  | encoded | `s 106(1) the application contains what the subsection requires` |
| s 106(2) | 1338 | (2) The application must be accompanied by— | encoded | `s 106(2) the application is accompanied by what the subsection requires` |
| s 106(2)(a) | 1339 | (a) a copy of the resolution that the company should re-regi | encoded | `s 106(2) the application is accompanied by what the subsection requires` |
| s 106(2)(b) | 1340 | (b) if the company is to be limited by guarantee, a statemen | encoded | `s 106(2) the application is accompanied by what the subsection requires` |
| s 106(2)(c) | 1341 | (c) a copy of the company's articles as proposed to be amend | encoded | `s 106(2) the application is accompanied by what the subsection requires` |
| s 106(3) | 1342 | (3) The statement of guarantee required to be delivered in t | fork 3 | `s 106(3) the member's undertaking covers the winding up`; `s 106(3) the statement of guarantee is as required` |
| s 106(3)(a) | 1343 | (a) payment of the debts and liabilities of the company cont | fork 3 | `s 106(3) the member's undertaking covers the winding up`; `s 106(3) the statement of guarantee is as required` |
| s 106(3)(b) | 1344 | (b) payment of the costs, charges and expenses of winding up | fork 3 | `s 106(3) the member's undertaking covers the winding up`; `s 106(3) the statement of guarantee is as required` |
| s 106(3)(c) | 1345-1346 | (c) adjustment of the rights of the contributories among the | fork 3 | `s 106(3) the member's undertaking covers the winding up`; `s 106(3) the statement of guarantee is as required` |
| s 106(4) | 1347 | (4) The statement of compliance required to be delivered tog | encoded | `s 106(4) the statement meets the description of the statement of compliance` |
| s 106(5) | 1348 | (5) The registrar may accept the statement of compliance as  | encoded | `s 106(5) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as a limited company` |
| s 107 | 1349 | Issue of certificate of incorporation on re-registration | encoded | `s 107(1) the company shall be re-registered as a limited company`; `s 107(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more (see the rows of its subsections) |
| s 107(1) | 1350 | (1) If on an application for re-registration of an unlimited | encoded | `s 107(1) the company shall be re-registered as a limited company` |
| s 107(2) | 1351 | (2) The registrar must issue a certificate of incorporation  | encoded | `s 107(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` |
| s 107(3) | 1352 | (3) The certificate must state that it is issued on re-regis | encoded | `s 107(3) the certificate meets the requirement of subsection (3)` |
| s 107(4) | 1353 | (4) On the issue of the certificate— | encoded | `s 107(4)(a) the company is a limited company on the day`; `s 107(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 107(4)(a) | 1354 | (a) the company by virtue of the issue of the certificate be | encoded | `s 107(4)(a) the company is a limited company on the day` |
| s 107(4)(b) | 1355 | (b) the changes in the company's name and articles take effe | encoded | `s 107(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 107(5) | 1356 | (5) The certificate is conclusive evidence that the requirem | encoded | `s 107(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` |
| s 108 | 1357 | Statement of capital required where company already has shar | encoded | `s 108(1) the company must deliver a statement of capital to the registrar`; `s 108(1) the statement of capital is delivered within 15 days after the re-registration`; +4 more (see the rows of its subsections) |
| s 108(1) | 1358 | (1) A company which on re-registration under section 107 alr | encoded | `s 108(1) the company must deliver a statement of capital to the registrar`; `s 108(1) the statement of capital is delivered within 15 days after the re-registration`; `s 108(1) the company's duty to deliver a statement of capital` |
| s 108(2) | 1359 | (2) This does not apply if the information which would be in | encoded | `s 108(1) the company must deliver a statement of capital to the registrar` |
| s 108(2)(a) | 1360 | (a) a statement of capital and initial shareholdings (see se | encoded | `s 108(1) the company must deliver a statement of capital to the registrar` |
| s 108(2)(b) | 1361 | (b) (if different) the last statement of capital sent by the | encoded | `s 108(1) the company must deliver a statement of capital to the registrar` |
| s 108(3) | 1362 | (3) The statement of capital must state with respect to the  | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(a) | 1363 | (a) the total number of shares of the company, | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(b) | 1364 | (b) the aggregate nominal value of those shares, | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(ba) | 1365 | (ba) the aggregate amount (if any) unpaid on those shares (w | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(c) | 1366 | (c) for each class of shares— | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(c)(i) | 1367 | (i) prescribed particulars of the rights attached to the sha | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(c)(ii) | 1368 | (ii) the total number of shares of that class, and | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(c)(iii) | 1369 | (iii) the aggregate nominal value of shares of that class, . | encoded | `s 108(3) the statement of capital states what the subsection requires` |
| s 108(3)(d) | 1370 | (d) . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | repealed or blank in this text | the text shows "(d) . . . ." (omitted) |
| s 108(4) | 1371 | (4) If default is made in complying with this section, an of | fork 7 | `s 108(4) the person commits an offence` |
| s 108(4)(a) | 1372 | (a) the company, and | fork 7 | `s 108(4) the person commits an offence` |
| s 108(4)(b) | 1373 | (b) every officer of the company who is in default. | fork 7 | `s 108(4) the person commits an offence` |
| s 108(5) | 1374 | (5) A person guilty of an offence under this section is liab | encoded | `s 108(5) the penalty on summary conviction` |
| heading@1375 | 1375 | Public company becoming private and unlimited | inert (reason 1) | none: a Part, Chapter or cross-heading, which creates no rule |
| s 109 | 1376 | Re-registration of public company as private and unlimited | encoded | `s 109(5) the person is a trustee in bankruptcy of a member of the company`; `s 109(4) the member's assent is given`; +5 more (see the rows of its subsections) |
| s 109(1) | 1377 | (1) A public company limited by shares may be re-registered  | encoded | `s 109(1)(a) all the members of the company have assented`; `s 109(1) the public company limited by shares may be re-registered as an unlimited private company with a share capital` |
| s 109(1)(a) | 1378 | (a) all the members of the company have assented to its bein | encoded | `s 109(1)(a) all the members of the company have assented` |
| s 109(1)(b) | 1379 | (b) the condition specified below is met, and | encoded | `s 109(1) the public company limited by shares may be re-registered as an unlimited private company with a share capital` |
| s 109(1)(c) | 1380 | (c) an application for re-registration is delivered to the r | encoded | `s 109(1) the public company limited by shares may be re-registered as an unlimited private company with a share capital` |
| s 109(1)(c)(i) | 1381 | (i) the other documents required by that section, and | encoded | `s 109(1) the public company limited by shares may be re-registered as an unlimited private company with a share capital` |
| s 109(1)(c)(ii) | 1382 | (ii) a statement of compliance. | encoded | `s 109(1) the public company limited by shares may be re-registered as an unlimited private company with a share capital` |
| s 109(2) | 1383 | (2) The condition is that the company has not previously bee | encoded | `s 109(2) the condition is met` |
| s 109(2)(a) | 1384 | (a) as limited, or | encoded | `s 109(2) the condition is met` |
| s 109(2)(b) | 1385 | (b) as unlimited. | encoded | `s 109(2) the condition is met` |
| s 109(3) | 1386 | (3) The company must make such changes— | encoded | `s 109(3)(a) the company must make such changes in its name as are necessary in connection with its becoming an unlimited private company`; `s 109(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming an unlimited private company` |
| s 109(3)(a) | 1387 | (a) in its name, and | encoded | `s 109(3)(a) the company must make such changes in its name as are necessary in connection with its becoming an unlimited private company` |
| s 109(3)(b) | 1388-1389 | (b) in its articles, | encoded | `s 109(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming an unlimited private company` |
| s 109(4) | 1390 | (4) For the purposes of this section— | encoded | `s 109(4) the member's assent is given` |
| s 109(4)(a) | 1391 | (a) a trustee in bankruptcy of a member of the company is en | encoded | `s 109(4) the member's assent is given` |
| s 109(4)(b) | 1392 | (b) the personal representative of a deceased member of the  | encoded | `s 109(4) the member's assent is given` |
| s 109(5) | 1393 | (5) In subsection (4)(a), “a trustee in bankruptcy of a memb | encoded | `s 109(5) the person is a trustee in bankruptcy of a member of the company` |
| s 109(5)(a) | 1394 | (a) a trustee or interim trustee in the sequestration under  | encoded | `s 109(5) the person is a trustee in bankruptcy of a member of the company` |
| s 109(5)(b) | 1395 | (b) a trustee under a protected trustee deed (within the mea | encoded | `s 109(5) the person is a trustee in bankruptcy of a member of the company` |
| s 110 | 1396 | Application and accompanying documents | encoded | `s 110(1) the application contains what the subsection requires`; `s 110(2) the application is accompanied by what the subsection requires`; +3 more (see the rows of its subsections) |
| s 110(1) | 1397 | (1) An application for re-registration of a public company a | encoded | `s 110(1) the application contains what the subsection requires` |
| s 110(2) | 1398 | (2) The application must be accompanied by— | encoded | `s 110(2) the application is accompanied by what the subsection requires` |
| s 110(2)(a) | 1399 | (a) the prescribed form of assent to the company's being reg | encoded | `s 110(2) the application is accompanied by what the subsection requires` |
| s 110(2)(b) | 1400 | (b) a copy of the company's articles as proposed to be amend | encoded | `s 110(2) the application is accompanied by what the subsection requires` |
| s 110(3) | 1401 | (3) The statement of compliance required to be delivered tog | encoded | `s 110(3) the statement meets the description of the statement of compliance` |
| s 110(4) | 1402 | (4) The statement must contain a statement by the directors  | encoded | `s 110(4) the statement of compliance contains the directors' statement` |
| s 110(4)(a) | 1403 | (a) that the persons by whom or on whose behalf the form of  | encoded | `s 110(4) the statement of compliance contains the directors' statement` |
| s 110(4)(b) | 1404 | (b) if any of the members have not authenticated that form t | encoded | `s 110(4) the statement of compliance contains the directors' statement` |
| s 110(5) | 1405 | (5) The registrar may accept the statement of compliance as  | encoded | `s 110(5) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as an unlimited private company` |
| s 111 | 1406 | Issue of certificate of incorporation on re-registration | encoded | `s 111(1) the company shall be re-registered as an unlimited private company`; `s 111(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more (see the rows of its subsections) |
| s 111(1) | 1407 | (1) If on an application for re-registration of a public com | encoded | `s 111(1) the company shall be re-registered as an unlimited private company` |
| s 111(2) | 1408 | (2) The registrar must issue a certificate of incorporation  | encoded | `s 111(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` |
| s 111(3) | 1409 | (3) The certificate must state that it is issued on re-regis | encoded | `s 111(3) the certificate meets the requirement of subsection (3)` |
| s 111(4) | 1410 | (4) On the issue of the certificate— | encoded | `s 111(4)(a) the company is an unlimited private company on the day`; `s 111(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 111(4)(a) | 1411 | (a) the company by virtue of the issue of the certificate be | encoded | `s 111(4)(a) the company is an unlimited private company on the day` |
| s 111(4)(b) | 1412 | (b) the changes in the company's name and articles take effe | encoded | `s 111(4)(b) the changes in the company's name and articles have taken effect on the day` |
| s 111(5) | 1413 | (5) The certificate is conclusive evidence that the requirem | encoded | `s 111(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` |
| term "specified" in s 56(5) | 603 | “specified” defined in s 56(5) | encoded | `s 56(5) the department or body is specified` |
| term "specified" in s 57(5) | 616 | “specified” defined in s 57(5) | encoded | `s 57(5) the character, sign, symbol, position or style is specified` |
| term "specified" in s 65(4) | 741 | “specified” defined in s 65(4) | encoded | `s 65(4) the word, expression, indication, part of the name or accompanying word is specified` |
| term "specified" in s 66(6) | 758 | “specified” defined in s 66(6) | encoded | `s 66(6) the circumstances or consent are specified` |
| term "specified" in s 67(6) | 775 | “specified” defined in s 67(6) | encoded | `s 67(6) the circumstances or consent are specified` |
| term "specified" in s 82(4) | 1031 | “specified” defined in s 82(4) | encoded | `s 82(4) the information, location, description of document or communication is specified` |
| term "specified" in s 84(3) | 1047 | “specified” defined in s 84(3) | encoded | `s 84(3) the requirement is specified` |
| term "relevant relationship" in s 57C(4) | 633 | “relevant relationship” defined in s 57C(4) | encoded | `s 57C(4) the person has a relevant relationship with the company` |
| term "the applicant" in s 69(1) | 792 | “the applicant” defined in s 69(1) | encoded | `s 69(1) the applicant may object to the company's registered name` |
| term "goodwill" in s 69(7) | 809 | “goodwill” defined in s 69(7) | encoded | `s 69(7) the interest is goodwill` |
| term "offending name" in s 73(2) | 853 | “offending name” defined in s 73(2) | encoded | `s 73(2) the name is an offending name` |
| term "crime" in s 76E(2)(a) | 977 | “crime” defined in s 76E(2)(a) | encoded | `s 76E(2)(a) the conduct is crime` |
| term "serious" in s 76E(2)(b) | 980 | “serious” defined in s 76E(2)(b) | encoded | `s 76E(2)(b) the crime is serious` |
| term "appropriate address" in s 86(2) | 1059 | “appropriate address” defined in s 86(2) | encoded | `s 86(2) the address is an appropriate address` |
| term "Welsh company" in s 88(1) | 1083 | “Welsh company” defined in s 88(1) | encoded | `s 88(1) the company is a Welsh company` |
| term "appropriate email address" in s 88A(2) | 1098 | “appropriate email address” defined in s 88A(2) | encoded | `s 88A(2) the email address is an appropriate email address` |
| term "unqualified report" in s 92(3) | 1166 | “unqualified report” defined in s 92(3) | encoded | `s 92(3) the report is an unqualified report` |
| term "net assets" in s 92(6) | 1171 | “net assets” defined in s 92(6) | encoded | `s 92(6) the amount of the company's net assets or undistributable reserves` |
| term "undistributable reserves" in s 92(6) | 1171 | “undistributable reserves” defined in s 92(6) | encoded | `s 92(6) the amount of the company's net assets or undistributable reserves` |
| term "arrangement" in s 93(7)(b) | 1197 | “arrangement” defined in s 93(7)(b) | encoded | `s 93(7)(b) the thing is an arrangement` |
| term "the court" in s 98(7) | 1261 | “the court” defined in s 98(7) | fork 6 | `s 98(7) the court is the High Court` |
| term "a trustee in bankruptcy of a member of the company" in s 102(5) | 1301 | “a trustee in bankruptcy of a member of the company” defined in s 102(5) | encoded | `s 102(5) the person is a trustee in bankruptcy of a member of the company` |
| term "a trustee in bankruptcy of a member of the company" in s 109(5) | 1393 | “a trustee in bankruptcy of a member of the company” defined in s 109(5) | encoded | `s 109(5) the person is a trustee in bankruptcy of a member of the company` |

## Fork register (coa2)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the provision, the function, the reading taken, the other reading, and the text that licenses each.
Rows of the coverage table that rest on an entry say `fork N`.
**Case-by-case sites** (the maintainer's ruling of 2026-11-05, quoted below): the six questions the rulings leave open are decided at each site on the text's own words, and each site carries one line for a reviewer to overrule.
Those lines are the rows of "Marginal readings for a lawyer (coa2)": the provision, the function, the answer taken, and the other reading.
The sites are the rows of that table (an "unless" or "except" once met that is not a fork below, such as s 64(7) and s 86(1); a duty whose "if" or "where" is unmet, the `(a)` rows); no Schedule and no state ledger is in this range.

### Forks taken

**Fork 1. Daily default fine, two wordings (s 63(3), s 64(6)).**
Text (lines 701 and 728): "a fine not exceeding level 5 on the standard scale and, for continued contravention, a daily default fine not exceeding one-tenth of level 5 on the standard scaleone-tenth of the greater of £5,000 or level 4 on the standard scale."
The wording after "scale" runs two limits together with no space.
Readings: (i) one-tenth of level 5; (ii) one-tenth of the greater of £5,000 or level 4; (iii) both are the Act, one replacing the other, which the rendering does not say.
Taken: the text does not choose. `Penalty`'s daily default fine is `NOTHING` in `s 63(3) the penalty on summary conviction` and `s 64(6) the penalty on summary conviction`; each wording is a separate function of the level amounts (`s 63(3) the daily default fine in pounds on the first wording` and `... on the second wording`, likewise for s 64(6)); the seat prints "daily default fine: not covered by the text".
The "greater of £5,000 or level 4" limit has no constructor in the core's `Fine limit` (NEEDS-CORE.md).

**Fork 2. "Before the end of the period" (ss 64(2B), 68(3), 75(3), 76(3A), 76A(4), 76B(4)).**
Text (s 64(2B), line 720): "Any such direction must be given before the end of the period for the time being specified."
Readings: (i) a further direction given on the last day of the period is given before the end of it; (ii) it must be given on an earlier day.
Taken: (i), `AT MOST` the last day, with a test on the last day and the day after.

**Fork 3. Periods in months and years (ss 68(2)(a), 75(2)(a), 92(1)(a), 106(3)).**
Text: "within twelve months of the company's registration by the name in question" (line 779); "within five years of the company's registration by that name" (line 885); "not more than seven months before the date on which the application is delivered" (line 1162); "within one year after he ceases to be a member" (line 1342).
Readings: (i) the last day is the same calendar date that many months or years on; (ii) it is the day before that date.
Taken: (i), by the keel's `add months` and `add years` applied to the earlier date, with a test on both sides of the end.
Periods in days follow the keel's counting convention and are not forks: "within 28 days after" is the date plus 28, "within three weeks beginning with the date" is the 21st day.

**Fork 4. A requirement that is not engaged counts as met (s 91(1)(c) and (d)).**
Text (lines 1141 and 1142-1144): "if any shares ... have been fully or partly paid up by an undertaking ..., the undertaking must have been performed or otherwise discharged"; "if shares have been allotted ... otherwise than in cash, and the consideration ... includes an undertaking to the company ..., then either ...".
Readings: (i) where no such shares exist the paragraph imposes nothing, so the requirement is met; (ii) the answer is "not covered".
Taken: (i): `JUST TRUE` for an allotment the paragraph does not reach; `JUST FALSE` where it applies and neither limb holds.

**Fork 5. An "unless" once met (ss 60(2), 93(2)).**
Text: s 60(2), "The registrar may refuse to register a private limited company by a name that does not include the word "limited" (or a permitted alternative) unless a statement has been delivered to him that the company meets the conditions for exemption" (line 657); s 93(2), "The registrar shall not entertain an application ... unless— (a) ... or (b) ..." (line 1176).
Taken: s 60(2) answers `JUST FALSE` to "the registrar may refuse" once the statement is delivered (the "unless" is the text's own no); s 93(2) answers `JUST TRUE` to "the registrar may entertain the application" once an "unless" route holds.
Other reading of s 93(2): the text only removes the bar and does not itself say the registrar may entertain, so the answer is `NOTHING`.

**Fork 6. "The court" in s 98(7), as rendered.**
Text (line 1261): "In this section and section 99(3) "the court", in England and Wales, means the High Court" and no more.
Readings: (i) the subsection says what the court is in England and Wales and nothing about elsewhere; (ii) the rendering lost words about Scotland and Northern Ireland, which the Act may supply elsewhere (outside this range).
Taken: (i): `JUST TRUE` for England and Wales, `NOTHING` elsewhere (finding 5).

**Fork 7. Shadow director as an officer (ss 64(5), 86(3), 88A(3), 99(4), 108(4)).**
Text: the sentence "For this purpose a shadow director is treated as an officer of the company." follows the offence in ss 63(2), 68(5), 75(5), 76(6), 76A(11) and 76B(11), and is absent from ss 64(5), 86(3), 88A(3), 99(4) and 108(4), which name "the company" and "every officer of the company who is in default".
Readings: (i) where the sentence is absent a shadow director is not named, so the answer for a shadow director is not covered; (ii) a shadow director is an officer for these offences anyway (a question for s 1121 and s 251, in other parts).
Taken: (i): `NOTHING` (silent) for a shadow director; `JUST TRUE` for the company and for the officer in default.

**Fork 8. "Immediately" (s 99(1), s 99(2)).**
Text (lines 1263 and 1265): "must immediately give notice to the registrar".
Readings: (i) the duty arises when the application is made or served and the text gives no number of days; (ii) "immediately" is a deadline of the same day.
Taken: (i): the two are decision functions (`JUST TRUE` when the trigger holds, `JUST FALSE` when it does not) with no day count; s 99(3) (15 days or a longer period) is a regulative rule with a trace.

**Fork 9. Registration permitted by regulations (s 66(1)).**
Text: s 66(1) "A company must not be registered under this Act by a name that is the same as another name appearing in the registrar's index of company names" (lines 745-746); s 66(4)(a) lets regulations provide that registration "that would otherwise be prohibited" is permitted in specified circumstances or with specified consent.
Readings: (i) where the regulations permit registration, s 66(1) does not bar it; (ii) the regulations are outside the sources, so the Act alone answers.
Taken: (i): the regulations' permission is a plain input; when it holds the answer is `JUST TRUE`.

**Forks 10 to 21: a power whose "if" gate failed answers `NOTHING` (name-test sweep of 2026-11-12).**
A function named for a grant or a power ("may ...") used to answer `JUST FALSE` when an "if" in the section failed, which reads as "may not": a grant turned into a bar.
The Guide (section 5, "In short") gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit".
Each line below is one function: the provision, the function, the answer taken, and the other reading (`JUST FALSE`, a failed "if" read as the text's own no).
Each is also a row of "Marginal readings for a lawyer (coa2)" and a `fork N` row of the coverage table.

- **Fork 10. s 64(1)**, `s 64(1) the Secretary of State may direct the company to change its name` (lines 711-716). Gate: "If it appears to the Secretary of State that a company whose name does not include “limited” or any of the permitted alternatives— (a) ... or (b) ..., the Secretary of State may direct the company to change its name". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 11. s 67(1)**, `s 67(1) the Secretary of State may direct the company to change its name` (lines 760-762). Gate: "The Secretary of State may direct a company to change its name if it has been registered in a name that is the same as or, in the opinion of the Secretary of State, too like— (a) ... or (b) ...". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 12. s 73(4)**, `s 73(4) the adjudicator may determine a new name for the company` (line 859). Gate: "If the respondent company's name is not changed in accordance with the order by the specified date, the adjudicator may determine a new name". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 13. s 74(4)**, `s 74(4) the court may specify the date, remit the matter or make any order or determination that the adjudicator might have made` (lines 870-873). Gate: "If on appeal the court— (a) affirms ... or (b) reverses ..., the court may ...". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 14. s 75(1)**, `s 75(1) the Secretary of State may direct the company to change its name` (lines 880-883). Gate: "If it appears to the Secretary of State— (a) ... or (b) ..., the Secretary of State may direct the company to change its name". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 15. s 76(1)**, `s 76(1) the Secretary of State may direct the company to change its name` (line 899). Gate: "If in the opinion of the Secretary of State the name by which a company is registered gives so misleading an indication of the nature of its activities as to pose a risk of harm to the public in the United Kingdom or elsewhere, the Secretary of State may direct the company to change its name". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 16. s 76A(1)**, `s 76A(1) the Secretary of State may direct the company to change its name` (lines 916-918). Gate: "The Secretary of State may direct a company to change its name if it appears to the Secretary of State that the name has been used, or is intended to be used, by the company to facilitate— (a) ... or (b) ...". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 17. s 76B(1)**, `s 76B(1) the Secretary of State may direct the company to change its name` (lines 935-938). Gate: "The Secretary of State may direct a company to change its name if— (a) ... or (b) ...". Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 18. s 64(2B)**, `s 64(2B) the Secretary of State may give a further direction extending the period` (lines 719-720). Gate: "The Secretary of State may by further direction in writing extend the period" (the "in writing" complement; the time limit is closed by the next sentence and stays `JUST FALSE`). Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 19. s 76(3A)**, `s 76(3A) the Secretary of State may give a further direction extending the period` (lines 902-903). Gate: "The Secretary of State may by further direction in writing extend the period" (the "in writing" complement; the time limit stays `JUST FALSE`). Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 20. s 76A(4)**, `s 76A(4) the Secretary of State may give a further direction extending the period` (lines 921-922). Gate: "The Secretary of State may by further direction in writing extend the period" (the "in writing" complement; the time limit stays `JUST FALSE`). Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.
- **Fork 21. s 76B(4)**, `s 76B(4) the Secretary of State may give a further direction extending the period` (lines 941-942). Gate: "The Secretary of State may by further direction in writing extend the period" (the "in writing" complement; the time limit stays `JUST FALSE`). Answer taken: `NOTHING` where the gate fails. Other reading: `JUST FALSE`, a failed "if" read as the text's own no.

**Listed, not decided (name-test sweep of 2026-11-12).** Two groups are not settled by a sweep and are not changed.
(i) "May" functions whose gate is "where": ruling (b) of the "Periods, where and scope limits" paragraph says `JUST FALSE`, and the Guide's line on grants points the other way, so this is a question for the maintainer or a lawyer.
Each answers `JUST FALSE` today.

| function | gate |
| --- | --- |
| `s 64(6A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | "Where a direction is given under subsection (1), the registrar may omit" |
| `s 67(1A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | "Where a direction is given under subsection (1), the registrar may omit" |
| `s 73(7) the registrar may omit from the register material available for public inspection any mention of the name to which the order relates` | "Where an order is made under subsection (1), the registrar may omit" |
| `s 75(4A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | "Where a direction is given under subsection (1), the registrar may omit" |
| `s 76(5B) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | "Where a direction is given under subsection (1), the registrar may omit" |
| `s 76A(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | "Where a direction is given under subsection (1), the registrar may omit" |
| `s 76B(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | "Where a direction is given under subsection (1), the registrar may omit" |
| `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register` | "Where, in the opinion of the registrar, a company’s registered name consists of or includes computer code, the registrar may" |
| `s 76D(1) the registrar may determine a new name for the company` | "Where a company fails to comply with a direction to change its name, the registrar may determine a new name for the company" |
| `s 98(1) the applicants may apply to the court for the cancellation of the resolution` | "Where a special resolution by a public company to be re-registered as a private limited company has been passed, an application to the court ... may be made" (its second `JUST FALSE`, "but not by a person who has consented to or voted in favour", is a flat negative and stays) |

(ii) "Entitled"-named functions: none answers `JUST FALSE`. The six functions with "entitled" in their names (`s 94(4)`, `s 100(4)`, `s 103(5)`, `s 106(5)`, `s 110(5)`: "the registrar may accept the statement ... that the company is entitled to be re-registered"; `s 98(2)`: "the persons entitled to make it") are powers or evidence rules whose only non-`JUST TRUE` answer is already `NOTHING`.

### Rulings applied (verbatim from the brief)

Each ruling below is recorded again, word for word, because this module carries the `NOTHING-kind` tags that rule produces.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Jural relations (coa2)

One row per provision (or group of provisions) that creates a relation, with the holder of the right, privilege, power or immunity, the bearer of the correlative duty, no-right, liability or disability, and the L4 rule.
Each relation is stated once, as a relation between two parties.
A provision that creates none is listed once as `none`.
Where the text names no counterparty the cell says so, and no actor is invented.
Rows are in the Act's order and cover every section from s 53 to s 111.

| section | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 53 | none named in the text | applicants for registration: cannot be registered by a name the Secretary of State thinks an offence or offensive | disability | `s 53 the company may be registered by the name` |
| s 53A | none named in the text | applicants for registration: cannot be registered by a name the Secretary of State thinks intended to facilitate dishonesty or deception | disability | `s 53A the company may be registered by the name` |
| s 54(1) | Secretary of State: approves | applicants and the company: no registration by a name suggesting a connection with government or a public authority without approval | power / liability | `s 54(1) the approval of the Secretary of State is required` |
| s 54(2) | none: definitions of "local authority" and "public authority" | - | none | (none: no relation) |
| s 55(1) | Secretary of State: approves | applicants and the company: no registration by a name with a specified sensitive word without approval | power / liability | `s 55(1) the approval of the Secretary of State is required` |
| s 56(2) | the specified department or body: to be asked for its view (only where regulations require it) | the applicant: must request it in writing | claim / duty | `s 56(2) the applicant must request the specified department or body in writing to indicate whether and why it has any objections` |
| s 56(3) | the registrar: to receive the statement and a copy of any response | the applicant (the application to register) | claim / duty | `s 56(3)(a) the application must include a statement that a request under this section has been made`; `s 56(3)(b) the application must be accompanied by a copy of the response received` |
| s 56(4) | the registrar: to receive the statement and a copy of any response | the company (the notice of the change of name) | claim / duty | `s 56(4)(a) the notice of the change must be accompanied by a statement by a director or secretary that a request has been made`; `s 56(4)(b) the notice of the change must be accompanied by a copy of the response received` |
| s 56(5) | none: definition of "specified" | - | none | (none: no relation) |
| s 56A | none named in the text | applicants: cannot be registered by a name likely to give the false impression of a connection with a foreign government or an international organisation | disability | `s 56A the company may be registered by the name` |
| s 57(3) | none named in the text | applicants: cannot be registered by a name with anything the regulations do not permit | disability | `s 57(3) the company may be registered by the name` |
| s 57(5) | none: definition of "specified" | - | none | (none: no relation) |
| s 57A | none named in the text | applicants: cannot be registered by a name that consists of or includes computer code in the Secretary of State's opinion | disability | `s 57A the company may be registered by the name` |
| s 57B(1) | Secretary of State: approves | a company made to change its name: cannot be registered again by its former name or a similar one without approval | power / disability | `s 57B(1) the company may be registered by the name` |
| s 57B(2) | none: counting rule (a name determined on default counts as a change following a direction or order) | - | none | (none: no relation) |
| s 57B(3) | none: counting rule | - | none | (none: no relation) |
| s 57C(1) | Secretary of State: approves | another company with a person who has a relevant relationship with both: cannot be registered by a name a company was directed or ordered to change, or a similar one, without approval | power / disability | `s 57C(1) the other company may be registered by the name` |
| s 57C(2) | none: carve-out | - | none | (none: no relation) |
| s 57C(3) | none: counting rule (whether the relationships coincided in time) | - | none | (none: no relation) |
| s 57C(4) | none: definition of "relevant relationship" | - | none | (none: no relation) |
| s 57C(5) | none: counting rule | - | none | (none: no relation) |
| s 58(1) | none named in the text | a limited public company: must end its name with "public limited company" or "p.l.c." | claim of none named / duty | `s 58(1) the name of the company must end with public limited company or p.l.c.`; `s 58(1) the name of the company ends as the section requires` |
| s 58 | a Welsh public company: may instead end with the Welsh form | none named | privilege / no-right | `s 58(1) the name of the company must end with public limited company or p.l.c.`; `s 58(1) the name of the company ends as the section requires` |
| s 59(1) | none named in the text | a limited private company that is not exempt: must end its name with "limited" or "ltd." | claim of none named / duty | `s 59(1) the name of the company must end with limited or ltd.`; `s 59(1) the name of the company ends as the section requires` |
| s 59 | a Welsh private company: may instead end with the Welsh form | none named | privilege / no-right | `s 59(1) the name of the company must end with limited or ltd.`; `s 59(1) the name of the company ends as the section requires` |
| s 60(1) | a private company that is a charity, exempted by regulations or within s 61 or s 62: exempt from s 59 | none named (no one may require "limited") | privilege / no-right | `s 60(1) the private company is exempt from section 59` |
| s 60(2) | the registrar: may refuse to register a private limited company by a name without "limited" | the company: liable to refusal; once a statement of exemption is delivered it is immune | power / liability; immunity / disability | `s 60(2) the registrar may refuse to register the company by the name` |
| s 60(3) | the registrar: may accept the statement as sufficient evidence | the company: liable to have the statement accepted | power / liability | `s 60(3) the registrar may accept the statement as sufficient evidence of the matters stated in it` |
| s 61 | a continued-exemption company limited by shares: exempt so long as it meets the two conditions and does not change its name | none named | privilege / no-right | `s 61(1) the section applies to the company`; `s 61(1)(a) the date on which the company must have been registered in Great Britain`; +4 more |
| s 62 | a continued-exemption company limited by guarantee: exempt on the same terms | none named | privilege / no-right | `s 62(2) the first condition is met`; `s 62(3) the second condition is met`; +1 more |
| s 63(1) | none named in the text | an exempt company: cannot amend its articles so that they cease to comply with the conditions | disability | `s 63(1) the company may amend its articles as proposed`; `s 63(1) the company's duty not to amend its articles` |
| s 63(2) | the State (the text makes the act an offence; it names no prosecutor) | the company; every officer in default; a shadow director (treated as an officer): liable for the offence | claim / duty; power / liability | `s 63(2) the person commits an offence` |
| s 63(3) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction to the penalty (fork 1 on the daily default fine) | power / liability | `s 63(3) the penalty on summary conviction`; `s 63(3) the daily default fine in pounds on the first wording`; +1 more |
| s 64(1) | Secretary of State: may direct a company whose name lacks "limited" to change it | the company: liable to the direction | power / liability | `s 64(1) the Secretary of State may direct the company to change its name` |
| s 64(2) | the company: entitled to a direction in the form the subsection requires | Secretary of State: duty to give the direction in writing, with a period | claim / duty | `s 64(2) the direction meets the requirements of subsection (2)` |
| s 64(2A) | the company: entitled to a period of at least 28 days | Secretary of State | claim / duty | `s 64(2A) the period meets the requirement of subsection (2A)` |
| s 64(2B) | Secretary of State: may extend the period by a further direction in writing | the company: liable to the extension | power / liability | `s 64(2B) the Secretary of State may give a further direction extending the period` |
| s 64(3) | the company (acting by its directors): may change its name by resolution of the directors to comply | none named | privilege / no-right | `s 64(3) the company may change its name by resolution of the directors`; `s 64(3) the resolution method does not prejudice another method of changing the name` |
| s 64(4) | the registrar: to be given notice of the change | the company: must give notice | claim / duty | `s 64(4) the company must give notice to the registrar of the change` |
| s 64(5) | the State (the text makes the act an offence; it names no prosecutor) | the company and every officer in default: liable for failing to comply with the direction (no shadow-director sentence: fork 7) | claim / duty; power / liability | `s 64(5) the company's duty to change its name as directed`; `s 64(5) the person commits an offence` |
| s 64(6) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction (fork 1) | power / liability | `s 64(6) the penalty on summary conviction`; `s 64(6) the daily default fine in pounds on the first wording`; +1 more |
| s 64(6A) | the registrar: may omit the former name from the register available for public inspection | none named | power / liability | `s 64(6A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 64(7) | Secretary of State: approves a later change to a name without "limited" | the company directed to change: cannot change to such a name without approval | power / disability | `s 64(7) the approval of the Secretary of State is required for the change of name` |
| s 65(3) | none named in the text | applicants: cannot be registered by a name with an indication of type or legal form the regulations prohibit | disability | `s 65(3) the company may be registered by the name` |
| s 65(4) | none: definition of "specified" | - | none | (none: no relation) |
| s 66(1) | none named in the text | applicants: cannot be registered by a name that is the same as one in the index (unless the regulations permit: fork 9) | disability | `s 66(1) the company may be registered by the name` |
| s 66(6) | none: definition of "specified" | - | none | (none: no relation) |
| s 67(1) | Secretary of State: may direct a company to change a name the same as, or too like, an indexed name | the company: liable to the direction | power / liability | `s 67(1) the Secretary of State may direct the company to change its name` |
| s 67(1A) | the registrar: may omit the former name from the register available for public inspection | none named | power / liability | `s 67(1A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 67(6) | none: definition of "specified" | - | none | (none: no relation) |
| s 68(2) | the company: entitled to a direction within twelve months, in writing, specifying a period | Secretary of State | claim / duty | `s 68(2)(a) the direction is given within twelve months of the company's registration by the name`; `s 68(2)(b) the direction specifies the period` |
| s 68(3) | Secretary of State: may extend the period by a further direction | the company: liable to the extension | power / liability | `s 68(3) the Secretary of State may give a further direction extending the period` |
| s 68(5) | the State (the text makes the act an offence; it names no prosecutor) | the company; every officer in default; a shadow director (treated as an officer): liable for failing to comply | claim / duty; power / liability | `s 68(5) the company's duty to change its name as directed`; `s 68(5) the person commits an offence` |
| s 68(6) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction | power / liability | `s 68(6) the penalty on summary conviction` |
| s 69(1) | the applicant: may object to a registered name (by application to an adjudicator) | the company with the registered name: liable to the objection | power / liability | `s 69(1) the applicant may object to the company's registered name` |
| s 69(3) | a member or director of the company: may be joined as a respondent | none named | privilege / no-right | `s 69(3) the person is the primary respondent to the application`; `s 69(3) the person may be joined as a respondent` |
| s 69(4) | the respondents: immune from the objection if they show one of the defences | the applicant: disability (the objection is not upheld on that ground) | immunity / disability | `s 69(4) the objection is upheld under subsection (4)` |
| s 69(5) | the applicant: may still have the objection upheld by showing a main purpose of obtaining money or blocking registration | the respondents: liable | power / liability | `s 69(5) the objection is nevertheless upheld` |
| s 69(6) | the respondents: immune once the objection is not upheld under (4) or (5) | the applicant: disability (the objection is dismissed) | immunity / disability | `s 69(6) the objection is dismissed` |
| s 69(7) | none: definition of "goodwill" | - | none | (none: no relation) |
| s 70 | none: appointment and staffing of adjudicators (machinery) | - | none | (none: no relation) |
| s 71 | none: power to make rules (machinery) | - | none | (none: no relation) |
| s 72 | the public (and the parties): to have the decision and reasons made available within 90 days | the adjudicator: must make them available | claim / duty | `s 72(1) the adjudicator's duty to make the decision available`; `s 72(1) the decision was made available within 90 days of the determination`; +1 more |
| s 73(1) | the successful applicant: to an order | the adjudicator: must make the order; the respondent company: liable to it | claim / duty; power / liability | `s 73(1) the adjudicator must make an order`; `s 73(1)(a) the order requires the person to change its name to one that is not an offending name`; +1 more |
| s 73(2) | none: definition of "offending name" | - | none | (none: no relation) |
| s 73(3) | the applicant: may enforce the order as an order of the court | the company: liable to enforcement | power / liability | `s 73(3) the order meets the requirement to specify a date`; `s 73(3) the order may be enforced` |
| s 73(4) | the adjudicator: may determine a new name if the company did not change it | the company: liable | power / liability | `s 73(4) the adjudicator may determine a new name for the company` |
| s 73(5) | the company, the applicant and the registrar: to be told of the determination | the adjudicator: must give notice | claim / duty | `s 73(5) the adjudicator must give notice of his determination to the recipient` |
| s 73(6) | none: when a name counts as changed in accordance with the order | - | none | (none: no relation) |
| s 73(7) | the registrar: may omit the former name from the register available for public inspection | none named | power / liability | `s 73(7) the registrar may omit from the register material available for public inspection any mention of the name to which the order relates` |
| s 74(1) | a party to the adjudicator's decision: may appeal to the court | the other party: liable to the appeal | power / liability | `s 74(1) an appeal lies to the court from the decision` |
| s 74(2) | the appellant: may give notice of appeal before the date the order sets | none named | power / liability | `s 74(2) notice of appeal is given in time` |
| s 74(3) | the appellant company: its duty under the order is suspended once notice of appeal is given | the applicant: cannot enforce meanwhile | immunity / disability | `s 74(3) the effect of the adjudicator's order is suspended` |
| s 74(4) | the court: may fix the date, remit the matter or make any order the adjudicator might have made | the parties: liable | power / liability | `s 74(4) the court may specify the date, remit the matter or make any order or determination that the adjudicator might have made` |
| s 74(5) | the company, the applicant and the registrar: to be told of the court's determination | the court: must give notice | claim / duty | `s 74(5) the court must give notice of the determination to the recipient` |
| s 75(1) | Secretary of State: may direct a company to change a name registered on misleading information or an unfulfilled undertaking | the company: liable to the direction | power / liability | `s 75(1) the Secretary of State may direct the company to change its name` |
| s 75(2) | the company: entitled to a direction within five years, in writing, specifying a period of at least 28 days | Secretary of State | claim / duty | `s 75(2)(a) the direction is given within five years of the company's registration by that name`; `s 75(2)(b) the direction specifies the period` |
| s 75(3) | Secretary of State: may extend the period by a further direction | the company: liable | power / liability | `s 75(3) the Secretary of State may give a further direction extending the period` |
| s 75(4A) | the registrar: may omit the former name from the register available for public inspection | none named | power / liability | `s 75(4A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 75(5) | the State (the text makes the act an offence; it names no prosecutor) | the company; every officer in default; a shadow director (treated as an officer): liable for failing to comply | claim / duty; power / liability | `s 75(5) the company's duty to change its name as directed`; `s 75(5) the person commits an offence` |
| s 75(6) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction | power / liability | `s 75(6) the penalty on summary conviction` |
| s 76(1) | Secretary of State: may direct a company to change a name that gives so misleading an indication of its activities as to pose a risk of harm | the company: liable to the direction | power / liability | `s 76(1) the Secretary of State may direct the company to change its name` |
| s 76(2) | the company: entitled to a direction in writing, specifying the period and the right to apply to the court | Secretary of State | claim / duty | `s 76(2) the direction meets the requirements of subsection (2)` |
| s 76(3) | the company: entitled to a period of at least 28 days | Secretary of State | claim / duty | `s 76(3) the period meets the requirement of subsection (3)` |
| s 76(3A) | Secretary of State: may extend the period by a further direction | the company: liable | power / liability | `s 76(3A) the Secretary of State may give a further direction extending the period` |
| s 76(4) | the company: may apply to the court to set the direction aside (within three weeks beginning with its date, s 76(4A)) | Secretary of State: liable to the application | power / liability | `s 76(4) the company may apply to the court to set the direction aside` |
| s 76(5) | the court: may set the direction aside or confirm it, and must then specify the period | the company and Secretary of State: liable | power / liability | `s 76(5) the court may set the direction aside or confirm it`; `s 76(5) the court must specify the period within which the direction is to be complied with` |
| s 76(5A) | the company: not required to comply while the proceedings are ongoing | Secretary of State: cannot require compliance meanwhile | immunity / disability | `s 76(5A) the company is not required to comply with the direction while the proceedings are ongoing` |
| s 76(5B) | the registrar: may omit the former name from the register available for public inspection | none named | power / liability | `s 76(5B) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` |
| s 76(6) | the State (the text makes the act an offence; it names no prosecutor) | the company; every officer in default; a shadow director (treated as an officer): liable for failing to comply | claim / duty; power / liability | `s 76(6) the company's duty to change its name as directed`; `s 76(6) the person commits an offence` |
| s 76(7) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction | power / liability | `s 76(7) the penalty on summary conviction` |
| s 76A | as s 76: Secretary of State power to direct (dishonesty or deception), company's power to apply to court, court power, company's immunity meanwhile, offence and penalty (76A(11) and (12)) | as s 76: company liable; company and officers duty and liability | as s 76 | `s 76A(1) the Secretary of State may direct the company to change its name`; `s 76A(2) the direction meets the requirements of subsection (2)`; +11 more |
| s 76B | as s 76: Secretary of State power to direct (registration in contravention of Part 5), company's power to apply to court, court power, company's immunity meanwhile, offence and penalty (76B(11) and (12)) | as s 76: company liable; company and officers duty and liability | as s 76 | `s 76B(1) the Secretary of State may direct the company to change its name`; `s 76B(2) the direction meets the requirements of subsection (2)`; +11 more |
| s 76C | the registrar: may determine a new name for a company whose name includes computer code | the company: liable; (2) the company is entitled to notice | power / liability; claim / duty | `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register`; `s 76C(2)(a) the registrar must give the company notice of the determination`; +3 more |
| s 76D | the registrar: may determine a new name for a company that failed to comply with a direction | the company: liable; (3) the company is entitled to notice | power / liability; claim / duty | `s 76D(2) the direction is one referred to in subsection (1)`; `s 76D(1) the registrar may determine a new name for the company`; +2 more |
| s 76E | Secretary of State: may disapply Part 5 so that a name is registered for national security or to prevent or detect serious crime | none named | power / liability | `s 76E(2)(a) the conduct is crime`; `s 76E(2)(b) the crime is serious`; +1 more |
| s 77 | the company: may change its name by special resolution or by other means in its articles | none named | privilege / no-right | `s 77(1) the company may change its name in that way`; `s 77(2) the name of the company may also be changed in that way` |
| s 78 | the registrar: to be given notice (with the resolution) of a change of name by special resolution, and notice when a condition is met | the company: must give notice | claim / duty | `s 78(1) the company must give notice to the registrar`; `s 78(2)(a) the notice must specify that the change is conditional`; +4 more |
| s 79 | the registrar: to be given notice of a change of name by means in the articles, with a statement | the company: must give notice | claim / duty | `s 79(1)(a) the company must give notice to the registrar`; `s 79(1)(b) the notice must be accompanied by a statement that the change of name has been made by means provided for by the company's articles`; +1 more |
| s 80 | the company: to have the new name entered on the register and a new certificate issued | the registrar: must enter the name and issue the certificate | claim / duty | `s 80(1) this section applies`; `s 80(2) the registrar must enter the new name on the register in place of the former name`; +1 more |
| s 81 | the company and everyone dealing with it: rights, obligations and legal proceedings are unaffected by the change of name | none named | immunity / disability | `s 81(1) the change of name has effect on the day`; `s 81(2) the change of name affects the right, the obligation or the proceedings`; +1 more |
| s 82 | none: power to make regulations (machinery) | - | none | (none: no relation) |
| s 83 | a person against whom a company claimant brings proceedings arising from a contract made while the company was in breach of the disclosure regulations: may have the proceedings dismissed | the company claimant: liable to dismissal (unless the court permits the proceedings to continue) | power / liability | `s 83(1) this section applies to the proceedings`; `s 83(2) the proceedings shall be dismissed`; +1 more |
| s 84 | none: power to make regulations (machinery) | - | none | (none: no relation) |
| s 85 | none: a rule of reading (which differences between names are left out of account) | - | none | (none: no relation) |
| s 86(1) | none named in the text | the company: must ensure its registered office is at an appropriate address | claim of none named / duty | `s 86(1) the company must ensure that its registered office is at an appropriate address` |
| s 86(2) | none: definition of "appropriate address" | - | none | (none: no relation) |
| s 86(3) | the State (the text makes the act an offence; it names no prosecutor) | the company and every officer in default: liable for failing without reasonable excuse (no shadow-director sentence: fork 7) | claim / duty; power / liability | `s 86(3) the person commits an offence` |
| s 86(4) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction | power / liability | `s 86(4) the penalty on summary conviction` |
| s 87(1) | the company: may change the address of its registered office by notice to the registrar | none named | privilege / no-right | `s 87(1) the company may change the address of its registered office` |
| s 87(2) | anyone serving a document: may validly serve it at the previously registered address for 14 days | the company: cannot object to that service | privilege / no-right | `s 87(2) the change takes effect on the day`; `s 87(2) a person may validly serve a document on the company at the address previously registered on the day` |
| s 87(3) | the company: may act on the change from the date of notice, within 14 days | none named | privilege / no-right | `s 87(3) the company may act on the change as from that date` |
| s 87(4) | the company: protected from being treated as in breach if it unavoidably ceased to perform a duty at its registered office and resumed and gave notice within 14 days | none named | immunity / disability | `s 87(4) the company is protected from being treated as having failed to comply with the duty` |
| s 88(1) | none: definition of "Welsh company" | - | none | (none: no relation) |
| s 88(2) | a company with its office in Wales and an England and Wales entry: may require the register to say Wales by special resolution | none named | power / liability | `s 88(2) the company may by special resolution require the register to state that its registered office is to be situated in Wales` |
| s 88(3) | a company with its office in Wales and a Wales entry: may require the register to say England and Wales by special resolution | none named | power / liability | `s 88(3) the company may by special resolution require the register to state that its registered office is to be situated in England and Wales` |
| s 88(4) | the registrar: to be given notice; the company is entitled to the amended register and a new certificate | the company: must give notice; the registrar: must amend and issue | claim / duty | `s 88(4) the company must give notice to the registrar`; `s 88(4)(a) the registrar must amend the register accordingly`; +1 more |
| s 88A(1) | none named in the text | the company: must ensure its registered email address is appropriate | claim of none named / duty | `s 88A(1) the company must ensure that its registered email address is an appropriate email address` |
| s 88A(2) | none: definition of "appropriate email address" | - | none | (none: no relation) |
| s 88A(3) | the State (the text makes the act an offence; it names no prosecutor) | the company and every officer in default: liable for failing without reasonable excuse (no shadow-director sentence: fork 7) | claim / duty; power / liability | `s 88A(3) the person commits an offence` |
| s 88A(4) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction | power / liability | `s 88A(4) the penalty on summary conviction` |
| s 88B | the company: may change its registered email address by notice; the change takes effect on registration | none named | privilege / no-right | `s 88B(1) the company may change its registered email address`; `s 88B(2) the notice must include a statement that the new address is an appropriate email address within the meaning given by section 88A(2)`; +1 more |
| s 89 | a company: may alter its status in the five ways listed by re-registration under Part 7 | the registrar: liable to re-register | power / liability | `s 89 the company may by re-registration under Part 7 alter its status in that way` |
| s 90 | a private company: may be re-registered as a public company limited by shares, if the conditions are met | the registrar: must re-register; the company: must change its name and articles (90(3), (4)) | power / liability; claim / duty | `s 90(1) all of the answers hold`; `s 90(2) the conditions are met`; +4 more |
| s 91 | none named in the text | a private company: cannot be re-registered as public unless the share capital requirements are met (a bar) | disability | `s 91(1)(a) the nominal value of the allotted share capital is not less than the authorised minimum`; `s 91(1)(b) the allotment is paid up as the paragraph requires`; +8 more |
| s 92 | none named in the text | a private company: cannot be re-registered as public without the balance sheet, the unqualified report, the auditor's statement and no adverse change (a bar) | disability | `s 92(1)(a) the balance sheet is prepared as at a date not more than seven months before the application is delivered`; `s 92(5) a qualification is material`; +8 more |
| s 93 | none named in the text | the registrar: shall not entertain the application unless a valuation, share exchange or merger route is met (a bar on the registrar) | disability | `s 93(1) section 93 applies (recent allotment of shares for non-cash consideration)`; `s 93(7)(b) the thing is an arrangement`; +7 more |
| s 94 | the registrar: to receive the application with the stated contents and documents | the company: must provide them | claim / duty | `s 94(1) the application contains what the subsection requires`; `s 94(2) the application is accompanied by what the subsection requires`; +2 more |
| s 95 | the registrar: to receive the statement of the proposed secretary with the company's statement of consent | the company: must provide it | claim / duty | `s 95(1) the statement of the company's proposed secretary contains the required information`; `s 95(3) the statement of the proposed secretary includes the company's statement of consent`; +1 more |
| s 96 | the company: to be re-registered as public, to receive a certificate, and to have the certificate conclusive of compliance | the registrar: must re-register and issue the certificate; anyone challenging: disability | claim / duty; immunity / disability | `s 96(1) the company shall be re-registered as a public company`; `s 96(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +5 more |
| s 97 | a public company: may be re-registered as a private limited company if the conditions are met | the registrar: liable to re-register | power / liability | `s 97(1) all of the answers hold`; `s 97(2) the conditions are met`; +3 more |
| s 98(1) | holders of at least 5% in nominal value of the issued share capital or of a class; if the company is not limited by shares, at least 5% of its members; or at least 50 members: may apply to the court to cancel the resolution (not a person who consented to or voted for it) | the company: liable to the application | power / liability | `s 98(1) the applicants may apply to the court for the cancellation of the resolution` |
| s 98(2) | the applicants: may apply within 28 days after the resolution is passed | the company | power / liability | `s 98(2) the application is made within 28 days after the passing of the resolution`; `s 98(2) the members' permission to apply to the court`; +1 more |
| s 98(3) | the court: must make an order cancelling or confirming the resolution | the applicants and the company: liable | power / liability | `s 98(3) the court shall make an order either cancelling or confirming the resolution` |
| s 98(4) | the court: may make the order on terms, adjourn, and give directions | the parties: liable | power / liability | `s 98(4) the court may make the order on terms, adjourn for the purchase of dissentient members' interests, and give directions` |
| s 98(5) | the court: may provide for the purchase of members' shares and alter the articles | the company and the members: liable | power / liability | `s 98(5) the court's order may provide for the purchase by the company of members' shares and alter the articles` |
| s 98(6) | the court: may require the company not to amend its articles without leave | the company: disability | power / disability | `s 98(6) the court's order may require the company not to amend its articles without the leave of the court` |
| s 98(7) | none: definition of "the court" (fork 6) | - | none | (none: no relation) |
| s 99(1) | the registrar: to be told at once of an application under s 98 | the applicants (or the person applying for them): must give notice immediately (fork 8) | claim / duty | `s 99(1) the applicants must immediately give notice to the registrar` |
| s 99(2) | the registrar: to be told at once by the company served with notice | the company: must give notice immediately (fork 8) | claim / duty | `s 99(2) the company must immediately give notice to the registrar` |
| s 99(3) | the registrar: to receive a copy of the order within 15 days (or the longer period the court directs) | the company: must deliver it | claim / duty | `s 99(3) the number of days allowed for delivering a copy of the order`; `s 99(3) the copy of the order is delivered within the time allowed`; +1 more |
| s 99(4) | the State (the text makes the act an offence; it names no prosecutor) | the company and every officer in default: liable for failing to comply with s 99(2) or (3) (no shadow-director sentence: fork 7) | claim / duty; power / liability | `s 99(4) the person commits an offence` |
| s 99(5) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction | power / liability | `s 99(5) the penalty on summary conviction` |
| s 100 | the registrar: to receive the application with the documents and the statement of compliance, and may accept the statement as sufficient evidence | the company: must provide them; liable to acceptance | claim / duty; power / liability | `s 100(1) the application contains what the subsection requires`; `s 100(2) the application is accompanied by what the subsection requires`; +2 more |
| s 101 | the company: to be re-registered as a private limited company and to receive a certificate (conclusive evidence of compliance) | the registrar: must re-register and issue it; anyone challenging: disability | claim / duty; immunity / disability | `s 101(1) the company shall be re-registered as a private limited company`; `s 101(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more |
| s 102(1) | a private limited company: may be re-registered as unlimited if all the members assent | the registrar: liable to re-register | power / liability | `s 102(1) all of the answers hold`; `s 102(1)(a) all the members of the company have assented`; +1 more |
| s 102(4) | each member (a trustee in bankruptcy for a bankrupt member; a personal representative for a deceased member): may assent | the company: cannot re-register without the assent | power / liability | `s 102(4) the member's assent is given` |
| s 102(5) | none: "a trustee in bankruptcy of a member" includes the listed office holders | - | none | (none: no relation) |
| s 103 | the registrar: to receive the application, the prescribed form of assent authenticated by or for all the members, the articles and the statement of compliance with the directors' statement | the company and its directors: must provide them | claim / duty | `s 103(1) the application contains what the subsection requires`; `s 103(2) the application is accompanied by what the subsection requires`; +3 more |
| s 104 | the company: to be re-registered as unlimited, with a certificate (conclusive evidence) | the registrar: must re-register and issue it; anyone challenging: disability | claim / duty; immunity / disability | `s 104(1) the company shall be re-registered as an unlimited company`; `s 104(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more |
| s 105 | an unlimited company: may be re-registered as a private limited company by special resolution | the registrar: liable to re-register | power / liability | `s 105(2) the condition is met`; `s 105(1) the unlimited company may be re-registered as a private limited company`; +3 more |
| s 106 | the registrar: to receive the application with the documents (and, for a guarantee company, a statement of guarantee); the statement must record each member's undertaking to contribute to the company's assets if it is wound up while he is a member or within one year after (the text names no one who may call on it) | the company: must provide them; each member of a guarantee company: bound by the undertaking | claim / duty | `s 106(1) the application contains what the subsection requires`; `s 106(2) the application is accompanied by what the subsection requires`; +4 more |
| s 107 | the company: to be re-registered as limited, with a certificate (conclusive evidence) | the registrar: must re-register and issue it; anyone challenging: disability | claim / duty; immunity / disability | `s 107(1) the company shall be re-registered as a limited company`; `s 107(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more |
| s 108(1) | the registrar: to receive a statement of capital within 15 days after re-registration (unless already sent) | the company: must deliver it | claim / duty | `s 108(1) the company must deliver a statement of capital to the registrar`; `s 108(1) the statement of capital is delivered within 15 days after the re-registration`; +1 more |
| s 108(3) | none: contents of the statement of capital | - | none | (none: no relation) |
| s 108(4) | the State (the text makes the act an offence; it names no prosecutor) | the company and every officer in default: liable for default (no shadow-director sentence: fork 7) | claim / duty; power / liability | `s 108(4) the person commits an offence` |
| s 108(5) | the State (the text makes the act an offence; it names no prosecutor) | the person guilty: liable on summary conviction | power / liability | `s 108(5) the penalty on summary conviction` |
| s 109 | a public company limited by shares: may be re-registered as unlimited if all the members assent | the registrar: liable to re-register | power / liability | `s 109(5) the person is a trustee in bankruptcy of a member of the company`; `s 109(4) the member's assent is given`; +5 more |
| s 109(4) | each member (a trustee in bankruptcy, a personal representative): may assent | the company | power / liability | `s 109(4) the member's assent is given` |
| s 109(5) | none: "a trustee in bankruptcy of a member" includes the listed office holders | - | none | (none: no relation) |
| s 110 | the registrar: to receive the application with the prescribed form of assent, the articles and the statement of compliance | the company and its directors: must provide them | claim / duty | `s 110(1) the application contains what the subsection requires`; `s 110(2) the application is accompanied by what the subsection requires`; +3 more |
| s 111 | the company: to be re-registered as an unlimited private company, with a certificate (conclusive evidence) | the registrar: must re-register and issue it; anyone challenging: disability | claim / duty; immunity / disability | `s 111(1) the company shall be re-registered as an unlimited private company`; `s 111(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case`; +4 more |

## Marginal readings for a lawyer (coa2)

The brief marks two readings "for a lawyer, not for you to decide", and asks that they be taken as the status quo and that every branch resting on one be listed here, with the other reading stated:

- **(a)** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no.
- **(b)** a prohibition or grant limited by its own wording does not say no outside the limit.

Each row below is one function and the branches of it that rest on (a) or (b).
The branch is quoted from its `FALSE-kind` or `NOTHING-kind` comment.
**Other reading**, for every `(a)` branch: the answer is `NOTHING`, because the text does not itself say no.
**Other reading**, for every `(b)` branch: the answer is `JUST FALSE`, because the limit is read as a general no outside it.
Branches that answer `NOTHING` for another reason (silent, list not closed, includes, undefined term, points outside the text) are not lawyer readings and are not listed.

| module | function | branches resting on a lawyer reading |
| --- | --- | --- |
| `ch1-prohibited-names` | `s 53 the company may be registered by the name` | (a) flat negative: "A company must not be registered under this Act by a name if, in the opinion of the Secretary of Sta..."<br>(b) limited by its own wording: "the prohibition names only the cases in (a) and (b)" |
| `ch1-prohibited-names` | `s 53A the company may be registered by the name` | (a) flat negative: "A company must not be registered under this Act by a name if, in the opinion of the Secretary of Sta..."<br>(b) limited by its own wording: "the prohibition names only the cases in (a) and (b)" |
| `ch1-prohibited-names` | `s 54(1) the approval of the Secretary of State is required` | (b) limited by its own wording: "a name that would be likely to give the impression that the company is connected with" |
| `ch1-prohibited-names` | `s 55(1) the approval of the Secretary of State is required` | (b) limited by its own wording: "a name that includes a word or expression for the time being specified in regulations" |
| `ch1-prohibited-names` | `s 56(2) the applicant must request the specified department or body in writing to indicate whether and why it has any objections` | (a) failed "if" or "where": "Where such a requirement applies, the applicant must request" |
| `ch1-prohibited-names` | `s 56(3)(a) the application must include a statement that a request under this section has been made` | (a) failed "if" or "where": "Where a request under this section is made in connection with an application for the registration of..." |
| `ch1-prohibited-names` | `s 56(3)(b) the application must be accompanied by a copy of the response received` | (a) failed "if" or "where": "Where a request under this section is made ... the application must ... be accompanied by a copy of ..." |
| `ch1-prohibited-names` | `s 56(4)(a) the notice of the change must be accompanied by a statement by a director or secretary that a request has been made` | (a) failed "if" or "where": "Where a request under this section is made in connection with a change in a company's name, the noti..." |
| `ch1-prohibited-names` | `s 56(4)(b) the notice of the change must be accompanied by a copy of the response received` | (a) failed "if" or "where": "Where a request under this section is made in connection with a change in a company's name, the noti..." |
| `ch1-prohibited-names` | `s 56A the company may be registered by the name` | (a) flat negative: "A company must not be registered under this Act by a name that, in the opinion of the Secretary of S..."<br>(b) limited by its own wording: "the prohibition names only a name that in the Secretary of State's opinion would be likely to give t..." |
| `ch1-prohibited-names` | `s 57(3) the company may be registered by the name` | (a) flat negative: "A company may not be registered under this Act by a name that consists of or includes anything that ..."<br>(b) limited by its own wording: "the prohibition names only a name that consists of or includes something the regulations do not perm..." |
| `ch1-prohibited-names` | `s 57A the company may be registered by the name` | (a) flat negative: "A company must not be registered under this Act by a name that, in the opinion of the Secretary of S..."<br>(b) limited by its own wording: "the prohibition names only a name that in the Secretary of State's opinion consists of or includes c..." |
| `ch1-prohibited-names` | `s 57B(2) subsection (1) does not prevent registration of the company by the name` | (b) limited by its own wording: "any name approved by the Secretary of State" |
| `ch1-prohibited-names` | `s 57B(1) the company may be registered by the name` | (a) flat negative: "the company must not subsequently be registered under this Act by the original name or a name that i..."<br>(b) limited by its own wording: "Where a company’s name has at any time been changed following a direction ... or an order" |
| `ch1-prohibited-names` | `s 57C(4) the person has a relevant relationship with the company` | (a) failed "if" or "where": "a person has a “relevant relationship” with a company if the person is— (a) an officer, or (b) a mem..." |
| `ch1-prohibited-names` | `s 57C(3) it matters whether the relationships coincided in time` | (a) failed "if" or "where": "it is irrelevant whether the person has, or has had, a relevant relationship with both companies at ..." |
| `ch1-prohibited-names` | `s 57C(2) subsection (1) does not prevent registration of the company by the name` | (b) limited by its own wording: "any name approved by the Secretary of State" |
| `ch1-prohibited-names` | `s 57C(1) the other company may be registered by the name` | (a) failed "if" or "where": "no other company may be registered under this Act by that name or a name that is similar if"<br>(b) limited by its own wording: "the prohibition names only the cases in (a) and (b), and only that name or a similar one" |
| `ch2-company-type` | `s 58(1) the name of the company must end with public limited company or p.l.c.` | (a) flat negative: "This section does not apply to community interest companies"<br>(b) limited by its own wording: "The name of a limited company that is a public company" |
| `ch2-company-type` | `s 58(1) the name of the company ends as the section requires` | (a) failed "if" or "where": "must end with “public limited company” or “p.l.c.”"<br>(b) limited by its own wording: "the section does not apply, so it says nothing about the name" |
| `ch2-company-type` | `s 59(1) the name of the company must end with limited or ltd.` | (a) flat negative: "This section does not apply to community interest companies"<br>(b) limited by its own wording: "The name of a limited company that is a private company"<br>(a) failed "if" or "where": "Certain companies are exempt from this requirement (see section 60)" |
| `ch2-company-type` | `s 59(1) the name of the company ends as the section requires` | (a) failed "if" or "where": "must end with “limited” or “ltd.”"<br>(b) limited by its own wording: "the section does not apply, so it says nothing about the name" |
| `ch2-company-type` | `s 61(1) the section applies to the company` | (b) limited by its own wording: "This section applies to a private company limited by shares" |
| `ch2-company-type` | `s 61(3) the first condition is met` | (a) failed "if" or "where": "The first condition is that the objects of the company are" |
| `ch2-company-type` | `s 61(4) the second condition is met` | (a) failed "if" or "where": "The second condition is that the company's articles— (a) ... (b) ... and (c) ..." |
| `ch2-company-type` | `s 61(2) the company is exempt from section 59` | (a) flat negative: "is exempt from section 59 ... so long as— (a) it continues to meet the following two conditions, and..."<br>(b) limited by its own wording: "A company to which this section applies" |
| `ch2-company-type` | `s 62(2) the first condition is met` | (a) failed "if" or "where": "the first condition ... that the objects of the company are" |
| `ch2-company-type` | `s 62(3) the second condition is met` | (a) failed "if" or "where": "the second condition is that the company's articles— (a) ... (b) ... and (c) ..." |
| `ch2-company-type` | `s 62(1) the company is exempt from section 59` | (a) flat negative: "is exempt from section 59 ... so long as it continues to meet the following two conditions and does ..."<br>(b) limited by its own wording: "A private company limited by guarantee that immediately before the commencement of this Part" |
| `ch2-company-type` | `s 60(1) the private company is exempt from section 59` | (b) limited by its own wording: "A private company is exempt"<br>(a) failed "if" or "where": "A private company is exempt from section 59 ... if— (a) it is a charity, (b) it is exempted ... by r..." |
| `ch2-company-type` | `s 60(2) the registrar may refuse to register the company by the name` | (b) limited by its own wording: "a private limited company by a name that does not include the word “limited” (or a permitted alterna..."<br>(a) failed "if" or "where": "unless a statement has been delivered to him that the company meets the conditions for exemption" |
| `ch2-company-type` | `s 60(3) the registrar may accept the statement as sufficient evidence of the matters stated in it` | (b) limited by its own wording: "The registrar may accept the statement" |
| `ch2-company-type` | `s 63(1) the company may amend its articles as proposed` | (a) flat negative: "must not amend its articles so that it ceases to comply with the conditions for exemption under that..."<br>(b) limited by its own wording: "the prohibition names only a company within (a) and (b), and only an amendment that ceases to comply" |
| `ch2-company-type` | `s 63(2) the person commits an offence` | (a) failed "if" or "where": "If subsection (1) above is contravened an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `ch2-company-type` | `s 64(1) the Secretary of State may direct the company to change its name` | (b) limited by its own wording: "If it appears to the Secretary of State that a company whose name does not include “limited” or any ..." [fork 10: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch2-company-type` | `s 64(2) the direction meets the requirements of subsection (2)` | (a) failed "if" or "where": "The direction must be in writing and must specify the period" |
| `ch2-company-type` | `s 64(2A) the period meets the requirement of subsection (2A)` | (a) failed "if" or "where": "The period must be a period of at least 28 days beginning with the date of the direction" |
| `ch2-company-type` | `s 64(2B) the Secretary of State may give a further direction extending the period` | (b) limited by its own wording: "by further direction in writing" [fork 18: the other reading is JUST FALSE, a failed "if" read as the text's own no]<br>(a) failed "if" or "where": "Any such direction must be given before the end of the period for the time being specified" |
| `ch2-company-type` | `s 64(3) the company may change its name by resolution of the directors` | (b) limited by its own wording: "A change of name in order to comply with a direction under this section" |
| `ch2-company-type` | `s 64(4) the company must give notice to the registrar of the change` | (a) failed "if" or "where": "Where a resolution of the directors is passed in accordance with subsection (3), the company must gi..." |
| `ch2-company-type` | `s 64(5) the person commits an offence` | (a) failed "if" or "where": "If the company fails to comply with a direction under this section an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `ch2-company-type` | `s 64(6A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | (a) failed "if" or "where": "Where a direction is given under subsection (1), the registrar may omit" |
| `ch2-company-type` | `s 64(7) the approval of the Secretary of State is required for the change of name` | (b) limited by its own wording: "A company that has been directed to change its name under this section may not ... subsequently chan..."<br>(a) flat negative: "This does not apply to a change of name on re-registration or on conversion to a community interest ..." |
| `ch2-company-type` | `s 65(3) the company may be registered by the name` | (a) flat negative: "A company must not be registered under this Act by a name that consists of or includes anything proh..."<br>(b) limited by its own wording: "the prohibition names only a name that consists of or includes something the regulations prohibit" |
| `ch3-similarity` | `s 66(1) the company may be registered by the name` | (a) flat negative: "A company must not be registered under this Act by a name that is the same as another name appearing..."<br>(b) limited by its own wording: "the prohibition names only a name that is the same as another name in the index" |
| `ch3-similarity` | `s 67(1) the Secretary of State may direct the company to change its name` | (b) limited by its own wording: "The Secretary of State may direct a company to change its name if it has been registered in a name t..." [fork 11: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch3-similarity` | `s 67(1A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | (a) failed "if" or "where": "Where a direction is given under subsection (1), the registrar may omit" |
| `ch3-similarity` | `s 68(2)(a) the direction is given within twelve months of the company's registration by the name` | (a) failed "if" or "where": "must be given within twelve months of the company's registration by the name in question" |
| `ch3-similarity` | `s 68(2)(b) the direction specifies the period` | (a) failed "if" or "where": "must specify the period within which the company is to change its name" |
| `ch3-similarity` | `s 68(2A) the period meets the requirement of subsection (2A)` | (a) failed "if" or "where": "The period must be a period of at least 28 days beginning with the date of the direction" |
| `ch3-similarity` | `s 68(3) the Secretary of State may give a further direction extending the period` | (a) failed "if" or "where": "Any such direction must be given before the end of the period for the time being specified" |
| `ch3-similarity` | `s 68(4) the direction meets the requirement of being in writing` | (a) failed "if" or "where": "A direction under section 67 or this section must be in writing" |
| `ch3-similarity` | `s 68(5) the person commits an offence` | (a) failed "if" or "where": "If a company fails to comply with the direction, an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `ch3-similarity` | `s 69(1) the applicant may object to the company's registered name` | (b) limited by its own wording: "A person (“the applicant”) may object to a company's registered name on the ground— (a) ... or (b) ...." |
| `ch3-similarity` | `s 69(2) the objection is made as the subsection requires` | (a) failed "if" or "where": "The objection must be made by application to a company names adjudicator" |
| `ch3-similarity` | `s 69(4) the objection is upheld under subsection (4)` | (a) failed "if" or "where": "If the ground specified in subsection (1)(a) or (b) is established, it is for the respondents to sho..."<br>(a) failed "if" or "where": "If none of those is shown, the objection shall be upheld." |
| `ch3-similarity` | `s 69(5) the objection is nevertheless upheld` | (a) failed "if" or "where": "If the facts mentioned in subsection (4)(a) ... or (c) are established, the objection shall neverthe..." |
| `ch3-similarity` | `s 69(6) the objection is dismissed` | (a) flat negative: "If the objection is not upheld under subsection (4) or (5), it shall be dismissed." |
| `ch3-similarity` | `s 72(1) the decision was made available within 90 days of the determination` | (a) failed "if" or "where": "must, within 90 days of determining an application under section 69, make his decision and his reaso..." |
| `ch3-similarity` | `s 72(2) the adjudicator may make the decision available by the means` | (b) limited by its own wording: "He may do so by means of a website or by such other means as appear to him to be appropriate" |
| `ch3-similarity` | `s 73(1) the adjudicator must make an order` | (a) failed "if" or "where": "If an application under section 69 is upheld, the adjudicator shall make an order" |
| `ch3-similarity` | `s 73(1)(a) the order requires the person to change its name to one that is not an offending name` | (b) limited by its own wording: "requiring the respondent company to change its name" |
| `ch3-similarity` | `s 73(1)(b) the order requires the person to take the steps and not to cause or permit steps towards another offending name` | (b) limited by its own wording: "requiring all the respondents" |
| `ch3-similarity` | `s 73(3) the order meets the requirement to specify a date` | (a) failed "if" or "where": "The order must specify a date by which the respondent company's name is to be changed" |
| `ch3-similarity` | `s 73(6) the name is changed in accordance with the order by the specified date` | (a) failed "if" or "where": "a company's name is changed when the change takes effect in accordance with section 81(1) (on the is..."<br>(a) flat negative: "is not changed in accordance with the order by the specified date" |
| `ch3-similarity` | `s 73(4) the adjudicator may determine a new name for the company` | (b) limited by its own wording: "If the respondent company's name is not changed in accordance with the order by the specified date, ..." [fork 12: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch3-similarity` | `s 73(5) the adjudicator must give notice of his determination to the recipient` | (a) failed "if" or "where": "If the adjudicator determines a new name for the respondent company he must give notice of his deter..." |
| `ch3-similarity` | `s 73(7) the registrar may omit from the register material available for public inspection any mention of the name to which the order relates` | (a) failed "if" or "where": "Where an order is made under subsection (1), the registrar may omit" |
| `ch3-similarity` | `s 74(1) an appeal lies to the court from the decision` | (b) limited by its own wording: "from any decision of a company names adjudicator to uphold or dismiss an application under section 6..." |
| `ch3-similarity` | `s 74(2) notice of appeal is given in time` | (b) limited by its own wording: "Notice of appeal against a decision upholding an application"<br>(a) failed "if" or "where": "must be given before the date specified in the adjudicator's order" |
| `ch3-similarity` | `s 74(3) the effect of the adjudicator's order is suspended` | (a) failed "if" or "where": "If notice of appeal is given against a decision upholding an application, the effect of the adjudica..." |
| `ch3-similarity` | `s 74(4) the court may specify the date, remit the matter or make any order or determination that the adjudicator might have made` | (b) limited by its own wording: "If on appeal the court— (a) affirms ... or (b) reverses ... the court may" [fork 13: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch3-similarity` | `s 74(5) the court must give notice of the determination to the recipient` | (a) failed "if" or "where": "If the court determines a new name for the company it must give notice of the determination" |
| `ch4-other-powers` | `s 75(1) the Secretary of State may direct the company to change its name` | (b) limited by its own wording: "If it appears to the Secretary of State— (a) ... or (b) ..., the Secretary of State may direct the c..." [fork 14: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch4-other-powers` | `s 75(2)(a) the direction is given within five years of the company's registration by that name` | (a) failed "if" or "where": "must be given within five years of the company's registration by that name" |
| `ch4-other-powers` | `s 75(2)(b) the direction specifies the period` | (a) failed "if" or "where": "must specify the period within which the company is to change its name" |
| `ch4-other-powers` | `s 75(2A) the period meets the requirement of subsection (2A)` | (a) failed "if" or "where": "The period must be at least 28 days beginning with the date of the direction" |
| `ch4-other-powers` | `s 75(3) the Secretary of State may give a further direction extending the period` | (a) failed "if" or "where": "Any such direction must be given before the end of the period for the time being specified" |
| `ch4-other-powers` | `s 75(4) the direction meets the requirement of being in writing` | (a) failed "if" or "where": "A direction under this section must be in writing" |
| `ch4-other-powers` | `s 75(4A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | (a) failed "if" or "where": "Where a direction is given under subsection (1), the registrar may omit" |
| `ch4-other-powers` | `s 75(5) the person commits an offence` | (a) failed "if" or "where": "If a company fails to comply with a direction under this section, an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `ch4-other-powers` | `s 76(1) the Secretary of State may direct the company to change its name` | (b) limited by its own wording: "If in the opinion of the Secretary of State the name by which a company is registered gives so misle..." [fork 15: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch4-other-powers` | `s 76(2) the direction meets the requirements of subsection (2)` | (a) failed "if" or "where": "The direction must be in writing and must specify the period within which the company is to change i..." |
| `ch4-other-powers` | `s 76(3) the period meets the requirement of subsection (3)` | (a) failed "if" or "where": "The period must be a period of at least 28 days beginning with the date of the direction" |
| `ch4-other-powers` | `s 76(3A) the Secretary of State may give a further direction extending the period` | (b) limited by its own wording: "by further direction in writing" [fork 19: the other reading is JUST FALSE, a failed "if" read as the text's own no]<br>(a) failed "if" or "where": "Any such direction must be given before the end of the period for the time being specified" |
| `ch4-other-powers` | `s 76(4) the company may apply to the court to set the direction aside` | (b) limited by its own wording: "to set aside a direction under subsection (1)" |
| `ch4-other-powers` | `s 76(4A) the application is made in time` | (a) failed "if" or "where": "must be made within the period of three weeks beginning with the date of the direction" |
| `ch4-other-powers` | `s 76(5) the court may set the direction aside or confirm it` | (b) limited by its own wording: "the power is given on an application under the preceding subsection" |
| `ch4-other-powers` | `s 76(5) the court must specify the period within which the direction is to be complied with` | (a) failed "if" or "where": "If the direction is confirmed, the court shall specify the period within which the direction is to b..." |
| `ch4-other-powers` | `s 76(5A) the company is not required to comply with the direction while the proceedings are ongoing` | (a) flat negative: "If a company applies to the court ... to set aside a direction, it is not required to comply with th..." |
| `ch4-other-powers` | `s 76(5B) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | (a) failed "if" or "where": "Where a direction is given under subsection (1), the registrar may omit" |
| `ch4-other-powers` | `s 76(6) the person commits an offence` | (a) failed "if" or "where": "If a company fails to comply with a direction under subsection (1), an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `ch4-other-powers` | `s 76A(1) the Secretary of State may direct the company to change its name` | (b) limited by its own wording: "The Secretary of State may direct a company to change its name if it appears to the Secretary of Sta..." [fork 16: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch4-other-powers` | `s 76A(2) the direction meets the requirements of subsection (2)` | (a) failed "if" or "where": "The direction must be in writing and must specify the period within which the company is to change i..." |
| `ch4-other-powers` | `s 76A(3) the period meets the requirement of subsection (3)` | (a) failed "if" or "where": "The period must be a period of at least 28 days beginning with the date of the direction" |
| `ch4-other-powers` | `s 76A(4) the Secretary of State may give a further direction extending the period` | (b) limited by its own wording: "by further direction in writing" [fork 20: the other reading is JUST FALSE, a failed "if" read as the text's own no]<br>(a) failed "if" or "where": "Any such direction must be given before the end of the period for the time being specified" |
| `ch4-other-powers` | `s 76A(5) the company may apply to the court to set the direction aside` | (b) limited by its own wording: "to set aside a direction under subsection (1)" |
| `ch4-other-powers` | `s 76A(6) the application is made in time` | (a) failed "if" or "where": "must be made within the period of three weeks beginning with the date of the direction" |
| `ch4-other-powers` | `s 76A(7) the court may set the direction aside or confirm it` | (b) limited by its own wording: "the power is given on an application under the preceding subsection" |
| `ch4-other-powers` | `s 76A(8) the court must specify the period within which the direction is to be complied with` | (a) failed "if" or "where": "If on an application under subsection (5) the direction is confirmed, the court must specify the per..." |
| `ch4-other-powers` | `s 76A(10) the company is not required to comply with the direction while the proceedings are ongoing` | (a) flat negative: "If a company applies to the court ... to set aside a direction, it is not required to comply with th..." |
| `ch4-other-powers` | `s 76A(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | (a) failed "if" or "where": "Where a direction is given under subsection (1), the registrar may omit" |
| `ch4-other-powers` | `s 76A(11) the person commits an offence` | (a) failed "if" or "where": "If a company fails to comply with a direction under subsection (1), an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `ch4-other-powers` | `s 76B(1) the Secretary of State may direct the company to change its name` | (b) limited by its own wording: "The Secretary of State may direct a company to change its name if— (a) ... or (b) ..." [fork 17: the other reading is JUST FALSE, a failed "if" read as the text's own no] |
| `ch4-other-powers` | `s 76B(2) the direction meets the requirements of subsection (2)` | (a) failed "if" or "where": "The direction must be in writing and must specify the period within which the company is to change i..." |
| `ch4-other-powers` | `s 76B(3) the period meets the requirement of subsection (3)` | (a) failed "if" or "where": "The period must be a period of at least 28 days beginning with the date of the direction" |
| `ch4-other-powers` | `s 76B(4) the Secretary of State may give a further direction extending the period` | (b) limited by its own wording: "by further direction in writing" [fork 21: the other reading is JUST FALSE, a failed "if" read as the text's own no]<br>(a) failed "if" or "where": "Any such direction must be given before the end of the period for the time being specified" |
| `ch4-other-powers` | `s 76B(5) the company may apply to the court to set the direction aside` | (b) limited by its own wording: "to set aside a direction under subsection (1)" |
| `ch4-other-powers` | `s 76B(6) the application is made in time` | (a) failed "if" or "where": "must be made within the period of three weeks beginning with the date of the direction" |
| `ch4-other-powers` | `s 76B(7) the court may set the direction aside or confirm it` | (b) limited by its own wording: "the power is given on an application under the preceding subsection" |
| `ch4-other-powers` | `s 76B(8) the court must specify the period within which the direction is to be complied with` | (a) failed "if" or "where": "If on an application under subsection (5) the direction is confirmed, the court must specify the per..." |
| `ch4-other-powers` | `s 76B(10) the company is not required to comply with the direction while the proceedings are ongoing` | (a) flat negative: "If a company applies to the court ... to set aside a direction, it is not required to comply with th..." |
| `ch4-other-powers` | `s 76B(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates` | (a) failed "if" or "where": "Where a direction is given under subsection (1), the registrar may omit" |
| `ch4-other-powers` | `s 76B(11) the person commits an offence` | (a) failed "if" or "where": "If a company fails to comply with a direction under subsection (1), an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `ch4-other-powers` | `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register` | (a) failed "if" or "where": "Where, in the opinion of the registrar, a company’s registered name consists of or includes computer..." |
| `ch4-other-powers` | `s 76C(2)(a) the registrar must give the company notice of the determination` | (a) failed "if" or "where": "If the registrar determines a new name for a company under this section, the registrar must— (a) giv..." |
| `ch4-other-powers` | `s 76C(2)(b) the registrar must place a note of the determination in the register` | (a) failed "if" or "where": "If the registrar determines a new name for a company under this section, the registrar must— ... (b)..." |
| `ch4-other-powers` | `s 76C(3)(a) the direction does not affect the registrar's power to act under subsection (1)` | (b) limited by its own wording: "Where a company is given a direction under section 76B to change its name" |
| `ch4-other-powers` | `s 76C(3)(b) the direction lapses` | (a) failed "if" or "where": "if the registrar does so, the direction lapses" |
| `ch4-other-powers` | `s 76D(2) the direction is one referred to in subsection (1)` | (a) failed "if" or "where": "The reference in subsection (1) to a direction to change a company’s name is to a direction under se..." |
| `ch4-other-powers` | `s 76D(1) the registrar may determine a new name for the company` | (a) failed "if" or "where": "Where a company fails to comply with a direction to change its name, the registrar may determine a n..."<br>(a) failed "if" or "where": "The reference in subsection (1) to a direction to change a company’s name is to a direction under se..." |
| `ch4-other-powers` | `s 76D(3)(a) the registrar must give the company notice of the determination` | (a) failed "if" or "where": "If the registrar determines a new name for a company under this section, the registrar must— (a) giv..." |
| `ch4-other-powers` | `s 76D(3)(b) the registrar must place a note of the determination in the register` | (a) failed "if" or "where": "If the registrar determines a new name for a company under this section, the registrar must— ... (b)..." |
| `ch4-other-powers` | `s 76E(2)(b) the crime is serious` | (a) failed "if" or "where": "crime is “serious” if— (i) ... imprisonment for 3 years or more, or (ii) the conduct involves the us..." |
| `ch4-other-powers` | `s 76E(1) Part 5 does not prevent the registration of the company by the name` | (b) limited by its own wording: "Nothing in this Part prevents the registration ... if the Secretary of State is satisfied that the r..." |
| `ch5-ch6-name-change-disclosure` | `s 77(1) the company may change its name in that way` | (b) limited by its own wording: "by special resolution (see section 78)"<br>(b) limited by its own wording: "by other means provided for by the company's articles (see section 79)" |
| `ch5-ch6-name-change-disclosure` | `s 77(2) the name of the company may also be changed in that way` | (b) limited by its own wording: "The name of a company may also be changed— (a) ... (e)" |
| `ch5-ch6-name-change-disclosure` | `s 78(1) the company must give notice to the registrar` | (a) failed "if" or "where": "Where a change of name has been agreed to by a company by special resolution, the company must give ..."<br>(a) failed "if" or "where": "Where a change of name has been agreed to by a company by special resolution" |
| `ch5-ch6-name-change-disclosure` | `s 78(2)(a) the notice must specify that the change is conditional` | (a) failed "if" or "where": "Where a change of name by special resolution is conditional on the occurrence of an event, the notic..." |
| `ch5-ch6-name-change-disclosure` | `s 78(2)(b) the notice must state whether the event has occurred` | (a) failed "if" or "where": "Where a change of name by special resolution is conditional on the occurrence of an event, the notic..." |
| `ch5-ch6-name-change-disclosure` | `s 78(3)(a) the registrar is not required to act under section 80 until further notice` | (a) flat negative: "If the notice states that the event has not occurred— (a) the registrar is not required to act under..." |
| `ch5-ch6-name-change-disclosure` | `s 78(3)(b) the company must give notice to the registrar stating that the event has occurred` | (a) failed "if" or "where": "If the notice states that the event has not occurred— ... (b) when the event occurs, the company mus..." |
| `ch5-ch6-name-change-disclosure` | `s 78(3)(c) the registrar may rely on the statement as sufficient evidence of the matters stated in it` | (b) limited by its own wording: "the registrar may rely on the statement" |
| `ch5-ch6-name-change-disclosure` | `s 79(2) the registrar may rely on the statement as sufficient evidence of the matters stated in it` | (b) limited by its own wording: "The registrar may rely on the statement" |
| `ch5-ch6-name-change-disclosure` | `s 80(1) this section applies` | (a) failed "if" or "where": "This section applies where— (a) ... or (b) ..." |
| `ch5-ch6-name-change-disclosure` | `s 80(2) the registrar must enter the new name on the register in place of the former name` | (a) failed "if" or "where": "This section applies where—" |
| `ch5-ch6-name-change-disclosure` | `s 80(3) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` | (a) failed "if" or "where": "On the registration of the new name, the registrar must issue a certificate of incorporation altered..." |
| `ch5-ch6-name-change-disclosure` | `s 81(1) the change of name has effect on the day` | (a) failed "if" or "where": "A change of a company's name has effect from the date on which the new certificate of incorporation ..."<br>(a) failed "if" or "where": "has effect from the date on which the new certificate of incorporation is issued" |
| `ch5-ch6-name-change-disclosure` | `s 81(2) the change of name affects the right, the obligation or the proceedings` | (a) flat negative: "The change does not affect any rights or obligations of the company or render defective any legal pr..."<br>(b) limited by its own wording: "the sentence speaks only of the company's rights and obligations and of legal proceedings by or agai..." |
| `ch5-ch6-name-change-disclosure` | `s 81(3) the proceedings may be continued or commenced against the company by its new name` | (b) limited by its own wording: "Any legal proceedings that might have been continued or commenced against it by its former name" |
| `ch5-ch6-name-change-disclosure` | `s 83(1) this section applies to the proceedings` | (b) limited by its own wording: "This section applies to any legal proceedings brought by a company ... to enforce a right arising ou..." |
| `ch5-ch6-name-change-disclosure` | `s 83(2) the proceedings shall be dismissed` | (a) failed "if" or "where": "unless the court before which the proceedings are brought is satisfied that it is just and equitable..."<br>(a) failed "if" or "where": "The proceedings shall be dismissed if the defendant ... shows— (a) ... or (b) ..."<br>(b) limited by its own wording: "this subsection speaks of the proceedings to which the section applies" |
| `ch5-ch6-name-change-disclosure` | `s 83(3) the section affects the person's right to enforce his rights against another person` | (a) flat negative: "This section does not affect the right of any person to enforce such rights as he may have against a..."<br>(b) limited by its own wording: "the sentence speaks only of rights a person enforces against another person in proceedings that pers..." |
| `ch5-ch6-name-change-disclosure` | `s 85(1) no account is taken of the difference` | (b) limited by its own wording: "no account is to be taken of— (a) ... (b) ... (c) ..."<br>(a) failed "if" or "where": "provided there is no real likelihood of names differing only in those respects being taken to be dif..." |
| `ch5-ch6-name-change-disclosure` | `s 85(2) subsection (1) affects the operation of the regulations` | (a) flat negative: "This does not affect the operation of regulations under section 57(1)(a) permitting only specified c..."<br>(b) limited by its own wording: "the sentence speaks only of regulations permitting only specified characters, marks or punctuation" |
| `part6-registered-office` | `s 86(2) the address is an appropriate address` | (a) failed "if" or "where": "An address is an “appropriate address” if, in the ordinary course of events— (a) ... and (b) ..." |
| `part6-registered-office` | `s 86(1) the company must ensure that its registered office is at an appropriate address` | (a) flat negative: "Subsection (1) does not apply in relation to a company during any period for which the address of it..." |
| `part6-registered-office` | `s 86(3) the person commits an offence` | (a) failed "if" or "where": "If a company fails, without reasonable excuse, to comply with this section an offence is committed b..."<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `part6-registered-office` | `s 87(1) the company may change the address of its registered office` | (b) limited by its own wording: "by giving notice to the registrar" |
| `part6-registered-office` | `s 87(1A) the notice must include a statement that the new address is an appropriate address within the meaning given by section 86(2)` | (b) limited by its own wording: "The notice must include a statement" |
| `part6-registered-office` | `s 87(2) the change takes effect on the day` | (a) failed "if" or "where": "The change takes effect upon the notice being registered by the registrar" |
| `part6-registered-office` | `s 87(2) a person may validly serve a document on the company at the address previously registered on the day` | (b) limited by its own wording: "the period begins with the date on which the notice is registered"<br>(a) failed "if" or "where": "until the end of the period of 14 days beginning with the date on which it is registered" |
| `part6-registered-office` | `s 87(3) the company may act on the change as from that date` | (a) failed "if" or "where": "may act on the change as from such date, not more than 14 days after the notice is given, as it may ..." |
| `part6-registered-office` | `s 87(4) the company is protected from being treated as having failed to comply with the duty` | (a) flat negative: "Where a company unavoidably ceases to perform ... but— (a) resumes performance ..., and (b) gives no..." |
| `part6-registered-office` | `s 88(2) the company may by special resolution require the register to state that its registered office is to be situated in Wales` | (b) limited by its own wording: "may by special resolution"<br>(b) limited by its own wording: "A company— (a) whose registered office is in Wales, and (b) as to which it is stated in the register..." |
| `part6-registered-office` | `s 88(3) the company may by special resolution require the register to state that its registered office is to be situated in England and Wales` | (b) limited by its own wording: "may by special resolution"<br>(b) limited by its own wording: "A company— (a) whose registered office is in Wales, and (b) as to which it is stated in the register..." |
| `part6-registered-office` | `s 88(4) the company must give notice to the registrar` | (a) failed "if" or "where": "Where a company passes a resolution under this section it must give notice to the registrar" |
| `part6-registered-office` | `s 88(4)(a) the registrar must amend the register accordingly` | (b) limited by its own wording: "who shall— (a) amend the register accordingly" |
| `part6-registered-office` | `s 88(4)(b) the registrar must issue a new certificate of incorporation altered to meet the circumstances of the case` | (b) limited by its own wording: "who shall— ... (b) issue a new certificate of incorporation altered to meet the circumstances of the..." |
| `part6-registered-office` | `s 88A(2) the email address is an appropriate email address` | (a) failed "if" or "where": "An email address is an “appropriate email address” if, in the ordinary course of events, emails sent..." |
| `part6-registered-office` | `s 88A(1) the company must ensure that its registered email address is an appropriate email address` | (b) limited by its own wording: "its registered email address" |
| `part6-registered-office` | `s 88A(3) the person commits an offence` | (a) failed "if" or "where": "If a company fails, without reasonable excuse, to comply with this section an offence is committed b..."<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `part6-registered-office` | `s 88B(1) the company may change its registered email address` | (b) limited by its own wording: "by giving notice to the registrar" |
| `part6-registered-office` | `s 88B(2) the notice must include a statement that the new address is an appropriate email address within the meaning given by section 88A(2)` | (b) limited by its own wording: "The notice must include a statement" |
| `part6-registered-office` | `s 88B(3) the change takes effect on the day` | (a) failed "if" or "where": "The change takes effect upon the notice being registered by the registrar" |
| `part7-other-routes` | `s 97(1) all of the answers hold` | (a) failed "if" or "where": "if" |
| `part7-other-routes` | `s 97(2) the conditions are met` | (a) failed "if" or "where": "The conditions are that— (a) where no application under section 98 for cancellation of the resolutio..."<br>(a) failed "if" or "where": "(b) where such an application has been made— (i) the application has been withdrawn, or (ii) an orde..." |
| `part7-other-routes` | `s 97(1) the public company may be re-registered as a private limited company` | (b) limited by its own wording: "A public company may be re-registered" |
| `part7-other-routes` | `s 97(3)(a) the company must make such changes in its name as are necessary in connection with its becoming a private company limited by shares or by guarantee` | (b) limited by its own wording: "the subsection speaks of the company's becoming a private company limited by shares or by guarantee ..." |
| `part7-other-routes` | `s 97(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming a private company limited by shares or by guarantee` | (b) limited by its own wording: "the subsection speaks of the company's becoming a private company limited by shares or by guarantee ..." |
| `part7-other-routes` | `s 98(1) the applicants may apply to the court for the cancellation of the resolution` | (a) failed "if" or "where": "Where a special resolution by a public company to be re-registered as a private limited company has ..."<br>(a) failed "if" or "where": "but not by a person who has consented to or voted in favour of the resolution" |
| `part7-other-routes` | `s 98(2) the application is made within 28 days after the passing of the resolution` | (a) failed "if" or "where": "The application must be made within 28 days after the passing of the resolution" |
| `part7-other-routes` | `s 98(2) the application may be made on behalf of the persons entitled to make it` | (b) limited by its own wording: "such one or more of their number as they may appoint for the purpose" |
| `part7-other-routes` | `s 98(3) the court shall make an order either cancelling or confirming the resolution` | (a) failed "if" or "where": "On the hearing of the application the court shall make an order either cancelling or confirming the ..." |
| `part7-other-routes` | `s 98(4) the court may make the order on terms, adjourn for the purchase of dissentient members' interests, and give directions` | (b) limited by its own wording: "The court may— (a) ... (b) ... (c) ..." |
| `part7-other-routes` | `s 98(5) the court's order may provide for the purchase by the company of members' shares and alter the articles` | (b) limited by its own wording: "The court's order may, if the court thinks fit— (a) ... (b) ..." |
| `part7-other-routes` | `s 98(6) the court's order may require the company not to amend its articles without the leave of the court` | (b) limited by its own wording: "The court's order may, if the court thinks fit, require the company not to make any, or any specifie..." |
| `part7-other-routes` | `s 99(1) the applicants must immediately give notice to the registrar` | (a) failed "if" or "where": "On making an application under section 98 ... the applicants, or the person making the application o..." |
| `part7-other-routes` | `s 99(2) the company must immediately give notice to the registrar` | (a) failed "if" or "where": "On being served with notice of any such application, the company must immediately give notice to the..." |
| `part7-other-routes` | `s 99(3) the copy of the order is delivered within the time allowed` | (a) failed "if" or "where": "Within 15 days of the making of the court's order on the application, or such longer period as the c..." |
| `part7-other-routes` | `s 99(4) the person commits an offence` | (a) failed "if" or "where": "If a company fails to comply with subsection (2) or (3) an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `part7-other-routes` | `s 100(1) the application contains what the subsection requires` | (a) failed "if" or "where": "An application for re-registration as a private limited company must contain a statement of the comp..." |
| `part7-other-routes` | `s 100(2) the application is accompanied by what the subsection requires` | (a) failed "if" or "where": "The application must be accompanied by— (a) ... (unless a copy has already been forwarded to the reg..." |
| `part7-other-routes` | `s 100(3) the statement meets the description of the statement of compliance` | (a) failed "if" or "where": "The statement of compliance ... is a statement that the requirements of this Part as to re-registrat..." |
| `part7-other-routes` | `s 100(4) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as a private limited company` | (b) limited by its own wording: "The registrar may accept the statement of compliance" |
| `part7-other-routes` | `s 101(1) the company shall be re-registered as a private limited company` | (a) failed "if" or "where": "If on an application for re-registration as a private limited company the registrar is satisfied tha..." |
| `part7-other-routes` | `s 101(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` | (b) limited by its own wording: "the duty follows the re-registration of subsection (1)" |
| `part7-other-routes` | `s 101(3) the certificate meets the requirement of subsection (3)` | (a) failed "if" or "where": "The certificate must state that it is issued on re-registration and the date on which it is issued." |
| `part7-other-routes` | `s 101(4)(a) the company is a private limited company on the day` | (a) failed "if" or "where": "On the issue of the certificate— (a) the company by virtue of the issue of the certificate becomes a..." |
| `part7-other-routes` | `s 101(4)(b) the changes in the company's name and articles have taken effect on the day` | (a) failed "if" or "where": "On the issue of the certificate— ... (b) the changes in the company's name and articles take effect" |
| `part7-other-routes` | `s 101(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` | (b) limited by its own wording: "The certificate is conclusive evidence" |
| `part7-other-routes` | `s 102(1) all of the answers hold` | (a) failed "if" or "where": "A private limited company may be re-registered as an unlimited company if— (a) ..., (b) ..., and (c)..." |
| `part7-other-routes` | `s 102(4) the member's assent is given` | (a) failed "if" or "where": "a trustee in bankruptcy of a member of the company is entitled, to the exclusion of the member, to a..."<br>(a) failed "if" or "where": "(a) all the members of the company have assented to its being so re-registered" |
| `part7-other-routes` | `s 102(2) the condition is met` | (a) failed "if" or "where": "The condition is that the company has not previously been re-registered as limited." |
| `part7-other-routes` | `s 102(1) the private limited company may be re-registered as an unlimited company` | (b) limited by its own wording: "A private limited company may be re-registered" |
| `part7-other-routes` | `s 102(3)(a) the company must make such changes in its name and its articles as are necessary in connection with its becoming an unlimited company` | (b) limited by its own wording: "the subsection speaks of the company's becoming an unlimited company on this re-registration" |
| `part7-other-routes` | `s 102(3)(b) the company must make such further changes as are necessary in connection with its becoming an unlimited company having a share capital` | (b) limited by its own wording: "the subsection speaks of the company's becoming an unlimited company on this re-registration"<br>(a) failed "if" or "where": "(b) if it is to have a share capital, as are necessary in connection with its becoming an unlimited ..." |
| `part7-other-routes` | `s 103(1) the application contains what the subsection requires` | (a) failed "if" or "where": "An application for re-registration as an unlimited company must contain a statement of the company's..." |
| `part7-other-routes` | `s 103(2) the application is accompanied by what the subsection requires` | (a) failed "if" or "where": "The application must be accompanied by— (a) the prescribed form of assent ... (b) a copy of the comp..."<br>(a) failed "if" or "where": "authenticated by or on behalf of all the members of the company" |
| `part7-other-routes` | `s 103(3) the statement meets the description of the statement of compliance` | (a) failed "if" or "where": "The statement of compliance ... is a statement that the requirements of this Part as to re-registrat..." |
| `part7-other-routes` | `s 103(4) the statement of compliance contains the directors' statement` | (a) failed "if" or "where": "The statement must contain a statement by the directors of the company— (a) ... (b) if any of the me..." |
| `part7-other-routes` | `s 103(5) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as an unlimited company` | (b) limited by its own wording: "The registrar may accept the statement of compliance" |
| `part7-other-routes` | `s 104(1) the company shall be re-registered as an unlimited company` | (a) failed "if" or "where": "If on an application for re-registration of a private limited company as an unlimited company the re..." |
| `part7-other-routes` | `s 104(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` | (b) limited by its own wording: "the duty follows the re-registration of subsection (1)" |
| `part7-other-routes` | `s 104(3) the certificate meets the requirement of subsection (3)` | (a) failed "if" or "where": "The certificate must state that it is issued on re-registration and the date on which it is issued." |
| `part7-other-routes` | `s 104(4)(a) the company is an unlimited company on the day` | (a) failed "if" or "where": "On the issue of the certificate— (a) the company by virtue of the issue of the certificate becomes a..." |
| `part7-other-routes` | `s 104(4)(b) the changes in the company's name and articles have taken effect on the day` | (a) failed "if" or "where": "On the issue of the certificate— ... (b) the changes in the company's name and articles take effect" |
| `part7-other-routes` | `s 104(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` | (b) limited by its own wording: "The certificate is conclusive evidence" |
| `part7-other-routes` | `s 105(2) the condition is met` | (a) failed "if" or "where": "The condition is that the company has not previously been re-registered as unlimited." |
| `part7-other-routes` | `s 105(1) the unlimited company may be re-registered as a private limited company` | (b) limited by its own wording: "An unlimited company may be re-registered" |
| `part7-other-routes` | `s 105(3) the special resolution meets the requirement of subsection (3)` | (a) failed "if" or "where": "The special resolution must state whether the company is to be limited by shares or by guarantee." |
| `part7-other-routes` | `s 105(4)(a) the company must make such changes in its name as are necessary in connection with its becoming a company limited by shares or by guarantee` | (b) limited by its own wording: "the subsection speaks of the company's becoming a company limited by shares or by guarantee on this ..." |
| `part7-other-routes` | `s 105(4)(b) the company must make such changes in its articles as are necessary in connection with its becoming a company limited by shares or by guarantee` | (b) limited by its own wording: "the subsection speaks of the company's becoming a company limited by shares or by guarantee on this ..." |
| `part7-other-routes` | `s 106(1) the application contains what the subsection requires` | (a) failed "if" or "where": "An application for re-registration as a limited company must contain a statement of the company's pr..." |
| `part7-other-routes` | `s 106(2) the application is accompanied by what the subsection requires` | (a) failed "if" or "where": "The application must be accompanied by— (a) ... (unless a copy has already been forwarded to the reg..." |
| `part7-other-routes` | `s 106(3) the member's undertaking covers the winding up` | (a) flat negative: "if the company is wound up while he is a member, or within one year after he ceases to be a member"<br>(a) failed "if" or "where": "if the company is wound up while he is a member, or within one year after he ceases to be a member" |
| `part7-other-routes` | `s 106(3) the statement of guarantee is as required` | (a) failed "if" or "where": "The statement of guarantee required to be delivered in the case of a company that is to be limited b..." |
| `part7-other-routes` | `s 106(4) the statement meets the description of the statement of compliance` | (a) failed "if" or "where": "The statement of compliance ... is a statement that the requirements of this Part as to re-registrat..." |
| `part7-other-routes` | `s 106(5) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as a limited company` | (b) limited by its own wording: "The registrar may accept the statement of compliance" |
| `part7-other-routes` | `s 107(1) the company shall be re-registered as a limited company` | (a) failed "if" or "where": "If on an application for re-registration of an unlimited company as a limited company the registrar ..." |
| `part7-other-routes` | `s 107(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` | (b) limited by its own wording: "the duty follows the re-registration of subsection (1)" |
| `part7-other-routes` | `s 107(3) the certificate meets the requirement of subsection (3)` | (a) failed "if" or "where": "The certificate must state that it is issued on re-registration and the date on which it is issued." |
| `part7-other-routes` | `s 107(4)(a) the company is a limited company on the day` | (a) failed "if" or "where": "On the issue of the certificate— (a) the company by virtue of the issue of the certificate becomes a..." |
| `part7-other-routes` | `s 107(4)(b) the changes in the company's name and articles have taken effect on the day` | (a) failed "if" or "where": "On the issue of the certificate— ... (b) the changes in the company's name and articles take effect" |
| `part7-other-routes` | `s 107(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` | (b) limited by its own wording: "The certificate is conclusive evidence" |
| `part7-other-routes` | `s 108(1) the company must deliver a statement of capital to the registrar` | (b) limited by its own wording: "A company which on re-registration under section 107 already has allotted share capital"<br>(a) flat negative: "This does not apply if the information which would be included in the statement has already been sen..." |
| `part7-other-routes` | `s 108(1) the statement of capital is delivered within 15 days after the re-registration` | (a) failed "if" or "where": "must within 15 days after the re-registration deliver a statement of capital to the registrar" |
| `part7-other-routes` | `s 108(3) the statement of capital states what the subsection requires` | (a) failed "if" or "where": "The statement of capital must state with respect to the company's share capital on re-registration— ..." |
| `part7-other-routes` | `s 108(4) the person commits an offence` | (a) failed "if" or "where": "If default is made in complying with this section, an offence is committed by"<br>(b) limited by its own wording: "every officer of the company who is in default" |
| `part7-other-routes` | `s 109(4) the member's assent is given` | (a) failed "if" or "where": "a trustee in bankruptcy of a member of the company is entitled, to the exclusion of the member, to a..."<br>(a) failed "if" or "where": "(a) all the members of the company have assented to its being so re-registered" |
| `part7-other-routes` | `s 109(2) the condition is met` | (a) failed "if" or "where": "The condition is that the company has not previously been re-registered— (a) as limited, or (b) as u..." |
| `part7-other-routes` | `s 109(1) the public company limited by shares may be re-registered as an unlimited private company with a share capital` | (b) limited by its own wording: "A public company limited by shares may be re-registered" |
| `part7-other-routes` | `s 109(3)(a) the company must make such changes in its name as are necessary in connection with its becoming an unlimited private company` | (b) limited by its own wording: "the subsection speaks of the company's becoming an unlimited private company on this re-registration" |
| `part7-other-routes` | `s 109(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming an unlimited private company` | (b) limited by its own wording: "the subsection speaks of the company's becoming an unlimited private company on this re-registration" |
| `part7-other-routes` | `s 110(1) the application contains what the subsection requires` | (a) failed "if" or "where": "An application for re-registration of a public company as an unlimited private company must contain ..." |
| `part7-other-routes` | `s 110(2) the application is accompanied by what the subsection requires` | (a) failed "if" or "where": "The application must be accompanied by— (a) the prescribed form of assent ... and (b) a copy of the ..."<br>(a) failed "if" or "where": "authenticated by or on behalf of all the members of the company" |
| `part7-other-routes` | `s 110(3) the statement meets the description of the statement of compliance` | (a) failed "if" or "where": "The statement of compliance ... is a statement that the requirements of this Part as to re-registrat..." |
| `part7-other-routes` | `s 110(4) the statement of compliance contains the directors' statement` | (a) failed "if" or "where": "The statement must contain a statement by the directors of the company— (a) ... (b) if any of the me..." |
| `part7-other-routes` | `s 110(5) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as an unlimited private company` | (b) limited by its own wording: "The registrar may accept the statement of compliance" |
| `part7-other-routes` | `s 111(1) the company shall be re-registered as an unlimited private company` | (a) failed "if" or "where": "If on an application for re-registration of a public company as an unlimited private company the reg..." |
| `part7-other-routes` | `s 111(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` | (b) limited by its own wording: "the duty follows the re-registration of subsection (1)" |
| `part7-other-routes` | `s 111(3) the certificate meets the requirement of subsection (3)` | (a) failed "if" or "where": "The certificate must state that it is issued on re-registration and the date on which it is issued." |
| `part7-other-routes` | `s 111(4)(a) the company is an unlimited private company on the day` | (a) failed "if" or "where": "On the issue of the certificate— (a) the company by virtue of the issue of the certificate becomes a..." |
| `part7-other-routes` | `s 111(4)(b) the changes in the company's name and articles have taken effect on the day` | (a) failed "if" or "where": "On the issue of the certificate— ... (b) the changes in the company's name and articles take effect" |
| `part7-other-routes` | `s 111(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` | (b) limited by its own wording: "The certificate is conclusive evidence" |
| `part7-private-to-public` | `s 89 the company may by re-registration under Part 7 alter its status in that way` | (b) limited by its own wording: "(a) from a private company to a public company"<br>(b) limited by its own wording: "(b) from a public company to a private company"<br>(b) limited by its own wording: "(c) from a private limited company to an unlimited company"<br>(b) limited by its own wording: "(d) from an unlimited private company to a limited company"<br>(b) limited by its own wording: "(e) from a public company to an unlimited private company" |
| `part7-private-to-public` | `s 90(1) all of the answers hold` | (a) failed "if" or "where": "if" |
| `part7-private-to-public` | `s 90(1) the private company may be re-registered as a public company limited by shares` | (b) limited by its own wording: "A private company (whether limited or unlimited) may be re-registered" |
| `part7-private-to-public` | `s 90(3)(a) the company must make such changes in its name as are necessary in connection with its becoming a public company` | (b) limited by its own wording: "becoming a public company" |
| `part7-private-to-public` | `s 90(3)(b) the company must make such changes in its articles as are necessary in connection with its becoming a public company` | (b) limited by its own wording: "becoming a public company" |
| `part7-private-to-public` | `s 90(4) the company must also make such changes in its articles as are necessary in connection with its becoming a company limited by shares` | (b) limited by its own wording: "becoming a company limited by shares"<br>(a) failed "if" or "where": "If the company is unlimited it must also make such changes in its articles" |
| `part7-private-to-public` | `s 91(1)(a) the nominal value of the allotted share capital is not less than the authorised minimum` | (a) failed "if" or "where": "the nominal value of the company's allotted share capital must be not less than the authorised minim..." |
| `part7-private-to-public` | `s 91(1)(b) the allotment is paid up as the paragraph requires` | (a) failed "if" or "where": "each of the company's allotted shares must be paid up at least as to one-quarter of the nominal valu..." |
| `part7-private-to-public` | `s 91(1)(c) the allotment meets the paragraph` | (a) failed "if" or "where": "the undertaking must have been performed or otherwise discharged" |
| `part7-private-to-public` | `s 91(1)(d) the allotment meets the paragraph` | (a) failed "if" or "where": "then either— (i) the undertaking must have been performed or otherwise discharged, or (ii) there mus..." |
| `part7-private-to-public` | `s 91(2)(a) the allotment may be disregarded` | (b) limited by its own wording: "(ii) before 31st December 1984 in the case of a company then registered in Northern Ireland"<br>(b) limited by its own wording: "(i) before 22nd June 1982 in the case of a company then registered in Great Britain" |
| `part7-private-to-public` | `s 91(2)(b) the allotment may be disregarded` | (b) limited by its own wording: "shares allotted in pursuance of an employees' share scheme by reason of which the company would, but..." |
| `part7-private-to-public` | `s 91(3) the disregard under subsection (2)(a) is within the limit` | (a) failed "if" or "where": "No more than one-tenth of the nominal value of the company's allotted share capital is to be disrega..." |
| `part7-private-to-public` | `s 91(1) the requirements of paragraphs (b) to (d) are met` | (a) flat negative: "The following requirements must be met"<br>(a) failed "if" or "where": "No more than one-tenth of the nominal value of the company's allotted share capital is to be disrega..." |
| `part7-private-to-public` | `s 91(5) the company may be re-registered as a public company` | (a) flat negative: "A company must not be re-registered as a public company if it appears to the registrar that"<br>(b) limited by its own wording: "the prohibition names only a company in the position of (a), (b) and (c)" |
| `part7-private-to-public` | `s 92(1)(a) the balance sheet is prepared as at a date not more than seven months before the application is delivered` | (a) failed "if" or "where": "a balance sheet prepared as at a date not more than seven months before the date on which the applic..." |
| `part7-private-to-public` | `s 92(5) a qualification is material` | (b) limited by its own wording: "a qualification is material unless"<br>(a) flat negative: "a qualification is material unless the auditor states in his report that the matter giving rise to t..." |
| `part7-private-to-public` | `s 92(3) the report is an unqualified report` | (a) failed "if" or "where": "a report stating without material qualification the auditor's opinion" |
| `part7-private-to-public` | `s 92(1)(b) the company has obtained an unqualified report by its auditor on the balance sheet` | (a) failed "if" or "where": "A company applying to re-register as a public company must obtain— ... (b) an unqualified report by ..." |
| `part7-private-to-public` | `s 92(1)(c) the company has obtained the auditor's written statement` | (a) failed "if" or "where": "A company applying to re-register as a public company must obtain— ... (c) a written statement by th..." |
| `part7-private-to-public` | `s 92(2) there is no change in the company's financial position of the kind the subsection excludes` | (a) failed "if" or "where": "there must be no change in the company's financial position that results in the amount of its net as..." |
| `part7-private-to-public` | `s 92(4) the provisions of this Act apply to the auditor's report with such modifications as are necessary` | (b) limited by its own wording: "For the purposes of an auditor's report on a balance sheet that was not prepared for a financial yea..." |
| `part7-private-to-public` | `s 93(1) section 93 applies (recent allotment of shares for non-cash consideration)` | (a) failed "if" or "where": "This section applies where— (a) ... and (b) ..." |
| `part7-private-to-public` | `s 93(3) the allotment is in connection with a share exchange` | (a) failed "if" or "where": "An allotment is in connection with a share exchange if— (a) ... and (b) ..." |
| `part7-private-to-public` | `s 93(5) it matters whether the arrangement involves an issue of shares in the other company` | (a) failed "if" or "where": "It is immaterial, for the purposes of deciding whether an allotment is in connection with a share ex..."<br>(a) failed "if" or "where": "It is immaterial ... whether or not the arrangement ... involves the issue" |
| `part7-private-to-public` | `s 93(6) there is a proposed merger with another company` | (a) failed "if" or "where": "There is a proposed merger with another company if one of the companies concerned proposes to acquir..." |
| `part7-private-to-public` | `s 93(7)(a) the amount counts as consideration for the allotment` | (a) flat negative: "the consideration for an allotment does not include any amount standing to the credit of any of the ..."<br>(b) limited by its own wording: "the sentence names only amounts standing to the credit of reserve accounts or the profit and loss ac..." |
| `part7-private-to-public` | `s 93(2) the registrar may entertain the application for re-registration` | (a) flat negative: "The registrar shall not entertain an application by the company for re-registration as a public comp..."<br>(b) limited by its own wording: "s 93 applies only where shares were recently allotted for non-cash consideration" |
| `part7-private-to-public` | `s 94(1) the application contains what the subsection requires` | (a) failed "if" or "where": "An application for re-registration as a public company must contain— (a) a statement of the company'..." |
| `part7-private-to-public` | `s 94(2) the application is accompanied by what the subsection requires` | (a) failed "if" or "where": "The application must be accompanied by— (a) ... (b) ... (c) ... (d) ... (e) ..." |
| `part7-private-to-public` | `s 94(3) the statement meets the description of the statement of compliance` | (a) failed "if" or "where": "The statement of compliance ... is a statement that the requirements of this Part as to re-registrat..." |
| `part7-private-to-public` | `s 94(4) the registrar may accept the statement of compliance as sufficient evidence that the company is entitled to be re-registered as a public company` | (b) limited by its own wording: "The registrar may accept the statement of compliance" |
| `part7-private-to-public` | `s 95(3) the statement of the proposed secretary includes the company's statement of consent` | (a) failed "if" or "where": "The statement must also include a statement by the company that the person named as secretary, or ea..." |
| `part7-private-to-public` | `s 95(3) consent may be given by one partner on behalf of all of them` | (b) limited by its own wording: "If all the partners in a firm are to be joint secretaries, consent may be given by one partner on be..." |
| `part7-private-to-public` | `s 96(1) the company shall be re-registered as a public company` | (a) failed "if" or "where": "If on an application for re-registration as a public company the registrar is satisfied that the com..." |
| `part7-private-to-public` | `s 96(2) the registrar must issue a certificate of incorporation altered to meet the circumstances of the case` | (b) limited by its own wording: "the duty follows the re-registration of subsection (1)" |
| `part7-private-to-public` | `s 96(3) the certificate meets the requirement of subsection (3)` | (a) failed "if" or "where": "The certificate must state that it is issued on re-registration and the date on which it is issued." |
| `part7-private-to-public` | `s 96(4)(a) the company is a public company on the day` | (a) failed "if" or "where": "On the issue of the certificate— (a) the company by virtue of the issue of the certificate becomes a..." |
| `part7-private-to-public` | `s 96(4)(b) the changes in the company's name and articles have taken effect on the day` | (a) failed "if" or "where": "On the issue of the certificate— ... (b) the changes in the company's name and articles take effect" |
| `part7-private-to-public` | `s 96(4)(c) the person named in the statement as secretary is deemed to have been appointed on the day` | (b) limited by its own wording: "where the application contained a statement under section 95"<br>(a) failed "if" or "where": "On the issue of the certificate— ... (c) ... the person or persons named in the statement as secreta..."<br>(a) failed "if" or "where": "On the issue of the certificate— ... (c) ... deemed to have been appointed to that office" |
| `part7-private-to-public` | `s 96(5) the certificate is conclusive evidence that the requirements of this Act as to re-registration have been complied with` | (b) limited by its own wording: "The certificate is conclusive evidence" |

Left out: 15 `FALSE-kind` branches whose quoted words say "means" (a definition the text gives with "means" is the text's own no under the brief and is not an open reading).

286 functions, 222 distinct `(a)` branches and 138 distinct `(b)` branches (a branch repeated word for word in the generated sections 76 to 76B is listed once per function).

### Name-test sweep of 2026-11-12

Every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" (80 functions) was read for a grant turned into a bar.
40 of them already answer only `JUST TRUE` or `NOTHING` (no `JUST FALSE` branch).
The other 40 answered `JUST FALSE`, and are counted below.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 12 | 18 | 10 | 0 |

Flipped (forks 10 to 21; the last four keep their time-limit `JUST FALSE` and flip only the "in writing" complement): `s 64(1) the Secretary of State may direct the company to change its name`; `s 67(1) the Secretary of State may direct the company to change its name`; `s 73(4) the adjudicator may determine a new name for the company`; `s 74(4) the court may specify the date, remit the matter or make any order or determination that the adjudicator might have made`; `s 75(1) the Secretary of State may direct the company to change its name`; `s 76(1) the Secretary of State may direct the company to change its name`; `s 76A(1) the Secretary of State may direct the company to change its name`; `s 76B(1) the Secretary of State may direct the company to change its name`; `s 64(2B) the Secretary of State may give a further direction extending the period`; `s 76(3A) the Secretary of State may give a further direction extending the period`; `s 76A(4) the Secretary of State may give a further direction extending the period`; `s 76B(4) the Secretary of State may give a further direction extending the period`.

Kept `JUST FALSE`:

- `s 53 the company may be registered by the name`: a bar: "must not be registered ... if"
- `s 53A the company may be registered by the name`: a bar
- `s 56A the company may be registered by the name`: a bar
- `s 57(3) the company may be registered by the name`: a bar: "may not be registered"
- `s 57A the company may be registered by the name`: a bar
- `s 57B(1) the company may be registered by the name`: a bar: "must not subsequently be registered"
- `s 57C(1) the other company may be registered by the name`: a bar: "no other company may be registered"
- `s 63(1) the company may amend its articles as proposed`: a bar: "must not amend"
- `s 65(3) the company may be registered by the name`: a bar
- `s 66(1) the company may be registered by the name`: a bar
- `s 91(5) the company may be re-registered as a public company`: a bar: "must not be re-registered"
- `s 60(2) the registrar may refuse to register the company by the name`: "unless a statement has been delivered"
- `s 93(2) the registrar may entertain the application for re-registration`: "shall not entertain ... unless"
- `s 68(3) the Secretary of State may give a further direction extending the period`: the time limit is closed by "Any such direction must be given before the end of the period"
- `s 75(3) the Secretary of State may give a further direction extending the period`: the same time limit
- `s 87(2) a person may validly serve a document on the company at the address previously registered on the day`: "until the end of the period of 14 days"
- `s 87(3) the company may act on the change as from that date`: "not more than 14 days after the notice is given"
- `s 91(1)(a) the nominal value of the allotted share capital is not less than the authorised minimum`: a duty (the name contains "authorised" for "the authorised minimum", not for a power): "must be not less than"

Listed, "may" with "where" (fork register): `s 64(6A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates`; `s 67(1A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates`; `s 73(7) the registrar may omit from the register material available for public inspection any mention of the name to which the order relates`; `s 75(4A) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates`; `s 76(5B) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates`; `s 76A(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates`; `s 76B(9) the registrar may omit from the register material available for public inspection any mention of the name to which the direction relates`; `s 76C(1) the registrar may determine a new name for the company and remove the old name from the register`; `s 76D(1) the registrar may determine a new name for the company`; `s 98(1) the applicants may apply to the court for the cancellation of the resolution`.

Listed, "entitled": none.

26 assertions were restated in place with `-- RECONCILED 2026-11-12: was ...` (17 in `coa2-tests-ch2.l4`, `-ch3`, `-ch4`, 9 in `coa2-cases-seat.l4`).

### Reading a result: FALSE and NOTHING (coa2)

In this Part, a `JUST FALSE` is the Act's own no.
Examples, each tested: s 53 answers `JUST FALSE` to "may the company be registered by the name" when the Secretary of State is of the opinion that its use would be an offence or that it is offensive, because the section says a company "must not be registered" on that opinion; the date functions answer `JUST FALSE` after the last day the text allows ("within twelve months of the company's registration" on the day after the anniversary); a duty that the text makes conditional (s 78(1), "must give notice" where the name change was agreed by special resolution) answers `JUST FALSE` where its trigger is absent, which is reading (a); a definition the text gives with "if" (s 86(2), s 88A(2)) answers `JUST FALSE` when a limb fails.
A `NOTHING` is "the Act does not decide on these facts".
Examples, each tested: s 53 answers `NOTHING` for a name the Secretary of State has formed no such opinion about, because the prohibition names only its own cases; the daily default fine of ss 63(3) and 64(6) is `NOTHING` (the rendering gives two wordings and does not choose); s 98(7) answers `NOTHING` for a court outside England and Wales; s 74(3) says nothing about when a suspension of the adjudicator's order ends; the shadow director in ss 64(5), 86(3), 88A(3), 99(4) and 108(4) is `NOTHING`.
A caller must never turn `NOTHING` into `FALSE`.
In the seat, every question returns `MAYBE BOOLEAN` (or a number, a string, or a named type where it asks for one); a `NOTHING` is shown as "not covered".
Amounts of money are never in the Act: the pounds a level on the standard scale stands for are asked as inputs, and the authorised minimum share capital (s 763) is an input.

## Seams (coa2)

The names are as PLAN.md section 8 (and the keel's `coa-core.l4`) give them where it gives one; otherwise the name is the section label plus the words of the question.
Every seam the module takes is an input (a parameter), so each module stands alone; none is defined here.

### Seam inputs taken from other parts or the keel

| name (as used in the module) | answering part | taken in |
| --- | --- | --- |
| `s 3(1) the company is a limited company` | keel | ch2-company-type, part7-other-routes, part7-private-to-public |
| `s 3(2) the company is limited by shares` | keel | part7-other-routes |
| `s 3(4) the company is an unlimited company` | keel | part7-other-routes |
| `s 4(1) the company is a private company` | keel | ch2-company-type, part7-other-routes, part7-private-to-public |
| `s 4(2) the company is a public company` | keel | ch2-company-type, part7-other-routes, part7-private-to-public |
| `s 279J the statement contains the required information about the individual` | coa6 | part7-private-to-public |
| `s 279K the statement contains the required information about the corporate secretary or firm` | coa6 | part7-private-to-public |
| `s 283 the resolution is a special resolution` | coa7 | ch5-ch6-name-change-disclosure, part6-registered-office, part7-other-routes, part7-private-to-public |
| `s 547 the amount of the company's called-up share capital` | coa13 | part7-private-to-public |
| `s 593(1) the requirements of paragraphs (a) and (b) of section 593(1) have been complied with` | coa13 | part7-private-to-public |
| `s 626 the reduction is made under section 626 (redenomination of share capital)` | coa14 | part7-private-to-public |
| `s 643 the reduction is supported by a solvency statement in accordance with section 643` | coa14 | part7-private-to-public |
| `s 648 the reduction has been confirmed by an order of the court under section 648` | coa14 | part7-private-to-public |
| `s 763 the authorised minimum` | coa16 | part7-private-to-public |
| `s 831 the amount of the company's net assets at the balance sheet date` | coa18 | part7-private-to-public |
| `s 831 the amount of the company's net assets on the date the application is delivered` | coa18 | part7-private-to-public |
| `s 831 the amount of the company's undistributable reserves` | coa18 | part7-private-to-public |
| `s 831 the amount worked out as section 831 provides` | coa18 | part7-private-to-public |
| `s 1097A(3)(h) the address of the registered office is a default address nominated by the registrar for the period` | coa24 | part6-registered-office |
| `s 1121 the officer is in default` | coa24 | ch2-company-type, ch3-similarity, ch4-other-powers, part6-registered-office, part7-other-routes |
| `s 1146 the form of assent is authenticated by or on behalf of all the members of the company` | coa25 | part7-other-routes |

### Answers this range gives to other parts

| expression (Schedule 8) | name | note |
| --- | --- | --- |
| registered office, of a company (s 86) | `s 86 the company has its registered office at the address` | PLAN.md's name. s 86 does not define the term, so the function takes "the address is the address entered in the register" and answers `NOTHING` otherwise (finding 8). |
| Welsh company (s 88) | `s 88(1) the company is a Welsh company` | defined by the register statement; `JUST FALSE` when the register does not say Wales. |
| net assets (s 92, in Part 7) | `s 92 the requirements as to net assets are met`, `s 92(6) the amount of the company's net assets or undistributable reserves` | s 92(6) points to s 831 (coa18): the amount is an input, `s 831 the amount worked out as section 831 provides`. |
| local authority; public authority (s 54(2)) | `s 54(2) the body is a local authority`, `s 54(2) the person or body is a public authority` | |
| appropriate address; appropriate email address (ss 86(2), 88A(2)) | `s 86(2) the address is an appropriate address`, `s 88A(2) the email address is an appropriate email address` | |

### Seams the plan lacks, or names wrongly

- **`s 763 the authorised minimum`** (coa16), taken by s 91(1)(a), s 91(5); **`s 547 the amount of the company's called-up share capital`** (coa13), taken by s 92; **`s 1146 ... authenticated`** (coa25), taken by ss 103 and 110; **`s 1121 the officer is in default`** (coa24) is in PLAN.md's table but not in coa2's explicit seam line.
  None of the four is in the explicit seam line for coa2 in PLAN.md section 6 (that line lists s 54: s 2; s 58 and s 59: s 33; s 77: s 1033; s 86: s 1097A; s 91: ss 626, 643, 648; s 92: s 831; s 93: s 593 and Part 26; s 94, s 100, s 106: Part 3; s 95: ss 279J, 279K; s 108: s 10).
- **False positives in that line** (finding 4): `s 54: s 2 [keel]` is "section 2 of the Local Government etc. (Scotland) Act 1994" (line 584), and `s 58: s 33` and `s 59: s 33 [coa1]` are "section 33 of the Companies (Audit, Investigations and Community Enterprise) Act 2004" (lines 644, 649): other Acts, not seams.
  They are plain facts here: `a council constituted under section 2 of the Local Government etc. (Scotland) Act 1994` and `the company is a community interest company`.
- **Seams the plan lists that this range takes as inputs described in the asking section's own words, not as a name carrying the other section's number:** Part 3 (ss 94(2), 100(2), 106(2): "a copy has already been forwarded to the registrar"), s 10 (s 108(1)), s 1033 (s 77(2)(d): the input's description cites it), Part 26 (s 93(3), (7): "arrangement" is defined in s 93(7)(b) and the arrangement itself is a fact).

## What the text turns out to say (numbered findings)

1. **Two wordings of one fine run together (ss 63(3), 64(6)).** Lines 701 and 728 read "... one-tenth of level 5 on the standard scaleone-tenth of the greater of £5,000 or level 4 on the standard scale." Fork 1; NEEDS-CORE.md.
2. **Two paragraphs shown as dots.** s 69(4)(b) (line 802) and s 108(3)(d) (line 1370) read "(b) . . . . ." and "(d) . . . . .": repealed or blank in this text. The other paragraphs of s 69(4) keep their letters, so (c), (d) and (e) are still (c), (d) and (e).
3. **Ellipses left in sentences.** s 69(5) reads "If the facts mentioned in subsection (4)(a) ... or (c) are established" (line 807), and s 108(3)(c)(iii) ends ", ..." (line 1369). Both are read as they stand; s 69(5) refers to (4)(a) and (4)(c), the paragraphs that remain.
4. **Two of PLAN.md's seams are other Acts.** s 54's "section 2" and ss 58/59's "section 33" are sections of the Local Government etc. (Scotland) Act 1994 and the Companies (Audit, Investigations and Community Enterprise) Act 2004. See Seams.
5. **s 98(7) as rendered says only what the court is in England and Wales** (line 1261, ending "means the High Court"). Fork 6.
6. **The shadow-director sentence is in six offence sections and absent from five.** Fork 7.
7. **s 74(3) says the effect of the adjudicator's order is suspended if notice of appeal is given and never says when the suspension ends.** The function answers only "is it suspended because notice of appeal was given against a decision upholding the application", with a test on each limb; it does not model the end.
8. **The registered office is not defined where PLAN.md expects it.** s 86 is a duty to ensure the registered office is at an appropriate address; s 87(2) makes the registered address the one that counts for service. `s 86 the company has its registered office at the address` takes "the address is the address entered in the register" and answers `NOTHING` otherwise, because the text in this range does not say that an unregistered address is not the office.
9. **No pound amount appears for any level on the standard scale.** The Act says "level 3", "level 4" and "level 5" (and "£5,000" once); the core's `Fine limit` carries (level, fraction), and the seat asks for the pounds only where the answer is a pounds figure (s 63(3), s 64(6)). The authorised minimum share capital (s 91(1)(a)) is likewise an input.

## What the stable binary does not accept (measured on 1.6.110; 1.6.109 gives the same assertion counts and the same 22 trace results)

Loud (the binary reports an error, so these teach):

- **A call argument on a continuation line indented less than the function-name token** after an `ELSE` fails with "unexpected (" (s 90(1) and s 97(1), first versions): the function name goes on its own line, with its argument indented deeper.
- **A `GIVEN` name equal to a function name, or to a name in the core, is an ambiguous identifier** ("There are multiple definitions for the identifier"); measured with `level` and `pounds` used as pattern variables over the core's `Fine limit` constructor fields. Pattern variables here are `lvl`, `frac` and `amt`.
- **`REFUSE`, `#ASSERT REFUSED`, `YMD`** are accepted by both supplied builds but forbidden by the brief; none is used.

Silent (exit code 0, wrong answer), the ones worth the words:

- **`NOT x AND y` reads as `NOT (x AND y)`.** Hand-written expectations failed in Part 7 (eight assertions) and in Part 6 (ss 86(3), 88A(3)) until every `NOT` was parenthesised, `(NOT (x)) AND y`; regression tests for s 94(1) and s 94(2) sit in `coa2-tests-part7a.l4`.
- **A `#TRACE` result is an Information diagnostic, not an assertion.** `l4 run` exits 0 whatever a trace shows, and an `#ASSERT` cannot take a trace as its subject. The 22 traces (in `coa2-tests-ch2`, `ch3`, `ch4`, `part7b`) each carry a `-- TRACE-EXPECT: ...` comment, and `coa2-tracecheck.py` compares it with the printed result (see the check output below). `check.sh` does not see traces; its own note says so.
- **A `SHANT` with no `WITHIN` leaves a standing residual (`MUST NOT ...`)**, not `FULFILLED`: the trace expectation for s 63(1) is the residual.
- **`l4 run` exits 0 when an assertion fails**; the numbers come from the diagnostics, as `check.sh` prints them.

Not measured here, kept in the layer-1 style because the brief says so: no `TYPICALLY` on a record field, no sets, no section `GIVEN`, `WAITUNTIL` spelled as one word, every `#ASSERT` on one line.

## The seat layer (`coa2-seat.l4`, `coa2-cases-seat.l4`)

**The seat** is an individual who is, or is about to become, a director, company secretary or member of a company registered under the Act, or who deals with one: someone asking, on facts they can state, what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done. This seat is assumed, not ruled.
There is no seat for an official: what ss 53 to 57C say to the Secretary of State or the registrar appears only as what it means for the person (what may be done to them, what they must be given, and by when).
`159` questions, each with `@export` and an `@desc`, named "Under section N, ...", grouped under `§` headings in the order of the text (Part 5 Chapters 1 to 6, Part 6, Part 7 by route).
Each question takes plain inputs (one per fact the person can state: yes or no, a number, a date, a choice from a list), builds the layer-1 record internally (the allotment of s 91, the member of s 102(4) and s 109(4), the `Party` of an offence question) and calls the layer-1 function; no rule is restated.
`coa2 seat a stated fact as an answer` turns a person's yes or no into the seam answer `JUST TRUE` or `JUST FALSE`; `coa2 seat a date if it has happened` turns "has it happened" and a date into a `MAYBE DATE`.
The penalty questions return a sentence built by `coa2 seat describe a penalty`.
`coa2-cases-seat.l4` has `335` assertions written from the text (not from the output): both sides of every boundary (28 days, 90 days, 3 weeks, 14 days, 15 days, 5%, one quarter, seven months, one year), mirror cases, and `NOTHING` cases ("not covered") for the questions where a set of facts falls outside what the Act says.
Provisions that address only an official appear in the seat only for what they mean to the person: for example `Under section 64(2A), is the period the direction gives us long enough` and `Under section 80(1), must the registrar enter our new name on the register`.

### Seat audit of 2026-11-12: does each question ask what its function answers?

All 159 questions were read against the layer-1 function each one calls, for direction ("may", "can", "need", "is barred" against the opposite) and for subject ("must" against "has" or "does", "will" against "must").
Seven did not match and were retitled, with their `@export` text, so that each asks what the function answers; none was fixed by negating the answer, because a bar's `NOTHING` and `JUST FALSE` are not a grant.
The 15 assertions they carry in `coa2-cases-seat.l4` are restated in place with a `-- RECONCILED 2026-11-12: was ...` comment (the values did not change; under the old titles some of them read the wrong way round).

| section | old name | new name | kind |
| --- | --- | --- | --- |
| s 91(5) | Under section 91(5), is my company barred from re-registering because of a capital reduction | Under section 91(5), may my company be re-registered as a public company after resolving to reduce its share capital | direction (the function is the permission; `JUST FALSE` is the bar, `NOTHING` is not covered) |
| s 76(5A) | Under section 76(5A), need we comply with the direction while the court proceedings are going on | Under section 76(5A), is my company not required to comply with the direction while the court proceedings are going on | direction (the function answers "not required") |
| s 92(2) | Under section 92(2), has the company's financial position changed so that net assets fell below the aggregate | Under section 92(2), is there no change in the company's financial position that makes net assets less than the aggregate | direction (the function answers "there is no such change") |
| s 105(3) | Under section 105(3), must the special resolution say whether we will be limited by shares or by guarantee | Under section 105(3), does the special resolution state whether we will be limited by shares or by guarantee | subject ("must" against "does it") |
| s 73(1) | Under section 73(1), will the adjudicator make an order against my company | Under section 73(1), must the adjudicator make an order against my company | subject ("will" against "must") |
| s 80(1) | Under section 80(1), will the registrar register our new name | Under section 80(1), must the registrar enter our new name on the register | subject ("will" against "must") |
| s 83 | Under section 83, will proceedings by a company be dismissed because it did not make the required disclosure | Under section 83, must proceedings by a company be dismissed because it did not make the required disclosure | subject ("will" against "shall") |

Read and kept: `Under section 76E(1), can Part 5 be disapplied so that my company is registered by the name` calls `s 76E(1) Part 5 does not prevent the registration of the company by the name`; the polarity is the same (`JUST TRUE` means registration is not prevented), so it was not changed.

## What `check.sh` prints

**The baseline it replaced.** The folder as supplied held only the keel's `coa-core.l4` and `coa-definitions.l4`; `check.sh` on that folder (measured at the end of this session, on a copy) printed a TOTAL of 2 modules with 0 errors, 0 satisfied, 0 failed, 0 refused on both builds.

**Now** (`L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`, exit code 0):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa2-cases-seat.l4                             0       335       0        0         0 |      0       335       0        0  same
coa2-ch1-prohibited-names.l4                   0         0       0        0         0 |      0         0       0        0  same
coa2-ch2-company-type.l4                       0         0       0        0         0 |      0         0       0        0  same
coa2-ch3-similarity.l4                         0         0       0        0         0 |      0         0       0        0  same
coa2-ch4-other-powers.l4                       0         0       0        0         0 |      0         0       0        0  same
coa2-ch5-ch6-name-change-disclosure.l4         0         0       0        0         0 |      0         0       0        0  same
coa2-part6-registered-office.l4                0         0       0        0         0 |      0         0       0        0  same
coa2-part7-other-routes.l4                     0         0       0        0         0 |      0         0       0        0  same
coa2-part7-private-to-public.l4                0         0       0        0         0 |      0         0       0        0  same
coa2-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa2-tests-ch1.l4                              0        80       0        0         0 |      0        80       0        0  same
coa2-tests-ch2.l4                              0       144       0        0         0 |      0       144       0        0  same
coa2-tests-ch3.l4                              0       114       0        0         0 |      0       114       0        0  same
coa2-tests-ch4.l4                              0       184       0        0         0 |      0       184       0        0  same
coa2-tests-ch5-ch6.l4                          0        78       0        0         0 |      0        78       0        0  same
coa2-tests-part6.l4                            0        87       0        0         0 |      0        87       0        0  same
coa2-tests-part7a.l4                           0       196       0        0         0 |      0       196       0        0  same
coa2-tests-part7b.l4                           0       297       0        0         0 |      0       297       0        0  same
TOTAL (20 modules)                             0      1515       0        0           |      0      1515       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Other checks run at the end of the session:

- `python3 -I srcrefs.py check --refs <raw text> coa2-*.l4`: `srcrefs check: 905 src: lines, 353 runs, 353 locators, 0 problems`
- `python3 -I srcrefs.py check --strict <raw text> coa2-*.l4`: `srcrefs check: 905 src: lines, 353 runs, 353 locators, 0 problems`
- `L4=<l4-main-110> python3 -I coa2-tracecheck.py <the four test files with traces>`: `traces: 22, as expected: 22`; with 1.6.109: `traces: 22, as expected: 22`
- Quoted fragments of the FALSE-kind and NOTHING-kind comments looked up in the raw text lines 564-1413 (whitespace, curly quotes and dashes normalised): `fragments checked: 462, not found: 0`
- `l4 check` on every `coa2-*.l4`, counting lines that mention a misplaced `@ref` or any error or warning severity: 0
- Every `l4 run` on the files above shows no `DiagnosticSeverity_Error` or `_Warning` (`check.sh` fails the run on any error).
