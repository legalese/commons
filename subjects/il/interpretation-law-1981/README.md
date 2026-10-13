# Interpretation Law 5741-1981 (and the surviving Interpretation Ordinance)

Israel's Interpretation Law is the statute that tells a reader how to read every other statute.
It defines the words that recur ("day", "year", "month", "fiscal year", "enactment", "regulation"), supplies canons of construction (the singular includes the plural; "until" includes the day it names), says how much power a grant of power carries, and fixes the rules a drafter would otherwise have to repeat: how a period of days, weeks, months or years is counted, whether rest days and holidays count, from what moment a statute binds, and what survives when an enactment is repealed.
It replaced most of the older Interpretation Ordinance [New Version], of which only ss. 16(2), 16(4), 17, 19 and 42 remain by the Law's s. 31 (the text shows 16(2) as deleted); s. 17 says that regulations of legislative effect come into force on the day they are published unless another provision says otherwise.

Other encodings of Israeli legislation need executable answers to questions such as "when does a period of three years from a day end?" and "from what moment does a statute bind?".
Those answers come from here and not from the statute being encoded, so this subject makes them executable and tested, as a module other encodings can import: `il-interpretation-time.l4`.

**The encoder worked from two unofficial Hebrew Wikisource consolidations.** The official Knesset PDFs were fetched afterwards and are in `source/official/`; s. 10 of the Law as enacted matches the Wikisource text word for word, and no other section has been compared with them. No domain expert has read any row against the statute.

## Rows

| row | method | status | what it holds |
| --- | --- | --- | --- |
| [`legalese-sonnet-5.5`](encodings/legalese-sonnet-5.5/NOTES.md) | a single Sonnet 5.5 agent working alone from a written brief; no ontology agent, fleet, integrator or independent test author | draft | the time rules as executable functions (Law ss. 3, 8, 10, 21 and Ordinance s. 17), the other computable provisions (Law ss. 1, 20, 22(2), 23, 24, 26, 31, 32, 33; Ordinance ss. 16(4), 19, 42), and the remaining sections carried as quoted text with a reason each is not computed; 630 assertions pass and 12 meant-to-fail assertions fail, as `check.sh` records (section 5 of NOTES.md) |

Start with `encodings/legalese-sonnet-5.5/NOTES.md`: its coverage table has a row for every section of both texts, its fork register records every reading that was weighed (including which of s. 10(a) and (b) governs "three years from a day", and what s. 10(c) does when several rest days come in a row), and its open questions are the ones a lawyer should answer first.
