# Criminal Injuries Compensation Act 2003 (WA) — baseline encoding, the victim's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18, the rulings on negatives of 2026-11-04 and 2026-11-05, and the `writing-l4-rules` skill (with `references/regulative.md`).
There is no REFUSE in it; a question that reaches a gap answers `not covered` with a reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind compensation and other civil claims, with the focus "the provisions a claimant meets". The Act is of moderate size, so everything a claimant meets is encoded, and the machinery and the assessor's procedural powers are left out (listed below). There was no earlier encoding of this Act to keep. No ledger entry was open for it.

There are 17 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order: am I a close relative (s 4); can a claim be made and under which section (ss 8, 12–17); how do I apply and who may apply for me (s 11); by when (s 9); does the entitlement end on death (s 10 — arises only if the person entitled has died); what can be compensated (ss 6, 30); the most that can be awarded (ss 31–34); mental and nervous shock (s 35); what stops an award (ss 36–41); the most in interim payments (s 23(2)); how much I will be paid (ss 20(2)(d), 23(3), 31–34, 42, 43); when it can be paid (s 47 — arises only once an award is made); can I appeal and by when (s 55); will I be given the decision and reasons (ss 26, 27); by when must I ask for future treatment money (s 48 — arises only if the award includes it); what I may have to pay back (ss 23(4), 68); what I face if accused of an offence under the Act (ss 19(5), 63(5), 64(5), 70, 71 — arises only if accused).

**Regulative rules.** `s 9 -- apply within 3 years, or an assessor may allow it later`: `PARTY I, the applicant DO make the compensation application WITHIN <days in the 3 years> HENCE FULFILLED LEST PARTY an assessor MAY allow the application to be made after the 3 years`. `s 55 -- appeal within 21 days, or the District Court may allow it later`: the same shape, with `WITHIN 21`. `DO`, not `MUST`: missing either period is not a wrong; it hands the question to an assessor (s 9(2)) or to the District Court (s 55(4)). The seat questions take plain facts (dates); the rules are asserted in the case file through `CONSIDER EVALTRACE ... WHEN FULFILLED` (applying on day 1095 of 1095: fulfilled; day 1096: not; day 1096 and then an assessor allowing it: fulfilled; the same three for the appeal on days 21, 22 and 22 + leave), and one residual of each is `#TRACE`d with an `-- expect:` line.

Date arithmetic is kept in one small module, `cica-dates.l4`, the only one that imports `daydate`.

## Edition

The compilation on the Western Australian Legislation website (law_a6998, mrdoc_47649), retrieved 7 September 2026, whose compilation table ends with the Criminal Law (Mental Impairment) Act 2023 (No. 10 of 2023, in operation 1 September 2024), as deposited at `../../registers/source-bundle/mrdoc_47649.txt`.
The Act (other than ss 1 and 2) came into operation on 1 January 2004 (compilation table), which fixes item 6 of the s 31 Table. The Acts Amendment (Justice) Act 2008 Part 7, which includes the s 31 that s 48(2) counts from, came into operation on 31 July 2008 (compilation table).
**Regulations.** s 31(3) lets regulations add items to the Table, and s 6(1)(g) lets them prescribe further personal items. No regulation is deposited, and the compilation records no amendment of the Table, so the Table's last item ($75 000) is used. If regulations have added an item, the maxima for later offences (and the 3% interim cap) would change; a worn item other than those s 6(1)(a)–(f) list answers `not covered`.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `cica-dates.l4`, `cica-victim.l4` | `cica-cases-victim.l4` | 152 written, 152 satisfied; 2 traces, as their `-- expect:` lines say |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text. Edges asserted: an offence on 21 and on 22 January 1971 (s 8); the last day of the 3 years and the day after; an offence on 29 February (3 years end on 28 February); an accused found unfit for an offence on 31 December 1985 and on 1 January 1986 (s 15 or s 16); every boundary of the s 31 Table (each first and last day, item 1 indictable and simple); an application on 22 and on 23 September 2003 (ss 34, 35); a motor vehicle offence on 30 June and on 1 July 1993 (s 37); an award equal to the maximum and $1 over it; deductions larger than the award; a set-off larger than the debt; the last day of the 21 days and the day after; an award made the day before and on the 18th birthday (s 48); an award before, on and after 31 July 2008; the last day for a prosecution and the day after (s 71).

## Seat

**The victim**: the person injured by an offence; and, where the victim died, **the close relative** who suffered loss from the death (the application is made for that relative by the deceased's personal representative, ss 12(2)–17(3)). "I was assaulted. Can I claim? By when? What is the most I can get? Will my insurance payout be taken off? Can I appeal?" A personal representative who is also a close relative asks the same questions. The offender is not given a seat: what the Act does to the offender (Part 6 recovery) is not the claimant's matter, and a second seat was not asked for.

The 2026-10-18 defaults:

- **The Act alone.** The Acts it names (the Fatal Accidents Act 1959, the Family Court Act 1997, the Guardianship and Administration Act 1990, the Motor Vehicle (Third Party Insurance) Act 1943, the National Health Act 1953, the Sentencing Act 1995, the Young Offenders Act 1994, the Criminal Code) are named, not encoded; what they decide is asked as a fact ("a registered organisation" is glossed as a private health insurer; whether an amount is of the Fatal Accidents Act s 5(2)(b) or (c) kind is asked).
- **The actors the text names:** the victim, the close relative, the personal representative, the applicant, an assessor, the Chief Assessor, the CEO, the District Court.
- **Judgments handed to others are answered conditionally:** every "if the assessor is satisfied", "is of the opinion", "thinks it is just" and "thinks fit" is an input (related offences, s 33(1); s 36; s 37's causation; s 38; s 39's separate offence; s 41's refusal; the amount the assessor is satisfied is just, s 30; the deduction for what will be received, s 42(4); the set-off, s 43). s 13(5), 15(5), 16(5), 17(5) (an offender not criminally responsible) sit inside the assessor's satisfaction that the offence was committed, so they are not separately asked.
- **The Act's own definitions are worked out from facts:** "close relative" (s 4(1)); "loss" and "personal item" (s 6); "injury" (s 3) through its three parts; "proved" and "alleged offence" through what happened in the criminal case; "convicted" (s 5) as a gloss on that choice. "De facto partner", "crime", "indictable offence", "simple offence", "represented person" and "motor vehicle" are borrowed and asked.
- **One case:** one application, for one offence or one set of offences.
- **The Act's own terms**, quoted in the comment above each rule, and glossed in the `@desc` lines.
- **Machinery out:** listed below.

## Scope

**In:** s 3 (as the definitions are used); s 4(1) (s 4(2) borrowed); s 5 (as a gloss); s 6; s 8; s 9(1), (2); s 10; s 11; ss 12–17; s 20(2)(d); s 23(2)–(4); ss 26, 27; s 30 (the just amount as an input); ss 31–34; s 35; ss 36–41; s 42(2)–(5); s 43; s 47; s 48(1), (2); s 55(1), (3), (4) and s 57; s 68 (with (1A)); ss 19(5), 63(5), 64(5) (the natural person's penalty), 70(2), (3), 71.

**Out, and why:**
- ss 1, 2, 7, 8A, Part 8 (ss 59–62), s 72, s 73, Schedules 1 and 2 — machinery, administration and transitional provisions.
- ss 18, 19(1)–(4), 20(1), (2)(a)–(c), (3), 21, 22, 24, 25, 62A, 63(1)–(4), (6)–(8), 64(1)–(4) — the assessor's procedural powers (to inquire, require examinations, require other proceedings, stay, hold hearings, restrict publication). They govern how and when the application is decided, not what the claimant is entitled to. s 20(2)(d) (the examination cost comes off the award) is in; s 20(3) (reduction for not attending) is folded into the amount the assessor is satisfied is just.
- s 28 (a copy to the CEO), s 29 (the general discretion; asked through the just amount), s 44 (payment to the person who paid expenses), s 45 and Part 6 (recovery from the offender), ss 46, 54, 69 (the Consolidated Account and debt recovery), ss 56–58 (the Court's powers on appeal; referral of questions of law), ss 65, 66 (immunities). s 67 (an assessor cannot award costs) is noted here and not encoded.
- s 23(1) (when an interim payment is warranted) — an assessor's satisfaction; only the cap and its consequences are encoded.
- s 64(5)(b) — the body corporate penalty; not this seat.

## Fork register (questions with no convention, decided case by case)

The 2026-11-04 and 2026-11-05 rulings were followed in choosing between "no" and `not covered`:

- s 8 for an offence before 22 January 1971: "no" (a flat negative, "does not apply").
- s 4(1) for a relationship it does not list (brother, sister, aunt, fiancé): "no" (an "is a person who ... was" definition, read as "means"). The other reading: `not covered`, since s 4(1) says "a close relative ... is", not "means".
- s 4(1) when the relationship began after the offence: "no" ("immediately before the offence was committed").
- ss 12(1)–17(2) for a person who suffered no injury: `not covered` (a grant limited in its own wording). The other reading: "no", since no section gives such a person a route.
- ss 12(2)–17(3) when no close relative suffered loss: "no" (an "if").
- s 13(2)(b), (3)(c) without the claim that someone else did it: "no" (an "if").
- A charge still undecided: `not covered` (none of ss 12–17 yet applies; the text is silent until it ends).
- s 15 for an accused found unfit for an offence before 1 January 1986: taken under s 16 (the accused is "for any other reason ... not brought to trial", s 16(1)(e), and s 15 "does not apply", s 16(1)(g)). The other reading: the Act gives no route, because s 16 is about charges not determined and a finding of unfitness is a determination of a kind.
- s 16(1)(f) when the person has been charged again or tried: `not covered` (the route depends on that charge).
- s 6(2) for property that is not a personal item worn when injured: "no" (a "means" definition). s 6(1)(g) for an item not in (a)–(f): `not covered` (the list is closed only by regulations that are not deposited).
- s 34 for an application before 23 September 2003: `not covered` (a scope limit with no "only").
- s 35(1) for an application before 23 September 2003: "section 35 does not stand in the way" (the section does not apply). s 35(2) when no link is met: "no" ("must not ... unless").
- s 55(1) for decisions other than making, refusing, or the amount of, an award: `not covered` (a grant limited in its own wording).
- ss 31–34 and s 42, 43: **the maximum is applied first, and the deductions are taken from the capped award.** s 42 says "deduct from a compensation award", and the award is what ss 31–34 cap. The other reading: the assessor assesses the full loss, makes the deductions, and then caps what is left, which would pay more where the just amount is above the maximum. Asserted: $100 000 just, $12 250 of deductions, $62 750 paid.
- s 42(2) and (3) can describe the same insurer's money (entitled to, then received). The input for (2) asks for what is not yet received, so it is not counted twice.
- s 43: the set-off is the assessor's choice, capped at what is owed and at what remains payable.
- s 47 "until the period ... has elapsed": payment may be made from the day after the 21st day.
- s 48(2)(a)(i) "before the victim reaches 28 years of age": by the day before the 28th birthday. (a)(ii) and (b)(i), "the expiry of 10 years after" 31 July 2008: by 31 July 2018. "Under 18 years of age on the date of the award": an award on the 18th birthday is not under 18.
- s 9(1) "within 3 years after the date", s 55(3) "within 21 days after the date", s 71 "within 2 years after the date": the period starts the day after and ends on the anniversary (or the 21st day); the Interpretation Act 1984 rules on time are not encoded (for example a last day on which the office is closed).
- s 23(2) "the maximum amount ... if the application were for compensation in relation to a single offence": taken as the s 31 Table maximum for the date of the offence (the last, if several).

## What the Act turns out to say

1. **Brothers and sisters are not close relatives.** s 4(1) lists parents, grandparents, stepparents, spouses, de facto partners, children, grandchildren and stepchildren only, and only if the relationship existed immediately before the offence. The Fatal Accidents Act 1959, to which s 6(3) points for the loss on a death, does count brothers and sisters. A sister of a person killed is not a close relative here, so no claim can be made for her loss, and s 35(2)(e) cannot help her even if she lived with the victim. Asserted.
2. **The 3 years run from the offence, with no extension for a child.** s 9 has no exception for a victim who was a child, or who did not know of the injury; only an assessor's discretion (s 9(2)) can let a late application in. Asserted (an offence in 2010, an application in 2026: late).
3. **An accused found unfit for an offence before 1986 falls to s 16.** s 15 is limited to offences "alleged to have been committed on or after 1 January 1986"; s 16(1)(e) and (g) then catch the case as one "not brought to trial" where s 15 "does not apply". Asserted (fork above).
4. **ss 34 and 35 date from 23 September 2003, before the Act itself came into operation (1 January 2004).** Applications made under the 1985 Act in those months and still pending at commencement were then dealt with under this Act (Schedule 2 cl 3(3)), so the limits reach them. Asserted at both edges.
5. **Most property is not compensated.** Loss means expenses, future treatment, lost earnings, and damage to a "personal item" the victim was wearing when injured (s 6(2)). A phone in a bag, stolen cash or a damaged car is not loss; a watch or jewellery worn at the time counts only if regulations prescribe it (s 6(1)(g)), and none is deposited. Asserted.
6. **s 42(5) shields only a personal representative's application, and only from subsections (3) and (4).** Life insurance or superannuation paid on a death is not deducted from an award for a close relative's loss, but the same kind of money received by an injured victim is (and s 42(2), private health insurance, is still deducted on a death). Asserted.
7. **The maxima have not moved since 2004.** The Table's last item is $75 000 for offences from 1 January 2004; s 31(3) lets regulations add items, and the compilation records none. Interim payments are capped at 3% of it, $2 250, not counting a funeral (s 23(2)).
8. **The cap is per person, not per application, except on a death.** s 31(1) caps the aggregate "in favour of one person"; s 31(2) caps the aggregate "on a compensation application made by the personal representative", however many close relatives share it. Encoded as one maximum; a personal representative claiming for several relatives meets the s 31(2) aggregate.
9. **A refused award turns interim payments into a debt** (s 23(4)), and money later recovered elsewhere for the same injury, not deducted and not reduced for the award, is a debt up to the award (s 68). Asserted.
10. **The appeal to the District Court is final** (s 57), and an assessor cannot award costs (s 67).
11. **Future treatment money must be asked for in time** (s 48): 10 years from the award for an adult, and for a child until the day before turning 28 (or 31 July 2018 if later). Unclaimed in time, it is not paid. Asserted.
12. **The deposited text loses the dashes in "crossexamine" and "reexamine"** (ss 25(2)(c), 51(3)(d)); conversion, not law. Nothing turns on it.

## Raised in the ledger

Nothing. No ledger entry named this Act, and no scenario life cites it.

## What would need doing before this is worth relying on

- **The Criminal Injuries Compensation Regulations**, for any items added to the s 31 Table and any personal items prescribed under s 6(1)(g), and for the District Court's scale of costs (s 56(2)(d)).
- **The Fatal Accidents Act 1959** encoding (`subjects/au/wa/fatal-accidents-act-1959/encodings/baseline-2026-11/`), for what counts as a close relative's loss on a death (s 6(3)) and the amounts s 42(5) protects. Linked here in words only; the stable `l4` cannot import across subjects.
- **The Interpretation Act 1984** rules on reckoning time and its definition of de facto partner.
- **Case law** on "related" offences (s 33), "relationship or connection" (s 36), what a victim "ought reasonably to have done" (s 38), and on the assessment of compensation. None was read.
- An independent test pass and a human review.
