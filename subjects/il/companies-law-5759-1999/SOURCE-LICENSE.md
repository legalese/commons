# Source license

The text of **Companies Law, 5759-1999** (חוק החברות, התשנ"ט-1999) is Israeli primary legislation.

- **Copyright**: none. Under the Israeli Copyright Act, 5768-2007, s 6, there is no copyright in
  statutes, regulations, Knesset records or judicial decisions.
- **Official version**: https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_IsraelLaw?%24filter=IsraelLawID%20eq%202000289&%24format=json. Israel publishes no free official *consolidated* text: the
  official version of a law is its original publication in Reshumot together with every amending Act.
- **Working text**: https://he.wikisource.org/wiki/חוק_החברות
  ("Reshumot / Sefer HaChukim (רשומות, ספר החוקים), published by the Knesset; consolidated working text from "The Open Book of Laws" (ספר החוקים הפתוח) on Hebrew Wikisource"), a maintained consolidated Hebrew text. **Not an official version.**
- **Attribution**: none required for the statute text. Wikisource's own editorial additions, where
  any survive, are CC BY-SA 4.0.

## Consequence for this subject

Statute text may be deposited and quoted in an encoding. Record which text was used and its date:
a consolidated working text has no official status, so an encoding that relies on it must say so.

## Language

Hebrew is authoritative; English translations are unofficial. The English title above is a rendering, not an enacted title.

## Status of this deposit

The Hebrew working text was deposited on 2026-10-21 at `registers/source-bundle/companies-law-5759-1999.he.wiki.txt`, as the raw MediaWiki source of the Wikisource page.
Its sha256 and retrieval URL are in the `.meta.json` beside it.
It is an unofficial consolidation as maintained at retrieval (page revision 3088229, last edited 2026-10-12T09:30:10Z), not a historical vintage.

## Access checks of 2026-10-21

Every request used the User-Agent `legalese-commons/1.0 (+https://github.com/legalese/commons; statute sourcing for Legalese commons)`, with at least 3 seconds between requests.

| Site | What was read | Result |
|---|---|---|
| `https://he.wikisource.org/robots.txt` | the whole file, including all 206 lines of the block for all agents | **200**. That block has 200 Disallow rules: `/w/`, `/api/`, `/trap/`, and 197 under `/wiki/` for Special pages, search and some Wikipedia project pages; none matches a statute page. The text was therefore fetched from `/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%97%D7%91%D7%A8%D7%95%D7%AA?action=raw`, which is under `/wiki/`, and not from `/w/index.php`. |
| `https://he.wikisource.org/wiki/…?action=raw` and the same page without `action` | the wikitext, and the HTML page for its revision id | **200**, 625,106 bytes and 1,080,750 bytes. |
| `https://knesset.gov.il/robots.txt` | from Singapore | **303**, to `https://www.knesset.gov.il/maintenance-page-geo`. From an Israeli address (a relay, il-central-1) the file answers **404**, so there are no robots rules. |
| `https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_IsraelLaw` and `KNS_LawBinding`, filtered by IsraelLawID 2000289 | JSON | **200**, through the relay, 626 and 12,654 bytes. |

**Control for the Wikisource route.** The same `/wiki/…?action=raw` request for the Minimum Wage Law page returned a file byte-identical to the committed deposit of that Law in this repository (sha256 `d74633b3e230f83e486642c2815a81fe98b3259450ee85f01bc6f1b972ef78f5`, `Last-Modified` 2026-08-26T07:30:08Z, the same revision its meta file records).

**Coverage check of the deposit.** The wikitext has 557 section templates; the integer section numbers run 1 to 378 with none missing, nothing is out of order, there are 11 part headings, and the file ends with the Fourth Schedule, the signature block and the closing template, so it is not truncated.

The requests of that day, in order:
  - 2026-10-21T09:14:10Z https://he.wikisource.org/robots.txt
  - 2026-10-21T09:14:13Z https://knesset.gov.il/robots.txt
  - 2026-10-21T09:14:39Z https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%97%D7%91%D7%A8%D7%95%D7%AA?action=raw
  - 2026-10-21T09:14:49Z https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%97%D7%91%D7%A8%D7%95%D7%AA
  - 2026-10-21T09:15:56Z via il-central-1 relay: https://knesset.gov.il/robots.txt
  - 2026-10-21T09:16:02Z via il-central-1 relay: https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_IsraelLaw?%24filter=IsraelLawID%20eq%202000289&%24format=json
  - 2026-10-21T09:16:09Z via il-central-1 relay: https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_LawBinding?%24filter=IsraelLawID%20eq%202000289&%24format=json
  - 2026-10-21T09:17:18Z https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%A9%D7%9B%D7%A8_%D7%9E%D7%99%D7%A0%D7%99%D7%9E%D7%95%D7%9D?action=raw (control)
