# Where I differ from the encodings

Status: written 2026-11-04, after the encoders' preliminary answers had reached my context (see `REVIEW.md` section 0); this file is post-leak throughout.
It compares my reading with the two encodings **as they stand in my copy**: their modules, `NOTES.md` and fork registers.
It does not compare my conclusions with the encoders' final answers, which are not in my copy; the lead does that.
Each item is marked:
- **B** if it concerns a reading, ambiguity or gap already in my frozen section 1 of `REVIEW.md`, so I identified it blind;
- **P** if I first noticed it at step 4 or later.
Agreements are listed at the end and are not counted.
Paths: `TA/` is `subjects/sg/telecommunications-act-1999/encodings/legalese-sonnet-5.5/`, `BA/` is `subjects/sg/broadcasting-act-1994/encodings/legalese-sonnet-5.5/`; source aliases are those of `REVIEW.md` §1.0.

**Count: 6 items marked B, 5 marked P.**

## D1 (B). Section 20(1)(c): does "on any premises … owned or occupied by the person" qualify "operate"?

Deciding text: a person must not "(c) operate or have on any premises in Singapore owned or occupied by the person broadcasting apparatus on or by which broadcasting services are received" (BA2026:1434-1436).
Against reading A: Rg 1 says "A licence shall not be required for the temporary use of a broadcast sound receiver in a public place or at an official or social function" (RG1:460-462), and the same for television (RG1:521-523).
The encoding takes reading A, that the place phrase qualifies both verbs: F-BA-03 (`BA/NOTES.md:241-248`), with the single field `operates it, or has it, on premises in Singapore owned or occupied by the person` (`BA/sgba-nouns.l4:79`).
I lean to reading B (§1.11 item 6), because an exemption for use "in a public place" is needed only if "operate" reaches places the person neither owns nor occupies.
Where it matters: before 2011, a portable television or radio used away from the person's own premises.
Reading A gives no BA offence; reading B gives a s 47 offence unless the use is temporary and in a place the regulations name.
The encoding cannot express reading B, because the noun has one field for the two verbs together.

## D2 (B). Whether the pre-2012 "equipment" wording matters (reading (d), TA FORK 6)

Deciding text: before 1 February 2012, "‘‘equipment’’ includes any appliance, apparatus or accessory used or intended to be used for telecommunication purposes" (TA2000:226-227).
From that day the words are "for telecommunications, including (to avoid doubt) any such appliance, apparatus or accessory capable of being used for the operation of any broadcasting service" (TA2026:325-329).
"telecommunications" means "a transmission, emission or reception" (TA2026:529-536).
The TA encoding carries this as a live fork, FORK 6 (`TA/NOTES.md:401`), and flags the old wording by version (`TA/sgta-ta-versions.l4:131-158`).
My section 1 said it "does not decide anything" (§1.4 and §1.11 item 4).
I now think that was too quick for one row (`REVIEW.md` §3(d)): conduct from 1 January 2011 to 31 January 2012, read on or after 31 October 2012.
For that row the TA exposure needs a receiver to be "equipment" under the old words, and the rival reading (that "telecommunication purposes" excluded broadcast reception, which is why the new words say "to avoid doubt") would remove it.
I still read the old words as covering a receiver, so we differ in weight, not in outcome.
**Possible anchoring:** the leaked file names FORK 6 among the TA forks.
I came to the "one row" point while reading the visible fork register and Act 19 of 2011, and I cannot rule out that the leaked mention made me look.

## D3 (B, resolved in the encoding's favour). TVRO licences and individuals (F-BA-05)

Deciding text: "‘‘institution’’ means any body of persons, corporate or unincorporate, and includes any undertaking" (TVRO:7); "No person other than an institution may be granted with a licence." (TVRO:16; from 1 August 2001, `subjects/sg/singapore-broadcasting-authority-tvro-system-amendment-regulations-2001/registers/source-bundle/BA1994-S354-2001.txt:52-53`).
My section 1 said "an individual cannot hold a TVRO licence" (§1.9).
The encoding chooses neither reading: whether the person is an institution is a plain fact (`BA/NOTES.md:259-266`; `BA/sgba-i-tvro-regs.l4:21`).
On reflection the encoding's refusal to choose is the safer position: an individual who carries on an undertaking may be an "institution".
My conclusion holds for an individual householder, the question's case (`REVIEW.md` §2 item 3).
Kept here so that the change is visible.

## D4 (B; the instrument found after the leak). A TA exemption order neither encoding has: O 3

Deciding text: "All persons shall be exempted from section 30 (1) to (5) of the Act in respect of — (a) any telecommunication equipment that has been approved for sale by the Authority under regulation 24 (1) of the Telecommunication (Dealers) Regulations (Rg 7); and (b) any telecommunication equipment that is set out in the Fifth Schedule to the Telecommunication (Dealers) Regulations …" (`review-out/sources/gazette-cap323-O3-1999/99323o3.txt:28-37`).
It was made under the Telecommunication Authority of Singapore Act and kept in force by TA s 98(2), "until it is revoked or repealed by subsidiary legislation made under this Act" (TA2026:7097-7102).
It is listed in the 2010 Subject Index (`review-out/sources/gazette-SL-index-2010/10rsl_index.txt:9717-9720`).
Neither encoding cites or deposits it: `grep -rn -i 'specified equipment'` over both encoding folders finds nothing (0 lines, 2026-11-04).
The gap itself is §1.11 item 8 of section 1 ("Whether an undeposited s 5 class licence or s 73 exemption exists").
Whether O 3 changes any answer depends on what s 30 of the TAS Act said, which no deposited text shows (`MISSED-INSTRUMENTS.md` E3).
A 1998 amending Bill (extrinsic) shows s 30(1) speaking of a "public telecommunication" licensee, the wording of the approval-before-use provision, so O 3 most likely does not reach the possession offence; I record the omission because the Order is in force on the 2010 index and neither encoding mentions it.
Both encodings' version tables start no earlier than 30 December 2000 for the Act (`TA/sgta-ta-versions.l4:85-97`) and 2 March 2001 for N 1 and Rg 5 (`TA/sgta-i-versions.l4:22-23`).
So neither covers 1 December 1999 to 1 March 2001, when the TAS-era Radio-communication Regulations governed stations, receivers included (`review-out/sources/gazette-cap323-Rg3-1999/99323rg3.txt:231-233, 249-252`).

## D5 (B). The BA dispatcher for a sound-receiver licence answers regulation 23 only

Deciding text: the dispatcher `Rg 1 a licence is required for a broadcast sound receiver, for conduct on a day, the law read as at a day` (`BA/sgba-versions.l4:419-428`) calls only the reg 23 helper, which is about receivers "installed in a vehicle" or in a vessel (`BA/sgba-versions.l4:371-380`; RG1:441-444).
So for a household radio before 2011 it answers FALSE.
But s 20(1)(c) requires a licence for any "broadcasting apparatus on or by which broadcasting services are received" on the person's premises (BA2003:706-710), and a broadcast sound receiver was broadcasting apparatus until 2011 (BA2003:2141).
The encoding states s 20(1) separately and correctly (`BA/sgba-versions.l4:234-247`).
F-BA-12 says the seat "answers 'Yes.' only where a regulation states a requirement in terms" (`BA/NOTES.md:322-327`).
If the quarantined seat answers the question "is a licence required for a radio?" from this dispatcher, it understates the Act.
I could not check the seat.
The issue is in section 1 (§1.6: "The Act itself requires a licence for a home radio; the deposited regulations never say so expressly").

## D6 (P). The BA version model cannot answer for the brief's "today"

Deciding text: `IF reading AT MOST (Date 1 10 2026) THEN … ELSE NOTHING` (`BA/sgba-versions.l4:109-112`, and the same at `:323` and `:367`).
My run: conduct and reading day both 3 November 2026 gives NOTHING for the First Schedule (`REVIEW.md` §3(f), pair 11).
Rg 1 for conduct in 2015, read on 3 November 2026, also gives NOTHING (pair 19), though Rg 1 is revoked and cannot have been revived.
The TA encoding has no such cutoff and answers for 3 November 2026 from the 2020 Revised Edition (pair 28).
So the two encodings treat the same reading day differently.
The brief asks about "today (3 November 2026)", and the BA encoding answers that only for a reading day no later than 1 October 2026.

## D7 (B). The N 1 and Rg 6 version tables are stale for today

Deciding text: the N 1 table's latest row is S 78/2017, in operation 1 April 2017 (`TA/sgta-i-versions.l4:31`); my run for today selects it (pair 32).
S 588/2023 amends N 1 from 1 September 2023 and renumbers its sections to "sections 53, 54(1)(b) and 55", deemed from 31 December 2021 (`review-out/sources/gazette-S588-2023/588.txt:19-35`).
S 589/2023 amends Rg 6 (`review-out/sources/gazette-S589-2023/589.txt:39-109`).
Neither is deposited, so neither is in a table.
Neither adds a receiver item, so no outcome on the question changes.
Section 1 flagged the gap blind (§1.5, last row), and I read both instruments before the leak (`MISSED-INSTRUMENTS.md` part E).

## D8 (P). TA NOTES finding 16 is stale about the pre-2012 "equipment" words

Deciding text: finding 16 says "the pre-2012 words are not encoded, because they come from a Bill that is not deposited" (`TA/NOTES.md:268`).
But the 2000 Revised Edition is deposited and prints them, "used or intended to be used for telecommunication purposes" (TA2000:226-227).
And `TA/sgta-ta-versions.l4:131-158` quotes those lines and flags the wording by version.
Finding 20 describes the deposited Acts correctly (`TA/NOTES.md:289-293`); finding 16 was not updated.
This is documentation drift only: the module is right and the note is wrong.

## D9 (P). TA NOTES finding 26 misses a retrospective row of its own table

Deciding text: finding 26 says that of the rows of `sgta-i-versions.l4` "none has a published day later than its effective day", and that "the retrospective instruments are S 549/2012 of the Broadcasting Act and, under this Act, S 485/2016 (Rg 3)" (`TA/NOTES.md:339-340`).
But the Rg 5 table has `IF (reading day AT LEAST (Date 1 8 2001)) AND (conduct day AT LEAST (Date 9 7 2001))` for S 374/2001 (`TA/sgta-i-versions.l4:58`).
That row is published on 1 August 2001 with an effective day of 9 July 2001.
And finding 28 itself says "S 374/2001 is retrospective by 23 days" (`TA/NOTES.md:368`).
The module is right; finding 26 is wrong.
It changes nothing for receivers (S 374/2001 inserts a fixed wireless broadband item, `TA/NOTES.md:367`).

## D10 (P). Citation defects in both encodings

All 15,530 quotations are verbatim, and `srcrefs.py check --strict` reports 0 problems.
The hand check found 17 locator-level mismatches of 8 kinds (`CITATION-CHECK.md` part 4).
Examples:
- Rg 1 ranges that run into the next regulation's heading or split reg 4(2) across two `@ref`s (M1-M4);
- N 1 item 16 cut mid-row (M6, M7);
- five sections of amending Acts labelled "clause" (M8), e.g. `TA/sgta-ta-versions.l4` "Act 10 of 2005 clause 28" for what the Act prints as "28. Section 65 of the Telecommunications Act is amended" (`TA1999.ACT10-2005.txt:961`).
None changes an answer.
Separately, `TA/srcrefs-all.sh` never runs the checker on `sgta-tv-*` (its Act run takes `grep -vE '^sgta-(tests|tv|i-|nouns|ta-vintage)'`), so the TA modules that state the answer to the question are outside its own quotation check (G2).

## D11 (P). The TA encoding reads "equipment … includes" as a full definition

Deciding text: "‘‘equipment’’ includes any appliance, apparatus or accessory used or intended to be used for telecommunications" (TA2026:325-329).
The encoding's `s 2: this is equipment` returns a `BOOLEAN` that is FALSE whenever the item is not used for telecommunications (`TA/sgta-s2-definitions.l4:26-42`, which reads "telecommunications" at `:29` and "equipment" at `:41`).
The BA encoding's own rule is that a definition that "includes" returns `MAYBE BOOLEAN`, "because an inclusive definition never says no" (`BA/NOTES.md:210`).
No outcome on the question changes, because a receiver is used for "reception" and so falls inside the words either way.
For other equipment, though, the TA encoding's FALSE is a "no" the Act does not give.

## Agreements (not counted)

- F-BA-01: "specified in the First Schedule" qualifies the whole s 2(1) definition (reading A); both encodings, and I, take it (`REVIEW.md` §3(a)).
- TA s 95, broad reading as default, narrow reading stated beside it (`TA/sgta-part6-offences.l4:126-150`); I agree with both the structure and the default (§3(b)).
- A receiver is radio-communication equipment on the two composed definitions (`TA/sgta-s2-definitions.l4:63-77`); I agree (§3(c)).
- The retrospective instruments are applied as their text states, on two days, without a ruling on validity; I agree (§3(e)).
- The version tables select the right version at all 37 pairs I ran, apart from the limits in D6 and D7 (§3(f)).
- FM and AM: nothing in either encoding's deposits covers an AM or FM receiver; H4's FM-band entry is a wireless-microphone (transmitter) item; I agree.
