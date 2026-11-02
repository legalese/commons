# SOURCE-LICENSE: terms of the quoted source text

This file records the terms the QUOTED LEGAL TEXT carries.
It is not the licence of the encoding, which is Apache-2.0 like the rest of canon.

## The source

- Text: the Interpretation Act 2005 (Ireland), Act No. 23 of 2005, as enacted, English text only.
- Form: `No.-23-of-2005.txt`, a plain-text rendering made by a converter script from the electronic Irish Statute Book's English print view.
  **It is an unofficial rendering, not the official text.**
  Nothing in this row is "verified against the official text"; `srcrefs.py check --strict` compares the modules' quotations with that rendering only.
- sha256 of the rendering: `0108a07dd3db98b0058eacee0baabc34ce41823a52c57d2b52ae94b1bb7893d4`.
- Where it came from: https://www.irishstatutebook.ie/eli/2005/act/23/enacted/en/print.html (retrieved 2026-10-21), as recorded in `../../registers/source-bundle/No.-23-of-2005.meta.json`.

## The terms

The subject's licence note is `../../SOURCE-LICENSE.md` (in the run's inputs directory).
It states the terms, the date they were checked and the attribution required, and it is not repeated here.
This run did not re-check them.
All this row does with the text is quote it in the modules with the notice below.

## The notice, copied mechanically from line 4 of the rendering

The same line heads every module that quotes the text.

> (c) Government of Ireland. Oireachtas Copyright Material is reproduced with the permission of the Houses of the Oireachtas.

## What the modules quote

Each `ie-*.l4` module that quotes the Act's text does so in `-- src:N | text` comment lines that `srcrefs.py quote` copied from the rendering, line by line, and cites each with an `@ref` that carries the same line numbers.
Two test files, `tests-schedule-definitions.l4` and `tests-acts-referred-to.l4`, repeat lines of the text in comments beside the assertions that were written from them, and carry the same notice in their headers; `srcrefs.py` does not check those comments.
The other test files quote at most a phrase or two.
`NOTES.md` section 1 says how this is checked.

## Not covered

The Irish-language text of the Act is not deposited and no term for it was checked.
