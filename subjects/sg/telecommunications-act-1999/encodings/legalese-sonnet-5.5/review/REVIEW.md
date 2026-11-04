# Independent review: receivers under the Telecommunications Act 1999 and the Broadcasting Act 1994

Status: section 1 written 2026-11-04 from the deposited source texts only, before any `NOTES.md`, `encoding.json` or `.l4` file under either encoding was opened.
Its line citations were re-read against the sources by hand once, immediately after writing, and five line ranges were corrected then; nothing else in it has been changed since.
Section 1 is not edited after it was written; later sections may disagree with it, and say so where they do.
Quotations keep the words of the deposited `.txt` files; line-end hyphenation is rejoined, the glyphs ‘‘ ’’ are written as quotation marks, and "…" marks an omission.
Every `file:line` is relative to the review copy's root (`subjects/sg/…`), through the aliases in §1.0.

## 0. Independence

This section and sections 2 to 7 were written on 2026-11-04, after section 1, and are not part of it.
- **What leaked.**
  At 2026-11-03T19:53:49Z, when my context was compacted, the harness attached four files to it.
  I had read one of them before, `REVIEWER-BRIEF.md`, my own brief, once.
  The other three I had not opened: the script that built this review copy, a project memory file kept outside VIEW, and the `WALKTHROUGH.md` of a quarantined row (named as read, its contents not included).
  The memory file states both encoders' preliminary answers at each date (before 2011, 2011 read before and after 31 October 2012, and today), for television and radio, with their forks and their check numbers.
  I reported it and stopped (`REQUESTS.md` R2, with a correction about the brief); the lead decided that I carry on with this disclosure.
- **Written before it.**
  Section 1 was last written at 2026-11-03T19:39:36Z.
  At that time the whole file's sha256 was `c40ec1bbd731cae1fd6f5bdc743d4ff5659c4467fb395184b9b79f0e480dd4bf`.
  The sha256 of section 1 is `dd6325a0943dd1744ecb76027edca414c6e32b2884d876fd5ad8d5a9b8d36176`, both then and now: section 1 is the text from "## 1." to the blank line before "## 2.", that blank line not included.
  To check it: `awk '/^## 1\. /{f=1} /^## 2\. /{f=0} f' REVIEW.md | sed '$d' | shasum -a 256`.
  `MISSED-INSTRUMENTS.md` parts A to E (E's first table) were last written at 19:50:58Z.
- **Written after it.**
  Everything else is post-leak and not blind:
  - `CITATION-CHECK.md`;
  - `MISSED-INSTRUMENTS.md` parts E2 and E3;
  - sections 0 and 2 to 7 of this file;
  - `DISAGREEMENTS.md`.
  Steps 4 and 6 were done after the leak.
- **What agreement can show.**
  On the points the leaked file states, my blind section 1 already gives the same answers.
  So the agreement is evidence of independence for section 1 only; nothing in sections 2 to 7 should be counted as a further independent confirmation of it.
  Where I think I may have been anchored, the item says so.

## 1. My answer, re-derived from the deposited texts

### 1.0 Files cited

| alias | path |
| --- | --- |
| BA2003 | `subjects/sg/broadcasting-act-1994/registers/source-bundle/BA1994.20030731.txt` (Revised Edition 31 July 2003) |
| BA2012 | `subjects/sg/broadcasting-act-1994/registers/source-bundle/BA1994.20120831.txt` (Revised Edition 31 August 2012) |
| BA2026 | `subjects/sg/broadcasting-act-1994/registers/source-bundle/BA1994.txt` (current; banner "version in force from 25/9/2024") |
| S549 | `subjects/sg/broadcasting-amendment-of-first-schedule-notification-2012/registers/source-bundle/BA1994-S549-2012.txt` |
| S548 | `subjects/sg/broadcasting-television-and-radio-licensing-revocation-regulations-2012/registers/source-bundle/BA1994-S548-2012.txt` |
| RG1 | `subjects/sg/broadcasting-television-and-radio-licensing-regulations/registers/source-bundle/BA1994-RG1.txt` (Rg 1, Revised Edition 29.2.2004) |
| S333 | `subjects/sg/broadcasting-television-and-radio-licensing-amendment-regulations-2004/registers/source-bundle/BA1994-S333-2004.txt` |
| TVRO | `subjects/sg/broadcasting-tvro-system-regulations-1991/registers/source-bundle/BA1994-RG3.txt` (lawplain-served 2004 RevEd) |
| BARG2 | `subjects/sg/broadcasting-composition-of-offences-regulations-2004/registers/source-bundle/BA1994-RG2.txt` |
| TA2000 | `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.20001230.txt` (Revised Edition 30 December 2000) |
| TA2026 | `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.txt` (2020 RevEd, banner "version in force from 2/10/2026") |
| A10-05 | `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.ACT10-2005.txt` (OCR) |
| S76-05 | `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.S76-2005.txt` |
| A19-11 | `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.ACT19-2011.txt` |
| S33-12 | `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.S33-2012.txt` |
| B20-11 | `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.BILL20-2011.txt` (extrinsic) |
| RG5 | `subjects/sg/telecommunications-radio-communication-regulations-2001/registers/source-bundle/TA1999-RG5.txt` (Rg 5, 2002 RevEd) |
| S461-09 | `subjects/sg/telecommunications-radio-communication-regulations-2001/registers/source-bundle/TA1999-RG5-S461-2009.txt` |
| N1 | `subjects/sg/telecommunications-exemption-notification-2001/registers/source-bundle/TA1999-N1.txt` (N 1, 2002 RevEd) |
| S726-14 | `subjects/sg/telecommunications-exemption-notification-2001/registers/source-bundle/TA1999-N1-S726-2014.txt` |
| RG6 | `subjects/sg/telecommunications-dealers-regulations-2003/registers/source-bundle/TA1999-RG6.txt` (Rg 6, 2004 RevEd) |
| S478-05 | `subjects/sg/telecommunications-dealers-regulations-2003/registers/source-bundle/TA1999-RG6-S478-2005.txt` |
| S210-10 | `subjects/sg/telecommunications-dealers-regulations-2003/registers/source-bundle/TA1999-RG6-S210-2010.txt` |
| S251-13 | `subjects/sg/telecommunications-dealers-regulations-2003/registers/source-bundle/TA1999-RG6-S251-2013.txt` |
| COMP05 | `subjects/sg/telecommunications-composition-of-offences-regulations-2005/registers/source-bundle/TA1999-COMP-S706-2005.txt` |
| IA | `subjects/sg/interpretation-act/registers/source-bundle/IA1965.txt` (current text, banner "version in force from 5/12/2025") |

### 1.1 The instruments, what each says on this question, and when it began and ended

| instrument | what it says that matters | began | ended |
| --- | --- | --- | --- |
| BA s 2(1) "broadcasting apparatus" | "any apparatus capable of or designed or constructed for the reception of any broadcasting service and specified in the First Schedule" (BA2003:198-200; BA2012:191-193; BA2026:277-279) | before 2003 (earliest deposited edition is 2003) | in force today, unchanged |
| BA First Schedule, three items | "1. Broadcast television receiver." "2. Broadcast sound receiver." "3. Television receive-only satellite receiving system (TVRO system)." (BA2003:2139-2143; BA2012:2167-2169) | before 2003 | replaced by S 549/2012, deemed from 1 January 2011 |
| BA First Schedule, one item (S 549/2012) | "1. Television receive-only satellite receiving system (TVRO system)." (S549:31; BA2026:4347) | deemed 1 January 2011 (S549:20-22); made 30 October 2012 (S549:37); first published 31 October 2012 (S549:3) | in force today |
| BA s 20(1) | no person shall "(a) install any broadcasting apparatus in any place, or on board any ship, aircraft or vehicle registered in Singapore; … (c) operate or have on any premises in Singapore owned or occupied by him broadcasting apparatus on or by which broadcasting services are received, except under and in accordance with a licence granted under this section" (BA2003:702-710) | before 2003 | in force today (BA2026:1427-1439) |
| BA s 47 | contravention of s 20(1)(a), (b) or (c): "a fine not exceeding $40,000 or to imprisonment for a term not exceeding 3 years or to both, and any broadcasting apparatus installed or found in the possession of the person so convicted shall be forfeited to the Authority" (BA2003:1736-1741) | before 2003 | in force today (BA2026:3676-3681) |
| Rg 1 (Television and Radio Licensing Regulations) | the licensing machinery for broadcast sound and television receivers: fees (RG1:627-633), household scope (RG1:485-488), vehicle and vessel receivers (RG1:441-457, 501-504) | 1 February 1980 (RG1:129) | revoked by S 548/2012, deemed from 1 January 2011 (S548:29-36) |
| S 333/2004 (amends Rg 1) | deletes reg 27(1) "No person shall operate a broadcast television receiver without a licence" (RG1:481-482) and substitutes an application provision (S333:138-144); narrows reg 23 to vessels (S333:124-133); defines "licence" as "any licence granted under section 20 of the Act in respect of any broadcasting apparatus" (S333:51-52) | 21 June 2004 (S333:21-23) | with Rg 1, deemed 1 January 2011 |
| S 548/2012 | "The Broadcasting (Television and Radio Licensing) Regulations (Rg 1) … are revoked" (S548:34-36), saves them for licences "for any period before 1st January 2011" (S548:37-53), refunds fees paid for periods from 1 January 2011 (S548:54-57) | deemed 1 January 2011 (S548:29-31); made 30 October 2012 (S548:59); published 31 October 2012 (S548:3) | n/a |
| TVRO Regulations (Rg 3) | "No person other than an institution may be granted with a licence." (TVRO:16) | 22 March 1991 (TVRO:1) | not shown: the deposited text is the 2004 RevEd served by lawplain, and its meta file says whether it was later amended or revoked "is NOT shown" |
| TA s 2 "equipment", old wording | "includes any appliance, apparatus or accessory used or intended to be used for telecommunication purposes" (TA2000:226-227) | 1 December 1999 | 31 January 2012 |
| TA s 2 "equipment", new wording | "includes any appliance, apparatus or accessory used or intended to be used for telecommunications, including (to avoid doubt) any such appliance, apparatus or accessory capable of being used for the operation of any broadcasting service" (TA2026:325-329), inserted by Act 19 of 2011 s 2(b) (A19-11:49-55) | 1 February 2012 (S33-12:23-24) | in force today |
| TA s 2 "telecommunications", "radio-communication" | "a transmission, emission or reception of signs, signals, writing, images, sounds or intelligence of any nature by wire, radio, optical or other electro-magnetic systems" (TA2000:299-306; TA2026:529-536); "radio-communication" "means any telecommunication by means of Hertzian or radio waves" (TA2000:249-250; TA2026:450-451) | 1 December 1999 | in force today |
| TA s 34(1)(b) / s 54(1)(b) | no person shall "possess any radio-communication equipment, except and in accordance with a licence granted under section 5 or any regulations made under this Act" (TA2000:1246-1251; TA2026:4894-4902) | 1 December 1999 | in force today, renumbered s 54 in the 2020 RevEd |
| TA s 35 / s 55 | operating radio-communication equipment "in any place or on board any vessel, aircraft or in any vehicle in Singapore without a licence" (TA2000:1256-1261); possession deemed operation (TA2000:1262-1264); occupier offence (TA2000:1270-1272) | 1 December 1999 | in force today (TA2026:4911-4929) |
| TA s 65 / s 85 general penalty | "a fine not exceeding $10,000 or to imprisonment for a term not exceeding 3 years or to both" "in addition to the forfeiture of any article seized" (TA2000:1916-1920); a continuing-offence fine of "$1,000 for every day or part thereof" added by Act 10 of 2005 s 28 (A10-05:961-964) | 1 December 1999; continuing fine from 16 February 2005 (S76-05:23-24) | in force today (TA2026:5941-5948) |
| TA s 72 / s 95 excluded matters | "This Act shall not apply to the licensing of any broadcasting service or any broadcasting apparatus under the [Broadcasting Act] except in respect of the regulation of any telecommunication system required for the operation of any broadcasting service or the approval of any broadcasting apparatus used in accordance with section 9." (TA2000:2030-2035; name of Act changed by A10-05:1188-1190; TA2026:6987-6992) | 1 December 1999 | in force today |
| Rg 5 reg 19 and "station" | "A station or network may be possessed, established, installed, maintained, provided or operated if authorised by — (a) a station (spectrum) licence or network (spectrum) licence; (b) a station licence or network licence; or (c) a class licence." (RG5:555-558); "station" "means a transmitter, a receiver, a combination of transmitters and receivers or any accessory thereto which is used or intended to be used for radio-communication" (RG5:273-275) | 2 March 2001 | deposited to S 100/2016; later text not deposited |
| Rg 5 reg 65 class licence | only for a "relevant radio-communication station", one "connected with any of the following telecommunication systems licensed under section 5 of the Act: (a) a public cellular mobile telephone system; (b) a public radio paging system; (c) a public mobile data system; (d) a public trunked radio system; (e) a public satellite mobile telephone or data system" (RG5:1094-1106) | 2 March 2001; (f) public wireless broadband added 1 June 2006; femtocell station class licence added 2 October 2009 (S461-09:69-99) | deposited to S 100/2016 |
| N 1 Exemption Notification | exempts from ss 33, 34(1)(b) and 35 "(b) the localised on-site installation or operation of the equipment specified in the Schedule" (N1:24-31); the Schedule lists transmitters and three receivers: "Stand-alone GPS Receivers" (N1:140-141), "Communication Receivers (excluding Scanning devices) and Microwave Multipoint Distribution Systems (MMDS) Receivers" (N1:144-149) | 2 March 2001 (N1:17) | Schedule replaced 1 November 2014 (S726-14:18-20, 45-48); the new First Schedule keeps GPS receivers (S726-14:186-187) and has no MMDS or broadcast-receiver item (S726-14:55-187) |
| Dealers Regulations reg 22 (as substituted) | "Any person intending to use any telecommunication equipment for personal purposes shall not be required to obtain the approval of the Authority provided that such equipment is designed, constructed, installed, established, maintained and operated in accordance with such standards and specifications as may be published by the Authority." (S478-05:144-149) | 21 July 2005 (S478-05:14-15) | deposited to S 725/2014 |
| Dealers Fifth Schedule item 3 | "Integrated receiver decoder devices intended for use with second generation digital terrestrial television broadcasting system", in the Schedule of "EQUIPMENT IN RESPECT OF WHICH REGISTRATION AND RENEWAL OF REGISTRATION FEES DO NOT APPLY" (S251-13:161-168; S210-10:216-222) | 25 April 2013 (S251-13:18-20) | deposited to S 725/2014 |

### 1.2 The Broadcasting Act chain

An analogue terrestrial television set is, on the plain words, a "broadcast television receiver": "any apparatus used for the visual and aural reception in monochrome or colour of any broadcasting service" (BA2003:2148-2149; BA2012:2173-2174).
A "broadcasting service" includes signals comprising "any programme capable of being received, or received and displayed, as visual images" or "any sound programme for reception" "irrespective of the means of delivery of that service" (BA2003:209-220).
An FM or AM radio is a "broadcast sound receiver": "any apparatus used for the aural reception of any broadcasting service" (BA2003:2146-2147; BA2012:2171-2172).
The Act draws no line between bands, so FM and AM stand or fall together under it.
Each was "broadcasting apparatus" while it stood in the First Schedule, because the s 2(1) definition requires both reception capacity "and specified in the First Schedule" (BA2003:198-200).
I read "specified in the First Schedule" as qualifying the whole definition: "capable of or designed or constructed for" is one compound modifier of "the reception of any broadcasting service", so the only noun the trailing "and specified" can attach to is "apparatus".
The rival reading (the qualifier attaches only to "designed or constructed for …") leaves "capable of" without an object and would make S 549/2012's deletion of items 1 and 2 ineffective; I hold the plain reading with high confidence.
So TV and sound receivers were "broadcasting apparatus" until the First Schedule was replaced, and are not afterwards; a TVRO system is "broadcasting apparatus" throughout (BA2003:2143; S549:31; BA2026:4347).

Section 20(1)(c) catches an individual who "operate[s] or ha[s] on any premises in Singapore owned or occupied by him broadcasting apparatus on or by which broadcasting services are received", without a licence (BA2003:706-710).
Section 20(1)(a) catches installing broadcasting apparatus "on board any ship, aircraft or vehicle registered in Singapore" (BA2003:702-703).
Section 47 makes either an offence, "liable on conviction to a fine not exceeding $40,000 or to imprisonment for a term not exceeding 3 years or to both", with forfeiture of "any broadcasting apparatus installed or found in the possession of the person so convicted" (BA2003:1736-1741; BA2012:1719-1724).
The offence is compoundable: "The offence under section 47 of the Act may be compounded by the Authority" (BARG2:5), from 21 June 2004 (BARG2:1), for "a sum not exceeding $1,000" (BA2012:1981-1985).
The Act's own exceptions are uniformed members on duty (s 20(3), BA2003:714-718) and an exemption the Authority may grant: "The Authority may exempt any person or broadcasting apparatus or class of broadcasting apparatus from subsection (1)." (BA2003:719-720).
I found no deposited instrument made under s 20(4) for receivers.

Rg 1 supplies the licence machinery, and it matters for "no licence of their own".
A television licence "shall permit the use of one or more broadcast television receivers and one or more broadcast sound receivers by the licensee, members of his family and domestic servants resident at the address specified therein" (RG1:485-488), and that paragraph survives S 333/2004, which replaced only paragraphs (1) and (2) of reg 27 (S333:138-146).
So a household member who uses a licensed household set does not need a licence of their own; a lodger or separate tenant does (RG1:489-493).
Rg 1 also says "A licence shall not be required for the temporary use of a broadcast television receiver in a public place or at an official or social function" (RG1:521-523), and the same for sound receivers (RG1:460-462).
From 21 June 2004 the express rule "No person shall operate a broadcast television receiver without a licence" (RG1:481-482) is gone (S333:138-144), so the obligation for 2004-2010 rests on BA s 20(1) itself, with "licence" now meaning "any licence granted under section 20 of the Act in respect of any broadcasting apparatus" (S333:51-52).

### 1.3 The Telecommunications Act chain

"telecommunications" includes the "reception of signs, signals, writing, images, sounds or intelligence of any nature by wire, radio, optical or other electro-magnetic systems" (TA2000:299-306), and "radio-communication" "means any telecommunication by means of Hertzian or radio waves" (TA2000:249-250).
An aerial-fed television or radio receives images and sounds by radio waves, so its use is "radio-communication" on the definitions.
"equipment" "includes any appliance, apparatus or accessory used or intended to be used for telecommunication purposes" (TA2000:226-227) until 31 January 2012, and "for telecommunications, including (to avoid doubt) … broadcasting service" (TA2026:325-329) from 1 February 2012 (S33-12:23-24).
Reception is within "telecommunications" under both wordings, so I do not think the change of wording on 1 February 2012 decides anything for a receiver; the Bill's explanatory statement (extrinsic) calls the change one "to clarify that the term includes" broadcasting-capable apparatus (B20-11:2571-2574).
The Act excludes broadcasting from "telecommunication service" ("but excludes any broadcasting service", TA2000:293-294) but not from "telecommunications" or "equipment", which I take as a deliberate contrast.
So I read an analogue TV set or radio receiver as "radio-communication equipment" for s 34(1)(b) and s 35, on the literal text.

Section 34(1)(b) forbids possessing "any radio-communication equipment, except and in accordance with a licence granted under section 5 or any regulations made under this Act" (TA2000:1249-1251); s 34(2) makes contravention an offence (TA2000:1252-1253).
Section 35(1) makes it an offence to operate radio-communication equipment "in any place or on board any vessel, aircraft or in any vehicle in Singapore without a licence" (TA2000:1256-1261); possession is "deemed, until the contrary is proved, to have operated the same" (TA2000:1262-1264); and "The occupier of any dwelling-house or premises in which is installed any radio-communication equipment in respect of which a licence is not in force shall be guilty of an offence" (TA2000:1270-1272), with a defence of reasonable unawareness (TA2000:1273-1276).
None of ss 34 and 35 states a penalty, so s 65 applies: "a fine not exceeding $10,000 or to imprisonment for a term not exceeding 3 years or to both", "in addition to the forfeiture of any article seized" (TA2000:1916-1920), and from 16 February 2005 "in the case of a continuing offence, to a further fine not exceeding $1,000 for every day or part thereof during which the offence continues after conviction" (A10-05:961-964; S76-05:23-24; TA2026:5941-5948).
The offences under ss 34(2), 35(1) and 35(3) are compoundable from 11 November 2005 (COMP05:23-31).

What could cover the person under the TA, and what each actually covers:
- A licence under s 5, which "may be granted either to any person, class of persons or a particular person" (TA2000:359-360); nothing deposited shows one for broadcast receivers, and nothing in the Act requires such a licence to be gazetted, so the deposited sources cannot exclude one.
- Rg 5 reg 19 authorises possession of a "station" (which includes "a receiver", RG5:273-275) only by a station, network or class licence (RG5:555-558); the class licence of reg 65 covers only stations connected with public cellular, paging, mobile data, trunked radio or satellite mobile systems (RG5:1094-1106), and the 2009 station (spectrum) class licence covers a femtocell operated by a telecommunication licensee (S461-09:69-72, 95-99).
- N 1 exempts from ss 33, 34(1)(b) and 35 only equipment in its Schedule (N1:24-31); item 11(e) "TV Receivers/Radio Systems" sits under item 11 "Remote Control Devices" (N1:102-111), so it exempts the remote control, not the receiver; the asterisk note concerns "Other low power equipment" that "meet the output power limits" (N1:161-164), which a receive-only set does not emit.
- The Dealers Regulations' personal-use rule says such a person "shall not be required to obtain the approval of the Authority" (S478-05:145-147); approval (TA s 9, "Any equipment to be used for connection to any telecommunication system … shall be approved by the Authority before use", TA2000:510-512) is a different thing from a licence under s 5, and the regulation does not say the person is licensed or that possession is authorised.
- The Ministerial exemption power, "The Minister may exempt any person or class of persons from all or any of the provisions of this Act" (TA2000:2038-2039); N 1 is the only deposited exercise of it that touches s 34(1)(b).

Section 72 (now s 95) is the hinge.
It says the TA "shall not apply to the licensing of any broadcasting service or any broadcasting apparatus under the [Broadcasting Act]", except for telecommunication systems used for broadcasting and the "approval of any broadcasting apparatus" under s 9 (TA2000:2030-2035; TA2026:6987-6992).
"broadcasting apparatus" in the TA has "the meanings given by the Broadcasting Act 1994" (TA2026:275-276), so it carries the First Schedule qualifier.
Two readings are open, and I record both.
Broad reading: the TA's licensing requirements do not reach apparatus that is "broadcasting apparatus" licensed under the BA; the exceptions for telecommunication systems and s 9 approval only make sense as carve-backs from such a general exclusion.
Narrow reading: s 72 only stops the TA from governing the BA's own licensing process, and ss 34 and 35 apply to any radio-communication equipment whatever its BA status.
On the narrow reading, every licensed household was also committing an s 34(1)(b) offence before 2011, which I think a court would not accept; I prefer the broad reading, with moderate confidence.
On the broad reading, the shield depends on the receiver being "broadcasting apparatus", and from 1 January 2011 (as read on or after 31 October 2012) a TV set or radio is not, so s 72 no longer covers it.
On the narrow reading, nothing changed at 2011 under the TA: the receiver was always exposed to s 34(1)(b).

### 1.4 Retrospective instruments and the two reading dates

S 548/2012 and S 549/2012 were made on 30 October 2012, first published on 31 October 2012, and each "shall be deemed to have come into operation on 1st January 2011" (S548:3, 29-31, 59; S549:3, 20-22, 37).
Subsidiary legislation "may be made to operate retrospectively to any date not being a date earlier than the commencement of the Act … by or under which the subsidiary legislation is made" (IA:1271-1274); the deposited IA is the current text, so I cite it for the rule and not for its 2012 section number.
A reader before 31 October 2012 could see only the First Schedule with three items (BA2012:2163-2169, an edition dated 31 August 2012) and Rg 1 in force.
A reader on or after 31 October 2012 is told that from 1 January 2011 TV and sound receivers were not "broadcasting apparatus" and that Rg 1 was revoked.
For conduct before 1 January 2011, a repeal does not "affect any penalty, forfeiture or punishment incurred in respect of any offence committed against any written law so repealed" "unless the contrary intention appears" (IA:1071-1088), and S 548/2012 itself saves the revoked Regulations for licences and matters before 1 January 2011 (S548:37-53).
For conduct in 2011, the deeming places the conduct after the repeal took effect, so on the literal text read after 31 October 2012 no BA licence was required for a TV set or radio in 2011.
The same deeming, on the broad reading of s 72, removes the TA shield for 2011 conduct as well; whether a court would let a retrospective instrument published after the conduct expose that conduct to TA ss 34 and 35 is a question the deposited sources do not answer (no constitutional text is deposited).

### 1.5 Answer: analogue terrestrial television receiver (aerial, receive-only, no decoder), conduct by an individual

| conduct day | read as at | answer | confidence |
| --- | --- | --- | --- |
| before 1 January 2011 (e.g. 1 June 2010) | any day | **Offence** under BA s 47 for contravening s 20(1)(c), if the person operates or has on premises they own or occupy a set on which broadcasts are received and holds no s 20 licence and is not covered by another's household, hotel, school or hospital licence (RG1:485-488, 525-552); max fine $40,000, imprisonment 3 years, or both; forfeiture of the set; compoundable up to $1,000. Under the broad reading of TA s 72, no TA offence. | High on the BA offence; moderate on the absence of a TA offence (depends on s 72). |
| in 2011 | before 31 October 2012 | **Offence** under BA s 47 as at date 1, on the text a reader could see then; TA shielded by s 72 on the broad reading. | High that this is what the text then said. |
| in 2011 | on or after 31 October 2012 | **Not a BA offence**: S 549/2012 deems the set not "broadcasting apparatus" from 1 January 2011 and S 548/2012 revokes Rg 1 from the same day. On the TA, the literal chain (broad reading of s 72 now inapplicable; set is radio-communication equipment; no licence, regulation or exemption deposited covers it) gives an s 34(2)/35 offence with the s 65 penalty, but only through a retrospective instrument published after the conduct. **The sources do not answer** whether that TA exposure is real. | High on "not a BA offence"; low on the TA question. |
| 1 November 2012 to 31 December 2018 (e.g. 1 June 2015) | that day | **Not a BA offence.** **Literal text: an offence** under TA s 34(1)(b)/(2) (possession) and s 35(1) (operation, with possession deemed operation) and s 35(3) (occupier), max fine $10,000, imprisonment 3 years, or both, plus up to $1,000 a day for a continuing offence, forfeiture of any article seized; compoundable. Conditions: the broad reading of s 72; the set counts as radio-communication equipment; no undeposited s 5 class licence or s 73 exemption. | Moderate that this is the literal reading; low that a court would convict, given s 9A (§1.9) and the possibility of an undeposited s 5 licence or exemption. |
| today, 3 November 2026 | today | **Not a BA offence** (First Schedule lists only TVRO, BA2026:4347). **Literal text: an offence** under TA s 54(1)(b)/(2) and s 55, penalty s 85, as for the row above; s 95 does not reach the set because it is not "broadcasting apparatus". The deposited Rg 5, N 1 and Dealers texts stop at 2016, 2017 and 2014 respectively, and **the sources do not answer** whether any later instrument covers receivers. Nothing deposited says when analogue terrestrial broadcasting ended; if no analogue broadcast is receivable, whether an idle set is still "used or intended to be used for telecommunications" is a further open question. | Low-to-moderate on the literal reading; low on what a court would hold. |

### 1.6 FM broadcast radio

Before 1 January 2011 an FM radio is a "broadcast sound receiver" (BA2003:2146-2147) and "broadcasting apparatus", so s 20(1)(c) and s 47 apply as for television.
Rg 1 names only vehicle and vessel sound receivers as needing a licence (RG1:441-444, narrowed to vessels by S333:130-133), sells a sound-receiver licence at "$27 for 12 months" (RG1:629), covers household radios under a television licence (RG1:485-488), and from 2004 provides for "a licence to install or operate a broadcast sound receiver" (S333:127-129).
The Act itself requires a licence for a home radio; the deposited regulations never say so expressly, which makes me suspect an exemption or a practice that is not deposited; **the sources do not fully answer** whether a lone home radio without a household TV licence needed its own licence in practice.
On the text, before 2011: offence under s 47 (moderate confidence); 2011 read after 31 October 2012 and later: not a BA offence; TA: the same literal chain as for television (§1.5).
H4 says low-power FM transmitters being lawful covers FM receivers.
The deposited FM-band entry is N 1 item 3, "Wireless Microphones … 88.00 – 108.00 MHz 60 dBµV/m @ 10m" (N1:48-50; S726-14:67-70), an exemption for "the localised on-site installation or operation of the equipment specified" (N1:30-31), that equipment being microphones, which are transmitters.
It does not exempt any other equipment in that band, and nothing in it mentions a receiver; H4 is refuted on the text.

### 1.7 AM broadcast radio (526.5-1606.5 kHz)

Under the BA an AM radio is a broadcast sound receiver exactly like an FM radio, so the BA answers are those of §1.6.
Under the TA I searched N 1 and its 2014 replacement for an AM receiver entry: item 3 lists "Wireless Microphones 0.51 - 1.60 MHz 57 dBµV/m @ 3m" (N1:48; S726-14:67), again transmitters, and item 12 "Cordless Telephones" starts at "1.605 – 1.800 MHz" (N1:118); there is no receiver entry in the medium-wave band.
The Dealers Fifth Schedule's "510 – 1600 kHz 57 dBµV/m @ 3m" (S210-10:231) is a registration-fee waiver for "Short Range / Low Power devices" (S210-10:227-229), not an authorisation to possess anything.
Nothing deposited covers an AM receiver under the TA; the literal answers are those of §1.5.

### 1.8 Receivers installed in a vehicle

Before 1 January 2011, installing a radio or television "on board any … vehicle registered in Singapore" without a licence contravenes BA s 20(1)(a) (BA2003:702-703), an offence under s 47.
Rg 1 as at February 2004: "A licence shall be required for every broadcast sound receiver installed in a vehicle" (RG1:441-444), "installed" meaning "affixed in that vehicle … by means of brackets or other mountings" (RG1:453-457), and "A separate licence shall be required for every broadcast television receiver installed in a vehicle" (RG1:501-504).
S 333/2004 removed "vehicle" from reg 23 (S333:130-133) but left reg 28(2), reg 5(5) (vehicle sound-receiver licence varied for TV, RG1:228-232) and reg 10(2) (licence follows the vehicle's registration, RG1:304-310), so the vehicle licence continued under s 20(1)(a) itself until 2011; the "$27 for 12 months" fee (RG1:629) is the sound-receiver fee those regulations attach to.
After 1 January 2011 (read after 31 October 2012) no BA licence is required; on the TA, s 35(1) expressly reaches operation "in any vehicle in Singapore" (TA2000:1259; TA2026:4914), so the literal chain of §1.5 applies with the same caveats.
A vehicle registered outside Singapore is outside s 20(1)(a) on its words.

### 1.9 Satellite receiving system (TVRO, dish)

A TVRO system is in the First Schedule at every date (BA2003:2143; BA2012:2169; S549:31; BA2026:4347), so installing or operating one needs a s 20 licence at every date.
The TVRO Regulations say "No person other than an institution may be granted with a licence" (TVRO:16), "institution" meaning "any body of persons, corporate or unincorporate, and includes any undertaking" (TVRO:7).
So an individual cannot hold a TVRO licence, and an individual who installs or operates a dish commits the s 47 offence at every date: max fine $40,000, imprisonment 3 years, or both, forfeiture; compoundable.
Because a TVRO is "broadcasting apparatus" throughout, TA s 72/95 keeps the TA's licensing out on the broad reading.
H6 ("individually licensed under the Broadcasting Act") is wrong for individuals: the Act requires a licence and the Regulations forbid granting one to an individual.
Confidence: high on the Act; moderate on the Regulations, whose deposited text is a 2004 RevEd served by lawplain with no evidence of its state after 2004.

### 1.10 The hypotheses

- H1, confirmed: the obligation existed (BA s 20 with Rg 1) and ended by S 548/2012 and S 549/2012, deemed from 1 January 2011 but published on 31 October 2012.
- H2, holds on the literal text with two conditions and one gap: nothing deposited replaced the licence for terrestrial receivers, and on the broad reading of s 72 the receiver moves from the BA offence ($40,000 and 3 years) into TA ss 34 and 35 (s 65: $10,000 and 3 years, plus the daily continuing fine and forfeiture); it requires the broad reading of s 72 (otherwise the TA exposure is not new) and that a receiver is radio-communication equipment; the gap is that an undeposited s 5 licence or s 73 exemption cannot be excluded.
- H3, not established from the deposited texts: the candidates are N 1 (no receiver item but GPS), Rg 5 reg 65 (public mobile systems only), and the Dealers personal-use rule (approval, not licence); the Class Licences Regulations concern operators of telecommunication services, not receivers.
- H4, refuted: the FM-band entry is for wireless microphones, and the same item has an AM-band entry, so the argument would prove AM too if it proved anything.
- H5, not confirmed: the deposited instrument naming DVB-T2 receivers is S 251/2013 from 25 April 2013, a registration-fee schedule for dealers (S251-13:161-168); "IMDA TS DVB-T2 IRD" is not named in any deposited text, and nothing deposited dates such a regime to 2019 or gives it the effect of a licence to possess.
- H6, refuted for individuals (§1.9).

### 1.11 Ambiguities I found that decide the answer

1. Whether "specified in the First Schedule" qualifies the whole s 2(1) definition (I say yes, high confidence).
2. How far TA s 72/95 reaches: the TA's licensing requirements for broadcasting apparatus, or only the BA's licensing process (I prefer the first, moderate confidence; the answer flips with it).
3. Whether a receive-only television or radio is "radio-communication equipment" (I say yes on the definitions; the regulator's own exemption of GPS receivers and the registration of DVB-T2 receivers as dealers' equipment point the same way).
4. Whether the pre-1 February 2012 "telecommunication purposes" wording matters (I say no for receivers).
5. The effect of S 548/2012 and S 549/2012 on 2011 conduct, read before and after 31 October 2012 (BA answer flips; TA exposure for 2011 unresolved).
6. Whether "on any premises in Singapore owned or occupied by him" in s 20(1)(c) qualifies "operate" as well as "have"; Rg 1's exemption of temporary use "in a public place" (RG1:460-462, 521-523) suggests the drafter thought "operate" stood alone.
7. Whether the Dealers personal-use rule (S478-05:144-149) is "in accordance with … any regulations made under this Act" for s 34(1)(b); I say no, because it dispenses with approval and grants nothing.
8. Whether an undeposited s 5 class licence or s 73 exemption exists; the deposited texts cannot say.

### 1.12 Section 9A, provisionally

On the literal reading, from 2011 every household with an aerial-fed television or radio and no TA licence commits an offence carrying three years' imprisonment, created by the same instruments that refunded the old licence fees (S548:54-57), with no route to compliance short of a station licence under Rg 5.
In my view that result is manifestly unreasonable, and a court may consult extrinsic material under s 9A(2)(b)(ii) (IA:902-930) to find the purpose of TA s 72/95 and of S 549/2012.
Against a purposive escape through the definitions, the regulator's own instruments treat receive-only devices as needing exemption (N 1's GPS and MMDS receivers, N1:140-149) and treat DVB-T2 receivers as radio-communication equipment to be registered for sale (S251-13:161-168), so any purposive answer would more naturally come through s 72/95 than through the meaning of "radio-communication equipment".
I leave the purposive outcome open.
No Hansard or Gazette material was read for purpose in section 1, except the Bill 20/2011 explanatory statement, which is extrinsic (B20-11).

## 2. Corrections to section 1

Section 1 is left as written; these are the points in it I now think wrong or incomplete, found after it was written (and so after the leak).
1. **§1.1, TVRO Regulations row, "began".**
   "22 March 1991" is when the Regulations began; the institution-only rule I quote there began on 1 August 2001.
   S 354/2001 substituted reg 3: "No person other than an institution may be granted with a licence" (`subjects/sg/singapore-broadcasting-authority-tvro-system-amendment-regulations-2001/registers/source-bundle/BA1994-S354-2001.txt:52-53`), and it "shall come into operation on 1st August 2001" (`:22-24`).
2. **§1.2, one of my two arguments against reading B of s 2(1) is wrong.**
   I said the rival reading "leaves 'capable of' without an object".
   It does not: on reading B, "capable of" shares the object "the reception of any broadcasting service", and only the second limb carries "and specified in the First Schedule".
   My other argument stands, and §3(a) gives the stronger ones.
3. **§1.9, "an individual cannot hold a TVRO licence", is too firm.**
   "institution" "means any body of persons, corporate or unincorporate, and includes any undertaking" (TVRO:7), and an individual who carries on an undertaking may be one (the BA encoder's F-BA-05, reading A).
   The conclusion holds for an individual acting as a householder, which is the question's case; H6 stays refuted for that case.
4. **§1.1 and §1.3, the dates "1 December 1999".**
   The earliest TA text deposited is the 2000 Revised Edition (dated 30 December 2000).
   The Act as enacted is not deposited.
   1 December 1999 is the date in s 3(1), "As from 1 December 1999 and subject to this Act" (`TA1999.txt:565`).
   So the start date I gave for ss 34, 35, 65 and 72, and for "equipment", is an inference that their 1999 words were the 2000 words.
5. **§1.3 and §1.11 item 8, what could cover the person under the TA.**
   I listed a s 5 licence, Rg 5, N 1, the Dealers rule and a s 73 exemption.
   A third kind of instrument exists: subsidiary legislation made under the Telecommunication Authority of Singapore Act and continued by TA s 98(2).
   The one found, O 3 (1998), is analysed in `MISSED-INSTRUMENTS.md` part E3; on the evidence of a 1998 Bill it most likely concerns approval of equipment before use, and it leaves only a small reservation on dates 2 and 3 (§7).
   Under the same Act, the 1999 Radio-communication Regulations governed receivers until 1 March 2001.
   Reg 4(1): "no person shall possess, establish, install or use any station … unless he has a valid licence granted under these Regulations" (`review-out/sources/gazette-cap323-Rg3-1999/99323rg3.txt:249-252`), "station" including a "receiver" (`:231-233`).
   Their First Schedule exempts no broadcast receiver.
   So section 1's TA answer for the years before 2011 has the same shape back to 1999.
6. **§1.5, last row, "the deposited Rg 5, N 1 and Dealers texts stop at 2016, 2017 and 2014".**
   S 588/2023 (N 1) and S 589/2023 (Rg 6) have now been read, and neither adds a receiver item (`MISSED-INSTRUMENTS.md` part E).
   S 588/2023 also renumbers N 1's sections to "sections 53, 54(1)(b) and 55" (`review-out/sources/gazette-S588-2023/588.txt:19-35`).
   Whether Rg 5 was amended after S 100/2016 is still open.

## 3. The readings (step 4), tested against the encodings

I read both fork registers only for this step.
The TA register points to a quarantined file for the five forks on the question's path (`subjects/sg/telecommunications-act-1999/encodings/legalese-sonnet-5.5/NOTES.md:393-401`), so for those I tested the modules' code, not the encoder's prose.

**(a) Whether "specified in the First Schedule" qualifies the whole of s 2(1) "broadcasting apparatus".**
The text: "any apparatus capable of or designed or constructed for the reception of any broadcasting service and specified in the First Schedule" (BA2026:277-279).
I hold reading A, the whole definition, with high confidence, for four reasons.
- On reading B every set capable of reception is broadcasting apparatus whatever the Schedule says, so the Schedule would bite only on apparatus designed for reception but incapable of it.
  Listing "Broadcast television receiver" and "Broadcast sound receiver" (BA2003:2139-2141), and S 549/2012's removal of them, would then do nothing.
- The Schedule is headed "BROADCASTING APPARATUS" with the note "Sections 2(1) and 65(1)" (BA2026:4342-4346).
  Section 65(1) lets the Minister "at any time amend the First, Second or Third Schedule" (BA2026:4289-4290), a power with no work to do for receivers on reading B.
- "capable of" and "designed or constructed for" are alternative complements of "apparatus" with one object, so the closing "and specified" is most naturally a further condition on "apparatus".
- A third attachment, to "broadcasting service", is excluded by the Schedules themselves: the First lists apparatus and the Second lists services ("LICENSABLE BROADCASTING SERVICES", BA2026:4362-4364).
The BA encoding takes A and encodes B beside it (`sgba-versions.l4:136-146`, F-BA-01).
The TA encoding takes "broadcasting apparatus" as an input whose meaning it describes with the conjunct (`sgta-part9-general.l4:14-15`).
**I agree with both.**

**(b) How far TA s 95 (2000 Ed. s 72) reaches.**
The text: "This Act does not apply to the licensing of any broadcasting service or any broadcasting apparatus under the Broadcasting Act 1994 except in respect of the regulation of any telecommunication system required for the operation of any broadcasting service or the approval of any broadcasting apparatus used in accordance with section 11." (`TA1999.txt:6987-6992`).
I still prefer the broad reading, with moderate confidence.
The two exceptions are a reason I did not give in section 1: on the narrow reading neither the regulation of a telecommunication system nor the approval of apparatus under s 11 is "licensing ... under the Broadcasting Act", so neither would need excepting.
They only do work as carve-backs from a general exclusion of the TA's regime for broadcasting apparatus.
Against it: "under the Broadcasting Act 1994" can be read as qualifying "licensing", which points at the BA's own process.
For 1 January 2003 to 15 February 2005, when s 72 still named "the Singapore Broadcasting Authority Act (Cap. 297)" (TA2000:2030-2035), the reference is read as to the Broadcasting Act: "a reference therein to the Singapore Broadcasting Authority Act (Cap. 297, 1995 Ed.) shall be read as a reference to the Broadcasting Act" (BA2003:2077-2082).
The TA encoding states both readings: Reading A displaces s 54(2) for broadcasting apparatus and Reading B does not (`sgta-part6-offences.l4:126-150`), with A the default (`sgta-part9-general.l4:7-12`).
Its Reading A turns on whether the apparatus is broadcasting apparatus, not on whether a BA licence was actually held, which I agree with: "licensing ... under the Broadcasting Act" names the regime.
It passes a literal `FALSE` for the s 11 approval exception when it applies s 95 to s 54(2) (`sgta-part6-offences.l4:131`); that is right for a possession question, where approval is not in issue.
**I agree with the encoding's structure and its default.**

**(c) Whether a television set is "radio-communication equipment" for s 54(1)(b).**
The Act defines "telecommunications" to include "reception" (`TA1999.txt:529-536`), "radio-communication" as "any telecommunication by means of Hertzian or radio waves" (`:450-451`), and "equipment" by use "for telecommunications" (`:325-329`); "radio-communication equipment" is not itself defined.
The TA encoding composes the two definitions (`sgta-s2-definitions.l4:63-77`, FORK 1), as I did.
Three things found after section 1 point the same way: the regulator has treated receive-only equipment as inside the licensing regime since before 1999.
- The 1999 Radio-communication Regulations made a "receiver" a "station" needing a licence (`99323rg3.txt:231-233, 249-252`), exempting GPS and MMDS receivers by name.
- The 1999 Dealers Regulations prohibited the sale of "Scanning Receivers" (`99323rg7.txt:646-654`).
- The Telecommunication Authority of Singapore Bill 1992 defined "telecommunications" with the same words, "transmission, emission or reception" (lawplain `bills` B16-1992, clause 2; extrinsic, a Bill as introduced).
The 2011 amendment does not cut the other way: its addition, "capable of being used for the operation of any broadcasting service" (`TA1999.txt:325-329`), speaks of operating a broadcasting service, which is the broadcaster's side, not reception.
**I agree with the encoding**, moderate-to-high confidence.

**(d) Whether the pre-1 February 2012 "equipment" ("used or intended to be used for telecommunication purposes", TA2000:226-227) matters.**
Section 1 said no; I now think it matters for one row, and I still read it the same way.
It matters for conduct from 1 January 2011 to 31 January 2012 read on or after 31 October 2012: there the TA exposure depends on a 2011 receiver being "equipment" under the old words.
On my reading, reception is a "telecommunication purpose" because "telecommunications" includes reception, so the old words cover a receiver too.
The rival reading has a textual hook: the new words say "including (for the avoidance of doubt)" (A19-11:49-54).
And the Bill's explanatory statement (extrinsic) says the change is "to clarify that the term includes" broadcasting-capable apparatus (B20-11:2571-2574), which implies someone had doubted it.
On that reading a 2011 receiver was not "equipment", and the retrospective TA exposure for 2011 disappears.
The TA encoding carries this as FORK 6.
Its `sgta-ta-versions.l4` flags the old wording by version (`:131-158`), and my run selects the old wording for conduct on 1 June 2011 read on 3 November 2026 (§3(f), pair 23).
It must do so for every reading day, because the Act 19 of 2011 row needs `conduct day AT LEAST (Date 1 2 2012)` (`sgta-ta-versions.l4:94`).
**I agree it is a live fork; I give the rival reading less weight than the encoder appears to, but it can only help the person.**

**(e) The retrospective instruments, S 548/2012 and S 549/2012.**
Both are "deemed to have come into operation on 1st January 2011" and were first published on 31 October 2012 (S548:3, 29-31; S549:3, 20-22).
The Interpretation Act allows subsidiary legislation to "operate retrospectively to any date not being a date earlier than the commencement of the Act" under which it is made (IA:1271-1274, current text).
Both encodings apply the deeming as written, on two days (BA `NOTES.md:53-58`; TA `NOTES.md:154-163`).
The BA notes add that whether a retrospective notification is valid, "and what a court would do with conduct already past, is not addressed" (BA `NOTES.md:76-78, 391`); the parts of the TA notes in my copy say nothing on validity.
For an encoding, not ruling on validity is right, and I agree.
My own view on the open point is unchanged from §1.4, with one addition.
For the Broadcasting Act the deeming only removes liability.
The exposure under the TA for 2011 conduct arises indirectly, because s 95's shield depends on the apparatus being "broadcasting apparatus" on the conduct day.
The revocation's own terms point to a fiscal purpose: S 548/2012 refunds "Any fee for the grant or renewal of a licence … paid … for a period commencing on or after 1st January 2011" (S548:54-57).
A court reading the deeming for that purpose would be slow to let it create criminal exposure for conduct already past.
Article 11 of the Constitution is not deposited and I have not read it.
The sources do not answer this.

**(f) The two-date version model, checked at 37 pairs by running the encodings' own selection functions.**
Method: I copied both encodings into my scratchpad, outside VIEW, and added one probe module to each that only calls the encodings' selection functions (kept as `review-out/tools/zz-review-pairs-ba.l4` and `zz-review-pairs-ta.l4`).
I ran it with the pinned l4 (0 errors) and compared each result with the dates printed in the deposited texts.

| # | function | conduct day | reading day | selected | what the texts say | agrees |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | BA First Schedule | 31 Jul 2003 | 31 Jul 2003 | Revised Edition 2003 | edition dated 31 July 2003, three items (BA2003:2134-2154) | yes |
| 2 | BA First Schedule | 30 Jul 2003 | 1 Oct 2026 | NOTHING | no earlier text deposited | yes (limit) |
| 3 | BA First Schedule | 1 Jun 2010 | 1 Oct 2026 | Revised Edition 2003 | S 549 takes effect only from 1 Jan 2011 | yes |
| 4 | BA First Schedule | 1 Jun 2011 | 30 Oct 2012 | Revised Edition 2003 | S 549 not yet published (S549:3) | yes |
| 5 | BA First Schedule | 1 Jun 2011 | 31 Oct 2012 | S 549/2012 | published 31 Oct 2012, deemed from 1 Jan 2011 | yes |
| 6 | BA First Schedule | 15 Sep 2012 | 15 Sep 2012 | Revised Edition 2012 | edition of 31 Aug 2012 prints three items (BA2012:2163-2169) | yes |
| 7 | BA First Schedule | 15 Sep 2012 | 1 Nov 2012 | S 549/2012 | S 549 replaces the Schedule whatever edition printed it | yes |
| 8 | BA First Schedule | 1 Jun 2015 | 1 Jun 2015 | S 549/2012 | TVRO only | yes |
| 9 | BA First Schedule | 24 Sep 2024 | 1 Oct 2026 | S 549/2012 | the day before the consolidation's date; same Schedule | yes |
| 10 | BA First Schedule | 1 Jan 2025 | 1 Oct 2026 | 2024 consolidation | BA2026:4342-4357 | yes |
| 11 | BA First Schedule | 3 Nov 2026 | 3 Nov 2026 | NOTHING | the brief's "today" | **no answer (design limit)** |
| 12 | BA First Schedule | 1 Nov 2012 | 1 Sep 2012 | Revised Edition 2012 | what a reader on 1 Sep 2012 could see | yes |
| 13 | BA Rg 1 | 20 Jun 2004 | 20 Jun 2004 | Revised Edition 2004 | S 333 in operation from 21 Jun 2004 (S333:21-23) | yes |
| 14 | BA Rg 1 | 21 Jun 2004 | 16 Jun 2004 | S 333/2004 | first published 15 Jun 2004 (S333:3) | yes |
| 15 | BA Rg 1 | 31 Dec 2010 | 1 Oct 2026 | S 333/2004 | S 548 saves the Regulations for matters before 1 Jan 2011 (S548:37-53) | yes |
| 16 | BA Rg 1 | 1 Jan 2011 | 30 Oct 2012 | S 333/2004 | S 548 not yet published | yes |
| 17 | BA Rg 1 | 1 Jan 2011 | 31 Oct 2012 | S 548/2012 (revoked) | S548:3, 29-36 | yes |
| 18 | BA Rg 1 | 28 Feb 2004 | 1 Oct 2026 | NOTHING | no Rg 1 text before the 2004 edition deposited | yes (limit) |
| 19 | BA Rg 1 | 1 Jun 2015 | 3 Nov 2026 | NOTHING | Rg 1 is revoked; nothing can revive it | **no answer (design limit)** |
| 20 | TA Act text | 29 Dec 2000 | 2 Oct 2026 | NOTHING | the Act as enacted is not deposited | yes (limit) |
| 21 | TA Act text | 15 Feb 2005 | 2 Oct 2026 | Revised Edition 2000 | Act 10 of 2005 in operation 16 Feb 2005 (S76-05:23-25) | yes |
| 22 | TA Act text | 16 Feb 2005 | 16 Feb 2005 | as amended by Act 10 of 2005 | same | yes |
| 23 | TA Act text | 1 Jun 2011 | 3 Nov 2026 | as amended by Act 10 of 2005 | Act 19 of 2011 in operation 1 Feb 2012 (S33-12:23-24) | yes |
| 24 | TA Act text | 1 Feb 2012 | 30 Jan 2012 | as amended by Act 10 of 2005 | S 33/2012 first published 31 Jan 2012 (S33-12:3) | yes |
| 25 | TA Act text | 1 Feb 2012 | 31 Jan 2012 | as amended by Act 19 of 2011 | same | yes |
| 26 | TA Act text | 1 Jun 2015 | 1 Jun 2015 | as amended by Act 19 of 2011 | next amendment in operation 1 Oct 2016 | yes |
| 27 | TA Act text | 1 Jan 2022 | 3 Nov 2026 | Acts after Act 15 of 2017, not deposited | no text deposited for those days | yes (limit) |
| 28 | TA Act text | 3 Nov 2026 | 3 Nov 2026 | 2020 Revised Edition as deposited | TA2026 banner "version in force from 2/10/2026" | yes |
| 29 | N 1 | 31 Oct 2014 | 3 Nov 2026 | version of 23 Jun 2014 (S 415/2014) | S 726/2014 in operation 1 Nov 2014 | yes |
| 30 | N 1 | 1 Nov 2014 | 30 Oct 2014 | version of 23 Jun 2014 | S 726/2014 first published 31 Oct 2014 (`TA1999-N1-S726-2014-GAZ.txt:3, 23`) | yes |
| 31 | N 1 | 1 Nov 2014 | 31 Oct 2014 | version of 1 Nov 2014 | same | yes |
| 32 | N 1 | 3 Nov 2026 | 3 Nov 2026 | version of 1 Apr 2017 (S 78/2017) | S 588/2023 (in operation 1 Sep 2023) is not in the table | **stale for today**, no receiver item lost |
| 33 | Rg 6 | 25 Apr 2013 | 24 Apr 2013 | version of 25 Apr 2013 | S 251/2013 first published 24 Apr 2013 (`TA1999-RG6-S251-2013-GAZ.txt:3`) | yes |
| 34 | Rg 6 | 20 Jul 2005 | 3 Nov 2026 | version of 1 Jan 2005 | S 478/2005 in operation 21 Jul 2005 | yes |
| 35 | Rg 6 | 21 Jul 2005 | 21 Jul 2005 | version of 21 Jul 2005 | first published 20 Jul 2005 (`TA1999-RG6-S478-2005-GAZ.txt:3`) | yes |
| 36 | Rg 5 | 1 Jun 2015 | 1 Jun 2015 | version of 21 Jan 2011 (S 20/2011) | next amendment S 100/2016 | yes |
| 37 | Rg 5 | 3 Nov 2026 | 3 Nov 2026 | version of 1 Apr 2016 (S 100/2016) | no later amendment found, not proven | yes, as far as known |

Result: every selection from the tables as built agrees with the texts' printed dates; the rule ("the latest published on or before the reading day among those that take effect on or before the day of the conduct") picks the right version in every case of these tables, the retrospective ones included.
Four findings remain.
- **The BA encoding cannot answer for the brief's "today".**
  It returns NOTHING for every reading day after 1 October 2026 (`sgba-versions.l4:109-112`; pairs 11 and 19).
  The TA encoding has no such cutoff (pair 28).
  So the two encodings treat the same reading day differently, and for Rg 1, which is revoked, the cutoff withholds an answer that cannot change.
- **N 1 and Rg 6 stop before S 588/2023 and S 589/2023** (pair 32), which are not deposited; neither adds a receiver, so no outcome on the question changes.
- **The hour of publication is dropped** (BA `NOTES.md:72`).
  S 548 and S 549 were published at 5.00 pm on 31 October 2012, so a reader that morning is given texts they could not yet read.
- **The rule can mis-select in a different table.**
  Suppose a retrospective version is published after a version with a later effective date, and does not amend that later version's text.
  Then "latest published" would pick the earlier-effective one for later conduct.
  No table here has that shape: S 549/2012 amends the Schedule whichever edition printed it, so for conduct after 31 August 2012 it rightly displaces the 2012 Revised Edition.
  A later table with that shape would need a different rule.

## 4. The receiver kinds, after step 4

Unchanged from section 1 except as follows.
- **Television, all dates:** the answers of §1.5 stand, with the corrections of §2 and the new condition from O 3 (§7).
- **FM and AM radio:** unchanged.
  The 1999 Radio-communication Regulations carry the same "Wireless Microphones" entries, at "0.51 — 1.60 MHz" and "88.00 — 108.00 MHz" (`99323rg3.txt:1059-1061`); they are transmitters there too, so H4 stays refuted for FM and nothing covers AM.
  On the lone home radio before 2011 (§1.6): the BA encoding's dispatcher `Rg 1 a licence is required for a broadcast sound receiver, for conduct on a day, the law read as at a day` (`sgba-versions.l4:419-428`) reads reg 23 only (vehicles and vessels).
  So for a household radio it answers FALSE, while s 20(1)(c), encoded separately (`sgba-versions.l4:234-247`), requires a licence for any broadcasting apparatus on premises.
  The two must be read together; see `DISAGREEMENTS.md` D5.
- **Portable receivers before 2011:** whether s 20(1)(c) reaches operating a set away from premises the person owns or occupies turns on F-BA-03.
  The encoder reads "on any premises … owned or occupied by the person" as qualifying "operate" too (reading A).
  I lean the other way (§1.11 item 6), because Rg 1 needed to exempt "temporary use … in a public place" (RG1:460-462, 521-523).
  An exemption like that is needed only if "operate" reaches places the person does not own or occupy.
  For a portable radio used in a park, reading A gives no BA offence and my reading gives one.
- **Vehicle receivers:** unchanged; s 20(1)(a) names a vehicle "registered in Singapore" (BA2003:702-703), and TA s 35 / s 55 names "any vehicle in Singapore" (TA2026:4911-4916).
- **TVRO:** as corrected in §2 item 3.
  The rule is an offence at every date for an individual householder, with the s 47 penalty.
  An individual who carries on an undertaking may be an "institution".

## 5. Section 9A of the Interpretation Act

Section 9A(1) prefers "an interpretation that would promote the purpose or object underlying the written law" (IA:902-906).
Section 9A(2) lets a court consider extrinsic material "to confirm" the ordinary meaning, or to ascertain the meaning when the provision "is ambiguous or obscure" or the ordinary meaning "leads to a result that is manifestly absurd or unreasonable" (IA:908-930).
**In my view the literal reading for 2011 to 2019, and today, is manifestly unreasonable, though not absurd on its face.**
It makes possession of every aerial-fed television and radio in Singapore an offence carrying up to three years' imprisonment (TA s 54(1)(b) with s 85).
No licence is designed for such a holder: Rg 5's class licence covers only stations connected to public mobile systems (RG5:1094-1106).
And the exposure was created by instruments whose own text points to a fiscal purpose: the refund of fees "for a period commencing on or after 1st January 2011" (S548:54-57).
The extrinsic material I found fits that purpose; each item is extrinsic:
- **Hansard, 8 March 2013 (extrinsic):** the Minister said "we stopped collecting radio and TV licence fees in 2011" (`review-out/sources/lawplain-hansard/EXTRACTS.md`, record 2013-03-08-084).
- **Hansard, 8 July 2013 (extrinsic):** households "will need a DVB-T2 set-top box and indoor antenna to continue receiving our FTA channels on their existing TV sets" (record 2013-07-08-120), which assumes that owning and using those sets is lawful.
- **Hansard, 11 February 2019 (extrinsic):** "On 1 January 2019, we switched off analogue free-to-air signals" (record 2019-02-11-143).
- **Bill 20/2011, explanatory statement (extrinsic):** it cuts the other way only weakly, since it concerns apparatus "capable of being used for the operation of any broadcasting service" (B20-11:2571-2574).
- **The Gazette instruments themselves are the law, not extrinsic material:** S 548/2012, S 549/2012 and O 3.
Two things argue against treating the literal result as a defect that only purpose can mend, and so against leaning.
- A purposive answer has a natural home in s 95, whose two exceptions show the drafter meant the TA to stand aside for broadcast reception (§3(b)), rather than in the meaning of "radio-communication equipment".
- The literal reading may not be the whole of the law.
  If O 3's "section 30" turns out to be the possession prohibition (branch 2 of `MISSED-INSTRUMENTS.md` E3), an exemption may have covered type-approved receivers all along.
  The 1998 Bill makes that unlikely (it shows s 30(1) as an approval provision; extrinsic), so this is a small reservation, not a reason to lean either way.
  The literal result would then be neither absurd nor unreasonable, and s 9A would not be needed.
**I leave the purposive outcome open.**

## 6. The checks run (step 5)

`check.sh` in each encoding, with `L4=$HOME/.cache/l4-main/98/l4 L4_MAIN_BUILD=98` and `JL4_LIBRARY_PATH` unset, both exit 0, main build `1.6.98 (main, 7689b0d, 2026-10-19)`:
- TA: `TOTAL (76 modules)  0 errors, 3003 satisfied, 0 failed, 0 refused | 0, 3003, 0, 0`, every module "same" on main.
- BA: `TOTAL (64 modules)  0 errors, 2108 satisfied, 0 failed, 0 refused | 0, 2108, 0, 0`, every module "same" on main.
- Each `encoding.json` reports three more modules than my copy holds.
  TA: "79 modules, 3,363 assertions satisfied, 0 errors, 0 failed, 0 refused, identical on both l4 1.6.98 (main) columns".
  BA: "67 modules, 0 errors, 2270 assertions satisfied, 0 failed, 0 refused; every module reads the same on the main build".
  I take the difference (360 and 162 assertions) to be the quarantined `sgta-tv-*` and `sgba-tv-*` modules; I could not check that.
- Diagnostics: I ran every module once more with the same l4 and kept the output.
  The run gave 5,111 diagnostics, all `DiagnosticSeverity_Information` from source `eval`, and every one of them reads "assertion satisfied"; there are no warnings and no errors.
  That count equals 3,003 + 2,108.
- What the numbers do not show: an assertion checks only what its writer expected, and the quarantined modules, where the answers to the question live, are not in these totals.

## 7. Confidence

| question | section 1 | now | what moved it |
| --- | --- | --- | --- |
| BA: TV and radio need a s 20 licence before 2011 (s 47: $40,000, 3 years) | high | high | nothing; F-BA-01 agreed |
| TA: no TA offence before 2011 (broad s 72) | moderate | moderate | the two exceptions strengthen the broad reading; the narrow reading is still open |
| 2011 conduct read before 31 Oct 2012: BA offence | high (that this is what the text said) | high | the version model agrees (pairs 4, 16) |
| 2011 conduct read on or after 31 Oct 2012: not a BA offence | high | high | pairs 5, 17 |
| 2011 conduct read on or after 31 Oct 2012: TA exposure | low | low | reading (d) is a second escape; O 3 (branch 2, unlikely) a third |
| 1 Nov 2012 to 2018: literal TA offence (s 54(1)(b), s 55; s 85: $10,000, 3 years, $1,000 a day, forfeiture) | moderate on the literal reading | moderate, with a small O 3 reservation | O 3 (part E3): branch 1, which the 1998 Bill favours, leaves the answer; branch 2 could remove it |
| today: not a BA offence; literal TA offence | low-to-moderate | low-to-moderate, same small O 3 reservation | S 588/2023 and S 589/2023 read, no receiver item; Rg 5 after 2016 still open |
| what a court would hold for 2011 onwards | low | low | s 9A (§5) |
| FM like TV; nothing covers AM; H4 refuted | moderate / high | same | the 1999 Radio-communication Regulations show the same pattern |
| TVRO: an offence for an individual householder at every date | high on the Act, moderate on the Regulations | same | §2 item 3 narrows the Regulations point to householders |
| H1 confirmed; H2 literal with conditions; H3 not established; H5 not confirmed; H6 refuted | as §1.10 | H3 and H5 each have one unlikely route through O 3 (branch 2) | part E3 |
