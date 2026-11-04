# TV-QUESTION: broadcast receivers under Singapore law (an analogue television, an FM radio, an AM radio)

QUARANTINED FILE.
This file, `sgta-tv-seat.l4`, `sgta-tv-cases.l4`, `sgta-tv-ba-schedule.l4` and any file whose name starts `sgta-tv-` are the only places that state the answer.
`NOTES.md`, the layer-1 modules and the layer-1 tests record what each provision says and nothing about the television question; `NOTES.md` has a one-line pointer here.
If you are the second reader who re-derives the answer from the sources, stop reading here until you have your own.

Status: this is the encoder's reading, written on 2026-11-03 and 2026-11-04 from the texts named below.
It is one session's work (Claude Sonnet 5.5); no domain expert has read it against the sources.
Every claim about a text carries the file and line, or the instrument and paragraph, that it rests on.
Two time axes are used throughout (design assumed, not ruled; `sgta-ta-versions.l4`): the day of the CONDUCT, and the day the law is READ AS AT.
The Act's text for the days before 2 October 2026 now comes from the e-Gazette copies deposited on 2026-11-04 (the Revised Edition 2000, Acts 10 of 2005 and 19 of 2011, S 33/2012, the 2020 Revised Edition as printed); the Singapore Statutes Online attempt for the SSO consolidations was not made: the Broadcasting Act encoder's single attempt at 03:07:48 SGT on 2026-11-04 ended in a 403 at robots.txt, which was the gate for mine, so no SSO consolidation by date is deposited and nothing in this file rests on one.
SSO: not attempted by the TA encoder because the BA encoder's one attempt was refused at robots.txt (403, CloudFront block page, 2026-11-04 03:07:48 SGT); no SSO text used, no mirror.

## The questions

1. Does Singapore law require a licence to possess, or to use, an analogue terrestrial television receiver (aerial or antenna, not a satellite dish; receive-only; no decoder)?
   Is it an offence for an individual to possess or use one with no licence of their own?
2. (Meng, 2026-11-04) Are plain old FM and AM radios exempted from all this?
   Section 10 answers that, at the same three dates, for FM radio and AM radio with the television as control.

## 1. The short answers

The Telecommunications Act answers for a pair of days: the day of the conduct and the day the law is read as at.
Two answers are kept apart.
"On the texts deposited for the day" answers only where the Act's own text for the conduct day is deposited: the Revised Edition 2000 with Acts 10 of 2005, 19 of 2011, 22 of 2016, 30 of 2016 and 15 of 2017 (conduct from 30 Dec 2000 to 15 May 2018), and the SSO consolidation in force from 2 Oct 2026.
"Also on the Act's own amendment markers" adds the days from 16 May 2018 to 1 Oct 2026, for which no deposited Act text exists, from the consolidation's margin markers.
The answers below are for a person who owns the receiver, holds no licence of their own, and knows of no regulation or exemption that covers them.
They use the default readings of section 4 (s 95 Reading A; Rg 6 reg 22(1) Reading X; N 1 item 11(e) Reading X; "equipment" before 1 Feb 2012 Reading P).

| Conduct | Read on | On the texts deposited for the day | Also on the markers |
| --- | --- | --- | --- |
| 31 Jul 2003 to 31 Dec 2010 (tested 31 Dec 2010) | any day | No offence under the Telecommunications Act: the Broadcasting Act's First Schedule lists a television receiver and a sound receiver, and on Reading A of s 95 the Act does not apply to the licensing of listed apparatus. The Broadcasting Act's own licence applied instead (s 20; offence s 47: fine up to $40,000 or 3 years or both, forfeiture to the Authority; `BA1994.20030731.txt:701-710, 1736-1741`). | the same |
| Before 31 Jul 2003 | any day | The sources do not answer: no text of the Broadcasting Act's First Schedule is deposited. | the same |
| 1 Jan 2011 to 30 Oct 2012 | read before 31 Oct 2012 | No offence under the Telecommunications Act, for the same reason: S 549/2012 is not yet published, and the Revised Editions 2003 and 2012 list a television and a sound receiver. | the same |
| 1 Jan 2011 onward | read on or after 31 Oct 2012 | S 549/2012, first published 31 Oct 2012 at 5.00 pm and "deemed to have come into operation on 1st January 2011", leaves the First Schedule with the satellite dish system alone. So an aerial television, an FM radio and an AM radio are not listed for those days, s 95 does not take them out of the Act, and possession is an offence under s 54(2) and operation under s 55(1): a fine up to $10,000, or imprisonment up to 3 years, or both, a further fine up to $1,000 for every day or part of a day the offence continues after conviction, and forfeiture of any article seized (s 85). This holds for conduct up to 30 Sep 2016. | the same, and it also holds for conduct from 1 Oct 2016 to 1 Oct 2026 |
| 4 Nov 2026 (today) | 4 Nov 2026 | An offence under s 54(2) (possession) and s 55(1) (operating), with the same maximum. | the same |
| a satellite dish system (TVRO) | any pair from 31 Jul 2003 | No offence under the Telecommunications Act: it is listed in every version, so s 95 Reading A applies. The Broadcasting Act licence (an institution only, TVRO Regulations reg 3(2)) is the one that applies. | the same |

What turns on the choices the person does not make: on Reading B of s 95 (the Act's licensing requirement is not switched off for listed apparatus) the first two rows become an offence; on Reading 2 of FORK 1 (the offence is aimed at two-way equipment only) no kind of receiver is caught on any pair (the seat does not run Reading 2: on it the offence provisions do not reach a receiver, whatever the pair); on Reading Q of FORK 6 (the earlier words of "equipment" leave a broadcast receiver out) conduct before 1 Feb 2012 is not caught.
The seat runs every combination (`What turns on the readings`) and `sgta-tv-cases.l4` states each one.

"A licence of their own" is a licence granted to the person under s 5 (`sgta-part6-offences.l4`, s 54(1) exception).
The seat questions (`sgta-tv-seat.l4`) ask it in those words.

## 2. What the Act says, with the text that decides each step

Line numbers are of `registers/source-bundle/TA1999.txt` (the consolidation headed "version in force from 2/10/2026") unless a file is named.
The 2000 Revised Edition numbers are 20 less than today's for ss 53 to 56 and s 85, and 23 less for ss 95 and 96 (s 34 is s 54; s 35 is s 55; s 36 is s 56; s 65 is s 85; s 72 is s 95; s 73 is s 96): the margin markers at `TA1999.txt:4884, 4907, 4931, 5937, 5950, 6994, 7003` say so.

1. **A broadcast receiver is "equipment", and its signal is "radio-communication", on the Act's words.**
   - "equipment" today: "any appliance, apparatus or accessory used or intended to be used for telecommunications, including (to avoid doubt) any such appliance, apparatus or accessory capable of being used for the operation of any broadcasting service" (lines 325-329).
     In the 2000 Revised Edition and as amended by Act 10 of 2005: "includes any appliance, apparatus or accessory used or intended to be used for telecommunication purposes" (`TA1999.20001230.txt:226-227`).
     Act 19 of 2011 section 2(b) substituted the current words for "telecommunication purposes" from 1 February 2012 (`TA1999.ACT19-2011.txt:49-54`; `TA1999.S33-2012.txt:23-24`).
   - "telecommunications" means "a transmission, emission or reception of signs, signals, writing, images, sounds or intelligence of any nature by wire, radio, optical or other electromagnetic systems" (lines 529-532; the same words in 2000 at `TA1999.20001230.txt:299-306`).
   - "radio-communication" means "any telecommunication by means of Hertzian or radio waves" (lines 450-451; `TA1999.20001230.txt:249-250`).
   - A receiver of broadcast pictures and sound, or of sound alone, carried by radio waves is equipment used for the reception of sounds (and images) by radio.
   - The Act has no defined term "radio-communication equipment".
   - The composition "equipment used for a telecommunication by Hertzian or radio waves" is a reading (FORK 1); on it, the receiver is radio-communication equipment (`sgta-s2-definitions.l4`).
2. **Possession.**
   - s 54(1) (lines 4894-4902): "A person must not — ... (b) possess any radio-communication equipment, except and in accordance with a licence granted under section 5 or any regulations made under this Act."
   - s 54(2) (lines 4904-4905): "Any person who contravenes or fails to comply with subsection (1) shall be guilty of an offence."
   - In the 2000 Edition it is s 34(1) and (2): "No person shall — ... (b) possess any radio-communication equipment, except and in accordance with a licence granted under section 5 or any regulations made under this Act", and "Any person who contravenes or fails to comply with subsection (1) shall be guilty of an offence" (`TA1999.20001230.txt:1246-1253`).
   - The two texts differ only in style ("must not" for "No person shall").
     The Gazette's own 2020 Revised Edition (31 Dec 2021) and the SSO consolidation of 2 Oct 2026 are word for word identical in ss 54, 55, 85 and 95 (compared by script on 2026-11-04 after normalising spacing, quotation marks and hyphens; `TA1999.RevEd2020-printed.txt:3875-3885, 3886-3907, 4696-4707, 5525-5534`).
3. **Use.**
   - s 55(1) (lines 4911-4916): a person who "establishes, installs, maintains, provides or operates a radio‑communication system or service or any radio‑communication equipment in any place ... in Singapore without a licence granted under section 5 or any regulations made under this Act shall be guilty of an offence"; the 2000 Edition says "in any place or on board any vessel, aircraft or in any vehicle in Singapore" (`TA1999.20001230.txt:1256-1261`).
   - s 55(2) (lines 4918-4920): "Any person who is in possession of any radio‑communication equipment is deemed, until the contrary is proved, to have operated the same."
   - s 55(3) and (4) (lines 4922-4929): "The occupier of any dwelling house or premises in which is installed any radio‑communication equipment in respect of which a licence is not in force shall be guilty of an offence", with the defence that the occupier "was not aware and could not with reasonable diligence have become aware".
4. **The penalty.**
   - Neither s 54 nor s 55 states a penalty.
   - s 85 (lines 5941-5950): a person guilty of an offence under the Act "for which no penalty is expressly provided shall, in addition to the forfeiture of any article seized, be liable on conviction to a fine not exceeding $10,000 or to imprisonment for a term not exceeding 3 years or to both and, in the case of a continuing offence, to a further fine not exceeding $1,000 for every day or part of a day during which the offence continues after conviction".
   - The 2000 Edition's s 65 has the same sentence without the words from "and, in the case of a continuing offence" (`TA1999.20001230.txt:1916-1920`); Act 10 of 2005 section 28 added them from 16 Feb 2005 (`TA1999.ACT10-2005.txt:961-964`).
   - "What conviction means": a criminal conviction in a Magistrate's Court or District Court, which may impose the full penalty (s 87, lines 5968-5973); seized equipment not prosecuted is forfeited to the Authority unless a claim is made within 2 months (s 57(3), lines 4993-4996).
   - The offence is compoundable by a sum of at most $5,000 (s 84(1), lines 5919-5930) where it is prescribed as compoundable; the Telecommunications (Composition of Offences) Regulations 2005 reg 2(a), in force 11 November 2005, name "34 (2), 35 (1) or (3)" of the Act, the 2000 numbers of s 54(2) and s 55(1) and (3).
   - The Act has an exclusive-privilege offence as well (s 53, lines 4831-4837, fine up to $100,000 or 3 years or both); I did not apply it to the receiver (FORK 2).
5. **The one carve-out in the Act for broadcast receivers.**
   - s 95 (lines 6987-6992): "This Act does not apply to the licensing of any broadcasting service or any broadcasting apparatus under the Broadcasting Act 1994 except in respect of the regulation of any telecommunication system required for the operation of any broadcasting service or the approval of any broadcasting apparatus used in accordance with section 11."
   - In the 2000 Edition it is s 72 and names "the Singapore Broadcasting Authority Act (Cap. 297)"; Act 10 of 2005 section 30 substituted "Broadcasting Act (Cap. 28)" from 16 Feb 2005 (`TA1999.20001230.txt:2030-2035`; `TA1999.ACT10-2005.txt:1188-1190`).
     The Act so named is the same Act: the Revised Edition 2003 of the Broadcasting Act is headed "1995 Ed. Cap. 297" (`BA1994.20030731.meta.json`, `header_as_printed`).
   - "Broadcasting apparatus" is "any apparatus capable of or designed or constructed for the reception of any broadcasting service and specified in the First Schedule" (Broadcasting Act, `BA1994.txt` lines 277-279; the Telecommunications Act has defined it by reference to that Act since 16 Feb 2005, `TA1999.ACT10-2005.txt:42-47`).
   - The First Schedule in the Revised Editions 2003 and 2012: "1. Broadcast television receiver. 2. Broadcast sound receiver. 3. Television receive-only satellite receiving system (TVRO system)" (`BA1994.20030731.txt:2139-2143`; `BA1994.20120831.txt:2167-2169`); "broadcast sound receiver" means "any apparatus used for the aural reception of any broadcasting service" and "broadcast television receiver" means "any apparatus used for the visual and aural reception in monochrome or colour of any broadcasting service" (`BA1994.20120831.txt:2171-2174`).
   - G.N. No. S 549/2012, made 30 Oct 2012, first published 31 Oct 2012 at 5.00 pm, "shall be deemed to have come into operation on 1st January 2011" and substitutes a First Schedule with one item, the TVRO system (`BA1994-S549-2012.txt:3, 21-22, 27-33, 37`).
     The current text (from 25 Sep 2024) lists the TVRO system alone (`BA1994.txt:4340-4357`); the Act's history lists S 549/2012 as the only notification amending the First Schedule (`BA1994.txt:4645-4648`).
6. **The Broadcasting Act's own licence, for the days a receiver was listed.**
   - s 20(1): no person shall "(a) install any broadcasting apparatus in any place, or on board any ship, aircraft or vehicle registered in Singapore; (b) import, offer for sale, sell or have in his possession with a view to sale, any broadcasting apparatus; or (c) operate or have on any premises in Singapore owned or occupied by him broadcasting apparatus on or by which broadcasting services are received, except under and in accordance with a licence granted under this section" (`BA1994.20030731.txt:701-710`); s 20(4): "The Authority may exempt any person or broadcasting apparatus or class of broadcasting apparatus from subsection (1)" (`:719-720`).
   - Whether a licence was in fact required on a given day, and what it cost, is the Broadcasting Act folder's answer, not this file's.

## 3. The instruments that could cover the person, and what each says

The instruments below are made under the Act; the 40 texts are IMDA's copies of the 2002 and 2004 Revised Editions and every gazetted amendment IMDA lists (all fetched 2026-11-03, deposited under `subjects/sg/telecommunications-*`).
On 2026-11-04 the e-Gazette's copy of 25 of those amendments was deposited beside the IMDA copy and compared with it (`NOTES.md` finding 23: the IMDA copies carry a few extraction defects in printed values, now corrected from the Gazette; the e-Gazette's copies replace the OCR text of the two scanned instruments, S 685/2011 and S 686/2011), and five instruments that IMDA's list lacks were deposited: S 525/2001 and S 78/2017 (N 1), S 485/2016 (Rg 3), S 23/2011 and S 24/2011 (the Designated Telecommunication Licensees notifications); only S 525/2001 bears on the question (finding 24: it is the Schedule the Revised Edition prints, so N 1 now answers from 17 October 2001, and the seat's answer for those days stays NOTHING because the Broadcasting Act's First Schedule is not deposited before 31 July 2003).
IMDA's list ends at S 726/2014 for N 1, S 100/2016 for Rg 5 and S 725/2014 for Rg 6, and the e-Gazette added S 78/2017 for N 1; whether either list is complete is not established.
The mechanical search of all deposited texts for a receiver, a sound or an AM or FM band is in section 10.

| Instrument | Where it could cover a receiver | What it says (quoted from the deposited text) | Covers? |
| --- | --- | --- | --- |
| Exemption Notification (Cap 323, N 1), made under s 73 (now s 96) | para 2 and the Schedule | para 2: "Sections 33, 34 (1) (b) and 35 of the Act shall not apply to any person in respect of —" (a) a station permitted under reg 75 of Rg 5, and (b) "the localised on-site installation or operation of the equipment specified in the Schedule". The Schedule has no item for a broadcast receiver as such. Item 11 is "Remote Control Devices" with sub-items (a) to (f), and (e) is "TV Receivers/ Radio Systems" (`TA1999-N1.txt:110`). Item 14 is "Stand-alone GPS Receivers". Item 15 (2002 to 31 October 2014) is "Communication Receivers (excluding Scanning devices) and Microwave Multipoint Distribution Systems (MMDS) Receivers" at 2.505 to 2.665 GHz. | Not on the natural reading. FORK 5. |
| Radio-communication Regulations (Cap 323, Rg 5) | reg 2 "station", reg 19(1), reg 65 | A "station" includes "a receiver" (`TA1999-RG5.txt:273-274`). Reg 19(1) says a station "may be possessed ... if authorised by" a spectrum licence, a station or network licence, or a class licence. Reg 65 gives a class licence to a person who possesses or uses a "relevant radio-communication station", meaning one connected with a public cellular mobile telephone system, radio paging system, mobile data system, trunked radio system, satellite mobile system (and from 1 June 2006 a public wireless broadband access system), or capable of being used with one. | No: a broadcast receiver is connected to none of them. |
| Class Licences Regulations (Cap 323, Rg 3) | reg 3 | Class licences for operators of telecommunication systems and services. | No: it concerns operators. |
| Dealers Regulations (Cap 323, Rg 6) | reg 22(1) from 21 July 2005 | "Any person intending to use any telecommunication equipment for personal purposes shall not be required to obtain the approval of the Authority provided that such equipment is designed, constructed, installed, established, maintained and operated in accordance with such standards and specifications as may be published by the Authority" (`TA1999-RG6-S478-2005.txt:145-150`; its subparagraph (2) at line 150). | Not on Reading X (it is about approval). FORK 4. |
| Dealers Regulations, Second Schedule para 9 and First Schedule | | A Dealer's Class Licensee "shall inform every purchaser or hirer ... of the need to obtain a licence from the Authority under the Act and these Regulations for the possession, operation, installation or use of that telecommunication equipment" (`TA1999-RG6.txt:503-506`); the First Schedule, "Telecommunication equipment not requiring approval", lists thirteen items and no television or radio receiver (`TA1999-RG6.txt:418-434`). | Neither covers the person. |
| Composition of Offences Regulations 2005 | reg 2(a) | Names the 2000 Edition offences ss 34(2), 35(1), (3) as compoundable from 11 November 2005. | It is a consequence of the offence, not a cover. |

No notification, order or licence-class instrument that names an ordinary aerial television set or a radio receiver was found among the 45 instrument texts (the 40 IMDA copies, with the Gazette's copies of S 685/2011 and S 686/2011 in place of the OCR, and the five instruments the e-Gazette supplied).
Rg 5 is encoded in full, and every other group is too (`COVERAGE.md`: no row pending).

## 4. The forks on the path

FORK 1, "radio-communication equipment".
The Act defines "equipment" and "radio-communication" but not "radio-communication equipment" (`TA1999.txt` lines 325-329, 450-451).
Reading 1: the term is the two definitions put together word for word, equipment used or intended to be used for a telecommunication by Hertzian or radio waves; a receiver of a broadcast carried by radio waves is within it, whether it carries pictures and sound or sound alone.
Reading 2: "radio-communication equipment" in s 54(1)(b) and s 55 means equipment for two-way or point-to-point radio-communication, because most licence types in Rg 5 Part VI (ship, aircraft, amateur, experimental, localised radio-communication, special purpose stations) are for stations that transmit, and because s 2 defines "telecommunication service" so as to exclude any broadcasting service, which suggests the Act's licensing is not aimed at receiving broadcasts.
I take Reading 1, which is the text; Reading 2 is a purposive reading and belongs to the s 9A weighing in section 7.
The text that licenses Reading 1: the definitions themselves; the two definitions of "station" that list "a receiver" (the Act's s 14(2), `TA1999.txt` lines 1332-1345, and Rg 5 reg 2); and Rg 5 reg 49, under which the General Radio-communication Station Licence enables a licensee "to transmit, receive or transmit and receive messages by means of radio-communication" (so the regulations contemplate licensing a receive-only station).
Nothing in either reading distinguishes a television from an FM or an AM radio: all three receive sounds by radio waves (section 10).

FORK 2, s 53 and "using".
Not applied to the receiver; see the bullet list at the end of this section.

FORK 3, s 95 (s 72 of the 2000 Edition).
Reading A: for apparatus the Broadcasting Act's list names, the licensing question belongs to that Act alone, so the Telecommunications Act's "except in accordance with a licence granted under section 5" requirement does not apply to it.
Reading B: s 95 switches off only the Authority's licensing machinery and leaves ss 54 and 55 as written.
It changes the answer only for apparatus that is on the First Schedule: a television receiver and a sound receiver for conduct before the days S 549/2012 reaches (and for readings before 31 Oct 2012), and the satellite dish system always.
`sgta-part6-offences.l4` has both readings; the seat uses A.

FORK 4, Rg 6 reg 22(1).
Reading X: it says a person need not obtain the Authority's approval (the approval s 11 requires for equipment connected to a telecommunication system or used with one) for personal-use equipment that meets published standards, and says nothing about a licence under s 5 or about s 54(1).
Reading Y: it is a regulation made under the Act that regulates personal use, so possession in accordance with it is "in accordance with ... any regulations made under this Act" (s 54(1)).
Whether the Authority has published standards that a broadcast receiver meets is not shown by any deposited source.
On Reading Y with a conforming set, the person is not guilty from 21 July 2005 (case in `sgta-tv-cases.l4`); on X it makes no difference.

FORK 5, N 1 item 11(e).
Reading X: Item 11 is "Remote Control Devices" and each of (a) to (f) names what the remote control controls: garage doors, cameras, toys and robots, cars and boats, television receivers and radio systems, others.
So (e) is a remote control for a television or a radio system, not the receiver.
Reading Y: (e) names the receivers themselves as equipment whose localised on-site operation is exempt, in the bands and powers the item gives.
CORRECTION to the 2026-11-03 text of this file, which said that on Y with local use the person is exempt on every date: the exemption is for "the equipment specified in the Schedule", and the Schedule specifies each item with its "Authorised Radio Frequency Bands" and "Maximum Approved Field Strength or Power".
Item 11's bands are 26.96 to 27.28 MHz and 40.66 to 40.70 MHz in the Revised Edition, and 26.96 to 27.28, 34.995 to 35.225, 40.665 to 40.695, 40.770 to 40.830 and 72.130 to 72.210 MHz from 2 Jan 2008 (read from `sgta-i-n1-bands.l4`'s item 11 function on 1 Jan 2003, 2 Jan 2008, 1 Apr 2011); none is a broadcast band.
So on Y the exemption reaches the receiver only while it is used in those bands, which a broadcast receiver is not; the seat asks that as a fact (`only in a band the item authorises`), and a case shows both answers.
I take X.

FORK 6 (new), s 2 "equipment" before 1 February 2012.
The words were "used or intended to be used for telecommunication purposes" until Act 19 of 2011 section 2(b) substituted "telecommunications, including (for the avoidance of doubt) any such appliance, apparatus or accessory capable of being used for the operation of any broadcasting service" on 1 February 2012 (S 33/2012, published 31 Jan 2012).
Reading P: "telecommunication purposes" already covers a receiver of broadcasts, because reception of sounds and images by radio is "telecommunications" (s 2) and the purpose of receiving a broadcast is a telecommunication purpose.
Reading Q: the earlier words leave a broadcast receiver out, because the legislature added express words about broadcasting "for the avoidance of doubt".
The text for P: the Bill's explanatory statement says "Clause 2(b) amends the definition of 'equipment' in section 2 to clarify that the term includes any appliance, apparatus or accessory used or intended to be used for telecommunications which is also capable of being used for the operation of any broadcasting service" (`TA1999.BILL20-2011.txt:2571-2574`).
The text for Q: the words "(for the avoidance of doubt)" themselves, which show a doubt was felt.
I take P.
The explanatory statement is extrinsic material (Interpretation Act s 9A(2), section 7), not part of the Act.

Two further points are not forks in the encoding but are open on the text:
- (From 1 Feb 2017 s 53(1) also reaches a person during the suspension of the person's licence: Act 30 of 2016 section 18; the television's owner holds no licence to suspend.)
- s 53(1) reaches an act that "otherwise infringes the privilege conferred upon the Authority by section 3", and s 3(2)(a) lists "using" among the privileged rights over "telecommunication systems and services".
  Whether a household set receiving a broadcast is "using a telecommunication system" is not decided by any text I found; I did not apply s 53.
- "Possess" in s 54(1)(b) and "operates" in s 55(1) are not defined; I read an owner who has the receiver in the home as possessing it, and a person who switches it on as operating it, which s 55(2) presumes from possession.

## 5. The dates

### Date (1): before the television and radio receiver licence ended

What the texts show:
- The Revised Edition 2003 of the Broadcasting Act (31 Jul 2003) lists "Broadcast television receiver" and "Broadcast sound receiver" in the First Schedule, and s 20(1)(c) requires a licence to "operate or have on any premises in Singapore owned or occupied by him broadcasting apparatus on or by which broadcasting services are received" (`BA1994.20030731.txt:701-710, 2139-2143`).
- So on Reading A of s 95 the Telecommunications Act did not apply to the licensing of a television or radio receiver, and the Broadcasting Act's s 20 and s 47 did.
- The Revised Edition 2012 (31 Aug 2012) prints the same three items (`BA1994.20120831.txt:2167-2169`); I assume the list did not change in between, because both ends print the same three items and the Act's history lists no other notification.
- EXTRINSIC: Hansard, 8 March 2013, Committee of Supply (lawplain speech id 2013-03-08-084): "even after we stopped collecting radio and TV licence fees in 2011".
- EXTRINSIC and NOT USED as a source: a search-engine summary of an MDA press release of 18 February 2011 says the radio and television licence was abolished with effect from 1 January 2011; the press release page could not be read, so it is not cited as a text.

The instruments behind the licence (deposited by the Broadcasting Act folder on 2026-11-04 and read here for facts; this folder deposits none of them):
- The licence of s 20(1) was provided for by the Broadcasting (Television and Radio Licensing) Regulations (Rg 1), Revised Edition 2004 (29 Feb 2004; `BA1994-RG1.txt`): licences for broadcast sound receivers (Part IV, regs 23 to 26), for broadcast television receivers (Part V, regs 27 to 35) and block licences for hotels and hospitals (regs 36 and 37).
  Reg 27(1): "No person shall operate a broadcast television receiver without a licence" (this sentence stood from 29 Feb 2004 to 20 Jun 2004 only: S 333/2004 deleted it from 21 Jun 2004, below and section 12); reg 27(3): a television licence "shall permit the use of one or more broadcast television receivers and one or more broadcast sound receivers by the licensee, members of his family and domestic servants resident at the address specified therein" (`BA1994-RG1.txt:481-488`).
  Reg 23(1): "A licence shall be required for every broadcast sound receiver installed in a vehicle or in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act" (`:441-444`).
  The fees are in its First Schedule: a licence for a broadcast television receiver in monochrome $40 per annum and in colour $110 per annum, for a broadcast sound receiver $27 for 12 months, and for dealing in either $330 per annum (`:624-633`).
- S 333/2004 (made 11 Jun 2004, first published 15 Jun 2004 at 5:00 pm, in operation 21 Jun 2004; `BA1994-S333-2004.txt:3, 21-23`) amended Rg 1 in 23 clauses.
  The ones that bear on a receiver:
  - cl 12(a) deletes reg 27(1) and (2) and substitutes one paragraph, "An application for a licence to install or operate a broadcast television receiver may be made at any post office or at such other places as the Authority may require" (`:137-144`).
    From 21 Jun 2004 reg 27 no longer says that no person shall operate a broadcast television receiver without a licence; reg 27(3) remains, and reg 27(4) now reads "installed or operated by" (`:145-146`; `BA1994-RG1.txt:485-493`).
  - cl 6 deletes "or of regulation 17, 27 or 36" from reg 7, which then speaks of a contravention of "section 20 (1) of the Act" alone (`:92-94`; `BA1994-RG1.txt:264-266`).
  - cl 11(a) deletes reg 23(1) and (2) and substitutes (1), where to apply, and (2), "A licence shall be required for every broadcast sound receiver in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act (Cap. 323)" (`:123-133`), so a vehicle is no longer named in reg 23.
  - cl 13 replaces reg 28(1) (the mounting of a television so that its screen cannot be seen from the driving or helmsman's position) and amends (5); reg 28(2), a separate licence for every television installed in a vehicle or vessel without a ship station licence, is not amended (`:149-160`).
  - cl 14 inserts reg 29A(1), "A separate licence shall be required for every broadcast television receiver installed in a commercial property" (`:162-167`), with "commercial property" defined in reg 2 as premises permitted to be used wholly or partly for business, or occupied by a charity, other than a hotel, hospital or institution providing education or instruction (`:34-42`).
  - cl 2 deletes the definitions of "broadcast sound receiver" and "broadcast television receiver" (the second ended "but does not include any Television Receive-Only Satellite Receiving System") and the definition of "TVRO system", and defines "broadcasting apparatus" (any broadcast sound receiver or broadcast television receiver) and "licence" (any licence granted under section 20 of the Act in respect of any broadcasting apparatus) (`:25-54`).
  - Also: cl 3 deletes regs 3 and 4; cl 4 changes reg 5 so that a licence is "valid for such period as the Authority may determine" (`:59-66`); cl 8 deletes regs 12 and 14; cl 10 deletes regs 16 to 22 and substitutes a new reg 16 (the application for a dealers' licence); cl 19 replaces reg 36 (block licences also for the owner or occupier of a commercial property); cl 23 substitutes the Second Schedule.
  The First Schedule, where the fees are, is not amended.
- S 548/2012, the Broadcasting (Television and Radio Licensing) (Revocation) Regulations 2012 (`BA1994-S548-2012.txt`), made 30 Oct 2012 under s 66 of the Broadcasting Act, first published 31 Oct 2012 at 5.00 pm (the same day and hour as S 549/2012): reg 1 says it "shall be deemed to have come into operation on 1st January 2011"; reg 2(1) revokes Rg 1; reg 2(2) keeps Rg 1 applying to licences granted under s 20(1) "for any period before 1st January 2011"; reg 2(3) refunds in full any fee paid in advance for a period commencing on or after 1 Jan 2011 (`BA1994-S548-2012.txt:28-57`).
- So the receiver licence, as instruments show it, was the Broadcasting Act's s 20(1) licence on the First Schedule's list, provided and priced by Rg 1; it ended for conduct from 1 Jan 2011 by two instruments published together on 31 Oct 2012, S 549/2012 (the First Schedule) and S 548/2012 (the regulations), each deemed in operation from 1 Jan 2011.
  A reader before 31 Oct 2012 saw Rg 1 (as amended by S 333/2004 from 21 Jun 2004) and the list unchanged; a reader from that day sees both gone for 2011 on.
  Rg 1 is not deposited before its Revised Edition 2004 (29 Feb 2004), so what licensed a receiver between 31 Jul 2003 and 28 Feb 2004 is not shown by a regulation text.
- The seat takes the First Schedule's list and whether Rg 1 is in operation as inputs of the two days (`sgta-tv-ba-schedule.l4`), and, since the correction of section 12, says what each of Rg 1's three versions (the Revised Edition 2004, as amended by S 333/2004, as revoked by S 548/2012) said in terms about a licence for a kind of receiver in a place.
  For a television, an FM radio and an AM radio they say the same on every pair of days where both are known (assertions in `sgta-tv-cases.l4`), so the Telecommunications Act answers above do not change.

What the texts do not show: whether the Broadcasting Act's s 20 licence was enforced or priced for sets between 1 January 2011 and 30 October 2012 as a matter of practice (S 548/2012, read from 31 Oct 2012, says no fee was payable for any period from 1 Jan 2011), whether s 20(1)(c) alone, without a regulation naming a household radio, required one (the regulations name sound receivers only in a vehicle or a vessel, reg 23, and price "a broadcast sound receiver" at $27 for 12 months, First Schedule item 2; I have not answered it), and the First Schedule before 31 July 2003.
The Telecommunications Act answer for conduct on 31 Dec 2010 is therefore: no offence under that Act on Reading A, an offence on Reading B, whatever day it is read.
Before 31 Jul 2003 the sources do not answer.

The Radio-communication Regulations (Cap. 323, Rg 3), 1999 Revised Edition, governed 1 Dec 1999 to 1 Mar 2001 (added 2026-11-04, Part 3 of the follow-up; no answer in this section changes).
Reg 2 defines "station" as "a transmitter, receiver, a combination of transmitters and receivers or any accessory thereto which is used or intended to be used for radio-communication" (`TA1999-RADIO99.txt:231-233`), and reg 4(1) reads "Except as provided in the First Schedule, no person shall possess, establish, install or use any station in any place or on board any local vessel or aircraft or in any vehicle in Singapore unless he has a valid licence granted under these Regulations" (`:249-252`).
The First Schedule exempts 15 kinds of equipment from the station licence "for in-building or localised on-site operations" (`:1043-1048`); a search of the deposited text for "television", "broadcast" and "sound" finds no hit, and item 15 names "Communication Receivers (excluding scanning devices) and Microwave Multipoint Distribution Systems (MMDS) Receivers" (`:1181-1193`).
The Regulations were continued by s 98(2) of the Act from 1 Dec 1999 and were revoked from 2 Mar 2001 by reg 80(1) of S 114/2001 (`TA1999-RG5-S114-2001.txt:1548-1549`).
They are encoded in `sgta-i-rg3-1999.l4`, beside the Dealers Regulations (Rg 7) of the same Edition in `sgta-i-rg7-1999.l4`; the seat does not consult either.
The seat answers NOTHING on the texts deposited for a television owned on each of 15 Dec 1999, 29 Dec 2000, 30 Dec 2000, 15 Jan 2001, 1 Mar 2001 and 2 Mar 2001, read on 4 Nov 2026 (six `#EVAL` lines run on 2026-11-04 in a probe file that was deleted after).
For 1 Dec 1999 to 29 Dec 2000 no printed text of the Act is held, the earliest being the Revised Edition 2000 of 30 Dec 2000; for 30 Dec 2000 to 2 Mar 2001 the Act is held but the seat's tables for N 1 and Rg 5 begin on 2 Mar 2001 and that for Rg 6 on 2 Apr 2003 (`sgta-i-versions.l4`).
Whether a television set is a "station" on these words turns on the questions of section 4 (FORK 1), which I have not applied to this text; I do not answer the receiver question for those days.

### Date (2): from 1 January 2011 to 2019

The decisive fact is S 549/2012, and it is a fact about WHEN THE LAW IS READ.
- Conduct on 1 January 2011, read on 1 August 2012: the First Schedule (Revised Edition 2003, the Revised Edition 2012 not yet printed) lists a television and a sound receiver; no offence under the Telecommunications Act on Reading A.
- The same conduct read on 31 October 2012 or later: S 549/2012, deemed in operation from 1 January 2011, has substituted a Schedule that lists the TVRO system alone; the receivers are not listed for 1 January 2011 onward; s 95 does not apply to them; ss 54(2) and 55(1) apply on Reading 1 of FORK 1.
- The pair is tested in `sgta-tv-cases.l4` for each of the television, an FM radio and an AM radio, and the satellite dish system stays "no offence" on both sides.
- A reader of the Gazette on 30 October 2012 could not know of S 549/2012, and S 549/2012 is retrospective in its effect on the Broadcasting Act's list.
  Whether it can make a person's conduct on a day before 31 October 2012 an offence under the Telecommunications Act is a question the encoding does not answer; the natural place to look, which I have not read and which is not deposited, is Article 11 of the Constitution of the Republic of Singapore.

The Act's own versions (`sgta-ta-versions.l4`; each row is {effective day, published day}):
- Revised Edition 2000: 30 Dec 2000.
- Act 10 of 2005: effective 16 Feb 2005 (the Act's history, `TA1999.txt:7134-7143`), first published 16 Feb 2005 at 5:00 pm (`TA1999.ACT10-2005.txt:10`, checked against the page image).
  It added the daily fine to the general penalty, the definitions of "broadcasting apparatus" and "broadcasting service", and the name of the Broadcasting Act in s 72; it touched none of ss 33 to 36 or 73.
  Its commencement notification, S 76/2005 (first published 16 Feb 2005 at 5:00 pm), is deposited (`TA1999.S76-2005.txt:3, 23-25`): the whole Act comes into operation on 16 Feb 2005 except sections 10 and 11, which are on neither the television's path nor the radio's (s 10 repeals s 19; s 11 amends s 20(5)).
- Act 19 of 2011: first published 20 Jan 2012 at 5:00 pm with no date of effect (`TA1999.ACT19-2011.txt:9`); S 33/2012, made 10 Jan 2012 and first published 31 Jan 2012 at 5.00 pm, brings it into operation on 1 Feb 2012 (`TA1999.S33-2012.txt:3, 23-24`).
  I take 31 Jan 2012 as the day the new version is published.
  It changed "equipment" and "telecommunication system" (s 2), and it did not touch ss 33 to 36, 65, 72 or 73.
- Act 22 of 2016, the Info-communications Media Development Authority Act 2016: effective 1 Oct 2016, first published 29 Sep 2016 (`TA1999.ACT22-2016.txt`, `TA1999.S461-2016.txt`); its section 100 changes definitions in s 2 ("Authority", "Chief Executive"), ss 21(1A), 27(1A), 59A, 64(3) and 69C(2)(a), and touches none of ss 33 to 36, 65, 72, 73 or "equipment".
- Act 30 of 2016, the Telecommunications (Amendment) Act 2016: first published 9 Jan 2017, S 14/2017 (first published 13 Jan 2017) appoints 1 Feb 2017, so the version counts as published on 13 Jan 2017 (`TA1999.ACT30-2016.txt`, `TA1999.S14-2017.txt`).
  Its section 18 amends s 33(1), now s 53(1), the prohibition on running a telecommunication system or service without a licence, to add ", or during the suspension of the person's licence under section 8"; it does not touch ss 34, 35, 65, 72 or 73 or "equipment".
- Act 15 of 2017, the Companies (Amendment) Act 2017: first published 30 Mar 2017 (Acts Supplement No. 17 of 2017; `TA1999.ACT15-2017.txt`); it comes into operation on a date the Minister appoints, and the Legislative History gives 23 May 2017 (its commencement notification is not deposited, so that day, and my assumption that it was published the same day, rest on the history alone).
  Its only amendment of the Telecommunications Act is section 53(6), which inserts "or 211I" in ss 32J(3)(a) and 32L(1)(b) and (2)(a) (`TA1999.ACT15-2017.txt:4217-4219`); it touches none of ss 2 "equipment", 33 to 36, 65, 72 or 73, so the printed texts answer through 15 May 2018 with the same words as before it (`NOTES.md` finding 28).
- Eight Acts and one Order after Act 15 of 2017 are deposited as enacted and encoded (section 8), but the seat does not use them; the Act's history lists Act 26 of 2018 (s 61, 16 May 2018) next (`TA1999.txt:7192-7205`).
  For conduct from 16 May 2018 to 1 Oct 2026 only the markers speak: the words of ss 54, 55, 85 and 95 are identical in the Gazette's 2020 Revised Edition of 31 Dec 2021 and in the 2 Oct 2026 consolidation, and the margin markers show no amendment of ss 54 and 55 after 2000, nor of ss 85 and 95 after 2005.
  What I cannot exclude is an Act in between that changed one of them and was changed back.

For the instruments, the days tested on each side of every change I found (each with a reading day, the instruments' effective and published days being in `sgta-i-versions.l4`): N 1 on 15 Dec 2003, 28 Oct 2004, 18 May 2006, 2 Jan 2008, 1 Apr 2011, 25 Apr 2013, 23 Jun 2014, 1 Nov 2014; Rg 5 on 2 Mar 2001, 9 Jul 2001, 1 Aug 2001, 18 Sep 2001, 11 Nov 2005, 1 Jun 2006, 2 Oct 2009, 21 Jan 2011, 1 Apr 2016; Rg 6 on 21 Jul 2005, 23 Jul 2007, 15 Apr 2010, 1 Apr 2011, 25 Apr 2013, 23 Jun 2014, 1 Nov 2014.
None of these dates changes the answer for this person (Reading B cases in `sgta-tv-cases.l4`).
Every published day is read from the "First published in the Government Gazette" line of the e-Gazette copy of the instrument, and every effective day from its commencement clause (`NOTES.md` finding 26; for example S 20/2011: published 17 Jan 2011, effective 21 Jan 2011; S 100/2016: published 7 Mar 2016, effective 1 Apr 2016; S 210/2010: published 8 Apr 2010, effective 15 Apr 2010; S 726/2014: published 31 Oct 2014, effective 1 Nov 2014).
The assumed days are the two Revised Editions' start days (1 Jan 2003 for N 1 and Rg 5, 1 Jan 2005 for Rg 6; N 1 and Rg 5 have rows before it from 2 Mar 2001, the Regulations as made), and, for the Act, the published days of the Act 15 of 2017 row (23 May 2017), of the row standing for the Acts after it (16 May 2018) and of the 2026 consolidation (2 Oct 2026).

s 2 "equipment" across 1 February 2012 (FORK 6): on Reading P (the default) the answer does not change across the edge; on Reading Q it does, and the pair (1 Feb 2012 conduct, read on 30 Jan 2012 against read on 31 Jan 2012) shows it with the Broadcasting Act's list set aside.

### Date (3): today

The deposited Act (in force from 2 October 2026) and the instruments last listed by IMDA give an offence under s 54(2) for possessing the receiver and under s 55(1) for operating it, with the maximum penalty in s 85 as above.
Which instrument covers or fails to cover: none covers on the natural reading (Rg 5 reg 65, in every vintage from the Regulations as made (S 114/2001, in operation 2 Mar 2001) on, covers no broadcast receiver; reg 65 has the same words as made as in the 2002 Revised Edition, and the four amendments of 2001 do not touch it; N 1's Schedule never named one; Rg 6 reg 22(1) began 21 July 2005 and is about approval).
That is the answer on the Act's words.

## 6. Hypotheses H1 to H6

| Hypothesis | Verdict | Citation |
| --- | --- | --- |
| H1. A receiver licence obligation existed, and it ended around 2011. | Supported by instruments, with a twist the hypothesis does not have: the obligation was the Broadcasting Act's s 20 licence for apparatus on the First Schedule, which listed television and sound receivers, provided for and priced by the Television and Radio Licensing Regulations (Rg 1: television $40 or $110 a year, sound receiver $27 for 12 months; the regulations' own sentence forbidding a television to be operated without a licence, reg 27(1), stood from 29 Feb 2004 to 20 Jun 2004 only, section 12). It ended by two instruments published together on 31 Oct 2012 at 5.00 pm and each deemed in operation from 1 Jan 2011: S 549/2012 removed the television and sound receivers from the list, and S 548/2012 revoked Rg 1 (saving licences for earlier periods and refunding advance fees for later ones). That fees stopped in 2011 is now on the instruments; Hansard 2013 (EXTRINSIC) is no longer the only support. | `BA1994.20030731.txt:701-710, 2139-2143`; `BA1994-RG1.txt:441-444, 481-488, 624-633`; `BA1994-S333-2004.txt:123-144`; `BA1994-S548-2012.txt:28-57`; `BA1994-S549-2012.txt`; Hansard 2013-03-08-084 (extrinsic) |
| H2. When it ended, nothing was put in its place, so possession or use of an ordinary analogue terrestrial receiver became an offence under the Telecommunications Act, maximum $10,000 and 3 years. | On the Act's words and the instruments I could reach: the sections and the maximum are right (s 54(2), s 55(1), s 85), but only for the days the law is read as including S 549/2012, that is from 31 Oct 2012, and then for conduct from 1 Jan 2011. For the same 2011 conduct read in 2011, the Telecommunications Act did not apply to a listed receiver. That "nothing was put in its place" is an absence: S 548/2012 revokes Rg 1 and says nothing further, S 549/2012 only deletes the entries, and I found no covering instrument among the deposited Telecommunications Act instruments or the 26 deposited Broadcasting Act instrument texts. | `TA1999.txt:4894-4905, 4911-4929, 5941-5950`; `TA1999.20001230.txt:1246-1275, 2030-2035` |
| H3. Some instrument covers that person, so H2 is false. | Not confirmed and not refuted: no instrument covers on the natural reading of each; two readings (Rg 6 reg 22(1) as an authorisation, N 1 item 11(e) as naming the receiver, and for the latter only in the item's bands) would cover. | N 1 para 2, Schedule item 11(e); Rg 6 reg 22(1) |
| H4. Low-power FM transmitters (88 to 108 MHz) being lawful is what covers FM radio receivers. | Refuted as a mechanism, re-tested on 2026-11-04 (section 10(c)): the entries at 88.00 to 108.00 MHz are item 3 of N 1 (wireless microphones) and item 1 of the Rg 6 Fifth Schedule (short range devices); each gives a limit on field strength, which is a limit on a transmitter, and neither names a receiver. Nothing exempts possession of a receiver. | N 1 Schedule item 3 (`TA1999-N1.txt:48-52`); Rg 6 Fifth Schedule item 1 (`TA1999-RG6-S251-2013.txt:84-126`) |
| H5. A type-approval or technical-specification regime for digital TV receivers ("IMDA TS DVB-T2 IRD") covers digital sets from 2019. | Refuted as stated: the only instrument text that names such equipment is item 3 of the Rg 6 Fifth Schedule ("Integrated receiver decoder devices intended for use with second generation digital terrestrial television broadcasting system"), inserted by S 251/2013 from 25 April 2013, and the Fifth Schedule lists equipment for which registration and renewal fees do not apply. It does not mention a licence to possess, and it dates from 2013. The technical specification itself was not obtained. | Rg 6 Fifth Schedule item 3 (S 251/2013) |
| H6. Satellite receivers (TVRO) are individually licensed under the Broadcasting Act. | Confirmed that a TVRO system needs a broadcasting apparatus licence (s 20(1)(c), First Schedule item 1; penalty s 47), and the list kept it in every version. Refined: the TVRO Regulations allow a licence only to an institution (reg 3(2): "No person other than an institution may be granted with a licence"; "institution" is "any body of persons, corporate or unincorporate, and includes any undertaking"), so a household as such cannot hold one. | `BA1994.txt:1425-1452, 3676-3681, 4346-4357`; `BA1994-RG3.txt` regs 2, 3(2) (BA folder) |

## 7. Interpretation Act s 9A

Interpretation Act 1965 s 9A is encoded at `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/` and is cited here, not re-encoded; stable l4 cannot IMPORT across folders, so there is no code link.
`sgta-tv-seat.l4` has `s 9A: the weighing of the literal answer`: it takes the literal answer and a court's finding, echoes the literal answer unchanged, and says whether a court may look at extrinsic material to find the meaning.

Is the literal reading absurd?
I think there is a real argument that it is, and I do not decide it.
For: on the Act's words every person who owns a household aerial set or a radio commits a continuing offence unless they hold a licence that nobody is shown to issue; the class licence in Rg 5 reg 65 reaches only stations tied to public mobile systems; the State collected fees from owners of such sets until 2011 and then stopped (EXTRINSIC, Hansard 2013-03-08), and encouraged households to buy digital receivers and indoor antennas to keep watching free-to-air channels (EXTRINSIC, Hansard 2013-07-08, lawplain speech id 2013-07-08-120); and the retrospective S 549/2012 is the step that took the receivers out of the Broadcasting Act's list and, with them, out of s 95's carve-out.
Against: s 54(1)(b) is general and clear; the Act has a mechanism for broadcast receivers (s 95 and the First Schedule) and the notification removed them from it; there are exemption powers (s 96, reg 79 of Rg 5 and reg 25 of Rg 6) that the authorities may use without gazetting a notice; and the offence is compoundable.
The Bill 20/2011 explanatory statement ("to clarify that the term includes ... broadcasting") bears on FORK 6 only.
The purposive outcome is left open.
Every citation of Hansard or of the Gazette in this paragraph is extrinsic material, used for purpose and for dates, never as the rule.

## 8. What could not be sourced

- The Singapore Statutes Online consolidations of the Act by date (SSO lists 19991201, 20001230, 20050216, 20120201, 20161001, 20170201, 20170523, 20180516, 20200101, 20200730, 20210301, 20211231, 20220113, 20220401, 20221101, 20251001 in `TA1999.meta.json`): no attempt was made (the Broadcasting Act encoder's single attempt at 03:07:48 SGT on 2026-11-04 ended in a 403 at robots.txt, and mine was gated on it).
  The Gazette copies of the Revised Edition 2000, Act 10 of 2005 and Act 19 of 2011 replace them for ss 2, 34, 35, 36, 65, 72 and 73; they are my assembly from primary texts and not an official consolidation.
- The Acts after Act 15 of 2017 as enacted (`TA1999.txt:7192-7302`): eight Acts and one Order that amend the Telecommunications Act are now deposited and encoded in `sgta-i-acts-after-2017.l4` (Act 26 of 2018, Act 15 of 2019, Act 40 of 2018, Act 4 of 2021, Act 25 of 2021, Act 12 of 2020, Act 13 of 2026 and Act 31 of 2022, with its commencement notification S 850/2022, and the Order G.N. No. S 26/2022; the Gazette's copies, deposited 2026-11-04).
  None of the nine amends s 34, 35, 36, 65, 72 or 73 of the 2000 Edition (ss 54, 55, 56, 85, 95 and 96 today) or the definitions of "equipment", "radio-communication" or "broadcasting apparatus" in s 2.
  Act 4 of 2021 changes only the definition of "owner" (it removes the HUDC housing estate words), which discharges the doubt this section used to record about it; Act 12 of 2020 changes only the name of the strata statute in "common property" and "owner".
  Act 25 of 2021 changes one word, "leave" to "permission", in s 33(7) of the 2000 Edition, now s 53(7) (the notice of the defence in the licensing offence).
  The seat does not consult these Acts: its version table still has the one row for them, so the days from 16 May 2018 to 1 Oct 2026 are still answered from the consolidation's margin markers, as before.
  Act 31 of 2022 (s 21(7): in s 46(3)(b) of the 2020 Edition, "Part 7" becomes "Parts 7 and 9" of the Insolvency, Restructuring and Dissolution Act 2018; in operation 1 Nov 2022 by S 850/2022) and G.N. No. S 26/2022 (paragraph 22: "(including a VCC)" in the definition of "securities", new definitions "VCC" and "VCC Act" in s 2, and ", the Trustees Act 1967 and the VCC Act" in ss 40(7)(a) and 41(7)(a); in operation 13 Jan 2022) are deposited too; none touches a provision the chain uses (`NOTES.md` finding 38).
  Acts 22 and 30 of 2016 and Act 15 of 2017 are deposited (the Gazette's Acts Supplements No. 19 of 2016, No. 2 of 2017 and No. 17 of 2017).
- The Telecommunication Authority of Singapore (Exemption in respect of Specified Equipment) Order (Cap. 323, O 3), made 11 November 1998, in operation 12 November 1998, kept in force by s 98(2) and listed in the 2010 Subject Index: now deposited (S 549/1998 and the 1999 Revised Edition) and encoded in `sgta-i-o3-1998.l4`, with the 1999 Dealers Regulations (Rg 7) and Radio-communication Regulations (Rg 3) it refers to.
  It exempts all persons "from section 30 (1) to (5) of the Act" (the Telecommunication Authority of Singapore Act) in respect of equipment approved for sale under reg 24(1) of Rg 7 or set out in its Fifth Schedule and meeting the published standards.
  The text of that section 30 is not held, so the module carries a fork: branch 1, it was the approval-before-use requirement (the extrinsic evidence of clause 6 of the Telecommunication Authority of Singapore (Amendment) Bill 1998 favours this; it was read by the independent reviewer and has not been re-read by this encoder), in which case the Order does not reach possessing or operating equipment; branch 2, it was the prohibition on possessing or operating equipment, in which case limb (a) would exempt every person in respect of equipment whose type was approved for sale.
  No deposited text shows that a receiver of the kind this question asks about was ever approved for sale under reg 24(1) or named in the Fifth Schedule (which names telephones, interfaces, modems and similar line equipment, and "other equipment as determined by the Authority").
  The seat does not consult O 3 and no answer in section 5 rests on it; the answers stand as written, with this as a named reservation that only the text of section 30 could remove.
- The 1999 Revised Editions of the Radio-communication Regulations (Rg 3) and the Dealers Regulations (Rg 7) are encoded (`sgta-i-rg3-1999.l4`, `sgta-i-rg7-1999.l4`) but not wired into the seat; the seat answers NOTHING for conduct from 1 Dec 1999 to 2 Mar 2001 (section 5, Date (1)).
  Rg 7 was amended by S 362/2001 from 1 Aug 2001 and revoked from 2 Apr 2003 by reg 26 of S 185/2003; an amendment of either Edition between 1 Jul 1999 and those days, other than the ones named, is unknown.
- The Code of Practice for Competition in the Provision of Telecommunication Services 2005 (S 87/2005), to which the designation notifications refer: not deposited (the Gazette's browse page showed no match under that number).
  (S 115/2001, N 1 as made, and the notifications S 86/2005, S 233/2005, S 390/2007, S 35/2012, S 192/2012 and S 521/2017 were deposited from the team lead's second list: `NOTES.md` finding 27.)
  (The commencement notification of Act 10 of 2005 and the published days of the instruments' amending notifications were requested and were read on 2026-11-04: `NOTES.md` findings 25 and 26.)
- The Singapore Statutes Online consolidation of every instrument; the texts read are IMDA's copies (an aid, with a few extraction defects that the e-Gazette's copies of 25 of them corrected: `NOTES.md` finding 23) and the e-Gazette's copies of the amendments named there; IMDA's listing and the Gazette's browse page may each be out of date.
  The IMDA file deposited as the Rg 6 "2004 Revised Edition" is not the Gazette's 2004 edition: reg 10(2) and (4) and the arrangement of regulations carry text from S 478/2005 (`TA1999-RG6.txt:223-232` against `TA1999-RG6-GAZ-RevEd2004.txt:311-333`); regs 22(1), the First and Second Schedules agree.
- The IMDA technical specifications ("IMDA TS SRD", "IMDA TS DVB-T2 IRD"): not obtained.
- Any Gazette notification not on IMDA's list, in particular other s 73 exemptions made by the Minister; and any Broadcasting Act notification under s 20(4) exempting a class of apparatus (none of the twelve deposited Broadcasting Act instruments other than the TVRO Regulations contains the words "apparatus", "section 20" or "receiver": the class-licence notifications of 1996 and 2020, the exemption orders of 1996, 2002, 2004, 2008, 2010 and 2022, the Third Schedule notification of 2010, the composition regulations of 2004, the online codes procedure rules and the service-of-documents notification of 2023; counted with `grep -c -i` on 2026-11-04).
- Whether the Authority publishes standards that a broadcast receiver meets (decides Reading Y of Rg 6 reg 22(1)).
- The Rg 1 editions before the Revised Edition 2004 (its title page names the 1990 Edition and its amendments S 21/80 to S 212/99, `BA1994-RG1.txt:11-27`), and so the fee schedule before 29 Feb 2004; any reported car-radio fee (the deposited First Schedule has one sound-receiver item, $27 for 12 months: section 10(d)).

## 9. How sure I am

- Date (1), conduct before 1 Jan 2011: about 60 per cent that "no offence under the Telecommunications Act" is right for a listed receiver, because it rests on Reading A of s 95 against Reading B.
- Date (2): about 65 per cent that the literal reading above is what the text said then, for the days the law is read from 31 Oct 2012; about 55 per cent for conduct from 1 Jan 2011 to 31 Jan 2012, where it also rests on Reading P of FORK 6.
  The risks are an exemption instrument I could not see, an Act after Act 15 of 2017 that the markers do not show, and the retrospective S 549/2012 (the Constitution question in section 5).
- Date (3): about 75 per cent that the literal reading above is right on the Act's words.
  The residual risk is a current instrument that neither IMDA's list nor the e-Gazette's browse page showed (the e-Gazette supplied one that IMDA's list lacked, S 78/2017, which does not touch a receiver).
- That any of this is also what a court would hold, or what the Authority enforces, is a different question that this file does not answer.

## 10. Are plain old FM and AM radios exempted from all this?

The short answer: no text in the 86 searched files exempts an FM or an AM broadcast receiver, and the Act's words catch each of them in the same way as the television on every pair of days; what exempts them, where anything does, is the Broadcasting Act's list, which treated a "broadcast sound receiver" as it treated a "broadcast television receiver" (and its licensing regulations Rg 1, which licensed both, with a sound receiver in a vehicle or vessel named in terms: sections 5 and 11).

### (a) Is an FM or AM receiver caught by s 54(1)(b) and s 55(1) as the television is?

| Reading of FORK 1 | Television | FM radio | AM radio |
| --- | --- | --- | --- |
| Reading 1 (equipment used for a telecommunication by Hertzian or radio waves) | caught | caught | caught |
| Reading 2 (two-way or point-to-point equipment only) | not caught | not caught | not caught |

Why the three are alike: each is an appliance used for the reception of sounds (the television also of images) by radio waves; "telecommunications" is "reception of ... images, sounds" "by wire, radio, optical or other electromagnetic systems" (`TA1999.txt:529-536`), and "Hertzian or radio waves" are "electromagnetic waves of frequencies not exceeding 1,000 terahertz propagated in space without any artificial guide" (`TA1999.txt:331-333`), which includes both the AM band (526.5 to 1606.5 kHz) and the FM band (87.5 or 88 to 108 MHz).
No text distinguishes the kinds by frequency, by kind of programme or by the presence of a picture.

### (b) Is there any instrument that names a sound-broadcast receiver or an AM or FM band?

The search is mechanical (`scratchpad/tools/fmam-search.py`, not committed; its output is `counts.tsv` and `contexts.txt` in the scratchpad), over 95 files (re-run on 2026-11-04 when the Broadcasting Act folder's deposits of Rg 1, S 333/2004 and S 548/2012 landed, and again when the third list's texts and Acts 22 and 30 of 2016, not searched before, were added): `TA1999.txt`, the Revised Edition 2000, Acts 10 of 2005, 19 of 2011, 22 of 2016, 30 of 2016 and 15 of 2017 and the printed 2020 Revised Edition; the 58 Telecommunications Act instrument texts (IMDA's 40, with the Gazette's copies of S 685/2011 and S 686/2011 in place of the OCR, and eighteen the e-Gazette supplied; S 114/2001's hits are the Revised Edition's Rg 5 again, with the reg 2 "station" and the reg 68(4) "general reception" words unchanged; S 525/2001's and S 115/2001's hits are the Schedule again, and the others have none of the terms read); the Broadcasting Act in its three deposited versions; and the 26 Broadcasting Act instrument texts, S 549/2012 among them.
The terms and the hits (total hits in files with a hit) are in `NOTES.md`; the ones that matter here:
- Zero hits for: "radio receiver", "medium wave", "AM" and "FM" in capitals, "amplitude modulation", "frequency modulation", "526", "1606", "87.5".
- "receiver": 206 hits in 21 files.
  Every one outside Rg 1 and S 333/2004 was read; in those two, which are about licensing receivers, the hits are the regulations' own subject (`BA1994-RG1.txt:141-148, 441-512`).
  The Act: s 14(2) "station" includes "a receiver"; "Official Receiver" and "receiver" as an insolvency office.
  The new hits of 2026-11-04 are outside the question: Act 30 of 2016's new s 11A(2), which defines "station" to include "a receiver" for the sharing of radio spectrum in s 11A(1) (`TA1999.ACT30-2016.txt:361-362`), and the insolvency receivers of Act 15 of 2017.
  Instruments: Rg 5 reg 2 (as made too, `TA1999-RG5-S114-2001.txt:302-303`) and Rg 1 "station" includes a receiver; Rg 6 Third Schedule item 1 "Scanning Receivers" (prohibited equipment for a dealer, `TA1999-RG6.txt:520`, undefined); Rg 6 Fifth Schedule item 3 "Integrated receiver decoder" (S 251/2013); N 1 item 11(e) "TV Receivers/ Radio Systems", item 14 "Stand-alone GPS Receivers", item 15 "Communication Receivers (excluding Scanning devices) and ... (MMDS) Receivers" at 2.5 GHz.
  The Broadcasting Act: First Schedule items 1 and 2 and their definitions; Rg 1 (licences for a "broadcast sound receiver" and a "broadcast television receiver"), S 333/2004 (amending them), S 548/2012 (revoking them) and the TVRO Regulations.
- "sound": 74 hits in 11 files: the definition of "message" and of "telecommunications" (`TA1999.txt:344, 530, 533`), the Broadcasting Act's definition of a broadcasting service, item 2 of its First Schedule, Rg 1 Part IV ("Broadcast sound receivers") and its amendments, S 548/2012, and a class licence notification's matter transmitted as sound (S 477/2020).
- "kHz": 59 hits in 9 files, all read (the twelve new ones are S 114/2001's fee bandwidths, the Revised Edition's again): the only instrument entries that overlap the AM band are 0.51 to 1.60 MHz ("510-1,600 kHz") for wireless microphones in N 1 item 3 (`TA1999-N1.txt:48`) and for short range devices in item 1 of the Rg 6 Fifth Schedule (for example `TA1999-RG6-S251-2013.txt:91`); the others are Rg 5 fee bandwidths and other bands (9 to 315 kHz, 1,605 to 1,800 kHz cordless telephones).
- "88" and "108": 88.00 to 108.00 MHz at N 1 item 3 (60 dBµV/m @ 10m; `TA1999-N1.txt:50`; the same entry in S 115/2001 as made, "60 dB @ 10m", `TA1999-N1-S115-2001.txt:67`, and in S 525/2001, S 1/2008 and S 726/2014) and at Rg 6 Fifth Schedule item 1 (for example `TA1999-RG6-S251-2013.txt:111`) in S 178/2011, S 210/2010, S 251/2013, S 414/2014 and S 725/2014: ten entries in ten files (the term "108" has five more hits: page numbers in the Act's two deposits and in Act 15 of 2017, and "Cap. 108", the Finance Companies Act, in Act 15 of 2017); they are field-strength limits.
- "television": 169 hits in 16 files; in the Telecommunications Act instruments the only hits are N 1's "TV Receivers" and Rg 6 S 251/2013 item 3; the rest are the Broadcasting Act's and its instruments' (Rg 1 Part V and its amendments, S 548/2012, the class licence and exemption notifications' television services).
- "general reception": 3 hits, Rg 5 reg 68 (as made too: `TA1999-RG5-S114-2001.txt:1392`) and Rg 6 reg 13 on secrecy (`TA1999-RG5.txt:1149`, `TA1999-RG6.txt:273`).
- "vehicle": 89 hits in 22 files, all read (see (d); the four of 2026-11-04 are the definition of "premises" in Act 22 of 2016, the Motor Vehicles (Third-Party Risks and Compensation) Act in a list in Act 15 of 2017, and two lists of places in S 114/2001 (`:1347`, `:1416`)); the new hits are Rg 1 regs 5, 10, 23 and 28 and S 333/2004, and a taxi or private hire car in S 477/2020.

Result: no Telecommunications Act instrument names an AM or FM broadcast receiver or reception band; the Broadcasting Act's Rg 1 names a "broadcast sound receiver" (not a band) as the thing its Part IV licenses.
The only entries in the AM and FM bands are limits for transmitters.

### (c) H4 re-tested

The claim "the 88 to 108 MHz items are transmitters and nothing exempts possession of a receiver" was checked again against the text.
N 1 para 2(b) exempts "the localised on-site installation or operation of the equipment specified in the Schedule".
The equipment of item 3 is "Wireless Microphones"; the 88.00 to 108.00 MHz line gives its authorised band and "60 dBµV/m @ 10m".
A wireless microphone transmits; an FM broadcast radio is not a wireless microphone.
The Rg 6 Fifth Schedule (equipment on which fees are not charged, item 1 "Short Range/Low Power Devices") lists the same band, again as a limit on a device's emission.
So nothing covers FM possession.
Nothing covers AM either: the 510 to 1,600 kHz entries are in the same two places and have the same character; no instrument has a line for the AM broadcast band as such.
The FM argument and the AM argument are therefore the same argument and both fail.

On Reading Y of FORK 5, item 11(e) "TV Receivers/ Radio Systems" would name the receivers, but item 11's bands are 26.96 to 27.28 MHz and 40.66 to 40.70 MHz (and the additional bands above from 2008), none of which is an AM or an FM broadcast band; so on Y the exemption does not reach a person tuning to an FM or AM broadcast either.

### (d) Vehicle radios

- s 55(1) says "in any place or on board any vessel, aircraft or in any vehicle in Singapore" (`TA1999.20001230.txt:1256-1261`; `TA1999.txt:4911-4916`): it covers operating radio-communication equipment in a vehicle on the same terms as in a place; it does not distinguish a receiver in a vehicle from one in a house.
- s 54(1)(b) does not mention places or vehicles.
- No instrument treats a receiver in a vehicle differently: the only "car" hits are "Car Theft Alarm Systems" (N 1 item 7(a)) and "Battery-operated Cars and Boats" (N 1 item 11(d)), and the "vehicle" hits in the instruments are inspection powers, vehicles as places that may be entered, and short range radar in a vehicle (N 1 item 16 and Rg 6 Fifth Schedule).
- On the Broadcasting Act side, s 20(1)(a) separately forbids installing broadcasting apparatus "on board any ship, aircraft or vehicle registered in Singapore" without a licence (`BA1994.20030731.txt:702-703`).
  A sound receiver was broadcasting apparatus while listed, so installing a car radio in a Singapore-registered vehicle was within it for those days.
- The licensing regulations then deposited by the Broadcasting Act folder speak to a car radio directly.
  Rg 1, Revised Edition 2004 (29 Feb 2004), reg 23(1): a licence "shall be required for every broadcast sound receiver installed in a vehicle or in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act" (`BA1994-RG1.txt:441-444`); reg 5(3): a licence for a sound receiver installed in a vehicle "shall, as from the date of its issue, be valid for such period as the licensing authority may determine" (`:220-223`).
  From 21 Jun 2004 S 333/2004 cl 11(a) deletes reg 23(1) and (2) and substitutes two paragraphs, of which (2) names a vessel only: "A licence shall be required for every broadcast sound receiver in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act" (`BA1994-S333-2004.txt:123-133`).
  A television in a vehicle or vessel has its own requirement in both versions, reg 28(2): "A separate licence shall be required for every broadcast television receiver installed in a vehicle or in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act" (`BA1994-RG1.txt:501-504`; S 333/2004 cl 13 amends only reg 28(1) and (5)).
  Until 20 Jun 2004 reg 27(1) also forbade operating a television anywhere without a licence; from 21 Jun 2004 it does not (section 12).
- The fee: the only sound-receiver fee in the deposited regulations is item 2 of the First Schedule, "Licence for a broadcast sound receiver", $27 for 12 months, with no separate item for a vehicle (`BA1994-RG1.txt:629`).
  I cannot match any reported car-radio figure to a text; S 548/2012 ends the regulations, and with them every such fee, for periods from 1 Jan 2011 (section 5, Date (1)).

### (e) The Broadcasting Act side

- "Broadcast sound receiver" is item 2 of the First Schedule in the Revised Edition 2003 (31 Jul 2003) and in the Revised Edition 2012 (31 Aug 2012), defined as "any apparatus used for the aural reception of any broadcasting service" (`BA1994.20030731.txt:2141, 2146-2147`; `BA1994.20120831.txt:2168, 2171-2172`).
- S 549/2012 deletes it, with the television receiver, from 1 Jan 2011 (deemed), as published on 31 Oct 2012.
- Of the 26 Broadcasting Act instrument texts now deposited (counted 2026-11-04 by `grep -c -i -e apparatus -e "section 20" -e receiver` over each file), five contain those words: Rg 1 (138 lines), S 333/2004 (29), the TVRO Regulations (`BA1994-RG3.txt`, 8, TVRO system only), S 548/2012 (7) and S 549/2012 (2).
  The other 21 contain none, among them every exemption order (the Exemption Orders of 1996, 2002, 2004, 2008, 2010, 2014 and 2022) and every class licence notification: so no exemption under s 20(4) of the Act for a receiver is among the deposited texts.
- Rg 1 is the instrument that licensed a "broadcast sound receiver" (Part IV, regs 23 to 26) and a "broadcast television receiver" (Part V); see section 5, Date (1), and section 10(d) for a vehicle.

### The three kinds at the three dates, in pairs of days

| Conduct | Read on | Television | FM radio | AM radio | Satellite dish system |
| --- | --- | --- | --- | --- | --- |
| 31 Dec 2010 | 31 Dec 2010 and 4 Nov 2026 | no offence (A) | no offence (A) | no offence (A) | no offence |
| 1 Jan 2011 | 1 Aug 2012 | no offence (A) | no offence (A) | no offence (A) | no offence |
| 1 Jan 2011 | 31 Oct 2012 | offence s 54(2), s 55(1) | offence | offence | no offence |
| 1 Jan 2011 | 4 Nov 2026 | offence | offence | offence | no offence |
| 15 Jun 2015 | 15 Jun 2015 | offence | offence | offence | no offence |
| 4 Nov 2026 | 4 Nov 2026 | offence | offence | offence | no offence |

"(A)" means Reading A of s 95; on Reading B each "no offence (A)" is an offence.
The seat takes the kind of receiver as an input (television, FM radio, AM radio, satellite dish system) and the Broadcasting Act's list is a function of the kind and the two days; `sgta-tv-cases.l4` has each cell.

## 11. What S 548/2012 and Rg 1 change in this file (added 2026-11-04, after the Broadcasting Act folder deposited them)

Changed (each now cites an instrument, not only Hansard or a search-engine summary):
1. Section 5, Date (1): "what the texts do not show" no longer includes "any regulation that fixed the receiver licence fee": Rg 1's First Schedule fixes it.
   The bullet "whether the licence was priced for sets after 1 January 2011" is answered for the law as read from 31 Oct 2012 (S 548/2012: Rg 1 revoked from 1 Jan 2011, advance fees refunded) and stays open for practice between 1 Jan 2011 and 30 Oct 2012.
2. H1: supported by S 548/2012 and Rg 1 as well as by S 549/2012; the EXTRINSIC Hansard line is now corroborating.
3. H2: the "nothing was put in its place" absence is now checked against 26 Broadcasting Act instrument texts, not the 12 I had.
4. Section 10(d): the car-radio question is partly answered: a vehicle sound receiver had its own regulation (reg 23(1)) until 20 Jun 2004, a vessel only after; a television in a vehicle or vessel has reg 28(2); the only sound-receiver fee in the deposited Rg 1 is $27 for 12 months.
5. Section 10(e): the "twelve instruments, all zero" count is replaced by the 26-text count; the exemption orders still contain nothing about a receiver.
6. Section 8: the fee-schedule gap is narrowed to Rg 1 editions before 29 Feb 2004.
7. The seat has a second Broadcasting Act input, `Were the receiver licensing regulations in operation` (S 548/2012 and Rg 1, both effective 1 Jan 2011 and published 31 Oct 2012), beside `Does the First Schedule list this kind of receiver` (S 549/2012).
   It treated Rg 1 as one unit from 29 Feb 2004; that was wrong as an account of what the regulations said and is corrected in section 12, which adds a third export, `What did the receiver licensing regulations say about a licence for this receiver`.

NOT changed:
- Every Telecommunications Act answer in sections 1 and 5 (offence under s 54(2) and s 55(1), the maximum of s 85, and the "no offence on Reading A" rows).
  The two Broadcasting Act inputs agree on every pair of days where both are known, for a television, an FM radio and an AM radio (32 assertions in `sgta-tv-cases.l4`), so adding the second moves no answer; it is deliberately not a conjunct of the first, because Rg 1 is not deposited before 29 Feb 2004 and a conjunct would turn the days 31 Jul 2003 to 28 Feb 2004 into NOTHING.
- The reading of s 95 (Reading A) rests on the First Schedule (the definition of "broadcasting apparatus" in s 2 of the Broadcasting Act is "specified in the First Schedule", `BA1994.20120831.txt:191-193`); S 548/2012 revokes the regulations that licensed it and does not itself delete an entry from the list.

New open point, not answered here: Rg 1 names a sound receiver in terms only for a vehicle or vessel (reg 23), while its First Schedule prices "a broadcast sound receiver" at $27 and reg 27(3) lets a television licence cover the household's sound receivers.
Whether a household radio needed its own licence by force of s 20(1)(c) is a Broadcasting Act question for the Broadcasting Act folder.

## 12. Correction of 2026-11-04 (team lead): what S 333/2004 did to Rg 1

What was wrong, in my account, before this section:
- Section 5 and H1 quoted reg 27(1) of the Revised Edition 2004 ("No person shall operate a broadcast television receiver without a licence") as the regulations' words without saying that they stood only from 29 Feb 2004 to 20 Jun 2004.
  I had listed S 333/2004's replacement of reg 27(1) and (2) as "a paragraph on where to apply" but did not draw the consequence: the substituted paragraph states no prohibition.
- `sgta-tv-ba-schedule.l4` had two rows for Rg 1 (the Revised Edition 2004 and the revocation) and said that S 333/2004 "changes what Rg 1 says, not whether it is in operation, so it is not a row here"; the seat's `Were the receiver licensing regulations in operation` therefore treated Rg 1 as one unit from 29 Feb 2004 to 31 Dec 2010.
  That answer is still true as an answer about operation, but it said nothing about what the regulations required, and the 32 assertions comparing it with the First Schedule compared operation only.
- My description of S 333/2004 in section 11 and 10(d) named reg 23 and reg 28(2) and left out the larger change (the clauses are listed in section 5, above).

Corrected by reading the Broadcasting Act folder's deposits (`BA1994-S333-2004.txt`, PDF sha256 68bf17f881f90e33..., the same file the team lead checked; `BA1994-RG1.txt`; `BA1994-S548-2012.txt`) and quoting only from them; every quoted fragment in the new function is checked against those files by script (`scratchpad/tools/verify-quotes-rg1.py`: 22 fragments, none missing).

What each version of Rg 1 said in terms about a licence (the function `what Rg 1 in the version says in terms about a licence for the kind of receiver in the place`, in `sgta-tv-ba-schedule.l4`; the Broadcasting Act's own s 20(1) is not a regulation and is not in this table):

| | Revised Edition 2004 (conduct from 29 Feb 2004) | as amended by S 333/2004 (conduct from 21 Jun 2004; published 15 Jun 2004) | revoked by S 548/2012 (conduct from 1 Jan 2011; published 31 Oct 2012) |
| --- | --- | --- | --- |
| television, house or flat | reg 27(1): no person shall operate a broadcast television receiver without a licence | no regulation says so in terms: reg 27(1) says only where to apply; reg 27(3) and, for a lodger or tenant, reg 27(4) remain; reg 7 speaks of s 20(1) of the Act | Rg 1 revoked; reg 2(2) keeps it for licences granted for periods before 1 Jan 2011 |
| television, vehicle or vessel without a ship station licence | reg 27(1), and reg 28(2): a separate licence for every television installed there | reg 28(2) (unamended) | revoked |
| television, commercial property | reg 27(1) | reg 29A(1): a separate licence for every television installed in a commercial property | revoked |
| radio (FM or AM), house or flat | no regulation says so in terms; reg 27(3) lets a television licence cover the household's sound receivers; First Schedule item 2 prices "a broadcast sound receiver" at $27 for 12 months | the same | revoked |
| radio, vehicle | reg 23(1): a licence for every sound receiver installed in a vehicle or vessel without a ship station licence | no regulation says so in terms: reg 23(1) is deleted and (2) names a vessel only | revoked |
| radio, vessel without a ship station licence | reg 23(1) | reg 23(2) | revoked |
| radio, commercial property | no regulation says so in terms | no regulation says so in terms; reg 29A(2) says a licence under reg 29A(1) permits the use of one or more sound receivers | revoked |
| satellite dish system | outside "broadcast television receiver" (reg 2(1)) | the definition and the exclusion are deleted; the text does not say in terms whether a dish is within it | revoked |

Both axes: a reader before 15 Jun 2004 does not have S 333/2004 even for conduct after 20 Jun 2004; a reader from 31 Oct 2012 has the revocation for conduct from 1 Jan 2011 and the amended text for conduct before it (46 assertions in `sgta-tv-cases.l4`).
New seat export: `What did the receiver licensing regulations say about a licence for this receiver` (conduct day, reading day, kind of receiver, place of the receiver); the export `Were the receiver licensing regulations in operation` now says in its own description that it is about existence, not content.

What does not change: every Telecommunications Act answer in sections 1 and 5 (they rest on Reading A of s 95 and the First Schedule's list, not on Rg 1: Rg 1 is not a conjunct), and the 32 operation assertions.
What the correction does to the Broadcasting Act side, as the texts show it: for a household television from 21 Jun 2004 the regulations no longer state the prohibition, and the deposited text that does is section 20(1)(c) of the Act ("operate or have on any premises in Singapore owned or occupied by him broadcasting apparatus on or by which broadcasting services are received ... except under and in accordance with a licence granted under this section", `BA1994.20030731.txt:701-710`) read with the First Schedule's list.
I draw no conclusion from that about whether, or how, the s 20(1) licence was enforced or priced for a household set, and the Telecommunications Act answers do not turn on it.

