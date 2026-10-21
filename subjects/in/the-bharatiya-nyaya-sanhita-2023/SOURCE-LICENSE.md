# Source license

The text of **The Bharatiya Nyaya Sanhita, 2023** is published on the [India Code (Legislative Department, Ministry of Law and Justice)](https://www.indiacode.nic.in/).

- **Terms**: No open licence found. The terms recorded for India Code in [`../the-income-tax-act-2025/SOURCE-LICENSE.md`](../the-income-tax-act-2025/SOURCE-LICENSE.md) (checked there 2026-09-22 via a Wayback copy of disclaimer.jsp, not re-verified here) are that India Code publishes no copyright licence, and that Copyright Act 1957 s.52(1)(q)(ii) makes reproducing or publishing an Act of a Legislature non-infringing only if it comes with commentary or other original matter. Bare reproduction and adaptation of Act text is therefore conditional, not clearly permitted.
- **Terms checked**: 2026-10-21, at https://indiacode.gov.in/robots.txt and https://www.indiacode.nic.in/robots.txt (see below). The disclaimer page was not re-read.
- **Attribution required**: none stated; source acknowledgement advisable
- **Source**: https://www.indiacode.nic.in/handle/123456789/496548

## Consequence for this subject

**Metadata only until resolved.** The decision on the s.52(1)(q)(ii) condition is a human one and is open; no text of this Act is deposited or staged. Confirm before depositing text or quoting it in an encoding.

## Language

English is the authoritative text of Acts of Parliament (Article 348(1)(b) of the Constitution), as recorded in the sibling licence file above; not re-verified here.

## Status of this deposit

No statute text has been deposited yet. Only the India Code record was read, to confirm the Act's identity and that it is listed as not repealed (`registers/source-bundle/Act-No.-45-of-2023.meta.json`).

## Access checks of 2026-10-21

Every request used the User-Agent `legalese-commons/1.0 (+https://github.com/legalese/commons; statute sourcing for Legalese commons)` and was at least 3 seconds after the last.

| Site | What was read | Result |
|---|---|---|
| `https://www.indiacode.nic.in/robots.txt` | 2026-10-21 | **403 Access Denied**. Use of that host stopped there. |
| `https://indiacode.gov.in/robots.txt` | 2026-10-21 | **500** (an HTML error page, 148 bytes). RFC 9309 treats a 5xx on robots.txt as disallow for crawling, so no pages or section text were requested; only the portal's documented DSpace API, which answers JSON with HTTP 200, was queried for the Act's record. |
| `https://indiacode.gov.in/server/api` and `/server/api/discover/search/objects` | 2026-10-21 | **200**, `DSpace 9.1`. The API requests below are the logged ones; one earlier probe of `/server/api` (HTTP 200, 8,774 bytes) was made just before the log began, with the two robots.txt requests above:
  - 2026-10-21T09:02:23Z /server/api
  - 2026-10-21T09:02:27Z /server/api/discover/search/objects?query=%22General%20Clauses%20Act%22&size=5
  - 2026-10-21T09:02:58Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22General+Clauses+Act%2C+1897%22&size=10
  - 2026-10-21T09:03:01Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Companies+Act%2C+2013%22&size=10
  - 2026-10-21T09:03:05Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Bharatiya+Nyaya+Sanhita%2C+2023%22&size=10
  - 2026-10-21T09:03:08Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Indian+Penal+Code%22&size=10
  - 2026-10-21T09:03:11Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Income-tax+Act%2C+1961%22&size=10 |
