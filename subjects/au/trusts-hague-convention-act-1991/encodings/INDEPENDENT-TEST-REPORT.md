# Independent test report: Trusts (Hague Convention) Act 1991

Expectations: `independent-expectations.md` (17 scenarios, written from BRIEF.md and the source before any L4 was read).
Tests: `tests-independent.l4` (27 assertions against `the trust position for`).

## Result

`L4=~/.local/bin/l4 ./check.sh .` : tests-independent.l4 — **25 satisfied, 2 failed**, no other errors.

## Disagreements

### 1. Article 18 (public policy): encoding says JUST FALSE, I expected NOTHING (scenario 16) — confidence: medium
Art 18: "The provisions of the Convention **may be** disregarded when their application would be manifestly incompatible with public policy." This is permissive, parallel in effect to Art 13 ("No State shall be bound to recognize"): the forum is released from the obligation but not forbidden to recognise. The brief's rule is that where the Convention leaves the answer to the forum the answer is NOTHING; Art 18 leaves it to the forum just as Art 13 does. The encoding returns JUST FALSE ("must not / need not be recognised" collapsed into FALSE), and its own comment reads "may be disregarded ... FALSE". If the output is read strictly as "must it be recognised?" then FALSE ("no, there is no obligation") is defensible, but then Art 13 should be FALSE too for consistency; the encoding treats two permissive releases differently. The weaker assertion (not JUST TRUE) is satisfied.

### 2. Recognition when the Convention does not apply: encoding NOTHING, I expected JUST FALSE (scenario 2) — confidence: low (representation)
For an oral trust (Art 3) the Convention imposes no recognition obligation. I recorded "not required to be recognised under it" = FALSE; the encoding returns NOTHING (no answer from the Convention). Both are readable; NOTHING arguably conflates "the Convention does not reach this trust" with "the Convention leaves it to the forum" (Art 13), which the brief reserves NOTHING for. Flagged as a design choice for review, not a legal error.

## Agreements (all satisfied)
Baseline applies / chosen law / recognised; each of the four Article 2 limbs failing (control, separate fund, title, accountable duty); Art 3 voluntary and writing limbs; s 7(1) purely intra-Australian conflict; Art 7 with no choice; Art 6 third para ineffective choice falling back to the closest law; Art 5 non-application when the governing law (chosen-and-effective or closest) lacks trusts; chosen law governs even where the closest law lacks trusts; Art 11 not created in accordance -> FALSE; Art 13 -> NOTHING; combined ineffective choice + not in accordance.

## Coverage gaps
- Art 2 last paragraph (settlor's reserved powers, trustee-beneficiary) has no input; correct by default (it only says these are "not necessarily inconsistent").
- Art 5 "to the extent that": the Convention's partial non-application is modelled as all-or-nothing.
- When the Convention does not apply, `my trust is governed by` is NOTHING; I did not assert this.
- Arts 13 and 18 together, and Art 13 with not-in-accordance, are not separately tested (precedence among the recognition branches is unasserted beyond the cases above).

## Change after the pass (encoder)

- Article 18 now gives NOTHING, as the tester read it.
- One disagreement is left open: a trust outside the Convention stays NOTHING (`tests-independent.l4` line 18 is expected to fail).
- The gaps are recorded as known limits in NOTES.md.
