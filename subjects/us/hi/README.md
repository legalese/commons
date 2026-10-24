# hawaii/

Hawaii (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Hawaii Revised Statutes, published by the Hawaii State Legislature (Legislative Reference Bureau, Revision of Statutes Division); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

BLOCKED — the register could not be read at all. Every request to www.capitol.hawaii.gov returned HTTP 403 behind a Cloudflare interstitial reading 'Sorry, you have been blocked / You are unable to access capitol.hawaii.gov', for the HRS index, the /hrscurrent/ directory and an individual chapter page alike. The same 403 was returned to the WebFetch tool and to a full browser, so this is a network-level block on the host, not a bot challenge I could have satisfied, and I made no attempt to work around it. The Legislature's alternate host data.capitol.hawaii.gov returned HTTP 522 (origin timeout) on two attempts, as did labor80.hawaii.gov. About 10 requests in total, spaced ~1.8 s apart. The block is consistent with the state's published terms of use, which forbid automated access outright (quoted below). The Legislative Reference Bureau site (https://lrb.hawaii.gov/statute-revision/), which is reachable, describes the HRS and its supplements but hosts no statutory text. Everything below was therefore corroborated only from Hawaii state agency pages that cite their own enabling chapters — an official government source, but not the register — so no HRS entry below has a verified in-force status or as-at date. THIS JURISDICTION NEEDS RE-VERIFICATION FROM capitol.hawaii.gov ON AN UNBLOCKED NETWORK.

## Topics with no legislation here

- **Passenger compensation**: No state statute identified, and the register was blocked so this could not be checked exhaustively. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250). Interisland carriers are regulated by the PUC under HRS ch. 271G as to certification and rates, not passenger compensation.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Hawaii's HRS ch. 390 (Child Labor Law) requires a 'work permit' — a child labor certificate for working minors until age 18, per the DLIR Wage Standards Division page — but that is a different subject and confers no immigration permission.

## Tax and benefits sample (2026-10-24): not deposited, terms bar automated access

A tax and benefits pass was tried on 2026-10-24 and found no route that may be used. **Nothing was deposited or encoded.**

**The register.** www.capitol.hawaii.gov (robots.txt, `/hrscurrent/` section pages) and data.capitol.hawaii.gov still return HTTP 403 behind Cloudflare's "Attention Required!" page. That was 4 requests, with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`.

**State agency copies.** The Department of Human Services publishes the Hawaii Administrative Rules for its programmes as PDFs at https://humanservices.hawaii.gov/admin-rules-2/admin-rules-for-programs/. Among them:
- HAR ch. 17-656.1, Temporary Assistance for Needy Families;
- ch. 17-655, General Eligibility Requirements;
- ch. 17-676, Income;
- ch. 17-678, Financial Assistance Standards, amended and adopted 26 January 2025, which sets the payment standard;
- ch. 17-659, General Assistance.

The Department of Taxation (tax.hawaii.gov) answered too. Both hosts' robots.txt set only `Crawl-delay: 10`.

**The terms rule it out.** The State of Hawaiʻi Terms of Use were read in a browser on 2026-10-24 at https://portal.ehawaii.gov/page/terms-of-use/. They define "web site" as any official State site, including pages whose addresses contain "hawaii.gov". They also say: "You specifically agree not to access, or attempt to access, ... any of the Services through any automated means (including, but not limited to, use of scripts, web crawlers or screen scrapers)". That is a bar on scripted access to every hawaii.gov host, including the DHS and Taxation sites, and it goes to Michael under the deposit rules. The DHS rules page also carries "Copyright © 2026, State of Hawaii. All rights reserved."

Before the terms were read, five scripted requests had gone to those agency hosts, 3-10 seconds apart: tax.hawaii.gov robots.txt and its Law & Guidance page, and humanservices.hawaii.gov robots.txt, its sitemap index, its page sitemap and its administrative rules page. No rule or statute file was downloaded. lrb.hawaii.gov's robots.txt was also read; that site hosts no statute text.

**Indexed for a later pass.** These would give Hawaii a tax and benefits sample once a permitted route exists, for example a human download with the State's permission, or a licence decision by Michael:
- HRS ch. 235 (income tax law), already a subject here;
- HRS ch. 346 (Department of Human Services), already a subject here;
- HAR ch. 17-656.1 (TANF) and ch. 17-678 (financial assistance standards), at the DHS addresses above;
- HRS ch. 383 (employment security), not yet a subject.

The text under each item is a government edict and is not copyrightable (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). The bar is on the delivery channel.
