# alberta/

Alberta (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Alberta King's Printer - Laws Online / Catalogue; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over HTTPS with curl identifying itself as 'canon-legislation-indexer/1.0 (metadata indexing)'; requests spaced about 2 seconds apart; roughly 18 requests in all, every one HTTP 200. No block, no rate limit, no bot challenge at any point. https://kings-printer.alberta.ca/default.aspx 301-redirects to https://www.alberta.ca/alberta-kings-printer.aspx, but the catalogue itself is still served from kings-printer.alberta.ca. Browsing is by letter (570.cfm?search_by=alpha&letter=A..Y); each catalogue entry is keyed by ISBN (570.cfm?frm_isbn=...&search_by=link) and states the title, Chapter/Regulation, Status, responsible ministry and a 'Current to' date, which is enough to verify without opening statute text. The Laws Online index header states 'Acts current to 2026-08-31' and 'Regulations current to 2026-09-02'. Free 'View PDF' and 'View HTML' links sit beside priced MS Word and paper copies (e.g. $10.00 for the Employment Standards Code, $33.00 for the Insurance Act), so the official consolidations can be read at no charge even though the King's Printer also sells them - the old assumption that Alberta puts its statutes behind a paywall is no longer right. Alberta King's Printer is the official publisher; no commercial publisher is involved.

## Topics with no legislation here

- **Passenger compensation**: Federal matter: compensation for denied boarding, delay, cancellation and lost baggage is set by the Air Passenger Protection Regulations, SOR/2019-150, made under the Canada Transportation Act, S.C. 1996, c. 10; interprovincial rail and bus carriage is federal too. No provincial statute provides a passenger-compensation scheme.
- **Customs/duties**: Federal matter: customs and tariffs are exclusively federal under s. 91(2)-(3) of the Constitution Act, 1867 - the Customs Act, R.S.C. 1985, c. 1 (2nd Supp.) and the Customs Tariff, S.C. 1997, c. 36. No provincial statute governs it.
- **Work permits/immigration**: Federal matter: work permits and immigration status are granted under the Immigration and Refugee Protection Act, S.C. 2001, c. 27, and the Immigration and Refugee Protection Regulations, SOR/2002-227. Alberta selects candidates through the Alberta Advantage Immigration Program under an agreement with Canada rather than by statute. Alberta does have a statute in this space - the Immigration Oversight Act, S.A. 2026, c. I-0.3, which the King's Printer catalogue (https://kings-printer.alberta.ca/570.cfm?frm_isbn=9780779862382&search_by=link) shows with Status 'Awaiting Proclamation' - but it is not yet in force, and it regulates recruiters and immigration-services providers rather than granting work permits.

## Licence ruling of 2026-10-24

Michael ruled on 2026-10-24 that Canadian texts whose terms permit reproduction but are silent on adaptation may be quoted in L4 encodings in Commons, keeping the attribution each publisher requires and an "unofficial version / not an official version" notice in the text header and `SOURCE-LICENSE.md`. The Alberta King's Printer's terms are of that kind (reproduction permitted without permission or charge, on due diligence and the acknowledgement "(c) Alberta King's Printer, 20__."), so the "metadata only until resolved" note above is resolved for quotation: Alberta text, once deposited, may be quoted in an encoding with that acknowledgement and an unofficial-version notice.

## Sourcing for tax and benefits refused by robots.txt (2026-10-24)

Sourcing was attempted on 2026-10-24 for the tax-and-benefits sample: the Alberta Personal Income Tax Act (R.S.A. 2000, c. A-30), the Income and Employment Supports Act (S.A. 2003, c. I-0.5) with the Income Supports, Health and Training Benefits Regulation, and the Assured Income for the Severely Handicapped Act (S.A. 2006, c. A-45.1) with its general regulation. **Nothing was deposited.** https://kings-printer.alberta.ca/robots.txt (fetched 2026-10-24, HTTP 200, sha256 `133e4db054e73a10017a1f429c80c35cd5bfa9c3a1aba581b364ecc459c48a4b`) reads in full:

```
User-agent: *
Disallow: /
```

Under the sourcing rules that is a no, so no catalogue entry, PDF or HTML of any Act or regulation was requested. Two requests were made in all, User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, 3 seconds apart: robots.txt and the copyright page (https://kings-printer.alberta.ca/copyright.cfm, HTTP 200, unchanged from the September reading). The September indexing above read about 18 catalogue pages from the same host; robots.txt was not recorded then. No other host, client or mirror was tried, and unofficial aggregators were not used.

**A human decision is needed:** whether the King's Printer will permit fetching despite `Disallow: /`, or whether the texts should be saved by hand from Laws Online (the free "View PDF"/"View HTML" links) and deposited; the reproduction terms and the ruling above would then allow them to be quoted.
