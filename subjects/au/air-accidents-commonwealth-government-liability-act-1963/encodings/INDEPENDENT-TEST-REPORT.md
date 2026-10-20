# Independent test report: Air Accidents (Commonwealth Government Liability) Act 1963

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. `tests-independent.l4` asserts them against `aa-rules.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh .`: tests-independent.l4: 0 errors, **40 satisfied, 0 failed**.

## Scenarios covered

Part II (Commonwealth-operated): applies by default; excluded by CLA Part IV (s 6(1)), VEA pension (s 6(2)), working crew (s 4). Cap s 8(1)(a) / (b) with prescribed amount lower, higher and equal. Insurance deduction s 8(2). Cap applied before deduction (s 8(2) "recoverable but for this subsection"). s 10(1)(a) bar. s 16 and s 17 do not reach Part II.

Part III (other operator): each connection route s 11(1)(a), (b), (c), (3A)/(4); no connection; s 11(2) declared State Act; s 11(3) VEA; s 12 accident not on board or embarking; s 14(2)(a)+(b) deductions, floor at nil, cap (b) then deduct; s 15(1)(a); s 16(1)(a), (b), (c) bars; s 17 pending (not heard, but not barred); working crew of a corporation.

## Disagreements

None.

## Coverage gaps (not testable through the module's shapes)

1. **Who is liable.** s 12 names the Commonwealth *or* the Commonwealth authority that employed/paid for/arranged the carriage; s 11(3B) and (6) substitute the ACT or the NT. The module returns only "Part III" and folds ACT and NT into one `Connection` value, so it cannot say which body is liable. The brief's question "Is the Commonwealth (or the ACT or Northern Territory) liable" is answered only implicitly.
2. **s 4 passenger is a single boolean** ("on board as working crew of a commercial operator"). The two cumulative limbs (employed by a Commonwealth authority or corporation running commercial transport operations; on board to perform crew functions) are not separate inputs, so the case of an off-duty commercial pilot travelling as a passenger (still a passenger) cannot be tested separately; nor can "lawfully entitled to be on board".
3. **VEA "other than Part IV"** carve-out in ss 6(2), 11(3) is left to the user's boolean.
4. `my action can be heard now` is FALSE whenever damages are nil, so it mixes "barred/no claim" with s 17's "on hold". Not wrong, but a caller cannot tell the two apart from that field alone.
5. Out of scope per brief and untested: ss 10(1)(b), 15(1)(b) (reduction of non-Act damages), s 16(2)-(3), incorporated CLA provisions (time bar in s 34 etc.).

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
