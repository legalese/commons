# Source license

**The Indian Penal Code, 1860** is recorded in the market register as repealed by The Bharatiya Nyaya Sanhita, 2023 (Act No. 45 of 2023), s.358(1); that clause was not re-read for this subject. This subject records the Act so that its place in the market register has a directory; no text of it has been sourced.

- **Terms**: No open licence found for Acts on India Code. The terms recorded for India Code in [`../the-income-tax-act-2025/SOURCE-LICENSE.md`](../the-income-tax-act-2025/SOURCE-LICENSE.md) (checked there 2026-09-22 via a Wayback copy of disclaimer.jsp, not re-verified here) are that India Code publishes no copyright licence, and that Copyright Act 1957 s.52(1)(q)(ii) makes reproducing or publishing an Act of a Legislature non-infringing only if it comes with commentary or other original matter. Bare reproduction and adaptation of Act text is therefore conditional, not clearly permitted.
- **Terms checked**: 2026-10-21, at the two India Code robots.txt files (see below). The disclaimer page was not re-read.
- **Attribution required**: none stated; source acknowledgement advisable
- **Source**: https://www.indiacode.nic.in/handle/123456789/496548 (the record or gazette of the repealing Act, not of this Act)

## Consequence for this subject

**Metadata only until resolved.** The s.52(1)(q)(ii) decision is a human one and is open, and no source for this Act's own text has been chosen. The text to deposit (as enacted, or as it stood on the day before the Sanhita commenced, with the State amendments set aside) is a decision for whoever sources it.

## Status of this deposit

No statute text has been deposited. India Code's DSpace API returned only two Indian Penal Code, 1860 records, both State versions (Chhattisgarh 123456789/549142, Rajasthan 123456789/588124), and no central one: queries on the title, and on act year 1860 with act number 45, found nothing else (2026-10-21).

## Access checks of 2026-10-21

Every request used the User-Agent `legalese-commons/1.0 (+https://github.com/legalese/commons; statute sourcing for Legalese commons)` and was at least 3 seconds after the last, except the two robots.txt probes.

| Site | Result |
|---|---|
| `https://www.indiacode.nic.in/robots.txt` | **403 Access Denied**. Use of that host stopped there. |
| `https://indiacode.gov.in/robots.txt` | **500** (an HTML error page, 148 bytes). RFC 9309 treats a 5xx on robots.txt as disallow for crawling, so no pages or section text were requested; only the portal's documented DSpace API (JSON, HTTP 200) was queried. |
| `https://archive.org/robots.txt` | **200**; the whole file (238 bytes) disallows only `/control/` and `/report/` for all agents, so `/download/` is permitted. The gazette OCR was fetched from `/download/`; the first attempt returned HTTP 500 from a storage node and the second succeeded. |

The requests in the fetch log of that day, in order:
  - 2026-10-21T09:02:23Z /server/api
  - 2026-10-21T09:02:27Z /server/api/discover/search/objects?query=%22General%20Clauses%20Act%22&size=5
  - 2026-10-21T09:02:58Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22General+Clauses+Act%2C+1897%22&size=10
  - 2026-10-21T09:03:01Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Companies+Act%2C+2013%22&size=10
  - 2026-10-21T09:03:05Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Bharatiya+Nyaya+Sanhita%2C+2023%22&size=10
  - 2026-10-21T09:03:08Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Indian+Penal+Code%22&size=10
  - 2026-10-21T09:03:11Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.title%3A%22Income-tax+Act%2C+1961%22&size=10
  - 2026-10-21T09:09:33Z /server/api/discover/search/objects?query=Indian+Penal+Code+1860&size=20&page=0
  - 2026-10-21T09:09:36Z /server/api/discover/search/objects?query=Income-tax+Act+1961&size=20&page=0
  - 2026-10-21T09:09:40Z /server/api/discover/search/objects?query=Income+Tax+Act+1961+Ministry+of+Finance&size=20&page=0
  - 2026-10-21T09:09:55Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.date.act_year%3A1860+AND+dc.identifier.act_number%3A45&size=20&page=0
  - 2026-10-21T09:09:58Z /server/api/discover/search/objects?query=dc.identifier.collection%3AACT+AND+dc.date.act_year%3A1961+AND+dc.identifier.act_number%3A43&size=20&page=0
  - 2026-10-21T09:10:23Z https://archive.org/download/in.gazette.central.e.2025-08-21.265620/265620_djvu.txt
  - 2026-10-21T09:10:28Z https://archive.org/advancedsearch.php?q=title%3A%28Bharatiya+Nyaya+Sanhita%29+AND+collection%3Agazetteofindia&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date&rows=10&output=json
  - 2026-10-21T09:10:39Z https://archive.org/download/in.gazette.central.e.2025-08-21.265620/265620_djvu.txt (-L)
  - 2026-10-21T09:11:14Z https://archive.org/download/in.gazette.central.e.2025-08-21.265620/265620_djvu.txt (-L, retry)
  - 2026-10-21T09:12:41Z https://archive.org/robots.txt (full read)
