# Crimes (Overseas) Act 1964 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the overseas position for` (`co-rules.l4`). It answers:

- whether this Act applies to me for the act;
- whether Jervis Bay criminal law applies to my act;
- whether proceedings may be commenced;
- whether I may be arrested or charged before consent;
- the last day to give me a copy of a certificate;
- the last day to notify the prosecutor to call the issuer.

The encoded provisions are ss 3, 3A, 4(1), (2), (4) and 8(6), (8)(a). The source is the compilation of 3 October 2014.

## Seat

The encoding is written from the seat of **the Australian whose act in a foreign country is in question**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Does this Act apply to what I did overseas, so that Jervis Bay criminal law applies to me; what must happen before I am prosecuted?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | Australian encoded; the other definitions are folded into the inputs |
| s 3A | encoded; (7)-(9) (the task periods) are folded into the ground |
| ss 3B-3C | out of scope: declarations are inputs |
| s 4 | (1), (2), (4) encoded; (3), (5) are out of scope |
| ss 5-7 | out of scope |
| s 8 | (6), (8)(a) encoded; the rest is out of scope |
| s 9 | out of scope |

## Forks (readings taken)

- **F1, s 3A(2).** It qualifies only the immunity ground in s 3A(1): the Act stops applying while the person is, or will be, subject to local prosecution that an Australian verdict would not end.
- **F2, s 3A(4)-(6).** Where the regulations limit a declaration to a category of people, the person must be within it.
- **F3, s 8(6), (8)(a).** "At least 14 days before" and "at least 4 days notice": the last days are the tender day − 14 and the hearing day − 4, as for the other notice periods read in this repo.
  - **Disagreement from the independent pass, left open.** The tester reads both as clear days (tender − 15, hearing − 5); its four date assertions (`tests-independent.l4` lines 72, 75, 78 and 81) are left failing. The tester's confidence is medium.
- **Known limits (from the independent pass).**
  - The ground is a single choice, so a person qualifying on two grounds cannot be expressed.
  - s 3A(7)-(9) (off-duty acts in the relevant period) are not modelled.
  - A declared country and a declared part share one value.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 37 assertions satisfied, 4 failed, 0 other errors — 15 the encoder's (`co-tests.l4`), 26 independent (`tests-independent.l4`). Four assertions in `tests-independent.l4` (lines 72, 75, 78 and 81) are expected to fail: they read s 8's 14 and 4 days as clear days (F3).

## Open questions for an Australian lawyer

- **F3:** are the 14 and 4 days clear days?
