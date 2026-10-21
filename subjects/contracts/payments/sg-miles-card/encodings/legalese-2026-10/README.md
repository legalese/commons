# sg-miles-card — encoding row `legalese-2026-10`

Which card earns the most on this purchase: twelve Singapore card programmes, one module per issuer document set, a shared ontology, and a composer that asks all twelve at once.
Status `draft`; no person has reviewed it (`encoding.json`).

- `NOTES.md`: what the row is, what is held, what was checked, what was not done, and every choice marked assumed, not ruled. Read it first.
- `registers/`: `source-bundle.json` (28 documents by URL and sha256), `fork-register.json` (27 forks), `external-modifications.json`.
- `source/fetch.sh`: fetches the 28 documents from their publishers and refuses any digest mismatch. No document is copied into this repository.
- `check.sh`: `L4=<path to l4> L4_TARGET=unstable ./check.sh`.
- `cards.l4`: the composer. Everything else is one issuer document set per file.

The earlier row, `../legalese`, is unchanged.
