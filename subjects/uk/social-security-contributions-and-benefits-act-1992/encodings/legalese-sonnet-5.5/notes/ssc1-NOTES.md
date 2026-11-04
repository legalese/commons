# NOTES -- ssc1: the Social Security Contributions and Benefits Act 1992 (United Kingdom), 1992 c. 4, Part I (Contributions), ss 1-19B, lines 2-710 of `ukpga-1992-4.txt`

Part agent `ssc1`, run `iaw-ssc1`, encoded in L4 on the stable build (1.6.98, main 7689b0d, 2026-10-19) and checked against a second build (main 1.6.108, 2ae7c9b, 2026-11-02).
Written 2026-11-04.

**The source is a plain-text rendering made by a converter script, not the official text.**
Nothing here is "verified against the official text".
Where the rendering shows an omission (a line of dots, a line reading `...`, or a gap such as the blank in `Classes 1, 1A, 1B, , 3 and 3A`), the encoding follows what the rendering shows and says so.

Where `inputs/PLAN.md` and `BRIEF.md` differ, the brief governs.
The one difference I found changed nothing I wrote: the brief says to name each seam "as PLAN.md section 8 names it" (BRIEF.md, the paragraph on NOTES.md), and the plan's seam register is its section 5 (section 1.3 says how a part takes another part's answer). I used section 5.
PLAN section 1.5 adds three things I followed: a `...` line gets its own row (the file lines are 22 and 641), a line of dots is text shown repealed or blank, and `Date` rolls an impossible date forward, so no date is built by adding years to a 29 February (`s 13A(4)` answers NOTHING for a 29 February start, fork F4).

## Method and files

- Layer 1 is six modules that follow the Act's own structure, each rule with its quotation (`-- src:N | ...`) and an `@ref` locator: `ssc1-prelim.l4` (ss 1-4C), `ssc1-class1.l4` (ss 5-9B), `ssc1-class1a1b.l4` (ss 10-10A), `ssc1-class23.l4` (ss 11-14C), `ssc1-class4.l4` (ss 15-18A), `ssc1-general.l4` (ss 19A and 19B; s 19 is machinery).
- Their tests are `ssc1-tests-prelim.l4`, `-class1`, `-class1a1b`, `-class23`, `-class4`, `-general` (642 assertions); expected values were written by hand from the text, not copied from the program's output, and every rule is named in at least one assertion (`coverage.py` prints the count of rules without one: 0).
- Layer 2 is `ssc1-seat.l4` (31 questions) and `ssc1-cases-seat.l4` (138 assertions).
- The `.l4` files were generated from `work/src/*.l4.in` by `work/build.py`, which copies the quoted lines out of the raw text; `work/coverage.py`, `work/coverage-data.py`, `work/marginal.py` and `work/notes.py` generate the tables below. `work/` is scratch and is not shipped.
- The shared core `ssc-core.l4` was used read-only and is unchanged. No `NEEDS-CORE.md` was needed: ssc1 declares the types it needs beyond the core in its own modules, under `s N ...` labels.
- A figure that regulations or orders supply (the s 5 earnings limits, the qualifying earnings factor, the maximum number of Class 3A units, prescribed equivalents, prescribed conditions) is an input. A figure the Act itself states (8% and 2% in s 8(2); 15% in s 9(2); GBP 7,105 in s 11(4)(b); GBP 3.65 in s 11(6); GBP 18.40 in s 13(1); GBP 12,570, GBP 50,270, 6% and 2% in s 15(3)) is a constant named "... as the Act states it", and the amount functions take it as an input too, because the Act says it can be altered.

## Seat

**Seat (Guide section 2): a person who works, is self-employed, or claims a contributory or non-contributory benefit, statutory pay or Child Benefit in Great Britain, asking, on facts they can state, whether and how much they must pay in contributions.**
Part I (ss 1-19B) answers the contribution half of that: who is an earner, what counts as earnings, which contributions are payable by or for the person, how much, and when a person may pay voluntarily.
The benefit and statutory-pay halves are in other parts (ssc2 onwards).
The seat layer takes plain inputs (yes or no, a number, a date, or one of the modules' own choices), builds the modules' records in each question's `WHERE`, and calls the same module rule; it restates no rule.
A record field that no rule reads has a fixed placeholder with a comment saying so (the `Employment` and `Person` placeholders).
The groups that arise only in a situation the person may not be in say so in their heading comment, so the form can ask first.

Departures from the defaults, and what is not in this seat:

- No seat is written for Class 1B (payable by a person accountable to the Inland Revenue under a PAYE settlement agreement, s 10A(1)) or for anything addressed to the Crown or the Treasury; they are in layer 1 for what they decide. The questions about what an employer pays (`Under section 6(1)(b)`, `9(1)`, `10(1)`, `10(4)`, `10ZA(3)`) are in the seat because a worker asks them, and are phrased from the worker's side.
- The Act's own figures are taken as the Act states them (the constants listed under "Method and files"), so a later order or regulation substituting one would change the answers. The figures that are set for a tax year by regulations are asked of the person.
- "Over 16" and "under 25" are plain yes or no answers (`s 173(a)`, the keel's section), not worked out from a date of birth.
- Judgments the Act leaves to someone else are plain facts: whether regulations prescribe otherwise, whether a prescribed exception applies, whether the person is "gainfully employed", what an "apprentice" is (s 9B(9) leaves it to the Treasury).
- Where a module takes a list (the weekly rates in the period, s 12(3); the other amounts in the period, s 13(6)), the seat asks for the one number that matters, the highest, and passes a one-item list (`Under section 12(2)` and `Under section 13(4)`).
- Questions are asked in the sense of the rule they call: JUST FALSE is the text's no, and NOTHING means the text, or the facts given, do not decide it. For s 14(1) the question is "am I entitled to pay", so JUST FALSE means barred.

The seat's questions, in the order they stand in the file, which follows the order of the text by group:

| # | seat question (the DECIDE name; the `@export` text adds a question mark) | group | calls |
|---|---|---|---|
| 1 | Under section 2(1)(a), am I an employed earner | Who is an earner (ss 1 to 3) | `s 2(1)(a) the person is an employed earner` |
| 2 | Under section 2(1)(b), am I a self-employed earner | Who is an earner (ss 1 to 3) | `s 2(1)(b) the person is a self-employed earner` |
| 3 | Under section 2(5), am I treated as a self-employed earner for a week | Who is an earner (ss 1 to 3) | `s 2(5) the person is treated as a self-employed earner as respects the week` |
| 4 | Under section 3(1)(a), is what I receive earnings | Who is an earner (ss 1 to 3) | `s 3(1)(a) the payment is earnings` |
| 5 | Under section 1(6)(a), am I liable to pay a contribution of this class | Who is an earner (ss 1 to 3) | `s 1(6)(a) the person is liable to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` |
| 6 | Under section 1(6)(b), am I entitled to pay Class 3 contributions | Who is an earner (ss 1 to 3) | `s 1(6)(b) the person is entitled to pay Class 3 contributions` |
| 7 | Under section 4(1)(a), is a statutory payment I receive treated as pay from employed earner's employment | Payments treated as earnings (ss 4 to 4C) | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` |
| 8 | Under section 4A(7), am I treated as performing the services | Payments treated as earnings (ss 4 to 4C) | `s 4A(7) the worker is treated as performing the services` |
| 9 | Under section 6(1)(a), must I pay a primary Class 1 contribution on these earnings | Class 1 contributions (ss 5 to 9B) | `s 6 a primary Class 1 contribution is payable, having regard to sections 1(6)(a), 6(2) and 6(3)` |
| 10 | Under section 8(1), how much primary Class 1 contribution must I pay on these earnings | Class 1 contributions (ss 5 to 9B) | `s 8(1) the amount of the primary Class 1 contribution` |
| 11 | Under section 6(1)(b), must my employer pay a secondary Class 1 contribution on these earnings | Class 1 contributions (ss 5 to 9B) | `s 6 a secondary Class 1 contribution is payable, having regard to sections 1(6)(a) and 6(2)` |
| 12 | Under section 9(1), how much secondary Class 1 contribution must my employer pay on these earnings | Class 1 contributions (ss 5 to 9B) | `s 9(1) the amount of the secondary Class 1 contribution` |
| 13 | Under section 9B(2), am I a relevant apprentice | Class 1 contributions (ss 5 to 9B) | `s 9B(2) the earner is a relevant apprentice` |
| 14 | Under section 6A(2), am I treated as having paid a primary Class 1 contribution for this week | Class 1 contributions (ss 5 to 9B) | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` |
| 15 | Under section 10(1), is a Class 1A contribution payable on the benefits I get from my job | Class 1A contributions on benefits in kind (ss 10 to 10ZB) | `s 10(1) a Class 1A contribution is payable for the tax year` |
| 16 | Under section 10(4), how much Class 1A contribution is payable on these benefits | Class 1A contributions on benefits in kind (ss 10 to 10ZB) | `s 10(4) the amount of the Class 1A contribution payable under subsection (1)` |
| 17 | Under section 10ZA(3), does the person who provides the benefit rather than my employer owe the Class 1A contribution | Class 1A contributions on benefits in kind (ss 10 to 10ZB) | `s 10ZA(3) the liability falls on the person providing the benefit` |
| 18 | Under section 11(5B), am I treated as having paid a Class 2 contribution for this week | Class 2 contributions of the self-employed (ss 11 to 12) | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` |
| 19 | Under section 11(6), may I pay a Class 2 contribution for this week | Class 2 contributions of the self-employed (ss 11 to 12) | `s 11(6) the earner may pay a Class 2 contribution in respect of the week` |
| 20 | Under section 12(2), how much must I pay for a late paid Class 2 contribution | Class 2 contributions of the self-employed (ss 11 to 12) | `s 12(2) the amount of the late paid Class 2 contribution` |
| 21 | Under section 13(1), am I entitled to pay a Class 3 contribution | Class 3 contributions that anyone may pay (ss 13 to 14) | `s 13(1) the person is entitled to pay a Class 3 contribution` |
| 22 | Under section 13(4), how much must I pay for a Class 3 contribution for an earlier tax year | Class 3 contributions that anyone may pay (ss 13 to 14) | `s 13(4) the amount of the Class 3 contribution for the earlier tax year` |
| 23 | Under section 13A(1), may I pay a Class 3 contribution for a missing year | Class 3 contributions that anyone may pay (ss 13 to 14) | `s 13A(1) an eligible person is entitled to pay a Class 3 contribution in respect of the missing year, having regard to subsections (3) and (4)` |
| 24 | Under section 14(1), am I entitled to pay a Class 3 contribution for the tax year | Class 3 contributions that anyone may pay (ss 13 to 14) | `s 14(1) the person is entitled to pay a Class 3 contribution for the tax year` |
| 25 | Under section 14A(1), may I pay a Class 3A contribution on this day | Class 3A contributions for units of additional pension (ss 14A to 14B) | `s 14A(1) the person is entitled to pay a Class 3A contribution on the day` |
| 26 | Under section 14A(5), may I pay a Class 3A contribution on this occasion | Class 3A contributions for units of additional pension (ss 14A to 14B) | `s 14A(5) the person may pay a Class 3A contribution on this occasion` |
| 27 | Under section 14B(3), am I treated as never having had the unit of additional pension | Class 3A contributions for units of additional pension (ss 14A to 14B) | `s 14B(3) the person is treated as never having had the unit of additional pension` |
| 28 | Under section 15(1), are Class 4 contributions payable on my profits for the tax year | Class 4 contributions on profits (ss 15 to 18A) | `s 15(1) Class 4 contributions are payable for the tax year in respect of the profits` |
| 29 | Under section 15(3), how much Class 4 contribution must I pay on my profits for the tax year | Class 4 contributions on profits (ss 15 to 18A) | `s 15(3) the amount of the Class 4 contribution for the tax year` |
| 30 | Under section 15(3A), am I as a member of a limited liability partnership liable to Class 4 contributions | Class 4 contributions on profits (ss 15 to 18A) | `s 15(3A) Class 4 contributions are payable by the member of the limited liability partnership` |
| 31 | Under section 19A(2), am I treated as having been in employed earner's employment despite the error | Contributions paid in error (s 19A) | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` |

## Coverage (ssc1)

One row per heading, section, subsection, paragraph, sub-paragraph, defined term and editorial omission of lines 2-710, 664 rows.
`work/coverage.py` enumerates the units from the raw text and asserts that each of the 709 non-blank lines lies in exactly one row. A row is `encoded` when the `@ref` locators of the layer-1 modules together cover every line of the row (the rule named is the narrowest `@ref` that covers its first line); `fork` for the five rows of the fork register; `inert` for a row with an explicit reason (reason 1 for every heading, reason 2 for machinery, taken from a table of subsections in `work/coverage-data.py` and inherited by uncovered descendants); and `repealed or blank in this text` where the text shows only dots or a `...` omission.
It warns if an `inert` row is covered by an `@ref` or a `fork` row has no covering rule (neither warning fired in the final run), and the last column counts the assertion lines, in the layer-1 tests and the seat cases, that mention the rule (or, for a type, one of its constructors).
The brief lists `repealed or blank in this text` as a disposition of its own, besides the inert reason 3 ("text shown repealed or blank"); I used the disposition and no row carries inert reason 3.

**Audit counts.**
Text units counted independently of the parser, by `sed -n 2,710p ukpga-1992-4.txt | awk NF | awk` with one pattern for a line that opens with a numbered or lettered label in brackets, one for a line reading `...`, one for a line that opens with an opening curly quote (a defined term), and a catch-all: 596 labelled lines, 2 `...` lines, 16 defined-term lines and 95 other lines. Of the 95, 49 are headings (10 part-level headings and 39 section headings, as `coverage.py` classes them), 1 is the unnumbered paragraph under s 19B, and 45 are continuation lines that belong to the unit above them. 596 + 2 + 16 + 49 + 1 = 664 units, and 664 + 45 = 709 non-blank lines.
`coverage.py` counts the same 664 rows by kind as 10 part heading, 39 section heading, 276 subsection, 277 paragraph, 43 sub-paragraph, 2 omission, 16 definition, 1 section text.
Rows before the audit: 662 (the first full run of `coverage.py`, which had attached the two `...` lines to the unit above them, against PLAN section 1.5). Rows after: 664, with a row of their own for the `...` lines at file lines 22 and 641. The audit also corrected a locator that passed `srcrefs.py` but named the wrong lines (`s 8(2)(b)` cited line 301 and now cites 303-304), added to a rule's locator the provisions it already implemented (for example `s 4B(11)`, `s 9A(9)`, `s 9B(6)`, `s 9B(7)`), and gave `s 13A(9)(a)(i)` and `s 13A(13)(a)(i)` rules of their own.

**Counts per disposition.**

| disposition | rows |
|---|---|
| encoded | 379 |
| fork | 5 |
| inert | 257 |
| repealed or blank in this text | 23 |
| total | 664 |

Of the 257 inert rows, 49 are reason 1 (headings) and 208 are reason 2 (machinery: regulation-making and order-making powers, who makes them, and savings that point at them); none is reason 3.
Where a rule depends on what a power's regulations provide, the outcome is an input to the rule (for example `s 9A(7)` and `s 9B(4)` upper secondary thresholds, `s 11(9)(b)` bars, `s 7(2)` who the secondary contributor is).

Provisions this part leaves without a rule although they look operative, and why:
- `s 9A(3)`: the table is not in the text (see finding 1); the age-related percentage is an input.
- `s 13A(9)(a)(ii)`, `(9)(b)`, `(13)(a)(ii)`, `(13)(b)`: they say the earnings factor is derived from Class 2 or Class 3 contributions or from earlier-year contributions; the conversion into an earnings factor is Schedule 3 (ssc8), so the factor is an input (`NOTE` in the table).
- `s 19(4)`: a duty on the Treasury to make regulations enabling an election by a woman married or widowed on 6 April 1977; the election itself is created by the regulations, which are outside the sources.

Rows (one per unit; the provision label is the Act's own numbering):

| provision | lines | disposition | L4 rule, or reason | assertions (file:count) |
|---|---|---|---|---|
| Heading: Part I — Contributions | 2 | inert | reason 1 (not operative): heading | - |
| Heading: Preliminary | 3 | inert | reason 1 (not operative): heading | - |
| s 1 | 4 | inert | reason 1 (not operative): heading | - |
| s 1(1) | 5 | encoded | `s 1(1) the funds are to be provided by means of contributions payable to the Inland Revenue` | tests-prelim:3 |
| s 1(1)(a) | 6 | encoded | `s 1(1) the funds are to be provided by means of contributions payable to the Inland Revenue` | tests-prelim:3 |
| s 1(1)(b) | 7-8 | encoded | `s 1(1) the funds are to be provided by means of contributions payable to the Inland Revenue` | tests-prelim:3 |
| s 1(2) | 9 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(a) | 10 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(a)(i) | 11 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(a)(ii) | 12 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(b) | 13 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(bb) | 14 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(c) | 15 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(d) | 16 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(da) | 17 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(2)(e) | 18 | encoded | `s 1(2) the description of the class` | tests-prelim:10 |
| s 1(3) | 19 | inert | reason 2 (machinery): amounts and rates are subject to regulations and Treasury orders (power to alter figures) | - |
| s 1(3)(a) | 20 | inert | reason 2 (machinery): amounts and rates are subject to regulations and Treasury orders (power to alter figures) | - |
| s 1(3)(b) | 21 | inert | reason 2 (machinery): amounts and rates are subject to regulations and Treasury orders (power to alter figures) | - |
| s 1(3)(b) (omission at line 22) | 22 | repealed or blank in this text | the text shows "...", an editorial omission, at line 22 | - |
| s 1(4) | 23 | encoded | `s 1(4) Schedule 1 has effect with respect to the computation, collection and recovery of the class` | tests-prelim:8 |
| s 1(4)(a) | 24 | encoded | `s 1(4) Schedule 1 has effect with respect to the computation, collection and recovery of the class` | tests-prelim:8 |
| s 1(4)(b) | 25 | encoded | `s 1(4) Schedule 1 has effect with respect to the computation, collection and recovery of the class` | tests-prelim:8 |
| s 1(5) | 26 | encoded | `s 1(5) the total of the amounts to be paid out of money provided by Parliament for the year` | tests-prelim:1 |
| s 1(6) | 27 | encoded | `s 1(6)(a) the person is liable to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` | tests-prelim:8 |
| s 1(6)(a) | 28 | encoded | `s 1(6)(a) the person is liable to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` | tests-prelim:8 |
| s 1(6)(aa) | 29 | encoded | `s 1(6)(aa) the person is treated under section 11(5B) as having actually paid Class 2 contributions` | tests-prelim:2 |
| s 1(6)(b) | 30 | encoded | `s 1(6)(b) the person is entitled to pay Class 3 contributions` | tests-prelim:2 |
| s 1(6)(c) | 31 | encoded | `s 1(6)(c) the person is entitled to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` | tests-prelim:5 |
| s 1(7) | 32 | inert | reason 2 (machinery): regulations under s 1(6) are made by the Treasury | - |
| s 2 | 33 | inert | reason 1 (not operative): heading | - |
| s 2(1) | 34 | encoded | `s 2(1)(a) the person is an employed earner` | tests-prelim:6 |
| s 2(1)(a) | 35 | fork | F1 (an office "with ... earnings") -- encoded by `s 2(1)(a) the person is an employed earner` | tests-prelim:6 |
| s 2(1)(b) | 36 | encoded | `s 2(1)(b) the person is a self-employed earner` | tests-prelim:4 |
| s 2(2) | 37 | inert | reason 2 (machinery): regulation-making power (employments disregarded; persons treated as in a category of earner) | - |
| s 2(2)(a) | 38 | inert | reason 2 (machinery): regulation-making power (employments disregarded; persons treated as in a category of earner) | - |
| s 2(2)(b) | 39 | inert | reason 2 (machinery): regulation-making power (employments disregarded; persons treated as in a category of earner) | - |
| s 2(2ZA) | 40 | inert | reason 2 (machinery): regulation-making power (arrangements to avoid a category of earner) | - |
| s 2(2ZA)(a) | 41 | inert | reason 2 (machinery): regulation-making power (arrangements to avoid a category of earner) | - |
| s 2(2ZA)(b) | 42 | inert | reason 2 (machinery): regulation-making power (arrangements to avoid a category of earner) | - |
| s 2(2ZB) | 43 | encoded | `s 2(2ZB) the thing is an arrangement` | tests-prelim:5 |
| s 2(2A) | 44 | inert | reason 2 (machinery): who makes regulations under s 2(2) | - |
| s 2(3) | 45 | encoded | `s 2(3) the person is treated as an employed earner for all purposes of this Act` | tests-prelim:2 |
| s 2(4) | 46 | encoded | `s 2(4) the employment is employed earner's employment for the purposes of industrial injuries benefit` | tests-prelim:6 |
| s 2(5) | 47 | encoded | `s 2(5) the person is treated as a self-employed earner as respects the week` | tests-prelim:2 |
| s 3 | 48 | inert | reason 1 (not operative): heading | - |
| s 3(1) | 49 | encoded | `s 3(1)(a) the payment is earnings`; `s 3(1)(b) the person is an earner` | tests-prelim:4 |
| s 3(1)(a) | 50 | encoded | `s 3(1)(a) the payment is earnings` | tests-prelim:2 |
| s 3(1)(b) | 51 | encoded | `s 3(1)(b) the person is an earner` | tests-prelim:2 |
| s 3(2) | 52 | inert | reason 2 (machinery): earnings are calculated as regulations prescribe | - |
| s 3(2)(a) | 53 | inert | reason 2 (machinery): earnings are calculated as regulations prescribe | - |
| s 3(2)(b) | 54-55 | inert | reason 2 (machinery): earnings are calculated as regulations prescribe | - |
| s 3(2A) | 56 | inert | reason 2 (machinery): regulation-making power (payments to two or more earners) | - |
| s 3(3) | 57 | inert | reason 2 (machinery): regulation-making power (payments disregarded or deemed) | - |
| s 3(4) | 58 | inert | reason 2 (machinery): scope of the regulation-making power in s 3(5) (directors) | - |
| s 3(5) | 59 | inert | reason 2 (machinery): regulation-making power (directors of companies) | - |
| s 3(5)(a) | 60 | inert | reason 2 (machinery): regulation-making power (directors of companies) | - |
| s 3(5)(b) | 61 | inert | reason 2 (machinery): regulation-making power (directors of companies) | - |
| s 4 | 62 | inert | reason 1 (not operative): heading | - |
| s 4(1) | 63 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a) | 64 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a)(i) | 65 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a)(ii) | 66 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a)(iii) | 67 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a)(iv) | 68 | repealed or blank in this text | the text shows only dots at line 68 | - |
| s 4(1)(a)(v) | 69 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a)(vi) | 70 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a)(vii) | 71 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(a)(viii) | 72 | encoded | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | tests-prelim:8 |
| s 4(1)(b) | 73 | encoded | `s 4(1)(b) the sickness payment is treated as remuneration derived from employed earner's employment` | tests-prelim:3 |
| s 4(1)(b)(i) | 74 | encoded | `s 4(1)(b) the sickness payment is treated as remuneration derived from employed earner's employment` | tests-prelim:3 |
| s 4(1)(b)(ii) | 75 | encoded | `s 4(1)(b) the sickness payment is treated as remuneration derived from employed earner's employment` | tests-prelim:3 |
| s 4(2) | 76 | inert | reason 2 (machinery): regulation-making power (disregarding the prescribed part of a sickness payment) | - |
| s 4(3) | 77 | encoded | `s 4(3) the payment is a sickness payment` | tests-prelim:2 |
| s 4(4) | 78 | encoded | `s 4(4)(a) the amount treated as remuneration derived from employed earner's employment`; `s 4(4)(b) the sum is treated as remuneration derived from an employed earner's employment` | tests-prelim:7 |
| s 4(4)(a) | 79 | fork | F2 (deductions greater than the gain) -- encoded by `s 4(4)(a) the amount treated as remuneration derived from employed earner's employment` | tests-prelim:4 |
| s 4(4)(b) | 80 | encoded | `s 4(4)(b) the sum is treated as remuneration derived from an employed earner's employment` | tests-prelim:3 |
| s 4(5) | 81 | inert | reason 2 (machinery): regulation-making power (payments to directors treated as remuneration) | - |
| s 4(6) | 82 | inert | reason 2 (machinery): regulation-making power (amounts chargeable to income tax treated as remuneration) | - |
| s 4(6)(a) | 83 | inert | reason 2 (machinery): regulation-making power (amounts chargeable to income tax treated as remuneration) | - |
| s 4(6)(b) | 84 | inert | reason 2 (machinery): regulation-making power (amounts chargeable to income tax treated as remuneration) | - |
| s 4(6A) | 85 | inert | reason 2 (machinery): regulation-making power (optional remuneration arrangements) | - |
| s 4(6A)(a) | 86 | inert | reason 2 (machinery): regulation-making power (optional remuneration arrangements) | - |
| s 4(6A)(b) | 87-88 | inert | reason 2 (machinery): regulation-making power (optional remuneration arrangements) | - |
| s 4(6B) | 89 | inert | reason 2 (machinery): content of regulations under s 4(6A) (the contributions limit) | - |
| s 4(6C) | 90 | encoded | `s 4(6C)(b) the regulations may prescribe the amount as an equivalent of the contributions limit` | tests-prelim:5 |
| s 4(6C)(a) | 91 | encoded | `s 4(6C)(b) the regulations may prescribe the amount as an equivalent of the contributions limit` | tests-prelim:5 |
| s 4(6C)(b) | 92 | encoded | `s 4(6C)(b) the regulations may prescribe the amount as an equivalent of the contributions limit` | tests-prelim:5 |
| s 4(6D) | 93 | inert | reason 2 (machinery): content of regulations under s 4(6A) | - |
| s 4(6D)(a) | 94 | inert | reason 2 (machinery): content of regulations under s 4(6A) | - |
| s 4(6D)(b) | 95 | inert | reason 2 (machinery): content of regulations under s 4(6A) | - |
| s 4(6D)(c) | 96 | inert | reason 2 (machinery): content of regulations under s 4(6A) | - |
| s 4(6E) | 97 | encoded | `s 4(6E) the meaning of the expression in subsection (6A)` | tests-prelim:2 |
| s 4(7) | 98 | inert | reason 2 (machinery): who makes regulations under s 4 | - |
| s 4A | 99 | inert | reason 1 (not operative): heading | - |
| s 4A(1) | 100 | encoded | `s 4A(1) the regulations may treat relevant payments or benefits as earnings paid to the worker in respect of an employed earner's employment` | tests-prelim:4 |
| s 4A(1)(a) | 101 | encoded | `s 4A(1) the regulations may treat relevant payments or benefits as earnings paid to the worker in respect of an employed earner's employment` | tests-prelim:4 |
| s 4A(1)(b) | 102 | encoded | `s 4A(1) the regulations may treat relevant payments or benefits as earnings paid to the worker in respect of an employed earner's employment` | tests-prelim:4 |
| s 4A(1)(c) | 103-104 | encoded | `s 4A(1) the regulations may treat relevant payments or benefits as earnings paid to the worker in respect of an employed earner's employment` | tests-prelim:4 |
| s 4A(2) | 105 | encoded | `s 4A(2)(a) who the intermediary is` | tests-prelim:4 |
| s 4A(2)(a) | 106 | encoded | `s 4A(2)(a) who the intermediary is` | tests-prelim:4 |
| s 4A(2)(a)(i) | 107 | encoded | `s 4A(2)(a) who the intermediary is` | tests-prelim:4 |
| s 4A(2)(a)(ii) | 108 | encoded | `s 4A(2)(a) who the intermediary is` | tests-prelim:4 |
| s 4A(2)(b) | 109 | encoded | `s 4A(2)(b) the person may be the intermediary despite being a person of the kind` | tests-prelim:3 |
| s 4A(2)(b)(i) | 110 | encoded | `s 4A(2)(b) the person may be the intermediary despite being a person of the kind` | tests-prelim:3 |
| s 4A(2)(b)(ii) | 111-112 | encoded | `s 4A(2)(b) the person may be the intermediary despite being a person of the kind` | tests-prelim:3 |
| s 4A(3) | 113 | encoded | `s 4A(3)(a) the worker's attributable earnings` | tests-prelim:1 |
| s 4A(3)(a) | 114 | encoded | `s 4A(3)(a) the worker's attributable earnings` | tests-prelim:1 |
| s 4A(3)(b) | 115 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(c) | 116 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(c)(i) | 117 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(c)(ii) | 118-119 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(d) | 120 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(e) | 121 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(f) | 122 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(g) | 123 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(h) | 124 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(i) | 125 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(i)(i) | 126 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(i)(ii) | 127-128 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(j) | 129 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(3)(k) | 130 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(4) | 131 | inert | reason 2 (machinery): content of regulations under s 4A(3)(c) | - |
| s 4A(4)(a) | 132 | inert | reason 2 (machinery): content of regulations under s 4A(3)(c) | - |
| s 4A(4)(b) | 133 | inert | reason 2 (machinery): content of regulations under s 4A(3)(c) | - |
| s 4A(4)(b)(i) | 134 | inert | reason 2 (machinery): content of regulations under s 4A(3)(c) | - |
| s 4A(4)(b)(ii) | 135 | inert | reason 2 (machinery): content of regulations under s 4A(3)(c) | - |
| s 4A(5) | 136 | inert | reason 2 (machinery): content of regulations under s 4A | - |
| s 4A(6) | 137 | encoded | `s 4A(6) the Part is among the applicable provisions of this Act` | tests-prelim:4 |
| s 4A(6) “the applicable provisions of this Act” | 138 | encoded | `s 4A(6) the Part is among the applicable provisions of this Act` | tests-prelim:4 |
| s 4A(6) “business” | 139-141 | encoded | `s 4A(6) the activity carried on by the body is a business` | tests-prelim:3 |
| s 4A(6) “relevant payments or benefits” | 142 | encoded | `s 4A(6) the payments or benefits are relevant payments or benefits` | tests-prelim:3 |
| s 4A(6) “specified” | 143 | encoded | `s 4A(6) the description is specified` | tests-prelim:2 |
| s 4A(7) | 144 | encoded | `s 4A(7) the worker is treated as performing the services` | tests-prelim:3 |
| s 4A(8) | 145 | inert | reason 2 (machinery): who makes regulations under s 4A | - |
| s 4A(9) | 146 | inert | reason 2 (machinery): regulation-making power (assimilation to income tax law) | - |
| s 4AA | 147 | inert | reason 1 (not operative): heading | - |
| s 4AA(1) | 148 | inert | reason 2 (machinery): regulation-making power (limited liability partnerships) | - |
| s 4AA(1)(a) | 149 | inert | reason 2 (machinery): regulation-making power (limited liability partnerships) | - |
| s 4AA(1)(a)(i) | 150 | inert | reason 2 (machinery): regulation-making power (limited liability partnerships) | - |
| s 4AA(1)(a)(ii) | 151 | inert | reason 2 (machinery): regulation-making power (limited liability partnerships) | - |
| s 4AA(1)(b) | 152 | inert | reason 2 (machinery): regulation-making power (limited liability partnerships) | - |
| s 4AA(1)(c) | 153 | inert | reason 2 (machinery): regulation-making power (limited liability partnerships) | - |
| s 4AA(2) | 154 | inert | reason 2 (machinery): regulation-making power (modifying definitions) | - |
| s 4AA(3) | 155 | inert | reason 2 (machinery): regulation-making power (assimilation to income tax law) | - |
| s 4AA(3)(a) | 156 | inert | reason 2 (machinery): regulation-making power (assimilation to income tax law) | - |
| s 4AA(3)(b) | 157-158 | inert | reason 2 (machinery): regulation-making power (assimilation to income tax law) | - |
| s 4AA(4) | 159 | inert | reason 2 (machinery): extent of the power in s 4AA(3) | - |
| s 4AA(5) | 160 | inert | reason 2 (machinery): concurrence for regulations under s 4AA | - |
| s 4AA(6) | 161 | inert | reason 2 (machinery): saving: Limited Liability Partnerships Act 2000 s 4(4) does not limit the regulations | - |
| s 4B | 162 | inert | reason 1 (not operative): heading | - |
| s 4B(1) | 163 | inert | reason 2 (machinery): conditions on the power to make retrospective regulations | - |
| s 4B(1)(a) | 164 | inert | reason 2 (machinery): conditions on the power to make retrospective regulations | - |
| s 4B(1)(b) | 165 | inert | reason 2 (machinery): conditions on the power to make retrospective regulations | - |
| s 4B(2) | 166 | inert | reason 2 (machinery): regulation-making power (retrospective effect) | - |
| s 4B(3) | 167 | encoded | `s 4B(3) the power is a relevant power` | tests-prelim:5 |
| s 4B(3)(a) | 168 | encoded | `s 4B(3) the power is a relevant power` | tests-prelim:5 |
| s 4B(3)(b) | 169 | encoded | `s 4B(3) the power is a relevant power` | tests-prelim:5 |
| s 4B(3)(c) | 170 | encoded | `s 4B(3) the power is a relevant power` | tests-prelim:5 |
| s 4B(3)(d) | 171 | encoded | `s 4B(3) the power is a relevant power` | tests-prelim:5 |
| s 4B(4) | 172 | encoded | `s 4B(4) the retrospective tax provision counts` | tests-prelim:2 |
| s 4B(5) | 173 | encoded | `s 4B(5) subsection (2) authorises regulations that have effect in relation to the time` | tests-prelim:3 |
| s 4B(6) | 174 | inert | reason 2 (machinery): content of regulations under s 4B(2) | - |
| s 4B(7) | 175 | encoded | `s 4B(7) the revised earnings` | tests-prelim:1 |
| s 4B(7) “relevant contributions legislation” | 176 | encoded | `s 4B(7) the revised earnings` | tests-prelim:1 |
| s 4B(7) “the relevant time” | 177 | encoded | `s 4B(7) the revised earnings` | tests-prelim:1 |
| s 4B(7) “the revised earnings” | 178 | encoded | `s 4B(7) the revised earnings` | tests-prelim:1 |
| s 4B(8) | 179 | encoded | `s 4B(8) how the reference in the relevant contributions legislation is read` | tests-prelim:5 |
| s 4B(8)(a) | 180 | encoded | `s 4B(8) how the reference in the relevant contributions legislation is read` | tests-prelim:5 |
| s 4B(8)(b) | 181-182 | encoded | `s 4B(8) how the reference in the relevant contributions legislation is read` | tests-prelim:5 |
| s 4B(9) | 183 | encoded | `s 4B(9) the matter is to be redetermined by reference to the revised earnings` | tests-prelim:4 |
| s 4B(9)(a) | 184 | encoded | `s 4B(9) the matter is to be redetermined by reference to the revised earnings` | tests-prelim:4 |
| s 4B(9)(b) | 185-186 | encoded | `s 4B(9) the matter is to be redetermined by reference to the revised earnings` | tests-prelim:4 |
| s 4B(10) | 187 | encoded | `s 4B(10) the matter is among the matters referred to in subsection (9)` | tests-prelim:3 |
| s 4B(10)(a) | 188 | encoded | `s 4B(10) the matter is among the matters referred to in subsection (9)` | tests-prelim:3 |
| s 4B(10)(b) | 189 | encoded | `s 4B(10) the matter is among the matters referred to in subsection (9)` | tests-prelim:3 |
| s 4B(11) | 190 | encoded | `s 4B(8) how the reference in the relevant contributions legislation is read` | tests-prelim:5 |
| s 4B(12) | 191 | inert | reason 2 (machinery): saving: the power in s 4B(2) is without prejudice to other powers | - |
| s 4B(13) | 192 | encoded | `s 4B(13) the thing is contributions legislation` | tests-prelim:2 |
| s 4C | 193 | inert | reason 1 (not operative): heading | - |
| s 4C(1) | 194 | inert | reason 2 (machinery): regulation-making power (consequential provision) | - |
| s 4C(2) | 195 | inert | reason 2 (machinery): purposes of the power in s 4C(1) | - |
| s 4C(2)(a) | 196 | inert | reason 2 (machinery): purposes of the power in s 4C(1) | - |
| s 4C(2)(b) | 197 | inert | reason 2 (machinery): purposes of the power in s 4C(1) | - |
| s 4C(2)(c) | 198 | inert | reason 2 (machinery): purposes of the power in s 4C(1) | - |
| s 4C(2)(d) | 199 | repealed or blank in this text | the text shows only dots at line 199 | - |
| s 4C(2)(e) | 200 | inert | reason 2 (machinery): purposes of the power in s 4C(1) | - |
| s 4C(2)(f) | 201 | inert | reason 2 (machinery): purposes of the power in s 4C(1) | - |
| s 4C(3) | 202 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(3)(a) | 203 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(3)(b) | 204 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(4) | 205 | encoded | `s 4C(4) regulations under subsection (1) may have effect in relation to the time` | tests-prelim:2 |
| s 4C(5) | 206 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(a) | 207 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(b) | 208 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(c) | 209 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(d) | 210 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(e) | 211 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(f) | 212 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(g) | 213 | repealed or blank in this text | the text shows only dots at line 213 | - |
| s 4C(5)(h) | 214 | repealed or blank in this text | the text shows only dots at line 214 | - |
| s 4C(5)(i) | 215 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(5)(j) | 216 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(6) | 217 | inert | reason 2 (machinery): content of regulations under s 4C(1) | - |
| s 4C(7) | 218 | encoded | `s 4C(7) the operative provisions are to be read with the modifications necessary to prevent that effect` | tests-prelim:3 |
| s 4C(7)(a) | 219 | encoded | `s 4C(7) the operative provisions are to be read with the modifications necessary to prevent that effect` | tests-prelim:3 |
| s 4C(7)(b) | 220-221 | encoded | `s 4C(7) the operative provisions are to be read with the modifications necessary to prevent that effect` | tests-prelim:3 |
| s 4C(8) | 222 | encoded | `s 4C(8)(a) the provision is one of the operative provisions`; `s 4C(8)(b) the entitlement is within the person's entitlement` | tests-prelim:6 |
| s 4C(8)(a) | 223 | encoded | `s 4C(8)(a) the provision is one of the operative provisions` | tests-prelim:4 |
| s 4C(8)(b) | 224 | encoded | `s 4C(8)(b) the entitlement is within the person's entitlement` | tests-prelim:2 |
| s 4C(9) | 225 | inert | reason 2 (machinery): saving: the powers are without prejudice to other powers | - |
| s 4C(10) | 226 | inert | reason 2 (machinery): content of regulations under s 4C(1) (modifying instruments) | - |
| s 4C(11) | 227 | encoded | `s 4C(11) the day is the commencement day`; `s 4C(11) the thing is an enactment`; `s 4C(11) the payment is a statutory payment` | tests-prelim:8 |
| s 4C(11) “the commencement day” | 228 | encoded | `s 4C(11) the day is the commencement day`; `s 4C(11) the thing is an enactment`; `s 4C(11) the payment is a statutory payment` | tests-prelim:8 |
| s 4C(11) “enactment” | 229 | encoded | `s 4C(11) the thing is an enactment`; `s 4C(11) the payment is a statutory payment` | tests-prelim:6 |
| s 4C(11) “statutory payment” | 230-232 | encoded | `s 4C(11) the payment is a statutory payment` | tests-prelim:4 |
| Heading: Class 1 contributions | 233 | inert | reason 1 (not operative): heading | - |
| s 5 | 234 | inert | reason 1 (not operative): heading | - |
| s 5(1) | 235 | encoded | `s 5(1) the limits and thresholds for the tax year` | tests-class1:3 |
| s 5(1)(a) | 236 | encoded | `s 5(1)(a) the lower earnings limit in force at the time in pounds`; `s 5(1)(a) the primary threshold in force at the time in pounds`; `s 5(1)(a) the upper earnings limit in force at the time in pounds` | tests-class1:3 |
| s 5(1)(a)(i) | 237 | encoded | `s 5(1)(a) the lower earnings limit in force at the time in pounds`; `s 5(1)(a) the primary threshold in force at the time in pounds`; `s 5(1)(a) the upper earnings limit in force at the time in pounds` | tests-class1:3 |
| s 5(1)(a)(ii) | 238 | encoded | `s 5(1)(a) the lower earnings limit in force at the time in pounds`; `s 5(1)(a) the primary threshold in force at the time in pounds`; `s 5(1)(a) the upper earnings limit in force at the time in pounds` | tests-class1:3 |
| s 5(1)(a)(iii) | 239 | encoded | `s 5(1)(a) the upper earnings limit in force at the time in pounds`; `s 5(1) the limits and thresholds for the tax year` | tests-class1:4 |
| s 5(1)(b) | 240-241 | encoded | `s 5(1)(b) the secondary threshold in force at the time in pounds`; `s 5(1) the limits and thresholds for the tax year` | tests-class1:4 |
| s 5(2) | 242 | repealed or blank in this text | the text shows only dots at line 242 | - |
| s 5(3) | 243 | repealed or blank in this text | the text shows only dots at line 243 | - |
| s 5(4) | 244 | encoded | `s 5(4) the limits and thresholds that apply to the earner` | tests-class1:3 |
| s 5(5) | 245 | encoded | `s 5(5) the regulations may prescribe the amount as an equivalent of the limit or threshold` | tests-class1:4 |
| s 5(6) | 246 | inert | reason 2 (machinery): who makes regulations under s 5 | - |
| s 6 | 247 | inert | reason 1 (not operative): heading | - |
| s 6(1) | 248 | encoded | `s 6(1)(a) a primary Class 1 contribution is payable in accordance with sections 6 and 8`; `s 6(1)(b) a secondary Class 1 contribution is payable in accordance with sections 6 and 9`; `s 6 a secondary Class 1 contribution is payable, having regard to sections 1(6)(a) and 6(2)` | tests-class1:16 |
| s 6(1)(a) | 249 | encoded | `s 6(1)(a) a primary Class 1 contribution is payable in accordance with sections 6 and 8`; `s 6 a primary Class 1 contribution is payable, having regard to sections 1(6)(a), 6(2) and 6(3)` | tests-class1:16 |
| s 6(1)(b) | 250 | encoded | `s 6(1)(b) a secondary Class 1 contribution is payable in accordance with sections 6 and 9`; `s 6 a secondary Class 1 contribution is payable, having regard to sections 1(6)(a) and 6(2)` | tests-class1:7 |
| s 6(2) | 251 | encoded | `s 6(2) a primary or secondary Class 1 contribution is payable in respect of the earnings` | tests-class1:2 |
| s 6(3) | 252 | encoded | `s 6(3) a primary Class 1 contribution is payable in respect of the earnings` | tests-class1:3 |
| s 6(4) | 253 | encoded | `s 6(4) who is liable to pay the Class 1 contribution` | tests-class1:4 |
| s 6(4)(a) | 254 | encoded | `s 6(4) who is liable to pay the Class 1 contribution` | tests-class1:4 |
| s 6(4)(b) | 255-256 | encoded | `s 6(4) who is liable to pay the Class 1 contribution` | tests-class1:4 |
| s 6(5) | 257 | encoded | `s 6(5) the earnings counted for this employment` | tests-class1:2 |
| s 6(6) | 258 | inert | reason 2 (machinery): regulation-making power (reducing contributions) | - |
| s 6(7) | 259 | inert | reason 2 (machinery): who makes regulations under s 6 | - |
| s 6A | 260 | inert | reason 1 (not operative): heading | - |
| s 6A(1) | 261 | encoded | `s 6A(1) section 6A applies to the earnings` | tests-class1:6 |
| s 6A(1)(a) | 262 | encoded | `s 6A(1) section 6A applies to the earnings` | tests-class1:6 |
| s 6A(1)(b) | 263 | encoded | `s 6A(1) section 6A applies to the earnings` | tests-class1:6 |
| s 6A(2) | 264 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(2)(a) | 265 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(2)(b) | 266-267 | fork | F3 (whether the whole earnings of the week count) -- encoded by `s 6 the earnings on which primary Class 1 contributions have been paid or treated as paid in the tax year`; `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:11 |
| s 6A(3) | 268 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(3)(a) | 269 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(3)(b) | 270 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(3)(c) | 271 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(3)(d) | 272 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(3)(e) | 273 | encoded | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | tests-class1:9 |
| s 6A(4) | 274 | inert | reason 2 (machinery): regulation-making power (modifying provisions for s 6A) | - |
| s 6A(4)(a) | 275 | inert | reason 2 (machinery): regulation-making power (modifying provisions for s 6A) | - |
| s 6A(4)(b) | 276-277 | inert | reason 2 (machinery): regulation-making power (modifying provisions for s 6A) | - |
| s 6A(5) | 278 | encoded | `s 6A(5) section 6A applies in relation to the earnings` | tests-class1:3 |
| s 6A(6) | 279 | encoded | `s 6A(6) the earnings counted for this employment` | tests-class1:2 |
| s 6A(7) | 280 | inert | reason 2 (machinery): who makes regulations under s 6A | - |
| s 7 | 281 | inert | reason 1 (not operative): heading | - |
| s 7(1) | 282 | encoded | `s 7(1) who the secondary contributor is` | tests-class1:5 |
| s 7(1)(a) | 283 | encoded | `s 7(1) who the secondary contributor is` | tests-class1:5 |
| s 7(1)(b) | 284 | encoded | `s 7(1) who the secondary contributor is` | tests-class1:5 |
| s 7(1)(b)(i) | 285 | encoded | `s 7(1) who the secondary contributor is` | tests-class1:5 |
| s 7(1)(b)(ii) | 286-287 | encoded | `s 7(1) who the secondary contributor is` | tests-class1:5 |
| s 7(2) | 288 | inert | reason 2 (machinery): regulation-making power (who is the secondary contributor); its outcome is an input to s 7(1) | - |
| s 7(2)(a) | 289 | inert | reason 2 (machinery): regulation-making power (who is the secondary contributor); its outcome is an input to s 7(1) | - |
| s 7(2)(b) | 290-291 | inert | reason 2 (machinery): regulation-making power (who is the secondary contributor); its outcome is an input to s 7(1) | - |
| s 7(2A) | 292 | inert | reason 2 (machinery): regulation-making power (arrangements) | - |
| s 7(2B) | 293 | encoded | `s 7(2B) the thing is an arrangement` | tests-class1:2 |
| s 7(3) | 294 | inert | reason 2 (machinery): who makes regulations under s 7 | - |
| s 8 | 295 | inert | reason 1 (not operative): heading | - |
| s 8(1) | 296 | encoded | `s 8(1) the amount of the primary Class 1 contribution` | tests-class1:8 |
| s 8(1)(a) | 297 | encoded | `s 8(1) the amount of the primary Class 1 contribution` | tests-class1:8 |
| s 8(1)(a)(i) | 298 | encoded | `s 8(1) the amount of the primary Class 1 contribution` | tests-class1:8 |
| s 8(1)(a)(ii) | 299 | encoded | `s 8(1) the amount of the primary Class 1 contribution` | tests-class1:8 |
| s 8(1)(b) | 300 | encoded | `s 8(1) the amount of the primary Class 1 contribution` | tests-class1:8 |
| s 8(2) | 301 | encoded | `s 8(2)(a) the main primary percentage as the Act states it` | tests-class1:1 |
| s 8(2)(a) | 302 | encoded | `s 8(2)(a) the main primary percentage as the Act states it` | tests-class1:1 |
| s 8(2)(b) | 303-304 | encoded | `s 8(2)(b) the additional primary percentage as the Act states it` | tests-class1:1 |
| s 8(3) | 305 | inert | reason 2 (machinery): saving: s 8(1) is subject to regulations under ss 6(6) and 116 to 120 | - |
| s 8(3)(a) | 306 | inert | reason 2 (machinery): saving: s 8(1) is subject to regulations under ss 6(6) and 116 to 120 | - |
| s 8(3)(b) | 307 | inert | reason 2 (machinery): saving: s 8(1) is subject to regulations under ss 6(6) and 116 to 120 | - |
| s 8(3)(c) | 308 | repealed or blank in this text | the text shows only dots at line 308 | - |
| s 9 | 309 | inert | reason 1 (not operative): heading | - |
| s 9(1) | 310 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9(1A) | 311 | encoded | `s 9(1A) the relevant percentage` | tests-class1:5 |
| s 9(1A)(a) | 312 | encoded | `s 9(1A) the relevant percentage` | tests-class1:5 |
| s 9(1A)(aa) | 313 | encoded | `s 9(1A) the relevant percentage` | tests-class1:5 |
| s 9(1A)(b) | 314 | encoded | `s 9(1A) the relevant percentage` | tests-class1:5 |
| s 9(2) | 315 | encoded | `s 9(2) the secondary percentage as the Act states it` | tests-class1:1 |
| s 9(3) | 316 | inert | reason 2 (machinery): saving: s 9(1) is subject to regulations under ss 6(6) and 116 to 120 | - |
| s 9(3)(a) | 317 | inert | reason 2 (machinery): saving: s 9(1) is subject to regulations under ss 6(6) and 116 to 120 | - |
| s 9(3)(b) | 318 | inert | reason 2 (machinery): saving: s 9(1) is subject to regulations under ss 6(6) and 116 to 120 | - |
| s 9(3)(c) | 319 | repealed or blank in this text | the text shows only dots at line 319 | - |
| s 9A | 320 | inert | reason 1 (not operative): heading | - |
| s 9A(1) | 321 | encoded | `s 9A(1) section 9A applies to the earnings` | tests-class1:5 |
| s 9A(1A) | 322 | encoded | `s 9A(1) section 9A applies to the earnings` | tests-class1:5 |
| s 9A(2) | 323 | encoded | `s 9(1A) the relevant percentage` [the percentage the omitted table specifies is an input (`s 9A(2) the age-related secondary percentage`)] | tests-class1:5 |
| s 9A(3) | 324 | repealed or blank in this text | the text says "Here is the table—" (src:324) and shows none; the age groups and their percentages are inputs to s 9(1A) and s 9(1) | - |
| s 9A(4) | 325 | inert | reason 2 (machinery): regulation-making power (amending the table) | - |
| s 9A(4)(a) | 326 | inert | reason 2 (machinery): regulation-making power (amending the table) | - |
| s 9A(4)(b) | 327 | inert | reason 2 (machinery): regulation-making power (amending the table) | - |
| s 9A(5) | 328 | encoded | `s 9A(5) the percentage may be specified for an added age group` | tests-class1:3 |
| s 9A(6) | 329 | encoded | `s 9A(6) the person is regarded as liable to pay a secondary Class 1 contribution` | tests-class1:2 |
| s 9A(7) | 330-331 | inert | reason 2 (machinery): regulation-making power (upper secondary threshold); the threshold is an input to s 9(1) | - |
| s 9A(8) | 332 | encoded | `s 9A(8) the regulations may prescribe the amount as an equivalent of the upper secondary threshold` | tests-class1:2 |
| s 9A(9) | 333 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9A(9)(a) | 334 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9A(9)(b) | 335 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9A(9)(c) | 336-337 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9A(10) | 338 | encoded | `s 9A(10) the earner falls within an age group for the purposes of subsections (7) to (9)` | tests-class1:2 |
| s 9B | 339 | inert | reason 1 (not operative): heading | - |
| s 9B(1) | 340 | encoded | `s 9B(1) section 9B applies to the earnings` | tests-class1:4 |
| s 9B(2) | 341 | encoded | `s 9B(2) the earner is a relevant apprentice` | tests-class1:5 |
| s 9B(2)(a) | 342 | encoded | `s 9B(2) the earner is a relevant apprentice` | tests-class1:5 |
| s 9B(2)(b) | 343 | encoded | `s 9B(2) the earner is a relevant apprentice` | tests-class1:5 |
| s 9B(3) | 344 | encoded | `s 9B(3) the person is regarded as liable to pay a secondary Class 1 contribution` | tests-class1:2 |
| s 9B(4) | 345-346 | inert | reason 2 (machinery): regulation-making power (upper secondary threshold for relevant apprentices); the threshold is an input to s 9(1) | - |
| s 9B(5) | 347 | encoded | `s 9B(5) the regulations may prescribe the amount as an equivalent of the upper secondary threshold for relevant apprentices` | tests-class1:2 |
| s 9B(6) | 348 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9B(6)(a) | 349 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9B(6)(b) | 350 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9B(6)(c) | 351 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9B(7) | 352 | encoded | `s 9(1) the amount of the secondary Class 1 contribution` | tests-class1:10 |
| s 9B(8) | 353 | inert | reason 2 (machinery): regulation-making power (modifying s 9B(7)) | - |
| s 9B(9) | 354 | encoded | `s 9B(2) the earner is a relevant apprentice` [what counts as an apprentice is for the Treasury to prescribe; whether the earner is employed as an apprentice is a plain fact] | tests-class1:5 |
| s 9B(10) | 355 | inert | reason 2 (machinery): regulation-making power (altering the age in s 9B(2)(a)) | - |
| Heading: Class 1A contributions | 356 | inert | reason 1 (not operative): heading | - |
| s 10 | 357 | inert | reason 1 (not operative): heading | - |
| s 10(1) | 358 | encoded | `s 10(1) a Class 1A contribution is payable for the tax year` | tests-class1a1b:5 |
| s 10(1)(a) | 359 | encoded | `s 10(1) a Class 1A contribution is payable for the tax year` | tests-class1a1b:5 |
| s 10(1)(b) | 360 | encoded | `s 10(1) a Class 1A contribution is payable for the tax year` | tests-class1a1b:5 |
| s 10(1)(b)(i) | 361 | encoded | `s 10(1) a Class 1A contribution is payable for the tax year` | tests-class1a1b:5 |
| s 10(1)(b)(ii) | 362 | encoded | `s 10(1) a Class 1A contribution is payable for the tax year` | tests-class1a1b:5 |
| s 10(1)(c) | 363-364 | encoded | `s 10(1) a Class 1A contribution is payable for the tax year` | tests-class1a1b:5 |
| s 10(1A) | 365 | encoded | `s 10(1A) a Class 1A contribution is payable for the tax year in respect of the termination award` | tests-class1a1b:3 |
| s 10(1A)(a) | 366 | encoded | `s 10(1A) a Class 1A contribution is payable for the tax year in respect of the termination award` | tests-class1a1b:3 |
| s 10(1A)(b) | 367 | encoded | `s 10(1A) a Class 1A contribution is payable for the tax year in respect of the termination award` | tests-class1a1b:3 |
| s 10(1B) | 368 | encoded | `s 10(1B) a Class 1A contribution is payable under subsection (1A) in respect of the amount` | tests-class1a1b:2 |
| s 10(1C) | 369 | encoded | `s 10(1C) a Class 1A contribution is payable under subsection (1A)` | tests-class1a1b:2 |
| s 10(2) | 370 | encoded | `s 10(2) who pays the Class 1A contribution payable under subsection (1)` | tests-class1a1b:6 |
| s 10(2)(a) | 371 | encoded | `s 10(2) who pays the Class 1A contribution payable under subsection (1)` | tests-class1a1b:6 |
| s 10(2)(b) | 372 | encoded | `s 10(2) who pays the Class 1A contribution payable under subsection (1)` | tests-class1a1b:6 |
| s 10(3) | 373 | encoded | `s 10(3) the payment is a relevant payment of earnings` | tests-class1a1b:2 |
| s 10(3A) | 374 | encoded | `s 10(3A) who pays the Class 1A contribution payable under subsection (1A)` | tests-class1a1b:2 |
| s 10(4) | 375 | encoded | `s 10(4) the amount of the Class 1A contribution payable under subsection (1)` | tests-class1a1b:3 |
| s 10(4A) | 376 | encoded | `s 10(4A) the amount of the Class 1A contribution payable under subsection (1A)` | tests-class1a1b:2 |
| s 10(5) | 377 | encoded | `s 10(5) the Class 1A percentage` | tests-class1a1b:1 |
| s 10(6) | 378 | encoded | `s 10(6) a Class 1A contribution is payable in respect of the general earnings` | tests-class1a1b:2 |
| s 10(7) | 379-380 | encoded | `s 10(7) the amount of the general earnings received` | tests-class1a1b:4 |
| s 10(7A) | 381 | encoded | `s 10(7) the amount of the general earnings received` | tests-class1a1b:4 |
| s 10(7A)(a) | 382 | encoded | `s 10(7) the amount of the general earnings received` | tests-class1a1b:4 |
| s 10(7A)(b) | 383-384 | encoded | `s 10(7) the amount of the general earnings received` | tests-class1a1b:4 |
| s 10(7B) | 385 | encoded | `s 10(7B) the provision is an excluded provision` | tests-class1a1b:5 |
| s 10(7B)(a) | 386 | encoded | `s 10(7B) the provision is an excluded provision` | tests-class1a1b:5 |
| s 10(7B)(aa) | 387 | encoded | `s 10(7B) the provision is an excluded provision` | tests-class1a1b:5 |
| s 10(7B)(b) | 388 | encoded | `s 10(7B) the provision is an excluded provision` | tests-class1a1b:5 |
| s 10(8) | 389 | inert | reason 2 (machinery): regulation-making power (amending s 10(7) to (7B)) | - |
| s 10(8)(a) | 390 | inert | reason 2 (machinery): regulation-making power (amending s 10(7) to (7B)) | - |
| s 10(8)(b) | 391 | inert | reason 2 (machinery): regulation-making power (amending s 10(7) to (7B)) | - |
| s 10(9) | 392 | inert | reason 2 (machinery): regulation-making power (Class 1A not payable or reduced) | - |
| s 10(9)(a) | 393 | inert | reason 2 (machinery): regulation-making power (Class 1A not payable or reduced) | - |
| s 10(9)(b) | 394 | inert | reason 2 (machinery): regulation-making power (Class 1A not payable or reduced) | - |
| s 10(10) | 395 | repealed or blank in this text | the text shows only dots at line 395 | - |
| s 10(11) | 396 | inert | reason 2 (machinery): regulation-making power (employment treated as existing under s 4AA) | - |
| s 10(12) | 397 | encoded | `s 10(12) the payment or benefit is a termination award` | tests-class1a1b:3 |
| s 10ZA | 398 | inert | reason 1 (not operative): heading | - |
| s 10ZA(1) | 399 | encoded | `s 10ZA(1) section 10ZA applies` | tests-class1a1b:6 |
| s 10ZA(1)(a) | 400 | encoded | `s 10ZA(1) section 10ZA applies` | tests-class1a1b:6 |
| s 10ZA(1)(b) | 401 | encoded | `s 10ZA(1) section 10ZA applies` | tests-class1a1b:6 |
| s 10ZA(1)(c) | 402 | encoded | `s 10ZA(1) section 10ZA applies` | tests-class1a1b:6 |
| s 10ZA(1)(d) | 403 | encoded | `s 10ZA(1) section 10ZA applies` | tests-class1a1b:6 |
| s 10ZA(1A) | 404 | encoded | `s 10ZA(1) section 10ZA applies` | tests-class1a1b:6 |
| s 10ZA(2) | 405 | encoded | `s 10ZA(2) the amount of the payment is treated as general earnings consisting in the provision of a benefit to the earner in that tax year` | tests-class1a1b:6 |
| s 10ZA(2)(a) | 406 | encoded | `s 10ZA(2) the amount of the payment is treated as general earnings consisting in the provision of a benefit to the earner in that tax year` | tests-class1a1b:6 |
| s 10ZA(2)(b) | 407-408 | encoded | `s 10ZA(2) the amount of the payment is treated as general earnings consisting in the provision of a benefit to the earner in that tax year` | tests-class1a1b:6 |
| s 10ZA(3) | 409 | encoded | `s 10ZA(3) the liability falls on the person providing the benefit` | tests-class1a1b:5 |
| s 10ZA(3)(a) | 410 | encoded | `s 10ZA(3) the liability falls on the person providing the benefit` | tests-class1a1b:5 |
| s 10ZA(3)(b) | 411-412 | encoded | `s 10ZA(3) the liability falls on the person providing the benefit` | tests-class1a1b:5 |
| s 10ZA(4) | 413 | encoded | `s 10ZA(4) subsection (3) applies in the case of a Class 1A contribution for the tax year` | tests-class1a1b:6 |
| s 10ZA(5) | 414 | inert | reason 2 (machinery): regulation-making power (when a person is treated as providing a benefit) | - |
| s 10ZA(6) | 415 | encoded | `s 10ZA(6) the person is a member of a person's family or household` | tests-class1a1b:2 |
| s 10ZB | 416 | inert | reason 1 (not operative): heading | - |
| s 10ZB(1) | 417 | encoded | `s 10ZB(1) the provision is the provision of a benefit for the purposes of section 10ZA` | tests-class1a1b:2 |
| s 10ZB(2) | 418 | encoded | `s 10ZB(2) sections 10 and 10ZA have effect as if the employment were not lower-paid employment as a minister of religion` | tests-class1a1b:3 |
| s 10ZB(2)(a) | 419 | encoded | `s 10ZB(2) sections 10 and 10ZA have effect as if the employment were not lower-paid employment as a minister of religion` | tests-class1a1b:3 |
| s 10ZB(2)(b) | 420-421 | encoded | `s 10ZB(2) sections 10 and 10ZA have effect as if the employment were not lower-paid employment as a minister of religion` | tests-class1a1b:3 |
| s 10ZB(3) | 422 | encoded | `s 10ZB(3) the voucher is a non-cash voucher` | tests-class1a1b:2 |
| s 10ZBA | 423 | inert | reason 1 (not operative): heading | - |
| s 10ZBA(1) | 424 | encoded | `s 10ZBA(1) section 10ZBA applies` | tests-class1a1b:4 |
| s 10ZBA(1)(a) | 425 | encoded | `s 10ZBA(1) section 10ZBA applies` | tests-class1a1b:4 |
| s 10ZBA(1)(b) | 426 | encoded | `s 10ZBA(1) section 10ZBA applies` | tests-class1a1b:4 |
| s 10ZBA(1)(c) | 427 | encoded | `s 10ZBA(1) section 10ZBA applies` | tests-class1a1b:4 |
| s 10ZBA(2) | 428 | encoded | `s 10ZBA(2) the liability falls on the controller of the sporting testimonial` | tests-class1a1b:2 |
| s 10ZBA(3) | 429 | encoded | `s 10ZBA(4) the amount to cover tax is treated as general earnings consisting in the making of a sporting testimonial payment to the earner` | tests-class1a1b:5 |
| s 10ZBA(3)(a) | 430 | encoded | `s 10ZBA(4) the amount to cover tax is treated as general earnings consisting in the making of a sporting testimonial payment to the earner` | tests-class1a1b:5 |
| s 10ZBA(3)(b) | 431 | encoded | `s 10ZBA(4) the amount to cover tax is treated as general earnings consisting in the making of a sporting testimonial payment to the earner` | tests-class1a1b:5 |
| s 10ZBA(4) | 432 | encoded | `s 10ZBA(4) the amount to cover tax is treated as general earnings consisting in the making of a sporting testimonial payment to the earner` | tests-class1a1b:5 |
| s 10ZBA(5) | 433 | encoded | `s 10ZBA(5) the liability for the further payment falls on the controller of the sporting testimonial` | tests-class1a1b:2 |
| s 10ZBA(6) | 434 | encoded | `s 10ZBA(6) the expression has the meaning it has in section 226E of ITEPA 2003` | tests-class1a1b:2 |
| s 10ZC | 435 | inert | reason 1 (not operative): heading | - |
| s 10ZC(1) | 436 | inert | reason 2 (machinery): regulation-making power (retrospective tax legislation) | - |
| s 10ZC(1)(a) | 437 | inert | reason 2 (machinery): regulation-making power (retrospective tax legislation) | - |
| s 10ZC(1)(b) | 438 | inert | reason 2 (machinery): regulation-making power (retrospective tax legislation) | - |
| s 10ZC(2) | 439 | encoded | `s 10ZC(2) the provision is a relevant retrospective tax provision` | tests-class1a1b:3 |
| s 10ZC(2)(a) | 440 | encoded | `s 10ZC(2) the provision is a relevant retrospective tax provision` | tests-class1a1b:3 |
| s 10ZC(2)(b) | 441 | encoded | `s 10ZC(2) the provision is a relevant retrospective tax provision` | tests-class1a1b:3 |
| s 10ZC(3) | 442 | encoded | `s 10ZC(3) the relevant retrospective tax provision counts` | tests-class1a1b:2 |
| s 10ZC(4) | 443 | inert | reason 2 (machinery): content of regulations under s 10ZC | - |
| s 10ZC(4)(a) | 444 | inert | reason 2 (machinery): content of regulations under s 10ZC | - |
| s 10ZC(4)(b) | 445 | inert | reason 2 (machinery): content of regulations under s 10ZC | - |
| s 10ZC(5) | 446 | encoded | `s 10ZC(5) regulations under section 10ZC may have effect in relation to the time` | tests-class1a1b:2 |
| s 10ZC(6) | 447 | inert | reason 2 (machinery): content of regulations under s 10ZC(5) | - |
| s 10ZC(6)(a) | 448 | inert | reason 2 (machinery): content of regulations under s 10ZC(5) | - |
| s 10ZC(6)(b) | 449 | inert | reason 2 (machinery): content of regulations under s 10ZC(5) | - |
| s 10ZC(7) | 450 | encoded | `s 10ZC(7) regulations under section 10ZC may have that effect` | tests-class1a1b:3 |
| s 10ZC(7)(a) | 451 | encoded | `s 10ZC(7) regulations under section 10ZC may have that effect` | tests-class1a1b:3 |
| s 10ZC(7)(b) | 452 | encoded | `s 10ZC(7) regulations under section 10ZC may have that effect` | tests-class1a1b:3 |
| s 10ZC(8) | 453 | encoded | `s 10ZC(8)(a) the powers are without prejudice to the liability` | tests-class1a1b:2 |
| s 10ZC(8)(a) | 454 | encoded | `s 10ZC(8)(a) the powers are without prejudice to the liability` | tests-class1a1b:2 |
| s 10ZC(8)(b) | 455 | encoded | `s 10ZC(8)(a) the powers are without prejudice to the liability` | tests-class1a1b:2 |
| s 10ZC(9) | 456 | inert | reason 2 (machinery): content of regulations under s 10ZC (modifying instruments) | - |
| s 10ZC(10) | 457 | encoded | `s 10ZC(10) the day is the commencement day`; `s 10ZC(10) the thing is an enactment` | tests-class1a1b:4 |
| s 10ZC(10) “the commencement day” | 458 | encoded | `s 10ZC(10) the day is the commencement day`; `s 10ZC(10) the thing is an enactment` | tests-class1a1b:4 |
| s 10ZC(10) “enactment” | 459 | encoded | `s 10ZC(10) the thing is an enactment` | tests-class1a1b:2 |
| Heading: Class 1B contributions | 460 | inert | reason 1 (not operative): heading | - |
| s 10A | 461 | inert | reason 1 (not operative): heading | - |
| s 10A(1) | 462 | encoded | `s 10A(1) a Class 1B contribution is payable by the person for the tax year` | tests-class1a1b:2 |
| s 10A(2) | 463 | encoded | `s 10A(3) the amount of the Class 1B contribution` | tests-class1a1b:3 |
| s 10A(2)(a) | 464 | encoded | `s 10A(3) the amount of the Class 1B contribution` | tests-class1a1b:3 |
| s 10A(2)(b) | 465 | encoded | `s 10A(3) the amount of the Class 1B contribution` | tests-class1a1b:3 |
| s 10A(3) | 466 | encoded | `s 10A(3) the amount of the Class 1B contribution` | tests-class1a1b:3 |
| s 10A(4) | 467 | encoded | `s 10A(4) the general earnings are chargeable emoluments` | tests-class1a1b:2 |
| s 10A(5) | 468 | encoded | `s 10A(5) the general earnings are taken to be included in the PAYE settlement agreement` | tests-class1a1b:3 |
| s 10A(5)(a) | 469 | encoded | `s 10A(5) the general earnings are taken to be included in the PAYE settlement agreement` | tests-class1a1b:3 |
| s 10A(5)(b) | 470-471 | encoded | `s 10A(5) the general earnings are taken to be included in the PAYE settlement agreement` | tests-class1a1b:3 |
| s 10A(6) | 472 | encoded | `s 10A(6) the Class 1B percentage` | tests-class1a1b:1 |
| s 10A(7) | 473 | inert | reason 2 (machinery): regulation-making power (persons excepted from Class 1B) | - |
| Heading: Class 2 contributions | 474 | inert | reason 1 (not operative): heading | - |
| s 11 | 475 | inert | reason 1 (not operative): heading | - |
| s 11(1) | 476 | encoded | `s 11(1) section 11 applies` | tests-class23:2 |
| s 11(2) | 477 | repealed or blank in this text | the text shows only dots at line 477 | - |
| s 11(3) | 478 | encoded | `s 11(3) the profits are relevant profits` | tests-class23:5 |
| s 11(4) | 479 | encoded | `s 11(4)(b) the small profits threshold as the Act states it` | tests-class23:1 |
| s 11(4)(a) | 480 | repealed or blank in this text | the text shows only dots at line 480 | - |
| s 11(4)(b) | 481 | encoded | `s 11(4)(b) the small profits threshold as the Act states it` | tests-class23:1 |
| s 11(5) | 482 | repealed or blank in this text | the text shows only dots at line 482 | - |
| s 11(5A) | 483 | encoded | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | tests-class23:7 |
| s 11(5B) | 484 | encoded | `s 11 the number of weeks for which a Class 2 contribution was paid in the tax year`; `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | tests-class23:9 |
| s 11(5C) | 485 | encoded | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | tests-class23:7 |
| s 11(5C)(a) | 486 | encoded | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | tests-class23:7 |
| s 11(5C)(b) | 487 | encoded | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | tests-class23:7 |
| s 11(6) | 488 | encoded | `s 11(6) the Class 2 contribution as the Act states it`; `s 11(6) the earner may pay a Class 2 contribution in respect of the week` | tests-class23:8 |
| s 11(7) | 489 | encoded | `s 11(7) a Class 2 contribution is to be paid or treated as paid in respect of the week` | tests-class23:4 |
| s 11(7)(a) | 490 | encoded | `s 11(7) a Class 2 contribution is to be paid or treated as paid in respect of the week` | tests-class23:4 |
| s 11(7)(b) | 491 | encoded | `s 11(7) a Class 2 contribution is to be paid or treated as paid in respect of the week` | tests-class23:4 |
| s 11(8) | 492 | inert | reason 2 (machinery): regulation-making power (higher Class 2 rate) | - |
| s 11(8)(a) | 493 | inert | reason 2 (machinery): regulation-making power (higher Class 2 rate) | - |
| s 11(8)(b) | 494 | inert | reason 2 (machinery): regulation-making power (higher Class 2 rate) | - |
| s 11(8)(b)(i) | 495 | inert | reason 2 (machinery): regulation-making power (higher Class 2 rate) | - |
| s 11(8)(b)(ii) | 496 | inert | reason 2 (machinery): regulation-making power (higher Class 2 rate) | - |
| s 11(9) | 497 | inert | reason 2 (machinery): regulation-making power (relevant profits; payment of Class 2 under s 11(6) barred) | - |
| s 11(9)(a) | 498 | inert | reason 2 (machinery): regulation-making power (relevant profits; payment of Class 2 under s 11(6) barred) | - |
| s 11(9)(b) | 499 | inert | reason 2 (machinery): regulation-making power (relevant profits; payment of Class 2 under s 11(6) barred) | - |
| s 11(9)(b)(i) | 500 | inert | reason 2 (machinery): regulation-making power (relevant profits; payment of Class 2 under s 11(6) barred) | - |
| s 11(9)(b)(ii) | 501 | inert | reason 2 (machinery): regulation-making power (relevant profits; payment of Class 2 under s 11(6) barred) | - |
| s 11(10) | 502 | inert | reason 2 (machinery): regulations under s 11(9)(a) may amend s 11 | - |
| s 11(11) | 503 | inert | reason 2 (machinery): concurrence for regulations under s 11(9)(b) | - |
| s 11A | 504 | inert | reason 1 (not operative): heading | - |
| s 11A(1) | 505 | encoded | `s 11A(1) Part 2 of the Taxes Management Act 1970 applies, with the necessary modifications, for the purpose` | tests-class23:2 |
| s 11A(2) | 506 | encoded | `s 11A(2) the profits are relevant profits` | tests-class23:3 |
| s 12 | 507 | inert | reason 1 (not operative): heading | - |
| s 12(1) | 508 | encoded | `s 12(1) section 12 applies to the contribution` | tests-class23:4 |
| s 12(2) | 509 | encoded | `s 12(2) the amount of the late paid Class 2 contribution` | tests-class23:9 |
| s 12(3) | 510 | encoded | `s 12(3)(a) and (b) the contribution is paid after the end of the tax year immediately following the contribution year, and the weekly rates differ` | tests-class23:3 |
| s 12(3)(a) | 511 | encoded | `s 12(3)(a) and (b) the contribution is paid after the end of the tax year immediately following the contribution year, and the weekly rates differ` | tests-class23:3 |
| s 12(3)(b) | 512-513 | encoded | `s 12(3)(a) and (b) the contribution is paid after the end of the tax year immediately following the contribution year, and the weekly rates differ` | tests-class23:3 |
| s 12(4) | 514 | inert | reason 2 (machinery): regulation-making power (higher-rate contributions) | - |
| s 12(5) | 515 | repealed or blank in this text | the text shows only dots at line 515 | - |
| s 12(6) | 516 | inert | reason 2 (machinery): regulation-making power (computing late-paid Class 2 by reference to another year) | - |
| s 12(6)(a) | 517 | inert | reason 2 (machinery): regulation-making power (computing late-paid Class 2 by reference to another year) | - |
| s 12(6)(b) | 518 | repealed or blank in this text | the text shows only dots at line 518 | - |
| s 12(7) | 519 | repealed or blank in this text | the text shows only dots at line 519 | - |
| s 12(8) | 520 | encoded | `s 12(8) the contribution is an ordinary contribution` | tests-class23:2 |
| s 12(8) “ordinary contribution” | 521 | encoded | `s 12(8) the contribution is an ordinary contribution` | tests-class23:2 |
| s 12(8) “higher-rate contribution” | 522 | encoded | `s 12(8) the contribution is an ordinary contribution` | tests-class23:2 |
| Heading: Class 3 contributions | 523 | inert | reason 1 (not operative): heading | - |
| s 13 | 524 | inert | reason 1 (not operative): heading | - |
| s 13(1) | 525 | encoded | `s 13(1) the amount of a Class 3 contribution as the Act states it`; `s 13(1) the person is entitled to pay a Class 3 contribution`; `s 13 the Class 3 contribution may be paid once the bars are taken into account` | tests-class23:8 |
| s 13(2) | 526 | encoded | `s 13(2) payment of the Class 3 contribution is allowed` | tests-class23:2 |
| s 13(3) | 527 | encoded | `s 13 the number of weeks for which a Class 3 contribution was paid in the tax year` | tests-class23:1 |
| s 13(4) | 528 | encoded | `s 13(4) the amount of the Class 3 contribution for the earlier tax year` | tests-class23:8 |
| s 13(5) | 529 | encoded | `s 13(5) the payment year`; `s 13(5) the contribution year` | tests-class23:2 |
| s 13(5) “the payment year” | 530 | encoded | `s 13(5) the payment year`; `s 13(5) the contribution year` | tests-class23:2 |
| s 13(5) “the contribution year” | 531 | encoded | `s 13(5) the payment year`; `s 13(5) the contribution year` | tests-class23:2 |
| s 13(6) | 532 | encoded | `s 13(4) the amount of the Class 3 contribution for the earlier tax year` | tests-class23:8 |
| s 13(6)(a) | 533 | encoded | `s 13(4) the amount of the Class 3 contribution for the earlier tax year` | tests-class23:8 |
| s 13(6)(b) | 534-535 | encoded | `s 13(4) the amount of the Class 3 contribution for the earlier tax year` | tests-class23:8 |
| s 13(7) | 536 | inert | reason 2 (machinery): regulation-making power (computing late-paid Class 3 by reference to another year) | - |
| s 13A | 537 | inert | reason 1 (not operative): heading | - |
| s 13A(1) | 538 | encoded | `s 13A(1) an eligible person is entitled to pay a Class 3 contribution in respect of the missing year, having regard to subsections (3) and (4)` | tests-class23:6 |
| s 13A(2) | 539 | encoded | `s 13A(2) the tax year is a missing year` | tests-class23:3 |
| s 13A(3) | 540 | encoded | `s 13A(3) the person is entitled to pay a contribution under section 13A for the tax year` | tests-class23:3 |
| s 13A(4) | 541 | fork | F4 (end of 6 years; a 29 February start) -- encoded by `s 13A(4) the last day on which a contribution may be paid under section 13A`; `s 13A(4) the person is entitled to pay a contribution under section 13A on the day` | tests-class23:6 |
| s 13A(5) | 542 | encoded | `s 13A(5) the person is an eligible person` | tests-class23:9 |
| s 13A(6) | 543 | encoded | `s 13A(6) the first condition is satisfied` | tests-class23:4 |
| s 13A(6)(a) | 544 | encoded | `s 13A(6) the first condition is satisfied` | tests-class23:4 |
| s 13A(6)(b) | 545 | encoded | `s 13A(6) the first condition is satisfied` | tests-class23:4 |
| s 13A(7) | 546 | encoded | `s 13A(7) the second condition is satisfied` | tests-class23:2 |
| s 13A(8) | 547 | encoded | `s 13A(8) the year is a year to which subsection (8) applies` | tests-class23:3 |
| s 13A(8)(a) | 548 | encoded | `s 13A(8) the year is a year to which subsection (8) applies` | tests-class23:3 |
| s 13A(8)(b) | 549 | encoded | `s 13A(8) the year is a year to which subsection (8) applies` | tests-class23:3 |
| s 13A(9) | 550 | encoded | `s 13A(9)(a)(i) the earnings from which the earnings factor is derived` | tests-class23:3 |
| s 13A(9)(a) | 551 | encoded | `s 13A(9)(a)(i) the earnings from which the earnings factor is derived` | tests-class23:3 |
| s 13A(9)(a)(i) | 552 | encoded | `s 13A(9)(a)(i) the earnings from which the earnings factor is derived` | tests-class23:3 |
| s 13A(9)(a)(ii) | 553 | encoded | `s 13A(9)(a)(i) the earnings from which the earnings factor is derived` [the conversion of Class 2 and Class 3 contributions into an earnings factor is Schedule 3 (ssc8); the factor is an input] | tests-class23:3 |
| s 13A(9)(b) | 554 | encoded | `s 13A(9)(a)(i) the earnings from which the earnings factor is derived` [the derivation of the earlier-year earnings factor is Schedule 3 (ssc8); the factor is an input] | tests-class23:3 |
| s 13A(10) | 555 | encoded | `s 13A(10) the year is a year to which subsection (10) applies` | tests-class23:3 |
| s 13A(11) | 556 | encoded | `s 13A(11) the third condition applies` | tests-class23:2 |
| s 13A(12) | 557 | encoded | `s 13A(12) the third condition is satisfied` | tests-class23:3 |
| s 13A(12)(a) | 558 | encoded | `s 13A(12) the third condition is satisfied` | tests-class23:3 |
| s 13A(12)(b) | 559 | encoded | `s 13A(12) the third condition is satisfied` | tests-class23:3 |
| s 13A(13) | 560 | encoded | `s 13A(13)(a)(i) the earnings from which the earnings factor is derived` | tests-class23:2 |
| s 13A(13)(a) | 561 | encoded | `s 13A(13)(a)(i) the earnings from which the earnings factor is derived` | tests-class23:2 |
| s 13A(13)(a)(i) | 562 | encoded | `s 13A(13)(a)(i) the earnings from which the earnings factor is derived` | tests-class23:2 |
| s 13A(13)(a)(ii) | 563 | encoded | `s 13A(13)(a)(i) the earnings from which the earnings factor is derived` [the conversion of Class 2 and Class 3 contributions into an earnings factor is Schedule 3 (ssc8); the factor is an input] | tests-class23:2 |
| s 13A(13)(b) | 564 | encoded | `s 13A(13)(a)(i) the earnings from which the earnings factor is derived` [the derivation of the earlier-year earnings factor is Schedule 3 (ssc8); the factor is an input] | tests-class23:2 |
| s 14 | 565 | inert | reason 1 (not operative): heading | - |
| s 14(1) | 566 | encoded | `s 14(1) the person is entitled to pay a Class 3 contribution for the tax year` | tests-class23:3 |
| s 14(1)(a) | 567 | encoded | `s 14(1) the person is entitled to pay a Class 3 contribution for the tax year` | tests-class23:3 |
| s 14(1)(b) | 568-569 | encoded | `s 14(1) the person is entitled to pay a Class 3 contribution for the tax year` | tests-class23:3 |
| s 14(2) | 570 | inert | reason 2 (machinery): regulation-making power (repayment of Class 3) | - |
| s 14(3) | 571 | encoded | `s 14(3) the contribution is treated as not having been paid for the purpose of determining entitlement to any benefit` | tests-class23:2 |
| s 14(4) | 572 | encoded | `s 14(4) the earnings on which primary Class 1 contributions are treated as paid for the purposes of subsection (1)(a)` | tests-class23:3 |
| s 14(5) | 573 | inert | reason 2 (machinery): who makes regulations under s 14(1) and (2) | - |
| Heading: Class 3A contributions | 574 | inert | reason 1 (not operative): heading | - |
| s 14A | 575 | inert | reason 1 (not operative): heading | - |
| s 14A(1) | 576 | encoded | `s 14A(1) the person is entitled to pay a Class 3A contribution on the day` | tests-class23:8 |
| s 14A(1A) | 577 | encoded | `s 14A(1A) the cut-off date` | tests-class23:9 |
| s 14A(1A)(a) | 578 | encoded | `s 14A(1A) the cut-off date` | tests-class23:9 |
| s 14A(1A)(b) | 579 | fork | F5 (end of a 30-day period beginning with a day) -- encoded by `s 14A(1A) the cut-off date` | tests-class23:9 |
| s 14A(2) | 580 | encoded | `s 14A(2) the person is eligible to pay a Class 3A contribution` | tests-class23:7 |
| s 14A(2)(a) | 581 | encoded | `s 14A(2) the person is eligible to pay a Class 3A contribution` | tests-class23:7 |
| s 14A(2)(b) | 582 | encoded | `s 14A(2) the person is eligible to pay a Class 3A contribution` | tests-class23:7 |
| s 14A(3) | 583 | inert | reason 2 (machinery): the amount of a Class 3A contribution is determined by regulations | - |
| s 14A(4) | 584 | inert | reason 2 (machinery): the Treasury must consult the Government Actuary before making those regulations | - |
| s 14A(5) | 585 | encoded | `s 14A(5) the person may pay a Class 3A contribution on this occasion` | tests-class23:4 |
| s 14A(5)(a) | 586 | encoded | `s 14A(5) the person may pay a Class 3A contribution on this occasion` | tests-class23:4 |
| s 14A(5)(b) | 587 | encoded | `s 14A(5) the person may pay a Class 3A contribution on this occasion` | tests-class23:4 |
| s 14A(6) | 588 | encoded | `s 14A(5) the person may pay a Class 3A contribution on this occasion` | tests-class23:4 |
| s 14A(7) | 589 | encoded | `s 14A(7) the graduated retirement benefit is deferred` | tests-class23:2 |
| s 14A(8) | 590 | encoded | `s 14A(8) the Category A or Category B retirement pension is deferred` | tests-class23:2 |
| s 14B | 591 | inert | reason 1 (not operative): heading | - |
| s 14B(1) | 592 | inert | reason 2 (machinery): regulation-making power (repayment of Class 3A) | - |
| s 14B(2) | 593 | inert | reason 2 (machinery): content of regulations under s 14B(1) | - |
| s 14B(3) | 594 | encoded | `s 14B(3) the person is treated as never having had the unit of additional pension` | tests-class23:2 |
| s 14B(4) | 595 | inert | reason 2 (machinery): content of regulations under s 14B(1) | - |
| s 14C | 596 | inert | reason 1 (not operative): heading | - |
| s 14C(1) | 597 | inert | reason 2 (machinery): regulation-making power (who is eligible to pay Class 3A) | - |
| s 14C(2) | 598 | inert | reason 2 (machinery): regulation-making power (removing the option to pay Class 3A) | - |
| s 14C(3) | 599 | inert | reason 2 (machinery): content of regulations under s 14C | - |
| Heading: Class 4 contributions | 600 | inert | reason 1 (not operative): heading | - |
| s 15 | 601 | inert | reason 1 (not operative): heading | - |
| s 15(1) | 602 | encoded | `s 15(1) Class 4 contributions are payable for the tax year in respect of the profits` | tests-class4:4 |
| s 15(1)(a) | 603 | encoded | `s 15(1) Class 4 contributions are payable for the tax year in respect of the profits` | tests-class4:4 |
| s 15(1)(b) | 604 | encoded | `s 15(1) Class 4 contributions are payable for the tax year in respect of the profits` | tests-class4:4 |
| s 15(1)(c) | 605 | encoded | `s 15(1) Class 4 contributions are payable for the tax year in respect of the profits` | tests-class4:4 |
| s 15(2) | 606 | encoded | `s 15(2) the person is liable to pay the Class 4 contribution` | tests-class4:3 |
| s 15(2)(a) | 607 | encoded | `s 15(2) the person is liable to pay the Class 4 contribution` | tests-class4:3 |
| s 15(2)(b) | 608-609 | encoded | `s 15(2) the person is liable to pay the Class 4 contribution` | tests-class4:3 |
| s 15(3) | 610 | encoded | `s 15(3)(a) the lower profits limit as the Act states it`; `s 15(3)(b) the upper profits limit as the Act states it`; `s 15(3) the amount of the Class 4 contribution for the tax year` | tests-class4:11 |
| s 15(3)(a) | 611 | encoded | `s 15(3)(a) the lower profits limit as the Act states it`; `s 15(3) the amount of the Class 4 contribution for the tax year` | tests-class4:10 |
| s 15(3)(b) | 612-613 | encoded | `s 15(3)(b) the upper profits limit as the Act states it`; `s 15(3) the amount of the Class 4 contribution for the tax year` | tests-class4:10 |
| s 15(3ZA) | 614 | encoded | `s 15(3ZA)(b) the additional Class 4 percentage as the Act states it`; `s 15(3ZA)(a) the main Class 4 percentage as the Act states it` | tests-class4:2 |
| s 15(3ZA)(a) | 615 | encoded | `s 15(3ZA)(b) the additional Class 4 percentage as the Act states it`; `s 15(3ZA)(a) the main Class 4 percentage as the Act states it` | tests-class4:2 |
| s 15(3ZA)(b) | 616-617 | encoded | `s 15(3ZA)(b) the additional Class 4 percentage as the Act states it`; `s 15(3ZA)(a) the main Class 4 percentage as the Act states it` | tests-class4:2 |
| s 15(3A) | 618 | encoded | `s 15(3A) Class 4 contributions are payable by the member of the limited liability partnership` | tests-class4:4 |
| s 15(4) | 619 | repealed or blank in this text | the text shows only dots at line 619 | - |
| s 15(5) | 620 | encoded | `s 15(5) the year of assessment corresponds to the tax year` | tests-class4:2 |
| s 16 | 621 | inert | reason 1 (not operative): heading | - |
| s 16(1) | 622 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(1)(a) | 623 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(1)(b) | 624 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(1)(c) | 625 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(1)(d) | 626 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(1)(e) | 627 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(1)(f) | 628-629 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(2) | 630 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(2)(a) | 631 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(2)(b) | 632 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(2)(c) | 633 | encoded | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | tests-class4:3 |
| s 16(3) | 634 | encoded | `s 16(3) Schedule 2 has effect in relation to the class of contribution` | tests-class4:2 |
| s 16(4) | 635 | repealed or blank in this text | the text shows only dots at line 635 | - |
| s 16(5) | 636 | repealed or blank in this text | the text shows only dots at line 636 | - |
| s 17 | 637 | inert | reason 1 (not operative): heading | - |
| s 17(1) | 638 | inert | reason 2 (machinery): regulation-making power (exceptions from, and deferment of, Class 4 liability) | - |
| s 17(1)(a) | 639 | inert | reason 2 (machinery): regulation-making power (exceptions from, and deferment of, Class 4 liability) | - |
| s 17(1)(b) | 640 | inert | reason 2 (machinery): regulation-making power (exceptions from, and deferment of, Class 4 liability) | - |
| s 17(1)(b) (omission at line 641) | 641 | repealed or blank in this text | the text shows "...", an editorial omission, at line 641 | - |
| s 17(2) | 642 | inert | reason 2 (machinery): content of regulations under s 17(1) | - |
| s 17(2)(a) | 643 | inert | reason 2 (machinery): content of regulations under s 17(1) | - |
| s 17(2)(b) | 644 | inert | reason 2 (machinery): content of regulations under s 17(1) | - |
| s 17(2)(c) | 645 | inert | reason 2 (machinery): content of regulations under s 17(1) | - |
| s 17(2)(d) | 646 | inert | reason 2 (machinery): content of regulations under s 17(1) | - |
| s 17(3) | 647 | inert | reason 2 (machinery): regulation-making power (incidental matters; repayment of Class 4) | - |
| s 17(3)(a) | 648 | inert | reason 2 (machinery): regulation-making power (incidental matters; repayment of Class 4) | - |
| s 17(3)(b) | 649 | inert | reason 2 (machinery): regulation-making power (incidental matters; repayment of Class 4) | - |
| s 17(4) | 650 | inert | reason 2 (machinery): regulation-making power (matters arising out of deferment) | - |
| s 17(5) | 651 | repealed or blank in this text | the text shows only dots at line 651 | - |
| s 17(6) | 652 | repealed or blank in this text | the text shows only dots at line 652 | - |
| s 18 | 653 | inert | reason 1 (not operative): heading | - |
| s 18(1) | 654 | encoded | `s 18(1) the regulations may make the earner liable to pay a Class 4 contribution in respect of the earnings` | tests-class4:4 |
| s 18(1)(a) | 655 | encoded | `s 18(1) the regulations may make the earner liable to pay a Class 4 contribution in respect of the earnings` | tests-class4:4 |
| s 18(1)(b) | 656 | encoded | `s 18(1) the regulations may make the earner liable to pay a Class 4 contribution in respect of the earnings` | tests-class4:4 |
| s 18(1)(c) | 657-658 | encoded | `s 18(1) the regulations may make the earner liable to pay a Class 4 contribution in respect of the earnings` | tests-class4:4 |
| s 18(1A) | 659 | encoded | `s 18(1A) the amount of the Class 4 contribution payable by virtue of regulations under section 18` | tests-class4:4 |
| s 18(1A)(a) | 660 | encoded | `s 18(1A) the amount of the Class 4 contribution payable by virtue of regulations under section 18` | tests-class4:4 |
| s 18(1A)(b) | 661-662 | encoded | `s 18(1A) the amount of the Class 4 contribution payable by virtue of regulations under section 18` | tests-class4:4 |
| s 18(2) | 663 | inert | reason 2 (machinery): regulation-making power (applying Schedule 1 to Class 4 under s 18) | - |
| s 18(2)(a) | 664 | inert | reason 2 (machinery): regulation-making power (applying Schedule 1 to Class 4 under s 18) | - |
| s 18(2)(b) | 665 | inert | reason 2 (machinery): regulation-making power (applying Schedule 1 to Class 4 under s 18) | - |
| s 18A | 666 | inert | reason 1 (not operative): heading | - |
| s 18A(1) | 667 | inert | reason 2 (machinery): regulation-making power (partners in a firm) | - |
| s 18A(1)(a) | 668 | inert | reason 2 (machinery): regulation-making power (partners in a firm) | - |
| s 18A(1)(b) | 669-670 | inert | reason 2 (machinery): regulation-making power (partners in a firm) | - |
| s 18A(2) | 671 | encoded | `s 18A(2) the body is a firm`; `s 18A(2) the person is a partner` | tests-class4:6 |
| s 18A(3) | 672 | encoded | `s 18A(3) regulations under section 18A may have effect from the day` | tests-class4:3 |
| Heading: General | 673 | inert | reason 1 (not operative): heading | - |
| s 19 | 674 | inert | reason 1 (not operative): heading | - |
| s 19(1) | 675 | inert | reason 2 (machinery): regulation-making power (maximum liability for contributions) | - |
| s 19(1)(a) | 676 | inert | reason 2 (machinery): regulation-making power (maximum liability for contributions) | - |
| s 19(1)(b) | 677-678 | inert | reason 2 (machinery): regulation-making power (maximum liability for contributions) | - |
| s 19(2) | 679 | inert | reason 2 (machinery): content of regulations under s 19(1) | - |
| s 19(2)(a) | 680 | inert | reason 2 (machinery): content of regulations under s 19(1) | - |
| s 19(2)(b) | 681 | inert | reason 2 (machinery): content of regulations under s 19(1) | - |
| s 19(3) | 682 | inert | reason 2 (machinery): regulation-making power (exceptions from liability) | - |
| s 19(4) | 683 | inert | reason 2 (machinery): regulation-making duty (election by women married or widowed on 6 April 1977) | - |
| s 19(4)(a) | 684 | inert | reason 2 (machinery): regulation-making duty (election by women married or widowed on 6 April 1977) | - |
| s 19(4)(b) | 685 | inert | reason 2 (machinery): regulation-making duty (election by women married or widowed on 6 April 1977) | - |
| s 19(4)(c) | 686 | inert | reason 2 (machinery): regulation-making duty (election by women married or widowed on 6 April 1977) | - |
| s 19(5) | 687 | inert | reason 2 (machinery): content of regulations under s 19(4) | - |
| s 19(5)(a) | 688 | inert | reason 2 (machinery): content of regulations under s 19(4) | - |
| s 19(5)(b) | 689 | inert | reason 2 (machinery): content of regulations under s 19(4) | - |
| s 19(5)(c) | 690 | inert | reason 2 (machinery): content of regulations under s 19(4) | - |
| s 19(5)(d) | 691 | inert | reason 2 (machinery): content of regulations under s 19(4) | - |
| s 19(5A) | 692 | inert | reason 2 (machinery): who makes regulations under s 19(1) to (5) | - |
| s 19(6) | 693 | inert | reason 2 (machinery): regulation-making power (earnings factors for reduced-rate payers) | - |
| s 19(6)(a) | 694 | inert | reason 2 (machinery): regulation-making power (earnings factors for reduced-rate payers) | - |
| s 19(6)(a)(i) | 695 | inert | reason 2 (machinery): regulation-making power (earnings factors for reduced-rate payers) | - |
| s 19(6)(a)(ii) | 696 | inert | reason 2 (machinery): regulation-making power (earnings factors for reduced-rate payers) | - |
| s 19(6)(b) | 697-698 | inert | reason 2 (machinery): regulation-making power (earnings factors for reduced-rate payers) | - |
| s 19A | 699 | inert | reason 1 (not operative): heading | - |
| s 19A(1) | 700 | encoded | `s 19A(1) section 19A applies` | tests-general:6 |
| s 19A(1)(a) | 701 | encoded | `s 19A(1) section 19A applies` | tests-general:6 |
| s 19A(1)(b) | 702 | encoded | `s 19A(1) section 19A applies` | tests-general:6 |
| s 19A(1)(c) | 703 | encoded | `s 19A(1)(c) the last day of year 2`; `s 19A(1) section 19A applies` | tests-general:8 |
| s 19A(2) | 704 | encoded | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` | tests-general:6 |
| s 19A(2)(a) | 705 | encoded | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` | tests-general:6 |
| s 19A(2)(b) | 706-707 | encoded | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` | tests-general:6 |
| s 19A(3) | 708 | inert | reason 2 (machinery): who makes regulations under s 19A(2) | - |
| s 19B | 709 | inert | reason 1 (not operative): heading | - |
| s 19B (single paragraph) | 710 | encoded | `s 19B a reference to benefit or contributory benefit in Part I includes the benefit` | tests-general:2 |

## Fork register (ssc1)

A fork is a place where the text can be read two or more ways with different outcomes. Each row of the coverage table marked `fork` points at one of these.
The reading taken is stated first; where the text does not choose, the rule answers NOTHING.

| id | provision (lines) | readings | reading taken, and the text that licenses each | rule |
|---|---|---|---|---|
| F1 | s 2(1)(a) (src:34-35), "in an office (including elective office) with ... earnings" | (A) the office must carry earnings; (B) the words "with ... earnings" are incomplete in this rendering (the dots), so the qualifier is not relied on and any office counts | (A) taken: the words that remain, "with ... earnings", still require earnings, and `means` closes the definition; (B) rests on "(including elective office)" and on the dots, which show the rendering has lost words. They differ for an unpaid elective office: not an employed earner under (A), an employed earner under (B). Under (A) the holder who is gainfully employed in Great Britain is a self-employed earner (s 2(1)(b)). The input `the office carries earnings` records the fact | `s 2(1)(a) the person is an employed earner` |
| F2 | s 4(4)(a) (src:78-79), "reduced by any amounts deducted under section 480(1) to (6)" | when the deductions exceed the gain: (A) nothing is treated as remuneration; (B) a negative amount; (C) the text does not say | (C) taken, answer NOTHING: "reduced by" fixes the subtraction but says nothing of a floor, so neither (A) nor (B) is licensed by any word of the text | `s 4(4)(a) the amount treated as remuneration derived from employed earner's employment` |
| F3 | s 6A(2)(b) (src:266), seam S4 | which earnings count as "earnings upon which such a contribution has been paid": (A) the whole earnings of a week in which a primary contribution was paid or treated as paid; (B) only the part up to the upper earnings limit, as s 14(4) says for s 14(1)(a) | (A) taken for the seam: s 6A(2)(b) says "those earnings", the earnings of the week as a whole, "shall be treated as earnings upon which such a contribution has been paid", and sets no cap. (B) is what s 14(4) provides for s 14(1)(a), and that function (`s 14(4) the earnings on which primary Class 1 contributions are treated as paid for the purposes of subsection (1)(a)`) is in the Class 3 module, so a caller who means s 14(1)(a) gets the capped figure. The lead aggregates by tax year at the merge | `s 6 the earnings on which primary Class 1 contributions have been paid or treated as paid in the tax year` |
| F4 | s 13A(4) (src:541), "after the end of 6 years beginning with the day on which he attains pensionable age" | (A) the last day is the day before the sixth anniversary of that day (6 April 2010 gives 5 April 2016); (B) the sixth anniversary itself; and, for a day of 29 February, the sixth anniversary of a common year does not exist | (A) taken: a period of 6 years "beginning with" a day includes that day, so it ends the day before the anniversary. For a 29 February the text does not say what the anniversary is: NOTHING (PLAN section 1.5 forbids adding years to a 29 February) | `s 13A(4) the last day on which a contribution may be paid under section 13A` |
| F5 | s 14A(1A)(b) (src:579), "the end of the 30-day period beginning with the day on which the person is sent information" | (A) the day itself is day 1, so the period ends on that day plus 29; (B) the period starts the next day and ends on that day plus 30 | (A) taken, as in F4: "beginning with" a day includes it. 7 March 2017 plus 29 days is 5 April 2017 (equal to paragraph (a)); 8 March gives 6 April | `s 14A(1A) the cut-off date` |

Not forks, though they look like one: "before the cut-off date" (s 14A(1)) is strict, the cut-off day itself is not before it, and the rule says so; "exceeds" and "does not exceed" at the thresholds in ss 6, 6A and 18(1)(c) are strict and inclusive as the words say, and each boundary is asserted on both sides.

## Jural relations (ssc1)

One row per provision that creates a relation, giving the party holding the right, privilege, power or immunity and the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it.
The last two rows are aggregates, not relations: the first lists the subsections that are machinery (powers or duties to make regulations or orders, inert reason 2, no rule; where a rule depends on what such a regulation provides, its outcome is an input), and the second lists the subsections that create no relation of their own (definitions, counting and deeming rules, conditions, the Act's own figures, limits on a power or privilege stated elsewhere, allocation rules whose duty another subsection creates).

| provision | relation | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | L4 rule |
|---|---|---|---|---|
| s 1(6) | immunity / disability | any person (no liability to pay Class 1, 1A, 1B or 2, no entitlement to pay Class 3, or to pay a Class 1, 1A, 1B or 2 contribution that is not theirs, unless the residence conditions or a permission by regulations are met) | the Crown (the Inland Revenue / HMRC) (disabled from imposing the liability) | `s 1(6)(a) the person is liable to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` |
| s 4A(1) | power / liability | the Treasury (by regulations: treat relevant payments to a worker as earnings) | the worker, the client and the intermediary (liable to be so treated) | `s 4A(1) the regulations may treat relevant payments or benefits as earnings paid to the worker in respect of an employed earner's employment` |
| s 4B(5) | power / liability | the Treasury (retrospective regulations from 6 April 1992 or later) | earners and secondary contributors (liable to retrospective regulations) | `s 4B(5) subsection (2) authorises regulations that have effect in relation to the time` |
| s 4C(4) | power / liability | the Treasury (consequential regulations with retrospective effect) | earners and secondary contributors | `s 4C(4) regulations under subsection (1) may have effect in relation to the time` |
| s 4C(7) | immunity / disability | a person with an entitlement to a contributory benefit, contribution-based jobseeker's allowance or statutory payment | the Treasury (disabled from removing or reducing it by regulations under s 4C(1)) | `s 4C(7) the operative provisions are to be read with the modifications necessary to prevent that effect` |
| s 6(1) | claim / duty | the Crown (the Inland Revenue / HMRC) (to a primary Class 1 contribution from an earner over 16, and a secondary one from the secondary contributor, where the amount paid exceeds the threshold) | the employed earner (primary); the secondary contributor (the employer or other payer of earnings) (secondary) | `s 6(1)(a) a primary Class 1 contribution is payable in accordance with sections 6 and 8`; `s 6(1)(b) a secondary Class 1 contribution is payable in accordance with sections 6 and 9` |
| s 6(2) | immunity / disability | the employed earner and the secondary contributor (the employer or other payer of earnings) (no Class 1 contribution on earnings on which Class 1B is payable) | the Crown (the Inland Revenue / HMRC) (disabled) | `s 6(2) a primary or secondary Class 1 contribution is payable in respect of the earnings` |
| s 6(3) | immunity / disability | the employed earner past pensionable age (no primary Class 1 contribution, save as prescribed) | the Crown (the Inland Revenue / HMRC) (disabled); secondary liability is unaffected | `s 6(3) a primary Class 1 contribution is payable in respect of the earnings` |
| s 6(4) | claim / duty | the Crown (the Inland Revenue / HMRC) | the employed earner (liable to pay the primary contribution); the secondary contributor (the employer or other payer of earnings) (liable to pay the secondary), subject to Schedule 1 paras 3 to 3B | `s 6(4) who is liable to pay the Class 1 contribution` |
| s 6A(2) | claim / duty | the employed earner with earnings from the lower earnings limit to the primary threshold (to be treated as having paid a primary contribution, for the listed benefit purposes) | the Secretary of State (and the authorities applying benefit law) | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` |
| s 8(1) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount of the primary contribution) | the employed earner | `s 8(1) the amount of the primary Class 1 contribution` |
| s 9(1) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount of the secondary contribution) | the secondary contributor (the employer or other payer of earnings) | `s 9(1) the amount of the secondary Class 1 contribution` |
| s 10(1) | claim / duty | the Crown (the Inland Revenue / HMRC) (to a Class 1A contribution on benefits in kind) | the secondary contributor (the employer or other payer of earnings) (or the person s 10(2) names) | `s 10(1) a Class 1A contribution is payable for the tax year` |
| s 10(1A) | claim / duty | the Crown (the Inland Revenue / HMRC) (to a Class 1A contribution on a termination award) | the person who would be liable for the secondary Class 1 contribution (s 10(3A)) | `s 10(1A) a Class 1A contribution is payable for the tax year in respect of the termination award` |
| s 10(1B) | immunity / disability | the payer (no Class 1A under s 10(1A) on an amount on which Class 1 is payable) | the Crown (the Inland Revenue / HMRC) (disabled) | `s 10(1B) a Class 1A contribution is payable under subsection (1A) in respect of the amount` |
| s 10(1C) | immunity / disability | the payer (no Class 1A under s 10(1A) unless the terminated employment is employed earner's employment) | the Crown (the Inland Revenue / HMRC) (disabled) | `s 10(1C) a Class 1A contribution is payable under subsection (1A)` |
| s 10(2) | claim / duty | the Crown (the Inland Revenue / HMRC) | the person liable for the secondary Class 1 contribution on the last relevant payment, or the person who would be (paragraph (b)) | `s 10(2) who pays the Class 1A contribution payable under subsection (1)` |
| s 10(3A) | claim / duty | the Crown (the Inland Revenue / HMRC) | the person who would be liable for the secondary Class 1 contribution | `s 10(3A) who pays the Class 1A contribution payable under subsection (1A)` |
| s 10(4) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount of the Class 1A contribution) | the secondary contributor (the employer or other payer of earnings) | `s 10(4) the amount of the Class 1A contribution payable under subsection (1)` |
| s 10(4A) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount of the Class 1A contribution on a termination award) | the secondary contributor (the employer or other payer of earnings) | `s 10(4A) the amount of the Class 1A contribution payable under subsection (1A)` |
| s 10(6) | immunity / disability | the secondary contributor (the employer or other payer of earnings) (no Class 1A where the earnings are in a PAYE settlement agreement) | the Crown (the Inland Revenue / HMRC) (disabled) | `s 10(6) a Class 1A contribution is payable in respect of the general earnings` |
| s 10ZA(3) | claim / duty | the Crown (the Inland Revenue / HMRC) | the person providing the benefit (instead of the relevant employer) | `s 10ZA(3) the liability falls on the person providing the benefit` |
| s 10ZBA(2) | claim / duty | the Crown (the Inland Revenue / HMRC) | the controller of the sporting testimonial (instead of the relevant employer) | `s 10ZBA(2) the liability falls on the controller of the sporting testimonial` |
| s 10ZBA(5) | claim / duty | the Crown (the Inland Revenue / HMRC) | the controller of the sporting testimonial (for a further payment) | `s 10ZBA(5) the liability for the further payment falls on the controller of the sporting testimonial` |
| s 10ZC(5) | power / liability | the Treasury (regulations with retrospective effect) | persons liable to Class 1A | `s 10ZC(5) regulations under section 10ZC may have effect in relation to the time` |
| s 10ZC(7) | immunity / disability | the payer (no new or increased Class 1A liability by retrospective regulations unless s 10ZC(7) permits) | the Treasury (disabled) | `s 10ZC(7) regulations under section 10ZC may have that effect` |
| s 10A(1) | claim / duty | the Crown (the Inland Revenue / HMRC) (to a Class 1B contribution) | the person accountable for income tax under a PAYE settlement agreement | `s 10A(1) a Class 1B contribution is payable by the person for the tax year` |
| s 10A(3) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount of the Class 1B contribution) | the person accountable under the PAYE settlement agreement | `s 10A(3) the amount of the Class 1B contribution` |
| s 11(5B) | claim / duty | the self-employed earner with relevant profits of, or exceeding, the small profits threshold (to be treated as having paid Class 2, for benefit purposes) | the Secretary of State (and the authorities applying benefit law) | `s 11 the number of weeks for which a Class 2 contribution was paid in the tax year`; `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` |
| s 11(6) | privilege / no-right | the self-employed earner below the threshold (may pay Class 2 of GBP 3.65 for a week) | the Crown (the Inland Revenue / HMRC) (no right to refuse it); regulations under s 11(9)(b) may bar | `s 11(6) the Class 2 contribution as the Act states it`; `s 11(6) the earner may pay a Class 2 contribution in respect of the week` |
| s 11(7) | immunity / disability | the self-employed earner (no Class 2 paid or treated as paid for a week before 16 or after pensionable age) | the Crown (the Inland Revenue / HMRC) (disabled) | `s 11(7) a Class 2 contribution is to be paid or treated as paid in respect of the week` |
| s 12(2) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the late-paid amount) | the self-employed earner | `s 12(2) the amount of the late paid Class 2 contribution` |
| s 12(3) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the highest weekly rate where an ordinary contribution is paid late) | the self-employed earner | `s 12(3)(a) and (b) the contribution is paid after the end of the tax year immediately following the contribution year, and the weekly rates differ` |
| s 13(1) | privilege / no-right | earners and others over 16 (may pay Class 3 contributions of GBP 18.40 a week, on prescribed conditions) | the Crown (the Inland Revenue / HMRC) (no right to refuse); the Treasury must make the regulations | `s 13(1) the amount of a Class 3 contribution as the Act states it`; `s 13(1) the person is entitled to pay a Class 3 contribution` |
| s 13(3) | power / liability | the Secretary of State (and the authorities applying benefit law) (by regulations: appropriate Class 3 contributions to another tax year) | the contributor | `s 13 the number of weeks for which a Class 3 contribution was paid in the tax year` |
| s 13(4) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount for an earlier tax year) | the contributor | `s 13(4) the amount of the Class 3 contribution for the earlier tax year` |
| s 13A(1) | privilege / no-right | an eligible person (may pay Class 3 contributions for a missing year, on prescribed conditions) | the Crown (the Inland Revenue / HMRC) (no right to refuse); ss 13A(3) and (4) limit the privilege to 6 years and to 6 years from pensionable age | `s 13A(1) an eligible person is entitled to pay a Class 3 contribution in respect of the missing year, having regard to subsections (3) and (4)` |
| s 14A(1) | privilege / no-right | an eligible person (may pay a Class 3A contribution before the cut-off date for a unit of additional pension) | the Crown (the Inland Revenue / HMRC) (no right to refuse) | `s 14A(1) the person is entitled to pay a Class 3A contribution on the day` |
| s 14A(5) | privilege / no-right | a person (may pay Class 3A contributions on more than one occasion, up to the maximum units) | the Crown (the Inland Revenue / HMRC) | `s 14A(5) the person may pay a Class 3A contribution on this occasion` |
| s 15(1) | claim / duty | the Crown (the Inland Revenue / HMRC) (to Class 4 contributions on trading profits) | the self-employed earner | `s 15(1) Class 4 contributions are payable for the tax year in respect of the profits` |
| s 15(2) | claim / duty | the Crown (the Inland Revenue / HMRC) | the person on whom the income tax is (or would be) charged | `s 15(2) the person is liable to pay the Class 4 contribution` |
| s 15(3) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount of the Class 4 contribution) | the self-employed earner | `s 15(3)(a) the lower profits limit as the Act states it`; `s 15(3)(b) the upper profits limit as the Act states it` |
| s 15(3A) | claim / duty | the Crown (the Inland Revenue / HMRC) | a member of a limited liability partnership | `s 15(3A) Class 4 contributions are payable by the member of the limited liability partnership` |
| s 16(1) | power / liability | the Crown (the Inland Revenue / HMRC) (all powers of the Income Tax Acts: assessment, collection, repayment, recovery, penalties) | the Class 4 contributor (liable to them) | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` |
| s 18(1) | power / liability | the Inland Revenue (by regulations: make an earner treated as self-employed liable to Class 4) | the earner | `s 18(1) the regulations may make the earner liable to pay a Class 4 contribution in respect of the earnings` |
| s 18(1A) | claim / duty | the Crown (the Inland Revenue / HMRC) (to the amount payable under regulations under s 18) | the earner so liable | `s 18(1A) the amount of the Class 4 contribution payable by virtue of regulations under section 18` |
| s 18A(3) | immunity / disability | a partner in a firm (no regulations under s 18A with effect from before the start of the tax year in which they are made) | the Treasury (disabled) | `s 18A(3) regulations under section 18A may have effect from the day` |
| s 19A(2) | claim / duty | the earner for whom contributions were paid in error (to be treated, after year 2, as in employed earner's employment) | the Secretary of State (and the authorities applying benefit law) and the Inland Revenue | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` |
| 93 subsections of reason 2 (machinery): s 1(3), s 1(7), s 2(2), s 2(2ZA), s 2(2A), s 3(2), s 3(2A), s 3(3), s 3(4), s 3(5), s 4(2), s 4(5), s 4(6), s 4(6A), s 4(6B), s 4(6D), s 4(7), s 4A(4), s 4A(5), s 4A(8), s 4A(9), s 4AA(1), s 4AA(2), s 4AA(3), s 4AA(4), s 4AA(5), s 4AA(6), s 4B(1), s 4B(2), s 4B(6), s 4B(12), s 4C(1), s 4C(2), s 4C(3), s 4C(5), s 4C(6), s 4C(9), s 4C(10), s 5(6), s 6(6), s 6(7), s 6A(4), s 6A(7), s 7(2), s 7(2A), s 7(3), s 8(3), s 9(3), s 9A(4), s 9A(7), s 9B(4), s 9B(8), s 9B(10), s 10(8), s 10(9), s 10(11), s 10ZA(5), s 10ZC(1), s 10ZC(4), s 10ZC(6), s 10ZC(9), s 10A(7), s 11(8), s 11(9), s 11(10), s 11(11), s 12(4), s 12(6), s 13(7), s 14(2), s 14(5), s 14A(3), s 14A(4), s 14B(1), s 14B(2), s 14B(4), s 14C(1), s 14C(2), s 14C(3), s 17(1), s 17(2), s 17(3), s 17(4), s 18(2), s 18A(1), s 19(1), s 19(2), s 19(3), s 19(4), s 19(5), s 19(5A), s 19(6), s 19A(3) | power / liability | the Treasury, the Secretary of State or the Inland Revenue (power to make regulations, orders or amendments), or the duty to make them | the persons the regulations will bind (liability); a person who may rely on a regulation once made | none: inert reason 2; where a rule depends on what such a regulation provides, its outcome is an input |
| 123 subsections that create no relation: s 1(1), s 1(2), s 1(4), s 1(5), s 2(1), s 2(2ZB), s 2(3), s 2(4), s 2(5), s 3(1), s 4(1), s 4(3), s 4(4), s 4(6C), s 4(6E), s 4A(2), s 4A(3), s 4A(6), s 4A(7), s 4B(3), s 4B(4), s 4B(7), s 4B(8), s 4B(9), s 4B(10), s 4B(11), s 4B(13), s 4C(8), s 4C(11), s 5(1), s 5(4), s 5(5), s 6(5), s 6A(1), s 6A(3), s 6A(5), s 6A(6), s 7(1), s 7(2B), s 8(2), s 9(1A), s 9(2), s 9A(1), s 9A(1A), s 9A(2), s 9A(5), s 9A(6), s 9A(8), s 9A(9), s 9A(10), s 9B(1), s 9B(2), s 9B(3), s 9B(5), s 9B(6), s 9B(7), s 9B(9), s 10(3), s 10(5), s 10(7), s 10(7A), s 10(7B), s 10(12), s 10ZA(1), s 10ZA(1A), s 10ZA(2), s 10ZA(4), s 10ZA(6), s 10ZB(1), s 10ZB(2), s 10ZB(3), s 10ZBA(1), s 10ZBA(3), s 10ZBA(4), s 10ZBA(6), s 10ZC(2), s 10ZC(3), s 10ZC(8), s 10ZC(10), s 10A(2), s 10A(4), s 10A(5), s 10A(6), s 11(1), s 11(3), s 11(4), s 11(5A), s 11(5C), s 11A(1), s 11A(2), s 12(1), s 12(8), s 13(2), s 13(5), s 13(6), s 13A(2), s 13A(3), s 13A(4), s 13A(5), s 13A(6), s 13A(7), s 13A(8), s 13A(9), s 13A(10), s 13A(11), s 13A(12), s 13A(13), s 14(1), s 14(3), s 14(4), s 14A(1A), s 14A(2), s 14A(6), s 14A(7), s 14A(8), s 14B(3), s 15(3ZA), s 15(5), s 16(2), s 16(3), s 18A(2), s 19A(1), s 19B (single paragraph) | none | definitions, counting and deeming rules, conditions, the Act's own figures, limits on a power or privilege stated elsewhere, and allocation rules whose duty is created by another subsection | - | the L4 rules named in the coverage table |

## Marginal readings for a lawyer (ssc1)

The rule of 2026-10-29 (FALSE only where the text says no in its own words; otherwise NOTHING) needs a lawyer's reading at the places listed here. The module comments cite the readings as M1, M1(a), M2 and M3: M1 is that "where" is read like "when", so a case outside it is NOTHING (a case of reading (b)); M1(a) is reading (a) below; M2 and M3 are this encoding's own, where the words needed a decision of the same kind. Each table lists every branch that rests on the reading, with the words relied on, and each reading states the other reading under its heading. These are my readings, not a lawyer's.


The modules carry 85 FALSE-kind branches (the text says no in its own words) and 162 NOTHING-kind branches (not covered).
FALSE-kind by basis: M1(a): "only with a view to" is read as a necessary condition whose failure is the text's no: 1; M1(a): a failed "if" or condition counts as the text's no: 26; M3: a defining "is" is read like "means": 2; definition ("means"): 20; definition by cross-reference ("has the meaning ... in"): 3; flat negative (counts as the text saying no): 30; flat negative (counts as the text saying no) ("must be lower"): 1; passes on a bar's own no (the bar has its own row): 2.
NOTHING-kind by why: includes: 14; limited by its own wording: 86; list not closed: 3; points outside the text: 39; silent: 19; undefined term: 1.
Of the FALSE-kind branches, 58 rest on reading (a), 2 on M3 and 25 are not marginal at all (the text defines, or an earlier row carries the no).
Of the NOTHING-kind branches, 86 rest on reading (b) and 3 on M2.

### Reading (a): a failed "if" counts as the text's no, and a flat negative counts as the text saying no

The other reading: "if A then B" does not itself say "if not A then not B", so a failed condition is silent (NOTHING), and a flat negative ("no", "shall not", "must not") would be read as a no only for the case it names.

| module:line | rule | words relied on | basis |
|---|---|---|---|
| prelim:144 | `s 1(6)(a) the person is liable to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` | "No person shall be liable to pay Class 1, Class 1A , Class 1B or Class 2 contributions unless he fulfils prescribed conditions as to residence or presence in Great Britain" | flat negative (counts as the text saying no) |
| prelim:153 | `s 1(6)(aa) the person is treated under section 11(5B) as having actually paid Class 2 contributions` | "No person shall ... be treated under section 11(5B) as having actually paid Class 2 contributions unless he fulfils such conditions" | flat negative (counts as the text saying no) |
| prelim:162 | `s 1(6)(b) the person is entitled to pay Class 3 contributions` | "No person shall ... be entitled to pay Class 3 contributions unless he fulfils such conditions" | flat negative (counts as the text saying no) |
| prelim:179 | `s 1(6)(c) the person is entitled to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` | "No person shall ... be entitled to pay Class 1, Class 1A , Class 1B or Class 2 contributions other than those which he is liable to pay, except so far as he is permitted by regulations to pay them" | flat negative (counts as the text saying no) |
| prelim:596 | `s 4B(5) subsection (2) authorises regulations that have effect in relation to the time` | "nothing in subsection (2) authorises regulations to be made which have effect in relation to any time before 2nd December 2004" | flat negative (counts as the text saying no) |
| prelim:689 | `s 4C(4) regulations under subsection (1) may have effect in relation to the time` | "must not have effect in relation to any time before 2nd December 2004" | flat negative (counts as the text saying no) |
| prelim:707 | `s 4C(7) the operative provisions are to be read with the modifications necessary to prevent that effect` | "If (ignoring this subsection) the operative provisions would directly or indirectly have effect in any case so as (a) to remove ... or (b) to reduce ..., those provisions are to be read with such modifications" | M1(a): a failed "if" or condition counts as the text's no |
| class1:141 | `s 6(1)(a) a primary Class 1 contribution is payable in accordance with sections 6 and 8` | "a primary Class 1 contribution shall be payable ... if the amount paid exceeds the current primary threshold (or the prescribed equivalent)" "if" | M1(a): a failed "if" or condition counts as the text's no |
| class1:161 | `s 6(1)(b) a secondary Class 1 contribution is payable in accordance with sections 6 and 9` | "a secondary Class 1 contribution shall be payable ... if the amount paid exceeds the current secondary threshold (or the prescribed equivalent)" | M1(a): a failed "if" or condition counts as the text's no |
| class1:172 | `s 6(2) a primary or secondary Class 1 contribution is payable in respect of the earnings` | "No primary or secondary Class 1 contribution shall be payable in respect of earnings if a Class 1B contribution is payable in respect of them" | flat negative (counts as the text saying no) |
| class1:188 | `s 6(3) a primary Class 1 contribution is payable in respect of the earnings` | "no primary Class 1 contribution shall be payable in respect of earnings paid to or for the benefit of an employed earner after he attains pensionable age" | flat negative (counts as the text saying no) |
| class1:370 | `s 6A(5) section 6A applies in relation to the earnings` | "nothing in this section applies in relation to earnings paid to or for the benefit of an employed earner after he attains pensionable age" | flat negative (counts as the text saying no) |
| class1:476 | `s 9B(2) the earner is a relevant apprentice` | "An earner is a “relevant apprentice” ... if the earner ... (b) is employed, in the employment, as an apprentice" | M1(a): a failed "if" or condition counts as the text's no |
| class1:503 | `s 9A(1) section 9A applies to the earnings` | "But this section does not apply to those earnings so far as section 9B ... applies to them" | flat negative (counts as the text saying no) |
| class1:506 | `s 9A(1) section 9A applies to the earnings` | "this section applies to the earnings ... if the earner falls within an age group specified in column 1" | M1(a): a failed "if" or condition counts as the text's no |
| class1:588 | `s 9A(5) the percentage may be specified for an added age group` | "A percentage specified under subsection (4)(a) must be lower than the secondary percentage" | flat negative (counts as the text saying no) ("must be lower") |
| class1a1b:57 | `s 10(1A) a Class 1A contribution is payable for the tax year in respect of the termination award` | "A Class 1A contribution is payable for a tax year ... if and so far as (a) that amount counts as employment income ... and (b) the earner is chargeable to income tax on that amount" | M1(a): a failed "if" or condition counts as the text's no |
| class1a1b:65 | `s 10(1B) a Class 1A contribution is payable under subsection (1A) in respect of the amount` | "No Class 1A contribution is payable under subsection (1A) in respect of an amount so far as it is an amount of earnings in respect of which Class 1 contributions are payable" | flat negative (counts as the text saying no) |
| class1a1b:75 | `s 10(1C) a Class 1A contribution is payable under subsection (1A)` | "No Class 1A contribution is payable under subsection (1A) unless the employment which is terminated is employed earner's employment" | flat negative (counts as the text saying no) |
| class1a1b:158 | `s 10(6) a Class 1A contribution is payable in respect of the general earnings` | "No Class 1A contribution shall be payable for any tax year in respect of so much of any general earnings as are taken ... to be included in a PAYE settlement agreement" | flat negative (counts as the text saying no) |
| class1a1b:232 | `s 10ZA(1) section 10ZA applies` | "(1A) This section does not apply if the benefit is a sporting testimonial payment" | flat negative (counts as the text saying no) |
| class1a1b:253 | `s 10ZA(2) the amount of the payment is treated as general earnings consisting in the provision of a benefit to the earner in that tax year` | "For the purposes of this Act if (a) ... and (b) ..., the amount of the payment shall be treated as if it were general earnings" | M1(a): a failed "if" or condition counts as the text's no |
| class1a1b:266 | `s 10ZA(4) subsection (3) applies in the case of a Class 1A contribution for the tax year` | "only if the person providing the benefit in question gives notice in writing" | M1(a): a failed "if" or condition counts as the text's no |
| class1a1b:270 | `s 10ZA(4) subsection (3) applies in the case of a Class 1A contribution for the tax year` | "only if ... on or before 6th July 2001" | M1(a): a failed "if" or condition counts as the text's no |
| class1a1b:285 | `s 10ZA(3) the liability falls on the person providing the benefit` | "Subsection (3) above applies in the case of a Class 1A contribution for the tax year beginning with 6th April 2000 only if ..." | M1(a): a failed "if" or condition counts as the text's no |
| class1a1b:371 | `s 10ZBA(4) the amount to cover tax is treated as general earnings consisting in the making of a sporting testimonial payment to the earner` | "Subsection (4) applies if" | M1(a): a failed "if" or condition counts as the text's no |
| class1a1b:419 | `s 10ZC(5) regulations under section 10ZC may have effect in relation to the time` | "must not have effect in relation to any time before 2nd December 2004" | flat negative (counts as the text saying no) |
| class1a1b:431 | `s 10ZC(7) regulations under section 10ZC may have that effect` | "Regulations under this section (a) may not impose any liability to pay a Class 1A contribution, and (b) may not increase the amount of any Class 1A contribution" | flat negative (counts as the text saying no) |
| class1a1b:486 | `s 10A(4) the general earnings are chargeable emoluments` | "General earnings are chargeable emoluments ... if, apart from section 6(2) or 10(6) above, the person accountable ... would be liable or entitled to pay secondary Class 1 contributions or Class 1A contributions in respe | M1(a): a failed "if" or condition counts as the text's no |
| class1a1b:498 | `s 10A(5) the general earnings are taken to be included in the PAYE settlement agreement` | "those general earnings shall not be taken to be included in the PAYE settlement agreement" | flat negative (counts as the text saying no) |
| class23:29 | `s 11(1) section 11 applies` | "This section applies if an earner is in employment as a self-employed earner in a tax year" | M1(a): a failed "if" or condition counts as the text's no |
| class23:68 | `s 11(7) a Class 2 contribution is to be paid or treated as paid in respect of the week` | "No Class 2 contributions are to be paid or treated as paid under this section in respect of any week ... (a) before that in which the earner attains the age of 16, or (b) after that in which the earner attains pensionab | flat negative (counts as the text saying no) |
| class23:88 | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | "No Class 2 contributions are to be paid or treated as paid under this section" | flat negative (counts as the text saying no) |
| class23:89 | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | "This section applies if an earner is in employment as a self-employed earner in a tax year" | flat negative (counts as the text saying no) |
| class23:112 | `s 11(6) the earner may pay a Class 2 contribution in respect of the week` | "No Class 2 contributions are to be paid ... in respect of any week" | flat negative (counts as the text saying no) |
| class23:113 | `s 11(6) the earner may pay a Class 2 contribution in respect of the week` | "This section applies if an earner is in employment as a self-employed earner in a tax year" | flat negative (counts as the text saying no) |
| class23:116 | `s 11(6) the earner may pay a Class 2 contribution in respect of the week` | "If the earner does not have relevant profits of, or exceeding, the small profits threshold, the earner may pay" "if" | flat negative (counts as the text saying no) |
| class23:240 | `s 13(1) the person is entitled to pay a Class 3 contribution` | "The Treasury shall by regulations provide for earners and others, if over the age of 16, to be entitled" | M1(a): a failed "if" or condition counts as the text's no |
| class23:255 | `s 13(2) payment of the Class 3 contribution is allowed` | "Payment of Class 3 contributions shall be allowed only with a view to enabling the contributor to satisfy ... conditions of entitlement to benefit by acquiring the requisite earnings factor" | M1(a): "only with a view to" is read as a necessary condition whose failure is the text's no |
| class23:337 | `s 13A(3) the person is entitled to pay a contribution under section 13A for the tax year` | "A person is not entitled to pay contributions in respect of more than 6 tax years under this section" | flat negative (counts as the text saying no) |
| class23:362 | `s 13A(4) the person is entitled to pay a contribution under section 13A on the day` | "A person is not entitled to pay any contribution under this section after the end of 6 years beginning with the day on which he attains pensionable age" | flat negative (counts as the text saying no) |
| class23:375 | `s 13A(6) the first condition is satisfied` | "A person is an eligible person if the following conditions are satisfied. The first condition is that the person attained or will attain pensionable age in the period" | M1(a): a failed "if" or condition counts as the text's no |
| class23:392 | `s 13A(8) the year is a year to which subsection (8) applies` | "This subsection applies if (a) ... and (b) ... not less than the qualifying earnings factor for that year" | M1(a): a failed "if" or condition counts as the text's no |
| class23:419 | `s 13A(10) the year is a year to which subsection (10) applies` | "This subsection applies ... if the year is one in which the person was precluded from regular employment by responsibilities at home" | M1(a): a failed "if" or condition counts as the text's no |
| class23:428 | `s 13A(7) the second condition is satisfied` | "The second condition is that there are at least 20 tax years each of which is a year to which subsection (8) or (10) applies" | M1(a): a failed "if" or condition counts as the text's no |
| class23:437 | `s 13A(11) the third condition applies` | "The third condition applies only if the person attained or will attain pensionable age before 6th April 2010" | M1(a): a failed "if" or condition counts as the text's no |
| class23:451 | `s 13A(12) the third condition is satisfied` | "That condition is that (a) ... and (b) ... not less than the qualifying earnings factor for that year" | M1(a): a failed "if" or condition counts as the text's no |
| class23:475 | `s 13A(5) the person is an eligible person` | "A person is an eligible person if the following conditions are satisfied" | M1(a): a failed "if" or condition counts as the text's no |
| class23:476 | `s 13A(5) the person is an eligible person` | the same, as to the third condition | M1(a): a failed "if" or condition counts as the text's no |
| class23:492 | `s 13A(1) an eligible person is entitled to pay a Class 3 contribution in respect of the missing year, having regard to subsections (3) and (4)` | "A person is not entitled to pay contributions in respect of more than 6 tax years under this section" | flat negative (counts as the text saying no) |
| class23:493 | `s 13A(1) an eligible person is entitled to pay a Class 3 contribution in respect of the missing year, having regard to subsections (3) and (4)` | "not entitled to pay any contribution under this section after the end of 6 years" | flat negative (counts as the text saying no) |
| class23:511 | `s 14(1) the person is entitled to pay a Class 3 contribution for the tax year` | "No person shall be entitled to pay a Class 3 contribution in respect of any tax year if his earnings factor ... is equal to or exceeds the qualifying earnings factor for that year" | flat negative (counts as the text saying no) |
| class23:578 | `s 14A(2) the person is eligible to pay a Class 3A contribution` | "A person is eligible to pay a Class 3A contribution if the person (a) ... or (b) ..." | M1(a): a failed "if" or condition counts as the text's no |
| class23:606 | `s 14A(5) the person may pay a Class 3A contribution on this occasion` | "may not obtain more than the maximum number of units of additional pension" | flat negative (counts as the text saying no) |
| class23:634 | `s 14B(3) the person is treated as never having had the unit of additional pension` | "A person is to be treated as never having had a unit of additional pension if the Class 3A contribution paid in respect of it is repaid" | M1(a): a failed "if" or condition counts as the text's no |
| class4:109 | `s 15(3A) Class 4 contributions are payable by the member of the limited liability partnership` | "Class 4 contributions shall be payable by him if they would be payable were the trade or profession carried on in partnership by the members" | M1(a): a failed "if" or condition counts as the text's no |
| class4:225 | `s 18A(3) regulations under section 18A may have effect from the day` | "they may not have effect before the beginning of the tax year in which they are made" | flat negative (counts as the text saying no) |
| general:68 | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` | "the earner shall, except in such circumstances as may be prescribed, be treated" | M1(a): a failed "if" or condition counts as the text's no |

### M3: a defining "is" is read like "means" (this encoding's own extension of reading (a))

The other reading: "is" in a definition (as in "A missing year is a tax year ...", "the year of assessment ... is the year ... which consists of the same period") names the case without closing it, so a case outside it is NOTHING.

| module:line | rule | words relied on |
|---|---|---|
| class23:328 | `s 13A(2) the tax year is a missing year` | "A missing year is a tax year not earlier than 1975-76 in respect of which the person would under regulations under section 13 be entitled to pay Class 3 contributions but for a limit on the time" "is" "means" |
| class4:119 | `s 15(5) the year of assessment corresponds to the tax year` | "the year of assessment which corresponds to a tax year is the year of assessment ... which consists of the same period as that tax year" "is" "means" |

### M2: a list the text does not close with "only" gives NOTHING for an item outside it

The other reading: "are" or "means" followed by a list closes the list, so an item outside it would be JUST FALSE.

| module:line | rule | why |
|---|---|---|
| prelim:97 | `s 1(4) Schedule 1 has effect with respect to the computation, collection and recovery of the class` | list not closed |
| prelim:725 | `s 4C(8)(a) the provision is one of the operative provisions` | list not closed |
| class1:358 | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | list not closed |

### Reading (b): a grant or prohibition limited by its own wording does not count as a no (the answer is NOTHING)

The other reading: a limit such as "when", "where", "in respect of any week", a stated period or a named complement makes everything outside it a no (JUST FALSE).

| module:line | rule | why not covered | words |
|---|---|---|---|
| prelim:143 | `s 1(6)(a) the person is liable to pay a Class 1, Class 1A, Class 1B or Class 2 contribution` | limited by its own wording | "unless" states a necessary condition; fulfilling it does not make the person liable |
| prelim:152 | `s 1(6)(aa) the person is treated under section 11(5B) as having actually paid Class 2 contributions` | limited by its own wording | "unless" states a necessary condition only |
| prelim:161 | `s 1(6)(b) the person is entitled to pay Class 3 contributions` | limited by its own wording | "unless" states a necessary condition only; sections 13 and 13A say who may pay |
| prelim:246 | `s 2(3) the person is treated as an employed earner for all purposes of this Act` | limited by its own wording | "Where a person is to be treated ..." grants for that case only |
| prelim:273 | `s 2(5) the person is treated as a self-employed earner as respects the week` | limited by its own wording | "as respects any week during any part of which he is such an earner" |
| prelim:330 | `s 4(1)(a) the sum is treated as remuneration derived from employed earner's employment` | limited by its own wording | the treatment is of "any sum paid ... in satisfaction ... of any entitlement" |
| prelim:345 | `s 4(1)(b) the sickness payment is treated as remuneration derived from employed earner's employment` | limited by its own wording | paragraph (b) treats "any sickness payment made (i) ... and (ii) ..."; a payment outside both limbs is not addressed |
| prelim:369 | `s 4(4)(a) the amount treated as remuneration derived from employed earner's employment` | limited by its own wording | the treatment is of "the amount of any gain ... in respect of which an amount counts as employment income of the earner under section 476" |
| prelim:384 | `s 4(4)(b) the sum is treated as remuneration derived from an employed earner's employment` | limited by its own wording | "any sum paid (or treated as paid) ... which is chargeable to tax by virtue of section 225 or 226" |
| prelim:399 | `s 4(6C)(b) the regulations may prescribe the amount as an equivalent of the contributions limit` | limited by its own wording | the power is to prescribe "an amount which exceeds by not more than £1" the arithmetical equivalent; "may prescribe ... not more than" limits a grant and is no flat negative, and (b) has no "only" (th |
| prelim:414 | `s 4(6E) the meaning of the expression in subsection (6A)` | limited by its own wording | "Expressions which are used in subsection (6A) and the benefits code" |
| prelim:435 | `s 4A(1) the regulations may treat relevant payments or benefits as earnings paid to the worker in respect of an employed earner's employment` | limited by its own wording | the power is given "where" all three conditions hold; outside them the section is silent |
| prelim:597 | `s 4B(5) subsection (2) authorises regulations that have effect in relation to the time` | limited by its own wording | from 2 December 2004 subsection (2) authorises only "if it appears to the Treasury to be expedient" |
| prelim:630 | `s 4B(8) how the reference in the relevant contributions legislation is read` | limited by its own wording | subsections (8) and (9) apply "In such a case" |
| prelim:636 | `s 4B(8) how the reference in the relevant contributions legislation is read` | limited by its own wording | "in so far as they so relate" |
| prelim:652 | `s 4B(9) the matter is to be redetermined by reference to the revised earnings` | limited by its own wording | subsection (9) speaks of "any matter which ... has been determined" by that reference |
| prelim:690 | `s 4C(4) regulations under subsection (1) may have effect in relation to the time` | limited by its own wording | from 2 December 2004 the text says "may be made so as to have retrospective effect" and no more; the grant is of RETROSPECTIVE effect and this function holds only the time, not the day the regulations |
| class1:120 | `s 6(1) the earnings fall within the opening words of subsection (1)` | limited by its own wording | "the current" threshold is that of the tax year of the tax week; other limits were supplied |
| class1:121 | `s 6(1) the earnings fall within the opening words of subsection (1)` | limited by its own wording | "Where ... an earner over the age of 16"; the case of an earner not over 16 is outside the opening words |
| class1:122 | `s 6(1) the earnings fall within the opening words of subsection (1)` | limited by its own wording | "in respect of any one employment of his which is employed earner’s employment" |
| class1:142 | `s 6(1)(a) a primary Class 1 contribution is payable in accordance with sections 6 and 8` | limited by its own wording | outside the opening words of subsection (1) |
| class1:162 | `s 6(1)(b) a secondary Class 1 contribution is payable in accordance with sections 6 and 9` | limited by its own wording | outside the opening words of subsection (1) |
| class1:173 | `s 6(2) a primary or secondary Class 1 contribution is payable in respect of the earnings` | limited by its own wording | the bar is for the case where a Class 1B contribution is payable; otherwise the subsection is silent |
| class1:186 | `s 6(3) a primary Class 1 contribution is payable in respect of the earnings` | limited by its own wording | the bar is on earnings "paid ... after he attains pensionable age" |
| class1:314 | `s 6A(1) section 6A applies to the earnings` | limited by its own wording | "This section applies where ... the amount paid (a) is not less than the current lower earnings limit ... but (b) does not exceed the current primary threshold" |
| class1:315 | `s 6A(1) section 6A applies to the earnings` | limited by its own wording | outside the opening words of subsection (1) |
| class1:348 | `s 6A(2) the earner is treated as having actually paid a primary Class 1 contribution for the week` | limited by its own wording | "This section applies where" the opening conditions hold |
| class1:368 | `s 6A(5) section 6A applies in relation to the earnings` | limited by its own wording | the bar is on earnings "paid ... after he attains pensionable age" |
| class1:412 | `s 7(1) who the secondary contributor is` | limited by its own wording | subsection (1) speaks of an earner under a contract of service and an earner in an office |
| class1:454 | `s 8(1) the amount of the primary Class 1 contribution` | limited by its own wording | "Where a primary Class 1 contribution is payable as mentioned in section 6(1)(a)" |
| class1:488 | `s 9B(1) section 9B applies to the earnings` | limited by its own wording | "Where a secondary Class 1 contribution is payable as mentioned in section 6(1)(b)" |
| class1:502 | `s 9A(1) section 9A applies to the earnings` | limited by its own wording | "Where a secondary Class 1 contribution is payable as mentioned in section 6(1)(b)" |
| class1:565 | `s 9(1) the amount of the secondary Class 1 contribution` | limited by its own wording | "Where a secondary Class 1 contribution is payable as mentioned in section 6(1)(b)" |
| class1:599 | `s 9A(6) the person is regarded as liable to pay a secondary Class 1 contribution` | limited by its own wording | "still ... even though the amount of the contribution is £0 because the age-related secondary percentage is 0%" |
| class1:628 | `s 9B(3) the person is regarded as liable to pay a secondary Class 1 contribution` | limited by its own wording | "still ... even if the amount of the contribution is £0 because this section applies to the earnings" |
| class1a1b:43 | `s 10(1) a Class 1A contribution is payable for the tax year` | limited by its own wording | "Where" all four conditions hold a Class 1A contribution "shall be payable"; the subsection is silent outside them |
| class1a1b:66 | `s 10(1B) a Class 1A contribution is payable under subsection (1A) in respect of the amount` | limited by its own wording | the bar is for the amount "so far as" it is Class 1 earnings |
| class1a1b:74 | `s 10(1C) a Class 1A contribution is payable under subsection (1A)` | limited by its own wording | "unless" states a necessary condition only |
| class1a1b:119 | `s 10(3A) who pays the Class 1A contribution payable under subsection (1A)` | limited by its own wording | "A Class 1A contribution payable under subsection (1A) is payable by the person who ..." |
| class1a1b:138 | `s 10(4) the amount of the Class 1A contribution payable under subsection (1)` | limited by its own wording | the amount is that of a contribution "payable under subsection (1)" |
| class1a1b:149 | `s 10(4A) the amount of the Class 1A contribution payable under subsection (1A)` | limited by its own wording | the amount is that of a contribution "payable under subsection (1A)" |
| class1a1b:159 | `s 10(6) a Class 1A contribution is payable in respect of the general earnings` | limited by its own wording | the bar is for general earnings taken to be included in a PAYE settlement agreement |
| class1a1b:199 | `s 10(7) the amount of the general earnings received` | limited by its own wording | subsections (7) and (7A) speak of a deduction "under any of the excluded provisions" |
| class1a1b:237 | `s 10ZA(1) section 10ZA applies` | limited by its own wording | "This section applies, where" all four conditions hold |
| class1a1b:251 | `s 10ZA(2) the amount of the payment is treated as general earnings consisting in the provision of a benefit to the earner in that tax year` | limited by its own wording | subsection (2) is in section 10ZA, which "applies, where" the four conditions of subsection (1) hold |
| class1a1b:271 | `s 10ZA(4) subsection (3) applies in the case of a Class 1A contribution for the tax year` | limited by its own wording | subsection (4) speaks of "the tax year beginning with 6th April 2000" only |
| class1a1b:284 | `s 10ZA(3) the liability falls on the person providing the benefit` | limited by its own wording | subsection (3) is within "This section applies, where" the conditions hold |
| class1a1b:320 | `s 10ZB(2) sections 10 and 10ZA have effect as if the employment were not lower-paid employment as a minister of religion` | limited by its own wording | "Where (a) ... and (b) ..." states the case; the subsection is silent otherwise |
| class1a1b:347 | `s 10ZBA(1) section 10ZBA applies` | limited by its own wording | "This section applies where" the three conditions hold |
| class1a1b:356 | `s 10ZBA(2) the liability falls on the controller of the sporting testimonial` | limited by its own wording | subsection (2) is within "This section applies where" the conditions hold |
| class1a1b:369 | `s 10ZBA(4) the amount to cover tax is treated as general earnings consisting in the making of a sporting testimonial payment to the earner` | limited by its own wording | subsection (3) is in section 10ZBA, which "applies where" the conditions of subsection (1) hold |
| class1a1b:380 | `s 10ZBA(5) the liability for the further payment falls on the controller of the sporting testimonial` | limited by its own wording | subsection (5) speaks of "any further sporting testimonial payment treated as made ... in accordance with subsection (4)" |
| class1a1b:389 | `s 10ZBA(6) the expression has the meaning it has in section 226E of ITEPA 2003` | limited by its own wording | "Expressions used in this section and section 226E" |
| class1a1b:420 | `s 10ZC(5) regulations under section 10ZC may have effect in relation to the time` | limited by its own wording | from 2 December 2004 the text says "may be made so as to have retrospective effect" and no more; the grant is of RETROSPECTIVE effect and this function holds only the time, not the day the regulations |
| class1a1b:443 | `s 10ZC(8)(a) the powers are without prejudice to the liability` | limited by its own wording | paragraph (a) saves a liability "which arises by virtue of any relevant retrospective tax provision" |
| class1a1b:477 | `s 10A(1) a Class 1B contribution is payable by the person for the tax year` | limited by its own wording | "Where for any tax year a person is accountable ... a Class 1B contribution shall be payable by him" |
| class1a1b:499 | `s 10A(5) the general earnings are taken to be included in the PAYE settlement agreement` | limited by its own wording | "Where (a) ... and (b) ..." states the case; the subsection is silent otherwise |
| class1a1b:523 | `s 10A(3) the amount of the Class 1B contribution` | limited by its own wording | the amount is that of the contribution payable "referred to in subsection (1)" |
| class23:69 | `s 11(7) a Class 2 contribution is to be paid or treated as paid in respect of the week` | limited by its own wording | the bar is for weeks before or after those; otherwise the subsection is silent |
| class23:91 | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | limited by its own wording | "in respect of each week in the relevant tax year that the earner is in the employment" |
| class23:93 | `s 11(5B) the earner is treated for relevant purposes as having actually paid a Class 2 contribution in respect of the week` | limited by its own wording | subsection (5B) applies to "an earner to whom this subsection applies"; (5A) names the earner with relevant profits of, or exceeding, the threshold and says no more |
| class23:115 | `s 11(6) the earner may pay a Class 2 contribution in respect of the week` | limited by its own wording | "in respect of any week in the relevant tax year that the earner is in the employment" |
| class23:166 | `s 12(1) section 12 applies to the contribution` | limited by its own wording | "This section applies to any Class 2 contribution under section 11(6) paid in respect of a week falling within a tax year earlier than the tax year in which it is paid" |
| class23:214 | `s 12(2) the amount of the late paid Class 2 contribution` | limited by its own wording | section 12 applies to a contribution under s 11(6) paid for a week in an earlier tax year |
| class23:254 | `s 13(2) payment of the Class 3 contribution is allowed` | limited by its own wording | "only with a view to" states a necessary condition; meeting it does not by itself allow the payment |
| class23:295 | `s 13(4) the amount of the Class 3 contribution for the earlier tax year` | limited by its own wording | subsection (4) speaks of "a tax year earlier than the tax year in which it is paid" |
| class23:338 | `s 13A(3) the person is entitled to pay a contribution under section 13A for the tax year` | limited by its own wording | the bar is on "more than 6 tax years"; within six the subsection is silent |
| class23:363 | `s 13A(4) the person is entitled to pay a contribution under section 13A on the day` | limited by its own wording | the bar is on payments after that day; up to it the subsection is silent |
| class23:417 | `s 13A(10) the year is a year to which subsection (10) applies` | limited by its own wording | "(in the case of a person who attained or will attain pensionable age before 6th April 2010)" |
| class23:495 | `s 13A(1) an eligible person is entitled to pay a Class 3 contribution in respect of the missing year, having regard to subsections (3) and (4)` | limited by its own wording | "An eligible person is entitled ... to pay Class 3 contributions in respect of a missing year", subject to prescribed conditions; the subsection grants to that person for that year and says no more |
| class23:512 | `s 14(1) the person is entitled to pay a Class 3 contribution for the tax year` | limited by its own wording | a prohibition "if" the earnings factor reaches the qualifying level does not grant a right below it (below the level the prohibition does not apply, which is not a grant); "regulations may provide for |
| class23:533 | `s 14(3) the contribution is treated as not having been paid for the purpose of determining entitlement to any benefit` | limited by its own wording | "nothing in this subsection shall be taken to imply that any other repayable contributions are to be treated for the purposes of benefit as having been paid" |
| class23:590 | `s 14A(1) the person is entitled to pay a Class 3A contribution on the day` | limited by its own wording | "An eligible person is entitled to pay a Class 3A contribution before the cut-off date"; a person not eligible, or a payment on or after the cut-off date, is outside the grant |
| class23:608 | `s 14A(5) the person may pay a Class 3A contribution on this occasion` | limited by its own wording | subsection (5) speaks of paying "on more than one occasion"; the first payment is subsection (1)'s |
| class4:36 | `s 15(1) Class 4 contributions are payable for the tax year in respect of the profits` | limited by its own wording | Class 4 contributions "shall be payable ... in respect of all profits which" meet (a), (b) and (c); paragraph (c), "are not profits of a trade, profession or vocation carried on wholly outside the Uni |
| class4:50 | `s 15(2) the person is liable to pay the Class 4 contribution` | limited by its own wording | "shall be payable ... by the person on whom the income tax is (or would be) charged"; the subsection does not say another person is not liable |
| class4:96 | `s 15(3) the amount of the Class 4 contribution for the tax year` | limited by its own wording | the amount is that of a Class 4 contribution "under this section" |
| class4:107 | `s 15(3A) Class 4 contributions are payable by the member of the limited liability partnership` | limited by its own wording | "Where income tax is (or would be) charged on a member of a limited liability partnership" |
| class4:143 | `s 16(1) the provision of the Income Tax Acts applies, with the necessary modifications, in relation to Class 4 contributions` | limited by its own wording | subsection (1) speaks of "the provisions of the Income Tax Acts" |
| class4:154 | `s 16(3) Schedule 2 has effect in relation to the class of contribution` | limited by its own wording | "Schedule 2 to this Act has effect ... in relation to Class 4 contributions" |
| class4:175 | `s 18(1) the regulations may make the earner liable to pay a Class 4 contribution in respect of the earnings` | limited by its own wording | the power is given "where" (a), (b) and (c) hold; (c) is "exceeds", so a total equal to the figure is outside it |
| class4:194 | `s 18(1A) the amount of the Class 4 contribution payable by virtue of regulations under section 18` | limited by its own wording | the amount is that of a contribution "payable by virtue of regulations under this section" |
| class4:226 | `s 18A(3) regulations under section 18A may have effect from the day` | limited by its own wording | "Regulations under this section may have retrospective effect" and no more; the grant is of RETROSPECTIVE effect and this function holds the start of the tax year of making, not the day the regulation |
| general:37 | `s 19A(1) section 19A applies` | limited by its own wording | "This section applies where" (a), (b) and (c); the section is silent on payments outside them |
| general:66 | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` | limited by its own wording | the subsection is for the cases in which section 19A applies |
| general:67 | `s 19A(2) the earner is treated as if the earnings were derived from employed earner's employment` | limited by its own wording | "After the end of year 2" |

### Not marginal: FALSE-kind branches where the text defines in its own words, or an earlier row carries the no

| module:line | rule | words relied on | basis |
|---|---|---|---|
| prelim:200 | `s 2(1)(a) the person is an employed earner` | "“employed earner” means a person who is gainfully employed in Great Britain either under a contract of service, or in an office (including elective office) with ... earnings" | definition ("means") |
| prelim:216 | `s 2(1)(b) the person is a self-employed earner` | "“self-employed earner” means a person who is gainfully employed in Great Britain otherwise than in employed earner’s employment" | definition ("means") |
| prelim:356 | `s 4(3) the payment is a sickness payment` | "“sickness payment” means any payment made in respect of absence from work due to incapacity for work" | definition ("means") |
| prelim:457 | `s 4A(2)(a) who the intermediary is` | "“the intermediary” means" | definition ("means") |
| prelim:507 | `s 4A(6) the Part is among the applicable provisions of this Act` | "“the applicable provisions of this Act” means this Part of this Act and Parts II to V below" | definition ("means") |
| prelim:535 | `s 4A(6) the payments or benefits are relevant payments or benefits` | "“relevant payments or benefits” means payments or benefits of any specified description made or provided ... in connection with the performance by the worker of the services in question" | definition ("means") |
| prelim:544 | `s 4A(6) the description is specified` | "“specified” means prescribed by or determined in accordance with regulations under this section" | definition ("means") |
| prelim:577 | `s 4B(3) the power is a relevant power` | "A “relevant power” means a power to make regulations under any of the following provisions" | definition ("means") |
| prelim:678 | `s 4B(13) the thing is contributions legislation` | "“contributions legislation” means any Part of this Act or provision of such a Part" | definition ("means") |
| prelim:749 | `s 4C(11) the day is the commencement day` | "“the commencement day” means the day on which the National Insurance Contributions Act 2006 was passed" | definition ("means") |
| prelim:778 | `s 4C(11) the payment is a statutory payment` | "“statutory payment” means" "or any other payment prescribed" | definition ("means") |
| class1:230 | `s 6 the answer once a bar is taken into account` | the bar's own no, passed on; ss 1(6)(a), 6(2) and 6(3) carry the quoted words | passes on a bar's own no (the bar has its own row) |
| class1a1b:110 | `s 10(3) the payment is a relevant payment of earnings` | "“relevant payment of earnings” means a payment which for the purposes of Class 1 contributions is a payment of earnings made to or for the benefit of the earner in respect of the relevant employment" | definition ("means") |
| class1a1b:180 | `s 10(7B) the provision is an excluded provision` | "any provision of Chapter 2 of Part 5 of ITEPA 2003 (deductions for employee’s expenses), other than section 352" | definition ("means") |
| class1a1b:183 | `s 10(7B) the provision is an excluded provision` | "“excluded provision” means" | definition ("means") |
| class1a1b:212 | `s 10(12) the payment or benefit is a termination award` | "“termination award” means a payment or benefit received by an earner (or an earner's spouse, civil partner, blood relative or dependant) in connection with the termination of the earner's employment" | definition ("means") |
| class1a1b:295 | `s 10ZA(6) the person is a member of a person's family or household` | "references to a member of a person’s family or household shall be construed in accordance with section 721(5) of ITEPA 2003" | definition by cross-reference ("has the meaning ... in") |
| class1a1b:329 | `s 10ZB(3) the voucher is a non-cash voucher` | "“non-cash voucher” has the same meaning as in section 84 of ITEPA 2003" | definition by cross-reference ("has the meaning ... in") |
| class1a1b:404 | `s 10ZC(2) the provision is a relevant retrospective tax provision` | "“Relevant retrospective tax provision” means a provision of the Income Tax Acts which (a) has retrospective effect, and (b) affects the amount of general earnings" | definition ("means") |
| class1a1b:455 | `s 10ZC(10) the day is the commencement day` | "“the commencement day” means the day on which the National Insurance Contributions Act 2006 was passed" | definition ("means") |
| class23:44 | `s 11(3) the profits are relevant profits` | "“Relevant profits” means profits, from the employment, in respect of which Class 4 contributions are payable under section 15" | definition ("means") |
| class23:47 | `s 11(3) the profits are relevant profits` | the same definition | definition ("means") |
| class23:177 | `s 12(8) the contribution is an ordinary contribution` | "“ordinary contribution” means a contribution of the amount specified in section 11(6)" | definition ("means") |
| class23:522 | `s 13 the Class 3 contribution may be paid once the bars are taken into account` | a bar's own no, passed on; ss 1(6)(b) and 14(1) carry the quoted words | passes on a bar's own no (the bar has its own row) |
| class23:617 | `s 14A(7) the graduated retirement benefit is deferred` | "“deferred”, in relation to graduated retirement benefit, has the meaning given by section 36(4A) of the National Insurance Act 1965" | definition by cross-reference ("has the meaning ... in") |

### Reading a result: FALSE and NOTHING (ssc1)

Every rule in this part answers a `MAYBE` value, and the seat's questions pass it on unchanged.
- **JUST TRUE** is the text saying yes in its own words: a person "is" an employed earner when the definition is met; a Class 1 contribution "shall be payable" when the amount paid exceeds the threshold.
- **JUST FALSE** is the text saying no in its own words, and only that. In Part I it is: a definition that says "means" and the case is outside it (a person who is not gainfully employed in Great Britain is not an employed earner under s 2(1)(a), asserted); a flat negative (no Class 1 contribution where a Class 1B contribution is payable, s 6(2); no primary contribution on earnings paid after pensionable age unless regulations prescribe otherwise, s 6(3); no entitlement to pay Class 3 where the earnings factor already reaches the qualifying level, s 14(1)); and, on reading (a), a condition the text states with "if", "unless" or "only" and it fails. Each such branch carries a `-- FALSE-kind` comment quoting the words, and the marginal tables list those that rest on a reading.
- **NOTHING** is "not covered": the text does not decide. In Part I it is mostly "limited by its own wording" (a contribution payable "where" the conditions hold says nothing about a case outside them), then "points outside the text" (the condition is set by regulations, a Schedule or a section of another part), "silent", "includes" (earnings "includes" remuneration, so a payment that is not remuneration is not decided), "list not closed" and "undefined term". Each such branch carries a `-- NOTHING-kind` comment saying which; the counts are at the head of the marginal tables.
- **A caller must never turn NOTHING into FALSE.** In particular NOTHING from a "may pay" rule is not "may not pay".
- A bar (s 6(2), s 6(3)) answers JUST FALSE where it applies and NOTHING where it does not: it never says yes. The rule that combines a grant with its bars is a separate one (`s 6 a primary Class 1 contribution is payable, having regard to sections 1(6)(a), 6(2) and 6(3)`, its secondary twin, and for Class 3 `s 13 the Class 3 contribution may be paid once the bars are taken into account`).

## Seams (ssc1)

PLAN section 5 names the seams. These are the inputs ssc1 took (the asking rule, the answering section, the input name as it stands in the module, its type):

| id | asking rule (src) | answering section | input name | type |
|---|---|---|---|---|
| S8 | `s 6A(3)(b)` (src:270; the rules `s 6A(2)`, `s 6A(3)`) | ssc2 s 21(5A) | `s 21(5A) the provision is one mentioned in section 21(5A)(a) to (c)` | `BOOLEAN` |
| S9 | `s 13(2)` (src:526) | ssc2 s 22 | `s 22 the payment is with a view to acquiring the requisite earnings factor for the purposes described` | `BOOLEAN` |
| S10 | `s 14A(2)` (src:580-582) and `s 14A(8)` (src:590) | ssc3 s 55(3) | `s 55(3) the retirement pension is deferred` | `MAYBE BOOLEAN` |
| K2 over 16 | `s 5(5)` (src:245), `s 6(1)(a)` and `(b)` (src:248-250), `s 6A(1)` (src:261-263), `s 13(1)` (src:525) | keel s 173(a) | `s 173(a) the person is over 16` | `MAYBE BOOLEAN` |
| K2 under 25 | `s 9B(2)` (src:341-343) | keel s 173(a) | `s 173(a) the person is under 25` | `MAYBE BOOLEAN` |

Seams ssc1 answers for other parts (the function, its type):

| id | answering function | what it takes |
|---|---|---|
| S4 | `s 6 the earnings on which primary Class 1 contributions have been paid or treated as paid in the tax year` | a list of `s 6 Week of earnings` (fork F3) |
| S4 | `s 11 the number of weeks for which a Class 2 contribution was paid in the tax year` | a list of `s 11 Week of the tax year` |
| S4 | `s 13 the number of weeks for which a Class 3 contribution was paid in the tax year` | three numbers: weeks of the tax year for which Class 3 was paid, weeks of other tax years appropriated to the earnings factor of this year, and weeks of this year appropriated to another year |
| S26 | `s 5(1)(a) the lower earnings limit in force at the time in pounds`, and `s 5(1)(a)` primary threshold and upper earnings limit, `s 5(1)(b)` secondary threshold, each in pounds | the core's `Earnings limits` |

Seams I found that PLAN section 5 does not list (the answering section is the one the text cites):

| asking rule | answering section | input name | type |
|---|---|---|---|
| `s 2(4)` (src:46) | ssc4 s 95 (src:2290) | `s 95 the employment is treated as employed earner's employment for the purposes of industrial injuries benefit` | `MAYBE BOOLEAN` |
| `s 13A` and `s 14(1)` | s 122(1) (ssc5; the qualifying earnings factor) | `the qualifying earnings factor for the year` (`s 13A`), `the qualifying earnings factor for the tax year` (`s 14(1)`) | `NUMBER` |
| `s 13A(9)`, `s 13A(13)` | Schedule 3 (ssc8) | `the earnings factor derived as mentioned in subsection (9)` and `... (13)` | `NUMBER` |

The qualifying earnings factor is defined in s 122(1) (src:2604, in ssc5) as the lower earnings limit multiplied by 52; I did not read ssc5, so I took the figure as an input. The Schedule 3 row is an input because ssc1 cannot see the answering section; the lead may replace it at the merge.

## Findings: what the text turns out to say

1. **The table of s 9A(3) is not in this text.** `Here is the table—` (src:324) is followed at once by s 9A(4) (src:325). The age groups and their percentages are therefore inputs (`s 9A(2) the age-related secondary percentage` and the fact that the earner falls within an age group), and s 9A(3) has the disposition `repealed or blank in this text`.
2. **s 1(4)(a) has a blank where a class should stand.** The text reads `Classes 1, 1A, 1B, , 3 and 3A` (src:24); the gap falls where Class 2 would be. Schedule 1 is read as having effect for the classes the text names, and for Class 4 only as regulations under s 18 provide (src:25); `s 1(4)` answers NOTHING for Classes 2 and 4 (asserted in `ssc1-tests-prelim.l4`).
3. **The earnings limits have no figures in the text.** s 5(1) says the limits and thresholds "shall be the amounts specified for that year by regulations" (src:241), and s 5(2) and (3) show only dots (src:242-243). Every limit and threshold is an input, per tax year.
4. **s 6(1)(a) and s 6A meet at the primary threshold without a gap or an overlap.** s 6(1)(a) applies if the amount paid "exceeds" the primary threshold (src:249); s 6A(1) applies if the amount "is not less than" the lower earnings limit and "does not exceed" the primary threshold (src:262-263). At exactly the threshold the earner is treated as having paid a primary contribution and pays nothing; one penny more and 8% of the penny is payable. Asserted at the boundary.
5. **s 11(5A) and s 11(6) meet at the small profits threshold the same way.** s 11(5A) is for an earner with relevant profits "of, or exceeding," the threshold (src:483) and s 11(6) for an earner who does not have them (src:488). At exactly GBP 7,105 the earner is treated as having paid Class 2 and may not pay it voluntarily; at GBP 7,104.99 it is the other way round. Asserted.
6. **The late-payment periods of s 12 and s 13 differ by a year.** s 12(3)(a) applies to a Class 2 contribution paid "after the end of the tax year immediately following the contribution year" (src:511), so one paid in the second tax year after the week or later; s 13(6)(a) to a Class 3 contribution paid "after the end of the next tax year but one following the contribution year" (src:533), so one paid in the third year after or later.
7. **The Class 1A and Class 1B percentages are defined as the secondary percentage.** s 10(5) says "the Class 1A percentage" means "a percentage rate equal to the secondary percentage for the tax year in question" (src:377) and s 10A(6) says the same of "the Class 1B percentage" (src:472).
8. **s 4(1)(a) lists seven statutory payments, and the rendering has a gap in the list.** Sub-paragraph (iv) shows only dots (src:68), and (iii), (v) and (vi) carry `...` marks (src:67, 69, 70). The seven payments that remain (sick, maternity, paternity, adoption, shared parental, parental bereavement and neonatal care pay) are the seven constructors of the core's `Statutory payment` type, so the rule never meets a payment outside the list. A sum that is not paid in satisfaction of an entitlement answers NOTHING (limited by its own wording), not FALSE.
9. **A cut-off of 2 December 2004 recurs in three places.** s 4B(5) says nothing in subsection (2) authorises regulations "which have effect in relation to any time before 2nd December 2004" (src:173), and s 4C(4) and s 10ZC(5) say regulations "must not have effect in relation to any time before 2nd December 2004" (src:205, 446). Each rule is a function of the time and is asserted on 1 and 2 December 2004: JUST FALSE before, NOTHING from the date.
10. **s 15(3) states GBP 12,570 and GBP 50,270, and s 18(1)(c) and (1A) state them again** (src:611, 657, 660-661); s 18(1A) adds that "the figures specified in this subsection are subject to alteration under section 141 of the Administration Act" (src:662). The rules for ss 15(3) and 18(1A) take the figures as inputs. s 18(1)(c) says the total "exceeds" GBP 12,570, and at exactly GBP 12,570 `s 18(1)` answers NOTHING, not FALSE (asserted).
11. **s 15(1) is silent about profits that fail its conditions.** Class 4 contributions "shall be payable ... in respect of all profits which" meet three conditions (src:602-605); the rule answers JUST TRUE if all three hold and NOTHING otherwise (limited by its own wording), never JUST FALSE.
12. **s 2(1)(a) and (b) are written for one employment, not one person.** s 2(1)(b) says in terms that a self-employed earner may "also" be employed in employed earner's employment (src:36), and s 2(5) treats a person as a self-employed earner for a week in which they are one "without prejudice to his being also treated as an employed earner" (src:47). The rules are asked of one employment at a time.
13. **No section in lines 2-710 states a deadline for a duty or a consequence of default in its own words.** Contributions are "payable" or a person is "liable"; computation, collection and recovery are for Schedule 1 (s 1(4)). The one place that reaches penalties is s 16(1), which applies the Income Tax Acts, including Part X (penalties) of the Taxes Management Act 1970 and Schedules 24 to 26 to the Finance Act 2021, to Class 4 contributions (src:622-629), by reference to text outside the sources. So no regulative rule (`PARTY ... MUST ... WITHIN ... HENCE ... LEST`) is written: it would need a deadline or consequence the text does not give, and the brief says not to invent one. Every provision is a decision function over the facts.
14. **No Great Britain and Northern Ireland versions of one provision were met** (PLAN section 1.5). The Northern Ireland Contributions and Benefits Act is mentioned only in s 16(1) to (3) (src:629, 632, 634), as a second Act to which the same application is made.

## What the stable binary does not accept

The binary governs where the skills differ. Each item below was run on the stable binary (1.6.98) in a probe file on 2026-11-04, and the message quoted is what it printed.

**Loud** (a parse or type error; the file is refused):

- `a NOT EQUALS b`: parse error, `unexpected NOT`. Write `NOT (a EQUALS b)`.
- A postfix percentage as an unparenthesised argument: `f 8% 200` is a parse error, `unexpected 200`. Write `f (8%) 200`.
- A possessive after a function name: `min a limits's ...` is a parse error, `unexpected 's`. Write `min a (limits's ...)`.
- An `IF ... ELSE IF ... ELSE` chain inside a `WHERE` definition, laid out over several lines under `MEANS`, was refused with `incorrect indentation (got 12, should be greater than 12)`. The same choice written with `BRANCH`, `IF ... THEN ...` lines and an `OTHERWISE` line was accepted.
- A quoted multi-word type name must stay quoted in an expression: `` `Tax year` OF 2030 `` evaluates, and `Tax year OF 2030` is a parse error, `unexpected OF`.

**Silent** (exit code 0, or a plausible value; the answer is wrong or the failure is only in the text of the output):

- `l4 run` exits 0 when an assertion fails; the failure is a `DiagnosticSeverity_Error` block reading `assertion failed` in the output. Count `assertion satisfied` and look for `DiagnosticSeverity_Error`, as `check.sh` does, rather than trusting the exit code.
- `Date 29 2 2023` evaluates to 1 March 2023, and `Date 31 4 2024` to 1 May 2024, with no error. `` `add years` (Date 29 2 2020) 6 `` evaluates to 28 February 2026. So `s 13A(4)` does not add years to a 29 February (fork F4).

Not tried, per the brief: `REFUSE`, `BECAUSE`, section `GIVEN`, `TYPICALLY`, `YMD`.

## After the independent review (2026-11-04)

The independent reviewer's tests failed 28 assertions in this range. I re-read the source line and my function for each. One was the reviewer's slip (the cut-off day itself is not "before the cut-off date", s 14A(1)). The other 27 asked for JUST TRUE or JUST FALSE where my function answers NOTHING, and each rests on a NOTHING ground in the brief: a grant limited by "where", by a relative clause or by a stated date (reading (b)); the complement of a prohibition, which the text does not grant ("is not entitled", "No person shall", "may not", "only with a view to", "unless"); or "includes". No rule's answer changed on their account; the NOTHING-kind comments of s 5(5), s 14(1), s 15(1), s 4C(4), s 10ZC(5) and s 18A(3) now state the ground more exactly.
The review made me compare siblings, and eight branches turned out to answer NOTHING for a failed "if" or "except" where the same encoding answers JUST FALSE for the same shape elsewhere (marginal reading M1(a)). They now answer JUST FALSE, each with a FALSE-kind comment: s 4C(7); s 10ZA(2); s 10ZBA(4); s 11(1), and with it s 11(5B) and s 11(6) when section 11 does not apply; the "if" limb of s 15(3A) (its "Where" limb still gives NOTHING); and the "except" limb of s 19A(2). Eleven expectations of mine changed from NOTHING to JUST FALSE, and twelve assertions were added: eight to pin the new branches and four to pin the s 14A(1) cut-off day (strict "before").

## What `check.sh` prints

Baseline replaced: the run of 2026-11-04 before the triage below (15 modules, 768 satisfied, 0 failed, 0 refused, same on main). Before that first run the folder held only the keel's `ssc-core.l4` (0 assertions).
`L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` printed:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc1-cases-seat.l4                             0       138       0        0         0 |      0       138       0        0  same
ssc1-class1.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc1-class1a1b.l4                              0         0       0        0         0 |      0         0       0        0  same
ssc1-class23.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc1-class4.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc1-general.l4                                0         0       0        0         0 |      0         0       0        0  same
ssc1-prelim.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc1-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc1-tests-class1.l4                           0       134       0        0         0 |      0       134       0        0  same
ssc1-tests-class1a1b.l4                        0       116       0        0         0 |      0       116       0        0  same
ssc1-tests-class23.l4                          0       160       0        0         0 |      0       160       0        0  same
ssc1-tests-class4.l4                           0        48       0        0         0 |      0        48       0        0  same
ssc1-tests-general.l4                          0        16       0        0         0 |      0        16       0        0  same
ssc1-tests-prelim.l4                           0       168       0        0         0 |      0       168       0        0  same
TOTAL (15 modules)                             0       780       0        0           |      0       780       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs <raw text> ssc1-*.l4`: `srcrefs check: 481 src: lines, 190 runs, 195 locators, 0 problems`
`python3 -I srcrefs.py check --strict <raw text> ssc1-*.l4`: `srcrefs check: 481 src: lines, 190 runs, 195 locators, 0 problems`
Warning grep over the 14 `ssc1-*.l4` files, on the output of `l4 run`: 0 warnings, 0 errors, 0 matches of "is at the end of the file" or "follows code on its line".

## What the text does not answer, and what needs doing before relying on it

- The quoted lines are a converter rendering; check them against the official text.
- The seam inputs above are not yet connected to the answering sections (ssc2 s 21(5A) and s 22, ssc3 s 55(3), ssc4 s 95, ssc5 s 122(1), ssc8 Schedule 3, the keel's s 173(a)); the three seams PLAN section 5 does not list need the lead's decision.
- The age-related percentages of s 9A(3) are not in the text; no figure of any limit or threshold is (findings 1 and 3).
- Have a lawyer read the marginal tables: the FALSE and NOTHING boundary rests on readings (a), (b), M2 and M3.
- Schedule 1 holds the computation, collection and recovery of these contributions (s 1(4)); none of it is in ssc1.
- There is no seat for Class 1B or for anything addressed to the Crown.

