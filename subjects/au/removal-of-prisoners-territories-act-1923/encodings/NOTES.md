# Removal of Prisoners (Territories) Act 1923 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the prisoner position for` (`rpt-rules.l4`). It answers:

- whether removal may be recommended, and whether it is lawful;
- that the conviction may be questioned in the Territory of origin;
- whether the prisoner is entitled to a free return;
- that time at large after an escape does not count towards the sentence.

## Seat

The encoding is written from the seat of **the prisoner sentenced to imprisonment in a Territory**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Can I be removed from the Territory to serve my sentence elsewhere; if removed, where can my conviction and sentence still be questioned; can I be sent home free after discharge; and if I escape, does my sentence keep running?"

## Coverage

| Provision | Disposition |
|---|---|
| s 2 | (1)-(2) applied: "prisoner"; the Act's exclusion is reflected in the input |
| s 2A | out of scope |
| s 3 | encoded |
| s 4 | out of scope: warrants (the s 8AA(1) bar on s 4(1) warrants is encoded) |
| s 5 | (2) encoded; (1), (3) are out of scope |
| s 6 | out of scope: remission is the Governor-General's discretion |
| s 7A | encoded |
| s 7B | out of scope: arrest of prisoners at large |
| s 8 | (3) encoded; (1)-(2) are out of scope |
| s 8AA | (1) encoded |
| ss 8A onwards | out of scope: licences and orders |

## Forks (readings taken)

- **F1, s 3(1).** The grounds are as they appear to the Administrator, and they are an input. The Act does not apply to the Northern Territory for this purpose.
- **F2, s 8(3).** The free return requires lawful removal under this Act, discharge or release in the receiving place, and no breach or unlawfulness. The application's manner and time are prescribed by regulations, which are not modelled.
- **F3, s 7A.** The answer is TRUE for any prisoner: the punishment not undergone while at large must still be undergone.

- **Known limits (from the independent pass).**
  - The s 2 exclusion and the s 2(2) commuted death sentence are folded into one input, and the two limbs of s 3(1)(a) are one choice.
  - Whether a recommendation was actually made is not an input; nor whether the removal was carried out (lawful removal stands in for "removed" in s 8(3)).
  - The s 8(3) application in the prescribed manner and time is not an input.
  - The s 7A answer is a constant TRUE for any prisoner; the time still to serve is not computed.
  - "Conviction questioned in the Territory of origin" is FALSE for a prisoner never removed, which only reflects that s 5(2) concerns removed prisoners.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 36 assertions satisfied, 0 failed, 0 other errors — 10 the encoder's (`rpt-tests.l4`), 26 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
