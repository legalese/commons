# new-zealand/

New Zealand Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

All 986 principal public Acts in force are indexed here and their text is deposited (sourced), from the Parliamentary Counsel Office's New Zealand Legislation Data API on 13 October 2026; 22 of them were first laid out on 2026-09-22 for twelve everyday topics. Each Act's text is converted from the PCO XML into `registers/source-bundle/<work_id>.txt`, with the version, source URL and hashes in the `.meta.json`; the XML itself is kept on disk but not in git. There is no copyright in New Zealand legislation (Copyright Act 1994 s 27). A few Acts are encoded (the Accident Compensation Act among them); the rest wait for New Zealand scenarios.

The requirement ledger for New Zealand law is [`requirements.jsonl`](requirements.jsonl), opened on 13 October 2026, empty until scenarios raise entries. It follows [`docs/ledger/LEDGER.md`](../../docs/ledger/LEDGER.md). Check it with `python docs/ledger/check-ledger.py subjects/nz/requirements.jsonl`.
