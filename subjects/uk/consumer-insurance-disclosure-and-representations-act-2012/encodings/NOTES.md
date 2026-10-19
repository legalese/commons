# Consumer Insurance (Disclosure and Representations) Act 2012 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the misrepresentation position for` (`cidra-goal.l4`). A consumer made a misrepresentation before taking out insurance and has made a claim. The goal answers:

- whether the Act applies;
- whether the misrepresentation is a qualifying one, and of which class;
- what the insurer may do.

Three goals sit under it:

1. **Does the Act apply** (`cidra-misrepresentation.l4`): ss 1 and 12(4).
2. **Qualifying misrepresentation and its class** (`cidra-misrepresentation.l4`): ss 2(2), 3(5), 4(1)-(2) and 5.
3. **The insurer's remedies** (`cidra-remedies.l4`): s 4(3), and Schedule 1 Part 1 paras 2 and 4-9.

As the user asked, this covers only the sections those goals need. The Act has no periods to compute: "reasonable notice" in para 9 is evaluative.

## Seat

The encoding is written from the seat of **the consumer policyholder**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "I made a mistake on my insurance application. Does the Act protect me; was my mistake careless or deliberate; and what can the insurer do to me — refuse my claim, keep my premiums, cut my claim or cancel my policy?"

The facts it asks for are ones that person can state, or findings made about them.

The remedy record (`Remedy`) is phrased as what the insurer "may" do. For the consumer, it is the most the insurer can do to them: the claim paid is the least they will receive, and a refund of premiums is money owed back to them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| s 1 | encoded (goal 1) |
| s 2(2) | encoded (goal 2) |
| s 2(1), (3)-(4) | inert, or folded into the "a misrepresentation was made" input (a failure to confirm or amend particulars counts as one) |
| s 3(1)-(4) | input: the finding on reasonable care |
| s 3(5) | encoded (goal 2) |
| s 4 | encoded (goals 2-3) |
| s 5 | encoded (goal 2) |
| s 6 | out of scope: warranties |
| s 7, Sch 1 Part 3 | out of scope: group insurance |
| s 8 | out of scope: life of another |
| s 9, Sch 2 | out of scope: agents |
| s 10 | out of scope: contracting out |
| s 11 | out of scope: consequential amendments |
| s 12(4) | encoded (goal 1): commencement is an input |
| s 12 otherwise | out of scope |
| Sch 1 Part 1 paras 1-9 | encoded (goal 3) |
| Sch 1 Part 2 | out of scope: variations |
| Sch 1 Part 4 | out of scope: marine insurance |

## Forks (readings taken)

- **F1, lost paragraph numbers and formula.** The conversion drops the Schedule paragraph numbers and the para 8 formula. The encoding uses the order of the printed text (paras 1-9), and the formula X = (premium actually charged ÷ higher premium) × 100 from the Act as published.
- **F2, s 4(1)(b): "only on different terms".** A higher premium is a different term. Inducement holds if the insurer would have declined, would have required different non-premium terms, or would have charged a higher premium.
- **F3, s 5(5): presumptions where nothing is shown.** For each limb of s 5(2), a fact shown either way (JUST) decides it. Where nothing is shown (NOTHING):
  - (a) gives the consumer the knowledge of a reasonable consumer, an input;
  - (b) presumes knowledge of relevance where the insurer asked a clear and specific question.
- **F4, the remedy is the most the insurer may do.** Para 6 applies "if the insurer so requires", and paras 7 and 9 say "may", so the encoding gives the insurer's full entitlement. The amount payable assumes the insurer exercises paras 6 and 7.
- **F5, para 2(b).** The premiums the insurer need not return are all of them except any part it would be unfair to keep, which is an input amount.
- **F6, para 9.** The notice and termination rights are given only for a careless misrepresentation where para 6 or 7 would apply, so not where the insurer would not have contracted at all (para 5 already lets it avoid). Termination is barred for contracts wholly or mainly of life insurance (para 9(5)).
- **F7, no rounding.** The proportionate reduction is not rounded. The Act states none.
- **F8, para 9(6).** After the insurer's notice under 9(4)(a), the consumer may terminate. The life-insurance bar does not apply to this. This was added after the independent pass. Paras 9(7)-(8) are not computed.
- **F9, commencement (s 12(2)-(4)).** The Act does not name its commencement day (an order fixed it), so "entered into after the Act came into force" is an input.
- **F10, the exported helpers.** `is a qualifying misrepresentation …` and `the insurer's remedy for …` do not check that the Act applies; only the top-level goal does.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18:

- 6 modules: 154 assertions satisfied, 0 failed, 0 other errors;
- 48 are the encoder's (`cidra-tests.l4`);
- 106 are independent (`tests-independent.l4`).

No assertion is expected to fail.

## Open questions for a UK lawyer

- **F3:** is s 5(5)(a) correctly modelled as supplying the knowledge of a reasonable consumer for both limbs of s 5(2)?
