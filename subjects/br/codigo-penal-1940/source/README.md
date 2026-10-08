# Sources: Código Penal (Decreto-Lei 2.848/1940)

Fetched 2026-09-29 by `fetch.sh`; digests in `SHA256SUMS`.
The encoding reads `codigo-penal-1940.txt` and nothing else.

| file | what it is |
| --- | --- |
| `del2848compilado.htm` | Planalto's compiled text, the "Texto Atualizado" that LexML points at. Windows-1252 HTML with no charset declaration. |
| `extract.py` | turns that HTML into `codigo-penal-1940.txt`, one source paragraph per line |
| `codigo-penal-1940.txt` | the text encoded from; its digest is the one the source bundle pins |
| `vide-index.tsv` | the 38 `(Vide …)` pointers in the text, numbered V1–V38 for the P2 sweep (V34–V38, the bare pointers to Lei 8.072, were added after sweep-b found the first inventory incomplete) |
| `senado-dadosabertos-527942.xml` | the Senado's amendment metadata for the Code (see below) |
| `lexml-record.html` | the LexML index page, kept as evidence of what it pointed at |

## Was LexML's structured XML any use?

**No, because there was none to use.**
LexML does define a full-text XML schema for Brazilian laws (technical norm LexML-BR Parte 3, which follows the Parte / Título / Capítulo / Artigo / § / inciso hierarchy that Lei Complementar 95/1998 prescribes).
But no instance of the Código Penal in that schema was found at any of the places LexML leads to:

- **The LexML record** (`lexml-record.html`) offers three texts, all `text/html`: Planalto's updated compilation, and the Câmara's and Senado's copies of the 1940 original.
- **The Senado's open-data API** (`legis.senado.leg.br/dadosabertos/legislacao/527942`) does return `application/xml`, but it is metadata, not text.
  See the next section.
- **normas.leg.br**, the LexML-based viewer the Senado record links to, publishes a schema.org JSON-LD record whose `encoding` entries, for both the original and the current version, are `text/html`.
  One of the two binary URLs it lists returned 404 when fetched. The other was not fetched.

So the Code was **converted to plain text at the first opportunity**, and its structure was recovered afterwards by regular expression, from line prefixes such as `Art. 121`, `§ 2º` and `TÍTULO I`.
That cost something measurable.
The first pass at listing the articles missed `Art 187.` (no full stop after "Art"), `⟧ Art. 189.` (an article opening straight after a struck-through passage) and `Art. 359-M-A` (a double suffix).
They were caught only because the enumeration is checked against "every article number from 1 to 361 is present".
A LexML-XML instance would have made that whole class of error impossible.
The six struck-through passages survive in the text wrapped as `⟦STRUCK: …⟧`, so revoked wording cannot be mistaken for law in force.

## The one structured source that did help: the Senado's `vides`

`senado-dadosabertos-527942.xml` lists **164 later norms** that affected the Code.
Each entry carries its signing and publication dates and names the dispositivos it touched, labelled Alteração (371), Acréscimo (184), Dispositivo Correlato (138), Revogação (24), Revogação de Parte do Texto (12) or Acréscimo Vetado (11).
Six entries are STF rulings. Five of them give an **interpretação conforme a Constituição**, and the Senado labels seven provision entries with that phrase between them:

- ADI 3.150 (2018), on art. 51
- ADPF 779 (2023), on arts. 23 II and 25, the "legítima defesa da honra" argument
- ADI 7.032 (2024), on art. 51
- ADPF 1.107 (2024), on art. 59
- ADPF 569 (2024), on art. 91 II b

The sixth, ADPF 496 (2020), is listed against art. 331 (desacato) as a Dispositivo Correlato.

This is the dated, per-provision amendment inventory that Planalto's inline notes give only as prose.
The P2 sweep reads it as its starting point.

## Caveats

- **Not official.** Only the Diário Oficial text is official; the Planalto page says so in its footer.
- **The raw HTML is not reproducible.** Planalto's F5 load balancer injects a per-request `<script>`, so `del2848compilado.htm` hashes differently on every fetch.
  The extracted text is stable: two fetches produced byte-identical output.
- **The LexML → Planalto link is broken.** LexML's own link to Planalto (`legislacao.planalto.gov.br/…/websearch?…`) answered 302 and then reset the connection on 2026-09-29.
  `fetch.sh` goes straight to Planalto's stable `ccivil_03` URL instead.
