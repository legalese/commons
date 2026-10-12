# Independence of Singapore Agreement 1965 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition. The cover page says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". No amendment is annotated anywhere in the deposit.

**The text deposit is only the cover page.** `ISA1965.txt` holds 594 characters:
the cover. The instrument itself is in `ISA1965.pdf` as sixteen scanned facsimile
pages with no text layer (page 2 is blank). This row was read from images of those
pages, so a human should check every quotation against the facsimile. The facsimile
holds, in order: Singapore's Proclamation of Singapore (9 August 1965, Lee Kuan Yew);
the Malaysian Proclamation on Singapore (9 August 1965, Tunku Abdul Rahman); the
Agreement (Articles I–VIII, dated 7 August 1965, signed for both Governments);
Annex A (the form of the Malaysian proclamation); and Annex B, a Bill "to amend
the Constitution of Malaysia and the Malaysia Act" (ss 1–14). The section numbers
used here are Annex B's.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0257** in `subjects/sg/requirements.jsonl`: tier 4 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Agreement decides for a person or business it applies to. No scenario has
asked a sharper question yet.

This row covers the provisions that decide something about a person, an officer, a
piece of property, a law or an agreement: Article II and Annex B s 3 (Singapore
Day), ss 6–14, Article VII and Article VIII. Not encoded: the recitals, and the
proclamations except where quoted. Also left out are Articles III–VI (the form of
proclamation, Malaysia's undertaking to enact Annex B, the promised defence treaty,
economic co-operation), Annex B ss 2, 4 and 5 (the powers provisions), and the second
paragraph of s 13 (the 1957 UK–Malaya defence agreement and the British bases).

Dates are encoded as numbers YYYYMMDD so that number comparison orders them.

## What the Act turns out to say

### 1. Becoming a citizen of Singapore cost a person Malaysian citizenship, on the day

Annex B s 12: "A citizen of Singapore shall on Singapore Day cease to be a citizen
of Malaysia." It applies automatically, with no election. The section says nothing
about anyone who was not a citizen of Singapore, and the encoding only says whether
s 12 ended Malaysian citizenship. Asserted.

### 2. Every existing law kept running, and so did appeals to Kuala Lumpur and London

Annex B s 7: all laws in force immediately before Singapore Day "continue to have
effect according to their tenor", "subject however to amendment or repeal by the
Legislature of Singapore". Annex B s 8: until the Legislature of Singapore provides
otherwise, appeals from the High Court "continue to lie to the Federal Court of
Appeal of Malaysia and then to the Privy Council". The Malaysian constitution
stopped applying in Singapore "except as hereinafter provided" (s 3), and s 8 is one
of those exceptions. Whether and when Singapore made other provision is not in the
deposit. Asserted.

### 3. Public officers and government property went back to Singapore

Annex B s 10(a): anyone who was a Singapore government officer immediately before
Malaysia Day and later became a Malaysian officer, "including members of the Armed
Forces, the Police Force, the Courts and the Judiciary", became a Singapore officer
again on Singapore Day. Under s 10(b), people Malaysia engaged between the two days
also became Singapore officers, but only if they worked in departments that had been
Singapore State departments. Someone Malaysia hired in 1964 into a federal ministry
is outside both limbs. Under s 9, property, rights and liabilities revert only if
they were Singapore's before Malaysia Day. The text says nothing about property
Malaysia acquired for itself in between. Asserted.

"Malaysia Day" is used in ss 9 and 10 but not defined in the deposit. Reading it as
16 September 1963 is an inference from the recital that "Malaysia was established on
the 16th day of September, 1963".

### 4. Annexes J and K of the 1963 Agreement were rescinded two days before separation

Article VII rescinds Annexes J and K of the Agreement relating to Malaysia of 9 July
1963 "as from the date of this Agreement". The Agreement is dated 7 August 1965, and
Singapore Day is 9 August 1965. What Annexes J and K contained is not in the deposit.
Asserted.

### 5. The Johore water supply is guaranteed by both Governments

Annex B s 14: Singapore guarantees that the Public Utilities Board will abide by the
Water Agreements of 1 September 1961 and 29 September 1962, made between the City
Council of Singapore and the State of Johore. Malaysia guarantees that Johore will
abide by them too. Each Government answers for its own side. Asserted.

### 6. Treaties made for Malaysia bind Singapore where they apply to Singapore; Singapore indemnifies Malaysia's guarantees in full

Annex B s 13: a treaty the Agong or the Malaysian Government made with another
country before Singapore Day is deemed a treaty between Singapore and that country
"in so far as such instruments have application to Singapore". Decisions of
international organisations accepted before that day are treated the same way. Under
Article VIII, where Malaysia guaranteed a Singapore Government agreement, Singapore
must negotiate a release and "indemnify the Government of Malaysia fully". The
encoding reads "fully" as the whole loss. Asserted.

### 7. 17 seats

Annex B s 11: Singapore's "two Senators and fifteen Members of Parliament" ceased to
be members of the Malaysian Parliament on Singapore Day. Asserted.

## What would need doing before this is worth anything

- A text deposit of the instrument itself: the `.txt` has only the cover, and every
  quotation here was transcribed from scanned images.
- Annex B is printed in the form of a Bill. The deposit does not show the Act that
  Malaysia's Parliament passed, or whether it differs.
- Singapore's own legislation on separation and on appeals (which the s 8 "other
  provision" points to) was not read.
- The Article V defence treaty and the British bases in s 13 were left out.
