# Military Rehabilitation and Compensation (Consequential and Transitional Provisions) Act 2004 — baseline encoding, the injured member's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill (a regulative rule for the duty the Act puts on the Commission).
There is no REFUSE in it; a claim finally determined before 1 July 2026 answers `not covered` (the rules then in force are not in the deposit), and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0109` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep.

There are 7 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings: which Act governs my claim; old impairment points; double compensation (impairment, then incapacity); DRCA incapacity payments moving across; treatment; Special Rate Disability Pension offsets.

**Regulative rule.** One duty is written as a rule: `s 13(2), (3) -- the Commission must determine my old condition's points and count them towards my total`, `PARTY the Commission MUST determine the old condition's impairment points using the s 67 guide, HENCE … SHANT determine my total impairment points without counting them … LEST BREACH … BECAUSE`. The seat question `Do my old impairment points count` reads the same conditions (an MRCA claim on or after `the date of commencement`, an old VEA or DRCA condition). The rule has no deadline (the Act gives none), so it is never `FULFILLED` by time; the case file traces it kept and breached, with `-- expect:` lines. The other provisions are entitlements and disentitlements ("is not entitled", "applies"), not duties on a party, and are written as decisions.

## Edition

The compilation registered as **C2026C00273** (Compilation No. 10, compilation date 1 July 2026, including amendments up to Act No. 31, 2026), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2004A01286.txt`.

This is the compilation after the **Veterans' Entitlements, Treatment and Support (Simplification and Harmonisation) Act 2025** (Act No. 17, 2025). In it, "date of commencement means 1 July 2026" (s 4(1)), and Part 2 (s 7) was substituted: the endnotes record Part 2 "rs No 17, 2025", s 7 "rs No 17, 2025", and ss 8–11 "rep No 17, 2025". The rules that sorted conditions straddling 1 July 2004 between the MRCA, the DRCA and the VEA before 1 July 2026 are therefore not in the deposit.

Nothing else is brought in. The DRCA's s 14AA and the VEA's s 12AA, which close those Acts to new claims and which ss 88 and 89 cite, are read from their deposits (`subjects/au/safety-rehabilitation-and-compensation-defence-related-claims-act-1988/registers/source-bundle/C1988A00156.txt` line 563; `subjects/au/veterans-entitlements-act-1986/registers/source-bundle/C2004A03268.txt` line 2862) and asked as facts, not encoded. The regulations converting DRCA lump sums to weekly amounts (s 14(2)) are not deposited; the converted amount is an input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `mrcct-member.l4` | `mrcct-cases-member.l4` | 33 written, 33 satisfied; 2 traces, each as its `-- expect:` line says |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text. The MRCA and VEA baselines' case files were re-run after the note added to their NOTES.md (below) and still pass unchanged.

## Seat

**The injured member**: a current or former member of the Australian Defence Force whose injury or disease began before 1 July 2004, straddles that date, or is already the subject of a DRCA or VEA claim, payment or pension. "My knee injury began in 2002 and later service made it worse. Which Act do I claim under? My VEA pension: does it stop an MRCA claim? My DRCA incapacity payments: do they carry on? Do my old impairment points count?"

The Act's provisions are addressed to the Commission or are statements of which Act applies. They are encoded as what they mean for the member. No question is asked from the seat of the Commission, the Department or the Board. Dependants (s 12(4)–(8), death and funeral compensation) would be a second seat; they are not written.

The 2026-10-18 defaults:

- **The Act alone.** The MRCA, DRCA and VEA provisions it names are named, not encoded; whether a claim falls under one of them is asked as a fact.
- **The actors the text names:** the person (member or former member), the Commission, the Commonwealth.
- **Judgments handed to others are answered conditionally:** whether a claim was "finally determined", the Commission's impairment determination, the regulations' conversion of lump sums. Each is an input.
- **The Act's own definitions are worked out from facts:** the date of commencement (s 4(1)); the transfer week's MRCA section by the member's category (s 92(3), (5)); the offset (s 14). "War-caused or defence-caused", "Permanent Forces member", "Reservist" are borrowed terms, asked as facts.
- **One case:** one member, one claim.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** Parts 4 to 6 on the Commission, the Board, the Repatriation Medical Authority and the Specialist Medical Review Council; the Schedules of amendments.

## Scope

**In:** s 4(1) (date of commencement); s 7(1)–(5); s 12(1)–(3), (9), (10); s 13(1)–(3); s 14; ss 88, 89, 92, 93, 110, 112 (as they decide which Act governs a pending claim); s 117.

**Out:** s 5 (the definition of "relates to defence service", which s 7 uses only to say service before or after the date does not matter); s 6; s 12(4)–(8) (dependants, funerals, medical expenses already paid); s 13(4); s 14A; ss 22–87; ss 90, 91, 94–109, 111, 113–116, 117A–125; Schedules 1–4. The former Part 2 (the rules before 1 July 2026) is not in the deposit.

## What the Act turns out to say

1. **From 1 July 2026 there is one Act for new claims, whenever the condition began.** "On and after the date of commencement, the MRCA applies to a person's injury, disease or death ... whether the injury is sustained ... before, on or after that date; and ... whether [it] relates to defence service rendered ... before, on or after that date" (s 7(1)), and the same for an aggravation or material contribution (s 7(2)). A knee injury from 2002, aggravated in 2010, claimed in November 2026, is the MRCA's. That is `REQ-0109`'s answer. Asserted (Jordan).
2. **The question `REQ-0109` asked — MRCA, DRCA or VEA for a condition straddling 1 July 2004 — is no longer answered by dates of injury.** The rules that did so (the former ss 7–11) were substituted or repealed by Act No. 17, 2025 and are not in this compilation. What decides the Act now is when the claim was made and whether it was still undecided on 1 July 2026. A claim finally determined before then answers `not covered`. Asserted.
3. **A claim pending on 1 July 2026 mostly stays where it was made.** A DRCA claim continues under the DRCA (s 88) and a VEA claim of a closed kind continues under the VEA (s 89), including reconsideration and review. The exceptions move to the MRCA: a pending DRCA incapacity claim (s 93), and a pending VEA prisoner of war claim or Part VII application (ss 110, 112). Asserted.
4. **DRCA incapacity payments in course on 30 June 2026 move to the MRCA without a claim** from the transfer week, the first week starting on or after 1 July 2026, under MRCA s 85, 86, 87 or 118 by the member's category, with the claim requirement omitted (s 92(3), Note 1). Earlier weeks stay under the old DRCA (s 92(2)). Hospital maintenance under old DRCA s 22 continues as it was (s 92(4)). Asserted.
5. **Old impairment counts.** For an MRCA claim made from 1 July 2026 by a person with a VEA war-caused or defence-caused, or a DRCA, condition, the Commission "must" determine that condition's impairment points with the MRCA's s 67 guide and count them towards the total (s 13(2), (3)). Asserted; the duty is traced.
6. **No double compensation, period by period.** No MRCA permanent impairment compensation for an impairment already compensated under DRCA s 24 or 25 (or the 1912, 1930 or 1971 Acts), or for which a VEA Part II or IV pension is being received (s 12(1)), though s 71 additional compensation for deterioration survives (Note). No MRCA incapacity payment for a period already paid under the DRCA or covered by a VEA pension (s 12(2)), but payments for other periods do not bar it (s 12(3)). A nil or negative payment still counts as received (s 12(10)). Asserted.
7. **Treatment follows the MRCA once it starts.** Becoming entitled to MRCA treatment for a service condition moves a separate VEA-treated condition to the MRCA as well, and VEA eligibility for it ends (s 117). Until then, VEA treatment for a condition and period excludes MRCA treatment for the same (s 12(9)). Asserted.
8. **The Special Rate Disability Pension maximum is reduced by half the fortnightly VEA pension and by DRCA lump sums converted to weekly amounts** (s 14). Asserted with the converted amount as an input.

## Raised in the ledger

Nothing new. A `rule-version` entry for the former Part 2 (the rules for claims decided before 1 July 2026) could be raised if a scenario asks about a claim decided then; it would need an earlier compilation deposited.

## Links, and the MRCA and VEA baselines

- **MRCA baseline** (`subjects/au/military-rehabilitation-and-compensation-act-2004/encodings/baseline-2026-10/`): its `Is it a service injury or disease` answers `not covered` for a condition from before 1 July 2004, with a reason naming "the transitional provisions, the DRCA or the VEA". For a claim made on or after 1 July 2026, this encoding's `Which Act governs my claim question` answers it: the MRCA (s 7). The MRCA baseline's code and tests are left as they are (IMPORT does not cross folders, and changing its answer changes its tests); a note in its NOTES.md now points here.
- **VEA baseline** (`subjects/au/veterans-entitlements-act-1986/encodings/baseline-2026-10/`): its s 12AA question says new Part II and Part IV claims go to the MRCA; ss 88, 89 here say what happens to claims pending at 1 July 2026. A note in its NOTES.md now points here.
- **DRCA**: deposited (`subjects/au/safety-rehabilitation-and-compensation-defence-related-claims-act-1988/`), not encoded.

## What would need doing before this is worth relying on

- **The former Part 2**, from an earlier compilation, for claims decided before 1 July 2026.
- **The DRCA**, and the MRCA's Chapter 4 and Part 6 (the Special Rate Disability Pension), which these answers lead into.
- **The dependants' seat**: s 12(4)–(8), death and funeral compensation, the education schemes (ss 111, 112).
- **The regulations** converting DRCA lump sums to weekly amounts (s 14(2), s 24(3)(b)).
- **Wider sources.** No DVA guidance, Board or Tribunal decision or case law was read.
- An independent test pass and a human review.
