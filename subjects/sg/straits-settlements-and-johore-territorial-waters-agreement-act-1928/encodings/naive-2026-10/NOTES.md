# Straits Settlements and Johore Territorial Waters (Agreement) Act 1928 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else (the skill was not loadable in this session, so the
conventions of the finished naive rows were followed). No pipeline, no coverage
table, no independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SSJTWAA1928.txt`, incorporating "all amendments up to
and including 1 December 2021" and in operation from 31 December 2021. The body
carries no amendment annotations. The Legislative History (not part of the Act)
lists only the original Act, 18 & 19 Geo. V, c. 23 (commencement 3 August 1928),
with a note that the Application of English Law Act 1993 declared it to apply or
continue to apply in Singapore, and the 1985 Revised Edition (operation 30 March
1987). No amending Act is listed. The deposit's arrangement of sections is out of
step by one line; the body's numbering is followed. The map annexed to the
Agreement is not in the deposit.

**Checks:** one case file, 28 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0255** in `subjects/sg/requirements.jsonl`: Tier 4 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act is two sections and a Schedule. s 1 gives Parliament's approval to an
Agreement of 19 October 1927 between the Governor of the Straits Settlements (for
the King) and the Sultan of Johore; s 2 is the short title. The whole substance is
the four Articles of the Agreement, and this row takes all four. Not encoded: the
recitals, the 1824 Treaty itself, the geography (where the channel runs, where
low water is), the map, the signatures, and anything after 1928.

## What the Act turns out to say

### 1. It decides nothing for any person — only whose sea it is

There is no right, duty, offence, penalty, fee or deadline anywhere in the Act or the
Agreement. What it decides is whose territorial waters a stretch of sea is (Articles
I and II) and who holds certain islets (Article III). For a fisherman or a boat
operator in Johore Strait, that is the question that matters, and it is the one
encoded: `whose territorial waters` returns the Settlement of Singapore, Johore, or
"not decided by the Agreement". Asserted.

### 2. In the Strait, the channel line beats the three-mile rule

Article II gives Johore all ceded waters within three nautical miles of its mainland,
but "Subject to the provisions of Article I". Inside Johore Strait the boundary is the
centre of the deep-water channel, so water on the Singapore side of that line stays
the Settlement's even when it lies within three miles of the Johore mainland — as,
the encoder infers, much of a narrow Strait would. Asserted.

### 3. Outside the Strait, ceded water within three miles of Johore went back to Johore

Ceded water outside the Strait and within three nautical miles of the Johore mainland
(measured from low water mark) "shall be deemed" Johore's. Ceded water beyond the three
miles is not mentioned; the encoding treats it as remaining the Settlement's, which is
an INFERENCE from silence, not a statement of the Agreement. Water never ceded in 1824
is outside the Agreement altogether. Asserted.

### 4. The text beats the map, "in all cases"

The boundary is "approximately delineated in red" on an annexed map, but if the map
"owing to alterations in the channels, etc." appears to conflict with the text, "the
text shall in all cases prevail". The encoding returns the text whatever the cause.
Where the channel splits into two portions of equal depth side by side, the line runs
midway between them. Asserted.

### 5. Islets in Johore's waters that were British were ceded "for ever"

Article III cedes "in full sovereignty and property" to the Sultan, "his heirs and
successors for ever", every islet in Johore's waters (as Articles I and II define them)
that immediately before formed part of the King's dominions. Both conditions are
needed. Asserted.

### 6. Nothing had force until Parliament approved it

Article IV: the Agreement "shall remain without force or effect until it has received
the approval of the British Parliament". s 1 of this Act is that approval. The
encoding answers "not decided by the Agreement" for every place when approval is
absent. Asserted.

## What would need doing before this is worth anything

- The boundary depends on facts the Agreement does not supply: where the deep-water
  channel runs, where low water is, which waters the 1824 Treaty ceded. Each is an
  input here. Hydrographic data and the annexed map would be needed to answer a real
  question about a real position.
- What became of these waters after 1928 (separation from the Straits Settlements,
  independence, later agreements with Malaysia, and the present law of Singapore's
  territorial waters) is not in this deposit and was not looked at. This row says
  what the 1927 Agreement says, not where the boundary is today.
- Pulau Merambong and Johore Shoal are named in Article I only as landmarks; the
  encoding does not say whose they are.
- No case law or treaty commentary was searched.
