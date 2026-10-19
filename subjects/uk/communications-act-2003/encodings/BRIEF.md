# Encoding brief: the Communications Act 2003 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Communications Act 2003** (2003 c. 21), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 6 April 2026, deposited at `../registers/source-bundle/ukpga-2003-21.txt` (Crown copyright, Open Government Licence v3.0).

## Seat

The encoding is written from the seat of **the individual end-user**: the customer of a phone or broadband provider, the person who watches television, and the person accused of misusing a network (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level, in the end-user's words: *"If I end my phone or broadband contract early, what can I be made to pay, and does it cover the whole bundle? Do I need a TV licence; do I meet the age for a concession; until when can a search warrant be used? If I am accused of misusing a network: is it an offence, can I still be prosecuted, how long must Ofcom give me to answer, and what is the most it can fine me?"*

1. **Ending a contract early** (ss 124U(1)-(4), 124V, 51(8)-(9)):
   - whether s 124U applies (a right to terminate early; machine-to-machine services only for qualifying end-users);
   - the most compensation for retained terminal equipment (the lesser of the remaining fees and the unexpired proportion of the agreed equipment value), and nothing else;
   - whether the rights extend to every element of a bundled contract (s 124U(4)), and whether a consumer may terminate the whole bundle for non-conformity of one element (s 124V).
2. **TV licensing** (ss 363(1)-(3), (5), 365(5A), 365A(2), 366(4), 368(3)):
   - whether installing or using a receiver without a licence is an offence;
   - whether I meet an age requirement of a concession (age at or before the end of the month of issue) and whether the age is one the Act allows (65 or higher);
   - the last day a warrant can be used for entry.
3. **Misuse of a network** (ss 127(1)-(2), (4)-(5), 128(2)-(4), 129(1), 130(1), (4)):
   - whether the conduct is an offence under s 127;
   - whether the information was laid in time (both limits in s 127(5));
   - the shortest representation period Ofcom must allow (s 128(3)), whether the period given was long enough, and whether Ofcom may act yet (ss 129(1), 130(1));
   - whether a penalty is within the £2,000,000 maximum (s 130(4)).

Left out on purpose: Ofcom and its functions, the regime of conditions (ss 45-124T except as above), spectrum, broadcasting licensing, Part 4A, competition, and the Schedules.

## Inputs, not worked out

- Contract: whether there is a right to terminate early, the kind of end-user, whether the service is machine-to-machine, whether I keep the equipment, the remaining fees, the agreed equipment value, the contract and remaining months, whether the contract is bundled and whether bundle rights were waived; for s 124V, whether an element failed to conform.
- TV: whether a receiver is installed or used to receive television programmes or BBC on-demand programmes, whether licensed, the dealer purposes and any exemption in regulations; date of birth, the day the licence is issued and the concession's specified age; the day the warrant was granted.
- Misuse: what was sent and why, whether in a programme service; the day of the offence, the day the prosecutor knew enough evidence (a certificate is conclusive), and the day the information was laid; the day of the s 128 notification, whether Ofcom considered the case urgent, the end of the period given, the day Ofcom acts, and the penalty.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **s 127(5), "before the end of the period of 3 years beginning with the day on which the offence was committed" and "6 months beginning with the day on which evidence comes to the knowledge"**: the last day is the day before the corresponding date, or the last day of the month where there is none; both limits must be met.
- **s 128(3), "must not be less than ... seven days" / "one month"**: the period must end on or after the notification day + 7 (urgent), or the corresponding date one month after the notification day (otherwise).
- **ss 129(1)(c), 130(1)(c), "the period ... has expired"**: Ofcom may act only after the last day of the period.
- **s 365A(2), "of or above a specified age ... at or before the end of the month in which the licence is issued"**: age on the last day of the month of issue; a person attains an age on the anniversary of birth (29 February: 28 February in a common year).
- **s 366(4), "not ... at any time more than one month after the day on which the warrant was granted"**: entry is allowed up to and including the corresponding date one month after that day, or the last day of the month where there is none.
- **s 124U(2)(b)**: the proportion is the unexpired months ÷ the agreed months.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`ca03-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
