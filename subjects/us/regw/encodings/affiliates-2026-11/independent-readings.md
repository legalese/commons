<!-- Written by the independent test author, from the regulation text alone, before the encoding was read. How each point is answered by the encoding is in NOTES.md. -->

# Readings: where the text of 12 CFR 223.2 and 223.3 is genuinely open

Written from `part223-sections-223.2-and-223.3.txt` alone, before the encoding was read.
Each entry gives the words that fork, the reading `regw-independent-tests.l4` takes, and what the other reading would give.
Every assertion that depends on an entry sits in the file's section `Contested readings`, under the same R-number.
Where a point is a `Readings` constructor, the file also asserts what the other constructor must give.

In every fixture the member bank "Bank" is a depository institution (`is a depository institution` TRUE), because a member bank is one.
That matters only for R1 under subpart F.

## Points where the text is open

### R1. Is the member bank its own affiliate? (`Self-affiliation`)

- Words: 223.2(a)(2) "Any company, including any subsidiary of the member bank, that is controlled by a company that controls the member bank", with 223.3(f) "includes a member bank".
- The member bank is a company, and it is controlled by the company that controls it.
  The same literal reading reaches the member bank through (a)(11), "subsidiary of a company described in (a)(1)": the bank is the parent's subsidiary.
  It also reaches it through (a)(4), where the bank's own directors are a majority of the bank's own board.
- Taken: the member bank is not its own affiliate.
  Covered transactions with oneself are meaningless, and nothing in the text suggests the drafters meant the bank to be its own affiliate.
- Other reading: when P controls the bank, "Bank" is an affiliate under 23A, and the list of affiliates contains "Bank".
  Under (a)(4) the bank is its own affiliate as soon as it has a board.
  Under subpart F, 223.2(c) still removes it, because it is a depository institution.
- Asserted: `f p30`, `f bank board`, the world list.

### R2. Interlocking directorates: one board, or all the boards pooled? (`Interlock reading`)

- Words: 223.2(a)(4) "a majority of the persons holding any such office with the member bank or any company that controls the member bank".
- Taken: one board at a time, "any company" read as "any one company".
  A company is an affiliate if a majority of its directors are a majority of the member bank's board, or of one controlling company's board.
- Other reading: pool the offices of the member bank and every controlling company, and ask whether a majority of the company's directors is a majority of the pool.
- The two differ both ways.
  In `f il pooled` Co shares b1, b2 with the bank and p1, p2 with its parent (Co has five directors): not an affiliate when read one board at a time, an affiliate when pooled (4 of 5, and 4 of 6).
  In `f il parent board` Co shares p1, p2 with a parent board of three (2 of Co's 3): an affiliate when read one board at a time, not when pooled (2 of 6).
- Both readings agree where Co's whole board is the controlling company's whole board and the bank's board is one person (`f il parent board entire`): an affiliate.

### R3. "Directly controlled by": direct control (`Direct control reading`)

- Words: 223.2(b)(1)(iii)(A), "Directly controlled by ... one or more affiliates", and (B), "A shareholder that controls the member bank".
  223.3(g) does not define "directly"; (g)(1)(i) and (g)(3) both speak of control "directly or indirectly", which suggests direct is the narrower word.
- Taken: direct control is the controller's own holdings, own elections and own Board determinations, without securities attributed from its subsidiaries.
- Other reading: any control, including what a subsidiary holds.
- Consequence, in `f direct reading` (P controls the bank, the bank holds 60 percent of Sub, P holds nothing in Sub): Sub is excluded as a subsidiary of the bank (taken), or is an affiliate (other reading).
  On the other reading every subsidiary of a bank that has a parent comes back in, and (b)(1) does almost nothing.
- Asserted: `f direct reading`; also `direct control relation`, which the interface defines as the narrow one.

### R4. Prong (a)(11): subsidiary of what? (`Prong 11 reading`)

- Words: 223.2(a)(11) "Any subsidiary of a company described in paragraphs (a)(1) through (10)", under the heading "Subsidiaries of affiliates".
- Two forks.
  (a) "described in" (1) to (10) before the exclusions of (b), or "affiliate" after them.
  (b) Whether a company described only by (11) can itself be the parent for another (11) (chaining).
- Taken: the body of the text.
  A subsidiary of a company described in (1) to (10), even if (b) then excludes that company; no chaining.
- Other reading: a subsidiary of an affiliate, so a subsidiary of an excluded company is not caught, and the prong chains.
- Where it matters:
  - `f prong eleven premises`: Prem is sponsored by the bank, described in (a)(5) but excluded by (b)(2), and holds 30 percent of Dd.
    Dd is an affiliate (taken), or is not (other reading).
  - `f subsidiary of a determined company`: Det is determined under (a)(12), and holds 30 percent of DS.
    Paragraph (a)(12) is not among "(a)(1) through (10)", so DS is not an affiliate under the taken reading, and is under the chaining reading (Det is an affiliate).
    This is the cleanest separator of the two readings, because nothing else describes DS.
  - `f prong eleven di`, under subpart F: a depository institution sponsored by the bank is excluded by (c), and its 30 percent company Dd is an affiliate (taken) or is not (other).
  - Chaining cannot be separated from ordinary control while control passes up by holdings, because 223.3(g)(3) makes a grandchild a subsidiary of the first company.
    It differs only where the second link is not a holding, which brings in R7 (`f prong eleven elections`).
    There the file asserts TRUE under both readings, because R7 is taken as "P controls T".
    If R7 goes the other way, the taken prong-11 reading gives FALSE for E1 and only chaining gives TRUE.

### R5. Fiduciary shares added to shares owned outright, within one class

- Words: 223.3(g)(2) "no company will be deemed to control another company by virtue of its ownership or control of shares in a fiduciary capacity".
- `f fiduciary mixed`: P holds 10 percent on its own account and 20 percent as fiduciary of one class.
- Taken: the fiduciary shares are disregarded, so 10 percent and no control.
- Other reading: control is "by virtue of" all 30 percent together, so the fiduciary shares count where the owned ones are the base, and P controls.

### R6. An individual who controls a company that holds securities

- Words: 223.3(g)(3) "A company controls securities ... owned or controlled ... by any subsidiary", and 223.3(ii) "Subsidiary with respect to a specified company".
  The attribution rule speaks of companies; (g)(1)(i) speaks of "the company or shareholder, directly or indirectly".
- `f individual through a company`: I holds 30 percent of S; S holds 30 percent of T.
- Taken: I controls T, through "indirectly" in (g)(1)(i).
- Other reading: (g)(3) is only for companies, so I does not control T.
- Note that the prongs in the file that use an individual controller of the bank (`f shareholder through a company`) were built so as not to depend on this: the middle company is an affiliate in its own right.

### R7. Control of an election exercised through a subsidiary

- Words: 223.3(g)(1)(ii) "controls in any manner the election of a majority of the directors", against (g)(3), which attributes "securities, assets, or other ownership interests" and not powers.
- `f election through a subsidiary`: P controls S by 30 percent; S controls the election of T's directors.
- Taken: P controls T ("in any manner").
- Other reading: the attribution rule does not carry an election up, so P does not control T.
- Likewise for a subsidiary whose control comes from a Board determination under (g)(1)(iii).

### R8. Kinds of party that are persons but are not named in the definition of company

- Words: 223.3(f) lists "corporation, partnership, limited liability company, business trust, association, or similar organization"; 223.3(bb) lists "joint venture, pool, syndicate, sole proprietorship, unincorporated organization, or any other form of entity" next to "company".
- Taken: a joint venture, pool, syndicate, unincorporated organization or other form of entity is not a company, because (bb) names them apart from "company".
  A plain trust and an individual are not companies either (asserted as clear).
- Other reading: an unincorporated organization or a syndicate is an "association, or similar organization", so a company.
- For prong (5), "including a real estate investment trust": the file assumes a REIT is a `Business trust`, and treats a plain `Trust` as not a company.

### R9. A depository institution of a kind that is not on the company list

- Words: 223.3(f) "and, unless specifically excluded, includes a member bank and a depository institution".
- Taken: a party flagged as a depository institution is a company whatever its kind.
- Other reading: the kind decides, and the flag adds only the member bank and insured institutions of the listed kinds.

### R10. A company that controls the member bank and is also its subsidiary

- `f cross with the bank`: A holds 30 percent of the bank, and the bank holds 30 percent of A.
- Words: 223.2(a)(1) makes A a parent; 223.2(b)(1) removes "Any company that is a subsidiary of the member bank" unless one of (i) to (v) applies, and none does.
- Taken, on the literal words: the exclusion wins, so A is not an affiliate.
  A is a subsidiary of the bank, it is not a depository or financial subsidiary, it is not directly controlled by an affiliate (the bank is not its own affiliate under R1) or by a shareholder that controls the bank, and so on.
- Other reading: the exclusion is meant for companies the bank controls and that do not control it, so A stays a parent and an affiliate.
- The file does not assert anything about self-pairs in the control relation (the bank controlling itself through A), which this fixture also creates.

### R11. A party flagged a financial subsidiary that the bank does not control

- `f flagged but not held`: `is a financial subsidiary` is TRUE, and the bank holds 10 percent.
- Words: 223.2(a)(8) "A financial subsidiary of the member bank"; 223.3(p)(1) "any subsidiary of a member bank that ...".
- Taken: not a subsidiary of the bank, so not its financial subsidiary, so not an affiliate under (a)(8).
- Other reading: the flag is a fact and decides.

### R12. A determination under (a)(12) that names something that is not a company

- Words: 223.2(a)(12) "Any company that the Board determines".
- `f determined individual`: the list of determined affiliates names an individual.
- Taken: not an affiliate, because the prong is about companies.
- Other reading: the determination decides.

### R13. Two rows of one holder and one class

- This is an input convention rather than a reading of the text.
- `f split rows`: P holds 15 percent and 10 percent of one class of T, in two rows.
- Taken: the holder owns 25 percent of the class and controls T.
- Other reading: each row is tested alone, so no control.
- Rows of different classes are not added in either reading (`f split rows classes`).

### R14. Fiduciary shares held by someone who is not a company

- Words: 223.3(g)(2) "no company will be deemed to control"; 223.3(g)(1) "the company or shareholder".
- `f fiduciary plain trust` and `f fiduciary individual holder`: a non-business trust, or an individual, holds 30 percent of T as fiduciary.
- Taken: the sentence is addressed to companies, so an individual or a plain trust that holds 30 percent controls.
- Other reading: the exclusion covers every holder, so there is no control.
- The (a)(3) exception is a separate point: R16.

### R15. A list of control links that is not closed

- Interface question rather than a reading of the text: it is about what `rel` is promised to be.
- (a) `rel chain`: `is a subsidiary of` is given the links (A, B) and (B, C), and asked whether C is A's subsidiary.
  Taken: the list is read as it stands, and (A, C) is not in it, so no (the function has no structure to derive it from).
  Other reading: the function closes the list, because control passes up through a subsidiary under (g)(3).
- (b) `f step two levels`: `control step` is given (P, S1) and (S1, S2) but not (P, S2), and S2 holds 30 percent of T.
  Taken: P controls T, because 223.3(g)(3) says "owned or controlled, directly or indirectly, by any subsidiary" and the structure is at hand.
  Other reading: the step looks only at the subsidiaries of P that the list names, so S2's shares are not attributed.
  The main assertion on this fixture uses the closed list (the one that also holds (P, S2)), which both readings answer the same way.

### R16. The exception in 223.3(g)(2) to the fiduciary rule

- Words: 223.3(g)(2) "except as provided in paragraph (a)(3) of § 223.2"; 223.2(a)(3) "controlled, directly or indirectly, by trust or otherwise, by or for the benefit of shareholders who ... control ... the member bank".
- `f fiduciary individual` and `f fiduciary corporate trustee`: a shareholder that controls the bank (30 percent) also holds 30 percent of Co as fiduciary.
- Taken: Co is an affiliate (and the corporate trustee is a parent), reading "by ... shareholders" as the shareholder itself acting as trustee.
- Other reading: the exception is for shares held "for the benefit of" controlling shareholders by someone else, which the inputs cannot say, so the fiduciary holder's own control stays excluded and Co is not an affiliate.
- The individual case also follows from R14 as taken, because (g)(2) does not reach a holder that is not a company.
- The negative cases are clear and sit outside the contested section: a trustee unconnected with the bank (`f fiduciary stranger`), and fiduciary shares of the bank itself (`f fiduciary of the bank`).

## Not genuinely open, but easy to get wrong (asserted as clear)

- 25 percent is inclusive ("25 percent or more"); just under is not control.
- "any class": 20 percent of class A and 20 percent of class B is not control, however the two add up; 10 and 30 is.
- Several holders of one class are looked at one at a time: 20 and 20 gives control to neither.
- Percentages of a subsidiary's holdings attributed under (g)(3) are not multiplied: 30 percent of S and S's 30 percent of T is control of T.
- Attribution adds within one class: the controller's own 15 and a subsidiary's 10 make 25; different classes do not add.
- A subsidiary's fiduciary shares are not attributed.
- A showing under (g)(4) removes the convertible securities only, not the shares owned outright, and a showing about another issuer or by another holder does not help.
- Cyclic definitions take the least solution: two unconnected companies that sponsor each other are not affiliates, because nothing starts the chain.
- Excluding a company under 223.2(b)(2) to (4) removes that company only: a company that the parent controls through the excluded one is still an affiliate under (a)(2) (`f premises below a sibling`, Sub2 is controlled by P through attribution under 223.3(g)(3)).
- A parent that controls the member bank is also "a shareholder that controls the member bank" under 223.2(b)(1)(iii)(B), so a bank subsidiary that it holds 30 percent of is back in whatever other affiliates are known (`step A` on `f sibling and bank subsidiary` with an empty list).
- Reading "an affiliate" in (a)(5), (a)(10) and (b)(1)(iii)(A) after the exclusions: a company sponsored by an excluded company is not sponsored by "an affiliate" (`f sponsored by an excluded company`).

## Not expressible with the inputs, so not tested

- 223.2(a)(3) "or for the benefit of": there is no beneficiary field, so the test only has the trustee itself be the controlling shareholder (`f fiduciary individual`, `f fiduciary corporate trustee`).
- Groups of shareholders: 223.2(b)(1)(iii)(B) "a group of shareholders that together control the member bank"; and "acting through one or more other persons" in 223.3(g)(1)(i), where shares are voted in concert.
- 223.3(g)(1)(i) "has power to vote" apart from ownership (a proxy, a voting trust); the holding row carries only a percentage.
- 223.2(a)(6) investment companies and funds, and 223.2(a)(9) merchant banking and insurance company investment authority: the inputs have no adviser or 15 percent equity capital rows, and the interface excludes them.
- 223.2(b)(5): the running of the two-year or authorized period is stated, not computed, so only the stated states are tested.
- 223.3(p)(1) and (p)(2) (the activity tests for a financial subsidiary), 223.3(k) (the operating-subsidiary gloss) and 223.3(aa): the flags are facts.
- 223.3(g)(1)(iii), (g)(4), (g)(5) and 223.2(a)(12): that a determination was made "after notice and opportunity for hearing", that a showing was made "to the Board's satisfaction", and that the Board or the agency made an order are stated inputs.
- What is a "class of voting securities" (223.3(jj), 12 CFR 225.2) and what is "equity capital" (223.3(n)).

## Interface questions (not readings of the text)

- `showings` is one list that serves both (g)(4) and (g)(5).
  The file never gives one holder a convertible and 25 percent equity in one issuer with a showing, so the answer cannot depend on which the showing was for.
- `control step` and `is a subsidiary of` take the control links as a parameter.
  The positive assertions need the function to read `rel`, and the main positives pass lists that hold every link they need (R15 is the exception, kept apart).
  The fixtures never put a direct holding between a controller and its subsidiary, so the negative assertions come out the same whether the function reads or derives the link.
- `affiliate step` takes `current`, the names already found.
  The assertions about (b)(1)(iii)(A) and about prong (11) in `step` assume `current` is what the exclusion and the prong consult.
  They use the chaining constructor of `Prong 11 reading` for prong (11), because under the other constructor `current` does not say which of the known affiliates are described in (a)(1) to (10).
- 223.3(p)(3), "any subsidiary of such a company is also a financial subsidiary": `f subsidiary of a financial subsidiary` asserts an affiliate by prong (11) and (b)(1)(iii)(A) whether or not the flag is set on the grandchild.
