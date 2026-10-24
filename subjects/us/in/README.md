# indiana/

Indiana (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Indiana General Assembly - Indiana Code (published by the Legislative Services Agency); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Verified, but only through the site's own client-side rendering. iga.in.gov is a React single-page app: a plain HTTPS client with an honest user agent gets the same 691-byte app shell for every path, including /laws/current/ic/titles/22 and the static data paths. The documented API host api.iga.in.gov answers without a key with HTTP 403 and the body {'error': '403', 'message': 'x-api-key not found'} - no key was requested, guessed or used, and nothing was worked around. Instead the site's own pages were rendered in a real browser with JavaScript enabled (an honest browser, not a spoofed user agent), and that is where the Code data was read: the app itself requests same-origin static files at https://iga.in.gov/ic/2026/Title_<n>.json, each entry carrying type, number, name, year and a public flag, and those files were read in the page context. Currency: the human path https://iga.in.gov/laws/current/ic redirects to https://iga.in.gov/laws/2026/ic/titles/1, and every entry read carried year '2026' and public true, so 'current' is the 2026 edition of the Indiana Code. About 20 requests in all (2 plain-HTTP probes, 1 API probe, browser navigations, and 12 in-page data fetches spaced 1.8 seconds apart). No CAPTCHA, no rate limiting and no bot challenge was encountered on iga.in.gov. Separately, https://www.in.gov/core/policies.html (the statewide terms page) was unreachable from this environment ('connect ECONNREFUSED 208.40.244.65:443'), so the statewide policy text could not be read.

## Topics with no legislation here

- **Leave/holiday pay**: No Indiana statute creates a general leave or holiday-pay entitlement. The register's 2026 Title 22 data file shows only narrow provisions in IC 22-2: 'Chapter 13. Military Family Leave' (unpaid, 10 days, service-member family) and 'Chapter 14. Employee Breaks' (minors); there is no paid sick leave, vacation or public-holiday pay Act. Private-sector vacation and holiday pay is a matter of contract or policy, enforceable as wages under IC 22-2-5 and IC 22-2-9. Family and medical leave is federal (FMLA, 29 U.S.C. 2601). State-employee leave is set administratively by the State Personnel Department rather than by statute.
- **Passenger compensation**: Federal, and preempted. Air passenger rights come from US DOT rules (14 CFR Parts 250, 259, 260) and the Airline Deregulation Act (49 U.S.C. 41713) preempts state regulation of airline prices, routes and services. Indiana has no passenger-compensation statute.
- **Customs/duties**: Federal, and constitutionally exclusive. U.S. Const. art. I, sec. 10, cl. 2 bars a state from laying imposts or duties on imports or exports; customs law is 19 U.S.C., administered by CBP.
- **Work permits/immigration**: Federal. Work authorisation and immigration status are governed by the Immigration and Nationality Act, 8 U.S.C., and 8 C.F.R. Indiana legislates only at the edges (for example IC 22-4-39.5, 'Chapter 39.5. Reimbursements by Employers of Unauthorized Aliens', seen in the register's Title 22 data, and E-Verify duties in IC 22-5-1.7), which is enforcement and not the grant of work authorisation.

## Benefits and personal income tax sample (2026-10-20): index only

This entry is part of the Priority 3 US-states sample, which aims at a connected set of Indiana statutes on personal income tax and benefits. **No text could be deposited**, because no permitted non-browser route to the Indiana Code was found:

- Every path on iga.in.gov, sent with the commons User-Agent, returned the same 691-byte app shell, served as CloudFront's error document (`X-Cache: Error from cloudfront`, HTTP 200). That held for the Code pages, the static data files the app reads (`/ic/2026/Title_<n>.json`), and even the app's own JavaScript bundle.
- robots.txt is absent: the path returns the shell.
- The documented API, api.iga.in.gov, requires an `x-api-key`, and getting one means registering an account.
- www.in.gov timed out on connect.

Nothing was worked around and no browser automation was used. 8 requests were made on 2026-10-20: 7 through the logged fetcher, and 1 HEAD request with curl, same User-Agent, to read the response headers.

The planned instruments are indexed, so a later fetch knows its targets:

| Instrument | Subject | Status |
|---|---|---|
| Adjusted Gross Income Tax, IC 6-3 (incl. the unified elderly credit, IC 6-3-3-9) | `indiana-code-title-6-article-3-state-income-taxes` (existing) | indexed 2026-09-23 |
| Local income tax, IC 6-3.6 | `indiana-code-title-6-article-3-6-local-income-taxes` (new) | indexed; citation unverified |
| Earned income tax credit, IC 6-3.1-21 | `indiana-code-title-6-article-3-1-chapter-21-earned-income-tax-credit` (new) | indexed; citation unverified |
| Unemployment Compensation System, IC 22-4 | `indiana-code-title-22-article-4-unemployment-compensation-system` (new) | indexed; chapters verified 2026-09-23 from the register's Title 22 data file |
| TANF, IC 12-14 | `indiana-code-title-12-article-14-family-assistance-services` (existing) | indexed 2026-09-23 |
| Over-65 property tax deduction, IC 6-1.1-12-9, and the circuit breaker credit, IC 6-1.1-20.6-8.5 | `indiana-code-title-6-article-1-1-chapter-12-over-65-property-tax` (new) | indexed; citations unverified |

**How they connect.** None of these links was read in a deposited text, so all are unverified (general knowledge):

- The state tax starts from federal adjusted gross income (IRC subject), with Indiana add-backs and deductions.
- The county local income tax uses the same base.
- The state EITC is a percentage of the federal credit under 26 U.S.C. s 32.
- UI benefits are federally taxable under 26 U.S.C. s 85.
- TANF is the state's plan under SSA Title IV-A.
- Indiana excludes Social Security benefits that are taxable federally under 26 U.S.C. s 86.

**To unblock.** Any one of these would do:

- a human requests an IGA API key for Legalese Commons;
- the owner approves a rendering-browser read of the app's own static Title JSON files, as the index check of 2026-09-23 did;
- the access check is re-run from a US egress.

Each new subject's `SOURCE-LICENSE.md` records the access check in full.

## Tax and benefits pass (2026-10-24): still blocked

The plain-client route was checked again on 2026-10-24 with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. Two requests were made: robots.txt, and `https://iga.in.gov/ic/2026/Title_6.html`. Both got the same 691-byte application shell, served as CloudFront's error document (`X-Cache: Error from cloudfront`, `Server: AmazonS3`).

The Code text itself was not read, but a browser that renders the site was used to see how it is published. The application loads each title's full text as a single same-origin static file, for example `https://iga.in.gov/ic/2026/Title_6.html` for Title 6 (Taxation, including IC 6-3 Adjusted Gross Income Tax), next to the `Title_<n>.json` index files described above. So the whole of IC 6-3, IC 12-14 and IC 22-4 is one static file per title. The obstacle is only the delivery layer: the files are served to a rendering browser but not to an honest scripted client.

Reading those files in a rendering browser and depositing them is the route that the 2026-10-20 note already leaves to the owner. Without that approval it was not taken, and nothing was deposited or encoded. The other two unblock routes in that note still apply: an API key, or a check from another network.
