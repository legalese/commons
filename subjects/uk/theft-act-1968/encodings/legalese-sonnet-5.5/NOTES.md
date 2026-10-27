# Theft Act 1968 (1968 c. 60): encoding `legalese-sonnet-5.5`

STATUS: draft, `not_reviewed`: no domain expert has read this against the text of the Act.
The numbers below are a point-in-time record from `l4` 1.6.98 (`main`, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.

## Method

One Sonnet 5.5 agent working alone from the brief (`BRIEF.md`), from the text in `../../registers/source-bundle/ukpga-1968-60.txt` (a plain-text rendering made by a converter script from legislation.gov.uk, version 2013-05-28; it is not the official text and nothing here is "verified against the official text").
Target dialect: `main`, stable `l4` 1.6.98.
The source is a converter's plain-text rendering of the revised text.
It carries dots where the converter shows a provision as repealed or removed, and some sentences have dots inside them (see Findings 2).
Every quotation in the `.l4` files is a line of that rendering, copied by `srcrefs.py quote` and checked by `srcrefs.py check --refs --strict`.
The case files and the seat are written from compact templates by a script that is not part of this deposit; the `.l4` files here are the artefacts, and they are what `check.sh` runs.
Every expected value in a case file was written by hand from the section named beside it, before the run, and not read back from the encoding.
Nothing here predicts what a court would find, and nothing here is advice to a person charged.

## Seat

A person who may be accused of an offence under the Theft Act 1968.
They ask what the Act makes of what they did, or are said to have done, and the most that can follow.
There is no seat for the police, a prosecutor, a justice or a court.
Provisions that only empower or direct an official are therefore either encoded for what they mean to the person (a warrant to search their premises, whether evidence of earlier dealings can be used against them, whether a step can be taken against them without the Director's consent) or entered as inert in the coverage table.

`theft-seat.l4` has 78 exported questions in the Act's order, under `§§` headings.
Each has `@export` and `@desc`, takes plain inputs (yes or no, numbers, dates and the modules' own choices) with an `@desc` worded as the person would be asked, builds the fact records in its `WHERE`, and calls the layer 1 rule.
A record field that the rule called never reads is given a fixed placeholder with a comment saying so.
Which fields those are is computed from the layer 1 rules, not written by hand: a field is unread for a question only when no rule reachable from the one it calls mentions it.
Every offence with a penalty has a second question beside the first, "what is the most that can follow if I am convicted of ...", which returns an `Outcome of a charge`: no offence on the facts, an offence with the penalty the section itself states, or an offence for which the text states no penalty.
`theft-cases-seat.l4` asserts 371 results, every question with at least two different expected results except the two constant dates.

The questions, by section:

- s 1 to s 6: guilty of theft; dishonest (s 2); appropriated (s 3); property that can be stolen (s 4); belongs to another (s 5); intended to deprive permanently (s 6).
- s 7 to s 14: the penalty for theft; robbery and its penalty; burglary and its penalty; aggravated burglary and its penalty; removal of articles and its penalty; taking a conveyance and its penalty; the s 12(4) alternative verdict and what follows; the s 12(4A) time limit; pedal cycles and the penalty; aggravated vehicle-taking, its penalty, the s 12A(5) alternative verdict and what follows (s 12A(6)); abstracting electricity and its penalty; the s 14 mail offence and what follows.
- s 17 to s 21: false accounting and its penalty; guilty as an officer (s 18) and its penalty; a false statement by an officer (s 19) and its penalty; suppressing a document and its penalty; whether a document is a valuable security (s 20(3)); blackmail and its penalty; whether the demand is unwarranted (s 21(1)).
- s 22 to s 25: handling and its penalty; advertising a reward and its penalty; whether goods are stolen goods (s 24); retaining a wrongful credit and its penalty; going equipped and its penalty; whether there is evidence of use (s 25(3)).
- s 26 to s 36: a warrant to search; entering and searching; seizing; being tried with others (s 27(1)); the jury's finding (s 27(2)); evidence of other dealings or convictions (s 27(3)); a statutory declaration (s 27(4)); summary trial (s 29(2)); a spouse's right to prosecute and to give evidence (s 30(2)); whether a step can be taken without the Director's consent (s 30(4)); the four questions on civil proceedings (s 31); whether the old offence is abolished (s 32(1)); when the Act came into force, when it was passed, whether it applies to what was done (s 35(1)) and whether s 27 applies to a pre-commencement offence (s 35(2)); where the Act extends (s 36(3)).
- Schedule 1: taking or destroying fish and its penalty; forfeiture; arrest; seizure.

Not asked, by design: the s 2 words of state of mind and judgment (dishonesty, reasonable cause, belief) are inputs the person answers, never decided for them.

## Jural relations

The Act is drafted in the language of guilt and liability, not of duty.
"Is guilty of an offence" and "shall be liable on conviction to ..." state a Hohfeldian liability of the accused, with the correlative power of the court to convict and sentence, and a power of the prosecutor to charge.
A duty not to do the act, and the public's claim to its performance, is implicit in every offence and is not encoded (the brief asks for no deontics).
The relation is stated once here and is not repeated in the layer 1 comments.
One row per provision, or per group of subsections that make one relation; a provision that creates no relation is listed once as `none`.
The last column names the layer 1 rules that carry the conditions under which the relation holds.

| Provision | Relation | Holder (right, privilege, power or immunity) | Bearer (duty, no-right, liability or disability) | L4 rule |
|---|---|---|---|---|
| s 1 | none: defines theft (the relation arises under s 7) | - | - | `s 1 guilty of theft` |
| s 2 | none: defines dishonestly | - | - | `s 2 the appropriation is dishonest`, `s 2(1) the appropriation is not to be regarded as dishonest` |
| s 3 | none: defines appropriates | - | - | `s 3 he appropriates, and the appropriation can amount to theft` |
| s 4 | none: defines property | - | - | `s 4 the thing is property that can be stolen` |
| s 5 | none: defines belonging to another | - | - | `s 5 the property belongs to another` |
| s 6 | none: defines the intention of permanently depriving | - | - | `s 6 he intends permanently to deprive the other of it` |
| s 7 | power to convict and sentence (up to seven years on indictment); liability | the court (and the prosecutor's power to charge) | the person guilty of theft | `s 7 liable on conviction on indictment for theft` |
| s 8 | power to convict and sentence (life); liability | the court | the person guilty of robbery or of an assault with intent to rob | `s 8(1) guilty of robbery`, `s 8(2) liable on conviction on indictment for robbery or assault with intent to rob` |
| s 9 | power to convict and sentence (fourteen years for a dwelling, ten otherwise); liability | the court | the person guilty of burglary | `s 9(1) guilty of burglary`, `s 9(3) liable on conviction on indictment for burglary` |
| s 10 | power to convict and sentence (life); liability | the court | the person guilty of aggravated burglary | `s 10(1) guilty of aggravated burglary`, `s 10(2) liable on conviction on indictment for aggravated burglary` |
| s 11(1), (2), (4) | power to convict and sentence (five years); liability | the court | the person who removes an article | `s 11 guilty of removing an article from a place open to the public`, `s 11(4) liable on conviction on indictment for removing an article` |
| s 11(3) | immunity; disability of the court to convict | the person who believes he has lawful authority | the court | `s 11(3) he believes he has lawful authority` |
| s 12(1), (2) | power to convict and sentence on summary conviction (six months, or level 5, or both); liability | the court | the person who takes a conveyance | `s 12(1) guilty of taking a conveyance without authority`, `s 12(2) liable on summary conviction for taking a conveyance without authority` |
| s 12(3) | none: blank in this text | - | - | none |
| s 12(4) | power of the jury to find guilty of the s 12(1) offence on a trial for theft, with the s 12(2) penalty; liability | the jury | the accused | `s 12(4) the jury may find him guilty of taking a conveyance without authority`, `s 12(4) liable as under subsection (2) on a verdict returned on a charge of theft` |
| s 12(4A) | immunity from proceedings begun after three years from the offence or six months from the relevant day; disability of the prosecutor | the accused | the prosecutor | `s 12(4A) the time limit for proceedings` |
| s 12(4B) | none: counting rule (the relevant day) | - | - | `s 12(4B) the relevant day` |
| s 12(4C) | none: rule of proof (a certificate is conclusive); asked through the date the person states | - | - | `s 12(4B) the relevant day` |
| s 12(5) | power to convict and sentence on summary conviction (level 3 fine); liability | the court | the person who takes or rides a pedal cycle | `s 12(5) guilty of taking or riding a pedal cycle without authority`, `s 12(5) liable on summary conviction for taking or riding a pedal cycle without authority` |
| s 12(6) | immunity; disability of the court to convict | the person who believes he has authority or would have the owner's consent | the court | `s 12(6) he did it in the belief that he had authority or the owner's consent` |
| s 12(7) | none: definitions of conveyance and owner | - | - | `s 12(7)(a) it is a conveyance`, `s 12(7)(b) the owner consented` |
| s 12A(1), (2), (4) | power to convict and sentence (two years; fourteen if death); liability | the court | the person guilty of aggravated taking of a vehicle | `s 12A(1) guilty of aggravated taking of a vehicle`, `s 12A(4) liable on conviction on indictment for aggravated taking of a vehicle` |
| s 12A(3) | conditional immunity (if he proves the defence); disability of the court to convict | the accused who proves it | the court | `s 12A(3) he proves one of the two defences for the circumstance` |
| s 12A(5), (6) | power of the court to convict of the basic offence and sentence as a magistrates' court would; liability | the court | the accused | `s 12A(5) he may be convicted of the basic offence`, `s 12A(6) liable as on summary conviction for the basic offence` |
| s 12A(7), (8) | none: definitions of driven dangerously and recovered | - | - | `s 12A(7) driven dangerously` |
| s 13 | power to convict and sentence (five years); liability | the court | the person who dishonestly abstracts electricity | `s 13 guilty of abstracting electricity`, `s 13 liable on conviction on indictment for abstracting electricity` |
| s 14(1) | power of the courts of England and Wales to prosecute, try and punish for what is done outside it; liability (no penalty of its own) | the courts of England and Wales | the person who steals or attempts to steal mail between jurisdictions, or robs in doing so | `s 14(1) guilty of the offence as if he had done it in England or Wales`, `s 14(1) punishable in England and Wales as the offence he committed` |
| s 14(2) | none: names the jurisdictions | - | - | `s 14(2) the jurisdiction is one of the British postal area` |
| ss 15, 15A, 15B, 16 | none: blank in this text | - | - | none |
| s 17(1) | power to convict and sentence (seven years); liability | the court | the person who commits false accounting | `s 17(1) guilty of false accounting`, `s 17(1) liable on conviction on indictment for false accounting` |
| s 17(2) | none: deeming rule (an entry or omission is falsifying) | - | - | `s 17(2) he is treated as falsifying the account or document` |
| s 18 | power to convict and sentence as for the company's offence; liability | the court | the officer who consented or connived, or who purported to act as one | `s 18 guilty as an officer of the offence committed by the body corporate`, `s 18 liable to be punished accordingly` |
| s 19 | power to convict and sentence (seven years); liability | the court | the officer who publishes a false statement | `s 19 guilty of a false statement by an officer`, `s 19(1) liable on conviction on indictment for a false statement by an officer` |
| s 20(1) | power to convict and sentence (seven years); liability | the court | the person who suppresses a document | `s 20(1) guilty of suppressing a document`, `s 20(1) liable on conviction on indictment for suppressing a document` |
| s 20(2) | none: blank in this text | - | - | none |
| s 20(3) | none: definition of valuable security | - | - | `s 20(3) the document is a valuable security` |
| s 21(1), (3) | power to convict and sentence (fourteen years); liability | the court | the blackmailer | `s 21(1) guilty of blackmail`, `s 21(3) liable on conviction on indictment for blackmail` |
| s 21(2) | none: says what is immaterial | - | - | `s 21(1) the demand is unwarranted` |
| s 22 | power to convict and sentence (fourteen years); liability | the court | the handler | `s 22(1) guilty of handling stolen goods`, `s 22(2) liable on conviction on indictment for handling stolen goods` |
| s 23 | power to convict and sentence on summary conviction (level 3 fine); liability | the court | the person who advertises, prints or publishes | `s 23 guilty of advertising a reward with no questions asked`, `s 23 liable on summary conviction for advertising a reward with no questions asked` |
| s 24 | none: defines stolen goods | - | - | `s 24 the goods are stolen goods` |
| s 24A(1), (6) | power to convict and sentence (ten years); liability | the court | the person who dishonestly retains a wrongful credit | `s 24A(1) guilty of dishonestly retaining a wrongful credit`, `s 24A(6) liable on conviction on indictment for retaining a wrongful credit` |
| s 24A(2) to (12) | none: definitions (credit, wrongful, account, business, stolen goods) | - | - | `s 24A(2A) the credit is wrongful at least in part`, `s 24A(9) the account is an account within the section`, `s 24A(10) the business is one within subsection (10)` |
| s 25(1), (2) | power to convict and sentence (three years); liability | the court | the person who goes equipped | `s 25(1) guilty of going equipped`, `s 25(2) liable on conviction on indictment for going equipped` |
| s 25(3) | none: rule of evidence (what counts as evidence of the use) | - | - | `s 25(3) there is evidence that he had the article for such use` |
| s 25(5) | none: treats a s 12(1) offence as theft for this section | - | - | none |
| s 26(1) | power to grant a warrant; liability to be searched | the justice of the peace | the person with the goods in custody, possession or on his premises | `s 26(1) a justice may grant a warrant to search for and seize stolen goods` |
| s 26(3) | privilege and power to enter, search and seize; no-right and liability | the person authorised | the occupier | `s 26(3) he may enter and search the premises`, `s 26(3) he may seize any goods he believes to be stolen goods` |
| s 26(5), s 27(5) | none: construction clauses (follow s 24; corresponding old offences) | - | - | none |
| s 27(1) | power to indict together and try together; liability | the prosecution | the persons charged | `s 27(1) he may be charged in one indictment with others and tried with them` |
| s 27(2) | power of the jury to find guilty whether or not jointly; liability | the jury | the accused | `s 27(2) the jury may find him guilty whether or not he handled the goods jointly` |
| s 27(3) | power to adduce evidence of other dealings and convictions; liability | the prosecution | the accused | `s 27(3)(a) evidence of other recent dealings in stolen goods is admissible`, `s 27(3)(b) evidence of a conviction in the last five years is admissible`, `s 27(3) evidence is admissible to prove he knew or believed the goods to be stolen goods` |
| s 27(4) | power to use a statutory declaration, defeated by the accused's timely notice (the notice is the accused's power; the prosecutor's liability) | the prosecution; the accused | the accused; the prosecution | `s 27(4) the statutory declaration is admissible as evidence of the facts stated` |
| s 27(4A), s 28, s 29(1) | none: blank in this text | - | - | none |
| s 29(2) | none: classifies offences by reference to a Schedule of an Act that is not an input; the accused's consent belongs to that Act | - | - | `s 29(2) paragraph 11 lists the offence as one that may be tried summarily with his consent` |
| s 30(1) | none: equaliser (marriage changes no answer); asserted rather than ruled | - | - | `s 1 guilty of theft` |
| s 30(2) | power of a spouse to bring proceedings as if unmarried, and competence to give evidence for the prosecution; liability | the wife or husband | the accused | `s 30(2) his wife or husband may bring proceedings against him as if they were not married`, `s 30(2) the spouse who brings the proceedings is competent to give evidence for the prosecution` |
| s 30(3) | none: blank in this text | - | - | none |
| s 30(4), (5) | immunity from the step without the Director's consent, except in the provisos; disability of the prosecutor; the Director's power to consent | the accused (immunity); the Director of Public Prosecutions (power) | the prosecutor (disability) | `s 30(4) the step may be taken`, `s 30(4)(a) the subsection does not apply to the proceedings`, `s 30(5) the step is one that subsection (4) applies to` |
| s 31(1), first limb | duty to answer and comply despite the risk of incrimination (the court's and the other party's claim) | the court and the other party to the civil proceedings | the person | `s 31(1) he is not excused from answering the question or complying with the order` |
| s 31(1), second limb | immunity from the use of the answers; disability of the prosecution; the same for the spouse unless married after | the person; the spouse or civil partner | the prosecution | `s 31(1) the statement or admission cannot be given in evidence against him`, `s 31(1) the statement or admission cannot be given in evidence against his spouse or civil partner` |
| s 31(2) | immunity of the title from change by conviction alone; disability of the conviction | the holder of the title | the court and the parties | `s 31(2) the conviction alone does not affect the title to the property` |
| s 32(1) | immunity from the abolished offences for conduct on or after commencement; disability of the prosecutor | the accused | the prosecutor | `s 32(1) the old offence is abolished as regards what he did` |
| s 32(2) | none: construction of other enactments (inert) | - | - | none |
| s 33 | none: amendments and repeals (inert) | - | - | none |
| s 34 | none: interpretation (gain, loss, goods) | - | - | `s 34(2)(a) a view to gain or an intent to cause loss`, `s 34(2)(b) the thing is goods` |
| s 35(1) | none: fixes when the relations above apply (the Act came into force 1 January 1969) | - | - | `s 35(1) the date the Act came into force`, `s 35(1) the Act has effect in relation to an offence` |
| s 35(2) | power to use s 27 for an offence committed before commencement; liability | the prosecution | the accused | `s 35(2) section 27 applies to the offence as it would to a corresponding offence under this Act` |
| s 35(3) | none: preserves old procedural law (inert) | - | - | none |
| s 36(1), (2) | none: the short title; blank in this text | - | - | none |
| s 36(3) | none: extent | - | - | `s 36(3) where the Act extends` |
| Sch 1 para 2(1) | power to convict and sentence on summary conviction (level 5 fine); liability | the court | the person who takes or destroys fish | `Sch 1 para 2(1) guilty of unlawfully taking or destroying fish`, `Sch 1 para 2(1) liable on summary conviction for taking or destroying fish` |
| Sch 1 para 2(3) | power to order forfeiture on conviction; liability of the thing | the court | the person convicted | `Sch 1 para 2(3) the court may order forfeiture of the thing he had with him` |
| Sch 1 para 2(4) | privilege and power to arrest without warrant and to seize; no-right and liability | any person | the person who is, or is reasonably suspected of, taking or destroying fish | `Sch 1 para 2(4) any person may arrest him without warrant`, `Sch 1 para 2(4) any person may seize the thing from him` |
| Sch 1 para 1, para 2(2) | none: blank in this text | - | - | none |
| Sch 2, Sch 3 | none: amendments and repeals of other enactments (inert) | - | - | none |

## Coverage table

Line numbers are lines of `ukpga-1968-60.txt`.
Disposition: `encoded`, `inert`, `repealed or blank in this text`, `not applicable`.
Counts, by whole row: 43 rows; 35 `encoded`, 3 `inert` (s 33, Sch 2, Sch 3), 5 `repealed or blank in this text` (ss 15, 15A, 15B, 16 and 28), 0 `not applicable` as a whole row.
Within rows: s 35 is encoded except for its second half and s 35(3) (inert), and s 36 is encoded except for s 36(1) (not applicable) and s 36(2) (blank); ss 26, 27 and 29 are encoded for what they mean to the accused only.
Blank sub-provisions (shown as dots in this text) are named in the row they sit in and are counted with it.

| Provision | Lines | Heading | Disposition |
|---|---|---|---|
| s 1 | 6-9 | Basic definition of theft | encoded: `s 1 guilty of theft` (theft-s01-06-definition.l4); s 1(2) asserted in theft-cases-s01-06.l4; s 1(3) is the reach of ss 2 to 6, kept by structure (fork 1) |
| s 2 | 10-15 | "Dishonestly" | encoded: `s 2 the appropriation is dishonest`, `s 2(1) ...`; s 2(2) asserted (changes no answer) |
| s 3 | 16-18 | "Appropriates" | encoded: `s 3 he appropriates, and the appropriation can amount to theft` with `s 3(1)`, `s 3(2)` |
| s 4 | 19-28 | "Property" | encoded: `s 4 the thing is property that can be stolen` with `s 4(2)`(a)(b)(c), `s 4(3)`, `s 4(4)`; the open list in s 4(1) is a residue constructor the person states |
| s 5 | 29-34 | "Belonging to another" | encoded: `s 5 the property belongs to another` with `s 5(1)` to `s 5(5)`, and the two "regarded as an intention to deprive" limbs of s 5(2), s 5(4) |
| s 6 | 35-37 | "With the intention of permanently depriving the other of it" | encoded: `s 6 he intends permanently to deprive the other of it`, `s 6(1)`, `s 6(2)` |
| s 7 | 39-40 | Theft | encoded: `s 7 liable on conviction on indictment for theft` (7 years) |
| s 8 | 41-43 | Robbery | encoded: `s 8(1) guilty of robbery`, `s 8(2) liable ...` (life); "assault with intent to rob" is a borrowed term (fork 9) |
| s 9 | 44-52 | Burglary | encoded: `s 9(1) guilty of burglary` and `s 9(1)(a)`, `(b)`, `s 9(2)`, `s 9(3)` (14 or 10 years), `s 9(4)` (inhabited vehicle or vessel) |
| s 10 | 53-58 | Aggravated burglary | encoded: `s 10(1) guilty of aggravated burglary` with the three definitions, `s 10(2)` (life) |
| s 11 | 59-64 | Removal of articles from places open to the public | encoded: `s 11 guilty of removing an article from a place open to the public`, `s 11(4)` (5 years) |
| s 12 | 65-82 | Taking motor vehicle or other conveyance without authority | encoded: `s 12(1)`, `s 12(2)` (6 months / level 5 / both), `s 12(4)`, `s 12(4A)` to `(4C)` as `s 12(4A) the time limit for proceedings` and `s 12(4B) the relevant day`, `s 12(5)` (level 3), `s 12(6)`, `s 12(7)`; s 12(3) is blank in this text |
| s 12A | 83-101 | Aggravated vehicle-taking | encoded: `s 12A(1) guilty of aggravated taking of a vehicle`, `(2)`, `(3)` defences, `(4)` (2 years, or 14 if death), `(5)`, `(6)`, `(7)`, `(8)` |
| s 13 | 102-103 | Abstracting of electricity | encoded: `s 13 guilty of abstracting electricity` (5 years) |
| s 14 | 104-110 | Extension to thefts from mails outside England and Wales, and robbery etc. on such a theft | encoded: `s 14(1)` as three rules and an outcome, `s 14(2)` the five jurisdictions; s 14(3) is blank in this text |
| s 15 | 112-113 | Obtaining property by deception | repealed or blank in this text: heading remains, body shows only dots (line 113); nothing encoded |
| s 15A | 114-115 | Obtaining a money transfer by deception | repealed or blank in this text: heading remains, body shows only dots (line 115); nothing encoded |
| s 15B | 116-117 | Section 15A: supplementary | repealed or blank in this text: heading remains, body shows only dots (line 117); nothing encoded |
| s 16 | 118-119 | Obtaining pecuniary advantage by deception | repealed or blank in this text: heading remains, body shows only dots (line 119); nothing encoded |
| s 17 | 120-125 | False accounting | encoded: `s 17(1) guilty of false accounting`, `(a)`, `(b)`, `s 17(2)` deemed falsifying, penalty 7 years |
| s 18 | 126-128 | Liability of company officers for certain offences by company | encoded: `s 18 guilty as an officer of the offence committed by the body corporate`, with the s 18(2) member-managed limb folded in; `s 18 liable to be punished accordingly` |
| s 19 | 129-132 | False statements by company directors, etc. | encoded: `s 19 guilty of a false statement by an officer`; s 19(2) (a person with a security counts as a creditor) and s 19(3) (member-managed bodies) folded in; penalty 7 years |
| s 20 | 133-136 | Suppression, etc. of documents | encoded: `s 20(1) guilty of suppressing a document`, `s 20(3)` valuable security; s 20(2) is blank in this text; penalty 7 years |
| s 21 | 137-142 | Blackmail | encoded: `s 21(1) guilty of blackmail`, `s 21(1) the demand is unwarranted`; s 21(2) asserted (immaterial); penalty 14 years |
| s 22 | 144-146 | Handling stolen goods | encoded: `s 22(1) guilty of handling stolen goods`, `s 22(2) liable ...` (14 years) |
| s 23 | 147-148 | Advertising rewards for return of goods stolen or lost | encoded: `s 23 guilty of advertising a reward with no questions asked`, summary, fine level 3 only |
| s 24 | 149-158 | Scope of offences relating to stolen goods | encoded: `s 24 the goods are stolen goods` with `s 24(1)` (proviso), `(2)(a)(b)` (proceeds), `(3)` (ceasing), `(4)` and `(5)` (blackmail, fraud); s 24A(8) is the sixth origin |
| s 24A | 159-190 | Dishonestly retaining a wrongful credit | encoded: `s 24A(1)`, `(2A)`, `(5)` and `(12)(b)` asserted immaterial, `(6)` (10 years), `(9)`, `(10)`; `(3)`, `(4)` blank in this text; `(7)`, `(8)` are the sixth `Origin of goods`; `(11)` and `(12)(a)` explained in comments (deposit is a stated fact) |
| s 25 | 192-197 | Going equipped for stealing, etc. | encoded: `s 25(1) guilty of going equipped`, `s 25(2)` (3 years), `s 25(3)` as evidence only, `s 25(5)` as a third purpose; `s 25(4)` blank in this text |
| s 26 | 199-204 | Search for stolen goods | encoded conditionally for the person whose premises may be searched: `s 26(1) a justice may grant a warrant ...`, `s 26(3) he may enter and search the premises`, `s 26(3) he may seize ...`; s 26(2) and (4) blank in this text; s 26(5) is a construction clause (follow s 24; old offences) with nothing to compute |
| s 27 | 205-215 | Evidence and procedure on charge of theft or handling stolen goods | encoded conditionally for the accused: `s 27(1)` joinder, `s 27(2)` jury, `s 27(3)(a)`, `(b)`, `s 27(3)` admissibility of other dealings and convictions (dates), `s 27(4)` statutory declarations (the accused's counter-notice); s 27(4A) blank; s 27(5) a construction clause |
| s 28 | 216 | (heading and body show only dots) | repealed or blank in this text: the heading is dots (line 216); nothing encoded |
| s 29 | 217-225 | Jurisdiction of quarter sessions, and summary trial | encoded conditionally: `s 29(2) paragraph 11 lists the offence as one that may be tried summarily with his consent` (the Magistrates' Courts Act 1952 is not among the inputs and was replaced; see "Before relying"); s 29(1) blank in this text |
| s 30 | 227-240 | Spouses and civil partners | encoded: `s 30(4) the step may be taken` with `(4)(a)`, `(5)`; `s 30(2)` (two rules); `s 30(1)` asserted (marriage changes no answer); s 30(3) and (4)(b) blank in this text |
| s 31 | 241-246 | Effect on civil proceedings and rights | encoded: `s 31(1)` (three rules: not excused; statement not usable against him; against spouse), `s 31(2)` title not affected |
| s 32 | 247-254 | Effect on existing law and construction of references to offences | encoded: `s 32(1) the old offence is abolished as regards what he did` (keyed on the commencement date); inert: s 32(2), a rule about how OTHER enactments read, which are not among the inputs |
| s 33 | 255-259 | Miscellaneous and consequential amendments, and repeal | inert: amendments and repeals of other enactments (s 33(1) blank, (2) Schedule 2 Parts II and III, (3) Schedule 3 repeals and their extension to Scotland, (4) the Extradition Acts). Those enactments are not among the inputs, so there is nothing to compute, and the repeals are the law's housekeeping for officials and drafters, not something an accused person is asked |
| s 34 | 261-268 | Interpretation | encoded: `s 34(2)(a) a view to gain or an intent to cause loss`, `s 34(2)(b) the thing is goods` (theft-s34-interpretation.l4); s 34(1) kept by structure (every offence that needs theft calls `s 1 guilty of theft`, which calls ss 4 and 5); s 34(2)(c) mail bag and postal packet (Postal Services Act 2000 not an input) is a stated fact |
| s 35 | 269-272 | Commencement and transitional provisions | encoded: `s 35(1) the date the Act came into force` (1 January 1969, as data), `the date the Theft Act 1968 was enacted` (26 July 1968, as data), `s 35(1) the Act has effect in relation to an offence`, `s 35(2)` first half; inert: s 35(2) second half (PCC(S)A 2000 s 148 not an input) and s 35(3) (only preserves old law not among the inputs) |
| s 36 | 273-276 | Short title, and general provisions as to Scotland and Northern Ireland | encoded: `s 36(3) where the Act extends`; not applicable: s 36(1) (the short title, a name); s 36(2) blank in this text |
| Sch 1 | 278-285 | Offences of Taking, etc. Deer or Fish | encoded: paragraph 2 (taking or destroying fish: offence, penalty, forfeiture, arrest and seizure by any person); paragraph 1 and paragraph 2(2) are blank in this text |
| Sch 2 | 286-356 | Miscellaneous and Consequential Amendments (Parts I, II, III) | inert: amendments of the Post Office Act 1953, the Public Stores Act 1875, the Army Act 1955, the Air Force Act 1955, the Naval Discipline Act 1957, the Army and Air Force Act 1961, the House to House Collections Act 1939, the Magistrates' Courts Act 1952, the Visiting Forces Act 1952, the Finance Acts 1965 and 1966, the Firearms Act 1968 and others. None of those enactments is among the inputs; each amendment changes only their text, so computing it would need them. Part I paragraph 10 restates s 14 for the Post Office Act and Part I paragraph 12 restates s 20(3)'s definition for the Post Office Act outside England and Wales; both are covered where the Theft Act states them (ss 14, 20) |
| Sch 3 | 357-498 | Repeals (Parts I, II, III) | inert: the repeal tables (Parts I to III), a list of enactments and the extent of each repeal. They are the law's housekeeping and tell an accused person nothing about their own conduct; the only part that could matter, the abolition of the old offences in s 32(1)(b), is encoded through `Abolished offence` in s 32(1) |

## Fork register

Each entry: the ambiguity, the readings seen, the one taken, the text that licenses it.
Begun before any L4 was written and completed at the end; 36 forks.

1. "Dishonestly" outside s 1. s 1(3) (line 9) says ss 2 to 6 "shall apply only for purposes of this section" except as the Act otherwise provides; the Act otherwise provides in s 34(1) (line 262: ss 4(1) and 5(1) apply generally), s 24(4) (line 155: "steal", "theft" and "thief" construed to match goods obtained by blackmail or fraud), s 24A(8) (line 175), s 25(5) (line 197: an s 12(1) offence is treated as theft for s 25) and s 32(2)(b) (line 254). Readings: (i) s 2 defines "dishonestly" wherever the Act uses the word; (ii) s 2 governs only s 1, so "dishonestly" in ss 13, 17, 20, 22 and 24A is a plain stated fact. Taken: (ii), because s 1(3) says so in terms and none of the five exceptions mentions s 2.
2. Whether s 2(1) is conclusive. Readings: (i) the three beliefs are conclusive ("is not to be regarded as dishonest"); (ii) they are evidence. Taken: (i). Where none applies, the Act gives no positive definition, so dishonesty is a stated fact.
3. s 2(2) willingness to pay. Taken: it removes nothing and adds nothing; it is carried as an unread field and an assertion shows it changes no answer.
4. s 3(2). Reading taken: a bar on theft by a good-faith purchaser for value, not a redefinition of "appropriates".
5. s 4(3) and s 4(2). Reading taken: s 4(3) is a further bar on top of s 4(2) for wild produce.
6. s 12A(3). "As regards any such proven driving, injury or damage" (line 92). Readings: (i) the defence must cover every proven incident; (ii) one covered incident is enough. Taken: (i), kept per circumstance (a) to (d).
7. s 12(4A). "Period of three years beginning with the day on which the offence was committed" (line 71). Taken: the period ends the day before the third anniversary. The month-end edge (a day that has no anniversary) is not asserted.
8. s 25(3) (line 195) "shall be evidence": evidential, not a deeming. The person's purpose stays a stated fact.
9. s 8(2) (line 43) states a penalty for "an assault with intent to rob", an offence the Act never defines. It is in the `Offence` list; its elements are a borrowed input.

10. s 12(1) (line 66). "without having the consent of the owner or other lawful authority" stands before both "he takes any conveyance" and "knowing that any conveyance has been taken without such authority, drives it". Readings: (i) it governs only the first limb; (ii) it governs both. Taken: (ii), the plain reading of a leading adverbial. The cases where it matters (a driver who knows the car was taken without authority but has the owner's consent) are unlikely.
11. s 12(4B)(b) (line 75). "the day on which sufficient evidence ... came to the knowledge of the person who has decided to commence the prosecution or (if later) the discontinuance of the other prosecution". Taken: the later of the two dates. If the discontinuance date is not stated, the evidence date is used and nothing else is guessed.
12. s 12(4A)(b) (line 72). "may be commenced at any time within the period of six months beginning with the relevant day". Readings: (i) a window with both ends, so proceedings begun before the relevant day are outside it; (ii) a limit with an upper end only. Taken: (ii); a time limit that barred proceedings begun too early would be odd, and nothing in (4A)(a) or (4C) supports it. Also: s 12(4A)(b) is read as a limit as well as a permission (the proceedings are barred once the six months run, provided the three years have not), because (4A) is the only provision in the text that regulates when these proceedings may begin.
13. s 12(4C) (line 77). A certificate is "conclusive evidence" of the date evidence came to knowledge. Encoded by how the date is asked: the date the person gives is the certified date where there is a certificate.
14. s 9(2) (line 48). The text reads "grievous bodily harm ... therein" with dots, meaning words repealed. Taken: the three offences left (stealing, grievous bodily harm, unlawful damage) are exactly what the text shows.
15. s 10(1) (line 54). "at the time has with him": the Act does not say at what moment of the burglary. Taken: a fact the person states ("at the time ... had with him"); no moment is imposed.
16. s 11(1) (lines 60 and 61). "a collection ... do not apply to a collection made or exhibited for the purpose of effecting sales or other commercial dealings": read as removing that collection from the access limb only (the building limb is untouched).
17. s 12A(3) "as regards any such proven driving, injury or damage" (see fork 6): guilt needs at least one proven circumstance for which neither defence is proved.
18. s 14(1)(a). "steals" is read as an offence under s 1 (all five elements), "attempts to steal" as a fact the person states; the Act does not define attempts and states no penalty for one, so the outcome is "an offence, but the text states no penalty for it".

19. s 24A(2A) (line 165) "wrongful to the extent that it derives from" theft, blackmail, fraud or stolen goods. The extent is a proportion; a yes-or-no rule can say only whether the credit derives from one of the four at least in part. Taken: ask that, and treat a partly derived credit as wrongful (to that part); the offence then turns on the person knowing or believing it is wrongful and dishonestly failing to take reasonable steps.
20. s 24(1) and (5)(a) (lines 150, 157). The provisions on stolen goods apply "whether it occurred before or after the commencement of this Act", and for fraud goods the reference is to the commencement of the Fraud Act 2006. Either way the date makes no difference to the answer, so no date is read; the Fraud Act 2006 itself is not among the inputs, so "fraud ... under section 1 of that Act" is a fact the person states.
21. s 22(1) (line 145). "dishonestly receives ..., or dishonestly undertakes or assists ..., or if he arranges to do so": the "do so" carries the dishonesty to the arranging limb. Taken: dishonesty is required for all four limbs.
22. s 24A(10) and (11) (lines 180 to 187). "Deposit" is read with the Financial Services and Markets Act 2000, which is not among the inputs. Whether money was received by way of deposit is a fact the person states.

23. s 27(3)(a) (line 209). "from any theft taking place not earlier than twelve months before the offence charged": only the earlier end is read, as the text states no later end. Month-end edges are not asserted (twelve months before 29 February).
24. s 27(3)(b) (line 210). "seven days' notice in writing": read as at least seven days; "within the five years preceding the date of the offence charged": a conviction on a day before the offence, and not earlier than five years before it.
25. s 27(4)(b) (line 213). "at least three days before the hearing or trial or within such further time as the court may in special circumstances allow": the notice defeats the declaration if given at least three days before the hearing, or within time the court allowed.
26. s 29(2) (lines 219 to 225). Paragraph 11 of Schedule 1 to the Magistrates' Courts Act 1952, as substituted, is encoded as the text states it. That Act is not among the inputs and its Schedule was replaced by later legislation; the rule says what the paragraph said, and nothing about the position today.
27. s 30(4)(a)(ii). "under no obligation to cohabit" is read as a fact about a decree or order that the person states; the provisos use "wife or husband" for (ii) and "civil partner" for (iii), and are encoded as the text has them.
28. s 32(1) (line 248). "abolished for all purposes not relating to offences committed before the commencement": keyed on the last day any part of the offence was committed, matching s 35(1)'s "wholly or partly committed on or after that date". An offence begun before 1 January 1969 and continued after is therefore outside the abolition.
29. s 36(3) and the long title (lines 3 and 276). The text says the Act does not extend to Scotland or Northern Ireland and says nothing about the Isle of Man, the Channel Islands or elsewhere; for those, the answer is the not-covered value `the text does not say whether the Act extends there`. That England and Wales is within the Act's extent rests on the long title, "An Act to revise the law of England and Wales ...", not on an operative provision.
30. s 34(2)(a) (lines 264 to 266). Only "gain or loss in money or other property" is a fact; "temporary or permanent" and "by keeping what one has" are what the definition adds, and none removes anything a bare view to gain would have included, so they are not fields.

31. s 14(1) (lines 104 to 110) gives no penalty of its own: the offender is "punished in England and Wales" for "the offence against this Act".
Readings: (i) the penalty is that of the offence the facts show (robbery, theft); (ii) no penalty is stated, so none is returned.
Taken: (i) where the facts fix the offence, (ii) otherwise.
`s 14(1) punishable in England and Wales as the offence he committed` returns the robbery penalty for robbery, the theft penalty for stealing the mail, and the not-covered value `an offence, but the text states no penalty for it` for an attempt that the facts do not make a complete offence.
32. s 30(5) (lines 238 to 240) extends s 30(4) to an arrest without warrant by the spouse and to a warrant on the spouse's information.
It says nothing of any other step.
Taken: `some other step` is not within s 30(4), so `s 30(4) the step may be taken` is TRUE for it.
That is the absence of a bar from s 30(4), not a permission; other law may still bar the step.
33. s 26(1) (line 200) "if it is made to appear ... that there is reasonable cause to believe".
The reasonable cause is the justice's judgment, so the seat asks whether it has been made to appear, and the rule treats it as a stated fact.
34. s 35(2) (line 271) also applies section 148 of the Powers of Criminal Courts (Sentencing) Act 2000, which is not among the inputs.
Taken: only the s 27 half is encoded; the other half is named here and nowhere computed.
35. s 11(2) (line 62). "does not thereby commit an offence under this section unless he removes it on a day when the public have access" applies only to an article that is not part of, or on loan with, a collection intended for permanent exhibition.
Taken: the day condition is asked only for such articles.
36. The seat asks every word of state of mind or judgment as the person's own answer: dishonesty outside s 2(1), reasonable cause, belief, knowledge, intent, "dangerous" driving.
The Act gives no test of dishonesty beyond the three beliefs in s 2(1); the seat's `@desc` says so in the question.

## Findings: what the text turns out to say

Each finding says what the text, read as written, produces.
"Asserted." means a case in this deposit checks it (the file is named); a finding without it rests on reading alone.

1. Twenty-two provisions are a line of dots and nothing else in this text (lines 68, 110, 113, 115, 117, 119, 135, 170, 171, 196, 201, 203, 214, 216, 218, 230, 237, 256, 275, 280, 283 and 308).
Five are whole sections: ss 15, 15A, 15B, 16 and 28 (a heading, then dots).
Seventeen are sub-provisions inside live sections: s 12(3), s 14(3), s 20(2), s 24A(3) and (4), s 25(4), s 26(2) and (4), s 27(4A), s 29(1), s 30(3) and s 30(4)(b), s 33(1), s 36(2), Sch 1 paragraph 1 and paragraph 2(2), and Sch 2 Part I paragraph 8.
The text says nothing about what they once said, and this encoding says nothing either.
In particular, the offences of obtaining property by deception (ss 15, 15A, 16) are not in this text at all.
2. Several sentences have gaps inside them, shown as dots: s 9(2) (line 48, after "grievous bodily harm"), s 18(1) (line 127, "under section ... 17"), s 20(3) (line 136, "For the purposes of this section ..."), s 25(5) (line 197), s 30(4)(a)(i) and (ii) (lines 233 and 235) and s 36(3) (line 276).
Two change what can be read.
s 18(1) names "section ... 17 of this Act": the other section numbers it once named are missing, so which offences s 18 reaches beyond s 17 cannot be read from this text, and only s 17 is encoded as the body corporate's offence.
s 36(3) reads "does not extend to Scotland or, . . . to Northern Ireland": words are missing, and the rule reads the Act as extending to neither.
The s 36(3) cases are in theft-cases-s30-36.l4 and theft-cases-seat.l4.
Asserted.
3. s 2(1)(c): a belief that the owner cannot be found by reasonable steps does not help a trustee or personal representative.
The cases are in theft-cases-s01-06.l4, theft-cases-seat.l4.
Asserted.
4. s 9(4) reaches the penalty as well as the offence: burglary of an inhabited vehicle or vessel carries the fourteen-year ceiling that s 9(3)(a) gives a dwelling.
The cases are in theft-cases-s07-14.l4, theft-cases-seat.l4.
Asserted.
5. A pedal cycle is outside s 12(1) altogether (s 12(5)); taking one is an offence with a fine of level 3 and no imprisonment.
The cases are in theft-cases-s07-14.l4, theft-cases-seat.l4.
Asserted.
6. s 12(4): a jury that is not satisfied of theft but finds the s 12(1) offence proved convicts of that offence and the penalty is that of s 12(2): six months, or a level 5 fine, or both.
The cases are in theft-cases-s07-14.l4, theft-cases-seat.l4.
Asserted.
7. s 12(4A) bars proceedings for the s 12(1) offence on a mechanically propelled vehicle three years after the day of the offence, or six months after the relevant day, whichever ends first; it does not apply to other vehicles or on a trial for theft.
The last day to begin is the day before the third anniversary, or the day before the date six months after the relevant day.
The cases cover both ends of both periods and the discontinued-prosecution case, in theft-cases-s07-14.l4, theft-cases-seat.l4.
Asserted.
8. s 12A(4): two years, or fourteen if the s 12A(2)(b) accident caused death; and a conviction for the basic offence under s 12A(5) carries the powers of a magistrates' court.
The cases are in theft-cases-s07-14.l4, theft-cases-seat.l4.
Asserted.
9. s 14 states no penalty.
An attempt to steal mail that the facts do not make a complete theft is therefore "an offence, but the text states no penalty for it", the not-covered value.
The cases are in theft-cases-s07-14.l4, theft-cases-seat.l4.
Asserted.
10. s 21(1): a demand with menaces is warranted only if the maker held both beliefs.
One of the two is not enough.
The cases are in theft-cases-s15-21.l4, theft-cases-seat.l4.
Asserted.
11. s 21(2): that the menaces relate to action by the demander changes no answer.
The cases are in theft-cases-s15-21.l4.
Asserted.
12. s 24A(2A) and (5), (12)(b): whether the account was overdrawn, and whether the credit is in sterling, make no difference to whether a credit is wrongful.
The cases are in theft-cases-s22-25.l4.
The seat does not ask either, because no rule reads them.
Asserted.
13. s 24A(8): money dishonestly withdrawn from an account is stolen goods only to the extent that it derives from the wrongful credit.
The cases are in theft-cases-s22-25.l4, theft-cases-seat.l4.
Asserted.
14. s 27(3)(a) reaches a theft exactly twelve months before the offence charged and not one a day earlier; s 27(3)(b) reaches a conviction exactly five years before and not one a day earlier, not one on the day of the offence, and needs at least seven days' notice.
The text states no later end for (a), and a conviction on the day of the offence is not one "preceding" it.
The cases are in theft-cases-s26-29.l4, theft-cases-seat.l4.
Asserted.
15. s 27(4)(b): a notice requiring the declarant to attend defeats the declaration if given three days before the hearing and not if given two, unless the court allowed further time and it was given within it.
The cases are in theft-cases-s26-29.l4, theft-cases-seat.l4.
Asserted.
16. s 30(1) adds no rule: marriage to the owner changes no answer to whether s 1 is made out, because s 5 reads no marriage field.
The cases are in theft-cases-s30-36.l4.
Asserted.
s 30(4) bars a step against a person for stealing or damaging property of a wife, husband or civil partner without the Director's consent, except in the three provisos, and s 30(5) extends it to an arrest and a warrant.
The cases are in theft-cases-s30-36.l4, theft-cases-seat.l4.
Asserted.
17. s 32(1) abolishes the old offences for conduct whose last part falls on or after the commencement date, and keeps cheating where it relates to the public revenue.
The cases are in theft-cases-s30-36.l4, theft-cases-seat.l4.
Asserted.
18. The dates the Act carries are data: enacted 26 July 1968 (line 4), in force 1 January 1969 (s 35(1)), each with its `@ref`.
The cases are in theft-cases-s30-36.l4, theft-cases-seat.l4.
Asserted.
19. s 29(2) substitutes paragraph 11 of Schedule 1 to the Magistrates' Courts Act 1952, a Schedule the subsection itself describes as listing indictable offences "which may be tried summarily with the consent of the accused".
The consent belongs to that Act and is not stated by this text; the rule says only which offences the paragraph lists.
The cases are in theft-cases-s26-29.l4 and the seat.
Asserted.
20. What the run found about this encoding's own tests (disclosed, not hidden): the first full run of the ss 7 to 14 cases had two failures, one a fixture error (a hired-conveyance fixture lacked the hire flag, so the owner's consent rule applied; the rule was right and the fixture was renamed and its comment says why) and one a real rule bug (`IF NOT (a) OR b` parsed as `NOT ((a) OR b)` in `s 12(4A)`; see the next section).

## What the stable binary does not accept

## What the stable binary does not accept

Each was measured on `l4` 1.6.98 `main` (7689b0d), 2026-10-22; the binary governs.
Loud failures say so in the diagnostics; silent ones return a wrong answer with no diagnostic, and are marked.

1. SILENT. `NOT (a) OR b` on one line parses as `NOT ((a) OR b)`, silently: a probe with `a` and `b` both `TRUE` returned `FALSE`, and the bracketed form `(NOT (a)) OR b` returned `TRUE`. It shows up as a wrong answer, not an error. `NOT` before a bracket at the start of a continuation line (`AND NOT (x)`, the next `AND` on the next line) is not affected. It was caught by an assertion on `s 12(4A)` (fixture `tl alternative verdict proceedings`) and fixed in the rule. Write `(NOT (a)) OR b`.
2. LOUD, but only as a warning. `AND` and `OR` at the same column draw "AND and OR operators appear at the same indentation level (column 5)" (Warning), reported twice for each occurrence in the probe.
Indent the `AND` limbs one step in under the `OR`, or bracket them; this encoding has no such warning (`check.sh` does not count warnings; they were counted separately: 0).
3. LOUD, but only when the name is used. Two enumerations that share a constructor name are accepted at declaration and fail on first use with "There are multiple definitions for the identifier"; so is a name defined in two imported modules.
Every constructor, field and rule name in this encoding is therefore distinct across the whole deposit.
4. LOUD. `TYPICALLY` and `YMD` are not in `main`: "I could not find a definition for the identifier".
Dates are written `Date d m y` from `daydate`, and `add years` and `add months` come from the same module.
5. Not measured here, taken from the brief and the skills: modules import only from their own folder; no section `GIVEN`, `REFUSE`, sets, `@lang` or opaque `DECLARE`.
The encoding does not use any of them and compiles clean, which is all this note claims.

## What `check.sh` prints

`L4=<stable l4 1.6.98> L4_TARGET=unstable ./check.sh`, exit status 0:

```
module                                    errors satisfied  failed  refused  expected
theft-cases-s01-06.l4                          0        98       0        0         0
theft-cases-s07-14.l4                          0       173       0        0         0
theft-cases-s15-21.l4                          0        79       0        0         0
theft-cases-s22-25.l4                          0        73       0        0         0
theft-cases-s26-29.l4                          0        56       0        0         0
theft-cases-s30-36.l4                          0        74       0        0         0
theft-cases-schedules.l4                       0        14       0        0         0
theft-cases-seat.l4                            0       371       0        0         0
theft-nouns.l4                                 0         0       0        0         0
theft-s01-06-definition.l4                     0         0       0        0         0
theft-s07-14-offences.l4                       0         0       0        0         0
theft-s15-21-fraud.l4                          0         0       0        0         0
theft-s22-25-goods.l4                          0         0       0        0         0
theft-s26-29-procedure.l4                      0         0       0        0         0
theft-s30-36-general.l4                        0         0       0        0         0
theft-s34-interpretation.l4                    0         0       0        0         0
theft-schedules.l4                             0         0       0        0         0
theft-seat.l4                                  0         0       0        0         0
TOTAL (18 modules)                             0       938       0        0
```

938 assertions satisfied, none failed, none refused, no deliberately failing test (so `expected_failed` is empty and there is no `expected_red`).
Warnings were counted separately, per file, with `l4 run`: 0 in all 18 modules, and the two `@ref` warnings from `l4 check` ("is at the end of the file", "follows code on its line"): 0.
`python3 -I srcrefs.py check --refs --strict <raw text> theft-*.l4`: 220 `src:` lines, 45 runs, 163 locators, 0 problems.
Controls run on the seat cases: negating every one of the 371 assertions in a scratch copy made all 371 fail, so none of them is vacuous.

## Before the encoding is worth relying on

1. A domain expert must read it against the official text.
The source here is a converter's plain-text rendering of the revised text, not the official text, and nothing in this deposit is "verified against the official text".
The rendering shows dots where text was removed, and two sentences with dots inside them (Findings 2).
2. The text is the Act as the rendering shows it (revised version 2013-05-28 according to the deposit note); later amendment is not known here.
3. Penalties are the ceilings each section states, as the rendering reads.
Fines are levels on the standard scale and no sum is supplied.
Sentencing law is not an input, so the "most that can follow" is what the section says and not what a court could in fact do today.
4. Enactments the Act points to are not inputs: the Magistrates' Courts Act 1952, the Fraud Act 2006, the Postal Services Act 2000, the Financial Services and Markets Act 2000, the Electronic Money Regulations 2011, the Powers of Criminal Courts (Sentencing) Act 2000.
Where a rule needs a fact from one of them, the person states it.
5. The three readings I would most want a lawyer to check are fork 1 (that "dishonestly" outside s 1 is a stated fact and not s 2's definition), forks 6 and 17 (that the s 12A(3) defence must cover every proven circumstance) and fork 12 (that the s 12(4A) period has an upper end only).
6. The seat asks the person for every word of state of mind and judgment; it cannot tell whether an answer is right, and no answer is a prediction of what a court would find.
7. Only the stable `main` binary was used; nothing was run on `unstable`, so the `main` dialect is the only dialect claimed.
8. Questions the person would ask that the text does not answer and the encoding does not guess: where the Act extends outside England, Wales, Scotland and Northern Ireland (returns the not-covered value); the penalty for an attempt to steal mail (returns the not-covered value); the position of any other step against a spouse under s 30 (no bar from s 30(4), and nothing more said).
