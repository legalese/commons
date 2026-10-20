# Independent test report: Asbestos-related Claims (Management of Commonwealth Liabilities) Act 2005

Tester: an independent pass. Expectations were written from BRIEF.md and the source text (`independent-expectations.md`) before any L4 was read; the rules module was then read only for names and input shapes.

## Result

`L4=~/.local/bin/l4 ./check.sh` on `tests-independent.l4`: **45 assertions, 41 satisfied, 4 failed**, no other errors.

## Scenarios

16 scenarios (see `independent-expectations.md`): claims before, on, and after the 26 October 2005 commencement (s 5(1)/(2)), a claim against Comcare (s 5(3)), no claim yet, every condition branch including "not caused by asbestos", every breacher (Commonwealth, authority, excluded bodies, someone else), all three exclusions from "liability", s 6 declarations for an authority and (no effect) for the Commonwealth, and a claim against Comcare before commencement.

## Disagreements

### 1. May I claim against Comcare when the liability is excluded (scenarios 10, 11; lines 83, 90)
- Code: `I may claim against Comcare` is FALSE when the liability arises under a contract of insurance or a final judgment (and, by the same rule, an earlier written settlement).
- My reading: TRUE. s 5(3) says "If, on or after the commencement of this Part, a person **could make an asbestos-related claim** against the Commonwealth or a Commonwealth authority then: (a) the person may make the claim against Comcare". "Asbestos-related claim" (s 3(1)) does not depend on what the liability arises under; the s 3(1) exclusions from "liability" only stop the *liability* transferring under s 5(3)(b). So the person may make the claim against Comcare, but no liability passes to it.
- Confidence: medium. The encoding's reading (a claim against Comcare is pointless if nothing transfers) is a practical one, but it is not what s 5(3)(a) says. Both readings agree that no liability transfers.

### 2. Claim against Comcare before commencement (scenario 16; lines 118, 119)
- Code: a claim made against Comcare on 1 October 2005 transfers the liability to Comcare on 26 October 2005 (it treats any claim made on or before commencement under s 5(1), whoever it was made against).
- My reading: no transfer from that claim. s 5(1) applies only where the claim "was made **against the Commonwealth or a Commonwealth authority**" on or before commencement; s 5(3) applies only "on or after the commencement". A pre-commencement claim against Comcare falls under neither, so the liability stays with the Commonwealth (until a fresh claim is made).
- Confidence: medium-high on the text; the case is unlikely in practice (Comcare had no function for these claims before the Act).

## Coverage gaps

- Commonwealth authority (a)-(c) limbs and s 4 declarations are folded into an input; not tested beyond the input values.
- "Subject to appeal" timing (judgment stayed / appeal pending at commencement) is folded into one input value; the boundary is not testable.
- s 6(1)(b) (successor in law of the authority) is not separately modelled.
- The date from which an s 6 declaration takes effect ("immediately after the instrument is made") is not an input or output, so not tested.
- A claim against the Commonwealth after a claim against Comcare (two claims) cannot be expressed.

## Change after the pass (encoder)

- Both disagreements were accepted: anyone with an asbestos-related claim may claim against Comcare (s 5(3)(a)), and a claim made against Comcare before commencement does not transfer (s 5(1)).
- The gaps are recorded as known limits in NOTES.md.
