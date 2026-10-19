# Independent expectations: Death Penalty Abolition Act 1973 (Cth)

Written from BRIEF.md and the source text (C2004A00004.txt) only, before reading any `.l4` file.

Seat: the person charged with, or convicted of, an offence. Questions asked in each scenario:

- **Q1 (s 4)** Am I liable to the punishment of death?
- **Q2 (s 6)** May the punishment of death be imposed on me? (i.e. can I be sentenced to death?)
- **Q3 (s 5)** If my law provides death, what is the penalty instead?
- **Q4 (s 3)** Does the Act apply to my offence at all (and which sections)?

"Nothing" means the Act gives no answer (NOTHING / REFUSE), never FALSE.

## Words of the Act relied on

- s 3(2): "This Act applies in relation to, and in relation to offences under, the laws of the Commonwealth and of the Territories, and, to the extent to which the powers of the Parliament permit, in relation to, and in relation to offences under, Imperial Acts."
- s 3(3): "Section 6 also applies in relation to, and in relation to offences under, the laws of the States."
- s 3(4): "This Act applies in relation to offences referred to in subsections (2) and (3) committed before, on or after the commencement of this Act."
- s 4: "A person is not liable to the punishment of death for any offence referred to in subsection 3(2)."
- s 5: "Where by any law referred to in subsection 3(2) ... it is provided that a person is liable to the punishment of death, the reference to the punishment of death shall be read, construed and applied as if the penalty of imprisonment for life were substituted for that punishment."
- s 6: "The punishment of death must not be imposed as the penalty for any offence referred to in subsection 3(2) or (3)."

## Scenarios

| # | Law | Law provides death? | Offence date | Q1 liable to death (s 4) | Q2 may death be imposed (s 6) | Q3 penalty instead (s 5) | Q4 Act applies |
|---|-----|-----|-----|-----|-----|-----|-----|
| 1 | Commonwealth | yes | after 1973 | No (not liable) | No | Imprisonment for life | Yes, ss 4,5,6 |
| 2 | Commonwealth | yes | before 1973 | No (s 3(4)) | No | Imprisonment for life | Yes |
| 3 | Commonwealth | no | after 1973 | No | No | Nothing to substitute (s 5 not engaged) | Yes |
| 4 | Territory | yes | after 1973 | No | No | Imprisonment for life | Yes |
| 5 | Territory | yes | before 1973 | No | No | Imprisonment for life | Yes |
| 6 | Territory | no | before 1973 | No | No | Not engaged | Yes |
| 7 | Imperial Act within powers | yes | before 1973 | No | No | Imprisonment for life | Yes |
| 8 | Imperial Act within powers | yes | after 1973 | No | No | Imprisonment for life | Yes |
| 9 | Imperial Act within powers | no | after 1973 | No | No | Not engaged | Yes |
| 10 | State | yes | after 1973 | Nothing (s 4 does not reach States) | No (s 6 via s 3(3)) | Nothing (s 5 does not reach States; State law decides) | s 6 only |
| 11 | State | yes | before 1973 | Nothing | No (s 3(4)) | Nothing | s 6 only |
| 12 | State | no | after 1973 | Nothing | No | Nothing | s 6 only |
| 13 | Other (foreign law) | yes | after 1973 | Nothing | Nothing | Nothing | No |
| 14 | Other (foreign law) | no | before 1973 | Nothing | Nothing | Nothing | No |
| 15 | Other (Imperial Act outside the Parliament's powers, if modelled as "other") | yes | after 1973 | Nothing | Nothing | Nothing | No |

Top-level goal ("Can I be sentenced to death?"): No for rows 1-12; Nothing for rows 13-15.
Offence date never changes any answer for a covered law (s 3(4)).

## Where I read the Act differently from the brief, or where the brief is silent

1. **State offence and s 4 (rows 10-12).** The brief says s 6 applies to States and s 5 does not. It is silent on s 4. I read s 4 as not reaching State offences ("offence referred to in subsection 3(2)"), so Q1 for a State offence is *Nothing*, not *No* and not *Yes*. The person still cannot be sentenced to death (s 6). An encoding that answers "not liable: TRUE" for a State offence overstates s 4; one that answers "liable: TRUE" overstates the Act's silence. If the encoding collapses Q1 and Q2 into one "can I be sentenced to death" answer, No is correct for States.
2. **Law with no death penalty (rows 3, 6, 9).** s 4 still applies (the person is not liable to death, trivially) and s 6 still forbids imposition. s 5 is not engaged; the substituted penalty should be Nothing / not applicable, never "imprisonment for life".
3. **Imperial Acts.** The brief turns "to the extent to which the powers of the Parliament permit" into a yes/no input. I accept that; an Imperial Act outside the powers falls to "other" and gets Nothing.
4. **s 5's parenthesis** ("including a provision that would, but for this Act, have effect by virtue of such a law") is folded into "the law provides death"; the brief has no separate input for it.
5. **s 3(1)** (within and outside Australia) means the place of the offence is not an input; fine.
