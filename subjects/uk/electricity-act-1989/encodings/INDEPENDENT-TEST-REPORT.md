# Independent test report: Electricity Act 1989 encoding

Files: `independent-expectations.md` (written from BRIEF.md and the source text before any
`.l4` file was read) and `tests-independent.l4` (imports prelude, daydate and the six
`ea89-*` modules other than `ea89-tests.l4`).

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 2 | 97 | 2 |
| ea89-tests.l4 (author's) | 0 | 101 | 0 |
| other modules | 0 | 0 | 0 |

99 independent assertions: 97 pass, 2 fail. The 2 errors are the 2 failed assertions; there
are no syntax or type errors. Both failures are deliberate dissents from the **brief's**
date convention. The encoding follows the brief faithfully on both.

Every other scenario agrees with the code: working days across Easter 2026 and 2027 (Good
Friday computed, Easter Monday from the list), Christmas 2026 with and without the bank
holiday list, weekends, the 4 May holiday; the day before, on and after each limit; the
para 2(3) 28 days across February in 2026 and the leap year 2028; s 23(1C) with 29 Feb
starts and ends; s 20(3) with whole 50p sums and whole quarters (including 31 Aug to 30 Nov);
s 27K 5 years, 3 months and 6 months with month-end clamping; s 27G(5) +7 across a leap day;
s 27M(2) +42; s 27M(5) suspension, including a late appeal that does not suspend; s 27N(1);
s 27O caps; s 44 excess, reduced maximum and interest; and the top-level goal.

## Failing assertions

### 1. C9g: s 17(3), "not less than seven working days' notice" (line 142)

* Scenario: maintained connection, s 17(1)(c) finding, notice of intention to disconnect
  given Mon 30 Mar 2026, 2026 bank holidays.
* Expected (clear days): **Mon 13 Apr 2026**. Code: **Fri 10 Apr 2026**.
* Source: s 17(3) "does not permit an electricity distributor to disconnect ... unless the
  distributor gives ... not less than seven working days' notice of his intention to
  disconnect".
* View: the brief tells the encoder to allow the act on the 7th working day after the day
  of notice, and the code does that correctly. But "not less than N days" is
  conventionally read as N *clear* days, excluding both the day of the notice and the day
  of the act (*Re Railway Sleepers Supply Co* (1885) 29 Ch D 204; *R v Turner* [1910]
  1 KB 346). On that reading the 7 working days are 31 Mar, 1, 2, 7, 8, 9 and 10 Apr, and
  disconnection is first lawful on Mon 13 Apr. I think the clear-days reading is the right
  one, and the brief's convention lets the act happen one working day early. The same point
  applies to Sch 6 para 2(2)(b) (also seven working days).

### 2. N12: Sch 6 para 7(5), "at least two working days' notice" (line 201)

* Scenario: supplier entitled under para 2 to install a pre-payment meter from 7 Apr 2026;
  entry notice Thu 2 Apr 2026; entry Wed 8 Apr 2026, at a reasonable time, with the
  document produced.
* Expected (clear days): entry **not** permitted (earliest Thu 9 Apr). Code: permitted
  (earliest Wed 8 Apr, the 2nd working day after the notice).
* Source: para 7(5) "may not be exercised unless at least two working days' notice has
  been given"; para 8(4) is the same.
* View: as in 1. "At least two working days' notice" means two full working days must pass
  between the notice and the entry: 7 and 8 Apr, so the earliest entry is 9 Apr. The code
  follows the brief. If the brief's convention stays, the issue should be recorded in
  NOTES.md as a judgement.

If the clear-days reading is adopted, the change is one place in each rule: use the 8th
(3rd) working day, or "the next working day after the 7th (2nd)", in `ea89-connection.l4`
(s 17(3)) and `ea89-nonpayment.l4` (para 2(2)(b), and the entry check for paras 7(5), 8(4)).

## Gaps and points noticed in the encoding (not asserted, or asserted only through inputs)

1. **Para 5 has no s 29 exception.** Para 5(1) applies only where the disconnection was
   "otherwise than in the exercise of a power conferred by regulations under section 29".
   `Non-payment case` has no field for this, so N11b (restoring after a s 29 disconnection is
   not a para 5 offence) cannot be expressed. The rule also returns TRUE whether or not any
   disconnection has happened; it depends only on the consent flag.
2. **s 17(1)(b) and s 17(2) are single booleans.** The "has taken all such steps as it was
   reasonable to take" limb of (1)(b), and the three cumulative limbs of s 17(2)(a)-(c)
   (power needed without consent, licence not providing for it, consent not given at the
   time of the request), are folded into the inputs. C5b and C8b test only the caller.
3. **Para 2(2)(a) is all-or-nothing.** The power is barred "as respects any amount which is
   genuinely in dispute". Where part of the debt is disputed and an undisputed part is
   unpaid, the Act still allows the power as respects the undisputed part. The single
   `genuinely in dispute` flag cannot express that, and it leaves the caller to disregard a
   s 39 dispute.
4. **Para 2 notice before the demand gives NOTHING.** The code refuses a notice of intention
   given before the written demand. The Act sets no such order; it only requires seven
   working days' notice before the power is exercised. This is a defensible choice, but it
   is the encoder's (their F6), not the Act's.
5. **Maintained connection with a s 17(1)(c) finding.** `must the distributor connect` gives
   `must maintain the connection` even after a valid notice period has run. The duty is in
   fact displaced from the earliest day. The disconnection goal gives the right day, but
   the outcome enum does not reflect it.
6. **s 27K(3).** A s 27I(1) notice served *before* the final order or confirmation is
   treated as outside the window (the code requires on or after the order date). The Act
   says only "within 3 months from". This is arguable either way.
7. **s 27N(4)** is a boolean input; the commencement date of Sch 14 to the Energy Act 2013 is
   not encoded. **s 27N(1)** gives the start day of interest but not the Judgments Act rate
   or an amount. Neither is wrong, but both are left to the caller.
8. **s 20(1A)(b)** disconnection for want of security carries no notice requirement in the
   code. That is correct: s 17(3) applies only to s 17(1)(c).

## Change after the pass (encoder)

- **Working days' notice (s 17(3), Sch 6 paras 2(2)(b), 7(5), 8(4)).** Not adopted. The clear-days reading was tried, but it contradicts the brief's convention, which the tester's other assertions on the same periods follow (14 of them then failed). The encoding keeps the brief's reading; the tester's two assertions are left failing and recorded as an open question (F2 in NOTES.md), together with the Gas Act 1986's "not less than 7 days' notice".
- The gaps listed above are recorded as known limits in NOTES.md.
