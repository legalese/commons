# Section A: Decree 67/2023 against the Law on Insurance Business 08/2022/QH15, and the join that checks it

This is Section A of the crosswalk between VN-10 (the decree's motor chapter, `nd67-*.l4`) and VN-29 (the Law, `law08-*.l4`).
The table in §1 is the crosswalk; `nd67-law08-join.l4` is its checked form.
A citation `decree67:N` is line N of the decree's gazette text (sha256 `27a63429c12aba7e65f1c157ee3202407f6fbf517374ca77e8699111d3700c15`); `law08:N` is line N of the Law's text (sha256 `c6de2c5aa59a6d4861e9c98cd0cba4ac3a9b22d442a4a580cc45123dda843099`); `decree220:N` is line N of Decree 220/2026's text (sha256 `3ed3bca14a5cd0e11d971578e893c5dc6c0dfac6fbb92f14f6450bc7e24bfa5a`). The run read them as `../reference/decree67.txt`, `law08.txt` and `decree220.txt`, the names §0's commands use.
Nothing here is legal advice, and no Vietnamese-qualified lawyer has read it.
It was drafted by one model session, not by two independent ones, and the precondition its plan set, an independent test pass of VN-29's Article 4 and Chapter II, has not been met.

## §0. The checks

To re-run both checks of the join here: `bash check.sh` in this directory (it also checks the copies of VN-10's and VN-29's modules listed in `COPIES`).
The last output of `bash ../check.sh .` (run in the deposit directory, after the last edit to the join):

```
module                                errors satisfied  failed  refused not-total-warn imported-warn
nd67-law08-join.l4                         0       152       0        0              0             0
(any error, failed or refused assertion, or a CONSIDER in a join module that is not total, makes the run red)
```

The last output of `python3 -I ../vnsrc.py check ../reference/both.txt SECTION-A.md nd67-law08-join.l4`:

```
vnsrc check: 0 src: lines, 61 Vietnamese runs, 0 problems
```

Both pass.
One of the brief's rules could not be followed to the letter, because the brief named a form of qualified name that `l4` does not have.

**Rule 2 (qualify a shared name with the module name) could not be followed as written.**
I tried, for the module `nd67-vn10-nouns` and for `law08-nouns`, these spellings of a qualified name: the module name, a dot, the name; the file name with `.l4`, a dot, the name; the module name, the `§` heading, the name; the module name, the `§` heading, the `§§` heading, the name.
Every one failed with "I could not find a definition for the identifier".
(Corrected after the run, when this file was filed: an `l4` qualified name is the chain of section headings above the definition in its own file, without the module name, and that form resolves here, for example ``` `Nouns for Law 08/2022/QH15`.`Chuong II: the contract of insurance`.`the insurer` ```. The join does not use it; the typed aliases below do the same work.)
The only name the two encodings both declare is the constructor `the insurer` (VN-10: `A party to the claim`; VN-29: `A party to the contract`); I compared every `DECLARE` name, every constructor name and every function name of the two sets.
`l4` reports `the insurer` as ambiguous only where nothing fixes its type (provoked with `#CHECK`); everywhere the join uses it, the type is fixed by a `CONSIDER` scrutinee, a `GIVETH`, or an argument position, and the run has no ambiguity error.
The join also names the two apart with typed aliases, `the decree's insurer` and `the Law's insurer`, and uses the alias where it passes the constructor as an argument.

**How the file was made.**
The fixtures and the field lists of the VN-29 records are expanded from the field lists in the two nouns modules by a scratch script, so that no field of a record is left out silently; the script is deleted, and the join is plain L4.
I mutation-tested the assertions: ten deliberately wrong assertions (a driver as a third party, an unpaid buyer as a policyholder, a wrong refusal reason, a wrong total and so on) each failed, and the 152 real ones still passed.
`#ASSERT` has no name in L4, so each block of assertions carries a label in a comment, `[A03.2]` and so on, and §1 and §3 cite those labels with the join's line numbers.

**What the Law vintages rest on.**
Law 139/2025/QH15, which makes V2 and V3, is not among the files I was given; the vintages are VN-29's encoding of it.
Where §1 says a row holds in V1, V2 and V3, that means VN-29 gives the predicate one arm only (in `law08-ch1-general.l4` the only vintage tests are in Dieu 3, 6, 8, 9, 11 and 13, and none in Dieu 4, which runs from line 110 to line 513; `law08-ch2-general.l4` and `law08-ch2-property.l4` have none), and each row's standard-case assertion is run at V1 (2025-06-01), V2 (2026-03-01) and V3 (2026-08-01) to show it.
V1 runs from 2023-01-01, V2 from 2026-01-01, V3 from 2026-07-01 (`law08-vintage.l4`).
Decree 220/2026 takes effect on 2026-07-01 (decree220:195); in the motor chapter it replaces one word (decree220:172-178).
The join takes the decree's vintage and the Law's vintage as two independent inputs and does not check that a pair of them can coexist.

## §1. The Section A table

How to read the relation column: it measures the decree's term against the Law's.
`same` means the decree uses the Law's term in the Law's sense; `narrower` means every case of the decree's term is a case of the Law's and not the reverse; `wider` means the reverse; `differs in scope` means each reaches cases the other does not, or they answer different questions; `no counterpart` means the Law has the provision and the decree has nothing that does its work.
The "VN-10 identifier" and "VN-29 identifier" columns give names from the `.l4` modules.
Each row of the last-but-one column starts with the row's id, which is also the id of the labels in the join.

| the decree's term | decree67 line | the Law's term | law08 line | relation | the Law vintages the row holds in | VN-10 identifier | VN-29 identifier | the join's function and assertions | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bên mua bảo hiểm | 104 | Bên mua bảo hiểm | 167 | narrower | V1, V2, V3 | `the insurance buyer or the insured`, `the vehicle owner` (`A party to the claim`) | `A role in a contract`; `Dieu 4(24): the person is the policyholder (ben mua bao hiem)` | **A01**: `the Law's role for the decree's insurance buyer`; [A01.1]-[A01.3], lines 561-572 | The decree coins the term as a short name for the persons of Art 2(1)-(3) who must buy (decree67:103-106), that is by status; the Law defines it by two acts, concluding the contract and paying the premium. An owner who has not paid is the decree's buyer and not yet the Law's (A01.2). |
| người được bảo hiểm | 295 | Người được bảo hiểm | 170 | same | V1, V2, V3 | `the insurance buyer or the insured` (`A party to the claim`) | `A role in a contract`; `Dieu 4(25): the person is the insured person (nguoi duoc bao hiem)` | **A02**: `the Law's role for the decree's insured`; [A02.1]-[A02.4], lines 574-587 | The decree never defines it and uses the Law's sense: the owner, whose civil liability Art 5 insures (decree67:183-186). VN-10 merges it with the buyer, so one record satisfies both Dieu 4(24) and 4(25) (A02.3); the merge is faithful only while buyer and insured are one person. |
| Người thứ ba | 84-89 | người thứ ba | 129 | narrower | V1, V2, V3 | `Article 3(5)(a) — a third party`; `A person harmed in the accident` | `A liability contract and a claim`; `Dieu 58(1): the insurer's liability arises`; `Dieu 58(2): the third person may claim directly from the insurer` | **A03**: `the Law's liability claim of the decree's third party`; [A03.1]-[A03.7], lines 655-682 | The Law uses the term without defining it (law08:129, 715-717, 1076-1124). The decree defines it for this insurance with four exceptions: the driver, the persons on the vehicle, the passengers on that vehicle, and the owner unless the owner has handed the vehicle to another (decree67:85-89). VN-29 has no record of a third person, so the join builds the Law's liability claim and lets the decree say who counts. |
| bên thứ ba | 84-89 (word replaced by decree220:173-175) | người thứ ba | 129 | narrower | V1, V2, V3 | `the term for the third party in`; `the vintage that governs`; `Article 3(5)(a) — a third party` | `A liability contract and a claim`; `Dieu 58(1): the insurer's liability arises` | **A04**: `the Law's liability claim of the third party under the contract`; [A04.1]-[A04.3], lines 684-697; the amended-vintage carve-outs are in [A03.4] | From 1 July 2026 Decree 220 Art 9(1) replaces the word in Art 3(5), 5, 7(1)(a), 10(2), 12(2), 12(6)(a) and 13(5) and changes no other word of the definition. The Law keeps its own word, and uses "bên thứ ba" (law08:290, 2864) for a recipient of confidential information. |
| vụ tai nạn | 318 | Sự kiện bảo hiểm | 178 | wider | V1, V2, V3 | `An accident`; `Article 7 — the answer on cover for the health and life of`; `The answer on cover` | `An occurrence`; `Dieu 4(27): the occurrence is an insured event (su kien bao hiem)` | **A05**: `the Law's occurrence made by the decree's accident, as it harmed`; [A05.1]-[A05.6], lines 737-761 | The decree's trigger is the accident, including one not yet found within cover (the advance of Art 12(3)(b), decree67:325-330). The Law's insured event is the accident that obliges the insurer. The decree uses "sự kiện bảo hiểm" once in the motor chapter, in Art 12(7) (decree67:382), for the accident. |
| Mức phí bảo hiểm | 232 | Phí bảo hiểm | 182 | narrower | V1, V2, V3 | `Annex I — the premium for the term of`; `Article 8(2) — the premium after an adjustment of` | `A payment`; `Dieu 4(28): the payment is insurance premium (phi bao hiem)` | **A06**: `the Law's payment made for the decree's premium under`; helper `the decree's verdict on the premium actually paid under`; [A06.1]-[A06.5], lines 784-796 | The decree's term is a level, fixed by Annex I and movable by at most 15% (decree67:233-238); the Law's is the sum, whatever the parties agree. A sum outside the band is still the Law's premium (A06.3). |
| Giới hạn trách nhiệm bảo hiểm | 187 | Giới hạn trách nhiệm bảo hiểm | 1090-1091 | differs in scope | V1, V2, V3 | `Article 6(1) — the limit for health and life, per person per accident`; `Article 6(2) — the limit for property, per accident, for a vehicle of class`; `Article 12(8) — the compensation within the limit` | `A liability contract and a claim` (field `limit of liability`); `Dieu 59(2)-(4): the total the insurer pays` | **A07**: `the Law's liability claim under the decree's limit for`; [A07.1]-[A07.5], lines 834-850 | The decree fixes two limits, per person per accident for health and life and per accident for property by kind of vehicle (decree67:188-196); the Law's is one sum the insurer pays the insured under the contract, with no "per person" (law08:1091-1107). |
| bảo hiểm bắt buộc | 104-105 | Bảo hiểm bắt buộc | 226-229 | narrower | V1, V2, V3 (limb (a) only; limb (c) changes wording in V2) | `Article 4(3) — the insurer has separated the compulsory part as required`; `Article 4(1) — the person must buy the compulsory motor insurance` | `A product for the purposes of compulsory insurance`; `Dieu 8(2): the product is compulsory insurance` | **A08**: `the Law's product that the decree's part of the cover is`; [A08.1]-[A08.3], lines 882-892 | The decree regulates three of the compulsory insurances; the motor one is the Law's Dieu 8(2)(a). The decree is the Government's rule under Dieu 8(5) (law08:244-245), which VN-29 declines for want of that decree. The extension the parties may agree beside it (decree67:112-118) is not compulsory insurance. |
| Hồ sơ bồi thường bảo hiểm | 401 | Thời hạn nộp hồ sơ yêu cầu bồi thường, trả tiền bảo hiểm | 706 | no counterpart | V1, V2, V3 | `A claim file`; `An accident` (field `date of the accident`) | `A claim`; `Dieu 30: the dossier was submitted in time` | **A09**: `the Law's claim made on the decree's accident, with the dossier submitted on`; [A09.1]-[A09.3], lines 918-927 | The decree lists the documents of the claim file (decree67:401-450) and sets no time to file it; Art 12(4) times the notice of the accident (5 working days, decree67:335-338), which is not the claim. The Law's one year runs from the decree's own date of the accident. |
| tạm ứng bồi thường | 318-319 | Thời hạn bồi thường, trả tiền bảo hiểm | 718 | no counterpart | V1, V2, V3 | `Article 12(3) — the advance for`; `An accident` | `A claim`; `Dieu 31(1): the last day for the insurer to pay`; `Dieu 31(2): the days of delay` | **A10**: `the Law's claim made on the decree's accident, received and paid`; [A10.1]-[A10.3], lines 955-964 | The decree's 3-working-day deadline binds the advance for harm to health and life only; it sets no time for paying the compensation itself. The Law's agreed time, or 15 days from the full dossier, fills the gap (law08:719-724), and its interest (law08:725-729) has no rate in either text. |
| Phụ lục I | 233-234 | phương pháp, cơ sở tính phí bảo hiểm | 1776-1782 (the words at 1790-1791) | no counterpart | V1; V2, V3 for the voluntary motor line | `Annex I section A — the premium for a 1-year term, VAT not included, for`; `Article 4(3) — the insurer has separated the compulsory part as required` | `A premium method`; `A product line for premium rules`; `Dieu 87(3)-(3a): the premium method meets the requirement that applies to its product line` | **A11**: `the Law's premium method for the decree's part of the cover`; [A11.1]-[A11.2], lines 991-1001 | The decree fixes the premium by table, so there is no method to register; Dieu 87(3) names motor vehicle insurance and excepts compulsory civil liability insurance of motor vehicle owners. In V2 (Law 139/2025 Dieu 87(3a)) the other motor insurance moves from registration and approval to written notice, so the extension of Art 4(3) changes regime on 2026-01-01 and the compulsory part never has one. |
| hợp đồng bảo hiểm | 124 | Hợp đồng bảo hiểm | 132 | same | V1, V2, V3 | `A contract of compulsory motor insurance` | `A contract arrangement`; `Dieu 4(16): the arrangement is a contract of insurance` | **A12 (added)**: `the Law's contract arrangement made by the decree's contract`; [A12.1]-[A12.4], lines 1025-1035 | The decree uses the term throughout and never defines it. It restricts the term (Art 9), the number of contracts per vehicle (Art 4(4), 12(9)) and the refund (Art 11); none of those makes an agreement cease to be a contract of insurance (A12.2, A12.3). |
| từ chối bán bảo hiểm bắt buộc | 125-128 | không được từ chối bán | 241 | differs in scope | V1, V2, V3 | `Article 4(5)(a) — the insurer may refuse to sell the insurance for`; `A motor vehicle` | `A sale of compulsory insurance`; `Dieu 8(4): the refusal to sell breaches Dieu 8(4)`; `Dieu 8(3): the buyer is bound to buy compulsory insurance` | **A13 (added)**: `the Law's sale of compulsory insurance of the decree's vehicle`; [A13.1]-[A13.3], lines 1053-1061 | The decree gives the insurer a right to refuse for a vehicle past its service life; the Law forbids refusing a buyer who meets the legal conditions (law08:240-243). The two agree only if the right to refuse is read as a condition of buying (see §3). |
| người bị thiệt hại | 343 | Người thụ hưởng | 175 | differs in scope | V1, V2, V3 | `Article 12(5) — the insurer pays`; `the injured person` | `A role in a contract`; `Dieu 4(26): the person is a beneficiary (nguoi thu huong)` | **A14 (added)**: `the Law's role of the person the decree has paid, designated or not`; [A14.1]-[A14.3], lines 1090-1099 | Art 12(5) pays the injured person directly when the insured has died or lost civil capacity (decree67:344-349), by the rule's own operation; the Law's beneficiary is designated by the buyer or the insured (law08:175-177), and the decree designates no one. |
| doanh nghiệp bảo hiểm | 65-66 | Doanh nghiệp bảo hiểm | 138 | differs in scope | V1, V2, V3 | `the insurer` (`A party to the claim`) | `An enterprise`; `Dieu 4(17): the enterprise is an insurer (doanh nghiep bao hiem)`; `Dieu 4(19): the enterprise is a branch of a foreign non-life insurer` | **A15 (added)**: `the Law's enterprise for the decree's insurer`; [A15.1]-[A15.4], lines 1135-1151 | Art 2(4) coins the short name for non-life insurers and branches of foreign non-life insurers together (decree67:65-66). The Law's term covers life, non-life and health insurers and keeps the branch as a separate category (law08:138-151), so the decree's term is narrower on one axis and wider on the other. |
| Đối tượng bảo hiểm | 183 | Đối tượng bảo hiểm | 1076 | wider | V1, V2, V3 | `Article 5 — the owner's insured liability is owed to` | `Dieu 57: the object of insurance of a liability contract`; `A liability contract and a claim`; `Dieu 58(1): the insurer's liability arises` | **A16 (added)**: `the Law's liability claim of a person the owner's insured liability is owed to`; [A16.1]-[A16.3], lines 699-714 | The decree's object is the owner's civil liability to third parties and to passengers (decree67:184-186); the Law's object for a liability contract is liability to a third person (law08:1077-1078). The passenger is outside the decree's own definition of the third party and inside its object. |

## §2. The rows I added to the seed list, and why

The seed list gave these terms: the buyer and the insured, the third party, the insured event against the accident, the premium against Annex I, the limit, compulsory insurance, the deadlines of Dieu 30 and 31, and the premium methods of Dieu 87(3).
Three seed bullets became more than one row, because the Vietnamese terms differ: A02 (the insured is a separate term from the buyer, as the seed itself lists them), A04 (Decree 220's "bên thứ ba" is a different word from "người thứ ba", with its own vintage), and A10 (Dieu 30 and Dieu 31 are separate provisions with separate records, and the decree meets them differently).
Five rows are new terms I found that the decree takes from the Law:

- **A12, hợp đồng bảo hiểm (Dieu 4(16)).** The decree builds every rule on "the insurance contract" (Art 4(3), 4(4), 9, 11, 12(9)) and defines it nowhere; the Law defines it in Dieu 4 beside the terms the seed already lists.
- **A13, từ chối bán bảo hiểm bắt buộc against Dieu 8(4).** VN-10's own comment on Art 4(5)(a) says "the two agree"; that is a join claim, and it needed a row to be tested.
- **A14, the person paid (người bị thiệt hại) set beside the beneficiary (người thụ hưởng) of Dieu 4(26).** The decree pays the injured person directly in one case; the Law's only defined payee status other than the insured is the beneficiary, and the question whether the injured person is one needed an answer.
- **A15, doanh nghiệp bảo hiểm (Dieu 4(17), 4(19)).** Art 2(4) coins the decree's short name for the insurer; it is the only definition in the decree's Art 2 that cuts across the Law's categories.
- **A16, Đối tượng bảo hiểm (Dieu 57).** The seed's third-party row cannot be decided without it: Art 5 insures liability to passengers, and Dieu 57 insures liability to "người thứ ba", so the object of the insurance is where the two meet.

I looked for and did not add rows for: "chủ xe cơ giới" (the decree's own definition, Art 3(1); the Law has no counterpart); "thời hạn bảo hiểm" and "Giấy chứng nhận bảo hiểm" (the Law has no Dieu 4 definition of either; Dieu 18 names the certificate only as evidence of the contract, law08:427-430); "thông báo" of the accident against Dieu 46 (a real pair, the decree's 5 working days against the Law's "time agreed in the contract" at law08:917-925, left for a later row).

## §3. What the join shows that the table alone does not

The brackets hold the join's labels; a line number is the line of the label's comment in `nd67-law08-join.l4`, and a range runs from a block's first label to its last assertion.

1. **One decree party satisfies two Law statuses; the join shows the Law's split mattering in one case, an unpaid premium.**
   `the insurance buyer or the insured` yields a record of which both Dieu 4(24) and Dieu 4(25) hold ([A02.3], line 580).
   An owner whose premium is unpaid is the Law's insured person and not the Law's policyholder ([A02.3], line 580, second assertion; [A01.2], line 564), although the decree makes that owner the "bên mua bảo hiểm" by status.
   VN-10 cannot say "a buyer who is not the insured", which the Law can.

2. **The third party's four exceptions hold, in both decree vintages, and the passenger is where the two texts part.**
   The driver, a person on the vehicle, a passenger and the owner are not third persons; the owner who handed the vehicle over is ([A03.2], [A03.3], lines 657 and 663; the same six results under Decree 220 in [A03.4], line 665).
   But Art 5 and Art 7(1)(b) insure the owner's liability to passengers, so a passenger's claim engages the insurer through Art 5 and not through Art 3(5)(a): the A03 function says no and the A16 function says yes for the same passenger in the same accident ([A16.2], line 707).
   For Dieu 57's object of insurance (liability to a third person) to cover what Art 5 insures, the Law's undefined "người thứ ba" must include passengers, so it is wider than the decree's definition.
   The join runs both readings and they disagree on exactly the passenger.

3. **The Law's bar on a direct claim against the insurer stands except in one case.**
   Dieu 58(2) bars a direct claim unless the law provides otherwise; the decree provides otherwise only where the insured has died or lost civil capacity (Art 12(5), second paragraph), and only for a person who is a third party ([A03.6], line 674).

4. **After 1 July 2026 the same Vietnamese word names two different things.**
   The two decree vintages name the third party differently and define the same persons ([A04.2], line 690; [A03.4]).
   The Law keeps "người thứ ba" for the third party and uses "bên thứ ba" for a recipient of confidential information (law08:290, 2864), so a reader of the amended decree and the Law meets "bên thứ ba" in two senses.

5. **The decree's accident is wider than the Law's insured event, and its exclusions fall on different limbs of the Law's definition.**
   The driver's own harm in the standard accident is an accident, reportable and within the advance of Art 12(3)(b), and no insured event ([A05.3], line 748).
   A passenger's harm is an insured event though a passenger is no third party ([A05.4], line 751).
   The intentional act of Art 7(2)(a) removes the Law's first limb (an objective event); a flight from the scene or an unlicensed driver leaves the event objective and removes only the obligation to pay ([A05.5], line 753).

6. **A premium outside the decree's band is still the Law's premium.**
   At 20% above Annex I the decree reports a problem and the Law's Dieu 4(28) still holds, because the parties agreed the sum ([A06.3], line 788).
   Neither text says which prevails; the Law has no band, and the decree sits under Dieu 8(5).

7. **The Law's limit has no "per person".**
   One Law claim for two persons each owed 100 million is capped at 150 million, where the decree pays 200 million, so the join must build one Law claim per person ([A07.4], line 844).
   The Law lets the contract agree another limit and gives no formula; the join declines, as VN-29 does ([A07.3], line 842).

8. **The extension beside the compulsory part changes regime on 2026-01-01; the compulsory part never has one.**
   The compulsory line is outside Dieu 87(3) at V1, V2 and V3, with VN-29's own two refusal messages ([A11.1], line 991).
   An extension that was registered and approved satisfies V1 only, and one that was notified and applied satisfies V2 and V3 only ([A11.2], line 995).
   Neither Decree 67 nor Decree 220 mentions it.

9. **The decree's deadlines are not the Law's, and the Law's apply to the decree's accident.**
   Filing: an accident on 2024-06-15 gives a last day of 2025-06-15, and force majeure days extend it ([A09.1], [A09.2], lines 918 and 922).
   Paying: a full dossier on 2025-02-20 gives 2025-03-07, and 13 days of delay on 2025-03-20 ([A10.1], line 955); interest has no rate in either text, so the join declines ([A10.2], line 959).

10. **Only the compulsory part is compulsory insurance.**
    The part the decree requires is a Dieu 8(2) product at V1, V2 and V3; the extension is not ([A08.1], [A08.2], lines 882 and 886); and the decree itself rejects an extension sold without the compulsory part separated ([A08.3], line 890).

11. **The decree's restrictions on a contract sit outside the Law's definition of it.**
    A four-year term, a second contract on the same car, and a contract with an unpaid premium are each still a contract of insurance under Dieu 4(16) ([A12.2]-[A12.4], lines 1029 to 1034).

12. **The decree's insurer is two Law categories and no life or health insurer.**
    Not a branch: a Dieu 4(17) insurer of the non-life kind, never of the life or health kind; a branch: a Dieu 4(19) branch and not a Dieu 4(17) insurer ([A15.1], [A15.2], lines 1135 and 1140); a life insurer is the Law's insurer that the decree's term never reaches ([A15.3], line 1143).

13. **The decree never designates a payee.**
    The person Art 12(5) pays is, in neither case, a Dieu 4(26) beneficiary; only a designation, which the decree does not mention, would make one ([A14.1], [A14.2], lines 1090 and 1094).

Where the join could not decide, and what it assumed instead (each is labelled "assumed, not ruled" in the join's comments):

- **Whether "người thứ ba" in the Law includes a passenger.** The Law does not define it; the join offers both readings (A03 and A16) and does not choose.
- **"Objective" in Dieu 4(27).** The join reads an event as not objective when the owner, the driver or the injured person acted intentionally to cause it, because Art 7(2)(a) names that act. The Law does not define "khách quan" ("objective"), and a fortuity test would also treat negligence differently.
- **Whether VN-29's premium flag means "payable" or "paid".** `is made by the policyholder to the insurer, branch or mutual organisation` is set from "a premium was paid"; for the contract limb of A12 "must pay premium" is set from "the decree fixes a premium". The two readings give different answers for an unpaid contract (A01.2 against A12.4).
  The flag `is required by law or agreed by the parties in the contract` was set from "the decree fixes a premium" alone until 2026-10-13, when `MIRRORBALL.md` (b3) showed that it then denies an agreed, paid premium for a vehicle the decree does not price; A06 now also reads a premium paid under the contract as agreed.
- **Whether Art 4(5)(a)'s right to refuse is a "condition the law sets for buying" under Dieu 8(4).** Neither text says so. The join writes the bridge as code, so [A13.2] proves only that the code does what the assumption says.
- **Whether the Art 12(3) advance is a payment "bồi thường, trả tiền bảo hiểm" within Dieu 31(1).** If it is, the 15 days could run from the advance; if not, they run from the full dossier, which is what the join does.
- **Which kind of day Dieu 31 means.** The Law says "ngày" and the decree separates "ngày làm việc" for the advance; VN-29 holds the Law's days as a fork, and VN-10 holds the working-day calendar as an input. The join uses calendar days for the Law's 15 days, and a calendar year for its year.
- **Pairing a decree vintage with a Law vintage.** The join does not check that the pair can coexist. The decree as made recites the Law of 16 June 2022 (decree67:28) and Decree 220 recites the Law as amended (decree220:24); Decree 220's amended vintage starts the same day as V3, 2026-07-01, and V2 starts earlier, so a pairing of the amended decree with V1 is one no date produces.
- **Dieu 8(5).** VN-29 declines it for want of the decree; the join supplies the decree as the Government's rule but does not make VN-29 stop declining it.
