# Higher Education Support Act 2003 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design defaults
ruled on 2026-10-18. No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use
as advice.

This encoding replaces the first-pass encoding `naive-2026-10`. It covers everything that
encoding covered and reuses its hand-checked values: the Lorraine, Paula and Kate examples,
the FEE-HELP loan fee, the 20% cut, and the c048 repayment. It adds:

- voluntary repayment (Division 151);
- re-crediting of the HELP balance on repayment (s 128-25);
- discharge on death (ss 137-20, 140-40);
- the notice on leaving Australia (s 154-18(1));
- the residence categories as one fact, so that New Zealanders and former humanitarian visa holders are handled.

**Edition:** Compilation No. 104, compilation date 1 July 2026 (includes amendments up to
Act No. 17, 2025), register id C2026C00297, deposited at
`../../registers/source-bundle/C2004A01234.txt`.

No regulation or guideline is deposited. The repayment thresholds and rates are the Act's own
(ss 154-10, 154-20). Section 154-25 indexes them for each income year after 2025-26, so for
later years the AWE figures that index them are inputs. The text deposit drops the formulas that the
Register prints as images: ss 93-5(1), 140-25(1), 140-26(2) and 154-25(2). They are transcribed by hand
from the Word rendering of the same compilation (fetched 2026-10-21) in
`../../registers/source-bundle/C2004A01234.formulas.md`, and encoded.

**Checks:** one module (`hesa-help.l4`) and one case file (`hesa-cases-help.l4`). 70
assertions satisfied, 0 errors, 0 warnings (re-run 2026-10-21 after the formulas were encoded). A deliberately wrong expected value ($676 for
$675) was run as a check, and it failed as it should.

## Seat

**The student, and later the former student repaying a HELP debt.** These are the people the
Act lends to and collects from. Their question is "What is deferred as a HELP debt, and when
must I repay?" Every exported question is phrased in their voice, for example `Am I entitled
to HECS-HELP assistance`, `Must I make a compulsory repayment` and `If I die how much of my
HELP debts can still be collected`.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No instrument is deposited. The figures the text states are encoded as the text states them. Indexed figures (the loan limit, maximum contributions, thresholds after 2025-26, CPI, WPI) are inputs.
- **The actors the text names.** Followed: the student, the provider, the Secretary and the Commissioner. Provider-only duties are encoded as what they mean for the student. An example is `Could my provider lawfully tell me I am Commonwealth supported` (s 36-10).
- **Judgments handed to someone else, answered conditionally.** Followed. The following are asked as facts, never guessed:
  - the provider's academic-suitability assessment;
  - the Secretary's genuine-student determination;
  - the Student Learning Entitlement;
  - the Overseas Debtors Repayment Guidelines exceptions;
  - Medicare levy outcomes under s 8 of the Medicare Levy Act 1986.
- **The Act's own definitions worked out; borrowed terms asked.** Followed. Worked out from facts:
  - Commonwealth supported student;
  - HELP balance;
  - HELP debt;
  - accumulated HELP debt;
  - repayment income;
  - repayable debt.

  Borrowed terms are asked as facts: taxable income, reportable fringe benefits, and the visa classes.
- **One case is the text's natural unit.** Followed: one enrolment in one unit of study, since a debt is incurred unit by unit at its census date. One income year is the unit for repayment.
- **The Act's own terms with a plain gloss.** Followed, in comments and `@desc`.
- **Operative sections in; machinery out.** Followed. Grants, provider approval, assessments, PAYG, recovery and the regulation-making powers are out.

## The lives

- **Chloe c030 (2021, Bachelor of Commerce at UWA, HECS-HELP).** Is she Commonwealth supported and entitled to HECS-HELP? What is the most a commerce place costs (the s 93-10 figure, $14,500)? What debt does a 2021 unit create (the loan, uncut)? Yes, yes, $14,500, the loan.
- **Chloe c045 (first return, 2023-24, $27,500).** `Must I make a compulsory repayment`: no. She is under the threshold and pays no Medicare levy. The thresholds for 2023-24 are not in the deposit (`a repealed rule that is not in the deposit`).
- **Chloe c048 (second return, 2024-25, $71,500).** `Which repayment thresholds apply to my income year` returns `a repealed rule that is not in the deposit`. Read against the compiled 2025-26 rule, she is liable and repays $675 (15% of $4,500). See finding 1.
- **Daniel d020 (2014, Bachelor of Commerce at UWA, HECS-HELP).** Commonwealth supported and entitled to HECS-HELP. The student identifier rule does not reach a 2014 census date.
- **Daniel d022 (2017, Juris Doctor at UWA, FEE-HELP).** Not advised that he is Commonwealth supported, he is entitled to FEE-HELP and not HECS-HELP. A postgraduate FEE-HELP loan carries no loan fee ($20,000 lent is a $20,000 debt). Had UWA advised him, the answer reverses.

## Why this scope

The plan names Parts 2-2, 3-2, 3-3 and 4-2 and ss 154-1, 154-10 and 154-20. The brief adds what
the seat meets: indexation, voluntary repayment and the debt on death. The notice on leaving
Australia is included because it is a duty the former student carries, with a 7-day deadline.

Left out, because no event asks it and it is machinery or another loan scheme:

- OS-HELP, SA-HELP, STARTUP-HELP and VET FEE-HELP;
- the overseas debtors' levy;
- location-preferred debtors;
- re-crediting for special circumstances;
- assessments.

## What the Act turns out to say

1. **The deposited repayment rule is the 2025-26 rule, and Chloe's 2024-25 repayment ran on a text that is not deposited.** The endnotes show that ss 154-10, 154-20 and 154-25 were substituted in 2025 ("rs No 30, 2025"). Section 154-25(2) indexes from the income years "after the 2025-26 income year". *Inference:* the compiled $67,000 / 15% / 17% / 10% rule speaks to 2025-26. The encoding says so explicitly: `What is my minimum repayment income` returns `NOTHING` for years before 2025-26. Read literally against the compiled rule, c048 gives $675. Asserted.
2. **The repayment is the least of three amounts.** They are the marginal amount, 10% of repayment income, and the repayable debt (s 154-20(1)). On $200,000 the 10% cap binds ($20,000, not $21,450). On a $3,000 debt the debt binds. Liability needs income that *exceeds* the minimum, so exactly $67,000 owes nothing. Asserted.
3. **No Medicare levy, no HELP repayment.** Section 154-1(2) removes liability where s 8 of the Medicare Levy Act 1986 leaves no levy payable or reduces it. This is a second, independent reason c045 owes nothing. Asserted.
4. **A permanent resident can hold a Commonwealth supported place but cannot defer it.** Section 36-10(2)(c) admits a permanent visa holder. Sections 90-5 and 104-5 admit only the following:
   - citizens;
   - permanent humanitarian visa holders, eligible former permanent humanitarian visa holders and Pacific engagement visa holders;
   - New Zealanders meeting the special category test.

   An ordinary permanent visa holder is Commonwealth supported but entitled to neither HECS-HELP nor FEE-HELP. Asserted.
5. **The reverse also happens: an eligible former permanent humanitarian visa holder may get FEE-HELP and not a Commonwealth supported place.** The Dictionary's definition does not require the visa they now hold to be permanent. If it is not, s 36-10(2) bars Commonwealth support, but s 104-5(1)(b) admits them to FEE-HELP. *Inference* that the visa can be temporary. Asserted.
6. **Whether a Juris Doctor is Commonwealth supported is not a question the Act answers.** It turns on the provider's written advice (s 36-5(1)(a)) and on whether the provider could lawfully give it (s 36-10). FEE-HELP is available only to a student who is *not* Commonwealth supported (s 104-1(1)(d)). Asserted both ways for Daniel.
7. **The 20% cut is in the text twice.** Section 140-26(1) adds "Step 7" for the debt accumulated for 2024-25, which turns Lorraine's $13,364.25 into $10,691.40. Section 137-19A cuts debts incurred from 1 January to 1 June 2025. A debt is incurred "immediately after the census date". *Inference:* read here as the next day, so a 31 December 2024 census date is inside the window and 1 June 2025 is outside it. An undergraduate FEE-HELP loan of $10,000 with a March 2025 census date becomes $12,000 with the loan fee, then $9,600. Asserted.
8. **Repaying restores what you can borrow, even though the balance "ignores" repayment.** Section 128-15(2) says "it is immaterial whether amounts ... have been repaid". Yet s 128-25 re-credits the balance with every payment made from 2019-20 onward, and with the 20% cuts. The two are reconciled through the balance's "as reduced by any amounts previously re-credited" limb. Asserted ($76,319 becomes $81,319 after a $5,000 re-credit).
9. **A voluntary repayment can be made at any time, and the Act decides where it goes if you do not.** Section 151-1 sets no minimum. Without directions, money goes first to the accumulated HELP debt and then to newer HELP debts in the order incurred (s 151-10(2)). Anything beyond all Chapter 4 debts and primary tax debts is refunded (s 151-15). Asserted.
10. **Death discharges the debt but not the repayments already owed.** Under s 137-20 a HELP debt is "taken to have been paid". Under s 140-40(1) the accumulated debt is "discharged". Section 140-40(2) keeps compulsory repayment amounts, "whether or not those amounts were assessed before the person's death". Asserted.
11. **A debtor leaving Australia for 183 days or more must tell the Commissioner within 7 days** (s 154-18(1)), unless the Overseas Debtors Repayment Guidelines except them. The Guidelines are not deposited. Asserted.
12. **Without a student identifier, Chloe would not be Commonwealth supported at all.** Sections 36-10(1)(f) and 104-1(1)(ga) require one for census dates in 2021-22 where the course began in 2021 or later, and for every census date from 2023. Daniel's 2014 enrolment is outside the requirement. Asserted.
13. **The four lost formulas say what the first pass inferred, and a little more.** From the sidecar: a unit's student contribution amount is the amount for a place times the unit's EFTSL value, rounded down (s 93-5(1), (4)); the accumulated HELP debt is former debt + debts incurred − repayments − the location-preferred reduction (s 140-25(1), the first pass's inference, now confirmed); for 2024-25 only the net new debt is cut to 80% (s 140-26(2)); and each repayment threshold after 2025-26 is the 2025-26 amount times AWE for the year over AWE for 2025-26, rounded down (s 154-25(2), (3)). $16,992 × 0.0833 gives $1,415; Lorraine's cut debt with $3,000 incurred and $500 repaid gives $12,691 on 1 June 2025; $67,000 at AWE 2,000/1,900 gives $70,526 (hypothetical AWE). Asserted.

14. **The text is the 2026 text.** Daniel's 2014 and 2017 answers apply today's text to past facts, including the Student Learning Entitlement and student identifier conditions added later (endnotes record amendments to ss 36-5 and 36-10 in 2020, 2022 and 2024). That is the right shape, but it is not the law as it stood. Not asserted as history.

## What would need doing before this is worth anything

- Deposit the 2023-24 and 2024-25 text of Division 154 (or the application provisions of the 2025 amending Act), so that c045 and c048 can be answered as the law stood. Do the same for the 2014 and 2017 texts for Daniel.
- Deposit the indexation instruments: the loan limit, the maximum contributions, and the thresholds from 2026-27.
- Deposit the published AWE figures, so that the thresholds from 2026-27 are worked out rather than asked.
- Encode s 8 of the Medicare Levy Act 1986 and the tax-law components of repayment income, so that they stop being inputs.
- Deposit the Overseas Debtors Repayment Guidelines and the Higher Education Provider Guidelines (genuine-student matters).
- Check the census-date boundary reading in finding 7 against departmental guidance.
- An independent test pass and the human gates.
