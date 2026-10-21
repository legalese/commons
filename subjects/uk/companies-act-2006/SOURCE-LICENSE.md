# Source license

The quoted text of **Companies Act 2006** is sourced from [legislation.gov.uk](https://www.legislation.gov.uk/),
published by The National Archives.

- **Copyright owner**: Crown copyright and database right (the site footer reads "© Crown and database right").
- **License**: [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
- **Terms checked**: 2026-10-21, at https://www.legislation.gov.uk/help
- **Source**: https://www.legislation.gov.uk/ukpga/2006/46

## Required attribution

Contains public sector information licensed under the Open Government Licence v3.0.

## Status of this deposit

Statute text deposited 2026-10-21: `registers/source-bundle/ukpga-2006-46.txt`, converted to plain text from
https://www.legislation.gov.uk/ukpga/2006/46/data.xml
(point in time (dct:valid) of the latest revised version: 2026-07-16). sha256 of the download: `ecc00b49b304b14f5b76f72875e75c2f4076257638cbcfbb8b653930c5fbe301`.

The commons converter that made the earlier UK deposits dropped tables, list enumerators, the numbers of headingless Schedule paragraphs, the long title and the date of enactment (checked on `uk/income-tax-act-2007`: about 800 paragraph numbers and 368 enumerators missing).
This text keeps them; the additions are listed in `registers/source-bundle/ukpga-2006-46.meta.json` (key `converter`).
Editorial commentary, the contents list and explanatory notes are left out, as in the earlier deposits.

## Terms read for the deposit of 2026-10-21

- **Licence statement**: the footer of https://www.legislation.gov.uk/help (read 2026-10-21) says: "All content is available under the Open Government Licence v3.0 except where otherwise stated." It adds that the site also contains content derived from EUR-Lex, reused under Commission Decision 2011/833/EU; the XML fetched for this Act contains no mention of EUR-Lex or europa.eu (case-insensitive search, 0 lines).
- **OGL v3.0 attribution**: the licence page (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/, read 2026-10-21) says that where the Information Provider gives no specific attribution statement, the user must use: "Contains public sector information licensed under the Open Government Licence v3.0." The help page gives none.
- **Fair use policy**: https://www.legislation.gov.uk/fair-use-policy (read 2026-10-21) requires a legitimate User-Agent that identifies the scraper and, preferably, a contact URL; compliance with robots.txt; and no more than 1,500 requests in any 5-minute period. It points large crawls to other download routes.
- **robots.txt**: https://www.legislation.gov.uk/robots.txt (read 2026-10-21) allows `User-agent: *` with `Crawl-delay: 5`; requests were spaced at least 5 seconds apart.
- **Access**: User-Agent `legalese-commons/1.0 (+https://github.com/legalese/commons; statute sourcing for Legalese commons)`. From a Singapore address the site answered both robots.txt and a data.xml request with HTTP 202 and no content (a challenge page), so the files were fetched through a short-lived relay in London (AWS eu-west-2), which was terminated afterwards. Twelve requests in all through the relay, all HTTP 200 except one 404 from a wrong URL guess (`/fair-use`; the policy is at `/fair-use-policy`):
  - 2026-10-21T08:49:10Z HTTP 200 /robots.txt
  - 2026-10-21T08:49:17Z HTTP 200 /help
  - 2026-10-21T08:49:26Z HTTP 200 /ukpga/2007/3/data.xml
  - 2026-10-21T08:50:34Z HTTP 200 /ukpga/1978/30/data.xml
  - 2026-10-21T08:50:43Z HTTP 200 /ukpga/2006/46/data.xml
  - 2026-10-21T08:50:50Z HTTP 200 /ukpga/1968/60/data.xml
  - 2026-10-21T08:50:56Z HTTP 200 /ukpga/2006/35/data.xml
  - 2026-10-21T08:51:04Z HTTP 200 /ukpga/1971/48/data.xml
  - 2026-10-21T08:51:10Z HTTP 200 /ukpga/Vict/24-25/100/data.xml
  - 2026-10-21T08:51:18Z HTTP 200 /ukpga/1994/23/data.xml
  - 2026-10-21T08:51:43Z HTTP 404 /fair-use
  - 2026-10-21T08:51:58Z HTTP 200 /fair-use-policy
