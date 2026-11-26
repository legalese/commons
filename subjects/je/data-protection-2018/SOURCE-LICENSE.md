# Source licence: Data Protection (Jersey) Law 2018

**Status: open. Open States Assembly Licence – Jersey (OSAL-J) v1.0.** Attribution is a condition of the licence.

## Required attribution

Contains States Assembly information licensed under the Open States Assembly Licence – Jersey v1.0.

## The source

Data Protection (Jersey) Law 2018 (L.3/2018), Official Consolidated Version on jerseylaw.je:

    https://www.jerseylaw.je/laws/current/l_3_2018

Retrieved 2026-11-26T00:19:38Z (UTC), HTTP 200, 1017206 bytes, sha256 `a53a9fe9780384c123f67bd799c1a207f1a9b542cf3b26c077a11afb4850011c`.
The page showed "Showing the law from 2 October 2026 to Current", and its banner reads "This is an official version of consolidated legislation compiled and issued under the authority of the Legislation (Jersey) Law 2021."
The L-number was found by fetching the page: `l_03_2018` and `l_02_2018` (guessed spellings) and `l_2_2018` answered 404; `l_3_2018` answered 200 with the title "Data Protection (Jersey) Law 2018".
The page links its definition of "Authority Law" to `/laws/current/l_4_2018`, the Data Protection Authority (Jersey) Law 2018; that page was not fetched.

## Terms read for this deposit (2026-11-26 UTC)

- **Copyright page**: https://www.jerseylaw.je/Pages/copyright.aspx, read 2026-11-26T00:22:10Z (sha256 of the HTML `1aa8f1bc22b78875bb0143dd2ec5425bcfa0367433a912121744c61ce95e35a0`). Key lines, verbatim:
  - "the States Assembly is entitled to copyright in any Jersey legislation (as defined in the Legislation (Jersey) Law 2021)"
  - "The Greffier of the States offers the Jersey legislation published from time to time on the current laws, laws as enacted and pending laws pages of the site for use and re-use under the terms of the Open States Assembly Licence (OSAL-J) v.1."
  - "This Greffier's offer does not extend to any other material, including legislation, published elsewhere on jerseylaw.je."
  - "If you wish to carry out bulk downloads of the information offered under the OSAL-J for re-use then please email programmedirector@jerseylaw.je to request access to an HTTP-based RESTful API, rather than 'scraping' links from the search pages."

  This text was read from the current laws pages (`/laws/current/`), so the offer covers it. It was fetched as one page by direct URL, with the other requests listed in its `.meta.json`; no search pages were scraped.
- **The licence itself** (https://statesassembly.je/open-licence): **not re-read, and not requested.** statesassembly.je answered the earlier request recorded in `subjects/je/long-term-care-2012/SOURCE-LICENSE.md` (its robots.txt, 2026-10-19) with HTTP 403 and a Cloudflare challenge, so no request was made to that host. The licence's terms are taken from the reading already recorded in this repository, at `subjects/je/charities-2014/encodings/cleanroom-2026-08/SOURCE-LICENSE.md` (an Internet Archive capture of 2026-02-11, read 2026-09-23). As recorded there, the licence lets you "copy, publish, distribute and transmit the Information; adapt the Information; exploit the Information commercially and non-commercially", on condition of the attribution statement above. It requires neither written permission nor freedom from modification, so the text may be deposited. It also says use "will be governed by the terms of the licence in force as of the date you accessed the Information"; the version in force on 2026-11-26 has not been re-read.
- **Owner's ruling (20 Oct 2026)**, as recorded in `subjects/je/long-term-care-2012/SOURCE-LICENSE.md`: Legalese Commons counts as non-commercial use. It is not needed here, because OSAL-J also allows commercial use, but it is recorded in case the licence turns out to have changed.
- **Disclaimer**: https://www.jerseylaw.je/pages/Disclaimer.aspx, read 2026-11-26T00:22:15Z (sha256 of the HTML `187f61e2e02843e98bc6e85b3b404a4795f669351bb39e3b25a70ad050df13d8`): "Nothing within this site should be relied upon as constituting verified or official text." (The page banner, by contrast, says "official version".)
- **robots.txt**: https://www.jerseylaw.je/robots.txt, read 2026-11-26T00:19:05Z (sha256 `e0a23e43e8e46404ade89d861ba71568dbb4414c2820f878b1422cf778040647`). It disallows `/laws/revised/`, `/laws/enacted/`, `/laws/currentarchive/` and some `/judgments/` paths for all user agents; `/laws/current/` is allowed, and there is no Crawl-delay. Every request used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 s apart. Nothing under `/laws/enacted/` was requested.

## Status of this deposit

`registers/source-bundle/l_3_2018.txt` is an **unofficial** plain-text conversion of the page (see its header and the `.meta.json` beside it): sha256 of the text `fb0e713896ac26cd38bc4cda55cde07dc6da3875fa2839451448d5979d3c0ec2`, 218018 characters.
The converter, `je_convert.py` in the same folder, was written on 2026-11-26 because the one that made the earlier `subjects/je` deposits was not kept in the repository.

The licence is OSAL-J because the publisher names it. Nothing here infers a licence the source does not state. **This is not legal advice.**

## The encoding

Any encoding under `encodings/` is licensed under **Apache-2.0**, per the repository `NOTICE`. That licence covers the encodings only, not the quoted legislative text.
