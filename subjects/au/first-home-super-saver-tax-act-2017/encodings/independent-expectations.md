# Independent expectations: First Home Super Saver Tax Act 2017 (Cth)

Written from `BRIEF.md` and `../registers/source-bundle/C2017A00133.txt` only, before reading any `.l4` file.

## The Act's words relied on

- s 3: "First home super saver tax payable under section 313-60 of the Income Tax Assessment Act 1997 by a person is imposed."
- s 4: "The amount of the first home super saver tax is 20% of the person's assessable FHSS released amount (within the meaning of the Income Tax Assessment Act 1997)."
- s 2 table, item 1: the whole Act commences "At the same time as Schedule 1 to the Treasury Laws Amendment (Reducing Pressure on Housing Affordability Measures No. 1) Act 2017 commences"; column 3 gives "1 July 2018".

## Scenarios

| # | Release date | Payable under s 313-60? | Assessable FHSS released amount | Expected tax | Why |
|---|---|---|---|---|---|
| 1 | 2019-03-01 | yes | 10,000 | 2,000 | s 4: 20% of the amount |
| 2 | 2019-03-01 | yes | 0 | 0 | 20% of nil |
| 3 | 2019-03-01 | no | 10,000 | 0 | s 3 imposes only tax "payable under section 313-60" |
| 4 | 2018-07-01 | yes | 5,000 | 1,000 | commencement day itself: Act in force |
| 5 | 2018-06-30 | yes | 5,000 | 0 | day before commencement: nothing imposed |
| 6 | 2017-12-13 | yes | 5,000 | 0 | assent day, before commencement |
| 7 | 2024-07-15 | yes | 1,234.56 | 246.912 | 20%, no rounding rule in the Act |
| 8 | 2025-01-01 | yes | 50,000 | 10,000 | no cap or threshold in this Act (any cap on releasable amounts lives in the ITAA 1997, outside scope) |

Also expected: a "tax is imposed" predicate is true for scenarios 1, 2, 4, 7, 8 and false for 3, 5, 6 (for scenario 2, the Act imposes the tax even though its amount is nil).

## Where I read the Act differently from the brief

- The brief states commencement as 1 July 2018. Strictly, s 2(2) says column 3 "is not part of this Act"; the legal commencement is tied to Schedule 1 of the Treasury Laws Amendment Act. Treating 1 July 2018 as the commencement date is a fair, factual simplification, and I test against it.
- The brief frames the date input as "the date of the release". The Act itself says nothing about release dates; whether a release before 1 July 2018 could ever give rise to tax is a question for the ITAA 1997. I accept the brief's framing.
- The Act sets no rounding. I expect the exact 20% figure, not rounding to cents or dollars.
