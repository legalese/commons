# Source licence: Corporations Law (Brazil, Lei nº 6.404, 1976)

**Not protected by copyright.**
Lei nº 9.610, de 19 de fevereiro de 1998 (the Copyright Act), art. 8º:

> Não são objeto de proteção como direitos autorais de que trata esta Lei: […]
> IV - os textos de tratados ou convenções, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais;

That was checked on 2026-10-21 against Planalto's own text of Lei nº 9.610 (https://www.planalto.gov.br/ccivil_03/leis/l9610.htm, fetched 2026-10-21, 148,434 bytes), word for word.
A *lei* is named in art. 8º IV, so the text may be reproduced, including verbatim quotation inside an encoding.

One point is not settled here, and the sibling subject `codigo-penal-1940` states it first.
Planalto's compilation adds editorial matter to the statute: the "(Redação dada pela Lei …)", "(Incluído pela Lei …)" and "(Vide …)" notes, the strike-through of superseded wording, and the page layout.
It is published by the Casa Civil da Presidência da República, which makes it arguably one of the *demais atos oficiais* in art. 8º IV.
No ruling on that point was found, so treat the notes as **probably unprotected, not established**.
The encodings quote the statute's text, not the notes.

Only the Diário Oficial text is official.
Each Planalto page says so in its footer ("Este texto não substitui o publicado no DOU …"); the deposited text is a compiled working text.

## What was deposited

The text of Corporations Law (Brazil, Lei nº 6.404, 1976) was deposited on 2026-10-21 under `registers/source-bundle/`, one UTF-8 text file per page and a `.meta.json` beside it holding the digests, the page's address and the checks below.
Superseded wording, which Planalto shows struck through, is kept but wrapped as `⟦STRUCK: …⟧` so it can never be read as current law.

| page | address under `https://www.planalto.gov.br/ccivil_03/` | size | lines of text | sha256 of the page (first 12) |
|---|---|---|---|---|
| `lei6404-sa` | leis/l6404consol.htm | 757,607 bytes | 2593 lines | `4d28ee2f7b8b` |

## Checks run on this deposit

**Control for the extractor.** The extractor used here (a parser-based rewrite; it is not deposited in this repository) was run on the page that the sibling subject `codigo-penal-1940` saved on 2026-09-29, and reproduced that subject's `codigo-penal-1940.txt` byte for byte (sha256 `899c987ee1b1b9879a2040d50e4c0c7946e286872d7c4c107cae140a40d3272a`).
A fresh fetch of the same Planalto page today differs from that text by one added line, "(Vide Lei nº 4.611, de 1965)", so the fetch route itself reproduces the sibling.
The sibling's six `⟦STRUCK:⟧` wrappers enclose only blank markup, so that control checks the extraction mechanics, not the handling of struck text.

**Completeness.** For every page, the multiset of non-whitespace characters in the text equals the multiset in a second HTML parser's reading of the same page (no characters missing, none extra; the one exception is a single asterisk after the closing `</html>` of Lei nº 15.270, which the extractor keeps and the second parser does not, and which that page's meta file notes), and the characters inside `⟦STRUCK:⟧` equal the second parser's count of text under `<strike>`, `<s>`, `<del>` or a `line-through` style.
The figures are in each `.meta.json`.
A struck passage can be marked by a `<strike>` tag or by CSS alone; the sibling's extractor handled only the tag.

**Structure.** The meta files list the article numbers with no opener line.

## Access checks of 2026-10-21

`https://www.planalto.gov.br/robots.txt` answered **404** (an error page, so no rules) to the User-Agent below.
The first probe, with the plain User-Agent `legalese-commons/1.0 (+https://github.com/legalese/commons; statute sourcing for Legalese commons)`, had its connection reset; the second, with the form below, was answered.
The log below records both requests but not their outcomes: the reset was noted at the time and left no file, and the 404 page of the second probe is the one saved.
Every later request used `Mozilla/5.0 (compatible; legalese-commons/1.0; +https://github.com/legalese/commons)`, which keeps the identification and the address of the project inside the `Mozilla/5.0 (compatible; …)` form crawlers conventionally use, with at least 6 seconds between requests.

The requests of that day, in order:
  - 2026-10-21T09:20:32Z [legalese-commons/1.0 (+https://github.com/legalese/commons; statute sourcing for Legalese commons)] https://www.planalto.gov.br/robots.txt
  - 2026-10-21T09:20:38Z [Mozilla/5.0 (compatible; legalese-commons/1.0; +https://github.com/legalese/commons)] https://www.planalto.gov.br/robots.txt
  - 2026-10-21T09:21:48Z https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm
  - 2026-10-21T09:22:00Z https://www.planalto.gov.br/ccivil_03/leis/l6404consol.htm
  - 2026-10-21T09:22:25Z https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm
  - 2026-10-21T09:23:06Z https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm
  - 2026-10-21T09:23:31Z https://www.planalto.gov.br/ccivil_03/leis/l8742.htm
  - 2026-10-21T09:23:48Z https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/D9580.htm
  - 2026-10-21T09:25:01Z https://www.planalto.gov.br/ccivil_03/leis/l7713.htm
  - 2026-10-21T09:25:13Z https://www.planalto.gov.br/ccivil_03/leis/l9249.htm
  - 2026-10-21T09:25:25Z https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
  - 2026-10-21T09:25:36Z https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/L15270.htm
  - 2026-10-21T09:25:47Z https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm
  - 2026-10-21T09:30:19Z https://www.planalto.gov.br/ccivil_03/leis/l9610.htm
