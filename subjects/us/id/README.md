# idaho/

Idaho (US state) legislation. Each body of law gets one subject-id, in the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

**Nothing is indexed, deposited or encoded yet.** The folder was opened on 2026-10-24 to record why. Neither the state's official statute publisher nor its rules publisher could be reached from this client, so the tax and benefits sample could not be sourced.

## Register access (2026-10-24)

Every request used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, with requests at least 3 seconds apart.

- **Idaho Statutes.** These are published by the Idaho Legislature (legislature.idaho.gov). `https://legislature.idaho.gov/robots.txt` and `https://legislature.idaho.gov/` were tried 3 times between about 02:20 and 03:30 UTC. Each time the TCP connection to port 443 timed out after about 21 seconds ("Could not connect to server"). DNS resolves the host to 164.165.66.180. A browser on the same network was also refused (`https://legislature.idaho.gov/statutesrules/idstat/`).
- **Idaho Administrative Code (IDAPA).** This is published by the Office of the Administrative Rules Coordinator (adminrules.idaho.gov). The connection to its robots.txt timed out the same way. The same happened with the State Tax Commission (tax.idaho.gov) and www.idaho.gov.
- **Department of Health and Welfare.** healthandwelfare.idaho.gov did answer: its robots.txt allows the public pages. But it hosts no rule or statute text. Its rules, including IDAPA 16.03.08 (Temporary Assistance for Families in Idaho), are published only at adminrules.idaho.gov.

A host that cannot be reached counts as a no. Nothing was worked around. No proxy, other user agent or mirror was tried, and none should be.

## What a tax and benefits sample would cover

This is unverified (general knowledge), noted for the next attempt.

- **Personal income tax:** Idaho Code Title 63, chapter 30 (Idaho Income Tax Act). It starts from federal taxable income, and has a flat rate, the grocery credit and the child tax credit.
- **Benefits:**
  - Idaho Code Title 56, chapter 2 (public assistance), with IDAPA 16.03.08 (TAFI: eligibility, income limits, the grant amount);
  - Title 72, chapter 13 (Employment Security Law: weekly benefit amount and eligibility).

## To unblock

Any of these would work:
- fetch from a network that the Idaho state hosts do not refuse (the refusals look like a block on this client's network, not on the client name);
- obtain the text from the publishers with permission.
