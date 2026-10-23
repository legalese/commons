<!-- Copy of ../../SOURCE-LICENSE.md, which is canonical: correct that file first, then copy it here. -->

# Source licence: Act No. 53 of 2025 (Japan)

This file records the terms the deposited source texts carry, as read on 2026-10-24.
It is not the licence of the encoding, which is Apache-2.0 like the rest of this repository.

## 1. The Japanese text (authoritative): e-Gov 法令検索

- **Files:** `registers/source-bundle/ai-act-ja.xml` (current revision), `ai-act-ja-20250604.xml` (earlier revision), `egov-laws-search.json` and `egov-law-revisions.json` (API metadata), and `ai-act-ja.txt`, a rendering of the first file made by `ai-act-ja-render.py`.
- **Where read:** the e-Gov 法令検索 利用規約 page, https://laws.e-gov.go.jp/terms (a single-page application; the text was read from its page bundle, `https://laws.e-gov.go.jp/assets/terms-a5a45db6.js`, fetched 2026-10-23T23:05:53Z).
- **What it says** (quoted verbatim):

  > 本サイトの著作権は、特記されていない限りデジタル庁に帰属し、権利表記の記載がない限り「公共データ利用規約（第1.0版）」（PDL1.0）が適用されています。

  and, under 1.1 出典の記載について:

  > コンテンツを利用する際は出典を記載してください。

  > コンテンツを編集・加工等して利用する場合は、上記出典とは別に、編集・加工等を行ったことを記載してください。なお、編集・加工した情報を、あたかも国（又は府省等）が作成したかのような態様で公表・利用してはいけません。

- **Licence:** Public Data License (Version 1.0) (公共データ利用規約（第1.0版）), linked from that page to https://www.digital.go.jp/resources/open_data/public_data_license_v1.0.
- **Copyright holder named:** デジタル庁 (Digital Agency), unless otherwise stated.

## 2. The English translation (aid): Japanese Law Translation Database System

- **Files:** `registers/source-bundle/ai-act-en.pdf`, `ai-act-en.txt` (its `pdftotext -layout` rendering) and `ai-act-en.history.html` (the translation's history fragment).
- **Where read:** https://www.japaneselawtranslation.go.jp/en/index/terms, fetched 2026-10-23T23:05:07Z.
  The address `/en/terms/` tried earlier in the session is a 404; the real page is linked as "Terms of Use" from the site's English home page.
- **What it says** (quoted verbatim):

  > Information published on this site (referred to below as "content") is subject to the "Public Data License (Version 1.0)" (PDL1.0) unless stated otherwise. In addition, the copyright belongs to the Ministry of Justice of Japan unless stated otherwise.

  and, from the "NOTICE TO USERS" on the same page:

  > The translations contained in the Japanese Law Translation Database System are not official texts, and not all of the translations are finalized versions. Only the original Japanese texts of the laws and regulations have legal effect, and the translations are to be used solely as reference materials to aid in the understanding of Japanese laws and regulations. The government of Japan is not responsible for the accuracy, reliability or currency of the legislative material provided in this website, or for any consequence resulting from use of the information in this website. For all purposes of interpreting and applying law to any legal issue or dispute, users should consult the original Japanese texts published in the Official Gazette.

  > The data contained in the Japanese Law Translation Database System may be cited, reproduced, or reprinted in accordance with the Terms of Use.

- **Excluded from the grant (cl. 1.4 as applied by the site):** the Japanese Law Translation logo and character. Nothing of either is deposited.
- **Copyright holder named:** the Ministry of Justice of Japan, unless otherwise stated.

## 3. The licence both sites apply: PDL 1.0

Read at https://www.digital.go.jp/en/resources/open_data/public_data_license_v1.0, fetched 2026-10-23T23:05:23Z.
That English page says of itself: "Note: This document is for reference only. Please refer to the Japanese version below for the official document."
The Japanese PDF of the licence was not fetched.
What the English page says, in the clauses that bear on this deposit (quoted verbatim):

> Information made available on this website (hereinafter referred to as Content), except for Content subject to other terms of use, may be freely used, copied, publicly transmitted, translated or otherwise modified on condition that the user complies with provisions 1.1 to 1.7 below (hereinafter referred to as "This Terms of Use"). [...] Commercial use of "This Content" is also permitted.

> 1.1. Source citation — The user must cite the source when using "This Content". [...] If the user has edited "This Content" for use, you must include a statement expressing that "This Content" has been edited and the name of entity, in addition to the abovementioned source citation. [...] But not in any way making public or using edited information in a format that may be misconstrued as if national government or the relevant ministries [...] has just created and unedited by anyone else.

> 1.6. Disclaimer — National government [...] bears absolutely no responsibility for any action taken by the user involving the use of "This Content" including use of information based on edited "This Content".

> 1.7. Other — [...] "This Terms of Use" is compatible with the Creative Commons Attribution License 4.0 (hereinafter referred to as the CC BY). National government [...] permits the user to use "This Content" to which "This Terms of Use" apply in accordance with CC BY.

So the CC BY 4.0 compatibility was read on the page, not assumed.
Neither site's copyright-in-statutes position under the Copyright Act of Japan was read in this session, and nothing here relies on one.

## 4. Source citations and edit statements, in PDL 1.0's form

- Source: 「人工知能関連技術の研究開発及び活用の推進に関する法律（令和七年法律第五十三号）」（e-Gov 法令検索）（https://laws.e-gov.go.jp/api/2/law_file/xml/507AC0000000053_20250901_000000000000000）PDL1.0（https://www.digital.go.jp/resources/open_data/public_data_license_v1.0）（2026年10月24日に利用）
- Source: "Act on Promotion of Research and Development, and Utilization of Artificial Intelligence-related Technology (Act No. 53 of 2025)" (Japanese Law Translation Database System, Ministry of Justice) (https://www.japaneselawtranslation.go.jp/en/laws/view/5066/en) PDL1.0 (https://www.digital.go.jp/en/resources/open_data/public_data_license_v1.0) (accessed on 2026/10/24)
- **Edit statement.** `ai-act-ja.txt` was created by Legalese Pte. Ltd. by editing the e-Gov XML of the Act: it re-lays the text one sentence per line and drops the markup, adding no words. `ai-act-en.txt` was created by Legalese Pte. Ltd. by extracting the text of the Ministry of Justice PDF with `pdftotext -layout`. The L4 modules in `encodings/` quote both and were written by Legalese Pte. Ltd.; they are not a publication of the Government of Japan, the Digital Agency or the Ministry of Justice, and nothing in them was made or checked by any of them.
- The deposited `.xml`, `.json`, `.pdf` and `.html` files are unaltered copies of what was fetched (sha256 in the `.meta.json` files).
