# Independent test report: War Gratuity Act 1945

Expectations were written in `independent-expectations.md` from BRIEF.md and the source text before reading any L4. Then I read `wg-rules.l4` for names and input shapes only and wrote `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 0 errors, **18 satisfied, 0 failed**. The encoder's own wg-tests.l4 gives 14 satisfied.

## Scenarios

The 30-day month edges are 30 general days = 1 month ($1.50) and 31 days = 2 months ($3.00) (s 2, s 12). On the s 8 deeming to 12 months, 90 overseas days count as 12 months ($93 with 400 general days). Return at the member's own request, for discipline or for an excepted injury takes the case out of s 8 (3 months plus 11, $39). On the 12-month edge, 330, 360 and 361 overseas days give $97.50, $97.50 and $103.50. Under s 13, death while overseas adds $52.50 and death in general service adds $10.50. The s 14 floor of $270 applies (including with no general service at all), and a gratuity already above the floor stays where it is ($442.50). A disqualified class gets $0 (s 15). Debts of $20 are deducted, and debts above the gratuity give $0 (s 16). The s 12(2) subtraction is floored at nil when the 12 deemed overseas months exceed the general months (30 overseas days and 60 general days give $90). In every case the gratuity may be withheld or deferred (s 6).

## Disagreements

None.

## Coverage gaps

- s 8's three exceptions (own request, discipline, excepted injury) are one boolean, so scenarios 6 and 7 cannot be told apart from scenario 5.
- s 14's "totally dependent" and "died before 1 July 1947" are one boolean, so the 1 July 1947 date edge cannot be tested.
- The order of the s 14 floor and the s 16 deductions (floor first, then deduct) was not asserted with a combined case.
- The s 15 provisos (a prescribed authority may still credit some or all of it) and the s 6 discretion appear only as a constant TRUE flag and a hard 0.
- The negative-general-months floor (scenario 19) is my reading, not text. The encoding agrees.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
