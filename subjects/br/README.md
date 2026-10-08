# brazil/

Brazilian legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

**Licence: open.** Lei nº 9.610/1998 (the Copyright Act), art. 8º IV, excludes "leis, decretos, regulamentos, decisões judiciais e demais atos oficiais" from copyright.
Portuguese is the official language (Constituição, art. 13), and there are no official translations.
Only the text published in the Diário Oficial da União is official. The consolidated texts that Planalto publishes ("Texto compilado") are working texts; the Código Penal's page says so in its footer.
Whether Planalto's editorial notes ("Redação dada pela Lei …", "Vide …") are themselves unprotected is not settled; see [`codigo-penal-1940/source/SOURCE-LICENSE.md`](codigo-penal-1940/source/SOURCE-LICENSE.md).

| subject | Law | Portuguese title | topics |
|---|---|---|---|
| [`codigo-penal-1940/`](codigo-penal-1940/) | Penal Code | Código Penal — Decreto-Lei nº 2.848, de 7 de dezembro de 1940 | Criminal law |

## Finding the text: LexML and its neighbours

Written 2026-10-08 from what the Código Penal encoding found when fetching its sources on 2026-09-29 and 2026-09-30.
The detailed account, with file names and digests, is in [`codigo-penal-1940/source/README.md`](codigo-penal-1940/source/README.md).

### What LexML is

LexML (`lexml.gov.br`) is Brazil's national network for legal information, run by the Senado Federal.
It is an **index of metadata about** legal documents, not a store of their text.
One record gathers a norm's identifier, links to the publishers that hold its text, and related bills and legal doctrine: the Código Penal's record does all three.

According to LexML's published technical standards, it offers:

- **Permanent names (URN:LEX).** Every norm, judgment or bill has a stable identifier, independent of any one publisher's URL. The Código Penal is `urn:lex:br:federal:decreto.lei:1940-12-07;2848`.
- **One search across many publishers:** legislation, case law, bills and doctrine.
- **Bulk metadata harvesting** over OAI-PMH, the archives' standard protocol.
- **A full-text XML schema for laws** (LexML-BR Parte 3), following the Parte / Título / Capítulo / Artigo / § / inciso structure that Lei Complementar nº 95/1998 prescribes for federal laws.

### What it gave in practice

- **No structured text.** The Código Penal's record offers three texts, all HTML: Planalto's "Texto Atualizado", and the Câmara's and the Senado's copies of the 1940 original. No instance of the Code in LexML's XML schema was found anywhere LexML leads, including normas.leg.br, whose machine-readable record gives the text's encoding as HTML for both the original and the current version (of the two binary links it also lists, one returned 404 and the other was not fetched).
  So the text was converted to plain text at once, and its structure recovered by pattern matching on line prefixes. That missed three articles on the first pass (`Art 187.` with no full stop, an article opening straight after struck-through text, and the double suffix of `359-M-A`). A check that every article number from 1 to 361 is present caught them; an XML instance would have made that class of error impossible.
- **A broken link.** LexML's link to Planalto (`legislacao.planalto.gov.br/…/websearch`) answered a redirect and then reset the connection on 2026-09-29. Planalto's own `ccivil_03` URLs work, so fetch from there.
- **Character encoding.** Planalto's HTML is Windows-1252 and declares no charset. Decoding it as ISO-8859-1 corrupts the en dash on 80 lines, and two lines needed NFC normalisation.
- **No stable bytes.** Planalto's load balancer injects a per-request script, so the HTML hashes differently on every fetch. Pin the extracted text, which is stable, rather than the page.

### Where it did help

- **Amendment metadata.** The Senado's open-data API (`legis.senado.leg.br/dadosabertos/legislacao/<id>`), run by the same institution, returns real XML. For the Código Penal it lists every later norm that touched the Code, and six STF rulings, each with its dates and a per-provision label (Alteração, Acréscimo, Revogação, Interpretação conforme a Constituição and so on). That inventory is the natural starting point for a sweep of later amendments.
- **Court judgments.** LexML holds records of judgments too. The encoding's sweep quotes an STJ judgment's ementa and decision from its LexML record (Corte Especial, HC 239.363/PR), read in a browser.

### The courts' own sites

Measured from Singapore, 2026-09-29 and 2026-09-30:

- **STF** (`portal.stf.jus.br`) refuses foreign IP addresses with HTTP 403, even in a real browser. From an AWS instance in São Paulo (`sa-east-1`) its case pages load. The tabs a case page loads are `processos/aba{Decisoes,Andamentos,Informacoes,Partes,Sessao,Pautas}.asp?incidente=N`, and those are the URLs to cite.
  After about 50 requests in ten minutes the portal began refusing that IP too, before the decision PDFs (`downloadPeca.asp`) had been fetched. Fetch the PDFs first and space the requests out.
  `jurisprudencia.stf.jus.br` serves a JavaScript challenge even from Brazil.
- **STJ** (`scon.stj.jus.br`, `www.stj.jus.br`) is not geo-blocked. It serves a Cloudflare JavaScript challenge, which a real browser passes.

### In short

LexML is good at naming and finding Brazilian legal documents and at recording how they relate.
It did not supply the text of the Código Penal in structured form; other codes have not been checked.
For text, go to Planalto; for amendments, go to the Senado's open-data API; for court decisions, LexML's records are worth trying alongside the courts' own sites.
