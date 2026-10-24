# ca/yt — Yukon

Yukon (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

No subject has been laid out here yet, and no text is deposited. This README records why.

## Register access (2026-10-24): refused

The official publisher of Yukon's consolidated statutes and regulations is **Yukon Laws** at <https://laws.yukon.ca/>, maintained by the Department of Justice, Government of Yukon. On 2026-10-24 it was approached for the tax and benefits sample: the Income Tax Act, R.S.Y. 2002, c.118, for personal tax, and the Social Assistance Act, R.S.Y. 2002, c.205, with its Social Assistance Regulation, for benefits.

- User agent: `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`.
- `https://laws.yukon.ca/robots.txt`: **HTTP 403**, a Cloudflare interstitial ("Just a moment...", `Cf-Mitigated: challenge`, Turnstile script, `noindex,nofollow`).
- `https://laws.yukon.ca/`: **HTTP 403**, the same challenge.

Two requests in all, at least 3 seconds apart. Under the sourcing rules a bot challenge is a refusal. No other user agent, client, proxy or mirror was tried, and nothing was fetched from any other host in place of the register. The site's terms of use could not be read, because they sit behind the same challenge.

**What it would take:** a person with a browser can download the consolidations by hand and hand them over, as was done for the FWC awards, after reading the site's terms. Michael would then decide on the licence. If the Yukon terms permit reproduction and are silent on adaptation, the ruling of 2026-10-24 would allow them to be encoded.

## Related deposit elsewhere

The Canada Revenue Agency page "Current year tax rates and income brackets (2026)", deposited in `../nt/income-tax-act/registers/source-bundle/cra-tax-rates-brackets-2026.txt`, prints the 2026 Yukon brackets. They are 6.4% to $58,523, 9% to $117,045, 10.9% to $181,440, 12.8% to $500,000, and 15% above that. The page is not law, and nothing here is encoded from it.
