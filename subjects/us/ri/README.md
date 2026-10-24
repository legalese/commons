# rhode-island/

Rhode Island (US state) law, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

This folder was opened on 2026-10-24 for "tax and benefits" (docs/ENCODING-GUIDE.md section 6): personal income tax, and social security and benefits.

## Register access (2026-10-24)

- **General Laws (statutes)**: the Rhode Island General Assembly's sites did not respond. Neither `webserver.rilegislature.gov` (the General Laws, e.g. `/Statutes/TITLE44/44-30/INDEX.htm`) nor `www.rilegislature.gov` answered. Every request ended in a connection timeout, on three tries at least 3 seconds apart, with the honest User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. The same pattern was met on 2026-10-24 for the Ohio, Oregon and Oklahoma (OSCN) legislature hosts, and it looks like a block on traffic from outside the United States. That is unverified. No workaround was tried: no proxy, no other user agent, no mirror. So **no statute text is deposited**, including the personal income tax (R.I. Gen. Laws ch. 44-30) and the RI Works Act (ch. 40-5.2).
- **Rhode Island Code of Regulations** (Department of State, `rules.sos.ri.gov`): reachable. It has no robots.txt (404) and no terms of use. Rules are edicts of government. **Licence category: open.**

## Subjects

| subject | deposited | encoded |
| --- | --- | --- |
| [`rhode-island-works-program-rules-and-regulations`](rhode-island-works-program-rules-and-regulations) | 218-RICR-20-00-2 (RI Works, Rhode Island's TANF cash assistance), in force on 2026-10-24, and the Amendment effective 2026-11-10 | [`baseline-2026-10`](rhode-island-works-program-rules-and-regulations/encodings/baseline-2026-10), from the parent's or caretaker's seat. Covers the child's age, resources and vehicles, the payment standard, net adjusted income (the $525-plus-half disregard, dependent care, set aside, child support), the monthly payment and the $10 minimum, the 60-month limit and hardship, the work penalty, reporting duties, notice and hearing |

## Not reached

- **Personal income tax.** The statute (R.I. Gen. Laws ch. 44-30: rates, standard deduction, exemptions, the state EITC) could not be fetched. The Division of Taxation's rules under 280-RICR-20-55 are reachable, but they cover procedure and special cases (estimated payments, extensions, the credit for other states' tax, part-year residents). They hold no rate schedule, so they cannot answer "how much do I owe?". They are not deposited.
