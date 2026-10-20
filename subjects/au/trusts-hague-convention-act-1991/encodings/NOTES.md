# Trusts (Hague Convention) Act 1991 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the trust position for` (`th-rules.l4`). It answers:

- whether the Convention applies to my trust;
- which law governs it;
- whether it must be recognised as a trust.

The encoded provisions are ss 6-7 and Articles 2, 3, 5, 6, 7, 11, 13 and 18 of the Convention. The source is the compilation of 1 July 2016.

## Seat

The encoding is written from the seat of **the settlor, trustee or beneficiary of a trust**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Does the Convention apply to my trust; which law governs it; must it be recognised as a trust?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-5 | out of scope: machinery |
| s 6 | applied: the Convention has the force of law |
| s 7 | (1) encoded; (2) is out of scope |
| Article 1 | inert: scope statement |
| Article 2 | encoded |
| Article 3 | encoded |
| Article 4 | out of scope: preliminary issues of validity of wills and transfers |
| Article 5 | encoded |
| Articles 6-7 | encoded; the closest connection (Article 7's factors) is a finding |
| Articles 8-10 | out of scope: what the governing law governs |
| Article 11 | first paragraph encoded; the effects of recognition are out of scope |
| Article 12 | out of scope |
| Article 13 | encoded: no obligation, NOTHING |
| Articles 14-17 | out of scope |
| Article 18 | encoded |
| Articles 19-32 | out of scope: fiscal matters, reservations, final clauses |

## Forks (readings taken)

- **F1, Article 6.** A chosen law that does not provide for trusts of the category is ineffective, and Article 7 applies.
- **F2, Article 5.** The Convention does not apply where the law specified by Chapter II (after F1) does not provide for trusts of the category; the governing law is then not reported.
- **F3, Article 13.** "No State shall be bound to recognize": the forum may still recognise, so the answer is NOTHING, not FALSE.
- **F4, Article 11.** A trust not created in accordance with the governing law need not be recognised under the Convention: FALSE. Article 14 (more favourable rules) is out of scope.
- **F5, Article 18 (changed after the independent pass).** The Convention "may be disregarded" when manifestly incompatible with public policy; like Article 13, that leaves recognition to the court: NOTHING.
- **F6, outside the Convention.** Where the Convention does not apply, the Act does not say whether the trust must be recognised: NOTHING.
  - **Disagreement from the independent pass, left open.** The tester reads an oral trust as JUST FALSE (`tests-independent.l4` line 18); the encoding keeps NOTHING, since other law may still recognise it. The tester's confidence is low.
- **Known limits (from the independent pass).**
  - Article 5's "to the extent that" is all-or-nothing.
  - Which rule wins when Articles 13 and 18 both apply is not tested.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 42 assertions satisfied, 1 failed, 0 other errors — 16 the encoder's (`th-tests.l4`), 27 independent (`tests-independent.l4`). One assertion in `tests-independent.l4` (line 18) is expected to fail: it reads a trust outside the Convention as not to be recognised (F6).

## Open questions for an Australian lawyer

- **F3:** how do Australian courts exercise the Article 13 discretion?
