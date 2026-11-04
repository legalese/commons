# NOTES (snap1): the Food and Nutrition Act of 2008, 7 U.S.C. ch. 51, lines 136-491 and 1341-1424

Status 2026-11-04. Written by part agent `snap1` (run `iaw-snap1`), on the stable binary 1.6.98; every module also runs on the main build 1.6.108 with the same counts.
This file is made by `work/tools/make_notes.py` from the text, the modules and the last `check.sh` run, so the tables below cannot drift from the tree they describe.
Where a sentence says "assumed, not ruled" it is a choice of mine that nobody has ruled on; everything else a sentence says about the tree was checked against the tree when this file was made.

**The text is a converter's rendering, not the official text.**
`inputs/usc07-ch51.txt` is a plain-text rendering made by a converter script from the OLRC's USLM XML.
Editorial and statutory notes are left out (section 2012a's footnote points at a "References in Text note" that the rendering omits), and Title 7 is not positive law.
Nothing in this folder is verified against the official text.
The USDA cost-of-living figures (`fna-snap-cola-fy2027.txt`) are input data, not statute.

## What this part is

My ranges are sections 2012a, 2013, 2014 (a) to (n), 2014a, 2018 (a) to (j) and 2019 (lines 136-491 and 1341-1424).
The Act's text is in layer 1, one module per section or group of subsections, each rule carrying `-- src:` quotation lines and an `@ref ... (src:N-M)` locator.
Layer 2 is a thin seat for a member of a household that applies for or receives SNAP.

| file | holds |
| --- | --- |
| `snap1-logic.l4` | the three-valued helpers (`snap1 both`, `either`, `not`, `known`, `is definitely yes`, `is definitely no`) and the whole-months count |
| `snap1-s2012a.l4` | section 2012a |
| `snap1-s2013.l4` | section 2013: the program, the State cost share, the reservation distribution program |
| `snap1-s2014-abc.l4` | section 2014 (a), (b), (c), and the FY2027 income-standard tables (USDA Tables 1 to 3) |
| `snap1-s2014-d.l4` | section 2014(d): what counts as income |
| `snap1-s2014-e1.l4`, `snap1-s2014-e2.l4` | section 2014(e): the deductions and the net income; the FY2027 deduction tables |
| `snap1-s2014-f.l4` | section 2014(f): how income is calculated |
| `snap1-s2014-g.l4` | section 2014(g): resources, and the FY2027 resource limits |
| `snap1-s2014-hn.l4` | section 2014 (h) to (n) |
| `snap1-s2014a.l4`, `snap1-s2018.l4`, `snap1-s2019.l4` | sections 2014a, 2018 and 2019 |
| `snap1-tests-*.l4` | tests for each module (expected values written from the text) |
| `snap1-seat.l4`, `snap1-cases-seat.l4` | layer 2 and its cases |
| `SEAMS.md`, `PROGRESS.md` | the seams in and out; the state of the work |
| `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` | supplied tooling, unchanged |

There is no `NEEDS-CORE.md`: nothing in `snap-core.l4` blocked this part.

## Coverage (snap1)

Every provision of my ranges has a row, and each row has exactly one disposition: `encoded` (a rule, definition or table in layer 1 with a test, quoting the provision), `inert` (only reasons 1 to 3 of the brief), `fork` (the text can be read two or more ways with different outcomes; the row names the fork and the rule that takes one reading or returns the explicit "not covered" value), or `repealed or blank in this text` (no row has this disposition: nothing in my ranges shows as repealed or blank).
There is no `out-of-scope` row and no `deferred` row.
The table is made by `work/tools/coverage.py` from the text itself: it reads each line, splits it into sentences, and matches each sentence against the quotation lines in the modules.
A sentence that no module quotes must be classified by hand (`work/tools/coverage-overrides.json`), or the script stops.

Audit counts (made by `work/tools/coverage.py --audit`, which reads the text and the quotations in the modules):

- Non-blank lines in my ranges: 434 (136-491 and 1341-1424).
- Text units counted: 467 = 289 body units (a sentence, or a list limb on its own line), 166 headings, 6 section titles, 6 source-credit lines.
- Rows in the table: 277. A heading is not a row of its own: its line is the first line of the row of the provision it heads, and the provision column lists each heading the row carries (172 headings carried).
- Rows by disposition: encoded 222, fork 38, inert (reason 1) 6, inert (reason 2) 11.
- Body units by disposition: encoded 239, fork 39, inert 11.
- Every non-blank line falls in a row: the script stops when one does not, and when a body unit is neither quoted by a rule nor classified.
- Rows before and after the audit pass: 266 rows before, 277 after. "Before" is the table the first draft's quotations supported: the pass found 13 body units that no rule quoted (the limbs of the factor list in section 2018(a)(1)(B), the two limbs of section 2013(b)(5), the two sub-clauses of section 2018(i)(1)(D), the second sentence of section 2014(f)(3)(A), paragraphs 2014(e)(6)(C)(iii)(III) and (D)(iii), and the second sentence of section 2014(i)(2)(C)(i)); each is now quoted, and two needed a new rule (`s 2018(i)(1)(D) the report includes the recommendations`, `s 2014(i)(2)(C)(i) the alien is required to provide the information and documentation given in support of the immigration application`, each with tests). The "before" figure is computed by leaving those units out and building the rows again.
- Rows that quote only part of their sentence: 5 (the words no quotation carries are printed in the row).

The `inert` rows, all of them (the headings are not rows, so none is counted here):

- C032 (lines 198-199, s 2013(b)(6)(C)): machinery: the Secretary determines the definition of a term for the fund; the text states no rule for anyone until that is done
- C037 (lines 209-210, s 2013(c)): machinery: regulation-making power of the Secretary (section 2013(c))
- C148 (lines 376, s 2014(f)(4)): machinery: the Secretary consults the Secretary of Health and Human Services when promulgating regulations
- C185 (lines 430, s 2014(h)(1)): machinery: rule-making procedure (emergency standards may be promulgated without regard to section 2013(c) or 553 of title 5)
- C186 (lines 431-432, s 2014(h)(2)(A)): machinery: the Secretary establishes a Disaster Task Force (an office and its work)
- C187 (lines 433, s 2014(h)(2)(B)): machinery: the Secretary may send members of the Task Force to a State (an office and its staffing)
- C200 (lines 450, s 2014(i)(2)(C)(ii)): machinery: agreements between the Secretary and the Secretary of State and the Attorney General about sharing information
- C235 (lines 1357-1358, s 2018(a)(2)(A)): machinery: the Secretary's regulations provide for periodic reauthorization of stores
- C236 (lines 1359, s 2018(a)(2)(B)): machinery: the Secretary's regulations provide for periodic notice of the definitions of retail food store and wholesale food concern
- C237 (lines 1360-1361, s 2018(a)(3)): machinery: the Secretary establishes the time periods of authorization; the text states none
- C238 (lines 1362-1363, s 2018(a)(4)): machinery: the Secretary issues guidance before implementing clause (iv) of paragraph (1)(B)

Reason 1 (not operative) rows: C002, C038, C223, C225, C273, C277, each a "[Source credit: ...]" line, the enactment history of a section, which creates no rule.
Headings are reason 1 as well; they sit inside the rows of the provisions they head.
No row is `inert` for any other reason; the brief's list of reasons that no longer stand ("addresses an official", "open-textured", "refers to another instrument", and the rest) was not used.
Where a sentence has a regulation-making or administrative part that I did not encode, the row says so in its note and the rest of the sentence is encoded.

### The table

| row | text lines | provision (headings carried by the row) | disposition | L4 name(s) / reason / fork |
| --- | --- | --- | --- | --- |
| C001 | 136-137 | s 2012a [headings: § 2012a. Publicly operated community health centers] | fork | F-A1; chosen: `s 2012a the provision is also applicable to the center` |
| C002 | 138 | s 2012a source credit | inert | reason 1: source credit: the enactment history of the section, creates no rule |
| C003 | 140-143 | s 2013(a)(1) [headings: § 2013. Establishment of supplemental nutrition assistanc...; (a) Program; (1) Establishment] | encoded | `s 2013(a)(1) the eligible household is provided an opportunity to obtain a more nutritious diet through the issuance of an allotment`; `s 2013(a)(1) the benefits may be used for the purchase`; `s 2013(a)(1) the benefits are redeemable at face value by the Secretary through the facilities of the Treasury` |
| C004 | 143 | s 2013(a)(1), sentence 3 | encoded | `s 2013(a)(1) the benefits may be used for the purchase`; `s 2013(a)(1) the benefits are redeemable at face value by the Secretary through the facilities of the Treasury` |
| C005 | 144-146 | s 2013(a)(2)(A) [headings: (2) State quality control incentive; (A) Definition of payment error rate] | encoded | `s 2013(a)(2)(A) the payment error rate of the State for the fiscal year` |
| C006 | 147-149 | s 2013(a)(2)(B)(i) [headings: (B) State cost share; (i) In general] | encoded | `s 2013(a)(2)(B)(i) the shares of the cost of the allotment for the State in the fiscal year` |
| C007 | 150 | s 2013(a)(2)(B)(i)(I) | encoded | `s 2013(a)(2)(B)(i) the shares for the payment error rate` |
| C008 | 151 | s 2013(a)(2)(B)(i)(II) | encoded | `s 2013(a)(2)(B)(i) the shares for the payment error rate` |
| C009 | 152 | s 2013(a)(2)(B)(i)(III) | encoded | `s 2013(a)(2)(B)(i) the shares for the payment error rate` |
| C010 | 153 | s 2013(a)(2)(B)(i)(IV) | encoded | `s 2013(a)(2)(B)(i) the shares for the payment error rate` |
| C011 | 154-156 | s 2013(a)(2)(B)(ii)(I) [headings: (ii) Elections; (I) Fiscal year 2028] | encoded | `s 2013(a)(2)(B)(ii)(I) the payment error rate the State elects to use for fiscal year 2028` |
| C012 | 157-158 | s 2013(a)(2)(B)(ii)(II) [headings: (II) Fiscal year 2029 and thereafter] | encoded | `s 2013(a)(2)(B)(ii)(II) the payment error rate the Secretary uses for fiscal year 2029 and each fiscal year thereafter` |
| C013 | 159-161 | s 2013(a)(2)(B)(iii)(I) [headings: (iii) Delayed implementation; (I) Fiscal year 2025] | fork | F-S1; chosen: `s 2013(a)(2)(B)(iii) the payment error rate multiplied by 1.5 is equal to or above 20 percent`; `s 2013(a)(2)(B)(iii) the fiscal year in which the implementation date under clause (i) falls` |
| C014 | 162-163 | s 2013(a)(2)(B)(iii)(II) [headings: (II) Fiscal year 2026] | fork | F-S1; chosen: `s 2013(a)(2)(B)(iii) the fiscal year in which the implementation date under clause (i) falls` |
| C015 | 164-165 | s 2013(a)(3) [headings: (3) Maximum Federal payment] | encoded | `s 2013(a)(3) the Secretary may pay the amount towards the cost of the allotment` |
| C016 | 166-168 | s 2013(b)(1) [headings: (b) Food distribution program on Indian reservations; (1) In general] | encoded | `s 2013(b)(1) the distribution of commodities shall be made` |
| C017 | 169-171 | s 2013(b)(2)(A) [headings: (2) Administration; (A) In general] | encoded | `s 2013(b)(2) the party that administers the distribution` |
| C018 | 172-173 | s 2013(b)(2)(B) [headings: (B) Administration by tribal organization] | encoded | `s 2013(b)(2)(B) the tribal organization is capable of effectively and efficiently administering the distribution`; `s 2013(b)(2) the party that administers the distribution` |
| C019 | 174-175 | s 2013(b)(2)(C) [headings: (C) Prohibition] | encoded | `s 2013(b)(2)(C) the Secretary may approve the plan` |
| C020 | 176-177 | s 2013(b)(3) [headings: (3) Disqualified participants] | encoded | `s 2013(b)(3) the period for which the individual is not eligible to participate in the supplemental nutrition assistance program`; `s 2013(b)(3) the individual is not eligible to participate in the supplemental nutrition assistance program` |
| C021 | 178-180 | s 2013(b)(4)(A) [headings: (4) Administrative costs; (A) In general] | encoded | `s 2013(b)(4)(A) the least amount the Secretary must pay` |
| C022 | 181-182 | s 2013(b)(4)(B) [headings: (B) Waiver] | encoded | `s 2013(b)(4)(B) the Secretary must waive the non-Federal share of the costs` |
| C023 | 183 | s 2013(b)(4)(B)(i) | encoded | `s 2013(b)(4)(B) the Secretary must waive the non-Federal share of the costs` |
| C024 | 184 | s 2013(b)(4)(B)(ii) | encoded | `s 2013(b)(4)(B) the Secretary must waive the non-Federal share of the costs` |
| C025 | 185-186 | s 2013(b)(4)(C) [headings: (C) Limitation] | encoded | `s 2013(b)(4)(C) the Secretary may reduce the benefits or services to the tribal organization` |
| C026 | 187-188 | s 2013(b)(4)(D) [headings: (D) Tribal contribution] | encoded | `s 2013(b)(4)(D) the Secretary may allow the tribal organization to use the funds to satisfy the non-Federal share` |
| C027 | 189-190 | s 2013(b)(5) [headings: (5) Bison meat] | encoded | `s 2013(b)(5) the Secretary may purchase the bison meat` |
| C028 | 191 | s 2013(b)(5)(A) | encoded | `s 2013(b)(5) the Secretary may purchase the bison meat` |
| C029 | 192 | s 2013(b)(5)(B) | encoded | `s 2013(b)(5) the Secretary may purchase the bison meat` |
| C030 | 193-195 | s 2013(b)(6)(A) [headings: (6) Traditional and locally- and regionally-grown food fund; (A) In general] | encoded | `s 2013(b)(6)(A) the Secretary must establish the fund` |
| C031 | 196-197 | s 2013(b)(6)(B) [headings: (B) Native American producers] | encoded | `s 2013(b)(6)(B) the food provided meets the requirement for Native American producers` |
| C032 | 198-199 | s 2013(b)(6)(C) [headings: (C) Definition of traditional and locally- and regionally-grown] | inert | reason 2: machinery: the Secretary determines the definition of a term for the fund; the text states no rule for anyone until that is done |
| C033 | 200-201 | s 2013(b)(6)(D) [headings: (D) Purchase of foods] | encoded | `s 2013(b)(6)(D) the Secretary must purchase or offer to purchase the food` |
| C034 | 202-203 | s 2013(b)(6)(E) [headings: (E) Authorization of appropriations] | encoded | `s 2013(b)(6)(E) the amount authorized to be appropriated for the fiscal year` |
| C035 | 204-206 | s 2013(b)(7)(A) [headings: (7) Availability of funds; (A) In general] | fork | F-S3; chosen: `s 2013(b)(7)(A) the last fiscal year in which the funds remain available for obligation` |
| C036 | 207-208 | s 2013(b)(7)(B) [headings: (B) Administrative costs] | fork | F-S3; chosen: `s 2013(b)(7)(B) the last fiscal year in which the funds for administrative costs remain available for obligation` |
| C037 | 209-210 | s 2013(c) [headings: (c) Regulations; transmittal of copy of regulations to Congre...] | inert | reason 2: machinery: regulation-making power of the Secretary (section 2013(c)) |
| C038 | 211 | s 2013 source credit | inert | reason 1: source credit: the enactment history of the section, creates no rule |
| C039 | 213-215 | s 2014(a) [headings: § 2014. Eligible households; (a) Income and other financial resources as substantial limit...] | encoded | `s 2014(a) the household may participate in the program`; `s 2014(a) the member receives one of the listed benefits`; `s 2014(a) each member of the household receives one of the listed benefits`; `s 2014(a) the household is eligible because each member receives a listed benefit`; `s 2014(a) the household is eligible because each member receives general assistance`; `s 2014(a) assistance must be furnished to the household` |
| C040 | 215 | s 2014(a), sentences 2-3 | encoded | `s 2014(a) the household may participate in the program`; `s 2014(a) the member receives one of the listed benefits`; `s 2014(a) each member of the household receives one of the listed benefits`; `s 2014(a) the household is eligible because each member receives a listed benefit`; `s 2014(a) the household is eligible because each member receives general assistance` |
| C041 | 215 | s 2014(a), sentence 4 | encoded | `s 2014(a) the household may participate in the program`; `s 2014(a) assistance must be furnished to the household` |
| C042 | 216-217 | s 2014(b) [headings: (b) Eligibility standards] | encoded | `s 2014(b) a standard of eligibility may differ from place to place`; `s 2014(b) the plan of operation may be approved`; `s 2014(b) the State agency may impose the standard` |
| C043 | 218-219 | s 2014(c) [headings: (c) Gross income standard] | fork | F-C1; chosen: `s 2014(c)(1) the poverty line for the household`; `s 2014(c)(1) the household is ineligible because its net income exceeds the poverty line`; `s 2014(c) the household is ineligible on income`; `s 2014(c) the standards are adjusted on the date` |
| C044 | 220 | s 2014(c)(1) | fork | F-C1; chosen: `s 2014(c)(1) the poverty line for the household`; `s 2014(c) the USDA's Table 3 limit for the household`; `s 2014(c)(1) the household is ineligible because its net income exceeds the poverty line`; `s 2014(c) the household is ineligible on income` |
| C045 | 221 | s 2014(c)(2) | fork | F-C1; chosen: `s 2014(c)(2) the gross monthly income limit for the household`; `s 2014(c) the USDA's Table 3 limit for the household`; `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit`; `s 2014(c)(2) the household is ineligible because its gross income exceeds the poverty line by more than 30 per centum`; `s 2014(c) the household is ineligible on income` |
| C046 | 222 | s 2014(c)(2) | encoded | `s 2014(c) the standard of eligibility for Guam or the Virgin Islands after the cap` |
| C047 | 223-224 | s 2014(d) [headings: (d) Exclusions from income] | encoded | `s 2014(d) the item is included in household income`; `s 2014(d) the monthly amount of the item that counts as income`; `s 2014(d) household income` |
| C048 | 225 | s 2014(d)(1) | encoded | `s 2014(d)(1) the item is excluded because it is not money payable directly to a household` |
| C049 | 226 | s 2014(d)(2) | fork | F-D1; chosen: `s 2014(d)(2) the amount excluded in the quarter` |
| C050 | 227-228 | s 2014(d)(3)(A) [headings: (3) all educational loans on which payment is deferred, grant...] | fork | F-D2; chosen: `s 2014(d)(3) the amount excluded` |
| C051 | 229 | s 2014(d)(3)(B) | fork | F-D2; chosen: `s 2014(d)(3) the amount excluded` |
| C052 | 230 | s 2014(d)(3)(C) | fork | F-D2; chosen: `s 2014(d)(3) the amount excluded` |
| C053 | 231 | s 2014(d)(4) | encoded | `s 2014(d)(4) the loan is excluded` |
| C054 | 232 | s 2014(d)(5) | encoded | `s 2014(d)(5) the item is excluded as a reimbursement or a school allowance` |
| C055 | 233 | s 2014(d)(6) | encoded | `s 2014(d)(6) the item is excluded as care and maintenance of a third party or child support paid out` |
| C056 | 234 | s 2014(d)(7) | encoded | `s 2014(d)(7) the child's earned income is excluded` |
| C057 | 235 | s 2014(d)(8) | fork | F-D1; chosen: `s 2014(d)(8) the cash donation excluded in the quarter`; `s 2014(d)(8) the lump-sum payment is excluded from income`; `s 2014(d)(8) the excluded payment is counted as a resource` |
| C058 | 236 | s 2014(d)(9) | encoded | `s 2014(d)(9) the cost of producing self-employed income that is excluded`; `s 2014(d)(9) the reduction of the other income that is included` |
| C059 | 237 | s 2014(d)(10) | encoded | `s 2014(d)(10) the income is excluded because another Federal law excludes it` |
| C060 | 238-239 | s 2014(d)(11)(A) [headings: (11)] | encoded | `s 2014(d)(11) the payment or allowance is excluded` |
| C061 | 240 | s 2014(d)(11)(B) | encoded | `s 2014(d)(11) the payment or allowance is excluded` |
| C062 | 241 | s 2014(d)(12) | encoded | `s 2014(d)(12) the cost-of-living increase is excluded on the date` |
| C063 | 242 | s 2014(d)(13) | encoded | `s 2014(d)(13) the advance earned income credit payment is excluded` |
| C064 | 243 | s 2014(d)(14) | encoded | `s 2014(d)(14) the payment for work related expenses or dependent care is excluded` |
| C065 | 244 | s 2014(d)(15) | encoded | `s 2014(d)(15) the amount for a plan for achieving self-support is excluded` |
| C066 | 245 | s 2014(d)(16) | encoded | `s 2014(d)(16) the educational award is excluded at the option of the State agency` |
| C067 | 246 | s 2014(d)(17) | encoded | `s 2014(d)(17) the State complementary assistance payment is excluded at the option of the State agency` |
| C068 | 247 | s 2014(d)(18) | encoded | `s 2014(d)(18) the income is excluded at the option of the State agency` |
| C069 | 248 | s 2014(d)(19) | encoded | `s 2014(d)(19) the combat pay is excluded` |
| C070 | 249 | s 2014(d)(19)(A) | encoded | `s 2014(d)(19) the combat pay is excluded` |
| C071 | 250 | s 2014(d)(19)(B) | encoded | `s 2014(d)(19) the combat pay is excluded` |
| C072 | 251-255 | s 2014(e)(1)(A)(i) [headings: (e) Deductions from income; (1) Standard deduction; (A) In general; (i) Deduction] | encoded | `s 2014(e)(1)(A) the standard deduction`; `s 2014(e)(1) the standard deduction for the household` |
| C073 | 256 | s 2014(e)(1)(A)(i)(I) | encoded | `s 2014(e)(1)(A) the standard deduction` |
| C074 | 257 | s 2014(e)(1)(A)(i)(II) | encoded | `s 2014(e)(1)(A) the standard deduction` |
| C075 | 258-259 | s 2014(e)(1)(A)(ii) [headings: (ii) Minimum amount] | encoded | `s 2014(e)(1)(A) the standard deduction`; `s 2014(e)(1)(A)(ii)(I) the minimum standard deduction for fiscal year 2009` |
| C076 | 260 | s 2014(e)(1)(A)(ii)(I) | encoded | `s 2014(e)(1)(A) the standard deduction`; `s 2014(e)(1)(A)(ii)(I) the minimum standard deduction for fiscal year 2009` |
| C077 | 261 | s 2014(e)(1)(A)(ii)(II) | encoded | `s 2014(e)(1)(A) the standard deduction`; `s 2014(e)(1)(A)(ii)(II) the minimum standard deduction after indexing` |
| C078 | 262-264 | s 2014(e)(1)(B)(i) [headings: (B) Guam; (i) In general] | encoded | `s 2014(e)(1)(B) the standard deduction for Guam` |
| C079 | 265 | s 2014(e)(1)(B)(i)(I) | encoded | `s 2014(e)(1)(B) the standard deduction for Guam` |
| C080 | 266 | s 2014(e)(1)(B)(i)(II) | encoded | `s 2014(e)(1)(B) the standard deduction for Guam` |
| C081 | 267-268 | s 2014(e)(1)(B)(ii) [headings: (ii) Minimum amount] | encoded | `s 2014(e)(1)(B) the standard deduction for Guam`; `s 2014(e)(1)(B)(ii)(I) the minimum standard deduction for Guam for fiscal year 2009` |
| C082 | 269 | s 2014(e)(1)(B)(ii)(I) | encoded | `s 2014(e)(1)(B) the standard deduction for Guam`; `s 2014(e)(1)(B)(ii)(I) the minimum standard deduction for Guam for fiscal year 2009` |
| C083 | 270 | s 2014(e)(1)(B)(ii)(II) | encoded | `s 2014(e)(1)(B) the standard deduction for Guam`; `s 2014(e)(1)(B)(ii)(II) the Guam minimum standard deduction after indexing` |
| C084 | 271-272 | s 2014(e)(1)(C) [headings: (C) Requirement] | encoded | `s 2014(e)(1)(C) the adjustment conforms` |
| C085 | 273-275 | s 2014(e)(2)(A) [headings: (2) Earned income deduction; (A) “Earned income” defined] | encoded | `s 2014(e)(2)(A) the earned income` |
| C086 | 276 | s 2014(e)(2)(A)(i) | encoded | `s 2014(e)(2)(A) the earned income` |
| C087 | 277 | s 2014(e)(2)(A)(ii) | encoded | `s 2014(e)(2)(A) the earned income` |
| C088 | 278-279 | s 2014(e)(2)(B) [headings: (B) Deduction] | encoded | `s 2014(e)(2) the household is allowed the earned income deduction`; `s 2014(e)(2)(B) the earned income deduction` |
| C089 | 280-281 | s 2014(e)(2)(C) [headings: (C) Exception] | encoded | `s 2014(e)(2) the household is allowed the earned income deduction` |
| C090 | 282-284 | s 2014(e)(3)(A) [headings: (3) Dependent care deduction; (A) In general] | encoded | `s 2014(e)(3)(A) the household is entitled to the dependent care deduction`; `s 2014(e)(3)(A) the dependent care deduction` |
| C091 | 285-286 | s 2014(e)(3)(B) [headings: (B) Excluded expenses] | encoded | `s 2014(e)(3)(B) the expense is an excluded expense` |
| C092 | 287 | s 2014(e)(3)(B)(i) | encoded | `s 2014(e)(3)(B) the expense is an excluded expense` |
| C093 | 288 | s 2014(e)(3)(B)(ii) | encoded | `s 2014(e)(3)(B) the expense is an excluded expense` |
| C094 | 289 | s 2014(e)(3)(B)(iii) | encoded | `s 2014(e)(3)(B) the expense is an excluded expense` |
| C095 | 290-292 | s 2014(e)(4)(A) [headings: (4) Deduction for child support payments; (A) In general] | encoded | `s 2014(e)(4)(A) the child support deduction` |
| C096 | 293-294 | s 2014(e)(4)(B) [headings: (B) Order of determining deductions] | encoded | `s 2014(e)(4)(B) the order of the computations conforms` |
| C097 | 295-297 | s 2014(e)(5)(A) [headings: (5) Excess medical expense deduction; (A) In general] | encoded | `s 2014(e)(5)(A) the household is entitled to the excess medical expense deduction`; `s 2014(e)(5)(A) the excess medical expense deduction` |
| C098 | 298-300 | s 2014(e)(5)(B)(i) [headings: (B) Method of claiming deduction; (i) In general] | encoded | `s 2014(e)(5)(B)(i) the State agency must offer the method of claiming recurring medical expenses` |
| C099 | 301-302 | s 2014(e)(5)(B)(ii) [headings: (ii) Method] | encoded | `s 2014(e)(5)(B)(ii) the method conforms` |
| C100 | 303 | s 2014(e)(5)(B)(ii)(I) | encoded | `s 2014(e)(5)(B)(ii) the method conforms` |
| C101 | 304 | s 2014(e)(5)(B)(ii)(II) | encoded | `s 2014(e)(5)(B)(ii) the method conforms` |
| C102 | 305 | s 2014(e)(5)(B)(ii)(III) | encoded | `s 2014(e)(5)(B)(ii) the method conforms`; `s 2014(e)(5)(B)(ii)(III) further reporting or verification of the change may be required` |
| C103 | 306-307 | s 2014(e)(5)(C) [headings: (C) Exclusion of medical marijuana] | encoded | `s 2014(e)(5)(C) the expense is treated as a medical expense` |
| C104 | 308-310 | s 2014(e)(6)(A) [headings: (6) Excess shelter expense deduction; (A) In general] | fork | F-E2; chosen: `s 2014(e)(6)(A) the excess shelter expense deduction before the maximum`; `s 2014(e)(6) the excess shelter expense deduction`; `s 2014(e) the household's net income` |
| C105 | 311-312 | s 2014(e)(6)(B) [headings: (B) Maximum amount of deduction] | encoded | `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6) the excess shelter expense deduction` |
| C106 | 313 | s 2014(e)(6)(B)(i) | encoded | `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6) the excess shelter expense deduction` |
| C107 | 314 | s 2014(e)(6)(B)(ii) | encoded | `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6) the excess shelter expense deduction` |
| C108 | 315 | s 2014(e)(6)(B)(iii) | encoded | `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6) the excess shelter expense deduction` |
| C109 | 316 | s 2014(e)(6)(B)(iv) | encoded | `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6) the excess shelter expense deduction` |
| C110 | 317 | s 2014(e)(6)(B)(v) | encoded | `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6) the excess shelter expense deduction` |
| C111 | 318 | s 2014(e)(6)(B)(vi) | encoded | `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6)(B)(vi) the maximum after indexing`; `s 2014(e)(6) the excess shelter expense deduction` |
| C112 | 319-321 | s 2014(e)(6)(C)(i) [headings: (C) Standard utility allowance; (i) In general] | encoded | `s 2014(e)(6)(C)(i) the State agency may use the standard utility allowance` (words of the sentence no quotation carries: "in computing the excess shelter expense deduction") |
| C113 | 322-323 | s 2014(e)(6)(C)(ii) [headings: (ii) Restrictions on heating and cooling expenses] | encoded | `s 2014(e)(6)(C)(ii) an allowance for a heating or cooling expense may be used` |
| C114 | 324 | s 2014(e)(6)(C)(ii)(I) | encoded | `s 2014(e)(6)(C)(ii) an allowance for a heating or cooling expense may be used` |
| C115 | 325 | s 2014(e)(6)(C)(ii)(II) | encoded | `s 2014(e)(6)(C)(ii) an allowance for a heating or cooling expense may be used` |
| C116 | 326 | s 2014(e)(6)(C)(ii)(III) | encoded | `s 2014(e)(6)(C)(ii) an allowance for a heating or cooling expense may be used` |
| C117 | 327-329 | s 2014(e)(6)(C)(iii)(I) [headings: (iii) Mandatory allowance; (I) In general] | encoded | `s 2014(e)(6)(C)(iii)(I) the State agency may make the use of a standard utility allowance mandatory` |
| C118 | 330 | s 2014(e)(6)(C)(iii)(I)(aa) | encoded | `s 2014(e)(6)(C)(iii)(I) the State agency may make the use of a standard utility allowance mandatory` |
| C119 | 331 | s 2014(e)(6)(C)(iii)(I)(bb) | encoded | `s 2014(e)(6)(C)(iii)(I) the State agency may make the use of a standard utility allowance mandatory` |
| C120 | 332-333 | s 2014(e)(6)(C)(iii)(II) [headings: (II) Household election] | encoded | `s 2014(e)(6)(C)(iii)(II) the household may switch between the standard utility allowance and actual utility costs` |
| C121 | 334-335 | s 2014(e)(6)(C)(iii)(III) [headings: (III) Inapplicability of certain restrictions] | encoded | `s 2014(e)(6)(C)(ii) an allowance for a heating or cooling expense may be used` |
| C122 | 336-338 | s 2014(e)(6)(C)(iv)(I) [headings: (iv) Availability of allowance to recipients of energy assistance; (I) In general] | encoded | `s 2014(e)(6)(C)(iv)(I) the standard utility allowance must be made available to the household` (words of the sentence no quotation carries: "subject to subclause ii") |
| C123 | 339-340 | s 2014(e)(6)(C)(iv)(II) [headings: (II) Separate allowance] | encoded | `s 2014(e)(6)(C)(iv)(II) the State agency may be required to use a separate standard utility allowance` |
| C124 | 341-342 | s 2014(e)(6)(C)(iv)(III) [headings: (III) States not electing to use separate allowance] | encoded | `s 2014(e)(6)(C)(iv)(III) the State agency may be required to reduce the allowance` (words of the sentence no quotation carries: "42 u s c 8621 et seq") |
| C125 | 343-344 | s 2014(e)(6)(C)(iv)(IV) [headings: (IV) Proration of assistance] | encoded | `s 2014(e)(6)(C)(iv)(IV) the monthly amount of the energy assistance prorated over the season` (words of the sentence no quotation carries: "for the purpose of the supplemental nutrition assistance program") |
| C126 | 345-347 | s 2014(e)(6)(D)(i) [headings: (D) Homeless households; (i) Alternative deduction] | encoded | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction`; `s 2014(e)(6)(D) the homeless shelter deduction for the fiscal year` |
| C127 | 348 | s 2014(e)(6)(D)(i)(I) | encoded | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction` |
| C128 | 349 | s 2014(e)(6)(D)(i)(II) | encoded | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction` |
| C129 | 350 | s 2014(e)(6)(D)(i)(III) | encoded | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction` |
| C130 | 351-352 | s 2014(e)(6)(D)(ii) [headings: (ii) Adjustment] | encoded | `s 2014(e)(6)(D)(ii) the adjusted homeless shelter deduction` |
| C131 | 353-354 | s 2014(e)(6)(D)(iii) [headings: (iii) Ineligibility] | encoded | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction` |
| C132 | 355-356 | s 2014(e)(6)(E) [headings: (E) Restrictions on internet expenses] | encoded | `s 2014(e)(6)(E) the expense is used in computing the excess shelter expense deduction` |
| C133 | 357-359 | s 2014(f)(1)(A) [headings: (f) Calculation of household income; prospective or retrospec...; (1)] | encoded | `s 2014(f)(1)(A) the household income is averaged over a twelve-month period`; `s 2014(f)(1)(A) the monthly income when averaged over a twelve-month period`; `s 2014(f)(1)(A) the farming income and expenses may be averaged over a 12-month period`; `s 2014(f)(1)(A) the monthly expenses when averaged over a 12-month period` |
| C134 | 359 | s 2014(f)(1)(A), sentence 2 | encoded | `s 2014(f)(1)(A) the household income is averaged over a twelve-month period`; `s 2014(f)(1)(A) the monthly income when averaged over a twelve-month period`; `s 2014(f)(1)(A) the farming income and expenses may be averaged over a 12-month period`; `s 2014(f)(1)(A) the monthly expenses when averaged over a 12-month period`; `s 2014(f)(1)(A) the State agency must calculate the self-employment income on anticipated earnings` |
| C135 | 359 | s 2014(f)(1)(A), sentence 3 | encoded | `s 2014(f)(1)(A) the monthly income when averaged over a twelve-month period`; `s 2014(f)(1)(A) the farming income and expenses may be averaged over a 12-month period`; `s 2014(f)(1)(A) the State agency must calculate the self-employment income on anticipated earnings` |
| C136 | 360 | s 2014(f)(1)(B) | encoded | `s 2014(f)(1)(B) the household income is averaged over the period for which it is received`; `s 2014(f)(1)(B) the monthly income when averaged over the period for which it is received` |
| C137 | 361-363 | s 2014(f)(1)(C)(i) [headings: (C) Simplified determination of deductions.—; (i) In general.—] | encoded | `s 2014(f)(1)(C) the State agency may disregard the change until the next recertification` |
| C138 | 364-365 | s 2014(f)(1)(C)(ii) [headings: (ii) Changes that may not be disregarded.—] | encoded | `s 2014(f)(1)(C) the State agency may disregard the change until the next recertification` |
| C139 | 366 | s 2014(f)(1)(C)(ii)(I) | encoded | `s 2014(f)(1)(C) the State agency may disregard the change until the next recertification` |
| C140 | 367 | s 2014(f)(1)(C)(ii)(II) | encoded | `s 2014(f)(1)(C) the State agency may disregard the change until the next recertification` |
| C141 | 368-369 | s 2014(f)(2)(A) [headings: (2)] | encoded | `s 2014(f)(2) the basis on which the household's income is calculated` |
| C142 | 370 | s 2014(f)(2)(B) | encoded | `s 2014(f)(2) the basis on which the household's income is calculated` |
| C143 | 371 | s 2014(f)(2)(C) | encoded | `s 2014(f)(2) the basis on which the household's income is calculated` |
| C144 | 372 | s 2014(f)(2)(D) | encoded | `s 2014(f)(2) the basis on which the household's income is calculated` |
| C145 | 373-374 | s 2014(f)(3)(A) [headings: (3)] | encoded | `s 2014(f)(3)(A) the figures the prospective calculation takes into account` |
| C146 | 375 | s 2014(f)(3)(B), sentence 1 | encoded | `s 2014(f)(3)(B) the income calculated on a retrospective basis`; `s 2014(f)(3)(B) the initial allotment must be supplemented` |
| C147 | 375 | s 2014(f)(3)(B), sentences 2-3 | encoded | `s 2014(f)(3)(B) the initial allotment must be supplemented` |
| C148 | 376 | s 2014(f)(4), sentence 1 | inert | reason 2: machinery: the Secretary consults the Secretary of Health and Human Services when promulgating regulations |
| C149 | 376 | s 2014(f)(4), sentence 2 | encoded | `s 2014(f)(4) the Secretary may waive the provision` |
| C150 | 377-380 | s 2014(g)(1)(A) [headings: (g) Allowable financial resources; (1) Total amount.—; (A) In general.—] | fork | F-G1; chosen: `s 2014(g)(1)(A) the resources exceed the limit`; `s 2014(g)(1)(A) the household is ineligible because its resources exceed the limit`; `s 2014(g)(1) the resource limit for the household`; `s 2014(g)(1) the value of the resource that is shown to count`; `s 2014(g)(1) the value of the resource that may count` |
| C151 | 381-383 | s 2014(g)(1)(B)(i) [headings: (B) Adjustment for inflation.—; (i) In general.—] | encoded | `s 2014(g)(1)(B)(i) the adjusted amount before rounding`; `s 2014(g)(1)(B)(i) the adjusted amount rounded down to the nearest $250 increment` |
| C152 | 384-385 | s 2014(g)(1)(B)(ii) [headings: (ii) Requirement.—] | encoded | `s 2014(g)(1)(B)(ii) the adjustment conforms` |
| C153 | 386-388 | s 2014(g)(2)(A) [headings: (2) Included assets.—; (A) In general.—] | encoded | `s 2014(g)(2)(A) the resource is included in financial resources by the regulations in force as of June 1, 1982` |
| C154 | 389-390 | s 2014(g)(2)(B) [headings: (B) Additional included assets.—] | encoded | `s 2014(g)(2)(B)(i) the resource is included in financial resources`; `s 2014(g)(2)(B)(ii) the resource is included in financial resources`; `s 2014(g)(2)(B)(iii) the resource is included in financial resources`; `s 2014(g)(2)(B)(iv) the value of the vehicle that counts as a resource`; `s 2014(g)(2)(B)(v) the resource is included in financial resources` (chapeau of the list that follows: its limbs are the rows below) |
| C155 | 391 | s 2014(g)(2)(B)(i) | encoded | `s 2014(g)(2)(B)(i) the resource is included in financial resources` |
| C156 | 392 | s 2014(g)(2)(B)(ii) | encoded | `s 2014(g)(2)(B)(ii) the resource is included in financial resources` |
| C157 | 393 | s 2014(g)(2)(B)(iii) | encoded | `s 2014(g)(2)(B)(iii) the resource is included in financial resources` |
| C158 | 394 | s 2014(g)(2)(B)(iv) | encoded | `s 2014(g)(2)(B)(iv) the value of the vehicle that counts as a resource` |
| C159 | 395 | s 2014(g)(2)(B)(v) | fork | F-G1; chosen: `s 2014(g)(2)(B)(v) the resource is included in financial resources` |
| C160 | 396-397 | s 2014(g)(2)(C) [headings: (C) Excluded vehicles.—] | encoded | `s 2014(g)(2)(C) the vehicle is included in financial resources under paragraph (2)`; `s 2014(g)(2)(C) the property related to the vehicle is included in financial resources under paragraph (2)` |
| C161 | 398 | s 2014(g)(2)(C)(i) | encoded | `s 2014(g)(2)(C) the vehicle is included in financial resources under paragraph (2)` |
| C162 | 399 | s 2014(g)(2)(C)(ii) | encoded | `s 2014(g)(2)(C) the vehicle is included in financial resources under paragraph (2)` |
| C163 | 400 | s 2014(g)(2)(C)(iii) | encoded | `s 2014(g)(2)(C) the vehicle is included in financial resources under paragraph (2)` |
| C164 | 401-402 | s 2014(g)(2)(D) [headings: (D) Alternative vehicle allowance.—] | encoded | `s 2014(g)(2)(D) the State agency may apply the State vehicle allowance standards to the household` |
| C165 | 403 | s 2014(g)(3), sentence 1 | encoded | `s 2014(g)(3) the burial plot is excluded from financial resources`; `s 2014(g)(3) the nonliquid resource for the plan is excluded from financial resources`; `s 2014(g)(3) the earned income tax credit is excluded from financial resources` |
| C166 | 403 | s 2014(g)(3), sentence 2 | encoded | `s 2014(g)(3) the burial plot is excluded from financial resources`; `s 2014(g)(3) the earned income tax credit is excluded from financial resources` |
| C167 | 404 | s 2014(g)(4) | encoded | `s 2014(g)(4) the farm property is excluded from financial resources` |
| C168 | 405 | s 2014(g)(5), sentences 1-3 | encoded | `s 2014(g)(5) the resource is excluded as an inaccessible resource`; `s 2014(g)(5) the Secretary may require the State agency to require verification of the value of the resource` |
| C169 | 405 | s 2014(g)(5), sentence 4 | encoded | `s 2014(g)(5) the Secretary may require the State agency to require verification of the value of the resource` |
| C170 | 406-408 | s 2014(g)(6)(A) [headings: (6) Exclusion of types of financial resources not considered ...; (A) In general.—] | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C171 | 409 | s 2014(g)(6)(A)(i) | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C172 | 410 | s 2014(g)(6)(A)(ii) | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C173 | 411-412 | s 2014(g)(6)(B) [headings: (B) Limitations.—] | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C174 | 413 | s 2014(g)(6)(B)(i) | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C175 | 414 | s 2014(g)(6)(B)(ii) | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C176 | 415 | s 2014(g)(6)(B)(iii) | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C177 | 416 | s 2014(g)(6)(B)(iv) | encoded | `s 2014(g)(6) the State agency may exclude the type of resource` |
| C178 | 417-419 | s 2014(g)(7)(A) [headings: (7) Exclusion of retirement accounts from allowable financial...; (A) Mandatory exclusions.—] | fork | F-G1; chosen: `s 2014(g)(7)(A) the retirement funds are excluded from financial resources` |
| C179 | 420 | s 2014(g)(7)(A)(i) | fork | F-G1; chosen: `s 2014(g)(7)(A) the retirement funds are excluded from financial resources` |
| C180 | 421 | s 2014(g)(7)(A)(ii) | fork | F-G1; chosen: `s 2014(g)(7)(A) the retirement funds are excluded from financial resources` |
| C181 | 422-423 | s 2014(g)(7)(B) [headings: (B) Discretionary exclusions.—] | fork | F-G1; chosen: `s 2014(g)(7)(B) the Secretary may exclude the retirement plan, contract, or account` |
| C182 | 424-426 | s 2014(g)(8)(A) [headings: (8) Exclusion of education accounts from allowable financial ...; (A) Mandatory exclusions.—] | encoded | `s 2014(g)(8)(A) the education funds are excluded from financial resources` |
| C183 | 427-428 | s 2014(g)(8)(B) [headings: (B) Discretionary exclusions.—] | encoded | `s 2014(g)(8)(B) the Secretary may exclude the education program, contract, or account` |
| C184 | 429-430 | s 2014(h)(1) [headings: (h) Temporary emergency standards of eligibility; Disaster Ta...] | encoded | `s 2014(h)(1) the Secretary must establish temporary emergency standards of eligibility for the household` |
| C185 | 430 | s 2014(h)(1), sentence 2 | inert | reason 2: machinery: rule-making procedure (emergency standards may be promulgated without regard to section 2013(c) or 553 of title 5) |
| C186 | 431-432 | s 2014(h)(2)(A) [headings: (2) The Secretary shall—] | inert | reason 2: machinery: the Secretary establishes a Disaster Task Force (an office and its work) |
| C187 | 433 | s 2014(h)(2)(B) | inert | reason 2: machinery: the Secretary may send members of the Task Force to a State (an office and its staffing) |
| C188 | 434-435 | s 2014(h)(3)(A) [headings: (3)] | encoded | `s 2014(h)(3)(A) the household is provided an emergency allotment to replace food destroyed in a disaster`; `s 2014(h)(3)(A) the value of the food replaced` |
| C189 | 436 | s 2014(h)(3)(B), sentences 1-2 | encoded | `s 2014(h)(3)(B) the factors the Secretary must consider`; `s 2014(h)(3)(B) the Secretary must adjust the issuance methods and the reporting and other application requirements for the household` |
| C190 | 437-438 | s 2014(i)(1) [headings: (i) Attribution of income and resources to sponsored aliens; ...] | encoded | `s 2014(i)(1) the income and resources of the sponsor are deemed to be the income and resources of the individual`; `s 2014(i)(1) the deemed income as an item of the individual's income` |
| C191 | 439-440 | s 2014(i)(2)(A) [headings: (2)] | fork | F-I1; chosen: `s 2014(i)(2)(A) the monthly income attributed to the alien` |
| C192 | 441 | s 2014(i)(2)(A)(i) | fork | F-I1; chosen: `s 2014(i)(2)(A) the monthly income attributed to the alien` |
| C193 | 442 | s 2014(i)(2)(A)(ii) | fork | F-I1; chosen: `s 2014(i)(2)(A) the monthly income attributed to the alien`; `s 2014(i)(2)(A)(ii) the size of the sponsor's household` |
| C194 | 443 | s 2014(i)(2)(A)(iii) | fork | F-I1; chosen: `s 2014(i)(2)(A) the monthly income attributed to the alien` |
| C195 | 444 | s 2014(i)(2)(B) | encoded | `s 2014(i)(2)(B) the resources deemed to be the alien's resources` |
| C196 | 445 | s 2014(i)(2)(B)(i) | encoded | `s 2014(i)(2)(B) the resources deemed to be the alien's resources` |
| C197 | 446 | s 2014(i)(2)(B)(ii) | encoded | `s 2014(i)(2)(B) the resources deemed to be the alien's resources` |
| C198 | 447 | s 2014(i)(2)(B)(iii) | encoded | `s 2014(i)(2)(B) the resources deemed to be the alien's resources`; `s 2014(i)(2)(B)(iii) the resources of the alien with the resources deemed` |
| C199 | 448-449 | s 2014(i)(2)(C)(i) [headings: (C)] | fork | F-I2; chosen: `s 2014(i)(2)(C)(i) the alien is barred from being an eligible individual or eligible spouse for not providing the information`; `s 2014(i)(2)(C)(i) the alien is required to provide the information and documentation given in support of the immigration application` |
| C200 | 450 | s 2014(i)(2)(C)(ii) | inert | reason 2: machinery: agreements between the Secretary and the Secretary of State and the Attorney General about sharing information |
| C201 | 451 | s 2014(i)(2)(D), sentences 1-2 | encoded | `s 2014(i)(2)(D) the sponsor and the alien are jointly and severally liable for the overpayment`; `s 2014(i)(2)(D) the amount for which the sponsor and the alien are each liable`; `s 2014(i)(2)(D) the overpayment is to be recovered in accordance with section 2022(b)` |
| C202 | 452 | s 2014(i)(2)(E) | encoded | `s 2014(i)(2)(E) the subsection applies to the alien` |
| C203 | 453-454 | s 2014(j) [headings: (j) Resource exemption for otherwise exempt households] | encoded | `s 2014(j) the member is considered to have satisfied the resource limitations of subsection (g)` |
| C204 | 455-456 | s 2014(k)(1) [headings: (k) Assistance to third parties included; educational benefit...] | fork | F-K1; chosen: `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household` |
| C205 | 457 | s 2014(k)(1)(A) | fork | F-K1; chosen: `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household` |
| C206 | 458-459 | s 2014(k)(1)(B)(i) [headings: (B) a benefit payable to the household for housing expenses u...] | fork | F-K1; chosen: `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household` |
| C207 | 460 | s 2014(k)(1)(B)(ii) | fork | F-K1; chosen: `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household` |
| C208 | 461-462 | s 2014(k)(2)(A) [headings: (2) Paragraph (1) shall not apply to—] | fork | F-K1; chosen: `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| C209 | 463 | s 2014(k)(2)(B) | fork | F-K1; chosen: `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| C210 | 464 | s 2014(k)(2)(C) | fork | F-K1; chosen: `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| C211 | 465 | s 2014(k)(2)(D) | fork | F-K1; chosen: `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| C212 | 466 | s 2014(k)(2)(E) | fork | F-K1; chosen: `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| C213 | 467 | s 2014(k)(2)(F) | fork | F-K1; chosen: `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| C214 | 468 | s 2014(k)(2)(G) | fork | F-K1; chosen: `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| C215 | 469 | s 2014(k)(3) | encoded | `s 2014(k)(3) the educational assistance is treated as money payable directly to the household` |
| C216 | 470-472 | s 2014(k)(4)(A) [headings: (4) Third party energy assistance payments.—; (A) Energy assistance payments.—] | encoded | `s 2014(k)(4)(A) the energy assistance payment is considered money payable directly to the household` |
| C217 | 473-474 | s 2014(k)(4)(B) [headings: (B) Energy assistance expenses.—] | encoded | `s 2014(k)(4)(B) the energy assistance expense is considered an out-of-pocket expense incurred and paid by the household` |
| C218 | 475-476 | s 2014(l) [headings: (l) Earnings to participants of on-the-job training programs;...] | encoded | `s 2014(l) the earnings of the individual in on-the-job training are considered earned income` |
| C219 | 477-479 | s 2014(m)(1) [headings: (m) Simplified calculation of income for the self-employed; (1) In general] | encoded | `s 2014(m)(1) the method may be used in lieu of calculating the actual cost of producing self-employment income` (words of the sentence no quotation carries: "not later than 1 year after august 22 1996") |
| C220 | 480-481 | s 2014(m)(2) [headings: (2) Inclusive of all types of income or limited types of income] | encoded | `s 2014(m)(3) the estimate of the method for the type of self-employment income` |
| C221 | 482-483 | s 2014(m)(3) [headings: (3) Differences for different types of income] | encoded | `s 2014(m)(3) the estimate of the method for the type of self-employment income` |
| C222 | 484-485 | s 2014(n) [headings: (n) State options to simplify determination of child support ...] | encoded | `s 2014(n) the State agency may rely on information from the child support agency in lieu of obtaining current information from the household` |
| C223 | 486 | s 2014 source credit | inert | reason 1: source credit: the enactment history of the section, creates no rule |
| C224 | 488-489 | s 2014a [headings: § 2014a. Notice of change in State of residence of certif...] | encoded | `s 2014a the household is required to report that it no longer resides in the State in which it is certified` |
| C225 | 490 | s 2014a source credit | inert | reason 1: source credit: the enactment history of the section, creates no rule |
| C226 | 1341-1345 | s 2018(a)(1)(A) [headings: § 2018. Approval of retail food stores and wholesale food...; (a) Authorization to accept and redeem benefits; (1) Applications.—; (A) In general.—] | encoded | `s 2018(a)(1)(A) the applicant is to be approved under the regulations` |
| C227 | 1346-1347 | s 2018(a)(1)(B) [headings: (B) Factors for consideration.—] | encoded | `s 2018(a)(1)(B) the factors that must be considered among such other factors as may be appropriate` |
| C228 | 1348 | s 2018(a)(1)(B)(i) | encoded | `s 2018(a)(1)(B) the factors that must be considered among such other factors as may be appropriate` |
| C229 | 1349 | s 2018(a)(1)(B)(ii) | encoded | `s 2018(a)(1)(B) the factors that must be considered among such other factors as may be appropriate` |
| C230 | 1350 | s 2018(a)(1)(B)(iii) | encoded | `s 2018(a)(1)(B) the factors that must be considered among such other factors as may be appropriate` |
| C231 | 1351 | s 2018(a)(1)(B)(iv) | encoded | `s 2018(a)(1)(B) the factors that must be considered among such other factors as may be appropriate` |
| C232 | 1352 | s 2018(a)(1)(B)(v) | encoded | `s 2018(a)(1)(B) the factors that must be considered among such other factors as may be appropriate` |
| C233 | 1353-1354 | s 2018(a)(1)(C) [headings: (C) Certificate.—] | encoded | `s 2018(a)(1)(C) the approval is evidenced by the issuance of a certificate of approval`; `s 2018(a)(1)(C) the certificate of approval may be transferred` |
| C234 | 1355-1356 | s 2018(a)(1)(D) [headings: (D) Visit required.—] | encoded | `s 2018(a)(1)(D) the store or concern may be approved to be authorized or reauthorized` |
| C235 | 1357-1358 | s 2018(a)(2)(A) [headings: (2) The Secretary shall issue regulations providing for—] | inert | reason 2: machinery: the Secretary's regulations provide for periodic reauthorization of stores |
| C236 | 1359 | s 2018(a)(2)(B) | inert | reason 2: machinery: the Secretary's regulations provide for periodic notice of the definitions of retail food store and wholesale food concern |
| C237 | 1360-1361 | s 2018(a)(3) [headings: (3) Authorization periods.—] | inert | reason 2: machinery: the Secretary establishes the time periods of authorization; the text states none |
| C238 | 1362-1363 | s 2018(a)(4) [headings: (4) Electronic benefit transfer equipment and service provide...] | inert | reason 2: machinery: the Secretary issues guidance before implementing clause (iv) of paragraph (1)(B) |
| C239 | 1364-1365 | s 2018(b)(1) [headings: (b) Effective and efficient operation of program; effect of d...] | encoded | `s 2018(b)(1) the wholesale food concern may be authorized to accept and redeem benefits`; `s 2018(b)(1) the co-located wholesale-retail food concern may be authorized to accept and redeem benefits as a retail food store`; `s 2018(b)(1) the firm may be authorized as both a retail food store and a wholesale food concern at the same time` |
| C240 | 1366-1367 | s 2018(b)(2)(A) [headings: (2)] | encoded | `s 2018(b)(2)(A) the buyer or transferee may accept or redeem benefits` |
| C241 | 1368 | s 2018(b)(2)(B) | encoded | `s 2018(b)(2)(B) the buyer or transferee may be required to furnish a bond under section 2021(d)` |
| C242 | 1369-1370 | s 2018(c) [headings: (c) Information submitted by applicants; safeguards; disclosu...] | encoded | `s 2018(c) the information obtained under the subsection may be disclosed to and used by the recipient`; `s 2018(c) the penalty to which the person is liable`; `s 2018(c) the sentence is within the limits the subsection sets` |
| C243 | 1370 | s 2018(c), sentence 2 | encoded | `s 2018(c) the penalty to which the person is liable`; `s 2018(c) the sentence is within the limits the subsection sets` |
| C244 | 1370 | s 2018(c), sentences 3-4 | encoded | `s 2018(c) the information obtained under the subsection may be disclosed to and used by the recipient`; `s 2018(c) the penalty to which the person is liable`; `s 2018(c) the sentence is within the limits the subsection sets` |
| C245 | 1370 | s 2018(c), sentences 5-6 | encoded | `s 2018(c) the penalty to which the person is liable`; `s 2018(c) the sentence is within the limits the subsection sets` |
| C246 | 1371-1372 | s 2018(d) [headings: (d) Hearing upon failure of applicant to receive approval; wa...] | encoded | `s 2018(d) the store or concern may obtain a hearing on the refusal`; `s 2018(d) the store or concern may submit a new application`; `s 2018(d) the longer period bars the new application` |
| C247 | 1373-1374 | s 2018(e) [headings: (e) Reporting of abuses by public] | encoded | `s 2018(e) the approved retail food store has not displayed the sign` |
| C248 | 1375-1376 | s 2018(f) [headings: (f) Limitation on participation of house-to-house trade routes] | encoded | `s 2018(f) the house-to-house trade route may participate` |
| C249 | 1377-1378 | s 2018(g) [headings: (g) EBT service requirement] | encoded | `s 2018(g) the approved retail food store has not provided the adequate EBT service` |
| C250 | 1379-1381 | s 2018(h)(1) [headings: (h) Private establishments; (1) In general] | encoded | `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits`; `s 2018(h) permitted under section 2018(h)` |
| C251 | 1382-1384 | s 2018(h)(2)(A) [headings: (2) Existing contracts; (A) In general] | fork | F-H1; chosen: `s 2018(h)(2)(A) the operation of the private establishment may continue without the determination of need` |
| C252 | 1385-1386 | s 2018(h)(2)(B) [headings: (B) Justification] | encoded | `s 2018(h)(2)(B) the Secretary must provide justification to the State for the termination` |
| C253 | 1387-1388 | s 2018(h)(3) [headings: (3) Report to Congress] | encoded | `s 2018(h)(3) the date the report is due`; `s 2018(h)(3) the report was submitted not later than the date it was due` |
| C254 | 1389-1391 | s 2018(i)(1) [headings: (i) Review of program operations; (1) Review by the Secretary] | encoded | `s 2018(i)(1)(A) the Secretary must review the facility`; `s 2018(i)(1)(B) the Secretary may review the program or arrangement`; `s 2018(i)(1)(C) the facility, program or arrangement must submit the information`; `s 2018(i)(1)(D) the results of the reviews were reported not later than 18 months after December 20, 2018`; `s 2018(i)(1)(D) the report includes the recommendations` (chapeau of the list that follows: its limbs are the rows below) |
| C255 | 1392 | s 2018(i)(1)(A) | encoded | `s 2018(i)(1)(A) the Secretary must review the facility` |
| C256 | 1393 | s 2018(i)(1)(B) | encoded | `s 2018(i)(1)(B) the Secretary may review the program or arrangement` |
| C257 | 1394 | s 2018(i)(1)(C) | encoded | `s 2018(i)(1)(C) the facility, program or arrangement must submit the information` |
| C258 | 1395 | s 2018(i)(1)(D) | encoded | `s 2018(i)(1)(D) the results of the reviews were reported not later than 18 months after December 20, 2018`; `s 2018(i)(1)(D) the report includes the recommendations` |
| C259 | 1396 | s 2018(i)(1)(D)(i) | encoded | `s 2018(i)(1)(D) the report includes the recommendations` |
| C260 | 1397 | s 2018(i)(1)(D)(ii) | encoded | `s 2018(i)(1)(D) the report includes the recommendations` |
| C261 | 1398-1399 | s 2018(i)(2) [headings: (2) Limitation] | fork | F-S2; chosen: `s 2018(i)(2) the subsection authorizes the Secretary to deny the application or request` |
| C262 | 1400-1402 | s 2018(j)(1) [headings: (j) Incentives; (1) Definition of eligible incentive food] | encoded | `s 2018(j)(1) the food is an eligible incentive food` |
| C263 | 1403 | s 2018(j)(1)(A) | encoded | `s 2018(j)(1) the food is an eligible incentive food` |
| C264 | 1404 | s 2018(j)(1)(B) | encoded | `s 2018(j)(1) the food is an eligible incentive food` |
| C265 | 1405-1407 | s 2018(j)(2)(A) [headings: (2) Guidance; (A) In general] | encoded | `s 2018(j)(2)(A) the incentive may be used for the purchase` |
| C266 | 1408-1409 | s 2018(j)(2)(B) [headings: (B) Guidance] | encoded | `s 2018(j)(2)(B) the approved retail food store may carry out the incentive program` |
| C267 | 1410 | s 2018(j)(2)(B)(i) | encoded | `s 2018(j)(2)(B) the approved retail food store may carry out the incentive program` |
| C268 | 1411 | s 2018(j)(2)(B)(ii) | encoded | `s 2018(j)(2)(B) the approved retail food store may carry out the incentive program` |
| C269 | 1412 | s 2018(j)(2)(B)(iii) | encoded | `s 2018(j)(2)(B) the approved retail food store may carry out the incentive program` |
| C270 | 1413-1414 | s 2018(j)(3) [headings: (3) No limitation on benefits] | encoded | `s 2018(j)(3) the waiver may be used to carry out the activity` |
| C271 | 1415-1416 | s 2018(j)(4) [headings: (4) Effect] | encoded | `s 2018(j)(4) the guidance affects the requirement` |
| C272 | 1417-1418 | s 2018(j)(5) [headings: (5) Report] | encoded | `s 2018(j)(5) the Secretary must submit the annual report describing the types of incentives approved` |
| C273 | 1419 | s 2018 source credit | inert | reason 1: source credit: the enactment history of the section, creates no rule |
| C274 | 1421-1422 | s 2019 [headings: § 2019. Redemption of program benefits] | encoded | `s 2019 the channel is one through which benefits accepted by retail food stores are redeemed`; `s 2019 the retail food store is authorized to redeem the members' food benefits before the members receive the food`; `s 2019 the retail food store is authorized to accept benefits before the delivery of the food`; `s 2019 the body may be authorized to redeem benefits through a financial institution`; `s 2019 the financial institution may impose on or collect from the retail food store a fee or other charge for the redemption` |
| C275 | 1422 | s 2019, sentence 2 | encoded | `s 2019 the retail food store is authorized to redeem the members' food benefits before the members receive the food`; `s 2019 the retail food store is authorized to accept benefits before the delivery of the food`; `s 2019 the body may be authorized to redeem benefits through a financial institution` |
| C276 | 1422 | s 2019, sentence 3 | encoded | `s 2019 the channel is one through which benefits accepted by retail food stores are redeemed`; `s 2019 the retail food store is authorized to redeem the members' food benefits before the members receive the food`; `s 2019 the retail food store is authorized to accept benefits before the delivery of the food`; `s 2019 the financial institution may impose on or collect from the retail food store a fee or other charge for the redemption` |
| C277 | 1423 | s 2019 source credit | inert | reason 1: source credit: the enactment history of the section, creates no rule |

## Fork register (snap1)

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives the readings, the text that licenses each, the reading taken (or the explicit "not covered" value), and the rule.
Every fork is assumed, not ruled.
The rows of the coverage table that point at an entry are the rows with the disposition `fork`.

| id | where | readings and the text that licenses each | taken | rule |
| --- | --- | --- | --- | --- |
| F-A1 | s 2012a, line 137 | The section applies "the provisions of subsections (f) and (i) of section 2012 ... concerning private, nonprofit drug addiction or alcohol treatment and rehabilitation programs" to publicly operated community health centers. (1) Read the letters as they stand in this text: (f) is the certification period and (i) the EBT card, which do not concern those programs. (2) Read the letters of 1985, when the definition of those programs may have carried them; the footnote that would say so ("See References in Text note below") is not in the rendering. | Neither can be shown from this text: section 2019, which the sentence names in full, is applied (`JUST TRUE`); the letters (f) and (i) as lettered here return `NOTHING` | `s 2012a the provision is also applicable to the center` |
| F-C1 | s 2014(c), lines 218-221 | "a household shall be ineligible ... if— (1) the household's income (after the exclusions and deductions) exceeds the poverty line ...; and (2) in the case of a household that does not include an elderly or disabled member, the household's income (after the exclusions ... but before the deductions) exceeds such poverty line by more than 30 per centum." (a) "and": both must hold. (b) The two are separate grounds of ineligibility, either suffices. | (b), because limb (2) is limited to households without an elderly or disabled member, so under (a) a household with such a member could meet no test it is subject to; each limb is also a rule of its own, so a caller can compose reading (a) | `s 2014(c) the household is ineligible on income` over `s 2014(c)(1) ...` and `s 2014(c)(2) ...` |
| F-D1 | s 2014(d)(2) and (8), lines 226 and 235 | The $30 and $300 limits are "in a quarter"; an item is received monthly and the Act does not say how a quarterly limit is shared among months. (a) Each month's amount is excluded in the proportion the limit bears to the quarter's amount. (b) The whole limit is used in the first month the item is received. (c) The limit is spread equally over the three months. | (a) | `s 2014(d) the monthly dollars excluded under a quarterly limit`, `s 2014(d)(2) the amount excluded in the quarter`, `s 2014(d)(8) the cash donation excluded in the quarter` |
| F-D2 | s 2014(d)(3), lines 227-230 | Loans, grants and the like are excluded (B) "to the extent that they do not exceed the amount used for or made available as an allowance ..." and (C) "to the extent loans include any origination fees and insurance premiums". (a) Excluded = the least of the award and (allowance + fees and premiums). (b) The award up to the allowance, plus the fees and premiums on top (which can exceed the award). | (a); (b) can exclude more than was awarded | `s 2014(d)(3) the amount excluded` |
| F-E2 | s 2014(e), lines 251-310 | The text allows deductions and does not say that income after them stops at zero. (a) No floor: income after the deductions other than shelter can be negative, and then the shelter excess (shelter costs less half of that income) is larger than the shelter costs. (b) Floor at zero. | (a), the text as written; the effect shows only when income after the other deductions is below zero | `s 2014(e) the household's income after the deductions other than the shelter deduction`, `s 2014(e) the household's net income` |
| F-G1 | s 2014(g)(1), (2)(B)(v), (7), lines 380, 395, 417-423 | A resource can be both on the list of included assets ("any savings account, regardless of whether there is a penalty for early withdrawal") and on a list of excluded ones (retirement accounts, subsection (g)(7)). (a) The exclusion decides (every exclusion paragraph says "shall exclude" or "shall not be included", and (g)(6)(B) speaks of resources "excluded under another paragraph of this subsection"). (b) The inclusion decides ("The Secretary shall include"). | (a) | `s 2014(g)(1) the value of the resource that is shown to count` and `... that may count`, with the inclusion and exclusion paragraphs |
| F-H1 | s 2018(h)(2)(A), line 1384 | The Secretary "shall allow the operation ... to continue without that determination of need for a period not to exceed 180 days from the date on which the Secretary establishes determination criteria". (a) The continuation runs on any day up to 180 days after the criteria date, including days before it (no determination can be made before the criteria exist). (b) It runs only from the criteria date to 180 days after. | (a) | `s 2018(h)(2)(A) the operation of the private establishment may continue without the determination of need` |
| F-I1 | s 2014(i)(2)(A) and (B), lines 440-447 | The sponsor's yearly income less "the income eligibility standard under subsection (c)" for the sponsor's household, and the sponsor's resources less $1,500, are deemed. When the subtraction is below zero: (a) nothing is deemed; (b) the text does not say. The text also does not say which standard of (c), or what "for a year" multiplies. | (b): `NOTHING`; the yearly standard is an input the caller supplies | `s 2014(i)(2)(A) the monthly income attributed to the alien`, `s 2014(i)(2)(B) the resources deemed to be the alien's resources` |
| F-I2 | s 2014(i)(2)(C)(i), line 449 | The first sentence requires information about the sponsor "during the period of three years after entry". The second ("Such alien shall also be required to provide such information and documentation which such alien or the sponsor provided in support of such alien's immigration application as the State agency may request") has no period of its own. (a) The three-year period carries into the second sentence ("also"). (b) It stands alone. | (b): no period is applied; outside the sentence's own words the answer is `NOTHING` | `s 2014(i)(2)(C)(i) the alien is required to provide the information and documentation given in support of the immigration application` |
| F-K1 | s 2014(k)(1) and (2), lines 456-468 | Paragraph (1) applies "except as provided in paragraph (2)", and paragraph (2) names seven classes of assistance, one of which is "emergency and special assistance, to the extent excluded in regulations prescribed by the Secretary". (a) The exceptions are exactly those listed: assistance in none of them is governed by (1) alone. (b) The list is not closed (a regulation may add), so the answer for assistance in none of them is not known. | (a) for the yes: when no class of paragraph (2) applies, paragraph (1) decides; paragraph (2) itself says only `JUST TRUE` or `NOTHING` | `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household`, `s 2014(k)(2) paragraph (1) does not apply to the assistance` |
| F-S1 | s 2013(a)(2)(B)(iii), lines 160-163 | A State whose fiscal year 2025 payment error rate times 1.5 is at least 20 percent has implementation date fiscal year 2029 (subclause (I)); one whose fiscal year 2026 rate is has fiscal year 2030 (subclause (II)). A State that meets both: (a) 2029; (b) 2030; (c) not decided. No sentence ranks the subclauses. | (c): `NOTHING` | `s 2013(a)(2)(B)(iii) the fiscal year in which the implementation date under clause (i) falls` |
| F-S2 | s 2018(i)(2), line 1399 | "Nothing in this subsection shall authorize the Secretary to deny any application ... based on a determination that residents ... are residents of an institution prior to December 31, 2022." (a) The date is the date of the determination, and "prior to" excludes 31 December. (b) The date limits when the residents were residents. (c) 31 December is included. | (a) | `s 2018(i)(2) the subsection authorizes the Secretary to deny the application or request` |
| F-S3 | s 2013(b)(7), lines 206 and 208 | Funds "shall remain available for obligation for a period of 2 fiscal years". (a) The fiscal year of the appropriation and the next. (b) The two fiscal years after it. | (a) | `s 2013(b)(7)(A) the last fiscal year in which the funds remain available for obligation`, `s 2013(b)(7)(B) ...` |

## Jural relations (snap1)

Hohfeld's correlatives: a right (claim) is matched by a duty; a privilege (liberty) by a no-right; a power by a liability; an immunity by a disability.
Each rule is stated once, as a relation between two parties, under a neutral name; no relation is written twice from both sides.
"(not named)" means the text names no one for that side, and none is invented.
The table has 110 rows over the whole of my ranges; 19 of them are `none` (a definition, a counting rule, a figure, a scope rule, an authorization of appropriations, or machinery).
Where a rule gives a relation to one party and its correlative to another in one function (for example `s 2014(e)(6)(C)(iv)(I)`), the row names both, and the function is not written twice.

| provision | holds the right, privilege, power or immunity | bears the duty, no-right, liability or disability | relation | L4 rule |
| --- | --- | --- | --- | --- |
| s 2012a | - | - | none: a scope rule that extends other provisions to publicly operated community health centers (fork F-A1) | `s 2012a the provision is also applicable to the center` |
| s 2013(a)(1), first sentence | an eligible household within a State | the Secretary | claim-duty: an opportunity to obtain a more nutritious diet through an allotment, at the State agency's request, subject to funds | `s 2013(a)(1) the eligible household is provided an opportunity to obtain a more nutritious diet through the issuance of an allotment` |
| s 2013(a)(1), first sentence, the exception | the Secretary | a State | immunity-disability: a State may not participate while the Secretary determines that sales taxes are collected on food bought with benefits | `s 2013(a)(1) the eligible household is provided an opportunity to obtain a more nutritious diet through the issuance of an allotment` |
| s 2013(a)(1), second sentence | (not named) | a household that holds benefits | claim-duty: the benefits are used only to buy food from approved retail food stores | `s 2013(a)(1) the benefits may be used for the purchase` |
| s 2013(a)(1), third sentence | an approved retail food store | the Secretary | claim-duty: redemption of benefits at face value through the Treasury | `s 2013(a)(1) the benefits are redeemable at face value by the Secretary through the facilities of the Treasury` |
| s 2013(a)(2)(A) | - | - | none: a definition (its meaning is in section 2025(c)(2), asked as an input) | `s 2013(a)(2)(A) the payment error rate of the State for the fiscal year` |
| s 2013(a)(2)(B)(i) | the United States (the Federal share) | a State | claim-duty: the State bears the part of the cost of the allotment that its payment error rate fixes | `s 2013(a)(2)(B)(i) the shares of the cost of the allotment for the State in the fiscal year` |
| s 2013(a)(2)(B)(ii)(I) | a State | the Secretary | power-liability: the State elects the rate used for fiscal year 2028 | `s 2013(a)(2)(B)(ii)(I) the payment error rate the State elects to use for fiscal year 2028` |
| s 2013(a)(2)(B)(ii)(II) | the Secretary | a State | power-liability: the Secretary fixes the rate used for fiscal year 2029 and after | `s 2013(a)(2)(B)(ii)(II) the payment error rate the Secretary uses for fiscal year 2029 and each fiscal year thereafter` |
| s 2013(a)(2)(B)(iii) | a State with a high payment error rate | the Secretary | immunity-disability: the shares take effect later (fiscal year 2029 or 2030; fork F-S1) | `s 2013(a)(2)(B)(iii) the fiscal year in which the implementation date under clause (i) falls` |
| s 2013(a)(3) | the United States (the Treasury) | the Secretary | claim-duty: the Secretary may not pay more than the Federal share | `s 2013(a)(3) the Secretary may pay the amount towards the cost of the allotment` |
| s 2013(b)(1) | a tribal organization | (not named) | claim-duty: commodities are distributed whenever it requests concurrent or separate food program operations | `s 2013(b)(1) the distribution of commodities shall be made` |
| s 2013(b)(2)(A) | (not named) | the State agency | claim-duty: responsibility for a distribution on a reservation, unless (B) or (C) displaces it | `s 2013(b)(2) the party that administers the distribution` |
| s 2013(b)(2)(B) | the Secretary | a tribal organization; the State agency | power-liability: the Secretary's finding that a tribal organization is capable of administering the distribution makes the organization, in place of the State agency, administer it | `s 2013(b)(2)(B) the tribal organization is capable of effectively and efficiently administering the distribution` |
| s 2013(b)(2)(C) | (not named) | the Secretary | claim-duty: the Secretary shall not approve a plan that lets a household on a reservation take part in both programs at once | `s 2013(b)(2)(C) the Secretary may approve the plan` |
| s 2013(b)(3) | the Secretary | an individual disqualified from the reservation distribution program | power-liability: ineligibility for SNAP for a period the Secretary determines | `s 2013(b)(3) the individual is not eligible to participate in the supplemental nutrition assistance program`; `s 2013(b)(3) the period for which the individual is not eligible to participate in the supplemental nutrition assistance program` |
| s 2013(b)(4)(A) | a State agency or tribal organization | the Secretary | claim-duty: payment of not less than 80 percent of administrative and distribution costs | `s 2013(b)(4)(A) the least amount the Secretary must pay` |
| s 2013(b)(4)(B) | a tribal organization | the Secretary | claim-duty: waiver of up to 100 percent of the non-Federal share where it is financially unable or the share is a substantial burden | `s 2013(b)(4)(B) the Secretary must waive the non-Federal share of the costs` |
| s 2013(b)(4)(C) | a tribal organization granted a waiver | the Secretary | immunity-disability: no reduction of benefits or services | `s 2013(b)(4)(C) the Secretary may reduce the benefits or services to the tribal organization` |
| s 2013(b)(4)(D) | the Secretary | a tribal organization | power-liability: the Secretary may let it use other Federal funds for the non-Federal share | `s 2013(b)(4)(D) the Secretary may allow the tribal organization to use the funds to satisfy the non-Federal share` |
| s 2013(b)(5) | the Secretary | (not named) | privilege-no-right: the Secretary may purchase bison meat, including from Native American bison producers and producer-owned cooperatives of bison ranchers, subject to appropriations | `s 2013(b)(5) the Secretary may purchase the bison meat` |
| s 2013(b)(6)(A) | (not named) | the Secretary | claim-duty: establish the fund, subject to appropriations | `s 2013(b)(6)(A) the Secretary must establish the fund` |
| s 2013(b)(6)(B) | (not named) | the Secretary | claim-duty: where practicable, at least 50 percent of the food from Native American producers | `s 2013(b)(6)(B) the food provided meets the requirement for Native American producers` |
| s 2013(b)(6)(C) | the Secretary | - | none: the Secretary defines a term (machinery, inert reason 2) | none (inert, reason 2) |
| s 2013(b)(6)(D) | (not named) | the Secretary | claim-duty: purchase or offer to purchase traditional foods that can be procured cost-effectively | `s 2013(b)(6)(D) the Secretary must purchase or offer to purchase the food` |
| s 2013(b)(6)(E) | - | - | none: an authorization of appropriations, which creates no relation between parties | `s 2013(b)(6)(E) the amount authorized to be appropriated for the fiscal year` |
| s 2013(b)(7)(A) and (B) | the Secretary; the State agency or tribal organization | - | privilege-no-right: funds may be obligated for 2 fiscal years (fork F-S3) | `s 2013(b)(7)(A) the last fiscal year in which the funds remain available for obligation`; `s 2013(b)(7)(B) the last fiscal year in which the funds for administrative costs remain available for obligation` |
| s 2013(c) | the Secretary | those regulated | power-liability: the power to make regulations (machinery, inert reason 2) | none (inert, reason 2) |
| s 2014(a), first to third sentences | a household in which each member receives a listed benefit or general assistance | the program (the text names no actor) | claim-duty: the household is eligible to take part | `s 2014(a) the household is eligible because each member receives a listed benefit`; `s 2014(a) the household is eligible because each member receives general assistance` |
| s 2014(a), fourth sentence | an eligible household that applies | the program (the text names no actor) | claim-duty: assistance is furnished | `s 2014(a) assistance must be furnished to the household` |
| s 2014(b), first sentence | (not named) | the Secretary | claim-duty: uniform national standards of eligibility are established | `s 2014(b) a standard of eligibility may differ from place to place` |
| s 2014(b), second sentence | the Secretary | a State agency | immunity-disability: no plan is approved unless its standards meet the Secretary's, and no other standard is imposed | `s 2014(b) the plan of operation may be approved`; `s 2014(b) the State agency may impose the standard` |
| s 2014(c)(1) | (not named) | a household whose net income exceeds the poverty line | privilege-no-right: the household is ineligible (fork F-C1) | `s 2014(c)(1) the household is ineligible because its net income exceeds the poverty line` |
| s 2014(c)(2) | (not named) | a household without an elderly or disabled member whose gross income exceeds 130 percent of the poverty line | privilege-no-right: the household is ineligible (fork F-C1) | `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit`; `s 2014(c)(2) the household is ineligible because its gross income exceeds the poverty line by more than 30 per centum` |
| s 2014(c), the limits and tables | - | - | none: the poverty line and the 130 percent limit are figures (the USDA's FY2027 tables); the adjustment date and the cap for Guam and the Virgin Islands are counting rules | `s 2014(c)(1) the poverty line for the household`; `s 2014(c)(2) the gross monthly income limit for the household`; `s 2014(c) the standard of eligibility for Guam or the Virgin Islands after the cap` |
| s 2014(d), chapeau | a household | (not named) | immunity-disability: only the income the subsection includes is counted | `s 2014(d) the item is included in household income` |
| s 2014(d)(1) | a household | (not named) | immunity-disability: benefits that are not money payable directly to the household are not counted | `s 2014(d)(1) the item is excluded because it is not money payable directly to a household` |
| s 2014(d)(2) | a household | (not named) | immunity-disability: infrequent or irregular income, up to $30 a quarter (fork F-D1) | `s 2014(d)(2) the amount excluded in the quarter` |
| s 2014(d)(3) | a household member enrolled in a qualifying program | (not named) | immunity-disability: educational loans, grants and the like (fork F-D2) | `s 2014(d)(3) the amount excluded` |
| s 2014(d)(4) to (7) | a household | (not named) | immunity-disability: loans, reimbursements, care and maintenance of a third party, a child's earned income are not counted | `s 2014(d)(4) the loan is excluded`; `s 2014(d)(5) the item is excluded as a reimbursement or a school allowance`; `s 2014(d)(6) the item is excluded as care and maintenance of a third party or child support paid out`; `s 2014(d)(7) the child's earned income is excluded` |
| s 2014(d)(8) | a household | (not named) | immunity-disability: nonrecurring lump sums, and cash donations up to $300 a quarter, are not counted (they count as resources) (fork F-D1) | `s 2014(d)(8) the lump-sum payment is excluded from income`; `s 2014(d)(8) the cash donation excluded in the quarter`; `s 2014(d)(8) the excluded payment is counted as a resource` |
| s 2014(d)(9) | a household with self-employment income | (not named) | immunity-disability: the cost of producing the income is not counted | `s 2014(d)(9) the cost of producing self-employed income that is excluded`; `s 2014(d)(9) the reduction of the other income that is included` |
| s 2014(d)(10) to (15) | a household | (not named) | immunity-disability: income another Federal law excludes, energy assistance, cost-of-living increases, advance earned income credit, work-related payments, plan for achieving self-support | `s 2014(d)(10) the income is excluded because another Federal law excludes it`; `s 2014(d)(11) the payment or allowance is excluded`; `s 2014(d)(12) the cost-of-living increase is excluded on the date`; `s 2014(d)(13) the advance earned income credit payment is excluded`; `s 2014(d)(14) the payment for work related expenses or dependent care is excluded`; `s 2014(d)(15) the amount for a plan for achieving self-support is excluded` |
| s 2014(d)(16) to (18) | the State agency | a household | power-liability: the State agency may exclude an educational award, a State complementary assistance payment, or other income by option | `s 2014(d)(16) the educational award is excluded at the option of the State agency`; `s 2014(d)(17) the State complementary assistance payment is excluded at the option of the State agency`; `s 2014(d)(18) the income is excluded at the option of the State agency` |
| s 2014(d)(19) | a household | (not named) | immunity-disability: additional combat pay is not counted | `s 2014(d)(19) the combat pay is excluded` |
| s 2014(d), counting what is left | - | - | none: counting rules that sum the income that counts | `s 2014(d) the monthly dollars excluded under a quarterly limit`; `s 2014(d) the monthly amount of the item that counts as income`; `s 2014(d) household income` |
| s 2014(e)(1)(A) | a household in the 48 States, DC, Alaska, Hawaii or the Virgin Islands | the Secretary | claim-duty: the standard deduction | `s 2014(e)(1)(A) the standard deduction` |
| s 2014(e)(1)(B) | a household in Guam | the Secretary | claim-duty: the standard deduction for Guam | `s 2014(e)(1)(B) the standard deduction for Guam` |
| s 2014(e)(1)(C) | - | - | none: a requirement that the adjustment conform | `s 2014(e)(1)(C) the adjustment conforms` |
| s 2014(e)(2) | a household with earned income | (not named) | claim-duty: the earned income deduction of 20 percent (not in the overissuance case of subparagraph (C)) | `s 2014(e)(2)(A) the earned income`; `s 2014(e)(2) the household is allowed the earned income deduction`; `s 2014(e)(2)(B) the earned income deduction` |
| s 2014(e)(3) | a household that pays for dependent care so a member can work or train | (not named) | claim-duty: the dependent care deduction | `s 2014(e)(3)(A) the household is entitled to the dependent care deduction`; `s 2014(e)(3)(B) the expense is an excluded expense` |
| s 2014(e)(4) | a household that pays legally obligated child support (once the State agency elects) | the State agency | power-liability: the State agency may elect a deduction for the payments in lieu of the exclusion in subsection (d)(6); once elected, the household has the deduction | `s 2014(e)(4)(A) the child support deduction` |
| s 2014(e)(5) | a household with an elderly or disabled member | (not named) for the deduction; the State agency for the method of claiming recurring expenses | claim-duty: the excess medical expense deduction, and the method of claiming recurring expenses | `s 2014(e)(5)(A) the household is entitled to the excess medical expense deduction`; `s 2014(e)(5)(B)(i) the State agency must offer the method of claiming recurring medical expenses`; `s 2014(e)(5)(C) the expense is treated as a medical expense` |
| s 2014(e)(6)(A) and (B) | a household | (not named) | claim-duty: the excess shelter expense deduction, up to the maximum | `s 2014(e)(6)(A) the excess shelter expense deduction before the maximum`; `s 2014(e)(6) the excess shelter expense deduction` |
| s 2014(e)(6)(C)(i) to (iii) | the State agency | a household | power-liability: the State agency may use, or make mandatory, a standard utility allowance; the household may switch back at the end of a certification period (a claim against a State agency that has not made it mandatory) | `s 2014(e)(6)(C)(i) the State agency may use the standard utility allowance`; `s 2014(e)(6)(C)(ii) an allowance for a heating or cooling expense may be used`; `s 2014(e)(6)(C)(iii)(I) the State agency may make the use of a standard utility allowance mandatory`; `s 2014(e)(6)(C)(iii)(II) the household may switch between the standard utility allowance and actual utility costs` |
| s 2014(e)(6)(C)(iv) | a household with an elderly or disabled member that receives energy assistance; the State agency | the State agency; the Secretary | claim-duty: the allowance reflecting heating and cooling costs is made available to that household; immunity-disability: the State agency may not be required to use a separate allowance or to reduce its single allowance | `s 2014(e)(6)(C)(iv)(I) the standard utility allowance must be made available to the household`; `s 2014(e)(6)(C)(iv)(II) the State agency may be required to use a separate standard utility allowance`; `s 2014(e)(6)(C)(iv)(III) the State agency may be required to reduce the allowance`; `s 2014(e)(6)(C)(iv)(IV) the monthly amount of the energy assistance prorated over the season` |
| s 2014(e)(6)(D) | a homeless household | the State agency | claim-duty: the homeless shelter deduction; the State agency may make a household with extremely low shelter costs ineligible (power-liability) | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction`; `s 2014(e)(6)(D)(ii) the adjusted homeless shelter deduction` |
| s 2014(e)(6)(E) | a household | (not named) | immunity-disability: an internet service fee is not used in the deduction | `s 2014(e)(6)(E) the expense is used in computing the excess shelter expense deduction` |
| s 2014(e), net income | - | - | none: the order of the deductions (fork F-E2) | `s 2014(e) the household's income after the deductions other than the shelter deduction`; `s 2014(e) the household's net income` |
| s 2014(f)(1) | a household with seasonal, contract or self-employment income | (not named) for the averaging; the State agency for the farm option, anticipated earnings and the disregard of changes | claim-duty: income is averaged over the period | `s 2014(f)(1)(A) the household income is averaged over a twelve-month period`; `s 2014(f)(1)(B) the household income is averaged over the period for which it is received`; `s 2014(f)(1)(C) the State agency may disregard the change until the next recertification` |
| s 2014(f)(2) | the State agency | a household | power-liability: the basis (prospective or retrospective) on which the household's income is calculated | `s 2014(f)(2) the basis on which the household's income is calculated` |
| s 2014(f)(3)(A) | - | - | none: a definition of the prospective basis | `s 2014(f)(3)(A) the figures the prospective calculation takes into account` |
| s 2014(f)(3)(B) | a newly applying household | the Secretary (the regulations shall provide) | claim-duty: supplement of the initial allotment where the retrospective basis causes serious hardship | `s 2014(f)(3)(B) the income calculated on a retrospective basis`; `s 2014(f)(3)(B) the initial allotment must be supplemented` |
| s 2014(f)(4) | the Secretary | a State agency | power-liability: the Secretary may waive provisions of the subsection on request | `s 2014(f)(4) the Secretary may waive the provision` |
| s 2014(g)(1) | (not named) | the Secretary | claim-duty: the Secretary assures that a household whose resources exceed the limit is not eligible (fork F-G1) | `s 2014(g)(1)(A) the household is ineligible because its resources exceed the limit` |
| s 2014(g)(1), the limits and their adjustment | - | - | none: the limits are figures; the adjustment is a counting rule | `s 2014(g)(1) the resource limit for the household`; `s 2014(g)(1)(B)(i) the adjusted amount rounded down to the nearest $250 increment`; `s 2014(g)(1)(B)(ii) the adjustment conforms` |
| s 2014(g)(2) | - | - | none: which assets count (the Secretary's duty to include them is not owed to a named party) | `s 2014(g)(2)(A) the resource is included in financial resources by the regulations in force as of June 1, 1982`; `s 2014(g)(2)(B)(i) the resource is included in financial resources`; `s 2014(g)(2)(B)(iv) the value of the vehicle that counts as a resource`; `s 2014(g)(2)(B)(v) the resource is included in financial resources` |
| s 2014(g)(2)(C) | a household | (not named) | immunity-disability: an excluded vehicle, and property directly related to it, is not counted | `s 2014(g)(2)(C) the vehicle is included in financial resources under paragraph (2)`; `s 2014(g)(2)(C) the property related to the vehicle is included in financial resources under paragraph (2)` |
| s 2014(g)(2)(D) | the State agency | a household | power-liability: the State agency may apply State vehicle allowance standards in lieu of clause (B)(iv) | `s 2014(g)(2)(D) the State agency may apply the State vehicle allowance standards to the household` |
| s 2014(g)(3) to (5) | a household | the Secretary for (3) and (4); (not named) for (5) | immunity-disability: a burial plot, plan resources, the earned income tax credit, farm property and inaccessible resources are not counted | `s 2014(g)(3) the burial plot is excluded from financial resources`; `s 2014(g)(3) the nonliquid resource for the plan is excluded from financial resources`; `s 2014(g)(3) the earned income tax credit is excluded from financial resources`; `s 2014(g)(4) the farm property is excluded from financial resources`; `s 2014(g)(5) the resource is excluded as an inaccessible resource` |
| s 2014(g)(5), verification | the Secretary | the State agency | power-liability: the Secretary may require verification of a questionable value | `s 2014(g)(5) the Secretary may require the State agency to require verification of the value of the resource` |
| s 2014(g)(6) | the State agency | a household | power-liability: the State agency may exclude types of resources considered under other Federal programs | `s 2014(g)(6) the State agency may exclude the type of resource` |
| s 2014(g)(7) and (8) | a household | the Secretary | immunity-disability: retirement and education accounts are not counted; the Secretary may exclude others (power-liability) | `s 2014(g)(7)(A) the retirement funds are excluded from financial resources`; `s 2014(g)(7)(B) the Secretary may exclude the retirement plan, contract, or account`; `s 2014(g)(8)(A) the education funds are excluded from financial resources`; `s 2014(g)(8)(B) the Secretary may exclude the education program, contract, or account` |
| s 2014(h)(1) | a household that is a disaster victim | the Secretary | claim-duty: temporary emergency standards of eligibility | `s 2014(h)(1) the Secretary must establish temporary emergency standards of eligibility for the household` |
| s 2014(h)(2) | - | - | none: the Disaster Task Force (machinery, inert reason 2) | none (inert, reason 2) |
| s 2014(h)(3)(A) | an eligible household whose food was destroyed in a disaster | the Secretary | claim-duty: an emergency allotment to replace the food, up to an approved limit | `s 2014(h)(3)(A) the household is provided an emergency allotment to replace food destroyed in a disaster`; `s 2014(h)(3)(A) the value of the food replaced` |
| s 2014(h)(3)(B) | a household in a disaster | the Secretary | claim-duty: the Secretary considers the listed factors and adjusts issuance, reporting and application requirements | `s 2014(h)(3)(B) the factors the Secretary must consider`; `s 2014(h)(3)(B) the Secretary must adjust the issuance methods and the reporting and other application requirements for the household` |
| s 2014(i)(1), (2)(A) and (B) | - | - | none: a counting rule that deems a sponsor's income and resources to a sponsored alien (no one is named as exercising it) | `s 2014(i)(1) the income and resources of the sponsor are deemed to be the income and resources of the individual`; `s 2014(i)(1) the deemed income as an item of the individual's income`; `s 2014(i)(2)(A) the monthly income attributed to the alien`; `s 2014(i)(2)(A)(ii) the size of the sponsor's household`; `s 2014(i)(2)(B) the resources deemed to be the alien's resources`; `s 2014(i)(2)(B)(iii) the resources of the alien with the resources deemed` |
| s 2014(i)(2)(C)(i) | the State agency | a sponsored alien | claim-duty: the alien provides information about the sponsor, and the immigration application papers the State agency requests (fork F-I2) | `s 2014(i)(2)(C)(i) the alien is barred from being an eligible individual or eligible spouse for not providing the information`; `s 2014(i)(2)(C)(i) the alien is required to provide the information and documentation given in support of the immigration application` |
| s 2014(i)(2)(C)(ii) | - | - | none: agreements between the Secretary and the Secretary of State and the Attorney General (machinery, inert reason 2) | none (inert, reason 2) |
| s 2014(i)(2)(D) | (not named) | a sponsor and the alien, jointly and severally | claim-duty: liability for an overpayment, except where the sponsor was without fault or there was good cause | `s 2014(i)(2)(D) the sponsor and the alien are jointly and severally liable for the overpayment`; `s 2014(i)(2)(D) the amount for which the sponsor and the alien are each liable`; `s 2014(i)(2)(D) the overpayment is to be recovered in accordance with section 2022(b)` |
| s 2014(i)(2)(E) | - | - | none: the classes of alien to which the subsection does not apply | `s 2014(i)(2)(E) the subsection applies to the alien` |
| s 2014(j) | a household member who receives SSI, aid to the aged, blind or disabled, or cash assistance | the State agency | immunity-disability: the member is considered to satisfy the resource limits | `s 2014(j) the member is considered to have satisfied the resource limitations of subsection (g)` |
| s 2014(k)(1) to (3) | - | - | none: a counting rule that treats assistance paid to a third party on a household's behalf as money payable to the household, except for the classes in paragraph (2) (fork F-K1) | `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household`; `s 2014(k)(2) paragraph (1) does not apply to the assistance`; `s 2014(k)(3) the educational assistance is treated as money payable directly to the household` |
| s 2014(k)(4) | - | - | none: a counting rule (State energy assistance is money payable, and the expense is an out-of-pocket expense paid by the household) | `s 2014(k)(4)(A) the energy assistance payment is considered money payable directly to the household`; `s 2014(k)(4)(B) the energy assistance expense is considered an out-of-pocket expense incurred and paid by the household` |
| s 2014(l) | - | - | none: a counting rule (on-the-job training earnings are earned income) | `s 2014(l) the earnings of the individual in on-the-job training are considered earned income` |
| s 2014(m) | a State | the Secretary | power-liability: the State submits a method of estimating self-employment income; the Secretary approves it | `s 2014(m)(1) the method may be used in lieu of calculating the actual cost of producing self-employment income`; `s 2014(m)(3) the estimate of the method for the type of self-employment income` |
| s 2014(n) | a State agency | the Secretary | claim-duty: simplified procedures, at the State agency's option, to determine legally obligated child support payments, including reliance on the child support agency's information in lieu of current information from the household | `s 2014(n) the State agency may rely on information from the child support agency in lieu of obtaining current information from the household` |
| s 2014a | (not named) | a certified household that no longer resides in the State | claim-duty: the household reports in the manner the Secretary prescribes (from 5 May 2017) | `s 2014a the household is required to report that it no longer resides in the State in which it is certified` |
| s 2018(a)(1)(A) to (D) | an applicant retail food store or wholesale food concern | (not named) | claim-duty: approval of those whose participation will effectuate the program, on factors including the listed ones; a certificate evidences it and is not transferable; no approval without a visit | `s 2018(a)(1)(A) the applicant is to be approved under the regulations`; `s 2018(a)(1)(B) the factors that must be considered among such other factors as may be appropriate`; `s 2018(a)(1)(C) the approval is evidenced by the issuance of a certificate of approval`; `s 2018(a)(1)(C) the certificate of approval may be transferred`; `s 2018(a)(1)(D) the store or concern may be approved to be authorized or reauthorized` |
| s 2018(a)(2) to (4) | the Secretary | stores and concerns | power-liability: regulations, authorization periods and guidance (machinery, inert reason 2) | none (inert, reason 2) |
| s 2018(b)(1) | the Secretary | a wholesale food concern, a co-located wholesale-retail concern, a firm that is both | immunity-disability: no authorization unless the stated conditions are met | `s 2018(b)(1) the wholesale food concern may be authorized to accept and redeem benefits`; `s 2018(b)(1) the co-located wholesale-retail food concern may be authorized to accept and redeem benefits as a retail food store`; `s 2018(b)(1) the firm may be authorized as both a retail food store and a wholesale food concern at the same time` |
| s 2018(b)(2) | the Secretary | a buyer or transferee of a disqualified store | immunity-disability: no accepting or redeeming until the penalty is paid; no bond required by reason of the sale | `s 2018(b)(2)(A) the buyer or transferee may accept or redeem benefits`; `s 2018(b)(2)(B) the buyer or transferee may be required to furnish a bond under section 2021(d)` |
| s 2018(c) | (not named) | an applicant retail food store or wholesale food concern; a person who discloses without authority | claim-duty: the applicant submits the information the regulations require; the information may be disclosed to and used by listed recipients; a penalty applies to unauthorised disclosure | `s 2018(c) the information obtained under the subsection may be disclosed to and used by the recipient`; `s 2018(c) the penalty to which the person is liable`; `s 2018(c) the sentence is within the limits the subsection sets` |
| s 2018(d) | a store or concern refused approval | (not named) for the hearing; the Secretary for the longer period | claim-duty: a hearing on the refusal; a bar of at least 6 months on a new application (the Secretary may set a longer one) | `s 2018(d) the store or concern may obtain a hearing on the refusal`; `s 2018(d) the store or concern may submit a new application`; `s 2018(d) the longer period bars the new application` |
| s 2018(e) | persons who observe abuses | an approved retail food store | claim-duty: the store displays a sign on how to report abuses | `s 2018(e) the approved retail food store has not displayed the sign` |
| s 2018(f) | the Secretary | a house-to-house trade route | power-liability: the Secretary limits participation to routes reasonably necessary where integrity is damaged | `s 2018(f) the house-to-house trade route may participate` |
| s 2018(g) | (not named) | an approved retail food store | claim-duty: the store provides adequate EBT service | `s 2018(g) the approved retail food store has not provided the adequate EBT service` |
| s 2018(h)(1) and (2)(A) | the Secretary | a private establishment that offers concessional meals | immunity-disability: no authorization unless the Secretary determines the participation is needed, with a 180-day continuation for existing contracts (fork F-H1) | `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits`; `s 2018(h)(2)(A) the operation of the private establishment may continue without the determination of need`; `s 2018(h) permitted under section 2018(h)` |
| s 2018(h)(2)(B) | a State | the Secretary | claim-duty: justification for terminating a contract in effect on 7 February 2014 | `s 2018(h)(2)(B) the Secretary must provide justification to the State for the termination` |
| s 2018(h)(3) | the Committees on Agriculture | the Secretary | claim-duty: the annual report within 90 days after each fiscal year | `s 2018(h)(3) the date the report is due`; `s 2018(h)(3) the report was submitted not later than the date it was due`; `s 2018(h)(3) the duty to submit the report` |
| s 2018(i)(1)(A) to (D) | (not named) | the Secretary; facilities, programs and arrangements | claim-duty: the Secretary reviews a sample and may review others; they submit the information; the Secretary reports within 18 months of 20 December 2018, with two recommendations | `s 2018(i)(1)(A) the Secretary must review the facility`; `s 2018(i)(1)(B) the Secretary may review the program or arrangement`; `s 2018(i)(1)(C) the facility, program or arrangement must submit the information`; `s 2018(i)(1)(D) the results of the reviews were reported not later than 18 months after December 20, 2018`; `s 2018(i)(1)(D) the report includes the recommendations`; `s 2018(i)(1)(D) the duty to report the results of the reviews` |
| s 2018(i)(2) | a facility, program or arrangement | the Secretary | immunity-disability: no denial based on a determination that residents are residents of an institution before 31 December 2022 (fork F-S2) | `s 2018(i)(2) the subsection authorizes the Secretary to deny the application or request` |
| s 2018(j)(1) | - | - | none: a definition of eligible incentive food | `s 2018(j)(1) the food is an eligible incentive food` |
| s 2018(j)(2) to (4) | an approved retail food store; a household | the Secretary | privilege-no-right: the store may offer an incentive usable only for eligible incentive food at the point of purchase, by waiver; benefits are not limited; section 7517 rules are not affected | `s 2018(j)(2)(A) the incentive may be used for the purchase`; `s 2018(j)(2)(B) the approved retail food store may carry out the incentive program`; `s 2018(j)(3) the waiver may be used to carry out the activity`; `s 2018(j)(4) the guidance affects the requirement` |
| s 2018(j)(5) | the Committees on Agriculture | the Secretary | claim-duty: an annual report on the incentives approved | `s 2018(j)(5) the Secretary must submit the annual report describing the types of incentives approved` |
| s 2019, first sentence | a retail food store | (not named) (regulations shall provide) | claim-duty: redemption of accepted benefits through wholesale food concerns or insured financial institutions | `s 2019 the channel is one through which benefits accepted by retail food stores are redeemed` |
| s 2019, exceptions to the channels | a retail food store defined in section 2012(o)(4); a store authorized to accept benefits on-line | (not named) | privilege-no-right: redeem members' benefits before the members receive the food; accept benefits before delivery if delivery follows within a reasonable time | `s 2019 the retail food store is authorized to redeem the members' food benefits before the members receive the food`; `s 2019 the retail food store is authorized to accept benefits before the delivery of the food` |
| s 2019, the bar and its exception | the Secretary | community mental health centers, drug and alcohol programs, shelters for battered women and children, group living arrangements for the disabled or blind | immunity-disability: not authorized to redeem through financial institutions, unless equipped with point-of-sale devices in an area with an electronic benefit transfer system | `s 2019 the body may be authorized to redeem benefits through a financial institution` |
| s 2019, fees | a retail food store | a financial institution | claim-duty: no fee or other charge for redeeming benefits submitted consistently with the requirements | `s 2019 the financial institution may impose on or collect from the retail food store a fee or other charge for the redemption` |

## Marginal readings for a lawyer (snap1)

The rule of 2026-10-29 sorts every answer of a rule into three: `JUST TRUE` (the text says yes), `JUST FALSE` (the text says no in its own words) and `NOTHING` (the text does not say).
My modules carry 93 `FALSE-kind` comments, each quoting the words, and 199 `NOTHING-kind` comments, each saying why the text is silent.
Two readings are taken as the status quo and are listed here so that a lawyer can overrule them; neither is a ruling.

**Reading (a): a failed "if" counts as no.**
Where the text says a thing happens "if" (or "whenever", read as "if") a condition holds, the rule answers `JUST FALSE` when the condition fails.
Another reading is that a failed "if" leaves the question open (`NOTHING`).
The 28 places that rest on reading (a), with the words relied on:

| rule | words relied on |
| --- | --- |
| `s 2013(b)(1) the distribution of commodities shall be made` | "shall be made whenever a request for concurrent or separate food program operations, respectively, is made by a tribal organization" |
| `s 2013(b)(2) the party that administers the distribution` |  |
| `s 2013(b)(4)(B) the Secretary must waive the non-Federal share of the costs` | "shall waive up to 100 percent of the non-Federal share ... if the Secretary determines that— (i) the tribal organization is financially unable ...; or (ii) providing a greater non-Federal share of... |
| `s 2013(b)(4)(D) the Secretary may allow the tribal organization to use the funds to satisfy the non-Federal share` | "if that use is otherwise consistent with the purpose of the funds" |
| `s 2014(a) the household is eligible because each member receives a listed benefit` | "Notwithstanding any other provisions of this chapter except subsections (b), (d)(2), (g), and (r) of section 2015 of this title and section 2012(m)(4) of this title" (the sentence does not overrid... |
| `s 2014(a) the household is eligible because each member receives general assistance` | "Except for sections 2015, 2025(e)(1), and section 2012(m)(4) of this title, households in which each member receives benefits ... shall be eligible" (an excepted provision that applies takes the h... |
| `s 2014(c)(1) the household is ineligible because its net income exceeds the poverty line` | "a household shall be ineligible to participate in the supplemental nutrition assistance program if" its income "exceeds the poverty line" |
| `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit` | "a household shall be ineligible to participate in the supplemental nutrition assistance program if" its income "exceeds such poverty line by more than 30 per centum" |
| `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit` | the "if" clause is "(2) in the case of a household that does not include an elderly or disabled member, the household's income ... exceeds such poverty line by more than 30 per centum"; a household... |
| `s 2014(d)(6) the item is excluded as care and maintenance of a third party or child support paid out` | "child support payments made by a household member to or for an individual who is not a member of the household if the household member is legally obligated to make the payments" |
| `s 2014(d)(12) the cost-of-living increase is excluded on the date` | "if the household was certified as eligible to participate in the supplemental nutrition assistance program or received an allotment in the month immediately preceding the first month in which the ... |
| `s 2014(d)(19) the combat pay is excluded` | "if the additional pay— (A) is the result of deployment to or service in a combat zone; and (B) was not received immediately prior to serving in a combat zone" |
| `s 2014(e)(3)(A) the household is entitled to the dependent care deduction` | the entitlement is "if the care enables a household member to accept or continue employment, or training or education that is preparatory for employment" |
| `s 2014(e)(6)(C)(iii)(I) the State agency may make the use of a standard utility allowance mandatory` | the power is given "if" both (aa) and (bb) hold |
| `s 2014(e)(6)(C)(iv)(I) the standard utility allowance must be made available to the household` | the duty arises "if a State agency elects to use a standard utility allowance that reflects heating and cooling costs" |
| `s 2014(e)(6)(C)(iv)(I) the standard utility allowance must be made available to the household` | the duty is "if in the current month or in the immediately preceding 12 months the household either received such a payment ... that was greater than $20 annually" |
| `s 2014(f)(1)(A) the State agency must calculate the self-employment income on anticipated earnings` | "if the averaged amount does not accurately reflect the household's actual monthly circumstances because the household has experienced a substantial increase or decrease in business earnings" |
| `s 2014(g)(1)(A) the resources exceed the limit` | "will not be eligible to participate if its resources exceed" the limit |
| `s 2014(g)(2)(D) the State agency may apply the State vehicle allowance standards to the household` | "If the vehicle allowance standards ... would result in a lower attribution of resources to certain households than under subparagraph (B)(iv)" |
| `s 2014(g)(3) the earned income tax credit is excluded from financial resources` | "if such member was participating in the supplemental nutrition assistance program at the time the credits were received and participated in such program continuously during the 12-month period" |
| `s 2014(g)(5) the resource is excluded as an inaccessible resource` | "A resource shall be so identified if its sale or other disposition is unlikely to produce any significant amount of funds for the support of the household" |
| `s 2014(h)(1) the Secretary must establish temporary emergency standards of eligibility for the household` | "if such households are in need of temporary food assistance and if commercial channels of food distribution have again become available to meet the temporary food needs of such households" |
| `s 2014(i)(2)(C)(i) the alien is barred from being an eligible individual or eligible spouse for not providing the information` | the information is required only "in order to be an eligible individual or eligible spouse", so an alien who provides it is not barred by this clause (marginal reading (a)) |
| `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household` | "shall be considered money payable directly to the household if the assistance is provided in lieu of" |
| `s 2014a the household is required to report that it no longer resides in the State in which it is certified` | "is required to report ... if the household no longer resides in the State in which it is certified" |
| `s 2018(h)(2)(A) the operation of the private establishment may continue without the determination of need` | "If, on the day before February 7, 2014, a State has entered into a contract with a private establishment described in paragraph (1) and the Secretary has not determined that the participation of t... |
| `s 2018(h)(2)(B) the Secretary must provide justification to the State for the termination` | "If the Secretary determines to terminate a contract with a private establishment that is in effect on February 7, 2014, the Secretary shall provide justification" |
| `s 2019 the retail food store is authorized to accept benefits before the delivery of the food` | "if the delivery occurs within a reasonable time of the purchase, as determined by the Secretary" |

**Reading (b): a prohibition or grant limited by its own wording does not answer outside the wording.**
Where the text says "only", "unless", "in the case of ...", "for ...", or names a class, the rule answers `JUST FALSE` inside what the text forbids and `NOTHING` outside the words (it does not say that everything else is allowed or owed).
Another reading is that the limit implies the converse.
The 139 places that rest on reading (b), with the limit:

| rule | what the wording limits |
| --- | --- |
| `s 2012a the provision is also applicable to the center` | the section is for "publicly operated community health centers" |
| `s 2012a the provision is also applicable to the center` | the section applies the provisions "concerning private, nonprofit drug addiction or alcohol treatment and rehabilitation programs" |
| `s 2013(a)(1) the eligible household is provided an opportunity to obtain a more nutritious diet through the issuance of an allotment` | the grant is "subject to the availability of funds", "at the request of the State agency", and for "eligible households within the State" |
| `s 2013(a)(1) the benefits may be used for the purchase` | "only" names who and what is outside; it does not say that every purchase of food from an approved store is allowed |
| `s 2013(a)(1) the benefits are redeemable at face value by the Secretary through the facilities of the Treasury` | the sentence is for benefits "issued and used as provided in this chapter" |
| `s 2013(a)(2)(B)(ii)(I) the payment error rate the State elects to use for fiscal year 2028` | the election is of "the payment error rate of the State from fiscal year 2025 or 2026" |
| `s 2013(a)(2)(B)(ii)(II) the payment error rate the Secretary uses for fiscal year 2029 and each fiscal year thereafter` | the clause is for "fiscal year 2029 and each fiscal year thereafter" |
| `s 2013(a)(2)(B)(i) the shares of the cost of the allotment for the State in the fiscal year` | the shares are for the fiscal years "beginning in fiscal year 2028", or from the later implementation date under clause (iii) |
| `s 2013(a)(3) the Secretary may pay the amount towards the cost of the allotment` | the sentence is a ceiling; it does not authorize a payment up to it |
| `s 2013(b)(2) the party that administers the distribution` | paragraph (2)(A) is "in the event of distribution on all or part of an Indian reservation" |
| `s 2013(b)(2)(C) the Secretary may approve the plan` | the bar is on a plan "that permits any household on any Indian reservation to participate simultaneously" |
| `s 2013(b)(3) the period for which the individual is not eligible to participate in the supplemental nutrition assistance program` | the sentence is for "an individual who is disqualified from participation in the food distribution program on Indian reservations" |
| `s 2013(b)(3) the individual is not eligible to participate in the supplemental nutrition assistance program` | the ineligibility is "for a period of time to be determined by the Secretary", and the period or the disqualification is not shown to run |
| `s 2013(b)(4)(C) the Secretary may reduce the benefits or services to the tribal organization` | the bar is for "any tribal organization that is granted a waiver under subparagraph (B)" |
| `s 2013(b)(4)(D) the Secretary may allow the tribal organization to use the funds to satisfy the non-Federal share` | the sentence is for "funds provided to the tribal organization through a Federal agency or other Federal benefit" |
| `s 2013(b)(5) the Secretary may purchase the bison meat` | the power is "subject to the availability of appropriations" and for "recipients of food distributed under this subsection" |
| `s 2013(b)(6)(A) the Secretary must establish the fund` | the duty is "subject to the availability of appropriations" |
| `s 2013(b)(6)(B) the food provided meets the requirement for Native American producers` | the requirement is "where practicable" |
| `s 2013(b)(6)(D) the Secretary must purchase or offer to purchase the food` | the duty is for "those traditional foods that may be procured cost-effectively" |
| `s 2013(b)(6)(E) the amount authorized to be appropriated for the fiscal year` | the authorization is "for each of fiscal years 2008 through 2023" |
| `s 2014(a) the household may participate in the program` | a limit names who is outside; it does not say that everyone inside may participate |
| `s 2014(a) the household is eligible because each member receives a listed benefit` | "households in which each member receives benefits" names the households the sentence reaches; it does not say what follows for the others |
| `s 2014(a) the household is eligible because each member receives general assistance` | the sentence reaches only households whose members all receive general assistance of the kind it describes |
| `s 2014(a) assistance must be furnished to the household` | the duty is owed "to all eligible households who make application"; the text is silent on anyone else |
| `s 2014(b) the plan of operation may be approved` | "unless" states a condition that must be met; it does not say that a plan meeting it is approved |
| `s 2014(b) the State agency may impose the standard` | the bar reaches "any other standards of eligibility as a condition for participating"; the text is silent on anything else the agency imposes |
| `s 2014(d)(1) the item is excluded because it is not money payable directly to a household` | paragraph (1) reaches only a gain or benefit that is not money payable directly to a household |
| `s 2014(d)(2) the amount excluded in the quarter` | paragraph (2) reaches only income "received too infrequently or irregularly to be reasonably anticipated" |
| `s 2014(d)(3) the amount excluded` | paragraph (3) reaches only such awards to an enrolled household member |
| `s 2014(d)(4) the loan is excluded` | paragraph (4) reaches only loans on which repayment is deferred |
| `s 2014(d)(5) the item is excluded as a reimbursement or a school allowance` | paragraph (5) reaches only the reimbursements and the school allowance it describes |
| `s 2014(d)(6) the item is excluded as care and maintenance of a third party or child support paid out` | paragraph (6) reaches only those two kinds of item |
| `s 2014(d)(7) the child's earned income is excluded` | paragraph (7) reaches only a child member who is a school student aged 17 or younger |
| `s 2014(d)(8) the cash donation excluded in the quarter` | the $300 limit is on "cash donations based on need that are received from one or more private nonprofit charitable organizations" |
| `s 2014(d)(8) the lump-sum payment is excluded from income` | paragraph (8) reaches nonrecurring lump-sum payments; the cash donations of the same paragraph are measured by the quarterly limit |
| `s 2014(d)(10) the income is excluded because another Federal law excludes it` | paragraph (10) reaches only income another Federal law "specifically excludes" |
| `s 2014(d)(11) the payment or allowance is excluded` | paragraph (11) reaches energy assistance under a Federal law other than part A of title IV, and a 1-time weatherization or repair payment |
| `s 2014(d)(12) the cost-of-living increase is excluded on the date` | paragraph (12) reaches "any increase in income attributable to a cost-of-living adjustment" under those provisions |
| `s 2014(d)(12) the cost-of-living increase is excluded on the date` | paragraph (12) runs "through September 30" of the fiscal year of an adjustment made on or after July 1 |
| `s 2014(d)(13) the advance earned income credit payment is excluded` | paragraph (13) reaches only payments under section 3507 of title 26 |
| `s 2014(d)(14) the payment for work related expenses or dependent care is excluded` | paragraph (14) reaches only such payments for work related expenses or dependent care |
| `s 2014(d)(15) the amount for a plan for achieving self-support is excluded` | paragraph (15) reaches only amounts necessary for such a plan |
| `s 2014(d)(16) the educational award is excluded at the option of the State agency` | paragraph (16) reaches only what the State agency has chosen to exclude and title XIX requires to be excluded |
| `s 2014(d)(17) the State complementary assistance payment is excluded at the option of the State agency` | paragraph (17) reaches only what the State agency has chosen to exclude and section 1931 excludes |
| `s 2014(d)(18) the income is excluded at the option of the State agency` | paragraph (18) reaches only what the State agency has chosen to exclude and does not consider for those programs |
| `s 2014(d)(19) the combat pay is excluded` | paragraph (19) reaches "any additional payment under chapter 5 of title 37, or otherwise designated by the Secretary to be appropriate for exclusion under this paragra... |
| `s 2014(e)(1)(A)(ii)(I) the minimum standard deduction for fiscal year 2009` | clause (A)(ii)(I) names "the 48 contiguous States and the District of Columbia, Alaska, Hawaii, and the Virgin Islands"; Guam's floor is in subparagraph (B)(ii)(I) |
| `s 2014(e)(2) the household is allowed the earned income deduction` | paragraph (2)(B) reaches "a household with earned income" |
| `s 2014(e)(4)(A) the child support deduction` | the deduction exists only "in lieu of providing an exclusion" where the State agency "may elect"; without the election paragraph (d)(6) governs |
| `s 2014(e)(5)(A) the household is entitled to the excess medical expense deduction` | the entitlement is given to "A household containing an elderly or disabled member"; the text does not say what a household without one may deduct |
| `s 2014(e)(5)(B)(i) the State agency must offer the method of claiming recurring medical expenses` | the duty is owed to "an eligible household under subparagraph (A)" |
| `s 2014(e)(5)(B)(ii)(III) further reporting or verification of the change may be required` | the bar is on a change "anticipated for the certification period"; the text is silent on any other change |
| `s 2014(e)(5)(C) the expense is treated as a medical expense` | paragraph (C) names medical marijuana only; whether another expense is a medical expense is for section 2012(c) |
| `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date` | the maximum is "In the case of a household that does not contain an elderly or disabled individual" |
| `s 2014(e)(6)(C)(i) the State agency may use the standard utility allowance` | the grant is "in accordance with regulations promulgated by the Secretary", subject to clause (iv) |
| `s 2014(e)(6)(C)(ii) an allowance for a heating or cooling expense may be used` | clause (ii) says when an allowance may not be used; it does not say that it may be used in any other case |
| `s 2014(e)(6)(C)(iii)(II) the household may switch between the standard utility allowance and actual utility costs` | the duty is of "A State agency that has not made the use of a standard utility allowance mandatory" and runs "at the end of a certification period" |
| `s 2014(e)(6)(C)(iv)(I) the standard utility allowance must be made available to the household` | the duty is owed "to households with an elderly or disabled member" |
| `s 2014(e)(6)(C)(iv)(II) the State agency may be required to use a separate standard utility allowance` | the bar is on being "required" to use a separate allowance; the State agency "may use" one |
| `s 2014(e)(6)(C)(iv)(III) the State agency may be required to reduce the allowance` | the bar is on a State agency that "does not elect to use a separate allowance but makes a single standard utility allowance available" |
| `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction` | the deduction is for households that meet (I), (II) and (III); the text is silent on the others (section 2012(l) is a seam input) |
| `s 2014(e)(6)(E) the expense is used in computing the excess shelter expense deduction` | subparagraph (E) bars internet service fees only; whether another expense is a shelter expense is not answered here |
| `s 2014(f)(1)(A) the household income is averaged over a twelve-month period` | the sentence is for "those households that" derive their annual income in a period shorter than one year |
| `s 2014(f)(1)(A) the farming income and expenses may be averaged over a 12-month period` | the sentence is for income from "the self-employment of a member in a farming operation, who derives income from such farming operation and who has irregular expenses ... |
| `s 2014(f)(1)(B) the household income is averaged over the period for which it is received` | the paragraph is for "those households that receive nonexcluded income of the type described in subsection (d)(3)" |
| `s 2014(f)(1)(C) the State agency may disregard the change until the next recertification` | the grant is for changes "that affect the amount of deductions the household may claim under subsection (e)" |
| `s 2014(f)(3)(B) the initial allotment must be supplemented` | the supplement is for "newly applying households in those cases in which" the determination "causes serious hardship" |
| `s 2014(f)(4) the Secretary may waive the provision` | the authority is "upon the request of a State agency" and "to the extent necessary" to calculate income on the title IV-A basis |
| `s 2014(g)(2)(A) the resource is included in financial resources by the regulations in force as of June 1, 1982` | the regulations of 1 June 1982 are followed "other than those relating to licensed vehicles and inaccessible resources" |
| `s 2014(g)(2)(C) the vehicle is included in financial resources under paragraph (2)` | the exclusion is for a vehicle that is used to produce earned income, necessary for a physically disabled member's transportation, or depended on for fuel or water |
| `s 2014(g)(2)(C) the property related to the vehicle is included in financial resources under paragraph (2)` | the exclusion reaches property "to the extent the property is directly related to the maintenance or use of the vehicle" of an excluded vehicle |
| `s 2014(g)(2)(B)(iv) the value of the vehicle that counts as a resource` | clause (iv) is for "any licensed vehicle that is used for household transportation or to obtain or continue employment" |
| `s 2014(g)(3) the burial plot is excluded from financial resources` | the exclusion is for "a burial plot for each member of a household" |
| `s 2014(g)(3) the nonliquid resource for the plan is excluded from financial resources` | the exclusion is for nonliquid resources "necessary to allow the household to carry out a plan for self-sufficiency approved by the State agency" that is adequate part... |
| `s 2014(g)(3) the earned income tax credit is excluded from financial resources` | the exclusion is for "any earned income tax credits received by any member of the household" |
| `s 2014(g)(3) the earned income tax credit is excluded from financial resources` | the exclusion is "for a period of 12 months from receipt", and the determination is outside that period |
| `s 2014(g)(4) the farm property is excluded from financial resources` | the exclusion is for "farm property ... that is essential to the self-employment of a household member in a farming operation" |
| `s 2014(g)(4) the farm property is excluded from financial resources` | the exclusion runs "until the expiration of the 1-year period" and the determination is outside it |
| `s 2014(g)(6) the State agency may exclude the type of resource` | the State agency's option is for types it does not consider for cash assistance under part A of title IV or medical assistance under section 1931 |
| `s 2014(g)(7)(B) the Secretary may exclude the retirement plan, contract, or account` | the power is over "any other retirement plans, contracts, or accounts" |
| `s 2014(g)(8)(B) the Secretary may exclude the education program, contract, or account` | the power is over "any other education programs, contracts, or accounts" |
| `s 2014(h)(1) the Secretary must establish temporary emergency standards of eligibility for the household` | the duty is for "households who are victims of a disaster which disrupts commercial channels of food distribution" |
| `s 2014(h)(3)(A) the household is provided an emergency allotment to replace food destroyed in a disaster` | the allotments are "to eligible households to replace food destroyed in a disaster" |
| `s 2014(h)(3)(B) the Secretary must adjust the issuance methods and the reporting and other application requirements for the household` | the adjustment is to what is practicable "under actual conditions in the affected area" |
| `s 2014(i)(2)(E) the subsection applies to the alien` | the exception names two classes and does not say that the subsection applies to everyone else |
| `s 2014(i)(1) the income and resources of the sponsor are deemed to be the income and resources of the individual` | the paragraph is for "an individual who is an alien as described in section 2015(f)(2)(B)" |
| `s 2014(i)(1) the income and resources of the sponsor are deemed to be the income and resources of the individual` | the paragraph deems the income of "any person who as a sponsor of such individual's entry into the United States executed an affidavit of support or similar agreement" |
| `s 2014(i)(1) the income and resources of the sponsor are deemed to be the income and resources of the individual` | the deeming is "for a period of three years after the individual's entry into the United States" and the determination is outside it |
| `s 2014(i)(2)(C)(i) the alien is barred from being an eligible individual or eligible spouse for not providing the information` | the requirement is "during the period of three years after entry into the United States" |
| `s 2014(i)(2)(C)(i) the alien is required to provide the information and documentation given in support of the immigration application` | the sentence reaches the information "which such alien or the sponsor provided in support of such alien's immigration application" "as the State agency may request"; w... |
| `s 2014(i)(2)(D) the sponsor and the alien are jointly and severally liable for the overpayment` | the liability is for an overpayment made "during the period of three years after such alien's entry" and "on account of such sponsor's failure to provide correct infor... |
| `s 2014(i)(2)(D) the overpayment is to be recovered in accordance with section 2022(b)` | the sentence is for "any such overpayment which is not repaid" |
| `s 2014(j) the member is considered to have satisfied the resource limitations of subsection (g)` | the subsection is for "a household member who receives" one of the three kinds of benefit |
| `s 2014(k)(1) the assistance to a third party is considered money payable directly to the household` | the paragraph is for "assistance provided to a third party on behalf of a household by a State or local government" |
| `s 2014(k)(3) the educational assistance is treated as money payable directly to the household` | the paragraph is for educational assistance "provided to a third party on behalf of a household for living expenses" |
| `s 2014(k)(4)(A) the energy assistance payment is considered money payable directly to the household` | the subparagraph is for a payment "to provide energy assistance to a household without an elderly or disabled member" |
| `s 2014(k)(4)(B) the energy assistance expense is considered an out-of-pocket expense incurred and paid by the household` | the subparagraph is for an expense "paid on behalf of a household with an elderly or disabled member" |
| `s 2014(l) the earnings of the individual in on-the-job training are considered earned income` | the subsection is for "earnings to individuals participating in on-the-job training under title I of such Act" |
| `s 2014(m)(1) the method may be used in lieu of calculating the actual cost of producing self-employment income` | the method is one "designed to not increase Federal costs" that the Secretary approves and determines "will produce a reasonable estimate" |
| `s 2014(m)(3) the estimate of the method for the type of self-employment income` | the method "may allow a State to estimate income for all types of self-employment income or may be limited to 1 or more types" |
| `s 2014(n) the State agency may rely on information from the child support agency in lieu of obtaining current information from the household` | the procedure is "at the option of the State agencies" and for "payments made in prior months" |
| `s 2014a the household is required to report that it no longer resides in the State in which it is certified` | the requirement is on "a household certified to participate in the Supplemental Nutrition Assistance Program" |
| `s 2014a the household is required to report that it no longer resides in the State in which it is certified` | the requirement begins "on May 5, 2017" |
| `s 2018(a)(1)(A) the applicant is to be approved under the regulations` | the regulations are to provide for "the approval of those applicants whose participation will effectuate the purposes" |
| `s 2018(a)(1)(C) the approval is evidenced by the issuance of a certificate of approval` | the sentence is for the "approval of an applicant" |
| `s 2018(a)(1)(C) the certificate of approval may be transferred` | the word "nontransferable" is of the "certificate of approval" that evidences approval |
| `s 2018(a)(1)(D) the store or concern may be approved to be authorized or reauthorized` | the bar is "unless" a visit has been made, and a visit does not itself approve the store or concern |
| `s 2018(b)(1) the wholesale food concern may be authorized to accept and redeem benefits` | the bar is "unless" the Secretary so determines, and the determination does not itself authorize the concern |
| `s 2018(b)(1) the co-located wholesale-retail food concern may be authorized to accept and redeem benefits as a retail food store` | the bar is "unless" one of two conditions holds, and either does not itself authorize the concern |
| `s 2018(b)(1) the firm may be authorized as both a retail food store and a wholesale food concern at the same time` | the bar is on authorization "as both ... at the same time" |
| `s 2018(b)(2)(A) the buyer or transferee may accept or redeem benefits` | the bar is on a buyer or transferee "(other than a bona fide buyer or transferee)" of a disqualified store or concern, and "until" the Secretary receives full payment |
| `s 2018(b)(2)(B) the buyer or transferee may be required to furnish a bond under section 2021(d)` | the bar is on a requirement imposed "as a result of the sale or transfer" |
| `s 2018(c) the information obtained under the subsection may be disclosed to and used by the recipient` | the exception names its recipients and purposes, and the safeguards limit use "to purposes directly connected with administration and enforcement" of the chapter and i... |
| `s 2018(c) the penalty to which the person is liable` | the penalty is for a disclosure "in any manner or to any extent not authorized by Federal law (including a regulation)" |
| `s 2018(d) the store or concern may obtain a hearing on the refusal` | the sentence is for a store or concern "which has failed upon application to receive approval" |
| `s 2018(d) the store or concern may submit a new application` | the waiting period is for a store or concern "denied approval ... because the store or concern does not meet criteria for approval established by the Secretary" |
| `s 2018(d) the store or concern may submit a new application` | the bar is "for at least 6 months" and no longer period was supplied |
| `s 2018(d) the longer period bars the new application` | the longer period has run |
| `s 2018(d) the longer period bars the new application` | the longer period has run |
| `s 2018(e) the approved retail food store has not displayed the sign` | the duty is on "approved retail food stores" |
| `s 2018(f) the house-to-house trade route may participate` | the limit is "in those areas in which the Secretary ... finds evidence that the operation of house-to-house trade routes damages the program's integrity" |
| `s 2018(f) the house-to-house trade route may participate` | a limit "to those routes that are reasonably necessary" names who is outside; it does not say that those inside may participate |
| `s 2018(g) the approved retail food store has not provided the adequate EBT service` | the duty is on "an approved retail food store" |
| `s 2018(h)(2)(A) the operation of the private establishment may continue without the determination of need` | the continuation is "for a period not to exceed 180 days from the date on which the Secretary establishes determination criteria" |
| `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` | the paragraph is for a private establishment "that contracts with a State agency to offer meals at concessional prices as described in paragraphs (3), (4), and (9) of ... |
| `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` | the bar is "unless" the Secretary so determines, and the determination does not itself authorize the establishment |
| `s 2018(h)(3) the date the report is due` | the first report is due "90 days after September 30, 2014" |
| `s 2018(h)(3) the report was submitted not later than the date it was due` | the first report is due "90 days after September 30, 2014" |
| `s 2018(i)(1)(A) the Secretary must review the facility` | the duty is for "a representative sample of currently authorized facilities referred to in section 2012(k)(3)" |
| `s 2018(i)(1)(B) the Secretary may review the program or arrangement` | the power is for "currently participating" programs and arrangements "referred to in section 2012(k)" |
| `s 2018(i)(1)(C) the facility, program or arrangement must submit the information` | the duty is for "such facilities, programs, and arrangements" and for "information deemed necessary for a full and thorough review" |
| `s 2018(i)(2) the subsection authorizes the Secretary to deny the application or request` | the limit is on a denial "based on a determination that residents ... are residents of an institution prior to December 31, 2022" |
| `s 2018(j)(2)(A) the incentive may be used for the purchase` | "only" names what is outside; it does not say that every purchase of an eligible incentive food is allowed |
| `s 2018(j)(3) the waiver may be used to carry out the activity` | the bar is on "any activity that limits the use of benefits" |
| `s 2018(j)(4) the guidance affects the requirement` | the bar is on any "requirements under section 7517" |
| `s 2019 the retail food store is authorized to redeem the members' food benefits before the members receive the food` | the exception is for "retail food stores defined in section 2012(o)(4)" |
| `s 2019 the retail food store is authorized to accept benefits before the delivery of the food` | the exception is for "retail food stores authorized to accept and redeem benefits through on-line transactions" |
| `s 2019 the body may be authorized to redeem benefits through a financial institution` | the bar names four kinds of body and does not say what applies to others |
| `s 2019 the financial institution may impose on or collect from the retail food store a fee or other charge for the redemption` | the bar is on a fee "for the redemption of benefits that are submitted ... in a manner consistent with the requirements" |

Other assumed choices that a lawyer may overrule, all recorded where they are made:

- **Composition rule (assumed, not ruled).** An amount function (a deduction, a net income) is arithmetic given that the household is entitled; an entitlement function answers `MAYBE BOOLEAN`. A caller who does not hold an entitlement as shown passes `0` for that deduction (the seat's net income question does this); a deduction the text does not grant is therefore not taken. The header of `snap1-s2014-e1.l4` states it.
- **A resource the text neither includes nor excludes.** Each resource is a pair (text includes it, text excludes it), both `MAYBE BOOLEAN`. The household's total is a pair too: the total of what is shown to count, and the total of what may count. A household is ineligible on resources only if the first total exceeds the limit; it is not ineligible only if the second does not; between them the answer is `NOTHING`.
- **The keel's `permitted under section 2018(h)`.** The core types it `BOOLEAN`, so `s 2018(h) permitted under section 2018(h)` answers `TRUE` unless the text says no (`NOTHING` becomes `TRUE`, never `FALSE`): a lossy step the core asked for. The finer rule `s 2018(h)(1) ...` returns the three values.
- **"Whole months".** The three-year periods of section 2014(i) are counted in whole months by `snap1 whole months from the earlier date to the later date`; a month is complete when the day of the month has been reached (31 January to 28 February is 0 whole months; 15 March 2026 to 15 March 2027 is 12). A lawyer may count month-ends differently.
- **Dates with a stated day count.** The report of section 2018(h)(3) is due 90 days after 30 September, which is 29 December; the report of section 2018(i)(1)(D), "18 months after December 20, 2018", is 20 June 2020 and is 548 days in the regulative twin.

### Reading a result: FALSE and NOTHING (snap1)

A function that returns `MAYBE BOOLEAN` answers one of three things.
`JUST TRUE` means the text says yes in its own words.
`JUST FALSE` means the text says no in its own words, and the line carries `-- FALSE-kind (the text says no in its own words): "<the words>"`.
`NOTHING` means the text does not say, and the line carries `-- NOTHING-kind (<why>)`: limited by its own wording, silent, a list that is not closed, or points outside the text (a fact or a determination the caller did not supply).
A caller must never turn `NOTHING` into `FALSE`; a caller that must produce a plain `BOOLEAN` for a core field says so (one place, listed above).
Four worked examples from the tests:

| call | answer | why |
| --- | --- | --- |
| `s 2014(c)(1) the household is ineligible because its net income exceeds the poverty line` with income 2750 and line 2750 | `JUST FALSE` | the text says a household is ineligible "if" its income "exceeds" the line; at the line the "if" fails (reading (a)) |
| `s 2013(a)(1) the benefits may be used for the purchase` for food from an approved store | `NOTHING` | the text says benefits "shall be used only to purchase food from retail food stores which have been approved"; "only" names what is outside, and does not say that every purchase of food from an approved store is allowed (reading (b)) |
| `s 2014(i)(2)(B) the resources deemed to be the alien's resources` with sponsor resources 1499 | `NOTHING` | the text deems the resources "in excess of $1,500"; below that it is silent |
| `s 2014(f)(2) the basis on which the household's income is calculated` for a first-month household in subparagraph (C) | the constructor `s 2014(f)(2) basis not covered by this text` | subparagraph (C) does not yield to (B), so the text gives two bases (finding 18) |

Where a rule returns a constructor instead of `NOTHING` it is named "not covered" (`s 2014(f)(2) basis not covered by this text`, `s 2014(e)(6)(B) cap not covered by this text`, `s 2014(e)(6)(B) no cap stated for the household`); every one is asserted.

## Seams (snap1)

Each seam input is named for the function that answers it, as PLAN.md section 4 asks; a seam that is a Secretary's determination is `MAYBE BOOLEAN`.
The full list of what I ask, and what I answer, is in `SEAMS.md`; the asks as the modules hold them are:

| input (named for the answering function) | type | read by |
| --- | --- | --- |
| `s 2012(j) the household includes an elderly or disabled member` | MAYBE BOOLEAN | `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross mon...`; `s 2014(c)(2) the household is ineligible because its gross income exceeds the poverty l...`; `s 2014(e)(5)(A) the household is entitled to the excess medical expense deduction`; `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6)(C)(iv)(I) the standard utility allowance must be made available to the hou...`; `s 2014(g)(1) the resource limit for the household`; `s 2014(g)(1)(A) the household is ineligible because its resources exceed the limit`; `s 2014(k)(4)(A) the energy assistance payment is considered money payable directly to t...`; `s 2014(k)(4)(B) the energy assistance expense is considered an out-of-pocket expense in...` |
| `s 2012(k) the establishment is one described in paragraphs (3), (4) and (9) of section 2012(k)` | BOOLEAN | `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` |
| `s 2012(k) the group living arrangement is one referred to in section 2012(k)` | BOOLEAN | `s 2018(i)(1)(B) the Secretary may review the program or arrangement`; `s 2018(i)(1)(C) the facility, program or arrangement must submit the information` |
| `s 2012(k)(3) the facility is one referred to in section 2012(k)(3)` | BOOLEAN | `s 2018(i)(1)(A) the Secretary must review the facility`; `s 2018(i)(1)(C) the facility, program or arrangement must submit the information` |
| `s 2012(l) every member of the household is a homeless individual` | MAYBE BOOLEAN | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction` |
| `s 2012(m)(4) the individual or group may constitute a household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit`; `s 2014(a) the household is eligible because each member receives general assistance` |
| `s 2012(o)(4) the seller is a private nonprofit cooperative food purchasing venture or an agricultural producer marketing directly to consumers` | BOOLEAN | `s 2019 the retail food store is authorized to redeem the members' food benefits before ...` |
| `s 2015 a provision of section 2015 applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives general assistance` |
| `s 2015(b) the exception in subsection (b) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2015(c)(1) the household is required to submit monthly reports of its income and household circumstances` | MAYBE BOOLEAN | `s 2014(f)(2) the basis on which the household's income is calculated` |
| `s 2015(c)(1)(A) the household is specified in clause (i), (ii) or (iii) of section 2015(c)(1)(A)` | MAYBE BOOLEAN | `s 2014(f)(2) the basis on which the household's income is calculated` |
| `s 2015(d)(2) the exception in subsection (d)(2) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2015(f)(2)(B) the individual is an alien as described in section 2015(f)(2)(B)` | MAYBE BOOLEAN | `s 2014(i)(1) the income and resources of the sponsor are deemed to be the income and re...` |
| `s 2015(g) the exception in subsection (g) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2015(r) the exception in subsection (r) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2016(h)(3)(B) the EBT service the store provides is adequate EBT service as described in section 2016(h)(3)(B)` | MAYBE BOOLEAN | `s 2018(g) the approved retail food store has not provided the adequate EBT service` |
| `s 2017 the maximum monthly allotment for the household size, in dollars` | NUMBER | `s 2014(h)(3)(A) the value of the food replaced` |
| `s 2020(e)(25) the Secretary determines that the participation of the private establishment is required to meet a documented need` | BOOLEAN | `s 2018(h) permitted under section 2018(h)`; `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` |
| `s 2021(a) the retail food store or wholesale food concern has been disqualified under section 2021(a)` | BOOLEAN | `s 2018(b)(2)(A) the buyer or transferee may accept or redeem benefits` |
| `s 2025(e)(1) section 2025(e)(1) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives general assistance` |

Seams the plan lacks, or that differ from it:

- **Household-level elderly and homeless inputs.** PLAN.md names `s 2012(j) the member is an elderly or disabled member` (one member) and `s 2012(l) the individual is a homeless individual`. Section 2014 asks the question of a household ("a household containing an elderly or disabled member", "all members are homeless individuals"), so I took `s 2012(j) the household includes an elderly or disabled member` and `s 2012(l) every member of the household is a homeless individual`, both `MAYBE BOOLEAN`; the merge folds the per-member answers (an elderly member makes it `JUST TRUE`; if no member is known to be and one is unknown, it is `NOTHING`).
- **Section 2015 exceptions.** Section 2014(a) is "except for sections 2015, 2025(e)(1), and 2012(m)(4)". PLAN.md's group A names the section 2012(m)(4) seam for this sentence; the section 2015 mentions are group C (references only, bodies not read). I took `s 2015(b)`, `s 2015(d)(2)`, `s 2015(g)` and `s 2015(r)` as separate inputs (the exceptions the second sentence of subsection (a) names) and `s 2015` for the general reference in the third sentence, plus `s 2025(e)(1)`.
- **Section 2015(c) and (f).** Section 2014(f)(2) needs `s 2015(c)(1)(A)` and `s 2015(c)(1)`; section 2014(i) needs `s 2015(f)(2)(B)`. These are group C seams found in the bodies.
- **Section 2016, 2017, 2020 and 2021.** `s 2016(h)(3)(B)` (adequate EBT service, section 2018(g)), `s 2017` (the maximum monthly allotment, section 2014(h)(3)), `s 2020(e)(25)` (the Secretary's determination of documented need, section 2018(h)) and `s 2021(a)` (disqualification, section 2018(b)(2)) are asked by name. `s 2016(h)(3)(B)` is `MAYBE BOOLEAN`; `s 2020(e)(25)` and `s 2021(a)` are plain `BOOLEAN` and `s 2017` is a `NUMBER`. If the answering functions return `MAYBE` types, the merge must adapt: a plain `BOOLEAN` here would otherwise force `NOTHING` into `FALSE`.
- **Section 2025(c)(2).** The payment error rate of a State is "the meaning given ... in section 2025(c)(2)"; the rates are inputs (`MAYBE NUMBER`), not a function.
- **The regulations in force on 1 June 1982** (section 2014(g)(2)(A)) are not among the sources and are not a section; whether a resource is included under them is an input (`MAYBE BOOLEAN`).
- **Answers I give.** `s 2018(h) permitted under section 2018(h)`; `s 2013(b)(2)(B) the tribal organization is capable of effectively and efficiently administering the distribution` (for section 2012(s)); `s 2014(c)(1) the poverty line for the household` (the core asks `NUMBER`; mine is `MAYBE NUMBER`, `NOTHING` where the tables hold no row, so the merge must decide what a missing line means); `s 2014(d) household income` (the core's "income of the others, excluding the spouse, determined under section 2014(d)" is this function over the list of the others' counted monthly amounts).

## The seat layer (snap1)

Seat: a member of a household that applies for, or receives, SNAP.
`snap1-seat.l4` has 44 questions, each named "Under section N, ...", each with `@export` and `@desc`, grouped under `§` headings in the text's order; `snap1-cases-seat.l4` has 221 cases (at least one per question, including a not-covered case where the rule has one).
The questions take plain inputs, one per fact the person can state, each `@desc` worded for that person.
They call the layer-1 rules and restate none.

How the seat handles what a person cannot be asked:

- **A fact another part of the Act answers** (the section 2015 exceptions, the section 2012(m)(4) household test, the Secretary's determination that a tribal organization is capable) is asked as two plain inputs, "do you know?" and "is it so?"; an unknown answer is passed on as `NOTHING`, so the result says the text does not decide it and never "no".
- **The four section 2015 exceptions** of section 2014(a) are asked as one question; the one answer is passed to each of the four inputs.
- **The figures the Act leaves to the Secretary** (the income standards, the standard deduction, the shelter cap, the homeless deduction and the resource limits) are the USDA's figures for fiscal year 2027 (1 October 2026 to 30 September 2027). A different year's figures would change these answers. The person is not asked for them, and there is no fiscal-year input.
- **A record field no rule reads** gets a fixed placeholder with a comment: `snap1 seat a person` builds the `Individual` for section 2014(j) and (l), which read only the age and the SSI flag; the other six fields are placeholders.
- **The net income question** assembles the chain of section 2014(e) from the layer-1 rules in the order the subsection gives. It assumes there is no work supplementation portion, no overissuance, that dependent care is entitled when its cost is entered (the single-rule question asks the rest), and it applies the composition rule above.
- **Fixed fiscal year.** The questions that fix the table year say "2027" in `snap1 seat the fiscal year of the tables`.

**Under section 2012a**
- Under section 2012a, does section 2019 also apply to the publicly operated community health center I use?
**Under section 2013**
- Under section 2013(a)(1), is my household given the opportunity to receive an allotment?
- Under section 2013(a)(1), may I use my benefits for this purchase?
- Under section 2013(b)(2), who is responsible for the food distribution on my reservation?
- Under section 2013(b)(3), am I barred from SNAP because I was disqualified from the food distribution program on Indian reservations?
**Under section 2014(a) to (c)**
- Under section 2014(a), is my household eligible because every member gets cash assistance, SSI or aid to the aged, blind or disabled?
- Under section 2014(a), is my household eligible because every member gets general assistance?
- Under section 2014(a), must assistance be furnished to my household?
- Under section 2014(b), may my State agency require a condition of eligibility that is not one the Secretary set?
- Under section 2014(c)(1), what is the most net income my household may have in a month, in dollars?
- Under section 2014(c)(2), what is the most gross income my household may have in a month, in dollars?
- Under section 2014(c)(1), is my household ineligible because its net income is over the limit?
- Under section 2014(c)(2), is my household ineligible because its gross income is over the limit?
**Under section 2014(d)**
- Under section 2014(d)(1), is a benefit I get that is not money paid to my household left out of my income?
- Under section 2014(d)(3), how much of my educational loan, grant, scholarship or fellowship is left out of my income, in dollars a month?
- Under section 2014(d)(7), is my child's earned income left out of my household's income?
- Under section 2014(d)(11), is my energy assistance payment left out of my income?
- Under section 2014(d)(12), is a cost-of-living increase in my income left out of my household's income?
- Under section 2014(d), how much of my household's income counts each month, in dollars?
**Under section 2014(e)**
- Under section 2014(e)(1), what is my household's standard deduction, in dollars a month?
- Under section 2014(e)(2), what is my household's earned income deduction, in dollars a month?
- Under section 2014(e)(3), what is my household's dependent care deduction, in dollars a month?
- Under section 2014(e)(4), what is my household's child support deduction, in dollars a month?
- Under section 2014(e)(5), what is my household's medical expense deduction, in dollars a month?
- Under section 2014(e)(6), what is my household's excess shelter deduction, in dollars a month?
- Under section 2014(e), what is my household's net income each month, in dollars?
**Under section 2014(f)**
- Under section 2014(f)(1), what is my monthly income if it is averaged over twelve months, in dollars?
- Under section 2014(f)(2), on what basis is my household's income calculated?
**Under section 2014(g)**
- Under section 2014(g), are my household's resources over the limit?
**Under section 2014(h) to (n)**
- Under section 2014(h)(1), will emergency standards of eligibility be set for my household after a disaster?
- Under section 2014(h)(3), how much will be replaced if my food was destroyed in a disaster, in dollars?
- Under section 2014(i)(1), is my sponsor's income and resources counted as mine?
- Under section 2014(i)(2), how much income a month is counted as mine from my sponsor, in dollars?
- Under section 2014(i)(2), how much of my sponsor's resources are counted as mine, in dollars?
- Under section 2014(i)(2)(D), are my sponsor and I both liable for an overpayment?
- Under section 2014(j), am I treated as having met the resource limits because I receive SSI, aid or cash assistance?
- Under section 2014(k)(1), is help paid to my landlord or another third party counted as money paid to my household?
- Under section 2014(k)(3), is an educational award paid to a school for my living expenses counted as money paid to my household?
- Under section 2014(k)(4), is an energy assistance payment made under State law counted as money paid to my household?
- Under section 2014(k)(4), is an energy assistance expense paid for my household under State law counted as one I paid myself?
- Under section 2014(l), are my on-the-job training earnings counted as earned income?
**Under section 2014a**
- Under section 2014a, must my household report that it no longer lives in the State where it is certified?
**Under section 2018**
- Under section 2018(j)(1), is this food an eligible incentive food?
- Under section 2018(j)(2), may I use a store's incentive for this purchase?

## What the text turns out to say

1. **Section 2014(c) says "and" between two grounds of ineligibility, and limits the second to households without an elderly or disabled member** (fork F-C1). Read as written, a household with such a member could never satisfy both limbs.
2. **The USDA's Table 2 is 130 percent of Table 1 only to within a dollar** (finding F-T1). Layer 1 holds the published Table 2 as the gross monthly income limit (`s 2014(c)(2) the gross monthly income limit for the household`), as it holds Table 3 for the 165 percent test: neither the Act (lines 219-222) nor the COLA page says how a percentage of the poverty line is rounded, Table 2 is the only FY 2027 figure in the sources that is stated to be the gross monthly income limit, and 1.3 times the already-rounded Table 1 gives figures that appear in no source (size 2: 2345.2 against the published 2345; up to 1 dollar for sizes 1 to 8, 1.5 for a ninth member in Hawaii, 3 at twelve members in Hawaii). The Act's own words, 30 per centum over a poverty line a caller supplies, stay in `s 2014(c)(2) the household is ineligible because its gross income exceeds the poverty line by more than 30 per centum`, which delegates to `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit` (the rule the seat uses). `snap1-tests-s2014-abc.l4` asserts the closeness for sizes 1 to 8. Changed on 2026-11-04 after the independent review: the first version computed 1.3 times Table 1.
3. **The USDA's standard deductions for sizes 4 to 6 are not exactly 8.31 percent of the rounded Table 1** (finding F-E1): $229 for 4 members against 0.0831 x 2750 = 228.525, and $308 for 6 against 307.22. The Act states no rounding. The formula rule (`s 2014(e)(1)(A) the standard deduction`) gives the unrounded figure and the household rule uses the USDA's table (`s 2014(e)(1) the standard deduction for the household`); both are tested.
4. **The text does not say that income after deductions stops at zero** (fork F-E2). The rule does not floor it.
5. **The quarterly limits of section 2014(d)(2) and (8) are not allocated to months** (fork F-D1).
6. **The educational-award exclusion combines an allowance cap and a fee add-on without saying how** (fork F-D2).
7. **The maximum excess shelter deduction is a chain of indexing from fiscal year 2001**: the text holds the figures for 22 August 1996 to 30 September 2001 and then "the applicable amount during the preceding fiscal year, as adjusted". The Act therefore gives the cap by itself only for those dates; the USDA's figure supplies fiscal year 2027, and every other date is `s 2014(e)(6)(B) cap not covered by this text`. The standard deduction minimum (section 2014(e)(1)(A)(ii)) and the resource limits (section 2014(g)(1)(B)) are indexed the same way and are handled the same way.
8. **The resource limits cannot be derived from the text for 2027.** Subsection (g)(1)(B) adjusts "the amounts specified" each October 1 and rounds down to the nearest $250, and clause (ii) requires each adjustment to be "based on the unrounded amount for the prior 12-month period". Only the rounded USDA figures ($3,000 and $4,750 for fiscal year 2027) are available, so the adjustment function answers `NOTHING` when it is given only a rounded base.
9. **Two subclauses of section 2013(a)(2)(B)(iii) can both apply to one State and give different dates** (fork F-S1).
10. **Section 2014(h)(1), read as written, sets emergency standards only "if ... commercial channels of food distribution have again become available".** The rule follows the words (`JUST FALSE` when they have not), though the policy sense looks reversed. A lawyer should look at the official text and at the References in Text notes before relying on this.
11. **Section 2012a names letters that do not match today's section 2012** (fork F-A1).
12. **A resource can be both included and excluded** (fork F-G1).
13. **The deemed amounts of section 2014(i)(2)(A) and (B) are silent below zero** (fork F-I1), and the second sentence of (C)(i) has no period of its own (fork F-I2).
14. **Section 2014(k)(2) names a class of exceptions that depends on the Secretary's regulations** ("to the extent excluded in regulations"), which are not in the sources: that class is a plain input (fork F-K1).
15. **The date in section 2018(i)(2) can attach to the determination or to the residence** (fork F-S2).
16. **"A period of 2 fiscal years" is not counted from a named year** (fork F-S3).
17. **Section 2018(h)(2)(A) starts a 180-day period at a date the Secretary fixes**, which is an input; before that date the text is silent (fork F-H1).
18. **Section 2014(f)(2)(C) does not yield to subparagraph (B), but (A) and (D) do.** Subparagraph (A) is "Except as provided in subparagraphs (B), (C), and (D)", (D) is "Except as provided in subparagraph (B)", and (C) has no such opening. A household in the first or second month that is also in a clause of section 2015(c)(1)(A) is therefore on two bases at once (B and C); the rule returns `s 2014(f)(2) basis not covered by this text` for it, and so it does for a household that is in both (C) and (D).
19. **The text names only one side of several relations.** Section 2014(a) "assistance ... shall be furnished" names no one who furnishes it; section 2018(g) names the store that must provide adequate EBT service and no one who is owed it; section 2013(b)(6)(A) to (D) name only the Secretary. In the Hohfeld table the unnamed side reads "(not named)"; no actor was invented, and the rules that carry such a duty do not name one either.
20. **Section 2014a is dated.** "Beginning on May 5, 2017 ... a household certified ... is required to report in a manner prescribed by the Secretary"; before 5 May 2017 the rule answers `NOTHING`, and the manner is not in the text.

## What the stable binary does not accept

Observed while writing this part, on 1.6.98 (and the main build 1.6.108 where noted):

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (other than `LEST BREACH ... BECAUSE`). A case outside the encoding returns `NOTHING` or a "not covered" constructor, and that is asserted.
- **A `DEONTIC` value cannot be compared by `#ASSERT`**: both `=` and `NOT =` fail. Each duty has a `#TRACE` (the outcome is printed, not asserted) and a decision-function twin that is asserted (`s 2018(h)(3) the duty to submit the report`, `s 2018(i)(1)(D) the duty to report the results of the reviews`). `check.sh` does not see a `#TRACE` outcome; I ran each trace on both builds and read the outcomes: they are the same.
- **`NOT a AND b` parses as `NOT (a AND b)`**; every `NOT` is parenthesised. `NOT EQUALS` is a parse error; write `NOT (x EQUALS y)`.
- **An `IF ... ELSE ...` inside a `BRANCH` arm raises an indentation error**; the arm calls a helper function instead.
- **A multi-line `LIST` of `OF` records needs each element in parentheses**; a field of a call result needs the call in parentheses, `(f a b)'s \`field\``.
- **A continuation line after `#ASSERT` is rejected**; every `#ASSERT` is on one line.
- **A name the core already holds, or a constructor shared by two types, compiles and errors only where it is used** (PLAN.md naming rule 6). No name of mine collides: every constructor begins with its section label, and the tests touch every constructor.
- **`@export`, `@desc` and a `MEANS` function with a `MAYBE` output and `Area` or `DATE` inputs** compile and run the same on both builds (the seat); I did not deploy the seat to a service.

## Where PLAN.md and the brief differ

I found no place where PLAN.md contradicts the brief in a way that changes an answer.
PLAN.md predates the brief's layer 2, the four dispositions with their three `inert` reasons, the coverage audit and the Hohfeld table, and is silent on them; the brief governs those.
PLAN.md section 4 names per-member and per-individual section 2012 functions; section 2014 asks about households, so I added household-level inputs (see Seams).
PLAN.md lists the Act's own definitions in my ranges as "payment error rate", "traditional and locally- and regionally-grown", "earned income" and "eligible incentive food"; each is encoded (`s 2013(a)(2)(A) ...`, row C032 is inert reason 2 because the Secretary determines the definition of the second, `s 2014(e)(2)(A) the earned income`, `s 2018(j)(1) the food is an eligible incentive food`).

## After the independent review (snap1)

The independent reviewer's tests, run against the merged encoding on 2026-11-04, failed 87 assertions in my range. The lead asked for one verdict on each, judged against the brief's own lists of the grounds for `JUST FALSE` (a definition that says "means"; a condition introduced with "if", "only if", "as long as", "unless", "so long as", "while", "until", "except", "save", "provided that"; a list closed with "only"; a flat negative) and for `NOTHING` (silent; list not closed; "includes"; undefined term; points outside the text; a grant or prohibition limited in its own wording by "without", "when", a stated period or a named complement, and the case falls outside the limit). After the changes below, 60 of the 87 pass and 27 still differ (replaying the 87 lines against this tree gives exactly those 27).

**Changes to the tree**
1. **The gross monthly income limit** (55 of the 87) is the published Table 2 figure, not 1.3 times Table 1 (finding 2, above). `s 2014(c)(2) the gross monthly income limit for the household` keeps its name and type; a new rule `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit` is called by the old rule over a poverty line and by the seat. At Alaska urban, one person, an income of 2162 is not over the limit (the first version said it was, by 10 cents).
2. **Four failed "if" or "except" clauses that answered `NOTHING` now answer `JUST FALSE`**, as their sibling branches already did (the brief's lists; reading (a)):
   - `s 2014(a)` second and third sentences: an excepted provision that applies (section 2015(b), (d)(2), (g), (r); section 2015; section 2025(e)(1); a group that section 2012(m)(4) says is not a household) now gives `JUST FALSE`, quoting "except" (reviewer 82). An exception whose answer is not supplied is still `NOTHING`; one known exception decides even when another is unknown.
   - `s 2014(c)(2)`: the clause "(2) in the case of a household that does not include an elderly or disabled member" is one of the "if" clauses of the ineligibility sentence, so a household that includes such a member fails it: `JUST FALSE`, as a household under the limit already did (reviewer 86c). Under the limit the answer is `JUST FALSE` whether or not the household includes such a member; over it, an unknown answer is `NOTHING`.
   - `s 2014(d)(6)`: a child support payment the household member is not legally obligated to make fails "if the household member is legally obligated" (reviewer 93b).
   - `s 2014(d)(19)`: additional pay of the kind the paragraph names that fails "if the additional pay— (A) ... and (B) ..." (reviewer 97b); pay outside the kind the paragraph names is still `NOTHING`.
3. **Three more places of the same shape**, found by listing every rule whose quoted text carries one of the brief's condition words and which still answered `NOTHING` where the "if" failed: `s 2014(d)(12)` ("if the household was certified ..."), `s 2018(h)(2)(A)` (the sentence's "If, on the day before February 7, 2014 ..."), `s 2018(h)(2)(B)` ("If the Secretary determines to terminate ..."). Each now gives `JUST FALSE` when its "if" fails; the date branches (a stated period) stay `NOTHING`.

4. **`s 2018(c) the sentence is within the limits the subsection sets`** answers `JUST TRUE` inside the limits (a fine of at most $1,000 and a term of at most 1 year) and `JUST FALSE` past them (reviewer 375b). **Assumed, not ruled:** the function is a predicate named for the limit, so it answers the question its own name asks, and the text states the limit; the lead reports that the part `snap6` uses the same rule (I have not read that part). Reading (b) would leave the inside case `NOTHING`, since a ceiling is a prohibition limited by its own wording (BRIEF.md line 56). **To revert this choice alone:** in `snap1-s2018.l4`, the branch `OTHERWISE JUST TRUE` of this function becomes `OTHERWISE NOTHING  -- NOTHING-kind (limited by its own wording): the limits are a ceiling; a sentence within them is not shown to be warranted by this subsection`, and the two assertions at the head of its tests in `snap1-tests-s2018.l4` (inputs `1000 1` and `0 0`) become `EQUALS NOTHING`. `s 2018(d) the store or concern may submit a new application` is named for a permission and is not changed (376b).

**My own expectations that changed:** the layer-1 limit for 2 people in the 48 States (2345.2 to 2345); seat cases "most gross income" for 2 in the 48 States, 3 in Hawaii, 1 in Alaska urban (2345.2, 3404.7, 2161.9 to 2345, 3404, 2162); `s 2014(c)(2)` over a poverty line and over the limit with an elderly or disabled member (`NOTHING` to `JUST FALSE`, 3 assertions); `s 2014(a)` with an excepted provision that applies (`NOTHING` to `JUST FALSE`, 8 assertions); `s 2014(d)(6)` not legally obligated (1); `s 2014(d)(12)` not certified (1); `s 2014(d)(19)` failing (A) or (B) (2); `s 2018(h)(2)(A)` failed "if" (2); `s 2018(h)(2)(B)` (1); `s 2018(c)` within the limits, at 1000 and 1 and at 0 and 0 (`NOTHING` to `JUST TRUE`, 2); seat cases for the same (5).

**The 27 that still differ, and the ground each rests on** (all `NOTHING`, none a defect by the brief's wording; the lawyer's reading (b) is the other way):
- *named class or complement, no condition word:* 80b and 81 ("households in which each member receives"), 94b and 94c ("a child ... who is 17 years of age or younger"; the "excluding only" of the chapeau is closed in `s 2014(d) the monthly amount of the item that counts as income`, which counts an item no paragraph excludes), 109 ("A household containing an elderly or disabled member shall be entitled"), 128b, 128c, 128d ("households— (I) in which ...; (II) that are not receiving ...; (III) that do not opt ..." are relative clauses of a grant), 133b ("those households that ..."), 171b (an exception that names two classes grants nothing to the rest), 75 ("Subject to the availability of appropriations": "subject to" is not on the brief's list; `s 2013(b)(6)(A)` is the sibling and answers the same way).
- *a stated period, case outside it:* 96b ("through September 30"), 153b ("a period of 12 months"), 154b and 720b ("until the expiration of the 1-year period", which ends a duty and does not say "may not"), 165b ("three years"), 178b ("Beginning on May 5, 2017"), 376b ("for at least 6 months ... may establish a longer time period"), 380b ("not to exceed 180 days").
- *the bar is lifted, not turned into a grant:* 121b and 124 ("unless the allowance is prorated"; "shall not apply" is said of the restriction and not of the use of the allowance), 373c ("unless (A) ... or (B) ..."), 374b ("other than a bona fide buyer").
- *an option the household did not take:* 134b.
- *points outside the text:* 70d (the Secretary's determination is a `MAYBE`; `NOTHING` is "not known", and a caller who knows there is none passes `JUST FALSE` and gets the State agency), S1.13 ("follow the regulations in force as of June 1, 1982" decide whether cash counts; the seat's limit is Table 5's $3,000, and savings of $2,500 are counted, so $3,200 in savings and cash is over the limit only if the $700 of cash counts).
- *a fork:* 57 (F-A1).

## Checks

`check.sh` output (stable binary `l4-stable-98`, main build `l4-main-108`, run in this folder):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
snap-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
snap1-cases-seat.l4                            0       221       0        0         0 |      0       221       0        0  same
snap1-logic.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-s2012a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap1-s2013.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-abc.l4                             0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-d.l4                               0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-e1.l4                              0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-e2.l4                              0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-f.l4                               0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-g.l4                               0         0       0        0         0 |      0         0       0        0  same
snap1-s2014-hn.l4                              0         0       0        0         0 |      0         0       0        0  same
snap1-s2014a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap1-s2018.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-s2019.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap1-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
snap1-tests-logic.l4                           0        35       0        0         0 |      0        35       0        0  same
snap1-tests-s2012a.l4                          0         6       0        0         0 |      0         6       0        0  same
snap1-tests-s2013.l4                           0       108       0        0         0 |      0       108       0        0  same
snap1-tests-s2014-abc.l4                       0       104       0        0         0 |      0       104       0        0  same
snap1-tests-s2014-d.l4                         0        91       0        0         0 |      0        91       0        0  same
snap1-tests-s2014-e.l4                         0       155       0        0         0 |      0       155       0        0  same
snap1-tests-s2014-f.l4                         0        60       0        0         0 |      0        60       0        0  same
snap1-tests-s2014-g.l4                         0       121       0        0         0 |      0       121       0        0  same
snap1-tests-s2014-hn.l4                        0       124       0        0         0 |      0       124       0        0  same
snap1-tests-s2014a.l4                          0         7       0        0         0 |      0         7       0        0  same
snap1-tests-s2018.l4                           0       144       0        0         0 |      0       144       0        0  same
snap1-tests-s2019.l4                           0        22       0        0         0 |      0        22       0        0  same
TOTAL (28 modules)                             0      1198       0        0           |      0      1198       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced: the supplied core alone, `snap-core.l4`, 1 module and 0 assertions.
`check.sh` does not see a `#TRACE` outcome; the five traces (sections 2018(h)(3) and 2018(i)(1)(D)) were run on both builds and give the same outcomes.

```
srcrefs.py check --refs   srcrefs check: 384 src: lines, 225 runs, 225 locators, 0 problems
srcrefs.py check --strict srcrefs check: 384 src: lines, 225 runs, 225 locators, 0 problems
verify-quotes             263 quoted pieces checked, 0 not found
```

`verify-quotes` is `work/tools/verify-quotes.py`: it folds punctuation, case and spacing and checks every quotation piece against the text.
The expected values of the tests are written from the text, with the USDA's FY2027 figures for the income standards, the standard deduction, the shelter cap and the resource limits; none is copied from a run.
The seat cases are asserted on both builds; a wrong expected value was shown to fail (a positive control) before the cases were trusted.
