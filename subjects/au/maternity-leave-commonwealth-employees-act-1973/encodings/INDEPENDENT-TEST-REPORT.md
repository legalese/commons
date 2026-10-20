# Independent test report: Maternity Leave (Commonwealth Employees) Act 1973 (`ml-rules.l4`)

## Method

I wrote scenarios 1-18 to `independent-expectations.md` from BRIEF.md and `../registers/source-bundle/C2004A00024.txt` alone, before opening any L4. I then read `ml-rules.l4` for names and shapes only (not `ml-tests.l4` or NOTES.md) and wrote `tests-independent.l4`.

Scenario 19 (the s 7(2)(b) "before the date" edge) came from the source while I was writing tests. In it I fixed one arithmetic slip of my own: the compulsory period ends 6 weeks from the *confinement* (21 Jul 2024), which I had first written as 22 Jul. That correction follows s 6(1)(b)(i); it was not made to match the code.

## Scenarios

There are 19 scenarios (see `independent-expectations.md`). They cover:
- s 6(1)(b)(i) and (ii) on both sides of, and exactly at, EDB - 42;
- the s 3 20-week confinement edge (on the boundary and one day earlier);
- a late birth, and no confinement yet;
- all three branches of s 7(2), plus the "before the date" edge;
- s 7(3) resumption before and after the end of the period;
- s 6(4) service day before, at and after the paid window;
- s 6(4C), s 6(4F), and s 5 not applying.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has **46 satisfied, 4 failed**, and no other errors. ml-tests.l4: 16 satisfied, 0 failed.

## Disagreements

### D1: line 52 (scenario 7). A pregnancy that ended more than 20 weeks before the EDB still yields a compulsory absence

EDB 1 Jul 2024, pregnancy ended 11 Feb 2024 (EDB - 141). I expect `the compulsory absence starts on` = NOTHING. The encoding returns a start date (`the start for`, ml-rules.l4 lines 58-65, does not check `there was a confinement`). Its end, leave limit and pay are NOTHING (those assertions passed), so the output is an orphan start with no end.

Source: s 3, "confinement ... means the birth ... or other termination of the pregnancy, that occurs not earlier than twenty weeks before the expected date of birth". s 6(2): where the pregnancy ends "other than by way of a confinement ... she shall not, after that termination, be granted permission to be absent from duty in accordance with this section". The s 6(1)(b) duty is tied to her still being pregnant 6 weeks before the EDB, or to a confinement, and neither exists here.

Confidence: high that there is no s 6 absence after the termination. The impact is small (a dangling start date).

### D2: line 70 (scenario 11). Pay after resuming early under s 7(3) runs past the day she resumed

Confined 1 Jul 2024, permitted to resume 1 Aug 2024. The compulsory absence ends 31 Jul (the encoding agrees, line 69 passes). I expect the last paid day to be 31 Jul. The encoding pays through 11 Aug 2024: `the paid end for` (line 116) is always start + 83 and ignores the resumption.

Source: s 6(3)(b) pays "in any other case [absence not exceeding 12 weeks] — for the whole of that absence". s 7(3) says the period "terminates immediately before that date". After resuming she is not absent, so s 6(3) pays nothing for 1-11 Aug.

Confidence: medium-high. It assumes a s 7(3) resumption ends her absence; the inputs cannot express further leave taken after resuming.

### D3: line 86 (scenario 16). Under s 6(4C) the encoding still allows 52 weeks of leave

Unauthorised absence just before, with no extenuating circumstances. I expect the leave to last only through the compulsory period (11 Aug 2024). The encoding gives 18 May 2025 (`the leave limit for`, lines 93-98, ignores s 6(4C)).

Source: s 6(4C)(a), "the other provisions of this Act do not apply to her in connection with her expected confinement, or with her confinement". That excludes the s 6(1)(a) and (c) permissions. Under (4C)(b) she "shall absent herself from duty during that first-mentioned period", the compulsory period, without pay. The pay side is right (line 85 passes).

Confidence: medium-high.

### D4: line 96 (scenario 19). Confinement *on* the s 7(1) date

Permission to continue duty until 10 Jun 2024, confined on 10 Jun 2024. Read literally, s 7(2)(b) applies only if "she is confined **before** the date so specified". Otherwise (c) applies and the period starts "on the day next following the date so specified", 11 Jun. The encoding starts the period on 10 Jun: line 62 compares `conf LESS THAN usual`, where usual = date + 1, which is the same as conf on or before the date.

Confidence: low-medium. The literal text supports 11 Jun. A purposive reading (she can't be on duty the day she gives birth) supports the encoding. Raised for a lawyer to decide.

## Coverage gaps and observations

- s 6(4F) leave limit: (4F)(a) bars permission under s 6(1) only "while she is absent from duty in accordance with that grant". The relevant period's end date is not an input, so I asserted only the pay bar (passes), not the leave limit.
- The s 7(1)(a) timing condition (certificate furnished at least 6 weeks before the EDB) is not checked; the permission date is taken as given. Not tested.
- s 6(4) is modelled as a clip (paid window [max(start, Q), start + 83]), which agrees with my reading. Scenarios 13-15 pass.
- When no confinement has happened yet, the end and pay outputs are NOTHING. That is reasonable, and only the start and leave limit were asserted.
- Paid days assume she is absent at least 12 weeks; actual length of absence is not an input, apart from s 7(3).

## Change after the pass (encoder)

- All four disagreements were accepted: no compulsory absence after an early end of pregnancy; pay stops on early resumption; no 52-week leave after an unexcused unauthorised absence; confinement on the permitted date starts the absence the next day.
- The gaps are recorded as known limits in NOTES.md.
