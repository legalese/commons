# Source license

The text of **106 CMR 704.000, Transitional Cash Assistance Program: Financial Eligibility**, and the **TAFDC Table of Need and Payment Standards 704.410-704.420**, are published by the Massachusetts Department of Transitional Assistance on [Mass.gov](https://www.mass.gov/regulations/106-CMR-70400-transitional-cash-assistance-program-financial-eligibility), the official website of the Commonwealth.

- **Terms**: Mass.gov Terms of Use, https://www.mass.gov/massgov-terms-of-use (read 2026-10-24), under "Public records and copyright": "All of the material posted on the Commonwealth's websites and available to the public without use of an authenticating and authorizing mechanism ... is public record. Most of the public record posted on Commonwealth websites can be copied and used for any purpose. For example, all judicial opinions and all laws and regulations are public record." The same section says the Commonwealth holds copyright in "most of the content on Mass.gov" and forbids copying other than fair use, with the exception that laws and regulations "can be copied and used for any purpose"; it also excepts "regulations based on technical codes developed and copyrighted by private organizations", which 106 CMR 704 is not.
- **Verdict**: deposit allowed. Both files are regulation text: 106 CMR 704 itself, and the figures that 106 CMR 704.410 and 704.420 say "are posted" by the Department. Only those two are deposited; no other Mass.gov content (guides, explanations) is.
- **robots.txt**: https://www.mass.gov/robots.txt (read 2026-10-24) disallows `/search/`, `/node/*`, `/media/*`, admin paths and a court download pattern; `/regulations/`, `/doc/` and `/lists/` are not disallowed.
- **Requests**: 6 to www.mass.gov on 2026-10-24 (robots.txt, the Site Policies page, the Terms of Use, the regulation page, its PDF, the standards page), one at a time and at least 4 seconds apart, User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. No block or challenge. One more request, to the address the regulation gives for the figures (www.mass.gov/dta/TAFDCPayments), answered HTTP 404.
- **Attribution**: 106 CMR 704.000, Department of Transitional Assistance, Commonwealth of Massachusetts (Mass.gov).

## Language

English.

## Status of this deposit

Deposited 2026-10-24.

- `registers/source-bundle/106-cmr-704-transitional-cash-assistance-financial-eligibility.txt`: 106 CMR 704.000 to 704.510, the whole chapter, converted from the official PDF (pages dated 5/10/24) with pypdf; the PDF carries most of its text twice and both layers are kept. 210,313 characters; text sha256 `dc427e5e2c73db83cbb9bc3223d4112ce949f94e7c17236842b37eaf8321b0a0`.
- `registers/source-bundle/tafdc-table-of-need-and-payment-standards-704410-704420.txt`: the posted table and the September 2026 clothing allowance note. 1,964 characters; text sha256 `9bcd7d4dd1a0c5ec4e4afbb71b03558d98babc728e7d7c03acc7f7bfc3af5094`.

Each has a `.meta.json` with the URLs, retrieval times, byte counts and sha256s of what was fetched.

**Not deposited**: the statute the regulation carries out (M.G.L. c. 118, and c. 18 s 10 cited as its authority): the General Court's site, malegislature.gov, did not answer the fetcher (see `../README.md`). The other chapters of 106 CMR (701 general policies, 703 nonfinancial eligibility, 705 grant details including the rent allowance rule) were not fetched in this pass.
