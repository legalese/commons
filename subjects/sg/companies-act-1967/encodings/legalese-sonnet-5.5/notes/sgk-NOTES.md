# NOTES (sgk): Companies Act 1967 (Singapore), Part 4 Division 8, Parts 8, 8A and 9

Status of this file, 2026-11-18: written after layer 1 (7 modules, 7 test files), the seat layer and `check.sh` were green on the stable builds 1.6.110 and 1.6.109.
Every count below was taken from the files on disk or from `check.sh` output on that day, and says which.
Every quotation in the fork register was checked mechanically against `CoA1967.txt` after the file was written (the check is described under "What the checks were" at the end).
Nothing here was checked against the official text, which was not read.

## Edition encoded

This is an encoding of the **Companies Act 1967, 2020 Revised Edition**, as rendered by Singapore Statutes Online (SSO) in its **informal consolidation, "version in force from 6/5/2026 to 20/10/2026"**, retrieved 2026-10-09.
That consolidation carries the amendments up to Act 24 of 2025.
A later consolidation may exist and was not read.
The encoding is of that text only.
The source file is `inputs/CoA1967.txt`, a PDF turned into plain text.
It is a rendering of the Act and **not the official text**: SSO's terms say so, and nothing here is claimed to be verified against the official text.
Line numbers everywhere (`src:N`, `@ref`, the coverage table) are lines of that file as it is.
Nothing in this folder is endorsed by, or associated with, the Singapore Government or the Attorney-General's Chambers.

**The brief governs over `inputs/PLAN.md`** wherever the two differ, and where they differ this file says so:

- PLAN.md section 6 describes my ranges as "registration of charges, judicial management (Part 4 Division 8, Parts 8, 8A, 9)".
  In this text Part 8 (ss 217 to 227) and Part 8A (ss 227AA to 227X) hold only the words "[Repealed by Act 40 of 2018]", and Part 9 is "INVESTIGATIONS" (ss 228 to 246, s 234 repealed).
  There is no judicial management to encode.
  The brief says the headings of Parts 8 and 8A are to be covered "with whatever text they hold", and the coverage table does that (rows for the two headings and one row for each repealed run).
- PLAN.md section 6 expects "`s 4(1) "charge"`-type terms if the keel defines them".
  The keel does define `s 4(1) "charge"`, `"Court"`, `"Registrar"` and `"prescribed"`.
  I do not call them; "Seams (sgk)" says why and what a caller does.
- PLAN.md section 6 gives my Part 9 seam only as "s 4(8)'s reference to Part 9".
  There are two more that the plan lacks (the Banking Act 1970 in s 244(4), and the keel's own `s 7(1) section 244` and `s 7(6A)`); both are in "Seams (sgk)".
- The brief's split-site rule (two sites, recorded site by site) and the grant ruling of 2026-11-12 (three limits) are the brief's; PLAN.md section 8 describes the split sites in the same words and I found no difference of substance there.

## The seat, the layers and the files (sgk)

**Seat.** An individual who is, or is about to become, a director, the company secretary or a member (shareholder) of a company incorporated under the Act, or of a foreign company registered under it, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows if it is not done.
(Assumed, not ruled, as the brief says: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.)
There is no seat for the Registrar, the Minister, the Authority or the Court.
A power of theirs appears in the seat only as what it means to the individual: whether I may be required to give information (s 244(1)), whether I must hand over books (s 236(2)), whether I am barred from suing (s 240(1)), and so on.
The duties of the Minister, the Registrar and the inspectors are encoded in layer 1 and have no seat question, except where the question is what the individual is owed (a copy of a report, s 233(1A); a certificate, s 134(3)).

**Layer 1** (the law, objectively), 7 modules and 7 test files, the 8 `sg-*` keel modules beside them (read-only, unchanged):

| module | provisions | test file |
| --- | --- | --- |
| `sgk-div8-application.l4` | ss 139, 140, 141 (time for documents made out of Singapore, earlier charges, foreign companies) | `sgk-tests-div8-application.l4` |
| `sgk-div8-registration.l4` | ss 131 to 133 (the statement of a charge, the duty to register, charges on property acquired) | `sgk-tests-div8-registration.l4` |
| `sgk-div8-register.l4` | ss 134 to 138 (the register, the certificate, endorsement, satisfaction and release, extension of time, copies of instruments) | `sgk-tests-div8-register.l4` |
| `sgk-part9-declared.l4` | ss 228 to 231 (the limit of Part 9, its words, declaring a company, appointing inspectors, who pays) | `sgk-tests-part9-declared.l4` |
| `sgk-part9-inspectors.l4` | ss 232 to 236 (application, reports, related corporations, the inspector's procedure and powers; s 234 repealed) | `sgk-tests-part9-inspectors.l4` |
| `sgk-part9-consequences.l4` | ss 237 to 242 (costs, evidence, the inspector's helpers, suspension of proceedings, winding up, penalties) | `sgk-tests-part9-consequences.l4` |
| `sgk-part9-ownership.l4` | ss 243 to 246 (ownership investigations, interests in shares, restrictions on shares, inspectors appointed in other countries) | `sgk-tests-part9-ownership.l4` |

**Layer 2** (one thin seat layer): `sgk-seat.l4` (93 questions, each with `@export` and `@desc`, grouped under `§` and `§§` headings in the text's order, each named "Under section N, ...") and `sgk-cases-seat.l4` (280 assertions).
The seat calls the layer-1 functions and restates no rule.

**Other files:** `PROGRESS.md` (what was done, in what order), `NEEDS-CORE.md` (what the core lacks), `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` (supplied).

**Conventions kept throughout** (all from the brief and PLAN.md section 2):

- Every top-level name, type and constructor begins with the label of its provision (`s 131(1) ...`, `s 231 party`, `s 241(1) deemed applicant`).
- Every rule is quoted mechanically (`-- src:N | text` lines and an `@ref label (src:min-max)` after them) and `srcrefs.py check --refs` and `--strict` report 0 problems for every sgk file.
- Every `FALSE-kind` branch quotes the words that say no, and every `NOTHING-kind` branch says why (one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording).
- Dates are `Date day month year`; every period is counted by a `period:` function of `sg-periods.l4`; money is a `NUMBER` in Singapore dollars.
- Expected values in the tests are hand-written from the text, and a failing assertion would be a finding (there is none: 906 assertions satisfied, 0 failed).


## Coverage (sgk)

One row per section, subsection, paragraph, sub-paragraph, defined term and heading of my two ranges (11039-11492 and 21886-22626 of `CoA1967.txt`), each with exactly one disposition and the L4 names that encode it.
The table is built by a script from the text (`work/covparse.py` splits the ranges into units; `work/coverage.py` joins them to the layer-1 functions by provision label and checks the result), not by hand.

**Counts.**
230 rows: **128 encoded**, **65 fork** (each pointing at its fork entry), **34 inert** (every one reason 1, a heading; there is none of reason 2 or 3), **3 repealed or blank in this text** (ss 217 to 227, ss 227AA to 227X, s 234; the text shows each as "[Repealed by ...]").
There is no `out-of-scope` row and no `deferred` row.

**Audit counts.**
The two ranges hold 1195 lines, of which 907 are not blank; of those, 50 are page furniture ("Informal Consolidation – version in force from 6/5/2026 to 20/10/2026" and "2020 Ed. Companies Act 1967 <page>"), which belong to the row of the section they sit in, and 857 are text.
The script checks that every non-blank line falls in exactly one row: it reports 0 lines in no row, 0 lines in two rows and 0 rows without a disposition.
Text units counted: 194 units (sections, subsections, paragraphs, sub-paragraphs, defined terms), 34 headings (the Division heading, the Part 8, 8A and 9 headings, the "INVESTIGATIONS" heading and the marginal headings of sections) and 2 repealed runs; the table has 230 rows.
Rows before and after: the first table that covered both ranges had 230 rows, 124 of them forks, 68 encoded and one row with no disposition; the table filed has 230 rows, 65 forks, 128 encoded and none without a disposition.
The row count did not move; the disposition did, because the first build called a row a fork whenever any function it cites carries a fork id, and the final build does so only when the row's own function does (a child paragraph whose parent carries the fork says so in the parent's row).
An earlier parser that absorbed marginal headings into the unit above them was corrected before any table was filed, and its row count was not kept.

**Modules, tests and traces.**

| module | provisions | layer-1 functions | test file | assertions satisfied | traces |
| --- | --- | --- | --- | --- | --- |
| `sgk-div8-application.l4` | ss 139, 140, 141 | 6 | `sgk-tests-div8-application.l4` | 24 | 0 |
| `sgk-div8-registration.l4` | ss 131 to 133 | 32 | `sgk-tests-div8-registration.l4` | 135 | 11 |
| `sgk-div8-register.l4` | ss 134 to 138 | 38 | `sgk-tests-div8-register.l4` | 93 | 22 |
| `sgk-part9-declared.l4` | ss 228 to 231 | 19 | `sgk-tests-part9-declared.l4` | 66 | 2 |
| `sgk-part9-inspectors.l4` | ss 232 to 236 | 44 | `sgk-tests-part9-inspectors.l4` | 127 | 20 |
| `sgk-part9-consequences.l4` | ss 237 to 242 | 23 | `sgk-tests-part9-consequences.l4` | 77 | 14 |
| `sgk-part9-ownership.l4` | ss 243 to 246 | 37 | `sgk-tests-part9-ownership.l4` | 104 | 14 |
| `sgk-seat.l4` | the 93 questions | 0 (calls layer 1) | `sgk-cases-seat.l4` | 280 | 0 |

**How to read the L4 column.**
A child paragraph or sub-paragraph is encoded by the functions of its provision label, so its cell says "as row s 131(3)" and so on where the names are the same as the row named; the full names are in the row named.
The module is named once per cell.
The seat layer is not repeated in the table: its 93 questions each call one layer-1 function and are listed in "Seat questions" below.
The tests column names the test file that holds the assertions for the row's functions; Parts 8 and 8A, s 234 and the headings carry no test.

| lines | row | disposition | L4 name (module: function) | fork | test file |
| --- | --- | --- | --- | --- | --- |
| 11039 | Division 8 — Registration of charges | inert (reason 1: heading) | Division 8 — Registration of charges |  |  |
| 11041 | marginal heading of s 131(1) | inert (reason 1: heading) | Registration of charges |  |  |
| 11043-11052 | s 131(1) | fork | sgk-div8-registration: `s 131(1) a statement of the charge must be lodged with the Registrar`; `s 131(1) the company must lodge the statement of the charge within 30 days after the creation of the charge`; `s 131(1) the security the charge confers is void against the liquidator and any creditor of the company`; `s 131(1) the statement is lodged within 30 days after the creation of the charge` | F-K4, F-K5, F-K6 | sgk-tests-div8-registration.l4 |
| 11054-11059 | s 131(1A) | fork | sgk-div8-registration: `s 131(1A) the instrument or a certified true copy must be produced to the Registrar`; `s 131(1A) the production is at no cost to the Registrar` | F-K5 | sgk-tests-div8-registration.l4 |
| 11061-11064 | s 131(2) | encoded | sgk-div8-registration: `s 131(2) subsection (1) affects the contract or obligation`; `s 131(2) the money secured by the charge becomes immediately payable by force of this subsection` |  | sgk-tests-div8-registration.l4 |
| 11066-11067 | s 131(3) | fork | sgk-div8-registration: `s 131(3) the charge falls within one of paragraphs (a) to (j)`; `s 131(3) the charge is one to which section 131 applies` | F-K3 | sgk-tests-div8-registration.l4 |
| 11069 | s 131(3)(a) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11071 | s 131(3)(b) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11073-11074 | s 131(3)(c) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11076-11078 | s 131(3)(d) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11080-11082 | s 131(3)(e) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11084-11087 | s 131(3)(f) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11089-11090 | s 131(3)(g) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11092 | s 131(3)(h) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11094-11095 | s 131(3)(i) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11097-11102 | s 131(3)(j) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11104 | s 131(3AA) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11106-11108 | s 131(3AA)(a) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11110-11112 | s 131(3AA)(b) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11114-11119 | s 131(3AB) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11121-11125 | s 131(3AC) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11127 | s 131(3AC)(a) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11129-11130 | s 131(3AC)(b) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11132-11135 | s 131(3AC)(c) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11137-11142 | s 131(3A) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11144-11149 | s 131(3B) | fork | as row s 131(3) | F-K3 | sgk-tests-div8-registration.l4 |
| 11151-11155 | s 131(3C) | encoded | as row s 131(3) |  | sgk-tests-div8-registration.l4 |
| 11157-11162 | s 131(4) | fork | sgk-div8-registration: `s 131(4) the statement may be lodged even though further proceedings are necessary under the law of the place where the property is` | F-K7 | sgk-tests-div8-registration.l4 |
| 11164-11170 | s 131(5) | fork | sgk-div8-registration: `s 131(5) the lodging of the statement is sufficient` | F-K8 | sgk-tests-div8-registration.l4 |
| 11172 | s 131(5)(a) | encoded | as row s 131(5) |  | sgk-tests-div8-registration.l4 |
| 11174-11176 | s 131(5)(b) | encoded | as row s 131(5) |  | sgk-tests-div8-registration.l4 |
| 11178 | s 131(5)(c) | encoded | as row s 131(5) |  | sgk-tests-div8-registration.l4 |
| 11180 | s 131(5)(d) | encoded | as row s 131(5) |  | sgk-tests-div8-registration.l4 |
| 11182-11186 | s 131(6) | fork | sgk-div8-registration: `s 131(6) the company must lodge the particulars of each issue within 30 days after it`; `s 131(6) the omission affects the validity of the debentures issued`; `s 131(6) the particulars of the issue are lodged within 30 days after the issue` | F-K4, F-K6 | sgk-tests-div8-registration.l4 |
| 11188-11200 | s 131(7) | fork | sgk-div8-registration: `s 131(7) the omission affects the validity of the debentures issued`; `s 131(7) the particulars required to be lodged must include the amount or rate per cent of the commission, allowance or discount` | F-K5 | sgk-tests-div8-registration.l4 |
| 11202-11204 | s 131(8) | encoded | sgk-div8-registration: `s 131(8) the deposit is treated as the issue of the debentures at a discount for the purposes of subsection (7)` |  | sgk-tests-div8-registration.l4 |
| 11206-11208 | s 131(9) | encoded | sgk-div8-registration: `s 131(9) the charge or assignment needs to be filed or registered under another written law` |  | sgk-tests-div8-registration.l4 |
| 11210-11222 | s 131(10) | fork | sgk-div8-registration: `s 131(10) the subsequent charge is not operative and has no validity as respects the property comprised in the prior charge` | F-K9 | sgk-tests-div8-registration.l4 |
| 11224-11225 | s 131(11) | encoded | sgk-div8-registration: `s 131(11) the lien is a shipowner's lien` |  | sgk-tests-div8-registration.l4 |
| 11227 | s 131(11)(a) | encoded | as row s 131(11) |  | sgk-tests-div8-registration.l4 |
| 11229 | s 131(11)(b) | encoded | as row s 131(11) |  | sgk-tests-div8-registration.l4 |
| 11231-11239 | s 131(11)(c) | encoded | as row s 131(11) |  | sgk-tests-div8-registration.l4 |
| 11241 | marginal heading of s 132(1) | inert (reason 1: heading) | Duty to register charges |  |  |
| 11243-11252 | s 132(1) | fork | sgk-div8-registration: `s 132(1) the most the person may be sentenced to on conviction`; `s 132(1) the person is guilty of the offence of default in complying with section 131`; `s 132(1) the person may lodge the documents and particulars for registration` | F-K10 | sgk-tests-div8-registration.l4 |
| 11254-11256 | s 132(2) | fork | sgk-div8-registration: `s 132(2) the amount the person may recover from the company`; `s 132(2) the person is entitled to recover the fees from the company` | F-K11 | sgk-tests-div8-registration.l4 |
| 11258-11259 | marginal heading of s 133(1) | inert (reason 1: heading) | Duty of company to register charges existing on property |  |  |
| 11261 | s 133(1) | fork | sgk-div8-registration: `s 133(1) the company must cause a statement of the prescribed particulars of the charge to be lodged with the Registrar`; `s 133(1) the company must cause the statement to be lodged within 30 days`; `s 133(1) the last day for lodging the statement`; `s 133(1) the statement is lodged within 30 days after the date` | F-K5, F-K12 | sgk-tests-div8-registration.l4 |
| 11263-11266 | s 133(1)(a) | encoded | as row s 133(1) |  | sgk-tests-div8-registration.l4 |
| 11268-11272 | s 133(1)(b) | encoded | as row s 133(1) |  | sgk-tests-div8-registration.l4 |
| 11274-11287 | s 133(1)(c) | encoded | as row s 133(1) |  | sgk-tests-div8-registration.l4 |
| 11289-11293 | s 133(2) | fork | sgk-div8-registration: `s 133(2) the most the person may be sentenced to on conviction`; `s 133(2) the person is guilty of the offence of default in complying with section 133` | F-K10 | sgk-tests-div8-registration.l4 |
| 11295 | marginal heading of s 134(1) | inert (reason 1: heading) | Register of charges to be kept by Registrar |  |  |
| 11297-11299 | s 134(1) | encoded | sgk-div8-register: `s 134(1) the Registrar must enter the particulars of the charge in the register`; `s 134(1) the particulars the Registrar must enter in the register` |  | sgk-tests-div8-register.l4 |
| 11301-11304 | s 134(1)(a) | encoded | as row s 134(1) |  | sgk-tests-div8-register.l4 |
| 11306 | s 134(1)(b) | encoded | as row s 134(1) |  | sgk-tests-div8-register.l4 |
| 11308-11311 | s 134(1)(b)(i) | encoded | as row s 134(1) |  | sgk-tests-div8-register.l4 |
| 11313 | s 134(1)(b)(ii) | encoded | as row s 134(1) |  | sgk-tests-div8-register.l4 |
| 11315-11316 | s 134(1)(b)(iii) | encoded | as row s 134(1) |  | sgk-tests-div8-register.l4 |
| 11318 | s 134(1)(b)(iv) | encoded | as row s 134(1) |  | sgk-tests-div8-register.l4 |
| 11320-11322 | s 134(2) | encoded | sgk-div8-register: `s 134(2) the Registrar must issue to the company a notice of the registration of a charge`; `s 134(2) the notice is conclusive evidence that the requirements as to registration have been complied with` |  | sgk-tests-div8-register.l4 |
| 11324-11331 | s 134(3) | fork | sgk-div8-register: `s 134(3) the Registrar must issue to the company a certificate confirming the registration of the charge`; `s 134(3) the certificate is conclusive evidence that the requirements as to registration have been complied with` | F-K5 | sgk-tests-div8-register.l4 |
| 11333 | marginal heading of s 135(1) | inert (reason 1: heading) | Endorsement of certificate of registration on debentures |  |  |
| 11335-11338 | s 135(1) | encoded | sgk-div8-register: `s 135(1) the company must cause a copy of the notice of registration, or a statement of the registration and its date, to be endorsed on the debenture or certificate`; `s 135(1) the company must cause the endorsement to be made` |  | sgk-tests-div8-register.l4 |
| 11340 | s 135(1)(a) | encoded | as row s 135(1) |  | sgk-tests-div8-register.l4 |
| 11342-11343 | s 135(1)(b) | encoded | as row s 135(1) |  | sgk-tests-div8-register.l4 |
| 11345-11347 | s 135(2) | encoded | as row s 135(1) |  | sgk-tests-div8-register.l4 |
| 11349-11352 | s 135(3) | fork | sgk-div8-register: `s 135(3) a person must not knowingly and wilfully authorise or permit the delivery of an unendorsed debenture or certificate`; `s 135(3) the most the person may be sentenced to on conviction`; `s 135(3) the person is guilty of the offence of authorising or permitting the delivery of an unendorsed debenture or certificate` | F-K10, F-K34 | sgk-tests-div8-register.l4 |
| 11354 | marginal heading of s 136(1) | inert (reason 1: heading) | Entries of satisfaction and release of property from charge |  |  |
| 11356 | s 136(1) | fork | sgk-div8-register: `s 136(1) the Registrar must enter the particulars of the statement in the register`; `s 136(1) the company may lodge with the Registrar a statement of satisfaction or release` | F-K5, F-K7 | sgk-tests-div8-register.l4 |
| 11358-11359 | s 136(1)(a) | encoded | as row s 136(1) |  | sgk-tests-div8-register.l4 |
| 11361-11371 | s 136(1)(b) | encoded | as row s 136(1) |  | sgk-tests-div8-register.l4 |
| 11373-11381 | s 136(2) | encoded | sgk-div8-register: `s 136(2) the chargee's statement constitutes sufficient evidence of the payment, satisfaction, release or ceasing`; `s 136(2) the statement of satisfaction or release is endorsed as the subsection requires` |  | sgk-tests-div8-register.l4 |
| 11383 | marginal heading of s 137 | inert (reason 1: heading) | Extension of time and rectification of register of charges |  |  |
| 11385-11398 | s 137 | fork | sgk-div8-register: `s 137 the Court may make the relief subject to a term that it is without prejudice to liability already incurred in respect of the default`; `s 137 the Court may order that the time for registration be extended or that the omission or mis-statement be rectified`; `s 137 the person may apply to the Court for the extension of time or the rectification` | F-K13 | sgk-tests-div8-register.l4 |
| 11400-11401 | marginal heading of s 138(1) | inert (reason 1: heading) | Company to keep copies of charging instruments and register |  |  |
| 11403-11410 | s 138(1) | fork | sgk-div8-register: `s 138(1) the company must keep the instrument creating the charge, or a copy, at its registered office`; `s 138(1) the company must keep the instrument or a copy at its registered office`; `s 138(1) the company must not cease to keep the instrument or a copy at its registered office while the charge remains in force`; `s 138(1) the company's keeping satisfies the subsection` | F-K16 | sgk-tests-div8-register.l4 |
| 11412-11414 | s 138(1A) | encoded | sgk-div8-register: `s 138(1A)(a) the instrument or copy is deemed to form part of the records required to be kept under section 199(1)`; `s 138(1A)(b) the instrument must still be retained on the day`; `s 138(1A)(b) the last day of the period of 5 years for which the instrument must be retained` |  | sgk-tests-div8-register.l4 |
| 11416-11417 | s 138(1A)(a) | encoded | sgk-div8-register: `s 138(1A)(a) the instrument or copy is deemed to form part of the records required to be kept under section 199(1)` |  | sgk-tests-div8-register.l4 |
| 11419-11423 | s 138(1A)(b) | fork | sgk-div8-register: `s 138(1A)(b) the instrument must still be retained on the day`; `s 138(1A)(b) the last day of the period of 5 years for which the instrument must be retained` | F-K14 | sgk-tests-div8-register.l4 |
| 11425-11426 | s 138(1A)(b)(i) | encoded | as row s 138(1A)(b) |  | sgk-tests-div8-register.l4 |
| 11428-11430 | s 138(1A)(b)(ii) | encoded | as row s 138(1A)(b) |  | sgk-tests-div8-register.l4 |
| 11432-11436 | s 138(1A)(b)(iii) | encoded | as row s 138(1A)(b) |  | sgk-tests-div8-register.l4 |
| 11438-11444 | s 138(2) | encoded | sgk-div8-register: `s 138(2) the company must keep a register of charges at its registered office`; `s 138(2) the particulars the company must give of each charge in its register of charges` |  | sgk-tests-div8-register.l4 |
| 11446-11451 | s 138(3) | encoded | sgk-div8-register: `s 138(3) the fee the company has fixed is within the limit`; `s 138(3) the item must be open to the person's inspection`; `s 138(3) the most the company may charge for one inspection` |  | sgk-tests-div8-register.l4 |
| 11453-11457 | s 138(3A) | fork | sgk-div8-register: `s 138(3A) the company must furnish the copy within 3 days of the application`; `s 138(3A) the last day for furnishing the copy`; `s 138(3A) the most the company may charge for the copy, in Singapore dollars`; `s 138(3A) the person may be furnished with a copy of the instrument or debenture` | F-K15, F-K34 | sgk-tests-div8-register.l4 |
| 11459-11462 | s 138(4) | fork | sgk-div8-register: `s 138(4) the most the person may be sentenced to on conviction`; `s 138(4) the person is guilty of the offence of default in complying with section 138` | F-K10 | sgk-tests-div8-register.l4 |
| 11464 | marginal heading of s 139 | inert (reason 1: heading) | Documents made out of Singapore |  |  |
| 11466-11475 | s 139 | fork | sgk-div8-application: `s 139 the last day for lodging the document`; `s 139 the number of days added to the time specified`; `s 139 the time specified is extended by` | F-K1 | sgk-tests-div8-application.l4 |
| 11477 | marginal heading of s 140 | inert (reason 1: heading) | Charges, etc., created before 29 December 1967 |  |  |
| 11479-11482 | s 140 | fork | sgk-div8-application: `s 140 this Division applies to the charge` | F-K2 | sgk-tests-div8-application.l4 |
| 11484 | marginal heading of s 141 | inert (reason 1: heading) | Application of Division |  |  |
| 11486-11491 | s 141 | encoded | sgk-div8-application: `s 141 a reference in Division 8 to a company includes the foreign company`; `s 141 this Division applies to the charge of the foreign company` |  | sgk-tests-div8-application.l4 |
| 21886 | PART 8 | inert (reason 1: heading) | PART 8 |  |  |
| 21887 | ss 217 to 227 | repealed or blank in this text | sections 217 to 227 are shown as "[Repealed by Act 40 of 2018]" |  |  |
| 21889 | PART 8A | inert (reason 1: heading) | PART 8A |  |  |
| 21890 | ss 227AA to 227X | repealed or blank in this text | sections 227AA to 227X are shown as "[Repealed by Act 40 of 2018]" |  |  |
| 21892 | PART 9 | inert (reason 1: heading) | PART 9 |  |  |
| 21894 | INVESTIGATIONS | inert (reason 1: heading) | INVESTIGATIONS |  |  |
| 21896 | marginal heading of s 228 | inert (reason 1: heading) | Application of this Part |  |  |
| 21898-21900 | s 228 | fork | sgk-part9-declared: `s 228 Part 9 is barred from authorising the investigation`; `s 228 the provision is in Part 9` | F-K17 | sgk-tests-part9-declared.l4 |
| 21902 | marginal heading of s 229 | inert (reason 1: heading) | Interpretation |  |  |
| 21904 | s 229 | encoded | sgk-part9-declared: `s 229 "company" the body is within the word company`; `s 229 "declared company" the body is a declared company`; `s 229 "officer or agent" the person is an officer or agent of the corporation` |  | sgk-tests-part9-declared.l4 |
| 21906-21907 | s 229 “company” | encoded | sgk-part9-declared: `s 229 "company" the body is within the word company` |  | sgk-tests-part9-declared.l4 |
| 21909-21914 | s 229 “declared company” | encoded | sgk-part9-declared: `s 229 "declared company" the body is a declared company` |  | sgk-tests-part9-declared.l4 |
| 21916 | s 229 “officer or agent” | encoded | sgk-part9-declared: `s 229 "officer or agent" the person is an officer or agent of the corporation` |  | sgk-tests-part9-declared.l4 |
| 21918-21919 | s 229(a) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21921 | s 229(b) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21923-21924 | s 229(b)(i) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21926-21927 | s 229(b)(ii) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21929 | s 229(c) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21931-21932 | s 229(c)(i) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21934 | s 229(c)(ii) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21936-21938 | s 229(c)(iii) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21940-21942 | s 229(d) | encoded | as row s 229 “officer or agent” |  | sgk-tests-part9-declared.l4 |
| 21944 | marginal heading of s 230 | inert (reason 1: heading) | Power to declare company or foreign company |  |  |
| 21946-21948 | s 230 | fork | sgk-part9-declared: `s 230 the Minister may by order declare the body to be a company to which Part 9 applies` | F-K18 | sgk-tests-part9-declared.l4 |
| 21950-21954 | s 230(a) | encoded | as row s 230 |  | sgk-tests-part9-declared.l4 |
| 21956-21963 | s 230(b) | encoded | as row s 230 |  | sgk-tests-part9-declared.l4 |
| 21965-21967 | s 230(c) | encoded | as row s 230 |  | sgk-tests-part9-declared.l4 |
| 21969-21972 | s 230(d) | encoded | as row s 230 |  | sgk-tests-part9-declared.l4 |
| 21974 | marginal heading of s 231(1) | inert (reason 1: heading) | Appointment of inspectors for declared companies |  |  |
| 21976-21979 | s 231(1) | fork | sgk-part9-declared: `s 231(1) the Minister must appoint inspectors for a declared company`; `s 231(1) the Minister must appoint one or more inspectors to investigate the affairs of the company` | F-K5 | sgk-tests-part9-declared.l4 |
| 21981-21986 | s 231(2) | fork | sgk-part9-declared: `s 231(2) the Minister may take such steps as the Minister considers fit`; `s 231(2) the inspector may inform the Minister of the matters without making an interim report` | F-K7 | sgk-tests-part9-declared.l4 |
| 21988-21990 | s 231(3) | encoded | sgk-part9-declared: `s 231(3) the expenses are defrayed in the first instance out of moneys provided by Parliament` |  | sgk-tests-part9-declared.l4 |
| 21992-21997 | s 231(4) | fork | sgk-part9-declared: `s 231(4) the Minister may by notification in the Gazette direct that the expenses be paid by the payer` | F-K7 | sgk-tests-part9-declared.l4 |
| 21999-22001 | s 231(5) | encoded | sgk-part9-declared: `s 231(5) the notification may specify the time or times and the manner in which the payment of the expenses must be made` |  | sgk-tests-part9-declared.l4 |
| 22003-22009 | s 231(6) | fork | sgk-part9-declared: `s 231(6) the person named in the notification is liable to reimburse the Minister in respect of the expenses to the extent specified` | F-K19 | sgk-tests-part9-declared.l4 |
| 22011-22012 | s 231(7) | encoded | sgk-part9-declared: `s 231(7) action to recover the expenses may be taken in the name of the Government in any court of competent jurisdiction` |  | sgk-tests-part9-declared.l4 |
| 22014-22022 | s 231(8) | encoded | sgk-part9-declared: `s 231(8) the expenses ordered to be paid by the company are part of the costs and expenses of the winding up for the purposes of section 203(1)(a) of the Insolvency, Restructuring and Dissolution Act 2018` |  | sgk-tests-part9-declared.l4 |
| 22024-22028 | s 231(9) | fork | sgk-part9-declared: `s 231(9) the report may include a recommendation as to the terms of the notification`; `s 231(9) the report must include a recommendation as to the terms of the notification` | F-K5, F-K18 | sgk-tests-part9-declared.l4 |
| 22030-22031 | marginal heading of s 232(1) | inert (reason 1: heading) | Investigation of affairs of company by inspectors at directi |  |  |
| 22033-22036 | s 232(1) | fork | sgk-part9-inspectors: `s 232(1) the Minister may appoint inspectors on the application` | F-K24 | sgk-tests-part9-inspectors.l4 |
| 22038-22039 | s 232(1)(a) | encoded | as row s 232(1) |  | sgk-tests-part9-inspectors.l4 |
| 22041-22044 | s 232(1)(a)(i) | encoded | sgk-part9-inspectors: `s 232(1)(a)(i) the application is made by enough members` |  | sgk-tests-part9-inspectors.l4 |
| 22046-22047 | s 232(1)(a)(ii) | encoded | sgk-part9-inspectors: `s 232(1)(a)(ii) the application is made by enough debenture holders` |  | sgk-tests-part9-inspectors.l4 |
| 22049-22051 | s 232(1)(b) | encoded | sgk-part9-inspectors: `s 232(1)(b) the application is made by enough of the persons on the register of members` |  | sgk-tests-part9-inspectors.l4 |
| 22053-22057 | s 232(1)(c) | encoded | sgk-part9-inspectors: `s 232(1) the Minister may appoint inspectors on the application` |  | sgk-tests-part9-inspectors.l4 |
| 22059-22064 | s 232(2) | fork | sgk-part9-inspectors: `s 232(2) the Minister may require the applicants to give security for the cost of the investigation`; `s 232(2) the application must be supported by the evidence the Minister requires` | F-K5, F-K7 | sgk-tests-part9-inspectors.l4 |
| 22066 | marginal heading of s 233(1) | inert (reason 1: heading) | As to reports of inspectors |  |  |
| 22068-22077 | s 233(1) | fork | sgk-part9-inspectors: `s 233(1) the Minister must deliver a further copy of the report to the applicants`; `s 233(1) the Minister must forward a copy of the report to the registered office`; `s 233(1) the Minister must forward a copy of the report to the registered office of the company`; `s 233(1) the inspector may make interim reports to the Minister`; `s 233(1) the inspector must make an interim report to the Minister`; `s 233(1) the inspector must report to the Minister on the conclusion of the investigation` | F-K5 | sgk-tests-part9-inspectors.l4 |
| 22079-22082 | s 233(1A) | fork | sgk-part9-inspectors: `s 233(1A) the Minister must give a copy of the report to the person whose affairs it relates to`; `s 233(1A) the Minister must give the person a copy of the report` | F-K5, F-K20 | sgk-tests-part9-inspectors.l4 |
| 22084-22087 | s 233(1B) | fork | sgk-part9-inspectors: `s 233(1) the Minister must deliver a further copy of the report to the applicants`; `s 233(1) the Minister must forward a copy of the report to the registered office`; `s 233(1) the Minister must forward a copy of the report to the registered office of the company`; `s 233(1) the inspector may make interim reports to the Minister`; `s 233(1) the inspector must make an interim report to the Minister`; `s 233(1) the inspector must report to the Minister on the conclusion of the investigation`; `s 233(1A) the Minister must give a copy of the report to the person whose affairs it relates to`; `s 233(1A) the Minister must give the person a copy of the report` | F-K20 | sgk-tests-part9-inspectors.l4 |
| 22089-22093 | s 233(1C) | fork | sgk-part9-inspectors: `s 233(1C) the Minister must not give a copy of the report where legal proceedings might be unduly prejudiced`; `s 233(1C) the Minister must not give the person a copy of the report under subsection (1A)` | F-K25 | sgk-tests-part9-inspectors.l4 |
| 22095-22101 | s 233(1D) | fork | sgk-part9-inspectors: `s 233(1D) the court may order that a copy of the report or part of it be given to the person` | F-K20 | sgk-tests-part9-inspectors.l4 |
| 22103-22107 | s 233(2) | fork | sgk-part9-inspectors: `s 233(2) the Minister may cause the report to be printed and published`; `s 233(2) the Minister must refrain from publishing the report when the Attorney-General has certified that publication would be prejudicial` | F-K18 | sgk-tests-part9-inspectors.l4 |
| 22109-22115 | s 233(3) | fork | sgk-part9-inspectors: `s 233(3) the Minister must cause a prosecution to be instituted`; `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution`; `s 233(3) the officer or agent must give the assistance on being required by the Minister` | F-K5, F-K26 | sgk-tests-part9-inspectors.l4 |
| 22117-22125 | s 233(4) | fork | sgk-part9-inspectors: `s 233(4) the Minister may bring proceedings in the name of the company` | F-K18 | sgk-tests-part9-inspectors.l4 |
| 22127 | s 234 | repealed or blank in this text | section 234 is shown as "[Repealed by Act 13 of 1987]" |  |  |
| 22129 | marginal heading of s 235 | inert (reason 1: heading) | Investigation of affairs of related corporation |  |  |
| 22131-22136 | s 235 | fork | sgk-part9-inspectors: `s 235 the inspector may investigate the affairs of the other corporation` | F-K21, F-K22 | sgk-tests-part9-inspectors.l4 |
| 22138 | marginal heading of s 236(1) | inert (reason 1: heading) | Procedure and powers of inspector |  |  |
| 22140-22151 | s 236(1) | fork | sgk-part9-inspectors: `s 236(1) the inspector has power to investigate also the affairs of the other corporation`; `s 236(1) the inspector must report on the affairs of the other corporation so far as the inspector thinks the results of the investigation relevant`; `s 236(1) the inspector must report on the affairs of the related corporation` | F-K5, F-K18, F-K22, F-K23 | sgk-tests-part9-inspectors.l4 |
| 22153-22158 | s 236(2) | fork | sgk-part9-inspectors: `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation`; `s 236(2) the officer or agent must produce the books and documents and give the assistance`; `s 236(2) the officer or agent must produce to the inspector all books and documents in the officer's or agent's custody or power` | F-K5, F-K26 | sgk-tests-part9-inspectors.l4 |
| 22160-22166 | s 236(3) | encoded | sgk-part9-inspectors: `s 236(3) the inspector may require the person to appear for examination on oath or affirmation` |  | sgk-tests-part9-inspectors.l4 |
| 22168-22171 | s 236(4) | encoded | sgk-part9-inspectors: `s 236(4)(a) the inspector may take possession of all the books and documents`; `s 236(4)(b) the inspector may retain the books and documents for the time`; `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents` |  | sgk-tests-part9-inspectors.l4 |
| 22173 | s 236(4)(a) | encoded | sgk-part9-inspectors: `s 236(4)(a) the inspector may take possession of all the books and documents` |  | sgk-tests-part9-inspectors.l4 |
| 22175-22177 | s 236(4)(b) | encoded | sgk-part9-inspectors: `s 236(4)(b) the inspector may retain the books and documents for the time` |  | sgk-tests-part9-inspectors.l4 |
| 22179-22181 | s 236(4)(c) | encoded | sgk-part9-inspectors: `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents` |  | sgk-tests-part9-inspectors.l4 |
| 22183-22203 | s 236(4A) | fork | sgk-part9-inspectors: `s 236(4A) the inspector may require the person to produce all documents in the person's possession or under the person's control relating to the bank account` | F-K18 | sgk-tests-part9-inspectors.l4 |
| 22205-22217 | s 236(5) | fork | sgk-part9-inspectors: `s 236(5) the Court may punish the offender in like manner as if the offender had been guilty of contempt of the Court`; `s 236(5) the inspector may certify the failure or refusal to the Court` | F-K7, F-K18 | sgk-tests-part9-inspectors.l4 |
| 22219-22229 | s 236(6) | fork | sgk-part9-inspectors: `s 236(6) the answer is barred from use in a subsequent criminal proceeding`; `s 236(6) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` | F-K11, F-K27 | sgk-tests-part9-inspectors.l4 |
| 22231-22236 | s 236(7) | fork | sgk-part9-inspectors: `s 236(7) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` | F-K11 | sgk-tests-part9-inspectors.l4 |
| 22238-22243 | s 236(8) | encoded | sgk-part9-inspectors: `s 236(8) the inspector may cause notes of the examination to be recorded, reduced to writing and read to or by and signed by the person examined`; `s 236(8) the signed notes may be used in evidence in legal proceedings against the person` |  | sgk-tests-part9-inspectors.l4 |
| 22245 | marginal heading of s 237(1) | inert (reason 1: heading) | As to costs of investigations |  |  |
| 22247-22252 | s 237(1) | fork | sgk-part9-consequences: `s 237(1) the company investigated must pay the expenses of the investigation`; `s 237(1) who must pay the expenses of and incidental to the investigation` | F-K28 | sgk-tests-part9-consequences.l4 |
| 22254 | s 237(2) | encoded | sgk-part9-consequences: `s 237(2)(a) the amount the applicants must make good`; `s 237(2)(a) the applicants must make good the deficiency`; `s 237(2)(b) the balance paid out of moneys provided by Parliament` |  | sgk-tests-part9-consequences.l4 |
| 22256-22261 | s 237(2)(a) | fork | sgk-part9-consequences: `s 237(2)(a) the amount the applicants must make good`; `s 237(2)(a) the applicants must make good the deficiency` | F-K5 | sgk-tests-part9-consequences.l4 |
| 22263-22265 | s 237(2)(b) | encoded | sgk-part9-consequences: `s 237(2)(b) the balance paid out of moneys provided by Parliament` |  | sgk-tests-part9-consequences.l4 |
| 22267 | marginal heading of s 238 | inert (reason 1: heading) | Report of inspector to be admissible in evidence |  |  |
| 22269-22273 | s 238 | encoded | sgk-part9-consequences: `s 238 the copy is admissible in any legal proceedings as evidence of the inspector's opinion and of the facts upon which the opinion is based` |  | sgk-tests-part9-consequences.l4 |
| 22275 | marginal heading of s 239(1) | inert (reason 1: heading) | Powers of inspector in relation to a declared company |  |  |
| 22277-22284 | s 239(1) | encoded | sgk-part9-consequences: `s 239(1) the inspector may employ the persons the inspector considers necessary`; `s 239(1) the inspector may in writing authorise the employed person to do the thing` |  | sgk-tests-part9-consequences.l4 |
| 22286 | s 239(2) | encoded | sgk-part9-consequences: `s 239(2) the officer or agent is liable to be dealt with in the manner provided in section 236(5)` |  | sgk-tests-part9-consequences.l4 |
| 22288-22290 | s 239(2)(a) | encoded | as row s 239(2) |  | sgk-tests-part9-consequences.l4 |
| 22292-22297 | s 239(2)(b) | encoded | as row s 239(2) |  | sgk-tests-part9-consequences.l4 |
| 22299 | marginal heading of s 240(1) | inert (reason 1: heading) | Suspension of actions and proceedings by declared company |  |  |
| 22301-22307 | s 240(1) | fork | sgk-part9-consequences: `s 240(1) a person must not commence or proceed with an action or proceeding in a Court without the consent of the Minister during the suspension`; `s 240(1) the action or proceeding is barred without the consent of the Minister`; `s 240(1) the day falls within the suspension`; `s 240(1) the number of days from the appointment to the end of 3 months after the final report` | F-K16, F-K29, F-K30 | sgk-tests-part9-consequences.l4 |
| 22309-22310 | s 240(1)(a) | encoded | as row s 240(1) |  | sgk-tests-part9-consequences.l4 |
| 22312-22315 | s 240(1)(b) | encoded | as row s 240(1) |  | sgk-tests-part9-consequences.l4 |
| 22317-22320 | s 240(1)(b)(i) | encoded | as row s 240(1) |  | sgk-tests-part9-consequences.l4 |
| 22322-22331 | s 240(1)(b)(ii) | encoded | as row s 240(1) |  | sgk-tests-part9-consequences.l4 |
| 22333-22334 | s 240(2) | encoded | sgk-part9-consequences: `s 240(2) the action or proceeding is void and of no effect` |  | sgk-tests-part9-consequences.l4 |
| 22336 | marginal heading of s 241(1) | inert (reason 1: heading) | Winding up of company |  |  |
| 22338 | s 241(1) | fork | sgk-part9-consequences: `s 241(1) the Minister may apply to the Court for the winding up`; `s 241(1) the application is treated as having been made by` | F-K7 | sgk-tests-part9-consequences.l4 |
| 22340-22341 | s 241(1)(a) | encoded | as row s 241(1) |  | sgk-tests-part9-consequences.l4 |
| 22343-22350 | s 241(1)(b) | encoded | as row s 241(1) |  | sgk-tests-part9-consequences.l4 |
| 22352-22353 | s 241(1)(c) | encoded | as row s 241(1) |  | sgk-tests-part9-consequences.l4 |
| 22355-22362 | s 241(1)(d) | encoded | as row s 241(1) |  | sgk-tests-part9-consequences.l4 |
| 22364-22368 | s 241(2) | fork | sgk-part9-consequences: `s 241(2) the foreign company must not carry on business or establish or keep a place of business in Singapore`; `s 241(2) the foreign company must not carry on business or establish or keep a place of business in Singapore once the order is made` | F-K5 | sgk-tests-part9-consequences.l4 |
| 22370 | marginal heading of s 242(1) | inert (reason 1: heading) | Penalties |  |  |
| 22372-22377 | s 242(1) | fork | sgk-part9-consequences: `s 242(1) the most the person may be sentenced to on conviction`; `s 242(1) the person is guilty of the offence of defeating the purposes of Part 9 or obstructing an investigation` | F-K10 | sgk-tests-part9-consequences.l4 |
| 22379-22380 | s 242(1)(a) | encoded | as row s 242(1) |  | sgk-tests-part9-consequences.l4 |
| 22382-22389 | s 242(1)(b) | encoded | as row s 242(1) |  | sgk-tests-part9-consequences.l4 |
| 22391-22392 | s 242(2) | fork | sgk-part9-consequences: `s 242(2) the person bears the onus of proving that the person did not act with the intent` | F-K5 | sgk-tests-part9-consequences.l4 |
| 22394-22395 | s 242(2)(a) | encoded | as row s 242(2) |  | sgk-tests-part9-consequences.l4 |
| 22397-22404 | s 242(2)(b) | encoded | as row s 242(2) |  | sgk-tests-part9-consequences.l4 |
| 22406-22407 | marginal heading of s 243(1) | inert (reason 1: heading) | Appointment and powers of inspectors to investigate |  |  |
| 22409-22416 | s 243(1) | fork | sgk-part9-ownership: `s 243(1) the Minister may appoint inspectors to investigate the ownership of the corporation` | F-K7 | sgk-tests-part9-ownership.l4 |
| 22418-22426 | s 243(2) | encoded | sgk-part9-ownership: `s 243(2) the appointment may define the scope of the inspector's investigation` |  | sgk-tests-part9-ownership.l4 |
| 22428-22439 | s 243(3) | fork | sgk-part9-ownership: `s 243(3) the Minister must appoint an inspector to conduct the investigation`; `s 243(3) the appointment must not exclude the matter from the scope of the investigation` | F-K5, F-K31 | sgk-tests-part9-ownership.l4 |
| 22441-22446 | s 243(4) | fork | sgk-part9-ownership: `s 243(4) the inspector's powers extend to the investigation of the circumstances` | F-K32 | sgk-tests-part9-ownership.l4 |
| 22448-22452 | s 243(5) | encoded | sgk-part9-ownership: `s 243(5) the provisions of Part 9 on the investigation of declared companies apply to the investigation with the necessary modifications` |  | sgk-tests-part9-ownership.l4 |
| 22454-22467 | s 243(5)(a) | encoded | sgk-part9-ownership: `s 243(5)(a) Part 9 applies in relation to the person as it applies in relation to officers and agents of the corporation` |  | sgk-tests-part9-ownership.l4 |
| 22469-22477 | s 243(5)(b) | fork | sgk-part9-ownership: `s 243(5)(b) the Minister is not bound to furnish the person with a copy of the report or with a complete copy of it`; `s 243(5)(b) the Minister may cause a copy of the report or of the parts of it to be kept by the Registrar` | F-K18, F-K33 | sgk-tests-part9-ownership.l4 |
| 22479-22480 | marginal heading of s 244(1) | inert (reason 1: heading) | Power to require information as to persons interested in sha |  |  |
| 22482-22490 | s 244(1) | fork | sgk-part9-ownership: `s 244(1) the Minister may require the person to give the information to the Minister` | F-K7 | sgk-tests-part9-ownership.l4 |
| 22492-22498 | s 244(2) | encoded | sgk-part9-ownership: `s 244(2) the person is deemed to have an interest in the share or debenture for the purposes of section 244` |  | sgk-tests-part9-ownership.l4 |
| 22500-22506 | s 244(3) | fork | sgk-part9-ownership: `s 244(3) a person must give the information required of the person under section 244`; `s 244(3) a person must not make a statement to the Minister that the person knows to be false in a material particular, or recklessly make one`; `s 244(3) the most the person may be sentenced to on conviction`; `s 244(3) the person is guilty of the offence of failing to give information or giving false information` | F-K10, F-K34 | sgk-tests-part9-ownership.l4 |
| 22508-22516 | s 244(4) | encoded | sgk-part9-ownership: `s 244(4) section 244 applies to the banking corporation`; `s 244(4) section 244 requires the banking corporation to disclose the information to the Minister` |  | sgk-tests-part9-ownership.l4 |
| 22518-22525 | s 244(5) | encoded | sgk-part9-ownership: `s 244(5) the Minister may delegate the powers under section 244 to the delegate` |  | sgk-tests-part9-ownership.l4 |
| 22527-22532 | s 244(6) | fork | sgk-part9-ownership: `s 244(6) the committee or body must keep the Minister informed of any information obtained under section 244` | F-K5 | sgk-tests-part9-ownership.l4 |
| 22534-22536 | s 244(7) | encoded | sgk-part9-ownership: `s 244(7) the Minister may exercise the power despite a delegation of it` |  | sgk-tests-part9-ownership.l4 |
| 22538 | marginal heading of s 245(1) | inert (reason 1: heading) | Power to impose restrictions on shares or debentures |  |  |
| 22540-22544 | s 245(1) | fork | sgk-part9-ownership: `s 245(1) the Minister may by order in the Gazette direct that the shares are until further order subject to the restrictions`; `s 245(1) the act is void or barred by the restrictions` | F-K7, F-K30 | sgk-tests-part9-ownership.l4 |
| 22546-22549 | s 245(1)(a) | encoded | as row s 245(1) |  | sgk-tests-part9-ownership.l4 |
| 22551-22552 | s 245(1)(b) | encoded | as row s 245(1) |  | sgk-tests-part9-ownership.l4 |
| 22554-22555 | s 245(1)(c) | encoded | as row s 245(1) |  | sgk-tests-part9-ownership.l4 |
| 22557-22562 | s 245(1)(d) | encoded | as row s 245(1) |  | sgk-tests-part9-ownership.l4 |
| 22564-22570 | s 245(2) | encoded | sgk-part9-ownership: `s 245(2) the order may continue the application of subsection (1)(c) and (d) to the shares` |  | sgk-tests-part9-ownership.l4 |
| 22572-22573 | s 245(3) | fork | sgk-part9-ownership: `s 245(3) the most the person may be sentenced to on conviction`; `s 245(3) the person is guilty of the offence of dealing in shares subject to the restrictions` | F-K10 | sgk-tests-part9-ownership.l4 |
| 22575-22578 | s 245(3)(a) | encoded | as row s 245(3) |  | sgk-tests-part9-ownership.l4 |
| 22580-22581 | s 245(3)(b) | encoded | as row s 245(3) |  | sgk-tests-part9-ownership.l4 |
| 22583-22592 | s 245(3)(c) | encoded | as row s 245(3) |  | sgk-tests-part9-ownership.l4 |
| 22594-22598 | s 245(4) | fork | sgk-part9-ownership: `s 245(4) the company is guilty of the offence of issuing shares in contravention of the restrictions`; `s 245(4) the company must not issue shares in contravention of the restrictions`; `s 245(4) the most the person may be sentenced to on conviction`; `s 245(4) the officer is guilty of the offence of issuing shares in contravention of the restrictions` | F-K10, F-K34 | sgk-tests-part9-ownership.l4 |
| 22600-22601 | s 245(5) | encoded | sgk-part9-ownership: `s 245(5) the prosecution is barred for want of the consent of the Public Prosecutor` |  | sgk-tests-part9-ownership.l4 |
| 22603-22607 | s 245(6) | encoded | sgk-part9-ownership: `s 245(6) section 245 applies to the debentures as it applies to shares` |  | sgk-tests-part9-ownership.l4 |
| 22609 | marginal heading of s 246 | inert (reason 1: heading) | Inspectors appointed in other countries |  |  |
| 22611 | s 246 | fork | sgk-part9-ownership: `s 246 the Minister may by notice declare that the inspector is to have the same powers and duties in Singapore as an inspector appointed under section 231`; `s 246 the inspector has the powers and duties of an inspector appointed under section 231` | F-K7 | sgk-tests-part9-ownership.l4 |
| 22613-22615 | s 246(a) | encoded | as row s 246 |  | sgk-tests-part9-ownership.l4 |
| 22617-22625 | s 246(b) | encoded | as row s 246 |  | sgk-tests-part9-ownership.l4 |

## Fork register (sgk)

One entry per fork id F-K1 to F-K34; the modules carry the same ids in their comments (`-- fork F-Kn`).
Each entry gives the provision, the function, the answer taken, the other reading, and the text that licenses each.
Where an entry is a split site of the brief's two questions it names the line of `inputs/ENCODING-GUIDE.md` section 5 that the answer relies on, quoting the Guide's own words.
The Guide's lines are cited by line number of that file: line 86 and line 87 ("In short ..." and "Everywhere else it answers ..."), line 92 (N2), line 93 (the periods ruling of 2026-11-05), line 94 (the delegated-definitions ruling of 2026-11-05, item (c)), line 95 (the case-by-case ruling of 2026-11-05), line 96 (the grant ruling of 2026-11-12) and lines 97 to 99 (its three limits).
"JUST FALSE" is the text's own no; "NOTHING" is "the text does not say".
Every site named here is a function of the module named in the coverage table; the names are exact, so a grep finds them.

**F-K1. s 139: "7 days or such further periods".**
Functions: `s 139 the number of days added to the time specified`, `s 139 the time specified is extended by`, `s 139 the last day for lodging the document`.
Taken: the time is extended by 7 days plus any further days the Registrar has allowed (the further days are an input, `the number of further days the Registrar has allowed`).
Other reading: "7 days or such further periods" as alternatives, so that an allowance replaces the 7 days.
Text: "extended by 7 days or such further periods as the Registrar may from time to time allow".

**F-K2. s 140: "Except as is otherwise expressly provided".**
Function: `s 140 this Division applies to the charge`.
Taken: where another provision of the Division expressly provides otherwise, JUST FALSE (an "except" once it is met).
Other reading: NOTHING, because the section does not say what the other provision provides.
Guide: line 95, "an 'unless' or 'except' once it is met" is "decided site by site".
Text: "Except as is otherwise expressly provided, this Division applies to any charge that on 29 December 1967 was registrable under any of the repealed written laws but which at that date was not registered under any of those laws."

**F-K3. s 131(3B) and (3C): the aircraft exclusion, and "registered" borrowed from another Act.**
Function: `s 131(3) the charge is one to which section 131 applies` (and `s 131(3) the charge falls within one of paragraphs (a) to (j)`).
Taken: JUST FALSE for a charge created on or after 1 May 2009 that is capable of being registered under the International Interests in Aircraft Equipment Act 2009: "does not include" is a flat negative (Guide line 92, N2).
The capability is one input, `the charge is capable of being registered under the International Interests in Aircraft Equipment Act 2009`, asked for the charge as a whole; "registered" has the meaning of section 2(1) of that Act (s 131(3C)), which is not among the sources.
Other reading: "to the extent that" splits a charge that is capable of registration in part, so that section 131 still reaches the remainder; the function answers for the charge as a whole, and a caller with a charge that is partly capable asks twice, once for each part.
Text: "A charge mentioned in subsection (3) does not include a charge created at any time on or after 1 May 2009 to the extent that it is capable of being registered under the International Interests in Aircraft Equipment Act 2009."

**F-K4. ss 131(1), 131(6), 133(1): "within 30 days after".**
Functions: `s 131(1) the statement is lodged within 30 days after the creation of the charge`, `s 131(6) the particulars of the issue are lodged within 30 days after the issue`, `s 133(1) the statement is lodged within 30 days after the date`, and the three rules `s 131(1) the company must lodge ...`, `s 131(6) the company must lodge ...`, `s 133(1) the company must cause the statement to be lodged within 30 days`.
Taken: a deadline.
Lodging not later than the 30th day after the day of the event is in time, and a lodging on the day of the event itself is in time (the keel's `period: the date is not later than the end of a period after`, conventions P1 and P2 of `sg-periods.l4`); outside the period the answer is JUST FALSE (the periods ruling, Guide line 93, item (a): "a period the text fixes in its own words ('within one month' ...): outside the period the answer is `JUST FALSE`").
Other reading: "within 30 days after" as a window that opens on the day after the event (P2's other half, `period: the date is within a period after`), so that a lodging on the very day of the event is not "within" it.
Text: "there must be lodged with the Registrar in the prescribed manner for registration, within 30 days after the creation of the charge, a statement containing the prescribed particulars of the charge".

**F-K5. A duty or prohibition whose "if", "where" or "upon" gate is unmet answers JUST FALSE (23 sites).**
Taken: JUST FALSE, the provision's own question.
Other reading: NOTHING, because the gate is a limit of the duty in its own wording and "the case falls outside the limit".
Guide: line 95, "a duty whose 'if' or 'where' is unmet" is one of the six questions "decided site by site"; line 93, item (b): "a 'where ...' condition: when it fails the answer is `JUST FALSE`"; line 94, item (c): "'when', 'upon' and 'whenever' count as 'where'"; line 98 (limit 2 of the grant ruling): "keep `JUST FALSE` ... for a bar, a duty or the provision's own question"; against them line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit".
The 23 sites, each one function:

| provision | function | gate |
| --- | --- | --- |
| s 131(1) | `s 131(1) a statement of the charge must be lodged with the Registrar` | "where a charge to which this section applies is created by a company" |
| s 131(1A) | `s 131(1A) the instrument or a certified true copy must be produced to the Registrar` | "upon the Registrar's request" |
| s 131(7) | `s 131(7) the particulars required to be lodged must include the amount or rate per cent of the commission, allowance or discount` | "Where any commission, allowance or discount has been paid" |
| s 133(1) | `s 133(1) the company must cause a statement of the prescribed particulars of the charge to be lodged with the Registrar` | "Where" one of paragraphs (a) to (c) |
| s 134(3) | `s 134(3) the Registrar must issue to the company a certificate confirming the registration of the charge` | "Upon the application of the company and payment of the prescribed fee" |
| s 136(1) | `s 136(1) the Registrar must enter the particulars of the statement in the register` | the duty follows the lodging of the statement |
| s 231(1) | `s 231(1) the Minister must appoint one or more inspectors to investigate the affairs of the company` | "Where a company or foreign company has been declared" |
| s 231(9) | `s 231(9) the report must include a recommendation as to the terms of the notification` | "must, if the Minister so directs" |
| s 232(2) | `s 232(2) the application must be supported by the evidence the Minister requires` | "such evidence as the Minister requires" |
| s 233(1) | `s 233(1) the inspector must make an interim report to the Minister` | "if so directed by the Minister" |
| s 233(1) | `s 233(1) the Minister must forward a copy of the report to the registered office of the company` | after the report on the conclusion of the investigation |
| s 233(1) | `s 233(1) the Minister must deliver a further copy of the report to the applicants` | "at the request of the applicants" |
| s 233(1A) | `s 233(1A) the Minister must give the person a copy of the report` | "to whom in the opinion of the Minister the report ought to be given" |
| s 233(3) | `s 233(3) the Minister must cause a prosecution to be instituted` | "If from any report ... it appears to the Minister that the case is one in which a prosecution ought to be instituted" |
| s 233(3) | `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution` | "on being required by the Minister" |
| s 236(1) | `s 236(1) the inspector must report on the affairs of the other corporation so far as the inspector thinks the results of the investigation relevant` | the duty follows the investigation of the other corporation |
| s 236(2) | `s 236(2) the officer or agent must produce to the inspector all books and documents in the officer's or agent's custody or power` | "if required by an inspector" |
| s 237(2)(a) | `s 237(2)(a) the amount the applicants must make good` | "if the company fails to pay the whole or any part of the sum" |
| s 241(2) | `s 241(2) the foreign company must not carry on business or establish or keep a place of business in Singapore` | "Where, in the case of a foreign company, on any application under subsection (1) an order is made" |
| s 242(2) | `s 242(2) the person bears the onus of proving that the person did not act with the intent` | "If in any prosecution for an offence under this section it is proved" |
| s 243(3) | `s 243(3) the Minister must appoint an inspector to conduct the investigation` | "Where an application ... is made to the Minister by members of the corporation" |
| s 243(3) | `s 243(3) the appointment must not exclude the matter from the scope of the investigation` | the same "Where" |
| s 244(6) | `s 244(6) the committee or body must keep the Minister informed of any information obtained under section 244` | "in the discharge of its powers under that subsection" |

**F-K6. s 131(1), (6): "there must be lodged" names no bearer.**
Functions: `s 131(1) the company must lodge the statement of the charge within 30 days after the creation of the charge`, `s 131(6) the company must lodge the particulars of each issue within 30 days after it`, and the facts functions of the same subsections.
Taken: the company is the party, because s 132(1) lets "the company concerned or ... any person interested" lodge and puts the default on "the company and every officer of the company who is in default".
Other reading: no bearer (the text says only that the statement "must be lodged"), so that the duty is a state of affairs and not a duty of anyone; the facts functions answer without a party either way.
Text: "there must be lodged with the Registrar in the prescribed manner for registration" (s 131(1)); "there must be lodged within 30 days after each issue particulars of the date and amount of each issue" (s 131(6)).

**F-K7. A "may" gated by "where", "when" or "upon" answers JUST FALSE (11 sites; split site type (ii); the Guide's own question, listed, not decided).**
Taken: JUST FALSE, by the periods ruling.
Other reading: NOTHING, by the grant ruling.
Guide: line 93, item (b): "a 'where ...' condition: when it fails the answer is `JUST FALSE`"; line 94, item (c): "'when', 'upon' and 'whenever' count as 'where'"; against them line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit"; line 99 (limit 3): "do not change, but list in the row's fork register for the maintainer or a lawyer, a 'may' function whose gate is 'where', 'when' or 'upon'".
The 11 sites, with the gate; the first seven are "where", the eighth is "thereupon", and the last three are time gates that I took by analogy with "when" (a site that fits line 94 only by analogy, listed also under Marginal readings):

| provision | function | gate |
| --- | --- | --- |
| s 131(4) | `s 131(4) the statement may be lodged even though further proceedings are necessary under the law of the place where the property is` | "Where a charge created in Singapore affects property outside Singapore" |
| s 136(1) | `s 136(1) the company may lodge with the Registrar a statement of satisfaction or release` | "Where, with respect to any registered charge" |
| s 231(4) | `s 231(4) the Minister may by notification in the Gazette direct that the expenses be paid by the payer` | "Where the Minister is of the opinion" |
| s 243(1) | `s 243(1) the Minister may appoint inspectors to investigate the ownership of the corporation` | "Where it appears to the Minister that there is good reason to do so" |
| s 244(1) | `s 244(1) the Minister may require the person to give the information to the Minister` | "Where it appears to the Minister that there is good reason" |
| s 245(1) | `s 245(1) the Minister may by order in the Gazette direct that the shares are until further order subject to the restrictions` | "Where in connection with an investigation under section 243 or 244 it appears to the Minister" |
| s 246 | `s 246 the Minister may by notice declare that the inspector is to have the same powers and duties in Singapore as an inspector appointed under section 231` | "Where — (a) ... and (b) the Minister is of the opinion" |
| s 236(5) | `s 236(5) the Court may punish the offender in like manner as if the offender had been guilty of contempt of the Court` | "thereupon" inquire and "after hearing" |
| s 231(2) | `s 231(2) the Minister may take such steps as the Minister considers fit` | "thereafter" |
| s 232(2) | `s 232(2) the Minister may require the applicants to give security for the cost of the investigation` | "before appointing an inspector" |
| s 241(1) | `s 241(1) the Minister may apply to the Court for the winding up` | "at any time after a report has been made" |

**F-K8. s 131(5): "it is sufficient if there is lodged".**
Function: `s 131(5) the lodging of the statement is sufficient`.
Taken: JUST FALSE when the lodging does not meet paragraphs (a) to (d) or the 30 days (an "if" unmet, reading (a)).
Other reading: NOTHING, because "sufficient if" gives a safe harbour and does not say that another lodging is insufficient.
Guide: line 86, "a condition the text introduces with 'if'".
Text: "it is sufficient if there is lodged with the Registrar for registration within 30 days after the execution of the instrument containing the charge".

**F-K9. s 131(10): "unless it is proved to the satisfaction of the Court".**
Function: `s 131(10) the subsequent charge is not operative and has no validity as respects the property comprised in the prior charge`.
Taken: when the Court has been satisfied that the subsequent charge was given in good faith, JUST FALSE (the charge is operative); the Court's satisfaction is an input, a judgment the text hands to the Court.
Other reading: NOTHING (an "unless" once met, Guide line 95).
Text: "the subsequent charge is not operative and does not have any validity unless it is proved to the satisfaction of the Court that it was given in good faith".

**F-K10. An unmet element of an offence (split site type (i); 9 sites).**
Taken: JUST FALSE, because the function is the provision's own question (is the person guilty of the offence?) and the element is a limit that the text states in the same sentence as the offence.
Other reading: NOTHING, because "knowingly and wilfully", "default" and "intent" are limits of a prohibition in its own wording, and the case outside the limit is then outside what the text says.
Guide: line 98 (limit 2): "keep `JUST FALSE` ... for a bar, a duty or the provision's own question"; line 92 (N2): "flat negatives count as a no"; against them line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit".
These sites fit line 98 and also line 87; they are listed under Marginal readings.
The penalty functions of the same provisions answer NOTHING for a person the text does not make guilty, because the penalty is fixed only for a person the subsection makes guilty.
The 9 sites:

| provision | function | element |
| --- | --- | --- |
| s 132(1) | `s 132(1) the person is guilty of the offence of default in complying with section 131` | "if default is made in complying with that section the company and every officer of the company who is in default" |
| s 133(2) | `s 133(2) the person is guilty of the offence of default in complying with section 133` | "If default is made in complying with this section" |
| s 135(3) | `s 135(3) the person is guilty of the offence of authorising or permitting the delivery of an unendorsed debenture or certificate` | "knowingly and wilfully authorises or permits" |
| s 138(4) | `s 138(4) the person is guilty of the offence of default in complying with section 138` | "If default is made in complying with this section" |
| s 242(1) | `s 242(1) the person is guilty of the offence of defeating the purposes of Part 9 or obstructing an investigation` | "with intent to defeat the purposes of this Part" |
| s 244(3) | `s 244(3) the person is guilty of the offence of failing to give information or giving false information` | "fails to give any information required" or a false statement |
| s 245(3) | `s 245(3) the person is guilty of the offence of dealing in shares subject to the restrictions` | "having knowledge that the shares are subject to any such restrictions" and paragraphs (a) to (c) |
| s 245(4) | `s 245(4) the officer is guilty of the offence of issuing shares in contravention of the restrictions` | "every officer of the company who is in default" |
| s 245(4) | `s 245(4) the company is guilty of the offence of issuing shares in contravention of the restrictions` | "Where shares in any company are issued in contravention of the restrictions" |

"Officer in default" is an input at the four sites that name it (s 132(1), s 133(2), s 138(4), s 245(4)): the Act's s 408(3) defines the phrase and is not in my ranges.

**F-K11. "Entitled"-named functions (3 sites; the Guide's own question, listed, not decided).**
Sites: `s 132(2) the person is entitled to recover the fees from the company`, `s 236(6) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person`, `s 236(7) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person`.
Taken: JUST FALSE where the text's own words say no: s 132(2) when "registration is effected by some person other than the company" does not hold (a "where" unmet, line 93 item (b)); s 236(6) from "No person ... is entitled to refuse" (a flat negative, line 92); s 236(7) when "Subject to subsection (6)" takes the entitlement away.
Other reading: NOTHING, because an entitlement is a claim and not a power and the Guide does not settle it.
Guide: line 99 (limit 3): "an 'entitled'-named function (an entitlement is a claim, not a power, and this guide does not settle it)".

**F-K12. s 133(1): "the date on which the acquisition is completed or the date of the registration ..., as the case may be".**
Functions: `s 133(1) the last day for lodging the statement`, `s 133(1) the statement is lodged within 30 days after the date`.
Taken: paragraph (a), a company that acquires property, runs from the completion of the acquisition; paragraphs (b) and (c), a foreign company that becomes registered, run from its registration in Singapore.
Other reading: the later (or the earlier) of the two dates in every case; for (c) the acquisition precedes the registration, so a reading from the acquisition date would give a day that has passed before the duty arose.
Text: "within 30 days after the date on which the acquisition is completed or the date of the registration of the company in Singapore, as the case may be".

**F-K13. s 137: the Court's power "on being satisfied" and "on the application of" (split site type (ii)).**
Function: `s 137 the Court may order that the time for registration be extended or that the omission or mis-statement be rectified`.
Taken: NOTHING outside the application, because the section does not say that the Court may not act otherwise.
Other reading: JUST FALSE, if "on the application of" is read as "upon" and so as "where" under line 94.
Guide: line 87, "limits a grant or prohibition in its own wording and the case falls outside the limit".
This gate is neither an "if" (limit 1 of the grant ruling) nor a "where", "when" or "upon" (limit 3): it fits none of the Guide's lines exactly and is listed under Marginal readings.
Text: "may on the application of the company or any person interested and on such terms and conditions as seem to the Court just and expedient ... order that the time for registration be extended".

**F-K14. s 138(1A)(b): "a period of 5 years after" the date of the debt's satisfaction, or of the release, or "the later of the dates".**
Functions: `s 138(1A)(b) the last day of the period of 5 years for which the instrument must be retained`, `s 138(1A)(b) the instrument must still be retained on the day`.
Taken: with only one of the two events, the 5 years run from that event; with both, from the later; with neither, no day is fixed (NOTHING, "limited by its own wording").
Other reading: the retention ends only when both events have occurred, so that after one event alone no end day yet exists.
Text: "(iii) where both of the events referred to in sub-paragraphs (i) and (ii) occur in any particular case, the later of the dates".

**F-K15. s 138(3A): "on application to a company and on payment of a fee" (split site type (ii)).**
Function: `s 138(3A) the person may be furnished with a copy of the instrument or debenture`.
Taken: NOTHING for a person who has not applied or paid, because the subsection does not say that such a person may not.
Other reading: JUST FALSE, if "on application" is read as "upon application" and so as "where" (line 94, item (c)).
Guide: line 87, "limits a grant or prohibition in its own wording and the case falls outside the limit".
Fits none of the Guide's lines exactly (the gate is "on", not "upon"); listed under Marginal readings.
Text: "Any person may, on application to a company and on payment of a fee, not exceeding $1 for every page or part thereof, be furnished with a copy of any instrument or debenture kept by the company pursuant to this section within 3 days of the person making the application."

**F-K16. A prohibition derived from a duty or a bar for as long as it lasts (2 sites).**
Sites: `s 138(1) the company must not cease to keep the instrument or a copy at its registered office while the charge remains in force` (derived from "for as long as the charge to which the instrument relates remains in force"), and `s 240(1) a person must not commence or proceed with an action or proceeding in a Court without the consent of the Minister during the suspension` (derived from "no action or proceeding may ... be commenced or proceeded with").
Taken: a `SHANT ... WITHIN n` rule where n is the number of days the charge remains in force, or the suspension lasts; it sunsets at day n, which is the point of the construct.
Guide: line 92 (N2): "where the text names the bearer the prohibition (`SHANT`) is derived from that answer".
Other reading: no deontic rule for these two; the facts function alone.
For s 240(1) the text does not name the bearer; the person who would sue is taken (`s 231 a person`).

**F-K17. s 228: "unless specifically provided for in this Part".**
Function: `s 228 Part 9 is barred from authorising the investigation`.
Taken: where this Part specifically provides for the investigation, JUST FALSE (an "unless" once it is met).
Other reading: NOTHING (Guide line 95).
Text: "This Part does not authorise any investigation into the insurance business of a company or into the business of a banking corporation, unless specifically provided for in this Part."

**F-K18. A "may" or "power" function with an "if" gate answers NOTHING when the gate fails (8 sites; grant ruling, limit 1).**
Taken: NOTHING.
Other reading: JUST FALSE (reading (a): a failed "if" counts as the text's no).
Guide: line 97 (limit 1): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ('may', 'is permitted to', 'has power to') whose `if` gate failed".
The 8 sites, one fork line each:

| provision | function | gate |
| --- | --- | --- |
| s 230 | `s 230 the Minister may by order declare the body to be a company to which Part 9 applies` | "if the Minister is satisfied" of a listed ground |
| s 231(9) | `s 231(9) the report may include a recommendation as to the terms of the notification` | "may if the inspector thinks fit" |
| s 233(2) | `s 233(2) the Minister may cause the report to be printed and published` | "if he or she is of the opinion that it is necessary in the public interest" |
| s 233(4) | `s 233(4) the Minister may bring proceedings in the name of the company` | "If from any report ... it appears to the Minister that proceedings ought in the public interest to be brought" |
| s 236(1) | `s 236(1) the inspector has power to investigate also the affairs of the other corporation` | "If an inspector ... thinks it necessary" |
| s 236(4A) | `s 236(4A) the inspector may require the person to produce all documents in the person's possession or under the person's control relating to the bank account` | "If an inspector has reasonable grounds for believing" |
| s 236(5) | `s 236(5) the inspector may certify the failure or refusal to the Court` | "If any officer or agent ... fails to comply" |
| s 243(5)(b) | `s 243(5)(b) the Minister may cause a copy of the report or of the parts of it to be kept by the Registrar` | "if the Minister thinks fit" |

**F-K19. s 231(6): "published by the Minister under subsection (5)".**
Function: `s 231(6) the person named in the notification is liable to reimburse the Minister in respect of the expenses to the extent specified`.
Taken: the notification is the one published under subsection (4) that subsection (5) says may specify time and manner; the function asks "a notification has been published" and answers JUST FALSE where none was (a "where" unmet).
Other reading: only a notification that itself specifies time and manner under (5) founds the liability.
Text: "Where a notification has been published by the Minister under subsection (5), the persons named in the notification to the extent therein specified shall be liable to reimburse the Minister in respect of such expenses."

**F-K20. s 233(1A) to (1D): the court's order and the Minister's grounds.**
Function: `s 233(1A) the Minister must give the person a copy of the report` (and `s 233(1D) the court may order that a copy of the report or part of it be given to the person`).
Taken: a court order under (1D) that a copy "must be given" to the person prevails over (1C), which is "Subject to subsection (1D)", and I let it prevail over (1B) as well.
Other reading: the order prevails over (1C) only, because only (1C) says "Subject to subsection (1D)", and (1B), "not bound to furnish", stands.
Text: "(1D) A court before which legal proceedings are brought against a person for or in respect of matters dealt with in a report under this Part may order that a copy of the report or part thereof must be given to that person."

**F-K21. s 235: "with the consent in writing of the Minister" (split site type (ii)).**
Function: `s 235 the inspector may investigate the affairs of the other corporation`.
Taken: NOTHING without the Minister's consent, because the section does not say that the inspector may not.
Other reading: JUST FALSE ("with the consent" as a condition).
Guide: line 87, "limits a grant or prohibition in its own wording and the case falls outside the limit".
Fits none of the lines exactly (the gate is "with the consent of", which the Guide names in the brief but not in section 5); listed under Marginal readings.
Text: "the inspector may, with the consent in writing of the Minister, investigate the affairs of that corporation."

**F-K22. s 235 against s 236(1): two sections on the same power.**
Functions: `s 235 the inspector may investigate the affairs of the other corporation` and `s 236(1) the inspector has power to investigate also the affairs of the other corporation`.
Section 235 gives the power "with the consent in writing of the Minister"; section 236(1) says that the inspector, if the inspector "thinks it necessary", "has power to do so" and says nothing of consent.
Taken: each is answered on its own words and neither overrides the other; the seat asks section 235 and section 236(1) separately.
Other reading: section 236(1) is the power and section 235 the Minister's consent for the case it covers (so the inspector needs consent), or section 235 is the specific rule and governs.
The text does not say.

**F-K23. s 236(2): two duties in one sentence.**
Functions: `s 236(2) the officer or agent must produce to the inspector all books and documents in the officer's or agent's custody or power`, `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation`, `s 236(2) the officer or agent must produce the books and documents and give the assistance`.
Taken: two duties; only the first depends on the requirement ("if required by an inspector").
Other reading: "if required" governs both.
Text: "must, if required by an inspector appointed under this Part, produce to the inspector all books and documents in the officer's or agent's custody or power and must give to the inspector all assistance in connection with the investigation which he or she is reasonably able to give."

**F-K24. s 232(1): "on the application of" (split site type (ii)).**
Function: `s 232(1) the Minister may appoint inspectors on the application`.
Taken: NOTHING for an application the paragraphs do not name, because the section does not say that the Minister may not act on any other.
Other reading: JUST FALSE ("on the application" read as "upon", line 94, item (c)).
Guide: line 87, "limits a grant or prohibition in its own wording and the case falls outside the limit".
Fits none of the lines exactly; listed under Marginal readings.
The thresholds (200 members, 10% of shares issued, 20% in nominal value of debentures, 20% in number of the persons on the register) are tested in `s 232(1)(a)(i) the application is made by enough members` and its two siblings, with a test on each side of each threshold.

**F-K25. s 233(1C): the bar "if the Minister believes".**
Function: `s 233(1C) the Minister must not give the person a copy of the report under subsection (1A)`.
Taken: JUST FALSE when the Minister does not hold the belief, or when a court order under (1D) applies; a bar's own question (limit 2, line 98).
Other reading: NOTHING (a failed "if" on a prohibition limits it in its own wording).
Text: "Subject to subsection (1D), the Minister must not give a copy of a report made under this Part to a person under subsection (1A) if the Minister believes that legal proceedings that have been or, in the Minister's opinion, might be instituted, might be unduly prejudiced by giving the report to that person."

**F-K26. "All assistance ... which they are reasonably able to give".**
Sites: `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution`, `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation`.
Taken: JUST FALSE when the person is not reasonably able, the duty's own question (limit 2, line 98).
Other reading: NOTHING, because the duty is limited in its own wording.
Text: "give all assistance in connection with the prosecution which they are reasonably able to give" (s 233(3)); "all assistance in connection with the investigation which he or she is reasonably able to give" (s 236(2)).

**F-K27. s 236(6): "except in the case of a charge against the person for making a false statement".**
Function: `s 236(6) the answer is barred from use in a subsequent criminal proceeding`.
Taken: JUST FALSE for the case of a charge for making a false statement (an "except" once it is met).
Other reading: NOTHING (Guide line 95).
Text: "the answer to the question may not be used in any subsequent criminal proceedings except in the case of a charge against the person for making a false statement in answer to that question."

**F-K28. s 237(1): "sections 232 and 243".**
Function: `s 237(1) who must pay the expenses of and incidental to the investigation`.
Taken: "and" read as "or": an inspector appointed under section 232 or under section 243 (no appointment is under both).
For an inspector appointed under section 231 the subsection says nothing, and the answer is NOTHING; section 231(3) and (4) deal with the expenses of a declared company.
Other reading: the subsection reaches only an appointment under both sections, which cannot occur.
Text: "The expenses of and incidental to an investigation by an inspector appointed pursuant to sections 232 and 243 (including the costs of any proceedings brought by the Minister in the name of the company), must be paid by the company investigated or if the Minister so directs by the applicants or in part by the company and in part by the applicants."

**F-K29. s 240(1) "any declared company" against s 243(5).**
Function: `s 240(1) the action or proceeding is barred without the consent of the Minister`.
Taken: NOTHING for a corporation that is not a declared company, because section 243(5) applies "the provisions of this Part with respect to the investigation of declared companies" to an ownership investigation "with the necessary modifications", and whether that carries the suspension of section 240 the text does not say.
Other reading: the suspension applies to a corporation under an investigation of ownership (JUST TRUE), or does not (JUST FALSE).
Text: "On and after the appointment of an inspector in respect of any declared company until the expiration of 3 months after the inspector has presented the inspector's final report to the Minister, no action or proceeding may without the consent of the Minister ... be commenced or proceeded with in any Court".

**F-K30. A list the text does not close with "only" (2 sites).**
Sites: `s 240(1) the action or proceeding is barred without the consent of the Minister` (the list (a) and (b) of proceedings that the bar covers) and `s 245(1) the act is void or barred by the restrictions` (the restrictions (a) to (d), introduced by "the following restrictions").
Taken: JUST FALSE for an act that is on neither list, because the list is the text's statement of what the bar or the order covers.
Other reading: NOTHING, because Guide line 87 closes a list only "with 'only'" and neither list is closed that way.
Both sites are listed under Marginal readings.

**F-K31. s 243(3): "not less than that required for an application ... under section 232".**
Function: `s 243(3) the Minister must appoint an inspector to conduct the investigation`.
Taken: whether the number of applicants or the amount of shares meets the section 232 threshold is an input, `the number of applicants or the amount of the shares held by them is not less than that required for an application for the appointment of an inspector under section 232`; the section 232(1) functions (`s 232(1)(a)(i) the application is made by enough members` and the two siblings) are there for a caller who wants to compute it.
Other reading: compute it inside section 243(3); not done because section 232(1) is stated for a company, and section 243 reaches "any corporation".
Where the threshold is unmet the answer is JUST FALSE (a "where" unmet on a duty, F-K5).

**F-K32. s 243(4): "Subject to the terms of an inspector's appointment".**
Function: `s 243(4) the inspector's powers extend to the investigation of the circumstances`.
Taken: "subject to" read as "unless" (the terms of the appointment otherwise provide): JUST FALSE where the terms exclude the circumstances.
Other reading: NOTHING.
Text: "Subject to the terms of an inspector's appointment, the inspector's powers extend to the investigation of any circumstances suggesting the existence of an arrangement or understanding".

**F-K33. s 243(5)(b): "the Minister is not bound ... if the Minister is of opinion".**
Function: `s 243(5)(b) the Minister is not bound to furnish the person with a copy of the report or with a complete copy of it`.
Taken: JUST TRUE when the Minister is of the opinion; NOTHING otherwise, as for a grant with an "if" gate (the ruling's limit 1, applied by analogy: the function is named for an exemption, not a "may").
Other reading: JUST FALSE when the Minister is not of the opinion (the Minister is then bound).
Text: "the Minister is not bound to furnish the corporation or any other person with a copy of any report by an inspector appointed under this section or with a complete copy thereof if the Minister is of opinion that there is good reason for not divulging the contents of the report or of parts thereof".

**F-K34. A rule derived from an offence or from an entitlement (10 regulative rules).**
Taken: where the text makes an act an offence and names the person ("Every person who knowingly and wilfully authorises or permits ...", "Any person who, with intent ...", "the company and every officer of the company who is in default"), the prohibition or duty is a regulative rule for that person, derived from the offence.
Where the text states a person's entitlement and a time, and names no one who must act (s 138(3A)), the duty is the company's.
The 10 rules:

| provision | rule | derived from |
| --- | --- | --- |
| s 135(3) | `s 135(3) a person must not knowingly and wilfully authorise or permit the delivery of an unendorsed debenture or certificate` | the offence of s 135(3) |
| s 138(3A) | `s 138(3A) the company must furnish the copy within 3 days of the application` | "Any person may, on application to a company and on payment of a fee ... be furnished with a copy ... within 3 days of the person making the application": the company is the only party the sentence mentions |
| s 242(1)(a) | `s 242(1)(a) a person must not destroy, conceal or alter a book, document or record of a declared company with intent to defeat the purposes of Part 9` | the offence of s 242(1) |
| s 242(1)(b) | `s 242(1)(b) a person must not send a book, document, record or property of a declared company out of Singapore with intent to defeat the purposes of Part 9` | the offence of s 242(1) |
| s 244(3) | `s 244(3) a person must give the information required of the person under section 244` | the offence of failing to give it |
| s 244(3) | `s 244(3) a person must not make a statement to the Minister that the person knows to be false in a material particular, or recklessly make one` | the offence of making such a statement |
| s 245(3)(a) | `s 245(3)(a) a person must not exercise a right to dispose of shares subject to the restrictions, or a right to be issued with them, knowing of the restrictions` | the offence of s 245(3) |
| s 245(3)(b) | `s 245(3)(b) a person must not vote in respect of shares subject to the restrictions or appoint a proxy to vote` | the offence of s 245(3) |
| s 245(3)(c) | `s 245(3)(c) the holder must notify the persons entitled to vote of the restrictions` | the offence of failing to notify |
| s 245(4) | `s 245(4) the company must not issue shares in contravention of the restrictions` | the offence of s 245(4) |

Guide: line 92 (N2): "where the text names the bearer the prohibition (`SHANT`) is derived from that answer" covers the prohibitions.
It does not say that a duty may be derived from the omission an offence names, nor from an entitlement; those three rules (s 244(3) give, s 245(3)(c), s 138(3A)) fit none of the Guide's lines and are listed under Marginal readings.
Other reading: no regulative rule for the provision; the function over the facts alone (the offence function for the nine rules derived from an offence, `s 138(3A) the person may be furnished with a copy of the instrument or debenture` and `s 138(3A) the last day for furnishing the copy` for the tenth), all tested.
The rules without a time limit are in "Rules with no breach path (sgk)"; the prohibitions reach BREACH when the act occurs.

## Jural relations (sgk)

One row per provision of my ranges that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it.
A provision that creates no such relation (a definition, a counting rule, a funding rule, a scope rule) is listed once as `none`.
Each relation is stated once, as a relation between two parties, and named neutrally; no rule is written twice, once from each side.
Hohfeld's pairs are used as the brief states them: a claim has a duty as its correlative, a privilege a no-right, a power a liability (being subject to the power, not an obligation), an immunity a disability.
Where the text names no claimant of an official's duty, the holder cell says that the text names none and does not guess one.
Two bearers are taken and not found in the text: the company at s 131(1) and (6) (F-K6) and the company at s 138(3A) (F-K34).
Parts 8 and 8A (ss 217 to 227X) and s 234 are shown repealed and create no relation.
Every layer-1 function of the seven modules (199 in all, counting the regulative rules and constants) is named in the last column of at least one row; the table was checked against the modules by script.


| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 131(1) the lodging | the Registrar (a claim that a statement of the charge be lodged; the text names no claimant) | the company (a duty to lodge it within 30 days; the bearer is taken, F-K6) | claim / duty | `s 131(1) a statement of the charge must be lodged with the Registrar`; `s 131(1) the company must lodge the statement of the charge within 30 days after the creation of the charge`; `s 131(1) the statement is lodged within 30 days after the creation of the charge` |
| s 131(1) the voidness | the liquidator and any creditor of the company (the security is void against them) | the chargee (cannot enforce the security against them) | immunity / disability | `s 131(1) the security the charge confers is void against the liquidator and any creditor of the company` |
| s 131(1A) | the Registrar (a claim to inspect the instrument or a certified true copy, at no cost to the Registrar) | the person registering the charge (the text names none) | claim / duty | `s 131(1A) the instrument or a certified true copy must be produced to the Registrar`; `s 131(1A) the production is at no cost to the Registrar` |
| s 131(2) first limb | the chargee (the contract or obligation for repayment is not affected by the voidness) | the company (cannot rely on the voidness to avoid repayment) | immunity / disability | `s 131(2) subsection (1) affects the contract or obligation` |
| s 131(2) second limb | the chargee (the money becomes immediately payable when the charge becomes void) | the company (must pay at once) | claim / duty | `s 131(2) the money secured by the charge becomes immediately payable by force of this subsection` |
| s 131(3), (3AA) to (3C) | none (a scope rule: which charges section 131 reaches) | none | none | `s 131(3) the charge is one to which section 131 applies`; `s 131(3) the charge falls within one of paragraphs (a) to (j)` |
| s 131(4) | the company (or the person lodging: may lodge although further proceedings are needed under foreign law) | the Registrar (cannot refuse the statement on that ground) | privilege / no-right | `s 131(4) the statement may be lodged even though further proceedings are necessary under the law of the place where the property is` |
| s 131(5) | the company that issues a series of debentures (one statement of the particulars within 30 days of the execution of the instrument is sufficient) | the Registrar (cannot require more) | immunity / disability | `s 131(5) the lodging of the statement is sufficient` |
| s 131(6) | the Registrar (a claim to particulars of each issue within 30 days) | the company (a duty to lodge them; the bearer is taken, F-K6) | claim / duty | `s 131(6) the company must lodge the particulars of each issue within 30 days after it`; `s 131(6) the particulars of the issue are lodged within 30 days after the issue` |
| s 131(6) validity | the debenture holders (an omission does not affect the validity of the debentures) | the company (cannot rely on the omission) | immunity / disability | `s 131(6) the omission affects the validity of the debentures issued` |
| s 131(7) | the Registrar (a claim that the particulars include the amount or rate of the commission, allowance or discount) | the company (a duty so to include it) | claim / duty | `s 131(7) the particulars required to be lodged must include the amount or rate per cent of the commission, allowance or discount` |
| s 131(7) validity | the debenture holders (omission does not affect validity) | the company (cannot rely on the omission) | immunity / disability | `s 131(7) the omission affects the validity of the debentures issued` |
| s 131(8) | none (a counting rule: a deposit as security is not an issue at a discount for subsection (7)) | none | none | `s 131(8) the deposit is treated as the issue of the debentures at a discount for the purposes of subsection (7)` |
| s 131(9) | the company or the chargee (a charge or assignment other than one relating to land need not be filed or registered under another written law) | the authority that administers that other law (cannot require it) | immunity / disability | `s 131(9) the charge or assignment needs to be filed or registered under another written law` |
| s 131(10) | the holder of the prior charge (the subsequent charge is not operative against the prior security) | the holder of the subsequent charge (cannot enforce it, unless the Court is satisfied it was given in good faith) | immunity / disability | `s 131(10) the subsequent charge is not operative and has no validity as respects the property comprised in the prior charge` |
| s 131(11) | none (a definition: shipowner's lien) | none | none | `s 131(11) the lien is a shipowner's lien` |
| s 132(1) lodging | the company and any person interested in the documents (may lodge them) | the Registrar (cannot refuse another lodger) | privilege / no-right | `s 132(1) the person may lodge the documents and particulars for registration` |
| s 132(1) offence | the State (the power to prosecute and to have the fine imposed) | the company and every officer in default (liable to a fine of up to $1,000 and a default penalty) | power / liability | `s 132(1) the person is guilty of the offence of default in complying with section 131`; `s 132(1) the most the person may be sentenced to on conviction` |
| s 132(2) | the person who effects registration other than the company (recovers the fees properly paid) | the company (must repay them) | claim / duty | `s 132(2) the person is entitled to recover the fees from the company`; `s 132(2) the amount the person may recover from the company` |
| s 133(1) | the Registrar (a claim to a statement of the particulars of a charge on property acquired, or of a foreign company on registration, within 30 days) | the company (a duty to cause it to be lodged) | claim / duty | `s 133(1) the company must cause a statement of the prescribed particulars of the charge to be lodged with the Registrar`; `s 133(1) the last day for lodging the statement`; `s 133(1) the statement is lodged within 30 days after the date`; `s 133(1) the company must cause the statement to be lodged within 30 days` |
| s 133(2) | the State | the company or the foreign company and every officer in default (liable to a fine of up to $1,000 and a default penalty) | power / liability | `s 133(2) the person is guilty of the offence of default in complying with section 133`; `s 133(2) the most the person may be sentenced to on conviction` |
| s 134(1) | the person who lodged the charge for registration (a claim that the Registrar enter the particulars in the register; the text names no claimant) | the Registrar (a duty to keep the register and enter the particulars) | claim / duty | `s 134(1) the particulars the Registrar must enter in the register`; `s 134(1) the Registrar must enter the particulars of the charge in the register` |
| s 134(2) | the company (a claim to a notice of the registration of the charge) | the Registrar (a duty to issue it) | claim / duty | `s 134(2) the notice is conclusive evidence that the requirements as to registration have been complied with`; `s 134(2) the Registrar must issue to the company a notice of the registration of a charge` |
| s 134(2) and (3) conclusive evidence | the company and the chargee (the notice or certificate is conclusive evidence that the requirements as to registration have been complied with) | a person who would dispute the registration (cannot) | immunity / disability | `s 134(2) the notice is conclusive evidence that the requirements as to registration have been complied with`; `s 134(3) the certificate is conclusive evidence that the requirements as to registration have been complied with` |
| s 134(3) | the company (on application and payment of the prescribed fee, a claim to a certificate confirming the registration) | the Registrar (a duty to issue it) | claim / duty | `s 134(3) the Registrar must issue to the company a certificate confirming the registration of the charge` |
| s 135(1) | the holder of a debenture or of a certificate of debenture stock secured by the registered charge (a claim to the endorsement; the text names none) | the company (a duty to cause the copy of the notice, or the statement of registration, to be endorsed) | claim / duty | `s 135(1) the company must cause a copy of the notice of registration, or a statement of the registration and its date, to be endorsed on the debenture or certificate`; `s 135(1) the company must cause the endorsement to be made` |
| s 135(2) | none (a scope rule: subsection (1) does not apply to debentures issued before the charge was registered) | none | none | `s 135(1) the company must cause a copy of the notice of registration, or a statement of the registration and its date, to be endorsed on the debenture or certificate` |
| s 135(3) | the State | any person who knowingly and wilfully authorises or permits the delivery of an unendorsed debenture or certificate (liable to a fine of up to $2,000) | claim / duty and power / liability | `s 135(3) the person is guilty of the offence of authorising or permitting the delivery of an unendorsed debenture or certificate`; `s 135(3) the most the person may be sentenced to on conviction`; `s 135(3) a person must not knowingly and wilfully authorise or permit the delivery of an unendorsed debenture or certificate` |
| s 136(1) lodging | the company (may lodge a statement of satisfaction or release) | the Registrar (cannot refuse it) | privilege / no-right | `s 136(1) the company may lodge with the Registrar a statement of satisfaction or release` |
| s 136(1) entry | the company (a claim that the Registrar enter the particulars of the statement) | the Registrar (a duty to enter them) | claim / duty | `s 136(1) the Registrar must enter the particulars of the statement in the register` |
| s 136(2) | the company (a statement endorsed with the chargee's statement is sufficient evidence of the payment, satisfaction, release or ceasing) | the Registrar (cannot demand other proof) | immunity / disability | `s 136(2) the statement of satisfaction or release is endorsed as the subsection requires`; `s 136(2) the chargee's statement constitutes sufficient evidence of the payment, satisfaction, release or ceasing` |
| s 137 application | the company or any person interested (may apply to the Court) | the Court (hears it; the text creates no duty to grant it) | privilege / no-right | `s 137 the person may apply to the Court for the extension of time or the rectification` |
| s 137 order | the Court (the power to extend the time or rectify the register, on such terms as seem just) | the company and the persons whose position the order affects | power / liability | `s 137 the Court may order that the time for registration be extended or that the omission or mis-statement be rectified`; `s 137 the Court may make the relief subject to a term that it is without prejudice to liability already incurred in respect of the default` |
| s 138(1), (1A) | the persons given inspection or copies by subsection (3) and (3A) (the text names no claimant of the keeping) | the company (a duty to keep the instrument or a copy at the registered office for as long as the charge is in force, and to retain it for 5 years after) | claim / duty | `s 138(1) the company must keep the instrument creating the charge, or a copy, at its registered office`; `s 138(1) the company's keeping satisfies the subsection`; `s 138(1) the company must keep the instrument or a copy at its registered office`; `s 138(1) the company must not cease to keep the instrument or a copy at its registered office while the charge remains in force`; `s 138(1A)(a) the instrument or copy is deemed to form part of the records required to be kept under section 199(1)`; `s 138(1A)(b) the last day of the period of 5 years for which the instrument must be retained`; `s 138(1A)(b) the instrument must still be retained on the day` |
| s 138(2) | the persons given inspection by subsection (3) (the text names no claimant of the register) | the company (a duty to keep a register of charges and enter the particulars) | claim / duty | `s 138(2) the particulars the company must give of each charge in its register of charges`; `s 138(2) the company must keep a register of charges at its registered office` |
| s 138(3) | a creditor or member (free inspection of the instruments and the register); any other person (inspection of the register on a fee of up to $2) | the company (a duty to open them; and a power to fix the fee) | claim / duty and power / liability | `s 138(3) the item must be open to the person's inspection`; `s 138(3) the most the company may charge for one inspection`; `s 138(3) the fee the company has fixed is within the limit` |
| s 138(3A) | any person (on application and payment of up to $1 a page, a copy within 3 days) | the company (a duty to furnish it; and a claim to the fee) | claim / duty | `s 138(3A) the person may be furnished with a copy of the instrument or debenture`; `s 138(3A) the last day for furnishing the copy`; `s 138(3A) the most the company may charge for the copy, in Singapore dollars`; `s 138(3A) the company must furnish the copy within 3 days of the application` |
| s 138(4) | the State | the company and every officer in default (liable to a fine of up to $2,000 and a default penalty) | power / liability | `s 138(4) the person is guilty of the offence of default in complying with section 138`; `s 138(4) the most the person may be sentenced to on conviction` |
| s 139 | the company (7 days more for a document executed or made out of Singapore; a privilege) and the Registrar (the power to allow further periods) | the Registrar (cannot treat the document as late within the extension) and the company concerned (subject to the Registrar's allowance) | privilege / no-right and power / liability | `s 139 the number of days added to the time specified`; `s 139 the time specified is extended by`; `s 139 the last day for lodging the document` |
| s 140 | none (a scope rule: earlier charges) | none | none | `s 140 this Division applies to the charge` |
| s 141 first limb | none (a scope rule: a reference to a company includes a foreign company registered under Division 2 of Part 11) | none | none | `s 141 a reference in Division 8 to a company includes the foreign company` |
| s 141 proviso | a registered foreign company (nothing in the Division applies to a charge on property outside Singapore) | the Registrar and the Division (no duty to register such a charge) | immunity / disability | `s 141 this Division applies to the charge of the foreign company` |
| Parts 8 and 8A (ss 217 to 227X) | none (shown repealed) | none | none | none (no rule: the text shows the provision repealed) |
| s 228 | an insurance company, and a banking corporation (no investigation of their business under this Part unless the Part specifically provides) | the Minister (no power to investigate under this Part) | immunity / disability | `s 228 Part 9 is barred from authorising the investigation` |
| s 229 | none (definitions: company, declared company, officer or agent; and the keel's s 4(8) seam) | none | none | `s 229 the definition governs the word where it is used in Part 9`; `s 229 "company" the body is within the word company`; `s 229 "declared company" the body is a declared company`; `s 229 "officer or agent" the person is an officer or agent of the corporation`; `s 228 the provision is in Part 9` |
| s 230 | the Minister (the power to declare by order that a company or foreign company is one to which Part 9 applies) | the company or foreign company (becomes a declared company) | power / liability | `s 230 the Minister may by order declare the body to be a company to which Part 9 applies` |
| s 231(1) | the company or foreign company declared, its members and creditors (the text names no claimant) | the Minister (a duty to appoint inspectors to investigate and report) | claim / duty | `s 231(1) the Minister must appoint one or more inspectors to investigate the affairs of the company`; `s 231(1) the Minister must appoint inspectors for a declared company` |
| s 231(2) | the inspector (may inform the Minister without an interim report) and the Minister (may thereafter take such steps as fit) | any person the matters tend to show to have committed an offence | privilege / no-right and power / liability | `s 231(2) the inspector may inform the Minister of the matters without making an interim report`; `s 231(2) the Minister may take such steps as the Minister considers fit` |
| s 231(3) | none (a funding rule: the expenses are met in the first instance out of moneys provided by Parliament) | none | none | `s 231(3) the expenses are defrayed in the first instance out of moneys provided by Parliament` |
| s 231(4) | the Minister (the power to direct by notification in the Gazette that the expenses be paid) | the company, or a person convicted on a prosecution under s 233(3) or ordered under s 233(4) | power / liability | `s 231(4) the Minister may by notification in the Gazette direct that the expenses be paid by the payer` |
| s 231(5) | the Minister (the power to specify time and manner of payment) | the payer named | power / liability | `s 231(5) the notification may specify the time or times and the manner in which the payment of the expenses must be made` |
| s 231(6) | the Minister (a claim to reimbursement of the expenses) | the persons named in the notification, to the extent specified | claim / duty | `s 231(6) the person named in the notification is liable to reimburse the Minister in respect of the expenses to the extent specified` |
| s 231(7) | the Government (may sue in any court of competent jurisdiction to recover the expenses) | the persons named in the notification | power / liability | `s 231(7) action to recover the expenses may be taken in the name of the Government in any court of competent jurisdiction` |
| s 231(8) | the Minister (the expenses ordered to be paid by a company in liquidation rank as costs and expenses of the winding up under the IRDA 2018, an input) | the liquidator, and the company in liquidation (the expenses are paid as costs of the winding up) | claim / duty | `s 231(8) the expenses ordered to be paid by the company are part of the costs and expenses of the winding up for the purposes of section 203(1)(a) of the Insolvency, Restructuring and Dissolution Act 2018` |
| s 231(9) | the inspector (may include a recommendation as to the notification) and the Minister (may direct that the report must) | the inspector (a duty if the Minister so directs) | power / liability | `s 231(9) the report must include a recommendation as to the terms of the notification`; `s 231(9) the report may include a recommendation as to the terms of the notification` |
| s 232(1) | the applicants (members, debenture holders, or the company by special resolution: a power to apply) and the Minister (the power to appoint inspectors on the application) | the company (subject to the investigation) | power / liability | `s 232(1)(a)(i) the application is made by enough members`; `s 232(1)(a)(ii) the application is made by enough debenture holders`; `s 232(1)(b) the application is made by enough of the persons on the register of members`; `s 232(1) the Minister may appoint inspectors on the application` |
| s 232(2) | the Minister (a claim to supporting evidence and a power to require security for the cost) | the applicants (a duty to support the application; liable to give security) | claim / duty and power / liability | `s 232(2) the application must be supported by the evidence the Minister requires`; `s 232(2) the Minister may require the applicants to give security for the cost of the investigation` |
| s 233(1) reports | the Minister (a claim to interim reports when directed, and to the final report) | the inspector (a duty to report) | claim / duty | `s 233(1) the inspector may make interim reports to the Minister`; `s 233(1) the inspector must make an interim report to the Minister`; `s 233(1) the inspector must report to the Minister on the conclusion of the investigation` |
| s 233(1) copies | the company (a copy at its registered office) and the applicants (a further copy at their request) | the Minister (a duty to forward and deliver the copies, subject to (1B)) | claim / duty | `s 233(1) the Minister must forward a copy of the report to the registered office of the company`; `s 233(1) the Minister must deliver a further copy of the report to the applicants`; `s 233(1) the Minister must forward a copy of the report to the registered office` |
| s 233(1A) | each person to whom in the Minister's opinion the report ought to be given because it relates to that person's affairs to a material extent | the Minister (a duty to give the copy, subject to (1B) and (1C)) | claim / duty | `s 233(1A) the Minister must give the person a copy of the report`; `s 233(1A) the Minister must give a copy of the report to the person whose affairs it relates to` |
| s 233(1B) | the Minister (not bound to furnish a copy where there is good reason for not divulging) | a company, an applicant or any other person (no claim to the copy) | privilege / no-right | `s 233(1) the Minister must forward a copy of the report to the registered office of the company`; `s 233(1) the Minister must forward a copy of the report to the registered office`; `s 233(1A) the Minister must give the person a copy of the report`; `s 233(1A) the Minister must give a copy of the report to the person whose affairs it relates to` |
| s 233(1C) | a person whose legal proceedings might be unduly prejudiced (the text names none) | the Minister (a duty not to give the copy) | claim / duty | `s 233(1C) the Minister must not give the person a copy of the report under subsection (1A)`; `s 233(1C) the Minister must not give a copy of the report where legal proceedings might be unduly prejudiced` |
| s 233(1D) | a person against whom legal proceedings are brought (may obtain an order that a copy be given) and the court (the power to order it) | the Minister (liable to be ordered) | power / liability | `s 233(1D) the court may order that a copy of the report or part of it be given to the person` |
| s 233(2) | the Minister (the privilege to publish the report if of the opinion that it is necessary in the public interest) | the company and the persons the report concerns (no right to stop publication, unless the Attorney-General has certified) | privilege / no-right | `s 233(2) the Minister may cause the report to be printed and published`; `s 233(2) the Minister must refrain from publishing the report when the Attorney-General has certified that publication would be prejudicial` |
| s 233(3) prosecution | the public (the text names no claimant) | the Minister (a duty to cause a prosecution to be instituted) | claim / duty | `s 233(3) the Minister must cause a prosecution to be instituted` |
| s 233(3) assistance | the Minister (a claim to assistance, on being required) | all officers and agents of the company other than the defendant (a duty to give all assistance reasonably able to give) | claim / duty | `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution`; `s 233(3) the officer or agent must give the assistance on being required by the Minister` |
| s 233(4) | the Minister (the power to bring proceedings in the name of the company) | the persons against whom the proceedings are brought | power / liability | `s 233(4) the Minister may bring proceedings in the name of the company` |
| s 234 | none (repealed) | none | none | none (no rule: the text shows the provision repealed) |
| s 235 | the inspector (the power, with the Minister's written consent, to investigate a related corporation) | the related corporation | power / liability | `s 235 the inspector may investigate the affairs of the other corporation` |
| s 236(1) | the inspector (the power to investigate also the other corporation) | the other corporation | power / liability | `s 236(1) the inspector has power to investigate also the affairs of the other corporation` |
| s 236(1) report | the text names no claimant | the inspector (a duty to report on the other corporation's affairs so far as relevant) | claim / duty | `s 236(1) the inspector must report on the affairs of the other corporation so far as the inspector thinks the results of the investigation relevant`; `s 236(1) the inspector must report on the affairs of the related corporation` |
| s 236(2) | the inspector (a claim to the books and documents and to all assistance) | every officer and agent of the corporation (a duty, if required, to produce; and to assist, so far as reasonably able) | claim / duty | `s 236(2) the officer or agent must produce to the inspector all books and documents in the officer's or agent's custody or power`; `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation`; `s 236(2) the officer or agent must produce the books and documents and give the assistance` |
| s 236(3) | the inspector (the power to require appearance for examination on oath or affirmation) | any officer or agent of the corporation | power / liability | `s 236(3) the inspector may require the person to appear for examination on oath or affirmation` |
| s 236(4)(a), (b) | the inspector (the power to take possession of, and retain, the books and documents) | the officer or agent who produced them | power / liability | `s 236(4)(a) the inspector may take possession of all the books and documents`; `s 236(4)(b) the inspector may retain the books and documents for the time` |
| s 236(4)(c) | the corporation (a claim to access at all reasonable times) | the inspector (a duty to permit it) | claim / duty | `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents` |
| s 236(4A) | the inspector (the power to require a director or past director to produce documents about a bank account) | the director or past director | power / liability | `s 236(4A) the inspector may require the person to produce all documents in the person's possession or under the person's control relating to the bank account` |
| s 236(5) | the inspector (the power to certify the failure to the Court) and the Court (the power to punish as for contempt) | the officer or agent who failed or refused | power / liability | `s 236(5) the inspector may certify the failure or refusal to the Court`; `s 236(5) the Court may punish the offender in like manner as if the offender had been guilty of contempt of the Court` |
| s 236(6) the bar | the inspector (a claim to an answer from a person who is or was an officer or agent) | that person (no entitlement to refuse on the ground of self-incrimination) | claim / duty (disability) | `s 236(6) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` |
| s 236(6) the answer | that person (the answer given under the compulsion may not be used in a later criminal proceeding, except for a false statement) | the prosecution (cannot use it) | immunity / disability | `s 236(6) the answer is barred from use in a subsequent criminal proceeding` |
| s 236(7) | any person (may refuse to answer on the ground of self-incrimination, subject to (6)) | the inspector (no right to the answer) | privilege / no-right | `s 236(7) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` |
| s 236(8) | the inspector (the power to have notes recorded and signed) and a party in a legal proceeding (may use the signed notes in evidence against the person examined) | the person examined | power / liability | `s 236(8) the inspector may cause notes of the examination to be recorded, reduced to writing and read to or by and signed by the person examined`; `s 236(8) the signed notes may be used in evidence in legal proceedings against the person` |
| s 237(1) | the Government (a claim to the expenses of the investigation) and the Minister (the power to direct that the applicants pay, in whole or in part) | the company investigated; or the applicants, if the Minister so directs | claim / duty and power / liability | `s 237(1) who must pay the expenses of and incidental to the investigation`; `s 237(1) the company investigated must pay the expenses of the investigation` |
| s 237(2)(a) | the Government (a claim to the deficiency, up to the security) | the applicants (a duty to make it good) | claim / duty | `s 237(2)(a) the amount the applicants must make good`; `s 237(2)(a) the applicants must make good the deficiency` |
| s 237(2)(b) | none (a funding rule: the balance is paid out of moneys provided by Parliament) | none | none | `s 237(2)(b) the balance paid out of moneys provided by Parliament` |
| s 238 | a party tendering the Minister's certified copy of the report (the power to have it admitted as evidence of the inspector's opinion and the facts) | the other party (cannot object to its admissibility) | power / liability | `s 238 the copy is admissible in any legal proceedings as evidence of the inspector's opinion and of the facts upon which the opinion is based` |
| s 239(1) | the inspector of a declared company (the power to employ persons and authorise them in writing, except to examine on oath) | the officers and agents of the corporation | power / liability | `s 239(1) the inspector may employ the persons the inspector considers necessary`; `s 239(1) the inspector may in writing authorise the employed person to do the thing` |
| s 239(2) | the inspector or the authorised person (a claim to the book, document or answer) | the officer or agent (liable to be dealt with as in s 236(5)) | claim / duty | `s 239(2) the officer or agent is liable to be dealt with in the manner provided in section 236(5)` |
| s 240(1) | the declared company (no action or proceeding against it, or by it on a contract or bill, without the Minister's consent, from appointment until 3 months after the final report) and the Minister (the power to consent, with conditions) | the person who would sue (disability); and anyone seeking consent (liable to its conditions) | immunity / disability and power / liability | `s 240(1) the day falls within the suspension`; `s 240(1) the number of days from the appointment to the end of 3 months after the final report`; `s 240(1) the action or proceeding is barred without the consent of the Minister`; `s 240(1) a person must not commence or proceed with an action or proceeding in a Court without the consent of the Minister during the suspension` |
| s 240(2) | the declared company (an action or proceeding commenced in contravention is void and of no effect) | the person who commenced or proceeded with it | immunity / disability | `s 240(2) the action or proceeding is void and of no effect` |
| s 241(1) | the Minister (the power to apply to the Court for the winding up after an inspector's report on a declared company) | the declared company (the IRDA 2018 then applies as if the company, or a creditor or contributory, had applied) | power / liability | `s 241(1) the Minister may apply to the Court for the winding up`; `s 241(1) the application is treated as having been made by` |
| s 241(2) | the State (the text names no claimant) | the foreign company (a duty not to carry on business or keep a place of business in Singapore once the winding-up order is made) | claim / duty | `s 241(2) the foreign company must not carry on business or establish or keep a place of business in Singapore`; `s 241(2) the foreign company must not carry on business or establish or keep a place of business in Singapore once the order is made` |
| s 242(1) | the State | any person who, with the intent, destroys, conceals or alters a book, document or record, or sends it or property out of Singapore (a duty not to; liable to a fine of up to $10,000 or imprisonment of up to 2 years) | claim / duty and power / liability | `s 242(1) the person is guilty of the offence of defeating the purposes of Part 9 or obstructing an investigation`; `s 242(1) the most the person may be sentenced to on conviction`; `s 242(1)(a) a person must not destroy, conceal or alter a book, document or record of a declared company with intent to defeat the purposes of Part 9`; `s 242(1)(b) a person must not send a book, document, record or property of a declared company out of Singapore with intent to defeat the purposes of Part 9` |
| s 242(2) | the prosecution (the proved act is enough, the onus of the absence of intent lies on the person) | the person charged (a burden of proof) | power / liability | `s 242(2) the person bears the onus of proving that the person did not act with the intent` |
| s 243(1) | the Minister (the power to appoint inspectors to investigate the ownership of a corporation) | the corporation, its members and those financially interested | power / liability | `s 243(1) the Minister may appoint inspectors to investigate the ownership of the corporation` |
| s 243(2) | the Minister (the power to define the scope of the appointment) | the corporation | power / liability | `s 243(2) the appointment may define the scope of the inspector's investigation` |
| s 243(3) | the applicant members (a claim to an appointment, unless the Minister is satisfied the application is vexatious, and to a scope that includes what the application seeks) | the Minister (a duty to appoint, and not to exclude a matter except as unreasonable) | claim / duty | `s 243(3) the Minister must appoint an inspector to conduct the investigation`; `s 243(3) the appointment must not exclude the matter from the scope of the investigation` |
| s 243(4) | the inspector (the power to investigate arrangements and understandings that are not legally binding) | the persons concerned | power / liability | `s 243(4) the inspector's powers extend to the investigation of the circumstances` |
| s 243(5) | the inspector (the powers of Part 9 over persons financially interested, as over officers and agents) | those persons (liable as officers and agents would be) | power / liability | `s 243(5)(a) Part 9 applies in relation to the person as it applies in relation to officers and agents of the corporation`; `s 243(5) the provisions of Part 9 on the investigation of declared companies apply to the investigation with the necessary modifications` |
| s 243(5)(b) | the Minister (not bound to furnish a copy of the report in whole where there is good reason for not divulging it; may have a copy kept by the Registrar) | the corporation and any other person (no claim to a complete copy) | privilege / no-right | `s 243(5)(b) the Minister is not bound to furnish the person with a copy of the report or with a complete copy of it`; `s 243(5)(b) the Minister may cause a copy of the report or of the parts of it to be kept by the Registrar` |
| s 244(1) | the Minister (the power to require information about interests in shares or debentures) | any person the Minister has reasonable cause to believe to have or be able to obtain it | power / liability | `s 244(1) the Minister may require the person to give the information to the Minister` |
| s 244(2) | none (a definition by deeming: who is treated as interested in a share or debenture) | none | none | `s 244(2) the person is deemed to have an interest in the share or debenture for the purposes of section 244` |
| s 244(3) | the State | any person who fails to give the information, or gives a false or reckless statement (a duty; liable to a fine of up to $5,000 or imprisonment of up to 12 months or both) | claim / duty and power / liability | `s 244(3) the person is guilty of the offence of failing to give information or giving false information`; `s 244(3) the most the person may be sentenced to on conviction`; `s 244(3) a person must give the information required of the person under section 244`; `s 244(3) a person must not make a statement to the Minister that the person knows to be false in a material particular, or recklessly make one` |
| s 244(4) | a banking corporation (need not disclose information about its customers other than the corporation of which it is the banker, subject to the Banking Act 1970) | the Minister (no right to that information) | immunity / disability | `s 244(4) section 244 applies to the banking corporation`; `s 244(4) section 244 requires the banking corporation to disclose the information to the Minister` |
| s 244(5), (7) | the Minister (the power to delegate the section 244 powers, and to exercise them despite a delegation) | the committee of an approved exchange or the body, panel or committee (the delegate) | power / liability | `s 244(5) the Minister may delegate the powers under section 244 to the delegate`; `s 244(7) the Minister may exercise the power despite a delegation of it` |
| s 244(6) | the Minister (a claim to be kept informed of information obtained) | the committee or body (a duty to keep the Minister informed) | claim / duty | `s 244(6) the committee or body must keep the Minister informed of any information obtained under section 244` |
| s 245(1) | the Minister (the power to restrict shares or debentures by order: transfers void, no voting, no further issue, no payment except in a liquidation) | the holders of the shares, and the company | power / liability | `s 245(1) the Minister may by order in the Gazette direct that the shares are until further order subject to the restrictions`; `s 245(1) the act is void or barred by the restrictions` |
| s 245(2) | the Minister (the power to continue the restrictions (c) and (d) when lifting the others to permit a transfer) | the holders of the shares | power / liability | `s 245(2) the order may continue the application of subsection (1)(c) and (d) to the shares` |
| s 245(3) | the State | any person who, knowing of the restrictions, exercises a right to dispose of or be issued shares, or votes or appoints a proxy, or a holder who fails to notify (a duty; liable to a fine of up to $5,000 or imprisonment of up to 12 months or both) | claim / duty and power / liability | `s 245(3) the person is guilty of the offence of dealing in shares subject to the restrictions`; `s 245(3) the most the person may be sentenced to on conviction`; `s 245(3)(a) a person must not exercise a right to dispose of shares subject to the restrictions, or a right to be issued with them, knowing of the restrictions`; `s 245(3)(b) a person must not vote in respect of shares subject to the restrictions or appoint a proxy to vote`; `s 245(3)(c) the holder must notify the persons entitled to vote of the restrictions` |
| s 245(4) | the State | the company and every officer in default who issues shares in contravention of the restrictions (a duty; liable to a fine of up to $5,000 or imprisonment of up to 12 months) | claim / duty and power / liability | `s 245(4) the officer is guilty of the offence of issuing shares in contravention of the restrictions`; `s 245(4) the company is guilty of the offence of issuing shares in contravention of the restrictions`; `s 245(4) the most the person may be sentenced to on conviction`; `s 245(4) the company must not issue shares in contravention of the restrictions` |
| s 245(5) | the Public Prosecutor (the power to consent to a prosecution) | any prosecutor (disability: cannot institute a prosecution without the consent) | power / liability (disability) | `s 245(5) the prosecution is barred for want of the consent of the Public Prosecutor` |
| s 245(6) | none (an extension rule: section 245 applies to debentures as it applies to shares) | none | none | `s 245(6) section 245 applies to the debentures as it applies to shares` |
| s 246 | the Minister (the power to declare by notice that an inspector appointed under a corresponding law of another country has the powers and duties of an inspector under section 231) and that inspector (thereupon has them) | the corporation investigated | power / liability | `s 246 the Minister may by notice declare that the inspector is to have the same powers and duties in Singapore as an inspector appointed under section 231`; `s 246 the inspector has the powers and duties of an inspector appointed under section 231` |

## Marginal readings for a lawyer (sgk)

The brief names two status-quo readings that it leaves to a lawyer and does not decide.
(a) A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no.
(b) A prohibition or grant limited by its own wording does not count as the text's no.
I took both as the status quo.
This section lists every branch that rests on one, with the other reading.

There are 198 branches that carry a `FALSE-kind` or a `NOTHING-kind` comment in the seven modules (102 "no" branches, 96 "not covered" branches).
Table 1 lists the 97 of the 102 "no" branches that rest on a reading; the other 5 are closed by the text's own "means", "if, and only if", "only if" or a stated amount ("not exceeding $2"), and are not marginal.
Of the 97, 4 rest on a period the text fixes (the periods ruling, line 93 item (a): settled, listed for completeness), and 29 of the failed gates on duties and "may" functions are "where", "upon" or "when" gates that the periods ruling settles (line 93 item (b), line 94 item (c)); the rest rest on reading (a) or on a decision case by case (line 95).
Table 2 lists the 83 "not covered" branches that rest on reading (b); the other 13 "not covered" branches rest on the text's silence or openness (a list not closed, "includes", an undefined term, a pointer outside the sources) and are not marginal.

**Sites that fit none of the Guide's lines exactly, or where two lines point apart** (each is also in Table 1 or Table 2 and has a fork entry):

- the four split-site (ii) sites that answer NOTHING (F-K13, F-K15, F-K21, F-K24): the gates are "on being satisfied" and "on the application of" (s 137), "on application to a company and on payment of a fee" (s 138(3A)), "with the consent in writing of the Minister" (s 235) and "on the application of" (s 232(1)); none is an "if" (limit 1 of the grant ruling) or a "where", "when" or "upon" (limit 3);
- the three time gates of F-K7 that I took by analogy with "when" (s 231(2) "thereafter", s 232(2) "before appointing", s 241(1) "at any time after");
- the nine unmet offence elements of F-K10, where line 98 (the provision's own question) and line 87 (a prohibition limited in its own wording) point different ways;
- the two lists of F-K30 (s 240(1), s 245(1)), closed by their structure and not by "only";
- the derived duties of F-K34 (s 244(3) give, s 245(3)(c) notify, s 138(3A) furnish), which the Guide's N2 ruling does not cover;
- the answer of F-K29 (NOTHING, "points outside the text") and the two sites of F-K22.

### Table 1. "No" branches that rest on a reading

Each row is a function with a `FALSE-kind` branch.
"Other reading" is what the branch would answer on the other reading.


| n | function | the reading the branch rests on | the words at the branch | other reading |
| --- | --- | --- | --- | --- |
| 1 | `s 140 this Division applies to the charge` | an "except" once it is met; line 95 (site by site) [F-K2] | 'Except as is otherwise expressly provided, this Division applies to any charge ...' (an 'except' met: fork F-K2) | NOTHING |
| 2 | `s 141 this Division applies to the charge of the foreign company` | a flat negative; reading (a), second half; line 92 (N2) | 'nothing in this Division applies to a charge on property outside Singapore of such foreign company' | NOTHING: a flat negative says no of what it names only |
| 3 | `s 134(3) the Registrar must issue to the company a certificate confirming the registration of the charge` | a failed "upon" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty arises 'Upon the application of the company and payment of the prescribed fee'; an 'upon' unmet on a duty (periods ruling of 2026-11-05, items (b) and (c); fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 4 | `s 135(1) the company must cause a copy of the notice of registration, or a statement of the registration and its date, to be endorsed on the debenture or certificate` | a flat negative; reading (a), second half; line 92 (N2) | 'Subsection (1) does not apply to any debenture or certificate of debenture stock which has been issued by the company before the charge was registered' (s 135(2)) | NOTHING: a flat negative says no of what it names only |
| 5 | `s 135(3) the person is guilty of the offence of authorising or permitting the delivery of an unendorsed debenture or certificate` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('Every person who knowingly and wilfully authorises or permits the delivery of any debenture or certificate of debenture stock which is ... | NOTHING |
| 6 | `s 136(1) the company may lodge with the Registrar a statement of satisfaction or release` | a failed "where" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the subsection begins 'Where, with respect to any registered charge — (a) the debt ... has been paid or satisfied ...; or (b) the property ... has been released'; a 'may' ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 7 | `s 136(1) the Registrar must enter the particulars of the statement in the register` | a failed "gate" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | the duty follows the lodging of the statement ('the company may lodge ... a statement ... and the Registrar must enter particulars of that statement'); with no statement ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 8 | `s 136(2) the statement of satisfaction or release is endorsed as the subsection requires` | the provision's own question, or a bar's own question; line 98 (limit 2) | 'The statement must be endorsed with a statement by the chargee'; a duty not met, the provision's own question | NOTHING (line 87) |
| 9 | `s 138(1) the company must keep the instrument creating the charge, or a copy, at its registered office` | a period or duration the text fixes has ended; line 93 item (a) (ruled) | the instrument is to be kept 'for as long as the charge to which the instrument relates remains in force'; the period has ended (periods ruling of 2026-11-05, item (a)) | none: settled by the ruling, listed for completeness |
| 10 | `s 138(1) the company's keeping satisfies the subsection` | the provision's own question, or a bar's own question; line 98 (limit 2) | 'Every company must cause the instrument ... or a copy thereof to be kept at the registered office ... but in the case of a series of debentures the keeping of a copy of one ... | NOTHING (line 87) |
| 11 | `s 138(1A)(b) the instrument must still be retained on the day` | a period or duration the text fixes has ended; line 93 item (a) (ruled) | a period of 5 years 'after' the date; past its last day the paragraph requires no more retention (periods ruling of 2026-11-05, item (a)) | none: settled by the ruling, listed for completeness |
| 12 | `s 138(4) the person is guilty of the offence of default in complying with section 138` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('If default is made in complying with this section, the company and every officer of the company who is in default shall be guilty of an ... | NOTHING |
| 13 | `s 131(3) the charge is one to which section 131 applies` | a flat negative; reading (a), second half; line 92 (N2) | 'a shipowner’s lien created by a company on or after 1 October 2018 ... is not a charge to which this section applies' (s 131(3AB)) | NOTHING: a flat negative says no of what it names only |
| 14 | `s 131(3) the charge is one to which section 131 applies` | a flat negative; reading (a), second half; line 92 (N2) [F-K3] | 'A charge mentioned in subsection (3) does not include a charge created at any time on or after 1 May 2009 to the extent that it is capable of being registered under the ... | NOTHING: a flat negative says no of what it names only |
| 15 | `s 131(1) the security the charge confers is void against the liquidator and any creditor of the company` | a failed "gate" gate on a duty or on the provision's own question; reading (a); no ruling | voidness is imposed 'if this section is not complied with in relation to the charge'; the section was complied with (an 'if' unmet: marginal reading (a)) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 16 | `s 131(1) the security the charge confers is void against the liquidator and any creditor of the company` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) | the provision applies 'where a charge to which this section applies is created by a company'; the charge is not one to which it applies (a 'where' unmet: periods ruling of ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 17 | `s 131(1A) the instrument or a certified true copy must be produced to the Registrar` | a failed "upon" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty arises 'upon the Registrar’s request' in connection with 'a charge to which this section applies'; without the request, or without such a charge, it does not arise ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 18 | `s 131(1A) the production is at no cost to the Registrar` | a flat negative; reading (a), second half; line 92 (N2) | the production must be 'at no cost to the Registrar' | NOTHING: a flat negative says no of what it names only |
| 19 | `s 131(2) subsection (1) affects the contract or obligation` | a flat negative; reading (a), second half; line 92 (N2) | 'Nothing in subsection (1) affects any contract or obligation for repayment of the money secured by a charge' | NOTHING: a flat negative says no of what it names only |
| 20 | `s 131(2) the money secured by the charge becomes immediately payable by force of this subsection` | a failed "when" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) | the money becomes immediately payable 'when a charge becomes void under this section'; a 'when' unmet (periods ruling of 2026-11-05, items (b) and (c); the name says 'by ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 21 | `s 131(4) the statement may be lodged even though further proceedings are necessary under the law of the place where the property is` | a failed "where" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the subsection begins 'Where a charge created in Singapore affects property outside Singapore'; a 'may' gated by 'where' (periods ruling of 2026-11-05, item (b); fork F-K7, ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 22 | `s 131(5) the lodging of the statement is sufficient` | a failed "if" gate on a duty or on the provision's own question; reading (a); no ruling [F-K8] | 'it is sufficient if there is lodged ... within 30 days ... a statement containing the following particulars' (an 'if' unmet: marginal reading (a); fork F-K8) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 23 | `s 131(6) the omission affects the validity of the debentures issued` | a flat negative; reading (a), second half; line 92 (N2) | 'an omission to do so does not affect the validity of the debentures issued' | NOTHING: a flat negative says no of what it names only |
| 24 | `s 131(7) the particulars required to be lodged must include the amount or rate per cent of the commission, allowance or discount` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the requirement arises 'where any commission, allowance or discount has been paid or made'; a 'where' unmet (periods ruling of 2026-11-05, item (b); fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 25 | `s 131(7) the omission affects the validity of the debentures issued` | a flat negative; reading (a), second half; line 92 (N2) | 'omission to do so does not affect the validity of the debentures issued' | NOTHING: a flat negative says no of what it names only |
| 26 | `s 131(8) the deposit is treated as the issue of the debentures at a discount for the purposes of subsection (7)` | a flat negative; reading (a), second half; line 92 (N2) | 'The deposit of any debentures as security for any debt of the company is not for the purposes of subsection (7) to be treated as the issue of the debentures at a discount' | NOTHING: a flat negative says no of what it names only |
| 27 | `s 131(9) the charge or assignment needs to be filed or registered under another written law` | a flat negative; reading (a), second half; line 92 (N2) | 'No charge or assignment to which this section applies (except a charge or assignment relating to land) need be filed or registered under any other written law' | NOTHING: a flat negative says no of what it names only |
| 28 | `s 131(10) the subsequent charge is not operative and has no validity as respects the property comprised in the prior charge` | an "unless" once it is met; line 95 (site by site) [F-K9] | the subsequent charge is not operative 'unless it is proved to the satisfaction of the Court' that it was given in good faith; an 'unless' met (fork F-K9) | NOTHING |
| 29 | `s 131(10) the subsequent charge is not operative and has no validity as respects the property comprised in the prior charge` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) | the subsection applies 'where a charge requiring registration ... is created before the lapse of 30 days after the creation of a prior unregistered charge' and the other ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 30 | `s 132(1) the person is guilty of the offence of default in complying with section 131` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('if default is made in complying with that section the company and every officer of the company who is in default shall be guilty of an ... | NOTHING |
| 31 | `s 132(2) the person is entitled to recover the fees from the company` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K11] | the entitlement arises 'where registration is effected by some person other than the company' and for 'fees properly paid'; a 'where' unmet (periods ruling of 2026-11-05, ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 32 | `s 133(1) the company must cause a statement of the prescribed particulars of the charge to be lodged with the Registrar` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty arises 'where' one of paragraphs (a) to (c) holds; a 'where' unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 33 | `s 133(2) the person is guilty of the offence of default in complying with section 133` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('If default is made in complying with this section, the company or the foreign company and every officer ... who is in default shall be ... | NOTHING |
| 34 | `s 237(2)(a) the amount the applicants must make good` | the provision's own question, or a bar's own question; line 98 (limit 2) | the security does not exceed the amount directed, so the ceiling is nothing ('up to the amount by which the security ... exceeds') | NOTHING (line 87) |
| 35 | `s 237(2)(a) the amount the applicants must make good` | a failed "gate" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | 'if the company fails to pay the whole or any part of the sum which it is so liable to pay'; the company has not failed (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 36 | `s 237(2)(b) the balance paid out of moneys provided by Parliament` | the provision's own question, or a bar's own question; line 98 (limit 2) | there is no balance, so nothing is paid out of moneys provided by Parliament | NOTHING (line 87) |
| 37 | `s 239(1) the inspector may in writing authorise the employed person to do the thing` | an "except" once it is met; line 95 (site by site) | 'to do anything the inspector could himself or herself do, except to examine on oath or affirmation' | NOTHING |
| 38 | `s 240(1) the action or proceeding is barred without the consent of the Minister` | a period or duration the text fixes has ended; line 93 item (a) (ruled) | the bar runs only 'On and after the appointment ... until the expiration of 3 months after the inspector has presented the inspector's final report' | none: settled by the ruling, listed for completeness |
| 39 | `s 240(1) the action or proceeding is barred without the consent of the Minister` | the provision's own question, or a bar's own question; line 98 (limit 2) | the bar is 'without the consent of the Minister (which may be given generally or in a particular case and which may be given subject to such conditions and limitations as the ... | NOTHING (line 87) |
| 40 | `s 240(1) the action or proceeding is barred without the consent of the Minister` | an "unless" once it is met; line 95 (site by site) | 'unless the holder or other person — (i) ... gave therefor adequate pecuniary consideration; and (ii) was not at the time ... or at any time within 3 years before that time a ... | NOTHING |
| 41 | `s 240(1) the action or proceeding is barred without the consent of the Minister` | a list the text does not close with "only" (F-K30); line 87 against the text's own structure | a closed list: the bar covers an action or proceeding '(a) by the company upon or in respect of any contract, bill of exchange or promissory note; or (b) by the holder or any ... | NOTHING |
| 42 | `s 241(1) the Minister may apply to the Court for the winding up` | a failed "after" gate on a "may" function (F-K7); by analogy with "when" (line 94 item (c)); listed, not decided: line 99 (limit 3) | the application 'may be made by the Minister at any time after a report has been made in respect of a declared company by an inspector'; a 'may' gated by 'at any time after' ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 43 | `s 241(2) the foreign company must not carry on business or establish or keep a place of business in Singapore` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty arises 'Where, in the case of a foreign company, on any application under subsection (1) an order is made'; a 'where' unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 44 | `s 242(1) the person is guilty of the offence of defeating the purposes of Part 9 or obstructing an investigation` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('Any person who, with intent ... (a) destroys, conceals or alters ...; or (b) sends or attempts to send ... shall be guilty of an ... | NOTHING |
| 45 | `s 242(2) the person bears the onus of proving that the person did not act with the intent` | a failed "gate" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | the onus lies on the person only 'If in any prosecution for an offence under this section it is proved that' the person did the act; an 'if' unmet (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 46 | `s 228 Part 9 is barred from authorising the investigation` | an "unless" once it is met; line 95 (site by site) [F-K17] | the bar is 'unless specifically provided for in this Part'; an 'unless' met (fork F-K17) | NOTHING |
| 47 | `s 229 the definition governs the word where it is used in Part 9` | an "unless" once it is met; line 95 (site by site) | 'In this Part, unless the contrary intention appears' | NOTHING |
| 48 | `s 231(1) the Minister must appoint one or more inspectors to investigate the affairs of the company` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty arises 'Where a company or foreign company has been declared'; a 'where' unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 49 | `s 231(2) the Minister may take such steps as the Minister considers fit` | a failed "when" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the Minister 'may thereafter take such steps'; a 'may' gated by 'thereafter', which counts as 'when' (periods ruling of 2026-11-05, items (b) and (c); fork F-K7) | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 50 | `s 231(4) the Minister may by notification in the Gazette direct that the expenses be paid by the payer` | a failed "where" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the subsection begins 'Where the Minister is of the opinion that ...'; a 'may' gated by 'where' (periods ruling of 2026-11-05, item (b); fork F-K7) | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 51 | `s 231(6) the person named in the notification is liable to reimburse the Minister in respect of the expenses to the extent specified` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K19] | the liability arises 'Where a notification has been published' and for 'the persons named in the notification'; a 'where' unmet (periods ruling of 2026-11-05, item (b); fork ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 52 | `s 231(8) the expenses ordered to be paid by the company are part of the costs and expenses of the winding up for the purposes of section 203(1)(a) of the Insolvency, Restructuring and Dissolution Act 2018` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) | the deeming applies 'Where a notification under subsection (4) has been published ... and the company is in liquidation or subsequently goes into liquidation'; a 'where' ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 53 | `s 231(9) the report must include a recommendation as to the terms of the notification` | a failed "if" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | the report 'must, if the Minister so directs, include a recommendation'; an 'if' unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 54 | `s 232(2) the application must be supported by the evidence the Minister requires` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty is to support the application with 'such evidence as the Minister requires'; where none is required it asks for none (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 55 | `s 232(2) the Minister may require the applicants to give security for the cost of the investigation` | a failed "before" gate on a "may" function (F-K7); by analogy with "when" (line 94 item (c)); listed, not decided: line 99 (limit 3) | the Minister 'may before appointing an inspector require the applicants to give security'; a 'may' gated by 'before' (periods ruling of 2026-11-05, items (b) and (c); fork ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 56 | `s 233(1) the inspector must make an interim report to the Minister` | a failed "if so directed" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | an inspector 'may, and if so directed by the Minister must, make interim reports'; an 'if' unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 57 | `s 233(1) the Minister must forward a copy of the report to the registered office of the company` | an "if" once it is met; line 95 (site by site) | the forwarding is 'subject to subsection (1B)', and under (1B) 'The Minister is not bound to furnish a company ... with a copy of the report or any part thereof if the ... | NOTHING |
| 58 | `s 233(1) the Minister must forward a copy of the report to the registered office of the company` | a failed "when" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the copy is forwarded when 'on the conclusion of the investigation the inspector must report' and the report has been made; not before (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 59 | `s 233(1) the Minister must deliver a further copy of the report to the applicants` | an "subject to" once it is met; line 95 (site by site) | 'a further copy must, subject to that subsection, at the request of the applicants be delivered to them'; under (1B) the Minister 'is not bound to furnish ... an applicant ... | NOTHING |
| 60 | `s 233(1) the Minister must deliver a further copy of the report to the applicants` | a failed "upon" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the further copy is delivered 'at the request of the applicants' once the report is made; an 'at the request' ('upon') unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 61 | `s 233(1A) the Minister must give the person a copy of the report` | an "if" once it is met; line 95 (site by site) | 'the Minister must not give a copy of a report ... to a person under subsection (1A) if the Minister believes that legal proceedings ... might be unduly prejudiced' (s ... | NOTHING |
| 62 | `s 233(1A) the Minister must give the person a copy of the report` | an "if" once it is met; line 95 (site by site) | (1A) is 'Subject to subsections (1B) and (1C)', and 'The Minister is not bound to furnish a company, an applicant or any other person with a copy of the report or any part ... | NOTHING |
| 63 | `s 233(1A) the Minister must give the person a copy of the report` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty is to give a copy 'to each person to whom in the opinion of the Minister the report ought to be given by reason that it relates to the affairs of that person to a ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 64 | `s 233(1C) the Minister must not give the person a copy of the report under subsection (1A)` | the provision's own question, or a bar's own question; line 98 (limit 2) [F-K25] | the bar applies 'if the Minister believes' and is 'Subject to subsection (1D)'; a bar's own question, with its 'if' unmet or its 'subject to' met (fork F-K25) | NOTHING (line 87) |
| 65 | `s 233(2) the Minister may cause the report to be printed and published` | an "if" once it is met; line 95 (site by site) | the Minister 'must refrain from so doing if the Attorney-General has certified in writing that publication of the report would be prejudicial to the administration of justice' | NOTHING |
| 66 | `s 233(3) the Minister must cause a prosecution to be instituted` | a failed "gate" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | the duty arises 'If from any report of an inspector appointed by the Minister it appears to the Minister that the case is one in which a prosecution ought to be instituted'; ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 67 | `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution` | an "unless" once it is met; line 95 (site by site) | 'all officers and agents of the company (other than the defendant in the proceedings)' | NOTHING |
| 68 | `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution` | a failed "on being required" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | the duty arises 'on being required by the Minister to do so'; an 'on' unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 69 | `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution` | a duty limited by its own wording, answered JUST FALSE (F-K26); line 98 (limit 2) against line 87 | 'all assistance in connection with the prosecution which they are reasonably able to give'; a duty limited by its own wording (fork F-K26) | NOTHING |
| 70 | `s 236(1) the inspector must report on the affairs of the other corporation so far as the inspector thinks the results of the investigation relevant` | a failed "gate" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | the duty to report follows the investigation of the other corporation ('the inspector has power to do so, and the inspector must report on the affairs of the other ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 71 | `s 236(2) the officer or agent must produce to the inspector all books and documents in the officer's or agent's custody or power` | a failed "gate" gate on a duty or on the provision's own question; reading (a); no ruling [F-K5] | the duty to produce arises 'if required by an inspector'; an 'if' unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 72 | `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation` | a duty limited by its own wording, answered JUST FALSE (F-K26); line 98 (limit 2) against line 87 | 'all assistance in connection with the investigation which he or she is reasonably able to give'; a duty limited by its own wording (fork F-K26) | NOTHING |
| 73 | `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents` | a period or duration the text fixes has ended; line 93 item (a) (ruled) | access 'at all reasonable times ... so long as they are in his or her possession'; the duty lapses outside reasonable times or when the inspector no longer has them ('so long ... | none: settled by the ruling, listed for completeness |
| 74 | `s 236(5) the Court may punish the offender in like manner as if the offender had been guilty of contempt of the Court` | a failed "thereupon" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the Court 'may thereupon inquire into the case and, after hearing any witnesses ... punish the offender'; a 'may' gated by 'thereupon' and 'after hearing' (periods ruling of ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 75 | `s 236(6) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` | a flat negative; reading (a), second half; line 92 (N2) [F-K11] | 'No person, who is or has formerly been an officer or agent of a corporation the affairs of which are being investigated under this Part, is entitled to refuse to answer any ... | NOTHING: a flat negative says no of what it names only |
| 76 | `s 236(6) the answer is barred from use in a subsequent criminal proceeding` | an "except" once it is met; line 95 (site by site) [F-K27] | the answer 'may not be used in any subsequent criminal proceedings except in the case of a charge against the person for making a false statement in answer to that question'; ... | NOTHING |
| 77 | `s 236(7) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` | an "subject to" once it is met; line 95 (site by site) [F-K11] | 'Subject to subsection (6)': subsection (6) takes the entitlement away from such a person (an 'entitled'-named function; fork F-K11) | NOTHING |
| 78 | `s 236(8) the signed notes may be used in evidence in legal proceedings against the person` | an "thereafter" once it is met; line 95 (site by site) | 'any such signed notes may except in the case of any answer which that person would not have been required to give but for subsection (6) thereafter be used in evidence'; an ... | NOTHING |
| 79 | `s 243(1) the Minister may appoint inspectors to investigate the ownership of the corporation` | a failed "where" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the subsection begins 'Where it appears to the Minister that there is good reason to do so'; a 'may' gated by 'where' (periods ruling of 2026-11-05, item (b); fork F-K7) | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 80 | `s 243(3) the Minister must appoint an inspector to conduct the investigation` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K31, F-K5] | the duty arises 'Where an application ... is made to the Minister by members of the corporation, and the number of applicants or the amount of the shares held by them is not ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 81 | `s 243(3) the Minister must appoint an inspector to conduct the investigation` | an "unless" once it is met; line 95 (site by site) | 'unless the Minister is satisfied that the application is vexatious' | NOTHING |
| 82 | `s 243(3) the appointment must not exclude the matter from the scope of the investigation` | a failed "where" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the prohibition arises 'Where an application ... is made ... the inspector's appointment must not exclude ... any matter which the application seeks to have included'; a ... | NOTHING (line 87: the gate limits the provision in its own wording) |
| 83 | `s 243(3) the appointment must not exclude the matter from the scope of the investigation` | an "except" once it is met; line 95 (site by site) | 'except insofar as the Minister is satisfied that it is unreasonable for that matter to be investigated' | NOTHING |
| 84 | `s 243(4) the inspector's powers extend to the investigation of the circumstances` | an "unless" once it is met; line 95 (site by site) [F-K32] | 'Subject to the terms of an inspector's appointment' (fork F-K32: 'subject to' is read as 'unless') | NOTHING |
| 85 | `s 244(1) the Minister may require the person to give the information to the Minister` | a failed "where" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the subsection begins 'Where it appears to the Minister that there is good reason ... and that it is unnecessary to appoint an inspector' and reaches 'any person whom the ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 86 | `s 244(3) the person is guilty of the offence of failing to give information or giving false information` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('Any person who fails to give any information required ..., or who ... makes any statement which the person knows to be false in a ... | NOTHING |
| 87 | `s 244(4) section 244 requires the banking corporation to disclose the information to the Minister` | a flat negative; reading (a), second half; line 92 (N2) | 'nothing therein requires ... disclosure by a banking corporation to the Minister of any information as to the affairs of any of its customers other than the corporation of ... | NOTHING: a flat negative says no of what it names only |
| 88 | `s 244(6) the committee or body must keep the Minister informed of any information obtained under section 244` | a failed "when" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) [F-K5] | the duty is stated for a committee or body 'in the discharge of its powers under that subsection'; a gate of the 'when' kind unmet on a duty (fork F-K5) | NOTHING (line 87: the gate limits the provision in its own wording) |
| 89 | `s 245(1) the Minister may by order in the Gazette direct that the shares are until further order subject to the restrictions` | a failed "where" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the subsection begins 'Where in connection with an investigation under section 243 or 244 it appears to the Minister that there is difficulty'; a 'may' gated by 'where' ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 90 | `s 245(1) the act is void or barred by the restrictions` | an "except" once it is met; line 95 (site by site) | 'that, except in a liquidation, no payment may be made of any sums due from the company on those shares' | NOTHING |
| 91 | `s 245(1) the act is void or barred by the restrictions` | a list the text does not close with "only" (F-K30); line 87 against the text's own structure | a closed list: the shares are subject to 'the following restrictions' (a) to (d) (fork F-K30) | NOTHING |
| 92 | `s 245(3) the person is guilty of the offence of dealing in shares subject to the restrictions` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('Where any shares are for the time being subject to any restrictions ..., any person who — (a) ...; (b) ...; or (c) ... shall be guilty of ... | NOTHING |
| 93 | `s 245(4) the officer is guilty of the offence of issuing shares in contravention of the restrictions` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('Where shares in any company are issued in contravention of the restrictions ..., the company and every officer of the company who is in ... | NOTHING |
| 94 | `s 245(4) the company is guilty of the offence of issuing shares in contravention of the restrictions` | an unmet element of an offence (split site (i), F-K10); line 98 against line 87 | an element of the offence is unmet ('Where shares in any company are issued in contravention of the restrictions ..., the company ... shall be guilty of an offence'); split ... | NOTHING |
| 95 | `s 245(5) the prosecution is barred for want of the consent of the Public Prosecutor` | an "except" once it is met; line 95 (site by site) | 'must not be instituted under this section except with the consent of the Public Prosecutor'; an 'except' met | NOTHING |
| 96 | `s 246 the Minister may by notice declare that the inspector is to have the same powers and duties in Singapore as an inspector appointed under section 231` | a failed "where" gate on a "may" function (F-K7); line 93 item (b) says JUST FALSE; listed, not decided: line 99 (limit 3) | the section begins 'Where — (a) under a corresponding law ... an inspector has been appointed ...; and (b) the Minister is of the opinion that ... it is expedient'; a 'may' ... | NOTHING (the grant ruling, line 87 and lines 96 to 99) |
| 97 | `s 246 the inspector has the powers and duties of an inspector appointed under section 231` | a failed "thereupon" gate on a duty or on the provision's own question; ruled: line 93 item (b), line 94 item (c) | the inspector has those powers and duties 'thereupon', on the Minister's declaration; a 'thereupon' unmet (periods ruling of 2026-11-05, item (b)) | NOTHING (line 87: the gate limits the provision in its own wording) |


### Table 2. "Not covered" branches that rest on reading (b)

Each row is a function with a `NOTHING-kind (limited by its own wording)` branch: a grant, a duty or a prohibition that the text limits in its own words, and a case that falls outside the limit.
The "other reading" of every row is JUST FALSE (the limit counted as the text's no).
Where a row relies on a ruling, the rule column says which: line 93 item (c) ("a scope limit with no 'only' ... outside the scope the answer is `NOTHING`"), line 97 (limit 1 of the grant ruling, for a "may" or "power" function whose `if` gate failed, F-K18), or line 87.


| n | function | tag | the limit in the text's words | rule it relies on | other reading |
| --- | --- | --- | --- | --- | --- |
| 1 | `s 139 the time specified is extended by` | limited by its own wording | 'in relation to an instrument, deed, statement or other document executed or made in a place out of Singapore' names the documents whose time is ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 2 | `s 141 this Division applies to the charge of the foreign company` | limited by its own wording | the proviso removes only a charge on property outside Singapore of a foreign company registered under Division 2 of Part 11; for any other charge of ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 3 | `s 134(2) the notice is conclusive evidence that the requirements as to registration have been complied with` | limited by its own wording | the sentence makes 'the notice' conclusive evidence; where no notice has been issued it says nothing of the requirements as to registration | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 4 | `s 134(3) the certificate is conclusive evidence that the requirements as to registration have been complied with` | limited by its own wording | the sentence makes 'the certificate' conclusive evidence; where none has been issued it says nothing of the requirements as to registration | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 5 | `s 135(1) the company must cause a copy of the notice of registration, or a statement of the registration and its date, to be endorsed on the debenture or certificate` | limited by its own wording | the duty is stated for 'every debenture forming one of a series of debentures, or certificate of debenture stock which is issued by the company and ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 6 | `s 135(3) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for a person the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 7 | `s 136(2) the chargee's statement constitutes sufficient evidence of the payment, satisfaction, release or ceasing` | limited by its own wording | the sentence makes 'the second-mentioned statement', the chargee's, sufficient evidence; it says nothing of other proof | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 8 | `s 137 the person may apply to the Court for the extension of time or the rectification` | limited by its own wording | the section names an application 'of the company or any person interested' for an omission or mis-statement of the kind it describes; it says nothing ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 9 | `s 137 the Court may order that the time for registration be extended or that the omission or mis-statement be rectified` | limited by its own wording | the Court's power is stated 'on being satisfied' and 'on the application of the company or any person interested'; the section does not say the Court ... | split site (ii): fits none of the Guide's lines exactly (F-K13, F-K15, F-K21, F-K24) | JUST FALSE (reading (b) turned the other way) |
| 10 | `s 137 the Court may make the relief subject to a term that it is without prejudice to liability already incurred in respect of the default` | limited by its own wording | the term is one of 'such terms and conditions as seem to the Court just and expedient' on which the Court orders relief; where it grants none the ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 11 | `s 138(1) the company must keep the instrument creating the charge, or a copy, at its registered office` | limited by its own wording | the duty is stated for 'any charge requiring registration under this Division'; the subsection says nothing of another charge | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 12 | `s 138(1A)(a) the instrument or copy is deemed to form part of the records required to be kept under section 199(1)` | limited by its own wording | the deeming is stated for an instrument or copy 'that is required to be kept under subsection (1)'; it says nothing of any other | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 13 | `s 138(1A)(b) the last day of the period of 5 years for which the instrument must be retained` | limited by its own wording | the 5 years run 'after' an event of (i) or (ii); until one occurs the paragraph fixes no day | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 14 | `s 138(1A)(b) the instrument must still be retained on the day` | limited by its own wording | no event of (i) or (ii) has occurred, so the paragraph fixes no period | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 15 | `s 138(3) the item must be open to the person's inspection` | limited by its own wording | the instruments or copies are made open to 'any creditor or member'; for any other person only the register is mentioned | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 16 | `s 138(3) the most the company may charge for one inspection` | limited by its own wording | the subsection fixes no fee for another person's inspection of the instruments, because it does not open them to another person | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 17 | `s 138(3) the fee the company has fixed is within the limit` | limited by its own wording | see the limit function | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 18 | `s 138(3A) the person may be furnished with a copy of the instrument or debenture` | limited by its own wording | the person may be furnished with a copy 'on application to a company and on payment of a fee'; the subsection does not say that a person who has not ... | split site (ii): fits none of the Guide's lines exactly (F-K13, F-K15, F-K21, F-K24) | JUST FALSE (reading (b) turned the other way) |
| 19 | `s 138(4) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for a person the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 20 | `s 131(3) the charge is one to which section 131 applies` | limited by its own wording | section 131(1) speaks of 'a charge to which this section applies is created by a company'; it says nothing of a charge created by anyone else | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 21 | `s 131(2) subsection (1) affects the contract or obligation` | limited by its own wording | the sentence is about a contract or obligation for repayment of the money secured | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 22 | `s 131(6) the omission affects the validity of the debentures issued` | limited by its own wording | the sentence speaks of an omission; where nothing was omitted it says nothing of validity | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 23 | `s 131(7) the omission affects the validity of the debentures issued` | limited by its own wording | the sentence speaks of an omission; where nothing was omitted it says nothing of validity | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 24 | `s 131(8) the deposit is treated as the issue of the debentures at a discount for the purposes of subsection (7)` | limited by its own wording | the sentence is about the deposit of debentures as security for a debt of the company | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 25 | `s 131(9) the charge or assignment needs to be filed or registered under another written law` | limited by its own wording | the sentence leaves out a charge or assignment relating to land and speaks only of one to which the section applies | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 26 | `s 132(1) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for a person the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 27 | `s 132(2) the amount the person may recover from the company` | limited by its own wording | the subsection fixes an amount only where registration is effected by a person other than the company | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 28 | `s 133(2) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for a person the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 29 | `s 237(1) who must pay the expenses of and incidental to the investigation` | limited by its own wording | the subsection speaks of 'an investigation by an inspector appointed pursuant to sections 232 and 243'; the cost of an investigation of a declared ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 30 | `s 238 the copy is admissible in any legal proceedings as evidence of the inspector's opinion and of the facts upon which the opinion is based` | limited by its own wording | the section makes admissible 'A copy of the report of any inspector appointed under this Part, certified as correct by the Minister'; whether any ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 31 | `s 239(1) the inspector may employ the persons the inspector considers necessary` | limited by its own wording | the subsection speaks of 'An inspector of a declared company' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 32 | `s 239(1) the inspector may in writing authorise the employed person to do the thing` | limited by its own wording | the subsection speaks of 'An inspector of a declared company' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 33 | `s 239(1) the inspector may in writing authorise the employed person to do the thing` | limited by its own wording | the inspector may 'in writing authorise any such person to do anything the inspector could himself or herself do'; the subsection says nothing of an ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 34 | `s 239(2) the officer or agent is liable to be dealt with in the manner provided in section 236(5)` | limited by its own wording | the subsection makes liable 'Any officer or agent of a corporation who' refuses or fails in the two ways it names; it does not say that no other ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 35 | `s 240(2) the action or proceeding is void and of no effect` | limited by its own wording | the subsection makes void 'Any action or proceeding which is commenced or proceeded with in contravention of this section'; whether any other action ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 36 | `s 241(1) the application is treated as having been made by` | limited by its own wording | the Insolvency, Restructuring and Dissolution Act 2018 applies 'as if' the application had been made, for an application 'made by the Minister' under ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 37 | `s 242(1) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for a person the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 38 | `s 228 Part 9 is barred from authorising the investigation` | limited by its own wording | the section bars an investigation into the insurance business of a company or the business of a banking corporation; it says nothing of any other ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 39 | `s 230 the Minister may by order declare the body to be a company to which Part 9 applies` | limited by its own wording | 'The Minister may by order declare ... if the Minister is satisfied' of a listed ground; a 'may' with an 'if' (not 'only if') gate: the grant ruling ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 40 | `s 231(2) the inspector may inform the Minister of the matters without making an interim report` | limited by its own wording | the power is stated for 'an inspector appointed under subsection (1)' and for 'matters coming to the inspector's knowledge as a result of the ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 41 | `s 231(3) the expenses are defrayed in the first instance out of moneys provided by Parliament` | limited by its own wording | the subsection speaks of 'the expenses of and incidental to an investigation of a declared company' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 42 | `s 231(5) the notification may specify the time or times and the manner in which the payment of the expenses must be made` | limited by its own wording | the sentence is about 'A notification under subsection (4)' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 43 | `s 231(7) action to recover the expenses may be taken in the name of the Government in any court of competent jurisdiction` | limited by its own wording | the subsection speaks of 'any such expenses', those of subsection (6) | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 44 | `s 231(9) the report may include a recommendation as to the terms of the notification` | limited by its own wording | the report 'may if the inspector thinks fit, and must, if the Minister so directs'; a 'may' with an 'if' gate: the grant ruling of 2026-11-12, limit ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 45 | `s 232(1) the Minister may appoint inspectors on the application` | limited by its own wording | the Minister 'may appoint ... on the application of' the applicants the paragraphs name; the section does not say that the Minister may not act on ... | split site (ii): fits none of the Guide's lines exactly (F-K13, F-K15, F-K21, F-K24) | JUST FALSE (reading (b) turned the other way) |
| 46 | `s 233(1) the inspector may make interim reports to the Minister` | limited by its own wording | the subsection speaks of 'An inspector appointed by the Minister' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 47 | `s 233(1D) the court may order that a copy of the report or part of it be given to the person` | limited by its own wording | the power is stated for 'A court before which legal proceedings are brought against a person for or in respect of matters dealt with in a report'; ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 48 | `s 233(2) the Minister may cause the report to be printed and published` | limited by its own wording | the Minister 'may, if he or she is of the opinion that it is necessary in the public interest'; a 'may' with an 'if' (not 'only if') gate: the grant ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 49 | `s 233(3) the officer or agent must give the Minister all assistance in connection with the prosecution` | limited by its own wording | the duty is stated for 'all officers and agents of the company'; it says nothing of anyone else (a scope limit with no 'only': periods ruling of ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 50 | `s 233(4) the Minister may bring proceedings in the name of the company` | limited by its own wording | the Minister 'may himself or herself bring proceedings' if the report shows proceedings ought in the public interest to be brought; a 'may' with an ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 51 | `s 235 the inspector may investigate the affairs of the other corporation` | limited by its own wording | the inspector 'may, with the consent in writing of the Minister, investigate the affairs of that corporation' where the inspector thinks it ... | split site (ii): fits none of the Guide's lines exactly (F-K13, F-K15, F-K21, F-K24) | JUST FALSE (reading (b) turned the other way) |
| 52 | `s 236(1) the inspector has power to investigate also the affairs of the other corporation` | limited by its own wording | 'If an inspector ... thinks it necessary ... to investigate also the affairs of any other corporation which is or has at any relevant time been ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 53 | `s 236(2) the officer or agent must produce to the inspector all books and documents in the officer's or agent's custody or power` | limited by its own wording | the duty is stated for 'Every officer and agent of a corporation the affairs of which are being investigated under this Part'; the subsection says ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 54 | `s 236(2) the officer or agent must give the inspector all assistance in connection with the investigation` | limited by its own wording | the duty is stated for 'Every officer and agent of a corporation the affairs of which are being investigated under this Part' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 55 | `s 236(3) the inspector may require the person to appear for examination on oath or affirmation` | limited by its own wording | the power is stated 'by notice in the prescribed form' and for 'any officer or agent of any corporation whose affairs are being investigated pursuant ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 56 | `s 236(4)(a) the inspector may take possession of all the books and documents` | limited by its own wording | paragraph (a) speaks of 'An inspector who, pursuant to this section, requires the production of all books and documents' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 57 | `s 236(4)(b) the inspector may retain the books and documents for the time` | limited by its own wording | the inspector may retain 'for such time as the inspector considers to be necessary for the purpose of the investigation'; a longer time is outside ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 58 | `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents` | limited by its own wording | paragraph (c) speaks of 'An inspector who, pursuant to this section, requires the production of all books and documents' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 59 | `s 236(4A) the inspector may require the person to produce all documents in the person's possession or under the person's control relating to the bank account` | limited by its own wording | 'If an inspector has reasonable grounds for believing ... an inspector may require'; a 'may' with an 'if' (not 'only if') gate: the grant ruling of ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 60 | `s 236(5) the inspector may certify the failure or refusal to the Court` | limited by its own wording | 'If any officer or agent ... fails to comply ... or fails or refuses to answer ..., the inspector may certify the failure or refusal'; a 'may' with ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 61 | `s 236(6) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` | limited by its own wording | subsection (6) speaks of a person who is or was an officer or agent of the corporation investigated and of a question relevant or material to the ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 62 | `s 236(6) the answer is barred from use in a subsequent criminal proceeding` | limited by its own wording | the bar is stated for a person who claims that the answer might incriminate and who but for the subsection would have been entitled to refuse | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 63 | `s 236(7) the person is entitled to refuse to answer the question on the ground that the answer might tend to incriminate the person` | limited by its own wording | the entitlement is to refuse 'on the ground that the answer might tend to incriminate'; where it would not, the subsection says nothing | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 64 | `s 236(8) the inspector may cause notes of the examination to be recorded, reduced to writing and read to or by and signed by the person examined` | limited by its own wording | the subsection speaks of 'any examination under this Part' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 65 | `s 236(8) the signed notes may be used in evidence in legal proceedings against the person` | limited by its own wording | the subsection speaks of 'such signed notes'; unsigned notes are outside it | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 66 | `s 243(2) the appointment may define the scope of the inspector's investigation` | limited by its own wording | the subsection speaks of 'The appointment of an inspector under this section' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 67 | `s 243(4) the inspector's powers extend to the investigation of the circumstances` | limited by its own wording | the powers 'extend to the investigation of any circumstances suggesting the existence of an arrangement or understanding ... relevant to the purposes ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 68 | `s 243(5) the provisions of Part 9 on the investigation of declared companies apply to the investigation with the necessary modifications` | limited by its own wording | 'For the purposes of any investigation under this section' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 69 | `s 243(5)(a) Part 9 applies in relation to the person as it applies in relation to officers and agents of the corporation` | limited by its own wording | 'this Part applies in relation to all persons who are or have been, or whom the inspector has reasonable cause to believe to be or to have been' so ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 70 | `s 243(5)(b) the Minister is not bound to furnish the person with a copy of the report or with a complete copy of it` | limited by its own wording | 'the Minister is not bound ... if the Minister is of opinion that there is good reason for not divulging'; an exemption with an 'if' (not 'only if') ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 71 | `s 243(5)(b) the Minister may cause a copy of the report or of the parts of it to be kept by the Registrar` | limited by its own wording | the Minister 'may, if the Minister thinks fit, cause to be kept by the Registrar a copy of the report or (as the case may be) the parts of the ... | line 97, limit 1: a grant with an "if" gate answers NOTHING (F-K18) | JUST FALSE (reading (b) turned the other way) |
| 72 | `s 244(2) the person is deemed to have an interest in the share or debenture for the purposes of section 244` | limited by its own wording | 'a person is deemed to have an interest ... if' one of three; a deeming says who is treated as interested and does not say that no one else is | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 73 | `s 244(3) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for a person the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 74 | `s 244(4) section 244 applies to the banking corporation` | limited by its own wording | the subsection speaks of 'a banking corporation'; for any other person the section applies as it reads | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 75 | `s 244(4) section 244 requires the banking corporation to disclose the information to the Minister` | limited by its own wording | the subsection excludes only a banking corporation's information about its other customers; for any other information section 244(1) governs | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 76 | `s 244(5) the Minister may delegate the powers under section 244 to the delegate` | limited by its own wording | the Minister 'may by notification in the Gazette delegate ... either generally or in any particular case' to the two kinds of delegate the subsection ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 77 | `s 244(7) the Minister may exercise the power despite a delegation of it` | limited by its own wording | the subsection speaks of 'any of the powers conferred upon the Minister under this section' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 78 | `s 245(1) the act is void or barred by the restrictions` | limited by its own wording | the restrictions are those to which the shares are 'until further order subject' under an order of the Minister; with no such order the subsection ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 79 | `s 245(2) the order may continue the application of subsection (1)(c) and (d) to the shares` | limited by its own wording | 'Any order ... directing that shares will cease to be subject to the restrictions ... which is expressed to be made with a view to permitting a ... | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 80 | `s 245(3) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for a person the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 81 | `s 245(4) the most the person may be sentenced to on conviction` | limited by its own wording | the penalty is fixed only for the company and the officer the subsection makes guilty | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 82 | `s 245(5) the prosecution is barred for want of the consent of the Public Prosecutor` | limited by its own wording | the bar is on 'A prosecution ... under this section' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |
| 83 | `s 245(6) section 245 applies to the debentures as it applies to shares` | limited by its own wording | the subsection speaks of 'debentures' | line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" | JUST FALSE (reading (b) turned the other way) |


### Reading a result: FALSE and NOTHING (sgk)

Every answer of a decision function in this encoding is one of three things.

- **JUST TRUE** is "yes, on the facts given": the charge must be registered, the Minister must give me a copy of the report, the person is guilty of the offence.
- **JUST FALSE** is the text's own no, in its own words, for the case given.
  In this subject it means things like: the statement was lodged inside the 30 days; the charge is one the section takes out (a shipowner's lien created on or after 1 October 2018, a charge capable of registration under the aircraft equipment Act); the subsection says "does not" or "nothing in this Division applies"; an element of an offence is missing (no default, no intent, no knowledge); the duty has not arisen because the "where", "if" or "upon" it depends on is not met; an "unless" or "except" has been met.
  It does not mean "the Minister may not" for a power: a "may" function whose "if" gate fails answers NOTHING, not JUST FALSE (F-K18).
- **NOTHING** is "the text does not say, on these facts": it is not a no.
  In this subject it means: the application is not one the paragraphs of s 232(1) name, and the section does not say the Minister may not act on it; the person has not applied for a copy under s 138(3A), and the subsection does not say a person who has not applied may not be furnished with one; the inspector has no written consent under s 235, and the section does not say the inspector may not investigate; the person is not one the penalty provision makes guilty, so it fixes no penalty for them; the case is one that depends on another Act, a regulation or a judgment the text hands to someone else.
  A caller must never turn NOTHING into FALSE; the header of `sgk-seat.l4` says how to read an answer.

A **penalty** function returns `JUST` a `Penalty` (the highest fine, the longest imprisonment, whether both may be imposed, whether a default penalty also applies) for a person the text makes guilty, and NOTHING for anyone else.
The amounts are copied from the text: $1,000 and a default penalty (ss 132(1), 133(2)), $2,000 (s 135(3)), $2,000 and a default penalty (s 138(4)), $10,000 or 2 years (s 242(1)), $5,000 or 12 months or both (ss 244(3), 245(3)), $5,000 or 12 months (s 245(4)).
The amount of a default penalty is s 408's and is not encoded.

A **regulative rule** is run with `#TRACE` and ends `FULFILLED` (done), `BREACH` (a missed deadline or a forbidden act done) or `RESIDUAL` (still open).
A `RESIDUAL` is not a pass.
A `MUST` with no time limit can only read `RESIDUAL` or `FULFILLED`; "Rules with no breach path (sgk)" lists the 21 of them.

A **question about an official** (the Minister must appoint inspectors, the Registrar must issue a certificate) asks what the text says the official must or may do; its answer tells the individual what to expect, and it never tells the individual what the official will in fact do.



## Seams (sgk)

PLAN.md section 4 says how a part takes another part's answer: as an input fact, named for the fact and the section it comes from.
Table A of that section gives one seam to my ranges (s 4(8)'s reference to Part 9).
The rest of this section lists each seam I took as an input, the one I gave, and the seams I found that the plan lacks.

### Seam given

| asking | answering | what | status |
| --- | --- | --- | --- |
| keel s 4(8) (`sg-interpretation.l4`: `the reference is in section 8A, 8C, 8D, 216, Part 9 or section 402`, a BOOLEAN) | `s 228 the provision is in Part 9` (a BOOLEAN over the number of the section, true for sections 228 to 246) | the caller passes my answer to the keel's input; both ends are tested (`sgk-tests-part9-declared.l4`: 227 and 247 are out, 228 and 246 are in) | given; the seat has no question for it |

### Seams taken as inputs

| asking provision of mine | answering provision or Act | input (name, type) |
| --- | --- | --- |
| s 235; s 236(1) (the other corporation) | s 6 (the keel's `s 6 the corporations are deemed to be related to each other`) | `the other corporation is or has at any relevant time been a corporation deemed to be related to the company by virtue of section 6`, BOOLEAN, one name in both modules and in the seat; see "Seams found that the plan lacks" below for why it is not PLAN.md's reserved name |
| s 132(1), s 138(4), s 245(4) | s 408(3), "officer in default" (a later wave) | `the person is an officer of the company who is in default, as section 408(3) uses the phrase`, BOOLEAN; for s 133(2) the same with "of the company or foreign company" |
| s 132(1), s 133(2), s 138(4) | s 4(1) "default penalty", s 408 (a later wave) | not an input: the `Penalty` record carries `penalty: the person is also liable to a default penalty` as TRUE and the amount is not encoded (PLAN.md section 3A) |
| s 138(1A)(a) | s 199(1) and (2) (a later wave) | not an input: the function states the deeming that the instrument or copy forms part of the records required under s 199(1) and the 5-year retention under s 199(2); s 199 itself is not applied |
| s 131(3B) | the International Interests in Aircraft Equipment Act 2009, and its s 2(1) for "registered" (s 131(3C)) | `the charge is capable of being registered under the International Interests in Aircraft Equipment Act 2009`, BOOLEAN (F-K3) |
| s 131(3)(d) | the law on bills of sale (not named in the text) | `the charge is created or evidenced by an instrument which, if executed by an individual, would require registration as a bill of sale`, BOOLEAN |
| s 131(3) as in force before 3 January 2016 (s 131(3AA)) | that earlier text of s 131(3), which is not in this edition | `the charge was one to which section 131 applied under subsection (3) as in force immediately before 3 January 2016`, BOOLEAN (the branch answers NOTHING with tag "undefined term" when the facts do not settle it) |
| s 131(9) | "any other written law" | not an input: the function answers whether a charge or assignment needs to be filed or registered under another written law, from `the charge or assignment relates to land` and the facts of s 131(3); what another law requires is not encoded |
| s 140 | "the repealed written laws" | `on 29 December 1967 the charge was registrable under one of the repealed written laws`, BOOLEAN |
| s 141 | Division 2 of Part 11 (foreign companies; a later wave) | `the foreign company is registered under Division 2 of Part 11`, BOOLEAN |
| s 134(3) and the other provisions that say "prescribed" | the regulations (not a source) | `the company has paid the prescribed fee`, `the requirement is made by notice in the prescribed form` and the like, BOOLEAN; no prescribed amount is encoded |
| s 137; s 131(10) | the Court's judgment | `the Court is satisfied that ...` (three facts for s 137) and `it is proved to the satisfaction of the Court that the subsequent charge was given in good faith ...` (s 131(10)), BOOLEAN each: a judgment the text hands to the Court, asked as a fact |
| s 230, s 231(4), s 233(1A), s 233(1B), s 233(1C), s 243(3), s 243(5)(b), s 244(1), s 245(1), s 246 | the Minister's opinion, belief or satisfaction | BOOLEAN each, named for the opinion (for example `the Minister is satisfied that the application is vexatious`) |
| s 231(8), s 241(1) | the Insolvency, Restructuring and Dissolution Act 2018 (s 203(1)(a); the winding-up application) | `the company is in liquidation or subsequently goes into liquidation`, BOOLEAN; for s 241(1) the choice `s 241(1) deemed applicant` (the company, or a creditor or contributory of the foreign company), and `on an application under subsection (1) an order has been made ...` for s 241(2) |
| s 243(3) | s 232 (my own range) | `the number of applicants or the amount of the shares held by them is not less than that required for an application for the appointment of an inspector under section 232`, BOOLEAN (F-K31); the s 232(1) functions are there to compute it |
| s 244(4) | the Banking Act 1970 | `the Banking Act 1970 provides that the banking corporation must disclose the information to the Minister`, BOOLEAN; the branch answers NOTHING with tag "points outside the text" |
| s 244(5) | "any written law relating to the securities industry" | `the delegate is a committee of an approved exchange that has been approved by the Minister under a written law relating to the securities industry`, BOOLEAN |
| s 245(5) | the Public Prosecutor | `the Public Prosecutor has consented to the prosecution`, BOOLEAN |
| s 246 | "a corresponding law of another country" | `under a corresponding law of another country an inspector has been appointed to investigate the affairs of a corporation`, BOOLEAN |

### Seams found that the plan lacks

- **The keel's own definitions that my ranges could call and do not.**
  The keel defines `s 4(1) "charge"` (an "includes" definition: a mortgage, or an agreement to give or execute a charge or mortgage, whether upon demand or otherwise), `s 4(1) "Court"`, `s 4(1) "Registrar"` and `s 4(1) "prescribed"`.
  I import only `sg-core` and `sg-periods`.
  A charge is the starting fact of Division 8: every function of ss 131 to 141 takes "the charge" as already given and asks the facts of s 131(3) about it.
  A caller who holds only a mortgage or an agreement to give a charge asks the keel's `s 4(1) "charge" the thing is within the word charge` first and, if it answers NOTHING, has no answer under this encoding.
  `Court`, `Registrar` and `Minister` are the core's `Party` constructors; "prescribed" things are inputs as above.
- **The keel's `s 7(1) section 244` and `s 7(6A)`.**
  The keel's s 7(1) says subsection (6A) "also has effect for the purposes of section 244", and s 7(6A) treats "a book-entry security ... as if it were an interest in a share" for section 244.
  My s 244(2) function (`s 244(2) the person is deemed to have an interest in the share or debenture for the purposes of section 244`) takes the three limbs of s 244(2) as facts and does not call the keel's `s 7(6A)` function; a caller whose person holds a book-entry security asks the keel with purpose `s 7(1) section 244`.
- **A name that is not PLAN.md's reserved one.**
  PLAN.md section 7 reserves `the other corporation is deemed to be related to the corporation by virtue of section 6` for the s 6 fact, and says that a seat which wants a fact not in its table names it for the fact.
  Sections 235 and 236(1) ask whether the other corporation "is or has at any relevant time been" related, which the reserved name does not carry, so I named that fact in the text's own words and used one name for it in both modules and in the seat.
  The merged seat may ask the reserved name and mine of the same person; the lead can alias them.


## Split sites (sgk)

The brief leaves two questions to the part agent, recorded site by site and not harmonised with any other part.
I did not look at, and did not change an answer to match, what another part did.
Each site below has one fork line (the entry named in the first column) giving the provision, the function, the answer taken and the other reading; each names the line of `inputs/ENCODING-GUIDE.md` section 5 that the answer relies on.

**Counts.** Type (i), an unmet element of an offence or a contravention: **9 sites, all answered JUST FALSE** (F-K10).
Type (ii), a "may" gated by "where", "when", "upon", "on application", "with the consent of" and the like: **15 sites**, of which **11 are answered JUST FALSE** (F-K7) and **4 are answered NOTHING** (F-K13, F-K15, F-K21, F-K24).
The 8 "may" or "power" functions with an `if` gate (F-K18) are not split sites: they answer NOTHING under limit 1 of the grant ruling, which settles them, and they have their own fork lines.

### Type (i): an unmet element of an offence (9 sites, all JUST FALSE)

The answer is JUST FALSE at every site because the function is the provision's own question (is the person guilty of the offence?), and the element that is missing is a limit that the text states in the same sentence as the offence.
Guide line 98 (limit 2 of the grant ruling of 2026-11-12): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question".
The other reading, NOTHING, rests on line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit".
Line 87 and line 98 point apart at every one of these sites, so all nine are also listed under Marginal readings.

| fork line | provision | function | missing element |
| --- | --- | --- | --- |
| F-K10 | s 132(1) | `s 132(1) the person is guilty of the offence of default in complying with section 131` | default in complying with s 131, or officer in default |
| F-K10 | s 133(2) | `s 133(2) the person is guilty of the offence of default in complying with section 133` | default in complying with s 133, or officer in default |
| F-K10 | s 135(3) | `s 135(3) the person is guilty of the offence of authorising or permitting the delivery of an unendorsed debenture or certificate` | "knowingly and wilfully", or an unendorsed debenture |
| F-K10 | s 138(4) | `s 138(4) the person is guilty of the offence of default in complying with section 138` | default in complying with s 138, or officer in default |
| F-K10 | s 242(1) | `s 242(1) the person is guilty of the offence of defeating the purposes of Part 9 or obstructing an investigation` | the intent, or one of the two acts |
| F-K10 | s 244(3) | `s 244(3) the person is guilty of the offence of failing to give information or giving false information` | the failure, or the false or reckless statement |
| F-K10 | s 245(3) | `s 245(3) the person is guilty of the offence of dealing in shares subject to the restrictions` | knowledge of the restrictions, or one of the three acts |
| F-K10 | s 245(4) | `s 245(4) the officer is guilty of the offence of issuing shares in contravention of the restrictions` | shares issued in contravention, or officer in default |
| F-K10 | s 245(4) | `s 245(4) the company is guilty of the offence of issuing shares in contravention of the restrictions` | shares issued in contravention |

### Type (ii): a "may" with a gate (15 sites)

**Answered JUST FALSE (11 sites, fork line F-K7).**
The periods ruling, line 93, item (b): "a 'where ...' condition: when it fails the answer is `JUST FALSE`"; line 94, item (c): "'when', 'upon' and 'whenever' count as 'where'".
Eight of the 11 gates are "where" (seven) or "thereupon" (one); three are time gates ("thereafter", "before", "at any time after") that I took by analogy with "when".
The other reading is NOTHING, on line 87 ("limits a grant or prohibition in its own wording and the case falls outside the limit") and line 99 (limit 3: "do not change, but list ... a 'may' function whose gate is 'where', 'when' or 'upon'").
I did not change the answer and list the 11 for the maintainer or a lawyer, as limit 3 asks.

| fork line | provision | function | gate |
| --- | --- | --- | --- |
| F-K7 | s 131(4) | `s 131(4) the statement may be lodged even though further proceedings are necessary under the law of the place where the property is` | "Where a charge created in Singapore affects property outside Singapore" |
| F-K7 | s 136(1) | `s 136(1) the company may lodge with the Registrar a statement of satisfaction or release` | "Where, with respect to any registered charge" |
| F-K7 | s 231(2) | `s 231(2) the Minister may take such steps as the Minister considers fit` | "thereafter" (analogy) |
| F-K7 | s 231(4) | `s 231(4) the Minister may by notification in the Gazette direct that the expenses be paid by the payer` | "Where the Minister is of the opinion" |
| F-K7 | s 232(2) | `s 232(2) the Minister may require the applicants to give security for the cost of the investigation` | "before appointing an inspector" (analogy) |
| F-K7 | s 236(5) | `s 236(5) the Court may punish the offender in like manner as if the offender had been guilty of contempt of the Court` | "thereupon" |
| F-K7 | s 241(1) | `s 241(1) the Minister may apply to the Court for the winding up` | "at any time after a report has been made" (analogy) |
| F-K7 | s 243(1) | `s 243(1) the Minister may appoint inspectors to investigate the ownership of the corporation` | "Where it appears to the Minister" |
| F-K7 | s 244(1) | `s 244(1) the Minister may require the person to give the information to the Minister` | "Where it appears to the Minister" |
| F-K7 | s 245(1) | `s 245(1) the Minister may by order in the Gazette direct that the shares are until further order subject to the restrictions` | "Where in connection with an investigation under section 243 or 244 it appears to the Minister" |
| F-K7 | s 246 | `s 246 the Minister may by notice declare that the inspector is to have the same powers and duties in Singapore as an inspector appointed under section 231` | "Where — (a) ... and (b) the Minister is of the opinion" |

**Answered NOTHING (4 sites).**
Guide line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit".
The gates are "on the application of" (s 137, s 232(1)), "on application ... and on payment" (s 138(3A)) and "with the consent in writing of the Minister" (s 235).
None of them is an "if" (limit 1) and none is a "where", "when" or "upon" (limit 3, line 94 item (c)), so the four fit none of the Guide's lines exactly; each says so in its fork line and is listed under Marginal readings.
The other reading is JUST FALSE, if "on application" is read as "upon application" (line 94, item (c)) or "with the consent" as a condition.

| fork line | provision | function | gate |
| --- | --- | --- | --- |
| F-K13 | s 137 | `s 137 the Court may order that the time for registration be extended or that the omission or mis-statement be rectified` | "on being satisfied" and "on the application of the company or any person interested" |
| F-K15 | s 138(3A) | `s 138(3A) the person may be furnished with a copy of the instrument or debenture` | "on application to a company and on payment of a fee" |
| F-K21 | s 235 | `s 235 the inspector may investigate the affairs of the other corporation` | "with the consent in writing of the Minister" |
| F-K24 | s 232(1) | `s 232(1) the Minister may appoint inspectors on the application` | "on the application of" |

**Two functions that look like (ii) and are not.**
`s 137 the person may apply to the Court for the extension of time or the rectification` answers NOTHING under line 93 item (c) (a scope limit: the section names the company and any person interested).
`s 244(5) the Minister may delegate the powers under section 244 to the delegate` has no gate of the kind; its limit is the two kinds of delegate the text names.


## Rules with no breach path (sgk)

A regulative `MUST` with no `WITHIN` has no time limit: a late act still reads `FULFILLED`, and no trace can show it breached.
21 of the regulative rules of my ranges are of that kind.
For each, the test file has one trace that reads `RESIDUAL` (nothing done) and one that reads `FULFILLED` (done), and none that reads `BREACH`; each trace carries its `-- EXPECT` word and `tracecheck.py` (work area, not shipped) compared every one with the output of both stable builds.
The column "consequence the text states" says where the text attaches a consequence to the same duty; that consequence is a separate function over the facts, tested, and is not something the rule's trace can reach.

| provision | rule | consequence the text states |
| --- | --- | --- |
| s 134(1) | `s 134(1) the Registrar must enter the particulars of the charge in the register` | none |
| s 134(2) | `s 134(2) the Registrar must issue to the company a notice of the registration of a charge` | none |
| s 134(3) | `s 134(3) the Registrar must issue to the company a certificate confirming the registration of the charge` | none |
| s 135(1) | `s 135(1) the company must cause the endorsement to be made` | none for the omission itself; s 135(3) makes it an offence knowingly and wilfully to authorise or permit the delivery of an unendorsed debenture or certificate (`s 135(3) the person is guilty of ...`) |
| s 136(1) | `s 136(1) the Registrar must enter the particulars of the statement in the register` | none |
| s 138(1) | `s 138(1) the company must keep the instrument or a copy at its registered office` | s 138(4): the default offence (`s 138(4) the person is guilty of the offence of default in complying with section 138`) |
| s 138(2) | `s 138(2) the company must keep a register of charges at its registered office` | s 138(4), as above |
| s 231(1) | `s 231(1) the Minister must appoint inspectors for a declared company` | none |
| s 233(1) | `s 233(1) the inspector must report to the Minister on the conclusion of the investigation` | none |
| s 233(1) | `s 233(1) the Minister must forward a copy of the report to the registered office` | none |
| s 233(1A) | `s 233(1A) the Minister must give a copy of the report to the person whose affairs it relates to` | none |
| s 233(3) | `s 233(3) the Minister must cause a prosecution to be instituted` | none |
| s 233(3) | `s 233(3) the officer or agent must give the assistance on being required by the Minister` | none |
| s 236(1) | `s 236(1) the inspector must report on the affairs of the related corporation` | none |
| s 236(2) | `s 236(2) the officer or agent must produce the books and documents and give the assistance` | the inspector may certify the failure to the Court (s 236(5)), which may punish as for contempt (`s 236(5) the inspector may certify ...`, `s 236(5) the Court may punish ...`); s 239(2) for an authorised person |
| s 236(4)(c) | `s 236(4)(c) the inspector must permit the corporation to have access to the books and documents` | none |
| s 237(1) | `s 237(1) the company investigated must pay the expenses of the investigation` | none |
| s 237(2)(a) | `s 237(2)(a) the applicants must make good the deficiency` | none |
| s 243(3) | `s 243(3) the Minister must appoint an inspector to conduct the investigation` | none |
| s 244(3) | `s 244(3) a person must give the information required of the person under section 244` | the offence of s 244(3) (`s 244(3) the person is guilty of ...`) |
| s 245(3)(c) | `s 245(3)(c) the holder must notify the persons entitled to vote of the restrictions` | the offence of s 245(3) (`s 245(3) the person is guilty of ...`) |

The prohibitions (`SHANT`) are not in this list: each reaches `BREACH` when the forbidden act occurs (`s 135(3)`, `s 138(1)` while the charge is in force, `s 233(1C)`, `s 233(2)`, `s 240(1)` during the suspension, `s 241(2)`, `s 242(1)(a)` and `(b)`, `s 244(3)` false statement, `s 245(3)(a)` and `(b)`, `s 245(4)`).
A `SHANT ... WITHIN n` sunsets at day n: `s 138(1)` (while the charge remains in force) and `s 240(1)` (while the suspension lasts) use it, and a trace of a forbidden act after day n reads `FULFILLED`.
The four rules with a deadline reach `BREACH` by a missed deadline: `s 131(1)`, `s 131(6)`, `s 133(1)` (30 days, extended by s 139) and `s 138(3A)` (3 days).


## What the text turns out to say (numbered findings, sgk)

Each finding was read off the text while encoding and is backed by a test or a fork entry.
None is a failing assertion (906 satisfied, 0 failed); they are things a reader of the Act might not expect.

1. **Parts 8 and 8A are two headings over repealed runs.**
   The text reads "217. to 227. [Repealed by Act 40 of 2018]" under Part 8 and "227AA. to 227X. [Repealed by Act 40 of 2018]" under Part 8A, and Part 9 follows at once.
   There is no judicial management to encode, and winding up has gone to the Insolvency, Restructuring and Dissolution Act 2018 (taken as inputs in ss 231(8) and 241).
2. **Section 234 is repealed.**
   The text reads "234. [Repealed by Act 13 of 1987]", so s 233 (reports of inspectors) is followed by s 235 (related corporations).
3. **Division 8 runs four different 30-day clocks, and a fifth period for foreign documents.**
   s 131(1) runs from the creation of the charge, s 131(5) from the execution of the instrument containing the charge (or the first debenture), s 131(6) from each issue of debentures in the series, and s 133(1) from the completion of an acquisition or the registration of a foreign company in Singapore.
   s 139 extends any time specified in the Division "by 7 days or such further periods as the Registrar may from time to time allow" for a document executed or made out of Singapore.
4. **Section 131 reaches charges created on or after 3 January 2016 by ten heads, and earlier ones only through a subsection that is not in this text.**
   s 131(3) lists heads (a) to (j) for charges created on or after 3 January 2016; s 131(3AA) adds a charge created before that date that "was a charge to which this section applied under subsection (3) in force immediately before 3 January 2016".
   That earlier subsection (3) is not printed, so the question whether an older charge was caught cannot be settled from this text: the encoding takes it as an input and answers NOTHING (tag "undefined term") when the facts do not settle it.
5. **The sanction for not registering falls on the security and not on the debt.**
   s 131(1) makes the security "void against the liquidator and any creditor of the company"; s 131(2) says nothing in subsection (1) "affects any contract or obligation for repayment of the money secured" and that "the money secured thereby immediately becomes payable".
   The text names only the liquidator and creditors as those against whom the security is void.
6. **The shipowner's lien is carved out in two steps.**
   A shipowner's lien created on or after 1 October 2018 "is not a charge to which this section applies" (s 131(3AB)); one created before that date is caught "only if", as at that date, an order for winding up had been made, a voluntary winding-up resolution had been passed, or a creditor had acquired a proprietary right (s 131(3AC)); the lien is a "contractual lien" on sub-freights, sub-hires or bill of lading freight (s 131(11)).
7. **The notice and the certificate of registration are each "conclusive evidence", and neither duty has a deadline.**
   s 134(2) makes the notice (issued without application) and s 134(3) the certificate (issued "Upon the application of the company and payment of the prescribed fee") "conclusive evidence that the requirements as to registration have been complied with".
   The Registrar's duties in s 134 and s 136(1) carry no time limit and no stated consequence, so no trace can show them breached.
8. **A debenture issued before the charge was registered need not be endorsed.**
   s 135(2): "Subsection (1) does not apply to any debenture or certificate of debenture stock which has been issued by the company before the charge was registered."
   The offence in s 135(3) is narrower than the duty in s 135(1): it needs a person who "knowingly and wilfully authorises or permits the delivery" of an unendorsed debenture.
9. **Section 137 gives the Court three alternative grounds, the last a catch-all.**
   The omission or mis-statement "was accidental or due to inadvertence or to some other sufficient cause", or "is not of a nature to prejudice the position of creditors or shareholders", or "on other grounds it is just and equitable to grant relief".
   The relief may be made "without prejudice to any liability already incurred by the company or any of its officers in respect of the default".
10. **Retention under s 138 is open-ended until one of two events, then 5 years.**
    The instrument is kept "for as long as the charge ... remains in force"; for the records under s 199(2) it is retained for 5 years after the date the debt was paid or satisfied in whole, the date the property was released, or "the later of the dates" if both occur (F-K14).
11. **The penalties are small in Division 8 and differ in form in Part 9.**
    ss 132(1) and 133(2): a fine not exceeding $1,000 and a default penalty; s 135(3): a fine not exceeding $2,000; s 138(4): $2,000 and a default penalty.
    s 242(1): $10,000 or 2 years; ss 244(3) and 245(3): $5,000 or 12 months or both; s 245(4): $5,000 or 12 months, with no "both".
12. **Section 138(3A) states a person's entitlement and a time, and no duty.**
    "Any person may, on application to a company and on payment of a fee ... be furnished with a copy ... within 3 days of the person making the application."
    The company's duty and its 3-day deadline are inferred (F-K34).
13. **Section 231(6) refers to a notification "under subsection (5)", and the power to publish one is in subsection (4).**
    Subsection (5) says only that "A notification under subsection (4) may specify the time or times and the manner" of payment (F-K19).
14. **Sections 235 and 236(1) give an inspector the same power on different conditions.**
    Section 235 says the inspector "may, with the consent in writing of the Minister, investigate the affairs of that corporation"; section 236(1) says that an inspector who thinks it necessary "has power to do so", without mentioning consent (F-K22).
15. **Section 237(1) names an inspector appointed "pursuant to sections 232 and 243", and says nothing about a declared company.**
    No inspector is appointed under both; for a declared company the expenses are in s 231(3) and (4) (F-K28).
16. **The suspension of s 240 speaks of "any declared company", and an ownership investigation need not be of one.**
    s 243(1) lets the Minister investigate "any corporation, whether or not it is a declared company", and s 243(5) applies the Part's provisions on declared companies "with the necessary modifications"; whether that carries the suspension the text does not say (F-K29).
17. **Section 236 gives officers and agents no privilege against self-incrimination, but a use immunity, and everyone else keeps the privilege.**
    s 236(6) says that "No person, who is or has formerly been an officer or agent of a corporation the affairs of which are being investigated under this Part, is entitled to refuse to answer any question which is relevant or material to the investigation on the ground that the person's answer might tend to incriminate him or her", and that the answer "may not be used in any subsequent criminal proceedings except in the case of a charge against the person for making a false statement in answer to that question".
    s 236(7) keeps the privilege for any person, "Subject to subsection (6)".
    s 236(8) lets signed notes be used in evidence "except in the case of any answer which that person would not have been required to give but for subsection (6)".
18. **Part 9 does not authorise an investigation into an insurer or a bank "unless specifically provided for in this Part", and s 244(4) is the provision that deals with a bank.**
    s 228 bars it; s 244(4) says s 244 "applies to a banking corporation" and then limits what it requires "subject to the provisions of the Banking Act 1970".
    That s 244(4) is the "specific provision" s 228 leaves room for is my reading; the text does not link them.
19. **Applying for an investigation takes numbers or a special resolution.**
    s 232(1): not less than 200 members (excluding the company itself if it is a member) or members holding not less than 10% of the shares issued (excluding treasury shares); debenture holders holding not less than 20% in nominal value; for a company with no share capital, not less than 20% in number of the persons on the register; or, in any case, the company on a special resolution.
20. **An ownership application carries a duty, where an ordinary application carries a power.**
    s 232(1): "The Minister may appoint"; s 243(3): where members apply for an investigation of particular shares or debentures and meet the s 232 numbers, "the Minister must appoint an inspector ... unless the Minister is satisfied that the application is vexatious".
21. **The winding-up route in s 241 opens only after an inspector has reported.**
    "may be made by the Minister at any time after a report has been made in respect of a declared company by an inspector"; the Insolvency, Restructuring and Dissolution Act 2018 then applies as if the company, or for a foreign company a creditor or contributory, had applied; and once a winding-up order is made for a foreign company's Singapore assets it "must not carry on business or establish or keep a place of business in Singapore" (s 241(2)).
22. **A restriction on shares lasts "until further order" and can be lifted in part.**
    s 245(1): the Minister may direct that shares are "until further order subject to the following restrictions"; s 245(2): an order lifting them to permit a transfer may continue restrictions (c) and (d) for rights acquired or offers made before the transfer; s 245(5): no prosecution "except with the consent of the Public Prosecutor".


## What the stable binary does not accept

The binary governs where the skills describe something it rejects.
What I met, each checked on the stable build 1.6.110 (`l4-main-110`) on 2026-11-18, and not an inference from the skills:

- **`MIN` and `MAX` do not exist.**
  `MIN a b` and `MAX a b` both fail with "I could not find a definition for the identifier".
  Where a smaller or larger of two numbers is needed (s 237(2)(a), the amount the applicants must make good, is the case), the function uses `IF`.
- **A record cannot be copied with one field changed.**
  The form `p WITH xx IS 5` on a record value `p` fails with `check/not-a-function` ("You are trying to apply p ... (which is not a function) to (named) arguments here").
  This is the one form I tried.
  The twenty-field record of s 131(3) (`s 131(3) the facts about the charge`) is therefore written in full, positionally with `OF`, once for each charge in `sgk-tests-div8-registration.l4`; the 30 fixtures at the head of that file were generated by a script (`genfix.py`, work area, not shipped) from a one-line description of each charge, so that no field is mistyped by hand.
- **The core `Party` has no Inspector.**
  `sg-core.l4` has no `Inspector` constructor (`grep -c Inspector sg-core.l4` is 0).
  An inspector is the bearer of three regulative rules of Part 9 (`s 233(1)`, `s 236(1)` and `s 236(4)(c)`), and the core's `Party` has Minister, Court, Registrar and Officer but no inspector, no agent of a corporation, and no committee or body of the kind s 244(5) and (6) name.
  I declared `s 231 party` (the Minister, an inspector appointed under Part 9, an officer or agent of a corporation, a person, a company, a foreign company) and `s 231 act` under my own label, and `NEEDS-CORE.md` asks for the constructors.
- **A `MUST` with no `WITHIN` cannot read `BREACH`, and a `SHANT` with `WITHIN n` stops at day n.**
  This is the behaviour PLAN.md section 5 warns of; the traces confirm it ("Rules with no breach path (sgk)").
  So the regulative rules of the Registrar, the Minister and the inspectors have a decision function beside them for the facts, and the traces show `RESIDUAL` and `FULFILLED` only.
- **The two stable builds agree on every one of the 83 traces and on all four counts of every module** (`check.sh` target `main`, and `tracecheck.py` for the traces, which `check.sh` does not compare).
- **Everything else in the brief's list** is avoided: no file uses `REFUSE`, `YMD`, `EVERY`, sets, `TYPICALLY` or a section-level `GIVEN`; `BECAUSE` appears only in `LEST BREACH BY ... BECAUSE`; every `NOT` that stands beside an `AND` or an `OR` is parenthesised (a bare `NOT x` stands only where it applies to one operand); each `#ASSERT` is on one line.
  The files check without an error or a warning (`check.sh` below).


## Seat questions (sgk)

`sgk-seat.l4` has 93 questions, every one with `@export` and `@desc`, every input with an `@desc` worded as the individual would be asked, and every name beginning "Under section N,".
They are grouped under `§` and `§§` headings in the text's order: Part 4 Division 8 (sections 131; 132; 133; 134 to 136; 137; 138; 139 to 141) and Part 9 (sections 228 to 231; 232; 233; 235 and 236; 237 to 239; 240 to 242; 243 to 246).
`sgk-cases-seat.l4` has 280 assertions, one or more for each question, each with the facts a person in the seat would state; every one is satisfied.
The seat restates no rule: each question builds the records the layer-1 function wants from its plain inputs, in a `WHERE`, and calls it.
A question that asks "am I guilty of" an offence passes FALSE for `the person is the company`, because the individual in the seat is never the company, and a second and third question project the highest fine and the longest imprisonment from the same offence function.
Parts 8 and 8A and s 234 have no question (repealed).
Provisions that address only an official have a question only where they mean something to the individual that no other question already answers; I judged that s 134(2), s 136(1) (the Registrar's entry), s 233(1) (the inspector's report and its forwarding), s 236(1), s 236(4)(a) to (c), s 239(1), s 243(1), (2) and (4), and s 244(5) to (7) do not, and they have none.

### The direction check

The brief asks for a list of every seat question whose name and body differ in direction or in subject, and for each to be fixed.
I compared the name of each of the 93 questions with the layer-1 function it calls, by script on 2026-11-18, and read each pair.

- **No question differs in direction.**
  Every "must" asks a function that says "must"; every "may" a function that says "may"; every "am I guilty", "am I entitled", "am I liable" and "is ... void" asks the function of the same name; the bars are titled as bars ("is the foreign company barred from carrying on business" against `s 241(2) the foreign company must not carry on business ...`; "is Part 9 barred from authorising the investigation" against `s 228 Part 9 is barred ...`; "is the action or proceeding barred without the consent of the Minister"; "is the prosecution barred for want of the consent of the Public Prosecutor"), and none is titled "may" or "can" over a bar.
- **No question differs in subject in a way that changes the answer.**
  32 names speak in the first person ("must I", "am I", "may I", "what is the most I can be fined"); their bodies speak of "the person", and the seat adds the facts that make the person the asker (that the person is an officer or agent of the corporation; that the person is not the company).
  The names that speak of the company, the Minister, the Registrar, the Court or the inspector ask the function with that subject; no name asks "must I" where the body is the company's duty.
- **24 names differ from the function name in words only**, and none was changed: 11 penalty questions ("what is the most I can be fined ...", "what is the longest I can be imprisoned ...") whose body projects the highest fine or the longest imprisonment from the offence function's `Penalty`; 6 that put a question word where the function has a noun ("how many days are added", "which particulars", "who must pay", "how much must the applicants make good", "how much may I recover"); 6 that say "does ... apply", "does ... affect" or "does ... include" where the function says "applies", "affects" or "includes"; and `s 241(2)`, "is the foreign company barred" against "must not", the same bar.


## What `check.sh` prints

Run on 2026-11-18, after the last edit of any `.l4` file, as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` (target `main`, the default): every module is run with the stable build 1.6.110 and again with the second stable build 1.6.109, and the four counts must match.
It exited 0.
The output, unedited:

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
sgk-cases-seat.l4                              0       280       0        0         0 |      0       280       0        0  same
sgk-div8-application.l4                        0         0       0        0         0 |      0         0       0        0  same
sgk-div8-register.l4                           0         0       0        0         0 |      0         0       0        0  same
sgk-div8-registration.l4                       0         0       0        0         0 |      0         0       0        0  same
sgk-part9-consequences.l4                      0         0       0        0         0 |      0         0       0        0  same
sgk-part9-declared.l4                          0         0       0        0         0 |      0         0       0        0  same
sgk-part9-inspectors.l4                        0         0       0        0         0 |      0         0       0        0  same
sgk-part9-ownership.l4                         0         0       0        0         0 |      0         0       0        0  same
sgk-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgk-tests-div8-application.l4                  0        24       0        0         0 |      0        24       0        0  same
sgk-tests-div8-register.l4                     0        93       0        0         0 |      0        93       0        0  same
sgk-tests-div8-registration.l4                 0       135       0        0         0 |      0       135       0        0  same
sgk-tests-part9-consequences.l4                0        77       0        0         0 |      0        77       0        0  same
sgk-tests-part9-declared.l4                    0        66       0        0         0 |      0        66       0        0  same
sgk-tests-part9-inspectors.l4                  0       127       0        0         0 |      0       127       0        0  same
sgk-tests-part9-ownership.l4                   0       104       0        0         0 |      0       104       0        0  same
TOTAL (24 modules)                             0       906       0        0           |      0       906       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit=0
```

The baseline it replaced: `check.sh` as supplied lists no module under `expected_failed`, so the expected count is 0 failed everywhere, and before my files were in the folder it printed 8 modules, all keel modules, with 0 satisfied each (the keel's modules carry no assertions of their own).
It now prints 24 modules: the 8 keel modules, the 7 layer-1 modules (0 assertions each), the 7 test files (24, 93, 135, 66, 127, 77 and 104: 626 assertions), the seat (0) and the seat's cases (280); 906 assertions in all, 0 failed, 0 refused, 0 errors, identical on the second build.
As the last lines of the output say, the two builds agreeing on counts does not see a different `#TRACE` outcome; `tracecheck.py` (work area) compares each `-- EXPECT` word with the outcome on both builds, and found 0 mismatches over the 83 traces.

## What the checks were

Each of these was run on 2026-11-18 after the last edit of the `.l4` files and the output read, not only the exit code.

- `python3 -I srcrefs.py check --refs <CoA1967.txt> sgk-*.l4` and the same with `--strict`: 853 `-- src:` lines, 106 quote runs, 196 locators, 0 problems, for all 16 `sgk-*.l4` files.
- `tracecheck.py` over the six test files that have traces: every `#TRACE` has a `-- EXPECT` word, and the outcome matches on both builds.
- `quotecheck.py` (work area): every quoted span of four words or more in a comment of any `sgk-*.l4` file and in this file was looked up in `CoA1967.txt` (page furniture and amendment marks left out, quotes and spacing normalised), or in the Guide, the brief or PLAN.md where it quotes those, with "..." taken as a gap.
  It found 19 inexact quotations in the comments of the modules and the tests (a dash dropped before a list, "the final report" for "the inspector's final report", "a fee not exceeding $2" for "such fee not exceeding $2", "to be furnished" for "be furnished", and similar); each was corrected to the text's own words, and the files were re-checked.
- The coverage script (`coverage.py`): 0 lines in no row or two rows, 0 rows without a disposition.
- The jural table was checked against the layer-1 functions by script: every one of the 199 is named in some row, and every rule named in a row exists.
- The "Rules with no breach path" table was checked against the test files by script: the rules whose traces include no `BREACH` are exactly the 21 listed.
- `l4 check` was not run separately: `l4 run`, which `check.sh` uses, reports the same diagnostics, and its output was read for `DiagnosticSeverity_Error` and `_Warning` (none).
- A fact asked under two names was looked for by script (input names within 0.88 similarity); four pairs were the same fact under two names and were unified (the s 408(3) "officer in default" input in s 245(4); the "officer or agent of a corporation the affairs of which are being investigated" input in s 236(3); the "foreign company" input in s 241(2); and the s 6 relatedness input in s 236(1)).

## The text is a rendering, and the brief governs

`CoA1967.txt` is the Singapore Statutes Online rendering of an informal consolidation of the Act, a PDF turned into plain text; it is not the official text, and nothing in this encoding is verified against the official text.
Where `inputs/PLAN.md` and the brief differ, the brief governs, and "Edition encoded" above says where they differed.
No section "Compared with the earlier pass" is written: there is no `inputs/NAIVE-EVIDENCE/` in this sandbox.

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

No site of this part changed under it (2026S1bC): the functions of this part that stay Boolean after the protocol split already answered as the ruling reads, and its protocol-shaped functions keep limit 3 of the grant ruling until they are re-encoded.
