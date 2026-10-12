# Retrenchment benefit and Workfare Income Supplement -- naive encoding (as published)

**ADMINISTRATIVE POLICY AS PUBLISHED, NOT LAW.** Neither scheme is encoded from a statute. The retrenchment benefit
norm is a tripartite guideline; the Workfare Income Supplement (WIS) is a Government scheme whose figures change by
announcement. Every figure here carries the date of the page it came from.

## Method

**Naive and as published.** One pass from official pages read on 12 October 2026, with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test pass, no human gate. Nothing from
the sources is deposited (see `../../SOURCE-LICENSE.md`); figures are restated, with only short phrases quoted.

## Sources (all read 12 October 2026)

| Page | Publisher | Last updated |
|---|---|---|
| https://www.mom.gov.sg/employment-practices/retrenchment/responsible-retrenchment | MOM | 14 Jul 2026 |
| https://www.mom.gov.sg/-/media/mom/documents/employment-practices/guidelines/tripartite-advisory-on-managing-excess-manpower-and-responsible-retrenchment.pdf | MOM (the Advisory) | updated 20 Jan 2023 |
| https://www.mom.gov.sg/faq/retrenchment/can-my-company-terminate-my-employment-contract-without-paying-any-rb-and-if-employers-must-pay-rb | MOM | 14 Mar 2024 |
| https://www.mom.gov.sg/faq/retrenchment/are-employees-who-have-worked-less-than-2-years-entitled-to-retrenchment-benefit | MOM | 14 Mar 2024 |
| https://www.mom.gov.sg/faq/retrenchment/are-my-employees-who-are-aged-63-or-above-eligible-for-retrenchment-benefit-or-eap | MOM | 14 Mar 2024 |
| https://www.tal.sg/tadm/faqs/advisory/i-have-been-retrenched | TADM | 2 Mar 2026 |
| https://www.cpf.gov.sg/member/growing-your-savings/government-support/workfare-income-supplement | CPF Board | 18 Jun 2026 |
| https://www.cpf.gov.sg/service/article/what-are-the-eligibility-criteria-of-the-workfare-income-supplement-scheme | CPF Board | 23 Jul 2026 |
| https://www.cpf.gov.sg/member/tools-and-services/calculators/workfare-income-supplement-employee-work-year-2026-calculator | CPF Board | 3 Aug 2026 |

Tried and not used: `mom.gov.sg/employment-practices/retrenchment/retrenchment-benefits` (404);
`workfare.gov.sg` (domain does not resolve); `tal.sg/tafep/employment-practices/retrenchment` (no figures);
the CPF "About Workfare" page (no figures); the CPF WIS factsheet PDF (it describes the 2020 changes only, so is
superseded and was not encoded).

## Checks

`l4 run rbw-cases-retrenchment-workfare.l4`: **46 assertions satisfied, 0 errors, 0 warnings** (counted with
`runcases.py`). The first twelve are REQ-0276's own question on its facts.

## Findings

### 1. REQ-0276 -- the norm is $32,550 to $65,100; Workfare pays him nothing

Jun Hao (cradle-to-grave-jun-hao, j087, 30 November 2055): security officer, 21 years' service, $3,100 a month,
retrenched at 49. Answered on the policy **as published in October 2026**; nothing on the pages says what will apply
in 2055.

- **Retrenchment benefit.** The Advisory (Annex C II, updated 20 January 2023) makes employees with 2 years' service or
  more eligible. Its norm is two weeks' to one month's salary per year of service, depending on the company's finances
  and the industry. Where a unionised company's collective agreement fixes the quantum, the norm is one month per
  year. For him: **$32,550 (bottom) to $65,100 (top); $65,100 under a collective agreement.** The contract or
  collective agreement comes first; the norm applies to negotiation where they are silent.
- **Two weeks' salary is not defined.** The bottom figure reads two weeks as half a month ($1,550). Reckoned as 12
  months' pay over 26 fortnights it is $1,430.77, and the bottom becomes about $30,046. Both are in the module; the
  cases assert the half-month reading.
- **Differs from the ledger.** The question says "the Act entitles him to a retrenchment benefit". The publishers say
  otherwise: MOM's FAQ says it is "not mandated by law", and TADM says that under the Employment Act it is "not
  compulsory". MOM does not attribute the 2-year threshold to the Employment Act; it is the Advisory's. Whatever the
  Act itself says about retrenchment benefit is for the `employment-act-1968` row, not this one.
- **Workfare.** WIS for employees is assessed month by month on income "for work done in that month", with a cap of
  **$3,000** a month and on the 12-month average (from Work Year 2025; the 2026 calculator repeats it). At $3,100 he was
  above the cap, so **he got no WIS in his last month of work**, and **none while unemployed**: WIS is paid only for
  months worked (the calculator says "for every month that you work"). The ledger's assumption, "Workfare by age and
  income", yields **nil**.
- **If he works again** at $3,000 or less, and his 12-month average is also at or below $3,000, he qualifies again
  (subject to the property and spouse tests). His age band (45 to 59) caps WIS at **$4,200 a year** (WY2025), paid
  **40% cash, 60% CPF** ($1,680 and $2,520 at the cap). How months without income enter the 12-month average is not
  stated, so the average is an input.
- **What WIS would be for a given income is not published** on the pages read: only the yearly maximum by age. So
  no monthly amount is computed for an eligible worker. The shape the ledger expects ("money") is met for the
  retrenchment benefit and for Jun Hao's WIS (nil), but not for WIS in general.

### 2. Smaller things recorded

- Pre-cut salary is used if retrenchment follows shortly after a salary cut (Advisory Annex C II(iii)).
- No CPF contributions on retrenchment benefit (MOM page).
- Aged 63 or above: the employer can use the Employee Assistance Payment instead, unless the contract or collective
  agreement provides retrenchment benefit (MOM FAQ). Its amount is in other guidelines, not encoded.
- A claim for unpaid contractual retrenchment benefit goes to TADM within 6 months of the last day of employment.
- WIS: citizen, at least 30 at 31 December of the work year (or a person with disabilities, who also gets the 60-and-above
  amount); floor $500, waived for persons with disabilities, ComCare Short-to-Medium-Term Assistance recipients and
  qualifying caregivers; home annual value at most $21,000 (from WY2024; $13,000 for WY2023); one property at most, with
  spouse; spouse's assessable income at most $70,000. Paid by the end of the second month after the work month.

## What would need doing

1. Find a published WIS payout schedule by income (the CPF calculator computes one but the page shows no table), and
   the WY2026 maximums; until then years from 2025 use the WY2025 table.
2. Settle how "two weeks' salary" is reckoned, if any official page says.
3. Link to the `employment-act-1968` row for what the Act says about retrenchment benefit and the service threshold.
4. Re-read every page before relying on a figure; the dates above are the as-published dates.
