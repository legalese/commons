# maine/

Maine (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Maine Revised Statutes, Office of the Revisor of Statutes (official); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with the standard WebFetch client, requests spaced roughly 2 seconds apart; 10 requests in total (the Titles index twice, then Title 26 index, Title 26 ch.7, Title 5 index, Title 5 ch.421, Title 24-A index, Title 24-A ch.27, Title 35-A index, Title 36 index, Title 22 ch.1053-B, Title 14 ch.709 and Title 14 ch.710). All returned 200 and no block, challenge or rate limit was encountered. One caveat on URL form: the Titles index advertises links under http://legislature.maine.gov/ros/LawsOfMaine/..., and http://legislature.maine.gov/ros/LawsOfMaine/26/title26ch0sec0.html returned HTTP 404; the working canonical form is https://legislature.maine.gov/statutes/<title>/title<NN>ch<C>sec0.html, which is what is recorded here.

## Topics with no legislation here

- **Passenger compensation**: No Maine statute. Air passenger rights are federal (49 U.S.C. 41712; 14 C.F.R. Part 250 oversold flights, Part 259 tarmac delays, US Department of Transportation) and are expressly pre-empted against state regulation by 49 U.S.C. 41713; intercity rail is Amtrak under 49 U.S.C. Subtitle V Part C. Maine's Title 35-A regulates transportation utilities but creates no passenger compensation entitlement.
- **Customs/duties**: Federal matter. US states are constitutionally barred from laying imposts or duties on imports or exports (U.S. Const. art. I, s.10, cl.2); customs law is 19 U.S.C. and the Harmonized Tariff Schedule.
- **Work permits/immigration**: Federal matter. Immigration and employment authorisation are governed by the Immigration and Nationality Act (8 U.S.C. 1101 et seq.), including employment verification at 8 U.S.C. 1324a; states have no power to issue work permits.

## Benefits and personal income tax sample (indexed 2026-10-20; text held back)

**Index only; no statute text deposited (flagged 2026-10-20).** The sample planned here is personal income tax and benefits, from the seat of the Maine resident who asks "What income tax do I owe, and what credits and benefits can I get?". When the register's terms were re-read for the deposit, the disclaimer page linked from every statute page (http://legislature.maine.gov/ros/LawsOfMaine/#Info) said: "All copyrights and other rights to statutory text are reserved by the State of Maine." That is a term needing permission, which the owner's ruling of 20 Oct 2026 (non-commercial use) does not cover, so under the sourcing rules the text was held back. The text of the law itself is not copyrightable (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)), so the reservation may not bind the bare text; the owner decides whether to deposit on that footing or to ask the Revisor of Statutes. The index check of 2026-09-23 had missed this line because it is not on the statute pages themselves.

Other terms read: robots.txt allows `/statutes/` (it disallows only bill search pages and `/LawMakerWeb`); the online text "reflects changes made through the Second Regular Session of the 132nd Maine Legislature, is current through October 1, 2026"; it is not certified (the certified text is the Maine Revised Statutes Annotated). Chapters and sections can be downloaded as PDF or MS-Word.

**Instruments confirmed against the register** (ready to fetch once the owner rules):

| Subject | Holds | Status |
|---|---|---|
| `maine-revised-statutes-title-36-part-8-income-taxes` (existing) | 36 M.R.S. Part 8: ch. 801 definitions (s 5102), ch. 803 rates (s 5111), ch. 805 resident taxable income and modifications (s 5122), ch. 822 credits -- earned income credit (s 5219-S), property tax fairness credit (s 5219-KK), dependent exemption tax credit (s 5219-SS) -- and ch. 841 inflation adjustments | indexed |
| `maine-revised-statutes-title-26-chapter-13-employment-security-benefits` (new index record) | 26 M.R.S. s 1043 (definitions) and ss 1191-1199 (benefits, eligibility, disqualification, claims) | indexed |
| `maine-revised-statutes-title-22-chapter-1053-b-temporary` (existing) | 22 M.R.S. ch. 1053-B, Temporary Assistance for Needy Families | indexed |
| `maine-revised-statutes-title-22-chapter-855-c-state-supplemental-income` (new index record) | 22 M.R.S. ch. 855-C, ss 3271-3274-A: State supplemental income for blind, disabled and elderly people (the state supplement to SSI); the plan's "3271 ff. (verify)" is confirmed | indexed |

**How the pieces would connect** -- all unverified (general knowledge), as no text was read into the corpus: Maine taxable income starts from federal adjusted gross income (`subjects/us/internal-revenue-code-of-1986`); s 5122 subtracts Social Security benefits taxed federally under IRC s 86; the earned income credit (s 5219-S) is a percentage of the federal credit under IRC s 32; unemployment benefits run under the federal-state scheme (Social Security Act Titles III and IX, FUTA); TANF is Maine's Title IV-A programme and ch. 855-C supplements federal SSI under SSA s 1616 (`subjects/us/social-security-act`). The Code of Maine Rules was not used: www.maine.gov answered 403 to robots.txt at set-up.
