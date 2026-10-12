# Development Fund Act 1959 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example rows (the `writing-l4-rules` skill was not available in this session).
No pipeline, no coverage table, no independent test pass, no human gate. NOT for
public use.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/DFA1959.txt`. The deposit says the revised edition
"incorporates all amendments up to and including 1 December 2021"; its footer reads
"version in force from 5/12/2025". The latest amendment annotated is Act 19 of 2025
(wef 5 December 2025), which inserted s 6(2A) and amended s 6(3). Act 3 of 2024
(wef 26 February 2024) amended ss 4 and 6(2). In the Legislative History the dates
for Act 19 of 2025 are column-shifted in the text extraction: matched by order, the
second and third readings were on 15 October 2025 and commencement was 5 December
2025, which agrees with the annotations.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0166** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for
a person or business it applies to; no scenario has asked a sharper question yet.

The answer is: almost nothing directly. This is a public-finance statute. Its duties
and powers belong to the Minister, the President and Parliament. A person or business
meets it only at the edges: as the recipient of a grant or loan from the Fund
(Schedule para 6, "any other corporation or body"), as a seller of land or of the use
of an invention (para 2), or as a borrower whose repayments go into the Fund
(s 2(f)). The Act is six sections and one Schedule, so this row encodes all of it.
Not encoded: what counts as a Supply law or as "nationally significant infrastructure
expenditure" under s 11 of the Significant Infrastructure Government Loan Act 2021
(that Act was not read); the definitions taken from s 7A of the Financial Procedure
Act 1966; and how Fund money is invested.

## What the Act turns out to say

### 1. A business can get a grant or loan from the Fund only for capital purposes

Schedule para 6 allows "Grants and loans to any public authority, or any other
corporation or body", but only "for any one or more of the purposes referred to in
paragraphs 1 to 4". Those are buildings, works and capital assets, land and the use
of inventions, preparatory surveys and research, and the charges incidental to them.
A grant to a body for any other purpose is outside the Schedule. Paragraph 6 does
not reach paragraph 5 (investment losses) or paragraph 7 (capital injections into
statutory corporations). Asserted.

### 2. Money borrowed under the 2021 infrastructure loan law is ring-fenced

s 5(1): sums borrowed under the Significant Infrastructure Government Loan Act 2021
"may be applied only to meet nationally significant infrastructure expenditure". So
that money cannot buy land for an ordinary purpose, even though land is a Schedule
purpose. s 5(2) still allows it to be spent "on a provisional basis" against an
estimate. Asserted. **Fork:** s 3 is "subject to section 5". The encoding reads that
as s 5's test replacing the Schedule for this money, so infrastructure outside every
Schedule paragraph would still qualify (asserted under that reading and labelled a
fork). The other reading requires both tests. The two readings differ only at the
margin, given how broad para 1 is (an inference).

### 3. Every spend needs a Supply law, and every issue needs a warrant

s 3: money is applied "in accordance with a Supply or Supplementary Supply law", and
s 4(1): the Minister authorises each issue "by warrant". A Schedule purpose without an
appropriation fails. Asserted.

### 4. Money moves between subheads only within one head, and only out of a surplus

s 4(2) lets the Minister move "a further sum out of any surplus arising on any other
subhead of the same head" to a deficient or new subhead, by warrant. Nothing can move
from one head to another. The head total "shall not be thereby exceeded": since the
money comes out of a surplus within the same head, the encoding treats that limit as
met whenever the sum moved is within the surplus (the encoding's arithmetic, not words
of the Act). Asserted, including the boundary (a transfer equal to the surplus is
allowed; one dollar more is not).

### 5. A Contingencies Fund advance needs six things, including the President's concurrence

s 6(2), (2A): the need must be urgent and unforeseen, with no other provision and no
s 4(2) transfer able to meet it; the President, "acting in his discretion", must
concur; and since 5 December 2025 the advance must be authorised by a Minister's
warrant. s 6(3): a supplementary estimate to replace the advance goes to Parliament
"as soon as practicable" and into a Supplementary Supply or Final Supply law. The Act
sets no deadline in days. Asserted.

### 6. The Contingencies Fund is not in the Schedule

s 6(1) builds the Contingencies Fund from "moneys from time to time appropriated
thereto from the Development Fund", but the Schedule does not list that as a purpose,
and s 3 says Fund money "shall be applied only" to Schedule purposes. The likely
answer is that s 6(1), as the specific provision, governs (an inference). Not asserted.

### 7. Old spending is safe

s 1(2): nothing in the Act affects "the legality of any expenditure incurred before
14 September 1959", the commencement date. Asserted at the boundary.

## What would need doing before this is worth anything

- Read s 11 of the Significant Infrastructure Government Loan Act 2021 to give
  "nationally significant infrastructure expenditure" content, and settle the s 3 / s 5
  fork.
- Read s 7A of the Financial Procedure Act 1966 for "capital contribution" and
  "statutory corporation" (Schedule para 7(2)).
- Supply Acts, the Constitution's provisions on the President's concurrence and any
  case law were not searched.
- The Schedule purposes are a fixed list of examples. A real spend would need to be
  classified by a person, and the encoding takes that classification as given.
