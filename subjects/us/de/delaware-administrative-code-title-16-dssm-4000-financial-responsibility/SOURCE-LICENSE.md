# Source license

The text of **Delaware Social Services Manual 4000, Financial Responsibility** (16 Del. Admin. Code 4000) is published in the Delaware Administrative Code by the Registrar of Regulations, https://regulations.delaware.gov/AdminCode.

- **Register**: Delaware Administrative Code, https://regulations.delaware.gov (a State of Delaware host). The site is a single-page application. Its pages are filled from the site's own read API (configured at https://regulations.delaware.gov/config.json as `rpsApiDomain` https://regulations.delaware.gov/api/). The deposit was read from that API exactly as the page reads it. No browser automation was used.
- **Terms as read (2026-10-19 UTC)**: the site's built-in "About" text (in the application bundle https://regulations.delaware.gov/main.e86913c3cd7c00bf.js) says: "The Administrative Code is a topically-oriented compilation of all regulations in effect and is the official version of the regulations for the State of Delaware. Administrative regulations have the force and effect of law." No copyright notice, terms of use or reuse restriction was found in the site or its bundle. The footer links only to delaware.gov's general pages (privacy, help).
- **robots.txt**: https://regulations.delaware.gov/robots.txt answers HTTP 200 with the application's HTML shell (the same 65,668-byte page the site serves for any unknown path), not a robots file. It is treated as absent: nothing is disallowed and there is no Crawl-delay.
- **Access**: User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds between requests; every request HTTP 200; no challenge, 403 or 429. The API call was a POST with a JSON body, the same request the page sends.
- **Copyright in the text**: none. These regulations have the force of law and are edicts of government (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). The Register citations are the Registrar's; there are no vendor annotations.
- **Verdict**: **clean**. No reliance on the owner's non-commercial ruling of 2026-10-20 was needed.
- **Attribution (courtesy)**: "Delaware Administrative Code, Title 16, Delaware Social Services Manual, Registrar of Regulations."

## Status of this deposit (2026-10-20)

- `registers/source-bundle/de-admin-code-16-dssm-4000-financial-responsibility.txt` -- DSSM 4000, as published (latest amendment cited 29 DE Reg. 530 (12/01/25)). The TANF table in 4007.2 is headed "Current for 10/2002 - 9/30/2003" and the manual points to a separate COLA Administrative Notice for current standards. That notice is not in the Administrative Code and is not deposited.

**Deliberately out**: the rest of the DSSM (1000-3000 administration, case processing and technical eligibility; 5000 fair hearings; 6000 emergency assistance; 7000 overpayments; 8000 refugee resettlement; 9000 SNAP; 11000 child care; 14000-20000 medical assistance).
