# nebraska/

Nebraska (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

**Nothing is indexed, deposited or encoded yet.** The folder was opened on 2026-10-24 to record why: the state's official publisher refused this client, so the tax and benefits sample could not be sourced.

## Register access (2026-10-24)

Publisher: Nebraska Revised Statutes, published by the Nebraska Legislature (nebraskalegislature.gov). Requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds apart.

- `https://nebraskalegislature.gov/robots.txt`: no connection on 2026-10-24 (curl: "Failed to connect to nebraskalegislature.gov port 443 after 21578 ms"); `http://nebraskalegislature.gov/` (port 80) the same a few minutes later.
- Treated as a site that hangs: **a no**. Nothing was fetched, so no terms were read.

## What a tax and benefits sample would cover (unverified (general knowledge), for the next attempt)

- **Personal income tax:** Neb. Rev. Stat. chapter 77, article 27 (77-2714 to 77-27,123: 77-2715 tax imposed and rate schedules, 77-2715.07 credits including the earned income credit, 77-2716 adjustments to federal AGI, including the social security exclusion).
- **Benefits:** chapter 68, article 17 (Welfare Reform Act, aid to dependent children) and 68-1001 and following; chapter 48, article 6 (Employment Security Law: 48-624 weekly benefit amount, 48-627 eligibility, 48-628 disqualification).

## To unblock

Fetch from a network the site does not refuse (the refusals look like a block on this client's network, not on the client name: the Cloudflare edge that answered Nevada was in Manila), or obtain the text from the publisher with permission. No mirror of the official site was tried, and none should be.
