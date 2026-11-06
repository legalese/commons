# SEAMS-FOUND (ea3)

Seams that ea3 takes as INPUTS from other parts (PLAN.md section 4 rows S9 to S13 and S15), and the seams ea3 found that PLAN.md does not list.
Each row gives the asking section, the answering section, the input name and the type used.
Where ea3 asks, it never answers `FALSE` for a `NOTHING` input: the asking rule answers `NOTHING` where its answer depends on one.

## Asked, as PLAN.md names them

| PLAN row | asking section (ea3) | answering section (part) | input name | type |
| --- | --- | --- | --- | --- |
| S9 | s 126A(a), s 126B(1)(a) (`ea3-penalties.l4`) | s 95(1) (ea2) | `the answer of s 95(1)` | MAYBE BOOLEAN, "the employer failed to comply" |
| S10 | s 126A(a), s 126B(1)(a) | s 95A(2) (ea2) | `the answer of s 95A(2)` | MAYBE BOOLEAN, the same meaning |
| S11 | s 126A(a), s 126B(1)(a) | s 96(1) (ea2) | `the answer of s 96(1)` | MAYBE BOOLEAN, the same meaning |
| S12 | s 126A(aa), s 126B(1)(aa) | s 96A (ea2) with S 200/2019 | `the answer of s 96A` | MAYBE BOOLEAN, "the employer failed to comply with a requirement in the notification" |
| S13 | s 116(3) (`ea3-claims.l4`) | s 65 (ea1) | `the answer of s 65 the principal is liable to pay the salary` | MAYBE BOOLEAN |
| S15 | s 124(2) (`ea3-claims.l4`), a second asker of the row | s 112 (ea2) | `the answer of s 112 first conviction` and `the answer of s 112 subsequent conviction` | each MAYBE `Penalty on conviction`; the caller also passes a BOOLEAN `this is a subsequent conviction` and the function picks one |

PLAN.md lists S15 for s 48 (ea1); s 124(2) (lines 4956-4958) is another section that states an offence and no penalty of its own, so it takes the same two inputs.

## Found, not in PLAN.md

| # | asking section (ea3) | answering section (part) | input name | type | why |
| --- | --- | --- | --- | --- | --- |
| F-S1 | s 116(3), lines 4720-4726: "the balance of the salary up to the amount for which that other person is liable under that section" | s 65 (ea1) | `the amount for which the other person is liable under section 65` | MAYBE NUMBER | S13 carries only whether the person is liable as a principal; the sum is a second answer of s 65. ea3 caps the balance at it, and answers `NOTHING` when it is not given. |
| F-S2 | s 115(4), lines 4691-4692: "'employer' includes the transferor and the transferee of an undertaking or part thereof referred to in section 18A" | s 2(1) "employer" (keel) | `the answer of s 2(1) "employer"` | MAYBE BOOLEAN | The definition of employer in the keel answers for a person who is neither; ea3 passes it through. |
| F-S3 | s 128, line 5255: "every place of employment" | s 2(1) "place of employment" (keel) | `the answer of s 2(1) "place of employment"` | MAYBE BOOLEAN | The same. |
| F-S4 | s 125(1), lines 4967-4974: proceedings "arising from" an inquiry under s 124 | s 124 (ea3, same module) | `the answer of s 125(1) the Commissioner may institute proceedings` | MAYBE BOOLEAN | Internal to ea3: the s 125(1) duty to institute for the employee takes the s 125(1) power. |

## Borrowed from another Act, as plain inputs (not seams between the parts)

These are facts or terms of Acts the Commons does not hold, or holds in no staged module, asked as BOOLEAN inputs with the section named:
the Employment Claims Act 2016 s 2(1) "approved mediator" and the Industrial Relations Act 1960 "conciliation officer" (s 115(2A)); Part 3 of the Industrial Relations Act 1960 recognition (s 120); the Evidence Act 1893 (s 119(2)(a)); the Penal Code 1871 "public servant" (s 127); the Liquor Control (Supply and Consumption) Act 2015 s 14(1) (s 128).
