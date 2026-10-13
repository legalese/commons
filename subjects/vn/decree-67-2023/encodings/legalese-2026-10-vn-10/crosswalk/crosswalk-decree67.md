# Crosswalk: Decree 67/2023/NĐ-CP and its neighbours

**Draft, not reviewed.** Written 2026-10-13 as Phase 2 of an alignment plan; no Vietnamese-qualified lawyer has read it.
Decree 67/2023/NĐ-CP fixes the compulsory motor vehicle owner's civil liability insurance.
Its encoding, row VN-10 (`decree-67-2023/encodings/legalese-2026-10-vn-10/`), is the hub; each section pairs its terms with one neighbour's.
A crosswalk row is two terms, each with where it is defined, and a relation: `same`, `narrower`, `wider`, `no counterpart`, or `differs in scope`.
A relation says what the drafting session read; a reviewer rules on the two texts, not on the relation.

| Section | Neighbour | State on 2026-10-13 |
| --- | --- | --- |
| A | the Law on Insurance Business 08/2022/QH15 (row VN-29) | written last, because the Law row's Article 4 and Chapter II have had no independent test pass; drafted by one session from the two texts and the two rows, with a join that checks it (`section-a/`); relations proposed |
| B | the Law on Road Traffic Order and Safety 36/2024/QH15 (row VN-28) | lifted from VN-28's NOTES §1.3, relations proposed |
| C | the decree's own Motor Vehicle Insurance Fund and insurer duties (row VN-27) | lifted from VN-27's GLOSSARY and NOTES §1.3 |
| D | a compulsory-cover page, in general | written from the decree alone |

Rows cited at commons commit `5b6341f4c68a318826ba0a5a19357db951c71d80`.

## A. Decree 67/2023 and the Law on Insurance Business 08/2022/QH15

The decree takes its basic statuses from the Law's Điều 4 and does not define them again.
VN-10 and VN-29 share no types, so a row here says "this decree term instantiates this Law status", and a join checks it.
The full table is §1 of `section-a/SECTION-A.md`. It gives each row's VN-10 and VN-29 identifiers, the Law vintages it holds in, and a note.
The same file says which rows the drafting session added to the seed list it was given (§2, rows A12-A16) and what the join shows that the table does not (§3).
The checked form is `section-a/nd67-law08-join.l4`. For each row it builds VN-29's record from VN-10's, and asserts that the Law's predicate holds, or fails, as the decree's text says it should; on 2026-10-13 it ran with 152 assertions satisfied and none failed.
The relation measures the decree's term against the Law's, and is the drafting session's reading, not reviewed.

| row | the decree's term | decree67 | the Law's term | law08 | relation |
| --- | --- | --- | --- | --- | --- |
| A01 | bên mua bảo hiểm | 104 | Bên mua bảo hiểm | 167 | narrower |
| A02 | người được bảo hiểm | 295 | Người được bảo hiểm | 170 | same |
| A03 | Người thứ ba | 84-89 | người thứ ba | 129 | narrower |
| A04 | bên thứ ba | 84-89 (word replaced by decree220:173-175) | người thứ ba | 129 | narrower |
| A05 | vụ tai nạn | 318 | Sự kiện bảo hiểm | 178 | wider |
| A06 | Mức phí bảo hiểm | 232 | Phí bảo hiểm | 182 | narrower |
| A07 | Giới hạn trách nhiệm bảo hiểm | 187 | Giới hạn trách nhiệm bảo hiểm | 1090-1091 | differs in scope |
| A08 | bảo hiểm bắt buộc | 104-105 | Bảo hiểm bắt buộc | 226-229 | narrower |
| A09 | Hồ sơ bồi thường bảo hiểm | 401 | Thời hạn nộp hồ sơ yêu cầu bồi thường, trả tiền bảo hiểm | 706 | no counterpart |
| A10 | tạm ứng bồi thường | 318-319 | Thời hạn bồi thường, trả tiền bảo hiểm | 718 | no counterpart |
| A11 | Phụ lục I | 233-234 | phương pháp, cơ sở tính phí bảo hiểm | 1776-1782 (the words at 1790-1791) | no counterpart |
| A12 (added) | hợp đồng bảo hiểm | 124 | Hợp đồng bảo hiểm | 132 | same |
| A13 (added) | từ chối bán bảo hiểm bắt buộc | 125-128 | không được từ chối bán | 241 | differs in scope |
| A14 (added) | người bị thiệt hại | 343 | Người thụ hưởng | 175 | differs in scope |
| A15 (added) | doanh nghiệp bảo hiểm | 65-66 | Doanh nghiệp bảo hiểm | 138 | differs in scope |
| A16 (added) | Đối tượng bảo hiểm | 183 | Đối tượng bảo hiểm | 1076 | wider |

Three things the join shows that the table alone does not (`SECTION-A.md` §3, points 2, 1 and 7):
- **The passenger.** The decree's third party excludes passengers (Art 3(5)(a), decree67:84-89), but its Art 5 insures the owner's liability to them. For the Law's Điều 57 object of insurance, liability to a third person, to cover that, the Law's undefined "người thứ ba" must include passengers. The join runs both readings, and they disagree only on the passenger.
- **The unpaid premium.** An owner whose premium is unpaid is the decree's "bên mua bảo hiểm" by status. Under the Law the same owner is the insured person but not yet the policyholder, which Điều 4(24) defines by concluding the contract and paying the premium.
- **No "per person" in the Law.** One Law claim for two persons each owed 100,000,000 is capped at 150,000,000, where the decree pays 200,000,000; the join therefore builds one Law claim per person.

`section-a/MIRRORBALL.md` adds two tests. One tries every combination of the enumerations and the boundary amounts (454 assertions); the other runs both maps backwards (61 assertions); all 515 are satisfied.
They found one disagreement with the Law's text, since fixed.
For a vehicle whose premium the decree does not fix, the join denied that an agreed, paid premium is the Law's premium, though Điều 4(28) counts a sum "do các bên thỏa thuận" (agreed by the parties); its A06 now reads a premium paid under the contract as agreed (assumed, not ruled).
They also showed that only one of VN-29's four role tests survives the round trip into the decree and back.

## B. Decree 67/2023 and the Road Traffic Law 36/2024

VN-10 takes these facts as inputs; the Law decides them. The first three columns are VN-28's NOTES §1.3 table, unchanged; the last two are added here. The relation is the drafting session's reading of the two texts, not reviewed.

| VN-10 field (`nd67-vn10-nouns.l4`) | Law 36 | function in this row | relation | note |
| --- | --- | --- | --- | --- |
| `the driver did not meet the age condition of the Road Traffic Law` | Art 56(1), 59(1) | NOT `Article 59 — the driver … is of the age to drive … on …` | same |  |
| `the driver had no driving licence` | Art 56(1) | the driver's list of licences is empty, or Decree 67's own deeming (revoked or withdrawn counts as none) | same |  |
| `the driver used an invalid driving licence` | Art 57(6)-(7) | not defined in the Law; 57(7) "không có hiệu lực" (not in force) is the nearest, and a foreign licence is declined | differs in scope | Law 36 has no 'invalid'; 57(7) 'không có hiệu lực' is the nearest |
| `the driver's licence was erased or altered` | — | the Law in the sources says nothing of it | no counterpart | Law 36 says nothing of an erased or altered licence |
| `the driver's licence had expired at the time of the accident` | Art 57(5), (7)(a), 89(1) | `Article 57(7)(a) — the licence … has expired by …` | same |  |
| `the driver used a licence not matching the vehicle` | Art 57(1)-(4), 89(2)-(3) | NOT `the driver … holds a licence whose class entitles the driving of …` | same |  |
| `the driver's right to use the licence was suspended for a term, or the licence was revoked` | Art 57(7)(b), 62(5) | `right to use withdrawn` (an input) and `Article 57(7)(b) — …` | same |  |
| `the driver's blood or breath alcohol exceeded the normal level in the Ministry of Health guidance` | Art 9(2), 87(5) | `Decision 2 — the test … exceeds the permitted level, on …`: TRUE for any alcohol, save blood alcohol found endogenous (fork F8) | differs in scope | Law 36 makes any alcohol a prohibited act (fork F8 of VN-28); the decree excludes only alcohol above the normal level |
| `the driver had used drugs or banned stimulants` | Art 9(3), 83(2)(a) | `Decision 2 — the test … found a prohibited narcotic or stimulant, on …` | same |  |
| `the driver who caused it deliberately fled` | Art 9(26) | a prohibited act ("Bỏ trốn sau khi gây tai nạn giao thông đường bộ để trốn tránh trách nhiệm"); not encoded, Decree 67 decides its own limb | differs in scope | Law 36 lists fleeing as a prohibited act; the decree's exclusion is fleeing without performing the owner's civil liability |
| `the owner had handed possession and use of the vehicle to another` | Art 9(7) | `Article 9(7) — handing … to … is prohibited for want of age or licence, on …`: the owner's own prohibited act; Decree 67's exclusions do not turn on it | differs in scope | Law 36 prohibits handing a vehicle to someone without the age or licence; the decree counts an owner who handed the vehicle to another as a third party |
| vehicle: `a driving licence is required to drive it` | Art 56(1), (2), (4) | `Article 56 — a driving licence is required to drive …`: FALSE for a moped, a tractor and a rudimentary vehicle | same |  |
| vehicle: `beyond its service life under the law` | Art 40 | `Article 40 — the vehicle … is past its service life on …` | same |  |
| vehicle: `remaining service life under the law of less than 1 year` | Art 40(1) | `Article 40 — less than a year of service life is left to … on …` | same |  |
| vehicle: `subject to temporary registration` | Art 39(5) | not encoded: 39(5) lists the cases (src 463-477); still an input | same | Law 36 lists the cases; still an input in VN-10 |
| Decree 67 Art 11: revocation of the registration certificate and plate | Art 39(6) | `Article 39 — the registration certificate in … has been revoked by …`, and the plate | same |  |
| Decree 67 Art 9(3) with Art 11 (VN-10 finding R9) | Art 39(6)(a), 43(2)(c) | a change of owner is a case for revocation (finding R12) | wider | Law 36 makes a change of owner a case for revoking the registration (VN-28 finding R12), which reaches Decree 67 Art 11 |

## C. Decree 67/2023 (VN-10) and the Fund and duties of the same decree (VN-27)

VN-27 encodes the decree's Motor Vehicle Insurance Fund (Articles 14-22) and the insurer's duties (Article 75), and was built to join VN-10 without importing it. These are its own tables of the joins, unchanged: first its GLOSSARY's names, then its NOTES §1.3 map of VN-10's answer on cover. Every pair is `same` by construction (two encodings of one decree), except where the second table maps two VN-10 answers onto one.

| this row | row VN-10 |
| --- | --- |
| `A vintage of the decree`: `the decree as made`, `the decree as amended by Decree 220/2026` | `A vintage of Decree 67/2023`: `Decree 67/2023 as made`, `Decree 67/2023 as amended by Decree 220/2026` |
| `A calendar of working days` | `A working-day calendar` (same field) |
| `The insurer's answer on the person's harm` | `The answer on cover` (NOTES.md §1.3 maps every member) |
| `the insurance enterprise`, `the buyer or the insured` | `the insurer`, `the insurance buyer or the insured` |
| `Article 6(1) — the limit per person per accident, for health and life` | `Article 6(1) — the limit for health and life, per person per accident` |
| `Article 12(3)(b) — the advance for` | `Article 12(3) — the advance for` (both points) |
| `the premium of Annex I for the vehicle and the term` (an input) | `Annex I — the premium for the term of` |

| VN-10 `The answer on cover` | this row's `The insurer's answer on the person's harm` |
| --- | --- |
| `covered` | `the insurer covers the harm` |
| `outside the scope: the vehicle was neither in road traffic nor operating` | `the harm is outside the scope of Article 7(1)` |
| `outside the scope: the person is neither a third party nor a passenger` | `the harm is outside the scope of Article 7(1)` |
| `excluded: an intentional act of the owner or the driver` | `Article 7(2)(a): an intentional act of the owner or the driver` |
| `excluded: an intentional act of the injured person` | `Article 7(2)(a): an intentional act of the injured person` |
| `excluded: the driver fled without performing the owner's civil liability` | `Article 7(2)(b): the driver fled without performing the owner's civil liability` |
| `excluded: the driver's age or licence` | `Article 7(2)(c): the driver's age or driving licence` |
| `excluded: war, terrorism or an earthquake` | `Article 7(2)(h): war, terrorism or an earthquake` |
| the property answers (`a passenger's property`, `an indirect consequence`, `alcohol or drugs, for damage to property`, `property stolen or robbed`, `special property`) | not used: the support pays only for death and injury |

## D. Decree 67/2023 and a compulsory-cover page, in general

An insurer's page or rule book on compulsory cover restates the decree: Article 4(2) (decree67:108-110) binds the parties to the decree's conditions, premium and minimum sums.
So an encoding of such a page should be a view of VN-10's types, and a join from it onto VN-10 should be total.
This section says, for each thing the decree fixes that a page may restate, what a page's encoding must be able to answer, and which departures the decree itself licenses or forbids.
It is written from the decree alone and names no page. `decree67:N` is line N of the gazette text the encodings quote (Official Gazette 1017-1018 of 20 September 2023).

| What the decree fixes | VN-10 type or function | Decree text | A page's encoding must be able to answer | Departures the decree licenses | Departures it rules out (by its text, or by Art 4(2)) |
| --- | --- | --- | --- | --- | --- |
| who is insured against whom | `A person harmed in the accident`; `Article 3(5)(a) — a third party` | Art 3(5)(a), 5, 7(1): decree67:84-89, 183-186, 199-203 | whether a harmed person is a third party, a passenger on the insured vehicle, the driver, someone else on the vehicle, or the owner, including an owner who had handed the vehicle to another, whom the decree counts as a third party | wider cover agreed in the same contract, with the compulsory part kept separate (Art 4(3), decree67:111-117) | a narrower class of protected persons |
| the word for the third party | `A vintage of Decree 67/2023` | Decree 220/2026 Art 9(1), 10(1) | which wording the page uses, "người thứ ba" (as made) or "bên thứ ba" (from 1 July 2026) | none needed: the change is of words, not of cover | — |
| the limits | `Article 6(1)`, `Article 6(2)` | Art 6: decree67:187-196 | 150,000,000 per person per accident for health and life; for property, per accident, 50,000,000 for motorcycles and mopeds and 100,000,000 for cars and other vehicles | higher sums agreed in addition (Art 4(3)) | a lower limit, or a different basis (for example a property limit counted per person) |
| what is covered and what is excluded | `The answer on cover` (thirteen answers) | Art 7: decree67:197-231 | each scope limit of Art 7(1) and each exclusion of Art 7(2)(a)-(h), with its own threshold (for example alcohol "vượt quá mức trị số bình thường", decree67:225-226) and its carve-out (a driver who fled but performed the owner's civil liability) | wider cover by agreement (Art 4(3)) | an exclusion the decree does not have, or a decree exclusion without its threshold or carve-out |
| the vehicle class and its premium | `A vehicle class in Annex I`; `Annex I section A — the premium for a 1-year term, VAT not included, for` | Art 8(1), Annex I: decree67:232-234, 2041-2127 | every class of Annex I, the premium of each for one year, and whether a figure includes VAT (Annex I's do not) | an adjustment of at most 15% either way on the vehicle's claims history or the owner's accident history (Art 8(2), decree67:235-238) | any promotion or payment discount (Art 75(1), decree67:1909-1910); a class priced off the table |
| a term other than one year | `Annex I section B — the premium for a term of` | Annex I B: decree67:2128-2139 | the premium for a term in days, pro rata to the annual figure | — | — |
| the term | `Article 9 — the term is permitted for` | Art 9: decree67:241-256 | a term of at least 1 year and at most 3, and the cases where it may be shorter (a temporarily imported vehicle, a service life under a year, temporary registration, and aligning an owner's vehicles) | the shorter terms of Art 9(1)(a)-(c) and 9(2) | a term outside 1 to 3 years in any other case; an unlimited term |
| one contract per vehicle | `Article 12(9)` (the first contract pays) | Art 4(4): decree67:121-123 | that only one contract's compulsory cover answers for a vehicle | — | — |
| the certificate | `A certificate of insurance`; `Article 10(2)`, `Article 10(3)` | Art 10: decree67:260-284 | the particulars a certificate carries, and that an electronic one must comply with the law on electronic transactions | — | — |
| the claim: duties and deadlines | `nd67-art12-duties-hours.l4`, `nd67-art12-duties-workdays.l4` | Art 12(1)-(4): decree67:293-338 | the buyer's notice within 5 working days of the accident (decree67:335-338); the insurer's guidance within 1 hour and inspection within 24 hours (decree67:311-315); the advance within 3 working days (decree67:317-319) | — | — |
| the amount paid | `Article 12(6)(a)`, `Article 12(6)(b)`; `the Annex VI amount for` | Art 12(6): decree67:350-378; Annex VI | for health and life, the injury rate of Annex VI times the limit (and half where an authority finds a third party wholly at fault); for property, the actual damage by the owner's share of fault, within the limit | an amount agreed with the victim or fixed by a court, within the Annex VI amount (decree67:351-358) | — |
| the claim file | `A claim file` | Art 13: decree67:401-451 | the documents the buyer must supply and those the insurer must collect | — | — |

How a join uses this section: every row of it is a question the page's types must be able to put to VN-10. A page whose encoding cannot express one is not wrong for that reason (a sales page may say little), but the join records the gap rather than inventing a mapping.

