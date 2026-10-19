# minnesota/

Minnesota (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Minnesota Office of the Revisor of Statutes - Minnesota Statutes (official publisher); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched cleanly over HTTPS with an honest identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon metadata research; contact address removed)'), requests spaced ~2 seconds apart; about 20 requests in total. No robots block, no challenge, no 403/429. Working URL patterns: chapter page /statutes/cite/<chapter> (e.g. /statutes/cite/177), full chapter text /statutes/<year>/cite/<chapter>/full, section page /statutes/cite/<section>. Note: /statutes/chapter/<n>, /statutes/part/<n> and /copyright/ do not exist (404). Two transient connection failures (curl exit 28 / empty response) on /statutes/info and /statutes/cite/181.13/pdf were worked around simply by retrying the same page through a different fetcher, not by changing identity. The site carries no copyright notice and no terms-of-use page that I could find.

## Topics with no legislation here

- **Passenger compensation**: No state statute. Air passenger rights are federal (49 U.S.C. 41712 and the DOT oversales/denied-boarding rules at 14 C.F.R. pt. 250); intercity rail is Amtrak under 49 U.S.C. subtit. V pt. C. Minnesota regulates carriers (ch. 221) but does not confer passenger compensation.
- **Customs/duties**: Federal matter, not state: Tariff Act of 1930 and the Harmonized Tariff Schedule, 19 U.S.C.
- **Work permits/immigration**: Federal matter, not state: Immigration and Nationality Act, 8 U.S.C. ch. 12; employment authorisation and verification at 8 U.S.C. 1324a. Minn. Stat. ch. 181A (child labour) issues employment certificates for minors, which is a different subject.

## Statute text deposited 2026-10-20: personal income tax and benefits

Five chapters of Minnesota Statutes were deposited as unofficial plain text, for a sample on personal income tax and state benefits. Each chapter is whole. The source is the Office of the Revisor of Statutes' **2025 edition**, the current online edition when fetched (2026-10-19 UTC). Changes made by the **2026 Regular Session are not incorporated**. Each file's header lists the provisions the Revisor flags as affected: 43 in ch. 290, 13 in ch. 256D, 8 in ch. 142G, 3 in ch. 268 and 1 in ch. 290A.

| Subject | Chapter | What it gives a person | Characters |
| --- | --- | --- | --- |
| `minnesota-statutes-chapter-290-income-and-franchise-taxes` (existing; text added) | Minn. Stat. ch. 290 | State income tax owed: net income from federal AGI (290.01, subd. 19), additions and subtractions (290.0131-290.0137), the bracket rates (290.06, subd. 2c), the child tax credit (290.0661), the working family credit (290.0671), the renter's credit (290.0693) | 492,386 |
| `minnesota-statutes-chapter-290a-property-tax-refund` (new) | Minn. Stat. ch. 290A | The homeowner's property tax refund, scaled to household income (290A.03, 290A.04) | 44,869 |
| `minnesota-statutes-chapter-268-unemployment-insurance` (existing; text added) | Minn. Stat. ch. 268 | Unemployment benefits: benefit account and weekly amount (268.07), eligibility (268.085), quit and discharge (268.095), tax withholding from benefits (268.145) | 342,338 |
| `minnesota-statutes-chapter-142g-minnesota-family-investment-program` (new) | Minn. Stat. ch. 142G | MFIP, the state's TANF cash assistance: eligibility (142G.10), income limits (142G.16), assistance standards (142G.17) | 306,849 |
| `minnesota-statutes-chapter-256d-general-assistance-and-minnesota-supplemental-aid` (new) | Minn. Stat. ch. 256D | General Assistance for adults without children (256D.05, 256D.06), and Minnesota Supplemental Aid, the state top-up for SSI recipients (256D.33-256D.54) | 100,295 |

**How the pieces connect, as read in the deposited texts:**

- **Federal income tax.** For an individual, Minnesota "net income" is federal adjusted gross income with the state's modifications (290.01, subd. 19(b)). The Code is incorporated "as amended through May 1, 2023" (290.01, subd. 31), which is a fixed conformity date. The federal text is in `subjects/us/internal-revenue-code-of-1986`.
- **Social Security benefits.** Minnesota subtracts taxable Social Security benefits from income, either as a simplified subtraction phased out above an AGI threshold or as an alternate subtraction. "Provisional income" and "Social Security benefits" take their meanings from IRC s86 (290.0132, subd. 26). IRC s86 is deposited in the IRC subject (`usc26-ch1-schB-ptI-III.txt`).
- **Working family credit and child tax credit.** To claim the working family credit, a person must be eligible for the federal EITC under IRC s32, with stated exceptions (290.0671, subd. 1(a)). The credit itself is a percentage of earned income, not a percentage of the federal credit. The child tax credit takes "qualifying child" from IRC s32(c) (290.0661, subd. 1). The two credits phase out jointly (290.0671, subd. 1(d)). IRC s32 is deposited in the IRC subject.
- **Property tax refund.** Household "income" starts from federal AGI and adds back nontaxable income, including cash public assistance and payments under the federal Social Security Act and SSI (290A.03, subd. 3). So the benefits in this set raise the income that the refund is measured against.
- **Unemployment insurance.** The chapter keys several definitions to the Federal Unemployment Tax Act, 26 U.S.C. ch. 23 (268.035). A claimant may elect 10% federal withholding and, in addition, 5% state withholding from benefits (268.145). Federal tax on benefits is IRC s85 (deposited in the IRC subject). Minnesota's own treatment of benefits is unverified (general knowledge): it follows from starting at federal AGI, with no ch. 290 subtraction for benefits found.
- **MFIP.** The commissioner receives and spends the federal TANF block grant under PRWORA (142G.03). Title IV-A of the Social Security Act is indexed in `subjects/us/social-security-act`, but its text is **not deposited** there, so the federal side of this link is not yet in commons.
- **General Assistance and Minnesota Supplemental Aid.** MSA serves people who receive SSI, or who would receive it but for excess income, and who have maintenance needs under state standards (256D.34). General Assistance clients who may be eligible for SSI are helped to apply and convert to it (256D.06). The SSI and state-supplementation text (SSA Title XVI, 42 U.S.C. 1381 and following, including 1382e) is deposited in `subjects/us/social-security-act` (`usc42-ch7-schXVI.txt`).
- **SNAP** is federal (`subjects/us/food-and-nutrition-act-of-2008`). Chapter 256D's heading mentions food support, but no state SNAP rules were sourced.

**Terms.** Read 2026-10-19 (UTC) at https://www.revisor.mn.gov/statutes/info. It says the authenticated PDFs are an official version and says nothing about reuse. There is no copyright notice and no terms page. robots.txt disallows only /alpha/, /beta/ and three search-result paths, and sets no Crawl-delay. Verdict: **clean**. Statute text carries no copyright (*Georgia v. Public.Resource.Org*, 2020). The headnotes, history lines and notes kept in the texts are the Revisor's own; none are vendor annotations. Each subject's SOURCE-LICENSE.md has the detail.

**Gaps.**
- The 2026 session laws are not applied.
- The inflation-adjusted bracket amounts and credit thresholds for the current tax year are set by the commissioner (290.06, subd. 2d) and are not sourced.
- The chapters these programs share or cross-refer to are not deposited: ch. 256P (income and asset rules for MFIP and GA), ch. 289A (filing and administration), ch. 268B (paid leave).
- Minnesota Rules (agency regulations) are not sourced.
