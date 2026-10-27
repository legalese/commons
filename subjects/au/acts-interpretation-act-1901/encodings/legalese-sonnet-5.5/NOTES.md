# NOTES: Acts Interpretation Act 1901 (Australia), encoding `legalese-sonnet-5.5`

Status: **draft**. No domain expert has read this against the text.
Edition encoded: Acts Interpretation Act 1901 (Act No. 2, 1901), Compilation No. 39, compilation date 28 March 2026, includes amendments to Act No. 4, 2026 (register id C2026C00117).
Source file: `../../registers/source-bundle/C1901A00002.txt`, which is a converter's plain-text rendering of the Federal Register of Legislation text, not the official text (see `SOURCE-LICENSE.md`).
Method: one Sonnet 5.5 agent working alone from `BRIEF.md`; no other encoding of this Act was read.
Built and checked with `l4` 1.6.98 (main, 7689b0d, 2026-10-19), `l4`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.

## Seat

The seat is a person who has a time limit to meet under an Act (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.
The Acts Interpretation Act is a rulebook for reading other Acts, so the only questions an individual asks of it directly are about counting time (ss 2G, 36, 37A), when an Act comes into operation (ss 3, 3A), when a posted document counts as served (s 29), and a few kindred limits and entitlements.
The person's counterparty is nearly always an official: the Minister, the decision-maker, the court.
An official is never a seat, so the official's side of each relation appears only as facts the person states about them (whether the appointer has directed otherwise, whether the Minister has granted an extension, on which day the Minister received the report) and as what the person is owed (reasons, and the laying of their report before Parliament).
The seat layer is `au-seat.l4` (questions) and `au-cases-seat.l4` (worked cases).

## Scope

All 83 body sections of the compilation are in the coverage table below: 51 are encoded (some in part) and 32 are inert, each with a reason.
The Act has no Schedules.
Layer 1 follows the Act's own structure, one module per Part where there is something to encode, plus one self-contained module for every rule that counts time:

| file | what it holds |
|---|---|
| `au-interpretation-time.l4` | Imports only `prelude` and `daydate`. The `YMD` shim; s 2B business day, calendar month, calendar year, financial year; s 2G months; s 2M sitting days; s 3 and s 3A commencement; s 29 service by post; s 36 calculating time; s 37A attaining an age. Holidays and closed days are always inputs. |
| `au-part1-application.l4` | ss 1, 2, 2A; the Act's own assent and commencement dates (endnote 3). |
| `au-part2-definitions.l4` | The s 2B definitions that compute (places, document, contravene, prescribed, Proclamation, Senior Counsel); ss 2C to 2F, 2H, 2J, 2K. |
| `au-part3-commencement.l4` | s 4 (powers before commencement), s 6 (evidence of the date of assent). |
| `au-part4-repeal.l4` | ss 7, 10, 10A, 11, 11B. |
| `au-part5-interpretation.l4` | ss 13, 15AB(1), 15B, 15C, 18B, 25A to 25D. |
| `au-part6-service.l4` | s 28A. |
| `au-part7-powers.l4` | ss 33(4), 33A, 33AB, 34A, 34B, 34C. |
| `au-part8-distance.l4` | s 35. |
| `au-part9-citation.l4` | ss 38, 39, 40, 40A. |
| `au-part10-11-instruments.l4` | ss 46, 46AA, 47, 51. |
| `au-seat.l4`, `au-cases-seat.l4` | Layer 2: the seat's questions and worked cases. |
| `au-tests-*.l4` | One test file per module, expected values written from the text. |

Every rule (every function) has an `@ref` with `src:` locators (the `DECLARE`d vocabulary of choices has none), and every quoted text line begins `-- src:N |` where N is the line number in `../../registers/source-bundle/C1901A00002.txt`.
What `srcrefs.py` checks is printed under the heading on what `check.sh` prints, below.

### Not encoded, and why

- **Time of day.** A moment is a day plus hour, minute and second with no time zone. Section 37 (legal time in each State) is not computed, because the text does not define legal time.
- **Public holidays and office closures.** Never listed by the Act. Every question asks for them as one list of days.
- **Weeks and years.** The Act never says how long they are (finding 5). The ordinary answer is NOTHING, and a separately named ALTERNATIVE READING function shows the 7-day and 12-month result.
- **Judgments left to someone else.** Whether a relationship is "as a couple", whether a contrary intention appears, whether a person is of the opinion that compliance is not reasonably possible, what extension a Minister grants: all inputs, never guessed.
- **Borrowed terms.** 16 definitions in s 2B take their meaning from another Act that is not in the text. They are asked as facts when a rule needs them and are otherwise inert.
- **Machinery of government and officials' powers.** Sections 19 to 19E, 33 (apart from the 12-month limit), 33B, 34, 34AAA to 34AB.

## Jural relations

Each relation is stated once in layer 1, from neither side, and the seat asks the paired question where the person holds the right, privilege, power or immunity or owes the duty or liability.

| provision | holder (right, privilege, power, immunity) | other party (duty, no-right, liability, disability) | relation | L4 rule | seat question |
|---|---|---|---|---|---|
| s 36(2) | the person who must do a thing | the other side (the authority or party to whom it is done) | privilege to do the thing on the next day that is not a Saturday, a Sunday or a holiday / no-right to treat it as late | `the last day on which the thing may be done` | What is the last day on which I may act ... (s 36(2))?; Am I in time ...? |
| ss 2G, 36(1), 3, 3A, 37A | none | none | none: counting and commencement rules fix WHEN a relation starts or ends and create no relation of their own | the time module's counting rules | the counting questions |
| s 29 | the person serving a document by post: power to effect service by posting; the person served: power to rebut by proving the contrary | the person served: liability to be treated as served on the ordinary delivery day; the person serving: liability to that day being displaced | power / liability, twice | `the day service by post is taken to be effected` | On which day am I taken to have been served by post? |
| s 28A | the person serving: power to serve by a listed method (or by another method another law or a court authorises) | the person served: liability to be served in that way | power / liability | `service by this method is permitted` | Was the document served on me in a way the Acts Interpretation Act allows? |
| s 33A(1)(b)(ii) | the appointer: power to terminate an acting appointment | the acting appointee: liability | power / liability (not encoded: a discretion) | not encoded | the acting questions take whether the appointer has directed otherwise as a fact |
| s 33A(1)(ba), (c) | the appointee: privilege to act in the office until the 12-month limit, the direction or the filling of the vacancy | the appointer: no-right to hold the appointee to a longer term | privilege / no-right | `the last day the appointee may act in a vacant office`, `the day the continued acting ends` | Until which day may I keep acting ...? |
| s 33(4)(b) | the appointer: power to appoint someone to act | the acting appointee: liability | power / liability, bounded by 12 months | `the last day of the 12 months for an acting appointment under section 33(4)` | On which day do the 12 months of an appointment to act under a power to appoint run out? |
| s 33AB | the person acting under a purported appointment, and those who dealt with them: immunity from invalidity on the listed grounds alone | anyone who would challenge: disability | immunity / disability | `the thing done is invalid merely because of this ground` | not asked (addresses the effect on third parties) |
| s 34C(2) | the Minister: claim to the report by the end of 6 months | the person: duty to furnish a periodic report | claim / duty | `the last day to furnish a periodic report to the Minister` | By which day must I furnish my periodic report to the Minister? |
| s 34C(4) | the person: power to apply for an extension within the specified period | the Minister: liability | power / liability | `the person may apply for an extension` | Can I still ask the Minister for more time to furnish my report? |
| s 34C(5) | the Minister: power to grant such extension as is reasonable | the person: liability | power / liability (not encoded: a discretion; the extended last day is an input) | not encoded | the extended last day is an input to the s 34C(6), (7) questions |
| s 34C(7)(a) | the Minister: claim to a written statement of reasons within 14 days after the late end | the person: duty to explain | claim / duty | `the last day to furnish the statement explaining why the report was late` | By which day must I explain in writing why my report was late? |
| s 34C(3), (6)(a), (6)(c), (7)(b) | each House of the Parliament (not a seat); the person is owed that their report and statements are laid | the Minister: duty to cause the copy to be laid within the stated sitting days | claim / duty | `the last day for the Minister to lay ...` (four rules) | By which day must the Minister lay ... (four questions) |
| s 7(2) | a person holding a right, privilege, obligation or liability acquired, accrued or incurred: immunity from loss by repeal or amendment (and liability to a penalty already incurred) | the repealing or amending Act: disability, unless a contrary intention appears | immunity / disability | `what a repeal or amendment does to` | What happens to what I already have or owe when the Act is repealed or amended? |
| s 25C | the person filing a prescribed form: privilege that substantial compliance is enough | the receiving body: no-right to reject a form for want of strict compliance | privilege / no-right | `the form requirement is met` | Does my form meet the requirement if it does not comply strictly with the prescribed form? |
| s 25D | the person affected by a decision: claim to reasons setting out the findings of fact and referring to the evidence | the decision-maker: duty | claim / duty | `the written reasons are complete` | Are the written reasons I was given complete? |
| ss 1, 1A, 2, 2A, 2B to 2M, 3, 3A, 4, 6, 7(1), 7(3), 7(4), 10, 10A, 11, 11B, 13, 15AB, 15B, 15C, 18B, 25A, 25B, 34A, 34B, 35, 37A, 38, 39, 40, 40A, 46, 46AA, 47, 51 | none | none | none: definitions, counting rules, rules of reading and powers of officials that create no claim, privilege, power or immunity between the person and another party | (the rules of the same names) | (where a seat question exists it is listed under the section it answers) |

## Coverage table

One row per body section of the compilation (83), then the s 2B defined terms (77), the s 36 table and subsections (10), the numbers repealed (49 listed in endnote 4), and the front matter and endnotes.

### Summary of dispositions

| group | encoded | inert | repealed | not applicable |
|---|---|---|---|---|
| body sections | 51 | 32 | 0 | 0 |
| s 2B defined terms | 21 | 56 | 0 | 0 |
| s 36 table and subsections | 10 | 0 | 0 | 0 |
| section numbers shown as repealed in endnote 4 | 0 | 0 | 49 | 0 |
| front matter, endnotes, Schedules | 0 | 2 | 0 | 1 |

A section that is encoded in part is counted as encoded, and its row says which subsections are inert.

### Body sections

| section | title | disposition | where, or why inert |
|---|---|---|---|
| 1 | Short title | encoded | au-part1-application.l4: `the short title of this Act`. |
| 1A | Simplified outline | inert | A table of contents in words: each line says which Part deals with what and states no rule of its own. Every line is stated by the section it summarises, so encoding it would say the same thing twice. |
| 2 | Application of Act | encoded | au-part1-application.l4: `a provision of this Act applies to the Act or provision` (subsections (1) and (2); a contrary intention is an input). The Note to (1), that the Act also applies to legislative instruments, notifiable instruments and other instruments, is inert: it only points at ss 46 and the Legislation Act 2003. Seat: `Does the Acts Interpretation Act 1901 apply to the Act that binds me`. |
| 2A | Binding the Crown | encoded | au-part1-application.l4: `this Act binds the Crown in each of its capacities`. |
| 2B | Definitions | encoded | In part. See the sub-table of s 2B terms below: 21 of 77 terms encoded (counting pointers to encoded sections), the rest inert (a borrowed meaning, a pointer to a section that is inert, a name, or a plain inclusion). |
| 2C | References to persons | encoded | au-part2-definitions.l4: `is included in an expression denoting persons generally` (subsection (1)); subsection (2) only says that naming companies elsewhere does not narrow (1), which the rule already gives, so it is not a separate rule. |
| 2CA | References to spouses | encoded | au-part2-definitions.l4: `is the spouse of the other person` (subsection (1)). Subsection (2) and the Example say it adds to any definition in another Act: inert, because they concern how it combines with another Act's own definition, which is not in this text. |
| 2D | References to de facto partners | encoded | au-part2-definitions.l4: `are de facto partners`. |
| 2E | Registered relationships | encoded | au-part2-definitions.l4: `are in a registered relationship` (what is a prescribed law or kind of relationship is an input; it is prescribed outside the text). |
| 2F | De facto relationships | encoded | au-part2-definitions.l4: `are in a de facto relationship`, `are related by family` (subsections (1), (4), (6), (7); subsection (5), that a marriage or relationship with someone ELSE does not stop it, is encoded by what the inputs leave out). Subsections (2) and (3), the list of circumstances for whether there is a relationship "as a couple" and that none is necessary, are inert: the finding "as a couple" is a judgment left to someone else and is taken as an input. |
| 2G | Months | encoded | au-interpretation-time.l4: `the last day of` n `calendar months starting on` s, `the last day of a month starting on` s (subsections (1) and (2), all four Examples asserted in au-tests-time.l4). |
| 2H | References to law of the Commonwealth | encoded | au-part2-definitions.l4: `is a law of the Commonwealth, apart from the Territory exclusion`. |
| 2J | Documents commencing proceedings | encoded | au-part2-definitions.l4: `the reference is taken to include the document`. |
| 2K | Rules of court | encoded | au-part2-definitions.l4: `are rules of court` (subsection (1)). Subsection (2), that the power includes power to make rules for the purpose of any Act that directs or authorises it, is inert: it widens a power of an official and decides no fact. |
| 2L | References to Australian Standards | inert | A reference "Australian Standard AS <number>" is a reference to the standard published by or for Standards Australia. It points at a document outside the text, so nothing in the text can compute with it. |
| 2M | Sitting day | encoded | au-interpretation-time.l4: `is a sitting day`, `the sitting day that is the n-th after` (subsections (1) and (2) and both Examples; subsection (3), that prorogation, dissolution and expiry count as adjournment, is not separately encoded: the person lists the days a sitting BEGAN, and each sitting is a separate entry). |
| 3 | When Acts come into operation | encoded | au-interpretation-time.l4: `the moment the enactment comes into operation` (start of the day). |
| 3A | Commencement of Acts | encoded | au-interpretation-time.l4: `the day the enactment commences` (subsections (1), (2), (3)). |
| 4 | Exercise of powers between enactment and commencement of Act | encoded | au-part3-commencement.l4: `section 4 allows the power to be exercised before the start time`, `the exercise may confer a power or right or impose an obligation before the relevant commencement`, `the day an appointment or instrument made before the start time takes effect` (subsections (1), (2), (4), (5), (7)). Subsections (3) and (6) are inert: (3) extends (2) to things done to prepare the exercise, and (6) says an instrument may rely on (2) and on an existing power at once; neither adds a condition or a day. |
| 6 | Evidence of date of assent | encoded | au-part3-commencement.l4: `the printed date is evidence of the date of assent, and is to be judicially noticed`. |
| 7 | Effect of repeal or amendment of Act | encoded | au-part4-repeal.l4: `the repeal of the repealing Act or part revives the old Act or part`, `what a repeal or amendment does to`, `counts as a repeal or amendment for section 7` (subsections (1) to (4)). Seat: `What happens to what I already have or owe when the Act is repealed or amended`. |
| 10 | References to amended or re-enacted Acts | encoded | au-part4-repeal.l4: `a reference to the short title of another Act includes that Act as amended from time to time`, `the reference includes the re-enacted Act`, `the reference to the repealed provision extends to the re-enacted provision`. |
| 10A | References to amended or re-enacted laws of States and Territories | encoded | au-part4-repeal.l4: `a reference to a citation of a law of a State or Territory includes that law as originally enacted or made and as amended from time to time`, `the reference includes the re-enacted or re-made law`, `the reference to the repealed provision of the State or Territory law extends to the re-enacted or re-made provision`. |
| 11 | Acts may be altered etc. in same session | encoded | au-part4-repeal.l4: `an Act may be altered, amended or repealed in the same session of Parliament in which it was passed` (a constant: the section permits and conditions nothing). |
| 11A | Inserting definitions into provisions or inserting items into lists or tables | inert | Says where an amending Act's new definition or list item is placed in the amended text (alphabetical position, or the position given). It governs how the compilation is laid out, and it decides no right, duty or date for a person. |
| 11B | Amending Act to be construed with amended Act | encoded | au-part4-repeal.l4: `the term has that meaning in the non-amending provision` (subsections (1) to (3)). |
| 12 | Every section a substantive enactment | inert | A rule of reading: every section has effect as a substantive enactment without introductory words. It takes no facts and returns no answer that depends on any. |
| 13 | Material that is part of an Act | encoded | au-part5-interpretation.l4: `is part of the Act`. |
| 15A | Construction of Acts to be subject to Constitution | inert | A rule of reading (read the Act subject to the Constitution and so as not to exceed power). Whether an Act exceeds power is a judgment for a court, not a fact the text can compute. |
| 15AA | Interpretation best achieving Act's purpose or object | inert | A rule of reading (prefer the interpretation that best achieves the purpose). "Best achieves" is a judgment left to the interpreter. |
| 15AB | Use of extrinsic material in the interpretation of an Act | encoded | au-part5-interpretation.l4: `consideration may be given to the material` (subsection (1)). Subsections (2) (a non-exhaustive list of material) and (3) (the weighing of desirability and the saving of time and cost) are inert: they are lists of examples and a judgment left to the interpreter. |
| 15AC | Changes to style not to affect meaning | inert | A rule of reading (a later change of wording is not a change of idea merely because the words differ). Whether two ideas are the same is the interpreter's judgment. |
| 15AD | Examples | inert | A rule of reading (an example in an Act is not exhaustive and may extend the provision). It decides no fact. |
| 15B | Application of Acts in coastal sea | encoded | au-part5-interpretation.l4: `is in the coastal sea of Australia`, `an Act is taken to have effect there as if it were part of Australia` (subsections (1), (2), (4)(a)). Subsections (3) and (3A) and (4)(b), the coastal sea of an external Territory, are inert: they repeat the same shape for a Territory whose sea limits are set by other Acts. |
| 15C | Jurisdiction of courts | encoded | au-part5-interpretation.l4: `the jurisdiction the provision vests in the court`. |
| 16 | References to the Sovereign | inert | Says a reference to the Sovereign reigning when the Act was passed, or to the Crown, is a reference to the Sovereign for the time being. A rule of wording for older Acts that decides nothing about a person's period or deadline. |
| 16A | References to the Governor-General | inert | Says a reference to the Governor-General includes the person for the time being administering the Government and, for an assigned power or function, the deputy. It addresses officials, and the seat is never an official. |
| 16B | References to the Governor of a State | inert | The same shape as s 16A for a State Governor: addresses an official. |
| 16BA | References to judge | inert | Says a reference to a judge does not include a Judge, or acting Judge, of the Local Court of New South Wales or of the Northern Territory. It is a naming rule for officials and decides no deadline. |
| 16C | References to Stipendiary Magistrate and Magistrate | inert | A naming rule for officials, in the same family as s 16BA. |
| 17A | Paper or document purporting to be printed by Government Printer | inert | Says that certain words printed on a paper (such as "Government Printer of the Commonwealth") are taken to refer to the Government Printer. A rule about the wording of a reference; it decides no fact. |
| 18A | Parts of speech and grammatical forms | inert | A rule of wording: where a word is given a meaning, other parts of speech and grammatical forms of it have a corresponding meaning. It decides no fact. |
| 18B | Titles of Chairs and Deputy Chairs | encoded | au-part5-interpretation.l4: `the person may be referred to by this chair title` (subsections (1) to (3)). Subsections (4) to (6), the same rule for Deputy Chair titles, are not separately encoded: they differ only in the list of titles. |
| 19 | References to Ministers in Acts | inert | Machinery of government: a table saying which Minister a reference to a Minister means for a matter on a day, by reference to the Administrative Arrangements Order. The Order is outside the text, the section addresses officials, and the seat is never an official. |
| 19A | References to Departments in Acts | inert | Machinery of government: the same shape as s 19, for references to Departments. |
| 19B | Machinery of government - substituted reference orders | inert | Machinery of government: orders substituting references. Depends on instruments outside the text and addresses officials. |
| 19C | Machinery of government - references to authorities in Commonwealth agreements | inert | Machinery of government: references in agreements. Depends on instruments outside the text. |
| 19D | Machinery of government changes - saving the validity of acts done by authorities | inert | Machinery of government: saves what an authority did; addresses officials. |
| 19E | Validity of acts done by Ministers | inert | Machinery of government: a thing is not invalid merely because a Minister purported to exercise a power conferred on another Minister. It addresses officials. |
| 20 | References to holders of appointments, offices and positions in Acts and agreements | inert | Says a reference to a holder covers a person who holds, occupies or performs the duties of the office. A rule of naming for officials. |
| 21 | Office etc. means office etc. of the Commonwealth | inert | A rule of reading (references to officers, offices, localities, jurisdictions and other matters are to those of the Commonwealth). It decides no fact. |
| 23 | Rules as to gender and number | inert | A rule of wording (words of one gender include every gender; singular includes plural and the reverse). It decides no fact. |
| 25A | Production of records kept in computers etc. | encoded | au-part5-interpretation.l4: `the requirement is complied with`. |
| 25B | Alterations of names and constitutions | encoded | au-part5-interpretation.l4: `a reference to the former name is read as a reference to the new name`, `an alteration of the constitution of a body affects its identity, functions, powers, property, rights, liabilities or obligations, or pending proceedings, investigations or inquiries` (subsections (1), (1A), (2)). Subsection (3), the meaning of "office", is inert: it is a definition. |
| 25C | Compliance with forms | encoded | au-part5-interpretation.l4: `the form requirement is met`. Seat: `Does my form meet the requirement if it does not comply strictly with the prescribed form`. |
| 25D | Content of statements of reasons for decisions | encoded | au-part5-interpretation.l4: `the written reasons are complete`. Seat: `Are the written reasons I was given complete`. |
| 28A | Service of documents | encoded | au-part6-service.l4: `service by this method is permitted`. Seat: `Was the document served on me in a way the Acts Interpretation Act allows`. |
| 29 | Meaning of service by post | encoded | au-interpretation-time.l4: `the day service by post is taken to be effected` (subsection (1)). Subsection (2), that it does not affect s 160 of the Evidence Act 1995, is inert: it saves another Act that is not in the text. |
| 33 | Exercise of powers and performance of functions or duties | encoded | In part. au-part7-powers.l4: `the last day of the 12 months for an acting appointment under section 33(4)`, `the 12 months under section 33(4) have expired by` (subsection (4)(b)). Inert: (1) (a power may be exercised from time to time as occasion requires), (2A) ("may" means discretion for Acts assented to after the commencement of (2A); this text does not date that commencement), (2B) (vacancies do not affect a body), (3) to (3B) and (3AA) to (3AC) (a power to make an instrument includes a power to vary or revoke it, to cover matters by class, and to make provision for an aspect), (4) apart from the 12 months (the power to appoint includes a power to remove, suspend or appoint temporarily), (5) (a limit on penalties does not stop an instrument requiring other things). Each is a rule about what an official's power includes; none computes from facts the person states. |
| 33AA | Power to appoint includes power to reappoint | inert | A power to appoint includes a power to reappoint. It widens an official's power and takes no fact. |
| 33AB | Validity of things done under appointments under Acts | encoded | au-part7-powers.l4: `the thing done is invalid merely because of this ground`. |
| 33A | Acting in offices or positions | encoded | In part. au-part7-powers.l4: `the last day the appointee may act in a vacant office` ((1)(ba)), `the day the continued acting ends` ((1)(c)). Inert: (1)(a), (b), (d), (e), (2), (3), (4): the appointer's discretion over terms and termination, resignation, the appointee's powers while acting, acting by operation of law, and a definition. |
| 33B | Participation in meetings by telephone etc. | inert | A body established by an Act may permit its members to take part in meetings by telephone, closed-circuit television or other means, and a member who does so is present. It is the body's discretion, with no condition a person can state. |
| 34 | Power to hear and determine a matter includes power to receive evidence and examine witnesses etc. | inert | Widens the powers of a person authorised to hear and determine a matter. It addresses officials. |
| 34AAA | Exercise of powers etc. by holders etc. of offices or positions | inert | A power conferred on an office-holder as such may be exercised by whoever holds the office for the time being. It addresses officials. |
| 34AAB | Minister may authorise others to perform functions or duties or exercise powers on his or her behalf | inert | Machinery between Ministers (authorisation, revocation, in writing). It addresses officials. |
| 34AA | Delegation to persons holding, occupying or performing the duties of an office or position | inert | A power to delegate is not limited to a named person. It addresses officials. |
| 34AB | Effect of delegation | inert | The effects of a delegation (made generally or as provided, not delegable further, deemed done by the authority, not preventing the authority acting, additional and altered functions). It addresses officials. |
| 34A | Exercise of powers and performance of functions or duties that depend upon the opinion etc. of delegates | encoded | au-part7-powers.l4: `the delegate may act on the delegate's own opinion, belief or state of mind`. |
| 34B | Presentation of papers to the Parliament | encoded | In part. au-part7-powers.l4: `it is sufficient compliance in relation to a House` (subsection (1)). Inert: (1A), which repeats (1)(a) and (b) for an Act that refers to papers presented; and (2), the meaning of "paper". |
| 34C | Periodic reports | encoded | In part. au-part7-powers.l4: `the last day to furnish a periodic report to the Minister` ((1), (2)), `the last day for the Minister to lay the report before a House` ((3)), `the person may apply for an extension` ((4)), `the last day for the Minister to lay the extension statement before a House` ((6)(a)), `the last day for the Minister to lay the extended report before a House` ((6)(c)), `the last day to furnish the statement explaining why the report was late` and `the last day for the Minister to lay the late-report statement before a House` ((7)), `section 34C applies to`, `subsection 34C(3) applies to`, `paragraph 34C(6)(c) applies to` ((7A), (8)). Inert: (5), the Minister's grant of "such extension as he or she considers reasonable" (a discretion: the extended last day is an input), and (6)(b), which is the same test as the application window, applied to the extended last day by `the thing is done within the time allowed`. |
| 35 | Measurement of distance | encoded | au-part8-distance.l4: `the distance for the purposes of an Act`. |
| 36 | Calculating time | encoded | au-interpretation-time.l4: see the sub-table of s 36 below. |
| 37 | Expressions of time | inert | Any reference to time is to the legal time in the State or part of the Commonwealth. "Legal time" is set by time-zone law outside this text, so no rule here can compute it. It is used only as the reading of "the start of the day" in `the moment the enactment comes into operation`, and the encoding models a moment as a day plus hour, minute and second with no time zone. |
| 37A | Attainment of particular age | encoded | au-interpretation-time.l4: `the moment a person attains the age`. Seat: `At what moment do I attain a given age`. |
| 38 | Reference to Acts | encoded | au-part9-citation.l4: `the term by which an Act of this body may be referred to`. |
| 39 | Numbering of Acts | encoded | au-part9-citation.l4: `the number given to the Act`. |
| 40 | Citation of Acts and instruments | encoded | au-part9-citation.l4: `it may be cited this way in an Act, instrument or document` (subsections (1A), (1), (2)). |
| 40A | References to the new corporations and ASIC legislation | encoded | au-part9-citation.l4: `the reference is taken to include the corresponding old provision and any relevant earlier law` (subsections (1) to (3), (5)). Subsection (4), how correspondence is determined (by Part 10.1 of the Corporations Act 2001 and Part 16 of the ASIC Act 2001), and (6), the definitions, borrow other Acts that are not in this text: inert. |
| 46 | Construction of instruments | encoded | au-part10-11-instruments.l4: `this Act applies to the instrument as if it were an Act and each of its provisions a section of an Act`, `this part of the instrument is valid`, `an amendment of the instrument by an Act prevents the authority from later amending or repealing it` (subsections (1) to (3)). The Note, that the Legislation Act 2003 has a parallel, is inert (and for such instruments the rules answer NOTHING). |
| 46AA | Prescribing matters by reference to other instruments | encoded | au-part10-11-instruments.l4: `the instrument may apply, adopt or incorporate the matter at this time` (subsections (1) to (4)). |
| 47 | Construction of resolutions | encoded | au-part10-11-instruments.l4: `this part of the resolution is valid`. |
| 51 | Regulations | encoded | au-part10-11-instruments.l4: `the Governor-General may make regulations prescribing the matter`. |

### Section 2B, term by term

| term | disposition | where, or why inert |
|---|---|---|
| acting SES employee | inert | Borrowed: "has the same meaning as in the Public Service Act 1999", which is not in the text. |
| Administrative Arrangements Order | inert | Names an instrument made by the Governor-General; used only by the machinery-of-government sections (19 to 19E), which are inert. |
| affidavit | inert | "Includes affirmation, declaration and promise": an inclusion that decides no fact. |
| appoint | inert | A pointer to s 33AA, which is inert. |
| APS employee | inert | Borrowed from the Public Service Act 1999. |
| Australia | encoded | au-part2-definitions.l4: `is within Australia in a geographical sense`. |
| Australian citizen | inert | Borrowed from the Australian Citizenship Act 2007. |
| Australian Privacy Principle | inert | Borrowed from the Privacy Act 1988. |
| Australian Standard | inert | A pointer to s 2L, which is inert. |
| business day | encoded | au-interpretation-time.l4: `is a business day`. |
| calendar month | encoded | au-interpretation-time.l4: `is one of the 12 calendar months`. |
| calendar year | encoded | au-interpretation-time.l4: `the calendar year containing`. |
| charitable | inert | Borrowed from Part 2 of the Charities Act 2013. |
| charitable purpose | inert | Borrowed from Part 3 of the Charities Act 2013. |
| charity | inert | Borrowed from Part 2 of the Charities Act 2013. |
| commencement | inert | Equates commencement with coming into operation, with a pointer to s 3 (encoded). The equation is used in the names of the rules and decides nothing by itself. |
| Commonwealth | encoded | au-part2-definitions.l4: `is within Australia in a geographical sense` (the definition has the same words as "Australia"). |
| Consolidated Revenue Fund | inert | Names the fund referred to in s 81 of the Constitution. |
| Constitution | inert | A name. |
| contiguous zone | inert | Borrowed from the Seas and Submerged Lands Act 1973. |
| continental shelf | inert | Borrowed from the Seas and Submerged Lands Act 1973. |
| contravene | encoded | au-part2-definitions.l4: `the person contravenes the provision`. |
| court exercising federal jurisdiction | inert | Classifies a court by what it is doing at the time, a judgment left to someone else; no rule in this text turns on it. |
| court of summary jurisdiction | inert | Classifies a justice or magistrate by function; no rule in this text turns on it. |
| de facto partner | encoded | A pointer to s 2D: au-part2-definitions.l4: `are de facto partners`. |
| document | encoded | au-part2-definitions.l4: `is a document`. |
| estate | inert | A list of interests the word includes; it decides no fact. |
| exclusive economic zone | inert | Borrowed from the Seas and Submerged Lands Act 1973. |
| Executive Council | inert | A name (the Federal Executive Council). |
| external Territory | encoded | au-part2-definitions.l4: `is an external Territory`. |
| federal court | inert | A name (the High Court or a court created by Parliament). |
| financial year | encoded | au-interpretation-time.l4: `the financial year containing`. |
| foreign country | encoded | au-part2-definitions.l4: `is a foreign country`. |
| Gazette | inert | A name (the Commonwealth of Australia Gazette). |
| Government Printer | inert | A definition with a pointer to s 17A, which is inert. |
| Governor of a State | inert | A pointer to s 16B, which is inert. |
| Governor-General | inert | A pointer to s 16A, which is inert. |
| High Court | inert | A name. |
| individual | inert | "A natural person": used as the choice `a natural person` in ss 2C and 28A, with no separate rule. |
| insolvent under administration | inert | Borrowed from the Corporations Act 2001. |
| internal Territory | encoded | au-part2-definitions.l4: `is an external Territory` (an internal Territory is never an external one). |
| Jervis Bay Territory | inert | A name (the Territory in the Jervis Bay Territory Acceptance Act 1915). |
| judge | inert | A pointer to s 16BA, which is inert. |
| justice of the peace | inert | An inclusion (a justice of the peace for a State or part of one). |
| land | inert | A list of interests the word includes; it decides no fact. |
| law of the Commonwealth | encoded | A pointer to s 2H: au-part2-definitions.l4: `is a law of the Commonwealth, apart from the Territory exclusion`. |
| legislative instrument | inert | Borrowed from the Legislation Act 2003; used as a choice in the rules that distinguish it. |
| Magistrate | inert | A pointer to s 16C, which is inert. |
| Minister | inert | A definition (one of the Ministers of State) with a pointer to s 19, which is inert. |
| modifications | inert | An inclusion (additions, omissions and substitutions). |
| month | encoded | A pointer to s 2G: au-interpretation-time.l4: `the last day of` n `calendar months starting on` s. |
| Northern Territory | inert | A name. |
| notifiable instrument | inert | Borrowed from the Legislation Act 2003; used as a choice in the rules that distinguish it. |
| oath | inert | An inclusion (affirmation, declaration, promise). |
| Parliament | inert | A name (the Parliament of the Commonwealth). |
| penalty unit | inert | Borrowed (the amount is fixed by the Crimes Act 1914). |
| person | encoded | A pointer to s 2C: au-part2-definitions.l4: `is included in an expression denoting persons generally`. |
| prescribed | encoded | au-part2-definitions.l4: `is prescribed`. |
| Proclamation | encoded | au-part2-definitions.l4: `is a Proclamation`. |
| record | inert | An inclusion (information stored by means of a computer). |
| regulations | inert | "Regulations under the Act": a definition with nothing to compute. |
| rules of court | encoded | A pointer to s 2K: au-part2-definitions.l4: `are rules of court`. |
| seat of Government | inert | A name. |
| Senior Counsel | encoded | au-part2-definitions.l4: `is Senior Counsel`. |
| SES employee | inert | Borrowed from the Public Service Act 1999. |
| sitting day | encoded | A pointer to s 2M: au-interpretation-time.l4: `is a sitting day`. |
| Sovereign | inert | A pointer to s 16, which is inert. |
| spouse | encoded | A pointer to s 2CA: au-part2-definitions.l4: `is the spouse of the other person`. |
| Standards Australia | inert | A name (Standards Australia Limited, with its ACN). |
| State | inert | A name (a State of the Commonwealth). |
| statutory declaration | inert | A declaration made under an Act authorising it; no rule in this text turns on it. |
| Stipendiary Magistrate | inert | A pointer to s 16C, which is inert. |
| swear | inert | An inclusion (affirm, declare, promise). |
| territorial sea | inert | Borrowed from the Seas and Submerged Lands Act 1973. |
| Territory (and its variants) | inert | "A Territory referred to in section 122 of the Constitution": a name for a class. |
| United Kingdom | inert | A name. |
| writing | inert | An inclusion (any mode of representing or reproducing words, figures, drawings or symbols in a visible form). |

### Section 36, the table and subsections

| part | what it says | disposition | where |
|---|---|---|---|
| (1) item 1 | a period expressed to occur between 2 days includes both days | encoded | au-interpretation-time.l4: `between two days` in `How a period is expressed`; `a period expressed in this way includes the specified day`; asserted in au-tests-time.l4 (Example 1). |
| (1) item 2 | begin at, on or with a specified day: includes that day | encoded | `begins at, on or with a specified day`; Example 2. |
| (1) item 3 | continue until a specified day: includes that day | encoded | `continues until a specified day`; Example 3. |
| (1) item 4 | end at, on or with a specified day: includes that day | encoded | `ends at, on or with a specified day`; Example 4. |
| (1) item 5 | begin from a specified day: does not include that day | encoded | `begins from a specified day`; Example 5 (a variation operating from 30 June starts on 1 July). |
| (1) item 6 | begin after a specified day: does not include that day | encoded | `begins after a specified day`; Example 6 (28 days after 2 August begins on 3 August). |
| (1) item 7 | end before a specified day: does not include that day | encoded | `ends before a specified day`; Example 7 (the 7-day period before 8 May is 1 to 7 May). |
| (1) rest | the chapeau: a period of a kind in column 1 is calculated by the rule in column 2 | encoded | `the first day of the period`, `the last day of the period`, `the last day of a period of` n u `starting on` s, `the last day of a counted period of` n u `that` how anchor. |
| (2) | if an Act requires or allows a thing to be done and the last day is a Saturday, a Sunday or a holiday, it may be done on the next day that is not | encoded | `the last day on which the thing may be done`, `the first day from` d `that is not a Saturday, a Sunday or a holiday, given` closures, `the thing is done within the time allowed`; the Example (31 March a Saturday, application on Monday 2 April) is asserted with 2018 dates. |
| (3)(a), (b) | holiday: a public holiday in the place, and, where the office or place is closed for the whole day, that day | encoded | `is a holiday for the time for doing a thing`, `is a Saturday, a Sunday or a holiday` (fork F5). |

### Numbers repealed (endnote 4)

These section numbers do not appear in the body of this compilation; endnote 4 shows each as repealed ("rep").

| section | how shown |
|---|---|
| 5 | repealed in this text: rep No 46, 2011 |
| 8 | repealed in this text: rep No 46, 2011 |
| 8A | repealed in this text: rep No 46, 2011 |
| 8B | repealed in this text: rep No 46, 2011 |
| 8C | repealed in this text: rep No 46, 2011 |
| 9 | repealed in this text: rep No 46, 2011 |
| 14 | repealed in this text: rep No 46, 2011 |
| 14A | repealed in this text: rep No 46, 2011 |
| 14B | repealed in this text: rep No 46, 2011 |
| 15 | repealed in this text: rep No 46, 2011 |
| 15AE | repealed in this text: rep No 10, 2015 |
| 17 | repealed in this text: rep No 46, 2011 |
| 17AA | repealed in this text: rep No 46, 2011 |
| 18 | repealed in this text: rep No 46, 2011 |
| 18C | repealed in this text: rep No 46, 2011 |
| 19BA | repealed in this text: rep No 10, 2015 |
| 19BAA | repealed in this text: rep No 10, 2015 |
| 19BB | repealed in this text: rep No 10, 2015 |
| 19BC | repealed in this text: rep No 10, 2015 |
| 19BD | repealed in this text: rep No 10, 2015 |
| 22 | repealed in this text: rep No 46, 2011 |
| 22A | repealed in this text: rep No 46, 2011 |
| 22B | repealed in this text: rep No 46, 2011 |
| 22C | repealed in this text: rep No 46, 2011 |
| 24 | repealed in this text: rep No 120, 1987 |
| 25 | repealed in this text: rep No 46, 2011 |
| 25E | repealed in this text: rep No 46, 2011 |
| 26 | repealed in this text: rep No 46, 2011 |
| 27 | repealed in this text: rep No 46, 2011 |
| 27A | repealed in this text: rep No 46, 2011 |
| 28 | repealed in this text: rep No 46, 2011 |
| 30 | repealed in this text: rep No 120, 1987 |
| 31 | repealed in this text: rep No 52, 1964 |
| 32 | repealed in this text: rep No 10, 1937 |
| 41 | repealed in this text: rep No 120, 1987 |
| 42 | repealed in this text: rep No 120, 1987 |
| 43 | repealed in this text: rep No 120, 1987 |
| 44 | repealed in this text: rep No 120, 1987 |
| 45 | repealed in this text: rep No 120, 1987 |
| 45A | repealed in this text: rep No 120, 1987 |
| 45B | repealed in this text: rep No 120, 1987 |
| 46A | repealed in this text: rep No 140, 2003 |
| 46B | repealed in this text: rep No 10, 2015 |
| 48 | repealed in this text: rep No 140, 2003 |
| 48A | repealed in this text: rep No 140, 2003 |
| 48B | repealed in this text: rep No 140, 2003 |
| 49 | repealed in this text: rep No 140, 2003 |
| 49A | repealed in this text: rep No 140, 2003 |
| 50 | repealed in this text: rep No 140, 2003 |

### Front matter, endnotes, Schedules

| part of the file | disposition | why |
|---|---|---|
| title, compilation details and "About this compilation" (lines 1 to 23) | inert | Describes the compilation (number, date, what endnotes are, uncommenced amendments, modifications). It states no rule of the Act. |
| Endnotes 1 to 4 (lines 915 to 1880) | inert | The legislation history and amendment history. Endnote 3 gives this Act's own assent and commencement (12 July 1901), which `au-part1-application.l4` carries as two values with an `@ref`; the rest is a record of which amending Act changed which section, and states no rule. |
| Schedules | not applicable | The Act has no Schedules (s 13(1)(a) speaks of an Act with none, and the body ends with s 51). |

## Fork register

Each fork is a place the text leaves open or can be read two ways.
The fork ids F1 to F6 are also the headings of tests in `au-tests-time.l4`.

| id | question | readings seen | reading taken | text that licenses it |
|---|---|---|---|---|
| F1 | Does a period "from" a day, or "after" it, count that day? | (A) the day is excluded; (B) it is counted, so that s 2G, which counts months from "the start of any day", applies from that day | (A) for "from" and "after"; the day is counted for "at, on or with" and "between". A month from 15 December therefore ends on 15 January, whereas a month starting on 15 December ends on 14 January | s 36(1) table items 5 and 6; Examples 5, 6 and 7; s 2G(1) Example 1 |
| F2 | Is the last day inside the period? | (A) always; (B) never; (C) depends on the wording | (C): items 3 and 4 ("until", "end at, on or with") include it; item 7 ("end before") excludes it | s 36(1) table items 3, 4, 7; Examples 3, 4, 7 |
| F3 | Does the rest-day rule move the last day of a period counted in months or years, and what if several days in a row are rest days? | (A) only periods in days; (B) any period; (C) the next day, or the next day that is not a Saturday, a Sunday or a holiday | (B) and the next day that is not one: consecutive Saturday, Sunday and a holiday Monday are skipped together | s 36(2) speaks of "the last day for doing the thing" with no unit and of "the next day that is not a Saturday, a Sunday or a holiday" |
| F4 | How long is a week, and a year? | (A) not stated, so no answer; (B) a week is 7 days and a year is 12 months | (A) in the ordinary rules (NOTHING); (B) only in separately named ALTERNATIVE READING functions and in the seat question that says in its title that the Act does not state it | The body never mentions a week; "year" is defined nowhere (it appears in "calendar month", "calendar year" and "financial year", in examples, in s 37A and in ss 39 and 40); s 2G defines only the month |
| F5 | What is a "holiday" in s 36? | (A) a public holiday only; (B) the union of a public holiday in the place and a day the office is closed for the whole day; (C) both limbs at once (a day that is both) | (B). Saturdays and Sundays are named in s 36(2) and computed; the person lists the other days as one list. Kept apart from a "business day" (s 2B), which ignores office closures | s 36(3)(a) and (b); s 2B "business day" |
| F6 | Does s 3A fill the gap for an instrument that says nothing about commencement? | (A) yes, by analogy; (B) no: s 3A speaks of an Act and of Royal Assent | (B): an instrument that says nothing gets NOTHING from this text | s 3A(1), (2), (3) ("An Act", "the Royal Assent"); the Note to s 2(1) sends legislative instruments to the Legislation Act 2003, which is not in the text |
| F7 | What does "passed" mean in "an Act passed on 2026-03-10"? | (A) the day of Royal Assent; (B) the day Parliament finished passing it | (A): the input is the day of Royal Assent | s 3A(2) counts from "the day on which that Act receives the Royal Assent"; s 39 uses "assents thereto" |
| F8 | An Act that says it commences on a day to be fixed later: does s 3 (start of the day) reach the day once fixed? | (A) yes, a fixed day is "a particular day"; (B) no, because the Act was not "expressed to come into operation on a particular day" | (A): once fixed, the start of that day; until fixed, no day. Section 3A does not apply either way | s 3; s 3A(1) |
| F9 | When s 36(2) moves the last day on, are the days between the original last day and the new one still in time? | (A) yes, the period simply runs to the new last day; (B) only the one next non-rest day is allowed | (A): acting on a holiday between the two is within time (whether the office will receive it is a separate matter) | s 36(2) says the thing "may be done on the next day that is not" a rest day and says nothing to forbid the days before it |
| F10 | In s 33A(1)(ba), from when are the 12 months of acting counted? | (A) from the first day of acting, that day included; (B) from the day after | (A): the paragraph says the appointee must not act "for more than 12 months", a length of time acted. Contrast (c)(iii), "12 months from the day of the vacancy", which is item 5 of the s 36 table (day excluded) | s 33A(1)(ba), (c)(iii); s 36(1) item 5 |
| F11 | Does s 36(2) move the last day of an acting appointment's 12 months (s 33(4)(b))? | (A) yes; (B) no | (B): nothing is "done" on the day an appointment expires. The 12 months run from the day after the office was created or became vacant (item 6) | s 33(4)(b) ("the expiration of 12 months after"); s 36(2) ("a thing to be done") |
| F12 | In s 34C, which day ends "within 15 sitting days of that House after the day on which he or she receives the report", and is s 36(2) applied? | (A) the 15th sitting day strictly after the day of receipt, no rest-day shift; (B) the 15th, shifted if it is a Saturday, Sunday or holiday | (A): a sitting day is a day the House actually sits, so it is not treated as a rest day. The text does not say what happens if the 15th sitting day is a Saturday | s 34C(3), (6), (7)(b); s 36(1) item 6; s 2M |
| F13 | What is a sitting day for the House when a sitting runs past midnight? | (A) every calendar day on which the House sits at any time; (B) only the day the sitting began, with later days part of it | (B), as the Examples say. The encoding takes the days on which a sitting BEGAN | s 2M(1), (2) and Examples 1 and 2 |
| F14 | How many days is "the ordinary course of post"? | (A) the Act fixes a number; (B) it does not | (B): the delivery day is an input; the rule only says that service is taken to be effected then, unless the contrary is proved | s 29(1) |
| F15 | A person born on 29 February attains an age in a year with no 29 February: which day? | (A) 28 February; (B) 1 March; (C) the Act does not say | (C): NOTHING | s 37A ("the relevant anniversary of the date of the birth"); contrast s 2G, which has an end-of-month rule for months only |
| F16 | Is a "business day" the same as a day that is not a "holiday"? | (A) yes; (B) no | (B): a business day ignores office closures | s 2B "business day" ("not a Saturday, a Sunday or a public holiday"); s 36(3)(b) |
| F17 | Is a period that ends before 30 June 1983 a "periodic report" period? | (A) yes; (B) no | (B): the definition covers a period that ends on or after 30 June 1983, so for an earlier one s 34C(2) gives NOTHING | s 34C(1) ("ends on or after 30 June 1983") |

## What the text turns out to say

Each finding says what the text says on reading, in the order they arose.
"Asserted." means a case in this folder asserts it, with the expected value written from the text before the run.

1. Saying a period runs "from" a day, or "after" it, leaves that day out: a person with 28 days after a decision on 2 August has a period that begins on 3 August (Example 6), and the 7 days before 8 May are 1 to 7 May (Example 7). Asserted.
2. The end of a period of months is the day before the corresponding day, or the end of the month when there is none: a month starting on 31 August ends at the end of September (s 2G(1) Example 2), and 6 months starting on 31 October end at the end of April (s 2G(2) Example 2). Asserted.
3. Counting the starting day or not changes the answer by a day even for a month: a month from 15 December ends on 15 January, while a month starting on 15 December ends on 14 January. The wording of the period, not the arithmetic, decides which applies. Asserted.
4. A month from 31 January 2025 begins on 1 February and ends on 28 February 2025, whether or not 31 January is counted, because February has no 31st. Asserted.
5. The Act never says how long a week or a year is. The word "week" does not occur in the body of the Act at all. "Year" is defined nowhere: it appears in "calendar month" ("the 12 months of the year"), in "calendar year" and "financial year" (each "a period of 12 months"), in examples (ss 2G and 36), in s 37A ("an age expressed in years"), and as "the secular year" or "the year it was made" in ss 39 and 40. Section 2G defines only the month. So three years from 16 July 2025, five years from 15 January 2025 and from 1 September 2025, two years from 28 February 2024 and one year from 29 February 2024 have no answer in the text. Asserted (NOTHING), with the 7-day / 12-month result separately asserted as an alternative reading.
6. Section 36(2) moves the last day of ANY period, including one counted in months or years, and moves it past several rest days in a row: the next day that is not a Saturday, a Sunday or a holiday. The text's own example (31 March a Saturday, application on Monday 2 April) is asserted. Asserted.
7. A "holiday" for the time for doing a thing is a public holiday in the place where it is to be done, or a day the office is closed for the whole day. The Act lists neither, so no encoding can be complete; the person supplies the days. A business day (s 2B) is a different test and ignores office closures. Asserted.
8. An Act that says nothing about commencement commences on the 28th day after the day it receives the Royal Assent (s 3A(2)); an Act to alter the Constitution commences on the day of Royal Assent (s 3A(3)); and an Act, or provision, expressed to commence on a particular day does so at the start of that day (s 3). An Act assented to on 10 March 2026 and silent therefore commences at the start of 7 April 2026. Asserted.
9. Section 3A applies to an Act "so far as it provides for its commencement" only when the Act is silent (s 3A(1)); it says nothing about an Act that names a day to be fixed later, so until that day is fixed the text gives no day, and once it is fixed as 1 June 2026 the Act commences at the start of that day (s 3, reading F8). Asserted.
10. The Act gives no default commencement for subordinate legislation. Section 3A speaks of an Act and its Royal Assent; the Note to s 2(1) says the Act also applies to legislative instruments and notifiable instruments, and a Note to s 46 says the Legislation Act 2003 contains the parallel. That Act is not in the text, so a legislative instrument made on 10 March 2026 that says nothing has no commencement day in this text. Asserted (NOTHING).
11. Service by post is taken to be effected at the time the letter would be delivered in the ordinary course of post, unless the contrary is proved; the Act gives no number of days (s 29(1)). Asserted.
12. A person attains an age at the START of the anniversary of the date of birth (s 37A). For a birth on 29 February and an anniversary year with no 29 February, the Act says nothing. Asserted (NOTHING).
13. Under s 28A the methods listed for a natural person (delivery to them personally; leaving it at, or posting it to, the last known place of residence or business) and for a body corporate (leaving it at, or posting it to, the head, a registered or a principal office) are DISJOINT: personal delivery is not listed for a body corporate, nor head-office service for a natural person. Section 28A(2) preserves any other law or court order that authorises another method. Asserted.
14. For a periodic report with no period specified, the deadline is 6 months after the end of the period reported on, "after" leaving the last day out (s 34C(2)). The Act "requires" the report, so s 36(2) can move it: a period ending 31 August 2025 has its 6 months end on 28 February 2026, a Saturday, so Monday 2 March 2026. Asserted.
15. For the statement explaining a late report the deadline is 14 days after the end of the specified period or extension (s 34C(7)(a)), moved by s 36(2) in the same way. Asserted.
16. The sitting-day deadlines of s 34C (15 sitting days for a report, 3 for a statement) count sitting days strictly after the day of receipt (or of the grant), and a sitting that runs past midnight counts only for the day it began. The text does not say whether s 36(2) can move a last day that is a sitting day falling on a Saturday (fork F12). Asserted for the counting; the Saturday case is not answered.
17. Sections 34C(7A) and (8) take three bodies (ASIO, the Australian Signals Directorate, the Office of National Intelligence) out of s 34C(3), and (6)(c) is disregarded for them after an extension; the Australian Secret Intelligence Service is outside the section altogether. Asserted.
18. The two twelve-month limits on acting appointments count differently: for a vacant office the appointee must not act "for more than 12 months" (first day of acting counted), whereas an acting appointee who stays on after the office they were acting in becomes vacant may continue until the first of a direction, the vacancy being filled, or "a period of 12 months from the day of the vacancy" ends (the vacancy day is not counted). Asserted.
19. The listed rights, privileges, obligations and liabilities accrued before a repeal or amendment survive it, and a repeal does not revive what was not in force; both are subject to a contrary intention (s 7(2), s 2(2)). Repealing the repealing Act revives the old Act only if express provision is made (s 7(1)). Asserted.
20. Under s 46AA an instrument may apply or incorporate an Act, a disallowable legislative instrument or rules of court "as in force from time to time", but any other instrument or writing only as in force or existing when the instrument commences or at a time before it. A form is outside the section (s 46AA(4)). Asserted.
21. The Act's own dates are in endnote 3: assent 12 July 1901, commencement 12 July 1901. They are carried as two values with an `@ref` to the endnote. Asserted (the two values).
22. The s 2B definitions of "Australia" and "Commonwealth", in a geographical sense, include Norfolk Island, the Territory of Christmas Island and the Territory of Cocos (Keeling) Islands but no other external Territory. Asserted.

## Answer table: the worked cases

Each answer was written from the text before it was run; the seat cases in `au-cases-seat.l4` and the time tests in `au-tests-time.l4` assert them.
Every move below is by s 36(2), and happens only where an Act requires or allows a thing to be done within the period; the weekday of the unmoved last day is given so a reader can see why.

| case | answer | text |
|---|---|---|
| three years from 2025-07-16 | The text is silent on the length of a year (finding 5). Alternative reading (a year is 12 months): from 17 July 2025, 36 months end on 16 July 2028, a Sunday. If an Act requires or allows a thing to be done within the period, s 36(2) moves the last day to Monday 17 July 2028; otherwise it stays 16 July 2028. | s 36(1) item 5; s 2G; no definition of "year" (fork F4) |
| five years from 2025-01-15 | Text silent. Alternative reading: ends 15 January 2030, a Tuesday. | same |
| five years from 2025-09-01 | Text silent. Alternative reading: ends 1 September 2030, a Sunday. If an Act requires or allows a thing to be done within the period, moved to Monday 2 September 2030; otherwise it stays 1 September 2030. | same |
| thirty days from 2026-01-01 | The period is 2 to 31 January 2026 ("from" leaves out 1 January). 31 January is a Saturday. If an Act requires or allows a thing to be done within the period, s 36(2) moves the last day to Monday 2 February 2026 (to Tuesday 3 February if 2 February is a holiday or the office is closed all day); otherwise it stays 31 January 2026. | s 36(1) item 5; s 36(2), (3) |
| two years from 2024-02-28 | Text silent. Alternative reading: from 29 February 2024, 24 months end on 28 February 2026, a Saturday. If an Act requires or allows a thing to be done within the period, moved to Monday 2 March 2026; otherwise it stays 28 February 2026. | same as three years |
| one year from 2024-02-29 | Text silent. Alternative reading: from 1 March 2024, 12 months end immediately before 1 March 2025, which is 28 February 2025, a Friday. | s 2G(2); fork F4 |
| one month from 2025-01-31 | From 1 February 2025 the month ends immediately before 1 March 2025: 28 February 2025, a Friday. | s 36(1) item 5; s 2G(1) |
| an Act passed on 2026-03-10 that says nothing about when it comes into force | Commences on the 28th day after the day of Royal Assent (10 March plus 28 days): 7 April 2026, a Tuesday, at the start of that day. | s 3A(2); s 3 |
| an Act that says it comes into force on a day to be fixed later, the day being fixed as 2026-06-01 | Section 3A does not apply (s 3A(1)). Until the day is fixed the text gives no day. Once fixed, it comes into operation at the start of 1 June 2026, a Monday (fork F8). | s 3A(1); s 3 |
| subordinate legislation made on 2026-03-10 that says nothing about when it comes into force | The text is silent: s 3A speaks of an Act and its Royal Assent, and the Legislation Act 2003, which the Notes to ss 2 and 46 point to for such instruments, is not in the text (fork F6). | s 3A; Notes to ss 2(1) and 46 |

## The seat's questions

31 questions, each with `@export` and an `@desc` on every input, grouped under `§§` headings in the text's order (9 groups).

- Does the Acts Interpretation Act 1901 apply to the Act that binds me (s 2)?
- Is this day a business day (s 2B)?
- On which day does the financial year that includes my day end (s 2B)?
- Which day is the Nth sitting day of the House after my day (ss 2M, 36)?
- On which day does the Act or instrument that binds me come into operation (ss 3, 3A)?
- At what moment does the Act or instrument that binds me come into operation (ss 3, 3A)?
- What happens to what I already have or owe when the Act is repealed or amended (s 7(2))?
- Does repealing the Act that repealed my old Act bring my old Act back (s 7(1))?
- Does my form meet the requirement if it does not comply strictly with the prescribed form (s 25C)?
- Are the written reasons I was given complete (s 25D)?
- Was the document served on me in a way the Acts Interpretation Act allows (s 28A)?
- On which day am I taken to have been served by post (s 29)?
- Until which day may I keep acting in a vacant office (s 33A(1)(ba))?
- Until which day may I keep acting after the office I was acting in became vacant (s 33A(1)(c))?
- On which day do the 12 months of an appointment to act under a power to appoint run out (s 33(4))?
- By which day must I furnish my periodic report to the Minister (s 34C(2))?
- Can I still ask the Minister for more time to furnish my report (s 34C(4))?
- By which day must I explain in writing why my report was late (s 34C(7))?
- By which day must the Minister lay my report before a House, when no extension was granted (s 34C(3))?
- By which day must the Minister lay my report before a House, when an extension was granted (s 34C(6)(c))?
- By which day must the Minister lay my explanation and the extension before a House (s 34C(6)(a))?
- By which day must the Minister lay my explanation for a late report before a House (s 34C(7)(b))?
- Does the day I am counting from count as part of my period (s 36(1))?
- On which day does my period begin (s 36(1))?
- On which day does my period of days, weeks, months or years end (ss 2G, 36)?
- On which day would my period end if a week were 7 days and a year were 12 months (a reading the Act does not state)?
- On which day does my period end when the Act ends it at, with, or before a named day (s 36(1))?
- Is the last day of my period a day I cannot act on, because it is a Saturday, a Sunday or a holiday (s 36(2), (3))?
- What is the last day on which I may act, if my period ends on a Saturday, a Sunday or a holiday (s 36(2))?
- Am I in time if I act on this day (s 36)?
- At what moment do I attain a given age (s 37A)?

The seat leaves out, as addressing only officials: s 4 (a power exercised before an Act commences), s 6 (evidence of the date of assent), ss 33 and 33B to 34AB apart from the acting limits, and Parts 9, 10 and 11, which concern how Acts and instruments are cited, made and read.

## What the stable binary does not accept

Measured with `l4` 1.6.98 (main, 7689b0d, 2026-10-19) in this run.

- **`YMD` is not defined.** A shim, `YMD y m d MEANS Date d m y`, is defined once, in `au-interpretation-time.l4`; the other modules import that file.
- **`NOT a OR b` parses as `NOT (a OR b)`.** Every `NOT` is parenthesised. A sitting-day rule written without the brackets returned the wrong answer on one assertion, found by that assertion and fixed in the module.
- **`x NOT EQUALS y` is a parse error** ("unexpected ("). Write `NOT (x EQUALS y)`.
- **A constructor pattern binds its fields by position.** `WHEN `a constructor` d THEN` names the first field; there is no way to leave a field out.
- **A multi-line `LIST` with leading commas breaks layout**, so every list in the tests is a one-line named fixture.
- **`IMPORT` of a hyphenated module name needs backticks**, and finds only modules in the same folder; a name defined in two imported modules cannot be used (the daydate names `the day before`, `the day after`, `the later of` and `the earlier of` collided with names I had chosen).
- **`daydate`'s `add months` and `add years` clamp** (31 January plus one month is 28 February), so they are not used: s 2G is written from the text.
- **`Date d m y` is lenient**: `Date 31 2 2025` rolls over to 3 March 2025. The module checks `Days in month` where a non-existent day matters (s 37A).
- **`l4 batch` cannot re-print a seat file with a `LIST OF` input that is not the last input of its `GIVEN`.** It reports `incorrect indentation (got 3, should be greater than 43)` at the next input. The same file passes `l4 check` and `l4 run`. So every seat question puts its single list last, and the two lists the module takes (public holidays; closed days) are asked as one.
- **`l4 batch` cannot re-print a lambda (`GIVEN x YIELD ...`) in the exporting file.** It reports that it "could not find a definition for the identifier" the lambda's variable, again while `l4 check` and `l4 run` pass. The seat uses a named helper instead; the layer-1 modules, which batch loads rather than re-prints, still use lambdas.
- After those two were avoided, all 31 seat questions ran through `l4 batch` with a JSON row each, with no error.
- Not tried here, avoided because the brief says the stable binary rejects them: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, section-level `GIVEN`, `TYPICALLY`, sets.

## What check.sh prints

`L4=l4 L4_TARGET=unstable ./check.sh`, exit status 0:

```
module                                    errors satisfied  failed  refused  expected
au-cases-seat.l4                               0       124       0        0         0
au-interpretation-time.l4                      0         0       0        0         0
au-part1-application.l4                        0         0       0        0         0
au-part10-11-instruments.l4                    0         0       0        0         0
au-part2-definitions.l4                        0         0       0        0         0
au-part3-commencement.l4                       0         0       0        0         0
au-part4-repeal.l4                             0         0       0        0         0
au-part5-interpretation.l4                     0         0       0        0         0
au-part6-service.l4                            0         0       0        0         0
au-part7-powers.l4                             0         0       0        0         0
au-part8-distance.l4                           0         0       0        0         0
au-part9-citation.l4                           0         0       0        0         0
au-seat.l4                                     0         0       0        0         0
au-tests-part1.l4                              0         8       0        0         0
au-tests-part10-11.l4                          0        27       0        0         0
au-tests-part2.l4                              0        62       0        0         0
au-tests-part3.l4                              0        17       0        0         0
au-tests-part4.l4                              0        30       0        0         0
au-tests-part5.l4                              0        41       0        0         0
au-tests-part6.l4                              0        15       0        0         0
au-tests-part7.l4                              0        60       0        0         0
au-tests-part8.l4                              0         5       0        0         0
au-tests-part9.l4                              0        37       0        0         0
au-tests-time.l4                               0       134       0        0         0
TOTAL (24 modules)                             0       560       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs <raw text> <every au-*.l4>` printed:

```
srcrefs check: 425 src: lines, 80 runs, 108 locators, 0 problems
```

`python3 -I srcrefs.py check --strict <raw text> <every au-*.l4>` printed:

```
srcrefs check: 425 src: lines, 80 runs, 108 locators, 0 problems
```

`l4 check` over each file, searched for the layout warnings "is at the end of the file" and "follows code on its line": 0 hits; warnings of any kind: 0.

Earlier in the work, one assertion in `au-tests-time.l4` failed because of a defect in the module (the `NOT a OR b` precedence trap above); the module was fixed and the expected value was left alone.

Two assertions failed on a first run later and were not findings about the text; both were mistakes in my hand-written expected values, found by re-deriving them from the text and a calendar, not by copying the program's answer:

- `au-tests-part7.l4`, a periodic report whose period ended on 30 June 1983: I wrote 30 December 1983 for the end of the 6 months. Six months after 30 June begin on 1 July and end immediately before 1 January, which is 31 December 1983, a Saturday, so Monday 2 January 1984.
- `au-cases-seat.l4`, acting on 2 February 2026 when that Monday is a listed holiday and the last day is Saturday 31 January: I wrote not in time. Section 36(2) lets the thing be done on the next day that is not a rest day (3 February) and says nothing to forbid the days before it; the program was right and the case now records fork F9.

## What would need doing before this encoding is worth relying on

1. A lawyer who knows Commonwealth drafting should read every fork in the register against the Act, in particular F1 to F5 (the counting rules) and F8 (a day fixed later).
2. The Legislation Act 2003 is not in the text, and the Acts Interpretation Act points at it for legislative and notifiable instruments (the Notes to ss 2(1) and 46). Without it, the commencement of subordinate legislation is NOTHING here.
3. The question of how long a week and a year are needs an authority outside this Act (a case, or the Legislation Act 2003); the ALTERNATIVE READING functions assume 7 days and 12 months.
4. Public holidays and office closures must be supplied by the person for each place; no list is bundled.
5. Time of day and time zone (s 37) are not modelled; an Act in force from "the start of a day" is a day plus 00:00:00 with no zone.
6. The seat's page for Legalese Cloud has not been deployed; only `l4 batch` was run against the questions.
7. The text is a converter's rendering. Its wording has not been compared line by line with the official compilation, although every `-- src:` line was produced mechanically from it and `srcrefs.py` checks the quotes against it.

## Files

- `BRIEF.md`
- `NOTES.md`
- `PROGRESS.md`
- `SOURCE-LICENSE.md`
- `au-cases-seat.l4`
- `au-interpretation-time.l4`
- `au-part1-application.l4`
- `au-part10-11-instruments.l4`
- `au-part2-definitions.l4`
- `au-part3-commencement.l4`
- `au-part4-repeal.l4`
- `au-part5-interpretation.l4`
- `au-part6-service.l4`
- `au-part7-powers.l4`
- `au-part8-distance.l4`
- `au-part9-citation.l4`
- `au-seat.l4`
- `au-tests-part1.l4`
- `au-tests-part10-11.l4`
- `au-tests-part2.l4`
- `au-tests-part3.l4`
- `au-tests-part4.l4`
- `au-tests-part5.l4`
- `au-tests-part6.l4`
- `au-tests-part7.l4`
- `au-tests-part8.l4`
- `au-tests-part9.l4`
- `au-tests-time.l4`
- `check.sh`
- `encoding.json`
- `srcrefs.py`
