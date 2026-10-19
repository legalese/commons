# Encoding brief: the Gas Act 1986 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Gas Act 1986** (1986 c. 44), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 13 November 2025, deposited at `../registers/source-bundle/ukpga-1986-44.txt` (Crown copyright, Open Government Licence v3.0).

## Seat

The encoding is written from the seat of **the gas consumer**: the owner or occupier of premises who wants gas, takes a supply, or has been affected by a supplier's breach (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level, in the consumer's words: *"Must the gas transporter connect my premises, or keep them connected, and what can I be charged? Can my supplier cut off my gas or fit a prepayment meter for an unpaid bill or deposit, from when, and may its officer enter; can it refuse to restore the supply? And if Ofgem acts on my supplier's breach, can a consumer redress order still be made, by when must I be paid, and if I bought gas resold to me, what can I recover?"*

1. **Connection** (ss 10(1)-(5A), (6), (8)-(10), 11(1)-(2)):
   - whether the premises fall within s 10(1) and the duty to connect (s 10(2)) or to maintain a connection (s 10(3)) applies;
   - the notice under s 10(4);
   - the exceptions in s 10(8) and (9), and the transporter's right to refuse without a contract under s 10(10);
   - the costs the consumer can be made to bear (s 10(5), (5A)), the vesting of the consumer's pipe (s 10(6)), and the security under s 11.
2. **Cutting off for debt, and entry** (Schedule 2B paras 7, 11, 19, 24 and 28(1)):
   - whether, and from when, a supplier may cut off the supply or fit a prepayment meter for an unpaid demand (para 7(1)) or a refused deposit (para 7(2)), after 7 days' notice (para 7(3)), including the assigned-debt case (7(4)) and the dispute bar (7(5));
   - whether restoring the supply oneself without consent is an offence (para 11);
   - whether the supplier can refuse to restore the supply (para 19);
   - whether its officer may enter to cut off the supply (para 24, with para 28(1)).
3. **Redress and resale** (ss 30G(1), (3)(e), (5), 30K, 30M(2), (5), 30N(1)-(2), (4), 30O(2)-(4) and 37(2)(b), (4)-(5)):
   - whether a consumer redress order can be made in respect of the contravention, given its time limits;
   - whether the compliance date in an order is lawful, the supplier's last day to appeal, whether compliance is suspended by an appeal, and from when interest runs on unpaid compensation;
   - the most compensation that can be required for the contravention;
   - the excess recoverable on gas resold above the maximum price.

Left out on purpose:
- the regulators' functions, licensing (ss 4AA-9, 23-29), and the penalty regime against the supplier (ss 30A-30F; only the penalty amount enters, under s 30O(4));
- standards of performance (ss 33A-33AB): the compensation is set by regulations, which are not in the deposited text;
- meters, safety and gas quality (ss 12-18A), Schedule 2B paras other than those listed, land acquisition, and Parts II onward.

## Inputs, not worked out

- **Connection:** where the premises are (within 23 metres of a relevant main, or able to be connected by the consumer's own pipe), whether they are already connected, the notice and the day it names, the expected annual supply in therms, and the transporter's circumstances (s 10(9), (10)).
- **Cut-off:** the dates of the written demand or deposit request, of any payment or deposit, of the notice of intention, and of the cut-off; whether the amount is genuinely in dispute; whether the supplier is still the consumer's supplier; the entry facts.
- **Redress:** the date of the contravention, any final or provisional order and its dates, the notices served, the dates in the order, any appeal, turnover and any penalty imposed.
- Judgments for someone else are inputs, and the answer is conditional on them: "the day named is not earlier than a reasonable time after the notice" (s 10(4)(b)), "the Authority is satisfied the Competition Act 1998 is the most appropriate way" (s 30N(2)).

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **Sch 2B para 7(1)(b), "does not make those payments within 28 days after the making of the demand"**: payment by demand day + 28 is in time. The power arises from demand day + 29.
- **Para 7(2)(b), "within 7 days after the making of the request"**: by request day + 7; the power arises from request day + 8.
- **Para 7(3), "after giving not less than 7 days' notice of his intention"**: the notice must be given once (1) or (2) applies; the earliest day to act is the notice day + 7.
- **Para 24(2), "after 24 hours' notice"**: the hours of notice given are an input, at least 24.
- **s 30G(5), "not ... earlier than the end of the period of 7 days from the date of the service"**: the compliance date must be on or after the service day + 7.
- **s 30K(1), "the end of the period of 5 years from the time of the contravention"**: the corresponding date 5 years on.
- **s 30K(3), "within 3 months from", "within 6 months from"**: on or before the corresponding date 3 (or 6) months on, or the last day of the month where there is none.
- **s 30M(2), "within 42 days from the date of service"**: by service day + 42.
- **s 30N(1)**: interest runs on any unpaid balance from the day after the date by which it was required to be paid.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`gas-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
