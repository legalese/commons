# Statutory Corporations (Contributions to Consolidated Fund) Act 1989 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the example rows. No pipeline, no coverage table, no independent test pass, no
human gate. NOT for public use.

**Edition:** 2020 Revised Edition, informal consolidation, as deposited at
`../../registers/source-bundle/SCCCFA1989.txt`. The page footer reads "version in
force from 1/7/2026". The latest amendment annotated is Act 17 of 2026 (wef 1 July
2026), which deleted Schedule item 49. The deposit does not say what item 49 was.

**Checks:** one module, one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0220** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked a
sharper question yet.

The Act has four sections and a Schedule, so the row encodes all of it: the
definitions (s 2), the Minister's power to take money (s 3), amendment of the
Schedule (s 4), and the Schedule's 49 bodies with the Acts that establish them. The
honest answer to REQ-0220 is that the Act decides nothing directly for a person or
business. It is addressed to the Minister for Finance and to the listed boards. A
person meets it only at one remove: as someone who pays fees or levies to a listed
board, or whose money a listed board holds.

## What the Act turns out to say

### 1. The Minister can take a board's surplus and its unneeded reserves, by notice alone

s 3: the Minister for Finance may, "by written notice", require any listed board to
pay into the Consolidated Fund (a) the whole or part of the excess of revenue over
expenditure "in any financial year", and (b) the whole or part of its funds that "in
the Minister's opinion" it does not need for its functions. Limb (b) turns on the
Minister's opinion alone; the Act sets no test for it, no consultation and no
appeal. Asserted, with the Minister's opinion as an input.

### 2. Trust money is the only thing protected, and the Act does not say what is trust money

s 2 takes "moneys subject to a trust" out of "revenue", and funds "created for the
accounting of moneys which are subject to a trust" out of "funds". That is the only
shield the Act gives to money a board holds for others. The CPF Board, HDB and the
Monetary Authority of Singapore are all in the Schedule. Whether, for example, CPF
members' balances are "subject to a trust" is not settled by this Act. That would
turn on the CPF Act and the general law, which were not read. The encoding takes the
split as given and asserts that trust receipts and trust funds never enter either
limb. Asserted.

### 3. Improper spending does not reduce the surplus

"Expenditure" is "all expenses properly incurred ... in performing its functions and
duties" (s 2). A board that spends outside its functions cannot shrink limb (a) by
doing so: on revenue of 100, proper expenses of 60 and 50 of other spending, the
excess is 40. Where expenditure exceeds revenue there is no excess, and the encoding
takes limb (a) as zero. That is an inference; the Act does not speak of a deficit.
Asserted.

### 4. s 3 overrides the boards' own Acts, and the Minister alone decides which boards those are

s 3 applies "Despite the provisions of any written law specified in the Schedule".
So a provision in, say, the Estate Agents Act 2010 cannot keep the Council for
Estate Agencies' surplus from the Minister. s 4 lets the Minister amend the Schedule
"by order in the Gazette". No resolution of Parliament is mentioned. The Minister
can therefore bring a board within the override by his own order. Asserted for the
form of the order and the override.

### 5. There is no sanction for not paying

The board must pay "within the period specified in the notice". The Act creates no
offence and states no consequence for missing the period. The encoding says only
that the board has not complied in time. Asserted.

### 6. Several boards are listed under an Act that does not bear their name

The Schedule names the Act "under which established or constituted". The Council
for Estate Agencies sits under the Estate Agents Act 2010, the Competition and
Consumer Commission under the Competition Act 2004, the Singapore Medical Council
under the Medical Registration Act 1997, and the Singapore Dental Council under the
Dental Registration Act 1999. The Schedule now includes bodies created as recently as
the Communicable Diseases Agency Act 2025 and the Skills and Workforce Development
Agency Act 2026. Asserted.

### 7. Fork: can the same dollar be demanded twice?

A year's surplus will usually also sit in the board's reserves by the time a notice
goes out (an inference). The Act joins limbs (a) and (b) with "and" and says nothing
about overlap. The encoding caps each limb separately and states no combined
ceiling. Not asserted beyond the separate caps.

## What would need doing before this is worth anything

- Read the establishing Acts, at least for the CPF Board, HDB and MAS, to see which
  of their moneys are "subject to a trust".
- Find what Schedule items 5, 34 and 49 were, and what Act 4 of 2025 and S 845/2022
  changed. The annotations do not say which items they touched.
- "Financial year" is not defined in this Act. Each board's own Act would need to be
  read.
- No Gazette orders under s 4, no s 3 notices and no case law were searched.
