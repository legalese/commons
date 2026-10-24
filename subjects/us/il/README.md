# illinois/

Illinois (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

**Nothing is indexed, deposited or encoded yet.** The folder was opened on 2026-10-24 to record why. Neither the official statute publisher nor the official rules publisher could be reached from this client, so the tax and benefits sample could not be sourced.

## Register access (2026-10-24)

Requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds apart.

- **Illinois Compiled Statutes and the Illinois Administrative Code**, both published by the General Assembly (www.ilga.gov; the Administrative Code is under the Joint Committee on Administrative Rules at ilga.gov/agencies/JCAR). Requests to `https://www.ilga.gov/robots.txt`, `https://ilga.gov/robots.txt` and `http://www.ilga.gov/legislation/ilcs/ilcs.asp` were made 4 times between about 02:20 and 03:35 UTC, and all failed: the TCP connection to ports 443 and 80 timed out after about 21 seconds ("Could not connect to server"). DNS resolves www.ilga.gov to 12.43.67.2. The General Assembly's other hosts that a search engine lists for statute files, my.ilga.gov and witnessslips.ilga.gov, timed out the same way. They were tried as the publisher's own hosts, not as mirrors.
- **Illinois Register**, published by the Secretary of State (www.ilsos.gov). robots.txt and the Register's home page each returned **HTTP 403** "Access Denied" from the Akamai edge (`errors.edgesuite.net`).
- **Department of Revenue** (tax.illinois.gov). This host answered: its robots.txt allows `User-agent: *`. But it hosts no statute or rule text. Its Legal Information page links to the Income Tax Act and to Title 86 of the Administrative Code on ilga.gov, which cannot be reached. Its regulations page redirects there too.
- **Department of Human Services** (www.dhs.state.il.us). The robots.txt answered (`Crawl-delay: 1`). Its cash assistance rules (89 Ill. Adm. Code 112) are published on ilga.gov. Its Policy Manual is administrative policy, not law, and was not used.

Unreachable hosts and 403s are a no. Nothing was worked around, and no mirror was tried.

## What a tax and benefits sample would cover (unverified (general knowledge), for the next attempt)

- **Personal income tax:** the Illinois Income Tax Act, 35 ILCS 5. It covers the flat rate (5/201), the base income starting from federal AGI (5/203), the exemption allowance (5/204), and the earned income credit and child tax credit (5/212).
- **Benefits:** the Illinois Public Aid Code, 305 ILCS 5, Article IV (TANF), with 89 Ill. Adm. Code 112 for the payment levels; or the Unemployment Insurance Act, 820 ILCS 405.

## To unblock

Fetch from a network the ilga.gov hosts do not refuse, or obtain the text from the publisher with permission.
