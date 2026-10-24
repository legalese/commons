# new hampshire/

New Hampshire (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

**Nothing is indexed, deposited or encoded yet.** The folder was opened on 2026-10-24 to record why: the state's official publisher refused this client, so the tax and benefits sample could not be sourced.

## Register access (2026-10-24)

Publisher: New Hampshire Revised Statutes Annotated, published online by the General Court (gc.nh.gov, formerly gencourt.state.nh.us). Requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds apart.

- `https://www.gencourt.state.nh.us/robots.txt` on 2026-10-24: **HTTP 403**. `https://gc.nh.gov/robots.txt`, `https://gc.nh.gov/` and `https://www.gencourt.state.nh.us/rsa/html/indexes/default.html`: the connection was dropped (curl: "Failure when receiving data from the peer"), two attempts some minutes apart. **A no**; not worked around. Nothing was fetched, so no terms were read.

## What a tax and benefits sample would cover (unverified (general knowledge), for the next attempt)

- **Personal income tax:** New Hampshire has no tax on wages. Its interest and dividends tax (RSA chapter 77) was repealed for taxable periods beginning after 31 December 2024 (2023 legislation); a NOTES finding would record that from the deposited RSA 77.
- **Benefits:** RSA chapter 167 (public assistance to blind, aged or disabled persons and to dependent children: Financial Assistance to Needy Families, 167:77-a and following) and chapter 282-A (unemployment compensation: 282-A:25 weekly benefit amount, 282-A:31 eligibility, 282-A:32 disqualification).

## To unblock

Fetch from a network the site does not refuse (the refusals look like a block on this client's network, not on the client name: the Cloudflare edge that answered Nevada was in Manila), or obtain the text from the publisher with permission. No mirror of the official site was tried, and none should be.
