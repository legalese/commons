# Territories Stolen Generations Redress Scheme (Facilitation) Act 2021 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `the answer for` (`tsgr-rules.l4`). For a question about a redress payment asked under a given law, it answers whether the payment:

- affects benefits;
- is compensation;
- counts as an asset;
- can be taken.

The operative s 4 is encoded. The source is the Act as made (No. 126, 2021), which commenced on 1 March 2022.

## Seat

The encoding is written from the seat of **the survivor who receives a redress payment**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Does my redress payment affect my Commonwealth pension or benefits; is it counted as compensation; is it counted in an assets test; and can anyone take it from me?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope: machinery and the definition |
| s 4 | encoded |
| ss 5-6 | out of scope (the regulations' prescriptions are inputs) |

## Forks (readings taken)

- **F1, s 4(1).** The protection of eligibility covers only Commonwealth laws. For a State or Territory law the Act does not answer, and the answer is NOTHING.
- **F2, s 4(2).** "Not compensation or damages" covers the Commonwealth laws and prescribed State or Territory laws. For other State or Territory laws the answer is NOTHING.
- **F3, s 4(3) (changed after the independent pass).** Subsections (1)-(2) do not apply to the value of assets. Whether the payment then counts is for the law asking, so the answer is NOTHING.
- **Known limits (from the independent pass).**
  - The s 4(6) exclusion is one input and cannot say which of (1)-(3) it excludes.
  - The Social Security Act and the Veterans' Entitlements Act are one value.
  - Prescription under s 4(2)(c) and s 4(3)(c) is one value.
  - Commencement and ss 5-6 are not modelled.
- **F4, s 4(5)-(6).** A Commonwealth law that expressly provides otherwise displaces all of (1)-(4). Regulations under (6) can exclude a Commonwealth law from (1)-(3) only, not from (4). Where the protection is displaced, the answer is NOTHING: the other law governs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 35 assertions satisfied, 0 failed, 0 other errors — 11 the encoder's (`tsgr-tests.l4`), 24 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F4:** does s 4(5)'s "unless ... the law expressly provides otherwise" reach inalienability (s 4(4))?
