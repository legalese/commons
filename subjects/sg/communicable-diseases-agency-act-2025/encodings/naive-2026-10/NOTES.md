# Communicable Diseases Agency Act 2025 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive rows (the `writing-l4-rules` skill was not loadable in this
session). No pipeline, no coverage table, no independent test pass, no human gate.

**Edition:** the Act as enacted (No. 4 of 2025), informal consolidation, "version in
force from 1/4/2025", deposited at `../../registers/source-bundle/CDAA2025.txt`
(retrieved 1 October 2026). The deposit shows no amendment annotations. s 1 leaves
commencement to a Gazette notification; that the Act commenced on 1 April 2025 is an
inference from the consolidation date, not something the text says.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0163** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The honest answer is: very little. The Act creates the Agency and its board. This row
takes what a member of the public, a business, an Agency insider or a transferred
employee actually meets: the definition of "infectious disease" (s 2), the symbol and
name offences (ss 8, 9), secrecy (s 35), protection from liability (s 36),
compounding (s 44), the liability of company officers (s 45), when service takes
effect (s 47(5), (6)), who transferred to the Agency (ss 49, 51 and the Schedule),
and the membership rules (ss 10, 12(2), 19, 21(1)(g), 25).

Not encoded: functions and powers (ss 5, 6) beyond s 5(4), ministerial directions
(s 7), appointment mechanics (ss 11, 13-18, 20, 22), meeting procedure beyond the
quorum (ss 23, 24, 26-28), committees and delegation (ss 29-32), the Chief Executive
and staff (ss 33, 34), finance (ss 37-43), unincorporated associations (s 46, which
mirrors s 45), regulations (s 48), transfer of assets and records (ss 50, 53),
employment continuity beyond the transfer (s 52), and ss 54, 55.

## What the Act turns out to say

### 1. The Agency gets no power over the public from this Act

The functions in s 5(2) are advice, programmes, research, surveillance, education,
standards and international representation. s 5(4) says nothing in s 5 imposes a duty
"enforceable by proceedings before any court". No section lets the Agency order a
person or business to do anything. The powers that touch a patient (isolation,
notification, closure) are not here; s 54(4) only replaces "the Board" with the
Agency in ss 48(2)(b)(i), 49, 50(4) and 63(1) of the Infectious Diseases Act 1976.
Which "Board" that was is not said in this deposit. Not asserted (a negative finding
about the whole text).

### 2. Using the name "CDA" in business is a crime, with no permission route

s 9(2) forbids anyone but the Agency to use its name, the acronym CDA, or anything
"likely to be mistaken for it", in a business, a firm's name, or for goods and
services: $10,000 or 6 months or both (s 9(3)). Unlike s 8, there is no "prior
written permission" exception. Asserted.

### 3. Permission covers an identical symbol, not a confusing one

s 8(2)(a) makes the Agency's "prior written permission" a defence to using an
identical symbol. s 8(2)(b), using a symbol that "so resembles" it as to be likely
to deceive or confuse, carries no such words. Read literally, permission saves the
copy but not the near-copy. This is a literal reading. Asserted.

### 4. The secrecy offence has a smaller fine but a longer prison term

Disclosing Agency information (s 35(2)): $2,000 or 12 months. Misusing the symbol or
name (ss 8, 9): $10,000 or 6 months. Compounding is capped at the lower of half the
maximum fine and $2,000 (s 44(1)), so $2,000 for ss 8 and 9 and $1,000 for s 35 —
if the offence is prescribed as compoundable, which this row did not check. Asserted.

### 5. A director can be guilty without knowing

s 45(2)(b)(iii): an officer or manager who "knew or ought reasonably to have known"
of the company's offence and "failed to take all reasonable steps" to stop it is
guilty of the same offence, whether or not the company is convicted (s 45(5)). A
junior employee with no management influence is outside s 45(2). Asserted.

### 6. Transferred staff lose nothing, and gain no payout

Staff of five named units (two HPB branches; two MOH divisions and the "Interim
Communicable Diseases Agency") moved to the Agency on terms "no less favourable"
(s 51(1)(b)). The move is not a retrenchment, gives no compensation, and s 18A of the
Employment Act 1968 does not apply (s 51(3), (5)). The encoding compares monthly
salary only, as a stand-in for "terms". Asserted.

### 7. Good faith is not enough for immunity

s 36 protects members, officers, delegates and those acting under the Agency's
direction only for acts done "in good faith and with reasonable care", and only for
functions and powers "under this Act". Asserted.

### 8. One-third of a board of 10 is four

The quorum is the higher of one-third of the members and 3 (s 25(1)). With 10
members, 3 present is not a quorum. Asserted.

## What would need doing before this is worth anything

- The regulations under s 44 (which offences are compoundable) and s 48 were not
  retrieved.
- The Infectious Diseases Act 1976 provisions touched by s 54(4) were not read; that
  is where the Agency's real reach over the public would be found.
- Whether the Agency's symbol has been selected or published was not checked.
- s 52 (continuity, accrued leave, disciplinary carry-over) and s 46 are left out.
- No case law was searched.
