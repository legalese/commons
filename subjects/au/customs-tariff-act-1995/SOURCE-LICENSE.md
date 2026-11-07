# Source license

The quoted text of **Customs Tariff Act 1995** is sourced from the [Federal Register of Legislation](https://www.legislation.gov.au/).

- **Copyright owner**: Commonwealth of Australia.
- **License**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
- **Terms checked**: 2026-09-22, at https://www.legislation.gov.au/terms-of-use
- **Source**: https://www.legislation.gov.au/C2004A04997/latest/text
- **Excluded from the license**: coats of arms, logos and trade marks on the source site,
  and any material marked otherwise.

## Required attribution

Sourced from the Federal Register of Legislation at 2026-09-22: "Customs Tariff Act 1995", Commonwealth of Australia, licensed under CC BY 4.0
(https://creativecommons.org/licenses/by/4.0/).

If this encoding modifies or adapts the quoted text (rather than reproducing it verbatim),
the attribution must instead read "Based on content from the Federal Register of Legislation ...", per the CC BY 4.0
terms.

## Status of this deposit

Statute text deposited 2026-09-22: `registers/source-bundle/C2004A04997.txt`, converted to plain text from
https://api.prod.legislation.gov.au/v1/Documents/Find(titleid='C2004A04997',asatspecification='Current',type='Primary',format='Word',uniquetypenumber=0,volumenumber=1..7,rectificationspecification='Latest')
(compilation register id: C2026C00399). sha256 of the download: `4393e1e1365cec7b9bf4844d65d8de063bcbb92282b10e6548a6d0b66ad178e2`.

Formulas, symbols and pictures the text deposit lost are transcribed 2026-10-24 in `registers/source-bundle/C2004A04997.formulas.md`, from the Word rendering of the same compilation (C2026C00399) on the same Register and under the same licence (CC BY 4.0, as above): https://api.prod.legislation.gov.au/v1/Documents/Find(registerid='C2026C00399',type='Primary',format='Word',uniquetypenumber=0,volumenumber=1,rectificationspecification='Latest') (volumes 1 to 7).

- **Reconverted, 7 November 2026**: the first converter (docx_text() in the workbench's tools/fetch/fetch-source.py)
  dropped Word symbol characters and kept Symbol-font characters typed as text as private-use code points. The text
  was converted again from the same seven Word volumes (same download sha256) with cth_convert_sym.py (kept outside the
  repository); the only changes are five degree signs restored ("20 °C" in Chapter 22 Note 2, Subheading Note 1 and
  Additional Note 2, lines 4940, 4943 and 4946; "between 15 °C and 30 °C" in Chapter 59 Note 2(a)(2), line 16715).
  Now 1,864,723 characters, sha256 `e7d0d57fb1a3de08d01b64cc43a12beb4c912c9adaf50b0ff1c0e87b7ab6716a` (was
  `731cd802878252870983673bc3abbb4bb0f0e1185cb4dabcb4d2083924d41681`); details in `C2004A04997.meta.json`.
- **Reconverted again, 8 November 2026**: cth_convert_sym.py did not map the Symbol-font digits, so the subscript
  digits of subheading 6902.20.00 (line 19051) were still missing. Converted again from the same seven Word volumes with
  cth_convert_sym_v4.py (kept outside the repository), which maps Symbol F030-F039 to 0-9; the only change is that line,
  now "alumina (Al2O3), of silica (SiO2)". Now 1,864,726 characters, sha256
  `c2b58b9ad8d6d3ee626689f48f2fd10a528a54c5329d3c5901d0dca870a68c26` (was `e7d0d57fb1a3de08d01b64cc43a12beb4c912c9adaf50b0ff1c0e87b7ab6716a`).
