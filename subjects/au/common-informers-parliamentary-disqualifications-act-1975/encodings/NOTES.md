# Common Informers (Parliamentary Disqualifications) Act 1975 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the common informer position for` (`cipd-rules.l4`). For a senator or member sued for having sat while incapable, it answers:

- the sum they can be made to pay (s 3);
- that no suit lies under s 46 of the Constitution (s 4).

The operative ss 3-4 are encoded. The source is the compilation prepared on 8 July 2008 (C2008C00320).

## Seat

The encoding is written from the seat of **the senator or member sued**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "How much can I be made to pay to the person suing me; and can I be sued under s 46 of the Constitution instead?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery |
| s 3 | encoded |
| s 4 | encoded |
| s 5 | a note: original jurisdiction is in the High Court alone |

## Forks (readings taken)

- **F1, s 3(2), "a time earlier than 12 months before the day on which the suit is instituted".** A sitting counts if it is on or after the corresponding date 12 months before that day.
- **F2, s 3(1)(a).** The $200 is due once if any counted sitting falls on or before the day the originating process was served. Each counted sitting after that day adds $200 (s 3(1)(b)).
- **F3, s 3(3).** Days already penalised in another suit are excluded. Whether an order "would ... cause [a person] to be penalized more than once" is the Court's opinion; the days are an input.
- **F5 (changed after the independent pass).** A day listed twice counts once.
- **Known limits (from the independent pass).** Section 3(3) is the Court declining to make an order; the encoding reduces the sum instead. The order of the dates (service after institution) is not checked.
- **F4.** Whether the person was incapable of sitting under the Constitution is a finding, and it is an input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 26 assertions satisfied, 0 failed, 0 other errors — 8 the encoder's (`cipd-tests.l4`), 18 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F2:** does s 3(1)(a)'s $200 cover all sittings before service, however many, or one sitting?
