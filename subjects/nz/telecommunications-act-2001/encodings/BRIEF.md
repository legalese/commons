# Encoding brief: the Telecommunications Act 2001 (New Zealand), consumer matters, copper withdrawal and levy, in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Telecommunications Act 2001**: New Zealand, Public Act 2001 No 103. The source is the version as at 4 September 2026, published by the Parliamentary Counsel Office on the New Zealand Legislation website.

The source file is `../registers/source-bundle/act_public_2001_103.txt` (sha256 `e36f6d7588bfadbea90e9056c68f7d5941b31ae6d3fb9a077f3b69f04a58856b`), converted from the PCO's XML on 2026-10-13. There is no copyright in New Zealand legislation (Copyright Act 1994, s 27).

**Consumer terms are mostly in codes.** Retail service quality codes, the 111 contact code and the copper withdrawal code are secondary legislation or industry codes, not in this source. This encoding covers what the Act itself makes computable for consumers: when Chorus may withdraw a copper service, the dispute resolution rules, the code-making periods, and the levy's late-payment interest.

**Working day** is defined in s 5. It includes the local anniversary day, which is an input.

## Scope

- **Copper withdrawal**: ss 69AC(2), 69AD(2) (Chorus may stop supplying only under an approved copper withdrawal code it complies with, or if the end-user chooses permanent disconnection), Schedule 2A cl 1(3) (the minimum protections the code must require), s 69AE (TSO instruments ceasing in specified fibre areas, except 111 call services).
- **Disputes**: s 241 (who may refer a dispute), s 242 (when a determination binds), ss 243-244 (only a non-member may appeal, within 5 working days after notification or further time allowed).
- **Periods**: s 239(3) (submissions on a draft Commission code "not later than 30 working days after" notice), Schedule 2A cl 2(2) (submissions on the copper withdrawal code "before the date that is 30 working days after" notice), s 246(1) (review of each industry scheme at least every 3 years), s 246(6) (20 working days for submissions on a draft report).
- **Levy**: s 14 (interest on unpaid levy at 1.5% a month for each month or part month from the due date).

## The top-level goal, and the goals under it

Top level: *for an end-user, a dispute and a levy payer: may Chorus stop supplying the copper service, may a party appeal a determination and by when, and what interest is due on late levy?*

1. **Copper withdrawal**: ss 69AC-69AE, Schedule 2A.
2. **Disputes and periods**: ss 239, 241-246, Schedule 2A cl 2.
3. **Levy**: s 14.

Inputs, not worked out: the copper service facts and each Schedule 2A protection; the end-user's choice; the code's approval and Chorus's compliance; the parties' scheme membership; dates of notification, notices and reviews; any court extension; the levy due date, amount and payment date; Matariki Observance Days and the local anniversary days.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on the goal of each group, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.
- Read the diagnostics, not the exit code.

## Deliverables (in this `encodings/` directory)

`tel-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
