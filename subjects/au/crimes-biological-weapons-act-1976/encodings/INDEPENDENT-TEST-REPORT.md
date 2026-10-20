# Independent test report: Crimes (Biological Weapons) Act 1976

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text only, before any L4 was read. `tests-independent.l4` asserts them against `cbw-rules.l4`.

## Result

`check.sh`: tests-independent.l4 — **22 assertions: 20 satisfied, 2 failed**, no other errors (the 2 errors reported are the 2 failed assertions).

## Scenarios asserted (agreeing)

- s 8(1)(a)/(b), 8(2): natural person (life imprisonment, 100 penalty units) and corporation (2,000 penalty units, no imprisonment); peaceful-purpose agents not unlawful and not forfeited.
- s 4/s 5 reach: non-citizen in Australia caught; citizen abroad caught; non-citizen and corporation abroad not committing an offence.
- s 9(1) forfeiture for an offence in Australia.
- s 9(2) retention: seized 1 Jan 2023 -> 2 Mar 2023; seized 1 Jan 2024 (leap year) -> 1 Mar 2024; prosecution instituted -> no fixed last day.
- s 10(3)-(4): committal only with written consent.
- s 12(4): certificate admissible only with a copy and reasonable notice.

## Disagreements (failing assertions)

1. **Forfeiture where the Act does not reach the conduct (tests-independent.l4 line 46).** A non-citizen acting outside Australia and the external Territories holding no-justification agents: the module says the material *is* forfeited (`it is forfeited` = `it is unlawful`, which ignores s 5), while it correctly says there is no offence. s 9(1) forfeits only material held "in contravention of subsection 8(1)"; by s 5 the Act extends outside Australia only to acts of Australian citizens, so a non-citizen's conduct abroad does not contravene s 8(1). The forfeiture rule should use the same reach test as the offence. Confidence: high that the outputs are inconsistent; medium-high on the reading.

2. **Last day to notify the prosecutor to call the analyst (line 62).** Hearing 10 Jun 2024: the module gives 5 Jun 2024 (hearing minus 5); I expected 4 Jun 2024. s 12(6)(a) requires "at least 5 days notice"; the conventional Australian reading of "at least N days" is N clear days, excluding both the day of notice and the day of the hearing, so the latest notice day is 4 Jun (clear days 5-9 June). Confidence: medium; if the drafter intends only the notice day to be excluded, 5 Jun is right, but the conservative answer for the person asking "by when" is 4 Jun.

## Coverage gaps

- Expectations 18-20 (whether the person *is entitled* to require the analyst, including the s 12(6)(b) court-order route) cannot be tested: the module outputs only the notice date and has no input for the date notice was given or for a court order.
- s 10(4) (may be charged, arrested and remanded without consent) has no output; only committal is modelled.
- Whether a corporation can be an Australian citizen for s 5 is left to the caller's boolean; the test passed `FALSE`.
- External Territory and Australia are one enum value, so s 4 is covered only implicitly.
- `I commit an offence` does not depend on `what I do with it` being one of the listed acts except via `it is unlawful`; asserted scenarios all use the listed acts.

## Change after the pass (encoder)

- Forfeiture now follows the s 5 reach, as the tester read it.
- One disagreement is left open: the tester reads s 12(6)(a)'s 5 days as clear days (`tests-independent.l4` line 62 is expected to fail).
- The gaps are recorded as known limits in NOTES.md.
