# Epidemiological Studies (Confidentiality) Act 1981 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the study position for` (`esc-rules.l4`). It answers:

- whether recording or passing on the information would be an offence;
- the maximum penalty (6 months' imprisonment or 10 penalty units);
- whether I may be required to give it to a court;
- whether I must take an oath of secrecy.

The encoded provisions are ss 3-11. The source is the compilation of 21 October 2016.

## Seat

The encoding is written from the seat of **the person who helps conduct a study**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "May I record or pass on what I learned about someone through the study; can a court make me produce it?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery |
| s 3 | encoded: prescribed study (the declaration is an input), assisting (s 3(2)); affairs (s 3(3)-(4)) is folded into the input |
| s 3A | out of scope: the Criminal Code's fault rules |
| s 4 | encoded |
| s 5 | encoded as a defence |
| s 6 | encoded |
| s 7 | encoded |
| s 8 | encoded |
| s 9 | applied: any capacity counts as assisting |
| s 10 | encoded |
| s 11 | encoded: (1) non-identifying publication is not an offence |
| s 12 | applied: earlier information is covered |
| s 13 | out of scope: regulations |

## Forks (readings taken)

- **F1, s 7.** It permits "giving information", so it does not excuse making a record.
- **F2, s 5.** The defence covers giving access to a document of the study, in accordance with the authorisation, to a person assisting another prescribed study.
- **F3, s 6.** "The purpose of the conduct of either of those studies" is the same purpose input.
- **F4, s 8.** Outside the Act's reach, whether a court can compel production is not answered: NOTHING.
- **F5, s 10.** Failing to take the oath is an offence with the same penalty; the encoding reports only whether I must take it.
- **Known limits (from the independent pass).**
  - An identifying s 11 publication is entered as the non-identifying flag being false.
  - s 7(c) consent is folded into the recipient.
  - s 8 gives NOTHING for information that came otherwise than through the study, though s 8(1)(a) may reach any study document.
  - s 10's "about to become" a person bound has no input.
  - The s 9 capacities are one value.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 41 assertions satisfied, 0 failed, 0 other errors — 15 the encoder's (`esc-tests.l4`), 26 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
