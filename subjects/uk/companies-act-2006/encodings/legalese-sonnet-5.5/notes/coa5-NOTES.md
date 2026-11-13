# NOTES (coa5): Companies Act 2006 (United Kingdom), 2006 c. 46, sections 205 to 269

Part agent `coa5`, encoding `legalese-sonnet-5.5`, lines 2697-3566 of `ukpga-2006-46.txt`: the rest of Part 10 (Chapter 4 from section 205, then Chapters 4A, 5, 6, 7, 8, 9 and 10; section 226 is blank in this text) and all of Part 11 (derivative claims and proceedings by members, Chapters 1 and 2).

**The source is a converter rendering, not the official text.**
`ukpga-2006-46.txt` is a plain-text rendering of the Act made by a converter script.
Nothing in this encoding is "verified against the official text".
What was checked is narrower: every quoted sentence in a `-- src:` line was compared with that file by `srcrefs.py` (`check --refs` and `check --strict`, 0 problems on every file), and every expected value in the tests was written from the text, with the brief's rulings applied.
No assertion in the final files fails or is refused.

## What is here

Two layers, as the brief asks.
Layer 1 is isomorphic to the text: each module quotes its sentences (`-- src:`), cites them with `@ref`, names every function, type and constructor with its section label (`s 217(1) ...`), and answers `MAYBE BOOLEAN` or a typed value under the rule of 2026-10-29 (see "Reading a result").
Layer 2 is the seat layer: `coa5-seat.l4` (239 `@export`ed questions, each named "Under section N, ...", with plain inputs worded for the person asking) and `coa5-cases-seat.l4` (498 cases, every question has at least one, including cases that answer NOTHING).

| module | sections | what it holds | tests | assertions satisfied | `#TRACE`s |
| --- | --- | --- | --- | --- | --- |
| `coa5-loans-exceptions.l4` | ss 205 to 214 | Chapter 4: exceptions to the need for members' approval of loans, quasi-loans and credit transactions; the value, the person for whom; civil consequences (ss 213, 214) | `coa5-tests-loans-exceptions.l4` | 182 | 0 |
| `coa5-loss-of-office.l4` | ss 215 to 222 | Chapter 4: payments for loss of office | `coa5-tests-loss-of-office.l4` | 189 | 3 |
| `coa5-ch4-supplementary.l4` | ss 223 to 226 | Chapter 4: shadow directors, accidental failure to send a memorandum, more than one approval (s 226 is blank in this text) | `coa5-tests-ch4-supplementary.l4` | 26 | 0 |
| `coa5-quoted-company-pay.l4` | ss 226A to 226F | Chapter 4A: directors of quoted companies | `coa5-tests-quoted-company-pay.l4` | 120 | 3 |
| `coa5-service-contracts.l4` | ss 227 to 231 | Chapter 5 (directors' service contracts) and Chapter 6 (sole member who is also a director) | `coa5-tests-service-contracts.l4` | 91 | 8 |
| `coa5-director-liabilities.l4` | ss 232 to 239 | Chapter 7: provisions exempting or indemnifying a director, qualifying indemnities, ratification | `coa5-tests-director-liabilities.l4` | 169 | 4 |
| `coa5-residential-addresses.l4` | ss 240 to 246 | Chapter 8: directors' residential addresses | `coa5-tests-residential-addresses.l4` | 97 | 3 |
| `coa5-director-supplementary.l4` | ss 247 to 249, 258, 259 | Chapter 9 (employees on cessation of business; minutes) and the general provisions at the end of Chapter 10 | `coa5-tests-director-supplementary.l4` | 54 | 2 |
| `coa5-director-definitions.l4` | ss 250 to 257 | Chapter 10: director, shadow director, connected persons, family, control, associated bodies, constitution | `coa5-tests-director-definitions.l4` | 110 | 0 |
| `coa5-derivative-claims.l4` | ss 260 to 269 | Part 11: derivative claims (Chapter 1) and derivative proceedings in Scotland (Chapter 2) | `coa5-tests-derivative-claims.l4` | 228 | 4 |

The seat layer and its cases are in `coa5-seat.l4` and `coa5-cases-seat.l4`; their counts are in "What check.sh prints".
Every file is `coa5-` prefixed, ASCII-named, and defines no name the core or another part could define.
Layer 1 imports the keel's `coa-core`; `coa-definitions.l4` (the keel's borrowed-term functions) is supplied and not imported by any of these files, because each module takes the borrowed facts as inputs named for the answering section (see "Seams").


## Seat (coa5)

**The seat is an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one.**
(Assumed, not ruled: the Act is addressed to companies and to the officers and members who stand behind them, so the person in the seat is whoever holds one of those places.)
They ask, on facts they can state, what the Act requires or lets them do, what rights they have against the company or its directors, what they must file, disclose, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done.
No official has a seat: the registrar, the court and the Secretary of State appear only as what the person can ask of them or must expect from them.

- **Questions:** 239 in 69 sections (every section of ss 205-269 except s 226, which is blank, and the machinery rows listed as `inert` in the coverage table; s 241(4)'s penalty record and the duty-as-rule rules are served by layer 1 only).
- **Names:** "Under section N, ..." or "Under section N(M), ..." as the brief requires; the one shared helper is `s 229(4) the most in pounds that a fine limit allows`.
- **Inputs are plain.** Yes/no, a number, a date, each with a `@desc` worded as the person is asked.
  Where a question needs another question's answer (is the person a shadow director, a connected person, a member of the family; is the memorandum available on time) it builds the answer inside, from plain facts, by calling the layer-1 rule; it never restates the rule.
  Where the chain would triple the question's size the sub-answer is asked as a plain fact named in the person's words and the question says so in its `@desc` (the member-or-connected-with-the-director inputs of s 239(3) and (4); the court's satisfaction in ss 263 and 268).
- **A person cannot state NOTHING.** The answers other parts give (s 1121 "in default", s 112 "member", s 1159 "subsidiary", s 988 "associate", s 1136 regulations, s 17, s 629, s 385) are asked as plain yes/no facts and passed to the layer-1 rule as `JUST` answers.
  So a seat question answers NOTHING only where the layer-1 rule does on the facts stated, and never because a seam was unknown.
- **There is no "I do not know" input.** A caller who does not know a seam's answer should call the layer-1 function directly with `NOTHING` for that seam and read the result as "not covered".
- **Money:** the sums the Act itself states (ss 207, 211, 221) are used as the Act states them.
  What a "level" on the standard scale stands for in pounds is not in the sources, so the penalty questions of ss 228(6), 229(4), 231(4), 237(7) and 238(4) take it as a number; the answer is that number, times one-tenth for the daily default fine.
  Section 258 lets the Secretary of State substitute larger sums; an order would change the answers of ss 207, 211 and 221 (finding 2).

| group | questions |
| --- | --- |
| Chapter 4: loans, quasi-loans and credit transactions with directors: exceptions to the need for members' approval (ss 205 to 214) | 16 |
| Chapter 4, payments for loss of office (ss 215 to 222) and the supplementary sections (ss 223 to 226) | 18 |
| Chapter 4A: directors of quoted companies: special provision (ss 226A to 226F) | 6 |
| Chapter 5: directors' service contracts (ss 227 to 230) and contracts with a sole member who is also a director (s 231) | 25 |
| Chapter 7: directors' liabilities (ss 232 to 239) | 42 |
| Chapter 8: directors' residential addresses: protection from disclosure (ss 240 to 246) | 29 |
| Chapter 9: supplementary provisions regarding directors (ss 247 to 249) | 15 |
| Chapter 10: interpretation of Part 10 (ss 250 to 259) | 29 |
| Part 11, Chapter 1: derivative claims in England and Wales or Northern Ireland (ss 260 to 264) | 26 |
| Part 11, Chapter 2: derivative proceedings in Scotland (ss 265 to 269) | 33 |


### Seat audit of 2026-11-12 (name against function)

The team lead asked for every seat question's name and `@export` text to be read against the layer-1 function its body calls, because a defect class had been found in other parts: a question named as a permission ("may I", "can the company") whose function returns the bar (`... may not ...`, `no person may ...`), or the reverse, or a question named "must I" / "how" / "may I take over" whose function answers "have I" / a yes-or-no / "may I apply".

**Result:** 239 seat questions read; **23 mismatched** (13 direction, 10 subject); 21 questions renamed and 2 had their `@export` text only corrected (ss 247(3) and 247(6): the name was right, the text said the opposite or something else).
Retitling was the fix; no answer was negated (a bar's NOTHING and JUST FALSE are not a grant).
The layer-1 functions are untouched.
The 47 assertions of the renamed questions were restated in place in `coa5-cases-seat.l4`, each with `-- RECONCILED 2026-11-12: was <the original assertion text>; <reason>`; the facts and the expected values did not change, and the case total is still 498.

| section | kind | the name before | the name now |
| --- | --- | --- | --- |
| s 214 | direction | `Under section 214, can the company still avoid the transaction after it was affirmed` | `Under section 214, is the transaction one that may no longer be avoided because the members affirmed it` |
| s 217(1) | direction | `Under section 217(1), may my company pay me for loss of office without members' approval` | `Under section 217(1), is my company barred from paying me for loss of office without members' approval` |
| s 218(1) | direction | `Under section 218(1), may a payment be made to me in connection with a transfer of the company's business without approval` | `Under section 218(1), is no person allowed to pay me for loss of office in connection with a transfer of the company's business without approval` |
| s 219(1) | direction | `Under section 219(1), may a payment be made to me in connection with a takeover bid without approval of the shareholders` | `Under section 219(1), is no person allowed to pay me for loss of office in connection with a takeover bid without approval of the shareholders` |
| s 226B(1) | direction | `Under section 226B(1), may my quoted company make me a remuneration payment` | `Under section 226B(1), is my quoted company barred from making me a remuneration payment` |
| s 226C(1) | direction | `Under section 226C(1), may a quoted company pay me for loss of office` | `Under section 226C(1), is no person allowed to pay me for loss of office from a quoted company unless the payment is consistent with the policy or approved` |
| s 239(4) | direction | `Under section 239(4), may I attend and take part in the meeting that ratifies a director's conduct` | `Under section 239(4), am I prevented from attending and taking part in the meeting that ratifies a director's conduct` |
| s 241(1) | direction | `Under section 241(1), may my company use or disclose my residential address` | `Under section 241(1), is my company barred from using or disclosing my residential address` |
| s 242(3) | direction | `Under section 242(3), may the registrar disclose my protected information` | `Under section 242(3), is the registrar barred from making this disclosure of my protected information` |
| s 246(4) | direction | `Under section 246(4), may a service address be registered for me after my address was published` | `Under section 246(4), is no service address other than my usual residential address allowed to be registered for me after my address was published` |
| s 247(3) | direction | `Under section 247(3), does a restriction from the company's objects stop a charity's directors` | unchanged (the `@export` text was corrected) |
| s 265(2) | direction | `Under section 265(2), may I raise such proceedings other than under section 265(1)` | `Under section 265(2), may I raise such proceedings in this way, which the Act allows only under section 265(1)` |
| s 266(1) | direction | `Under section 266(1), may I raise derivative proceedings without the court's leave` | `Under section 266(1), may I raise derivative proceedings, which the Act allows only with the court's leave` |
| s 225(2) | subject | `Under section 225(2), must every approval requirement be met when two sections apply` | `Under section 225(2), has approval been given as Chapter 4 requires where it is needed under more than one provision` |
| s 234(4) | subject | `Under section 234(4), does the conviction, judgment or refusal of relief count when it is not yet final` | `Under section 234(4), does the conviction, judgment or refusal of relief count for the exclusion in section 234(3)(b)` |
| s 235(4) | subject | `Under section 235(4), does the conviction count when it is not yet final` | `Under section 235(4), does the conviction count for the exclusion in section 235(3)(b)` |
| s 241(2) | subject | `Under section 241(2), has the director consented to the use or disclosure of the protected information` | `Under section 241(2), does section 241(1) prohibit use or disclosure of protected information where the director has consented` |
| s 247(6) | subject | `Under section 247(6), have the other requirements of my articles been complied with for that power` | unchanged (the `@export` text was corrected) |
| s 260(2) | subject | `Under section 260(2), how may I bring a derivative claim` | `Under section 260(2), may my derivative claim be brought by this route, which the Act allows only under Chapter 1 or a section 994 order` |
| s 262(2) | subject | `Under section 262(2), may I, a member, take over the company's claim` | `Under section 262(2), may I, a member, apply for permission to continue the company's claim as a derivative claim` |
| s 264(2) | subject | `Under section 264(2), may I, another member, take over the claim the claimant is running` | `Under section 264(2), may I, another member, apply for permission to continue the claim the claimant is running` |
| s 267(2) | subject | `Under section 267(2), may I, a member, be substituted for the company in its proceedings` | `Under section 267(2), may I, a member, apply to be substituted for the company in its proceedings` |
| s 269(2) | subject | `Under section 269(2), may I, another member, be substituted for the claimant` | `Under section 269(2), may I, another member, apply to be substituted for the claimant` |


## Coverage (coa5)

Lines 2697-3566 hold 870 non-blank lines of text.
The table has **817 rows**, one per section, subsection, paragraph, sub-paragraph, cross-heading, chapter or Part heading, dotted blank line and defined term, built by a script that reads the text (so no unit is skipped by hand) and then given a disposition from a hand-written map.
Rows are kept at their finest unit; a row marked "(in s 243(3))" falls under its parent's disposition.
Dispositions, counted over the 817 rows: **encoded 565, fork 200, inert 45 (reason 1: 22; reason 2: 23; reason 3: 0), repealed or blank in this text 7; total 817**; no row is left undecided.
A `fork` row points at its entry in the fork register and at the rule that encodes the reading taken.
There is no `out-of-scope` and no `deferred` row.
Every row that is `inert` has reason 1 (not operative: headings and one signpost, s 245(6)) or reason 2 (machinery: regulation-making powers and their procedure, ss 243(3), (5), (6), (6A), (8), 258(1), (2), 263(5)-(7), 268(4)-(6)); none has reason 3.
The seven `repealed or blank in this text` rows are s 215(6) (line 2840, dots only), s 226 (lines 2947-2948: the heading is followed by dots only) and the dotted line under it, the dotted line at 2962 (after the definitions of s 226A(1)), s 226A(10)(b) (2984), s 243(1) (3211) and the dotted line at 3226 (in s 243(7)).

| unit | kind | lines | disposition | L4 name (or the row it falls in) |
| --- | --- | --- | --- | --- |
| s 205 | section | 2697-2721 | encoded | see its subsections |
| s 205(1) | subsection | 2698-2703 | encoded | `s 205(1) approval under sections 197, 198, 200 and 201 is not required by this section` |
| s 205(1)(a) | paragraph | 2699-2701 | encoded | (in s 205(1)) |
| s 205(1)(a)(i) | sub-paragraph | 2700-2700 | encoded | (in s 205(1)) |
| s 205(1)(a)(ii) | sub-paragraph | 2701-2701 | encoded | (in s 205(1)) |
| s 205(1)(b) | paragraph | 2702-2703 | encoded | (in s 205(1)) |
| s 205(2) | subsection | 2704-2712 | fork F-205-1 | `s 205(2) the terms are met` |
| s 205(2)(a) | paragraph | 2705-2708 | fork F-205-1 | (in s 205(2)) |
| s 205(2)(a)(i) | sub-paragraph | 2706-2706 | fork F-205-1 | (in s 205(2)) |
| s 205(2)(a)(ii) | sub-paragraph | 2707-2707 | fork F-205-1 | (in s 205(2)) |
| s 205(2)(a)(iii) | sub-paragraph | 2708-2708 | fork F-205-1 | (in s 205(2)) |
| s 205(2)(b) | paragraph | 2709-2712 | fork F-205-1 | (in s 205(2)) |
| s 205(2)(b)(i) | sub-paragraph | 2710-2710 | fork F-205-1 | (in s 205(2)) |
| s 205(2)(b)(ii) | sub-paragraph | 2711-2711 | fork F-205-1 | (in s 205(2)) |
| s 205(2)(b)(iii) | sub-paragraph | 2712-2712 | fork F-205-1 | (in s 205(2)) |
| s 205(3) | subsection | 2713-2715 | encoded | `s 205(3) the date when the conviction, judgment or refusal of relief becomes final` |
| s 205(3)(a) | paragraph | 2714-2714 | encoded | (in s 205(3)) |
| s 205(3)(b) | paragraph | 2715-2715 | encoded | (in s 205(3)) |
| s 205(4) | subsection | 2716-2718 | encoded | `s 205(4) the appeal is disposed of` |
| s 205(4)(a) | paragraph | 2717-2717 | encoded | (in s 205(4)) |
| s 205(4)(b) | paragraph | 2718-2718 | encoded | (in s 205(4)) |
| s 205(5) | subsection | 2719-2721 | encoded | `s 205(5) the application is an application for relief` (+ type `s 205(5) provision for relief`) |
| s 206 | section | 2722-2728 | encoded | `s 206 approval under sections 197, 198, 200 and 201 is not required by this section` |
| s 206(a) | paragraph | 2724-2727 | encoded | (in s 206) |
| s 206(a)(i) | sub-paragraph | 2725-2725 | encoded | (in s 206) |
| s 206(a)(ii) | sub-paragraph | 2726-2727 | encoded | (in s 206) |
| s 206(b) | paragraph | 2728-2728 | encoded | (in s 206) |
| s 207 | section | 2729-2740 | encoded | see its subsections |
| s 207(1) | subsection | 2730-2733 | encoded | `s 207(1) approval under sections 197, 198 and 200 is not required by this section` (+ `s 207(1) the sum in pounds`) |
| s 207(1)(a) | paragraph | 2731-2731 | encoded | (in s 207(1)) |
| s 207(1)(b) | paragraph | 2732-2733 | encoded | (in s 207(1)) |
| s 207(2) | subsection | 2734-2737 | encoded | `s 207(2) approval under section 201 is not required by this section` (+ `s 207(2) the sum in pounds`) |
| s 207(2)(a) | paragraph | 2735-2735 | encoded | (in s 207(2)) |
| s 207(2)(b) | paragraph | 2736-2737 | encoded | (in s 207(2)) |
| s 207(3) | subsection | 2738-2740 | encoded | `s 207(3) approval under section 201 is not required by this section` |
| s 207(3)(a) | paragraph | 2739-2739 | encoded | (in s 207(3)) |
| s 207(3)(b) | paragraph | 2740-2740 | encoded | (in s 207(3)) |
| s 208 | section | 2741-2747 | encoded | `s 208 approval is not required by this section` |
| s 208(1) | subsection | 2742-2744 | encoded | (in s 208) |
| s 208(1)(a) | paragraph | 2743-2743 | encoded | (in s 208) |
| s 208(1)(b) | paragraph | 2744-2744 | encoded | (in s 208) |
| s 208(2) | subsection | 2745-2747 | encoded | (in s 208) |
| s 208(2)(a) | paragraph | 2746-2746 | encoded | (in s 208) |
| s 208(2)(b) | paragraph | 2747-2747 | encoded | (in s 208) |
| s 209 | section | 2748-2760 | encoded | see its subsections |
| s 209(1) | subsection | 2749-2751 | fork F-209-1 | `s 209(1) approval under sections 197, 198 and 200 is not required by this section` |
| s 209(1)(a) | paragraph | 2750-2750 | fork F-209-1 | (in s 209(1)) |
| s 209(1)(b) | paragraph | 2751-2751 | fork F-209-1 | (in s 209(1)) |
| s 209(2) | subsection | 2752-2752 | encoded | `s 209(2) the company is a money-lending company` |
| s 209(3) | subsection | 2753-2756 | encoded | `s 209(3) the condition in subsection (1)(b) does not of itself prevent the company from making the home loan` |
| s 209(3)(a) | paragraph | 2754-2754 | encoded | (in s 209(3)) |
| s 209(3)(b) | paragraph | 2755-2756 | encoded | (in s 209(3)) |
| s 209(4) | subsection | 2757-2760 | encoded | `s 209(4) the loan is a home loan` |
| s 209(4)(a) | paragraph | 2758-2758 | encoded | (in s 209(4)) |
| s 209(4)(b) | paragraph | 2759-2759 | encoded | (in s 209(4)) |
| s 209(4)(c) | paragraph | 2760-2760 | encoded | (in s 209(4)) |
| s 210 | section | 2761-2776 | encoded | see its subsections |
| s 210(1) | subsection | 2762-2763 | encoded | `s 210(1) this section has effect for determining the other relevant transactions or arrangements` |
| s 210(2) | subsection | 2764-2764 | fork F-210-1 | `s 210(2) the other transaction or arrangement is a relevant transaction or arrangement` |
| s 210(3) | subsection | 2765-2768 | encoded | `s 210(3) the conditions are met` |
| s 210(3)(a) | paragraph | 2766-2766 | encoded | (in s 210(3)) |
| s 210(3)(b) | paragraph | 2767-2768 | encoded | (in s 210(3)) |
| s 210(4) | subsection | 2769-2772 | encoded | `s 210(4) the conditions are met` |
| s 210(4)(a) | paragraph | 2770-2770 | encoded | (in s 210(4)) |
| s 210(4)(b) | paragraph | 2771-2772 | encoded | (in s 210(4)) |
| s 210(5) | subsection | 2773-2776 | encoded | `s 210(5) the transaction or arrangement is not a relevant transaction or arrangement` |
| s 210(5)(a) | paragraph | 2774-2774 | encoded | (in s 210(5)) |
| s 210(5)(b) | paragraph | 2775-2776 | encoded | (in s 210(5)) |
| s 211 | section | 2777-2789 | encoded | see its subsections |
| s 211(1) | subsection | 2778-2780 | encoded | `s 211(1)(a) the value of the transaction or arrangement` and `s 211(1)(b) the value of an other relevant transaction or arrangement` (type `s 211 value`) |
| s 211(1)(a) | paragraph | 2779-2779 | encoded | (in s 211(1)) |
| s 211(1)(b) | paragraph | 2780-2780 | fork F-211-1 | `s 211(1)(b) the value of an other relevant transaction or arrangement` |
| s 211(2) | subsection | 2781-2781 | encoded | `s 211(2) the value of a loan` |
| s 211(3) | subsection | 2782-2782 | encoded | `s 211(3) the value of a quasi-loan` |
| s 211(4) | subsection | 2783-2783 | encoded | `s 211(4) the value of a credit transaction` |
| s 211(5) | subsection | 2784-2784 | encoded | `s 211(5) the value of a guarantee or security` |
| s 211(6) | subsection | 2785-2785 | encoded | `s 211(6) the value of an arrangement to which section 203 applies` |
| s 211(7) | subsection | 2786-2789 | encoded | `s 211(7) the value is deemed to exceed 50,000 pounds` and `s 211(7) the aggregate of the two values exceeds the sum` |
| s 211(7)(a) | paragraph | 2787-2787 | encoded | (in s 211(7)) |
| s 211(7)(b) | paragraph | 2788-2789 | encoded | (in s 211(7)) |
| s 212 | section | 2790-2795 | encoded | `s 212 the person for whom the transaction or arrangement is entered into` |
| s 212(a) | paragraph | 2792-2792 | encoded | (in s 212) |
| s 212(b) | paragraph | 2793-2793 | encoded | (in s 212) |
| s 212(c) | paragraph | 2794-2794 | encoded | (in s 212) |
| s 212(d) | paragraph | 2795-2795 | encoded | (in s 212) |
| s 213 | section | 2796-2816 | encoded | see its subsections |
| s 213(1) | subsection | 2797-2797 | encoded | `s 213(1) this section applies` |
| s 213(2) | subsection | 2798-2801 | fork F-213-2 | `s 213(2) the transaction or arrangement is voidable at the instance of the company` |
| s 213(2)(a) | paragraph | 2799-2799 | fork F-213-2 | (in s 213(2)) |
| s 213(2)(b) | paragraph | 2800-2800 | fork F-213-2 | (in s 213(2)) |
| s 213(2)(c) | paragraph | 2801-2801 | fork F-213-2 | (in s 213(2)) |
| s 213(3) | subsection | 2802-2804 | encoded | `s 213(3) the person is liable to account to the company for any gain and to indemnify it for any loss` (+ (3)(a), (3)(b) amounts) |
| s 213(3)(a) | paragraph | 2803-2803 | encoded | (in s 213(3)) |
| s 213(3)(b) | paragraph | 2804-2804 | encoded | (in s 213(3)) |
| s 213(4) | subsection | 2805-2809 | fork F-213-1 | `s 213(4) the person is one of the persons liable` |
| s 213(4)(a) | paragraph | 2806-2806 | fork F-213-1 | (in s 213(4)) |
| s 213(4)(b) | paragraph | 2807-2807 | fork F-213-1 | (in s 213(4)) |
| s 213(4)(c) | paragraph | 2808-2808 | fork F-213-1 | (in s 213(4)) |
| s 213(4)(d) | paragraph | 2809-2809 | fork F-213-1 | (in s 213(4)) |
| s 213(5) | subsection | 2810-2810 | encoded | `s 213(5) the liability is subject to subsections (6) and (7)` (applied in `s 213(3)`) |
| s 213(6) | subsection | 2811-2811 | encoded | `s 213(6) the director is not liable by virtue of subsection (4)(c)` |
| s 213(7) | subsection | 2812-2815 | encoded | `s 213(7) the person is not liable by virtue of subsection (4)(b) or (d)` |
| s 213(7)(a) | paragraph | 2813-2813 | encoded | (in s 213(7)) |
| s 213(7)(b) | paragraph | 2814-2815 | encoded | (in s 213(7)) |
| s 213(8) | subsection | 2816-2816 | encoded | `s 213(8) this section excludes the operation of any other enactment or rule of law` |
| s 214 | section | 2817-2821 | encoded | `s 214 the transaction or arrangement may no longer be avoided under section 213` |
| s 214(a) | paragraph | 2819-2819 | encoded | (in s 214) |
| s 214(b) | paragraph | 2820-2821 | encoded | (in s 214) |
| heading@2822 | cross-heading | 2822-2822 | inert 1 | not operative: a heading (cross-heading) |
| s 215 | section | 2823-2840 | encoded | see its subsections |
| s 215(1) | subsection | 2824-2832 | encoded | `s 215(1) the payment is a payment for loss of office` (+ type `s 215(1) nature of the payment`) |
| s 215(1)(a) | paragraph | 2825-2825 | encoded | (in s 215(1)) |
| s 215(1)(b) | paragraph | 2826-2828 | encoded | (in s 215(1)) |
| s 215(1)(b)(i) | sub-paragraph | 2827-2827 | encoded | (in s 215(1)) |
| s 215(1)(b)(ii) | sub-paragraph | 2828-2828 | encoded | (in s 215(1)) |
| s 215(1)(c) | paragraph | 2829-2829 | encoded | (in s 215(1)) |
| s 215(1)(d) | paragraph | 2830-2832 | encoded | (in s 215(1)) |
| s 215(1)(d)(i) | sub-paragraph | 2831-2831 | encoded | (in s 215(1)) |
| s 215(1)(d)(ii) | sub-paragraph | 2832-2832 | encoded | (in s 215(1)) |
| s 215(2) | subsection | 2833-2833 | encoded | `s 215(2) the benefit counts as compensation, consideration or payment` |
| s 215(3) | subsection | 2834-2837 | encoded | `s 215(3) the payment is treated as payment to the director` |
| s 215(3)(a) | paragraph | 2835-2835 | encoded | (in s 215(3)) |
| s 215(3)(b) | paragraph | 2836-2837 | encoded | (in s 215(3)) |
| s 215(4) | subsection | 2838-2838 | encoded | `s 215(4) the payment is treated as a payment by the person` |
| s 215(5) | subsection | 2839-2839 | encoded | `s 215(5) section 215 and sections 216 to 222 apply to the payment` |
| s 215(6) | subsection | 2840-2840 | repealed or blank in this text | the text shows only dots |
| s 216 | section | 2841-2850 | encoded | see its subsections |
| s 216(1) | subsection | 2842-2846 | encoded | `s 216(1) this section applies` |
| s 216(1)(a) | paragraph | 2843-2843 | encoded | (in s 216(1)) |
| s 216(1)(b) | paragraph | 2844-2846 | encoded | (in s 216(1)) |
| s 216(1)(b)(i) | sub-paragraph | 2845-2845 | encoded | (in s 216(1)) |
| s 216(1)(b)(ii) | sub-paragraph | 2846-2846 | encoded | (in s 216(1)) |
| s 216(2) | subsection | 2847-2850 | encoded | `s 216(2)(a) the excess taken to have been a payment for loss of office` and `s 216(2)(b) the money value taken to have been a payment for loss of office` |
| s 216(2)(a) | paragraph | 2848-2848 | encoded | (in s 216(2)) |
| s 216(2)(b) | paragraph | 2849-2850 | encoded | (in s 216(2)) |
| s 217 | section | 2851-2861 | encoded | see its subsections |
| s 217(1) | subsection | 2852-2852 | fork F-UNLESS-1 | `s 217(1) the company may not make the payment` (+ duty `s 217(1) and (2) the company's duty not to make the payment`) |
| s 217(2) | subsection | 2853-2853 | fork F-UNLESS-1 | `s 217(2) the company may not make the payment` (+ the same duty) |
| s 217(3) | subsection | 2854-2858 | fork F-UNLESS-1 | `s 217(3) the resolution approving the payment must not be passed` (+ type `s 217(3) memorandum`) |
| s 217(3)(a) | paragraph | 2855-2855 | fork F-UNLESS-1 | (in s 217(3)) |
| s 217(3)(b) | paragraph | 2856-2858 | fork F-UNLESS-1 | (in s 217(3)) |
| s 217(3)(b)(i) | sub-paragraph | 2857-2857 | fork F-UNLESS-1 | (in s 217(3)) |
| s 217(3)(b)(ii) | sub-paragraph | 2858-2858 | fork F-UNLESS-1 | (in s 217(3)) |
| s 217(4) | subsection | 2859-2861 | encoded | `s 217(4) no approval is required under section 217 on the part of the members of the body corporate` |
| s 217(4)(a) | paragraph | 2860-2860 | encoded | (in s 217(4)) |
| s 217(4)(b) | paragraph | 2861-2861 | encoded | (in s 217(4)) |
| s 218 | section | 2862-2876 | encoded | see its subsections |
| s 218(1) | subsection | 2863-2863 | fork F-UNLESS-1 | `s 218(1) no person may make the payment` |
| s 218(2) | subsection | 2864-2864 | fork F-UNLESS-1 | `s 218(2) no person may make the payment` |
| s 218(3) | subsection | 2865-2869 | fork F-UNLESS-1 | `s 218(3) the resolution approving the payment must not be passed` (+ type `s 218(3) memorandum`) |
| s 218(3)(a) | paragraph | 2866-2866 | fork F-UNLESS-1 | (in s 218(3)) |
| s 218(3)(b) | paragraph | 2867-2869 | fork F-UNLESS-1 | (in s 218(3)) |
| s 218(3)(b)(i) | sub-paragraph | 2868-2868 | fork F-UNLESS-1 | (in s 218(3)) |
| s 218(3)(b)(ii) | sub-paragraph | 2869-2869 | fork F-UNLESS-1 | (in s 218(3)) |
| s 218(4) | subsection | 2870-2872 | encoded | `s 218(4) no approval is required under section 218 on the part of the members of the body corporate` |
| s 218(4)(a) | paragraph | 2871-2871 | encoded | (in s 218(4)) |
| s 218(4)(b) | paragraph | 2872-2872 | encoded | (in s 218(4)) |
| s 218(5) | subsection | 2873-2876 | fork F-218-1 | `s 218(5) the payment is presumed to be a payment to which section 218 applies` |
| s 218(5)(a) | paragraph | 2874-2874 | fork F-218-1 | (in s 218(5)) |
| s 218(5)(b) | paragraph | 2875-2876 | fork F-218-1 | (in s 218(5)) |
| s 219 | section | 2877-2895 | encoded | see its subsections |
| s 219(1) | subsection | 2878-2878 | fork F-UNLESS-1 | `s 219(1) no person may make the payment` |
| s 219(2) | subsection | 2879-2879 | fork F-219-1 | `s 219(2) the holder is one of the relevant shareholders` |
| s 219(3) | subsection | 2880-2884 | fork F-UNLESS-1 | `s 219(3) the resolution approving the payment must not be passed` (+ type `s 219(3) memorandum`) |
| s 219(3)(a) | paragraph | 2881-2881 | fork F-UNLESS-1 | (in s 219(3)) |
| s 219(3)(b) | paragraph | 2882-2884 | fork F-UNLESS-1 | (in s 219(3)) |
| s 219(3)(b)(i) | sub-paragraph | 2883-2883 | fork F-UNLESS-1 | (in s 219(3)) |
| s 219(3)(b)(ii) | sub-paragraph | 2884-2884 | fork F-UNLESS-1 | (in s 219(3)) |
| s 219(4) | subsection | 2885-2887 | encoded | `s 219(4) the person is entitled to vote on the resolution`, `s 219(4)(a) the person is entitled to be sent a copy of the written resolution`, `s 219(4)(b) the person is entitled to notice of the meeting, to attend and speak and, if present, to count towards the quorum` |
| s 219(4)(a) | paragraph | 2886-2886 | encoded | (in s 219(4)) |
| s 219(4)(b) | paragraph | 2887-2887 | encoded | (in s 219(4)) |
| s 219(5) | subsection | 2888-2888 | encoded | `s 219(5) the payment is deemed to have been approved` |
| s 219(6) | subsection | 2889-2891 | encoded | `s 219(6) no approval is required under section 219 on the part of the shareholders in the body corporate` |
| s 219(6)(a) | paragraph | 2890-2890 | encoded | (in s 219(6)) |
| s 219(6)(b) | paragraph | 2891-2891 | encoded | (in s 219(6)) |
| s 219(7) | subsection | 2892-2895 | fork F-218-1 | `s 219(7) the payment is presumed to be a payment to which section 219 applies` |
| s 219(7)(a) | paragraph | 2893-2893 | fork F-218-1 | (in s 219(7)) |
| s 219(7)(b) | paragraph | 2894-2895 | fork F-218-1 | (in s 219(7)) |
| s 220 | section | 2896-2905 | encoded | see its subsections |
| s 220(1) | subsection | 2897-2901 | fork F-220-1 | `s 220(1) approval under section 217, 218 or 219 is not required by this section` (+ type `s 220(1) ground`) |
| s 220(1)(a) | paragraph | 2898-2898 | fork F-220-1 | (in s 220(1)) |
| s 220(1)(b) | paragraph | 2899-2899 | fork F-220-1 | (in s 220(1)) |
| s 220(1)(c) | paragraph | 2900-2900 | fork F-220-1 | (in s 220(1)) |
| s 220(1)(d) | paragraph | 2901-2901 | fork F-220-1 | (in s 220(1)) |
| s 220(2) | subsection | 2902-2902 | encoded | `s 220(2) the obligation is an existing legal obligation` |
| s 220(3) | subsection | 2903-2903 | encoded | `s 220(3) the obligation is an existing legal obligation` |
| s 220(4) | subsection | 2904-2904 | encoded | `s 220(4) which definition of an existing legal obligation applies` |
| s 220(5) | subsection | 2905-2905 | encoded | `s 220(5) the amount of the separate payment that is not within subsection (1)` |
| s 221 | section | 2906-2917 | encoded | see its subsections |
| s 221(1) | subsection | 2907-2909 | encoded | `s 221(1) approval under section 217, 218 or 219 is not required by this section` (+ `s 221(1) the sum in pounds`) |
| s 221(1)(a) | paragraph | 2908-2908 | encoded | (in s 221(1)) |
| s 221(1)(b) | paragraph | 2909-2909 | encoded | (in s 221(1)) |
| s 221(2) | subsection | 2910-2910 | encoded | `s 221(2) the other payment is one of the other relevant payments` |
| s 221(3) | subsection | 2911-2914 | encoded | `s 221(3) the conditions are met` |
| s 221(3)(a) | paragraph | 2912-2912 | encoded | (in s 221(3)) |
| s 221(3)(b) | paragraph | 2913-2913 | encoded | (in s 221(3)) |
| s 221(3)(c) | paragraph | 2914-2914 | encoded | (in s 221(3)) |
| s 221(4) | subsection | 2915-2917 | encoded | `s 221(4) the conditions are met` |
| s 221(4)(a) | paragraph | 2916-2916 | encoded | (in s 221(4)) |
| s 221(4)(b) | paragraph | 2917-2917 | encoded | (in s 221(4)) |
| s 222 | section | 2918-2927 | encoded | see its subsections |
| s 222(1) | subsection | 2919-2921 | encoded | `s 222(1) subsection (1) applies to the payment`, `s 222 the payment is held by the recipient on trust for` (limb (a)), `s 222(1)(b) the director is jointly and severally liable to indemnify the company that made the payment` |
| s 222(1)(a) | paragraph | 2920-2920 | encoded | (in s 222(1)) |
| s 222(1)(b) | paragraph | 2921-2921 | encoded | (in s 222(1)) |
| s 222(2) | subsection | 2922-2922 | encoded | `s 222(2) subsection (2) applies to the payment`, `s 222 the payment is held by the recipient on trust for` |
| s 222(3) | subsection | 2923-2925 | encoded | `s 222(3) subsection (3) applies to the payment`, `s 222 the payment is held by the recipient on trust for`, `s 222(3)(b) the expenses incurred by the recipient in distributing the sum are borne by him and not retained out of the sum` |
| s 222(3)(a) | paragraph | 2924-2924 | encoded | (in s 222(3)) |
| s 222(3)(b) | paragraph | 2925-2925 | encoded | (in s 222(3)) |
| s 222(4) | subsection | 2926-2926 | encoded | `s 222(1) subsection (1) applies to the payment` and `s 222(2) subsection (2) applies to the payment` (the displacement) |
| s 222(5) | subsection | 2927-2927 | fork F-222-1 | `s 222(1) subsection (1) applies to the payment` and `s 222(3) subsection (3) applies to the payment` (the court's direction is an input) |
| heading@2928 | cross-heading | 2928-2928 | inert 1 | not operative: a heading (cross-heading) |
| s 223 | section | 2929-2936 | encoded | see its subsections |
| s 223(1) | subsection | 2930-2935 | encoded | `s 223(1) the shadow director is treated as a director for the provision` (coa5-ch4-supplementary.l4; type `s 223(1) provisions`) |
| s 223(1)(a) | paragraph | 2931-2931 | encoded | (in s 223(1)) |
| s 223(1)(b) | paragraph | 2932-2932 | encoded | (in s 223(1)) |
| s 223(1)(c) | paragraph | 2933-2933 | encoded | (in s 223(1)) |
| s 223(1)(d) | paragraph | 2934-2935 | encoded | (in s 223(1)) |
| s 223(2) | subsection | 2936-2936 | encoded | `s 223(2) a reference to loss of office as a director applies to the loss` (coa5-ch4-supplementary.l4) |
| s 224 | section | 2937-2942 | encoded | see its subsections |
| s 224(1) | subsection | 2938-2941 | encoded | `s 224(1) the failure is disregarded in determining whether the requirement has been met` (coa5-ch4-supplementary.l4) |
| s 224(1)(a) | paragraph | 2939-2939 | encoded | (in s 224(1)) |
| s 224(1)(b) | paragraph | 2940-2941 | encoded | (in s 224(1)) |
| s 224(2) | subsection | 2942-2942 | encoded | `s 224(2) subsection (1) has effect subject to a provision of the articles` (coa5-ch4-supplementary.l4) |
| s 225 | section | 2943-2946 | encoded | see its subsections |
| s 225(1) | subsection | 2944-2944 | encoded | `s 225(1) approval is required under more than one provision of this Chapter` (coa5-ch4-supplementary.l4) |
| s 225(2) | subsection | 2945-2945 | encoded | `s 225(2) approval has been given as this Chapter requires` (coa5-ch4-supplementary.l4) |
| s 225(3) | subsection | 2946-2946 | encoded | `s 225(3) a separate resolution is required for each provision` (coa5-ch4-supplementary.l4) |
| s 226 | section | 2947-2948 | repealed or blank in this text | the section number and heading are followed by dots only |
| blank@2948 | blank line (dots) | 2948-2948 | repealed or blank in this text | a line of dots under the heading of s 226: the section is shown repealed or blank |
| heading@2949 | chapter or part heading | 2949-2949 | inert 1 | not operative: a heading (chapter or Part heading) |
| heading@2950 | cross-heading | 2950-2950 | inert 1 | not operative: a heading (cross-heading) |
| s 226A | section | 2951-2984 | encoded | see its subsections (coa5-quoted-company-pay.l4) |
| s 226A(1) | subsection | 2952-2962 | encoded | `s 226A(1) the company is a quoted company in this Chapter`, `s 226A(1) the payment is a payment for loss of office in this Chapter`, `s 226A(1) the payment is a remuneration payment`, `s 226A(1) the policy is a directors' remuneration policy` |
| s 226A(1) defined term directors' remuneration policy | defined term | 2953-2953 | encoded | (in s 226A(1)) |
| s 226A(1) defined term quoted company | defined term | 2954-2954 | encoded | (in s 226A(1)) |
| s 226A(1) defined term remuneration payment | defined term | 2955-2955 | encoded | (in s 226A(1)) |
| s 226A(1)(a) | paragraph | 2956-2956 | encoded | (in s 226A(1)) |
| s 226A(1)(b) | paragraph | 2957-2960 | encoded | (in s 226A(1)) |
| s 226A(1)(b)(i) | sub-paragraph | 2958-2958 | encoded | (in s 226A(1)) |
| s 226A(1)(b)(ii) | sub-paragraph | 2959-2960 | encoded | (in s 226A(1)) |
| s 226A(1) defined term payment for loss of office | defined term | 2961-2961 | encoded | (in s 226A(1)) |
| blank@2962 | blank line (dots) | 2962-2962 | repealed or blank in this text | a line of dots after the definitions of subsection (1) |
| s 226A(2) | subsection | 2963-2967 | encoded | `s 226A(2) subsection (3) applies` |
| s 226A(2)(a) | paragraph | 2964-2964 | encoded | (in s 226A(2)) |
| s 226A(2)(b) | paragraph | 2965-2967 | encoded | (in s 226A(2)) |
| s 226A(2)(b)(i) | sub-paragraph | 2966-2966 | encoded | (in s 226A(2)) |
| s 226A(2)(b)(ii) | sub-paragraph | 2967-2967 | encoded | (in s 226A(2)) |
| s 226A(3) | subsection | 2968-2971 | encoded | `s 226A(3)(a) the excess taken to have been a payment for loss of office for section 226C`, `s 226A(3)(b) the money value taken to have been a payment for loss of office for section 226C` |
| s 226A(3)(a) | paragraph | 2969-2969 | encoded | (in s 226A(3)) |
| s 226A(3)(b) | paragraph | 2970-2971 | encoded | (in s 226A(3)) |
| s 226A(4) | subsection | 2972-2974 | encoded | `s 226A(4) the transfer is a relevant transfer` |
| s 226A(4)(a) | paragraph | 2973-2973 | encoded | (in s 226A(4)) |
| s 226A(4)(b) | paragraph | 2974-2974 | encoded | (in s 226A(4)) |
| s 226A(5) | subsection | 2975-2975 | encoded | `s 226A(5) the reference is read in accordance with section 226A` |
| s 226A(6) | subsection | 2976-2976 | encoded | `s 226A(6) the payment is treated as a payment by the company` |
| s 226A(7) | subsection | 2977-2979 | encoded | `s 226A(7) the payment is treated as a payment to B who is, has been or is to be a director` |
| s 226A(7)(a) | paragraph | 2978-2978 | encoded | (in s 226A(7)) |
| s 226A(7)(b) | paragraph | 2979-2979 | encoded | (in s 226A(7)) |
| s 226A(8) | subsection | 2980-2980 | encoded | `s 226A(8) section 252 applies to determine whether a person is connected with the person` |
| s 226A(9) | subsection | 2981-2981 | encoded | `s 226A(9) the reference includes the shadow director` |
| s 226A(10) | subsection | 2982-2984 | encoded | `s 226A(10) the reference to a director includes the person` |
| s 226A(10)(a) | paragraph | 2983-2983 | encoded | (in s 226A(10)) |
| s 226A(10)(b) | paragraph | 2984-2984 | repealed or blank in this text | dots only |
| heading@2985 | cross-heading | 2985-2985 | inert 1 | not operative: a heading (cross-heading) |
| s 226B | section | 2986-2990 | encoded | see its subsections |
| s 226B(1) | subsection | 2987-2989 | fork F-UNLESS-1 | `s 226B(1) the quoted company may not make the remuneration payment` (+ duty `s 226B(1) and s 226C(1) the duty not to make the payment`) |
| s 226B(1)(a) | paragraph | 2988-2988 | fork F-UNLESS-1 | (in s 226B(1)) |
| s 226B(1)(b) | paragraph | 2989-2989 | fork F-UNLESS-1 | (in s 226B(1)) |
| s 226B(2) | subsection | 2990-2990 | encoded | `s 226B(2) the policy is the approved directors' remuneration policy` |
| s 226C | section | 2991-2995 | encoded | see its subsections |
| s 226C(1) | subsection | 2992-2994 | fork F-UNLESS-1 | `s 226C(1) no person may make the payment for loss of office` (+ the same duty) |
| s 226C(1)(a) | paragraph | 2993-2993 | fork F-UNLESS-1 | (in s 226C(1)) |
| s 226C(1)(b) | paragraph | 2994-2994 | fork F-UNLESS-1 | (in s 226C(1)) |
| s 226C(2) | subsection | 2995-2995 | encoded | `s 226C(2) the policy is the approved directors' remuneration policy` |
| s 226D | section | 2996-3007 | encoded | see its subsections |
| s 226D(1) | subsection | 2997-2999 | fork F-UNLESS-1 | `s 226D(1) the resolution approving the payment must not be passed` |
| s 226D(1)(a) | paragraph | 2998-2998 | fork F-UNLESS-1 | (in s 226D(1)) |
| s 226D(1)(b) | paragraph | 2999-2999 | fork F-UNLESS-1 | (in s 226D(1)) |
| s 226D(2) | subsection | 3000-3000 | encoded | `s 226D(2) the memorandum meets the requirement` |
| s 226D(3) | subsection | 3001-3001 | encoded | `s 226D(3) the company has ensured the memorandum is available on its website` (no regulative twin: the duty is continuing and the text states no time to act by) |
| s 226D(4) | subsection | 3002-3002 | encoded | `s 226D(4) the failure affects the validity of the meeting or of anything done at it` |
| s 226D(5) | subsection | 3003-3003 | encoded | `s 226D(5) section 226B or 226C authorises the payment` |
| s 226D(6) | subsection | 3004-3006 | encoded | `s 226D(6) sections 226B and 226C apply to the payment` |
| s 226D(6)(a) | paragraph | 3005-3005 | encoded | (in s 226D(6)) |
| s 226D(6)(b) | paragraph | 3006-3006 | encoded | (in s 226D(6)) |
| s 226D(7) | subsection | 3007-3007 | encoded | `s 226D(7) the website is the company's website` |
| heading@3008 | cross-heading | 3008-3008 | inert 1 | not operative: a heading (cross-heading) |
| s 226E | section | 3009-3024 | encoded | see its subsections |
| s 226E(1) | subsection | 3010-3010 | encoded | `s 226E(1) the obligation has effect` |
| s 226E(2) | subsection | 3011-3013 | encoded | `s 226E the payment is held by the recipient on trust for`, `s 226E(2)(b) the director is jointly and severally liable to indemnify the company that made the payment` |
| s 226E(2)(a) | paragraph | 3012-3012 | encoded | (in s 226E(2)) |
| s 226E(2)(b) | paragraph | 3013-3013 | encoded | (in s 226E(2)) |
| s 226E(3) | subsection | 3014-3016 | encoded | `s 226E the payment is held by the recipient on trust for` (kind `s 226E(3) ...`) |
| s 226E(3)(a) | paragraph | 3015-3015 | encoded | (in s 226E(3)) |
| s 226E(3)(b) | paragraph | 3016-3016 | encoded | (in s 226E(3)) |
| s 226E(4) | subsection | 3017-3020 | encoded | `s 226E the payment is held by the recipient on trust for` (kind `s 226E(4) ...`), `s 226E(4)(c) the expenses incurred by the recipient in distributing the sum are borne by the recipient and not retained out of the sum` |
| s 226E(4)(a) | paragraph | 3018-3018 | encoded | (in s 226E(4)) |
| s 226E(4)(b) | paragraph | 3019-3019 | encoded | (in s 226E(4)) |
| s 226E(4)(c) | paragraph | 3020-3020 | encoded | (in s 226E(4)) |
| s 226E(5) | subsection | 3021-3024 | fork F-NT-1 | `s 226E(5) the court may relieve the director from liability` |
| s 226E(5)(a) | paragraph | 3022-3022 | fork F-NT-1 | (in s 226E(5)) |
| s 226E(5)(b) | paragraph | 3023-3024 | fork F-NT-1 | (in s 226E(5)) |
| s 226F | section | 3025-3027 | encoded | see its subsections |
| s 226F(1) | subsection | 3026-3026 | encoded | `s 226F(1) this Chapter affects a requirement for approval by a resolution of the members under Chapter 4` |
| s 226F(2) | subsection | 3027-3027 | encoded | `s 226F(2) the approval obtained for Chapter 4 is treated as satisfying section 226B(1)(b) or 226C(1)(b)` |
| heading@3028 | chapter or part heading | 3028-3028 | inert 1 | not operative: a heading (chapter or Part heading) |
| s 227 | section | 3029-3034 | encoded | see its subsections (coa5-service-contracts.l4) |
| s 227(1) | subsection | 3030-3032 | encoded | `s 227(1) the contract is a director's service contract` (type `s 227(1) arrangement`) |
| s 227(1)(a) | paragraph | 3031-3031 | encoded | (in s 227(1)) |
| s 227(1)(b) | paragraph | 3032-3032 | encoded | (in s 227(1)) |
| s 227(2) | subsection | 3033-3034 | encoded | `s 227(2) the provisions of this Part relating to directors' service contracts apply to the terms` and `s 227(2) the provisions relating to directors' service contracts are restricted to contracts for services outside the scope of the ordinary duties of a director` |
| s 228 | section | 3035-3049 | encoded | see its subsections |
| s 228(1) | subsection | 3036-3038 | fork F-MUST-1 | `s 228(1) the company has kept the copy or memorandum available for inspection` |
| s 228(1)(a) | paragraph | 3037-3037 | fork F-MUST-1 | (in s 228(1)) |
| s 228(1)(b) | paragraph | 3038-3038 | fork F-MUST-1 | (in s 228(1)) |
| s 228(2) | subsection | 3039-3041 | fork F-MUST-1 | `s 228(2) the copies and memoranda are kept at a permitted place` (type `s 228(2) place`) |
| s 228(2)(a) | paragraph | 3040-3040 | fork F-MUST-1 | (in s 228(2)) |
| s 228(2)(b) | paragraph | 3041-3041 | fork F-MUST-1 | (in s 228(2)) |
| s 228(3) | subsection | 3042-3042 | fork F-228-1 | `s 228(3) the copies and memoranda must still be retained and kept available on the date` |
| s 228(4) | subsection | 3043-3046 | encoded | `s 228(4) the company must give notice to the registrar of the place and of any change in it` and the rule `s 228(4) the company's duty to give notice to the registrar` |
| s 228(4)(a) | paragraph | 3044-3044 | encoded | (in s 228(4)) |
| s 228(4)(b) | paragraph | 3045-3046 | encoded | (in s 228(4)) |
| s 228(5) | subsection | 3047-3047 | encoded | `s 228(5) the officer commits an offence` |
| s 228(6) | subsection | 3048-3048 | encoded | `s 228(6) the penalty`, `s 228(6) the largest fine in pounds`, `s 228(6) the largest daily default fine in pounds` |
| s 228(7) | subsection | 3049-3049 | encoded | `s 228(7) the provisions of this section apply to the variation as to the original contract` |
| s 229 | section | 3050-3056 | encoded | see its subsections |
| s 229(1) | subsection | 3051-3051 | encoded | `s 229(1) the person may inspect the copy or memorandum without charge` |
| s 229(2) | subsection | 3052-3053 | encoded | `s 229(2) the member is entitled to be provided with a copy`, `s 229(2) the copy has been provided in time` and the rule `s 229(2) the company's duty to provide the copy` |
| s 229(3) | subsection | 3054-3054 | encoded | `s 229(3) the officer commits an offence` |
| s 229(4) | subsection | 3055-3055 | encoded | `s 229(4) the penalty` |
| s 229(5) | subsection | 3056-3056 | encoded | `s 229(5) the court may by order compel an immediate inspection or direct that the copy be sent` |
| s 230 | section | 3057-3058 | encoded | `s 230 the shadow director is treated as a director for the provisions of this Chapter` |
| heading@3059 | chapter or part heading | 3059-3059 | inert 1 | not operative: a heading (chapter or Part heading) |
| s 231 | section | 3060-3072 | encoded | see its subsections |
| s 231(1) | subsection | 3061-3064 | encoded | `s 231(1) this section applies` |
| s 231(1)(a) | paragraph | 3062-3062 | encoded | (in s 231(1)) |
| s 231(1)(b) | paragraph | 3063-3063 | encoded | (in s 231(1)) |
| s 231(1)(c) | paragraph | 3064-3064 | encoded | (in s 231(1)) |
| s 231(2) | subsection | 3065-3067 | fork F-MUST-1 | `s 231(2) the company must ensure the terms are set out or recorded`, `s 231(2) the company has complied` and the rule `s 231(2) the company's duty to ensure the terms are set out or recorded` |
| s 231(2)(a) | paragraph | 3066-3066 | fork F-MUST-1 | (in s 231(2)) |
| s 231(2)(b) | paragraph | 3067-3067 | fork F-MUST-1 | (in s 231(2)) |
| s 231(3) | subsection | 3068-3068 | encoded | `s 231(3) the officer commits an offence` |
| s 231(4) | subsection | 3069-3069 | encoded | `s 231(4) the penalty`, `s 231(4) the largest fine in pounds` |
| s 231(5) | subsection | 3070-3070 | encoded | `s 231(5) the shadow director is treated as a director` |
| s 231(6) | subsection | 3071-3071 | encoded | `s 231(6) the failure affects the validity of the contract` |
| s 231(7) | subsection | 3072-3072 | encoded | `s 231(7) this section excludes the operation of any other enactment or rule of law applying to contracts between a company and a director` |
| heading@3073 | chapter or part heading | 3073-3073 | inert 1 | not operative: a heading (chapter or Part heading) |
| heading@3074 | cross-heading | 3074-3074 | inert 1 | not operative: a heading (cross-heading) |
| s 232 | section | 3075-3082 | encoded | see its subsections (coa5-director-liabilities.l4) |
| s 232(1) | subsection | 3076-3076 | encoded | `s 232(1) the provision is void` |
| s 232(2) | subsection | 3077-3080 | fork F-232-1 | `s 232(2) the provision is void` |
| s 232(2)(a) | paragraph | 3078-3078 | fork F-232-1 | (in s 232(2)) |
| s 232(2)(b) | paragraph | 3079-3079 | fork F-232-1 | (in s 232(2)) |
| s 232(2)(c) | paragraph | 3080-3080 | fork F-232-1 | (in s 232(2)) |
| s 232(3) | subsection | 3081-3081 | encoded | `s 232(3) this section applies to the provision` |
| s 232(4) | subsection | 3082-3082 | encoded | `s 232(4) this section prevents the articles from making the provision` |
| s 233 | section | 3083-3084 | encoded | `s 233 the insurance is permitted` |
| s 234 | section | 3085-3107 | encoded | see its subsections |
| s 234(1) | subsection | 3086-3086 | encoded | `s 234(1) the provision is permitted as qualifying third party indemnity provision` |
| s 234(2) | subsection | 3087-3088 | encoded | `s 234(2) the provision is third party indemnity provision` and `s 234(2) the provision is qualifying third party indemnity provision` |
| s 234(3) | subsection | 3089-3096 | encoded | `s 234(3) the provision provides no indemnity against the excluded liabilities` |
| s 234(3)(a) | paragraph | 3090-3092 | encoded | (in s 234(3)) |
| s 234(3)(a)(i) | sub-paragraph | 3091-3091 | encoded | (in s 234(3)) |
| s 234(3)(a)(ii) | sub-paragraph | 3092-3092 | encoded | (in s 234(3)) |
| s 234(3)(b) | paragraph | 3093-3096 | encoded | (in s 234(3)) |
| s 234(3)(b)(i) | sub-paragraph | 3094-3094 | encoded | (in s 234(3)) |
| s 234(3)(b)(ii) | sub-paragraph | 3095-3095 | encoded | (in s 234(3)) |
| s 234(3)(b)(iii) | sub-paragraph | 3096-3096 | encoded | (in s 234(3)) |
| s 234(4) | subsection | 3097-3097 | encoded | `s 234(4) the conviction, judgment or refusal of relief counts for subsection (3)(b)` |
| s 234(5) | subsection | 3098-3104 | encoded | `s 234(5)(a) the date when the conviction, judgment or refusal of relief becomes final` and `s 234(5)(b) the appeal is disposed of` |
| s 234(5)(a) | paragraph | 3099-3101 | encoded | (in s 234(5)) |
| s 234(5)(a)(i) | sub-paragraph | 3100-3100 | encoded | (in s 234(5)) |
| s 234(5)(a)(ii) | sub-paragraph | 3101-3101 | encoded | (in s 234(5)) |
| s 234(5)(b) | paragraph | 3102-3104 | encoded | (in s 234(5)) |
| s 234(5)(b)(i) | sub-paragraph | 3103-3103 | encoded | (in s 234(5)) |
| s 234(5)(b)(ii) | sub-paragraph | 3104-3104 | encoded | (in s 234(5)) |
| s 234(6) | subsection | 3105-3107 | encoded | `s 234(6) the application is an application for relief` (type `s 234(6) provision for relief`) |
| s 235 | section | 3108-3125 | encoded | see its subsections |
| s 235(1) | subsection | 3109-3109 | encoded | `s 235(1) the provision is permitted as qualifying pension scheme indemnity provision` |
| s 235(2) | subsection | 3110-3111 | encoded | `s 235(2) the provision is pension scheme indemnity provision` and `s 235(2) the provision is qualifying pension scheme indemnity provision` |
| s 235(3) | subsection | 3112-3116 | encoded | `s 235(3) the provision provides no indemnity against the excluded liabilities` |
| s 235(3)(a) | paragraph | 3113-3115 | encoded | (in s 235(3)) |
| s 235(3)(a)(i) | sub-paragraph | 3114-3114 | encoded | (in s 235(3)) |
| s 235(3)(a)(ii) | sub-paragraph | 3115-3115 | encoded | (in s 235(3)) |
| s 235(3)(b) | paragraph | 3116-3116 | encoded | (in s 235(3)) |
| s 235(4) | subsection | 3117-3117 | encoded | `s 235(4) the conviction counts for subsection (3)(b)` |
| s 235(5) | subsection | 3118-3124 | encoded | `s 235(5)(a) the date when the conviction becomes final` and `s 235(5)(b) the appeal is disposed of` |
| s 235(5)(a) | paragraph | 3119-3121 | encoded | (in s 235(5)) |
| s 235(5)(a)(i) | sub-paragraph | 3120-3120 | encoded | (in s 235(5)) |
| s 235(5)(a)(ii) | sub-paragraph | 3121-3121 | encoded | (in s 235(5)) |
| s 235(5)(b) | paragraph | 3122-3124 | encoded | (in s 235(5)) |
| s 235(5)(b)(i) | sub-paragraph | 3123-3123 | encoded | (in s 235(5)) |
| s 235(5)(b)(ii) | sub-paragraph | 3124-3124 | encoded | (in s 235(5)) |
| s 235(6) | subsection | 3125-3125 | encoded | `s 235(6) the scheme is an occupational pension scheme` |
| s 236 | section | 3126-3134 | encoded | see its subsections |
| s 236(1) | subsection | 3127-3130 | encoded | `s 236(1) the provision is qualifying indemnity provision` |
| s 236(1)(a) | paragraph | 3128-3128 | encoded | (in s 236(1)) |
| s 236(1)(b) | paragraph | 3129-3130 | encoded | (in s 236(1)) |
| s 236(2) | subsection | 3131-3131 | fork F-MUST-1 | `s 236(2) to (5) the directors' report must state that the provision is in force or was in force` and `s 236 the directors' report meets the requirement` |
| s 236(3) | subsection | 3132-3132 | fork F-MUST-1 | the same functions (kind `s 236(3) ...`) |
| s 236(4) | subsection | 3133-3133 | fork F-MUST-1 | the same functions (kind `s 236(4) ...`) |
| s 236(5) | subsection | 3134-3134 | fork F-MUST-1 | the same functions (kind `s 236(5) ...`) |
| s 237 | section | 3135-3155 | encoded | see its subsections |
| s 237(1) | subsection | 3136-3138 | encoded | `s 237(1) this section applies to the company` |
| s 237(1)(a) | paragraph | 3137-3137 | encoded | (in s 237(1)) |
| s 237(1)(b) | paragraph | 3138-3138 | encoded | (in s 237(1)) |
| s 237(2) | subsection | 3139-3141 | fork F-MUST-1 | `s 237(2) the company has kept the copy or memorandum available for inspection` |
| s 237(2)(a) | paragraph | 3140-3140 | fork F-MUST-1 | (in s 237(2)) |
| s 237(2)(b) | paragraph | 3141-3141 | fork F-MUST-1 | (in s 237(2)) |
| s 237(3) | subsection | 3142-3144 | fork F-MUST-1 | `s 237(3) the copy or memorandum is kept at a permitted place` |
| s 237(3)(a) | paragraph | 3143-3143 | fork F-MUST-1 | (in s 237(3)) |
| s 237(3)(b) | paragraph | 3144-3144 | fork F-MUST-1 | (in s 237(3)) |
| s 237(4) | subsection | 3145-3145 | fork F-228-1 | `s 237(4) the copy or memorandum must still be retained and kept available on the date` |
| s 237(5) | subsection | 3146-3149 | fork F-228-2 | `s 237(5) the company must give notice to the registrar of the place and of any change in it` and the rule `s 237(5) the company's duty to give notice to the registrar` |
| s 237(5)(a) | paragraph | 3147-3147 | fork F-228-2 | (in s 237(5)) |
| s 237(5)(b) | paragraph | 3148-3149 | fork F-228-2 | (in s 237(5)) |
| s 237(6) | subsection | 3150-3150 | encoded | `s 237(6) the officer commits an offence` |
| s 237(7) | subsection | 3151-3151 | encoded | `s 237(7) the penalty` |
| s 237(8) | subsection | 3152-3152 | encoded | `s 237(8) the provisions of this section apply to the variation as to the original provision` |
| s 237(9) | subsection | 3153-3155 | encoded | `s 237(9) the provision is qualifying indemnity provision` |
| s 237(9)(a) | paragraph | 3154-3154 | encoded | (in s 237(9)) |
| s 237(9)(b) | paragraph | 3155-3155 | encoded | (in s 237(9)) |
| s 238 | section | 3156-3162 | encoded | see its subsections |
| s 238(1) | subsection | 3157-3157 | encoded | `s 238(1) the person may inspect the copy or memorandum without charge` |
| s 238(2) | subsection | 3158-3159 | encoded | `s 238(2) the member is entitled to be provided with a copy`, `s 238(2) the copy has been provided in time` and the rule `s 238(2) the company's duty to provide the copy` |
| s 238(3) | subsection | 3160-3160 | encoded | `s 238(3) the officer commits an offence` |
| s 238(4) | subsection | 3161-3161 | encoded | `s 238(4) the penalty` |
| s 238(5) | subsection | 3162-3162 | encoded | `s 238(5) the court may by order compel an immediate inspection or direct that the copy be sent` |
| heading@3163 | cross-heading | 3163-3163 | inert 1 | not operative: a heading (cross-heading) |
| s 239 | section | 3164-3178 | encoded | see its subsections |
| s 239(1) | subsection | 3165-3165 | encoded | `s 239(1) this section applies to the ratification` |
| s 239(2) | subsection | 3166-3166 | fork F-MUST-1 | `s 239(2) the decision to ratify has been made as this subsection requires` |
| s 239(3) | subsection | 3167-3167 | encoded | `s 239(3) the member is an eligible member` |
| s 239(4) | subsection | 3168-3169 | encoded | `s 239(4) the vote counts towards the necessary majority` and `s 239(4) the director or the connected member is prevented from attending, being counted towards the quorum and taking part in the proceedings` |
| s 239(5) | subsection | 3170-3174 | encoded | `s 239(5)(a) the matter is conduct`, `s 239(5)(b) the person is a director for this section`, `s 239(5)(c) the shadow director is treated as a director`, `s 239(5)(d) section 252(3) applies, excluding a person who is himself a director from the persons connected with the director` |
| s 239(5)(a) | paragraph | 3171-3171 | encoded | (in s 239(5)) |
| s 239(5)(b) | paragraph | 3172-3172 | encoded | (in s 239(5)) |
| s 239(5)(c) | paragraph | 3173-3173 | encoded | (in s 239(5)) |
| s 239(5)(d) | paragraph | 3174-3174 | encoded | (in s 239(5)) |
| s 239(6) | subsection | 3175-3177 | encoded | `s 239(6) this section affects it` (type `s 239(6) what is affected`) |
| s 239(6)(a) | paragraph | 3176-3176 | encoded | (in s 239(6)) |
| s 239(6)(b) | paragraph | 3177-3177 | encoded | (in s 239(6)) |
| s 239(7) | subsection | 3178-3178 | encoded | `s 239(7) this section affects any other enactment or rule of law imposing additional requirements for valid ratification or any rule of law as to acts that are incapable of being ratified` |
| heading@3179 | chapter or part heading | 3179-3179 | inert 1 | not operative: a heading (chapter or Part heading) |
| s 240 | section | 3180-3186 | encoded | see its subsections (coa5-residential-addresses.l4) |
| s 240(1) | subsection | 3181-3183 | encoded | `s 240(2) the information is protected information` (type `s 240(1) information`) |
| s 240(1)(a) | paragraph | 3182-3182 | encoded | (in s 240(1)) |
| s 240(1)(b) | paragraph | 3183-3183 | encoded | (in s 240(1)) |
| s 240(2) | subsection | 3184-3184 | encoded | `s 240(2) the information is protected information` |
| s 240(3) | subsection | 3185-3186 | encoded | `s 240(3) the information ceases to be protected information` and `s 240(3) a reference in this Chapter to a director includes the person` |
| s 241 | section | 3187-3198 | encoded | see its subsections |
| s 241(1) | subsection | 3188-3191 | encoded | `s 241(1) the company may not use or disclose the protected information` and the rule `s 241(1) the company's duty not to use or disclose protected information` |
| s 241(1)(a) | paragraph | 3189-3189 | encoded | (in s 241(1)) |
| s 241(1)(b) | paragraph | 3190-3190 | encoded | (in s 241(1)) |
| s 241(1)(c) | paragraph | 3191-3191 | encoded | (in s 241(1)) |
| s 241(2) | subsection | 3192-3192 | encoded | `s 241(2) subsection (1) prohibits the use or disclosure` |
| s 241(3) | subsection | 3193-3195 | encoded | `s 241(3)(a) the company commits an offence` and `s 241(3)(b) the officer commits an offence` |
| s 241(3)(a) | paragraph | 3194-3194 | encoded | (in s 241(3)) |
| s 241(3)(b) | paragraph | 3195-3195 | encoded | (in s 241(3)) |
| s 241(4) | subsection | 3196-3198 | encoded | `s 241(4) the penalty` |
| s 241(4)(a) | paragraph | 3197-3197 | encoded | (in s 241(4)) |
| s 241(4)(b) | paragraph | 3198-3198 | encoded | (in s 241(4)) |
| s 242 | section | 3199-3209 | encoded | see its subsections |
| s 242(1) | subsection | 3200-3202 | encoded | `s 242(1) the registrar must omit the protected information from the material available for inspection` |
| s 242(1)(a) | paragraph | 3201-3201 | encoded | (in s 242(1)) |
| s 242(1)(b) | paragraph | 3202-3202 | encoded | (in s 242(1)) |
| s 242(2) | subsection | 3203-3205 | encoded | `s 242(2) the registrar is obliged to do it` |
| s 242(2)(a) | paragraph | 3204-3204 | encoded | (in s 242(2)) |
| s 242(2)(b) | paragraph | 3205-3205 | encoded | (in s 242(2)) |
| s 242(3) | subsection | 3206-3209 | encoded | `s 242(3) the registrar must not make the disclosure` |
| s 242(3)(a) | paragraph | 3207-3207 | encoded | (in s 242(3)) |
| s 242(3)(b) | paragraph | 3208-3208 | encoded | (in s 242(3)) |
| s 242(3)(c) | paragraph | 3209-3209 | encoded | (in s 242(3)) |
| s 243 | section | 3210-3227 | encoded | see its subsections |
| s 243(1) | subsection | 3211-3211 | repealed or blank in this text | dots only |
| s 243(2) | subsection | 3212-3212 | encoded | `s 243(2) the registrar may disclose protected information to the person` |
| s 243(3) | subsection | 3213-3215 | inert 2 | machinery: the Secretary of State's regulation-making power over conditions and fees |
| s 243(3)(a) | paragraph | 3214-3214 | inert 2 | (in s 243(3)) |
| s 243(3)(b) | paragraph | 3215-3215 | inert 2 | (in s 243(3)) |
| s 243(4) | subsection | 3216-3216 | encoded | `s 243(4) the registrar must refrain from disclosing the protected information to a credit reference agency` (the regulations are an input) |
| s 243(5) | subsection | 3217-3221 | inert 2 | machinery: what regulations under (4) may provide |
| s 243(5)(a) | paragraph | 3218-3218 | inert 2 | (in s 243(5)) |
| s 243(5)(b) | paragraph | 3219-3219 | inert 2 | (in s 243(5)) |
| s 243(5)(c) | paragraph | 3220-3220 | inert 2 | (in s 243(5)) |
| s 243(5)(d) | paragraph | 3221-3221 | inert 2 | (in s 243(5)) |
| s 243(6) | subsection | 3222-3222 | inert 2 | machinery: the regulations may confer a discretion on the registrar |
| s 243(6A) | subsection | 3223-3223 | inert 2 | machinery: referral of a question in a determination under the regulations |
| s 243(7) | subsection | 3224-3226 | encoded | `s 243(7) the person is a credit reference agency` |
| s 243(7) defined term credit reference agency | defined term | 3225-3225 | encoded | (in s 243(7)) |
| blank@3226 | blank line (dots) | 3226-3226 | repealed or blank in this text | a line of dots in s 243(7) |
| s 243(8) | subsection | 3227-3227 | inert 2 | machinery: regulations under this section are subject to negative resolution procedure |
| s 244 | section | 3228-3237 | encoded | see its subsections |
| s 244(1) | subsection | 3229-3232 | fork F-NT-2 | `s 244(1) the court may make an order for the disclosure of protected information` |
| s 244(1)(a) | paragraph | 3230-3230 | fork F-NT-2 | (in s 244(1)) |
| s 244(1)(b) | paragraph | 3231-3232 | fork F-NT-2 | (in s 244(1)) |
| s 244(2) | subsection | 3233-3235 | encoded | `s 244(2) an order for disclosure by the registrar may be made` |
| s 244(2)(a) | paragraph | 3234-3234 | encoded | (in s 244(2)) |
| s 244(2)(b) | paragraph | 3235-3235 | encoded | (in s 244(2)) |
| s 244(3) | subsection | 3236-3236 | encoded | `s 244(3) the order may be made on the application of the person` |
| s 244(4) | subsection | 3237-3237 | fork F-MUST-1 | `s 244(4) the order meets the requirement` |
| s 245 | section | 3238-3250 | encoded | see its subsections |
| s 245(1) | subsection | 3239-3241 | fork F-NT-3 | `s 245(1) the registrar may put the director's usual residential address on the public record` |
| s 245(1)(a) | paragraph | 3240-3240 | fork F-NT-3 | (in s 245(1)) |
| s 245(1)(b) | paragraph | 3241-3241 | fork F-NT-3 | (in s 245(1)) |
| s 245(2) | subsection | 3242-3244 | encoded | `s 245(2) the registrar must give notice of the proposal to the recipient` |
| s 245(2)(a) | paragraph | 3243-3243 | encoded | (in s 245(2)) |
| s 245(2)(b) | paragraph | 3244-3244 | encoded | (in s 245(2)) |
| s 245(3) | subsection | 3245-3247 | fork F-MUST-1 | `s 245(3) the notice meets the requirement` |
| s 245(3)(a) | paragraph | 3246-3246 | fork F-MUST-1 | (in s 245(3)) |
| s 245(3)(b) | paragraph | 3247-3247 | fork F-MUST-1 | (in s 245(3)) |
| s 245(4) | subsection | 3248-3248 | encoded | `s 245(4) the notice must be sent to the director at his usual residential address` and `s 245(4) the notice may be sent to a service address provided in place of the usual residential address` |
| s 245(5) | subsection | 3249-3249 | encoded | `s 245(5) the registrar must take account of the representations` |
| s 245(6) | subsection | 3250-3250 | inert 1 | a signpost: "What is meant by putting the address on the public record is explained in section 246" creates no rule; section 246 is encoded |
| s 246 | section | 3251-3263 | encoded | see its subsections |
| s 246(1) | subsection | 3252-3254 | encoded | `s 246(1) the registrar must proceed as if each relevant company had given notice under section 167H` |
| s 246(1)(a) | paragraph | 3253-3253 | encoded | (in s 246(1)) |
| s 246(1)(b) | paragraph | 3254-3254 | encoded | (in s 246(1)) |
| s 246(2) | subsection | 3255-3257 | encoded | `s 246(2) the registrar must give notice of having done so to the recipient` |
| s 246(2)(a) | paragraph | 3256-3256 | encoded | (in s 246(2)) |
| s 246(2)(b) | paragraph | 3257-3257 | encoded | (in s 246(2)) |
| s 246(3) | subsection | 3258-3258 | fork F-MUST-1 | `s 246(3) the notice meets the requirement` |
| s 246(4) | subsection | 3259-3259 | fork F-246-1 | `s 246(4) no service address may be registered for the director other than the usual residential address` |
| s 246(5) | subsection | 3260-3262 | encoded | `s 246(4) no service address may be registered for the director other than the usual residential address` ((5)(b)) and `s 246(5)(a) subsection (4) limits the service address that may be registered` ((5)(a)) |
| s 246(5)(a) | paragraph | 3261-3261 | encoded | (in s 246(5)) |
| s 246(5)(b) | paragraph | 3262-3262 | encoded | (in s 246(5)) |
| s 246(6) | subsection | 3263-3263 | encoded | `s 246(6) the company is a relevant company` |
| heading@3264 | chapter or part heading | 3264-3264 | inert 1 | not operative: a heading (chapter or Part heading) |
| heading@3265 | cross-heading | 3265-3265 | inert 1 | not operative: a heading (cross-heading) |
| s 247 | section | 3266-3280 | encoded | see its subsections (coa5-director-supplementary.l4) |
| s 247(1) | subsection | 3267-3267 | encoded | `s 247(1) the powers of the directors include the power to make the provision` |
| s 247(2) | subsection | 3268-3268 | encoded | `s 247(2) the general duty in section 172 prevents the exercise of the power` |
| s 247(3) | subsection | 3269-3269 | encoded | `s 247(3) a restriction flowing from the company's objects prevents the exercise of the power` |
| s 247(4) | subsection | 3270-3273 | encoded | `s 247(4) the power may be exercised` |
| s 247(4)(a) | paragraph | 3271-3271 | encoded | (in s 247(4)) |
| s 247(4)(b) | paragraph | 3272-3273 | encoded | (in s 247(4)) |
| s 247(5) | subsection | 3274-3276 | encoded | `s 247(5) the resolution of the directors is sufficient sanction` |
| s 247(5)(a) | paragraph | 3275-3275 | encoded | (in s 247(5)) |
| s 247(5)(b) | paragraph | 3276-3276 | encoded | (in s 247(5)) |
| s 247(6) | subsection | 3277-3277 | fork F-MUST-1 | `s 247(6) the other requirements of the articles have been complied with` |
| s 247(7) | subsection | 3278-3280 | fork F-MUST-1 | `s 247(7) the payment may be made` |
| s 247(7)(a) | paragraph | 3279-3279 | fork F-MUST-1 | (in s 247(7)) |
| s 247(7)(b) | paragraph | 3280-3280 | fork F-MUST-1 | (in s 247(7)) |
| heading@3281 | cross-heading | 3281-3281 | inert 1 | not operative: a heading (cross-heading) |
| s 248 | section | 3282-3286 | encoded | see its subsections |
| s 248(1) | subsection | 3283-3283 | fork F-MUST-1 | `s 248(1) the company has caused minutes of all proceedings at meetings of its directors to be recorded` and the rule `s 248(1) the company's duty to cause minutes to be recorded` |
| s 248(2) | subsection | 3284-3284 | fork F-228-1 | `s 248(2) the records must still be kept on the date` |
| s 248(3) | subsection | 3285-3285 | encoded | `s 248(3) the officer commits an offence` |
| s 248(4) | subsection | 3286-3286 | encoded | `s 248(4) the penalty` |
| s 249 | section | 3287-3292 | encoded | see its subsections |
| s 249(1) | subsection | 3288-3288 | encoded | `s 249(1) the minutes are evidence of the proceedings at the meeting` and `s 249(1) the minutes are sufficient evidence of the proceedings at the meeting` |
| s 249(2) | subsection | 3289-3292 | encoded | `s 249(2)(a) the meeting is deemed duly held and convened`, `s 249(2)(b) all proceedings at the meeting are deemed to have duly taken place`, `s 249(2)(c) all appointments at the meeting are deemed valid` |
| s 249(2)(a) | paragraph | 3290-3290 | encoded | (in s 249(2)) |
| s 249(2)(b) | paragraph | 3291-3291 | encoded | (in s 249(2)) |
| s 249(2)(c) | paragraph | 3292-3292 | encoded | (in s 249(2)) |
| heading@3293 | cross-heading | 3293-3293 | inert 1 | not operative: a heading (cross-heading) |
| s 250 | section | 3294-3295 | fork F-250-1 | `s 250 the person occupies the position of director` (coa5-director-definitions.l4) |
| s 251 | section | 3296-3306 | encoded | `s 251 the person is a shadow director` with `s 251(1)`, `s 251(2)`, `s 251(3)` |
| s 251(1) | subsection | 3297-3297 | encoded | (in s 251) |
| s 251(2) | subsection | 3298-3301 | encoded | (in s 251) |
| s 251(2)(a) | paragraph | 3299-3299 | encoded | (in s 251) |
| s 251(2)(b) | paragraph | 3300-3300 | encoded | (in s 251) |
| s 251(2)(c) | paragraph | 3301-3301 | encoded | (in s 251) |
| s 251(3) | subsection | 3302-3306 | encoded | (in s 251) |
| heading@3307 | cross-heading | 3307-3307 | inert 1 | not operative: a heading (cross-heading) |
| s 252 | section | 3308-3324 | encoded | `s 252 the person is connected with the director` with `s 252(2)(a)` to `s 252(2)(e)` and `s 252(3)` |
| s 252(1) | subsection | 3309-3309 | encoded | (in s 252) |
| s 252(2) | subsection | 3310-3323 | encoded | (in s 252) |
| s 252(2)(a) | paragraph | 3311-3311 | encoded | (in s 252) |
| s 252(2)(b) | paragraph | 3312-3312 | encoded | (in s 252) |
| s 252(2)(c) | paragraph | 3313-3316 | encoded | (in s 252) |
| s 252(2)(c)(i) | sub-paragraph | 3314-3314 | encoded | (in s 252) |
| s 252(2)(c)(ii) | sub-paragraph | 3315-3316 | encoded | (in s 252) |
| s 252(2)(d) | paragraph | 3317-3319 | encoded | (in s 252) |
| s 252(2)(d)(i) | sub-paragraph | 3318-3318 | encoded | (in s 252) |
| s 252(2)(d)(ii) | sub-paragraph | 3319-3319 | encoded | (in s 252) |
| s 252(2)(e) | paragraph | 3320-3323 | encoded | (in s 252) |
| s 252(2)(e)(i) | sub-paragraph | 3321-3321 | encoded | (in s 252) |
| s 252(2)(e)(ii) | sub-paragraph | 3322-3322 | encoded | (in s 252) |
| s 252(2)(e)(iii) | sub-paragraph | 3323-3323 | encoded | (in s 252) |
| s 252(3) | subsection | 3324-3324 | encoded | (in s 252) |
| s 253 | section | 3325-3333 | fork F-219-1 | `s 253(2) the person is a member of the director's family` and `s 253(3) subsection (2)(b) applies to the person` |
| s 253(1) | subsection | 3326-3326 | fork F-219-1 | (in s 253) |
| s 253(2) | subsection | 3327-3332 | fork F-219-1 | (in s 253) |
| s 253(2)(a) | paragraph | 3328-3328 | fork F-219-1 | (in s 253) |
| s 253(2)(b) | paragraph | 3329-3329 | fork F-219-1 | (in s 253) |
| s 253(2)(c) | paragraph | 3330-3330 | fork F-219-1 | (in s 253) |
| s 253(2)(d) | paragraph | 3331-3331 | fork F-219-1 | (in s 253) |
| s 253(2)(e) | paragraph | 3332-3332 | fork F-219-1 | (in s 253) |
| s 253(3) | subsection | 3333-3333 | fork F-219-1 | (in s 253) |
| s 254 | section | 3334-3344 | encoded | `s 254(2) the director is connected with the body corporate`, `s 254(3)` to `s 254(6)(b)` |
| s 254(1) | subsection | 3335-3335 | encoded | (in s 254) |
| s 254(2) | subsection | 3336-3338 | encoded | (in s 254) |
| s 254(2)(a) | paragraph | 3337-3337 | encoded | (in s 254) |
| s 254(2)(b) | paragraph | 3338-3338 | encoded | (in s 254) |
| s 254(3) | subsection | 3339-3339 | encoded | (in s 254) |
| s 254(4) | subsection | 3340-3340 | encoded | (in s 254) |
| s 254(5) | subsection | 3341-3341 | encoded | (in s 254) |
| s 254(6) | subsection | 3342-3344 | encoded | (in s 254) |
| s 254(6)(a) | paragraph | 3343-3343 | encoded | (in s 254) |
| s 254(6)(b) | paragraph | 3344-3344 | encoded | (in s 254) |
| s 255 | section | 3345-3359 | encoded | `s 255(2) the director controls the body corporate`, `s 255(3)` to `s 255(6)(b)` |
| s 255(1) | subsection | 3346-3346 | encoded | (in s 255) |
| s 255(2) | subsection | 3347-3353 | encoded | (in s 255) |
| s 255(2)(a) | paragraph | 3348-3350 | encoded | (in s 255) |
| s 255(2)(a)(i) | sub-paragraph | 3349-3349 | encoded | (in s 255) |
| s 255(2)(a)(ii) | sub-paragraph | 3350-3350 | encoded | (in s 255) |
| s 255(2)(b) | paragraph | 3351-3353 | encoded | (in s 255) |
| s 255(2)(b)(i) | sub-paragraph | 3352-3352 | encoded | (in s 255) |
| s 255(2)(b)(ii) | sub-paragraph | 3353-3353 | encoded | (in s 255) |
| s 255(3) | subsection | 3354-3354 | encoded | (in s 255) |
| s 255(4) | subsection | 3355-3355 | encoded | (in s 255) |
| s 255(5) | subsection | 3356-3356 | encoded | (in s 255) |
| s 255(6) | subsection | 3357-3359 | encoded | (in s 255) |
| s 255(6)(a) | paragraph | 3358-3358 | encoded | (in s 255) |
| s 255(6)(b) | paragraph | 3359-3359 | encoded | (in s 255) |
| s 256 | section | 3360-3363 | encoded | `s 256(a) the bodies corporate are associated` and `s 256(b) the companies are associated` |
| s 256(a) | paragraph | 3362-3362 | encoded | (in s 256) |
| s 256(b) | paragraph | 3363-3363 | encoded | (in s 256) |
| s 257 | section | 3364-3368 | encoded | `s 257 the matter is part of the company's constitution for the purposes of this Part` |
| s 257(1) | subsection | 3365-3367 | encoded | (in s 257) |
| s 257(1)(a) | paragraph | 3366-3366 | encoded | (in s 257) |
| s 257(1)(b) | paragraph | 3367-3367 | encoded | (in s 257) |
| s 257(2) | subsection | 3368-3368 | encoded | (in s 257) |
| heading@3369 | cross-heading | 3369-3369 | inert 1 | not operative: a heading (cross-heading) |
| s 258 | section | 3370-3374 | encoded | see its subsections (coa5-director-supplementary.l4) |
| s 258(1) | subsection | 3371-3371 | inert 2 | machinery: the Secretary of State's power to substitute larger sums by order; the sums in ss 207, 211(7) and 221 are encoded as the Act states them |
| s 258(2) | subsection | 3372-3372 | inert 2 | machinery: an order under this section is subject to negative resolution procedure |
| s 258(3) | subsection | 3373-3374 | encoded | `s 258(3) an order under this section has effect in relation to the thing done or not done` |
| s 259 | section | 3375-3376 | encoded | `s 259 it matters whether the law that governs the arrangement or transaction is the law of the United Kingdom, or a part of it, or not` |
| heading@3377 | chapter or part heading | 3377-3377 | inert 1 | not operative: a heading (chapter or Part heading) |
| heading@3378 | chapter or part heading | 3378-3378 | inert 1 | not operative: a heading (chapter or Part heading) |
| s 260 | section | 3379-3393 | encoded | see its subsections (coa5-derivative-claims.l4)  |
| s 260(1) | subsection | 3380-3383 | encoded | `s 260(1) the proceedings are a derivative claim` |
| s 260(1)(a) | paragraph | 3381-3381 | encoded | (in s 260(1)) |
| s 260(1)(b) | paragraph | 3382-3383 | encoded | (in s 260(1)) |
| s 260(2) | subsection | 3384-3386 | encoded | `s 260(2) the derivative claim may be brought` |
| s 260(2)(a) | paragraph | 3385-3385 | encoded | (in s 260(2)) |
| s 260(2)(b) | paragraph | 3386-3386 | encoded | (in s 260(2)) |
| s 260(3) | subsection | 3387-3388 | encoded | `s 260(3) a derivative claim under this Chapter may be brought in respect of the cause of action` and `s 260(3) the cause of action may be against the defendant` |
| s 260(4) | subsection | 3389-3389 | encoded | `s 260(4) it matters whether the cause of action arose before or after the person became a member of the company` |
| s 260(5) | subsection | 3390-3393 | encoded | `s 260(5)(a) the person is a director for this Chapter`, `s 260(5)(b) the shadow director is treated as a director`, `s 260(5)(c) the person is a member for this Chapter` |
| s 260(5)(a) | paragraph | 3391-3391 | encoded | (in s 260(5)) |
| s 260(5)(b) | paragraph | 3392-3392 | encoded | (in s 260(5)) |
| s 260(5)(c) | paragraph | 3393-3393 | encoded | (in s 260(5)) |
| s 261 | section | 3394-3405 | encoded | see its subsections |
| s 261(1) | subsection | 3395-3395 | encoded | `s 261(1) the member must apply to the court for permission to continue the claim` and the rule `s 261(1) the member's duty to apply for permission to continue the claim` |
| s 261(2) | subsection | 3396-3398 | fork F-261-1 | `s 261(2) the court must dismiss the application` and `s 261(2)(b) the court may make any consequential order it considers appropriate` |
| s 261(2)(a) | paragraph | 3397-3397 | fork F-261-1 | (in s 261(2)) |
| s 261(2)(b) | paragraph | 3398-3398 | fork F-261-1 | (in s 261(2)) |
| s 261(3) | subsection | 3399-3401 | fork F-NT-4 | `s 261(3) the court may give directions as to the evidence and may adjourn the proceedings` |
| s 261(3)(a) | paragraph | 3400-3400 | fork F-NT-4 | (in s 261(3)) |
| s 261(3)(b) | paragraph | 3401-3401 | fork F-NT-4 | (in s 261(3)) |
| s 261(4) | subsection | 3402-3405 | encoded | `s 261(4) the court's course on hearing the application` (type `s 261(4) course`) |
| s 261(4)(a) | paragraph | 3403-3403 | encoded | (in s 261(4)) |
| s 261(4)(b) | paragraph | 3404-3404 | encoded | (in s 261(4)) |
| s 261(4)(c) | paragraph | 3405-3405 | encoded | (in s 261(4)) |
| s 262 | section | 3406-3423 | encoded | see its subsections |
| s 262(1) | subsection | 3407-3409 | encoded | `s 262(1) this section applies` |
| s 262(1)(a) | paragraph | 3408-3408 | encoded | (in s 262(1)) |
| s 262(1)(b) | paragraph | 3409-3409 | encoded | (in s 262(1)) |
| s 262(2) | subsection | 3410-3413 | encoded | `s 262(2) the member may apply to the court for permission to continue the claim as a derivative claim` |
| s 262(2)(a) | paragraph | 3411-3411 | encoded | (in s 262(2)) |
| s 262(2)(b) | paragraph | 3412-3412 | encoded | (in s 262(2)) |
| s 262(2)(c) | paragraph | 3413-3413 | encoded | (in s 262(2)) |
| s 262(3) | subsection | 3414-3416 | fork F-261-1 | `s 262(3) the court must dismiss the application` and `s 262(3)(b) ...` |
| s 262(3)(a) | paragraph | 3415-3415 | fork F-261-1 | (in s 262(3)) |
| s 262(3)(b) | paragraph | 3416-3416 | fork F-261-1 | (in s 262(3)) |
| s 262(4) | subsection | 3417-3419 | fork F-NT-5 | `s 262(4) the court may give directions as to the evidence and may adjourn the proceedings` |
| s 262(4)(a) | paragraph | 3418-3418 | fork F-NT-5 | (in s 262(4)) |
| s 262(4)(b) | paragraph | 3419-3419 | fork F-NT-5 | (in s 262(4)) |
| s 262(5) | subsection | 3420-3423 | encoded | `s 262(5) the court's course on hearing the application` |
| s 262(5)(a) | paragraph | 3421-3421 | encoded | (in s 262(5)) |
| s 262(5)(b) | paragraph | 3422-3422 | encoded | (in s 262(5)) |
| s 262(5)(c) | paragraph | 3423-3423 | encoded | (in s 262(5)) |
| s 263 | section | 3424-3446 | encoded | see its subsections |
| s 263(1) | subsection | 3425-3425 | encoded | `s 263(1) the provisions of this section have effect` |
| s 263(2) | subsection | 3426-3431 | fork F-263-1 | `s 263(2) permission (or leave) must be refused` (type `s 263 when the act or omission occurs`) |
| s 263(2)(a) | paragraph | 3427-3427 | fork F-263-1 | (in s 263(2)) |
| s 263(2)(b) | paragraph | 3428-3428 | fork F-263-1 | (in s 263(2)) |
| s 263(2)(c) | paragraph | 3429-3431 | fork F-263-1 | (in s 263(2)) |
| s 263(2)(c)(i) | sub-paragraph | 3430-3430 | fork F-263-1 | (in s 263(2)) |
| s 263(2)(c)(ii) | sub-paragraph | 3431-3431 | fork F-263-1 | (in s 263(2)) |
| s 263(3) | subsection | 3432-3440 | fork F-263-2 | `s 263(3) the matters the court must take into account in particular` (returns the matters engaged) |
| s 263(3)(a) | paragraph | 3433-3433 | fork F-263-2 | (in s 263(3)) |
| s 263(3)(b) | paragraph | 3434-3434 | fork F-263-2 | (in s 263(3)) |
| s 263(3)(c) | paragraph | 3435-3437 | fork F-263-2 | (in s 263(3)) |
| s 263(3)(c)(i) | sub-paragraph | 3436-3436 | fork F-263-2 | (in s 263(3)) |
| s 263(3)(c)(ii) | sub-paragraph | 3437-3437 | fork F-263-2 | (in s 263(3)) |
| s 263(3)(d) | paragraph | 3438-3438 | fork F-263-2 | (in s 263(3)) |
| s 263(3)(e) | paragraph | 3439-3439 | fork F-263-2 | (in s 263(3)) |
| s 263(3)(f) | paragraph | 3440-3440 | fork F-263-2 | (in s 263(3)) |
| s 263(4) | subsection | 3441-3441 | encoded | `s 263(4) the court must have particular regard to the evidence` |
| s 263(5) | subsection | 3442-3444 | inert 2 | machinery: the Secretary of State's power to amend subsections (2) and (3) by regulations |
| s 263(5)(a) | paragraph | 3443-3443 | inert 2 | (in s 263(5)) |
| s 263(5)(b) | paragraph | 3444-3444 | inert 2 | (in s 263(5)) |
| s 263(6) | subsection | 3445-3445 | inert 2 | machinery: the duty to consult before making such regulations |
| s 263(7) | subsection | 3446-3446 | inert 2 | machinery: such regulations are subject to affirmative resolution procedure |
| s 264 | section | 3447-3465 | encoded | see its subsections |
| s 264(1) | subsection | 3448-3451 | encoded | `s 264(1) this section applies` |
| s 264(1)(a) | paragraph | 3449-3449 | encoded | (in s 264(1)) |
| s 264(1)(b) | paragraph | 3450-3450 | encoded | (in s 264(1)) |
| s 264(1)(c) | paragraph | 3451-3451 | encoded | (in s 264(1)) |
| s 264(2) | subsection | 3452-3455 | encoded | `s 264(2) another member may apply to the court for permission to continue the claim` |
| s 264(2)(a) | paragraph | 3453-3453 | encoded | (in s 264(2)) |
| s 264(2)(b) | paragraph | 3454-3454 | encoded | (in s 264(2)) |
| s 264(2)(c) | paragraph | 3455-3455 | encoded | (in s 264(2)) |
| s 264(3) | subsection | 3456-3458 | fork F-261-1 | `s 264(3) the court must dismiss the application` and `s 264(3)(b) ...` |
| s 264(3)(a) | paragraph | 3457-3457 | fork F-261-1 | (in s 264(3)) |
| s 264(3)(b) | paragraph | 3458-3458 | fork F-261-1 | (in s 264(3)) |
| s 264(4) | subsection | 3459-3461 | fork F-NT-6 | `s 264(4) the court may give directions as to the evidence and may adjourn the proceedings` |
| s 264(4)(a) | paragraph | 3460-3460 | fork F-NT-6 | (in s 264(4)) |
| s 264(4)(b) | paragraph | 3461-3461 | fork F-NT-6 | (in s 264(4)) |
| s 264(5) | subsection | 3462-3465 | encoded | `s 264(5) the court's course on hearing the application` |
| s 264(5)(a) | paragraph | 3463-3463 | encoded | (in s 264(5)) |
| s 264(5)(b) | paragraph | 3464-3464 | encoded | (in s 264(5)) |
| s 264(5)(c) | paragraph | 3465-3465 | encoded | (in s 264(5)) |
| heading@3466 | chapter or part heading | 3466-3466 | inert 1 | not operative: a heading (chapter or Part heading) |
| s 265 | section | 3467-3483 | encoded | see its subsections |
| s 265(1) | subsection | 3468-3468 | encoded | `s 265(1) the member may raise the proceedings` |
| s 265(2) | subsection | 3469-3469 | encoded | `s 265(2) a member may raise such proceedings` |
| s 265(3) | subsection | 3470-3470 | encoded | `s 265(3) the act or omission is one specified in subsection (3)` |
| s 265(4) | subsection | 3471-3473 | encoded | `s 265(4) proceedings may be raised against the defendant` |
| s 265(4)(a) | paragraph | 3472-3472 | encoded | (in s 265(4)) |
| s 265(4)(b) | paragraph | 3473-3473 | encoded | (in s 265(4)) |
| s 265(5) | subsection | 3474-3474 | encoded | `s 265(5) it matters whether the act or omission arose before or after the person became a member of the company` |
| s 265(6) | subsection | 3475-3477 | encoded | `s 265(6) this section affects it` |
| s 265(6)(a) | paragraph | 3476-3476 | encoded | (in s 265(6)) |
| s 265(6)(b) | paragraph | 3477-3477 | encoded | (in s 265(6)) |
| s 265(7) | subsection | 3478-3483 | fork F-265-1 | `s 265(7)(a) the proceedings are derivative proceedings`, `s 265(7)(b) the act or omission is the cause of action`, `s 265(7)(c) the person is a director for this Chapter`, `s 265(7)(d) the shadow director is included among the references to a director`, `s 265(7)(e) the person is a member for this Chapter` |
| s 265(7)(a) | paragraph | 3479-3479 | fork F-265-1 | (in s 265(7)) |
| s 265(7)(b) | paragraph | 3480-3480 | fork F-265-1 | (in s 265(7)) |
| s 265(7)(c) | paragraph | 3481-3481 | fork F-265-1 | (in s 265(7)) |
| s 265(7)(d) | paragraph | 3482-3482 | fork F-265-1 | (in s 265(7)) |
| s 265(7)(e) | paragraph | 3483-3483 | fork F-265-1 | (in s 265(7)) |
| s 266 | section | 3484-3501 | encoded | see its subsections |
| s 266(1) | subsection | 3485-3485 | encoded | `s 266(1) derivative proceedings may be raised by the member` |
| s 266(2) | subsection | 3486-3488 | fork F-MUST-1 | `s 266(2) the application meets the requirement` |
| s 266(2)(a) | paragraph | 3487-3487 | fork F-MUST-1 | (in s 266(2)) |
| s 266(2)(b) | paragraph | 3488-3488 | fork F-MUST-1 | (in s 266(2)) |
| s 266(3) | subsection | 3489-3491 | fork F-261-1 | `s 266(3) the court must refuse the application` and `s 266(3)(b) ...` |
| s 266(3)(a) | paragraph | 3490-3490 | fork F-261-1 | (in s 266(3)) |
| s 266(3)(b) | paragraph | 3491-3491 | fork F-261-1 | (in s 266(3)) |
| s 266(4) | subsection | 3492-3497 | encoded | `s 266(4)(a) the applicant must serve the application on the company` and the rule `s 266(4)(a) the applicant's duty to serve the application on the company`, `s 266(4)(b) ...`, `s 266(4)(c) the company is entitled to take part in the further proceedings on the application` |
| s 266(4)(a) | paragraph | 3493-3493 | encoded | (in s 266(4)) |
| s 266(4)(b) | paragraph | 3494-3496 | fork F-NT-7 | `s 266(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings` |
| s 266(4)(b)(i) | sub-paragraph | 3495-3495 | fork F-NT-7 | (in s 266(4)(b)) |
| s 266(4)(b)(ii) | sub-paragraph | 3496-3496 | fork F-NT-7 | (in s 266(4)(b)) |
| s 266(4)(c) | paragraph | 3497-3497 | encoded | (in s 266(4)) |
| s 266(5) | subsection | 3498-3501 | encoded | `s 266(5) the court's course on hearing the application` |
| s 266(5)(a) | paragraph | 3499-3499 | encoded | (in s 266(5)) |
| s 266(5)(b) | paragraph | 3500-3500 | encoded | (in s 266(5)) |
| s 266(5)(c) | paragraph | 3501-3501 | encoded | (in s 266(5)) |
| s 267 | section | 3502-3522 | encoded | see its subsections |
| s 267(1) | subsection | 3503-3505 | encoded | `s 267(1) this section applies` |
| s 267(1)(a) | paragraph | 3504-3504 | encoded | (in s 267(1)) |
| s 267(1)(b) | paragraph | 3505-3505 | encoded | (in s 267(1)) |
| s 267(2) | subsection | 3506-3509 | encoded | `s 267(2) the member may apply to the court to be substituted for the company` |
| s 267(2)(a) | paragraph | 3507-3507 | encoded | (in s 267(2)) |
| s 267(2)(b) | paragraph | 3508-3508 | encoded | (in s 267(2)) |
| s 267(2)(c) | paragraph | 3509-3509 | encoded | (in s 267(2)) |
| s 267(3) | subsection | 3510-3512 | fork F-261-1 | `s 267(3) the court must refuse the application` and `s 267(3)(b) ...` |
| s 267(3)(a) | paragraph | 3511-3511 | fork F-261-1 | (in s 267(3)) |
| s 267(3)(b) | paragraph | 3512-3512 | fork F-261-1 | (in s 267(3)) |
| s 267(4) | subsection | 3513-3518 | encoded | `s 267(4)(a) ...`, `s 267(4)(b) ...`, `s 267(4)(c) ...` |
| s 267(4)(a) | paragraph | 3514-3514 | encoded | (in s 267(4)) |
| s 267(4)(b) | paragraph | 3515-3517 | fork F-NT-8 | `s 267(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings` |
| s 267(4)(b)(i) | sub-paragraph | 3516-3516 | fork F-NT-8 | (in s 267(4)(b)) |
| s 267(4)(b)(ii) | sub-paragraph | 3517-3517 | fork F-NT-8 | (in s 267(4)(b)) |
| s 267(4)(c) | paragraph | 3518-3518 | encoded | (in s 267(4)) |
| s 267(5) | subsection | 3519-3522 | encoded | `s 267(5) the court's course on hearing the application` |
| s 267(5)(a) | paragraph | 3520-3520 | encoded | (in s 267(5)) |
| s 267(5)(b) | paragraph | 3521-3521 | encoded | (in s 267(5)) |
| s 267(5)(c) | paragraph | 3522-3522 | encoded | (in s 267(5)) |
| s 268 | section | 3523-3544 | encoded | see its subsections |
| s 268(1) | subsection | 3524-3529 | fork F-263-1 | `s 268(1) leave to raise derivative proceedings or an application under section 267 must be refused` (type `s 268 when the act or omission occurs`) |
| s 268(1)(a) | paragraph | 3525-3525 | fork F-263-1 | (in s 268(1)) |
| s 268(1)(b) | paragraph | 3526-3526 | fork F-263-1 | (in s 268(1)) |
| s 268(1)(c) | paragraph | 3527-3529 | fork F-263-1 | (in s 268(1)) |
| s 268(1)(c)(i) | sub-paragraph | 3528-3528 | fork F-263-1 | (in s 268(1)) |
| s 268(1)(c)(ii) | sub-paragraph | 3529-3529 | fork F-263-1 | (in s 268(1)) |
| s 268(2) | subsection | 3530-3538 | fork F-263-2 | `s 268(2) the matters the court must take into account in particular` |
| s 268(2)(a) | paragraph | 3531-3531 | fork F-263-2 | (in s 268(2)) |
| s 268(2)(b) | paragraph | 3532-3532 | fork F-263-2 | (in s 268(2)) |
| s 268(2)(c) | paragraph | 3533-3535 | fork F-263-2 | (in s 268(2)) |
| s 268(2)(c)(i) | sub-paragraph | 3534-3534 | fork F-263-2 | (in s 268(2)) |
| s 268(2)(c)(ii) | sub-paragraph | 3535-3535 | fork F-263-2 | (in s 268(2)) |
| s 268(2)(d) | paragraph | 3536-3536 | fork F-263-2 | (in s 268(2)) |
| s 268(2)(e) | paragraph | 3537-3537 | fork F-263-2 | (in s 268(2)) |
| s 268(2)(f) | paragraph | 3538-3538 | fork F-263-2 | (in s 268(2)) |
| s 268(3) | subsection | 3539-3539 | encoded | `s 268(3) the court must have particular regard to the evidence` |
| s 268(4) | subsection | 3540-3542 | inert 2 | machinery: the Secretary of State's power to amend subsections (1) and (2) by regulations |
| s 268(4)(a) | paragraph | 3541-3541 | inert 2 | (in s 268(4)) |
| s 268(4)(b) | paragraph | 3542-3542 | inert 2 | (in s 268(4)) |
| s 268(5) | subsection | 3543-3543 | inert 2 | machinery: the duty to consult before making such regulations |
| s 268(6) | subsection | 3544-3544 | inert 2 | machinery: such regulations are subject to affirmative resolution procedure |
| s 269 | section | 3545-3566 | encoded | see its subsections |
| s 269(1) | subsection | 3546-3549 | encoded | `s 269(1) this section applies` |
| s 269(1)(a) | paragraph | 3547-3547 | encoded | (in s 269(1)) |
| s 269(1)(b) | paragraph | 3548-3548 | encoded | (in s 269(1)) |
| s 269(1)(c) | paragraph | 3549-3549 | encoded | (in s 269(1)) |
| s 269(2) | subsection | 3550-3553 | encoded | `s 269(2) another member may apply to the court to be substituted for the claimant` |
| s 269(2)(a) | paragraph | 3551-3551 | encoded | (in s 269(2)) |
| s 269(2)(b) | paragraph | 3552-3552 | encoded | (in s 269(2)) |
| s 269(2)(c) | paragraph | 3553-3553 | encoded | (in s 269(2)) |
| s 269(3) | subsection | 3554-3556 | fork F-261-1 | `s 269(3) the court must refuse the application` and `s 269(3)(b) ...` |
| s 269(3)(a) | paragraph | 3555-3555 | fork F-261-1 | (in s 269(3)) |
| s 269(3)(b) | paragraph | 3556-3556 | fork F-261-1 | (in s 269(3)) |
| s 269(4) | subsection | 3557-3562 | encoded | `s 269(4)(a) ...`, `s 269(4)(b) ...`, `s 269(4)(c) ...` |
| s 269(4)(a) | paragraph | 3558-3558 | encoded | (in s 269(4)) |
| s 269(4)(b) | paragraph | 3559-3561 | fork F-NT-9 | `s 269(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings` |
| s 269(4)(b)(i) | sub-paragraph | 3560-3560 | fork F-NT-9 | (in s 269(4)(b)) |
| s 269(4)(b)(ii) | sub-paragraph | 3561-3561 | fork F-NT-9 | (in s 269(4)(b)) |
| s 269(4)(c) | paragraph | 3562-3562 | encoded | (in s 269(4)) |
| s 269(5) | subsection | 3563-3566 | encoded | `s 269(5) the court's course on hearing the application` |
| s 269(5)(a) | paragraph | 3564-3564 | encoded | (in s 269(5)) |
| s 269(5)(b) | paragraph | 3565-3565 | encoded | (in s 269(5)) |
| s 269(5)(c) | paragraph | 3566-3566 | encoded | (in s 269(5)) |


## Fork register (coa5)

Every ambiguity met, the readings seen, the one taken, and the text that licenses each.
The sites that rest on the "no convention: decide case by case" ruling of 2026-11-05 (the maintainer, quoted in the brief) are marked **[case by case]** and carry the provision, the function, the answer taken and the other reading, for the human reviewer to overrule.

| id | provision and function | the readings | the one taken, and why |
| --- | --- | --- | --- |
| F-205-1 | s 205(2), `s 205(2) the terms are met` | (A) the terms must cover the event the proceedings can end in: conviction (criminal proceedings), judgment against the director (civil), refusal of relief (an application for relief), the repayment date being the date that event becomes final. (B) every loan's terms must cover all three events. | A. The text says "in the event of (i) ..., (ii) ..., or (iii) ..." and "not later than (i) the date when the conviction becomes final, (ii) ..., or (iii) ...": "or" lists alternatives, and a civil proceeding has no conviction. The function takes the facts for the one event that applies. |
| F-UNLESS-1 | ss 217(1), (2), (3), 218(1), (2), (3), 219(1), (3), "may not / must not ... unless", functions `s 217(1) the company may not make the payment` etc. **[case by case: an "unless" once it is met]** | (A) once the "unless" condition is met the bar's answer is JUST FALSE ("the bar does not apply on these facts"). (B) it is NOTHING (the text says only what bars the payment, not that the payment is then lawful). | A. The brief lists "unless" among the words that give JUST FALSE. The function's question is "does THIS section bar it", never "is it lawful": JUST FALSE says only that this section does not bar the payment, and other sections (for instance s 188, s 226C) are not asked here. |
| F-210-1 | s 210(2), `s 210(2) the other transaction or arrangement is a relevant transaction or arrangement` **[case by case: a "where" whose condition fails]** | When the transaction in question is entered into for no director or connected person of either company, neither (3) nor (4) is engaged. (A) NOTHING: the section gives conditions only for the cases in (3) and (4). (B) JUST FALSE: "Other relevant transactions or arrangements are those ... in relation to which the following conditions are met" and none is met. | A. Subsections (3) and (4) open with "Where the transaction ... is entered into for a director ..." (a scope limit with no "only": NOTHING by the 2026-11-05 ruling (c)). If both engaged and both unmet the answer is JUST FALSE. |
| F-211-1 | s 211(1)(b), `s 211(1)(b) the value of an other relevant transaction or arrangement` | (A) the value so determined minus the reduction in the liabilities, with no floor. (B) floored at nought. | A. The text says "reduced by any amount by which the liabilities of the person ... have been reduced" and gives no floor; a reduction larger than the value would give a negative number, which a caller should see. |
| F-213-1 | s 213(4)(a), (b), (c), `s 213(4) the person is one of the persons liable` | (A) liability under (4)(a), (b) and so (c) reaches contraventions of ss 197, 198, 201 and 203 only: (a) names "section 197, 198, 201 or 203", (b) says "any of those sections", (c) says "any such person". (B) s 200 is included, as subsection (6) speaks of a contravention of "section 200, 201 or 203" in the case of (4)(c). | A: the literal text. Under A the s 200 reference in (6) has no case to bite on for (4)(c); the function answers NOTHING (limited by its own wording) for a s 200 contravention in (a), (b) and (c), and (d) catches any section. Finding 3. |
| F-213-2 | s 213(2), `s 213(2) the transaction or arrangement is voidable at the instance of the company` **[case by case: an "unless" once it is met]** | (A) when one of (a), (b), (c) holds the answer is JUST FALSE. (B) NOTHING. | A: "is voidable ... unless" is a condition the text introduces with "unless". |
| F-218-1 | s 218(5) and s 219(7), the presumptions, `s 218(5) the payment is presumed to be a payment to which section 218 applies` **[case by case: an "except" once it is met]** | (A) "except in so far as the contrary is shown": when the contrary is shown the presumption does not hold, JUST FALSE. (B) the contrary may be shown in part ("in so far as"), so the presumption survives for the part not rebutted: the function would need the extent shown. | A, with the extent left to the caller: the function answers for the payment as a whole; a caller who shows the contrary for part of a payment splits it first. When the arrangement is outside the window, or no one named is privy, the answer is NOTHING (the presumption does not arise; the text says nothing of the payment then). |
| F-219-1 | s 219(2), `s 219(2) the holder is one of the relevant shareholders` | (A) "The relevant shareholders are A and B": a list not closed, so NOTHING for any other holder. (B) closed, JUST FALSE. | A: no "only" or "means". |
| F-220-1 | s 220(1), `s 220(1) approval under section 217, 218 or 219 is not required by this section` | When the obligation is not an "existing legal obligation" (limbs (a), (b)): (A) NOTHING, the grant is limited by its wording; (B) JUST FALSE. | A: limbs (c) and (d) may still apply on other facts; the function takes one ground at a time. |
| F-222-1 | s 222(5), `s 222(1) subsection (1) applies to the payment`, `s 222(3) subsection (3) applies to the payment` | In a payment contravening ss 217 and 219 "subsection (3) ... applies rather than subsection (1), unless the court directs otherwise". (A) when the court directs otherwise, what applies is for the court: NOTHING for both subsections. (B) when it directs otherwise, subsection (1) applies as though (5) were absent. | A: the text says only "unless the court directs otherwise" and does not say what the direction is. |
| F-MUST-1 | ss 228(1), 228(2), 231(2), and every later duty phrased "must" (ss 236, 237, 238, 248(1)), the "has complied" functions **[case by case: a bare "must" not done]** | When a duty phrased "must" is not done: (A) the "has the duty been met" function answers JUST FALSE and the rule is breached; (B) NOTHING, the text saying what must be done and not what follows. | A. The functions ask a factual question ("has the company kept the copy available?"), and the text states the duty flatly; a "no" is the text's own "must". The consequence (the offence) is a separate function that needs s 1121's "in default" as an input. |
| F-228-1 | s 228(3), `s 228(3) the copies and memoranda must still be retained and kept available on the date` | "for at least one year from the date of termination or expiry": (A) the anniversary day itself is within the year; (B) the year ends on the day before the anniversary. | A (`add years` the date 1, on or before it). Under B the last day would be a day earlier. The period is stated in the text's own words, so after it the answer is JUST FALSE (the periods ruling, (a)). |
| F-228-2 | s 228(4), the rule `s 228(4) the company's duty to give notice to the registrar` | (4) states no time; (5) makes default "for 14 days" in complying with (4) an offence. (A) the duty's time is 14 days, from when the duty arises. (B) no time is stated: the duty stands until done. | A for the rule (so a trace can end FULFILLED or BREACHED); the decision function `s 228(5) the officer commits an offence` takes the number of days of default as input and is the same under both readings. |
| F-232-1 | s 232(2), `s 232(2) the provision is void` **[case by case: an "except" once it is (not) met]** | "is void, except as permitted by ss 233, 234, 235": (A) when none of the three permissions is shown to apply (each answers NOTHING) the provision is void, JUST TRUE; when one applies, JUST FALSE. (B) when a permission's answer is unknown the provision's voidness is NOTHING. | A for the all-NOTHING case, because s 233 and s 234(1), s 235(1) answer NOTHING when they do not apply (their grants are limited by their own wording) and an unknown answer cannot be told from a "does not apply"; a caller passing an unknown answer should pass NOTHING for that permission and read the result with that in mind. |
| F-246-1 | s 246(4), `s 246(4) no service address may be registered for the director other than the usual residential address` | "for the period of five years beginning with the date of the registrar's decision": (A) the period runs from the decision date to the day before the fifth anniversary (the decision date is day one). (B) the fifth anniversary is the last day. | A: the period "begins with the date", so it includes that date and runs five years; the fifth anniversary is the first day outside it. |
| F-219-1 (also s 253) | s 253(2), `s 253(2) the person is a member of the director's family`; s 219(2) | "the members of a director's family are (a) ... (e)": (A) a list not closed (no "only"), so a person outside it (a cousin) is NOTHING. (B) a closed definition, JUST FALSE for the cousin. | A, by the rule of 2026-10-29. s 252(2) says "(and only those persons)" for connected persons, which includes the family in (a); under A a cousin answers NOTHING in (a), and the composite `s 252` answers NOTHING (not JUST FALSE) for such a person unless the other limbs are all JUST FALSE. |
| F-250-1 | s 250, `s 250 the person occupies the position of director` | "includes any person occupying the position of director, by whatever name called": (A) a person who does not occupy the position gets NOTHING (the word is "includes", and an appointed director is a director by its ordinary meaning, which the section does not restate). (B) JUST FALSE. | A. The input is a single fact, that the person holds a post carrying the position of director by whatever name; the caller who knows the person was formally appointed passes TRUE. |
| F-261-1 | ss 261(2), 262(3), 264(3), 266(3), 267(3), 269(3), the court's "must dismiss/refuse", **[case by case: a duty whose "if" is unmet]** | "If it appears to the court that the application and the evidence do not disclose a prima facie case, the court must dismiss": (A) when the "if" is unmet the function answers JUST FALSE ("this subsection requires no dismissal on these facts"). (B) NOTHING. | A, the "if" being the text's own; JUST FALSE does not say the application succeeds: it says only that this subsection does not require its dismissal. What appears to the court is an input, since the text makes the court's view the trigger. |
| F-263-1 | ss 263(2), 268(1), "must be refused if the court is satisfied" | The grounds are the court's satisfaction ((a) a person acting under s 172 would not seek to continue; (b) a future act authorised; (c) a past act authorised or ratified). (A) the inputs are the grounds the court is satisfied of (what the member can state is the underlying fact; the satisfaction is the court's). (B) the inputs are the underlying facts, the court's satisfaction being assumed. | A: each ground is a plain input worded "the court is satisfied that ...", so a caller who states only the fact (the act was ratified) says the court is satisfied of it. The seat layer words them as the member would state them and says in its `@desc` that the court must be satisfied. |
| F-263-2 | ss 263(3), 268(2), "must take into account, in particular" | (A) the function returns the list of matters engaged (a list of the text's matters, by whether the act is yet to occur or has occurred). (B) a decision function over the matters. | A: the text lists matters for the court to weigh and gives no weights; a verdict would invent one. |
| F-265-1 | s 265(7)(a), (b), "derivative proceedings", "cause of action" | "are referred to as": (A) a naming rule, JUST TRUE for the named case and NOTHING otherwise. (B) a closed definition, JUST FALSE otherwise. | A: the paragraphs introduce names and the text says nothing of other proceedings. |
| F-209-1 | s 209(1), `s 209(1) approval under sections 197, 198 and 200 is not required by this section` **[case by case: "(other than X)" / a rescue that does not apply]** | When condition (1)(b) (no more favourable than for an unconnected person) is not met and s 209(3)'s rescue for home loans does not apply (its answer is NOTHING, because the loan is not a home loan to a director or employee): (A) JUST FALSE, the "if" of (1)(b) failing; (B) NOTHING. | A. NOTHING from s 209(3) cannot tell "does not apply" from "not known"; a caller who does not know whether s 209(3) applies should say so by asking s 209(3) first. |
| F-NT-1 | s 226E(5), `s 226E(5) the court may relieve the director from liability` **[name-test sweep 2026-11-12]** | "If in proceedings ... (a) the director shows that he or she has acted honestly and reasonably, and (b) the court considers that ... the director ought to be relieved of liability, the court may relieve the director": (A) a power given "if", so NOTHING when (a) or (b) fails. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line) |
| F-NT-2 | s 244(1), `s 244(1) the court may make an order for the disclosure of protected information` **[name-test sweep 2026-11-12]** | "The court may make an order ... if— (a) ... or (b) ..., and the court is otherwise satisfied that it is appropriate": (A) NOTHING when the gate fails. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line); s 244(2) says "only if" and keeps JUST FALSE |
| F-NT-3 | s 245(1), `s 245(1) the registrar may put the director's usual residential address on the public record` **[name-test sweep 2026-11-12]** | "The registrar may put a director's usual residential address on the public record if— (a) ... or (b) ...": (A) NOTHING when neither ground exists. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line); the section heading ("Circumstances in which registrar may put address on the public record") is a heading and not operative text |
| F-NT-4 | s 261(3), `s 261(3) the court may give directions as to the evidence and may adjourn the proceedings` **[name-test sweep 2026-11-12]** | "If the application is not dismissed under subsection (2), the court— (a) may give directions ..., and (b) may adjourn": (A) NOTHING when the application was dismissed. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line) |
| F-NT-5 | s 262(4), `s 262(4) the court may give directions as to the evidence and may adjourn the proceedings` **[name-test sweep 2026-11-12]** | "If the application is not dismissed under subsection (3), the court— (a) may give directions ..., and (b) may adjourn": (A) NOTHING when the application was dismissed. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line) |
| F-NT-6 | s 264(4), `s 264(4) the court may give directions as to the evidence and may adjourn the proceedings` **[name-test sweep 2026-11-12]** | "If the application is not dismissed under subsection (3), the court— (a) may give directions ..., and (b) may adjourn": (A) NOTHING when the application was dismissed. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line) |
| F-NT-7 | s 266(4)(b), `s 266(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings` **[name-test sweep 2026-11-12]** | "If the application is not refused under subsection (3) ... (b) the court— (i) may make an order requiring evidence to be produced by the company, and (ii) may adjourn the proceedings": (A) NOTHING when the application was refused. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line) |
| F-NT-8 | s 267(4)(b), `s 267(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings` **[name-test sweep 2026-11-12]** | "If the application is not refused under subsection (3) ... (b) the court— (i) may make an order requiring evidence to be produced by the company, and (ii) may adjourn the proceedings": (A) NOTHING when the application was refused. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line) |
| F-NT-9 | s 269(4)(b), `s 269(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings` **[name-test sweep 2026-11-12]** | "If the application is not refused under subsection (3) ... (b) the court— (i) may make an order requiring evidence to be produced by the company, and (ii) may adjourn the proceedings": (A) NOTHING when the application was refused. (B) a failed "if" is the text's own no, JUST FALSE (reading (a) of the brief's marginal readings). | A: the function is named for a power given "if" its gate is met and the text has no "only if", so a failed gate gives NOTHING (the Guide's "limits a grant or prohibition in its own wording" line) |
| F-NT-E1 | s 219(4), `s 219(4) the person is entitled to vote on the resolution` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE for the person making the offer or an associate (the text's flat "Neither ... is entitled to vote"); NOTHING for anyone else. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |
| F-NT-E2 | s 219(4)(a), `s 219(4)(a) the person is entitled to be sent a copy of the written resolution` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE when the person would not otherwise be entitled ("they are entitled (if they would otherwise be so entitled)"); NOTHING outside the written-resolution case. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |
| F-NT-E3 | s 219(4)(b), `s 219(4)(b) the person is entitled to notice of the meeting, to attend and speak and, if present, to count towards the quorum` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE when the person would not otherwise be entitled; NOTHING outside the meeting case. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |
| F-NT-E4 | s 229(2), `s 229(2) the member is entitled to be provided with a copy` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE until the request is made and the fee paid ("on request and on payment of such fee as may be prescribed"); NOTHING for a non-member. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |
| F-NT-E5 | s 238(2), `s 238(2) the member is entitled to be provided with a copy` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE until the request is made and the fee paid; NOTHING for a non-member. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |
| F-NT-E6 | s 266(4)(c), `s 266(4)(c) the company is entitled to take part in the further proceedings on the application` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE when the application was refused ("If the application is not refused under subsection (3)"); NOTHING when that is not known. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |
| F-NT-E7 | s 267(4)(c), `s 267(4)(c) the company is entitled to take part in the further proceedings on the application` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE when the application was refused; NOTHING when that is not known. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |
| F-NT-E8 | s 269(4)(c), `s 269(4)(c) the company is entitled to take part in the further proceedings on the application` **[name-test sweep 2026-11-12: listed, not flipped]** | An "entitled" function: an entitlement is a claim, not a power, and the Guide does not settle whether a failed gate gives NOTHING or JUST FALSE. Current answer: JUST FALSE when the application was refused; NOTHING when that is not known. | Not settled by the sweep: left as written; a question for the maintainer or a lawyer. |

### Name-test sweep of 2026-11-12

The team lead's specification: a layer-1 function named for a grant or a power ("may", "is permitted", "has power", "entitled", "authorised") that answers `JUST FALSE` because an "if" gate failed reads as "may not", which is a grant turned into a bar; the Guide gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit".
Every function of this part whose name contains "may", "permitted", "power", "entitled" or "authorised" (65 of them; none is named "authorised") was read against its source sentence.
The other 25 never answer `JUST FALSE` for a failed gate (they already answer `NOTHING`, or only `JUST TRUE`), so no column applies to them: ss 229(1), 238(1), 229(5), 238(5), 233, 234(1), 235(1), 243(2), 244(3), 247(1), the six "consequential order" functions of ss 261(2)(b), 262(3)(b), 264(3)(b), 266(3)(b), 267(3)(b) and 269(3)(b), ss 262(2), 264(2), 267(2), 269(2), 265(1), 265(4), 260(3) (the defendant), 254(4) and 255(4).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 9 | 16 | 0 | 8 |

**Flipped to NOTHING (9; one fork line each in the fork register, F-NT-1 to F-NT-9, and in the marginal readings):**
`s 226E(5) the court may relieve the director from liability`;
`s 244(1) the court may make an order for the disclosure of protected information`;
`s 245(1) the registrar may put the director's usual residential address on the public record`;
`s 261(3) the court may give directions as to the evidence and may adjourn the proceedings`;
`s 262(4) the court may give directions as to the evidence and may adjourn the proceedings`;
`s 264(4) the court may give directions as to the evidence and may adjourn the proceedings`;
`s 266(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings`;
`s 267(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings`;
`s 269(4)(b) the court may make an order requiring evidence to be produced by the company and may adjourn the proceedings`.
Each now answers NOTHING when its "if" gate fails ("if the application is not dismissed", "if the application is not refused", "if (a) ... or (b) ...") and the other reading, JUST FALSE, is named in its fork line.
Eleven layer-1 assertions and nine seat cases were restated in place, each with `-- RECONCILED 2026-11-12: was <the original assertion text>; <reason>`.

**Kept JUST FALSE because the text closes the gate itself (16):**
`s 244(2) an order for disclosure by the registrar may be made` ("is to be made only if");
`s 245(4) the notice may be sent to a service address provided in place of the usual residential address` ("must be sent ... unless it appears ..., in which case it may be sent");
`s 247(4) the power may be exercised` ("may only be exercised if");
`s 247(7) the payment may be made` ("must be made" before winding up and out of profits);
`s 260(2) the derivative claim may be brought` ("may only be brought");
`s 260(3) a derivative claim under this Chapter may be brought in respect of the cause of action` ("may be brought only in respect of");
`s 265(2) a member may raise such proceedings` ("only under subsection (1)");
`s 266(1) derivative proceedings may be raised by the member` ("only with the leave of the court");
`s 217(1)`, `s 217(2) the company may not make the payment`; `s 218(1)`, `s 218(2) no person may make the payment`; `s 219(1) no person may make the payment`; `s 226B(1) the quoted company may not make the remuneration payment`; `s 226C(1) no person may make the payment for loss of office` (each "may not ... unless");
`s 241(1) the company may not use or disclose the protected information` ("must not ... except").

**Also kept, and not counted in the column (7): a bar, or the provision's own question, not named for a grant (test 2):**
`s 214 the transaction or arrangement may no longer be avoided under section 213`;
`s 246(4) no service address may be registered for the director other than the usual residential address`;
`s 246(5)(a) subsection (4) limits the service address that may be registered`;
`s 247(2) the general duty in section 172 prevents the exercise of the power`;
`s 247(3) a restriction flowing from the company's objects prevents the exercise of the power`;
`s 228(2) the copies and memoranda are kept at a permitted place`;
`s 237(3) the copy or memorandum is kept at a permitted place`.

**Listed: "may" with a "where", "when" or "upon" gate (0):** none of the functions in this part is of that kind; the gates in the grants above are "if" gates.

**Listed: "entitled" (8; one row each in the fork register, F-NT-E1 to F-NT-E8, not flipped):**
`s 219(4) the person is entitled to vote on the resolution`;
`s 219(4)(a) the person is entitled to be sent a copy of the written resolution`;
`s 219(4)(b) the person is entitled to notice of the meeting, to attend and speak and, if present, to count towards the quorum`;
`s 229(2) the member is entitled to be provided with a copy`;
`s 238(2) the member is entitled to be provided with a copy`;
`s 266(4)(c) the company is entitled to take part in the further proceedings on the application`;
`s 267(4)(c) the company is entitled to take part in the further proceedings on the application`;
`s 269(4)(c) the company is entitled to take part in the further proceedings on the application`.


### Rulings in force (copied word for word from the brief; the rows above that carry a `NOTHING-kind` tag follow them)

In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.


## Jural relations (coa5)

Hohfeld's correlatives: a claim is matched by a duty, a privilege (liberty) by a no-right, a power by a liability (being subject to the power, not an obligation), and an immunity by a disability.
One row per provision that creates a relation; the right is held by the party named first.
Rows that only define a term, count a time or state a fact create no relation and say `none`.
The relations are recorded here and the rules do not type them: the brief's ruling N2 keeps the Hohfeld kinds in this table, and the rule answers `JUST TRUE` or `JUST FALSE`.

| provision | right, privilege, power or immunity (holder) | correlative: duty, no-right, liability or disability (bearer) | L4 rule |
| --- | --- | --- | --- |
| s 205(1)-(5) | privilege (liberty): the company, to provide a director with funds for defence without members' approval, on the stated terms | no-right: the members, who cannot insist on approval under ss 197, 198, 200, 201 | `s 205(1) approval under sections 197, 198, 200 and 201 is not required by this section` |
| s 205(3), (4) | none (counting rules: when a conviction, judgment or refusal becomes final; when an appeal is disposed of) | none | `s 205(3) ...`, `s 205(4) ...` |
| s 206 | privilege: the company, to fund a director's defence in a regulatory investigation or action | no-right: the members | `s 206 approval under sections 197, 198, 200 and 201 is not required by this section` |
| s 207(1)-(3) | privilege: the company, to make minor loans and credit transactions without approval | no-right: the members | `s 207(1)`, `s 207(2)`, `s 207(3)` functions |
| s 208 | privilege: the company, to deal with an associated body corporate without approval | no-right: the members | `s 208 approval is not required by this section` |
| s 209(1), (3) | privilege: a money-lending company, to lend in the ordinary course without approval; to make a home loan to a director or employee | no-right: the members | `s 209(1)`, `s 209(3)` functions |
| s 209(2), (4) | none (definitions: money-lending company, home loan) | none | `s 209(2)`, `s 209(4)` |
| s 210 | none (what counts as other relevant transactions) | none | `s 210(1)` to `s 210(5)` |
| s 211, s 212 | none (value of a transaction; the person for whom it is entered into) | none | `s 211(1)` to `s 211(7)`, `s 212 ...` |
| s 213(2) | power: the company, to avoid a transaction made in contravention | liability (subjection): the other party to the transaction | `s 213(2) the transaction or arrangement is voidable at the instance of the company` |
| s 213(3), (4) | claim: the company, to an account of gains and an indemnity for loss | duty: each person liable (the director, the connected person, the director connected with that person, an authorising director) | `s 213(3) ...`, `s 213(4) ...`, amounts `s 213(3)(a)`, `s 213(3)(b)` |
| s 213(6), (7) | immunity (defence): a director who took all reasonable steps; a connected person or director who did not know | disability: the company, which cannot hold them liable | `s 213(6) ...`, `s 213(7) ...` |
| s 213(1), (5), (8) | none (application; ordering of subsections; saving of other law) | none | `s 213(1) ...`, `s 213(5) ...`, `s 213(8) ...` |
| s 214 | immunity: the other party and the director, from avoidance once affirmed | disability: the company, which can no longer avoid under s 213 | `s 214 the transaction or arrangement may no longer be avoided under section 213` |
| s 215(1)-(5) | none (definitions and extensions: payment for loss of office; benefits not in cash; payments to connected persons; payments by others; quoted companies carved out) | none | `s 215(1)` to `s 215(5)` |
| s 216 | none (amounts taken to be payments for loss of office) | none | `s 216(1)`, `s 216(2)(a)`, `s 216(2)(b)` |
| s 217(1), (2) | claim: the company's members, that the company not pay a director for loss of office without their approval | duty (SHANT): the company | `s 217(1) the company may not make the payment`, `s 217(2) ...`, duty `s 217(1) and (2) the company's duty not to make the payment` |
| s 217(3), 218(3), 219(3) | claim: the members whose approval is sought, to a memorandum of the particulars before the resolution is passed | duty: the company (and those proposing the resolution) | `s 217(3)`, `s 218(3)`, `s 219(3)` functions |
| s 217(4), 218(4), 219(6) | immunity: the members of a non-UK-registered or wholly-owned body corporate, from the approval requirement | disability: the company, which cannot require it | `s 217(4)`, `s 218(4)`, `s 219(6)` |
| s 218(1), (2), 219(1) | claim: the members of the company (or the relevant shareholders), that no person pay a director in connection with a transfer without approval | duty (SHANT): any person making the payment | `s 218(1)`, `s 218(2)`, `s 219(1)` |
| s 218(5), 219(7) | none (a presumption of fact: a payment under an arrangement is presumed to be within the section) | none | `s 218(5)`, `s 219(7)` |
| s 219(2) | none (definition: relevant shareholders) | none | `s 219(2)` |
| s 219(4) | disability: the offeror and its associates, who may not vote; privilege/claim: they keep a copy, notice, attendance, speech, quorum | no-right: the offeror; duty: the company, to send notice and a copy | `s 219(4)`, `s 219(4)(a)`, `s 219(4)(b)` |
| s 219(5) | power: the company's directors, to treat the payment as approved after two inquorate meetings | liability: the members | `s 219(5) the payment is deemed to have been approved` |
| s 220(1)-(5) | privilege: the payer, to pay in good faith under an existing obligation, damages, settlement or pension without approval | no-right: the members | `s 220(1)` to `s 220(5)` |
| s 221(1)-(4) | privilege: the payer, to make a small payment (up to 200 pounds with other relevant payments) without approval | no-right: the members | `s 221(1)` to `s 221(4)` |
| s 222(1)(a), (2), (3)(a) | claim: the company that made the payment (s 217), the company whose undertaking is transferred (s 218), the shareholders who sold (s 219), to the sum held on trust | duty: the recipient, as trustee | `s 222 the payment is held by the recipient on trust for` |
| s 222(1)(b) | claim: the company that made the payment, to an indemnity | duty: any director who authorised the payment, jointly and severally | `s 222(1)(b) ...` |
| s 222(3)(b) | claim: the persons who sold their shares, to the full sum | duty: the recipient, who bears the distribution expenses | `s 222(3)(b) ...` |
| s 222(4), (5) | none (which subsection applies where two sections are contravened) | none | `s 222(1)`, `s 222(2)`, `s 222(3)` |
| s 223(1), (2) | none (a shadow director is treated as a director; loss of status as shadow director is not loss of office) | none | `s 223(1) ...`, `s 223(2) ...` |
| s 224(1), (2) | immunity: the company, whose resolution stands despite an accidental failure to send the memorandum | disability: the members who were not sent it, who cannot object on that ground | `s 224(1) ...`, `s 224(2) ...` |
| s 225(1)-(3) | none (approval under several provisions: each must be met; one resolution may serve) | none | `s 225(1)`, `s 225(2)`, `s 225(3)` |
| s 226 | none (shown as dots) | none | none |
| s 226A(1)-(10) | none (definitions and rules of reading for Chapter 4A) | none | the `s 226A(...)` functions |
| s 226B(1), 226C(1) | claim: the members of a quoted company, that it not pay a director a remuneration payment or loss of office payment unless consistent with the approved policy or approved by resolution | duty (SHANT): the company (s 226B) or any person (s 226C) | `s 226B(1) the quoted company may not make the remuneration payment`, `s 226C(1) no person may make the payment for loss of office`, duty `s 226B(1) and s 226C(1) the duty not to make the payment` |
| s 226B(2), 226C(2) | none (definition: the approved directors' remuneration policy) | none | `s 226B(2)`, `s 226C(2)` |
| s 226D(1), (2) | claim: the members, to a memorandum available for inspection at the registered office for 15 days and at the meeting, explaining the inconsistency | duty: the company | `s 226D(1)`, `s 226D(2)` |
| s 226D(3) | claim: the members (and anyone), to the memorandum on the website until the next accounts meeting | duty: the company | `s 226D(3) the company has ensured the memorandum is available on its website` |
| s 226D(4), (5), (6), (7) | immunity (the meeting's validity is unaffected); none (nothing in 226B/226C authorises a payment contrary to the articles); immunity (payments before the first policy are outside 226B/226C); none (definition of the company's website) | disability: anyone challenging the meeting; none; disability: the members; none | `s 226D(4)` to `s 226D(7)` |
| s 226E(1) | immunity: the company, from an obligation to make a payment that would contravene 226B or 226C | disability: the payee, who has no enforceable obligation | `s 226E(1) the obligation has effect` |
| s 226E(2)-(4) | claim: the company or person making the payment, the company whose undertaking is transferred, the sellers of shares, to the sum held on trust; the company, to an indemnity from an authorising director | duty: the recipient as trustee; the authorising director | `s 226E the payment is held by the recipient on trust for`, `s 226E(2)(b)`, `s 226E(4)(c)` |
| s 226E(5) | power: the court, to relieve a director who acted honestly and reasonably | liability: the company and the other claimants, who are subject to the relief | `s 226E(5) the court may relieve the director from liability` |
| s 226F(1), (2) | none (Chapter 4A does not affect Chapter 4; Chapter 4 approval counts for 226B(1)(b) and 226C(1)(b)) | none | `s 226F(1)`, `s 226F(2)` |
| s 227(1), (2) | none (definition of a director's service contract; the Part applies to the terms of appointment) | none | `s 227(1)`, `s 227(2)` |
| s 228(1)-(3), (7) | claim: members (s 229) and anyone who may inspect, to a copy or memorandum kept available at the registered office (or a specified place) for at least a year | duty: the company | `s 228(1)`, `s 228(2)`, `s 228(3)`, `s 228(7)` |
| s 228(4) | claim: the registrar, to notice of the place and of any change | duty: the company (14 days: offence) | `s 228(4)` function and rule |
| s 228(5), (6) | claim: the Crown (prosecution), power to prosecute and punish | liability: every officer of the company in default | `s 228(5)`, `s 228(6)` |
| s 229(1), (2) | claim: any member, to inspect without charge and to a copy within seven days on request and payment of the prescribed fee | duty: the company | `s 229(1)`, `s 229(2)` and the rule `s 229(2) the company's duty to provide the copy` |
| s 229(3), (4) | claim: the Crown, as in s 228(5), (6) | liability: every officer in default | `s 229(3)`, `s 229(4)` |
| s 229(5) | power: the court, to compel inspection or direct that the copy be sent | liability: the company (and officers in default) | `s 229(5)` |
| s 230, 231(5) | none (a shadow director is treated as a director) | none | `s 230`, `s 231(5)` |
| s 231(1)-(2) | claim: the sole member's company's other stakeholders, to a record of the terms of a non-ordinary-course contract with the sole member who is a director | duty: the company, to ensure the terms are set out in a memorandum or minuted | `s 231(1)`, `s 231(2)` and the rule |
| s 231(3), (4) | claim: the Crown, as in s 228(5), (6) (fine up to level 5, no daily fine) | liability: every officer in default | `s 231(3)`, `s 231(4)` |
| s 231(6), (7) | immunity: the contract, whose validity is unaffected; none (savings of other law) | disability: anyone who would avoid it for want of the record; none | `s 231(6)`, `s 231(7)` |
| s 232(1), (2) | immunity-denial: none; the company and its members hold the claim that no provision exempts or indemnifies a director (voidness) | disability: the director and the company, who cannot make an effective exemption or indemnity | `s 232(1)`, `s 232(2)` |
| s 232(3), (4) | none (where a provision is found; the articles may deal with conflicts of interest) | none | `s 232(3)`, `s 232(4)` |
| s 233, 234(1), 235(1) | privilege: the company, to buy insurance for, and to give a qualifying third party or pension scheme indemnity to, a director | no-right: the members and the company's creditors, who cannot object under s 232(2) | `s 233`, `s 234(1)`, `s 235(1)` |
| s 234(2)-(6), 235(2)-(6) | none (definitions: qualifying provision; finality; relief; occupational pension scheme) | none | `s 234(2)` to `s 234(6)`, `s 235(2)` to `s 235(6)` |
| s 236(1)-(5) | claim: the members who read the directors' report, to a statement that qualifying indemnity provision is (or was) in force | duty: the company's directors (who approve the report), for the company | `s 236(1)`, `s 236(2) to (5)`, `s 236 the directors' report meets the requirement` |
| s 237(1)-(5), (8), (9) | claim: members and any person entitled to inspect, to the copy or memorandum of qualifying indemnity provision kept at the registered office for a year after the provision ends | duty: the company of which the director is a director, and (if it made the provision) the associated company | `s 237(1)` to `s 237(5)`, `s 237(8)`, `s 237(9)` |
| s 237(6), (7) | claim: the Crown, to prosecute and punish (level 3 and a daily default fine of one-tenth of level 3) | liability: every officer in default | `s 237(6)`, `s 237(7)` |
| s 238(1)-(5) | claim: any member, to inspect without charge and to a copy within seven days on request and fee; power: the court, to compel | duty: the company; liability: the company and officers in default | `s 238(1)` to `s 238(5)` |
| s 239(2) | power: the members, by resolution, to ratify a director's conduct | liability: the company and the director, who are bound by the ratification; the director, who may be relieved | `s 239(2)` |
| s 239(3), (4) | disability: the director and members connected with him, who are not eligible members and whose votes are disregarded; privilege: they may attend, count towards the quorum and take part | no-right: the other members; duty: the company, to allow them to attend | `s 239(3)`, `s 239(4)` |
| s 239(5)-(7) | none (definitions and savings: conduct, director, shadow director, s 252(3), unanimous consent, directors' power to settle, other law) | none | `s 239(5)(a)` to `s 239(7)` |
| s 240(1)-(3) | none (what is protected information; protection continues after the director leaves) | none | `s 240(2)`, `s 240(3)` |
| s 241(1), (2) | claim: the director, that the company not use or disclose his usual residential address except to communicate with him, for particulars to the registrar, or under a court order; power: the director, to consent | duty (SHANT): the company; liability: the company, which may use with consent | `s 241(1)`, `s 241(2)` and the rule `s 241(1) the company's duty not to use or disclose protected information` |
| s 241(3), (4) | claim: the Crown, to prosecute and punish | liability: the company and every officer in default | `s 241(3)(a)`, `s 241(3)(b)`, `s 241(4)` |
| s 242(1), (3) | claim: the director, that the registrar omit and not disclose his address | duty: the registrar | `s 242(1)`, `s 242(3)` |
| s 242(2) | privilege: the registrar, not obliged to check other documents or omit earlier material | no-right: the director | `s 242(2)` |
| s 243(2), (4), (7) | privilege: the registrar, to disclose protected information to a credit reference agency; claim: the director, to be spared if the regulations so provide | no-right: the director; duty: the registrar (under the regulations) | `s 243(2)`, `s 243(4)`, `s 243(7)` |
| s 243(1), (3), (5), (6), (6A), (8) | none (shown as dots; regulation-making machinery) | none | none |
| s 244(1)-(4) | power: the court, to order disclosure; privilege: a liquidator, creditor, member or other interested person, to apply | liability: the company and the registrar, who are subject to the order; the director, whose address may be disclosed; no-right: the company (as to the order's terms) | `s 244(1)` to `s 244(4)` |
| s 245(1)-(5) | power: the registrar, to put the address on the public record; claim: the director and the director's companies, to notice, grounds, a period for representations and account taken of them | liability: the director; duty: the registrar | `s 245(1)` to `s 245(5)` |
| s 246(1)-(6) | duty: the registrar, to treat the address as the service address; claim: the director and each relevant company, to notice stating the decision date; immunity: the registrar's act, five-year bar on registering another service address (not for s 1097B) | liability: the director, whose address is public for five years; duty: the registrar | `s 246(1)` to `s 246(6)` |
| s 247(1)-(7) | power: the directors, to make provision for employees on cessation or transfer of the business (despite s 172 and, for a charity, its objects) | liability: the company (it bears the cost) and its members, whose interest in the profits is subject to the power; no-right: the members; duty: the directors, to meet the sanction, articles and timing conditions | `s 247(1)` to `s 247(7)` |
| s 248(1), (2) | claim: the company's members, directors and anyone entitled to see the records, to minutes of all proceedings at directors' meetings kept for ten years | duty: the company | `s 248(1)`, `s 248(2)` and the rule |
| s 248(3), (4) | claim: the Crown, to prosecute and punish | liability: every officer in default | `s 248(3)`, `s 248(4)` |
| s 249(1), (2) | privilege: the company and anyone relying on the minutes, to treat them as evidence and the meeting, proceedings and appointments as valid until the contrary is proved | no-right: anyone challenging them, who bears the burden of proving the contrary | `s 249(1)`, `s 249(2)` |
| ss 250, 251, 252, 253, 254, 255, 256, 257 | none (definitions: director, shadow director, connected person, family, connected with a body corporate, controlling, associated, constitution) | none | the functions of coa5-director-definitions.l4 |
| s 258(1), (2) | none (machinery: the Secretary of State's power to substitute larger sums) | none | none |
| s 258(3) | immunity: anyone who did or failed to do something before an order came into force | disability: the Secretary of State, whose order cannot reach it | `s 258(3) an order under this section has effect in relation to the thing done or not done` |
| s 259 | none (the governing law of an arrangement or transaction is immaterial for this Part) | none | `s 259 ...` |
| s 260(1)-(5) | none (definition of a derivative claim; when it may be brought; whether it matters when the cause of action arose; who counts as a director and member) | none | `s 260(1)` to `s 260(5)` |
| s 261(1) | duty: the member, to apply for permission (leave) to continue a derivative claim | claim: the court and the company, to an application before the claim continues | `s 261(1)` function and rule |
| s 261(2)-(4), 262(3)-(5), 264(3)-(5) | power: the court, to dismiss, give directions, adjourn, grant on terms or refuse; duty: the court, to dismiss where no prima facie case appears | liability: the applicant member and the company, who are subject to the court's orders; claim: the applicant, to a dismissal only on those facts | `s 261(2)` to `s 261(4)`, `s 262(3)` to `s 262(5)`, `s 264(3)` to `s 264(5)` |
| s 262(1), (2) | power: a member, to apply for permission to continue a claim the company has brought, on the three grounds | liability: the company, whose claim may be taken over | `s 262(1)`, `s 262(2)` |
| s 263(1)-(4), 268(1)-(3) | duty: the court, to refuse permission or leave where satisfied of the stated grounds, to take stated matters into account, and to have regard to disinterested members' views | claim: the company, and the members who oppose the claim, to those considerations; disability: the applicant, who cannot obtain permission on those grounds | `s 263(1)` to `s 263(4)`, `s 268(1)` to `s 268(3)` |
| s 263(5)-(7), 268(4)-(6) | none (machinery: regulation-making powers) | none | none |
| s 264(1), (2) | power: another member, to apply to continue a claim the claimant has brought or continued | liability: the claimant, who may be displaced | `s 264(1)`, `s 264(2)` |
| s 265(1)-(7) | power: a member in Scotland, to raise derivative proceedings for the company; immunity: the member's own right to proceed for his own interests and the court's power under s 996(2)(c) are not affected | liability: the director or another person sued; disability: nobody may stop the member's own-interest proceedings by this section | `s 265(1)` to `s 265(7)` |
| s 266(1), (2) | claim: the court, to leave before derivative proceedings are raised and to an application specifying the cause of action and summarising the facts | duty: the member (applicant) | `s 266(1)`, `s 266(2)` |
| s 266(3)-(5), 267(3)-(5), 269(3)-(5) | power and duty: the court, as in s 261 (refuse, order evidence, grant, refuse, adjourn); duty: the applicant, to serve the application on the company; claim: the company, to take part | liability: the applicant and the company | `s 266(3)` to `s 266(5)`, `s 267(3)` to `s 267(5)`, `s 269(3)` to `s 269(5)` and the rule `s 266(4)(a) the applicant's duty to serve the application on the company` |
| s 267(1), (2), 269(1), (2) | power: a member, to apply to be substituted for the company (s 267) or for the claimant (s 269) on the three grounds | liability: the company; the claimant | `s 267(1)`, `s 267(2)`, `s 269(1)`, `s 269(2)` |


## Marginal readings for a lawyer (coa5)

Each line lists branches that rest on one of the two readings the brief leaves open for a lawyer: (a) a failed "if" counts as the text's no, clause by clause within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
The status quo is taken in every case, and the other reading is stated.

- ss 205(1), 207(1)-(3), 209(1), 220(1), 221(1): "Approval is not required ... if ..." and "for a payment made in good faith". Taken: the function asks whether THIS section removes the requirement; a failed "if" is JUST FALSE (reading (a): a failed "if" counts as the text's no); the other reading: NOTHING (the text says only when approval is not required, not that it is required otherwise). Good faith (s 220(1)) is taken as a limit on the grant (reading (b): NOTHING) and not as an "if".
- ss 205(2), 205(4), 209(2), 209(4), 215(1), 220(2), 220(3), 221(3), 221(4): a definition the text states with "means", "are" or "the conditions are": JUST FALSE for a case outside it (the delegated and closed definitions: flat "means"); for "are" (s 219(2) only) NOTHING is taken, and F-219-1 records the other reading. Other reading of the "means" cases: NOTHING.
- ss 205(5), 206, 208, 210(3)-(4), 216(2), 217(4), 218(4), 219(6), 219(4)(a)-(b): a grant or immunity limited by its own wording ("a body corporate that ..."): NOTHING outside the limit (reading (b)); the other reading: JUST FALSE.
- ss 217(1)-(3), 218(1)-(3), 219(1), (3): flat negatives "may not ... unless" (N2: flat negatives count as the text's no): JUST TRUE for "the bar applies" when the "unless" condition is unmet, JUST FALSE when it is met (F-UNLESS-1); the other reading for the met case is NOTHING.
- s 213(2): "voidable ... unless" met: JUST FALSE (F-213-2). ss 213(6), 213(7): "is not liable ... if he shows that" (a defence, ruling (b) of 2026-11-05): when not shown, JUST FALSE for that provision's defence ("this subsection gives no defence on these facts"), never "no defence at all".
- ss 218(5), 219(7), "except in so far as the contrary is shown": JUST FALSE when shown (F-218-1); the other reading: NOTHING, the presumption surviving in part.
- s 219(5): a deeming provision introduced by "If": a failed "if" is JUST FALSE ("not deemed"); the other reading: NOTHING.
- s 213(8), a flat saving ("Nothing in this section shall be read as excluding ..."): JUST FALSE.
- s 215(5): a flat negative ("Nothing in this section or sections 216 to 222 applies ..."): JUST FALSE for a payment to a director of a quoted company other than the s 226D(6) exception; NOTHING elsewhere.
- ss 223(1), 226A(6), 226A(7), 226A(10), 215(2)-(4): extensions phrased with "include" or "is treated as": NOTHING for a case outside the listed extension (includes); the other reading is JUST FALSE for an outsider (not covered by the extension).
- s 224(1): "Where (a) ... and (b) ..., any accidental failure ... shall be disregarded": a failed "where" is JUST FALSE (periods ruling (b)); a failure that is not accidental is outside the grant: NOTHING (reading (b)); the other reading for both: the opposite choice.
- s 225(2), 225(3): "If so, ... must be met" and "This does not require": the "if so" scope (approval required under more than one provision) gives NOTHING when it fails; when it holds, a bare "must" not done is JUST FALSE and "does not require" is JUST FALSE (a flat negative). The other reading for the bare "must" not done: NOTHING (the text says what must be met, not what follows).
- ss 226D(4), 226D(5), 226F(1): flat negatives ("does not affect", "Nothing ... authorises", "does not affect any requirement"): JUST FALSE inside their stated case, NOTHING outside it.
- s 226D(6): "Nothing in section 226B or 226C applies ... before the earlier of": JUST FALSE for the proposition "226B and 226C apply" before the earlier date; NOTHING on or after it (the subsection is silent after). The other reading: JUST TRUE after.
- s 226E(5): "the court may relieve": "if" (a) and (b) unmet is JUST FALSE ("this subsection gives the court no power on these facts"); the other reading: NOTHING.
- ss 226B(2), 226C(2): "The approved directors' remuneration policy is the most recent ...": a definition with "is": taken as closed (JUST FALSE otherwise); the other reading: NOTHING.
- ss 227(1), 227(2), 228(2): "means" and "must be kept ... at (a) or (b)" closed lists: JUST FALSE for a case outside; the other reading: NOTHING.
- ss 228(1), 228(2), 231(2): a bare "must" not done: JUST FALSE for "has the duty been met" (F-MUST-1); the other reading: NOTHING.
- s 228(3): a stated period (one year): after it JUST FALSE (the periods ruling (a)); F-228-1 records the anniversary day.
- ss 228(4), 231(2): "unless" met (always kept at the registered office; the contract is in writing): JUST FALSE for "the company must give notice" and "must ensure"; the other reading: NOTHING.
- ss 228(5), 229(3), 231(3): "If default is made ... an offence is committed by every officer ... who is in default": the "if" failing is JUST FALSE for the offence; for an officer not in default NOTHING (a scope limit, with no "only"); the other reading: JUST FALSE for that officer.
- s 229(2): "entitled, on request and on payment of such fee" is read as "upon": JUST FALSE until requested and paid (ruling (c)); the other reading: NOTHING (a limit in the grant's own wording).
- ss 227(2), 231(6), 231(7), 229(5): the flat negatives "not restricted", "does not affect", "Nothing ... shall be read as excluding": JUST FALSE.
- s 232(2): "void, except as permitted by ss 233, 234, 235": an "except" (F-232-1); s 233, 234(1), 235(1): "does not prevent" and "does not apply to": grants limited by their wording: NOTHING outside them (reading (b)); the other reading: JUST FALSE.
- ss 234(2), 235(2): "Such provision is qualifying ... if the following requirements are met": a failed "if" is JUST FALSE for "is qualifying" (reading (a)); the other reading: NOTHING. ss 234(3), 235(3): "must not provide any indemnity against": a flat negative on the provision: JUST FALSE when it does provide one.
- s 236(2)-(5): "If ... in force ..., the report must state": a failed "if" is JUST FALSE for "must state"; a bare "must" not done is JUST FALSE for "the report meets the requirement" (F-MUST-1).
- ss 237(2)-(4), (6), 238: as ss 228, 229 (the notes above).
- s 239(2): bare "must" (F-MUST-1). ss 239(3), (4): "neither ... is an eligible member", "disregarding votes in favour": flat negatives inside their stated case (a written resolution; a meeting), NOTHING outside; the other reading: JUST FALSE for a member the subsection does not name.
- s 239(5)(a)-(c), "includes", "is treated as": NOTHING outside the extension; s 239(5)(d), (6), (7): flat negatives: JUST FALSE.
- s 240(2): "That information is referred to in this Chapter as 'protected information'": a definition by reference taken as closed (JUST FALSE for other information); the other reading: NOTHING. s 240(3): "does not cease": a flat negative: JUST FALSE inside its case.
- s 241(1): "must not ... except": the three exceptions give JUST FALSE (F-UNLESS-1 applies to "except" too); s 241(2): "does not prohibit ... with the consent": JUST FALSE with consent, NOTHING without (the subsection says only what consent does).
- ss 241(3), 245(1), 244(1): "If ... an offence is committed", "may ... if", "may make an order ... if ... and the court is otherwise satisfied": a failed "if" is JUST FALSE (reading (a)); the court's satisfaction is an input.
- s 244(2): "only if": JUST FALSE otherwise (closed with "only"); s 244(3): the list of applicants is not closed (NOTHING for another person unless the court sees a sufficient interest).
- ss 245(5), 246(4): "within the specified period", "for the period of five years": outside the period JUST FALSE (the periods ruling (a)); the other reading: NOTHING.
- s 242(2), 243(2), 246(5)(a): "not obliged", "may disclose", "does not limit": a flat negative or a grant limited by its own wording; JUST FALSE inside, NOTHING outside.
- ss 247(2), 247(3): "exercisable notwithstanding": taken as the flat negative "this duty / these restrictions do not prevent the exercise": JUST FALSE where the power exists, NOTHING otherwise. s 247(4): "may only be exercised if sanctioned": closed with "only": JUST FALSE otherwise.
- ss 247(6), 247(7), 248(1), 244(4), 245(3), 246(3): a bare "must" not done: JUST FALSE for "has the duty / requirement been met" (F-MUST-1); the other reading: NOTHING.
- s 249(1), 249(2): "are evidence if ..." and "until the contrary is proved": a failed "if" is JUST FALSE for "evidence by this subsection"; "where minutes have been made" is a "where" (JUST FALSE when it fails); "until the contrary is proved": JUST FALSE once proved. The other reading for each: NOTHING.
- s 250 ("includes"), 253 ("are" list): NOTHING outside (F-250-1, F-219-1); other reading: JUST FALSE.
- ss 251(1), 252, 254(2), 255(2) ("means", "(and only those persons)", "if, but only if"): closed with "means", "only": JUST FALSE outside; ss 251(2), 251(3): "is not to be regarded ... by reason only": JUST TRUE for the excluding proposition inside its case, NOTHING outside it.
- s 252(2)(a): the family limb passes s 253's answer: NOTHING for a relation outside s 253's list (F-219-1), so the composite s 252 answers NOTHING, not JUST FALSE, for such a person; the other reading: JUST FALSE.
- s 256: "are associated if": a failed "if" is JUST FALSE (reading (a)); the other reading: NOTHING.
- s 258(3): "does not have effect ... before it comes into force": JUST FALSE for a thing done before; NOTHING from the day it comes into force (what an order provides is outside the sources).
- ss 260(1), 262(1), 264(1), 265(3), 267(1), 269(1): "applies where", "is referred to as", "is any ... act": a failed "where" is JUST FALSE (periods ruling (b)); the other reading: NOTHING.
- ss 260(2), 260(3), 266(1), 265(2): "may only be brought", "may be brought only", "only with the leave", "only under subsection (1)": closed with "only": JUST FALSE otherwise.
- ss 261(2), 262(3), 264(3), 266(3), 267(3), 269(3): "If it appears to the court ... must dismiss": F-261-1; ss 261(3), 262(4), 264(4), 266(4), 267(4), 269(4): "If the application is not dismissed (refused) ...": JUST FALSE where it was dismissed (reading (a)); the other reading: NOTHING.
- ss 261(4), 262(5), 264(5), 266(5), 267(5), 269(5): "On hearing the application, the court may (a), (b) or (c)": a list not closed (NOTHING for another course); the other reading: JUST FALSE for a course not listed.
- ss 262(2), 264(2), 267(2), 269(2): "may apply ... on the ground that (a), (b) and (c)": the grounds limit the grant by its own wording: NOTHING when a ground is missing (reading (b)); the other reading: JUST FALSE.
- ss 263(2), 268(1): "must be refused if the court is satisfied": JUST FALSE when no ground is satisfied (reading (a) for a failed "if"); the other reading: NOTHING. ss 263(4), 268(3): "shall have particular regard to any evidence": NOTHING without evidence.
- s 226E(5) (F-NT-1): the court may relieve "if" (a) and (b), with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 244(1) (F-NT-2): the court may order disclosure "if" (a) or (b) and it is otherwise satisfied, with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 245(1) (F-NT-3): the registrar may put the address on the record "if" (a) or (b), with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 261(3) (F-NT-4): the court may give directions "if the application is not dismissed", with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 262(4) (F-NT-5): the court may give directions "if the application is not dismissed", with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 264(4) (F-NT-6): the court may give directions "if the application is not dismissed", with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 266(4)(b) (F-NT-7): the court may order evidence "if the application is not refused", with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 267(4)(b) (F-NT-8): the court may order evidence "if the application is not refused", with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).
- s 269(4)(b) (F-NT-9): the court may order evidence "if the application is not refused", with no "only if": a power limited by its own wording gives NOTHING when the gate fails (reading (b)); the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)).


### Reading a result: FALSE and NOTHING (coa5)

In this row (the rest of Part 10 and Part 11) a `JUST FALSE` is the Act saying no in its own words, for example:
a "means" or "are" definition not met (s 215(1), "a payment for loss of office"; s 253(3), the people excluded from the "enduring family relationship" limb);
a condition the text introduces with "if" or "unless" that fails or is met (s 217(1), the company may not pay "unless" the members approve);
a period the text fixes that has run out or not begun (s 228(3), "at least one year from the date of termination"; s 229(2), "within seven days"; s 246(4), "five years beginning with the date of the registrar's decision");
a flat negative (s 232(1), (2), "void"; s 226D(4) and s 231(6), "does not affect the validity"; s 260(4) and s 265(5), "immaterial");
a list the text closes with "only" (s 252(2), "and only those persons"; s 254(2), "if, but only if"; s 255(2); s 260(3), "only in respect of a cause of action arising from ...").
Where the text hands a definition to a list ("the relevant shareholders are ...") or a defence is not shown, the answer follows the brief's ruling of 2026-11-05 (a defence not shown is "this subsection gives no defence on these facts", never "no defence at all").

A `NOTHING` is "not covered by what this Act's words say on these facts", never "no".
It is the answer where a grant or prohibition is limited by its own wording and the case falls outside the limit (s 205, "a director of the company or of its holding company"; the offence sections speak of "every officer of the company who is in default", so an officer who is not in default gets NOTHING, not FALSE);
where a list is not closed (s 253(2), the five kinds of family member; s 263(3), the matters the court must take into account "in particular");
where the text says "includes" (s 250, s 257, s 260(5), s 265(7));
where a term is undefined or lies outside the sources (s 1121 "in default", s 112 "member", s 1159 "subsidiary", the regulations and orders under ss 243, 258, 263 and 268, the pounds a level on the standard scale stands for);
and where the text is silent (s 258(3) says an order does not reach things done before it, and says nothing of those done after).
A caller must never turn `NOTHING` into `FALSE`; the seat layer does not either.
Every `JUST FALSE` branch in layer 1 carries `-- FALSE-kind (the text says no in its own words): "<quoted>"` and every `NOTHING` branch carries `-- NOTHING-kind (<why>)`, with the why drawn from: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.

## Seams (coa5)

A seam is an answer another part gives that a rule here needs.
Each is taken as an input named for the answering section, as `PLAN.md` section 4 names them, typed `MAYBE BOOLEAN` so that "not covered" in the answering section stays "not covered" here; the layer-1 rule answers NOTHING (`NOTHING-kind (points outside the text)`) when the input is NOTHING.
The seat layer asks each as a plain yes/no and passes it as `JUST`.

| seam input (the name the layer-1 rule takes) | answering section (part) | used by |
| --- | --- | --- |
| `s 197 ...`, `s 198 ...`, `s 200 ...`, `s 201 ...`, `s 203 the transaction or arrangement was entered into in contravention of section N` | ss 197 to 203 (coa4) | `s 213(1) this section applies`, and through it ss 213(2)-(4), 214 |
| `s 112 the person is a member of the company` | s 112 (coa3) | `s 229(1)`, `s 229(2)`, `s 238(1)`, `s 238(2)`, `s 260(5)(c)`, `s 265(7)(e)` |
| `s 1121 the officer is in default` | s 1121 (coa24) | `s 228(5)`, `s 229(3)`, `s 231(3)`, `s 237(6)`, `s 238(3)`, `s 241(3)(b)`, `s 248(3)` (and the `Officer in default` party in the regulative rules) |
| `s 1136 the place is specified in regulations` | s 1136 (coa25) | `s 228(2)`, `s 237(3)` |
| `s 1159(1) one body corporate is a subsidiary of the other`, `... both bodies corporate are subsidiaries of the same body corporate`, the same for companies, and `the company is a subsidiary of the body corporate` | s 1159 (keel) | `s 256(a)`, `s 256(b)`, `s 251(3)` |
| `s 988 the person is an associate of the person making the offer` | s 988 (coa21) | `s 219(4)` (three functions) |
| `s 629 holds shares of the same class as any of those shares` | s 629 (coa14) | `s 219(2)` |
| `s 385 the company is a quoted company` | s 385 (coa8) | `s 226A(1) the company is a quoted company in this Chapter` |
| `s 17 the matter is one mentioned in section 17` | s 17 (coa1) | `s 257` |
| regulations under s 243(4) "require the registrar, on application, to refrain from disclosing" (not a section: the regulations are not in the sources) | regulations under s 243(4) | `s 243(4)` |

What this part answers for others (each its own function, with the borrowed facts as inputs, as the plan asks): `s 250 the person occupies the position of director`, `s 251 the person is a shadow director`, `s 252 the person is connected with the director` (and (2)(a) to (e), (3)), `s 253(2) the person is a member of the director's family`, `s 254(2) the director is connected with the body corporate`, `s 255(2) the director controls the body corporate`, `s 256(a) the bodies corporate are associated`, `s 256(b) the companies are associated`, `s 257 the matter is part of the company's constitution for the purposes of this Part`, `s 240(3) a reference in this Chapter to a director includes the person`, `s 260(1) the proceedings are a derivative claim`, `s 260(5)(a)` to `(c)`, `s 265(7)(a)` to `(e)`, and `s 226A(1)` to `(10)`.
Sections 254(6) and 255(6) are circularity guards (a body corporate or a trustee connected only through the other test); they are encoded as functions that say when the guard applies and are not wired into the tests of 254(2) and 255(2), which take the already-reduced figures as inputs (the caller applies subsection (4)-(6) first).
No seam was found that `PLAN.md` section 4 lacks, except the regulations in the last row, which the plan could not name because they are not a section.

## Numbered findings: what the text turns out to say

1. **Section 252(2) says "only"; section 253(2) does not.**
   Line 3310: "The following persons (and only those persons) are connected with a director of a company"; line 3327: "For the purposes of this Part the members of a director's family are", with five paragraphs and no "only".
   So the list of connected persons is closed but the family limb of it is, read literally, not (fork F-219-1, reading A).
   Consequence: `s 252` answers NOTHING, not JUST FALSE, for a person who fits none of the five family descriptions and fails every other limb, because the family limb answers NOTHING for "some other relationship".
   The seat case "252: no listed connection" records it.
2. **The money figures are the Act's own and a Secretary of State's order would change the answers.**
   £10,000 (line 2733, s 207(1)), £15,000 (2737, s 207(2)), £50,000 (2789, s 211(7)) and £200 (2909, s 221(1)) are encoded as the Act states them.
   Section 258(1) (line 3371) lets the Secretary of State "substitute for any sum of money specified in this Part a larger sum", and s 258(3) says an order does not reach what was done before it comes into force; the encoding has the date rule (`s 258(3)`) and no input for a substituted sum.
   A user after an order must treat the answers of ss 207, 211 and 221 as stale.
   Asserted.
3. **Section 213(4) and section 213(6) name different sections.**
   Lines 2805-2811: (4)(a) "in contravention of section 197, 198, 201 or 203"; (4)(b) "in contravention of any of those sections"; (4)(c) "the director of the company or of its holding company with whom any such person is connected"; but (6) is about a transaction "in contravention of section 200, 201 or 203 with a person connected with a director of the company or of its holding company", where "that director is not liable by virtue of subsection (4)(c) if he shows that he took all reasonable steps".
   Section 200 is in neither (4)(a) nor (4)(b), yet (6) speaks of a section 200 contravention and of liability under (4)(c) for it.
   Taken (F-213-1, reading A): the literal text, so a s 200 contravention answers NOTHING in `s 213(4)`, and subsection (6)'s s 200 reference has no case to bite on.
   Asserted.
4. **Section 226D(3) is a continuing duty with a stated start and end and no deadline to act by.**
   Line 3001: the memorandum must be on the website "from the first day on which the memorandum is made available for inspection under subsection (1) until its next accounts meeting".
   It is encoded as a decision function over the first and last day it was on the website and the date of the next accounts meeting, and no regulative rule is written for it, so that no deadline is invented.
5. **Section 247(3) speaks only of charities.**
   Line 3269: "In the case of a company that is a charity it is exercisable notwithstanding any restrictions on the directors' powers (or the company's capacity) flowing from the objects of the company."
   For a company that is not a charity the text does not say whether a restriction from its objects prevents the power; the function answers JUST FALSE for a charity and NOTHING otherwise.
6. **Section 254(2) divides by a company's equity share capital, which can be nought.**
   Lines 3336-3338: limb (a) is "interested in shares comprised in the equity share capital of that body corporate of a nominal value equal to at least 20% of that share capital".
   A body corporate with no equity share capital has no such shares, but the arithmetic "0 is at least 20% of 0" is true; the first draft of `s 254(2)` answered JUST TRUE for such a body, which the seat layer's no-connection case exposed.
   Fixed: limb (a) now needs the capital to be more than nought (`coa5-director-definitions.l4`, with a test and a seat case); limb (b), the voting power, is unaffected.
7. **Levels on the standard scale are not in the sources.**
   ss 228(6), 229(4), 231(4), 237(7), 238(4), 241(4)(b) and 248(4) fix penalties by "level 3" or "level 5 on the standard scale" (lines 3048, 3055, 3069, 3151, 3161, 3198, 3286).
   The core's `Fine limit` carries the level and the fraction in layer 1; the seat questions of ss 228(6), 229(4), 231(4), 237(7) and 238(4) that give a figure in pounds take the pounds a level stands for as an input; ss 241(4) and 248(4) have no seat question.
8. **Section 239(4) separates voting from attending.**
   Line 3169: "This does not prevent the director or any such member from attending, being counted towards the quorum and taking part in the proceedings at any meeting at which the decision is considered."
   So a connected member's vote does not count towards the majority, and the member is not prevented from attending: two functions, both asserted.

## What the stable binary does not accept

The binary governs; where the skills describe something it rejects, the rule below was followed.
Each row below was re-run against `l4 1.6.110` on 2026-11-13 before it was written down.

| what | what happens | what was done |
| --- | --- | --- |
| `#ASSERT <deontic rule> EQUALS FULFILLED` | `eval/unsupported-equality`: "assertion could not be evaluated" (an Error, counted as a failed assertion) | a regulative rule is run with `#TRACE`; the outcome (FULFILLED, BREACHED or STANDING) is printed as Information, not asserted; each `#TRACE` carries a `-- TRACE EXPECT: X` comment above it, compared with the printed outcome by a scratch script (27 of 27 hold on 1.6.110 and on the main build 1.6.109); every duty is also encoded as a decision function, which is asserted |
| `NOT x OR y` | read as `NOT (x OR y)`; no error, a wrong answer | every `NOT` is parenthesised: `((NOT x) OR y)` |
| `a NOT EQUALS b` | `parse/unexpected-NOT` | `NOT (a EQUALS b)` |
| `IF c THEN a` newline `ELSE IF d` newline `THEN b` | `parse/indentation` | `BRANCH` with one `IF ... THEN ...` per line and a final `OTHERWISE` |
| `length` of a list | not in the prelude | `elem` against a list of the expected strings (the two "matters the court must take into account" lists) |
| `REFUSE`, `#ASSERT REFUSED`, `YMD`, sets, section `GIVEN`, opaque `DECLARE`, `TYPICALLY` on a field, `BECAUSE` except on `LEST BREACH` | not used (the brief excludes them); `PLAN.md` says the two supplied builds accept some of them | "not covered" is `NOTHING` or a typed constructor, asserted |
| A trace's outcome | `check.sh` counts assertion lines only, so it does not see a different `#TRACE` outcome | each trace was also run on 1.6.109 and read: the same 27 outcomes |

## What check.sh prints

Run as `L4=<1.6.110> L4_MAIN=<1.6.109> ./check.sh` (target `main`, the default; every module is run on both builds and the counts compared).
Exit status 0.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa5-cases-seat.l4                             0       498       0        0         0 |      0       498       0        0  same
coa5-ch4-supplementary.l4                      0         0       0        0         0 |      0         0       0        0  same
coa5-derivative-claims.l4                      0         0       0        0         0 |      0         0       0        0  same
coa5-director-definitions.l4                   0         0       0        0         0 |      0         0       0        0  same
coa5-director-liabilities.l4                   0         0       0        0         0 |      0         0       0        0  same
coa5-director-supplementary.l4                 0         0       0        0         0 |      0         0       0        0  same
coa5-loans-exceptions.l4                       0         0       0        0         0 |      0         0       0        0  same
coa5-loss-of-office.l4                         0         0       0        0         0 |      0         0       0        0  same
coa5-quoted-company-pay.l4                     0         0       0        0         0 |      0         0       0        0  same
coa5-residential-addresses.l4                  0         0       0        0         0 |      0         0       0        0  same
coa5-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa5-service-contracts.l4                      0         0       0        0         0 |      0         0       0        0  same
coa5-tests-ch4-supplementary.l4                0        26       0        0         0 |      0        26       0        0  same
coa5-tests-derivative-claims.l4                0       228       0        0         0 |      0       228       0        0  same
coa5-tests-director-definitions.l4             0       110       0        0         0 |      0       110       0        0  same
coa5-tests-director-liabilities.l4             0       169       0        0         0 |      0       169       0        0  same
coa5-tests-director-supplementary.l4           0        54       0        0         0 |      0        54       0        0  same
coa5-tests-loans-exceptions.l4                 0       182       0        0         0 |      0       182       0        0  same
coa5-tests-loss-of-office.l4                   0       189       0        0         0 |      0       189       0        0  same
coa5-tests-quoted-company-pay.l4               0       120       0        0         0 |      0       120       0        0  same
coa5-tests-residential-addresses.l4            0        97       0        0         0 |      0        97       0        0  same
coa5-tests-service-contracts.l4                0        91       0        0         0 |      0        91       0        0  same
TOTAL (24 modules)                             0      1764       0        0           |      0      1764       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

The baseline it replaced (the two supplied modules only, before any `coa5-` file existed):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (2 modules)                              0         0       0        0           |      0         0       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Every `coa5-` module has 0 errors; the layer-1 modules have no assertions of their own (their tests are in the `coa5-tests-` files); every test file and the seat cases have all assertions satisfied, none failed, none refused, with the same counts on 1.6.109.
No file has a "follows code on its line" or "at the end of the file" warning (warnings count is 0 in every run).

