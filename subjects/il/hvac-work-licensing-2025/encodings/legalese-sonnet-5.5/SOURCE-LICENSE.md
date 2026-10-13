# SOURCE-LICENSE.md

This file records the terms the quoted source text carries.
It is not the licence of the encoding, which `encoding.json` gives as Apache-2.0.

## Status: undetermined

**The terms of the source texts are undetermined.**
None of the input files carries a licence statement, copyright notice or terms of reuse for the text it holds, and the brief does not supply one.
No grant is claimed here, because none was found.
The Hebrew text of the Law and the regulations is quoted in comments across the modules (the quotations are copied by script from the files below, and not retyped).
The question of whether quoting it is permitted is therefore real and open; it belongs to someone qualified to answer it, who should read the instruments themselves.
Three things remain to be established, none of which this encoding establishes: the status of the gazette text itself, the licence the Hebrew Wikisource texts carry (the two `.wiki` files record revision numbers but no licence), and the terms on which the screenshot and the English caption page, which come from a published paper, may be quoted.
The screenshot is quoted only as short phrases (the panel's outcome words, headings and the draft's regulation text) and as a transcription of its table.

## Sources

The sha256 values are of the files as supplied in `inputs/`.

| file | what it is | authority | sha256 |
| --- | --- | --- | --- |
| `sefer-hachukim-3349-pp182-209.pdf` | the Law, official gazette issue Sefer HaChukim 3349, 14 January 2025, pp 182-209 | authoritative | `8ff58ab8023568363994ad1a325d4b2829422bd993d317a8bf9b6bf44b28b168` |
| `sefer-hachukim-3349-pp182-209.txt` | text extraction of the same issue (right-to-left layout artefacts; margin notes interleaved) | aid | `56bb076074d0a4a290ac0eb44f05e8a2596b400725f89ed8d82f915769ee361c` |
| `law.wiki` | the Law, Hebrew Wikisource rev 2947808 (OpenLawBot, 2025-07-10); header records the gazette PDF https://fs.knesset.gov.il/25/law/25_lsr_5482863.pdf | aid (unofficial) | `e8a8ac3bedbc0e7b34dda6c71a4030224c5bbae8af71c47099f393f44eb1c485` |
| `kovetz-hatakanot-11951-p2116.pdf` | the Fees Regulations as made, Kovetz HaTakanot 11951, 9 July 2025, p. 2116 | authoritative | `fe5d0d1080858f6f4ff06128b7342f2f1d865c265f05083382c23d8b01954b1f` |
| `kovetz-hatakanot-11951-p2116.txt` | text extraction of the same page | aid | `fcf7cf8a4b872da8c8fce6962764d16cb21e5780348cdd1929e19ccc33417c05` |
| `takanot-12383.pdf` | the 5786 amendment, Kovetz HaTakanot 12383, 4 May 2026, p. 2062 | authoritative | `b034686dfd8b537df0e5015a09e7207a2db1de908a2506fbebb78e112e33e007` |
| `takanot-12383.txt` | text extraction of the same page | aid | `56381444a5437e0860c21802d98432aa50d2e325234dd8e01687f8da7eeb9b76` |
| `regulations-fees.wiki` | consolidated Fees Regulations, Hebrew Wikisource rev 3011135 (OpenLawBot, 2026-05-04); its boxes link https://olaw.org.il/takanot/takanot-11951.pdf and https://olaw.org.il/takanot/takanot-12383.pdf | aid (unofficial) | `4c08bf33dbfa1b4c36108174c9d769f6537dd1c6d30651f161023cec0bcf09a2` |
| `revisions.json` | the Wikisource revisions of the two wiki files | aid | `84cb0a971b8829d42e0e54b20747241c46c4576b0190e267177c3ae2e19020c8` |
| `knesset-bill-25_ls2_5256851.pdf` | the bill for second and third reading, 11 December 2024 | aid (used only to check section numbering) | `6ded44c4ed2397befd510a6e91c6de1744db1c4d8a8ef189392e8c3a9ec392fb` |
| `fig4-simplex-screenshot.png` | Figure 4 of Schwartz, Bar-Siman-Tov & Gelbard (2025): screenshot of the SimpLEX drafting-and-testing tool (crop) | the only source for the draft vintage; an image | `259ac9e4000020d9062dedae0fbd39989ba666799d6e50b525d32ecc2cc86f27` |
| `fig4-page34-400dpi.png` | the whole page of the paper carrying the figure | aid | `eb4472b2e4a1459b9938d02c9bd8af1c6fe58b3b269eeb66942c770e865e4b47` |
| `fig4-en-p28-28.png` | the English page of the paper carrying the figure caption (page 379 of the journal) | aid | `9b3328a07fb55af03e5a72c97747ca705c56a2b412ae77b989d81612131ccb31` |

Fetch dates and original URLs are not recorded in the inputs beyond the links the two Wikisource files carry (above), so none is asserted here.
