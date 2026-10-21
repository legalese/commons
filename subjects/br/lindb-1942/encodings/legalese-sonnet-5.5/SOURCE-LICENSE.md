# Source licence: Decreto-Lei 4.657/1942 (Lei de Introdução às normas do Direito Brasileiro)

This file records the terms the quoted source text carries.
It does not give the licence of the encoding, which is Apache-2.0.

## What the encoding quotes

The encoding quotes the statute's text, one raw line at a time, in the `-- src:N | ...` comment lines of the four `.l4` modules (91 quotation lines).
Each quotation was produced by `quote-lines.py expand` from the plain-text file the run was given, `../../registers/source-bundle/lindb-1942.pt.txt`, and checked by `quote-lines.py check`.
The quotation tool drops Planalto's editorial notes, such as `(Redação dada pela Lei ...)`, `(Incluído pela Lei ...)`, `(Vide ...)` and `(Vigência)`, so the encoding quotes the statute's words and not Planalto's notes.

## The source file is a converter rendering, not the official text

`../../registers/source-bundle/lindb-1942.pt.txt` is a plain-text rendering of Planalto's compiled page (`https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm`, fetched 2026-10-21), made by a converter script.
Only the text published in the Diário Oficial da União is official, and Planalto's own footer, kept at raw line 112, says so.
The rendering carries one converter marker, `⟦STRUCK: º⟧` at raw line 33.
Nothing in this encoding has been checked against the Diário Oficial text.

## The terms

The terms are recorded in `STUB-SOURCE-LICENSE.md`, a file in the `inputs` directory this run was given, beside the text file.
That file is not copied into this directory, so a path from here to it would not survive the copy into `subjects/br/lindb-1942/`.
Whoever makes the copy should place a copy of that file beside the subject's source text, or check this summary against it.
This file does not depend on it: what it says that matters here is restated below.

What that file says, as I read it (I did not fetch or re-check the statute it cites):

- The text is not protected by copyright: Lei nr 9.610 of 19 February 1998, art. 8, IV, lists among the things not protected `os textos de tratados ou convenções, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais`, and a decreto-lei is a decree issued with the force of a statute. The file concludes that the text may be reproduced, including verbatim quotation inside an encoding.
- One point is not settled: Planalto's compilation adds editorial matter (the amendment and `Vide` notes, the strike-through of superseded wording, the page layout). No ruling on whether that matter is protected was found, so the file says to treat the notes as probably unprotected, not established. The encoding does not quote the notes.
- The compiled text is a working text, not the official one.

The terms of the quoted statute text are therefore as that file states them, and the one open point (the editorial notes) does not affect what this encoding quotes.
If the terms of the source cannot be established to a reviewer's satisfaction, the answer is **undetermined**, and no grant has been assumed beyond what that file records.
