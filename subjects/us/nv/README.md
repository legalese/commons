# nevada/

Nevada (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

**Nothing is indexed, deposited or encoded yet.** The folder was opened on 2026-10-24 to record why: the state's official publisher refused this client, so the tax and benefits sample could not be sourced.

## Register access (2026-10-24)

Publisher: Nevada Revised Statutes, published by the Legislative Counsel Bureau (leg.state.nv.us). Requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds apart.

- `https://www.leg.state.nv.us/robots.txt` and `https://www.leg.state.nv.us/` on 2026-10-24: **HTTP 403** from Cloudflare (`Server: cloudflare`, `CF-RAY: ...-MNL`), page title "Attention Required! | Cloudflare": a bot challenge. **A no**; not worked around. Nothing was fetched, so no terms were read.

## What a tax and benefits sample would cover (unverified (general knowledge), for the next attempt)

- **Personal income tax:** Nevada levies no personal income tax (the Nevada Constitution, art. 10, s 1(9), as amended in 1989, bars one). A short NOTES finding would record this from the deposited Constitution, with whatever personal tax Nevada does levy that a person meets (none on wages).
- **Benefits:** NRS chapter 422A (welfare and supportive services: TANF at 422A.400 and following) and chapter 612 (unemployment compensation: 612.340 weekly benefit amount, 612.375 eligibility, 612.380 to 612.390 disqualification).

## To unblock

Fetch from a network the site does not refuse (the refusals look like a block on this client's network, not on the client name: the Cloudflare edge that answered Nevada was in Manila), or obtain the text from the publisher with permission. No mirror of the official site was tried, and none should be.
