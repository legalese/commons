# Source licence: Swiss Code of Obligations (OR), Art. 336 to 336b: abusive termination of an employment contract

The deposited text is German; no other language of the Act is deposited.
- `ch-or-sr220-art-336-336b-20261001.txt`: Art. 336, 336a and 336b of the Code of Obligations (SR 220): abusive termination, its sanctions and the procedure; sha256 values in the `.meta.json` file of the same name.
- `ch-or-sr220-art-333-335f-context-20261001.txt`: Art. 333 and 335f of the Code of Obligations (SR 220): the two provisions Art. 336(2)(c) and (3) refer to, deposited as context (not part of the encoded scope); sha256 values in the `.meta.json` file of the same name.

## Terms

- **Basis**: Art. 5 of the Urheberrechtsgesetz (URG, SR 231.1), "Nicht geschützte Werke". Fetched on 2026-11-17 from Fedlex, the consolidated version applicable from 2025-07-01 (XML file `eli/cc/1993/1798_1798_1798/20250701/de/xml/fedlex-data-admin-ch-eli-cc-1993-1798_1798_1798-20250701-de-xml-7.xml`, sha256 `4f98ae50ab3d5e7b91c1b26692a3fd208a1db725ad4d446dd206c8c3e698e7cb`), verbatim:

  >
  > Art. 5 Nicht geschützte Werke
  > 1 Durch das Urheberrecht nicht geschützt sind:
  >   a. Gesetze, Verordnungen, völkerrechtliche Verträge und andere amtliche Erlasse;
  >   b. Zahlungsmittel;
  >   c. Entscheidungen, Protokolle und Berichte von Behörden und öffentlichen Verwaltungen;
  >   d. Patentschriften und veröffentlichte Patentgesuche.
  > 2 Ebenfalls nicht geschützt sind amtliche oder gesetzlich geforderte Sammlungen und Übersetzungen der Werke nach Absatz 1.

  Art. 5(1)(a) and (2) cover the Act deposited here and Fedlex's consolidated version of it.
- **Fedlex's own terms**: not read. Fedlex's pages are a JavaScript application: a `GET` of `https://www.fedlex.admin.ch/de/legal-notice` (and two other paths tried) returns the same 77,151-byte application shell as `https://www.fedlex.admin.ch/de/`, and no legal-notice text was found in the application's script files. This is an inability to read, not a refusal by the site.
- **The federal administration's notice**: `https://www.admin.ch/gov/de/start/rechtliches.html` redirects to `https://www.admin.ch/de/rechtliches`, which answered 200 on 2026-11-17. Its copyright paragraph, verbatim:

  > Copyright, Bundesbehörden der Schweizerischen Eidgenossenschaft. Die auf den Websites der Bundesbehörden enthaltenen Informationen werden der Öffentlichkeit zugänglich gemacht. Durch das Herunterladen oder Kopieren von Inhalten, Bildern, Fotos oder anderen Dateien werden keinerlei Rechte bezüglich der Inhalte übertragen. Die Urheber- und alle anderen Rechte an Inhalten, Bildern, Fotos oder anderen Dateien auf den Websites der Bundesbehörden gehören ausschliesslich diesen oder den speziell genannten Rechtsinhabern. Für die Reproduktion jeglicher Elemente ist die schriftliche Zustimmung der Urheberrechtsträger im Voraus einzuholen.

  That notice is for "the websites of the federal authorities" and does not mention legislative texts. It is recorded for completeness, and the deposit rests on Art. 5 URG above.
- **robots.txt**: `https://www.fedlex.admin.ch/robots.txt` was read on 2026-11-17: `User-agent: *`, `Allow: /`, and `Disallow` only for URLs with `print`/`printId` parameters (`/*?print=*`, `/*&print=*`, `/*?printId=*`, `/*&printId=*`). `https://fedlex.data.admin.ch/robots.txt` (the linked-data host) was read the same day: `Disallow: /filestore/*` for every agent. The text files were therefore fetched from `www.fedlex.admin.ch/filestore/...`, the site's own host, and not from `fedlex.data.admin.ch/filestore/`; only the data endpoint `https://fedlex.data.admin.ch/sparqlendpoint` was queried on that host, to find the file locations.
- **Rights holder**: the XML files name `ch.bk` (the Federal Chancellery) as publisher and rights holder in their metadata.
- **Requests**: the User-Agent was `legalese-commons/1.0 (+https://github.com/legalese/commons; statute sourcing for Legalese commons)`, with a pause of at least two seconds between downloads.
- **Terms checked**: 2026-11-17.
- **Attribution**: Fedlex, Swiss Federal Chancellery, for the consolidated text.

## Language

German is the only language deposited. The encoding quotes the German and glosses it in English in comments; an English gloss is not the text. Whether the consolidated version on Fedlex or only the Official Compilation of Federal Legislation is the authoritative text was not established here (Fedlex's own statement was not read).

## The encoding

The encodings under `encodings/` are licensed under **Apache-2.0**, per the repository `NOTICE`.
That licence covers the encodings only, not the quoted legislative text.
