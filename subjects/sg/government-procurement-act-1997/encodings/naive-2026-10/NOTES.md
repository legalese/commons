# Government Procurement Act 1997 — naive encoding

**Method: naive.** Straight from the deposited text. The `writing-l4-rules` skill
could not be loaded in this session, so the conventions of the finished naive rows
(coroners-act-2010, stamp-duties-act-1929) were followed instead. No pipeline, no
coverage table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, deposited at
`../../registers/source-bundle/GPA1997.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". The latest amendment annotated in the body is 40/2019 (ss 8(6),
21(2)). The retrieval record calls it the current version as at 1 October 2026.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0114** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to. Here that means a supplier bidding
for a government contract. No scenario has asked a sharper question yet.

The Act is short (26 sections). Nearly all of it is about the supplier's challenge,
and that is what this row takes: who is owed the duty (ss 2, 7(2)), where a breach
can be taken (s 7(3)), lodging, deposit and notice (ss 12 to 14), mandatory
invalidity (s 15(2)), procurements started before 13 May 2002 (s 26), suspension
(s 16), the breach the applicant may rely on (s 17(2)), timing and remedies
(ss 18, 19(2), 21(1)) and document retention (s 24).

Not encoded:
- which States, contracting authorities and procurements are covered. Sections 3 and 4
  leave all of this to Gazette orders, and none was retrieved;
- the procurement regulations made under s 6, so no actual breach can be tested;
- the Tribunal's constitution and powers (ss 8 to 11, 22);
- enforcement (s 20), reporting to the Minister (s 23);
- the prescribed fee and deposit amounts (s 25 regulations, not retrieved). The
  deposit figures in the cases are illustrative.

## What the Act turns out to say

### 1. A breach can never go to court, and a winner cannot get lost profit

s 7(3): a breach of the duty to follow the procurement regulations "is not to be the
subject of any proceedings in any court". It can go only to the Government
Procurement Adjudication Tribunal. The most money the Tribunal can award is the cost
of tender preparation or of taking part in supplier qualification (s 18(3)(d)), or
the costs of the challenge itself. No section gives damages for the contract that
was lost. Asserted (the forum; the remedy list).

### 2. Once the contract is awarded, the only remedy left is money

s 18(5): if the applicant wins but the contract "has already been awarded", the
Tribunal "may only" order tender or qualification costs. If the applicant had none
of those costs, it may award the costs of the challenge instead. Setting aside the
decision or amending documents is then unavailable. Read literally, an applicant who
did incur tender costs cannot also get the costs of the challenge in that case. That
sits awkwardly with the general discretion over costs in s 21(1). Asserted on the
literal reading.

### 3. Fifteen days, from the facts and not from discovery

s 12(1): the Notice of Challenge must be lodged and served, and the fee paid, within
15 days "from the date the facts constituting the basis of the challenge first took
place". A late challenge must be declared invalid (s 15(2)(f)) unless the Tribunal is
satisfied "there has been no unreasonable delay". In judging delay it must consider
when the applicant knew or ought to have known (s 15(3)). Day counting is an
inference here: the facts are day 0 and day 15 is in time. Asserted.

### 4. No deposit at lodgment, no challenge

s 13(2): if the deposit is not paid when the Notice is lodged, the challenge "is
deemed to have been withdrawn". The deposit pays any costs awarded to the contracting
authority. The authority can recover any shortfall, and any balance goes back to the
applicant (s 13(3) to (5)). Asserted, with illustrative amounts.

### 5. A suspension is lost once the contract is awarded, or on the Minister's word

s 16(3): the Tribunal "must not" suspend the procurement if suspension is against the
public interest. Nor may it if the contract is already awarded by the date of the
hearing. A Minister's certificate on the public interest is "conclusive evidence"
(s 16(8)). The Tribunal must rescind a suspension whose continuance is against the
public interest (s 16(7)). Asserted.

### 6. The Act protects only suppliers it names

The duty is owed to "relevant suppliers": nationals of Singapore or a specified
State, bodies formed under those laws **and** based in them, or suppliers named in
the order (s 2). It is also owed to anyone the Minister declares (s 7(2)(b)). A
Singapore-incorporated company based in an unlisted country is outside both limbs. A
"supplier" includes one who "would have wished" to be awarded the contract (s 2), so
a supplier who never bid can still be one. Asserted (except the would-have-wished
point, which is only quoted).

### 7. Smaller timings

The Tribunal decides within 45 days of lodgment unless there are exceptional
circumstances. That limit does not apply if the challenge was disposed of as a
preliminary issue (s 18(1), (2)). Certified copies of the decision go out within
7 days (s 19(2)). The hearing needs 14 days' notice (s 14(c)). Documents are kept
for at least 3 years (s 24). Asserted.

## What would need doing before this is worth anything

- Retrieve the Gazette orders under ss 3 and 4 (covered States, contracting
  authorities, thresholds, exclusions) and the s 6 and s 25 regulations (procedure,
  fee, deposit). Without them, coverage and breach are bare inputs.
- Check the s 18(5) and s 21(1) reading against Tribunal decisions, if any are
  published.
- Settle day counting under the Interpretation Act for ss 12, 18 and 19.
