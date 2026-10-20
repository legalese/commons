# Independent test report: War Crimes Act 1945

Expectations were written in `independent-expectations.md` from BRIEF.md and the source text before reading any L4. Then I read `wc-rules.l4` for names and input shapes only and wrote `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 0 errors, **18 satisfied, 0 failed**. The encoder's own wc-tests.l4 gives 16 satisfied.

## Scenarios asserted (each checks the whole `War crime position` record)

1 base (murder, hostilities, Europe, 1942, killing, citizen): serious, war crime, offence, chargeable, life. 2 and 4: the first and last days (1 Sep 1939, 8 May 1945) are inside the window (s 5 war, s 9(1)(a)). 3 and 5: 31 Aug 1939 and 9 May 1945 are outside it, so it is a serious crime but not a war crime. 6: not in Europe means not a war crime (s 5 war). 7: not an offence under Australian law means not a serious crime (s 6(1),(2),(3)). 8: another act is not a serious crime (s 8(2)). 9: deportation is a serious crime even though local law did not make it an offence (s 6(4),(6)); it is in the course of an occupation and the maximum is 25 years (s 10(2)). 10: complicity in deportation in pursuit of a war policy (s 6(5), 7(1)(c)). 11: an only incidental or remote connection means not a war crime (s 7(2)). 12: persecution (s 7(3)). 13: on behalf of a power at war (s 7(1)(d)). 14: neither citizen nor resident means an offence that cannot be charged (s 11). 16 and 20: no wilful killing means 25 years. 17: permitted by the laws of war and not a crime against humanity gives a defence (s 17(2)). 18: a crime against humanity means no defence.

## Disagreements

None.

## Coverage gaps (in the encoding's input shape or my tests)

- Scenario 15 (resident but not citizen) cannot be tested on its own, because s 11(a)/(b) are merged into one boolean. That is harmless.
- Scenario 19 (superior orders, s 16) has no input. The encoding gives no defence for it, which agrees with s 16, but nothing is tested.
- s 7(4) (several serious crimes together forming a war crime) is not modelled. It is out of the brief's listed sections only by implication, since the brief says s 7 is in scope.
- s 7(3)(b): a crime committed outside Europe in the territory of a country "involved in a war" (war being the European war) could arguably still be a war crime under s 7(3). The encoding requires Europe for every connection. I did not assert this edge because the reading is uncertain (low confidence either way).
- The Baltic occupation limb (s 5 occupation (b)) and the s 6(1)(h)-(k) variants are folded into enum values, so they cannot be tested separately.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
