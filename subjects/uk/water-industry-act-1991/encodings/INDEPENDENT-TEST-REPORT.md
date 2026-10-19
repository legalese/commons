# Water Industry Act 1991: independent test report

The expectations in `independent-expectations.md` were written from BRIEF.md and the Act (ss 45-51, 61-63A, 106, 144-144B and Schedule 4A) before any `.l4` file was opened. `tests-independent.l4` then asserts them against `wia-connection`, `wia-disconnection`, `wia-charges` and `wia-goal`. No expected value was changed to fit the code.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 3 | 109 | 3 |
| wia-tests.l4 | 0 | 82 | 0 |
| other modules | 0 | 0 | 0 |

There are 112 independent assertions: 109 pass and 3 fail. There are no syntax or type errors; each of the 3 errors is one of the failed assertions.

## Failing assertions

### 1. Payment made after the seven days but before the cut-off (D14). Line 124.

- **Scenario.** A shop is served a payment notice on 2 Mar 2026. The occupier pays on 11 Mar, which is late, and the supply is cut off on 12 Mar.
- **Expected.** The cut-off is not lawful.
- **Code.** Lawful. `the earliest day my water can be cut off for` only asks whether payment was in time. Under the code's finding F4, a later payment does not end the power.
- **Source.** s 61(1ZA) says the subsection applies if the occupier "(a) **is liable** ... to pay charges due to the undertaker ...; and (b) has failed to do so before the end of the period of seven days ...".
- **View.** Low confidence. Paragraph (a) is in the present tense. Once the charges are paid, nothing is "due", so on the day of the cut-off (1ZA) arguably no longer applies and s 61(1) gives no power. Cutting off after payment would then be an offence under s 63(3)(a). The code reads (b) as a historical trigger that survives payment. I think the Act favours the present-tense reading. Either way, the encoding should state its choice as a fork, or REFUSE where payment came after the deadline but before the cut-off.

### 2. Counter-notice served on the same day as the payment notice (D21). Line 137.

- **Scenario.** The notice is served on 2 Mar 2026 and the counter-notice disputing liability is served on 2 Mar too.
- **Expected.** The counter-notice is not "within the period of seven days" (3 to 9 Mar), so it does not bar a cut-off on 20 Mar.
- **Code.** It bars the cut-off. The test is `k AT MOST` service + 7, with no lower bound.
- **Source.** s 61(2)(b) "within the period of seven days mentioned in that paragraph". The period in (1ZA)(b) is "seven days beginning with the day after he is served".
- **View.** Low confidence, and I lean towards the code. The literal reading excludes a counter-notice served on the day of service. A court would very probably hold that a dispute raised early still counts. Even so, the code has no lower bound at all: a "counter-notice" dated *before* the payment notice would also count, and that cannot be right. I recommend adding a lower bound of the service day and recording the same-day point as a fork.

### 3. Informing on a Saturday, then leaving the second working day after (H9). Line 182.

- **Scenario.** The occupier informs the undertaker on Sat 17 Oct 2026 and ceases to occupy on Tue 20 Oct.
- **Expected.** Not in time, so the occupier can be charged after leaving.
- **Code.** In time. The brief's day rule, "the day of ceasing is on or after WD+2", gives Tue 20 Oct.
- **Source.** s 144(3)(a) "at least two working days before he ceases to occupy". s 144(7) "a period of forty-eight hours calculated after disregarding any time falling on (a) a Saturday or Sunday ...".
- **View.** The Act differs from the brief here. When the informing day is itself a working day, informing during day d and leaving at the same hour on WD+2(d) gives exactly 48 counted hours, so the day rule is a fair approximation. When the informing day is excluded, none of it counts: the 48 hours run from 00:00 Mon 19 Oct to 24:00 Tue 20 Oct. Leaving at any time on Tue 20 Oct is therefore less than 48 hours after informing. The earliest day to leave in time is Wed 21 Oct, which is the day after WD+2. The same point affects informing on a bank holiday, Good Friday or Christmas Day. The fix is to roll an excluded informing day forward to the previous working-day boundary, or count from the next working day as working day 0. The s 144(6)(b) end of period, the end of the second working day, is not affected.

## Gaps noticed (not asserted, or not expressible in the types)

1. **The s 51(3) customer's part of the pipe (C7).** No input says whether the customer's part of the service pipe has been laid. Until it is laid the duty "shall not arise", but `the duty to connect has arisen for` ignores this, and `the last day to connect for` returns a date even when the customer has not laid the pipe. The brief lists s 51(3) only through s 51(6)(b), but s 51(3) is what stops the duty arising.
2. **The s 63A(1) intention.** The offence needs "the intention of enforcing payment of charges". The code makes the offence depend on Schedule 4A alone, and there is no input for intention (D24 could not be written).
3. **The s 61(2) occupier limb.** After a counter-notice the power returns only "at a time when that person is the occupier of the premises" *and* the charges are enforceable. Occupation is not an input; only enforceability is checked.
4. **The s 144(4) "first occurs after he ceases".** `the first relevant day for` filters the new-occupier day and the 28th day for being after the day of leaving, but not the meter-reading day. If `next normal meter reading on` is on or before the day of leaving, the code returns that day as the last day of liability, which is before the occupier even left. Only one meter-reading day can be given, so the caller must supply the first one after leaving.
5. **The s 144(5)(b) exclusion.** s 144(5) does not apply where the s 62 notice is given in connection with ceasing to occupy and s 144(2) provision applies. The proviso "otherwise than in pursuance of a demand for a supply made since the service of the notice" is also missing. `the last day I can be charged for after my s 62 notice` always returns a date.
6. **Prescribed conditions.** s 144A(5)(b) and s 144B(1)(c) depend on "such other conditions as may be prescribed". There is no input for them, and they are treated as met. The brief asks for `REFUSE` where the source does not answer, or at least an input.
7. **Revocation in s 144B(2)(a).** The single input "I gave a measured charges notice or consent" folds in "which has not been revoked", and s 144B(3) is folded into "occupation changed and no charges yet demanded". The Act's own tests are pushed onto the caller, so B4 and B7 could not be tested independently.
8. **No "may I revoke on day X" decision.** s 144A(5) gives only the last day. The day before, on and after the limit were tested through that date.
9. **Schedule 4A is a five-way enum.** Whether a dwelling is someone's "only or principal home" is answered by the caller choosing the enum value, so D2 and D5 (no principal home) reduce to "not listed".
10. **Conditions satisfied "as at" when.** `conditions satisfied on` is any date, with no as-at date. A future satisfaction date makes the duty "arisen" now.

## Agreements worth noting

All of these date conventions agree with my reading of the Act:

- s 47(3): service + 14, including month ends and the leap year.
- s 51: R + 13 and R + 20, with the relevant day rolling over month and year ends.
- s 48: whole 50p sums and whole three-month periods by corresponding date.
- s 106(4): receipt + 21.
- s 61(1ZA): cut-off from service + 8.
- s 144(4)(a): informing + 28.
- s 144(6) and the working days across Easter 2026, the May and August bank holidays, Christmas and New Year.
- s 144A(5): the day before the corresponding date, including 29 Feb.

## Change after the pass (encoder)

- **Line 124 (paying late, before the cut-off).** Not adopted. The encoding keeps the reading taken for the Gas Act 1986 (D3) and the Electricity Act 1989: once the seven days pass unpaid, a later payment does not end the power. The assertion is left failing and recorded as an open question (F4).
- **Line 137 (counter-notice on the day of service).** Accepted. The counter-notice must fall within the seven days beginning with the day after service; a lower bound was added.
- **Line 182 (informing on a Saturday).** Accepted. Informing on an excluded day starts the 48 hours at the next working day (F5).
- The gaps listed above are recorded as known limits in NOTES.md.
