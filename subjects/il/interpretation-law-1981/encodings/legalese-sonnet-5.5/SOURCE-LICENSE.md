# Source licence

This file records the terms the quoted legal text carries. It is not the licence of the encoding, which is Apache-2.0 like the rest of canon.

## What is quoted

`source/law.wiki` and `source/ordinance.wiki` are Hebrew Wikisource consolidations of the Interpretation Law 5741-1981 and the Interpretation Ordinance [New Version] (revisions 2883979 and 2966850, fetched 2026-10-13). The encoding quotes them in `-- src:N | …` comments and in the strings of `il-interpretation-carried-text.l4`.

## The statutes

The task brief states that statutes carry no copyright under the Israeli Copyright Act 5768-2007, s. 6. I took that from the brief; the Copyright Act is not among the sources, and I did not look the provision up.

## Wikisource's own additions

Wikisource's editorial additions, if any survive in what is quoted, are CC BY-SA 4.0. They cannot be separated mechanically from the statute: the wikitext carries Wikisource's own notes (the `{{ח:הערה|…}}` template) beside the statutory text. The encoding quotes some of those notes, and says so where it does: the note under the "coastal waters" definition of s. 3 (`law.wiki` line 48); the notes in the blank ss. 27 to 30 (lines 147, 150, 153, 156); the head note and the s. 1 note of the Ordinance (`ordinance.wiki` lines 12 and 31); the notes in Ordinance s. 1 that restate pre-Law definitions. Anyone reusing those quotations should treat them as possibly CC BY-SA 4.0 with attribution to Hebrew Wikisource and its contributors.

## The official text

The official texts could not be fetched (`fs.knesset.gov.il` returned an HTML "Unavailable" page for every request), so the terms of the official publication were not examined. Nothing here is verified against the gazette.

### Update, 2026-10-13, after the run (added by the launching session)

The official texts were fetched after the encoder finished, through an Israeli address; they are in `source/official/` with their sha256 in `source/official/OFFICIAL-SOURCES.md`.
The terms of the official publication were still not examined.
s. 10 of the Law as enacted matches `law.wiki` word for word; nothing else was compared.

