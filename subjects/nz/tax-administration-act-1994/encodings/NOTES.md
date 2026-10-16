# NOTES: the Tax Administration Act 1994 (New Zealand), PAYE reporting, filing and penalties, row `legalese-aswathy`

**Draft. No New Zealand lawyer or tax adviser has reviewed this encoding against the Act.**

## What is encoded

The computable rules of the Tax Administration Act 1994 (version as at 4 September 2026, from the text converted from the PCO XML) on reporting PAYE income, filing returns and penalties. They sit under one top-level goal, `the administration position for` (`taa-goal.l4`). For a taxpayer and a tax year it answers: whether they must file, the due date and the latest date to which a tax agent's extension may run, the late filing penalty, the late payment penalty accrued by a date, the shortfall penalty, and the last day the Commissioner may increase the assessment. Four goals sit under it:

1. **Employment income information and tax codes** (`taa-reporting.l4`, with `taa-dates.l4`): ss 23D-23H, 23M, 24E, and the Income Tax Act working day.
2. **Returns and the time bar** (`taa-returns.l4`): ss 33(1), 37(1), (4)-(5), 108(1)-(2).
3. **Late filing and late payment** (`taa-penalties.l4`): ss 139A, 139B.
4. **Shortfall penalties** (`taa-penalties.l4`): ss 141A-141E, 141FB, 141G-141K, 141JAA.

Modules: `taa-types.l4` (nouns only), `taa-dates.l4`, `taa-reporting.l4`, `taa-returns.l4`, `taa-penalties.l4`, `taa-goal.l4`; tests in `taa-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** The rest of the Act: information-gathering, disputes and challenges (Parts 4-8A), use of money interest (Part 7, whose rates are set by regulation), provisional tax instalments, GST returns and the GST late filing penalty (s 139AAA), the non-electronic filing penalty (s 139AA), employer withholding penalties (s 141ED), promoter penalties, offences, remission (Part 10), and the schedules. Whether the Commissioner has notified a penalty, the taxpayer's culpability, disclosures and history, and the default dates of tax are inputs.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 23D | employer groups | encoded |
| s 23E | online group: 2 working days | encoded |
| s 23F | non-electronic group: $50,000, 10 working days, twice-monthly payday | encoded (an Order in Council threshold is not) |
| s 23G | exemptions | encoded as an input |
| s 23H | new group | encoded |
| ss 23I-23L, 23N-23Q | other employment income information rules | out of scope |
| s 23M | ceasing to employ: 30 working days | encoded |
| s 24E | non-notified tax codes | encoded |
| ss 24B-24D, 24F-24P | other tax code and schedular rules | out of scope |
| s 33(1) | who must file | encoded |
| s 37(1) | due dates | encoded |
| s 37(3)-(5) | extensions | encoded: the latest date in (5); the Commissioner's discretion is not |
| s 108(1)-(2) | time bar | encoded |
| s 139A(2)-(4) | late filing penalty | encoded |
| s 139A(5)-(9) | notice and monthly cap for employment income information | not encoded (the notice is an input) |
| s 139B(1)-(4), (7) | late payment penalty | encoded (partial payments are not) |
| s 139BA | financial relief | out of scope |
| ss 141A-141E | shortfall penalty rates | encoded (the culpability is an input); s 141B(1D)'s threshold added after the independent pass |
| s 141FB | previous behaviour | encoded (no disqualifying offence or penalty is an input) |
| ss 141G-141J | disclosure and temporary shortfall reductions | encoded |
| s 141JAA | $50,000 cap | encoded |
| s 141K | obstruction | encoded |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 24E(1)(a) | A non-notified code when the employee "has not notified ... their name; and ... tax file number; and ... tax code" | When any one of the three is missing | A code cannot be applied without all three |
| F2 | s 37(5)(b) | "Between 30 September and the next succeeding 31 March", "between 31 March and the next succeeding 1 October" | Exclusive of the named days: October to March, and April to September | The two ranges then meet without overlap |
| F3 | s 139B(4) | When do the "successive monthly intervals" start? | From the day after the default date, when the 1% is added | That is the first day the tax is overdue |
| F4 | s 139B(3)-(4) | Does a payment on the day a penalty is added avoid it? | Not the 1% or a monthly penalty (added at the start of the day); yes the 4%, added "at the end of the sixth day" | The words of s 139B(3)(b); decided by the encoder before commit |
| F5 | ss 141G-141J | How do the disclosure and temporary shortfall reductions combine? | The larger of s 141G and s 141H on the permanent part; s 141J (or s 141I) on the temporary part | The Act does not say they stack |
| F6 | ss 141FB, 141K, 141JAA | In what order do the 50%, the 25% increase and the cap apply? | Disclosure reductions, then s 141FB, then s 141K, then the cap | s 141FB halves "the amount that would be payable"; s 141JAA applies "despite section 141J" |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `taa-tests.l4` (encoder) | 0 | 97 | 0 |
| `tests-independent.l4` | 0 | 157 | 0 |
| the 6 rule modules | 0 | 0 | 0 |
| **total** | 0 | 254 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found one gap, causing 2 failures, now fixed: s 141B(1D) penalises an unacceptable tax position only for income tax shortfalls above both $50,000 and 1% of the total tax figure. **The encoder's test that encoded the old reading was changed** and marked. Before commit, the encoder also changed the 4% timing (F4) and corrected two of its own threshold inputs that had been miscalculated by hand.

**Known limits.** No input for an unacceptable interpretation of a tax law (ss 141G, 141J); the early balance date relies on the caller's tax year; the top-level goal's late filing test uses the s 37(1) due date, ignoring any extension; partial payments of unpaid tax are not modelled.

## Open questions for a New Zealand tax adviser

1. F1: does s 24E(1)(a) give a non-notified code when any one of name, tax file number and tax code is missing?
2. F3: from which day do the s 139B(4) monthly intervals run?
3. F5 and F6: how do the s 141G, 141H, 141I and 141J reductions combine, and in what order do s 141FB and s 141K apply?
