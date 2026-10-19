# Encoding brief: the Transferred Officers' Allowances Act 1948 (Cth), in L4

## The subject

**Transferred Officers' Allowances Act 1948** (Act No. 20, 1948, as amended to Act No. 20, 1956), Commonwealth of Australia, deposited at `../registers/source-bundle/C1948A00020.txt` (CC BY 4.0).

## Seat

**The transferred officer, or the widow** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level: *"What allowances are payable to me on my pension or retiring allowance, at a given date?"* Sections 4-7, as amended. The text gives the rates as amended by the 1954 Act (in force from 31 October 1953) and the 1956 Act (from 12 November 1955); earlier rates are not in the text, so a date before 31 October 1953 answers NOTHING.

- s 4: pension P below £360 a year: if P ≤ £288, P ÷ 4; if £288 < P < £360, enough to bring P to £360.
- s 5: if P ≤ £702: with S = P + the s 4 allowance, S ≤ £260 → S ÷ 5; £260 < S ≤ £650 → £52; P strictly between £650 and £702 → enough to bring P to £702.
- s 6 (from 12 November 1955 to 31 December 1956): on T = P + the s 4 and s 5 allowances: T ≤ £156 → £52; £156 < T ≤ £312 → T ÷ 6 + £26; £312 < T ≤ £448 → £78; £448 < T ≤ £500 → the greater of £52 and £526 − T; T > £500 → £52.
- s 7: a widow receiving a pension gets half the allowances her husband would get if alive and in receipt of a pension (the inputs give his pension).

## Inputs

The annual rate of the pension or retiring allowance (in pounds); the date; whether a widow.

## Rules that matter

- A failing assertion is a finding. Never edit an expected value to match the code.
