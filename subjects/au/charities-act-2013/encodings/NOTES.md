# Charities Act 2013 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `we are a charity` (`charities-rules.l4`). It answers whether an entity is a charity under s 5, with ss 6-12 applied. The source is the compilation on the Federal Register of Legislation.

## Seat

The encoding is written from the seat of **the organisation asking whether it is a charity**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Are we a charity under the Charities Act?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | the definitions are folded into the inputs |
| s 5 | encoded |
| ss 6-10 | encoded: public benefit (a finding), the s 7 presumption, s 8, s 10; s 9 (native title) is folded into the public benefit finding |
| s 11 | encoded: a disqualifying purpose is an input kind |
| s 12 | encoded: the kinds of charitable purpose |
| ss 13-17 | out of scope: what the named purposes include, contribution funds |
| the rest of the Act | out of scope |

## Forks (readings taken)

- **F1, s 5.** An entity with no charitable purpose at all is not a charity, even if every listed purpose is "incidental", because incidental purposes must further a charitable purpose.
- **F2, s 8.** For relieving necessitous circumstances, only the s 6(1)(a) limb (that achieving the purpose would be of public benefit) is needed.
- **F3, s 10.** A self-help group or contemplative order meeting s 10 needs no public benefit finding for any purpose.
- **Known limits (from the independent pass).**
  - s 9 (native title) is reached only through a public benefit finding.
  - The five s 10(1) criteria and the s 10(2) condition are one input.
  - The s 11(a)/(b) split and the s 12(1)(l) conditions are left to how the purpose is classified.
  - A purpose that is both relieving poverty (s 7(c)) and necessitous circumstances (s 8) must be entered as one kind.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 39 assertions satisfied, 0 failed, 0 other errors — 13 the encoder's (`charities-tests.l4`), 26 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
