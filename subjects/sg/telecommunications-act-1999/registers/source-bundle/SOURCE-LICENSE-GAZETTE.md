# Source licence note: Telecommunications Act texts and Gazette copies taken from the e-Gazette

This note covers the files listed below and their `.meta.json` files in this directory.
It does not replace or change `../../SOURCE-LICENSE.md`, which covers `TA1999.txt` (the Singapore Statutes Online rendering) where that subject has one, and that file was not edited.

## What the texts are

- `TA1999.20001230.txt`: the Telecommunications Act (Chapter 323), **Revised Edition 2000 (30th December 2000)**, as the Gazette PDF prints it ("Prepared and Published by the Law Revision Commission ... Printed by the Government Printer, Singapore 2000").
- `TA1999.ACT10-2005.txt`: the **Telecommunications (Amendment) Act 2005 (Act 10 of 2005)**, Acts Supplement No. 3, "First published in the Government Gazette, Electronic Edition, on 16th February 2005 at 5:00 pm."
- `TA1999.ACT19-2011.txt`: the **Telecommunications (Amendment) Act 2011 (Act 19 of 2011)**, Acts Supplement No. 2 of 2012, "First published ... on 20th January 2012 at 5:00 pm."
- `TA1999.S33-2012.txt`: the **Telecommunications (Amendment) Act (Commencement) Notification 2012 (S 33/2012)**, "First published ... on 31st January 2012 at 5.00 pm", which brings Act 19 of 2011 into operation on 1st February 2012.
- `TA1999.BILL20-2011.txt` and `TA1999.BILL30-2016.txt`: **Bill 20/2011** (first published 20th October 2011) and **Bill 30/2016** (first published 10th October 2016), each with its explanatory statement, as the Bills Supplement prints it.
- `TA1999.RevEd2020-printed.txt`: the **2020 Revised Edition** of the Act as printed in the Gazette, which "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021."
- Each is the output of `pdftotext -layout` on a PDF that has a text layer, unedited, except where stated below; the PDF is the source and the text is an aid for quotation.
  The URL, the retrieval time, the sha256 of the PDF and of the text, and how each was obtained are in the `.meta.json` beside it.
- **`TA1999.ACT10-2005.txt` is OCR.** Its PDF has no text layer.
  It was made with `pdftoppm -r 300` and `tesseract 5.5.3 -l eng --psm 4` on each of the 27 pages, the page texts joined with form feeds, unedited.
  How far it was compared with the page images is stated in `TA1999.ACT10-2005.meta.json` (`ocr_checked`): four of the 27 pages, and the rest not.

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
The two editions the first part of this note covers were published before that date; Act 13 of 2026 (deposited 2026-11-04, first published 5 June 2026) was published after it, and this note does not state the evidentiary status of its copy.
So these copies are an aid and are not stated to be prima facie evidence of their contents.

## What this is not

The deposit is a **reliance** on the e-Gazette's clause 11 permission, not a clearance from the Government or the e-Gazette.
Whether a Revised Edition, a Bill or an Act printed as a legislation supplement is an "e-Gazette" within clause 11 is read here in the way the terms' own heading ("Reproduction of legislation-Gazettes") suggests; no one has asked the Government.
The files were deposited in the Telecommunications Act subject because every one of them is an amendment, a commencement notice, a Bill or an edition of that Act.

## Added on 2026-11-04: the Gazette's copies of amending instruments

The e-Gazette's text of each of these instruments (`pdftotext -layout`, a text layer in every PDF, no OCR; the PDF is the source) is deposited with a `.meta.json` carrying the URL, the retrieval time, the sha256 of the PDF and of the text, and the "First published" line as printed:
- `TA1999.S76-2005.txt`

Those whose stem ends `-GAZ` are copies of instruments whose IMDA copy is deposited beside them; the encoder compared the pairs (NOTES.md of the encoding, finding 23).
Those without `-GAZ` are instruments that IMDA's Telecommunications Act page did not list and that are deposited here as the instrument's text.
Each PDF was fetched on 2026-11-04 by one request, with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, five seconds after the previous request, at an exact URL taken from the e-Gazette's browse page by the team lead; the `robots.txt` (`Disallow: /search`) was respected and no search path was used.

## Added on 2026-11-04 (second list): more of the e-Gazette's texts

Deposited from the second list of exact URLs the team lead gave (one GET each, five seconds apart, the same User-Agent, `pdftotext -layout` on PDFs with text layers, no OCR; a `.meta.json` beside each):
- `TA1999.ACT30-2016.txt`
- `TA1999.S14-2017.txt`
- `TA1999.ACT22-2016.txt`
- `TA1999.S461-2016.txt`

They rest on the same e-Gazette clause 11 reliance as above, and the same limits apply.

## Added on 2026-11-04 (third list): more of the e-Gazette's texts

Deposited from the third list of exact URLs the team lead gave (one GET each, five seconds apart, the same User-Agent, `pdftotext -layout` on PDFs with text layers, no OCR; a `.meta.json` beside each):
- `TA1999.ACT15-2017.txt`

They rest on the same e-Gazette clause 11 reliance as above, and the same limits apply.

## Added on 2026-11-04 (follow-up list): more of the e-Gazette's texts

Deposited from the exact URLs the team lead gave after the independent review (one GET each, five seconds apart, the same User-Agent, `pdftotext -layout` on PDFs with text layers, no OCR; the PDF is the source):
- `TA1999.ACT26-2018.txt`
- `TA1999.ACT40-2018.txt`
- `TA1999.ACT15-2019.txt`
- `TA1999.ACT12-2020.txt`
- `TA1999.ACT4-2021.txt`
- `TA1999.ACT25-2021.txt`
- `TA1999.ACT13-2026.txt`
Each has a `.meta.json` with the URL, the retrieval time, the sha256 of the PDF and of the text, and the "First published" line as printed (the 1999 Revised Edition texts print none).

## Added on 2026-11-04 (second follow-up list, Part 3): more of the e-Gazette's texts

Deposited from the exact URLs the team lead gave for Part 3 of the follow-up (one GET each, five seconds apart, the same User-Agent, `pdftotext -layout` on PDFs with text layers, no OCR; the PDF is the source):
- `TA1999.ACT31-2022.txt`
- `TA1999.S850-2022.txt`
- `TA1999.BILL24-2022.txt`
- `TA1999.S26-2022.txt`
Each has a `.meta.json` with the URL, the retrieval time, the sha256 of the PDF and of the text, and the "First published" line as printed (the 1999 Revised Edition texts print none).

`TA1999.BILL24-2022.txt` (Statutes (Miscellaneous Amendments) Bill, Bill No. 24/2022) is a Bill as introduced and is EXTRINSIC material only, like `TA1999.BILL20-2011.txt`; it is not the Act.
`TA1999.S26-2022.txt` is an Order under the Variable Capital Companies Act 2018 whose paragraph 22 amends this Act; `TA1999.S850-2022.txt` is the commencement notification of Act 31 of 2022; `TA1999.ACT31-2022.txt` is the Act, whose section 21(7) amends this Act.
