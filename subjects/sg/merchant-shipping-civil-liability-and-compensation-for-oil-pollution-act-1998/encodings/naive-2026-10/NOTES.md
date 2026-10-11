# Merchant Shipping (Civil Liability and Compensation for Oil Pollution) Act 1998 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation, version in force from 1/4/2022, as deposited
at `../../registers/source-bundle/MSCLCOPA1998.txt`. The latest amendment annotated is
Act 25 of 2021 wef 01/04/2022 (ss 18(4), 28(4), 29(5)); the limits in ss 6(2) and 28(1)
are annotated S 486/2003.

**Checks:** one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is **REQ-0106** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

This row takes what a shipowner, charterer, salvor, insurer, oil importer or pollution
claimant meets: which ships carry the owner's liability (ss 3(3), (4), 18(1)), the
owner's defences (s 4), who else is shielded (s 5(1)(d), (2)), recoverable environmental
loss (s 5(3)), the limit in SDRs and its loss (ss 6, 15(3)), the time bars (ss 12, 30),
the insurance certificate (s 13), contributions to the International Fund (s 25(5),
(6)), when the Fund pays and its cap (ss 27, 28), and selected offences (ss 13(6), 20(2)).
Not encoded: SDR conversion (ss 7(3), 28(5)), limitation-action procedure (ss 7 to 10),
jurisdiction and foreign judgments (ss 16, 17, 29), contribution amounts (s 25(7) to
(11)), the Director's powers, joint liability of two ships (s 3(6)), the Contributory
Negligence links (ss 3(8), 27(8)), and Part 4 beyond the offences named.

## What the Act turns out to say

### 1. The Fund's cap for natural disasters is lower than its ordinary cap

s 28(1)(a) caps the Fund **and the owner together** at 203 million SDR for an incident;
s 28(1)(b) caps the Fund **alone** at 135 million SDR where the damage resulted from "an
exceptional, inevitable and irresistible natural phenomenon". Since the owner pays
nothing in that case (s 4(a)), a claimant after a natural disaster can recover at most
135 million SDR, against up to 203 million in an ordinary spill. Both rise to 300.74
million under s 28(1)(c) when three Fund countries received 600 million tons in the
preceding year. Whether 135 million is a figure left behind when S 486/2003 raised the
others is an inference the deposit cannot settle. Asserted (203m less 64.455m paid
by the owner leaves 138.545m; a natural phenomenon gives 135m).

### 2. Liability attaches to tankers only, and a dedicated tanker even when empty

s 3(3) applies the owner's liability to "any ship constructed or adapted for carrying oil
in bulk as cargo". A dedicated tanker in ballast is covered, even if proved clean; a
combination carrier is covered only while carrying oil or on a later voyage unless
"proved that no residues ... remain" (s 3(4)). A container ship spilling its own bunker
fuel is outside s 3, although "oil" in s 2(1) includes bunkers. Warships and government
non-commercial ships are outside Part 2 entirely (s 18(1)). Asserted.

### 3. The owner is strictly liable and almost everyone else is shielded

The owner's defences are narrow (s 4): war, an exceptional natural phenomenon, sabotage
"wholly" by an outsider, or "wholly" a lighthouse authority's neglect. An ordinary storm,
sabotage by the owner's own employee, or outsider sabotage combined with crew negligence
leaves the owner liable. Meanwhile s 5(1)(d) shields the crew, charterers (including
bareboat), managers, consenting salvors and clean-up responders unless they acted with
intent or recklessly. A salvor acting on its own initiative, the cargo owner and another
colliding ship are not on the list. Asserted.

### 4. The insurer may limit even when the owner cannot

The owner loses the s 6 limit if the discharge resulted from the owner's intent or
recklessness (s 6(4)), but the insurer, sued directly under s 15, may limit "whether or
not" that is so (s 15(3)). The owner's limit is 4.51 million SDR up to 5,000 tons plus
631 SDR a ton above, capped at 89.77 million (reached above about 140,000 tons).
Asserted.

### 5. The certificate rules depend on the flag, and the Director cannot certify a foreign Convention ship

s 13 bites on ships carrying "more than 2,000 tons" of oil in bulk entering or leaving a
Singapore port or offshore terminal, and on Singapore ships entering or leaving any port.
Passing through without calling is not caught. For a ship registered in another
Liability Convention country only its own government's certificate will do (s 13(3)(b));
for a non-Convention ship the flag government's certificate is not enough unless
regulations under s 13(4) say so. Trading without one is a fine of up to $1 million on
the master or owner (s 13(6)). Asserted.

### 6. The Fund pays when the owner cannot, except for war and unidentified ships

s 27(1) lists the natural-phenomenon, sabotage and navigational-aid defences, insolvency
and damage above the limit, but not war, and s 27(6) excludes war, government ships and
cases where the claimant cannot identify the ship. A claimant's own fault may reduce
the Fund's payment, but not for preventive measures (s 27(7), (9)). An oil receiver
pays contributions only above 150,000 tonnes a year, counting the whole group (s 25(5),
(6)). Asserted.

## What would need doing before this is worth anything

- The SDR conversion and the limitation-action procedure (ss 7 to 10) are not modelled,
  so no Singapore-dollar figure comes out.
- The Liability and Fund Conventions themselves were not retrieved; whether the 135
  million SDR figure in s 28(1)(b) matches them is unchecked.
- No subsidiary legislation (certificate fees, contribution security, compoundable
  offences) and no case law were searched.
