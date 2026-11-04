# PROGRESS (wra4: Welfare Reform Act 2012, lines 1520-2474, ss 96-134)

Status, 4 November 2026: every deliverable is written and checked, and the whole was read by an advisor, whose point about the seat inputs (ask for facts, not legal conclusions) was applied.
Verified by `check.sh` with the stable binary 1.6.98 and the main build 1.6.108: 26 modules, 0 errors, 1117 assertions satisfied, 0 failed, 0 refused, the same counts on main (the exact output is in NOTES.md, last section).
`srcrefs.py check --refs` and `--strict` over every `wra4-*.l4`: 0 problems.
No `wra4-*.l4` file prints a `DiagnosticSeverity_Warning` or `_Error` on either binary (`l4 run`, scanned for both).

## Done

| file | content | assertions |
| --- | --- | --- |
| wra4-ss96-97.l4 | ss 96, 96A, 97 (benefit cap) | 94 |
| wra4-ss98-104.l4 | ss 98-104 (claims, payments, appeals, electronic communications) | 47 |
| wra4-s105-recovery.l4 | s 105 (SSAA 71ZB-71ZH, 115B, SSA 1998 Sch 3) | 149 |
| wra4-ss106-112.l4 | ss 106-112 (earnings, limitation, investigation, prosecution) | 71 |
| wra4-ss113-116.l4 | ss 113-116 (penalties) | 88 |
| wra4-ss117-119.l4 | ss 117-119 (SSFA 6A, 6B, 7) | 97 |
| wra4-s120-taxcredits.l4 | s 120 (TCA 36A-36D, 38, 67) | 124 |
| wra4-ss121-126.l4 | ss 121-126 (cautions, tax credit fraud, transfer of functions) | 53 |
| wra4-ss127-129.l4 | ss 127-129 (HMRC and DPP information-sharing, unlawful disclosure) | 110 |
| wra4-ss130-134.l4 | ss 130-134 (local authority information-sharing, supplementary, amendments) | 141 |
| wra4-regulative.l4 | the duties, permissions and prohibitions of ss 96A(1), 115, 127(5), 129(1) | 8 `#TRACE`s (not counted by check.sh) |
| wra4-seat.l4, wra4-cases-seat.l4 | layer 2: 49 questions in 9 groups, 143 cases | 143 |

Each layer-1 module has a `wra4-tests-<same name>.l4`.
`NOTES.md` has the coverage table (931 rows, one disposition each), the fork register (F1 to F8), the jural-relations table (115 rows, all 257 rules cited), the marginal readings (31 rows), the reading of FALSE and NOTHING, the seams, the findings, what the stable binary does not accept, the seat, and what check.sh prints.
`NEEDS-CORE.md`: the core `Authority` lacks the Northern Ireland Department, the Northern Ireland Housing Executive and the Treasury.

## Decisions taken (with the text that licenses each)

- Amending words ("is amended as follows", "for X there is substituted Y") are `inert` (reason 2); the text a section inserts into a host Act is encoded under the host Act's own number.
- "May" in the information-sharing sections is a power the text grants: `JUST TRUE` where the facts fit, `NOTHING` otherwise, because ss 127(9) and 128(5) say the sections do not limit supply apart from them.
- "Must not ... without" (127(5), 129(8)): the bar is `JUST FALSE` where it bites; with the authority or consent the answer is `NOTHING`.
- A caution is a trigger in the printed text of 6B(11A)(c) and TCA 36A(1)(c), (7)(c) and is repealed by s 121; both are encoded as printed, and s 121 has its own function that answers `JUST FALSE` for the caution ground (fork F6).
- The seat wraps a plain-`BOOLEAN` layer-1 rule in `JUST` and passes a `MAYBE` through unchanged; it never turns `NOTHING` into `FALSE`.
- Eight seat questions chain two layer-1 rules (118(7), 119(8) 7B, 127(2), 127(4), 129(5), 130(5), 131(1), 132(1)) so that the person is asked facts they can state, not a legal conclusion another rule here computes.
- Every `NOT` is parenthesised, because a bare `NOT` swallows the rest of a conjunction on the stable binary (measured).

## Not done, and why

- No `wra4-` file is added to a git index and none is committed (the brief forbids it).
- The work scripts in `runs/iaw-wra4/work/` (generators for the modules, the seat, the cases and NOTES.md) are scratch outside the deposit; the deposit holds only their output.
