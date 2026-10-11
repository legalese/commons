# Foreshores Act 1920 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, deposited as `../../registers/source-bundle/FA1920.txt`.
The deposit says it "incorporates all amendments up to and including 1 December 2021
and comes into operation on 31 December 2021". The latest amending Act in its
Legislative History is Act 16 of 2016 (s 8, from 10 June 2016), which repealed s 3.
Section numbers follow the body: the arrangement at the top of the deposit is out of
step by one.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0153**: tier 2 of the remaining Singapore Acts, ordered by
everyday-life relevance. The requirement asks what the Act decides for a person or
business it applies to; no scenario has asked a sharper question yet. The Act has 12
sections, so nearly all of it is encoded: ss 4(2), 5 to 11. Not encoded: the short
title, s 3 (repealed), the Government's works powers in s 4(1) (used only to define
"the works"), the s 12 saving, and the State Lands Act 1920 rules that ss 5(2) and
10(2) borrow (not read).

## What the Act turns out to say

### 1. There is no right to compensation for the works, only an appeal to the Minister

s 6 bars any claim or action against the Government for lands "injuriously affected
by the execution of the works", and s 7(1) repeats it, naming "loss of sea frontage".
A person whose property has been **damaged** may appeal to the Minister, "whose
decision shall be final" (s 7(2)); the Minister "may, in his discretion", after an
officer's inquiry, pay a sum he determines or direct repairs (s 7(3)). The encoding
treats loss of sea frontage or of a view as outside the appeal; that is an inference,
since the text does not say whether it is "damage". Asserted.

### 2. Being inside the port makes a reclamation harder to approve, not easier

s 4(2): Parliament must approve a reclamation unless it "does not exceed 8 hectares
or, if the whole of that part is within port limits, 4 hectares", in which case the
Minister may authorise it. A 6-hectare reclamation partly outside the port goes to
the Minister; the same 6 hectares wholly inside the port needs Parliament. Exactly
8 (or 4) hectares is still the Minister's. Asserted.

### 3. Sand and coral under a foreshore lease belong to the State

Every s 9 lease must reserve "all mines and minerals" to the State (s 9(4)(b)), and
s 9(5) defines minerals to include "corals, stone, clay, sand, gravel", brine,
petroleum and natural gas. A lessee who stops using the land for the lease's stated
purposes at any time during the term can have it re-entered and forfeited by a
Collector of Land Revenue (s 9(4)(a)). Asserted.

### 4. Leases run up to 100 years, licences up to one year

s 9(2): a lease term "shall not exceed 100 years except in special cases", and the
lease needs a Presidential declaration that it does not substantially infringe public
rights, preceded by a Gazette notice inviting written objections to the Minister
within 3 weeks (s 9(3)). The encoding counts 3 weeks as 21 days after publication (an
inference; the Interpretation Act was not read). A temporary occupation licence may
not exceed one year, is granted by the Commissioner of Lands or a deputed Collector,
and may not be renewed if the Minister is shown it substantially infringes public
rights (s 10). Asserted.

### 5. A beach farmer can charge no more than both the agreed price and the grant's cap

s 11(4): the farmer may not recover "a larger sum than that specially agreed on" with
the user, "nor a larger sum than that permitted in the grant by the President". The
recoverable sum is the lesser of the two. Asserted.

### 6. Reclaimed land is cleared of old rights only by Gazette proclamation; old grants need both dates before 1901

s 5(1): rights over the former foreshore are extinguished when the President declares
reclaimed land State land by proclamation in the Gazette, not on reclamation. s 8
validates a Governor's grant only where both the grant and the reclamation or
building on the land came before 25 January 1901. Asserted.

## What would need doing before this is worth anything

- The State Lands Act 1920 rules on temporary occupation licences, which s 10(2)
  applies to foreshore licences, were not read.
- The meaning of "damaged" in s 7(2), and how "3 weeks" is counted in s 9(3), were
  not checked against the Interpretation Act or any case.
- No subsidiary legislation, Gazette notices or decided cases were searched.
