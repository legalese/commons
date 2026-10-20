# Encoding brief: the Trusts (Hague Convention) Act 1991 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Trusts (Hague Convention) Act 1991** (No. 50, 1991), Commonwealth of Australia, compilation No. 1 of 1 July 2016, with the Convention on the law applicable to trusts and on their recognition in its Schedule, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A04125.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the settlor, trustee or beneficiary of a trust** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Does the Hague Trusts Convention apply to my trust? Which law governs it? Must it be recognised as a trust?"*

In scope: ss 6-7 and Articles 2, 3, 5, 6, 7, 11 (first sentence), 13 and 18 of the Convention. Out of scope: ss 1-5; Articles 1, 4, 8-10 (what the governing law governs; severable aspects), 11(a)-(d) and 12 (the effects of recognition), 14-17, 19-32 (other rules of law, mandatory rules, reservations and final clauses).

## Inputs

- The Article 2 characteristics: assets under a trustee's control for a beneficiary or a purpose; a separate fund; title in the trustee's name (or another's on the trustee's behalf); the trustee's power and accountable duty to manage.
- Whether the trust was created voluntarily and is evidenced in writing (Article 3).
- Whether the conflict is solely between laws of Australian States or Territories (s 7(1)).
- Whether the settlor chose a law, expressly or by implication; whether the chosen law, and the most closely connected law, provide for trusts of this category (the closest connection itself is a finding).
- Whether the trust was created in accordance with the governing law; whether its significant elements are more closely connected with States without trusts (Article 13); whether applying the Convention would be manifestly incompatible with public policy (Article 18).

## Rules that matter

- Where the Convention leaves the answer to the forum (Article 13), the answer is NOTHING.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`th-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
