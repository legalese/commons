# missouri/

Missouri (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

**Nothing is indexed, deposited or encoded yet.** The folder was opened on 2026-10-24 to record why: the state's official publisher refused this client, so the tax and benefits sample could not be sourced.

## Register access (2026-10-24)

Publisher: Missouri Revised Statutes, published by the Missouri Revisor of Statutes (Committee on Legislative Research). Requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds apart.

- `https://revisor.mo.gov/robots.txt`: no connection, two attempts on 2026-10-24 about 20 minutes apart (curl: "Failed to connect to revisor.mo.gov port 443 after 21112 ms"); `http://revisor.mo.gov/robots.txt` (port 80) and `https://www.revisor.mo.gov/robots.txt` the same.
- `https://revisor.mo.gov/main/Home.aspx` and `.../OneSection.aspx?section=143.011`: no connection (2026-10-24).
- DNS resolves (`revisor.mo.gov` -> 168.166.54.15); the host does not accept the connection. Treated as a site that hangs: **a no**. Nothing was fetched, so no terms were read.

## What a tax and benefits sample would cover (unverified (general knowledge), for the next attempt)

- **Personal income tax:** RSMo chapter 143 (sections 143.011 rates with the statutory triggers, 143.021, 143.101 resident, 143.111 Missouri adjusted gross income from federal AGI, 143.121 modifications, 143.124 social security subtraction, 143.131-143.161 deductions and exemptions, 143.177 Missouri working family tax credit, 143.481 returns).
- **Benefits:** RSMo chapter 208 (public assistance; temporary assistance 208.040 and following, supplemental aid to the blind) and chapter 288 (employment security: 288.030 definitions, 288.036, 288.038 weekly benefit amount, 288.040 eligibility, 288.050 disqualification).

## To unblock

Fetch from a network the site does not refuse (the refusals look like a block on this client's network, not on the client name: the Cloudflare edge that answered Nevada was in Manila), or obtain the text from the publisher with permission. No mirror of the official site was tried, and none should be.
