# Source license

The text of **Indiana Code Title 6, Article 3.1, Chapter 21 (Earned Income Tax Credit)** is published on the [Indiana General Assembly - Indiana Code (published by the Legislative Services Agency)](https://iga.in.gov/laws/current/ic).

- **Terms**: none found on iga.in.gov at the reading of 2026-09-23 (no copyright notice, licence or terms; the footer ends with the Statehouse address). The statewide terms at www.in.gov could not be read (connection timeout on 2026-09-23 and 2026-10-20).
- **Terms checked**: 2026-09-23, at https://iga.in.gov/information/faq (not re-readable on 2026-10-20: see below)
- **Attribution required**: none known; cite as Indiana Code (Indiana General Assembly, Legislative Services Agency)
- **Source**: https://iga.in.gov/laws/current/ic/titles/6#6-3.1-21

In the United States the text of a statute is not copyrightable: it is an edict of government (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). The owner ruled on 20 Oct 2026 that Legalese Commons counts as non-commercial use; no Indiana condition is known that would need that ruling.

## Consequence for this subject

**Index only.** The terms do not stand in the way. The register cannot be read without a rendering browser or an API key.

## Language

English is the sole language of the Indiana Code.

## Access check of 2026-10-20: no permitted route, index only

Every request was sent with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds apart, and every one is logged. No browser automation was used.

- **robots.txt**: `https://iga.in.gov/robots.txt` returns the app's 691-byte HTML shell (HTTP 200, text/html). That is not a robots file, so it was treated as absent.
- **Plain HTTP**: every path on iga.in.gov returns the same 691-byte shell, with the CloudFront header `X-Cache: Error from cloudfront`. That covers the Code pages (`/laws/2026/ic/titles/6`), the static data file the app reads (`/ic/2026/Title_6.json`), `/manifest.json`, and even the JavaScript bundle that the shell itself loads (`/static/js/main.0fd45481.js`). The shell is CloudFront's error document, served with status 200. The data the app reads in a browser never reaches this client, and changing the Accept header made no difference. The cause is not known: it may be a filter on headers, referrer or origin, or the site may need a rendering browser. It was not probed further or worked around.
- **API**: the documented API host `api.iga.in.gov` requires an `x-api-key`; without one it answers HTTP 403 `{'error': '403', 'message': 'x-api-key not found'}` (recorded 2026-09-23). Getting a key means registering an account, which this agent may not do.
- **Other official routes**: none was found that avoids iga.in.gov. The state portal www.in.gov (which hosts the statewide terms page) timed out on connect again on 2026-10-20 (`ConnectTimeout` on `/robots.txt`), so its robots rules and terms could not be read, and nothing was requested there.
- **Terms**: the register's terms page (`https://iga.in.gov/information/faq`) is inside the same app, so it could not be re-read today. The earlier reading of 2026-09-23, made in a real browser, found no copyright notice, licence or terms on iga.in.gov. The statewide terms at www.in.gov remain unread. Verdict as planned: clean on the register's own terms, but **unreachable without a rendering browser or an API key**.

**To unblock**: (a) a human requests an IGA API key (api.iga.in.gov) for Legalese Commons, and the owner confirms its terms; or (b) the owner approves a rendering-browser fetch of the app's own static files `https://iga.in.gov/ic/<year>/Title_<n>.json`, as the 2026-09-23 index check did; or (c) a US egress re-check, in case the CloudFront error is network-specific.

## Status of this deposit

No statute text has been deposited. The citation and chapter names are unverified (general knowledge) unless `verified_how` in the `.meta.json` says otherwise.
