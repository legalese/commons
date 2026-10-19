# Independent expectations: Maintenance Orders (Commonwealth Officers) Act 1966

Written from BRIEF.md and the Act only, before reading any .l4 file.

## Scenarios

| # | Facts | Expected | Working / words of the Act |
|---|---|---|---|
| 1 | State law provides for enforcing maintenance orders by attachment of earnings orders; officer paid by the Commonwealth | pay attachable = YES | s 6(1) the provisions apply "as if a reference ... to an employer included a reference to the Commonwealth and to every Commonwealth authority" |
| 2 | State law makes no such provision | attachable = NO | s 5 "Except as provided by this Act, moneys payable by the Commonwealth ... are not subject to attachment"; s 6(1) not triggered |
| 3 | As 1, and another law (e.g. a pay-protection law) would otherwise prevent attachment | attachable = YES | s 6(3) "notwithstanding any law that, but for this Act, would prevent the attachment" |
| 4 | One order: earnings 1000, order requires 300 | paid 300; 700 left to officer | s 6(1) |
| 5 | Earnings 1000; order A in force 1 Jan 2020 requires 300; order B in force 1 Jan 2021 requires 500 | A 300, B 500, left 200 | s 7(1)(a) by date; (b) B from residue 700 |
| 6 | As 5 but B requires 900 | A 300, B 700, left 0 | s 7(1)(b): B applies as if the earnings were the residue (700) |
| 7 | As 5 but supplied with B listed first | A 300, B 500 (same as 5) | s 7(1)(a) "according to the respective dates on which they came into force" - list order irrelevant |
| 8 | Earnings 200; A (2020) requires 300; B (2021) requires 500 | A 200, B 0, left 0 | s 7(1)(a) "disregard any order until an earlier order has been complied with"; residue 0 |
| 9 | Earnings 1000; A in force 1 Jan 2019, varied in 2022, as varied requires 600; B in force 1 Jan 2021 requires 500 | A first: A 600, B 400 | s 7(3): the varied order "deemed to have come into force as so varied on the day upon which the order came into force" (2019), so it still precedes B |
| 10 | Three orders: earnings 1000; C 2018 requires 100, A 2020 requires 300, B 2021 requires 800 | C 100, A 300, B 600, left 0 | s 7(1) chain of residues |
| 11 | Two orders but no State law provision (scenario 2) | nothing paid under any order | s 5 |
| 12 | Total paid never exceeds earnings | invariant | s 7(1)(b) |

## Where I read the Act differently from the brief / gaps

- s 7(1) applies only where two or more orders are "directed to the Commonwealth ... by virtue of this Act in respect of maintenance orders against the one person". The brief's input list has no person identifier, so I assume all orders are against the one person.
- The Act does not say what to do with two orders that came into force on the same day; I do not test that.
- s 7(2) (Matrimonial Causes Act Third Schedule orders taking priority) is out of the brief's scope; not tested.
- Whether the State law's own protected-earnings rules cap the amount is a matter of State law; the expected amounts take each order's "amount it requires on that occasion" as given (brief's inputs).
