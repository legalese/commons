# Source license

The quoted text in this folder's `.l4` files, and the tables built from it, is taken from `../../registers/source-bundle/IA1965.txt`, a plain-text rendering of the Interpretation Act 1965 (Singapore) made by a converter script.
It is not the official text.
Its terms, its attribution wording, the conditions of the grant and its unofficial status are recorded in `../../SOURCE-LICENSE.md`, the subject-level licence note written when the text was deposited.
That note is not repeated here.

What this encoding adds to it:

- Every quotation is a line copied out of `../../registers/source-bundle/IA1965.txt` by script (`qx.py` and `gen-defs.py`), carrying its line number, so that the grant's accuracy condition can be checked by a reader who holds the text beside the code.
  `srcrefs.py` re-checks each quotation against the text.
- Nothing in this folder claims to be verified against the official text, and nothing conveys that the Attorney-General's Chambers or Singapore Statutes Online endorses this work.
- The encoding itself (the code, the tests, the notes) is Apache-2.0 like the rest of canon; that does not widen the terms of the quoted text.
