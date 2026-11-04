# TV-QUESTION-BA: what the Broadcasting Act contributes to the question

Status: first written 2026-11-03 from the consolidation in force from 25 September 2024 and the lawplain instruments; rewritten the same night after the e-Gazette texts were deposited (the Revised Editions 2003 and 2012, S 549/2012, S 559/2010); rewritten again on 2026-11-04 after the Television and Radio Licensing Regulations (Rg 1), S 333/2004 and S 548/2012 were deposited, which are the licensing instruments for the question.
Verified by: every quotation below was copied from the deposit named, and every line number was checked against it; the answers by date are asserted in `sgba-tests-versions.l4`, `sgba-tests-rg1.l4` and `sgba-tv-cases-seat.l4`, which `check.sh` runs.
Not verified: whether anything in the SSO consolidations for 2010-10-01 and 2011-01-01 differs from the Gazette texts (the single SSO attempt, at 03:07:48 Singapore time on 2026-11-04, answered 403 at robots.txt, so those consolidations were not seen).
This file is quarantined: it is the only prose file in this folder that states a conclusion.
`NOTES.md`, the layer-1 modules and their tests do not state it, and nothing imports `sgba-tv-*.l4` except other quarantined files.

The question, as the brief puts it, is whether Singapore law requires a licence to possess or use a television or radio receiver (aerial, receive-only, no decoder), and whether it is an offence for an individual to have one with no licence of their own.
The Telecommunications Act side of that is Encoder TA's.
This file covers the Broadcasting Act (BA) side, hypothesis H6 (satellite receivers), and the explicit question about plain FM and AM radios.

## The decisive provisions, quoted from the deposited texts

Deposits, all under `../../registers/source-bundle/` unless stated: `BA1994.20030731.txt` (Revised Edition 2003, title page "31st July 2003"), `BA1994.20120831.txt` (Revised Edition 2012, "31st August 2012"), `BA1994.txt` (the informal consolidation "version in force from 25/9/2024", retrieved 2026-10-01), and `BA1994-S549-2012.txt` in `../../../broadcasting-amendment-of-first-schedule-notification-2012/registers/source-bundle/`.
The first two are from the e-Gazette (static PDFs, text by `pdftotext -layout`); the third is the file already in the repository, and its `BA1994.meta.json` records retrieval from SSO on 2026-10-01; the fourth is from the e-Gazette.
Sections 8, 9, 20, 47, 51, 57, 60 and 65 read the same in the 2003 and 2012 editions (compared by script after removing page furniture, `tools/cmp_sections.py` in my scratch; s 47 differs only in the spacing of "20 (1)").
The 2024 text differs from the 2012 text in ss 20, 47, 51, 57, 60 and 65 only in drafting style ("no person shall" becomes "a person must not", "he" and "his" become "the person" and "the person's", s 57(1) drops "in its discretion", s 60 drops "published" before "in the Gazette"), except that the 2012 s 57(3), "All sums collected under this section shall be paid to the Authority", is not in the 2024 text.

1. The definition of "broadcasting apparatus", s 2(1), in all three editions (2003 edition lines 198-200; 2012 edition 191-193; 2024 consolidation 277-279):
   > "broadcasting apparatus" means any apparatus capable of or designed or constructed for the reception of any broadcasting service and specified in the First Schedule;
2. The First Schedule in each version:
   - **Revised Edition 2003** (lines 2134-2154) and **Revised Edition 2012** (lines 2163-2178) have the same items and the same definitions: "1. Broadcast television receiver. 2. Broadcast sound receiver. 3. Television receive-only satellite receiving system (TVRO system)."
     "For the purposes of this Schedule — 'broadcast sound receiver' means any apparatus used for the aural reception of any broadcasting service; 'broadcast television receiver' means any apparatus used for the visual and aural reception in monochrome or colour of any broadcasting service; 'television receive-only satellite receiving system' means any apparatus (including a dish antenna) or any combination of apparatus capable of direct reception of any broadcasting service emitted from or passing through any communication or broadcast satellite in extra-terrestrial space."
   - **S 549/2012** (deposit lines 3, 20-22, 25-35, 37): "First published in the Government Gazette, Electronic Edition, on 31st October 2012 at 5.00 pm"; "Made this 30th day of October 2012"; made under section 65.
     Paragraph 1: it "shall be deemed to have come into operation on 1st January 2011".
     Paragraph 2: "The First Schedule to the Broadcasting Act is deleted and the following Schedule substituted therefor: FIRST SCHEDULE ... BROADCASTING APPARATUS 1. Television receive-only satellite receiving system (TVRO system)." with the same definition of that term.
   - **The consolidation in force from 25/9/2024** (lines 4342-4357): the same single item as S 549/2012.
3. Section 20(1) (2003 edition lines 701-710; 2012 edition 684-694; 2024 consolidation 1425-1439):
   > Subject to this section, no person shall — (a) install any broadcasting apparatus in any place, or on board any ship, aircraft or vehicle registered in Singapore; (b) import, offer for sale, sell or have in his possession with a view to sale, any broadcasting apparatus; or (c) operate or have on any premises in Singapore owned or occupied by him broadcasting apparatus on or by which broadcasting services are received, except under and in accordance with a licence granted under this section.

   (The 2024 text reads "a person must not" and "the person's possession" and "owned or occupied by the person".)
   Section 20(2): a licence is in the form, for the period and on the terms and conditions the Authority determines.
   Section 20(3): members of the Singapore Armed Forces, Police Force, Vigilante Corps and Civil Defence Force working a broadcasting apparatus in the course of duty need no licence.
   Section 20(4): "The Authority may exempt any person or broadcasting apparatus or class of broadcasting apparatus from subsection (1)."
4. Section 47 (2003 edition lines 1736-1741; 2012 edition 1719-1724; 2024 consolidation 3676-3681): fine up to $40,000 or imprisonment up to 3 years or both, and "any broadcasting apparatus installed or found in the possession of the person so convicted shall be forfeited to the Authority".
5. Section 57(1) and the Composition of Offences Regulations (reg 2, as deposited from 2 July 2007): the Authority may compound a prescribed offence for a sum "not exceeding $1,000"; reg 2 prescribes "The offence under section 47 of the Act".
6. The TVRO System Regulations (G.N. S 126/1991, 2004 Revised Edition, as lawplain served them), reg 3(2): "No person other than an institution may be granted with a licence."
   Reg 2: "institution" means "any body of persons, corporate or unincorporate, and includes any undertaking".
7. Section 65(1) (2024 consolidation lines 4289-4290): "The Minister may, by notification in the Gazette, at any time amend the First, Second or Third Schedule."
   S 549/2012 was made under that power.

## The licensing regulations: Rg 1, S 333/2004 and S 548/2012

Section 20(2) of the Act leaves the form, period, terms and conditions of a licence to the Authority, and the Authority set them by regulations made under s 66: the Broadcasting (Television and Radio Licensing) Regulations (Rg 1).
Three Gazette texts decide what those Regulations said and when they stopped.
Deposits: `BA1994-RG1.txt` (Revised Edition 2004, "REVISED EDITION 2004 (29.2.2004)"), `BA1994-S333-2004.txt` and `BA1994-S548-2012.txt`, in `../../../broadcasting-television-and-radio-licensing-regulations/`, `../../../broadcasting-television-and-radio-licensing-amendment-regulations-2004/` and `../../../broadcasting-television-and-radio-licensing-revocation-regulations-2012/`, each under `registers/source-bundle/`.

1. **Rg 1, Revised Edition 2004** (29 February 2004; "Rg 1, 1990 Ed., G.N. No. S 21/80, amended by S 46/83 ... S 212/99").
   - Reg 27(1), television receivers (lines 481-482): "No person shall operate a broadcast television receiver without a licence."
   - Reg 27(3) (lines 485-488): "A licence shall permit the use of one or more broadcast television receivers and one or more broadcast sound receivers by the licensee, members of his family and domestic servants resident at the address specified therein."
   - Reg 23(1), sound receivers (lines 441-444): "A licence shall be required for every broadcast sound receiver installed in a vehicle or in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act (Cap. 323)."
     Reg 23 is the only regulation that says in terms that "a licence shall be required" for a sound receiver; the Regulations also name a sound receiver licence elsewhere without limiting it to a vehicle or vessel (reg 8(b), reg 24, reg 25, the First Schedule and the Second Schedule: see "Household radios" below).
   - Regs 24 and 29 (lines 460-462, 521-523): a licence "shall not be required for the temporary use of a broadcast sound receiver [television receiver] in a public place or at an official or social function or a function organised for charitable purposes".
   - Reg 28(2): "A separate licence shall be required for every broadcast television receiver installed in a vehicle or in a vessel in respect of which a ship station licence has not been granted".
   - Reg 2(1) (lines 139-156): "broadcast sound receiver" is any apparatus used for the aural reception, and "broadcast television receiver" any apparatus used for the aural and the visual reception in monochrome or colour, "of broadcast matter transmitted by radio waves, wire or cable"; the television receiver "does not include any Television Receive-Only Satellite Receiving System".
   - First Schedule (fees; lines 624-651): item 2, "Licence for a broadcast sound receiver ... $27 for 12 months"; item 3, a television receiver in monochrome, "$40 per annum"; item 4, in colour, "$110 per annum"; items 5 to 8, hotels and hospitals.
   - No provision of Rg 1 names a car, a car radio, an FM radio or an AM radio.
2. **S 333/2004** (made 11 June 2004; "First published ... on 15th June 2004 at 5:00 pm"; "shall come into operation on 21st June 2004").
   - Reg 23(1) and (2) are deleted and replaced (lines 127-133): "(1) An application for a licence to install or operate a broadcast sound receiver may be made at any post office or at such other places as the Authority may require. (2) A licence shall be required for every broadcast sound receiver in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act (Cap. 323)."
     The vehicle has gone from the requirement.
   - Reg 27(1) and (2) are deleted and replaced (lines 141-144): "(1) An application for a licence to install or operate a broadcast television receiver may be made at any post office or at such other places as the Authority may require."
     The sentence "No person shall operate a broadcast television receiver without a licence" is no longer in the Regulations.
   - New reg 29A (lines 165-169): "A separate licence shall be required for every broadcast television receiver installed in a commercial property."
   - Para 2(a) deletes the definitions of "broadcast sound receiver" and "broadcast television receiver" (F-BA-11 in NOTES.md).
   - It leaves the First Schedule (fees), regs 24, 28(2) and 29 as they were.
3. **S 548/2012** (made 30 October 2012, "First published in the Government Gazette, Electronic Edition, on 31st October 2012 at 5.00 pm"; made under s 66 by the Media Development Authority with the Minister's approval).
   - Reg 1 (lines 29-31): the Regulations "shall be deemed to have come into operation on 1st January 2011".
   - Reg 2(1) (lines 34-36): "The Broadcasting (Television and Radio Licensing) Regulations (Rg 1) ... are revoked."
   - Reg 2(2) (lines 37-53): the revoked Regulations "shall continue to apply to and in relation to" (a) every licence granted under s 20(1) of the Act in respect of any broadcast television receiver or broadcast sound receiver "for any period before 1st January 2011", (b) every such receiver "in respect of any matter ... which occurred before 1st January 2011", and (c) every such licensee "in respect of any thing which he is required, before 1st January 2011, to do", "as if these Regulations had not been made".
   - Reg 2(3) (lines 54-57): any fee for the grant or renewal of a licence, or for its variation, "paid in advance under regulation 5 of the revoked Regulations, for any period commencing on or after 1st January 2011, shall be refunded to the licensee in full".
4. S 549/2012 (the First Schedule of the Act) has the same publication day and hour (31 October 2012, 5.00 pm) and the same deemed commencement (1 January 2011).
   The two instruments together take receivers out of the Act's First Schedule and revoke the Regulations that licensed them, each from 1 January 2011 and each published on 31 October 2012.

The Regulations' version table has three rows (Revised Edition 2004: effective and published 29 February 2004; as amended by S 333/2004: effective 21 June 2004, published 15 June 2004; revoked by S 548/2012: effective 1 January 2011, published 31 October 2012).
No text of Rg 1 before 29 February 2004 was obtained; the history line names S 21/80 and eleven amendments, of which only S 212/99 (14 May 1999: reg 8, "waive or reduce") was fetched.

## How the encoding reads two days

Every version of the First Schedule has two dates: the day it takes effect (valid time) and the day it was published (rule-version time); `sgba-versions.l4` holds them as a table.
A question has two days: the day of the conduct, and the day the law is read as at.
The version read is the latest published on or before the reading day among those that take effect on or before the day of the conduct; where none qualifies, the answer is "the texts deposited do not say for those two days".
On an `unstable` build the same table would be read with `EVAL UNDER VALID TIME` or `RULES EFFECTIVE DATE` for the conduct day and the rule-version axis for the reading day; build 98 of `main` rejects those, so both days are plain inputs.

| version | takes effect | published |
| --- | --- | --- |
| Revised Edition 2003 | 31 July 2003 | 31 July 2003 |
| Revised Edition 2012 | 31 August 2012 | 31 August 2012 |
| S 549/2012 (deemed) | 1 January 2011 | 31 October 2012 |
| consolidation in force from 25 September 2024 | 25 September 2024 | 25 September 2024 (the day it says it is in force from; its own publication day is not shown) |

The table holds every version I could source.
A conduct day or reading day before 31 July 2003, or a reading day after 4 November 2026 (the day the sources were last checked; assumed, not ruled, one line in `sgba-vintage.l4`), answers "not covered".
A reading day from 2 October to 4 November 2026 is answered from the latest text deposited. On 4 November 2026 the orchestrating session searched the e-Gazette index (first page of each of two searches) and read the three results that name the Act; none amends a provision of the Broadcasting Act (detail in sgba-vintage.l4). That is what a first-page index search and three readings show; it is not a finding that nothing exists.
A conduct day later than the reading day is not rejected: the day of the conduct is whatever the person types.
S 549/2012 is retrospective: it is "deemed to have come into operation on 1st January 2011" although first published on 31 October 2012.
Whether such a notification is valid, and what a court would do with conduct already past, is not addressed; the encoding takes the notification's deeming as the text states it.
The 5.00 pm of the publication is not kept, because the reading day is a date.

## The answers, by date

Reading A of s 2(1): "specified in the First Schedule" qualifies the whole of "capable of or designed or constructed for the reception of any broadcasting service".
"Television" is a broadcast television receiver (used for the visual and aural reception of a broadcasting service); "FM radio" and "AM radio" are broadcast sound receivers (used for the aural reception of a broadcasting service; no version of the Schedule, and no text I have, distinguishes the band); "satellite dish" is a TVRO system.
`sgba-tests-versions.l4` asserts the table's selection and `sgba-tv-cases-seat.l4` asserts each cell, kind by kind.

| conduct day | read as at | television | FM radio | AM radio | satellite dish |
| --- | --- | --- | --- | --- | --- |
| before 31 July 2003 | any | not covered | not covered | not covered | not covered |
| 31 July 2003 to 31 December 2010 | 31 July 2003 to 4 November 2026 | broadcasting apparatus (item 1) | broadcasting apparatus (item 2) | broadcasting apparatus (item 2) | broadcasting apparatus (item 3) |
| 1 January 2011 onward | 31 July 2003 to 30 October 2012 | broadcasting apparatus | broadcasting apparatus | broadcasting apparatus | broadcasting apparatus |
| 1 January 2011 onward | 31 October 2012 to 4 November 2026 | not broadcasting apparatus | not broadcasting apparatus | not broadcasting apparatus | broadcasting apparatus (item 1) |
| any | after 4 November 2026 | not covered | not covered | not covered | not covered |

Conduct before 1 January 2011 (row 2) gets the same answer on every reading day, because S 549/2012 is deemed from 1 January 2011 and so never applies to earlier conduct; conduct from that day (rows 3 and 4) gets one answer or the other according to the reading day.

What the Television and Radio Licensing Regulations (Rg 1) say, by the same two days, for a person who operates the equipment where it is named and has no licence (`sgba-tests-rg1.l4`, and section 3A of `sgba-tv-cases-seat.l4`).
"Says a licence is needed" means a regulation of the text read states it; it is not a finding that the Act required one (F-BA-12).

| conduct day | read as at | television at home | television in a car | radio at home (FM or AM) | radio in a car (FM or AM) |
| --- | --- | --- | --- | --- | --- |
| before 29 February 2004 | any | not covered | not covered | not covered | not covered |
| 29 February 2004 to 20 June 2004 | from 29 February 2004 | says so (reg 27(1)) | says so (reg 28(2)) | says nothing | says so (reg 23(1)) |
| 21 June 2004 to 31 December 2010 | from 15 June 2004 | says nothing (27(1) replaced) | says so (reg 28(2)) | says nothing | says nothing (reg 23(2) names vessels) |
| 21 June 2004 to 31 December 2010 | 29 February to 14 June 2004 | says so (reg 27(1)) | says so | says nothing | says so (reg 23(1)) |
| 1 January 2011 onward | 15 June 2004 to 30 October 2012 | says nothing | says so (reg 28(2)) | says nothing | says nothing |
| 1 January 2011 onward | 31 October 2012 to 4 November 2026 | Regulations revoked: says nothing | revoked | revoked | revoked |
| any | after 4 November 2026 | not covered | not covered | not covered | not covered |

In a commercial property reg 29A(1) (21 June 2004 onward, until the revocation as read) says a separate licence is required for every television receiver installed there; "installed" is a word the Regulations use for fixing, and reg 28(5) deems a receiver installed in a vehicle if fixed by brackets or other mountings.
"Says nothing" for a radio at home means no regulation states a requirement in terms; it is not a statement that none applied, and it is not a statement about the Act: several regulations presuppose a general sound receiver licence (see "Household radios" below, F-BA-12).
"Broadcasting apparatus" means s 20(1) applies to installing it, importing or selling it, and operating it or having it on premises one owns or occupies where services are received on it; unless licensed or exempt, s 47 makes that an offence.
"Not broadcasting apparatus" means s 20(1) and s 47 have nothing to attach to on reading A.

### (1) Before the receiver licence ended

On the Gazette texts, from the Revised Edition 2003 (31 July 2003) until 31 December 2010 the First Schedule listed television receivers and sound receivers.
So s 20(1)(c) required a licence for a person who operated, or had on premises in Singapore that they owned or occupied, a television or radio receiver on which broadcasting services were received, unless exempted; s 47 made the contravention an offence ($40,000, or 3 years, or both, with forfeiture of the apparatus).
The same holds for conduct from 1 January 2011 as the law could be read until 30 October 2012: the Revised Edition 2012, published 31 August 2012, still listed the receivers.
The end date is therefore 1 January 2011 as S 549/2012 deems it, and 31 October 2012 as a reader could see it.
I found no s 20(4) exemption and no s 60(b) order covering receivers (see the search below).
The Regulations that set the licences say what that meant for a person.
Under Rg 1 as the Revised Edition printed it (29 February 2004 to 20 June 2004), reg 27(1) said in terms that "No person shall operate a broadcast television receiver without a licence", and reg 23(1) required a licence for a broadcast sound receiver installed in a vehicle or in a vessel without a ship station licence.
Regs 24 and 29 excused temporary use in a public place or at an official, social or charitable function.
From 21 June 2004, as S 333/2004 amended them, reg 27(1) no longer carried that sentence (it says where an application is made), reg 23(2) required a licence only for a sound receiver in a vessel, and reg 29A required a separate licence for every television receiver installed in a commercial property; regs 27(3) and (4), 28(2) and the First Schedule's fees ($40 and $110 a year for a television receiver, $27 for 12 months for a sound receiver) stayed.
What the BA sources do not say: anything before 29 February 2004 about Rg 1 or before 31 July 2003 about the Act (no earlier text was obtained); whether and how the Authority issued or waived licences for receivers (reg 8 gives it a discretion to waive or reduce the fee for a blind person, a deaf person, a Government use or other reasonable circumstances); and what licence, if any, was carried over from before 1 January 2003 by s 68 (below).

### (2) Between the end date and 2019

For conduct on or after 1 January 2011, a reader on or after 31 October 2012 finds a First Schedule listing only the TVRO system (S 549/2012, deemed from 1 January 2011), and the 2024 consolidation's First Schedule is the same.
So on reading A, television and radio receivers are not broadcasting apparatus for any conduct from 1 January 2011, as that law is read from 31 October 2012.
Between 1 January 2011 and 30 October 2012 a reader of the published text still found receivers listed, and still found the Television and Radio Licensing Regulations in force as S 333/2004 amended them: the encoding returns both answers, by reading day, and does not choose between them.
The Regulations went the same way and on the same dates as the Schedule: S 548/2012 revoked them, deemed from 1 January 2011 and published at the same hour as S 549/2012 on 31 October 2012, with reg 2(2) keeping them alive for licences for periods, receivers' matters and licensees' duties before 1 January 2011 and reg 2(3) refunding in full any fee paid in advance for a period commencing on or after 1 January 2011.
So for conduct from 1 January 2011, read from 31 October 2012, neither the Act's First Schedule nor any Regulation lists, licenses or prices a broadcast receiver; read before 31 October 2012, both still do.
The claim that the licensing step was "missed" is a claim about why S 548/2012 and S 549/2012 were made retrospectively and published on the same day, which the Gazette texts do not give; what they show is that both were made on 30 October 2012 and published on 31 October 2012 at 5.00 pm.
The 2024 consolidation's legislative history lists no later notification amending the First Schedule, but it does not name sections; the claim that nothing amended the Schedule again between 2012 and 2024 rests on that list and on the identity of the 2012 substituted text and the 2024 text.

### (3) Today (the consolidation as at 2026-10-01)

For conduct today, read today, on reading A, a television set or a radio (FM or AM) is not broadcasting apparatus, so the BA requires no licence for it and creates no offence by having or using it.
A satellite dish with its receiver is listed, so installing it, selling it, or operating it or having it on premises where services are received, without a licence or exemption, is an offence under s 47.
A television with a satellite tuner connected to a dish is, with the dish, within item 1.
Whether any other written law covers a receiver the BA does not is not a BA question.

### A reading that would change every "not broadcasting apparatus" cell: F-BA-01

The answer depends on reading "specified in the First Schedule" in s 2(1) as qualifying the whole of "capable of or designed or constructed for the reception of any broadcasting service" (reading A).
Reading B attaches it only to "designed or constructed for", so that equipment capable of reception would be broadcasting apparatus whether or not listed (NOTES.md, F-BA-01).
`sgba-versions.l4` encodes both readings; `sgba-tv-seat.l4` answers the question on each; `sgba-tv-cases-seat.l4` asserts both.
On reading B every cell of the table is "broadcasting apparatus" wherever the equipment can receive a broadcasting service and a version exists, so a television or radio would be within s 20(1)(c) today unless licensed or exempt.
The Gazette texts bear on which reading the Act itself uses: the 2003 and 2012 First Schedules list "Broadcast television receiver" and "Broadcast sound receiver" as items.
On reading B those items would add nothing for equipment capable of reception, since a receiver is by definition capable of reception; listing receivers by name does work on reading A, where listing is the gate.
That is an argument from the text and I take reading A on it; it does not rule B out, and I cite no court or regulator for either reading.

### A reading that would change the answer for equipment used away from the person's own premises: F-BA-03

Section 20(1)(c) forbids anyone to "operate or have on any premises in Singapore owned or occupied by the person broadcasting apparatus on or by which broadcasting services are received" (2024 consolidation, lines 1434-1436).
Reading A, which the encoding takes as its default, reads "on any premises in Singapore owned or occupied by the person" as qualifying both "operate" and "have".
Reading B reads it as qualifying only "have", so that "operate" reaches a place the person neither owns nor occupies.
`sgba-p5-apparatus.l4` and `sgba-versions.l4` encode both, the premises phrase being asked as three facts (the person operates it; the person has it; the place is premises in Singapore that the person owns or occupies); `sgba-tv-seat.l4` answers question 2 on reading A and its next question on reading B; `sgba-tv-cases-seat.l4`, section 5, asserts both.
Nothing in the tables above changes on reading A.
On reading B, with reading A of s 2(1), a person who operates, away from their own premises, a receiver that is listed on the reading day, with services received on it, no licence and no exemption, contravenes s 20(1)(c):
- for conduct from 31 July 2003 to 31 December 2010, a television set or a radio (items 1 and 2 of the First Schedule), on every reading day up to 4 November 2026; and for conduct from 1 January 2011, a television set or a radio read from 31 July 2003 to 30 October 2012;
- a satellite dish (item 3, then item 1) for conduct from 31 July 2003, today included;
- not a television set or a radio for conduct from 1 January 2011 read from 31 October 2012, nor today.
The suggested argument for reading B is that Rg 1 reg 24 and reg 29 say "A licence shall not be required for the temporary use of a broadcast sound receiver [television receiver] in a public place or at an official or social function or a function organised for charitable purposes" (`BA1994-RG1.txt:460-462`, `521-523`), an exemption that would be needed only if operating a receiver reaches places the person does not own or occupy.
Against that, reg 27(1) of the Revised Edition 2004, until S 333/2004 replaced it, said "No person shall operate a broadcast television receiver without a licence" (`BA1994-RG1.txt:481-482`) with no limit to premises, so reg 29 has work to do under the Regulations' own requirement without s 20(1)(c) reaching public places; for sound receivers that reply is weaker, because reg 23 names only vehicles and vessels.
The words "operate or have on any premises ... owned or occupied by the person" also read naturally with the premises phrase after both verbs.
I keep reading A as the default on that balance; the balance is close, the text does not settle it, and I cite no court or regulator.
Whether reg 24 or reg 29 is an exemption under s 20(4) for the purposes of the Act is not decided here: the seat asks it as a fact.

## Radios, FM and AM: the explicit question, (a) to (c)

**(a) "Broadcast sound receiver" in the First Schedule: answered.**
Item 2 of the First Schedule in the Revised Edition 2003 (line 2141) and in the Revised Edition 2012 (line 2168) is "Broadcast sound receiver", defined as "any apparatus used for the aural reception of any broadcasting service" (lines 2146-2147 and 2171-2172).
S 549/2012 deleted the First Schedule and substituted one listing only the TVRO system, deemed from 1 January 2011, so the sound receiver went out with the television receiver.
The 2003 and 2012 Schedules are identical, which is the evidence that nothing changed it between the editions.
Between the editions, the instruments I read do not touch the First Schedule: Act 55 of 2004 (Broadcasting (Amendment) Act 2004) touches only sections 48 and 48A; Act 10 of 2005 (Telecommunications (Amendment) Act 2005) touches only section 26 of the Broadcasting Act; S 559/2010 amends the Third Schedule only.
The 2012 edition's legislative history lists two more between the editions, which I have now read in the Gazette on 2026-11-04: Act 21 of 2005 (Companies (Amendment) Act 2005) touches only section 35(3), and Act 15 of 2010 (Criminal Procedure Code 2010) touches only section 55 (the authorisation of the Public Prosecutor, from 2 January 2011).
None of the five touches the First Schedule, s 2(1), s 20 or s 47; s 55 is the section that says who may conduct proceedings for an offence under the Act, and its wording changed on 2 January 2011 (F-BA-13 in NOTES.md); the seat answers nothing about it.
The words "FM", "AM", "VHF", "UHF", "medium wave", "frequency modulation" and "amplitude" appear in no edition of the Act and in no deposited instrument, Rg 1 included: both the Act's definition ("any apparatus used for the aural reception of any broadcasting service") and the Regulations' ("of broadcast matter transmitted by radio waves, wire or cable") are by use for aural reception, so on the text FM and AM radios are treated alike.
On the Regulations: reg 23 says in terms that a licence is required only for a sound receiver installed in a vehicle or vessel (as the Edition printed it) and in a vessel (as S 333/2004 amended it); reg 27(3) says a television licence permits one or more sound receivers at the licensed address; yet several regulations speak of a sound receiver licence without that limit.
Whether a household radio needed a licence of its own is the fork F-BA-12, written up in "Household radios: did a radio at home need its own licence?" below; the texts do not settle it.

**(b) Each pair of days, and any exemption: answered, with a limit.**
The table above gives, for radios as for television sets and satellite dishes, whether each is "broadcasting apparatus" for each pair of days (reading A).
Mechanical search of every deposited instrument and edition for "receiver", "sound", "radio", "television", "apparatus", "licence fee", "vehicle" and "car" (whole words, case-insensitive; the counts are in NOTES.md, "Search for receivers") found these in the instruments:
- "receiver": only in the TVRO System Regulations (reg 2's definition of "broadcast television receiver"; reg 10, a TVRO licensee's diagram of receivers connected to the system; reg 13(2), a change in the number of such receivers), never as something that needs a licence of its own.
- "radio": once, in S 523/2010 para 4(c)(i), the services of an educational institution's closed network.
- "television": S 549/2012 and S 559/2010 (a Schedule), O 1 (close circuit television surveillance services), S 523/2010, S 477/2020 and the TVRO Regulations.
- "licence fee": once, the heading above reg 4 of the TVRO Regulations.

No exemption order, class licence or licence-exemption provision in any deposited instrument covers a television set, a radio or a satellite dish as receiving equipment; the exemptions found are from ss 8 and 9 (services), s 33, s 43 and Part X (holding companies, funds and ownership).
Under the Act itself the only exemptions that could reach a receiver are s 20(3) (four uniformed services in the course of duty), s 20(4) (an Authority exemption of any person, apparatus or class) and s 60(b) (a Minister's order); I found none exercised in any source.
The limit: the Authority's exemptions under s 20(4) are not published in anything I have, so "none found" is a statement about my sources.

**(c) A receiver in a vehicle: answered from the text, with a limit.**
Section 20(1)(a) reaches installing broadcasting apparatus "on board any ship, aircraft or vehicle registered in Singapore", in all three editions (the word "vehicle" appears once in each), so a receiver fixed in a Singapore-registered vehicle was within (a) while receivers were listed, in addition to (c) for premises, and it is outside s 20(1) wherever receivers are not listed (reading A).
The Television and Radio Licensing Regulations treat the vehicle expressly, and the Gazette texts show how that changed:
- Rg 1 as the Revised Edition 2004 printed it (29 February 2004 to 20 June 2004): reg 23(1) "A licence shall be required for every broadcast sound receiver installed in a vehicle or in a vessel in respect of which a ship station licence has not been granted"; reg 23(5) deems a receiver installed in a vehicle if affixed by brackets or other mountings, temporarily or permanently, "other than one which is merely carried"; reg 28(2) a separate licence for every television receiver installed in a vehicle or vessel; fee, First Schedule item 2, "$27 for 12 months" for a sound receiver licence (reg 5(3): a vehicle sound receiver licence runs from its issue).
- As amended by S 333/2004 (21 June 2004 to 31 December 2010, and for conduct from 1 January 2011 read before 31 October 2012): reg 23(2) "A licence shall be required for every broadcast sound receiver in a vessel in respect of which a ship station licence has not been granted"; the vehicle is gone from the sound receiver requirement, the "merely carried" exception to reg 23(5) is deleted, and reg 28(2) for a television receiver in a vehicle is unchanged.
- Revoked by S 548/2012 (conduct from 1 January 2011, read from 31 October 2012): none of these regulations is in force.
- No provision names a car, a car radio, an FM radio or an AM radio; a car radio is a "broadcast sound receiver installed in a vehicle".
In the Act, s 20(1)(a) separately forbids installing broadcasting apparatus on board a vehicle registered in Singapore except under a licence, while the First Schedule listed sound receivers; the Regulations as amended no longer say in terms that a vehicle sound receiver needs one, but they keep provisions that presuppose such a licence (see "Was a vehicle sound receiver licensed after 21 June 2004?" below).
`sgba-tv-cases-seat.l4`, section 3A, asserts each cell for "FM radio" and "AM radio" in "a car or other road vehicle".
No other fee, rule or exemption for a car radio is in the BA or its instruments: "vehicle" appears in the other instruments only in S 477/2020 (digital display panels in public passenger transport vehicles, not receivers), and "car" only there ("Taxi or chauffeured private hire car").

Answered: (a) and (b) from the BA texts for the periods the Gazette covers, and (c) from the text; unanswered: anything before 31 July 2003, the Authority's licensing practice and fees, and the SSO cross-check.

## Household radios: did a radio at home need its own licence? (F-BA-12)

The question, put by the Telecommunications Act encoder (message of 2026-11-03 18:07 UTC) and relayed by the orchestrating session: Rg 1 says in terms that a licence is required for a sound receiver only in a vehicle or vessel (reg 23(1)), yet its First Schedule prices "a broadcast sound receiver" and reg 27(3) lets a television licence cover the household's sound receivers.
Did a household radio need its own licence under s 20(1)(c) of the Act and Rg 1, or only a radio in a vehicle or vessel, or only a radio not covered by a television licence?
Answered from the Gazette text, on the same three dates and the two time axes; the texts do not settle it, and the readings are set out below as a fork.

### The text

Rg 1, Revised Edition 2004 (`BA1994-RG1.txt`):
- Reg 23(1) (lines 441-444): "A licence shall be required for every broadcast sound receiver installed in a vehicle or in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act (Cap. 323)."
  The only regulation that says in terms that "a licence shall be required" for a sound receiver; its heading reads "Broadcast sound receivers for vehicles or vessels".
- Reg 24 (lines 460-462): "A licence shall not be required for the temporary use of a broadcast sound receiver in a public place or at an official or social function or a function organised for charitable purposes."
  The exemption is not limited to a vehicle or vessel.
- Reg 25 (lines 465-467): "The combined height and length of an external aerial for a fixed broadcast sound receiver shall not, except with the written consent of the licensing authority, exceed 30 metres."
- Reg 26 (lines 470-472): "A licensee shall, if so required by the licensing authority, cease to operate a broadcast sound receiver for any period specified by the licensing authority."
- Reg 2(2)(b) (line 170): "regulations 23 to 26 — licence for broadcast sound receivers".
- Reg 27(3) (lines 485-488): a licence "shall permit the use of one or more broadcast television receivers and one or more broadcast sound receivers by the licensee, members of his family and domestic servants resident at the address specified therein".
- Reg 8 (lines 276-289): the Authority may "waive or reduce the payment of the fee payable for a licence for any broadcast sound receiver or any broadcast television receiver ... (b) to a blind person for operating a broadcast sound receiver".
- Reg 5(2) and (3) (lines 215-223): a licence "(other than a licence for a broadcast sound receiver installed in a vehicle)" is valid from the first day of the month of issue; "A licence for a broadcast sound receiver installed in a vehicle" is valid from the date of issue.
- First Schedule, item 2 (line 629): "Licence for a broadcast sound receiver ... $27 for 12 months."
  Second Schedule, item 1 (lines 657-660): a late payment fee of $10 "for the grant or renewal of a broadcast sound receiver licence".
- Reg 7 (lines 264-273) names "section 20(1) of the Act or ... regulation 17, 27 or 36" as the contraventions for which a renewal does not prejudice a prosecution; it does not name reg 23.

The Act: s 20(1)(c) (2003 edition lines 706-710; 2012 edition 689-691; 2024 consolidation 1425-1439, where it reads "a person must not") forbids anyone to "operate or have on any premises in Singapore owned or occupied by him broadcasting apparatus on or by which broadcasting services are received" except under a licence granted under s 20; s 20(2) leaves the form, period, terms and conditions of a licence to the Authority.
The First Schedule listed "2. Broadcast sound receiver" in the Revised Editions 2003 and 2012, and S 549/2012 deleted it with effect deemed from 1 January 2011 (published 31 October 2012).

S 333/2004, from 21 June 2004 (published 15 June 2004), replaced reg 23(1) and (2) (lines 127-133 of `BA1994-S333-2004.txt`):
"(1) An application for a licence to install or operate a broadcast sound receiver may be made at any post office or at such other places as the Authority may require.
(2) A licence shall be required for every broadcast sound receiver in a vessel in respect of which a ship station licence has not been granted under the Telecommunications Act (Cap. 323)."
The new reg 23(1) is not limited to a vehicle or vessel; the new reg 23(2) names a vessel only.
Regs 5(2) and (3) were deleted and replaced by a single paragraph (S 333/2004 para 4(a)), so the vehicle-specific validity rule went; reg 8 was amended to cover the fee for any licence (S 333/2004 para 7 deletes "for any broadcast sound receiver or any broadcast television receiver"; (b), "to a blind person for operating a broadcast sound receiver", stays); regs 10(2), 24, 25, 26 and 27(3) were left as printed except for the renaming of "licensing authority" to "Authority"; the First Schedule item 2 was left as printed.
S 548/2012 (published 31 October 2012, deemed from 1 January 2011) speaks of "every licence granted under section 20(1) of the Act, in respect of any broadcast television receiver or broadcast sound receiver" (reg 2(2)(a)) and of "any fee for the grant or renewal of a licence ... paid in advance under regulation 5 of the revoked Regulations" (reg 2(3)), with no limit to a vehicle or vessel.

### The readings

- **Reading X: every sound receiver needed a licence.**
  The Regulations treat a sound receiver licence as a general class: a price for it (First Schedule item 2), a late fee (Second Schedule item 1), a fee waiver for a blind person "operating" one (reg 8(b)), an exemption for temporary use in a public place or at a function (reg 24), a rule about the aerial of a "fixed" receiver (reg 25), a duty to cease operating (reg 26), the type label "licence for broadcast sound receivers" over regs 23 to 26 (reg 2(2)(b)), and, from 21 June 2004, an application for a licence "to install or operate a broadcast sound receiver" without limit (reg 23(1) as amended); S 548/2012 itself speaks of licences "in respect of any ... broadcast sound receiver".
  The Act's s 20(1)(c) supplies the prohibition for premises, and reg 23(1) states the requirement expressly for a vehicle or vessel because they get a special rule (reg 5(2) and (3)).
  Reg 27(3) would be needed to say a television licence also covers the household's sound receivers.
- **Reading Y: only a sound receiver in a vehicle or vessel needed a licence under Rg 1.**
  Reg 23(1) is the only regulation that says in terms "a licence shall be required" for a sound receiver, and its heading limits it to vehicles and vessels; for a television receiver reg 27(1) states a prohibition without that limit, and no parallel prohibition exists for a sound receiver kept on premises; reg 7 names regs 17, 27 and 36 and not reg 23.
  On Y, the Act's s 20(1)(c) either did not bite on a home radio (the Authority having determined under s 20(2) that no licence was required) or bit with no licence available under the Regulations; the texts do not say which.
- **Reading Z: a home radio needed a licence only if no television licence covered it.**
  The same as X for a household with no television licence; reg 27(3) supplies the cover when there is one.

I take none of the three.
The encoding says what each regulation says (NOTES.md, F-BA-12, a pointer to this section) and `sgba-tv-seat.l4` answers "Yes." to "Did the Television and Radio Licensing Regulations say I needed a licence?" only where a regulation states the requirement in terms (reg 27(1) as printed, reg 23(1) as printed, reg 23(2) as amended, reg 28(2), reg 29A), and "No." otherwise, which for a radio at home is Y's data and says nothing about whether the Act or the Regulations, read as X, required one.

### The three dates

For a household radio, conduct and reading days as in the table above:

| conduct day | read as at | X | Y | Z |
| --- | --- | --- | --- | --- |
| before 31 July 2003 (Act) and before 29 February 2004 (Rg 1) | any | not covered | not covered | not covered |
| 29 February 2004 to 20 June 2004 | from 29 February 2004 | licence needed ($27 for 12 months, item 2) | no regulation requires one; reg 23(1) names vehicle and vessel | needed unless a television licence covers it (reg 27(3)) |
| 21 June 2004 to 31 December 2010 (date 1: before the end) | from 15 June 2004 | licence needed; reg 23(1) as amended speaks of a licence "to install or operate a broadcast sound receiver" | no regulation requires one; reg 23(2) names a vessel only | needed unless a television licence covers it |
| 1 January 2011 to 30 October 2012 read (date 2, as a reader then saw it) | 15 June 2004 to 30 October 2012 | as the row above | as the row above | as the row above |
| 1 January 2011 onward, read from 31 October 2012 (date 2, as read now) | 31 October 2012 to 4 November 2026 | Regulations revoked; the First Schedule no longer lists sound receivers: no requirement | the same | the same |
| today (date 3) | read today | no requirement under the Regulations (revoked) or the First Schedule (no sound receiver, reading A of s 2(1)) | the same | the same |

On reading B of s 2(1) (F-BA-01) the last two rows would differ for the Act, but the Regulations are revoked in both.

### Was a vehicle sound receiver licensed after 21 June 2004?

Confirmed against the deposit: S 333/2004 para 11(a) (lines 123-133) substitutes reg 23(1) and (2); the new reg 23(2) names "a vessel" only, and "a vehicle" is gone from the requirement.
A television receiver in a vehicle or vessel keeps reg 28(2): S 333/2004 para 13 amends only reg 28(1) and (5).
So the Regulations no longer say in terms, after 21 June 2004, that a sound receiver installed in a vehicle needs a licence.
Four texts still presuppose such a licence: reg 10(2), which S 333/2004 did not amend, deems a licence "in respect of a broadcast sound receiver installed in the vehicle" transferred with the vehicle's registration; reg 23(5), amended only to delete the "merely carried" exception, still speaks of a receiver "installed" in a "vehicle or vessel"; reg 23(1) as amended invites an application for a licence "to install or operate a broadcast sound receiver"; and the First Schedule fee for "a broadcast sound receiver" was not touched.
In the Act, s 20(1)(a) forbade installing broadcasting apparatus on board a vehicle registered in Singapore except under a licence while the First Schedule listed sound receivers (to 31 December 2010, or until 31 October 2012 as read before that day).
So after 21 June 2004: the Regulations stopped requiring a vehicle sound receiver licence in terms; they continued to presuppose one (reg 10(2), reg 23(5), reg 23(1)); the Act's own prohibition for installing apparatus in a vehicle continued while sound receivers were listed.
Whether a car radio was therefore licensed after 21 June 2004 is the same fork as for a home radio, and I do not decide it.

## The instrument that covers or fails to cover the person, and when it began

For the BA side, no instrument covers a television or radio receiver as such: neither the exemption orders and class licences I deposited (O 1, O 2, O 3, S 121/2008, S 211/2022, S 523/2010, N 1, S 477/2020) nor the TVRO and Composition Regulations exempt anyone from s 20(1) for a receiver.
What takes receivers out of s 20(1) for conduct from 1 January 2011, on reading A, is the change to the First Schedule by S 549/2012, deemed from 1 January 2011 and first published on 31 October 2012, made under s 65(1); and what takes them out of the Regulations that licensed them is S 548/2012, deemed from 1 January 2011 and first published at the same hour on the same day, made under s 66.
Before that, the one instrument that covered a person's receiver was the licence regime itself (Rg 1): reg 27(1) for a television receiver until 20 June 2004, and regs 23(1) and 28(2) for a vehicle or vessel.

## The savings provision, section 68

Section 68 (BA1994.txt:4311-4340) is the Act's only savings and transitional provision.
It keeps valid "all acts done by the Singapore Broadcasting Authority before 1 January 2003" until "invalidated, revoked, cancelled or otherwise determined by the Authority" (s 68(1)), and deems "any decision, document, licence, consent, approval or authorisation" made, issued or granted by that Authority under the Singapore Broadcasting Authority Act (Cap. 297, 1995 Revised Edition) before 1 January 2003 to have been made, issued or granted by the Authority, "so far as it is not inconsistent with the provisions of this Act" (s 68(2)).
It does not name a receiver licence.
Whether a television or radio receiver licence was a licence issued by the Singapore Broadcasting Authority under that Act, or was issued by another body under other law, is not shown by any source in hand.
The one pointer is a lawplain hit on the Chit Funds (Advertisements) Regulations, which mention "broadcast television receivers within the meaning of the Singapore Broadcasting Authority (Broadcasting and Television) Regulations", an instrument lawplain does not hold.
The Gazette identifies it: S 212/1999 amends "the Singapore Broadcasting Authority (Broadcasting and Television) Regulations (Rg 1)", and the Revised Edition 2004 of Rg 1, titled "Broadcasting (Television and Radio Licensing) Regulations", lists S 212/99 as its last amendment before the Edition and G.N. S 21/80 as its origin ("[1st February 1980]"); so the instrument the Chit Funds Regulations name is Rg 1 under its title before the Act's name changed, and its text before 29 February 2004 was not obtained.
If a pre-2003 receiver licence was carried across by s 68(2), it continued until determined by the Authority; the section says nothing about 2011 or about any other end date.
`sgba-p12-misc.l4` encodes s 68(1) to (5), and takes "it is a licence made, issued or granted by the Singapore Broadcasting Authority under that Act" as a plain fact.

## Hypotheses

| H | what the BA sources say | status |
| --- | --- | --- |
| H1: a receiver licence obligation existed and ended around 2011 | On the Gazette texts, television and radio receivers were broadcasting apparatus (First Schedule items 1 and 2 in the Revised Editions 2003 and 2012), so s 20(1)(c) required a licence and s 47 made lacking one an offence.<br>S 549/2012 deleted those items, deemed in operation from 1 January 2011, first published 31 October 2012.<br>The Regulations that licensed them (Rg 1) required a licence for a television receiver (reg 27(1), until 20 June 2004) and for a sound receiver in a vehicle or vessel (reg 23), and S 548/2012 revoked Rg 1, deemed from 1 January 2011, published at the same hour on 31 October 2012, with a full refund of any fee paid in advance for a period from 1 January 2011 (reg 2(3)). | answered from the BA side on reading A: the obligation ended on 1 January 2011 as deemed, and on 31 October 2012 as a reader could see it; the Regulations' own requirement for a television receiver had gone from their text on 21 June 2004 (S 333/2004) |
| H2: nothing replaced it, so possession or use of an analogue terrestrial receiver became an offence under the Telecommunications Act | Not a BA question.<br>The BA creates no offence for a receiver that is not "broadcasting apparatus" (s 20(1), s 47), which from the notification's date on reading A includes televisions and radios. | not answered here (TA's); the BA does not supply the offence |
| H3: some instrument covers the person | No deposited BA instrument exempts a receiver; for conduct from 1 January 2011 (read from 31 October 2012) no cover is needed on reading A. | answered for the BA side: none found, none needed from the notification's date |
| H4: low-power FM transmitters being lawful covers FM receivers | Not on the BA path; the First Schedule item was by use for aural reception, not by band. | not answered |
| H5: a technical specification covers digital sets from 2019 | Not on the BA path. | not answered |
| H6: satellite receivers (TVRO) are individually licensed under the Broadcasting Act | Satellite receiving systems are broadcasting apparatus in every version (First Schedule item 3, then item 1) and are licensed under s 20.<br>But the TVRO System Regulations (2004 text) allow a licence to be granted only to an "institution" (reg 3(2)), a body of persons or an undertaking.<br>So the licence is not available to an individual acting alone. | partly confirmed (licensed under s 20) and partly refuted ("individually": an individual acting alone is not within reg 3(2)) |

H6 in more detail.
A person who installs a dish, or operates one or has one on premises they own or occupy where services are received, with no licence and no exemption, contravenes s 20(1) on the deposited text and commits an offence under s 47 (`sgba-tv-cases-seat.l4`, section 2).
On the same text an individual acting alone cannot obtain the licence that would take them out of s 20(1) (reg 3(2); `sgba-tv-cases-seat.l4`, section 3), and the Authority's power under s 20(4) to exempt any person is the only remaining route; I found no exercise of it.
Two points keep this from being settled.
First, "institution" includes "any undertaking": whether an individual who runs an undertaking is an institution is a fork (F-BA-05 in NOTES.md), asked in the seat as a plain fact.
Second, the Regulations served are the 2004 Revised Edition with amendments shown only to 2001; I could not check whether they were amended or revoked afterwards, or whether the Authority licenses individuals as a matter of practice.
The Gazette dates the institution-only rule: S 354/2001 ("Singapore Broadcasting Authority (TVRO System) (Amendment) Regulations 2001", first published 23 July 2001, "shall come into operation on 1st August 2001") substitutes a regulation 3 whose paragraph (2) reads "No person other than an institution may be granted with a licence" (`BA1994-S354-2001.txt`, lines 52-53), the same words as the Revised Edition.
So the rule is in the Gazette text from 1 August 2001; the text of regulation 3 before that day was not obtained, and `sgba-tv-cases-seat.l4` answers "not covered" for a day before it.

## Section 9A of the Interpretation Act

The Interpretation Act's s 9A is encoded in `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/` and cited here, not re-encoded.
On the literal reading, a person who is not an institution and has a satellite receiving system installed or operating on their premises commits an offence that no licence available to them can cure.
`sgba-tv-s9a.l4` computes only a marker for that: the literal answer is an offence and the person has no lawful way to comply.
The marker places the literal reading in the territory s 9A(2)(b)(ii) names, which a court may weigh, and it never changes the literal answer (tested: the literal answer is the same with and without the marker).
I do not say whether the literal result is "manifestly absurd or unreasonable", and I leave the purposive outcome open.
For a television or radio receiver the marker does not arise on reading A for conduct from 1 January 2011 read from 31 October 2012, because the literal reading produces no offence.
For a receiver while it was listed, the BA's own text provided a licence route under s 20(2), so the marker's premise (no lawful way to comply) is not shown on the sources.
The legislative history and the Gazette notice of S 549/2012 are extrinsic material, usable only to confirm the ordinary meaning or, if it is ambiguous or absurd, to find it, and never as the rule; here they are cited for dates only.

## What could not be sourced

- Any text of the Broadcasting Act earlier than the Revised Edition 2003 (31 July 2003): the 1995 and earlier editions.
- Any text of the Television and Radio Licensing Regulations before the Revised Edition of 29 February 2004: the history line names the original G.N. S 21/80 (1 February 1980) and twelve amendments (S 46/83, S 52/83, S 314/83, S 151/87, S 105/88, S 404/90, S 125/91, S 525/93, S 87/95, S 214/95, S 291/96, S 212/99); only S 212/99, which changed reg 8, was fetched.
  The Gazette prints S 212/1999 under the Singapore Broadcasting Authority Act (Cap. 297), as the "Singapore Broadcasting Authority (Broadcasting and Television) (Amendment) Regulations 1999", which is the instrument another Regulation refers to (see section 68 above).
- Any s 20(4) exemption: on 4 November 2026 the orchestrating session searched the e-Gazette index for 'Broadcasting Act section 20(4) exemption' (63 results; the first page was read by title only, nothing was opened) and no title on that page names an exemption under section 20(4).
  That is a first-page title search; it is not a finding that none exists.
  The lawplain search recorded in the coverage table row for s 20(4) exemptions in NOTES.md is the other place looked.
- The consolidated text of the Act as at days between the 2003 and 2012 editions (for example 2010-10-01 or 2011-01-01): only the two Revised Editions and the amending instruments I fetched are in hand.
  SSO's historical versions of those days are the one place such a consolidation exists; the single permitted SSO attempt was made at 03:07:48 Singapore time on 2026-11-04 and answered 403 at robots.txt (a CloudFront "Request blocked" page), so nothing was obtained from SSO (NOTES.md, "The single SSO attempt").
- The Authority's licensing practice for receivers: terms of licences, fees, and any s 20(4) exemption.
- The Schedule to the Class Licence Notification and the Schedule to S 523/2010: not in the text lawplain served.
- Any IMDA licensing page on receivers: IMDA's pages are client-rendered and returned no text.

## How sure I am, in a sentence for each date

- (1) Before the receiver licence ended: on the Gazette texts and reading A, sure that televisions and radios were broadcasting apparatus within s 20(1) from 31 July 2003; I can say nothing before that date.
- (2) Between the end date and 2019: sure of what S 549/2012 and S 548/2012 say and of their dates (each made 30 October 2012, first published 31 October 2012 at 5.00 pm, deemed from 1 January 2011), and that the answer for 2011 depends on the reading day; sure that S 333/2004 took the sentence "No person shall operate a broadcast television receiver without a licence" out of the Regulations from 21 June 2004; the legal effect of a retrospective deeming on conduct already past is not addressed, and neither is whether the Act's s 20(1)(c) still required a licence for a television or a home radio in the years when the Regulations said nothing (F-BA-12).
- (3) Today: on reading A, sure that the BA creates no licence requirement or offence for a television set or a radio; not able to exclude reading B from the text alone, although the First Schedule's listing of receivers by name points to A; moderately sure of H6, because of the 2004 vintage of the TVRO Regulations and the unseen s 20(4) exemptions.
