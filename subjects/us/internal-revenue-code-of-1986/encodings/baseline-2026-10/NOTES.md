# Internal Revenue Code of 1986: the individual's federal income tax for 2026 (baseline encoding)

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual taxpayer, with the design defaults ruled on 2026-10-18.
It contains no REFUSE. A case outside the encoding gets an explicit `not covered` answer naming the gap, and tests assert those answers.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
There was no pipeline, coverage table, independent test pass or human gate.
**Not for public use as advice.**

There was no earlier encoding of this Act to keep.

The encoding has two layers:

- **The core, `irc-individual.l4`, with the one calendar computation (the s 6013(b)(2)(A) three years) in `irc-dates.l4`.** It is seat-neutral and written in the Code's own actors and terms ("the taxpayer", "the spouse", "the individual", "the husband and wife"). Each computation is a function. Each duty or permission is a regulative rule (`DEONTIC`), so whoever holds the seat is a parameter of the rule.
- **The seat layer, `irc-seat.l4`.** It IMPORTs the core and asks the taxpayer's questions, each with `@export` and a seat-worded `@desc` on every input. The layer builds the core's records from plain answers, and every fixed value it supplies is commented. It restates no rule.

Each layer has its own case file: `irc-cases.l4` for the core and `irc-cases-seat.l4` for the seat layer.

## Edition

- **Statute.** The Office of the Law Revision Counsel's USLM text at release point **Public Law 119-121, current through 9 October 2026**, as deposited on 2026-10-19 in `../../registers/source-bundle/`. That release includes Pub. L. 119-21 (4 July 2025), whose amendments the text shows: s 1(j) without an end year, s 24(h)(2) at $2,200 and indexed by (i)(2), s 63(c)(7) at $15,750 and $23,625 indexed from 2026, the s 151(d)(5)(C) deduction for seniors, and ss 224 and 225. The provisions used, by file:

  | Deposited file | Provisions used |
  |---|---|
  | `usc26-ch1-schA-ptI.txt` | ss 1(a)-(d), 1(j), 2 |
  | `usc26-ch1-schA-ptIV-sptA-C.txt` | ss 24, 26(a), 31(a), 32 |
  | `usc26-ch1-schA-ptVI.txt` | s 55(b)(1), (d), only as a screen |
  | `usc26-ch1-schB-ptI-III.txt` | ss 61, 62(a), 63, 86 |
  | `usc26-ch1-schB-ptV-VII-sel.txt` | ss 151, 152, 164(f) |
  | `usc26-ch2.txt` | ss 1401, 1402(a), (b) |
  | `usc26-ch21-schA.txt` | s 3101, read only for what s 24(d)(2) counts |
  | `usc26-ss6012-6013-7703.txt` | ss 6012, 6013, 7703 |

- **Figures for 2026.** Rev. Proc. 2025-32, `irs-rev-proc-2025-32.txt`. These are sourced facts, not statute. They are written into the module as dated constants, and each comment cites its section of the Rev. Proc.:
  - s 4.01, Tables 1-4: the rate tables;
  - s 4.05: the CTC figures, $2,200 and $1,700;
  - s 4.06: the EITC table and the $12,200 limit;
  - s 4.10: the AMT exemption, phase-out and 28% point;
  - s 4.14: the standard deduction, the dependent's limit and the additional amounts;
  - s 4.23: $5,300.

  The EITC figures were read against the deposited text's broken table layout and checked against the statute. Each completed phaseout amount equals the threshold plus the maximum credit divided by the phaseout percentage; for example 31,160 + 4,427 / 15.98% = 58,863. They match `registers/annual-figures.json`.
- **The 2026 OASDI contribution and benefit base, $184,500.** This is from the SSA's notice at 90 FR 49047, deposited with the Social Security Act subject (`../../../social-security-act/registers/source-bundle/fr-2025-19763-ssa-cola-2026.txt`). s 1402(b)(1) borrows it from s 230 of that Act.
- **Only taxable year 2026.** Any other year answers `not covered`, because no other year's revenue procedure is deposited. The 2027 procedure had not been published by 2026-10-19.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `irc-individual.l4` | `irc-cases.l4` | 113 written, 113 satisfied |
| `irc-seat.l4` (with `irc-dates.l4`) | `irc-cases-seat.l4` | 53 written, 53 satisfied |

`l4 run` on all five files gives 0 errors and 0 warnings (2026-10-24). Run times on this machine: core 5 s, seat 12 s, core cases 15 s, seat cases 38 s. Only `irc-dates.l4` imports the daydate library. When the core imported it, its overloaded `PLUS` and `MINUS` made the stable `l4` take 35 s to check the core and over 100 s for the seat, before any evaluation. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked out by hand from the text, and the arithmetic is shown in the comment above each case. No value was copied from the encoding's output.

**Regulative rules (3)**, plus one party-selection function (s 6012(b): who makes the return) that the duty uses.

- The s 6012(a), (b), (d) duty to make a return.
- The s 6013(a) permission to make a joint return, which turns into a prohibition when a spouse was a nonresident alien.
- The s 6013(b)(1), (2)(A) permission to switch to a joint return within three years.

They are tested with `EVALTRACE … EQUALS FULFILLED` and with two `#TRACE`s that breach on purpose, each with an `-- expect:` comment:

- a return made without the tax-exempt interest, with no proper return by day 105;
- a joint return made with a nonresident-alien spouse.

The diagnostics show both breaches with the expected party and reason. The stable `l4` cannot assert a breach (see the brief), so these two are checked by reading the output.

Amounts are not rounded. The Code computes in dollars and cents. The rounding that the IRS tables apply comes from s 3 (tax tables) and s 32(f) (credit tables), and those tables are prescribed by the Secretary and not deposited (finding 7).

## Seat

**The individual taxpayer**: a US citizen or resident filing for the calendar year 2026, alone or with a spouse. The questions are the ones that person asks:

- "What is my filing status?"
- "Must I file a return?"
- "Does this person count as my dependent, for the child tax credit, the EITC and head of household?"
- "How much of my Social Security is taxable?"
- "How much self-employment tax do I owe?"
- "What does my 2026 return come to, and do I get a refund?"
- "Having filed separately, until when can we switch to a joint return?"

Most duties in these provisions sit on the individual already: "Returns … shall be made by … every individual" (s 6012(a)). The Secretary appears only through the figures the Secretary prescribes, and those come in as the Rev. Proc.'s dated constants.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** The Code, plus Rev. Proc. 2025-32 and the SSA notice's contribution and benefit base. Nothing else is brought in.
- **The actors the text names:**
  - the individual (the taxpayer);
  - the spouse, and "the husband and wife" together for s 6013;
  - the executor, administrator or other person charged with the decedent's property (s 6012(b)(1));
  - the authorized agent, committee, guardian or fiduciary of an individual unable to make a return (s 6012(b)(2)).
- **Judgments handed to others are asked as facts:**
  - the s 152(c)(4) tie-breaker ("someone else has the better claim");
  - whether the taxpayer is a dependent or qualifying child of another taxpayer;
  - "student" (s 152(f)(2));
  - "permanently and totally disabled" (s 22(e)(3));
  - "blind" (s 63(f)(4));
  - whether a social security number is "valid for employment" (s 24(h)(7)(B), s 32(m));
  - the bars in s 6013(b)(2)(B)-(D).
- **The Code's own definitions are worked out from facts:**
  - marital status (s 7703(a), (b));
  - surviving spouse and head of household (s 2);
  - qualifying child and qualifying relative, dependent (s 152);
  - the s 24(c) and s 32(c)(3) qualifying child;
  - the s 32 eligible individual;
  - earned income (s 32(c)(2));
  - gross income, AGI and taxable income (ss 61, 62, 63);
  - net earnings from self-employment and self-employment income (s 1402).
- **Borrowed terms are asked as amounts:**
  - wages (s 3121(a));
  - Title II benefits (s 86(d));
  - the taxable part of pensions (s 72, not deposited);
  - FICA withheld;
  - income tax withheld (chapter 24, not deposited);
  - itemized deductions;
  - the other s 62 and s 63(b) deductions (IRA, HSA, ss 199A, 224, 225 and the others).
- **One case** is one individual's taxable year: the calendar year, the spouse if there is one, and the people in the household.
- **The Code's own terms** are used, each with a gloss in the comment above the rule. The filing statuses carry the s 1 table headings: `joint return`, `surviving spouse`, `head of household`, `unmarried individual`, `married filing separately`.
- **Machinery is out:** the Secretary's powers to prescribe tables and regulations, inflation-adjustment formulas (their results come from the Rev. Proc.), and ss 24(j), (k).

**Fixed values in the seat layer.** Each is commented in the code.

- A person not filing jointly is taken to have a spouse who files a separate return.
- "The same household at the close of the year" is read from "lived with me in the last 6 months".
- A widowed person is taken to have been able to file jointly for the year of the death (s 2(a)(2)(B)).
- The household is built from counts:
  - a child under 17 is placed at age 10, and an older child at 18;
  - "more than half the year" is placed at 7 months and "all year" at 12;
  - children are taken to be US citizens and residents, unmarried and not self-supporting;
  - a parent lives elsewhere, and another relative lives with the taxpayer all year with no gross income.
- One question ("can someone else claim you?") stands for both "a dependent of another" and "a qualifying child of another" (s 32(c)(1)(B)).

## Read with

- **`../../../social-security-act/`.** This holds Title II benefits, which s 86 makes partly taxable, and the contribution and benefit base that s 1402(b)(1) borrows. Another agent is encoding the Social Security Act today and will link to this encoding's `How much of my Social Security is taxable` and to the core's `the social security benefits included in gross income under s 86 on … with modified AGI … base amount … adjusted base amount`. That function is written on plain numbers so it can be called without a return.
- **The state income tax baselines under `../../../<st>/`.** These start from federal AGI or borrow federal definitions. They take them as inputs and point here.
- The stable `l4` cannot IMPORT across folders, so these links are recorded here, not in code.

## Scope

**In:**

- **Rates and tax:** s 1(a)-(d) and (j)(1)-(2), with the s 1(j)(3)(B) tables for 2026 as a dated table.
- **Filing status:**
  - s 2(a)(1), (2) (surviving spouse);
  - s 2(b)(1), (2), (3)(A), and (3)(B)(i) (head of household);
  - s 2(c);
  - s 7703(a), (b);
  - s 6013(a)(1) and (d)(2), and (b)(1)-(2)(A) as a permission with its deadline.
- **Who must file:**
  - s 6012(a)(1)(A)-(D);
  - s 6012(b)(1), (2) as who makes the return;
  - s 6012(d) as part of what the duty requires.
- **Gross income to taxable income:**
  - s 61(a), s 62(a)(1) with s 164(f), s 63(a)-(f) and s 86(a)-(d)(2);
  - s 151(a)-(d), with the deduction for seniors in (d)(5)(C);
  - s 152(a)-(d)(2), except (d)(3), (d)(4), (d)(5) and (e).
- **Credits:**
  - s 24(a)-(d)(2), (h), with (i) through the Rev. Proc.;
  - s 26(a), s 31(a);
  - s 32(a)-(d), (i), (m) and (j) through the Rev. Proc.
- **Self-employment tax:** ss 1401(a), (b)(1)-(2) and 1402(a), (a)(12), (b).

**Out, each named by a `not covered` answer:**

- other taxable years;
- nonresident aliens (s 2(d), s 871, and s 6013(g), (h));
- net capital gain and qualified dividends (s 1(h), whose subchapter P definitions are not deposited);
- the s 1(g) "kiddie tax", screened as unearned income above $2,700 for anyone another can claim;
- the alternative minimum tax, beyond a screen (finding 9);
- the s 6017 return of self-employment tax (not deposited) where s 6012 alone would not require a return.

**Out, not asked:**

- s 152(b)(3)(B) (adopted children abroad);
- s 152(c)(4) as rules (asked as a fact);
- s 152(d)(3) multiple support, (d)(4), (d)(5), (e);
- s 7703(b) "but for section 152(e)";
- s 32(d)(2)(B)(iii)(II) (separation agreements);
- the s 24(g) and s 32(k) disallowance periods;
- s 24(d)(3), s 32(c)(1)(C) and the other s 911 rules;
- s 24(j) advance payments;
- s 86(e) lump-sum elections;
- the ss 85(c), 135, 137, 221, 911 adjustments to s 86 modified AGI. "Adjustments to income" is applied as given, and the `@desc` asks it to leave out student loan interest.
- every other credit in subparts A to C;
- the s 3101(b)(2) additional Medicare tax on wages, which is collected through withholding under chapter 21 and not part of chapter 1 or 2;
- s 6072, the return's due date. It is not deposited, so the duty takes the number of days to the due date as a parameter, and the cases use 105 days (15 April 2027).
- s 6409, refunds disregarded for means-tested programs. It is not deposited.

## What the Code turns out to say

1. **For 2026 the deposited text does not settle the filing thresholds, because "exemption amount" can be read two ways.** Section 6012(f), which tied the thresholds to the standard deduction, applies only "before January 1, 2026". For 2026, s 6012(a)(1) applies again, with thresholds of "the exemption amount plus the basic standard deduction", and (D)(ii) gives "exemption amount" "the meaning given such term by section 151(d)". Section 151(d)(5)(A) says that for years after 2017 "The term 'exemption amount' means zero". Section 151(d)(5)(B) keeps the zero from deciding whether a deduction is allowed, but s 6012 asks no such question. On that reading:
   - The single threshold is $16,100 and the joint threshold $32,200.
   - Any married individual outside clause (iv), for example one whose spouse files separately, must file on any gross income at all, since gross income always "equals or exceeds" zero.

   The IRS uses the indexed $5,300 as "the exemption amount referred to in § 152(d)(1)(B)" (Rev. Proc. 2025-32 s 4.23), and the same reading in s 6012 would give thresholds of $21,400 (single) and $42,800 (joint). The encoding computes both readings. When they agree it answers plainly. When they differ it says "a return is required if the exemption amount in s 6012 is zero, but not if it is $5,300". Asserted: the Garcias, with $40,000 jointly, and Dana, with $25,000 as head of household, get the conditional answer; Alex and Ruth do not. This is an interpretive question, not tested against any IRS guidance.
2. **The deduction for seniors is a s 151 deduction, so it is taken below AGI by itemizers and non-itemizers alike, and it is lost on a separate return.** Section 151(d)(5)(C) provides $6,000 for each qualified individual through 2028, reduced by 6% of modified AGI above $75,000 ($150,000 joint). Section 63(b)(2) lists the s 151 deduction for non-itemizers, and s 63(a) covers itemizers. Clause (v) denies it to a married individual unless the spouses file jointly. Asserted: Ruth gets $6,000, and Ruth filing separately gets 0.
3. **A married person filing separately who lived with the spouse at any time in the year has a s 86 base amount of zero.** So up to 85% of their benefits is taxable from the first dollar. Asserted: Ruth's $24,000 gives $4,000 taxable when she is single, $20,400 when she is married filing separately, and $4,000 again if the spouses lived apart all year.
4. **The child tax credit cannot reduce self-employment tax, and its refundable part is capped per child.** Section 24(a) allows the credit "against the tax imposed by this chapter" (chapter 1), while self-employment tax is chapter 2. Section 24(d) refunds the lesser of:
   - (A) the credit, capped at $1,700 for each qualifying child "without regard to paragraph (4)", so the $500 credit for other dependents is never refundable; and
   - (B) the unused credit, up to 15% of earned income above $2,500.

   Asserted: the Garcias get $780 against tax and $3,400 refunded of $4,400; Hana, whose son is 17, gets $500 and none of it refundable.
5. **A spouse's additional standard deduction for age or blindness on a joint return.** Section 63(f)(1)(B) and (2)(B) give the spouse's amount only "if an additional exemption is allowable to the taxpayer for such spouse under section 151(b)". Section 151(b) applies only "if a joint return is not made". Read literally, a 65-year-old spouse on a joint return would get no additional amount. The encoding reads a joint return as one in which both spouses are "the taxpayer" (s 6013(d)(3), "the tax shall be computed on the aggregate income"), so each spouse's own age and blindness count under (A). This is an interpretive choice, flagged.
6. **"Earned income" from self-employment is read as the business profit less the s 164(f) deduction.** Section 32(c)(2)(A)(ii) counts "net earnings from self-employment … (within the meaning of section 1402(a))", "determined with regard to the deduction allowed … by section 164(f)". But s 1402(a)(12) replaces the s 164(f) deduction with a 7.65% deduction when computing those earnings. The encoding takes the profit less the s 164(f) amount, which applies the instruction in s 32 rather than s 1402(a)(12). For Sam that is $46,467.6125. Under s 1402(a)(12) alone it would be $46,175. The same figure is used for s 24(d)(1)(B)(i).
7. **The Code's tax and the IRS's tables are not the same number.**
   - Section 3 imposes a table tax "in lieu of" the s 1 tax for most taxpayers, under tables the Secretary prescribes.
   - Section 32(f)(1) has the EITC "determined under tables prescribed by the Secretary", in brackets of up to $50.

   Neither table is deposited, so the encoding computes from s 1 and s 32(a) directly, to the cent. Its figures can differ from the table figures by a few dollars. For example, the Garcias' EITC comes out at $5,454.296, where a $50 table works from a bracket midpoint.
8. **A qualifying child without a valid social security number still makes the taxpayer an "eligible individual", but counts for nothing.**
   - Section 32(c)(1)(A)(i) makes anyone "who has a qualifying child" eligible.
   - Section 32(c)(3)(D) and (m) keep a child without a social security number out of the count under subsection (b).
   - So the credit is the no-child credit, without the age test of (A)(ii).
   - Under s 24(h)(4)(C), the same child moves from the $2,200 credit to the $500 one.

   Asserted: the Garcias without SSNs for the children get $780 of nonrefundable credit (from 2 × $500), no refundable credit, and no EITC, because $40,000 phases out the no-child credit.
9. **The alternative minimum tax is screened, not encoded.** For the facts this encoding takes, an upper bound on alternative minimum taxable income is the taxable income with every deduction below AGI added back, and with all tax-exempt interest treated as a preference. If the s 55(b) tentative minimum tax on that bound does not exceed the regular tax, the s 55(a) tax is zero and the answer is covered. Otherwise it is `not covered`. This works because the tentative minimum tax rises with AMTI. Asserted: a single earner with $1.2 million of wages passes the screen ($331,110 against $394,000.25).
10. **On the return's due date, "the time prescribed by law" is outside the deposit.** The duty to make a return (s 6012) and the three-year window in s 6013(b)(2)(A) both run from the s 6072 due date, which is not deposited. The duty takes the days to that date as a parameter. The window is computed from a due date the person gives: from 15 April 2027, 1,096 days, ending on 15 April 2030. Asserted.
11. **Refunds and means-tested benefits.** Section 32(l) keeps an EITC refund out of income and resources for the housing programs and SNAP for the month of receipt and the next. The wider rule for all federal means-tested programs is s 6409, which is not deposited. An encoding of SSI or SNAP that needs it should take it as an input.

## What would be needed before relying on it

- An IRS reading of "exemption amount" in s 6012 for 2026, such as the Form 1040 instructions or a notice (finding 1).
- s 6072 (the due date), s 6017 (the self-employment return), s 6409, s 72 (the taxable part of pensions), s 3121 (wages) and chapter 24 (withholding), deposited and linked.
- s 1(h) and its subchapter P definitions, for anyone with capital gains or qualified dividends.
- The full s 55 to s 59, in place of the screen.
- The s 3 and s 32(f) tables, if answers are to match the forms to the dollar.
- An independent test pass against IRS worked examples, such as Publication 596 for the EITC and Publication 915 for Social Security benefits, which are not deposited.
- Rev. Proc. 2026-xx for 2027, when it is published.
