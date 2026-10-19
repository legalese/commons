# Work Injury Compensation Act 2019 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`: where the
encoding cannot answer it says so with an explicit value (`NOTHING` from a table
lookup, `only if the Commissioner directs ...`, or a fact the caller states). No
pipeline, no coverage table, no independent test pass, no human gate. It is not
for public use as advice.

This encoding replaces the encoding moved to `solutions/Litigate.4` on
19 October 2026 and the first-pass encoding `naive-2026-10`. It covers everything
the first pass covered (s 7, ss 8 to 10, s 13, s 16 with paragraph 5, s 24,
s 34B, First Schedule paragraphs 1 to 3 and Tables A and B) and adds s 3 with the
Third Schedule, s 4(5), s 12, the s 10(3) time bars, s 13(5), s 23(1), s 25(4),
s 35(4) to (7), s 63(1) and First Schedule paragraph 4. The first pass's
hand-checked figures for death, total and partial incapacity and medical
treatment were re-derived from the text and reused where still right; one of its
findings is withdrawn (finding 2 below).

**Edition:** 2020 Revised Edition, informal consolidation, version in force from
1 December 2025, as deposited at `../../registers/source-bundle/WICA2019.txt`. It
carries the S 694/2025 figures, in force 1 November 2025, and the Act 30 of 2024
amendments. Tables A and B are taken from
`../../registers/source-bundle/WICA2019.first-schedule-tables.txt`, deposited
beside the main text.

**Checks:** with the stable `l4` of VS Code extension 1.6.98,
`l4 run wica-cases-liability.l4` (37 assertions) and
`l4 run wica-cases-compensation.l4` (23 assertions): 60 assertions satisfied,
0 errors, 0 warnings. Both modules also run clean on their own.

| file | what it holds |
|---|---|
| `wica-liability.l4` | s 3 and Third Schedule, ss 7 to 10, 12, 13, 23(1), 24, 25(4), 35(4) to (7), 63(1), 34B(a) |
| `wica-compensation.l4` | s 4(5), Tables A and B as data, First Schedule paragraphs 1 to 5, s 16(1) |
| `wica-cases-liability.l4`, `wica-cases-compensation.l4` | generated fixtures, hand-written expected values |

## Seat

**The injured employee.** The Act is written to and about employers, insurers
and the Commissioner, but every right in it lands on the employee: whether I am
covered, whether my employer must pay, how much, what I lose by suing, and when
my claim lapses. Every decision is named as that employee would ask it
(`Must my employer pay me compensation`, `What am I paid for this day off work`,
`Is my claim deemed withdrawn`) and every input is a fact the employee could
state. Death compensation is asked on the employee's behalf
(`What lump sum is payable for my death`); the family is not a separate seat.
The s 34B(a) map is asked from the seat of a platform worker, the one place the
Act's individual changes.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.**
  Followed. The S 694/2025 figures are in the consolidation itself. The
  instrument that is used and *not* deposited — the regulations prescribing the
  excluded classes for s 24(2)(a) — is an input, said so where used. The Second
  Schedule is part of the Act but is not encoded; whether a disease is listed
  for an occupation is a fact the employee states.
- **The actors the text names.** Followed: employer, principal, contractor,
  Commissioner, court, health professional, approved medical institution.
- **A judgment handed to someone else, answered conditionally.** Followed. The
  s 3(3) saving of an illegal contract, the s 13(1) direction to a principal,
  the s 16(1)(b) opinion on treatment abroad and the s 35(6) later period are
  each an input naming who decides; s 13 returns
  `only if the Commissioner directs the principal to pay me` rather than a yes
  or no.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Followed for "employee" (s 3 with the Third Schedule), the s 7(4)
  presumption, s 8's deemed accidents and s 4(5)'s partial and total incapacity.
  "Contract of service", "drug" (defined by reference to two other Acts) and
  "approved medical institution" are asked as facts. **Departed from for AME**:
  average monthly earnings is the Act's own term, but its computation in First
  Schedule paragraph 6 runs to six sub-paragraphs with several Commissioner
  discretions, and is left as an input.
- **One case is the text's natural unit.** One accident (`My accident`), one
  disease, one day off work, one course of medical treatment.
- **The Act's own terms, each with a plain gloss.** Followed: "AME", "C",
  "in the course of", "limitation period", "replaced section" are used as the
  Act uses them and glossed in comments.
- **The operative sections in scope; the machinery out.** Followed in kind but
  not in full: the Act is about 344,000 characters, so the scope is the
  provisions an injured employee meets first (see below). Appointments,
  regulation-making, the Commissioner's processing powers and commencement are
  out.

## Why this scope

An injured employee asks, in order: am I covered; was this a work accident; is
it excluded; who pays; how much for my days off, my treatment and any lasting
incapacity; and what could make me lose the claim. Those questions are ss 3, 4,
7 to 10, 12, 13, 16, 23, 35 and 63 and First Schedule paragraphs 1 to 5. ss 24
and 25(4) are in because they are what the employee can check about the
employer's insurance and pay slip. The insurance Parts beyond that, the claims
procedure after notice (ss 36 to 62), s 63(2) to (8), s 64, Part 3A beyond the
s 34B(a) map, the Fifth Schedule and the offences other than s 25(4) are left
out.

## What the Act turns out to say

1. **The quarter for total incapacity is added after the cap, so the most
   payable is a quarter more than the cap.** Paragraph 2 clamps C to $116,000
   and $346,000 (accidents on or after 1 November 2025) and then pays
   C + 0.25C. At or above the cap an employee receives $432,500, and $361,250
   for an accident before that date. Asserted.

2. **There is no "partial incapacity at 100%". The first pass's second finding
   is withdrawn.** The first pass asserted that an employee assessed at 100%
   loss of earning capacity under paragraph 3 receives C, a quarter less than
   total incapacity. But s 4(5) defines partial incapacity as an aggregate
   percentage "less than 100%" and total incapacity as "100% or more". At 100%
   paragraph 2 applies and the employee receives C + 0.25C; at 99% paragraph 3
   pays 0.99C. The step at 100% is real (from 142,560 to 180,000 on a C of
   144,000), but it falls between two definitions, not inside one paragraph.
   Asserted. *Inference, not asserted:* because an aggregate of 100% or more is
   total incapacity, the paragraph 3(2) cap on aggregated injuries ("not so as to
   exceed ... permanent total incapacity") appears never to bite.

3. **Breaking up a fight is excused only on the employer's instruction or with
   its consent.** s 7(2)(c)(ii) as deposited ends "under any instruction or with
   the consent, whether express or implied, of the employee's employer", printed
   after limb (B) on a line labelled "(ii)". Read as qualifying the whole limb,
   an employee who breaks up a fight on their own initiative and is hurt is
   barred, unless they struck no one. The first pass did not have this
   condition. Asserted; the reading of the stray label is an inference not
   checked against the PDF.

4. **The public bus is excluded however the employer arranged it.** s 8(1)
   requires transport operated by or for the employer *and* "not operated in the
   ordinary course of a public transport service". Asserted.

5. **Disobedience does not defeat a claim; acting for oneself does.** s 8(3)
   saves an accident while acting against orders or without instructions, if the
   act was "for the purposes of and in connection with the employer's trade or
   business". Asserted both ways.

6. **The open-ended disease limb is limited to chemical and biological agents,
   and has a one-year tail.** s 10(1)(c) covers an unlisted disease only if
   "directly attributable to an exposure to a chemical or biological agent";
   s 10(3)(b) then bars it if incapacity begins more than a year after exposure
   ends, unless (s 10(4)) it is a death after compensable incapacity. A disease
   from noise is outside unless the Second Schedule lists it, or s 12 applies.
   Asserted.

7. **The principal owes nothing until the Commissioner directs it, and only for
   accidents at its site.** s 13(1) says the Commissioner "may direct"; s 13(5)
   confines the section to a place where the principal undertook the work or
   which it controls. Asserted as three outcomes.

8. **A claim lapses if the employer has no notice within a year, and suing for
   damages forfeits the extension.** s 35(5) deems the claim withdrawn; the
   Commissioner may extend under s 35(6) but "must not" under s 35(7) where the
   delay was caused by an action for damages. Asserted.

9. **Medical treatment has two ceilings and the one-year window bites first.**
   Paragraph 5 pays the lower of the cost within a year of the accident and
   $53,000 ($45,000 before 1 November 2025). $2,000 inside the year and $40,000
   after it recovers $2,000. Asserted.

10. **Temporary incapacity is a rate, not a sum, and the Act gives no daily
    divisor.** Paragraph 4 pays "based on" AME, a monthly figure: full AME for
    the first 60 days in hospital and the first 14 days of medical leave and
    light duties, two-thirds after. A day certified as needing hospital but not
    spent there counts as hospital (para 4(4)). The encoding answers with the
    rate and reads the 14 days as one count shared by medical leave and light
    duties. Asserted.

11. **The deposited main text misreads both tables at page breaks, in two
    different ways.** In Table A the age 32 is printed with no factor and every
    later factor on that page sits one row low (so 40 shows 110, not 108). In
    Table B the row for age 40 is missing altogether and 144 is printed against
    41. The encoding uses the tables deposited separately; the row the main text
    loses is asserted (Table A at 32 is 121, Table B at 40 is 144).

12. **The s 34B(a) table is also misaligned in the deposit, but can be read from
    the deposit itself.** The first row "(i) 7" has nothing beside it and "34N"
    stands alone at the foot. Read against the headings of ss 34D to 34N, s 7 is
    replaced by 34D and s 8 by 34F. Asserted for those two rows.

## What would need doing before this is worth anything

- AME (First Schedule paragraph 6) and the Fourth Schedule percentages, so that a
  figure can be computed from facts rather than supplied.
- The Second Schedule's occupations, diseases and limitation periods, and s 11 on
  the date of accident for a disease. Tables crossing page breaks in this deposit
  must be checked against the PDF.
- The claims procedure from s 36, s 63(2) to (8) on when an employee may still sue,
  and s 64.
- Part 3A and the Fifth Schedule for platform workers, beyond the s 34B(a) map.
- The reading of s 7(2)(c)(ii) checked against the PDF.
- No case law was searched, and no human gate has been sought.
