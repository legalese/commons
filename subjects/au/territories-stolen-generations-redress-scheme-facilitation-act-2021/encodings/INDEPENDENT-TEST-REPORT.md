# Independent test report: Territories Stolen Generations Redress Scheme (Facilitation) Act 2021 (Cth)

Expectations were written in `independent-expectations.md` from `BRIEF.md` and the source text alone, before any `.l4` file was opened. `tests-independent.l4` asserts them against `tsgr-rules.l4`. No expected value was changed after the tests ran.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 4 | 20 | 4 |
| tsgr-rules.l4 | 0 | 0 | 0 |
| tsgr-tests.l4 | 0 | 11 | 0 |

There are 24 independent assertions: 20 pass and 4 fail. The 4 errors are the 4 failed assertions. There are no syntax or type errors.

## How the expectations map to the encoding's output

The encoding answers each question as asked: JUST TRUE, JUST FALSE, or NOTHING where the Act does not answer. In the expectations:

- **"protected"** becomes JUST FALSE. The payment does not affect eligibility, is not compensation, and cannot be sold or taken.
- **"not protected"** becomes NOTHING. This is the encoding's own convention: where s 4(5) or s 4(6) displaces the protection, it gives NOTHING.

## Failures (all on s 4(3), the assets question)

| # | Assertion | Expected | Encoding |
|---|---|---|---|
| 15 | assets, SSA/VEA | NOTHING | JUST TRUE |
| 16 | assets, SSA/VEA (VEA case) | NOTHING | JUST TRUE |
| 17 | assets, another Commonwealth law | NOTHING | JUST TRUE |
| 18 | assets, prescribed State or Territory law | NOTHING | JUST TRUE |

Why I expect NOTHING: s 4(3) says only that "subsections (1) and (2) do not apply for the purposes of determining the value of a person's assets". It switches the protection off. It does not enact that the payment *is* counted in the value of assets; that is for the SSA, the VEA or the other law asking.

The encoding's answer "yes, it is counted" (JUST TRUE), and its export text "it does count in the value of my assets", go beyond the Act. The encoding is also inconsistent with itself:
- For a displaced Commonwealth law (s 4(5) express provision) on the same assets question, it gives NOTHING.
- Where the protection never existed (an unprescribed State law), it also gives NOTHING.
- But where (3) removes the protection, it gives TRUE.

The practical likelihood is that the payment will count, which is presumably the purpose of (3). If the authors prefer to keep JUST TRUE, they should note that it is an inference about the other law, not a holding of this Act. This is a finding to adjudicate, not a test to change.

## Agreements worth recording

- s 4(1) is limited to Commonwealth laws. Eligibility under any State or Territory law gives NOTHING (tests 6 and 7).
- s 4(2)(c) reaches only prescribed State or Territory laws. Compensation under an unprescribed one gives NOTHING (test 11).
- s 4(5)'s express-provision escape applies only to Commonwealth laws. A flag set on a State law changes nothing (tests 14 and 24).
- s 4(6) does not reach s 4(4). Inalienability survives a regulation exclusion (test 23); the encoding carves this out correctly.
- s 4(4) applies against State law (test 21).

## Gaps

- **s 4(6) granularity.** The Act lets the regulations exclude a law from "one or more of" (1), (2), (3), but the encoding has a single flag. Under the encoding, excluding a law from (3) alone is indistinguishable from excluding it from (1) and (2). On the Act, a law excluded from (3) only would bring the (1)/(2) protection back for the assets question. I did not assert assets plus regs exclusion.
- **SSA and VEA** are one constructor in the encoding, so tests 2 and 16 duplicate tests 1 and 15.
- **Prescription in s 4(2)(c) and s 4(3)(c)** is made "for the purposes of this paragraph" in each case, so a State law could be prescribed for one paragraph and not the other. The single "prescribed State or Territory law" value cannot express that.
- **Commencement** (1 March 2022), s 5 (binds the Crown) and s 6 (regulation-making power) are not modelled and not tested.

## Change after the pass (encoder)

- **Tests 15-18 (the assets question).** Accepted. s 4(3) only switches (1)-(2) off; the answer is now NOTHING (F3). One of the encoder's tests was updated, with a comment.
- The gaps are recorded as known limits in NOTES.md.
