# Parliamentary Pensions (Abolition) Act 2012 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, "incorporates all amendments up to and including
1 December 2021", as deposited at `../../registers/source-bundle/PPAA2012.txt`. The
Legislative History lists only Act 21 of 2012 itself (Bill 18/2012, passed 10 September
2012) and no later amendment.

**Checks:** one case file, 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0260** in `subjects/sg/requirements.jsonl`: Tier 4 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person it applies to; no scenario has asked a sharper question yet. The
person it applies to is a present or former Member of Parliament or political
office-holder, and anyone with a claim against their pension.

The Act is short, so this row takes nearly all of it: commencement (s 1), the
definitions (s 2), the cut-off (s 3), the conditions for a grant (s 4(1), (2)), the
stopped pension of an office-holding Member (s 4(3)), and the saving provisions of the
Schedule on assignment, corruption and bankruptcy (paras 2-4). Not encoded: s 4(4)
(subject to ss 13 and 15 of the 1978 Act, which were not read), s 6 (consequential
amendments), Schedule para 5 (pensions charged on the Pension Fund), and anything the
1978 Act itself decides, including the minimum years of service, which is a parameter
here.

## What the Act turns out to say

### 1. The repeal it is named for may never have happened

s 5(1): "The Parliamentary Pensions Act 1978 is repealed." But s 1(2) says ss 5 and 6
and the Schedule "are to come into operation on a date that the Minister appoints by
notification in the Gazette", and the deposit records no such date: the Legislative
History gives "Commencement: 21 May 2011 (except sections 7 and 8 and the Schedule)" and
nothing more. **Inference:** in this edition the 1978 Act stands, and the Schedule's
saving provisions are not yet operative. The 1978 Act is deposited elsewhere in this
repository as a 2020 Revised Edition Act, which is consistent with that. The encoding
treats ss 5, 6 and the Schedule as operating only from an appointed date that the caller
supplies. Asserted.

### 2. The cut-off was set retrospectively, nearly 16 months before the Act was passed

The Act was passed on 10 September 2012 but ss 2-4 are "deemed to have come into
operation on 21 May 2011" (s 1(1)). From that date no pension or gratuity may be granted
"in respect of" any service as a Member of Parliament or in any office (s 3). Service
that began on 20 May 2011 can count; service from 21 May 2011 cannot, and only the years
before the date count for a person whose service straddles it. Asserted.

### 3. A sitting Member with enough years still gets nothing until they leave

s 4(1), (2): a grant on or after 21 May 2011 needs both "not less than the minimum number
of years of reckonable service" under the 1978 Act and that the person "has ceased at any
time thereafter" to be a Member (or to hold any office). A Member who already had the
minimum before 21 May 2011 but keeps sitting cannot be granted a pension. A grant made
before 21 May 2011 is outside s 4(1) and (2). Asserted, with the minimum as a parameter.

### 4. An office-holder's existing pension was frozen, then paid back in full, without interest

s 4(3): a pension granted before 21 May 2011 to an office-holding Member under s 4 of the
1978 Act by virtue of its s 5 "stops on or after 21 May 2011" while the person remains an
office-holding Member; any payment in that period "must be immediately refunded to the
Pension Fund". On leaving office, all the stopped pension becomes "payable in a lump sum
(without interest)", and the pension is re-computed by adding service from the grant to
20 May 2011, never service from 21 May 2011. Asserted (the withheld sum is a caller input;
the encoding does not compute the pension).

### 5. A maintenance order can take an assignment of the pension but cannot attach it

Schedule para 2: the pension may be assigned only to satisfy a debt due to the Government
or a court order for periodical maintenance of a spouse, former spouse or minor child
"whether legitimate or not". But it "is not liable to be attached ... for or in respect of
any debt or claim whatever except a debt due to the Government". A bank or private
judgment creditor can do neither. Asserted.

### 6. Corruption can cost the pension even on a fine, but only after the President reads the record

Schedule para 3: the President may reduce or withhold the pension on a conviction under
the Prevention of Corruption Act 1960 or for corruption under any other written law, "even
if only a fine and no term of imprisonment has been imposed", and must first "consider the
record of the proceedings of the court". The President may redirect the pension to the
wife and children, and to the person only "after the expiry of any term of imprisonment".
**Inference:** with no imprisonment there is no term to wait for. Asserted.

### 7. Bankruptcy anywhere stops the pension; discharge restores it

Schedule para 4: bankruptcy or insolvency by judgment "in Singapore or elsewhere" ends the
pension "forthwith"; a "full and proper discharge" restores it from the date of discharge.
Meanwhile the President may direct the money to the person, his wife, children or other
dependants, and paying the person's debts counts as applying it for his benefit. Asserted.

### 8. The section numbers in the enacting note are the old ones

The note under the long title, and the Legislative History, say "Except sections 7 and 8
and the Schedule"; s 1(1) itself says "with the exception of sections 5 and 6". The
Comparative Table explains it: the 2020 Edition's ss 5 and 6 were ss 7 and 8 of Act 21 of
2012, and the original ss 5 and 6(1) were "[Omitted as having had effect]". Not asserted.

## What would need doing before this is worth anything

- Read the Parliamentary Pensions Act 1978 (ss 3, 4, 5, 13, 15) to fix the minimum years,
  what "by virtue of section 5" covers and how s 4(4) qualifies s 4.
- Confirm from the Gazette whether a date has been appointed under s 1(2).
- Days and amounts are caller inputs; the encoding does not count the inclusive periods in
  s 4(3) or compute a pension.
- No case law or parliamentary debate was searched.
