# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| `MWA1983.txt` | text extracted (pypdf 6.20.1, plain mode) from the PCO PDF "Minimum Wage Act 1983 version 38_0 as at 20 December 2023", supplied by the user on 2026-10-15; 616 lines, 18 pages. The encoding's references are to this file | `efd7491bf98ebdc431b99516318f31248c2c6968fa8fb607ad27327a1392f017` |

- **The PDF itself is not deposited** (at the user's direction). It is `676e1bb1ff10dd31e404af53d6e4e6dd948b9415710765551cfc775c9bc59d0e` (sha256, 477,021 bytes), from the New Zealand Legislation website (https://www.legislation.govt.nz/), published by the Parliamentary Counsel Office.
- **Status**: the PCO's consolidation "version as at 20 December 2023". Note 2 of the PDF says that under s 78 of the Legislation Act 2019 the electronic consolidation is an official version. Whether a later version exists (an amendment after 20 December 2023) was not checked: the register refuses scripted clients.
- **Completeness**: checked. Sections 1-14, Schedules 1AA and 1, the reprinted transitional provisions of the Minimum Wage Amendment Act 2007 (s 6) and the Minimum Wage (Starting-out Wage) Amendment Act 2013 (s 7), and the endnotes are present.
- **Extraction notes**: the text carries running heads (for example "Version as at 20 December 2023 Minimum Wage Act 1983 s 4"), page numbers, the table of contents, the Legislation Act 2019 publication tables, and the amendment history notes after sections. None of these is part of the operative text.
- **The rates themselves are not in the Act.** They are prescribed by Order in Council (the Minimum Wage Order of each year) under ss 4, 4A and 4B, which is not deposited here. The encoding takes the Order's rates as inputs.
