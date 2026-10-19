# Papua New Guinea (Members of the Forces Benefits) Act 1957 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `the forces position for` (`pngf-rules.l4`), answering the question below. The scope is set out in BRIEF.md.

## Seat

The encoding is written from the seat of **the member of the Forces, or a dependant**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Am I a member of the Forces under this Act; is the Commonwealth liable for my incapacity (or the member's death); what benefits am I eligible for; and can my pension be taken?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | encoded: member of the Forces, the war |
| s 4 | encoded |
| s 5 | encoded: liability (rates are in the regulations, not computed) |
| s 6 | noted: other benefits are prescribed |
| s 7 | out of scope |
| s 8 | encoded |
| ss 8A-9 | out of scope |

## Forks (readings taken)

- **F1, s 3, "the war" (changed after the independent pass).** Service must have begun before 3 September 1945; service begun before 3 September 1939 counts if it continued into the war. There is no end date input, so service that ended before the war began is not distinguished. The Act gives no end date for "the war"; 3 September 1945 only limits which other wars count.
- **Expected failure.** `tests-independent.l4` line 31 expects service beginning on 2 September 1939 not to count, following the brief's original start-date reading. That contradicts the tester's own scenario 22 (enlisted before the war, served into it), which the code now follows. Without an end date both cannot hold, so line 31 is left failing.
- **Known limits (from the independent pass).** Sex, indigeneity and the island test are one input. The s 4 and s 8 outputs follow membership, though s 8 has no membership condition.
- **F2, s 5(1)-(3).** Liability needs any one of the connections to service, and none of the three exclusions.
- **F3.** Rates and amounts are fixed by the regulations, which are not in the deposited text.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 33 assertions satisfied, 1 failed, 0 other errors — 10 the encoder's (`pngf-tests.l4`), 24 independent (`tests-independent.l4`). One assertion in `tests-independent.l4` (line 31) is expected to fail; see the expected-failure note above.

## Open questions for an Australian lawyer

- None of substance.
