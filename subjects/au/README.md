# commonwealth-of-australia/

Commonwealth of Australia Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

All 1,261 principal Commonwealth Acts in force are indexed here and their text is deposited (sourced), from the Federal Register of Legislation's API on 13 October 2026; 24 of them were first laid out on 2026-09-22 for twelve everyday topics. Each Act's text is the current compilation converted to plain text (from Word, or from EPUB for older compilations) in `registers/source-bundle/<id>.txt`, with the version, source URL and hashes in the `.meta.json`; 26 Acts whose newest amendments are not yet compiled say so in a `text_caveat`. The state and territory folders (`wa/`, `nsw/` and the rest) hold their own Acts.

The requirement ledger for Commonwealth law is [`requirements.jsonl`](requirements.jsonl), opened on 13 October 2026, empty until scenarios raise entries. It follows [`docs/ledger/LEDGER.md`](../../docs/ledger/LEDGER.md). Questions that Western Australian lives raise but Commonwealth law answers belong here; the state folders (`wa/`, `nsw/` and the rest) keep their own ledgers. Check it with `python docs/ledger/check-ledger.py subjects/au/requirements.jsonl`.
