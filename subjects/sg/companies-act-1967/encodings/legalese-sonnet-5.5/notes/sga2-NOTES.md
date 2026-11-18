# NOTES (sga2): the Companies Act 1967 (Singapore), sections 76 and 76A

This folder holds the encoding of lines 7321 to 8311 of `inputs/CoA1967.txt`: section 76 (a company's financial assistance for dealings in its own shares or those of its holding company) and section 76A (what follows from a contravention).
It was written by the part agent `sga2` of an eleven-agent parallel encoding of the Act, from the text alone, in L4 on the stable binary.

Layer 1, the law, is seven modules: `sga2-nouns.l4` (the types only) and six modules named for the provisions they hold, each of the six with its own tests file.
Layer 2, the seat, is `sga2-seat.l4` (106 questions) and `sga2-cases-seat.l4` (278 assertions).
The layer-1 modules and the seat are generated from sources and scripts that live outside the deposit, in `../../work/` (`build.py`, `mkseat.py`, `mkcases.py`, `coverage.py`, `covtable.py`, `mknotes.py`); the `.l4` files in this folder are the output and are never edited by hand.
The counts in this file come from scripts that read the files in this folder when the file was written.

## Edition encoded

The Companies Act 1967, 2020 Revised Edition, as the Singapore Statutes Online (SSO) informal consolidation "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, carrying the amendments up to Act 24 of 2025.
That file is a PDF turned into plain text: a rendering, not the official text, and nothing here is "verified against the official text".
A later consolidation may exist and was not read; the encoding is of that text only.
Line numbers everywhere are of `inputs/CoA1967.txt` as it is.
Page furniture and amendment marks (`[36/2014]` and the like) are not text; they sit in the row of the section they fall in.

## Seat

The seat is: an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company incorporated under the Act, or who deals with one.
(Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.
There is never a seat for the Registrar, the Minister, the Authority or the Court: their powers appear only as what they mean to the person.)

`sga2-seat.l4` has 106 questions under six `§§` groups in the text's order (s 76(1) to (4); s 76(5) to (7); s 76(8), (8A) and (9); s 76(9A) to (9D); s 76(10) to (15); s 76A).
Every question is named "Under section N, ..." with the Act's own numbering, has `@export`, and has an `@desc` on each input worded as the person would be asked.
Every question calls one layer-1 rule and restates none.
The headings of the groups that arise only in a situation say so: the offence and compensation of s 76(5) to (7) ("arises only where the company has contravened section 76(1) or (1A)") and the consequences of s 76A (contracts, orders, the certificate).

- **Plain inputs.** Yes/no, numbers, dates, a choice from one of the modules' own lists (the means of giving assistance, who the applicant is, what order the Court is asked to make), and one list of dates, the public holidays, because the Act counts "business days" against them (s 4(1) "business day").
  The list input is the one input that is not plain in the sense of the Guide; I did not find out whether the website's Interact form can ask a list.
- **Shared inputs.** `the company is a private company` is the keel's shared seat input (PLAN.md, section 3, line 46); the seat works out "public company" by the keel's `s 4(1) "public company"`, taking "the body is a company" as TRUE (assumed).
  `the company is exempt from audit requirements under section 205B or 205C` is the keel's seam input (PLAN.md section 4A).
  **PLAN.md sections 7 and 8 (the seat names every part shares, and the `NOTES.md` sections) are missing from this agent's copy of PLAN.md** (it ends at section 6); the brief governs, and the two names above are the only shared names I could find fixed elsewhere.
  The holding company and ultimate holding company are asked as `... is a public company` (answer no if there is none), which is what the layer-1 rule takes.
- **Records.** The `Solvency statement` of s 7A that s 76(9A)(e) and (9B)(c) need is built inside those two questions, in their `WHERE`, from 11 of their 13 plain answers (the other two are the audit exemption and whether all the directors made the statement); no field is left unasked.
  The statement the person describes is taken to be the one made for this giving of financial assistance (assumed).
- **Dates asked for a branch that may not arise.** Some questions need a date only on one branch (for example s 76(10)(h), which needs the parent's resolution date only where paragraph (b) applies); the `@desc` says what to give when the branch does not arise.
- **Two layer-1 functions have no seat question:** s 76(8)(n) and (o) (the savings that say subsection (8) implies nothing and limits no rule of law): they are statements about how to read subsection (8), and ask nothing of a person.
  The ten regulative rules are not seat questions either; each has a decision-function question that asks the same thing.
- **Direction check.** Each question's name asks in the direction of the layer-1 function it calls, because the name is generated from the function's own name (`work/mkseat.py`, `inv_title`) or, for the 19 functions whose name has no auxiliary verb or whose generated title would read badly, written by hand beside the call (`SPECIAL_TITLE` and the `title=` arguments).
  Questions that ask a bar ("does subsection (1) bar the company", "is the company barred", "is the person guilty", "is the Court barred") call the bar function; questions that ask a permission ("does subsection (1) not prohibit", "may the Court", "is the act one that subsections (1) and (1A) do not prohibit") call the permission function.
  No question negates a function's answer.
  I found no question whose name and body differ in direction or in subject.
  Three titles are awkward in English but mirror the function exactly: "does subsection (1) not prohibit the giving of the assistance" (the four route questions), "does the section not apply to the act or thing" (s 76(17)), "does subsection (6) not apply to the person" (s 76A(7)).
- **Not from the person.** Amounts the text fixes are in the layer-1 functions (the penalties $20,000 and 36 months, $5,000 and 12 months; the 10 percent; the 21 and 14 days; the 12 months; 15 May 1987).
  Nothing in sections 76 and 76A is left to regulations or a Minister, so no figure is substituted.

## Coverage (sga2)

Rows are made by `work/coverage.py` from the text itself: one row per section, subsection, paragraph, sub-paragraph and marginal heading of lines 7321 to 8311, plus a row for each place where the rendering repeats a paragraph label (Finding 1).
Each row has exactly one disposition: `encoded`, `fork` (with the fork id in the register below), `inert` with its reason, or `repealed or blank in this text`.
The defined terms of the range ("odd-lot" and "board lot", in s 76(8A)(a) and (b)) are rows of their own, `encoded`.
There are no table rows in this range.
A row's "L4 name" lists every layer-1 function whose `@ref` locator overlaps the row's lines and whose provision label is the row's, an ancestor of it or a descendant of it; a row under a subsection therefore also lists the function that encodes the whole subsection.

Rows: **199** (61 `encoded`, 136 `fork`, 2 `inert`, 0 `repealed or blank in this text`).
Fork rows by id (a row can carry several): F-A1 7, F-A2 7, F-A3 7, F-A4 1, F-A5 2, F-A6 29, F-A7 34, F-A8 16, F-A9 2, F-A10 4, F-A11 6, F-A12 3, F-A13 10, F-A14 4, F-A15 3, F-A16 4, F-A17 1, F-A18 1, F-A19 3.

**Audit.**
`work/coverage.py` counts the non-blank lines of 7321 to 8311 and checks that each falls in exactly one row: 739 non-blank lines in lines 7321-8311, 0 in no row, 0 in more than one row; 199 rows.
`work/covtable.py` checks that every row has at least one layer-1 function (except the two headings) and that every layer-1 function is named in at least one row: no row is empty and no function is orphaned.
The first run of the row script gave 185 rows, because it read the subsection order of s 76A as 1, 2, 1A and so took the lines of s 76A(1A) for text of (2); the checker showed 12 rows with no function, I corrected the order, and the second run gave 199 rows.
Rows in the table: before the audit 185, after 199.
The two `inert` rows are the marginal headings (reason 1); no row is `repealed or blank in this text`, and no row is `inert` for reason 2 or 3.

| row | lines | the text begins | disposition | L4 name |
| --- | --- | --- | --- | --- |
| s 76 marginal heading | 7321-7322 | Company financing dealings in its shares, etc. | inert, reason 1 (a marginal heading, not operative) | - |
| s 76(1) | 7323-7328 | 76.—(1) Except as otherwise expressly provided b... | fork F-A1 | `s 76(1) the company is one the subsection binds`<br>`s 76(1) subsection (1) bars the company from giving the financial assistance`<br>`s 76(1) a company the subsection binds must not give the financial assistance` |
| s 76(1)(a) | 7329-7331 | (a) the acquisition by any person, whether befor... | fork F-A1 | `s 76(1)(a) the acquisition is one that paragraph (a) names`<br>`s 76(1) subsection (1) bars the company from giving the financial assistance` |
| s 76(1)(a)(i) | 7332-7333 | (i) shares or units of shares in the company; or | fork F-A1 | `s 76(1)(a) the acquisition is one that paragraph (a) names`<br>`s 76(1) subsection (1) bars the company from giving the financial assistance` |
| s 76(1)(a)(ii) | 7334-7337 | (ii) shares or units of shares in a holding comp... | fork F-A1 | `s 76(1)(a) the acquisition is one that paragraph (a) names`<br>`s 76(1) subsection (1) bars the company from giving the financial assistance` |
| s 76(1)(b) | 7338-7339 | (b) the proposed acquisition by any person of — | fork F-A1 | `s 76(1)(b) the proposed acquisition is one that paragraph (b) names`<br>`s 76(1) subsection (1) bars the company from giving the financial assistance` |
| s 76(1)(b)(i) | 7340-7344 | (i) shares or units of shares in the company; or | fork F-A1 | `s 76(1)(b) the proposed acquisition is one that paragraph (b) names`<br>`s 76(1) subsection (1) bars the company from giving the financial assistance` |
| s 76(1)(b)(ii) | 7345-7350 | (ii) shares or units of shares in a holding comp... | fork F-A1 | `s 76(1)(b) the proposed acquisition is one that paragraph (b) names`<br>`s 76(1) subsection (1) bars the company from giving the financial assistance` |
| s 76(1A) | 7351-7353 | (1A) Except as otherwise expressly provided by t... | fork F-A2 | `s 76(1A) subsection (1A) bars the company from the act`<br>`s 76(1A) a company must not acquire its own shares or lend on the security of them` |
| s 76(1A)(a) | 7354-7355 | (a) whether directly or indirectly, in any way — | fork F-A2 | `s 76(1A) subsection (1A) bars the company from the act`<br>`s 76(1A) a company must not acquire its own shares or lend on the security of them` |
| s 76(1A)(a)(i) | 7356-7357 | (i) acquire shares or units of shares in the com... | fork F-A2 | `s 76(1A) subsection (1A) bars the company from the act`<br>`s 76(1A) a company must not acquire its own shares or lend on the security of them` |
| s 76(1A)(a)(ii) | 7358-7361 | (ii) purport to acquire shares or units of share... | fork F-A2 | `s 76(1A) subsection (1A) bars the company from the act`<br>`s 76(1A) a company must not acquire its own shares or lend on the security of them`<br>`s 76(1A)(a)(ii) a company must not purport to acquire shares in its holding company or ultimate holding company` |
| s 76(1A)(b) | 7362-7364 | (b) whether directly or indirectly, in any way, ... | fork F-A2 | `s 76(1A) subsection (1A) bars the company from the act`<br>`s 76(1A) a company must not acquire its own shares or lend on the security of them`<br>`s 76(1A)(b)(i) a company must not lend money on the security of shares in the company`<br>`s 76(1A)(b)(ii) a company must not lend money on the security of shares in its holding company or ultimate holding company` |
| s 76(1A)(b)(i) | 7365-7366 | (i) shares or units of shares in the company; or | fork F-A2 | `s 76(1A) subsection (1A) bars the company from the act`<br>`s 76(1A) a company must not acquire its own shares or lend on the security of them`<br>`s 76(1A)(b)(i) a company must not lend money on the security of shares in the company`<br>`s 76(1A)(b)(ii) a company must not lend money on the security of shares in its holding company or ultimate holding company` |
| s 76(1A)(b)(ii) | 7367-7372 | (ii) shares or units of shares in a holding comp... | fork F-A2 | `s 76(1A) subsection (1A) bars the company from the act`<br>`s 76(1A) a company must not acquire its own shares or lend on the security of them`<br>`s 76(1A)(b)(i) a company must not lend money on the security of shares in the company`<br>`s 76(1A)(b)(ii) a company must not lend money on the security of shares in its holding company or ultimate holding company` |
| s 76(2) | 7373-7378 | (2) A reference in this section to the giving of... | encoded | `s 76(2) the means is within the giving of financial assistance` |
| s 76(3) | 7379-7383 | (3) For the purposes of this section, a company ... | fork F-A3 | `s 76(3) the company is taken to have given the assistance for the purpose of the acquisition` |
| s 76(3)(a) | 7384-7386 | (a) the company gave the financial assistance fo... | fork F-A3 | `s 76(3) the company is taken to have given the assistance for the purpose of the acquisition` |
| s 76(3)(b) | 7387-7391 | (b) the relevant purpose was a substantial purpo... | fork F-A3 | `s 76(3) the company is taken to have given the assistance for the purpose of the acquisition` |
| s 76(4) | 7392-7401 | (4) For the purposes of this section, a company ... | fork F-A3 | `s 76(4) the company is taken to have given the assistance in connection with the acquisition` |
| s 76(4)(a) | 7402-7404 | (a) the acquisition by a person of shares or uni... | fork F-A3 | `s 76(4) the company is taken to have given the assistance in connection with the acquisition` |
| s 76(4)(b) | 7405-7411 | (b) where shares in the company had already been... | fork F-A3 | `s 76(4) the company is taken to have given the assistance in connection with the acquisition` |
| s 76(5) | 7412-7419 | (5) If a company contravenes subsection (1) or (... | fork F-A5 | `s 76(5) the company is guilty of an offence by contravening subsection (1) or (1A)`<br>`s 76(5) the officer is guilty of the offence this subsection creates`<br>`s 76(5) the most the officer may be sentenced to on conviction`<br>`s 76(5) an officer of the company must not be in default when the company contravenes subsection (1) or (1A)` |
| s 76(6) | 7420-7428 | (6) Where a person is convicted of an offence un... | fork F-A6 | `s 76(6) the Court may order the convicted person to pay compensation`<br>`s 76(6) the order may be enforced as if it were a judgment of the Court` |
| s 76(7) | 7429-7435 | (7) The power of a Court under section 391 to re... | encoded | `s 76(7) the power of the Court under section 391 extends to relieving the person from the liability to have an order made under subsection (6)` |
| s 76(8) | 7436-7437 | (8) Nothing in subsection (1) or (1A) prohibits ... | fork F-A7 | `s 76(8)(a) the act is one that subsections (1) and (1A) do not prohibit because it is a lawful dividend`<br>`s 76(8)(aa) the act is one that subsections (1) and (1A) do not prohibit because it is a distribution in a winding up`<br>`s 76(8)(b) the act is one that subsections (1) and (1A) do not prohibit because it is a payment on a reduction of capital`<br>`s 76(8)(c) the act is one that subsections (1) and (1A) do not prohibit because it is the discharge of a liability incurred in good faith`<br>`s 76(8)(d) the act is one that subsections (1) and (1A) do not prohibit because it is done under an order made under section 210`<br>`s 76(8)(e) the act is one that subsections (1) and (1A) do not prohibit because it is done under an arrangement under section 178 of the Insolvency, Restructuring and Dissolution Act 2018`<br>`s 76(8)(f) the act is one that subsections (1) and (1A) do not prohibit because it is done under an arrangement binding on creditors under section 187 of the Insolvency, Restructuring and Dissolution Act 2018`<br>`s 76(8)(g) the act is one that subsections (1) and (1A) do not prohibit because it is a guarantee or security by a subsidiary of a borrowing corporation`<br>`s 76(8)(ga) the act is one that subsections (1) and (1A) do not prohibit because it is a representation, warranty or indemnity on an offer to the public`<br>`s 76(8)(h) the act is one that subsections (1) and (1A) do not prohibit because it is a purchase of the company's shares under an order of a Court`<br>`s 76(8)(i) the act is one that subsections (1) and (1A) do not prohibit because it is a lien on shares that are not fully paid`<br>`s 76(8)(j) the act is one that subsections (1) and (1A) do not prohibit because it is an agreement for payment by instalments`<br>`s 76(8)(k) the act is one that subsections (1) and (1A) do not prohibit because it is an allotment of bonus shares`<br>`s 76(8)(l) the act is one that subsections (1) and (1A) do not prohibit because it is a redemption in accordance with the constitution`<br>`s 76(8)(m) the act is one that subsections (1) and (1A) do not prohibit because it is the payment of the costs of an odd-lot scheme` |
| s 76(8)(a) | 7438-7440 | (a) a distribution of a company’s assets by way ... | fork F-A7 | `s 76(8)(a) the act is one that subsections (1) and (1A) do not prohibit because it is a lawful dividend` |
| s 76(8)(aa) | 7441-7445 | (aa) a distribution in the course of a company’s... | fork F-A7 | `s 76(8)(aa) the act is one that subsections (1) and (1A) do not prohibit because it is a distribution in a winding up` |
| s 76(8)(b) | 7446-7448 | (b) a payment made by a company pursuant to a re... | fork F-A7 | `s 76(8)(b) the act is one that subsections (1) and (1A) do not prohibit because it is a payment on a reduction of capital` |
| s 76(8)(c) | 7449-7452 | (c) the discharge by a company of a liability of... | fork F-A7 | `s 76(8)(c) the act is one that subsections (1) and (1A) do not prohibit because it is the discharge of a liability incurred in good faith` |
| s 76(8)(d) | 7453-7455 | (d) anything done pursuant to an order of Court ... | fork F-A7 | `s 76(8)(d) the act is one that subsections (1) and (1A) do not prohibit because it is done under an order made under section 210` |
| s 76(8)(e) | 7456-7459 | (e) anything done under an arrangement made purs... | fork F-A7 | `s 76(8)(e) the act is one that subsections (1) and (1A) do not prohibit because it is done under an arrangement under section 178 of the Insolvency, Restructuring and Dissolution Act 2018` |
| s 76(8)(f) | 7460-7464 | (f) anything done under an arrangement made betw... | fork F-A7 | `s 76(8)(f) the act is one that subsections (1) and (1A) do not prohibit because it is done under an arrangement binding on creditors under section 187 of the Insolvency, Restructuring and Dissolution Act 2018` |
| s 76(8)(g) | 7465-7468 | (g) where a corporation is a borrowing corporati... | fork F-A7 | `s 76(8)(g) the act is one that subsections (1) and (1A) do not prohibit because it is a guarantee or security by a subsidiary of a borrowing corporation` |
| s 76(8)(g)(i) | 7469-7475 | (i) the giving, in good faith and in the ordinar... | fork F-A7 | `s 76(8)(g) the act is one that subsections (1) and (1A) do not prohibit because it is a guarantee or security by a subsidiary of a borrowing corporation` |
| s 76(8)(g)(ii) | 7476-7480 | (ii) the provision, in good faith and in the ord... | fork F-A7 | `s 76(8)(g) the act is one that subsections (1) and (1A) do not prohibit because it is a guarantee or security by a subsidiary of a borrowing corporation` |
| s 76(8)(ga) | 7481-7486 | (ga) the giving by a company in good faith and i... | fork F-A7 | `s 76(8)(ga) the act is one that subsections (1) and (1A) do not prohibit because it is a representation, warranty or indemnity on an offer to the public` |
| s 76(8)(h) | 7487-7492 | (h) the purchase by a company of shares in the c... | fork F-A7 | `s 76(8)(h) the act is one that subsections (1) and (1A) do not prohibit because it is a purchase of the company's shares under an order of a Court` |
| s 76(8)(i) | 7493-7498 | (i) the creation or acquisition, in good faith a... | fork F-A7 | `s 76(8)(i) the act is one that subsections (1) and (1A) do not prohibit because it is a lien on shares that are not fully paid` |
| s 76(8)(j) | 7499-7503 | (j) the entering into, in good faith and in the ... | fork F-A7 | `s 76(8)(j) the act is one that subsections (1) and (1A) do not prohibit because it is an agreement for payment by instalments` |
| s 76(8)(k) | 7504-7505 | (k) an allotment of bonus shares; | fork F-A7 | `s 76(8)(k) the act is one that subsections (1) and (1A) do not prohibit because it is an allotment of bonus shares` |
| s 76(8)(l) | 7506-7508 | (l) a redemption of redeemable shares of a compa... | fork F-A7 | `s 76(8)(l) the act is one that subsections (1) and (1A) do not prohibit because it is a redemption in accordance with the constitution` |
| s 76(8)(m) | 7509-7517 | (m) the payment of some or all of the costs by a... | fork F-A7 | `s 76(8)(m) the act is one that subsections (1) and (1A) do not prohibit because it is the payment of the costs of an odd-lot scheme` |
| s 76(8)(n) | 7518-7521 | (n) is to be construed as implying that a partic... | encoded | `s 76(8)(n) subsection (8) implies that the act would otherwise be prohibited by subsection (1) or (1A)` |
| s 76(8)(o) | 7522-7529 | (o) is to be construed as limiting the operation... | encoded | `s 76(8)(o) subsection (8) limits the operation of a rule of law permitting the act` |
| s 76(8A) | 7530-7531 | (8A) For the purposes of subsection (8)(m) — | encoded | `s 76(8A)(a) the holding is an odd-lot` |
| s 76(8A)(a) | 7532-7535 | (a) an “odd‑lot” means any amount of shares in t... | encoded | `s 76(8A)(a) the holding is an odd-lot` |
| s 76(8A)(b) | 7536-7541 | (b) a “board lot” means a standard unit of tradi... | encoded | `s 76(8A)(b) the amount of shares is a board lot` |
| s 76(8A)(c) | 7542-7547 | (c) the reference to “rounding off any odd‑lots”... | encoded | `s 76(8A)(c) the act is within rounding off any odd-lots` |
| s 76(9) | 7548-7549 | (9) Nothing in subsection (1) or (1A) prohibits ... | fork F-A7 | `s 76(9)(a) the act is one that subsections (1) and (1A) do not prohibit because it is ordinary banking, finance or insurance business`<br>`s 76(9)(b) the act is one that subsections (1) and (1A) do not prohibit because it is assistance for the acquisition of shares for employees`<br>`s 76(9)(c) the act is one that subsections (1) and (1A) do not prohibit because it is a buy-back in accordance with sections 76B to 76G` |
| s 76(9)(a) | 7550-7558 | (a) the making of a loan, or the giving of a gua... | fork F-A7 | `s 76(9)(a) the act is one that subsections (1) and (1A) do not prohibit because it is ordinary banking, finance or insurance business` |
| s 76(9)(a)(i) | 7559-7563 | (i) the lending of money, or the giving of guara... | fork F-A7 | `s 76(9)(a) the act is one that subsections (1) and (1A) do not prohibit because it is ordinary banking, finance or insurance business` |
| s 76(9)(a)(ii) | 7564-7570 | (ii) the loan that is made by the company, or, w... | fork F-A7 | `s 76(9)(a) the act is one that subsections (1) and (1A) do not prohibit because it is ordinary banking, finance or insurance business` |
| s 76(9)(b) | 7571-7580 | (b) the giving by a company of financial assista... | fork F-A7 | `s 76(9)(b) the act is one that subsections (1) and (1A) do not prohibit because it is assistance for the acquisition of shares for employees` |
| s 76(9)(c) | 7581-7589 | (c) the purchase or acquisition or proposed purc... | fork F-A7 | `s 76(9)(c) the act is one that subsections (1) and (1A) do not prohibit because it is a buy-back in accordance with sections 76B to 76G` |
| s 76(9A) | 7590-7595 | (9A) Nothing in subsection (1) prohibits the giv... | fork F-A7 | `s 76(9A)(a) the assistance is within 10 percent of paid-up capital and reserves`<br>`s 76(9A) subsection (1) does not prohibit the giving of the assistance` |
| s 76(9A)(a) | 7596-7600 | (a) the amount of the financial assistance, toge... | encoded | `s 76(9A)(a) the assistance is within 10 percent of paid-up capital and reserves` |
| s 76(9A)(a)(i) | 7601-7602 | (i) the total paid‑up capital of the company; an... | encoded | `s 76(9A)(a) the assistance is within 10 percent of paid-up capital and reserves` |
| s 76(9A)(a)(ii) | 7603-7604 | (ii) the reserves of the company, | encoded | `s 76(9A)(a) the assistance is within 10 percent of paid-up capital and reserves` |
| s 76(9A)(a) (continuation after its sub-paragraphs) | 7605-7607 | (a) as disclosed in the most recent financial st... | encoded | `s 76(9A)(a) the assistance is within 10 percent of paid-up capital and reserves` |
| s 76(9A)(b) | 7608-7610 | (b) the company receives fair value in connectio... | encoded | `s 76(9A)(b) the company receives fair value` |
| s 76(9A)(c) | 7611-7613 | (c) the board of directors of the company passes... | encoded | `s 76(9A)(c) the board has passed the resolution the paragraph requires` |
| s 76(9A)(c)(i) | 7614-7615 | (i) the company should give the assistance; | encoded | `s 76(9A)(c) the board has passed the resolution the paragraph requires` |
| s 76(9A)(c)(ii) | 7616-7618 | (ii) giving the assistance is in the best intere... | encoded | `s 76(9A)(c) the board has passed the resolution the paragraph requires` |
| s 76(9A)(c)(iii) | 7619-7621 | (iii) the terms and conditions under which the a... | encoded | `s 76(9A)(c) the board has passed the resolution the paragraph requires` |
| s 76(9A)(d) | 7622-7624 | (d) the resolution sets out in full the grounds ... | encoded | `s 76(9A)(d) the resolution sets out the grounds` |
| s 76(9A)(e) | 7625-7627 | (e) all the directors of the company make a solv... | fork F-A9 | `s 76(9A)(e) all the directors have made a solvency statement` |
| s 76(9A)(f) | 7628-7631 | (f) within 10 business days of providing the fin... | fork F-A8 | `s 76(9A)(f) the company has sent each member the notice in time` |
| s 76(9A)(f)(i) | 7632-7638 | (i) the class and number of shares or units of s... | fork F-A8 | `s 76(9A)(f) the company has sent each member the notice in time` |
| s 76(9A)(f)(ii) | 7639-7641 | (ii) the consideration paid or payable for those... | fork F-A8 | `s 76(9A)(f) the company has sent each member the notice in time` |
| s 76(9A)(f)(iii) | 7642-7646 | (iii) the identity of the person receiving the f... | fork F-A8 | `s 76(9A)(f) the company has sent each member the notice in time` |
| s 76(9A)(f)(iv) | 7647-7649 | (iv) the nature and, if quantifiable, the amount... | fork F-A8 | `s 76(9A)(f) the company has sent each member the notice in time` |
| s 76(9A)(g) | 7650-7657 | (g) not later than the business day next followi... | fork F-A8 | `s 76(9A)(g) the company has lodged the copies with the Registrar in time` |
| s 76(9B) | 7658-7663 | (9B) Nothing in subsection (1) prohibits the giv... | fork F-A7 | `s 76(9B)(a) the board has passed the resolution the paragraph requires`<br>`s 76(9B) subsection (1) does not prohibit the giving of the assistance` |
| s 76(9B)(a) | 7664-7666 | (a) the board of directors of the company passes... | encoded | `s 76(9B)(a) the board has passed the resolution the paragraph requires` |
| s 76(9B)(a)(i) | 7667-7668 | (i) the company should give the assistance; | encoded | `s 76(9B)(a) the board has passed the resolution the paragraph requires` |
| s 76(9B)(a)(ii) | 7669-7671 | (ii) giving the assistance is in the best intere... | encoded | `s 76(9B)(a) the board has passed the resolution the paragraph requires` |
| s 76(9B)(a)(iii) | 7672-7674 | (iii) the terms and conditions under which the a... | encoded | `s 76(9B)(a) the board has passed the resolution the paragraph requires` |
| s 76(9B)(b) | 7675-7677 | (b) the resolution sets out in full the grounds ... | encoded | `s 76(9B)(b) the resolution sets out the grounds` |
| s 76(9B)(c) | 7678-7680 | (c) all the directors of the company make a solv... | fork F-A9 | `s 76(9B)(c) all the directors have made a solvency statement` |
| s 76(9B)(d) | 7681-7690 | (d) not later than the business day next followi... | fork F-A8 | `s 76(9B)(d) the company has sent the members the notice in time` |
| s 76(9B)(d)(i) | 7691-7692 | (i) the directors’ resolution mentioned in parag... | fork F-A8 | `s 76(9B)(d) the company has sent the members the notice in time` |
| s 76(9B)(d)(ii) | 7693-7696 | (ii) the class and number of shares or units of ... | fork F-A8 | `s 76(9B)(d) the company has sent the members the notice in time` |
| s 76(9B)(d)(iii) | 7697-7699 | (iii) the consideration payable for those shares... | fork F-A8 | `s 76(9B)(d) the company has sent the members the notice in time` |
| s 76(9B)(d)(iv) | 7700-7704 | (iv) the identity of the person receiving the fi... | fork F-A8 | `s 76(9B)(d) the company has sent the members the notice in time` |
| s 76(9B)(d)(v) | 7705-7707 | (v) the nature and, if quantifiable, the amount ... | fork F-A8 | `s 76(9B)(d) the company has sent the members the notice in time` |
| s 76(9B)(d)(vi) | 7708-7713 | (vi) such further information and explanation as... | fork F-A8 | `s 76(9B)(d) the company has sent the members the notice in time` |
| s 76(9B)(e) | 7714-7715 | (e) a resolution is passed — | encoded | `s 76(9B)(e) the members have passed the resolution the paragraph requires` |
| s 76(9B)(e)(i) | 7716-7719 | (i) by all the members of the company present an... | encoded | `s 76(9B)(e) the members have passed the resolution the paragraph requires` |
| s 76(9B)(e)(ii) | 7720-7723 | (ii) if the resolution is proposed to be passed ... | encoded | `s 76(9B)(e) the members have passed the resolution the paragraph requires` |
| s 76(9B)(e) (continuation after its sub-paragraphs) | 7724-7725 | (e) to give that assistance; | encoded | `s 76(9B)(e) the members have passed the resolution the paragraph requires` |
| s 76(9B)(f) | 7726-7734 | (f) not later than the business day next followi... | fork F-A8 | `s 76(9B)(f) the company has lodged the copies with the Registrar in time` |
| s 76(9B)(g) | 7735-7739 | (g) the financial assistance is given not more t... | fork F-A8 | `s 76(9B)(g) the assistance is given within 12 months of the resolution` |
| s 76(9BA) | 7740-7745 | (9BA) Nothing in subsection (1) prohibits the gi... | fork F-A7, F-A10 | `s 76(9BA)(a) giving the assistance does not materially prejudice the company, its shareholders or its creditors`<br>`s 76(9BA) subsection (1) does not prohibit the giving of the assistance` |
| s 76(9BA)(a) | 7746-7747 | (a) giving the assistance does not materially pr... | fork F-A10 | `s 76(9BA)(a) giving the assistance does not materially prejudice the company, its shareholders or its creditors` |
| s 76(9BA)(a)(i) | 7748-7749 | (i) the interests of the company or its sharehol... | fork F-A10 | `s 76(9BA)(a) giving the assistance does not materially prejudice the company, its shareholders or its creditors` |
| s 76(9BA)(a)(ii) | 7750-7751 | (ii) the company’s ability to pay its creditors; | fork F-A10 | `s 76(9BA)(a) giving the assistance does not materially prejudice the company, its shareholders or its creditors` |
| s 76(9BA)(b) | 7752-7754 | (b) the board of directors of the company passes... | encoded | `s 76(9BA)(b) the board has passed the resolution the paragraph requires` |
| s 76(9BA)(b)(i) | 7755-7756 | (i) the company should give the assistance; and | encoded | `s 76(9BA)(b) the board has passed the resolution the paragraph requires` |
| s 76(9BA)(b)(ii) | 7757-7760 | (ii) the terms and conditions under which the as... | encoded | `s 76(9BA)(b) the board has passed the resolution the paragraph requires` |
| s 76(9BA)(c) | 7761-7763 | (c) the resolution sets out in full the grounds ... | encoded | `s 76(9BA)(c) the resolution sets out the grounds` |
| s 76(9BA)(d) | 7764-7768 | (d) the company lodges with the Registrar a copy... | encoded | `s 76(9BA)(d) the company has lodged a copy of the resolution with the Registrar` |
| s 76(9C) | 7769-7771 | (9C) A company must not give financial assistanc... | fork F-A11 | `s 76(9C) the company is barred from giving the assistance under subsection (9A) or (9B)`<br>`s 76(9C) a company must not give the assistance under subsection (9A) or (9B) once a director has ceased to be satisfied` |
| s 76(9C)(a) | 7772-7774 | (a) any of the directors who voted in favour of ... | fork F-A11 | `s 76(9C) the company is barred from giving the assistance under subsection (9A) or (9B)`<br>`s 76(9C) a company must not give the assistance under subsection (9A) or (9B) once a director has ceased to be satisfied` |
| s 76(9C)(a)(i) | 7775-7777 | (i) ceases to be satisfied that the giving of th... | fork F-A11 | `s 76(9C) the company is barred from giving the assistance under subsection (9A) or (9B)`<br>`s 76(9C) a company must not give the assistance under subsection (9A) or (9B) once a director has ceased to be satisfied` |
| s 76(9C)(a)(ii) | 7778-7781 | (ii) ceases to be satisfied that the terms and c... | fork F-A11 | `s 76(9C) the company is barred from giving the assistance under subsection (9A) or (9B)`<br>`s 76(9C) a company must not give the assistance under subsection (9A) or (9B) once a director has ceased to be satisfied` |
| s 76(9C)(b) | 7782-7787 | (b) any of the directors no longer has reasonabl... | fork F-A11 | `s 76(9C) the company is barred from giving the assistance under subsection (9A) or (9B)`<br>`s 76(9C) a company must not give the assistance under subsection (9A) or (9B) once a director has ceased to be satisfied` |
| s 76(9CA) | 7788-7796 | (9CA) A company must not give financial assistan... | fork F-A11 | `s 76(9CA) the company is barred from giving the assistance under subsection (9BA)`<br>`s 76(9CA) a company must not give the assistance under subsection (9BA) once a director has ceased to be satisfied` |
| s 76(9D) | 7797-7804 | (9D) A director of a company is not relieved of ... | encoded | `s 76(9D) the director is relieved of the director's duty to the company by the resolution` |
| s 76(9D)(a) | 7805-7808 | (a) the passing of a resolution by the board of ... | encoded | `s 76(9D) the director is relieved of the director's duty to the company by the resolution` |
| s 76(9D)(b) | 7809-7815 | (b) the passing of a resolution by the board of ... | encoded | `s 76(9D) the director is relieved of the director's duty to the company by the resolution` |
| s 76(10) | 7816-7821 | (10) Nothing in subsection (1) prohibits the giv... | fork F-A7, F-A13 | `s 76(10)(a) the company has resolved by special resolution to give the assistance`<br>`s 76(10) subsection (1) does not prohibit the giving of the assistance` |
| s 76(10)(a) | 7822-7825 | (a) the company, by special resolution, resolves... | encoded | `s 76(10)(a) the company has resolved by special resolution to give the assistance` |
| s 76(10)(b) | 7826-7827 | (b) where — | fork F-A13 | `s 76(10)(b) paragraph (b) applies to the company` |
| s 76(10)(b)(i) | 7828-7833 | (i) the company is a subsidiary of a listed corp... | fork F-A13 | `s 76(10)(b) paragraph (b) applies to the company` |
| s 76(10)(b)(ii) | 7834-7837 | (ii) the company is not a subsidiary of a listed | fork F-A13 | `s 76(10)(b) paragraph (b) applies to the company` |
| s 76(10)(b) (continuation after its sub-paragraphs) | 7838-7841 | (b) the listed corporation or the ultimate holdi... | fork F-A13 | `s 76(10)(b) the listed corporation or ultimate holding company has approved the giving by special resolution` |
| s 76(10)(c) | 7842-7845 | (c) the notice specifying the intention to propo... | encoded | `s 76(10)(c) the notice and the statement are as the paragraph requires` |
| s 76(10)(c)(i) | 7846-7849 | (i) particulars of the financial assistance prop... | encoded | `s 76(10)(c) the notice and the statement are as the paragraph requires` |
| s 76(10)(c)(ii) | 7850-7857 | (ii) the effect that the giving of the financial... | encoded | `s 76(10)(c) the notice and the statement are as the paragraph requires` |
| s 76(10)(c) (continuation after its sub-paragraphs) | 7858-7870 | (c) and is accompanied by a copy of a statement ... | encoded | `s 76(10)(c) the notice and the statement are as the paragraph requires` |
| s 76(10)(d) | 7871-7878 | (d) the notice specifying the intention to propo... | fork F-A13 | `s 76(10)(d) the notice to the parent is accompanied by the notice and statement` |
| s 76(10)(e) | 7879-7884 | (e) not later than the day next following the da... | fork F-A8 | `s 76(10)(e) the copies have been lodged with the Registrar in time` |
| s 76(10)(f) | 7885-7887 | (f) the notice mentioned in paragraph (c) and a ... | encoded | `s 76(10)(f) the notice and the statement have been sent to the members and debenture holders` |
| s 76(10)(f)(i) | 7888-7889 | (i) all members of the company; | encoded | `s 76(10)(f) the notice and the statement have been sent to the members and debenture holders` |
| s 76(10)(f)(ii) | 7890-7892 | (ii) all trustees for debenture holders of the c... | encoded | `s 76(10)(f) the notice and the statement have been sent to the members and debenture holders` |
| s 76(10)(f)(iii) | 7893-7899 | (iii) if there are no trustees for, or for a par... | encoded | `s 76(10)(f) the notice and the statement have been sent to the members and debenture holders` |
| s 76(10)(g) | 7900-7902 | (g) the notice mentioned in paragraph (d) and th... | fork F-A13 | `s 76(10)(g) the notice and the documents have been sent to the members and debenture holders of the parent` |
| s 76(10)(g)(i) | 7903-7905 | (i) all members of the listed corporation or of ... | fork F-A13 | `s 76(10)(g) the notice and the documents have been sent to the members and debenture holders of the parent` |
| s 76(10)(g)(ii) | 7906-7908 | (ii) all trustees for debenture holders of the l... | fork F-A13 | `s 76(10)(g) the notice and the documents have been sent to the members and debenture holders of the parent` |
| s 76(10)(g)(iii) | 7909-7917 | (iii) if there are no trustees for, or for a par... | fork F-A13 | `s 76(10)(g) the notice and the documents have been sent to the members and debenture holders of the parent` |
| s 76(10)(h) | 7918-7927 | (h) within 21 days after the date on which the r... | fork F-A14 | `s 76(10)(h) the notice has been published in time` |
| s 76(10)(h)(i) | 7928-7930 | (i) setting out the terms of the resolution ment... | fork F-A14 | `s 76(10)(h) the notice has been published in time` |
| s 76(10)(h)(ii) | 7931-7935 | (ii) stating that any of the persons referred to... | fork F-A14 | `s 76(10)(h) the notice has been published in time` |
| s 76(10)(h) (continuation after its sub-paragraphs) | 7936-7938 | (h) is published in a daily newspaper circulatin... | fork F-A14 | `s 76(10)(h) the notice has been published in time` |
| s 76(10)(i) | 7939-7945 | (i) no application opposing the giving of the fi... | encoded | `s 76(10)(i) no application stands in the way of the giving of the assistance` |
| s 76(10)(j) | 7946-7949 | (j) the financial assistance is given in accorda... | fork F-A12 | `s 76(10)(j) the assistance is given in accordance with the resolution and not too early` |
| s 76(10)(j)(i) | 7950-7953 | (i) in a case to which sub‑paragraph (ii) does n... | fork F-A12 | `s 76(10)(j) the assistance is given in accordance with the resolution and not too early` |
| s 76(10)(j)(ii) | 7954-7966 | (ii) if an application or applications has or ha... | fork F-A12 | `s 76(10)(j) the assistance is given in accordance with the resolution and not too early` |
| s 76(10A) | 7967-7975 | (10A) If the resolution mentioned in subsection ... | fork F-A15 | `s 76(10A) paragraph (f) or (g) has been complied with in time for a resolution by written means` |
| s 76(10A)(a) | 7976-7978 | (a) agreement to the resolution is sought in acc... | fork F-A15 | `s 76(10A) paragraph (f) or (g) has been complied with in time for a resolution by written means` |
| s 76(10A)(b) | 7979-7984 | (b) documents referred to in section 183(3A) in ... | fork F-A15 | `s 76(10A) paragraph (f) or (g) has been complied with in time for a resolution by written means` |
| s 76(11) | 7985-7992 | (11) Where, on application to the Court by a com... | fork F-A6 | `s 76(11) the Court may declare that the provisions of subsection (10) have been complied with` |
| s 76(12) | 7993-7998 | (12) Where a special resolution mentioned in sub... | fork F-A6 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(a) | 7999-8000 | (a) by a member of the company; | fork F-A6 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(b) | 8001-8002 | (b) by a trustee for debenture holders of the co... | fork F-A6 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(c) | 8003-8004 | (c) by a debenture holder of the company; | fork F-A6 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(d) | 8005-8006 | (d) by a creditor of the company; | fork F-A6 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(e) | 8007-8008 | (e) if subsection (10)(b) applies by — | fork F-A6, F-A7 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(e)(i) | 8009-8012 | (i) a member of the listed corporation or ultima... | fork F-A6, F-A7 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(e)(ii) | 8013-8015 | (ii) a trustee for debenture holders of that lis... | fork F-A6, F-A7 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(e)(iii) | 8016-8021 | (iii) a debenture holder of that listed corporat... | fork F-A6, F-A7 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(e)(iv) | 8022-8024 | (iv) a creditor of that listed corporation or ul... | fork F-A6, F-A7 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(12)(f) | 8025-8026 | (f) by the Registrar. | fork F-A6 | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(13) | 8027-8031 | (13) Where an application or applications opposi... | fork F-A6 | `s 76(13)(a) the Court must have regard to the rights and interests of the members and of the creditors` |
| s 76(13)(a) | 8032-8037 | (a) must, in determining what order or orders to... | fork F-A6 | `s 76(13)(a) the Court must have regard to the rights and interests of the members and of the creditors` |
| s 76(13)(b) | 8038-8040 | (b) must not make an order approving the giving ... | encoded | `s 76(13)(b) the Court is barred from making an order approving the giving of the assistance` |
| s 76(13)(b)(i) | 8041-8044 | (i) the company has disclosed to the members of ... | encoded | `s 76(13)(b) the Court is barred from making an order approving the giving of the assistance` |
| s 76(13)(b)(ii) | 8045-8052 | (ii) the proposed financial assistance would not... | encoded | `s 76(13)(b) the Court is barred from making an order approving the giving of the assistance` |
| s 76(13)(b) (continuation after its sub-paragraphs) | 8053-8054 | (b) and may do all or any of the following: | fork F-A6 | `s 76(13) the Court may make the order` |
| s 76(13)(b)(iii) | 8055-8059 | (iii) if it thinks fit, make an order for the pu... | fork F-A6 | `s 76(13) the Court may make the order` |
| s 76(13)(b)(iv) | 8060-8068 | (iv) if it thinks fit, adjourn the proceedings i... | fork F-A6 | `s 76(13) the Court may make the order` |
| s 76(13)(b)(v) | 8069-8072 | (v) give such ancillary or consequential directi... | fork F-A6 | `s 76(13) the Court may make the order` |
| s 76(13)(b)(vi) | 8073-8077 | (vi) make an order disapproving the giving of th... | fork F-A6 | `s 76(13) the Court may make the order` |
| s 76(14) | 8078-8082 | (14) Where the Court makes an order under this s... | encoded | `s 76(14) the company has lodged a copy of the order with the Registrar in time`<br>`s 76(14) the company must lodge a copy of the order with the Registrar within 14 days` |
| s 76(15) | 8083-8091 | (15) The passing of a special resolution by a co... | encoded | `s 76(15) the director is relieved of the director's duty to the company by the special resolution or the Court's approval` |
| s 76(16) | 8092-8096 | (16) A reference in this section to an acquisiti... | encoded | `s 76(16) the way of acquiring is within the acquisition the section speaks of` |
| s 76(17) | 8097-8101 | (17) This section does not apply in relation to ... | fork F-A4 | `s 76(17) the section does not apply to the act or thing` |
| s 76A marginal heading | 8102-8103 | Consequences of company financing dealings in it... | inert, reason 1 (a marginal heading, not operative) | - |
| s 76A(1) | 8104-8106 | 76A.—(1) The following contracts or transactions... | fork F-A16 | `s 76A(1) the contract or transaction is void` |
| s 76A(1)(a) | 8107-8114 | (a) a contract or transaction by which a company... | fork F-A16 | `s 76A(1) the contract or transaction is void` |
| s 76A(1)(b) | 8115-8121 | (b) a contract or transaction by which a company... | fork F-A16 | `s 76A(1) the contract or transaction is void` |
| s 76A(1A) | 8122-8129 | (1A) Subsection (1) does not apply to a disposit... | fork F-A6 | `s 76A(1A) subsection (1) applies to the disposition`<br>`s 76A(1A) the Court may order the transfer of the shares acquired in contravention of subsection (1)` |
| s 76A(2) | 8130-8137 | (2) Subject to subsection (1), a contract or tra... | fork F-A7, F-A16 | `s 76A(2) the contract or transaction is one to which subsection (2) applies`<br>`s 76A(2) the company may avoid the contract or transaction by written notice` |
| s 76A(3) | 8138-8143 | (3) The Court may, on the application of a membe... | fork F-A17 | `s 76A(3) the Court may authorise the applicant to give notice in the name of the company` |
| s 76A(4) | 8144-8145 | (4) Where — | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(4)(a) | 8146-8148 | (a) a company makes or performs a contract, or e... | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(4)(b) | 8149-8154 | (b) the contract is made or performed, or the tr... | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(4)(c) | 8155-8162 | (c) the Court is satisfied, on the application o... | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(4)(c)(i) | 8163-8165 | (i) the making or performance of the contract or... | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(4)(c)(ii) | 8166-8168 | (ii) the making or performance of a related cont... | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(4)(c)(iii) | 8169-8171 | (iii) the contract or transaction being void by ... | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(4)(c)(iv) | 8172-8183 | (iv) a related contract or transaction being voi... | fork F-A6 | `s 76A(4) the Court may make an order against the person` |
| s 76A(5) | 8184-8185 | (5) The orders that may be made under subsection... | encoded | `s 76A(5) the order is one of the orders mentioned in subsection (5)` |
| s 76A(5)(a) | 8186-8188 | (a) an order directing a person to refund money ... | encoded | `s 76A(5) the order is one of the orders mentioned in subsection (5)` |
| s 76A(5)(b) | 8189-8192 | (b) an order directing a person to pay to the co... | encoded | `s 76A(5) the order is one of the orders mentioned in subsection (5)` |
| s 76A(5)(c) | 8193-8198 | (c) an order directing a person to indemnify the... | encoded | `s 76A(5) the order is one of the orders mentioned in subsection (5)` |
| s 76A(6) | 8199-8211 | (6) If a certificate signed by not less than 2 d... | encoded | `s 76A(6) the certificate is one that subsection (6) speaks of`<br>`s 76A(6)(a) the person is under a liability to have an order made against the person under subsection (4)` |
| s 76A(6)(a) | 8212-8217 | (a) the person to whom the certificate is given ... | encoded | `s 76A(6) the certificate is one that subsection (6) speaks of`<br>`s 76A(6)(a) the person is under a liability to have an order made against the person under subsection (4)` |
| s 76A(6)(b) | 8218-8226 | (b) any such contract or transaction is not inva... | encoded | `s 76A(6) the certificate is one that subsection (6) speaks of`<br>`s 76A(6)(b) the contract or transaction is invalid or voidable under subsection (2) by reason of the contravention` |
| s 76A(7) | 8227-8241 | (7) Subsection (6) does not apply in relation to... | fork F-A18 | `s 76A(7) subsection (6) does not apply to the person` |
| s 76A(8) | 8242-8247 | (8) For the purposes of subsection (7), a person... | fork F-A19 | `s 76A(8) the person is deemed to have been aware of the matter` |
| s 76A(9) | 8248-8254 | (9) In any proceeding, a document purporting to ... | fork F-A19 | `s 76A(9) the document is deemed to be a certificate given under subsection (6) and duly given` |
| s 76A(10) | 8255-8258 | (10) A person who has possession of a certificat... | fork F-A19 | `s 76A(10) the person is deemed to be the person to whom the certificate was given` |
| s 76A(11) | 8259-8270 | (11) If a person signs a certificate stating tha... | fork F-A5 | `s 76A(11) the person is guilty of the offence this subsection creates`<br>`s 76A(11) the most the person may be sentenced to on conviction`<br>`s 76A(11) a person must not sign a certificate that the requirements have been complied with when any had not`<br>`s 76A(11) the person is guilty of the offence and subsection (12) gives no defence` |
| s 76A(12) | 8271-8280 | (12) It is a defence to a prosecution for an off... | encoded | `s 76A(12) the subsection gives the defendant a defence on these facts` |
| s 76A(13) | 8281-8287 | (13) The power of a Court under section 391 to r... | encoded | `s 76A(13) the power of the Court under section 391 extends to relieving the person from the liability to have an order made under subsection (4)` |
| s 76A(14) | 8288-8297 | (14) If a company makes a contract or engages in... | fork F-A3 | `s 76A(14) the other contract or transaction is deemed to be related to the firstmentioned one` |
| s 76A(15) | 8298-8311 | (15) Any rights or liabilities of a person under... | encoded | `s 76A(15) the right or liability is in addition to the rights and liabilities of the person apart from the section`<br>`s 76A(15) the section or the order prevails over the inconsistent right or liability` |

## Fork register (sga2)

Each entry: the provision and function, the readings seen, the one taken, the text that licenses it.
The comments in the layer-1 modules carry most of these ids (`{F-A7}`, `fork F-A1` and so on); where a function belongs to an entry but its comment does not say so, the coverage table's fork column (made by `work/forkmap.py` with a short list of additions) and this register are authoritative.
Where an entry is one of the two split sites, it names the line of `inputs/ENCODING-GUIDE.md` section 5 that the answer relies on, in the Guide's own words.
The Guide's lines used below are these (all from section 5, "Rulings on negatives and legal effects"):

- **In short:** "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit."
- **Periods ruling of 2026-11-05:** "(a) a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" ...: outside the scope the answer is `NOTHING`."
- **Delegated definitions and defences, 2026-11-05, (b):** "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts".
- **N2 (2026-11-04):** "flat negatives count as a no".
- **E1 (2026-11-04):** option C, per-section answers.
- **Grant ruling of 2026-11-12:** (1) `NOTHING`, with one fork line each, "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; (2) "keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question"; (3) "do not change, but list ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function".

**F-A1** (split site (i)).
`s 76(1)(a)`, `s 76(1)(b)` and `s 76(1) subsection (1) bars the company from giving the financial assistance` (lines 7323-7350).
Taken: `JUST FALSE` when an element of the prohibition is unmet (no assistance given; neither purpose nor connection nor deeming; neither an acquisition nor a proposed one; shares in a stranger), when an exception expressly provided by the Act applies, or when s 76(17) applies; `NOTHING` when the company is outside the class the subsection binds (`s 76(1) the company is one the subsection binds`: scope limit with no "only", periods ruling (c)).
Other reading: `NOTHING` for an unmet element (the facts bring the case outside the prohibition and the text is silent on it).
Guide line: grant ruling limit 2, "for a bar, a duty or the provision's own question"; and "a flat negative ("does not", "shall not", "may not")" (the text says "must not").

**F-A2** (split site (i)).
`s 76(1A) subsection (1A) bars the company from the act` (lines 7351-7369).
Taken: `JUST FALSE` for an act that is none of the four the subsection names, or where an exception or s 76(17) applies; the other reading is `NOTHING` for an act the subsection does not name.
Guide line: grant ruling limit 2, "the provision's own question".

**F-A3.**
`s 76(3)`, `s 76(4)` (lines 7379-7408) and `s 76A(14)` (lines 8288-8294): the deeming rules ("is taken to have given ... if", "is deemed ... to be related").
Taken: `JUST TRUE` when the "if" holds, `NOTHING` when it fails, because a deeming adds to the ordinary meaning of "for the purpose of", "in connection with" and "related" and does not say that other cases are not so (In short: "says "includes""): this departs from marginal reading (a) on purpose.
Other reading: `JUST FALSE` (a failed "if" is the text's no).

**F-A4.**
`s 76(17) the section does not apply to the act or thing` (lines 8097-8100).
Taken: `JUST FALSE` when a limb of the "if" fails ("the exclusion does not take the act out of the section"); marginal reading (a).
Other reading: `NOTHING`, treating it as a carve-out like those of F-A7 (it has the same shape; I did not harmonise, and I flag the inconsistency here and under Marginal readings).
Guide line: In short, "a condition the text introduces with "if"".

**F-A5** (split site (i)).
`s 76(5) the officer is guilty of the offence this subsection creates` (lines 7412-7418) and `s 76A(11) the person is guilty of the offence this subsection creates` (lines 8259-8267).
Taken: `JUST FALSE` when an element of the offence is unmet (the company did not contravene, the person is not an officer, the officer is not in default; no certificate signed, no requirement unmet).
Other reading: `NOTHING`.
Guide line: grant ruling limit 2, "the provision's own question"; "shall be guilty" is the provision's own question.
The company's own position under s 76(5), "the company shall not be guilty of an offence", is a flat negative (N2): `JUST FALSE` where the company contravened (1) or (1A), `NOTHING` where it did not.

**F-A6 and G1** (split site (ii)).
The "may" functions (and one "must") gated by "where", "when" or "on application": the periods ruling item (b) says `JUST FALSE` when the gate fails; the grant rule points the other way.
Taken: `JUST FALSE`, as the periods ruling says; I did not decide the group by myself, so it is listed here, **G1, 7 functions**, and the other reading is `NOTHING` for each:

1. `s 76(6) the Court may order the convicted person to pay compensation` ("Where a person is convicted ... and the Court ... is satisfied ...").
2. `s 76(11) the Court may declare that the provisions of subsection (10) have been complied with` ("Where, on application to the Court by a company, the Court is satisfied ...").
3. `s 76(12) the person may apply to the Court opposing the giving of the assistance` ("Where a special resolution ... is passed ... may be made, within the period of 21 days"); the 21 days is item (a), `JUST FALSE` outside it, and the period test comes before the list of applicants, so a late application by anyone answers `JUST FALSE`.
4. `s 76(13)(a) the Court must have regard ...` ("Where an application ... is made ..., the Court (a) must ..."): a duty, not a "may", listed here because the same gate decides it.
5. `s 76(13) the Court may make the order` ("Where an application ... may do all or any of the following").
6. `s 76A(1A) the Court may order the transfer of the shares acquired in contravention of subsection (1)` ("a Court, on being satisfied ... may, on the application of the Registrar or any other person").
7. `s 76A(4) the Court may make an order against the person` ("Where (a) ...; (b) ...; and (c) the Court is satisfied ...").

**G2** ("entitled"-named functions): **0**.
Nothing in the range gives an "entitlement"; the rights of s 76A(2), (3) and (6) are powers and immunities.

**F-A7** (grant ruling limit 1).
A carve-out or permission whose "if" gate fails answers `NOTHING`, not `JUST FALSE`.
The functions are named for a permission ("do not prohibit", "may avoid", "may apply") rather than worded "may", so the grant ruling applies to them by its reason: "limits a grant or prohibition in its own wording and the case falls outside the limit" (In short).
The other reading is `JUST FALSE` (a failed "if" is the text's no, marginal reading (a)).
One line per function, **24 functions**:

- F-A7.1 `s 76(10) subsection (1) does not prohibit the giving of the assistance`: `JUST TRUE` when every paragraph is met, `NOTHING` when one is not (the route says nothing for the assistance, and subsection (1) decides); other reading `JUST FALSE`.
- F-A7.2 `s 76(12) the person may apply to the Court opposing the giving of the assistance`: the (e) persons (members, trustees, debenture holders and creditors of the parent) when subsection (10)(b) does not apply: `NOTHING` ("if subsection (10)(b) applies by"); `JUST TRUE` when it applies; other reading `JUST FALSE`.
- F-A7.3 `s 76(8)(a) the act is one that subsections (1) and (1A) do not prohibit because it is a lawful dividend`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.4 `s 76(8)(aa) the act is one that subsections (1) and (1A) do not prohibit because it is a distribution in a winding up`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.5 `s 76(8)(b) the act is one that subsections (1) and (1A) do not prohibit because it is a payment on a reduction of capital`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.6 `s 76(8)(c) the act is one that subsections (1) and (1A) do not prohibit because it is the discharge of a liability incurred in good faith`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.7 `s 76(8)(d) the act is one that subsections (1) and (1A) do not prohibit because it is done under an order made under section 210`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.8 `s 76(8)(e) the act is one that subsections (1) and (1A) do not prohibit because it is done under an arrangement under section 178 of the Insolvency, Restructuring and Dissolution Act 2018`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.9 `s 76(8)(f) the act is one that subsections (1) and (1A) do not prohibit because it is done under an arrangement binding on creditors under section 187 of the Insolvency, Restructuring and Dissolution Act 2018`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.10 `s 76(8)(g) the act is one that subsections (1) and (1A) do not prohibit because it is a guarantee or security by a subsidiary of a borrowing corporation`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.11 `s 76(8)(ga) the act is one that subsections (1) and (1A) do not prohibit because it is a representation, warranty or indemnity on an offer to the public`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.12 `s 76(8)(h) the act is one that subsections (1) and (1A) do not prohibit because it is a purchase of the company's shares under an order of a Court`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.13 `s 76(8)(i) the act is one that subsections (1) and (1A) do not prohibit because it is a lien on shares that are not fully paid`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.14 `s 76(8)(j) the act is one that subsections (1) and (1A) do not prohibit because it is an agreement for payment by instalments`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.15 `s 76(8)(k) the act is one that subsections (1) and (1A) do not prohibit because it is an allotment of bonus shares`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.16 `s 76(8)(l) the act is one that subsections (1) and (1A) do not prohibit because it is a redemption in accordance with the constitution`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.17 `s 76(8)(m) the act is one that subsections (1) and (1A) do not prohibit because it is the payment of the costs of an odd-lot scheme`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.18 `s 76(9)(a) the act is one that subsections (1) and (1A) do not prohibit because it is ordinary banking, finance or insurance business`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.19 `s 76(9)(b) the act is one that subsections (1) and (1A) do not prohibit because it is assistance for the acquisition of shares for employees`: `JUST TRUE` when every element of the paragraph holds, `NOTHING` when one fails; other reading `JUST FALSE`.
- F-A7.20 `s 76(9)(c) the act is one that subsections (1) and (1A) do not prohibit because it is a buy-back in accordance with sections 76B to 76G`: `JUST TRUE` when the buy-back is in accordance with ss 76B to 76G (a seam input), `NOTHING` otherwise; other reading `JUST FALSE`.
- F-A7.21 `s 76(9A) subsection (1) does not prohibit the giving of the assistance`: `JUST TRUE` when every paragraph is met, `NOTHING` when one is not (the route says nothing for the assistance, and subsection (1) decides); other reading `JUST FALSE`.
- F-A7.22 `s 76(9B) subsection (1) does not prohibit the giving of the assistance`: `JUST TRUE` when every paragraph is met, `NOTHING` when one is not (the route says nothing for the assistance, and subsection (1) decides); other reading `JUST FALSE`.
- F-A7.23 `s 76(9BA) subsection (1) does not prohibit the giving of the assistance`: `JUST TRUE` when every paragraph is met, `NOTHING` when one is not (the route says nothing for the assistance, and subsection (1) decides); other reading `JUST FALSE`.
- F-A7.24 `s 76A(2) the company may avoid the contract or transaction by written notice`: `JUST TRUE` when subsection (2) applies and the company gives written notice to the other party or parties, `NOTHING` otherwise; other reading `JUST FALSE`.

**F-A8.**
Periods stated as "within N business days of", "not later than the business day next following", "not later than the day next following", "not more than 12 months after": `s 76(9A)(f)`, `(9A)(g)`, `(9B)(d)`, `(9B)(f)`, `(9B)(g)`, `s 76(10)(e)`.
Taken: an act on the day itself or earlier counts (the keel's "last day of a number of business days after" with `AT MOST`, "not later than the end of a period after"); the text sets only an upper limit.
Other reading: the act must fall in a window that opens the day after the event (the keel's convention P2), as for the functions of F-A12, F-A14 and s 76(12), (14), whose text says "after".

**F-A9.**
`s 76(9A)(e)` and `s 76(9B)(c)`: "all the directors of the company make a solvency statement in relation to the giving of the financial assistance".
Taken: whether all the directors "made" it is a plain fact (`all the directors of the company have made the statement`), and the keel's `s 7A(1)` decides whether the statement is a solvency statement (which looks at signatures, the auditor's report and the opinions); both must hold, and the statement must concern the giving of financial assistance.
Other reading: "make" means "sign", so the number of signatures decides.

**F-A10.**
`s 76(9BA)(a)`: "giving the assistance does not materially prejudice (i) the interests of the company or its shareholders; or (ii) the company's ability to pay its creditors".
Taken: it must prejudice neither.
Other reading: it suffices that it does not prejudice one of them.

**F-A11.**
`s 76(9C)` and `s 76(9CA)`: "A company must not give financial assistance under ... if, before the assistance is given, ...".
Taken: `JUST FALSE` when none of the listed events has occurred (the bar is the provision's own question; marginal reading (a)), `NOTHING` when the assistance is not given under (9A), (9B) or (9BA) (scope).
Other reading: `NOTHING` where the "if" fails.

**F-A12.**
`s 76(10)(j)`: "not earlier than the expiration of the period mentioned in subsection (12)".
Taken: from the day after the last day of the 21 days.
Other reading: from the last day itself.

**F-A13.**
`s 76(10)(b) paragraph (b) applies`, `s 76(10)(b)` (approval), `s 76(10)(d)`, `s 76(10)(g)` and the route `s 76(10) subsection (1) does not prohibit ...`.
Paragraphs (b), (d) and (g) speak only of "the listed corporation or ... the ultimate holding company" of case (b).
Taken: where paragraph (b) does not apply they ask nothing: the approval, (d) and (g) functions answer `NOTHING` (limited by their own wording), and the route reads `NOTHING` there as met.
Other reading: they are unmet requirements for every company.

**F-A14.**
`s 76(10)(h)`: "within 21 days after the date on which the resolution mentioned in paragraph (a) is passed or, in a case to which paragraph (b) applies, the date on which the resolution referred to in that paragraph is passed, whichever is the later".
Taken: the later of the two dates starts the period.
Other reading: none seen in the text; recorded because the text offers two start dates.

**F-A15.**
`s 76(10A)`: "must be complied with at or before the time".
Taken: the two events are compared as days (a time of day is not asked).
Other reading: compare the time of day.

**F-A16** (split site (i)).
`s 76A(1) the contract or transaction is void` (lines 8104-8118).
Taken: `NOTHING` when the contract was not "made or entered into in contravention of section 76", and for any contract not in the two listed classes.
Other reading: `JUST FALSE` for the unmet element.
Guide line: In short, "limits a grant or prohibition in its own wording and the case falls outside the limit"; the list in (1) is not closed with "only".

**F-A17.**
`s 76A(3)`: "The Court may, on the application of a member ..., a holder of debentures ..., a trustee ... or a director".
Taken: `NOTHING` for an applicant not named (a grant limited to a named complement, grant ruling limit 1).
Other reading: `JUST FALSE` for any other applicant.

**F-A18.**
`s 76A(7)`: "Subsection (6) does not apply ... if the Court, on application ..., by order, declares ...".
Taken: `JUST FALSE` where the declaration has not been made (marginal reading (a)): the exclusion is not made out.
Other reading: `NOTHING`.

**F-A19.**
`s 76A(8)`, `(9)`, `(10)`: "in the absence of proof to the contrary, deemed".
Taken: `JUST FALSE` when proof to the contrary has been given (the deeming does not operate), `NOTHING` when the matter deemed does not arise.
Other reading: `NOTHING` when proof to the contrary has been given.

## Jural relations (sga2)

The text names few right-holders; where it does not, the cell says "not named".
The Court appears in the table only as the bearer or holder of a power, because the seat has no Court seat.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 76(1) | not named by the text (the claim is enforced through s 76(5), by prosecution, and s 76A(4), by the company or another who suffers loss) | a public company, or a company whose holding company or ultimate holding company is public: the duty not to give the financial assistance | `s 76(1) a company the subsection binds must not give the financial assistance`; `s 76(1) subsection (1) bars the company from giving the financial assistance`; `s 76(1) the company is one the subsection binds` |
| s 76(1)(a), (b) | none: they say which acquisitions the prohibition is about | - | `s 76(1)(a) ...`; `s 76(1)(b) ...` |
| s 76(1A) | not named | any company: the duty not to acquire its own shares or lend on their security, and the same for its holding company or ultimate holding company | four `SHANT` rules and `s 76(1A) subsection (1A) bars the company from the act` |
| s 76(2), (3), (4), (16) | none: a meaning and two deeming rules for the prohibition | - | `s 76(2) ...`; `s 76(3) ...`; `s 76(4) ...`; `s 76(16) ...` |
| s 76(17) | a company that does an act under a contract made before 15 May 1987, lawful apart from the Act: immunity from the section | no one may enforce the section against that act: disability | `s 76(17) the section does not apply to the act or thing` |
| s 76(5), the company | the company: immunity from conviction ("shall not be guilty ... despite section 407") | the prosecuting authority (not named): disability | `s 76(5) the company is guilty of an offence by contravening subsection (1) or (1A)` |
| s 76(5), the officer | the prosecuting authority and the Court (not named): power to convict and to sentence | each officer in default: liability to a fine of up to $20,000 or 3 years or both; and the duty not to be in default | `s 76(5) the officer is guilty ...`; `s 76(5) the most the officer may be sentenced to on conviction`; `s 76(5) an officer of the company must not be in default when the company contravenes subsection (1) or (1A)` |
| s 76(6) | the Court: power to order compensation on a conviction; the company or other person who suffered loss: the claim that the order creates, enforceable "as if it were a judgment of the Court" | the convicted person: liability to the order | `s 76(6) the Court may order the convicted person to pay compensation`; `s 76(6) the order may be enforced as if it were a judgment of the Court` |
| s 76(7) | the Court: power under s 391 to relieve a person from the liability to an order under (6) | the company or other person entitled to compensation: liability to the Court's relief | `s 76(7) the power of the Court under section 391 extends to ...` |
| s 76(8)(a) to (m) | the company: privilege to do each act (a lawful dividend, a distribution in a winding up, a reduction payment, the discharge of a liability, and so on) | any person who would complain of a contravention of (1) or (1A): no-right | `s 76(8)(a)` to `s 76(8)(m)` (15 functions) |
| s 76(8)(n), (o) | none: rules for reading subsection (8) | - | `s 76(8)(n) ...`; `s 76(8)(o) ...` |
| s 76(8A) | none: two definitions for (8)(m) and an extension of "rounding off" | - | `s 76(8A)(a)`, `(b)`, `(c)` |
| s 76(9)(a) to (c) | the company: privilege to do the act (ordinary banking, finance or insurance business; assistance for employees' shares; a buy-back under ss 76B to 76G) | any person who would complain: no-right | `s 76(9)(a)`, `(b)`, `(c)` |
| s 76(9A), (9B), (9BA) | the company: privilege to give the assistance when the conditions are met | any person who would complain of a contravention of (1): no-right | the condition functions of each and the route functions `s 76(9A) subsection (1) does not prohibit ...`, `s 76(9B) ...`, `s 76(9BA) ...` |
| s 76(9A)(f), (g); (9B)(d), (f); (9BA)(d) | each member (and the Registrar): the claim to the notice and to the lodged copies, not stated in terms (the text speaks of what the company "sends" and "lodges") | the company: duty to send and to lodge in time | `s 76(9A)(f)`, `(g)`; `s 76(9B)(d)`, `(f)`; `s 76(9BA)(d)` |
| s 76(9C), (9CA) | not named | the company: duty not to give the assistance under the routes once a director has ceased to be satisfied or no longer has reasonable grounds | `s 76(9C) a company must not give the assistance under subsection (9A) or (9B) once a director has ceased to be satisfied`; `s 76(9CA) ...`; the two bar functions |
| s 76(9D), (15) | the company: the claim against its director that the duty (under s 157 or otherwise, fiduciary or not) is not relieved by the resolution, the special resolution or the Court's approval | each director: the duty continues | `s 76(9D) the director is relieved ...`; `s 76(15) the director is relieved ...` |
| s 76(10) | the company: privilege to give the assistance when every paragraph is met | any person who would complain: no-right | the paragraph functions `s 76(10)(a)` to `(j)` and the route `s 76(10) subsection (1) does not prohibit ...` |
| s 76(10)(c) to (h) | members, trustees for debenture holders and debenture holders (and those of the parent where (b) applies): the claim to the notice and the statement and to the published notice | the company: duty to send, accompany and publish in time | `s 76(10)(c)`, `(d)`, `(e)`, `(f)`, `(g)`, `(h)` |
| s 76(10)(i), (j), (10A) | the persons who may oppose: the benefit of the waiting period and of the written-means timing | the company: disability from giving the assistance before the period ends or the Court has decided; duty to comply with (f) or (g) at or before the time | `s 76(10)(i)`, `(j)`; `s 76(10A) ...` |
| s 76(11) | the company: power to apply; the Court: power to declare | the persons who might oppose: liability to the declaration | `s 76(11) the Court may declare that ...` |
| s 76(12) | a member, a trustee for debenture holders, a debenture holder, a creditor, the Registrar (and the like persons of the parent where (10)(b) applies): power to apply to the Court within 21 days | the company: liability to the opposing application | `s 76(12) the person may apply to the Court opposing the giving of the assistance` |
| s 76(13)(a), (b) | the members, the creditors and their classes: the claim that the Court has regard to their rights and interests; the Court: powers to order a purchase of dissentient members' interests, to adjourn, to give directions, to disapprove or (subject to (b)) approve | the Court: duty to have regard; disability to approve unless satisfied of disclosure and of no material prejudice | `s 76(13)(a) ...`; `s 76(13)(b) the Court is barred ...`; `s 76(13) the Court may make the order` |
| s 76(14) | the Registrar (not named): the claim to a copy of the Court's order | the company: duty to lodge within 14 days after the order is made | `s 76(14) the company must lodge a copy of the order with the Registrar within 14 days` (rule); `s 76(14) the company has lodged a copy ... in time` |
| s 76A(1) | none: contracts of two listed kinds, made in contravention of s 76, are void; the effect is on the contract and not a relation between parties | - | `s 76A(1) the contract or transaction is void` |
| s 76A(1A) | a disposition of book-entry securities: immunity from (1); the Court: power, on the application of the Registrar or any other person, to order a transfer of the shares | the holder of the shares: liability to the transfer order | `s 76A(1A) subsection (1) applies to the disposition`; `s 76A(1A) the Court may order the transfer ...` |
| s 76A(2) | the company: power to avoid by written notice a contract made in contravention of s 76 or related to one | the other party or parties: liability to avoidance | `s 76A(2) the contract or transaction is one to which subsection (2) applies`; `s 76A(2) the company may avoid ...` |
| s 76A(3) | the Court: power, on the application of a member, a holder of debentures, a trustee for debenture holders or a director, to authorise that person to give the notice in the company's name; the person so authorised: the derived power | the company: liability to be avoided by another's notice | `s 76A(3) the Court may authorise the applicant ...` |
| s 76A(4), (5) | the company or any other person who has suffered or is likely to suffer loss: claim to an order; the Court: power to make "such order or orders as it thinks just and equitable", including those of (5) | any party to the contract or transaction or a related one, the company, and any person who aided, abetted, counselled or procured the contravention: liability to the order | `s 76A(4) the Court may make an order against the person`; `s 76A(5) the order is one of the orders mentioned in subsection (5)` |
| s 76A(6) | a person to whom a certificate signed by two directors, or a director and a secretary, is given: immunity from an order under (4) for acts in reliance on it, and the contract is not invalid or voidable | the company and any other person who might have an order against that person: disability | `s 76A(6) the certificate is one that subsection (6) speaks of`; `s 76A(6)(a) ...`; `s 76A(6)(b) ...` |
| s 76A(7) | the company concerned or any other person who has suffered loss: power to apply; the Court: power to declare that the person became aware | the person given the certificate: liability to lose the immunity of (6) | `s 76A(7) subsection (6) does not apply to the person` |
| s 76A(8), (9), (10) | none: presumptions "in the absence of proof to the contrary" | - | `s 76A(8) ...`; `s 76A(9) ...`; `s 76A(10) ...` |
| s 76A(11) | the prosecuting authority and the Court (not named): power to convict and to sentence | a person who signs a certificate that the requirements of s 76(9A), (9B), (9BA) or (10) were complied with when any was not: liability to a fine of up to $5,000 or 12 months or both; and the duty not to sign it | `s 76A(11) the person is guilty ...`; `s 76A(11) the most the person may be sentenced to on conviction`; `s 76A(11) a person must not sign a certificate ...` (rule) |
| s 76A(12) | the defendant who proves a reasonable belief: immunity from conviction (a defence) | the prosecuting authority: disability | `s 76A(12) the subsection gives the defendant a defence on these facts`; `s 76A(11) the person is guilty of the offence and subsection (12) gives no defence` |
| s 76A(13) | the Court: power under s 391 to relieve a person from the liability to an order under (4) | the company or other person entitled to an order: liability to the relief | `s 76A(13) the power of the Court under section 391 extends to ...` |
| s 76A(14) | none: a deeming that a contract made as a result of or in relation to the assistance is "related" | - | `s 76A(14) the other contract or transaction is deemed to be related ...` |
| s 76A(15) | none: the rights and liabilities of the section are in addition to others and prevail where inconsistent | - | `s 76A(15) the right or liability is in addition ...`; `s 76A(15) the section or the order prevails ...` |

## Marginal readings for a lawyer (sga2)

These are the places where the answer depends on a reading that the Guide's rulings do not settle, listed so that a lawyer can overrule them.

1. **Marginal reading (a), a failed "if" counts as the text's no.** Taken at four sites: `s 76(17)` (F-A4), `s 76(9C)` and `s 76(9CA)` (F-A11), `s 76A(7)` (F-A18).
   The 24 functions of F-A7 and the three of F-A3 are answered the other way, as marginal reading (b) (a grant or prohibition limited by its own wording does not say no outside the limit): **the two groups have the same shape, a carve-out with an "if" gate, and are answered differently**, because the carve-outs named for a permission follow the grant ruling and the four bars and exclusions follow the periods ruling.
   A lawyer who prefers one reading throughout would change 4 functions or 27.
2. **G1, the "where" gate on a "may" (split site (ii)).** 7 functions answer `JUST FALSE` under the periods ruling item (b); the grant rule says `NOTHING`.
3. **F-A9 ("make" against "sign"), F-A10 (prejudice to "either" or "neither"), F-A12 (from the last day or the day after), F-A15 (time against day).**
4. **The labelling of s 76(13)(b) and (iii) to (vi) (Finding 2):** the encoding keeps the rendering's labels; if the printed Act labels the "may do" list as paragraph (c), only the constructor names change.
5. **s 76(14) is encoded twice and the two disagree on the same day** (Finding 8): the function says lodging on the day the order is made is not "within 14 days after"; the regulative rule's `WITHIN 14` counts the same day as in time.

### Reading a result: FALSE and NOTHING (sga2)

The rule of 2026-10-29, assumed and not ruled by a lawyer as a whole, and the rulings of 2026-11-04, 2026-11-05 and 2026-11-12 that settle parts of it, as the Guide records them (quoted above):

- `JUST TRUE`: the text says yes on these facts.
- `JUST FALSE`: the text says no to the case in its own words: a "means" definition, a condition introduced by "if", a flat negative ("does not", "shall not", "must not"), a period the text fixes, a "where" that fails; for a bar, a duty or the provision's own question, an unmet element.
  In a seat answer it means "the text says no", never "the text says nothing".
- `NOTHING`: the text says nothing on these facts: a list it does not close with "only", "includes", an undefined term, silence, a matter it points outside the text for, or a grant or prohibition its own wording limits and the case falls outside the limit.
  It is not a no.
  In particular, for a carve-out ("Nothing in subsection (1) prohibits ...") `NOTHING` means "this paragraph does not take the act out of the prohibition", and the prohibition then decides; it does not mean the act is prohibited.
- `this section gives no defence on these facts` is the wording of the answer of `s 76A(12)` when the defendant has not proved the belief (`JUST FALSE`), never "no defence at all" (ruling of 2026-11-05, (b)).
- A flat negative that counts as a no (N2): s 76(5) (the company is not guilty), s 76(9D) and s 76(15) (a director is not relieved of a duty), s 76A(6)(a) and (b) (the person is not under a liability; the contract is not invalid or voidable), s 76A(1A) (subsection (1) does not apply to book-entry securities).

The branches of the layer-1 modules carry a tag `-- FALSE-kind (...)` or `-- NOTHING-kind (...)`.
Counted by `work/tags.py` over the six provision modules (`sga2-s76-*.l4`, `sga2-s76a-consequences.l4`):

| answer | kind of branch | branches |
| --- | --- | --- |
| `JUST FALSE` | the text says no in its own words | 72 |
| `NOTHING` | limited by its own wording | 58 |
| `NOTHING` | includes | 6 |
| `NOTHING` | silent | 3 |
| `NOTHING` | list not closed | 3 |
| `NOTHING` | points outside the text | 1 |
| all | | 143 (`JUST FALSE` 72, `NOTHING` 71) |

## Seams (sga2)

Each seam input taken (a fact another part or another Act decides), the layer-1 function that asks for it, and the lines where the text shows it.
PLAN.md section 4 in this copy has no row for s 76 as a seam owner, only for the keel functions that I call (section 6, row `sga2`); the table below is from `inputs/XREFS.md` and from reading the lines cited.

| seam | input taken (name, type) | asked by | lines |
| --- | --- | --- | --- |
| s 76B to 76G (sga3) | `the purchase or acquisition, or proposed purchase or acquisition, by the company of its own shares is in accordance with sections 76B to 76G`, BOOLEAN | `s 76(9)(c)` | 7583 |
| s 157 (sgb1), a director's duty | none: s 76(9D) and s 76(15) are flat negatives that say the duty is not relieved; s 157's own conditions are not encoded here | `s 76(9D)`, `s 76(15)` | 7798, 8088 |
| s 183(3A), s 184A, s 184C (later wave) | `the resolution ... was proposed to be passed by written means under section 184A`, BOOLEAN; `the day agreement to the resolution is sought under section 184C, or the documents are served ... under section 183(3A)`, DATE | `s 76(9B)(e)`, `s 76(10A)` | 7721, 7968, 7977, 7979, 7981 |
| s 201 (sgc1), financial statements | `those figures are disclosed in the most recent financial statements of the company that comply with section 201`, BOOLEAN | `s 76(9A)(a)` | 7606 |
| s 205B, s 205C (sgc2) | `the company is exempt from audit requirements under section 205B or 205C`, BOOLEAN (the keel's seam input, PLAN.md section 4A) | `s 76(9A)(e)`, `s 76(9B)(c)` | via the keel's `s 7A(1)` |
| s 210 (sgd) | `the act is done pursuant to an order of Court made under section 210`, BOOLEAN | `s 76(8)(d)` | 7454 |
| s 391 (later wave), relief | none: s 76(7) and s 76A(13) say only that the power extends to the order; s 391's own conditions are not encoded here | `s 76(7)`, `s 76A(13)` | 7429, 8281 |
| s 408(3) (later wave), "officer who is in default" | `the officer is in default`, BOOLEAN (the Act defines the phrase there: an officer who knowingly and wilfully is guilty of the offence or authorises or permits it) | `s 76(5)` | 7414, 28136-28141 |
| s 407 (later wave), general penalty | none: s 76(5) says the company is not guilty "despite section 407", which is a flat negative here | `s 76(5)` | 7413 |
| s 5, s 5A, s 6 and s 4(1) "listed", "related corporation", "borrowing corporation", "book-entry securities", "public company" (the keel) | called, not asked: `s 5(1) ...`, `s 5A ...`, `s 4(1) "listed" ...`, `s 4(1) "related corporation" ...`, `s 4(1) "borrowing corporation" ...`, `s 4(1) "book-entry securities" ...` (the seat also calls `s 4(1) "public company" ...`) | `s 76(8)(g)`, `(8)(m)`, `(9)(b)`, `s 76(10)(b)`, `s 76A(1A)`, the seat | 7465-7479, 7509-7514, 7571-7579, 7826-7836, 8122, 7323 |
| s 7A (the keel) | `s 7A(1) the statement is a solvency statement`, with the proposal `a giving of financial assistance under section 76(9A) or (9B)` | `s 76(9A)(e)`, `s 76(9B)(c)` | 7625, 7678 |
| the `period:` functions (the keel) | called: `the last day of a number of business days after`, `the date is within a period after`, `the date is not later than the end of a period after`, `the last day of a period after` | `s 76(9A)(f)`, `(g)`, `s 76(9B)(d)`, `(f)`, `(g)`, `s 76(10)(e)`, `(h)`, `(j)`, `s 76(12)`, `s 76(14)` | various |
| Insolvency, Restructuring and Dissolution Act 2018, s 178 and s 187 | `the act is done under an arrangement made pursuant to section 178 of the Insolvency, Restructuring and Dissolution Act 2018`, BOOLEAN; `the arrangement is binding on the creditors by virtue of section 187 of the Insolvency, Restructuring and Dissolution Act 2018`, BOOLEAN; the Act is not encoded | `s 76(8)(e)`, `s 76(8)(f)` | 7456-7463 |
| Division 3A of Part 4 of this Act (later wave) | `the reduction of capital is in accordance with Division 3A of Part 4`, BOOLEAN | `s 76(8)(b)` | 7446-7447 |
| Securities and Futures Act 2001, s 81SF | `the securities are book-entry securities as section 81SF of the Securities and Futures Act 2001 gives that meaning`, BOOLEAN | `s 76A(1A)` | 8122-8126 |
| Banking, finance and insurance laws; the Monetary Authority of Singapore | `the activities of the company are regulated by a written law relating to banking, finance companies or insurance`, BOOLEAN; `the activities of the company are subject to supervision by the Monetary Authority of Singapore`, BOOLEAN | `s 76(9)(a)` | 7550-7569 |
| Public holidays (s 4(1) "business day") | `the public holidays`, LIST OF DATE | the four rules counting business days: `s 76(9A)(f)`, `(g)`, `s 76(9B)(d)`, `(f)` | 7628, 7650, 7681, 7726 |

Sections that cite mine (`XREFS.md`): the keel at line 2297 (s 7A), sga3 at line 8314 (s 76B "Despite section 76"), sgb2 at 13944 and 14754 and sgc2 at 20093 (s 76A), and a later wave at 16688 (s 76).
The functions they would call are `s 76(1) subsection (1) bars the company from giving the financial assistance` and `s 76A(1) the contract or transaction is void`.

## Split sites (sga2)

The two questions the Guide leaves to the part (brief, "Two questions the Guide leaves to you").

**(i) An unmet element of an offence or a contravention: 11 sites; `JUST FALSE` at 8, `NOTHING` at 3.**

| site | function | answer taken | fork line | Guide line relied on |
| --- | --- | --- | --- | --- |
| s 76(1) | `s 76(1) subsection (1) bars the company from giving the financial assistance` | `JUST FALSE` (class scope `NOTHING`) | F-A1 | grant ruling limit 2: "for a bar, a duty or the provision's own question"; periods ruling (c) for the scope |
| s 76(1)(a) | `s 76(1)(a) the acquisition is one that paragraph (a) names` | `JUST FALSE` | F-A1 | grant ruling limit 2 |
| s 76(1)(b) | `s 76(1)(b) the proposed acquisition is one that paragraph (b) names` | `JUST FALSE` | F-A1 | grant ruling limit 2 |
| s 76(1A) | `s 76(1A) subsection (1A) bars the company from the act` | `JUST FALSE` | F-A2 | grant ruling limit 2 |
| s 76(5), officer | `s 76(5) the officer is guilty of the offence this subsection creates` | `JUST FALSE` | F-A5 | grant ruling limit 2: "the provision's own question" |
| s 76(5), company | `s 76(5) the company is guilty of an offence by contravening subsection (1) or (1A)` | `NOTHING` where it did not contravene (`JUST FALSE`, a flat negative, where it did) | F-A5 | N2: "flat negatives count as a no"; In short: "is silent" |
| s 76(9C) | `s 76(9C) the company is barred from giving the assistance under subsection (9A) or (9B)` | `JUST FALSE` where no event has occurred | F-A11 | In short: "a condition the text introduces with "if""; marginal reading (a) |
| s 76(9CA) | `s 76(9CA) the company is barred from giving the assistance under subsection (9BA)` | `JUST FALSE` where no event has occurred | F-A11 | the same |
| s 76A(1) | `s 76A(1) the contract or transaction is void` | `NOTHING` | F-A16 | In short: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| s 76A(2) | `s 76A(2) the contract or transaction is one to which subsection (2) applies` | `NOTHING` where neither contravention nor relation holds (`JUST FALSE` only where (6) protects it) | F-A16 (the same element) | In short: "limits ... in its own wording"; the flat negative of (6)(b) for the `JUST FALSE` |
| s 76A(11) | `s 76A(11) the person is guilty of the offence this subsection creates` | `JUST FALSE` | F-A5 | grant ruling limit 2 |

**(ii) A "may" gated by "where", "when", "upon" or "on application": 9 sites; `JUST FALSE` at 7 (G1), `NOTHING` at 2.**

| site | function | answer taken | fork line | Guide line relied on |
| --- | --- | --- | --- | --- |
| s 76(6) | `s 76(6) the Court may order the convicted person to pay compensation` | `JUST FALSE` | F-A6 (G1) | periods ruling (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| s 76(11) | `s 76(11) the Court may declare that the provisions of subsection (10) have been complied with` | `JUST FALSE` | F-A6 (G1) | periods ruling (b) |
| s 76(12) | `s 76(12) the person may apply to the Court opposing the giving of the assistance` | `JUST FALSE` (resolution not passed; outside the 21 days); `NOTHING` for the (e) persons where (10)(b) does not apply, and for a person not listed | F-A6 (G1), F-A7 | periods ruling (a) and (b); grant ruling limit 1 for (e); In short, "a list not closed" for a stranger |
| s 76(13)(a) | `s 76(13)(a) the Court must have regard to the rights and interests of the members and of the creditors` | `JUST FALSE` | F-A6 (G1) | periods ruling (b) (a duty, not a "may") |
| s 76(13) | `s 76(13) the Court may make the order` | `JUST FALSE` | F-A6 (G1) | periods ruling (b) |
| s 76A(1A) | `s 76A(1A) the Court may order the transfer of the shares acquired in contravention of subsection (1)` | `JUST FALSE` | F-A6 (G1) | delegated definitions ruling (c): "when", "upon" and "whenever" count as "where" ("on being satisfied" is read so) |
| s 76A(4) | `s 76A(4) the Court may make an order against the person` | `JUST FALSE` | F-A6 (G1) | periods ruling (b) |
| s 76A(2) | `s 76A(2) the company may avoid the contract or transaction by written notice` | `NOTHING` | F-A7 | grant ruling limit 1 |
| s 76A(3) | `s 76A(3) the Court may authorise the applicant to give notice in the name of the company` | `NOTHING` for an applicant not named | F-A17 | grant ruling limit 1 |

Each answer is a fork line above; none was changed to match another part.
`s 76(6) the order may be enforced as if it were a judgment of the Court` is not a split site: its gate is the object of the grant ("any such order"), a scope limit answered `NOTHING` under the periods ruling (c).

## Rules with no breach path (sga2)

None.
The range has ten regulative rules, and each has a `#TRACE` that reaches `BREACH`: the four prohibitions of s 76(1A) and the prohibition of s 76(1) (breached by the forbidden act), s 76(5) (an officer in default), s 76(9C) and s 76(9CA) (giving the assistance after a director has ceased to be satisfied), s 76A(11) (signing a false certificate), each a `SHANT` with `HENCE FULFILLED LEST BREACH`; and s 76(14), a `MUST ... WITHIN 14` whose trace reaches `BREACH` at day 15 and `FULFILLED` at day 14.
Duties of the text that are encoded only as decision functions, with no regulative rule, because the text names no party's act and deadline together: s 76(10A) (a duty to comply with (10)(f) or (g) "at or before the time"), s 76(13)(a) (a duty of the Court, not a seat), and the notice and lodging duties inside the conditions of (9A), (9B) and (10), which are conditions of a permission and not free-standing duties.

## Findings: what the text turns out to say

1. **The rendering repeats a paragraph label where a paragraph runs on after its sub-paragraphs, in six places:** `(a) as disclosed in the most recent financial statements ...` at line 7605 (the tail of s 76(9A)(a)); `(e) to give that assistance;` at 7724 (tail of s 76(9B)(e)); `(b) the listed corporation or the ultimate holding company ... has approved` at 7838 (tail of s 76(10)(b)); `(c) and is accompanied by a copy of a statement` at 7858 (tail of s 76(10)(c)); `(h) is published in a daily newspaper` at 7936 (tail of s 76(10)(h)); `(b) and may do all or any of the following:` at 8053 (Finding 2).
   The coverage table has a row for each, "(continuation after its sub-paragraphs)", and the function that encodes the paragraph carries the tail's words.
2. **s 76(13)(b) as rendered has two different things under one label.** Line 8038 `(b) must not make an order approving ... unless the Court is satisfied that (i) ... and (ii) ...`, then line 8053 `(b) and may do all or any of the following:` followed by sub-paragraphs numbered (iii) to (vi).
   The second `(b)` is most probably a separate paragraph of the printed Act, and (iii) to (vi) its sub-paragraphs under a different number; the rendering has flattened it.
   The encoding keeps the rendering's labels (`s 76(13)(b)(iii)` and so on) and cites by line number; I did not check this against the official text.
3. **s 76(5): the company itself commits no offence.** "If a company contravenes subsection (1) or (1A), the company shall not be guilty of an offence, despite section 407, but each officer of the company who is in default shall be guilty of an offence" (7412-7416).
   The penalty is a fine not exceeding $20,000 or imprisonment not exceeding 3 years or both; s 76A(11) (signing a false certificate) is a fine not exceeding $5,000 or imprisonment not exceeding 12 months or both.
4. **s 76(5) makes an offence of a contravention of subsection (1) or (1A) only.** The range has no provision that attaches a penalty to giving assistance in breach of (9C) or (9CA) as such, and the text does not say whether such giving takes the case out of the permission of (9A), (9B) or (9BA) so that (1) is contravened (see "What the text does not answer").
5. **The three whitewash routes differ.** (9A) and (9B) need a solvency statement and a notice to members; (9BA) needs neither, but requires that the assistance does not materially prejudice the company, its shareholders or its creditors (7740-7767).
   (9C) bars the assistance under (9A) or (9B) when a director ceases to be satisfied (in the best interests, or the terms fair and reasonable) or no longer has reasonable grounds for an opinion in the solvency statement; (9CA) bars it under (9BA) only for the director's ceasing to be satisfied that the terms are fair and reasonable.
6. **s 76(10)(h) starts its 21 days from the later of two resolutions** (the company's and, where (b) applies, the parent's); **s 76(10)(j) distinguishes three waiting periods** (the 21 days of (12); the withdrawal of the last application; the Court's decision).
7. **s 76(8A)(a) and (b) are definitions for (8)(m) only** ("For the purposes of subsection (8)(m)"): an odd-lot is an amount of shares less than a board lot, a board lot a standard unit of trading of the exchange on which the company is listed; (c) says the reference to "rounding off any odd-lots" includes a shareholder who owns only odd-lots disposing of all of them.
8. **s 76(14) is encoded twice, and the two disagree on one fact.** As a decision function (`s 76(14) the company has lodged a copy of the order with the Registrar in time`) a copy lodged on the day the order is made is not "within 14 days after the order is made", because the keel's convention P2 opens the window the day after; as a regulative rule (`PARTY Company MUST ... WITHIN 14`) the same-day lodging at time 0 reads `FULFILLED` (tested by hand on both builds, not kept as a test).
   I left both as they are: the text says "within 14 days after", and the two encodings read "after" differently; a lawyer would choose.
9. **The seat asks whether the company is private, not whether it is public.** The keel's shared seat input is `the company is a private company` and "public company" means "a company other than a private company" (s 4(1), line 1676-1677), so the seat asks the former and computes the latter.
10. **One expected value of my own was wrong, and the harness caught it.** In `sga2-cases-seat.l4` I first wrote `NOTHING` for s 76(8A)(a) with exactly one board lot held, and for s 76(8A)(b) with a non-standard unit; the run showed `JUST FALSE`.
    The text says "means" in both (7532-7538), so the layer-1 tests (written from the text earlier) were right and my seat expectation was a slip; I corrected the expectation from the text, not from the output.
    Nothing else failed.
11. **No assertion fails or is refused in the final run.** There is no test that is meant to fail, so `expected_failed` is empty and none is registered.

## What the text does not answer

- Who may enforce the prohibition of s 76(1) beyond what s 76(5) (prosecution) and s 76A(4) (an application by the company or any other person who has suffered loss) say: the text names no holder of the claim.
- The meaning of "financial assistance" beyond the open list of s 76(2).
- What follows from a breach of s 76(9C) or (9CA): no penalty or remedy of its own is stated, and the text does not say whether giving assistance in breach of them is a contravention of subsection (1), which is what s 76(5) makes an offence.
- Whether the 10 percent of s 76(9A)(a) is measured against the figures in the most recent financial statements even when the company's position has since changed: the text says "as disclosed in" them, and the encoding asks whether the figures are so disclosed.
- Whether the notice of s 76(9A)(f) may be sent before the assistance is provided: the text says "within 10 business days of providing"; F-A8 lets early acts count.
- The labelling of s 76(13)(b)(iii) to (vi) (Finding 2).

## What the stable binary does not accept

Met while writing, all on the stable builds 1.6.110 and 1.6.109 (the tests run on both, and the counts are the same):

- `REFUSE`, `#ASSERT REFUSED`, `YMD`, a section-level `GIVEN`, `TYPICALLY` on a field, and sets: not used.
- A chained comparison `... EQUALS JUST (...) EQUALS FALSE` is a type error; the tests write `#ASSERT NOT (... EQUALS JUST (...))` (`sga2-tests-s76-offence.l4`, `sga2-tests-s76a.l4`).
- Every `NOT` is parenthesised; one `#ASSERT` per line; dates are `Date d m y`; `WAITUNTIL` is spelled without a space; a `MAYBE` result is written with `MEANS` or `DECIDE ... IS`.
- A regulative rule with `SHANT` or `MUST ... WITHIN` is run with `#TRACE` and asserted by the comment `-- EXPECT BREACH|FULFILLED|RESIDUAL`, which `check.sh` does not read: I compared every trace on both builds with `work/rt.py` and each agreed with its expectation.
  The traces: 19 in all (11 BREACH, 1 FULFILLED, 7 RESIDUAL), in sga2-tests-s76-offence.l4 2; sga2-tests-s76-prohibition.l4 7; sga2-tests-s76-special-resolution.l4 4; sga2-tests-s76-whitewash.l4 4; sga2-tests-s76a.l4 2.
  `check.sh` counts assertions, so the trace outcomes are not in its numbers.
- A `LIST OF DATE` input in a seat question is accepted by the compiler; whether the Interact form can ask it is not something I could test.

## What check.sh prints

Run from this folder with `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`.
The baseline it replaced: the keel's eight `sg-*` modules, which carry no assertions (the first eight rows below read 0 satisfied); I did not run `check.sh` on the folder before adding my files, so these eight rows are the baseline.

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
sga2-cases-seat.l4                             0       278       0        0         0 |      0       278       0        0  same
sga2-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
sga2-s76-exceptions.l4                         0         0       0        0         0 |      0         0       0        0  same
sga2-s76-offence.l4                            0         0       0        0         0 |      0         0       0        0  same
sga2-s76-prohibition.l4                        0         0       0        0         0 |      0         0       0        0  same
sga2-s76-special-resolution.l4                 0         0       0        0         0 |      0         0       0        0  same
sga2-s76-whitewash.l4                          0         0       0        0         0 |      0         0       0        0  same
sga2-s76a-consequences.l4                      0         0       0        0         0 |      0         0       0        0  same
sga2-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sga2-tests-s76-exceptions.l4                   0        84       0        0         0 |      0        84       0        0  same
sga2-tests-s76-offence.l4                      0        18       0        0         0 |      0        18       0        0  same
sga2-tests-s76-prohibition.l4                  0        56       0        0         0 |      0        56       0        0  same
sga2-tests-s76-special-resolution.l4           0       130       0        0         0 |      0       130       0        0  same
sga2-tests-s76-whitewash.l4                    0       120       0        0         0 |      0       120       0        0  same
sga2-tests-s76a.l4                             0        84       0        0         0 |      0        84       0        0  same
TOTAL (23 modules)                             0       770       0        0           |      0       770       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Also: `python3 -I srcrefs.py check --refs ../../../inputs/CoA1967.txt sga2-*.l4` and the same with `--strict` each print `0 problems` (871 quote lines, 116 runs, 116 locators).
`l4 run` on every `sga2-*.l4` on both builds shows no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning`.
One mutation check: a copy of `sga2-cases-seat.l4` with the expected value of one s 76(9C) assertion flipped fails that assertion (and is deleted).
