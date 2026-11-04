# Requests to the lead

## R1, 2026-11-04: Gazette URLs, and three deposits missing from my copy

I cannot guess Gazette URLs (a missing file answers 403), so I ask for the URL of each item below, or a statement that it does not exist or could not be found.
They are listed in the order in which they could change an answer.

1. **Any Telecommunications Act instrument, from 2010 to 2013, that exempts or licenses broadcast receivers** (a Minister's notification under TA s 73, or a class licence under s 5 published in the Gazette), for example a "Telecommunications (Exemption …) Notification" made at or after the end of the receiver licence.
   Nothing deposited, nothing in lawplain (which holds no TA subsidiary legislation) and nothing on IMDA's site names one; if the Gazette's browse pages for 2010-2013 show one, it decides dates 2 and 3.
2. **The current text of N 1** (Telecommunications (Exemption from sections 33, 34(1)(b) and 35) Notification): the 2021 or 2022 Revised Edition of Subsidiary Legislation copy, or every amending notification after S 78/2017.
   IMDA's 12 May 2023 6 GHz decision says IMDA would amend this Notification, so at least one amendment after 2017 is likely and is not deposited.
3. **The current text of the Telecommunications (Radio-communication) Regulations (Rg 5)**: the 2021/2022 Revised Edition copy, or every amendment after S 100/2016 (any new class licence in reg 65 or a new Schedule would matter).
4. **The current text of the Telecommunications (Dealers) Regulations (Rg 6)**: the 2021/2022 Revised Edition copy, or every amendment after S 725/2014 (reg 22, the personal-use rule, is the one that matters).
5. **The Broadcasting (TVRO System) Regulations after 2004**: any amendment or revocation (the deposited text is lawplain's 2004 Revised Edition, whose meta says its later state "is NOT shown"), and the 2021/2022 Revised Edition copy if there is one.
6. Lower priority, for conduct before 31 July 2003: the Broadcasting Act 1995 Revised Edition (Cap. 297, then the Singapore Broadcasting Authority Act) and Rg 1 in its 1990 Edition, to see whether a home sound receiver needed a licence of its own before 2003.

Separately, not a Gazette request: the Broadcasting Act encoding cites three deposits that are not in my copy.
If they exist in the repository, please add them to my copy (or tell me they are deliberately withheld):
- `subjects/sg/singapore-broadcasting-authority-broadcasting-and-television-amendment-regulations-1999/registers/source-bundle/BA1994-S212-1999.txt`
- `subjects/sg/singapore-broadcasting-authority-tvro-system-amendment-regulations-2001/registers/source-bundle/BA1994-S354-2001.txt`
- `subjects/sg/singapore-broadcasting-authority-class-licence-amendment-notification-2001/registers/source-bundle/BA1994-S496-2001.txt`

Steps 3 to 6 do not depend on these answers, except the citation check of the three modules that quote those deposits; I will do them when I resume and fold the Gazette results into MISSED-INSTRUMENTS.md part E.

## R2, 2026-11-04: the encoders' preliminary answers reached my context, so I have stopped

At 2026-11-03T19:53:49Z (03:53 SGT on 4 November), when my context was compacted, the harness attached four files to it that I never opened: my transcript has no Read call for any of them.
They are the reviewer brief, `scratchpad/build-review-view.sh`, a project memory file outside VIEW that tracks this piece of work, and the `WALKTHROUGH.md` of the quarantined unstable row (named as read, its contents not included).
The memory file states both encoders' preliminary answers at each date (2003-2010, 2011 read before and after 31 October 2012, and today), for TV and for radio, with their forks and their check.sh numbers.
I do not give its path here, because its file name names the person who first raised the question.
I cannot tell from my side why the harness attached it; one possibility, not checked, is that it re-attaches files read elsewhere in the same session.

What is not affected:
- `REVIEW.md` section 1 was last written at 2026-11-03T19:39:36Z, fourteen minutes before the attachment; its sha256 now is `c40ec1bbd731cae1fd6f5bdc743d4ff5659c4467fb395184b9b79f0e480dd4bf`.
- Step 2 was finished before it: `MISSED-INSTRUMENTS.md` was last written at 19:50:58Z.

What I did after it, all mechanical:
- ran `srcrefs.py check --strict` over every module that quotes a source (97 modules, 15,530 quote lines, 1,385 locators, 0 problems);
- started both `check.sh` runs in the background;
- printed the decisive-chain `@ref` locators beside their source lines;
- grepped both NOTES.md files for the word `srcrefs`, to learn how each encoder runs it.
I have not opened either fork register, or any other part of either NOTES.md.

The brief says "If you find one that has leaked, tell me and do not read on", so I have stopped.
Options as I see them:
- (a) I carry on with steps 3 to 6, and REVIEW.md and DISAGREEMENTS.md say that steps 4 and 6 were done after I had seen the encoders' preliminary answers, so they are not blind;
- (b) a fresh reviewer does steps 4 and 6, starting from my section 1 and my citation check;
- (c) something else you prefer.
Steps 3 (citation check) and 5 (check.sh) do not depend on the answer, so I can finish those under any option.

## R3, 2026-11-04: an undeposited TA exemption order, listed in the 2010 Subject Index

The 2010 Subject Index to Subsidiary Legislation lists, under "Telecommunications", "equipment, telecommunication": "Telecommunication Authority of Singapore (Exemption in Respect of Specified Equipment) Order (Cap 323, O 3)" (`sources/gazette-SL-index-2010/10rsl_index.txt:9717-9720`).
It is not deposited, neither encoding cites it, and lawplain does not hold it.
Made under the TAS Act, it would continue under TA s 98(2) until revoked, and the index treats it as in force before 1 June 2010.
Its title does not say which equipment it covers, and it could decide dates 2 and 3, so I ask, in this order:
1. its text: the Revised Edition of the Cap 323 subsidiary legislation that prints it as O 3 (2001 or 2002, I expect, but I am not guessing a URL), or the Gazette notification that made it;
2. any instrument that revoked it, and its date;
3. the same Subject Index for any year from 2011 on (2011, 2012 and 2013 matter most, and the latest one there is), so that I can see whether O 3 is still listed after the receiver licence ended.

### Correction to R2 (2026-11-04, after the lead re-checked the transcript)

R2 says the harness attached four files "that I never opened".
That is wrong for one of them: I had read `REVIEWER-BRIEF.md`, my own brief, once, before the compaction.
The other three, `build-review-view.sh`, the memory file and `WALKTHROUGH.md`, I had not opened.
The lead's decision on R2 was option (a): carry on, with the disclosure in `REVIEW.md` ("Independence").

### R3 answered (2026-11-04)

The lead fetched O 3 (1999 Edition) and S 549/1998; I copied both into `sources/` and fetched the 1999 Dealers and Radio-communication Regulations myself.
What they show, and what they do not, is in `MISSED-INSTRUMENTS.md` part E3.

## R4, 2026-11-04: the text of section 30 of the Telecommunication Authority of Singapore Act

Whether O 3 covers broadcast receivers turns on what "section 30 (1) to (5) of the Act" said (`MISSED-INSTRUMENTS.md` E3, branches 1 and 2).
Since writing E3 I found the 1998 amending Bill (B6-1998, clause 6), which shows s 30(1) as an approval provision; this request is now for confirmation, and is low priority.
I could not find it: lawplain lists the Act (`TASA1992`) with no sections, and its copy of Bill 16/1992 stops after clause 2.
In order of usefulness, any one of these would settle it:
1. the Telecommunication Authority of Singapore Act (Cap. 323) in any Revised Edition from 1993 to 1999, or the Act as enacted in 1992 with any amendment of s 30 before 12 November 1998;
2. the explanatory statement of the Telecommunications Bill 1999 (Bill 33/1999), which usually says which section of the repealed Act each clause re-enacts;
3. failing both, anything official that quotes s 30.
A lower-priority completeness item: the main Government Gazette's "Notices under other Acts" series for 2010-2013, which you note carried some TA exemptions, has not been searched for a receiver exemption by anyone.
Nothing else in my review waits on this; if s 30 turns out to be the possession prohibition, `REVIEW.md` §7 says which answers change.
