# Source licence note: Telecommunications Act texts and Gazette copies taken from the e-Gazette

This note covers the files listed below and their `.meta.json` files in this directory.
It does not replace or change `../../SOURCE-LICENSE.md`, which covers `TA1999.txt` (the Singapore Statutes Online rendering) where that subject has one, and that file was not edited.

## What the texts are

- `TA1999-RG6-GAZ-RevEd2004.txt`: the Telecommunications (Dealers) Regulations (Rg 6), **Revised Edition 2004 (31.12.2004)**, as the Gazette PDF prints it (G.N. No. S 185/2003, amended by S 48/2004 and S 593/2004).
- `TA1999-RG6-S178-2011-GAZ.txt`: the **Telecommunications (Dealers) (Amendment) Regulations 2011 (S 178/2011)**, "First published ... on 1st April 2011 at 5:00 pm."
- These are the Gazette's copies of two instruments of which the IMDA-hosted copies are deposited beside them (`TA1999-RG6.txt` and `TA1999-RG6-S178-2011.txt`); the encoder compared the two sets (see the encoder's NOTES.md).
- Each is the output of `pdftotext -layout` on a PDF that has a text layer, unedited, except where stated below; the PDF is the source and the text is an aid for quotation.
  The URL, the retrieval time, the sha256 of the PDF and of the text, and how each was obtained are in the `.meta.json` beside it.

## Where they came from

Each PDF was fetched on 2026-11-04 from the e-Gazette's static file host (`assets.egazette.gov.sg`), by one request with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, five seconds after the previous request (the tool is `tools/gazette-fetch.py` in the encoder's scratchpad; its log is the source of the retrieval times in the meta files).
The e-Gazette's `robots.txt` (`https://www.egazette.gov.sg/robots.txt`) says `Allow: /` and `Disallow: /search`; no search path was used.
The file names and URLs were given to the encoder by the team lead, who had found them by browsing the e-Gazette.

## What the e-Gazette's terms say, quoted

From the e-Gazette Terms of Use (`https://www.egazette.gov.sg/terms-of-use/`, which says "Last updated on 10 July 2026"), the section headed "Reproduction of legislation-Gazettes" (clause 11 of the terms; the page text refers to it as clause (11)):

> The Government has granted permission to the users of the Website to reproduce any e-Gazettes in any print or electronic material or platform (collectively, "the relevant material/platform"), subject to these Terms of Use and the following conditions:
>
> the following information must be included in the relevant material/platform:
> that the e-Gazettes are subject to copyright of the Singapore Government and are reproduced in the relevant material/platform with the permission of the Singapore Government;
> that the users of the relevant material/platform may check the Website for the latest e-Gazettes;
>
> the producers* of the relevant material/platform are responsible for ensuring the accuracy of the e-Gazettes reproduced in the relevant material/platform;
>
> the reproduction of the e-Gazettes on the relevant material/platform must not create any suggestion that the Government or the Website is associated or affiliated in any manner with the relevant material/platform, the producers of the relevant material/platform or the producers' affiliates;
>
> in the case where the producers, or the producers' affiliates or agents, intend to extract the e-Gazettes from the Website through automated means, such extraction of the e-Gazettes from the Website is subject to these Terms of Use and the following conditions:
> the extraction must not be carried out in an abusive or intrusive, or a deceptive, manner;
> the extraction must not disrupt or affect the Website's performance, cause any harm or damage to the Website, or breach or circumvent of the Websites security measures.
>
> The Government may, at any time and without ascribing any reason or giving any prior notice, revoke the permission, or modify the permission or the conditions of the permission, granted under clause (11) of these Terms of Use.

(The page's own formatting numbers and indents these items; the quotation above is the page's text with that formatting removed and its curly quotation marks and apostrophes written as straight ones; the page's own wording, including "the Websites security measures", is kept.)

## The information the terms require, stated here

- These e-Gazette texts are subject to the copyright of the Singapore Government and are reproduced here with the permission of the Singapore Government.
- Readers may check the e-Gazette website (`https://www.egazette.gov.sg/`) for the latest e-Gazettes.
- The producers of this repository are responsible for the accuracy of what is reproduced here; nothing here has been checked against the official printed text, and the text is the output of a PDF-to-text converter.
- Nothing here suggests that the Government or the e-Gazette website is associated or affiliated with this repository or its producers.

## Status of the texts

The e-Gazette FAQ (`https://www.egazette.gov.sg/faq/`, read 2026-11-03) says: "Before 9 March 2025, only copies of the Gazette printed by the Government Printer are regarded as prima facie evidence of their contents. These printed copies prevail over all other forms of the Gazette if there is any inconsistency."
Both editions here were published before that date.
So these copies are an aid and are not stated to be prima facie evidence of their contents.

## What this is not

The deposit is a **reliance** on the e-Gazette's clause 11 permission, not a clearance from the Government or the e-Gazette.
Whether a Revised Edition, a Bill or an Act printed as a legislation supplement is an "e-Gazette" within clause 11 is read here in the way the terms' own heading ("Reproduction of legislation-Gazettes") suggests; no one has asked the Government.
The Gazette copies were fetched to check the IMDA-hosted copies of the same instruments, and are deposited so that the comparison can be repeated.

## Added on 2026-11-04: the Gazette's copies of amending instruments

The e-Gazette's text of each of these instruments (`pdftotext -layout`, a text layer in every PDF, no OCR; the PDF is the source) is deposited with a `.meta.json` carrying the URL, the retrieval time, the sha256 of the PDF and of the text, and the "First published" line as printed:
- `TA1999-RG6-S210-2010-GAZ.txt`
- `TA1999-RG6-S251-2013-GAZ.txt`
- `TA1999-RG6-S396-2007-GAZ.txt`
- `TA1999-RG6-S414-2014-GAZ.txt`
- `TA1999-RG6-S478-2005-GAZ.txt`
- `TA1999-RG6-S725-2014-GAZ.txt`

Those whose stem ends `-GAZ` are copies of instruments whose IMDA copy is deposited beside them; the encoder compared the pairs (NOTES.md of the encoding, finding 23).
Those without `-GAZ` are instruments that IMDA's Telecommunications Act page did not list and that are deposited here as the instrument's text.
Each PDF was fetched on 2026-11-04 by one request, with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, five seconds after the previous request, at an exact URL taken from the e-Gazette's browse page by the team lead; the `robots.txt` (`Disallow: /search`) was respected and no search path was used.

## Added on 2026-11-04 (follow-up list): more of the e-Gazette's texts

Deposited from the exact URLs the team lead gave after the independent review (one GET each, five seconds apart, the same User-Agent, `pdftotext -layout` on PDFs with text layers, no OCR; the PDF is the source):
- `TA1999-RG6-S589-2023.txt`
Each has a `.meta.json` with the URL, the retrieval time, the sha256 of the PDF and of the text, and the "First published" line as printed (the 1999 Revised Edition texts print none).

## Added on 2026-11-04 (second follow-up list, Part 3): more of the e-Gazette's texts

Deposited from the exact URLs the team lead gave for Part 3 of the follow-up (one GET each, five seconds apart, the same User-Agent, `pdftotext -layout` on PDFs with text layers, no OCR; the PDF is the source):
- `TA1999-RG6-S185-2003.txt`
- `TA1999-RG6-S48-2004.txt`
- `TA1999-RG6-S593-2004.txt`
Each has a `.meta.json` with the URL, the retrieval time, the sha256 of the PDF and of the text, and the "First published" line as printed (the 1999 Revised Edition texts print none).
