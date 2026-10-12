# western-australia/

Reserved for L4 encodings of Western Australian law — one subject-id per body of law
(Act, regulation, or contract form), following the subject-sidecar shape described in
[`subjects/README.md`](../README.md). 813 Acts are indexed here and their text is deposited (sourced); a few are encoded, most from legislative quality assurance work.

The requirement ledger for Western Australia is [`requirements.jsonl`](requirements.jsonl), opened on 13 October 2026 and empty until the WA scenarios raise entries. It follows [`docs/ledger/LEDGER.md`](../../../docs/ledger/LEDGER.md); entries may name Commonwealth Acts by their path from `subjects/` (for example `au/fair-work-act-2009`). Check it with `python docs/ledger/check-ledger.py subjects/au/wa/requirements.jsonl`.
