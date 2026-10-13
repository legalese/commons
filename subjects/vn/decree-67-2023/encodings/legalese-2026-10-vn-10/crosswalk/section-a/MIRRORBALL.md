# MIRRORBALL on Section A, 2026-10-13

MIRRORBALL added three tests to the remaining Phase 2 work on the Decree 67/2023 crosswalk:
- (a) run each total map in both directions, and report the fragment on which the directions agree;
- (b) check every constructor combination of the finite enumerations, with amounts at their boundaries;
- (c) compare state graphs.

This file reports (a) and (b) on Section A.
(c) does not apply here: neither the join nor VN-29 has a regulative rule (`PARTY … MUST`) or a `#TRACE`.
(c) was tried on other encodings in a private record.

## Limits

- The expected value of every assertion was computed by `gen_mirrorball_section_a.py`, in this directory, from one reader's reading of the decree and the Law, with citations in the generator.
  That reader is a Claude Code session, not a lawyer, and had read VN-10 and the join before writing the oracle.
  Where the encodings and the oracle agree, they can be wrong in the same way.
- Some properties are close to tautologies.
  For example, the join's A03 passes VN-10's own Art 3(5)(a) answer to the Law's record.
  What (b1) tests is that answer's passage through VN-29's Điều 58(1), in every combination; it does not test VN-10's reading of Art 3(5)(a).
- (b3) fixes each class's argument (seats, cylinder capacity, payload) at one value. Annex I's own bands are VN-10's tests, not these.
- Whether the last day of the insurance term is inside it is the join's reading (both ends inclusive), assumed, not ruled. The four boundary assertions pin that reading; they do not test it against the text.
- This was done by hand in an interactive session, not by a headless run, so no CLI cost estimate covers it.

## How it was run

```
$ python3 -I gen_mirrorball_section_a.py
wrote nd67-law08-mirrorball-join.l4: (b) 454 assertions, of which 0 pin a disagreement with the oracle; (a) 61 assertions; (a2) fragment 4 of 16: [...]
$ bash check.sh
copies: 17 match their digests; [...]
module                                errors satisfied  failed  refused not-total-warn imported-warn
nd67-law08-join.l4                         0       152       0        0              0             0
nd67-law08-mirrorball-join.l4              0       515       0        0              0             0
```

- `l4` sha256: `0eb98517a791f5d86b83add8e76666434b9c6dd2e6806c84e7b2bbebc9ca6b2d`.
- `nd67-law08-mirrorball-join.l4` is generated; edit the generator instead.
- It imports `nd67-law08-join.l4` and leaves it unchanged, and builds its fixtures from the join's own record literals.
- Seven single-line mutations, one in each of (b1) third party, (b1) term edge, (b2), (b3), (b4), (a2) and (a4), each turned exactly one assertion red.

## (b) Every combination: 454 assertions

| Part | What is enumerated | Assertions | Result |
| --- | --- | ---: | --- |
| b1 | A03 and A16: the harmed person's four roles (driving, on the vehicle, passenger, owner) × the owner's hand-over × the two decree vintages, plus four dates at the edges of the insurance term | 132 | all agree with the oracle |
| b2 | A07: health and life, and property damage by each of 32 vehicle classes (16 base classes, and a driving-school vehicle of each) × the amount owed at 0, the limit less 1, the limit, and the limit plus 1; each also checked against VN-10's Art 12(8) | 132 | all agree |
| b3 | A06: the same 32 classes × the premium paid at the edges of Art 8(2)'s ±15% band | 166 | all agree, after a fix to the join (below); 13 disagreed before it |
| b4 | A01 and A02: the four parties the decree names × premium paid or unpaid, against Điều 4(24), 4(25) and 4(26) | 24 | all agree |

Two things came out of (b3).

1. **The generator's first run had 65 failures, all of them the oracle's mistake.**
   The oracle gave every driving-school vehicle an Annex I premium.
   Annex I VII.1 prices a driving-school vehicle at 120% of "xe cùng chủng loại quy định mục IV và mục VI" (decree67:2101-2103), so it fixes no premium for a driving-school motorcycle, moped, taxi, bus and the like.
   VN-10 reads it that way.
   The oracle was corrected.
   The 65 failures were 13 classes × 5 amounts, and they are recorded in the generator's comment.
2. **For those 13 classes, the join disagreed with the Law's text, and has been fixed.**
   The decree fixes no premium for them.
   The join set VN-29's single flag, "required by law or agreed by the parties", from the decree alone.
   It therefore answered that a premium the parties agreed and the buyer paid is not the Law's premium.
   Điều 4(28) says it is: "theo quy định của pháp luật hoặc do các bên thỏa thuận trong hợp đồng bảo hiểm" (law08:184-185).
   The first version of this file pinned the join's answer in 13 assertions and classed it `wrong map`.
   On 2026-10-13 the join's A06 was changed to read a premium paid under the contract as agreed by the parties (assumed, not ruled), and the 13 assertions now expect the oracle's answer.
   Run against the join as it was, they fail, and nothing else does.

## (a) Both directions: 61 assertions

Section A has two maps that are total over a type of constructors:
- A01/A02, from a party to the claim to a role in a contract;
- A07, from a harm Article 6 limits to its limit.

The generator writes an inverse for each, assumed, not ruled, and stated in the module.
It then sends VN-29's own test fixtures back through the inverse into VN-10, forward again, and compares the Law's answers.

| Part | What | Result |
| --- | --- | --- |
| a1 | VN-29's four role fixtures (`law08-tests-ch1.l4`, Điều 4(24)-(26)) | 1 of 4 keeps its Law statuses (`a person whose life is insured`). Two do not: a buyer who pays but holds no insured interest, and a person who contracts while another pays. `a designated recipient` has no preimage: the decree designates no one. |
| a2 | all 16 role records | the agreeing fragment is 4 of 16: the empty role; the insured interest alone; contract and insured interest, unpaid; contract, payment and insured interest |
| a3 | the four decree parties, sent to the Law and back | 2 of 4 return as themselves. The vehicle owner returns as the buyer-or-insured, and the insurer as the injured person, because the forward map sends each pair to one role. |
| a4 | VN-29's four Điều 59 fixtures (`law08-tests-ch2-property.l4`) | none has a preimage: each has a limit of 500,000,000, which no Article 6 harm has, so the fragment is empty |
| a5 | every decree harm, owed 1 đồng above its limit, through the Law and back | the total survives in all 33; the inverse recovers the limit, not the vehicle class |

**The agreeing fragment.**
For roles it is 4 of 16 role records and 2 of 4 decree parties.
For limits it is every harm on the decree's side, and none of VN-29's own Điều 59 tests.

**What it adds to the table.**
VN-29's own tests of Điều 4 sit almost entirely where VN-10 cannot follow them.
That is because of the buyer-insured merge and the decree's silence on designation, which `SECTION-A.md` already describes in A01, A02 and A14; here the gap is measured.
VN-29's Điều 59 tests use a limit the decree never sets.
So running the Law's tests back into the decree checks nothing for Điều 59, and only one of four role fixtures for Điều 4.
