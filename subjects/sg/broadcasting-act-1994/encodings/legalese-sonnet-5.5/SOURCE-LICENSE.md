# Source license

The quoted text of the Act in this folder's `.l4` files, and the tables built from it, is taken from `../../registers/source-bundle/BA1994.txt`, a plain-text rendering of the Broadcasting Act 1994 (Singapore) made by a converter script from Singapore Statutes Online.
It is not the official text.
Its terms, its attribution wording, the conditions of the grant and its unofficial status are recorded in `../../SOURCE-LICENSE.md`, the subject-level licence note written when the text was deposited.
That note is not repeated here.

The quoted text of each instrument in the `sgba-i-*.l4` files is taken from the instrument's own deposit, a subject of its own under `../../../` (`broadcasting-tvro-system-regulations-1991`, `broadcasting-composition-of-offences-regulations-2004`, `broadcasting-class-licence-notification-1996`, `broadcasting-class-licence-digital-display-panels-notification-2020`, `broadcasting-exemption-order-1996`, `broadcasting-exemption-no-2-order-2002`, `broadcasting-exemption-no-3-order-2004`, `broadcasting-exemption-order-2008`, `broadcasting-exemption-order-2022`, `broadcasting-exemption-educational-institutions-order-2010`, `broadcasting-service-of-documents-website-notification-2023`, `broadcasting-online-codes-of-practice-procedure-rules-2023`).
Each of those has its own `SOURCE-LICENSE.md`, which records that the deposit is the text the lawplain corpus served on 2026-11-03, a secondary source and not the official text, and which relies on the same Singapore Statutes Online grant.

What this encoding adds to them:

- Every quotation is a line copied out of the deposited text by script (`qx.py`), carrying its line number, so that the grant's accuracy condition can be checked by a reader who holds the text beside the code.
  `srcrefs.py` re-checks each quotation against the text.
- Nothing in this folder claims to be verified against the official text, and nothing conveys that the Attorney-General's Chambers or Singapore Statutes Online endorses this work.
- The encoding itself (the code, the tests, the notes) is Apache-2.0 like the rest of canon; that does not widen the terms of the quoted text.
