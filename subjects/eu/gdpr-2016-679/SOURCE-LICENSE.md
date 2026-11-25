# Source licence: EU General Data Protection Regulation (Regulation (EU) 2016/679)

## Official Journal text, its corrigendum and the Publications Office consolidated version: UNDETERMINED

Three plain-text renderings are deposited in `registers/source-bundle/`, each made by `xhtml_to_text.py` from an XHTML file fetched from the Publications Office cellar on **2026-11-26**:

| file                                                | what it renders                                                                          | CELEX                 |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------- |
| `eu-gdpr-2016-679.txt`                              | the Regulation as published in the Official Journal, L 119, 4.5.2016, p. 1 (uncorrected) | `32016R0679`          |
| `eu-gdpr-2016-679-corrigendum-20180523.txt`         | the corrigendum, Official Journal L 127, 23.5.2018, p. 2                                 | `32016R0679R(02)`     |
| `eu-gdpr-2016-679-consolidated-20160504.txt`        | the Publications Office consolidated version of 4.5.2016, which applies that corrigendum | `02016R0679-20160504` |

No reuse grant that covers Official Journal legal texts or the Publications Office's consolidated versions has been read as applying to them, so none is recorded here.
Each `.meta.json` gives the URL, the retrieval date and the sha256 of the XHTML and of the text, which is how the source is acknowledged.
Only the plain-text renderings are deposited, not the XHTML originals.

What was read on **2026-11-26**, with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`:

- `https://publications.europa.eu/robots.txt` answered 200 after a redirect to `https://op.europa.eu/robots.txt` (sha256 `de63106ad6607ba0bf3e313c31871d96ccc7e949ee0e29fa0b1c85a450305a75`).
  It reads `User-agent: *` / `Allow: /`, followed by Disallow lines for portal pages (login, basket, control panel, `*requestAction=rdf`, `/webdav/*`, `/s/*`, query-string pages such as `/*/publication-detail?*`) and a `Disallow: /` for two named crawlers (Sogou web spider and PetalBot).
  None of its rules matches `/resource/celex/...` or the cellar document paths used to fetch these texts.
- Commission Decision 2011/833/EU of 12 December 2011 on the reuse of Commission documents, Official Journal L 330, 14.12.2011, p. 39 (CELEX `32011D0833`), fetched the same way (XHTML sha256 `2d5bc877b9a5aad948af21c680aca1d3409f41df5dd0dcc57ef9b1b225f60982`).
  The Commission's own legal notice says its reuse policy "is implemented by" this Decision (quoted in `subjects/eu/ai-act-2024/SOURCE-LICENSE.md`), so it is the nearest statement of terms that could be read.
  The text of the Decision as published in 2011 was read; whether it has since been amended or replaced was **not checked**.
  What it says, verbatim:

  > **Article 2, Scope.** 1. This Decision applies to public documents produced by the Commission or by public and private entities on its behalf:
  > (a) which have been published by the Commission or by the Publications Office on its behalf through publications, websites or dissemination tools; or
  > (b) which have not been published for economic or other practical reasons, such as studies, reports and other data.
  > 2. This Decision shall not apply: ... (b) to documents for which the Commission is not in a position to allow their reuse in view of intellectual property rights of third parties; ...
  >
  > **Article 4, General principle.** All documents shall be available for reuse:
  > (a) for commercial or non-commercial purposes under the conditions laid down in Article 6;
  > (b) without charge, subject to the provisions laid down in Article 9; and
  > (c) without the need to make an individual application, unless otherwise provided in Article 7.
  >
  > **Article 6, Conditions for reuse of documents.** 1. Documents shall be made available for reuse without application unless otherwise specified and without restrictions or, where appropriate, an open licence or disclaimer setting out conditions explaining the rights of reusers.
  > 2. Those conditions, which shall not unnecessarily restrict possibilities for reuse, may include the following:
  > (a) the obligation for the reuser to acknowledge the source of the documents;
  > (b) the obligation not to distort the original meaning or message of the documents;
  > (c) the non-liability of the Commission for any consequence stemming from the reuse.

  **What this does not settle.**
  The Regulation is an act of the European Parliament and of the Council, published by the Publications Office in the Official Journal.
  Whether it is a "public document produced by the Commission or by public and private entities on its behalf" within Article 2(1), and whether the consolidated version is one, is a question the text of the Decision does not answer, and no reading is recorded here.
  If the Decision does apply, Article 6(2)(a) and (b) are the conditions it names as possible: acknowledge the source (each `.meta.json` does) and do not distort the meaning (the renderings are mechanical, and each `.meta.json` records the check that no word of the XHTML is missing from the rendering).
- Not retried on 2026-11-26: EUR-Lex (a bot challenge on 2026-10-01 and 2026-10-24), the Publications Office's own copyright notice (HTTP 403 from an "Azure WAF" page on 2026-10-24 and 2026-11-17) and the `commission.europa.eu` legal notice (200 on 2026-10-24, covering "content owned by the EU on this website", meaning that site).
  The results are recorded in `subjects/eu/ai-act-2024/SOURCE-LICENSE.md` and `subjects/eu/eprivacy-directive-2002/SOURCE-LICENSE.md`.
  The 403 and the challenge were treated as a no and not worked around.

This deposit follows the precedent of `subjects/eu/ai-act-2024/` and `subjects/eu/eprivacy-directive-2002/`, which deposit Publications Office texts under the same UNDETERMINED status.
The choice of these three files, and of the consolidated text as the one quoted for Articles 1 to 99 and the as-published text as the one quoted for the recitals, is assumed, not ruled: the coordinating session accepted it on 2026-11-26 and the maintainer has not confirmed it.
**A person with authority to decide should settle the terms before this subject is relied on as redistributable.**

## The encoding

The encodings under `encodings/` are licensed under **Apache-2.0**, per the repository `NOTICE`.
That licence covers the encodings only, not the quoted legislative text.
