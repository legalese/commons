# Source license

The text of **Powers of Attorney Act 2014** is published on the [Victorian Legislation website](https://www.legislation.vic.gov.au/)
by the Office of the Chief Parliamentary Counsel.

- **Copyright owner**: the Government Printer for the State of Victoria.
- **License**: **none. Not openly licensed.** The site's copyright notice (read 2026-11-07T06:24:42Z,
  https://www.legislation.vic.gov.au/copyright, unchanged since 2026-10-19) states that no part may be reproduced except in
  accordance with the Copyright Act 1968 (Cth), and that authorised electronic versions are published for personal use only.
- **Source**: https://www.legislation.vic.gov.au/in-force/acts/powers-attorney-act-2014

## Owner's ruling, 24 October 2026

The Victorian terms were put to Michael (the owner of Legalese Commons), with the warning that nothing could be
deposited without permission. The terms were the Government Printer's notice at https://www.legislation.vic.gov.au/copyright
(no reproduction except in accordance with the Copyright Act 1968; authorised electronic versions published "for personal
use only"). On 24 October 2026 he answered, in chat:

> "On NT, Vic and SA, yes please go ahead."

The ruling: Legalese Commons may deposit Victorian legislation and quote it in L4 encodings, keeping the copyright
notice, the Government Printer's attribution and a notice that the version is unofficial. The ruling is about the
licence only. It does not lift robots.txt: nothing is fetched from a path that robots.txt disallows.

## Deposit, 7 November 2026

The text is deposited, under the ruling above. robots.txt still keeps a crawler off the register's Word and PDF files,
so the owner saved the Word file by hand, in a browser, on 2026-11-07, and it was converted from that copy.

- **Saved from**: https://www.legislation.vic.gov.au/in-force/acts/powers-attorney-act-2014/007 (Version No. 007, incorporating amendments as at 26 April 2021, the current version on 2026-11-07).
- **Word file**: https://content.legislation.vic.gov.au/sites/default/files/2021-04/14-57a007.docx (identified from its own cover: title, number, version and date).
- **Deposited text**: `registers/source-bundle/powers-of-attorney-act-2014.txt`, a plain-text conversion headed by the copyright notice, the Government
  Printer's attribution and an unofficial-version notice; hashes, the page read and the conversion are in `powers-of-attorney-act-2014.meta.json`.
- **Authorised version**: https://content.legislation.vic.gov.au/sites/default/files/2021-04/14-57aa007%20authorised.pdf. It was not saved; it is the version to check the conversion against.
- **Reconverted, 7 November 2026**: the converter first used dropped every Word symbol character with a code of F000 or more, and the register sets its raised decimal point, multiplication sign, minus sign and bullet that way (in the Symbol font), and its tick-boxes in Wingdings. The text was converted again from the same Word file with the fixed converter, `vic_convert2.py`. In this Act the only characters lost were the three tick-boxes before the commencement options of the Schedule form ("immediately", "on this date", "on this occasion"), now restored as "[ ]". No number or sign was lost. Nothing else changed (checked by a diff); the notice header and line numbers are unchanged. The new hash and the record of the change are in `powers-of-attorney-act-2014.meta.json` (`text.reconverted_2026_11_07`).
