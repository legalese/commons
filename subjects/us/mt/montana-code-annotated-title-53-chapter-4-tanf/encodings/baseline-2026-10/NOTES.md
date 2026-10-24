# Montana TANF cash assistance (MCA Title 53, ch. 4, parts 2 and 6) — baseline encoding

## Method

**Baseline**, written straight from the deposited text from the applicant's seat, with the design defaults ruled on 2026-10-18.

- **`mt-tanf.l4`** is the seat-neutral core, in the Code's own terms.
- **`mt-tanf-seat.l4`** is the seat layer. It asks the applicant's questions, with `@export` and `@desc` on each.
- **`mt-tanf-cases.l4`** tests the seat layer.

Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.** There was no earlier encoding of this subject.

## Edition

Montana Code Annotated 2025 (laws through the 2025 session), site marked "Updated August 2026", retrieved 2026-10-19 UTC, as deposited at `../../registers/source-bundle/mca-53-4-part-2.txt` and `mca-53-4-part-6.txt`.

The amount of assistance, the payment standards and the income and resource tests are set "according to the rules and standards of assistance established by the department" (53-4-241). They are in the Administrative Rules of Montana, Title 37, which were **not deposited**: the terms of the vendor-hosted rules.mt.gov could not be read (see `subjects/us/mt/README.md`, 2026-10-20). So this encoding does **not** answer "how much will I get".

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `mt-tanf.l4` (core), `mt-tanf-seat.l4` (seat) | `mt-tanf-cases.l4` | 22 written, 22 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24).
One `#TRACE` checks a breach: required employment and training not done. Its `-- expect:` comment was read against the output, which shows `BREACH BY the applicant`.

## Seat

**The applicant**: the caretaker relative applying for the family, or a needy pregnant woman with no other children. They ask: "Is my child a dependent child?", "Can we get cash assistance, or are we barred?", "How much of our child support do we keep?", "Can we get help with child care?", and what the department must do with the application.

The 2026-10-18 defaults:

- **The Code alone.** Parts 2 and 6. The department's rules are not deposited, so what they define is asked as a fact: who is a "student", the degrees of kinship of a "specified caretaker relative", the absence period, and the teen-parent settings.
- **Actors as the text names them:** the applicant, the specified caretaker relative, and the department of public health and human services.
- **Judgments handed to others, answered conditionally:** whether a plan or screening is "required", and whether employment and training is "appropriate" (53-4-613).
- **One case:** one family's application.
- **Machinery out:** state and county administration, rule-making, tribal plans (53-4-210), the parents-as-scholars programme (53-4-209), and federal cooperation.

## Regulative rules

There are two `DEONTIC` rules, with the seat as a parameter.

1. **`what follows my application`** (53-4-232, 53-4-233):
   - the relative the child lives with **must** apply to the department;
   - then the applicant **shall** take part in the required screening, and the department **must** inform the applicant of the fair-hearing right and of confidentiality, and **shall** promptly decide and notify the applicant in writing;
   - if the applicant is eligible, aid **must** be furnished promptly.

   "Promptly" sets no number of days, so these duties have no `WITHIN` (finding 3).
2. **`the employment and training condition`** (53-4-613): a recipient **may be required** to take part in employment and training as a condition of eligibility. The text gives no time limit, so the days allowed are an input.

## Read with the federal TANF frame

The federal frame is 42 U.S.C. 601-619, in `subjects/us/social-security-act/` (`usc42-ch7-schIV-ptA.txt`). Montana's text mirrors it in several places:

- no entitlement: s 601(b) and 53-4-231(6);
- the 60-month limit: s 608(a)(7) and 53-4-231(5);
- assignment of support: s 608(a)(3) and 53-4-231(4)(d);
- the fugitive-felon bar: s 608(a)(9) and 53-4-231(4)(h);
- residence fraud: s 608(a)(8) and 53-4-231(4)(i).

SNAP treats households in which every member receives TANF as categorically eligible (7 U.S.C. 2014(a), in `subjects/us/food-and-nutrition-act-of-2008/`). Cross-folder IMPORT is not possible in the stable `l4`, so these links are recorded only here.

## Scope

**In:**

- 53-4-201(5): who is a dependent child;
- 53-4-231: eligibility;
- 53-4-232 and 53-4-233: the application and the department's determination (regulative);
- 53-4-260(1): the child support pass-through;
- 53-4-611: child-care assistance;
- 53-4-613: employment and training (regulative).

**Out:**

- 53-4-237: stepparent income, which is at the department's discretion;
- 53-4-241: the amount, set by department rule and not deposited;
- 53-4-242: periodic reconsideration;
- 53-4-244: payment to a person interested in the child;
- 53-4-245: tribal per capita payments;
- 53-4-248: parents' debt to the department (it falls on a non-recipient parent);
- 53-4-202, 53-4-209 to 53-4-222: programme administration.

## What the Code turns out to say

1. **The statute sets no amount, no income test and no resource test.** Everything a family receives is "determined according to the rules and standards of assistance established by the department" (53-4-241). Without the ARM, the deposited law can say who *may* be granted assistance and who is barred, but not how much anyone gets.
2. **There is no entitlement.** Assistance "may be granted" (53-4-231(1)), and "This part may not be interpreted to entitle any individual or family to assistance" (53-4-231(6)). The best answer the encoding can give is "may be granted". Asserted.
3. **The department must decide "promptly", but no number of days is set.** Under 53-4-233 the department must decide promptly and furnish aid promptly; neither the statute nor anything deposited gives a time.
4. **The 60-month limit counts every state, and months need not be consecutive.** 53-4-231(5) bars the family "unless an exception is expressly granted by federal law". The federal hardship exemption (s 608(a)(7)(C)) is a state option, so whether it is "expressly granted" here is not clear. This encoding does not model an exception. Asserted (60 months: barred).
5. **A drug felony is no bar while the person complies with supervision, or once the sentence is discharged** (53-4-231(3)). This is Montana's use of the federal opt-out. Asserted (as the "no" input).
6. **The child support pass-through is $100 per family, however many children there are** (53-4-260(1)). Asserted.
7. **The pregnant woman's start is approximated.** The text lets payments begin "no earlier than the third month prior to the month in which the child is expected to be born". The encoding asks for whole months until the birth and allows assistance at 3 or fewer.

## Before relying on it

- Deposit ARM Title 37, chapter 78 (TANF standards), once the rules.mt.gov terms can be read. Then encode the payment standards and the income and resource tests.
- Do an independent test pass.
