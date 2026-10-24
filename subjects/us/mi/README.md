# michigan/

Michigan (US state) law, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md). Folder opened on 2026-10-24 to record a sourcing attempt; **no law is indexed, deposited or encoded yet.**

## Tax and benefits sample: not reached (2026-10-24)

The aim was a sample on personal income tax (the Income Tax Act of 1967, MCL 206.1 and following) and benefits (the Social Welfare Act, MCL 400.1 and following, for the Family Independence Program); citations unverified (general knowledge). Both are published officially only in the Michigan Compiled Laws on the Legislature's site, legislature.mi.gov.

**The hosts refused the connection.** Every request carried the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`:

| When (UTC, 2026-10-24) | Request | Result |
|---|---|---|
| about 02:30 | https://www.legislature.mi.gov/robots.txt | no connection (curl exit 7, after about 3 s) |
| about 02:31 | https://legislature.mi.gov/ | "Connection refused" on port 443 (198.109.173.29) |
| about 03:00 | https://www.michigan.gov/robots.txt | HTTP 403 |
| 03:56 | https://legislature.mi.gov/robots.txt, https://www.legislature.mi.gov/robots.txt, http://legislature.mi.gov/robots.txt | no connection on each |

A refused connection and a 403 are treated as a no. No other identity, proxy, mirror or third-party copy of the Compiled Laws was tried. The refusal may be a block on the network the requests came from; that was not tested.

**To do when the site answers:** read its terms and robots.txt; index and deposit MCL 206 (income tax: the rate in MCL 206.51, the personal exemption in MCL 206.30, the earned income tax credit in MCL 206.272) and the Social Welfare Act provisions for the Family Independence Program (MCL 400.57 and following) (the section numbers are unverified (general knowledge)); the payment standards are in the Department of Health and Human Services' manuals (administrative policy) unless deposited.
