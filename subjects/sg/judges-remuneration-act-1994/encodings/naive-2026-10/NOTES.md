# Judges' Remuneration Act 1994 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive rows (the `writing-l4-rules` skill was not available in this
session). No pipeline, no coverage table, no independent test pass, no human gate.
NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/JRA1994.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021". The latest amending Act annotated in the text and listed in the
Legislative History is Act 39 of 2019 (Judges' Remuneration (Amendment) Act 2019, in
force 2 January 2021). The source metadata records the version as current at 1
October 2026.

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0180** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The Act is five sections long, so this row takes all of it except s 1 (short title),
s 4(3) (the power to make regulations) and s 4(6) (the Consolidated Fund charge). The
people it reaches are the Judges, their dependants and estates, and their creditors.
No Gazette order fixing salaries and no gratuity regulations were retrieved, so no
salary figure appears, and the gratuity rate, its limit, the death gratuity amount and
any "prescribed" circumstances or service are inputs, not law.

## What the Act turns out to say

### 1. A maintenance order can take an assignment of the gratuity, but cannot attach it

s 4(4)(a) lets a gratuity be assigned to satisfy a debt due to the Government or a
court order for "periodical sums" towards the maintenance of a spouse, former spouse
or minor child "whether legitimate or not". But s 4(4)(b) allows attachment,
sequestration or levy only for "a debt due to the Government". So a former spouse
holding a maintenance order cannot attach the gratuity; only the Government can. A
lump-sum maintenance order, an adult child's maintenance, a bank loan or a private
judgment debt get neither. Asserted.

### 2. There are two schemes, split on the date of first appointment

s 1A: a Judge's annual pensionable salary counts for a pension under the Pensions Act
1956 if appointed to a judicial office before 1 January 2015, and for a gratuity under
this Act if first appointed on or after that date. s 4(8) confines the gratuity, and
the death gratuity, to those first appointed on or after 1 January 2015. Asserted.

### 3. The gratuity is a "may", and the Act says so twice

s 4(1): the President "may" grant it; s 4(5): "no holder of a judicial office has an
absolute right to compensation for past services or to any gratuity". Eligibility
needs a judicial office, first appointment on or after 1 January 2015, and retirement
"on attaining 65 years of age or in such other circumstances as may be prescribed".
The amount is the prescribed rate times each complete month of unbroken reckonable
service, capped at the prescribed limit. Asserted. (Inference, not asserted: read
literally, a Judge who retires later than on attaining 65 qualifies only if the
regulations prescribe that circumstance.)

### 4. Judicial Commissioner service counts only if there is no gap

s 4(7): reckonable service is service in a judicial office; service as a Judicial
Commissioner "if, and only if" it immediately precedes appointment without a break;
and prescribed Government service on the same condition, but never service as a
Senior Judge or an International Judge. A Judicial Commissioner, Senior Judge and
International Judge do not hold a "judicial office" (s 1A), so none of them can be
granted the gratuity in that capacity. Asserted.

### 5. A death gratuity goes to the dependants the President picks, or else the estate

s 4(2): where a Judge dies in office after 1 January 2015, the death gratuity may be
paid to "such of the deceased's dependants as the President may think fit" or, if
there are none, to the legal personal representatives. Asserted.

### 6. The allowance floor is the public service

s 2(2): a Judge's allowances and privileges "must not be less than" those of a public
officer receiving the same pensionable salary. Salary and allowances run from the date
of appointment (an allowance subject to its condition), accrue from day to day, and
are paid monthly (s 2(3)). The salary is whatever the Minister's Gazette order says,
and the order goes to Parliament (s 2(1), (4)). s 3 keeps s 2(2)(b) of the repealed
1985 Act for Judges appointed before 1 September 1994; what that paragraph said is not
in the deposit. Asserted (the floor, the start date, the s 3 cut-off).

## What would need doing before this is worth anything

- Retrieve the Judges' Remuneration (Gratuity) regulations, if any, for the rate, the
  limit, the death gratuity, and the prescribed circumstances and service.
- Retrieve the current salary order under s 2(1).
- Retrieve s 2(2)(b) of the 1985 Revised Edition to say what s 3 preserves.
- Read the Pensions Act 1956 for the pre-2015 scheme and the Constitution (Art 98)
  on Judges' retirement age and extensions.
