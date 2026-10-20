# Independent expectations: War Gratuity Act 1945

Written from BRIEF.md and the source text only, before reading any L4.

## Reading

- Month = 30 days (s 2), and any fraction counts as a whole month (s 12). Overseas months = ceil(O/30).
- s 8: if there is overseas qualifying service and the months are fewer than 12, they are deemed to be 12. That does not apply where the member returned at their own request, for prescribed disciplinary reasons, or on account of an excepted injury or illness.
- s 12(2): general months = ceil(G/30) minus the overseas months (G includes the overseas days, s 9(1)(a)). A negative result is taken as 0, since there cannot be a negative number of months (moderate confidence: the text does not say).
- s 4: $7.50 per overseas month and $1.50 per general month.
- s 13: death due to war service during s 7 (overseas) service adds 7 x $7.50 = $52.50. Death during other general qualifying service adds 7 x $1.50 = $10.50.
- s 14(1): death due to war service before 1 July 1947 with a totally dependent person sets a floor of 36 x $7.50 = $270, which includes the s 13 addition.
- s 15: a member in a disqualified class gets nothing (subject to the prescribed authority's discretion, which is not modelled).
- s 16: debts are deducted from the amount credited. The result is floored at 0.
- s 6: the gratuity may always be withheld or deferred by a prescribed authority.

## Scenarios

| # | Overseas days | General days | Other facts | Overseas months | General months | Amount | Licence |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | none | 0 | 0 | 0.00 | s 12 |
| 2 | 0 | 30 | none | 0 | 1 | 1.50 | s 2 month, s 4(2), s 12(2) |
| 3 | 0 | 31 | none | 0 | 2 | 3.00 | s 12 fraction is a whole month |
| 4 | 90 | 400 | none | 12 (from 3) | 2 | 93.00 | s 8, s 12 |
| 5 | 90 | 400 | returned at own request | 3 | 11 | 39.00 | s 8 exception |
| 6 | 90 | 400 | returned for disciplinary reasons | 3 | 11 | 39.00 | s 8 |
| 7 | 90 | 400 | returned for excepted injury | 3 | 11 | 39.00 | s 8 |
| 8 | 330 | 500 | none | 12 (from 11) | 5 | 97.50 | s 8 |
| 9 | 360 | 500 | none | 12 | 5 | 97.50 | s 12 |
| 10 | 361 | 500 | none | 13 | 4 | 103.50 | s 12 |
| 11 | 360 | 500 | died of war service while overseas | 12 | 5 | 150.00 | s 13(1) |
| 12 | 0 | 300 | died of war service in general service | 0 | 10 | 25.50 | s 13(2) |
| 13 | 0 | 300 | as 12, plus total dependency, death before 1 Jul 1947 | 0 | 10 | 270.00 | s 14(1) floor |
| 14 | 1500 | 1800 | died overseas, total dependency | 50 | 10 | 442.50 (above floor) | s 13(1), 14(1) |
| 15 | 0 | 0 | died of war service, no general service, total dependency | 0 | 0 | 270.00 | s 14(1) "whether or not ... any general qualifying service" |
| 16 | 90 | 400 | disqualified class | - | - | 0.00 | s 15 |
| 17 | 90 | 400 | debts $20 | 12 | 2 | 73.00 | s 16 |
| 18 | 90 | 400 | debts $200 | 12 | 2 | 0.00 | s 16 (floored) |
| 19 | 30 | 60 | none | 12 | 0 (2 - 12, floored) | 90.00 | s 8, s 12(2) |

In every case the gratuity may be withheld or deferred (s 6).
