# south-australia/

South Australian Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

**579 Acts are indexed here. None is sourced yet, and nothing is encoded.**

## Indexed

Every principal Act on the South Australian *Current Titles* list of 22 September 2026 has a subject folder with `subject.json`, `SOURCE-LICENSE.md` and `registers/source-bundle/<id>.meta.json`.
Fourteen were laid out on 2026-09-22 for twelve everyday topics (payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits); the other 565 were added on 2026-10-19 from the same list.
Each new `meta.json` carries the version the list gave (`listed_version`, as `d.m.yyyy`).

Eight entries appear on the list with only an uncommenced version stamp: Animal Welfare Act 2025, Biodiversity Act 2025, Biosecurity Act 2025, Children and Young People (Safety and Support) Act 2025, Explosives Act 2024, Scrap Metal Dealers Act 2025, Social Workers Registration Act 2021, and Environment Protection (Sea Dumping) Act 1984.
Their `meta.json` has a `note` saying the Act may not yet be in force.
Some of them (the 1984 Act certainly) are in force with an amendment pending, and the stamp sits where the list wrapped a line; the register must settle each one.

The list could not be re-read on 2026-10-19 (see below), so an Act passed, commenced or repealed after 22 September 2026 is not yet reflected here.

## Not yet sourced

No statute text is deposited.
On 2026-10-19 the register's documents, for example the current RTF of the Electricity Act 1996 at
`https://www.legislation.sa.gov.au/_legislation-documents/lz/c/a/electricity-act-1996/current/1996.96.un.rtf`,
answered a scripted client with HTTP 403 and a Cloudflare managed challenge (`Cf-Mitigated: challenge`, "Enable JavaScript and cookies to continue").
The Copyright page and the Current Titles page answered the same way.
The fetch stopped there: this repository does not route around bot protection.
The Act landing pages (`/lz?path=/C/A/<TITLE>`) and the Disclaimer page did load, and show where each text lives: every Act has `current/<year>.<number>.un.rtf` (unauthorised, the one to convert) and `current/<year>.<number>.auth.pdf` (the authorised version) under `_legislation-documents/lz/c/a/<slug>/`.
Sourcing needs either scripted access allowed by the site's operator (the Attorney-General's Department) or another lawful route to the same texts.

## Terms

Read on 2026-10-19:

- `https://www.legislation.sa.gov.au/robots.txt` allows `/lz` and `/_legislation-documents`, disallows `/search` and the CMS's own paths, and sets `Crawl-delay: 10`.
- The footer of every page: "Except where otherwise noted content on this site is licensed under a Creative Commons Attribution 4.0 International Licence (CC BY 4.0). See Copyright for more information."
- `https://www.legislation.sa.gov.au/copyright` (read on 2026-09-22: CC BY 4.0) was behind the bot challenge.
- `https://www.legislation.sa.gov.au/disclaimer`: the State accepts no liability for accuracy except as set out there; legislation published under the *Legislation Revision and Publication Act 2002* is the authorised version, identified by a tick logo at the point of download and a statement at the foot of each page.

Each subject's `SOURCE-LICENSE.md` records the licence and the attribution it requires.
