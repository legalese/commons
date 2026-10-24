# Customs Tariff Act 1995 — traveller and small importer baseline

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; a question that reaches a gap answers `not covered`, naming it, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0078` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep. No scenario raised it; every case is hypothetical.

**Added 24 October 2026 (REQ-0112):** `cta-by-laws.l4`, a module beside `cta-importer.l4` that IMPORTs it, reads the deposited Customs By-Laws 2023 for Schedule 4 items 17, 25, 26, 28 and 37: whether the goods are prescribed (five questions) and, for items 26 and 37, whether the concession then applies (two questions, through `Does a concession apply to my goods`). Nothing in `cta-importer.l4` was changed.

## Edition

**Compilation No. 100**, compilation date 4 July 2026, includes amendments up to Act No. 67, 2026 (register id C2026C00399, seven volumes), as deposited at `../../registers/source-bundle/C2004A04997.txt` (76,562 lines; Schedule 3 at lines 1134–30111, Schedule 4 at 30112–30499).

`cta-by-laws.l4` reads the **Customs By-Laws 2023** (F2023L00366, made under s 271 of the Customs Act 1901), Compilation No. 6 (F2026C00194, compilation date 17 February 2026, includes amendments up to F2026L00107; retrieved 23 October 2026), deposited at `../../../customs-by-laws-2023/registers/source-bundle/F2023L00366.txt`.

In `cta-importer.l4`, no instrument is brought in. The Customs By-laws that "prescribe" goods for most Schedule 4 items, the Customs Tariff Regulations that list the Forum Island, Developing and Least Developed Countries (s 12), and the Customs Act's rules of origin and valuation are not deposited here; each is asked as a fact.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `cta-importer.l4` | `cta-cases-importer.l4` | 34 written, 34 satisfied |
| `cta-by-laws.l4` | `cta-cases-by-laws.l4` | 33 written, 33 satisfied |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text: the rate in the third column of each Schedule 3 line and Schedule 4 item.

## Seat

**The traveller or small importer**: a person bringing goods into Australia or ordering them from overseas. The questions are that person's: "What is the general rate for my goods?", "What rate applies, given where they come from?", "Does a Schedule 4 concession make them free or cheaper?", "How much duty is that?".

The Act addresses no one directly; it imposes duties (s 15). The Comptroller-General's and the Collector's decisions (s 9(2); Schedule 4 item 24) are asked as facts.

The 2026-10-18 defaults:

- **The Act alone.** Followed. The by-laws and regulations the Act points to are not deposited; asked as facts.
- **The actors the text names:** the importer, the Comptroller-General of Customs, the Collector.
- **Judgments handed to others are answered conditionally:** the tariff classification (the Interpretation Rules, s 7, Schedule 2), whether goods are originating goods (the Customs Act), whether a by-law prescribes them, whether the Collector is satisfied (item 24).
- **The Act's own definitions are worked out from facts:** which paragraph of s 16(1) applies and the least-duty rule (s 16(5)); when a Schedule 4 item applies (ss 8, 18(1)); duty on an ad valorem rate (s 9).
- **One case:** one consignment of one kind of goods.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** ss 1–3A, 20A–22.

## Read with the Customs Act 1901 baseline

`../../../customs-act-1901/encodings/baseline-2026-10/` answers the incoming passenger's questions — the passenger concession (this Act's Schedule 4 item 15, which it brings in together with s 18), the incoming passenger card, prohibited imports, and the penalties for a false card or smuggling. None of it is restated here: item 15 answers `not covered` in this encoding, naming that baseline. The stable `l4` cannot IMPORT across encoding folders, so the link is recorded here and in the module header, not in code. Both encodings apply s 18 the same way: a concessional item applies only if it gives less duty.

## Scope

**In:** ss 6, 7 (as a fact), 8(1), 9(1), 10(1), 14(1)(a), (i), 15, 16(1)(a), (b), (d), (ja)–(v), 16(5), 18(1); nine representative Schedule 3 lines; Schedule 4 items 17, 18, 24, 25, 26, 28, 36 and 37.

**The nine Schedule 3 lines** (the deposit's line number, the rate as printed):

| Line | Goods | Rate |
|---|---|---|
| 8471.30.00 (24638) | portable computers of 10 kg or less | Free |
| 8517.13.00 (25871) | smartphones | Free |
| 6109.10.00 (17358) | T-shirts, singlets and vests of cotton, knitted or crocheted | 5% |
| 4202.21.00 (12025) | handbags with an outer surface of leather | 5% |
| 9503.00.20 (29555) | dolls representing human beings | 5% CA:Free |
| 8711.60.00 (27836) | motorcycles and cycles with an electric motor | 5% DCS:4% DCT:5% |
| 8703.80.11 (27330) | electric passenger cars, used | 5% CA:Free |
| 8703.80.12 (27333) | electric passenger cars, NSA, below the fuel-efficient car limit | Free |
| 8703.80.19 (27336) | other electric passenger cars | 5% CA:Free |

**Out:** the rest of Schedule 3 (`not covered`); the other preferences of s 16(1) (Papua New Guinea, Forum Island, Developing and Least Developed Countries: `not covered`); the free trade schedules' tables themselves (whether one lists a classification, and its rate, is asked); s 9(2); s 11 (phasing rates); ss 16A–16B, 17, 18A–18B, 19–19AD (indexation of alcohol, tobacco and fuel rates), 20; Schedule 4 item 15 (the Customs Act baseline's) and the items not listed above; s 8(2) (choosing between two items).

## What the Act turns out to say

1. **Finding a rate is a chain of three steps.** Classify the goods under Schedule 3 with the Interpretation Rules (ss 6–7); take the rate that applies to their origin (s 16(1)), and where more than one paragraph applies the one with the least duty (s 16(5)); then check whether a Schedule 4 item gives less (s 18(1)). Asserted.
2. **Free trade partners' goods are Free unless the partner's schedule lists them.** Every free trade paragraph of s 16(1) ((ja)–(v)) says: the rate in the partner's schedule if the classification is listed there, "otherwise—Free". New Zealand originating goods are Free unless the line sets an NZ rate (s 16(1)(b)); none of the nine lines does. Asserted (with the listing as an input).
3. **Canada is the odd one out.** Goods made in Canada get the CA rate only where the line sets one, and otherwise the general rate, not Free (s 16(1)(d)): a Canadian doll is Free, a Canadian handbag 5%. Asserted.
4. **A concession that gives no less duty does not apply.** Section 18(1): a Schedule 4 item "only applies ... if the duty payable ... under that item is less". A used electric car under item 37 (5%) gains nothing over 8703.80.11 (5%); a car 30 or more years old is Free under item 36 whatever it is. Asserted.
5. **Most of the useful concessions depend on a by-law.** Items 15, 17, 25, 26, 28 and 37 apply only to goods "as prescribed by by-law", and item 26's low-value threshold is "the amount prescribed by by-law". The by-laws are not deposited, so REQ-0112 asks for them. Items 18 (warranty), 24 (inheritance) and 36 (old cars) stand on the Act's own words. Asserted (with the by-law as an input).
6. **Electric passenger cars below the fuel-efficient car limit are Free.** Subheading 8703.80.12 covers new ("NSA") electric passenger cars "with a value less than the fuel-efficient car limit" (Additional Note 6 to Chapter 87), at Free; others are 5%. The limit is an Additional Note figure not encoded here; which subheading applies is the classification input. Asserted.
7. **The Act sets customs duty only.** GST, luxury car tax and the excise-equivalent duties on alcohol, tobacco and fuel (the s 19 family) are other rates or other Acts. Not asserted.

8. **Goods of low value means $1,000 or less, but not for passengers, alcohol, tobacco or bulk orders.** By-Laws s 36(2) prescribes goods "the value of which is less than $1000.01"; (3) excludes tobacco, tobacco products and alcoholic beverages, goods a passenger or crew member brings in, and goods forming part of a bulk order. The compilation prints two paragraphs "(a)"; both are read. Asserted.
9. **A used car needs a written import approval.** By-Laws s 59 prescribes for item 37 only used or second-hand passenger motor vehicles under heading 8703 (not ambulances, hearses, police vans, amphibious or off-road vehicles), on condition of a written import approval under the Road Vehicle Standards Rules 2019. Asserted.
10. **Item 28 is narrow.** By-Laws s 38 prescribes four kinds of aid only: braille tiles and road rivets designed for the blind; reading machines turning print into tactile images or speech; reading systems that enlarge print on a screen; and sound reproducers and recorders meeting seven conditions (under 2.5 W, magnetic tape, monophonic, DC or AC/DC, hand-carried, colour-coded raised keys, dual speeds). A wheelchair or hearing aid is not prescribed by it. Asserted.
11. **Item 25's by-law for trophies won overseas lists two conditions joined by "and".** Section 35(2) says "each of the following are goods to which that paragraph of the item applies: (a) the goods are trophies won outside of Australia in competition; and (b) the trophies are appliances or articles of a kind used in an office or the household". Read as written, a trophy qualifies only if it is also an office or household article; a reading that treats (a) and (b) as two classes would admit any trophy won overseas. The encoding takes the conjunctive reading. Asserted.
12. **The general passenger concession (item 15) is not in the By-Laws 2023.** They prescribe for item 15 only motor vehicles of Canadian and United Kingdom forces (s 25, item 15(d)). The by-law that sets the duty-free amounts for travellers was not found among the in-force instruments searched (titles containing "Customs By-law", "Customs (International Obligations) By-Laws 2023", and "Passenger"); the Customs Act 1901 baseline still asks its figures as inputs. A new ledger entry, REQ-0114, asks for it. Not asserted (a finding about the sources).
13. **Item 17 is prescribed only for the Antarctic.** The By-Laws 2023 prescribe for item 17 only goods temporarily exported to the Australian Antarctic Territory or Heard Island and McDonald Islands and returned unaltered (s 28). Goods taken anywhere else and brought back are not prescribed by them; item 18 (warranty repair or replacement) and the general rules may still help. Asserted.

## What would need doing before this is worth relying on

- **The Customs By-laws** for Schedule 4: the By-Laws 2023 are deposited and used for items 17, 25, 26, 28 and 37 (REQ-0112, `cta-by-laws.l4`); the by-law setting the item 15 passenger concession is still to be found and deposited (finding 12), as are any by-laws for items 17 and 28 outside the 2023 consolidation.
- **The rest of Schedule 3**, ideally as data rather than code, with the phasing dates of s 11.
- **The free trade schedules** (Schedules 4A–16) as data, and the rules of origin in the Customs Act.
- **The Customs Tariff Regulations** listing the preference countries (s 12).
- **The indexed alcohol, tobacco and fuel rates** (ss 19–19AD), which a traveller over the duty-free allowance meets.
- **Customs rulings and case law** on classification were not read.
