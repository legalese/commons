# Independent expectations: United States Naval Communication Station (Civilian Employees) Act 1968

Written from BRIEF.md and the source text only, before reading any `.l4` file. Commencement: Royal Assent, 24 June 1968 (s 2; Note 1 table).

## Scenarios

| # | Facts | Expected | Act's words |
|---|---|---|---|
| E1 | Australian citizen (not US citizen/national), civilian, employed by US Government at the Station | Act applies; CEC Act applies as if employee | s 4(a), s 5(1) |
| E2 | Same, but employed by an *instrumentality* of the US Government | Act applies (deemed employed by US Government) | s 3(2), s 4(a) |
| E3 | US citizen, employed on terms agreed with a Fair Work registered organisation | Act applies | s 4(b) |
| E4 | US citizen, employed on terms agreed with a WA-registered trade union (Industrial Relations Act 1979 (WA)) | Act applies | s 4(b) |
| E5 | US citizen, ordinary US terms (no agreed terms) | Act does not apply; CEC Act not applied | s 4(b) not met |
| E6 | US *national* (not citizen), ordinary terms | Act does not apply | s 4(a) "is not a citizen, and is not a national" |
| E7 | Non-US citizen who is a member of the US naval forces | Act does not apply | s 4 "(other than a member of the naval, military or air forces of the United States of America)" |
| E8 | Non-US citizen employed by US Government but not in connexion with the Station | Act does not apply | s 4 "in or in connexion with the establishment, maintenance or operation of the Station" |
| E9 | Non-US citizen employed by a private contractor (not US Government or instrumentality) | Act does not apply | s 4, s 3(2) |
| E10 | E1 person; injury 1 Jan 1970; s 9 or 10 CEC applies; damages would be recoverable on the Commonwealth-employment hypothesis | may recover like damages from the Commonwealth (s 6(1)) | s 6(1) |
| E11 | As E10 but s 9/10 does not apply | no s 6(1) damages | s 6(1)(b) |
| E12 | As E10 but damages would not be recoverable on the hypothesis | no damages | s 6(1)(c) |
| E13 | As E10, death case; a dependant claims | the dependant ("another person") may recover | s 6(1) "or, in the event of his or her death, another person" |
| E14 | As E10 but injury on 24 June 1968 (commencement day) | s 6(1) applies; may recover | s 6(1)(a) "after the commencement" (Act commences at the start of 24 June 1968) |
| E15 | As E10 but injury 29 Aug 1966 (first day of s 6(2) window) | may recover (s 6(2)) | s 6(2)(a) "on or after the twenty-ninth day of August, 1966" |
| E16 | As E10 but injury 28 Aug 1966 | no damages under s 6(1) or (2) | s 6(2)(a) |
| E17 | As E10 but injury 23 June 1968 (day before commencement) | may recover (s 6(2)) | s 6(2)(a) "before the commencement" |
| E18 | Injury 1 Jan 1970; all conditions met, but person is a US citizen on ordinary terms (Act does not apply) | no damages | s 6(1)(a) "a person to whom this Act applies" |

## Where I read the Act differently from, or more precisely than, the brief

- **The commencement-day edge.** I read 24 June 1968 as falling under s 6(1) ("after the commencement"), because the Act is in force from the start of the day of Royal Assent. An encoding using a strict `> 24 June 1968` would give no damages for an injury on that day (E14). That would leave a gap, since s 6(2) covers only days "before the commencement".
- **s 6(2) runs on a hypothesis.** It asks whether damages would have been recoverable under s 6(1) "if this Act had come into operation on that date" and with the 1930-1964 version of the CEC Act. In substance that means: the person meets s 4, ss 9/10 apply, and damages are recoverable on the Commonwealth-employment hypothesis. I use the same inputs for both windows.
- **s 4(b) agreed terms.** "In accordance with, or by reference to" terms agreed with a registered organisation *or* a WA union. Either body suffices (E3, E4).
- **s 6(3)-(4) and the Schedule** are out of scope and not tested.
