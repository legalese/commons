# Independent test report: Commonwealth Entities (Payment Surcharges) Act 2024

Files: `independent-expectations.md` (written from BRIEF.md and the source only), `tests-independent.l4` (against `ceps-rules.l4`).

## Counts

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 — 2 errors (both are the failed assertions), **20 satisfied, 2 failed**. (ceps-tests.l4 9/0.)

## Failures

1. **L35, scenario 3** — amount is neither limb of "payment surcharge" (s 4). Expected `this Act authorises the surcharge` = `JUST FALSE`; module gives `NOTHING`.
2. **L46, scenario 5** — base payment already a surchargeable payment under another law (s 5(1)(b) fails). Expected `JUST FALSE`; module gives `NOTHING`.

Reasoning: the question the field answers is "does *this Act* authorise the surcharge". s 5(1) authorises only "a payment surcharge" and only "if ... (b) apart from this section, the base payment is not a surchargeable payment". Where either condition fails, s 5 plainly does not authorise it; the answer to that question is no, not unknown. The module's choice of NOTHING is deliberate (its comment: "Where another law already governs the surcharge, this Act does not decide it") and is defensible as signalling "look elsewhere", but it treats a failed statutory condition differently from s 5(1)(a) and s 5(2), which return `JUST FALSE` though they are equally conditions of the same subsection. For the payer, scenario 3 is especially misleading: an amount that is not a payment surcharge is simply not authorised by this Act. Recommend `JUST FALSE` for both, or a separate field ("another law governs") if the look-elsewhere signal is wanted. The downstream refund field is correct in both cases (FALSE).

## Gaps and reading notes

- s 7(1) is a duty to "take all reasonable steps to comply", not to comply; the module's input is "followed the policies". Because s 7(2) makes validity unaffected either way, and the output is a constant FALSE, nothing turns on it — but the input is also unused, so the module cannot report whether the entity was in breach of s 7(1).
- `Kind of amount` is a single enum, so an amount meeting both limbs (a) and (b) (my scenario 9) is not expressible; harmless, either limb suffices.
- `a refund is in the entity's discretion` correctly is TRUE only for a s 5 surcharge (s 6 "under section 5") and never asserts an entitlement.
- No date edge: the module does not take the date of the charge, so a surcharge before commencement (3 Dec 2024) is not distinguished. The brief names no date input; noted as a gap.
- s 7(3)-(7) out of scope per brief.

## Change after the pass (encoder)

- **L35, L46 (not a surcharge; another law governs).** Accepted: the answer is now FALSE, consistent with the other s 5 conditions (F1). Two of the encoder's tests were updated, with a comment.
- The gaps are recorded as known limits in NOTES.md.
