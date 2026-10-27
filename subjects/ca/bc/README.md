# british-columbia/

British Columbia (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the BC Laws (King's Printer, Province of British Columbia) - CiviX; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. When the subjects were laid out, no statute text had been deposited and nothing was encoded; the last section says what has been added since.

**Licence category: open.** Statute text may be deposited and quoted in an encoding, subject to the attribution above.

## Topics with no legislation here

- **Passenger compensation**: This is a federal matter. Air passenger compensation comes from the Canada Transportation Act and the Air Passenger Protection Regulations. BC's Passenger Transportation Act licenses commercial passenger vehicles but does not provide a passenger compensation scheme.
- **Customs/duties**: This is exclusively federal (the Customs Act and the Customs Tariff). BC has no provincial customs legislation.

## Sourcing for tax and benefits refused by robots.txt (2026-10-24)

Sourcing was attempted on 2026-10-24 for the tax-and-benefits sample: the Income Tax Act (RSBC 1996, c. 215), the Employment and Assistance Act (SBC 2002, c. 40) and the Employment and Assistance for Persons with Disabilities Act (SBC 2002, c. 41), with their regulations' rate schedules (B.C. Reg. 263/2002 and 265/2002). **Nothing was deposited.** https://www.bclaws.gov.bc.ca/robots.txt (fetched 2026-10-24, HTTP 200, sha256 `5bf5d269f0454b901d1c294ab1e67819b725cfd549b222dac7218811e8a582a1`) allows only Googlebot and Bingbot and disallows everything else:

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# Block everything else
User-agent: *
Disallow: /
```

Under the sourcing rules that is a no, so no statute or regulation page was requested. Two requests were made in all, User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, 3 seconds apart: robots.txt and the licence page (https://www.bclaws.gov.bc.ca/standards/Licence.html, HTTP 200, unchanged from the September reading: King's Printer Licence - British Columbia, use, copy, publish and distribute for commercial or non-commercial purposes, with the mandatory attribution and "THESE MATERIALS ARE NOT AN OFFICIAL VERSION" statement). The licence would allow deposit and quotation; only access is in the way. No other host, client or mirror was tried, and unofficial aggregators were not used.

**A human decision is needed:** whether BC Laws' own developer API and CiviX document links may be fetched for a request-by-request deposit notwithstanding the blanket `Disallow: /` (for example with the King's Printer's written permission), or whether the texts should be saved by hand from the site and deposited.

## Interpretation Act

`interpretation-act/` holds the Interpretation Act, RSBC 1996, c. 238, as a plain-text rendering of the King's Printer consolidation current to 2026-10-13.
The text is under the King's Printer Licence – British Columbia, which requires an attribution statement with every reproduction; each file that quotes the text carries it.
The first encoding is `interpretation-act/encodings/legalese-sonnet-5.5/`, written by one Sonnet 5.5 agent against the `unstable` compiler.
It encodes the rules for counting periods of days, weeks, months and years, commencement, repeal and the defined terms, and lists the canons of construction as inert, each with a reason.
Whether an encoding that quotes the text is within clause 2.2 of the licence has not been decided; the row's `SOURCE-LICENSE.md` says so.
No one has read the encoding against the official text.
