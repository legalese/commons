# Source license

The quoted text of the **UK General Data Protection Regulation** (Regulation (EU) 2016/679, as shown on [legislation.gov.uk](https://www.legislation.gov.uk/) with the added title "(United Kingdom General Data Protection Regulation)") is sourced from that site; the file's `dc:publisher` reads "King's Printer of Acts of Parliament".

- **Copyright owner**: Crown copyright and database right (the site footer reads "© Crown and database right").
- **License**: [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), as the site states it for its content in general; the site's footer also says that it contains EUR-Lex-derived content reused under Commission Decision 2011/833/EU, and this deposit does not decide which of the two statements governs the Regulation's EU-derived base text (see "What the XML shows about EUR-Lex").
- **Terms checked**: terms as recorded at 2026-10-21 in `subjects/uk/fraud-act-2006/SOURCE-LICENSE.md` (the footer of https://www.legislation.gov.uk/help, read that day); the OGL v3.0 page itself was re-read on 2026-11-26. No page of legislation.gov.uk was requested for these terms on 2026-11-26 (see "How the XML was obtained").
- **Source**: https://www.legislation.gov.uk/eur/2016/679

## Required attribution

Contains public sector information licensed under the Open Government Licence v3.0.

That is the attribution the OGL prescribes where the Information Provider names none; for the Regulation's EU-derived base text see "What the XML shows about EUR-Lex".

## Status of this deposit

Statute text deposited 2026-11-26: `registers/source-bundle/eur-2016-679.txt`, converted to plain text from
https://www.legislation.gov.uk/eur/2016/679/data.xml
(point in time (dct:valid) of the version served: 2026-09-30; dc:modified 2026-11-24).
The XML as saved is deposited unchanged beside it, `registers/source-bundle/eur-2016-679-data.xml` (1,675,337 bytes, sha256 `027f41d0cef381b12cf5abcbf63b065cd639949329d6d7bbf9a845f6f7fe6183`).

The text is the in-force text at 2026-09-30 only; where the file records an amendment as unapplied, the text does not carry it, with one exception named in `text_caveat` (Art. 57(3)).
How repeals, the amendment notes (Commentary Type F and the others), the unapplied effects (ukm:UnappliedEffect: 5 in this file), extents and, for this Regulation, the recitals and footnotes are treated is in `registers/source-bundle/eur-2016-679.meta.json` (keys `converter` and `text_caveat`).

The commons converter that made the earlier UK deposits dropped tables, list enumerators, the numbers of headingless Schedule paragraphs, the long title and the date of enactment (checked on `uk/income-tax-act-2007`, as recorded in `subjects/uk/fraud-act-2006/SOURCE-LICENSE.md`).
This text keeps them, as the Fraud Act 2006 deposit does; the additions made for this deposit are listed in the `converter` key of the meta.json.
The text includes the recitals, before Article 1, and the 20 Official Journal footnotes, after Annex 2.
Editorial commentary, the contents list and explanatory notes are left out, as in the earlier deposits.

## How the XML was obtained

The site answered an automated request with an AWS WAF challenge on 2026-11-26.
A plain request for https://www.legislation.gov.uk/robots.txt at 2026-11-26T03:52:21Z was answered HTTP 202 with an empty body and the header `x-amzn-waf-action: challenge`; the retrieval log notes that the run stopped, with no further requests.
The XML file was therefore saved by hand, in a web browser, on 2026-11-26, from
https://www.legislation.gov.uk/eur/2016/679/data.xml,
and the retrieval log records the file at 2026-11-26T04:16:10Z, with the note that it was extracted from the saved page's web archive (its main resource); that time is the `retrieved_utc` of the meta.json, and the time of the saving itself is not recorded.
The bytes deposited are the bytes extracted, 1,675,337 bytes, sha256 `027f41d0cef381b12cf5abcbf63b065cd639949329d6d7bbf9a845f6f7fe6183`.
The file begins `<Legislation xmlns=` with no XML declaration, as the Fraud Act 2006 XML fetched by program on 2026-10-21 does; whether the server's own response matches these bytes was not checked.

## Terms as recorded at 2026-10-21

The footer of https://www.legislation.gov.uk/help, read on 2026-10-21 and saved (the saved page's sha256 is `0ed9688bdc6db3922faa8c84905c9b71730fa199aa98b833ebfb1fc713d6a696`), reads, verbatim:

> All content is available under the Open Government Licence v3.0 except where otherwise stated. This site additionally contains content derived from EUR-Lex, reused under the terms of the Commission Decision 2011/833/EU on the reuse of documents from the EU institutions. For more information see the EUR-Lex public statement on re-use.
>
> © Crown and database right

The Fraud Act 2006 deposit records the same reading, in its own words, in `subjects/uk/fraud-act-2006/SOURCE-LICENSE.md`; that saved page is not kept in commons, and was not read again on 2026-11-26.
The "EUR-Lex public statement on re-use" that the sentence links to (https://eur-lex.europa.eu/content/legal-notice/legal-notice.html) was not read for this deposit.

## Terms read again on 2026-11-26

The OGL v3.0 page (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/, a different site from legislation.gov.uk) was read on 2026-11-26 at 06:12 UTC: HTTP 200, 10,450 bytes, sha256 `f5b2b9f2af63647cde889fa6c3508f5705925295b74912c68caa28dd37e64aa5`, the same as the copy read on 2026-10-21.
It says that where the Information Provider does not provide a specific attribution statement, the user must use: "Contains public sector information licensed under the Open Government Licence v3.0."
The 2026-10-21 reading of the help page gives no attribution statement of its own (`subjects/uk/fraud-act-2006/SOURCE-LICENSE.md`).
The OGL page's list of what the licence does not cover includes "third party rights the Information Provider is not authorised to license".

## What the XML shows about EUR-Lex

The site's statement says the site "contains content derived from EUR-Lex"; it does not say which pages.
The XML of this Regulation does mention EUR-Lex and europa.eu: 42 of its 465 lines match (case-insensitive search for `eur-lex` or `europa.eu`), 76 occurrences of the two strings in all.
They are in three places, none of them the Regulation's own words: not one text node of the Regulation's body or of its footnotes contains either string.

- the `dc:source` metadata element, which reads `https://webarchive.nationalarchives.gov.uk/eu-exit/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016R0679-20160504`;
- the 38 `VALUE` text nodes of the `ukm:EURLexMetadata` block, which hold identifiers of the EUR-Lex record as URIs on europa.eu (cellar, celex, eli, oj and similar); beside the block, `ukm:EURLexModified` (2019-04-18T16:51:42Z) and `ukm:EURLexExtracted` (2019-04-18T19:52:48Z) give the dates the EUR-Lex text was modified and extracted;
- the `URI` attributes of 18 `Citation` elements (the references to Official Journal pages), which point into the National Archives' web archive of EUR-Lex.

The `dc:source` element names a EUR-Lex consolidated text as the source of the document, and the XML carries EUR-Lex's own metadata block; this deposit reads that as marking the Regulation's base text as EUR-Lex-derived, which is an inference from the markup and not a statement by the site.
The UK amendments are marked in the text as Addition and Substitution elements (1,042 and 510 of them) and were made by UK instruments; that the EUR-Lex statement reaches the base text and not those amendments is a further inference, not something the site says.

Whether Commission Decision 2011/833/EU reaches an act of the European Parliament and of the Council is not decided here.
`subjects/eu/gdpr-2016-679/SOURCE-LICENSE.md` records that question as undetermined for the same Regulation as the Publications Office publishes it, and quotes the Decision's Articles 2, 4 and 6 as read on 2026-11-26; nothing is added to it here.
This deposit records both statements, the OGL one and the EUR-Lex one, and does not decide which governs the Regulation's base text.
**A person with authority to decide should settle the terms of the EU-derived base text before this deposit is relied on as redistributable.**

## The encoding

No encoding is deposited: this directory holds the source and its provenance only.
