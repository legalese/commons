# Source license

The text of **Code of the District of Columbia, Title 51 (Social Security), Chapter 1 - Unemployment Compensation** is published by the Council of the District of Columbia in the Code of the District of Columbia (code.dccouncil.gov), and in bulk as XML at github.com/DCCouncil.

## Bulk deposit of 20 October 2026

- **Route used: the bulk download the Council itself offers.** The Council's site, code.dccouncil.gov, says on every page: "The codes and laws on this website are in the public domain. Please do not scrape. Instead, bulk download the HTML or XML." Its robots.txt (as recorded in the plan read on 2026-10-20) carries `Content-signal: search=yes,ai-train=no`, allows `/` for `*`, and disallows `/` by name for AI crawlers including ClaudeBot, GPTBot, CCBot, Google-Extended, Amazonbot, Applebot-Extended, Bytespider and meta-externalagent. **No page of code.dccouncil.gov was fetched for this deposit.** The text was taken instead from the bulk XML the site points to, with the owner's approval of 20 October 2026: the Council's GitHub repository [DCCouncil/law-xml-codified](https://github.com/DCCouncil/law-xml-codified) ("the code fully supplemented"; the Code's own `index.xml` lists `https://github.com/dccouncil/law-xml` as its xml-bulk URL, and law-xml's README names law-xml-codified as the supplemented code).
- **How it was fetched.** One repository archive (zip) of publication branch `publication/2026-05-23` at commit `9c950ac5f53283bdf32c1150a45a9245f930dedd`, through the documented GitHub REST API (`api.github.com/repos/DCCouncil/law-xml-codified/zipball/<sha>`, which redirects to codeload.github.com), on 2026-10-19T23:38:30Z: 70,317,370 bytes, sha256 `fb9dbdaa494735fc4d662285bfd2bfc4dac92df68963679ceb79af04e34287cc`. No git command and no clone. github.com's robots.txt disallows `/*/archive/` and `*/zipball/` on the website and points crawlers to its API instead; api.github.com, codeload.github.com and raw.githubusercontent.com have no robots.txt (HTTP 404). About 20 small API and raw requests (repository metadata, branch lists, READMEs) preceded the download, all HTTP 200, at least 3 seconds apart, with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. The zip was deleted from the scratchpad after the sections were extracted.
- **Licence as the repository states it.** The repository itself carries no LICENSE file (the GitHub API reports `license: null`). The Council's DC-Law project repository ([DCCouncil/dc-law](https://github.com/DCCouncil/dc-law), README read 2026-10-19T23:38:15Z) says: "All repositories are licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/)." The site footer says the codes and laws are in the public domain, and statutory text carries no copyright in any case (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). No reliance on the owner's non-commercial ruling of 2026-10-20 was needed.
- **ai-train=no.** The Council's site signals that its content is not to be used for AI training. Legalese Commons deposits this text for public reference and for encoding the law as rules; it is not deposited for model training, and should not be used as training data.
- **What is deposited.** Unannotated statutory text only: each section's `<annotations>` block (history credits, editor's notes, short-title notes, cross-references) is dropped. The free Council edition is not the commercially annotated D.C. Official Code; nothing is taken from a commercial publisher.
- **Currency.** The Code's recency block reads "through 2026-09-26" (last codified D.C. Law 26-187; last codified emergency D.C. Act 26-416; last codified federal law Pub. L. 115-334); the build and codified date of the archive is 2026-10-07.
- **Official status.** The deposit is an unofficial plain-text conversion by Legalese Commons; compare with the Code at code.dccouncil.gov before relying on it for a legal result.
- **Verdict:** conditions (do not scrape; bulk download; ai-train=no), met: bulk route, no scraping, reference and encoding use only.
- **Attribution (courtesy)**: "Code of the District of Columbia, Council of the District of Columbia (bulk XML, github.com/DCCouncil)."

## Language

English is the sole language of the Code of the District of Columbia; there is no second authentic language version.

## Consequence for this subject

Statute text may be deposited and quoted in an encoding, for reference and encoding, not for model training.

## Status of this deposit (2026-10-20)

Statute text may be deposited and quoted in an encoding. Deposited as unofficial plain text from the Council's bulk XML, current through 2026-09-26. Each `.meta.json` gives the archive URL, its sha256 and size, the commit, the retrieval time (UTC), and the sha256 and character count of the text.

- `registers/source-bundle/dc-code-51-ch1-unemployment-compensation-2026-10.txt` -- Code of the District of Columbia, Title 51 (Social Security), Chapter 1 (Unemployment Compensation) (D.C. Code ss 51-101 to 51-178). The whole chapter: administration of the District Unemployment Fund, definitions, contributions, the weekly benefit amount and duration (51-107), eligibility (51-109), disqualification (51-110), claims and appeals (51-111), domestic-violence provisions, and the shared work program. 47 sections; 259,858 characters.
