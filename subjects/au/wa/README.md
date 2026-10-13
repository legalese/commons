# western-australia/

Reserved for L4 encodings of Western Australian law — one subject-id per body of law
(Act, regulation, or contract form), following the subject-sidecar shape described in
[`subjects/README.md`](../README.md). 813 Acts are indexed here and their text is deposited (sourced). None is encoded: on 13 October 2026 the earlier legislative quality assurance work (Cat Act, Residential Tenancies Act, Dog Act, Retail Barring Orders Bill) moved to the private solutions repository as examples, and the WA statute book starts fresh from the scenarios and the ledger.

The requirement ledger for Western Australia is [`requirements.jsonl`](requirements.jsonl), opened on 13 October 2026 and empty until the WA scenarios raise entries. It follows [`docs/ledger/LEDGER.md`](../../../docs/ledger/LEDGER.md); a question a WA life raises that Commonwealth law answers goes in the Commonwealth ledger, [`../requirements.jsonl`](../requirements.jsonl), instead; entries in either may name the other layer's Acts by path (for example `au/fair-work-act-2009`). Check it with `python docs/ledger/check-ledger.py subjects/au/wa/requirements.jsonl`.
