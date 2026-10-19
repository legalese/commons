# Encoding brief: the Electricity Act 1989 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Electricity Act 1989** (1989 c. 29), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 24 July 2026, deposited at `../registers/source-bundle/ukpga-1989-29.txt` (Crown copyright, Open Government Licence v3.0). The conversion drops the paragraph numbers in the Schedules. Schedule 6 ("The electricity code") runs, in order: 1 meters for disabled persons; 2 non-payment of suppliers' charges; 3 deemed contracts; 4 supplies illegally taken; 5 restoration of connection without consent; 6 damage to electrical plant; 7 entry during continuance; 8 entry on discontinuance; 9 entry for replacing lines or plant; 10 provisions as to powers of entry; 11 distress.

## Seat

The encoding is written from the seat of **the electricity customer**: the owner or occupier who wants a connection, is supplied, or was affected by the supplier's breach (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level, in the customer's words: *"Must the distributor connect my premises, or keep them connected; when can it disconnect me; what interest is due on my security; until when can I refer a connection dispute to Ofgem? Can my supplier fit a pre-payment meter or disconnect me for unpaid charges, from when; may its officer enter; can I restore the connection myself? And if Ofgem acts on my supplier's breach, can a consumer redress order still be made, by when must I be paid, and what can I recover on electricity resold to me?"*

1. **Connection** (ss 16(1), (4), 16A(1)-(2), 17, 20(1A), (3), 22(2), 23(1C)):
   - whether the duty to connect (or maintain) applies, with the s 16A notice, the exceptions in s 17(1)-(2), a special connection agreement, and security under s 20(1A);
   - the earliest day the distributor may disconnect a maintained connection under s 17(1)(c), after not less than seven working days' notice (s 17(3));
   - the interest on a security deposit (s 20(3));
   - the last day to refer a dispute about making the connection (s 23(1C)).
2. **Non-payment, and entry** (Schedule 6 paras 2, 5, 7(4)-(5), 8(3)-(4), 10(4)):
   - from when the supplier may install a pre-payment meter or disconnect for unpaid charges (para 2), and whether it may on the day;
   - whether its officer may enter to do so;
   - whether restoring the connection oneself is an offence (para 5).
3. **Redress and resale** (ss 27G(1), (5), 27K, 27M(2), (5), 27N(1)-(2), (4), 27O(2)-(4), 44(2)(b), (4)): as for the Gas Act 1986 — whether an order can be made within the time limits, the compliance date, the appeal period and suspension, interest on unpaid compensation, the cap, and the excess on resale.

Left out on purpose: licensing and the regulators (ss 3A-15A), penalties (ss 27A-27F, except their amount under s 27O(4)), standards of performance (ss 39-40B, set by regulations), the renewables obligation, generating station consents, meters (Schedule 7), and the other Parts and Schedules.

## Inputs, not worked out

- **Working days:** s 64(1) — any day other than a Saturday, a Sunday, Christmas Day, Good Friday or a bank holiday under the Banking and Financial Dealings Act 1971. The bank holidays are an input list; Good Friday is computed.
- **Connection:** who requires it, the notice and whether it specifies the premises, date and maximum power, whether the connection is maintained, the distributor's circumstances (s 17), security, the disconnection notice and day, the day the connection was made; the deposit, the rate fixed per 50p per three months, and its dates.
- **Non-payment:** the demand and payment dates, any genuine dispute, the notice of intention, the action and its day, the entry notice, the time and the officer's document, consent to restore.
- **Redress:** as for the Gas Act 1986.
- Judgments for someone else are inputs: "not reasonable in all the circumstances" (s 17(1)(c)), the Authority's view under s 27N(2).

## Dates, as the Act gives them

Compute every period exactly as the Act words it.

- **s 17(3), "not less than seven working days' notice"; Sch 6 para 2(2)(b) likewise; paras 7(5), 8(4) "at least two working days' notice"**: the act may be done on or after the seventh (or second) working day after the day of the notice.
- **Sch 6 para 2(3), "the period of 28 days after the making ... of a demand"**: payment by the demand day + 28 is in time; the power can be exercised from the demand day + 29 at the earliest.
- **s 23(1C), "the end of the period of 12 months beginning with the time when the connection is made"**: the day before the corresponding date, or the last day of the month where there is none.
- **s 20(3), "on every sum of 50p ... for every three months"**: whole sums of 50p and whole periods of three months.
- **ss 27G(5), 27K, 27M(2), 27N(1)**: as for the Gas Act 1986 ss 30G(5), 30K, 30M(2), 30N(1): compliance date on or after service + 7; 5 years and 3 or 6 months "from" are corresponding dates; appeal by service + 42; interest from the day after the compliance date.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`ea89-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
