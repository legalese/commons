# Independent test report: Third Parties (Rights against Insurers) Act 2010

## Method

1. I read BRIEF.md and the source text (`../registers/source-bundle/ukpga-2010-10.txt`, PIT 4 January 2024) only.
2. I wrote `independent-expectations.md` (78 scenario rows across the three goals, with readings R1-R11 and the ambiguities) before opening any `.l4` file.
3. I then read `tprai-types.l4`, `tprai-transfer.l4`, `tprai-recovery.l4`, `tprai-information.l4` and `tprai-goal.l4` for names and record shapes. I did not read `tprai-tests.l4`.
4. I wrote `tests-independent.l4`, which imports prelude, daydate and the five modules. No expected value was changed after the encoding was read.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 0 | 97 | 0 |
| all 7 modules | 0 | 147 | 0 |

- 97 assertions: 34 for transfer, 32 for recovery and s 9, 17 for Sch 1, and 14 for the top-level goal (3 composite cases).
- Zero non-assertion errors.
- Liveness check: I appended two deliberately wrong assertions to a temporary copy. Both failed, so the assertions are really evaluated. The copy was deleted.

## Failures

None. Every scenario the encoding's inputs can express gave the value I derived from the Act. That includes:

- same-day ordering (route (a));
- the (b)-only events on the same day and the day after (DRO, NI DRO, died insolvent);
- s 6(5)-(6), s 6A(2)-(3), s 15 and Sch 3 para 3;
- s 8 with s 10;
- s 14(6)(a)/(b) with the FSCS gate in (7)(a) and the payment in (7)(b);
- s 9(3)-(6), including the notify-a-claim carve-out and marine property damage;
- the 28-day ends across month end, year end, 29 Feb 2028 and a weekend.

## Scenarios I could not express (not tested)

These rows in the expectations file have no matching input in the encoding:

- **T17 vs T18.** These are not distinguished. An LLP and an unincorporated non-partnership body are both `dissolved FALSE FALSE`.
- **R14-R18, the method of establishment.** `the liability is established` is a single boolean. The s 1(4) test "existence and amount", and the four methods, are left to the user.
- **I4, I14, I15, I16, I21.** Para 1(2)'s four beliefs and para 3(1)'s three conditions are each folded into one boolean. The encoding therefore does not itself apply:
  - the partnership exclusion in para 3(1)(b)(ii);
  - the rule that a restored body still counts as dissolved (para 3(6)(b)).
- **Ambiguity 3 (s 9(6), "to the extent").** A marine liability that is partly personal injury cannot be expressed; the encoding's input is all-or-nothing.

## Remarks on the encoding

1. **It is faithful and compact.** Every rule I could test agrees with the Act's words. The same-day and (b)-only logic is done correctly: `route (a) applies to` uses AT MOST, and a DRO or a death fails on route (a).
2. **The s 6A / s 9(8) asymmetry is handled correctly.**
   - For transfer, a restored body is not a relevant person (s 6A(2)), and `dissolved` carries a restoration flag.
   - For s 9(3), `Insured kind` has no restoration flag, so dissolution counts even after restoration (s 9(8)(b)).
3. **The FSCS treatment nets the payment against the insolvency shortfall, with a floor of 0** (`shortfall - FSCS paid`).
   - This equals my reading (net amount, less shortfall, plus FSCS payment) whenever the payment is no more than the shortfall.
   - It differs only if the FSCS amount exceeds the insurer-insolvency shortfall. This is arguably impossible in practice, so I did not test it.
4. **Coarse booleans move legal judgement to the user.** This affects:
   - `the liability is established` (s 1(4));
   - `proceedings started against a dissolved body's insurer` (para 3(1)(a)-(c) plus 3(6));
   - `the recipient is within para 3(2)`;
   - the para 1(2) beliefs.

   This is within the brief. However, para 3 has a trap the encoding does not show: the partnership exclusion and "dissolved even if restored". It would be safer to split these out, or to name them in the `@desc`.
5. **Not modelled, and plausibly worth a line in NOTES.md:**
   - s 21(4): Sch 1 paras 3-4 do not extend to Scotland, and there is no jurisdiction input;
   - the re-transfer on recall or reduction of a sequestration (ss 4(5), 6(7), 7(2));
   - Sch 3 para 2(7), which limits deemed relevant persons to the contract in force at the event;
   - s 9(3)'s causal words "cannot be fulfilled because". The encoding treats the insured's status as conclusive.
6. **No `REFUSE` is used anywhere.** The brief asks for `REFUSE` where the source does not answer. The case most likely to need one is a partly-PI marine liability under s 9(6), but the boolean input cannot express it.
7. **The top-level goal is sensible.** When nothing transfers, it returns 0 from the insurer and the whole liability against the insured. "May enforce" requires both transfer and establishment.

## Change after the pass (encoder)

No assertion failed, so the encoding was not changed. The remarks are recorded in NOTES.md as known limits:
- single flags for s 1(4) and for the beliefs in Sch 1 para 1 and para 3;
- no jurisdiction input for s 21(4);
- no re-transfer on recall of a sequestration;
- the insured's status is treated as conclusive under s 9(3).
