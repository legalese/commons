# Provenance of the source text

| file | what it is | sha256 |
| --- | --- | --- |
| `WPA1983.txt` | text extracted (pypdf 6.20.1, plain mode) from the PCO PDF "Wages Protection Act 1983 version 25_0 as at 27 November 2025", supplied by the user on 2026-10-15; 467 lines, 12 pages. The encoding's references are to this file | `f20a7186a704ff40ac05104ff89037dd0bcc51892410913e30eeb2fc5d80bcc5` |

- **The PDF itself is not deposited** (at the user's direction). It is `935ded4a32568a33b976fbfca7230260664d77f8d7d5fb2e07e060b67d04a367` (sha256, 401,270 bytes), from the New Zealand Legislation website (https://www.legislation.govt.nz/), published by the Parliamentary Counsel Office.
- **Status**: the PCO's consolidation "version as at 27 November 2025". Note 2 of the PDF says that under s 78 of the Legislation Act 2019 the electronic consolidation is an official version. It is the same version as the XML-derived text in `../registers/source-bundle/act_public_1983_143.txt` (version id `act_public_1983_143_en_2025-11-27`, harvested from the PCO's Data API on 2026-10-13), which was the latest version on that date.
- **Completeness**: checked. Sections 1-19, the Schedule and the endnotes are present.
- **Extraction notes**: the text carries running heads (for example "Version as at 27 November 2025 Wages Protection Act 1983 s 5"), page numbers, the table of contents and the amendment history notes after sections. None of these is part of the operative text.
