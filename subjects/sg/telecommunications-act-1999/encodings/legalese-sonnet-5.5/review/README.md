# Independent review of the Telecommunications Act and Broadcasting Act encodings

Status: written on 2026-11-04 by the orchestrating session.
This folder holds the record of one independent review of the two encodings in `telecommunications-act-1999/encodings/legalese-sonnet-5.5/` and `broadcasting-act-1994/encodings/legalese-sonnet-5.5/`, both made to answer a question about analogue terrestrial television receivers (see `TV-QUESTION.md` in each).
This README states no answer to that question.
`REVIEW.md` does: it is one reader's answer, re-derived from the deposited texts, with its confidence, and it is neither a statement of what the law is nor a court's view.
The `NOTES.md` files of the two encodings keep to their quarantine and do not repeat it.

## What is here

| file | what it is | who wrote it |
| --- | --- | --- |
| `REVIEW.md` | the reviewer's answer, section 1 written blind from the deposited texts, then sections 2 to 7 after step 4 (readings, receiver kinds, section 9A, checks, confidence) | the reviewer, unedited |
| `DISAGREEMENTS.md` | eleven items (D1 to D11) where the reviewer differs from an encoding; 6 are marked B (identified blind) and 5 are marked P (noticed at step 4 or later) | the reviewer, unedited |
| `MISSED-INSTRUMENTS.md` | what the reviewer searched for and where, including the searches that found nothing | the reviewer, unedited |
| `CITATION-CHECK.md` | the reviewer's check of every quotation and of the decisive chain by hand | the reviewer, unedited |
| `REQUESTS.md` | the reviewer's requests for sources and decisions, and the answers | the reviewer, unedited |
| `DISPOSITIONS.md` | what each encoder did about each of the eleven items, and where | the encoders' accounts, assembled by the orchestrating session |
| `sources/` | provenance notes and extracts for sources the reviewer used that are not deposited elsewhere in the repository (see below) | the reviewer, unedited |

The five reviewer files are byte-for-byte what the reviewer wrote.
In them, "the lead" means the orchestrating session, which is a Claude session and not a person.

## Who reviewed, and what it was shown

The reviewer was a separate Claude session (Opus 5.5).
The method, set by the project owner, was: Sonnet 5.5 encoders, then one independent Opus 5.5 reviewer who is not shown the encoders' conclusion.
The reviewer worked in a read-only copy of the repository tree without `TV-QUESTION.md`, `TV-QUESTION-BA.md`, any `sgta-tv-*` or `sgba-tv-*` module, any `PROGRESS.md`, and the forward-looking row `unstable-multitemporal-2026-11`.
It was told to re-derive the answer from the deposited texts before opening any encoding file, to hunt for instruments the encoders had missed, to check the citations on the decisive chain and a random sample, to test the readings that decide the answer, to run each encoding's `check.sh`, and to list its disagreements.

## Independence: what was and was not independent

A leak happened, and the reviewer reported it itself (`REVIEW.md` section 0, `REQUESTS.md` R2).
At 2026-11-03T19:53:49Z the reviewer's context was compacted and the harness attached four files to it.
One was its own brief, which it had read once.
The other three it had not opened: the script that built its copy, a project memory file kept outside its copy, and a walkthrough of a quarantined row.
The memory file stated both encoders' preliminary answers.
The orchestrating session had written or read those four files earlier, and they match the ones attached, which is why it infers that the harness re-attached files from the orchestrating session's own context to the reviewer.
That mechanism is an inference from the match, not something shown directly.
The reviewer opened none of the three it had not read before.

What survives:

- Section 1 of `REVIEW.md` was last written at 2026-11-03T19:39:36Z, 14 minutes before the compaction, and has not been edited since.
  Its sha256 is `dd6325a0943dd1744ecb76027edca414c6e32b2884d876fd5ad8d5a9b8d36176`.
  To check it: `awk '/^## 1\. /{f=1} /^## 2\. /{f=0} f' REVIEW.md | sed '$d' | shasum -a 256`.
  The orchestrating session ran that command on the copy in this folder on 2026-11-04 and got the same value.
- `CITATION-CHECK.md`, part E2 and E3 of `MISSED-INSTRUMENTS.md`, sections 0 and 2 to 7 of `REVIEW.md`, and `DISAGREEMENTS.md` were written after the compaction and are not blind.
- On the points the leaked file states, the blind section 1 already gives the same answers, so agreement is evidence of independence for section 1 only.
  Nothing in sections 2 to 7 should be counted as a further independent confirmation of it.

## What the review found, in numbers

- Quotations: all 15,530 quote lines in the 97 quoting modules the reviewer checked are verbatim substrings of the source lines they name.
  By hand it found 17 locator-level mismatches of 8 kinds and 2 coverage gaps; none is in a quotation's words and none changes an answer; 15 of the 17 are on the decisive chain; a random sample of 64 had 1.
- Disagreements: 11 items, 6 marked B and 5 marked P (`DISAGREEMENTS.md`).
- The reviewer's own run of each `check.sh` on its copy: the Telecommunications Act encoding 76 modules, 3,003 assertions satisfied; the Broadcasting Act encoding 64 modules, 2,108 assertions satisfied; none failed, refused or errored, and every module read the same on the main build.
  Its copy lacked the quarantined `sgta-tv-*` and `sgba-tv-*` modules, so those totals are lower than the encodings' own; the encodings have grown since, and their current figures are in the "Checks" section of each `NOTES.md`.
- The headline answers of the reviewer's blind section 1 and of both encodings agree at each of the three dates and for each kind of receiver.
  The differences the reviewer recorded are about which reading of a provision to prefer, how much weight a second escape deserves, and how to word confidence; they are items D1 and D2 and the confidence column of `REVIEW.md` section 7.

## Reading these files after the encodings changed

- Line numbers into `NOTES.md` in the reviewer's files are those of the `NOTES.md` the reviewer was shown.
  Both `NOTES.md` files have been edited since, so find a passage by its heading, finding number or fork identifier.
- The reviewer's `file:line` citations into encoding modules are likewise to the modules as the reviewer saw them.
- Its citations into deposited source texts remain valid, because deposited texts are not edited.
  The reviewer wrote them as `sources/<name>/<file>` or through the aliases in `REVIEW.md` section 1.0.
  The next section says where each now lives.

## The reviewer's retrieved sources, and where they are now

Ten of the texts the reviewer fetched from the e-Gazette are identical, byte for byte, to texts the Telecommunications Act encoder deposited later (matched by sha256 of the text file on 2026-11-04), so line numbers carry over:

| reviewer's path | deposited at |
| --- | --- |
| `sources/gazette-cap323-O3-1999/99323o3.txt` | `telecommunications-tas-exemption-specified-equipment-order-1998/registers/source-bundle/TA1999-O3.txt` |
| `sources/gazette-cap323-Rg3-1999/99323rg3.txt` | `telecommunications-radio-communication-regulations-1999/registers/source-bundle/TA1999-RADIO99.txt` |
| `sources/gazette-cap323-Rg7-1999/99323rg7.txt` | `telecommunications-dealers-regulations-1999/registers/source-bundle/TA1999-DEAL99.txt` |
| `sources/gazette-S549-1998/549.txt` | `telecommunications-tas-exemption-specified-equipment-order-1998/registers/source-bundle/TA1999-O3-S549-1998.txt` |
| `sources/gazette-S588-2023/588.txt` | `telecommunications-exemption-notification-2001/registers/source-bundle/TA1999-N1-S588-2023.txt` |
| `sources/gazette-S589-2023/589.txt` | `telecommunications-dealers-regulations-2003/registers/source-bundle/TA1999-RG6-S589-2023.txt` |
| `sources/gazette-S560-2024/560.txt` | `telecommunications-composition-of-offences-regulations-2005/registers/source-bundle/TA1999-COMP-S560-2024.txt` |
| `sources/gazette-S381-2024/381.txt` | `telecommunications-in-vehicle-unit-exemption-notification-2024/registers/source-bundle/TA1999-ERP-S381-2024.txt` |
| `sources/gazette-S22-2011/022.txt` | `telecommunications-cancellation-notification-2011/registers/source-bundle/TA1999-CANC-S22-2011.txt` (the PDF sha256 is also the same, `d682419753b958efb5e28175517e66d12ad734ecb3214cd995019c37f8b058a5`; the text sha256 is `aa8180945959322a8308b39d8ea307216826964831588f7f98ff0ce077e272b0`; the encoder fetched the PDF once, on 2026-11-04) |
| `sources/gazette-SL-index-2010/10rsl_index.txt` | `telecommunications-tas-exemption-specified-equipment-order-1998/registers/source-bundle/TA1999-AID-INDEX2010.txt` (an aid, an index "as at 1 June 2010", not law) |

All paths in the second column are under `subjects/sg/`.

Sources that are not deposited:

- Four IMDA documents, which are guidance or technical documents and not legislation, so they are recorded here by URL, retrieval time and sha256 (`sources/imda-*/SOURCE.md`) and are not redistributed: the Equipment Registration guide of November 2023, the Spectrum Management Handbook, a draft of the technical specification "IMDA TS DVB-T2 IRD" (Issue 1, Revision 2) and IMDA's decision paper on that specification.
  The reviewer read them as evidence of the regulator's practice only, and no graph arrow or encoded rule rests on them.
- Two sets of extracts read through the lawplain server, one of Hansard and one of Bills, each a few sentences with their provenance (`sources/lawplain-hansard/EXTRACTS.md`, `sources/lawplain-bills/EXTRACTS.md`).
  They are extrinsic material, used by the reviewer only for context and purpose and never for the literal reading.
