# Missed instruments: what was searched, where, and what was found

Status: parts A-D were done on 2026-11-04 before any Gazette request was answered; part E records the Gazette requests and the three files fetched after the lead's answer, the same day.

## A. Mechanical search of the deposited texts

Script: `review-out/hunt/term_hunt.py` (sha256 `ce49d73e…30b6a9`), run as `python3 -I term_hunt.py <VIEW> term_hunt.tsv`.
It reads all 127 `.txt` files under `subjects/sg/*/registers/source-bundle/`, rejoins hyphenated line breaks, collapses whitespace (so a term split over two lines is found), and counts matches per file, case-insensitively except where a row says case-sensitive.
Per-file counts are in `review-out/hunt/term_hunt.tsv` (359 rows); totals are in `review-out/hunt/term_hunt.summary.txt`.
Two first-run terms were too broad and were narrowed before the recorded run: `MW` matched "mW" (milliwatts) when case-insensitive, and `\bdish` matched "dishonestly".

| term (regex in the script) | hits | files | what the hits are |
| --- | --- | --- | --- |
| receiver | 218 | 27 | BA First Schedule and Rg 1 (TV and sound receivers, TVRO); N 1 GPS, MMDS and "TV Receivers/ Radio Systems" (remote controls); Rg 5 "station" definition; Dealers "Scanning Receivers" (prohibited) and S 251/2013 item 3; Companies Act "receiver" (insolvency) |
| receive-only / receive only | 11 | 6 | only the TVRO definition (BA 2003, 2012, 2026, S 549/2012, Rg 1, S 333/2004) |
| broadcast sound receiver | 50 | 5 | BA First Schedule (2003, 2012), Rg 1, S 333/2004, S 548/2012 |
| broadcast television receiver | 93 | 6 | the same five plus the TVRO Regulations |
| sound broadcast | 0 | 0 | none |
| television (any) | 170 | 17 | BA and its instruments; TA texts only in broadcasting-service definitions |
| TV (word, case-sensitive) | 8 | 8 | N 1 item 11(e) in every version (6 files), S 121/2008 "Niche Subscription TV Licence" |
| radio receiver / radio set | 0 | 0 | none |
| FM (word, case-sensitive) | 0 | 0 | none |
| 88 MHz band edge (`88…108`) | 16 | 16 | N 1 wireless-microphone item (7 versions) and the Dealers Fifth Schedule short-range-device item (9 files): transmitters only |
| AM (word, case-sensitive) | 0 | 0 | none |
| medium wave | 0 | 0 | none |
| MW (word, case-sensitive) | 0 | 0 | none |
| 526.5 or 1606.5 kHz | 0 | 0 | none: no deposited instrument names the medium-wave broadcast band |
| 0.51-1.60 MHz / 510-1600 kHz | 15 | 15 | N 1 wireless microphones and the Dealers short-range-device item: transmitters only |
| vehicle | 104 | 29 | BA s 20(1)(a), Rg 1 regs 5, 10, 23, 28; TA s 3, s 35; N 1 car alarms and vehicle radar; others irrelevant |
| car radio / motor | 2 | 2 | "motor vehicle" in S 477/2020 and the Companies Act; no "car radio" anywhere |
| type approval / type-approved | 39 | 4 | Dealers Regulations 2004 RevEd and S 478/2005 (abolished type approval) |
| technical specification | 12 | 10 | Rg 5 class-licence conditions (as made and 2002 RevEd), S 461/2009 femtocells, S 726/2014 white-space devices, the 2004 RevEd Dealers reg 22 (testing for personal use, split over two lines), and S 251/2013's registration-fee item for equipment sharing "the same technical specifications"; none for broadcast receivers |
| IDA TS / IMDA TS | 0 | 0 | none: "IMDA TS DVB-T2 IRD" is not named in any deposited text |
| DVB (case-sensitive) | 0 | 0 | none |
| integrated receiver (decoder) | 1 | 1 | S 251/2013 Fifth Schedule item 3 only |
| IRD (word, case-sensitive) | 0 | 0 | none |
| set-top box | 0 | 0 | none |
| digital terrestrial | 2 | 2 | S 251/2013 (text and Gazette copy) only |
| analogue | 4 | 2 | Dealers Fourth Schedule fee items ("Analogue Radio-communication Equipment", "Analogue Cellular Mobile Phone") |
| decoder | 42 | 5 | BA s 48 (unauthorised decoders) and S 251/2013 |
| class licence | 458 | 41 | BA N 1 (services), TA Class Licences Regulations (operators), Rg 5 reg 65 (public mobile stations), S 461/2009 (femtocells), Dealers' Class Licence: none covers a broadcast receiver |
| exempt (any) | 269 | 49 | BA exemption orders under s 60 (services, ownership, funding), TA N 1, Dealers reg 25, S 478/2005: none exempts a receiver from BA s 20 or TA s 34(1)(b) except GPS/MMDS in N 1 |
| s 20(4) (`20 ( 4 )`) | 12 | 11 | only TA and Dealers cross-references to other provisions numbered 20(4); no BA instrument cites BA s 20(4) |
| s 34(1)(b) / 54(1)(b) | 63 | 20 | the title and paragraph 2 of N 1 in every version; TA s 54 itself |
| broadcasting apparatus | 190 | 11 | BA, Rg 1, S 333/2004, TVRO Regs, TA s 2 and s 72/95, Act 10 of 2005 |
| TVRO | 35 | 7 | BA First Schedule, S 549/2012, Rg 1, S 333/2004, TVRO Regs |
| satellite | 89 | 15 | TVRO texts; TA s 5B orbital slots; Rg 5 satellite stations |
| dish (word) | 6 | 6 | the TVRO definition only |
| aerial / antenna | 20 | 8 | Rg 1 regs 4, 25, 34 (aerial dimensions); TVRO definition; Rg 5 amateur aerials |
| station licence | 305 | 10 | Rg 5, Rg 1 (ship station), Ship Station Operators Regs |
| personal use / personal purposes | 21 | 6 | Dealers reg 22 (personal use, approval not needed) and Rg 5 First Schedule fee rows "(Personal use)" for remote controls, wireless microphones and CB walkie-talkies |
| radio-communication equipment | 88 | 13 | TA ss 34, 35, 37; Rg 5; Dealers regs 20 and Third Schedule |
| sound programme | 3 | 3 | BA "broadcasting service" definition (3 editions) |
| free-to-air | 53 | 3 | BA editions only |

Negative results worth stating: no deposited instrument mentions an FM or AM broadcast receiver, a car radio, a set-top box, DVB or an IMDA technical specification by name; no deposited instrument is made under BA s 20(4); no deposited TA instrument licenses or exempts a broadcast receiver.

## B. lawplain (secondary source; current texts only)

| corpus | query | results | relevant |
| --- | --- | --- | --- |
| subsidiary_legislation | `broadcast receiver` | 20 | only BA1994-RG3 (TVRO Regs, already deposited); others are advertising rules in other Acts |
| subsidiary_legislation | `Telecommunications exemption` | 19 | none from the Telecommunications Act |
| subsidiary_legislation | `radio-communication` | 14 | none from the Telecommunications Act |
| subsidiary_legislation | `Telecommunications` with `parent_act_id=TA1999` | 0 | — |
| subsidiary_legislation | `Telecommunications Radio-communication Regulations station licence` | 7 | none from the Telecommunications Act |
| subsidiary_legislation | `walkie talkie` | 4 | none from the Telecommunications Act (so N 1 is not in lawplain) |
| subsidiary_legislation | get_document `TA1999-N1` | HTTP 404 "subsidiary legislation not found" | lawplain does not hold N 1 |
| subsidiary_legislation | `TVRO` | 1 | BA1994-RG3, doc_date 2004-02-29, already deposited |
| subsidiary_legislation | `Broadcasting Act` (50 results) | 12 BA instruments | all 12 are already deposited (S 523/2010, S 121/2008, S 477/2020, S 211/2022, S 30/2023, O 1, Rg 3, O 2, N 1, Rg 2, O 3, S 47/2023); none is under s 20(4) |
| subsidiary_legislation | `Broadcasting Act exemption broadcasting apparatus section 20` | 2 | none relevant |
| bills | `Telecommunications broadcasting apparatus` | 8 | Bill 67/2004 cl 2(a) inserted the TA s 2 definition "broadcasting apparatus" with the BA's meaning (enacted as Act 10 of 2005 s 2, deposited at `TA1999.ACT10-2005.txt:45-47`); nothing on receivers |
| hansard | see `review-out/sources/lawplain-hansard/EXTRACTS.md` | — | fees "stopped" in 2011; analogue switch-off on 1 January 2019; DVB-T2 consumer labels; nothing on TA licensing of receivers |

Conclusion for lawplain: it holds no Telecommunications Act subsidiary legislation at all, so it can neither confirm nor exclude a TA exemption for receivers; for the BA it holds nothing that is not already deposited.

## C. IMDA's own site (guidance, not legislation)

Searched with a web search restricted to `imda.gov.sg`, then fetched by URL; each retrieved file is in its own folder under `review-out/sources/` with URL, time and sha256.

- `imda-ts-dvb-t2-ird-i1r2/`: the DVB-T2 IRD technical specification (draft Issue 1 Rev 2, 2014). Its introduction says it "is established to enable equipment manufacturers and/or suppliers to bring in compatible DVB-T2 IRD modules and IDTVs"; it says nothing about licensing a user's possession.
- `imda-ts-dvb-t2-ird-decision/`: IMDA's decision paper on that specification; about features and cost, nothing about licensing.
- `imda-eqr-guide-nov2023/`: IMDA Guide EQR, Issue 1 Rev 9, November 2023; lists "Integrated Receiver Decoders for use with 2nd- generation Digital Terrestrial Television broadcasting system (DVB-T2 IRD)", including "receiver set-top box, Integrated Digital TV (IDTV), In-vehicle receiver", for dealer registration against "IMDA TS DVB-T2 IRD"; its §3.7.5 says "Where a licence is required for the use of the telecommunication equipment under the Regulations, suppliers shall inform every customer of the need to obtain such a licence from IMDA", without saying whether one is required for a DVB-T2 receiver.
- `imda-spectrum-mgmt-handbook/`: Spectrum Management Handbook, Issue 1 Rev 2.16, June 2022; chapter 6 (broadcasting) lists the MW (0.5265-1.6065 MHz), FM (88-108 MHz) and DTT bands and says broadcasters need a broadcasting station licence; it says nothing about receivers; "Short Range Devices are exempted from licensing if the transmitter output power is kept below the maximum approved field strength", which concerns transmitters.
- The IMDA listing page for the Telecommunications Act (`/regulations-and-licensing-listing/telecommunications-act-1999`) renders its list by script; a fetch returned no instrument list.

Result: IMDA's published guidance treats a DVB-T2 receiver as dealer-registrable telecommunication equipment and is silent on whether the person who owns one needs a licence; I found no IMDA statement that receive-only broadcast receivers are exempt.

## D. Instruments the encoders cite, compared with the deposit

Every deposited instrument is cited by at least one encoding (stem search over all `.l4`, `.sh` and `encoding.json` files), except the Gazette duplicate copies (`*-GAZ.txt`), the Interpretation Act (`IA1965.txt`), the 2020 printed Revised Edition of the TA and Bill 30/2016.
The Interpretation Act is cited by neither encoding, although s 23(2) (retrospective subsidiary legislation) and s 16 (effect of repeal) bear on S 548/2012 and S 549/2012.
The Broadcasting Act encoding cites three deposits that are **not in my copy**:
- `singapore-broadcasting-authority-broadcasting-and-television-amendment-regulations-1999/.../BA1994-S212-1999.txt` (S 212/1999, reg 8 of Rg 1: fee waiver), cited by `sgba-i-s212-1999.l4` and `sgba-tests-rg1.l4`;
- `singapore-broadcasting-authority-tvro-system-amendment-regulations-2001/.../BA1994-S354-2001.txt` (S 354/2001, TVRO Regs regs 3-5, 8, 9 substituted from 1 August 2001), cited by `sgba-i-s354-2001.l4`;
- `singapore-broadcasting-authority-class-licence-amendment-notification-2001/.../BA1994-S496-2001.txt` (S 496/2001, BA class licence for services), cited by `sgba-i-s496-2001.l4`.
I asked for them (R1); the lead said a copying script had missed their subject names and added all three to my copy on 2026-11-04, so their quotations are checked in `CITATION-CHECK.md`.
S 354/2001 confirms the TVRO point independently of lawplain: from 1 August 2001 "No person other than an institution may be granted with a licence" (`subjects/sg/singapore-broadcasting-authority-tvro-system-amendment-regulations-2001/registers/source-bundle/BA1994-S354-2001.txt:52-53`).

## E. Gazette

Requests are in `review-out/REQUESTS.md` (R1).
The lead answered from e-Gazette index queries, which the lead says are not exhaustive; I treated the answers as leads and fetched the three files named.

| request | lead's answer | what I fetched and found |
| --- | --- | --- |
| 1. a TA exemption or class licence for broadcast receivers, 2010-2013 | none found; every TA notice the index showed for 2010-2013 is already deposited; a broader title search is pending | nothing to fetch; **negative so far, not proven** |
| 2. N 1 after S 78/2017 | S 588/2023 | `sources/gazette-S588-2023/`: from 1 September 2023 it deletes "localised on‑site" from paragraph 2(b) (`588.txt:36`) and the First Schedule heading (`588.txt:43`), renumbers the section references to "sections 53, 54(1)(b) and 55", deemed from 31 December 2021 (`588.txt:19-35`), and replaces items 2-3, 5 and 8-15; item 3 is still "Wireless Microphones" with "0.51 – 1.60 MHz" and "88.00 – 108.00 MHz" (`588.txt:50-56`); item 11(e) "TV Receivers/ Radio Systems" is still under "Remote Control Devices" (`588.txt:108-122`); item 14 becomes "Global Navigation Satellite Systems Receivers" (`588.txt:162-164`); **no broadcast-receiver item** |
| 3. Rg 5 after S 100/2016 | none seen | nothing to fetch; the deposited text may be current, not proven |
| 4. Rg 6 after S 725/2014 | S 589/2023 (and S 560/2024, Composition) | `sources/gazette-S589-2023/`: replaces Fifth Schedule item 1 only (`589.txt:39-109`) and updates Act names; **reg 22 and Fifth Schedule item 3 (DVB-T2 IRDs) are untouched**; `sources/gazette-S560-2024/`: adds an offence under the Wiring Work Regulations 2024 to the compoundable list; nothing on receivers |
| 5. TVRO Regs after 2004 | only S 354/2001 seen | nothing to fetch; no later amendment or revocation seen, not proven |
| 6. 1995 Ed. Act and 1990 Ed. Rg 1 | not looked up | not fetched; the pre-2003 position of a lone home radio remains open |

What this adds to the answer: as at 1 September 2023 the Minister re-made the N 1 Schedule and again exempted one class of receive-only equipment (satellite-navigation receivers) without naming broadcast receivers.
That is evidence on reading 3 (whether receivers are "radio-communication equipment" in the regulator's own scheme), not on the operative answer, which still turns on s 95 and on whether an undeposited s 5 licence or s 96 exemption exists.
No instrument I found covers an analogue terrestrial TV, FM radio, AM radio or vehicle receiver under the TA.

### E2. Second round, after the lead's browse results (2026-11-04)

The lead's second answer gave titles only, from the first page of each e-Gazette index query, and said it was not exhaustive.
I fetched three of the files it named (`sources/gazette-SL-index-2010/`, `sources/gazette-S22-2011/`, `sources/gazette-S381-2024/`, each with a SOURCE.md).

| item | what it is | what I found |
| --- | --- | --- |
| S 22/2011 | "Telecommunications (Cancellation) Notification 2011", made under "section 26(5) of the Telecommunications Act" (`gazette-S22-2011/022.txt:24-25`) | it cancels thirteen Telecom Competition Code exemption notifications, items (a) to (m) (`022.txt:34-78`); **nothing on receivers or on licences of equipment** |
| S 381/2024 | "Telecommunications (Exemption from Section 54(1)(a) and Telecommunications (Dealers) Regulations) Notification 2024", made under "section 96 of the Telecommunications Act 1999" (`gazette-S381-2024/381.txt:23-24`) | para 3(1): "section 54(1)(a) of the Act does not apply to any person in respect of the sale, offer for sale or possession for sale of an in‑vehicle unit" (`381.txt:51-53`); it exempts dealing in one ERP 2.0 device, and not possession for use under s 54(1)(b); **no broadcast receiver** |
| Subject Index to Subsidiary Legislation, 2010 | "Incorporating all Subsidiary Legislation enacted before 1.6.2010" (`gazette-SL-index-2010/10rsl_index.txt:53`, the footer of every page) | see below |

**What the 2010 index lists under Broadcasting** (`10rsl_index.txt:1033-1064`):
- Rg 1 (Pts II-VI);
- Rg 2;
- Rg 3;
- the class licence N 1;
- the Exemption Order O 1;
- S 121/2008.
Every one is deposited.
The index does not list the deposited Exemption (No. 2) and (No. 3) Orders, so it is **not exhaustive**.

**What it lists under Telecommunications and Radio-communication** (`10rsl_index.txt:9707-9758`, `8112-8118`):
- Rg 1, Rg 3, Rg 4, Rg 5 and Rg 6;
- S 86/2005, S 479/2005, S 706/2005 and S 77/2007;
- the competition Code S 87/2005 and S 564/2008;
- one instrument that is **not deposited and is cited by neither encoding**:

> equipment, telecommunication          Telecommunication Authority of
>                                       Singapore (Exemption in Respect of
>                                       Specified Equipment) Order
>                                       (Cap 323, O 3); Telecommunications
>                                       (Dealers) Regulations (Cap 323, Rg 6)

(`10rsl_index.txt:9717-9721`.)
Its title says it was made under the Telecommunication Authority of Singapore Act, the "repealed Act" of TA s 2, "the Telecommunication Authority of Singapore Act (Cap. 323, 1993 Revised Edition)" (`TA1999.txt:459-462`).
TA s 98(2) keeps such an instrument alive: "Any subsidiary legislation made under the repealed Act … and in force immediately before 1 December 1999, so far as it is not inconsistent with the provisions of this Act, continues in force as if made under this Act until it is revoked or repealed by subsidiary legislation made under this Act." (`TA1999.txt:7097-7102`).
Listing it in an index of legislation "enacted before 1.6.2010" means it was still treated as in force at that date.
**I have not seen its text**, and its title does not say which equipment it exempts, or from which provision.
It could be the instrument that decides dates 2 and 3 (an exemption for receive-only equipment), or it could concern something else entirely (dealers, or a class of transmitter).
Until it is read, the answer at every date after 1999 carries this gap.
lawplain does not hold it: subsidiary_legislation searches for "Exemption in Respect of Specified Equipment" and for "Telecommunication Authority of Singapore Exemption Order" returned no Cap 323 instrument (2026-11-04).
The TA N 1, which certainly existed in 2010 (its 2002 Revised Edition is deposited), is **not** in the index's Telecommunications entries either, which is a second reason to treat the index as a lead and not a register.
I have asked the lead for the Order's text (REQUESTS.md R3).

### E3. The undeposited TA exemption order O 3, and the 1999 regulations it names (2026-11-04)

Sources, each in its own folder with a SOURCE.md:
- `sources/gazette-cap323-O3-1999/`, O 3 in the 1999 Revised Edition, and `sources/gazette-S549-1998/`, the Order as made; the lead fetched both, and I copied them (the sha256 values match the lead's).
- `sources/gazette-cap323-Rg7-1999/`, the Telecommunication (Dealers) Regulations, Rg 7, 1999 Revised Edition; I fetched it.
- `sources/gazette-cap323-Rg3-1999/`, the Radio-communication Regulations, Rg 3, 1999 Revised Edition; I fetched it.
All four were made under the Telecommunication Authority of Singapore Act (the "repealed Act" of TA s 2).

**What O 3 says.**
It was made "In exercise of the powers conferred by section 130 of the Telecommunication Authority of Singapore Act" (`gazette-S549-1998/549.txt:20-22`) and came "into operation on 12th November 1998" (`549.txt:25-27`).
Paragraph 2 reads: "All persons shall be exempted from section 30 (1) to (5) of the Act in respect of — (a) any telecommunication equipment that has been approved for sale by the Authority under regulation 24 (1) of the Telecommunication (Dealers) Regulations (Rg 7); and (b) any telecommunication equipment that is set out in the Fifth Schedule to the Telecommunication (Dealers) Regulations and that meets the standards and specifications approved by the Authority and published by the Authority from time to time." (`gazette-cap323-O3-1999/99323o3.txt:28-37`).

**What the two Dealers provisions it names said in 1999.**
Reg 24(1): "no dealer shall sell — (a) any type of telecommunication equipment to be used for connection to any telecommunication system or equipment belonging to a telecommunication system licensee; or (b) any type of radio-communication equipment to be used in Singapore, unless the type of equipment has been approved by the Authority to be sold." (`99323rg7.txt:487-493`).
The Fifth Schedule, "TELECOMMUNICATION EQUIPMENT NOT REQUIRING APPROVAL", lists telephones, line interfaces, autodiallers, answering sets, caller identification, security alarms, facsimile, modems, EFTPOS/CCAT, telex and digital leased circuit equipment, and "13. Other equipment as determined by the Authority." (`99323rg7.txt:828-859`).
It names no receiver.
Its First Schedule, "TELECOMMUNICATION EQUIPMENT THE IMPORT, MANUFACTURE, SALE, OFFER OR POSSESSION FOR SALE OF WHICH IS PROHIBITED", begins "1. Scanning Receivers." (`99323rg7.txt:646-654`).

**What the 1999 Radio-communication Regulations said about receivers.**
Reg 4(1): "Except as provided in the First Schedule, no person shall possess, establish, install or use any station in any place or on board any local vessel or aircraft or in any vehicle in Singapore unless he has a valid licence granted under these Regulations." (`99323rg3.txt:249-252`).
"station" "means a transmitter, receiver, a combination of transmitters and receivers or any accessory thereto which is used or intended to be used for radio-communication" (`99323rg3.txt:231-233`).
The First Schedule ("EQUIPMENT* FOR WHICH NO STATION LICENCE IS REQUIRED FOR IN-BUILDING OR LOCALISED ON-SITE OPERATIONS", `99323rg3.txt:1046-1048`) has the same receiver entries N 1 later carried: "(e) TV Receivers/ Radio Systems" under "11. Remote Control Devices" (`:1135-1143`), "14. Stand-alone GPS Receivers" (`:1178-1179`) and item 15, communication and MMDS receivers.
It names no broadcast receiver.
These Regulations were revoked by Rg 5 as made: "The Radio-communication Regulations (Cap. 323, Rg 3) are revoked." (`subjects/sg/telecommunications-radio-communication-regulations-2001/registers/source-bundle/TA1999-RG5-S114-2001.txt:1548-1549`).
So under the TAS Act and, through TA s 98(2), from 1 December 1999 to 1 March 2001, possessing a "station", receivers included, needed a licence unless the First Schedule exempted it, and that Schedule had no broadcast receiver.
That is the same shape as the position under Rg 5 and N 1 from 2 March 2001.

**Whether O 3 reaches a broadcast receiver: one unread fact decides it.**
"section 30 (1) to (5) of the Act" is a section of the TAS Act, whose text is not deposited and which I could not obtain.
lawplain lists the Act (`TASA1992`, "act_repealed") with no sections, and its copy of the 1992 Bill (B16-1992) stops after clause 2 (`body_length` 8876).
Searches of lawplain `bills` and `hansard` for the 1999 Telecommunications Bill's explanatory statement or debate returned nothing usable (2026-11-04).
One Bill does bear on it: the Telecommunication Authority of Singapore (Amendment) Bill 1998, read the first time on 14 January 1998, ten months before O 3 was made (lawplain `bills` B6-1998; extract in `sources/lawplain-bills/EXTRACTS.md`; extrinsic).
Its clause 6: "Section 30(1) of the principal Act is amended by deleting the words “public telecommunication” and substituting the words “telecommunication system”."
Its clause 12(a) adds, after "section 30" in the search-and-seizure section 74(1), "or that the telecommunication equipment is imported in contravention of any provision of this Act".
So s 30(1) spoke of a "public telecommunication" licensee or system, to become a "telecommunication system" licensee.
That is the wording of TA 2000 Ed. s 9(1), "equipment to be used for connection to any telecommunication system or equipment belonging to a telecommunication system licensee shall be approved by the Authority before use" (`TA1999.20001230.txt:510-512`).
This is strong evidence for branch 1 below, short of proof: it is a Bill as introduced, it shows a phrase and not the section, and I have not seen the Act as passed.
There are two branches; the evidence now favours branch 1.
- **Branch 1: s 30 was the approval-before-use provision**, the predecessor of TA 2000 Ed. s 9, "Any equipment to be used for connection to any telecommunication system or equipment belonging to a telecommunication system licensee shall be approved by the Authority before use." (`TA1999.20001230.txt:510-512`).
  O 3 would then mean that equipment already approved for sale, or listed as not needing approval, needs no separate approval before use.
  It would say nothing about the possession offence (now TA s 54(1)(b)) or the operation offence (s 55).
  The 1998 Bill's clause 6 points this way (above), and so does the structural evidence; both are inference, not a reading of s 30.
  TA 2000 Ed. s 9 has seven subsections, of which (1) to (5) are the approval regime and (6) and (7) are fees and the cessation of supply (`TA1999.20001230.txt:510-545`).
  O 3 exempts from "(1) to (5)" exactly.
  The items of the 1999 Fifth Schedule are all equipment for connection to a network.
  And s 95's second exception, "the approval of any broadcasting apparatus used in accordance with section 11" (`TA1999.txt:6987-6992`), shows the Act treating approval as a separate matter from licensing.
- **Branch 2: s 30 was the possession and operation prohibition** (now TA ss 54-55).
  Then limb (a) would exempt every person "in respect of" any radio-communication equipment whose type was approved for sale under reg 24(1)(b).
  If broadcast receivers were type-approved, that would take in every lawfully sold set.
  Two further links would then be needed, and neither is established:
  - that broadcast receivers were in fact approved for sale under reg 24(1)(b), when until 2011 they were "broadcasting apparatus" and their dealers were licensed under Part III of the Broadcasting Act's Rg 1 (`subjects/sg/broadcasting-television-and-radio-licensing-regulations/registers/source-bundle/BA1994-RG1.txt:372-387`);
  - that the references survive the replacement of Rg 7.

**How the references would have to be read after 1999.**
TA s 98(2) continues the Order "as if made under this Act until it is revoked or repealed by subsidiary legislation made under this Act" (`TA1999.txt:7097-7102`).
IA s 15(2)(a) reads a reference to a repealed and re-enacted provision "as a reference to the provision so re‑enacted" (`subjects/sg/interpretation-act/registers/source-bundle/IA1965.txt:1052-1058`, current text).
That would carry "regulation 24 (1)" of Rg 7 to reg 20(1) of the Dealers Regulations 2003 (Rg 6), whose words are the same (`TA1999-RG6.txt:349-355`), and after 21 July 2005 to approval for sale "by way of registration" (`TA1999-RG6-S478-2005.txt:86-93`).
**A trap in that chain.**
O 3's "Fifth Schedule" was the 1999 list of equipment "NOT REQUIRING APPROVAL".
Its re-enacted counterpart in Rg 6 is the **First** Schedule, "Telecommunication equipment not requiring approval" (reg 20(2); `TA1999-RG6.txt:413-434`).
It is not Rg 6's Fifth Schedule, which held testing fees in 2004 (`TA1999-RG6.txt:581-601`) and from 2007 lists "EQUIPMENT IN RESPECT OF WHICH REGISTRATION AND RENEWAL OF REGISTRATION FEES DO NOT APPLY" (`TA1999-RG6-S396-2007.txt:66-72`), DVB-T2 decoders among them from 25 April 2013 (`TA1999-RG6-S251-2013.txt:161-168`).
A reader who joins O 3 to item 3 of Rg 6's Fifth Schedule is reading across two different schedules.
Under limb (a), on branch 2 and with IA s 15(2), a DVB-T2 decoder registered for sale under Rg 6 reg 20 could be within the exemption.
That is the only route I found by which a digital receiver might be exempted under the TA (H5), and it depends on branch 2.

**Whether O 3 is still in force.**
The 2010 Subject Index lists it (part E2).
The lead found no revocation, and reports that the 2002 Revised Edition of Cap 323 subsidiary legislation does not list O 3, a weak sign, since that listing also omits the Dealers Regulations.
The lead also found no Subject Index later than 2010.
Some TA exemptions were published in the main Government Gazette under "Notices under other Acts" rather than in a supplement, and nobody has searched that series for 2010-2013 (the lead's note).
**Result: O 3 is a missed instrument, cited by neither encoding.**
On branch 1, which the 1998 Bill and the structure both favour, it exempts approved and listed equipment from approval before use, and it does not change any answer to the question.
On branch 2 it would cover type-approved radio-communication equipment and could make H2 false.
I rate branch 2 unlikely, but the answers at dates 2 and 3 carry it as a small condition until s 30 of the TAS Act is read (REQUESTS.md R4).
