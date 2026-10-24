# alaska/

Alaska (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Alaska State Legislature, BASIS - Alaska Statutes (Legislative Affairs Agency); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet (still so on 2026-10-24: see the last section).

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Scripted fetching is blocked: a plain HTTP fetch of https://www.akleg.gov/basis/statutes.asp returns 403 Forbidden, and the old host www.legis.state.ak.us now fails TLS (certificate covers only akleg.gov). I did not try to defeat the 403; instead I opened the same public page in a real browser (Claude's browser pane, ordinary Chrome, no user-agent spoofing), where it loads normally with the page title 'Alaska Statutes 2025'. Title and chapter contents are delivered by the site's own endpoint statutes.asp?media=js&type=TOC&title=<n>, which the page itself calls; I requested about 16 of those from inside the loaded page, spaced ~1.7 seconds apart. One transient 522 (Cloudflare origin timeout) on http://akleg.gov/disclaimer.php; the https URL served it. No CAPTCHA was encountered. The statutes pages carry no copyright notice and no 'current through' line beyond the 'Alaska Statutes 2025' page title.

## Topics with no legislation here

- **Personal tax/withholding**: Alaska levies no individual income tax, so there is no personal tax or wage-withholding statute. Verified on the register: the Title 43 chapter table of contents for AS 43.20 ('Alaska Net Income Tax Act') shows 'Sec. 43.20.010. Tax on individuals, fiduciaries, and corporations. [Repealed, s 13 ch 70 SLA 1975.]', with the live charging section being 43.20.011 'Tax on corporations'; the individual credit and exemption provisions 43.20.015 and 43.20.017 are also flagged '[Repealed, s 10 ch 1 SSSLA 1980.]'. Personal income tax and wage withholding are therefore federal only (Internal Revenue Code, 26 U.S.C., withholding at 26 U.S.C. s 3402).
- **Passenger compensation**: Federal. Air passenger rights are US DOT rules (14 C.F.R. Parts 250, 259) and state regulation of airline prices, routes and services is preempted by the Airline Deregulation Act, 49 U.S.C. s 41713. Alaska regulates ferry and motor-carrier operations (AS 42.25 Alaska Ferry Transportation Act, AS 42.10) but has no passenger compensation scheme.
- **Customs/duties**: Federal and exclusive: U.S. Const. art. I, ss 8 and 10; Tariff Act of 1930, 19 U.S.C. States levy no customs duties.
- **Work permits/immigration**: Federal. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. (employment verification at 8 U.S.C. s 1324a). Alaska has no E-Verify or work-authorisation statute; AS 23.05.125 establishes only an 'Office of citizenship assistance' within the labour department, which is assistance rather than regulation of work permits.

## Tax and benefits (2026-10-24): indexed, not deposited

The aim was a connected sample on personal income tax and benefits. Nothing could be deposited or encoded.

- **Personal income tax:** Alaska has none. Already recorded above: AS 43.20.010, the tax on individuals, was repealed by s 13 ch 70 SLA 1975, and the live charging section, AS 43.20.011, taxes corporations. An Alaskan's income tax is federal only (`subjects/us/internal-revenue-code-of-1986`).
- **Benefits:** three subjects were indexed from the Legislature's own tables of contents, each with `text_deposited: false`:
  - [`alaska-statutes-title-43-chapter-23-permanent-fund-dividends`](alaska-statutes-title-43-chapter-23-permanent-fund-dividends): the Permanent Fund Dividend (eligibility, allowable absences, application, amount);
  - [`alaska-statutes-title-47-chapter-27-alaska-temporary-assistance-program`](alaska-statutes-title-47-chapter-27-alaska-temporary-assistance-program): TANF cash assistance;
  - [`alaska-statutes-title-47-chapter-25-adult-public-assistance`](alaska-statutes-title-47-chapter-25-adult-public-assistance): the state supplement to SSI.
- **Why no text.** On 2026-10-24 akleg.gov answered plain requests with our User-Agent (HTTP 200; it had answered 403 on 2026-09-23), and robots.txt does not disallow the statutes pages. But the Legislature's Disclaimer/Credits page (http://akleg.gov/disclaimer.php) says: "To obtain permission to reproduce the information (text or graphics) contained on the Alaska Legislature web site, send an email to: webmaster@akleg.gov. The Alaska Legislature should be given credit and provided a copy of the final product." That is a permission requirement, so under the encoding guide (section 8) the text waits for Michael's ruling. No section text was requested.
- **To unblock:** a ruling that the statute text (an edict of government, *Georgia v. Public.Resource.Org*) may be deposited notwithstanding the page, or permission from webmaster@akleg.gov. Then the PFD (AS 43.23.005-.025) and ATAP (AS 47.27.010-.035) are the two encodings to write.
