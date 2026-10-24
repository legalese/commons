# nova-scotia/

Nova Scotia (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Nova Scotia Office of the Legislative Counsel - Consolidated Statutes (nslegislature.ca/legc/statutes), UNREACHABLE; title and citation verification fell back to the Government of Nova Scotia Office of the Registrar of Regulations (novascotia.ca/just/regulations); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

BLOCKED at the network level. Every attempt to reach nslegislature.ca - the only official source of Nova Scotia's consolidated statutes - failed with 'connect ECONNREFUSED 64.15.49.119:443'. Attempts on 2026-09-23: four fetches (https://nslegislature.ca/legislative-business/legislation, https://nslegislature.ca/legc/statutes/, https://nslegislature.ca/legc/statutes/index.htm and https://www.nslegislature.ca/sites/default/files/legc/statutes/labour%20standards%20code.pdf) plus two loads in a real browser, which both reported 'navigation to https://nslegislature.ca was denied or failed'. That is a refused connection rather than a 403 or a bot challenge, and no workaround was attempted. The separate Government of Nova Scotia domain novascotia.ca IS reachable, so the Office of the Registrar of Regulations was used to verify Act titles and chapter citations: about 12 requests, spaced about 1.8s apart, with the honest User-Agent 'canon-legislation-indexer/1.0 (contact address removed)' - the 'Regulations by Act' index plus one regulation page per target Act, each of which recites its enabling Act and citation. That site is official but it is the register of REGULATIONS, and it labels its own consolidations 'unofficial and ... for reference only', so every Act below is recorded with in_force 'unclear'. A human on a network that can reach nslegislature.ca must confirm in-force status and as-at dates, and read the Legislative Counsel site's own terms. CanLII was not used: it refuses this network.

## Topics with no legislation here

- **Passenger compensation**: No provincial passenger-compensation statute identified. Air, rail and marine passenger rights are federal: Canada Transportation Act, SC 1996 c 10, and the Air Passenger Protection Regulations, SOR/2019-150. Nova Scotia's Motor Carrier Act licenses intra-provincial passenger carriers but is not a compensation statute, and it could not be checked on the register in any event.
- **Customs/duties**: Federal matter: Customs Act, RSC 1985 c 1 (2nd Supp), and Customs Tariff, SC 1997 c 36.
- **Work permits/immigration**: Federal matter: Immigration and Refugee Protection Act, SC 2001 c 27. The Nova Scotia Nominee Program and the Atlantic Immigration Program operate under federal-provincial agreements, not under a provincial statute.

## Tax and benefits: not sourced (2026-10-24)

The aim on 2026-10-24 was the **Income Tax Act** (R.S.N.S. 1989, c. 217) for personal income tax and the **Employment Support and Income Assistance Act** (S.N.S. 2000, c. 27) with its Regulations (N.S. Reg. 195/2019) for income assistance. **Nothing was deposited**, for two reasons:

1. **The statutes are still unreachable.** A request for https://nslegislature.ca/robots.txt with the user agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)` failed to connect after 21 seconds ("Could not connect to server"). A host that hangs is a no; nothing else was tried.
2. **The regulations carry terms that go to Michael.** The Office of the Registrar of Regulations (novascotia.ca/just/regulations, robots.txt read, not disallowed) is reachable, but:
   - the Government of Nova Scotia's copyright page, https://novascotia.ca/copyright (read 2026-10-24), permits non-commercial reproduction only if, among other things, "materials must not be modified and the reproduction must be accurate";
   - every consolidation carries the Registrar's disclaimer, which "must not be removed" (https://novascotia.ca/just/regulations/consregs.htm, read 2026-10-24), including: "This electronic version is copyright © [year], Province of Nova Scotia, all rights reserved. It is for your personal use and may not be copied for the purposes of resale in this or any other form." The Employment Support and Income Assistance Regulations page (https://novascotia.ca/just/regulations/regs/esiaregs.htm, consolidated to O.I.C. 2026-315, N.S. Reg. 200/2026, effective September 3, 2026) carries it word for word.

   A no-modification term and a personal-use term are outside the rulings of 20 and 24 October 2026, so the regulations are **reported to Michael** and not deposited. Five requests were made to novascotia.ca (robots.txt, the copyright page, the regulations home and index, the disclaimer page, the ESIA Regulations page), at least 3 s apart.
