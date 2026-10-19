# Independent expectations: Common Informers (Parliamentary Disqualifications) Act 1975 (Cth)

Written from BRIEF.md and `../registers/source-bundle/C2004A00250.txt` only, before any `.l4` file was read.

## The Act's words relied on

- s 3(1): liable "to pay to any person who sues for it in the High Court a sum equal to the total of: (a) $200 in respect of his or her having so sat on or before the day on which the originating process in the suit is served on him or her; and (b) $200 for every day, subsequent to that day, on which he or she is proved in the suit to have so sat."
- s 3(2): "A suit under this section shall not relate to any sitting ... at a time earlier than 12 months before the day on which the suit is instituted."
- s 3(3): the Court "shall refuse to make an order ... that would ... cause the person ... to be penalized more than once in respect of any period or day of sitting".
- s 4: "On and after the date of commencement of this Act, a person is not liable to pay any sum under section 46 of the Constitution and no suit shall be instituted, continued, heard or determined in pursuance of that section."

## Reading

- **12-month window (s 3(2)).** Instituted on day D. A sitting counts if it is on or after the same calendar date 12 months earlier. If that date does not exist (D = 29 Feb), use the last day of that month (28 Feb). A sitting on the exact anniversary is not "earlier than 12 months before" D, so it counts.
- **(a)** is one sum of $200, not $200 per day. It is due if at least one counted sitting falls on or before the service day. The service day itself is within (a), because (b) covers only days "subsequent to that day".
- **(b)** is $200 per distinct *day* after the service day on which a counted sitting is proved. Two sittings recorded on the same day make one day.
- **s 3(3).** A day already penalised in an earlier suit is not penalised again, so it is removed from (b). I also read it to take that day out of the reckoning for (a). If *every* counted sitting on or before service was already penalised, the (a) sum would penalise again for that period, so (a) is not due. The brief's sentence "The $200 in s 3(1)(a) is due only if at least one counted sitting falls on or before the day of service" does not say whether "counted" excludes days already penalised. **I read it as excluding them.** Scenario 11 tests this.
- **Not incapable** (the finding is no): nothing payable, $0.
- **s 4:** under s 46 of the Constitution: not liable, no suit. Always "no" in this encoding's frame (after commencement; the assent date is not in the source).

## Scenarios

Default: instituted 15 Jun 2026, served 22 Jun 2026, incapable = yes, nothing already penalised.

| # | Facts | Expected | Basis |
|---|---|---|---|
| 1 | Incapable = no; sat 1 Jun 2026 | $0 | s 3(1) "while he or she was a person declared ... incapable" |
| 2 | Sat 1 Jun 2026 | $200 | s 3(1)(a) |
| 3 | Sat 1, 10, 20 Jun 2026 (all before service) | $200 (one sum) | s 3(1)(a) |
| 4 | Sat 22 Jun 2026 only (the service day) | $200 under (a); nothing under (b) | (a) "on or before the day"; (b) "subsequent to that day" |
| 5 | Sat 23 Jun 2026 only | $200 under (b); (a) not due | s 3(1)(b); brief |
| 6 | Sat 1 Jun, 22 Jun, 23 Jun, 24 Jun 2026 | $600 = 200 + 2×200 | s 3(1)(a),(b) |
| 7 | Sat 15 Jun 2025 (exactly 12 months before institution) | $200 (counts) | s 3(2) |
| 8 | Sat 14 Jun 2025 only | $0 (outside window) | s 3(2) |
| 9 | Sat 14 Jun 2025 and 23 Jun 2026 | $200 (only (b)) | s 3(2), s 3(1)(b) |
| 10 | Instituted 29 Feb 2028, served 7 Mar 2028; sat 28 Feb 2027 | $200 (counts: last day of Feb 2027) | s 3(2); brief |
| 11 | As 10 but sat 27 Feb 2027 | $0 | s 3(2) |
| 12 | Sat 1 Jun, 23 Jun, 24 Jun; 23 Jun already penalised | $400 = 200 + 200 | s 3(3) |
| 13 | Sat 1 Jun (already penalised), 23 Jun | $200: (a) not due (its only day already penalised), (b) $200 | s 3(3) — my reading, see above |
| 14 | Sat 23 Jun twice in the list | $200 (one day) | s 3(1)(b) "every day" |
| 15 | Sittings given out of order: 24 Jun, 1 Jun, 23 Jun | $600 | order irrelevant |
| 16 | No proved sittings | $0 | s 3(1) |
| 17 | Can I be sued under s 46 of the Constitution? | No | s 4 |

## Where I differ from or go beyond the brief

- Scenario 13: in the brief, "counted" is ambiguous about already-penalised days. I read s 3(3) ("any period or day of sitting") as stopping the (a) sum when every pre-service day it rests on was already penalised.
- s 3(3) is framed as the Court refusing to *make an order*, not as a reduction of the sum. Reducing the sum by the already-penalised days is a simplification. Strictly, the Court might refuse the whole order. I test the reduction reading because it is the brief's.
- Commencement (s 2): the assent date is not in the source. "Whether before or after the commencement" in s 3(1) means pre-commencement sittings still count, subject to the 12-month window.
