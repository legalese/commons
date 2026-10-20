# Independent test report: Protection of Word "Anzac" Act 1920

Expectations were fixed in `independent-expectations.md` from BRIEF.md and the source text before any L4 was read. Tests are in `tests-independent.l4`.

## Result

`L4=~/.local/bin/l4 ./check.sh`: tests-independent.l4 has 0 errors, 10 satisfied, 0 failed. (The whole encoding: 18 satisfied, 0 failed.)

## Scenarios (10)

1-3 the s 22(2) uses, each with a breach of reg 2(1), for 12 months' imprisonment. 4 s 22(3), a street, road or park name with a breach of reg 3(1). 5-7 cross-combinations that neither s 22(2) nor s 22(3) lists, which fall back to the s 22(1)(g) fine of at most $1,000. 8 another regulation. 9-10 no breach.

## Disagreements

None.

## Coverage gaps and observations

- s 22(2)/(3) say the penalty "is imprisonment", and the encoding returns imprisonment alone. Neither the Act nor the encoding says whether the regulations' fine is also available in those cases. That is a modelling choice I did not test.
- s 22(1)(g) is a cap on what the regulations may prescribe ($1,000), not the penalty they actually set. The regulations are not deposited, so the encoding cannot give the real figure, and it says so in the enum label.
- The two "street name" rows rely on reg 2(1) and reg 3(1) being independent inputs. Whether reg 2(1) can be breached by naming a street depends on the regulations, which are not deposited.

## Change after the pass (encoder)

- No disagreements.
- The gaps are recorded as known limits in NOTES.md.
