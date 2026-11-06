# SEAMS-FOUND (ea1)

Seams that PLAN.md section 4 does not list, found while encoding ea1's range (ss 8-66).
Format: asking section, answering section, the input name and the type used.
Where a table seam is asked by ea1, that is also listed (so the lead can wire it): the rows marked "table".

## Asked by ea1 (inputs named `the answer of <label>`)

| asking section (ea1) | answering section | input name and type | seam |
| --- | --- | --- | --- |
| s 27(3)(b)(i) (`ea1-part3b-deductions`) | s 88A (ea2) | `the answer of s 88A the days of paid annual leave`: MAYBE NUMBER | S4 (table) |
| s 11(1) (`ea1-part2a-termination`) | s 107A and the Third Schedule (ea2, ea3) | `the answer of sch 3 gross rate of pay per day`: MAYBE NUMBER | S6 (table) |
| s 28(2) (`ea1-part3b-deductions`) | the same | `the answer of sch 3 gross rate of pay per day`: MAYBE NUMBER | S6 (table) |
| s 37(2), s 37(3) (`ea1-part4a-rest-hours`) | the same | `the answer of sch 3 basic rate of pay per day`: MAYBE NUMBER | S6 (table) |
| s 37(3A)(b), s 37(2), s 37(3), s 38(4), s 38(6), s 40(4) (`ea1-part4a-rest-hours`) | Fourth Schedule (ea3) | `the answer of sch 4 hourly basic rate of pay`: MAYBE NUMBER | S7 (table) |
| s 19 (`ea1-part2b-continuity`) | s 112 (ea2) | `the answer of s 112 first conviction` and `the answer of s 112 subsequent conviction`: each MAYBE `Penalty on conviction` | S15 (table lists only s 48) |
| s 34(1), for a failure that is not a contravention of s 21, 22 or 23 (`ea1-part3b-deductions`) | s 112 (ea2) | the same two inputs | S15, not in the table |
| s 48(4) (`ea1-part4b-benefits`) | s 112 (ea2) | the same two inputs | S15 (table) |
| s 66(7) (`ea1-part6-contractors`) | s 112 (ea2) | the same two inputs | S15, not in the table |

Sections 34(2), 53 and 61 state their own penalties and ask nothing of s 112.
The penalty types are the keel's `Penalty on conviction`.

## Found and not in the table, inside ea1's own range (no wiring across parts)

These are inputs that carry one ea1 function's answer into another; the lead needs to wire nothing, but a caller must pass them.

| asking section | answering section | input name and type |
| --- | --- | --- |
| s 14(2) (`ea1-part2a-termination`) | s 14(2A) | `the answer of s 14(2A) the employee is a relevant employee`: MAYBE BOOLEAN |
| s 47(2) sum (`ea1-part4b-benefits`) | s 47(2) deemed provision | `the answer of s 47(2) the provision is deemed`: MAYBE BOOLEAN |
| s 63(2) (`ea1-part5-truck`) | s 57 | `the answer of s 57 the amount of salary the workman is entitled to recover`: MAYBE NUMBER |

## Facts from outside the sources (plain inputs, not seams between parts)

- The Minister's substitutes: the proportion in ss 29(1), 30(2), 31(3) and 31(5) (MAYBE NUMBER, named `the proportion the Minister has prescribed in substitution`), the percentage in s 32(1) (`the percentage the Minister has prescribed in substitution`), and the ceilings of ss 33(1)(a), 33(1)(b) and 35 (`the amount the Minister has prescribed in substitution for $4,500` and `... for $2,600`); each MAYBE NUMBER, `NOTHING` meaning none made.
- Other Acts' answers, each a plain input named after the other source: the Employment Claims Act 2016 (s 14(2): `section 3 of the Employment Claims Act 2016 leaves the claim open`, MAYBE BOOLEAN; s 65(2): `the workman has submitted to the Commissioner, under section 3(1) of the Employment Claims Act 2016, a mediation request ...`, BOOLEAN); the Companies Act 1967 (s 47(5): `the Companies Act 1967 section 4(1) says the body is a company`, MAYBE BOOLEAN); the Variable Capital Companies Act (s 47(5): `the VCC Act section 2(1) says the body is a sub-fund, an umbrella VCC or a VCC`, MAYBE BOOLEAN); the Variable Capital Companies (Miscellaneous Amendments) Act 2019 (s 47(5) "operative date": `the date of commencement of sections 29, 48 and 62 of the Variable Capital Companies (Miscellaneous Amendments) Act 2019`, MAYBE DATE); the MediShield Life Scheme Act 2015 and the CareShield Life and Long-Term Care Act 2019 (s 26(2): `... section 2(1) says the body is a recovery body`, MAYBE BOOLEAN each).
- The public holidays: `the public holidays` LIST OF DATE in ss 21(1), 21(2), 23(2), 24(2), 65(2A) and 66(4); the Holidays Act is not among the sources.
- The Commissioner's orders and decisions (ss 38(3), 41A): plain BOOLEAN facts.
