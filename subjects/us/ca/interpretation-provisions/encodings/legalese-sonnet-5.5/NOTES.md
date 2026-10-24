# NOTES: California interpretation provisions, row `legalese-sonnet-5.5`

**Status: draft.**
No domain expert has read this encoding against the statute.
The row was written by one Sonnet 5.5 agent working alone from a brief, with no second pass by a fresh session (step 8 of the skill was not run: the brief allowed no subagents).

**The source text.**
The six `.txt` files this encoding was written from are a converter-made plain-text rendering of California Legislative Information (the Legislature's bulk file), not the official text.
Nothing here was checked against the official text.
Every quotation in the modules (`-- src:ID:N | text` lines) was copied by script from those files and checked against them by `srcrefs.py check --refs` (the tool of the encoding skill, `/Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/srcrefs.py`, documented in its `references/source-locators.md`), which reports 0 problems for each of the four modules.
That proves the quotation is the deposited text; it does not prove the deposited text is the law.
The terms of the source are in `SOURCE-LICENSE.md`.

## What is encoded, and what is not

**Scope.**
California has no single interpretation act; Gov. Code § 9603 says the general rules of construction are in the preliminary provisions of the different codes.
The deposit therefore holds six files, 159 sections: Gov. Code §§ 1-26, Civ. Code §§ 1-23.6, Code Civ. Proc. §§ 1-34, Gov. Code §§ 6700-6736 (holidays), §§ 6800-6808 (computation of time) and §§ 9600-9612 (operation of statutes and resolutions).
The coverage table below has a row for every one of those sections and a second table for the seven numbers the text does not contain.

**The questions the brief asked, and where they are answered.**

| Question | Where | In one line |
|---|---|---|
| Commencement of a statute, a resolution, the codes | `usca-interpretation-time.l4`, section `When an enactment goes into effect` | Gov. Code § 9600(a) and (b), § 9602, Civ. Code § 2, Code Civ. Proc. § 2, with the moment within the day; an Act that names its own day, subordinate legislation and the Government Code's own day are refused |
| Counting days, weeks, months, years | same, sections `Counting a period` and `Year, half year and quarter of a year` | § 6800, § 6803, § 6804, § 6805; a month with no day of the start day's number is refused |
| Rest days and holidays | same, section `The last day of a period when it falls on a holiday`, and `usca-holidays.l4` | The calendar is an input; the holidays module offers the Government Code, Civil Code and Code of Civil Procedure calendars |
| Deemed service or notice | `usca-general-provisions.l4` | The deposit has no general rule; both functions refuse and say so; nothing was invented |
| Repeal | `usca-operation-of-statutes.l4` | Gov. Code §§ 9605-9611 (and 9604), Civ. Code § 20, Code Civ. Proc. § 18 |
| Time words | `usca-interpretation-time.l4` | Gov. Code §§ 6803-6806 (year, half year, quarter, month, week, day), § 6807 (daytime), § 6808 (daylight saving time) |

**What is not encoded, and why.**
The coverage table says, section by section, which sections are `inert` (a canon or a definition with no input that could change its answer), `not applicable` (the section is about something other than interpretation, time, commencement, repeal or notice) or absent from the text.
Beyond that, these parts of encoded sections are not encoded:
- Gov. Code § 6700(b) (a memorandum of understanding controls in a conflict), which turns on the content of an agreement;
- Gov. Code § 6808(c) (the Legislature may amend by a two-thirds vote);
- the dates of Lunar New Year, Diwali, Good Friday, Thanksgiving Day and of days appointed by the President or Governor, which the text does not compute and which are inputs;
- the content of Code Civ. Proc. § 135, which is not in the deposit.

## Target, build and layout

- **Target: `unstable`.** The brief requires `REFUSE` and `@lang en`, which `main` does not read.
  `check.sh` defaults to target `unstable`; with that target it prints that the main check was skipped, and there is no `fetch-main-l4.sh` in this row.
  Do not file this row for `main`.
- **Build.** `l4 --version` prints `dev`.
  The binary is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`, also recorded in `encoding.json`.
  `JL4_LIBRARY_PATH` was left unset throughout.
- **Modules, in reading order.**
  1. `usca-interpretation-time.l4` imports only `prelude` and `daydate`, as the brief requires.
     It has no holiday and no rest day in it: every function that needs a calendar takes it as an input of type `FUNCTION FROM DATE TO BOOLEAN`.
     The nouns it needs (`Moment`, `Kind of enactment`, `Enactment of a statute`) are declared in it; there is no separate nouns module.
  2. `usca-holidays.l4` imports `prelude`, `daydate` and the time module.
     It builds the calendars the time module takes, from the days the text fixes by the calendar and from lists the caller supplies for what the text does not compute.
  3. `usca-operation-of-statutes.l4` imports `prelude` and `daydate`: amendment, repeal, revival, retroactivity, continuation, conflicts among provisions.
  4. `usca-general-provisions.l4` imports `prelude`: "shall" and "may", joint authority, signature by mark, digital and electronic signature, notice, "writing", "State", the Air Force.
- **Tests** are at the top level (`check.sh` globs `*.l4` non-recursively): `test-usca-time.l4`, `test-usca-rules.l4`, `test-usca-holidays.l4`, `test-usca-operation.l4`, `test-usca-general.l4`, `test-usca-worked.l4`, and `tests-red.l4`, which is meant to fail (see "What `check.sh` prints").
- **How the calendars are meant to be used.**
  The caller builds a `Days supplied by the caller` record (or uses `no day is supplied`) and passes the time module a function from a date to a Boolean.
  A mixfix function is not partially applicable in L4, so the calendar is a named function of one date (`calendar G` in `test-usca-worked.l4`) or a lambda (`GIVEN x YIELD ...`, used in `test-usca-holidays.l4`).

**Conventions.**
- `FALSE` means "this section does not give this result"; `REFUSE` means an antecedent is undetermined or the section has no consequence for the case.
  No module has a home-made three-valued type.
- A moment is a day and a count of seconds after the midnight that begins it (fork F-midnight).
- Every refusal is a named `REFUSE "..."` whose message says what the text does not say; the tests assert the message exactly.

## Coverage table

| Provision | Text file : line | Disposition | What is encoded, or why not |
|---|---|---|---|
| Gov. Code § 1 | GOV-ss-1-26.txt:8 | inert | Gives the Act its citation name, "the Government Code". A citation form: no date, period or fact can change what it says, so there is nothing to compute. |
| Gov. Code § 2 | GOV-ss-1-26.txt:10 | encoded | `usca-operation-of-statutes.l4`: Provisions substantially the same as existing statutory provisions on the same subject are continuations, not new enactments. One function serves this section, Civ. Code § 5 and Code Civ. Proc. § 5, taking the kind of code as an input (Civ. Code § 5 adds the common law to the existing statutes, Code Civ. Proc. § 5 does not). Functions: `the section construes a provision of`. |
| Gov. Code § 3 | GOV-ss-1-26.txt:12 | encoded | `usca-operation-of-statutes.l4`: Holders of office under acts repealed by the code, in offices the code continues, keep them on their former tenure. Functions: `a holder of an office under a repealed act continues to hold it under Gov. Code § 3`. |
| Gov. Code § 4 | GOV-ss-1-26.txt:14 | encoded | `usca-operation-of-statutes.l4`: Proceedings begun and rights accrued before the code takes effect are unaffected; later procedure conforms "so far as possible". Functions: `the section protects an action, proceeding or accrued right from the code`; `procedure taken after the code took effect in a proceeding begun before must conform to the code`. |
| Gov. Code § 5 | GOV-ss-1-26.txt:16 | encoded | `usca-operation-of-statutes.l4`: The general provisions govern construction of the Government Code unless the provision or context requires otherwise; used to bound the scope of §§ 1-26 (a fork, see NOTES). Functions: `the general provisions of the Government Code govern the construction of the code`. |
| Gov. Code § 6 | GOV-ss-1-26.txt:18 | inert | Headings of titles, divisions, parts, chapters, articles and sections do not affect scope, meaning or intent. A canon about how to read the text: it has no input fact that could change its answer, and the plain-text deposit carries no headings to apply it to. |
| Gov. Code § 7 | GOV-ss-1-26.txt:20 | encoded | `usca-general-provisions.l4`: A power or duty of a public officer may be exercised or performed by a deputy or a person the officer authorises under law, unless the code expressly provides otherwise. Functions: `a power of a public officer may be exercised, or a duty performed, by`. |
| Gov. Code § 7.5 | GOV-ss-1-26.txt:22 | not applicable | Lets the director of a state department designate a deputy director in a position named in the Constitution to sit on a state board in the director's place, counted for quorum and voting, at most one director being represented at a meeting. Board-membership machinery for state departments; no question about time, commencement, repeal or the meaning of words turns on it, and the positions it names are in the Constitution, which is not deposited. |
| Gov. Code § 7.6 | GOV-ss-1-26.txt:24 | not applicable | The same device for officers whose offices the Constitution creates (Lieutenant Governor, Chief Justice, Attorney General, Superintendent of Public Instruction), with officer-by-officer limits in (b)-(f). Organisational detail about who may sit on boards; nothing in it is computed from a date or a fact about a statute. |
| Gov. Code § 7.7 | GOV-ss-1-26.txt:31 | not applicable | Says §§ 7.5 and 7.6 do not affect or modify § 7. A saving clause that preserves § 7 and adds no rule of its own. |
| Gov. Code § 7.8 | GOV-ss-1-26.txt:33 | not applicable | Lets the Directors of Finance, General Services and Education appoint any deputy or assistant director to sit on the State Allocation Board. Board-membership machinery for one body, outside every question this encoding answers. |
| Gov. Code § 7.9 | GOV-ss-1-26.txt:35 | not applicable | Lets the Controller, Treasurer, Director of Finance and Superintendent of Public Instruction designate a deputy to sit on state boards (a), with a staffing direction in (b) and a limit in (c). Board and staffing machinery for named offices, not a rule of interpretation. |
| Gov. Code § 7.9a | GOV-ss-1-26.txt:39 | not applicable | Gives the Controller two more career-executive positions. A staffing provision with no bearing on interpretation, time, commencement or repeal. |
| Gov. Code § 8 | GOV-ss-1-26.txt:41 | encoded | `usca-general-provisions.l4`: "Writing" includes any recorded message capable of comprehension by ordinary visual means; notices, reports, statements and records required or authorised by the code are in writing in English unless otherwise provided (the nearest the deposit comes to a language-of-record rule). Functions: `a message is a writing`; `a notice, report, statement or record required or authorized by the Government Code is made as the code requires`; `the version of a document in two languages that has authority`. |
| Gov. Code § 9 | GOV-ss-1-26.txt:43 | encoded | `usca-operation-of-statutes.l4`: A reference to any portion of the code or of any other State law applies to all amendments and additions made before or after the reference. Functions: `a reference to a portion of the Government Code or of another law of this State applies to its amendments and additions, whenever made`. |
| Gov. Code § 10 | GOV-ss-1-26.txt:45 | inert | "Section" means a section of this code unless another statute is specifically mentioned; "subdivision" means a subdivision of the section in which the term occurs unless another section is expressly mentioned. A definition whose application depends on the wording of the text being read, which no function over facts can see. |
| Gov. Code § 11 | GOV-ss-1-26.txt:47 | inert | The present tense includes the past and future tenses, and the future the present. A canon of construction; the brief allows these to stay inert, and no input fact changes the answer. |
| Gov. Code § 12 | GOV-ss-1-26.txt:49 | inert | The masculine gender includes the feminine and neuter. A canon of construction with no computable output. |
| Gov. Code § 12.2 | GOV-ss-1-26.txt:51 | inert | "Spouse" includes "registered domestic partner", as Family Code § 297.5 (not deposited) requires. A one-line widening of a word's meaning; none of the modules models persons or marriage. |
| Gov. Code § 12.5 | GOV-ss-1-26.txt:53 | inert | Declares the Legislature's intent that "man" or "men" be read, and amended, as "person" or "persons". An instruction to drafters about future amendments, declaratory not operative. |
| Gov. Code § 13 | GOV-ss-1-26.txt:55 | inert | The singular includes the plural and the plural the singular. A canon of construction with no computable output. |
| Gov. Code § 14 | GOV-ss-1-26.txt:57 | encoded | `usca-general-provisions.l4`: "Shall" is mandatory and "may" is permissive (function from the word to its force). Functions: `the force of the word in the Government Code word`. |
| Gov. Code § 15 | GOV-ss-1-26.txt:59 | inert | "Oath" includes affirmation. A one-line definition; the modules model no oaths. |
| Gov. Code § 16 | GOV-ss-1-26.txt:61 | encoded | `usca-general-provisions.l4`: A signature or subscription includes a mark when the signer cannot write, the name being written near it by a witness; to be acknowledged or to serve on a sworn statement the mark needs two witnesses who sign their own names. Functions: `a mark is a signature or subscription`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement`. |
| Gov. Code § 16.5 | GOV-ss-1-26.txt:63 | encoded | `usca-general-provisions.l4`: (a) A digital signature has the force and effect of a manual signature if and only if the public entity elects to use it and it embodies all five attributes (unique, verifiable, under sole control, linked to data, conforming to Secretary of State regulations); (b) use or acceptance is at the option of the parties and no public entity is required to use one; (c) signatures employed under Public Resources Code § 71066 are exempt; (d)-(f) are definitions and notes that limit nothing and stay inert. Functions: `a digital signature has the same force and effect as a manual signature`; `a public entity is required to use or permit the use of a digital signature`; `Gov. Code § 16.5 applies to the digital signature`. |
| Gov. Code § 17 | GOV-ss-1-26.txt:76 | inert | Defines "person" to include firm, association, organization, partnership, limited liability company, business trust, corporation or company. A list definition; nothing here asks who is a person. |
| Gov. Code § 18 | GOV-ss-1-26.txt:78 | encoded | `usca-general-provisions.l4`: "State" means California unless applied to the different parts of the United States, when it includes the District of Columbia and the territories. Functions: `the meaning of State in the Government Code`. |
| Gov. Code § 19 | GOV-ss-1-26.txt:80 | inert | "County" includes "city and county". A one-line definition. |
| Gov. Code § 20 | GOV-ss-1-26.txt:82 | inert | "City" includes "city and county" and "incorporated town" but not "unincorporated town" or "village". A list definition about types of local government. |
| Gov. Code § 21 | GOV-ss-1-26.txt:84 | inert | "Town" includes "unincorporated town" and "village". A list definition. |
| Gov. Code § 22 | GOV-ss-1-26.txt:86 | inert | "Process" includes a writ or summons issued in judicial proceedings, civil or criminal. A one-line definition. |
| Gov. Code § 23 | GOV-ss-1-26.txt:88 | inert | Severability: if a provision or its application is held invalid, the rest is unaffected. Whether anything has been "held invalid" is a fact about a court's decision, and the only output is that the remainder stands; there is no calculation to encode. |
| Gov. Code § 24 | GOV-ss-1-26.txt:90 | inert | Declares the Legislature's intent that "workmen's compensation" also be known as "workers' compensation" and be so changed when sections are amended. A terminology direction to drafters, declaratory and not operative. |
| Gov. Code § 25 | GOV-ss-1-26.txt:92 | not applicable | Defines "assessed value" for the property tax (25 percent of full value through 1980-81, 100 percent from 1981-82) and gives tax-rate conversion factors in (c). Property-tax arithmetic, not interpretation. One reading problem, noted here for whoever encodes it: (c) multiplies a dollars-per-$100 rate by "twenty-five hundredths of 1 percent" and a percentage rate by 400, which are consistent only if the percentage is read as a fraction, and the text does not say so. |
| Gov. Code § 26 | GOV-ss-1-26.txt:96 | inert | Says "recycled water" and "reclaimed water" have the meaning Water Code § 13050(n) gives "recycled water". The content is in a section that is not deposited, and no function here reads the word, so there is nothing to compute; a named refusal would only mark a gap no rule can reach. |
| Civ. Code § 1 | CIV-ss-1-23.6.txt:8 | inert | Names the Act the Civil Code and lists its four divisions. A citation form with no computable content. |
| Civ. Code § 2 | CIV-ss-1-23.6.txt:14 | encoded | `usca-interpretation-time.l4`: The Civil Code takes effect at 12 o'clock noon on 1 January 1873 (function giving the day and the moment). Functions: `the moment the Civil Code takes effect`. |
| Civ. Code § 3 | CIV-ss-1-23.6.txt:16 | encoded | `usca-operation-of-statutes.l4`: No part of the code is retroactive unless expressly so declared. Functions: `a part of the Civil Code or the Code of Civil Procedure is retroactive`. |
| Civ. Code § 4 | CIV-ss-1-23.6.txt:18 | inert | Abolishes the common-law rule that statutes in derogation of it are strictly construed, and says the code is liberally construed to effect its objects and promote justice. A canon of construction; nothing to compute. |
| Civ. Code § 5 | CIV-ss-1-23.6.txt:20 | encoded | `usca-operation-of-statutes.l4`: Provisions substantially the same as existing statutes or the common law are continuations, not new enactments. Functions: `the section construes a provision of`. |
| Civ. Code § 6 | CIV-ss-1-23.6.txt:22 | encoded | `usca-operation-of-statutes.l4`: No action or proceeding begun before the code takes effect, and no accrued right, is affected by it. Functions: `the section protects an action, proceeding or accrued right from the code`. |
| Civ. Code § 7 | CIV-ss-1-23.6.txt:24 | encoded | `usca-holidays.l4`: Holidays within the meaning of the Civil Code are every Sunday and the days the Government Code specifies as holidays. Functions: `the section that says which days are holidays for kind` in `usca-interpretation-time.l4`; `a holiday under Civ. Code § 7 supplied d`; `the day is a holiday within the meaning of a provision of kind kind supplied d`. |
| Civ. Code § 7.1 | CIV-ss-1-23.6.txt:26 | encoded | `usca-holidays.l4`: Optional bank holidays (a)-(r): the computable paragraphs are encoded from the calendar; paragraph (a) (extraordinary closing) and Good Friday and Thanksgiving are inputs. Functions: `an optional bank holiday under Civ. Code § 7.1 supplied d`; `the moment falls in the Good Friday optional bank holiday of Civ. Code § 7.1(o)`. |
| Civ. Code § 9 | CIV-ss-1-23.6.txt:46 | encoded | `usca-holidays.l4`: All days other than those in § 7 are business days for all purposes, with provisos for acts to be performed at banks on optional bank holidays. Functions: `a business day under Civ. Code § 9 supplied d`; `a business day under Civ. Code § 9 for an act to be performed through a bank supplied d`; `an act appointed for an optional bank holiday may be performed on that day itself`; `the next business day after an optional bank holiday on which an act was appointed for a bank`. |
| Civ. Code § 10 | CIV-ss-1-23.6.txt:49 | encoded | `usca-interpretation-time.l4`: Period counting for acts provided by law, identical in words to Gov. Code § 6800 and Code Civ. Proc. § 12. Functions: `before the rest-day rule, the last day of n days counted from firstDay`; `with a holiday last day also excluded, once holiday d`; `the last day of a period of`; `the date d falls inside the period after firstDay through lastDay`. |
| Civ. Code § 11 | CIV-ss-1-23.6.txt:51 | encoded | `usca-interpretation-time.l4`: An act of a secular nature appointed for a particular day that falls on a holiday may be performed on the next business day. Functions: `the latest day on which an act appointed for`. |
| Civ. Code § 12 | CIV-ss-1-23.6.txt:53 | encoded | `usca-general-provisions.l4`: Joint authority given to three or more public officers or persons is exercised by a majority unless otherwise expressed. Functions: `a joint authority may be exercised by those acting`. |
| Civ. Code § 13 | CIV-ss-1-23.6.txt:55 | inert | Words and phrases are construed by context and approved usage; technical or peculiar legal meanings, or those defined in the next section, control. A canon of construction with no input fact. |
| Civ. Code § 14 | CIV-ss-1-23.6.txt:57 | encoded | `usca-interpretation-time.l4`: Definitions: "month" means a calendar month (encoded in the time module) and signature by mark (encoded in the general-provisions module); the present-tense, gender, number, person, county, writing, oath, property, will, section and spouse limbs are canons and one-line definitions and stay inert. Functions: `the section that defines month for kind`; `a mark is a signature or subscription` in `usca-general-provisions.l4`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement` in `usca-general-provisions.l4`. |
| Civ. Code § 17 | CIV-ss-1-23.6.txt:69 | encoded | `usca-general-provisions.l4`: Where the Civil Code requires registered mail, certified mail is a sufficient compliance. Functions: `a requirement of the Civil Code or the Code of Civil Procedure that a notice be mailed by registered mail is met by`; `the day service by mail is deemed made, the document having been mailed on`; `the day a notice is deemed given, the notice having been sent on the day the notice is sent`. |
| Civ. Code § 18 | CIV-ss-1-23.6.txt:71 | encoded | `usca-general-provisions.l4`: Notice is actual (express information of a fact) or constructive (imputed by law). Functions: `a person has actual notice of a fact the person has express information of the fact`; `a person has constructive notice of a fact the law imputes the fact to the person`. |
| Civ. Code § 19 | CIV-ss-1-23.6.txt:75 | encoded | `usca-general-provisions.l4`: A person with actual notice of circumstances sufficient to put a prudent person on inquiry has constructive notice of the fact itself where prosecuting the inquiry would have revealed it. Functions: `a person has constructive notice of the fact itself under Civ. Code § 19`. |
| Civ. Code § 20 | CIV-ss-1-23.6.txt:77 | encoded | `usca-operation-of-statutes.l4`: The code does not continue earlier law because it is consistent; earlier statutes, laws and rules on matters the code provides for are repealed; the repeal does not revive former law or affect existing rights or actions already taken. Functions: `an earlier statute, law or rule remains in force`; `the repeal by the code revives a former law that was repealed before`. |
| Civ. Code § 21 | CIV-ss-1-23.6.txt:80 | inert | Allows the Act to be cited simply as "The Civil Code" with the section number. A citation form. |
| Civ. Code § 22 | CIV-ss-1-23.6.txt:82 | inert | Defines law as a solemn expression of the will of the supreme power of the State. A definition with no computable consequence. |
| Civ. Code § 22.1 | CIV-ss-1-23.6.txt:84 | inert | The will of the supreme power is expressed by the Constitution and by statutes. A classification with no input that could change it. |
| Civ. Code § 22.2 | CIV-ss-1-23.6.txt:88 | encoded | `usca-operation-of-statutes.l4`: The common law of England is the rule of decision in all courts of the State so far as not repugnant to or inconsistent with the federal or State Constitution or State laws. Functions: `the common law of England is the rule of decision`. |
| Civ. Code § 23 | CIV-ss-1-23.6.txt:90 | encoded | `usca-operation-of-statutes.l4`: The four 1872 codes are construed as though each had been passed on the first day of the 1872 session; the deposit does not give that day, so the function that returns it is a named refusal. Functions: `the day each of the four 1872 codes is construed as having been passed`. |
| Civ. Code § 23.1 | CIV-ss-1-23.6.txt:92 | encoded | `usca-operation-of-statutes.l4`: Provisions of any 1872-session law that contravene or are inconsistent with a provision of one of the four codes prevail. Functions: `Civ. Code § 23.1 makes the provision of a law passed at the 1872 session prevail over the code provision`. |
| Civ. Code § 23.2 | CIV-ss-1-23.6.txt:94 | encoded | `usca-operation-of-statutes.l4`: As between themselves the four codes are construed as passed at the same moment and parts of one statute, so none prevails by being later. Functions: `one of the four 1872 codes prevails over another by having been passed later`. |
| Civ. Code § 23.3 | CIV-ss-1-23.6.txt:96 | encoded | `usca-operation-of-statutes.l4`: Conflict between titles: each title prevails as to matters arising out of its own subject matter. Functions: `the provision that prevails when units conflict unit matter`. |
| Civ. Code § 23.4 | CIV-ss-1-23.6.txt:98 | encoded | `usca-operation-of-statutes.l4`: Conflict between chapters of the same title: each chapter prevails as to matters arising out of its own subject matter. Functions: `the provision that prevails when units conflict unit matter`. |
| Civ. Code § 23.5 | CIV-ss-1-23.6.txt:100 | encoded | `usca-operation-of-statutes.l4`: Conflict between articles of the same chapter: each article prevails as to matters arising out of its own subject matter. Functions: `the provision that prevails when units conflict unit matter`. |
| Civ. Code § 23.6 | CIV-ss-1-23.6.txt:102 | encoded | `usca-operation-of-statutes.l4`: Conflict between sections of the same chapter or article: the section last in numerical order prevails unless that is inconsistent with the meaning of the chapter or article. Functions: `the section that prevails, the first being`. |
| Code Civ. Proc. § 1 | CCP-ss-1-34.txt:8 | inert | Names the Act the Code of Civil Procedure and lists its four parts. A citation form with no computable content. |
| Code Civ. Proc. § 2 | CCP-ss-1-34.txt:14 | encoded | `usca-interpretation-time.l4`: The Code of Civil Procedure takes effect at 12 o'clock noon on 1 January 1873. Functions: `the moment the Code of Civil Procedure takes effect`. |
| Code Civ. Proc. § 3 | CCP-ss-1-34.txt:16 | encoded | `usca-operation-of-statutes.l4`: No part of the code is retroactive unless expressly so declared. Functions: `a part of the Civil Code or the Code of Civil Procedure is retroactive`. |
| Code Civ. Proc. § 4 | CCP-ss-1-34.txt:18 | inert | Abolishes the strict-construction rule for statutes in derogation of the common law and requires liberal construction of the code and proceedings under it. A canon of construction; nothing to compute. |
| Code Civ. Proc. § 5 | CCP-ss-1-34.txt:20 | encoded | `usca-operation-of-statutes.l4`: Provisions substantially the same as existing statutes are continuations, not new enactments (narrower than Civ. Code § 5, which adds the common law). Functions: `the section construes a provision of`. |
| Code Civ. Proc. § 6 | CCP-ss-1-34.txt:22 | encoded | `usca-operation-of-statutes.l4`: Persons holding office under repealed Acts when the code takes effect keep their offices on the old tenure, except offices not continued by one of the codes adopted at that session. Functions: `a holder of an office under a repealed Act continues to hold it under Code Civ. Proc. § 6 and § 7`. |
| Code Civ. Proc. § 7 | CCP-ss-1-34.txt:24 | encoded | `usca-operation-of-statutes.l4`: An office abolished by repeal of an Act that is not in substance re-enacted or continued in either code ceases when the codes take effect. Functions: `a holder of an office under a repealed Act continues to hold it under Code Civ. Proc. § 6 and § 7`. |
| Code Civ. Proc. § 8 | CCP-ss-1-34.txt:26 | encoded | `usca-operation-of-statutes.l4`: No action or proceeding begun before the code takes effect, and no accrued right, is affected; proceedings must conform to the code as far as applicable. Functions: `the section protects an action, proceeding or accrued right from the code`; `procedure taken after the code took effect in a proceeding begun before must conform to the code`. |
| Code Civ. Proc. § 9 | CCP-ss-1-34.txt:28 | encoded | `usca-operation-of-statutes.l4`: Where a limitation period began running before the code and the code prescribes the same or any limitation, the time already run counts as part of the time the code prescribes. Functions: `days left of a limitation that began to run before the code took effect`. |
| Code Civ. Proc. § 10 | CCP-ss-1-34.txt:30 | encoded | `usca-holidays.l4`: Holidays within the code are every Sunday and the judicial holidays specified in § 135. Section 135 is not in the deposit, so its days are a list the caller supplies; an empty list is the caller saying there are none, and the module cannot tell that from an omission (open question Q-135). Functions: `the section that says which days are holidays for kind` in `usca-interpretation-time.l4`; `a holiday under Code Civ. Proc. § 10 supplied d`; `a holiday for computing time under Code Civ. Proc. § 12 supplied d`; `a holiday for the extension of Code Civ. Proc. § 12a(a), taking in the Sundays of § 10 supplied d` (and 1 more). |
| Code Civ. Proc. § 11 | CCP-ss-1-34.txt:32 | encoded | `usca-general-provisions.l4`: Where the code requires registered mail, certified mail is a sufficient compliance. Functions: `a requirement of the Civil Code or the Code of Civil Procedure that a notice be mailed by registered mail is met by`; `the day service by mail is deemed made, the document having been mailed on`; `the day a notice is deemed given, the notice having been sent on the day the notice is sent`. |
| Code Civ. Proc. § 12 | CCP-ss-1-34.txt:34 | encoded | `usca-interpretation-time.l4`: Period counting for acts provided by law, identical in words to Gov. Code § 6800 and Civ. Code § 10. Functions: `before the rest-day rule, the last day of n days counted from firstDay`; `with a holiday last day also excluded, once holiday d`; `the last day of a period of`; `the date d falls inside the period after firstDay through lastDay` (and 1 more). |
| Code Civ. Proc. § 12a | CCP-ss-1-34.txt:36 | encoded | `usca-interpretation-time.l4`: A last day that is a holiday extends the period to and including the next day that is not a holiday; "holiday" for this section includes all day Saturdays, § 135 days and § 12b days; § 12a(b) reaches every provision of law. Functions: `next day from the date that is not a holiday, counting days so far holiday d daysSoFar`; `extended to the next day that is not a holiday holiday d`; `the last day of a period of n u counted from firstDay under the calendar holiday`; `the date d falls inside a period of n u counted from firstDay under the calendar holiday` (and 5 more). |
| Code Civ. Proc. § 12b | CCP-ss-1-34.txt:40 | encoded | `usca-holidays.l4`: A city, county, state or public office (other than a branch office) closed for the whole of a day makes that day a holiday for computing time under §§ 12 and 12a. Functions: `the day is a closure day under Code Civ. Proc. § 12b supplied d`; `a holiday for computing time under Code Civ. Proc. § 12 supplied d`. |
| Code Civ. Proc. § 12c | CCP-ss-1-34.txt:42 | encoded | `usca-interpretation-time.l4`: An act due a number of days before a hearing: count backward from the hearing date excluding the hearing day; extra days for a method of service count backward from the resulting day. Functions: `the last day to act, when the act is due`; `the day service by mail is deemed made, the document having been mailed on` in `usca-general-provisions.l4`; `the day a notice is deemed given, the notice having been sent on the day the notice is sent` in `usca-general-provisions.l4`. |
| Code Civ. Proc. § 13 | CCP-ss-1-34.txt:46 | encoded | `usca-interpretation-time.l4`: An act of a secular nature appointed for a particular day that falls on a holiday may be performed on the next business day. Functions: `the latest day on which an act appointed for`. |
| Code Civ. Proc. § 13a | CCP-ss-1-34.txt:48 | encoded | `usca-interpretation-time.l4`: An act required on a particular day or within a period may be performed, but need not be, on a special holiday as § 6705 of the Government Code uses the term. Functions: `an act required by law on a day or within a period may be performed on kind`. |
| Code Civ. Proc. § 13b | CCP-ss-1-34.txt:50 | encoded | `usca-interpretation-time.l4`: An act required on a particular day or within a period may be performed, but need not be, on a Saturday. Functions: `an act required by law on a day or within a period may be performed on kind`. |
| Code Civ. Proc. § 14 | CCP-ss-1-34.txt:52 | inert | "Seal" includes an impression on the paper alone as well as on wax or wafer. A one-line definition about physical form; the modules model no seals. |
| Code Civ. Proc. § 15 | CCP-ss-1-34.txt:54 | encoded | `usca-general-provisions.l4`: Joint authority given to three or more public officers or persons is exercised by a majority unless otherwise expressed. Functions: `a joint authority may be exercised by those acting`. |
| Code Civ. Proc. § 16 | CCP-ss-1-34.txt:56 | inert | Words and phrases are construed by context and approved usage; technical and peculiar legal meanings, or those defined in § 17, control. A canon of construction with no input fact. |
| Code Civ. Proc. § 17 | CCP-ss-1-34.txt:58 | encoded | `usca-interpretation-time.l4`: (a) tense, gender and number canons (inert); (b) definitions: "month" means a calendar month (encoded in the time module), "signature" by mark and "electronic signature" (general-provisions module); the other defined words are one-line definitions and stay inert. Functions: `the section that defines month for kind`; `a mark is a signature or subscription` in `usca-general-provisions.l4`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement` in `usca-general-provisions.l4`; `a thing is an electronic signature` in `usca-general-provisions.l4`. |
| Code Civ. Proc. § 18 | CCP-ss-1-34.txt:84 | encoded | `usca-operation-of-statutes.l4`: The code does not continue earlier law because it is consistent; earlier law on matters provided for is repealed; the repeal does not revive former law or affect existing rights or actions already taken, and does not affect a private statute not expressly repealed. Functions: `an earlier statute, law or rule remains in force`; `the repeal by the code revives a former law that was repealed before`; `the repeal by the Code of Civil Procedure affects a private statute`. |
| Code Civ. Proc. § 19 | CCP-ss-1-34.txt:86 | inert | Allows the Act to be cited simply as "The Code of Civil Procedure" with the section number. A citation form. |
| Code Civ. Proc. § 20 | CCP-ss-1-34.txt:88 | not applicable | Defines judicial remedies as those administered by courts or by judicial officers empowered by the Constitution and statutes. A definition of a category of remedy in civil procedure, not an interpretation rule; no input the modules take bears on it. |
| Code Civ. Proc. § 21 | CCP-ss-1-34.txt:90 | not applicable | Divides judicial remedies into actions and special proceedings. A classification of remedies in civil procedure. |
| Code Civ. Proc. § 22 | CCP-ss-1-34.txt:94 | not applicable | Defines an action as an ordinary proceeding in a court of justice by which one party prosecutes another for the declaration, enforcement or protection of a right, the redress or prevention of a wrong, or the punishment of a public offense. A definition of a procedural category. |
| Code Civ. Proc. § 23 | CCP-ss-1-34.txt:96 | not applicable | Every other remedy is a special proceeding. The residual half of the § 21 classification. |
| Code Civ. Proc. § 24 | CCP-ss-1-34.txt:98 | not applicable | Actions are civil or criminal. A classification of actions. |
| Code Civ. Proc. § 25 | CCP-ss-1-34.txt:102 | not applicable | A civil action arises out of an obligation or an injury. A statement of the two sources of civil actions. |
| Code Civ. Proc. § 26 | CCP-ss-1-34.txt:106 | not applicable | Defines an obligation as a legal duty by which one person is bound to do or not do a thing, arising from contract or operation of law. A definition of a substantive category. |
| Code Civ. Proc. § 27 | CCP-ss-1-34.txt:110 | not applicable | An injury is to the person or to property. A classification. |
| Code Civ. Proc. § 28 | CCP-ss-1-34.txt:114 | not applicable | An injury to property consists in depriving its owner of the benefit of it, by taking, withholding, deteriorating or destroying it. A definition of a substantive category. |
| Code Civ. Proc. § 29 | CCP-ss-1-34.txt:116 | not applicable | Every other injury is an injury to the person. The residual half of the § 27 classification. |
| Code Civ. Proc. § 30 | CCP-ss-1-34.txt:118 | not applicable | A civil action is prosecuted by one party against another for the declaration, enforcement or protection of a right, or the redress or prevention of a wrong. A definition of a procedural category that overlaps § 22. |
| Code Civ. Proc. § 31 | CCP-ss-1-34.txt:120 | not applicable | Says the Penal Code defines and provides for the prosecution of a criminal action. A pointer to another code, which is not deposited. |
| Code Civ. Proc. § 32 | CCP-ss-1-34.txt:122 | not applicable | Where the violation of a right admits of both a civil and a criminal remedy, the right to prosecute one is not merged in the other. A rule about remedies whose only output is that nothing merges; no date or fact decides it. |
| Code Civ. Proc. § 32.5 | CCP-ss-1-34.txt:124 | not applicable | "Jurisdictional classification" of a case means its classification as a limited or an unlimited civil case. A one-line definition used elsewhere in the Code of Civil Procedure, which is not deposited. |
| Code Civ. Proc. § 33 | CCP-ss-1-34.txt:126 | not applicable | A prosecuting attorney may in discretion assist in the civil resolution of a violation of an offense in Title 13 of Part 1 of the Penal Code instead of filing a criminal complaint. A discretionary power of one officer over one class of offence, not an interpretation rule. |
| Code Civ. Proc. § 34 | CCP-ss-1-34.txt:128 | encoded | `usca-general-provisions.l4`: An electronic signature (as § 17 defines it) by a court or judicial officer is as effective as an original signature. Functions: `an electronic signature is as effective as an original signature under Code Civ. Proc. § 34`. |
| Gov. Code § 6700 | GOV-ss-6700-6736.txt:8 | encoded | `usca-holidays.l4`: The holidays in the State, (a)(1)-(20). The days the calendar fixes are computed. Lunar New Year (4), Diwali (9), Good Friday (19) and the days appointed by the President or Governor (20) are lists the caller supplies. Good Friday is a function of the moment, with the instant of 3 p.m. a named refusal. (a)(20)(B), which keeps (3), (4), (7) and (20) from a city, county or district unless made applicable, is a function of its own. (b), under which a memorandum of understanding controls in a conflict, is not encoded: it turns on the content of an agreement that is not in the text. Functions: `the section that says which days are holidays for kind` in `usca-interpretation-time.l4`; `Gov. Code § 6700(a) fixes the day by the calendar d`; `Gov. Code § 6700(a)(3) makes the day a holiday d`; `Gov. Code § 6700(a)(7), as § 6701(c) qualifies it, makes the day a holiday supplied d` (and 5 more). |
| Gov. Code § 6701 | GOV-ss-6700-6736.txt:33 | encoded | `usca-holidays.l4`: When January 1, February 12, March 31, July 4, September 9, November 11 or December 25 falls on a Sunday the Monday following is a holiday ((a)); November 11 on a Saturday makes the preceding Friday one ((b)). Both are computed. (c) lets the Legislature observe March 31 on another day: the caller supplies that day and says whether March 31 itself stays a holiday, which the text does not say (fork F-6701c). (d) lets a county board name an alternate day as a holiday for county employees other than court attaches: the caller supplies the alternate days and nothing is taken away from the Saturday (fork F-6701d). Functions: `one of the days Gov. Code § 6701(a) names d`; `Gov. Code § 6701(a) or (b) makes the day a holiday d`; `Gov. Code § 6700(a)(7), as § 6701(c) qualifies it, makes the day a holiday supplied d`; `a holiday under Gov. Code § 6700 and § 6701 for the state supplied d` (and 2 more). |
| Gov. Code § 6702 | GOV-ss-6700-6736.txt:43 | encoded | `usca-holidays.l4`: Saturday from noon to midnight is a holiday for public-office business where laws, ordinances or charters close offices on holidays (a function of the moment). The section does not prevent the issuance, filing or service of legal process in that period (a function that returns TRUE). City offices close on the holidays enumerated in § 6700 unless a charter, ordinance or resolution provides otherwise: computed, and a named refusal when something else is provided (fork F-6702city). Functions: `the moment falls in the Saturday holiday of Gov. Code § 6702`; `legal process may be issued, filed, served, executed or recorded in the Saturday holiday of Gov. Code § 6702`; `public offices of a city are closed on the day under Gov. Code § 6702`. |
| Gov. Code § 6703 | GOV-ss-6700-6736.txt:45 | encoded | `usca-holidays.l4`: State public offices close on Admission Day and on Veterans Day, moved to Friday November 10 or Monday November 12 when November 11 is a Saturday or Sunday. Functions: `Gov. Code § 6703 requires public offices of the state to be closed on the day d`; `the day is a closure day under Code Civ. Proc. § 12b supplied d`. |
| Gov. Code § 6704 | GOV-ss-6700-6736.txt:49 | encoded | `usca-holidays.l4`: A city or district legislative body may by ordinance or resolution make every Saturday a holiday for its public offices, keeping essential services. Functions: `a Saturday is a holiday for the public offices of a city or district under Gov. Code § 6704`. |
| Gov. Code § 6705 | GOV-ss-6700-6736.txt:51 | encoded | `usca-holidays.l4`: A special or limited holiday applies only to a special class of business or persons; on one appointed by the President or Governor courts and public offices stay open and contracts are performed as usual except for the class named. Functions: `courts and public offices are open on a special or limited holiday appointed by the President or Governor`. |
| Gov. Code § 6706 | GOV-ss-6700-6736.txt:55 | encoded | `usca-interpretation-time.l4`: An act of a secular nature, other than a work of necessity or mercy, appointed by law or contract for a particular day that falls on a holiday may be performed on the next business day. Functions: `the latest day on which an act appointed for`. |
| Gov. Code § 6707 | GOV-ss-6700-6736.txt:57 | encoded | `usca-interpretation-time.l4`: When the last day for filing a document with a state agency falls on a Saturday or holiday the act may be performed on the next business day. Functions: `the latest day for filing with a state agency, when the last day is`. |
| Gov. Code § 6708 | GOV-ss-6700-6736.txt:59 | not applicable | Directs the Governor to proclaim September 28 as "Cabrillo Day". A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6709 | GOV-ss-6700-6736.txt:61 | not applicable | Directs the Governor to proclaim January 15 as Dr. Martin Luther King, Jr., Day (while § 6700(a)(3) makes the third Monday in January the holiday). A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6710 | GOV-ss-6700-6736.txt:63 | not applicable | Directs the Governor to proclaim March 7 as "Arbor Day". A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6711 | GOV-ss-6700-6736.txt:65 | not applicable | Directs the Governor to proclaim February 19 as "A Day of Remembrance: Japanese American Evacuation". A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6712 | GOV-ss-6700-6736.txt:67 | not applicable | Directs the Governor to proclaim annually the fourth Friday in September as "Native American Day" (the same day § 6700(a)(15) makes a holiday). A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6713 | GOV-ss-6700-6736.txt:69 | not applicable | Directs the Governor to proclaim annually the first Sunday in October as "Stepparents Day". A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6714 | GOV-ss-6700-6736.txt:71 | not applicable | Directs the Governor to proclaim April 21 as "John Muir Day". A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6715 | GOV-ss-6700-6736.txt:73 | not applicable | Directs the Governor to proclaim March 30 as Welcome Home Vietnam Veterans Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6716 | GOV-ss-6700-6736.txt:75 | not applicable | Directs the Governor to proclaim December 7 as "Pearl Harbor Day". A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6717 | GOV-ss-6700-6736.txt:77 | not applicable | Directs the Governor to proclaim March 31 as "Farmworkers Day" (the same day § 6700(a)(7) makes a holiday). A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6718 | GOV-ss-6700-6736.txt:79 | not applicable | Directs the Governor to proclaim the month of February as Black History Month. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6719 | GOV-ss-6700-6736.txt:81 | not applicable | Directs the Governor to proclaim the third Saturday in June as "Juneteenth National Freedom Day: A day of observance" (§ 6700(a)(11) makes June 19 a holiday). A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6720 | GOV-ss-6700-6736.txt:83 | not applicable | Directs the Governor to proclaim April 24 as the "California Day of Remembrance of the Armenian Genocide", with days of remembrance from the Sunday before to the Sunday after (§ 6700(a)(8) makes April 24 a holiday). A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6721 | GOV-ss-6700-6736.txt:86 | not applicable | Directs the Governor to proclaim May 22 as Harvey Milk Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6722 | GOV-ss-6700-6736.txt:88 | not applicable | Directs the Governor to proclaim January 30 as Fred Korematsu Day of Civil Liberties and the Constitution. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6723 | GOV-ss-6700-6736.txt:90 | not applicable | Directs the Governor to proclaim February 6 as Ronald Reagan Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6724 | GOV-ss-6700-6736.txt:92 | not applicable | Directs the Governor to proclaim January 23 as Ed Roberts Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6725 | GOV-ss-6700-6736.txt:94 | not applicable | Directs the Governor to proclaim October 25 as Larry Itliong Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6726 | GOV-ss-6700-6736.txt:96 | not applicable | Directs the Governor to proclaim the first Friday in May as Space Day, with lights-out and school provisions. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6727 | GOV-ss-6700-6736.txt:102 | not applicable | Directs the Governor to proclaim the day of the astronomical Northward equinox as Nowruz Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6728 | GOV-ss-6700-6736.txt:104 | not applicable | Directs the Governor to proclaim the month of June as LGBTQ+ Pride Month. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6729 | GOV-ss-6700-6736.txt:106 | not applicable | Directs the Governor to proclaim April 10 as Dolores Huerta Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6731 | GOV-ss-6700-6736.txt:108 | not applicable | Directs the Governor to proclaim August 26 as California Farmworker Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6733 | GOV-ss-6700-6736.txt:111 | not applicable | Directs the Governor to proclaim November 20 as "Transgender Day of Remembrance". A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6735 | GOV-ss-6700-6736.txt:113 | not applicable | Directs the Governor to proclaim December 1 as World AIDS Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6736 | GOV-ss-6700-6736.txt:115 | not applicable | Directs the Governor to proclaim September 25 as Dolly Parton Day. A commemorative proclamation, not an addition to the § 6700(a) list: that list is what §§ 6800, 6701-6707 and the codes' holiday provisions refer to, and this section does not call the day a holiday. Whether a proclamation under it is also a day "appointed ... for a public fast, thanksgiving, or holiday" under § 6700(a)(20)(A) is not answered by the text (fork F-hol-6); the holiday module takes appointed days as a caller input, so a caller who treats it as one supplies it. |
| Gov. Code § 6800 | GOV-ss-6800-6808.txt:8 | encoded | `usca-interpretation-time.l4`: Period counting: first day excluded, last included, unless the last day is a holiday, and then it is also excluded. Functions: `before the rest-day rule, the last day of n days counted from firstDay`; `before the rest-day rule, the last day of n months counted from firstDay`; `last day of a count of units in which the leap-day pair counts once`; `with a holiday last day also excluded, once holiday d` (and 5 more). |
| Gov. Code § 6801 | GOV-ss-6800-6808.txt:10 | encoded | `usca-interpretation-time.l4`: Time is computed by the Gregorian calendar, which is what daydate's day numbers are, so the rule is used and not computed. The rule that January 1 after 1752 is the first day of the year changes no count and is not computed. The leap-year function refuses a hundredth year before 1900, for which § 6802 names no rule; no other date is checked against 1752. Functions: `is a leap year under section 6802 year`. |
| Gov. Code § 6802 | GOV-ss-6800-6808.txt:12 | encoded | `usca-interpretation-time.l4`: Leap years: the hundredth years 1900, 2100, 2200, 2300 are common years, 2000, 2400, 2800 and every fourth hundredth year and every fourth year otherwise are leap years of 366 days. Functions: `is a leap year under section 6802 year`. |
| Gov. Code § 6803 | GOV-ss-6800-6808.txt:14 | encoded | `usca-interpretation-time.l4`: A year is 365 days, a half year 182, a quarter of a year 91, with the added day of a leap year and the day before it reckoned together as one day. Functions: `leap-day pair of the year lies in the period`; `count of leap-day pairs in the period`; `day number on which a count of units ends`; `last day of a count of units in which the leap-day pair counts once` (and 7 more). |
| Gov. Code § 6804 | GOV-ss-6800-6808.txt:16 | encoded | `usca-interpretation-time.l4`: A month is a calendar month unless otherwise expressed. Functions: `before the rest-day rule, the last day of n months counted from firstDay`; `the section that defines month for kind`. |
| Gov. Code § 6805 | GOV-ss-6800-6808.txt:18 | encoded | `usca-interpretation-time.l4`: A week is seven consecutive days. Functions: `before the rest-day rule, the last day of n weeks counted from firstDay`; `days in a week under section 6805`. |
| Gov. Code § 6806 | GOV-ss-6800-6808.txt:20 | encoded | `usca-interpretation-time.l4`: A day is the period between any midnight and the midnight following (used for the moment within a day). Functions: `the midnight that begins the day d`; `the midnight that ends the day d`; `the moment m falls within the day d`; `the moment a statute goes into effect enactment` (and 3 more). |
| Gov. Code § 6807 | GOV-ss-6800-6808.txt:22 | encoded | `usca-interpretation-time.l4`: Daytime is between sunrise and sunset and nighttime between sunset and sunrise; sunrise and sunset are inputs and the exact instants are a named refusal. Functions: `the part of the day at t given sunrise at sunrise and sunset at sunset`. |
| Gov. Code § 6808 | GOV-ss-6800-6808.txt:24 | encoded | `usca-interpretation-time.l4`: (a) names Pacific standard time as the standard time; the modules take clock readings on the clock then in force and encode nothing for (a). (b) is computed: the second Sunday of March, the first Sunday of November, whether daylight saving time is in effect at a clock reading, and the hours the clock is advanced; the readings the change skips or repeats are refused. (c), the Legislature's power to amend by a two-thirds vote, stays inert. Functions: `the second Sunday of March of y`; `the first Sunday of November of y`; `daylight saving time at a clock reading on the day it commences secs`; `daylight saving time at a clock reading on the day it ends secs` (and 2 more). |
| Gov. Code § 9600 | GOV-ss-9600-9612.txt:8 | encoded | `usca-interpretation-time.l4`: Commencement of statutes: regular session, January 1 next following a 90-day period from enactment; special session, the 91st day after adjournment; elections, tax levies, usual-expenses appropriations and urgency statutes immediately upon enactment. Functions: `a statute is of a kind that goes into effect immediately upon its enactment enactment`; `the day a regular-session statute goes into effect when enacted on dayOfEnactment`; `the day a special-session statute goes into effect, the special session having adjourned on`; `the day a statute goes into effect enactment` (and 6 more). |
| Gov. Code § 9602 | GOV-ss-9600-9612.txt:11 | encoded | `usca-interpretation-time.l4`: A concurrent or joint resolution takes effect on its filing with the Secretary of State. Functions: `the moment a concurrent or joint resolution takes effect, having been filed with the Secretary of State at`; `the day silent subordinate legislation comes into force, when made on madeOn`. |
| Gov. Code § 9603 | GOV-ss-9600-9612.txt:13 | inert | Says the general rules for the construction of statutes are in the preliminary provisions of the different codes. A pointer, not a rule: its content is the reason this encoding is a cluster of sections rather than one Act, and it is used in the scope fork (F-scope-1), but it asks no question a function could answer. |
| Gov. Code § 9604 | GOV-ss-9600-9612.txt:15 | encoded | `usca-operation-of-statutes.l4`: A reference to provisions carried into another statute as restatements and continuations is deemed a reference to the restatement, unless a contrary intent appears. Functions: `Gov. Code § 9604 deems a reference to be a reference to the restatements and continuations`. |
| Gov. Code § 9605 | GOV-ss-9600-9612.txt:17 | encoded | `usca-operation-of-statutes.l4`: Amendment is not repeal and re-enactment; unaltered provisions date from enactment, new ones from the amendment, omitted ones are repealed at the amendment; precedence among amendments passed at one session. Functions: `the day a provision of an amended section is considered to have been enacted`; `the day a provision of an amended section is considered to have been repealed`; `a portion stands after successive acts of one session amend the same section`; `the statute that prevails when two statutes of one session amend the same section first second`. |
| Gov. Code § 9606 | GOV-ss-9600-9612.txt:25 | encoded | `usca-operation-of-statutes.l4`: A statute may be repealed at any time except where vested rights would be impaired. Functions: `a statute may be repealed vested rights would be impaired`. |
| Gov. Code § 9607 | GOV-ss-9600-9612.txt:27 | encoded | `usca-operation-of-statutes.l4`: A statute repealed by another is not revived by repeal of the repealing statute without express words; a later statute that extends a termination date, chaptered before that date, revives the law when it becomes operative. Functions: `a repealed statute is revived by the repeal of the statute that repealed it`; `the day a terminated or repealed law is revived by a later statute chaptered on`. |
| Gov. Code § 9608 | GOV-ss-9600-9612.txt:30 | encoded | `usca-operation-of-statutes.l4`: Termination or suspension of a law creating a criminal offense does not bar punishment of an act already committed, unless the intention to bar it is expressly declared. Functions: `the termination or suspension of a criminal law bars indictment, information and punishment`. |
| Gov. Code § 9609 | GOV-ss-9600-9612.txt:32 | encoded | `usca-operation-of-statutes.l4`: A statute amending a section of a repealed statute is void. Functions: `Gov. Code § 9609 makes a statute amending a section of a repealed statute void`. |
| Gov. Code § 9610 | GOV-ss-9600-9612.txt:34 | encoded | `usca-operation-of-statutes.l4`: A statute fixing a State officer's or employee's salary is not an appropriation; the salary is paid only if moneys are made available by another provision of law. Functions: `a statute fixing the salary of a State officer or employee is an appropriation of money for it`; `the salary fixed by statute shall be paid`. |
| Gov. Code § 9611 | GOV-ss-9600-9612.txt:36 | encoded | `usca-operation-of-statutes.l4`: A law temporarily suspended, or modified or repealed by a provision effective for a limited period, is not repealed and resumes its force when the suspension or limited provision ends. Functions: `a law temporarily suspended or modified is deemed repealed`; `the original provision has its full force again on the day`. |
| Gov. Code § 9612 | GOV-ss-9600-9612.txt:38 | encoded | `usca-general-provisions.l4`: Unless the context requires otherwise, "United States Army", "Army of the United States", "United States Navy" or "military service" in a statute includes the United States Air Force. Functions: `a term in a statute is deemed to include the United States Air Force`. |

Counts: 82 encoded, 29 inert, 48 not applicable; 159 sections in all.

Numbers inside the deposited ranges that the text does not contain (disposition `repealed or blank in this text`; the deposit holds only sections marked current, so the text shows nothing more about them than their absence):

| Number | Where the gap sits | Disposition |
|---|---|---|
| Civ. Code § 8 | between its neighbours in CIV-ss-1-23.6.txt | repealed or blank in this text |
| Civ. Code § 15 | between its neighbours in CIV-ss-1-23.6.txt | repealed or blank in this text |
| Civ. Code § 16 | between its neighbours in CIV-ss-1-23.6.txt | repealed or blank in this text |
| Gov. Code § 6730 | between its neighbours in GOV-ss-6700-6736.txt | repealed or blank in this text |
| Gov. Code § 6732 | between its neighbours in GOV-ss-6700-6736.txt | repealed or blank in this text |
| Gov. Code § 6734 | between its neighbours in GOV-ss-6700-6736.txt | repealed or blank in this text |
| Gov. Code § 9601 | between its neighbours in GOV-ss-9600-9612.txt | repealed or blank in this text |

7 numbers absent. Code of Civil Procedure § 135, to which CCP §§ 10 and 12a point, is not in any deposited file; it has no row because the text does not contain it.

## Fork register

A fork is a place where the deposited text allows more than one reading, or says nothing.
Each entry gives the readings seen, the one the code takes, the text that licenses each reading, and where in the code the choice sits.
"The text" always means the deposited `.txt` files, which are a converter-made rendering and not the official text.
Where a reading is not licensed by the deposited text the code refuses (`REFUSE`) and the entry says so.
Where the code offers both readings as separate functions the entry says which one the headline function uses.
Nothing here was settled by a court or by a regulator: the deposit contains no decision and no commentary.
No fork was resolved by looking at another encoding.

**A convention that is not a fork.**
In these modules a Boolean result `FALSE` means "this section does not give this result", and `REFUSE` is used where an antecedent is undetermined or where the section has no consequence for the case.
So a function such as `a statute fixing the salary of a State officer or employee is an appropriation of money for it` is constant `FALSE` (Gov. Code § 9610 says it is not), and `an earlier statute, law or rule remains in force` refuses on a matter the code does not provide for.
There is no home-made third value anywhere.

### Counting a period

**F-from: which day is the excluded "first day", and is the last day inside the period?**
- Text: Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. § 12 all say a period is computed "by excluding the first day, and including the last".
  The text says the last day is included; that part is not a fork.
- Readings of "first day": (1) the day of the event the period runs from; (2) the day after it.
  Under (1) a period of 30 days from 1 January ends on 31 January; under (2) it ends on 1 February.
- Taken: (1).
  Every counting function takes the day the period is counted from and treats that day as the excluded first day.
  The caller who means "from the day after the event" passes the day after.
- The text does not distinguish "from" from "after": nothing deposited says that "within 30 days after" and "within 30 days from" differ.
  The code has one function for both, so the difference is the caller's choice of start day.
- `the date d falls inside the period after firstDay through lastDay` reads the period as the first day excluded and the last included, and is tested at both ends.
- Where: `usca-interpretation-time.l4`, the section `Counting a period`.

**F-contract: does the period rule reach a period fixed by contract?**
- Text: Gov. Code § 6800 and Civ. Code § 10 speak of "any act provided by law"; Code Civ. Proc. § 12a(a) of "any act provided or required by law"; Gov. Code § 6706, Civ. Code § 11 and Code Civ. Proc. § 13 speak of an act "appointed by law or contract" but only for an act on a particular day.
- Readings: (1) a period set by contract is counted the same way; (2) it is not within these sections.
- Taken: neither.
  The counting functions take a period and a start and make no claim about the kind of act, so nothing refuses and nothing asserts coverage.
  Which readings apply to a contract is an open question (Q-contract).

**F-run: when the last day is a holiday, does the extension stop at the next day, or run past several in a row?**
- Text: Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. § 12: "unless the last day is a holiday, and then it is also excluded".
  Code Civ. Proc. § 12a(a): the period "is hereby extended to and including the next day that is not a holiday".
- Readings: (1) run: carry on to the first day that is not a holiday (the words of § 12a(a)); (2) one step: exclude the holiday last day once, and the day after it is the last day, whatever that day is.
- Taken: (1) for the headline function `the last day of a period of n u counted from d under the calendar holiday`; (2) is offered as `with a holiday last day excluded once under the calendar`.
  The two differ when the day after a holiday last day is itself a holiday.
  Example from the worked cases: five years from 2025-09-01 ends on Sunday 2030-09-01; the Government Code calendar gives 2030-09-03 on (1) and 2030-09-02 on (2), and 2030-09-02 is itself a holiday (first Monday in September, Gov. Code § 6700(a)(13)).
- "Two holidays in a row" is therefore tested on both: Saturday and Sunday under the Code of Civil Procedure calendar, and Sunday and Monday holiday together under the Government Code calendar.
- A calendar in which more than 366 days in a row are holidays is refused rather than looped over (the loop guard is a limit on the caller's calendar, not a rule of the text; 366 in a row resolve, 367 are refused).
- Where: `extended to the next day that is not a holiday`, `with a holiday last day also excluded, once`.

**F-direction: which way does a last day on a holiday move?**
- Text: Code Civ. Proc. § 12a(a) says "extended to and including the next day"; § 6800's "also excluded" does not say which way.
- Taken: forward, for every forward-counted period.
  Excluding a counted day lengthens the span, so "also excluded" is read as the same direction as § 12a(a).
- For a period counted backward from a hearing (Code Civ. Proc. § 12c) the text gives no direction: see F-backward.

**F-unit: does the holiday extension apply to a period of months or years, not only of days?**
- Text: the sections say "any act provided by law" and "a specified period of time" and draw no line by unit.
- Taken: the same rule for every unit (days, weeks, months, years, half years, quarters of a year).
  A reader who thinks a period counted in months ends on its date whatever the day can read `before the rest-day rule, the last day of ...`, which does not apply the extension.
- Where: the dispatcher `the last day of a period of n u counted from d under the calendar holiday`.

**F-holiday: which days are "holidays"?**
- The text has three definitions and they differ.
  Gov. Code § 6700(a): "the holidays in this state", a list of twenty paragraphs, Sundays among them, Saturdays not.
  Civ. Code § 7: "every Sunday and such other days as are specified or provided for as holidays in the Government Code".
  Code Civ. Proc. § 10: every Sunday and the judicial holidays in § 135; Code Civ. Proc. § 12a(a): "all day on Saturdays, all holidays specified in Section 135 and, to the extent provided in Section 12b, all days that by terms of Section 12b are required to be considered as holidays".
- Readings of § 12a(a): (1) literal: Sunday is not named, so it is a holiday for the extension only if § 135 specifies it, and § 135 is not in the deposit; (2) § 10 is read into § 12a, so Sundays count.
- Taken: both are functions (`...read literally`, `...taking in the Sundays of § 10`); the worked cases use (2).
- Code Civ. Proc. § 135 is not in the deposited text.
  Its days are a list the caller supplies.
  A caller who supplies none gets Saturdays and Sundays (and § 12b closures) under the Code of Civil Procedure calendars, and, for example, 1 January is then not a holiday under them.
  The module cannot tell an empty list from an omitted one (Q-135).
- The days that need a calendar the text does not give are inputs, never computed: Lunar New Year (§ 6700(a)(4)), Diwali (§ 6700(a)(9)), Good Friday, days appointed by the President or Governor, Thanksgiving Day (the Thursday "appointed"), days a public office is closed (§ 12b), bank closings (Civ. Code § 7.1(a)).
- Where: `usca-holidays.l4`, with the record `Days supplied by the caller`.

**F-vintage: which version of a section applies to a date.**
- Text: the deposit holds one version of each section, the current one (the `current_to` field of the `.meta.json` files in `../../registers/source-bundle/` says 2026-10-19), with its amendment line (for example § 6700: "Amended by Stats. 2026, Ch. 7, Sec. 1. (AB 2156) Effective March 26, 2026").
  It holds no earlier version of any section.
- Taken: the deposited text is applied to every date, including dates before the amendment, because the text carries nothing to apply instead.
  A period counted in 2024 against the holiday list therefore uses today's list.
  The functions take no vintage; adding one would need the earlier texts (Q-vintage).
  The worked cases and many tests use dates before 26 March 2026, so the modules do not refuse on a date before an amendment.

**F-governs: which definition of "holiday" and of "month" governs which kind of enactment?**
- Text: each code says "within the meaning of this code" for holidays (Civ. Code § 7, Code Civ. Proc. § 10).
  "Month" is defined three times, in the same words: Gov. Code § 6804, Civ. Code § 14(b)(4) and Code Civ. Proc. § 17(b)(4) ("a calendar month, unless otherwise expressed").
  The two codes give their definitions "in this code" and "unless otherwise apparent from the context" as well; § 6804 has no limit of its own beyond "unless otherwise expressed".
  Gov. Code § 9603 says the general rules of construction are in the preliminary provisions of the different codes.
  Gov. Code § 5 says the general provisions govern the construction of that code.
  Code Civ. Proc. § 12a(b) makes § 12a apply to "all other provisions of law ... whether expressed in this or any other code or statute, ordinance, rule, or regulation".
- Taken, with `Kind of enactment`:
  a provision of the Civil Code: Civ. Code § 7 and § 14(b)(4); a provision of the Code of Civil Procedure: Code Civ. Proc. § 10 (with § 12b) and § 17(b)(4); a provision of the Government Code: Gov. Code § 6700(a) and § 6804; another State statute: Gov. Code § 6700(a) and § 6804; an ordinance, rule or regulation: REFUSE.
- "Another State statute" taking the Government Code's definitions is an assumption: § 6700(a) says "the holidays in this state" and § 6804 has no limit of its own, and nothing deposited says more.
- For the extension of a last day, Code Civ. Proc. § 12a(a) names its own holiday list "for purposes of this section", and § 12a(b) reaches every kind of provision, so the extension question is answered the same for every kind (`the section that extends a last day falling on a holiday for kind`).
- Where: the section `Which section governs` of `usca-interpretation-time.l4` and `the day is a holiday within the meaning of a provision of kind` in `usca-holidays.l4`.

**F-overlap: Gov. Code § 6800, Civ. Code §§ 10-11 and Code Civ. Proc. §§ 12-13b overlap.**
- Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. § 12 say the same thing in the same words (§ 10 omits one comma).
  One set of functions serves all three.
- Gov. Code § 6706, Civ. Code § 11 and Code Civ. Proc. § 13 also say one thing (an act of a secular nature, not a work of necessity or mercy, appointed for a particular day that is a holiday may be done on the next business day).
  One function serves all three.
- The real overlap: Code Civ. Proc. § 12a(b) extends "an act to be performed on a particular day" to the next day that is not a holiday, and § 13 gives the next business day.
  They reach different days where one makes Saturday a holiday (§ 12a(a)) and the other makes Saturday a business day (Civ. Code § 9 counts every day other than those in § 7 as a business day).
  The function for § 13, Civ. Code § 11 and Gov. Code § 6706 takes both a holiday calendar and a business-day calendar and returns the day by that rule alone; it does not pick between that rule and § 12a.
- Gov. Code § 6707 (a filing with a state agency whose last day is a Saturday or a holiday) names Saturday expressly, so a Saturday is not a business day for this one rule even though it is for Civ. Code § 9.
- Code Civ. Proc. § 13a and § 13b allow an act to be performed on a special holiday or on a Saturday "with like effect"; the text has no sentence about performing an act on a Sunday or another holiday, and the function refuses for that case.

**F-week: a week.**
- Gov. Code § 6805: "seven consecutive days".
  Taken: a period of n weeks is a period of 7n days, counted by § 6800.
  Nothing in the text counts weeks by the calendar week.

**F-month: a month, and a start on the 29th, 30th or 31st.**
- Text: Gov. Code § 6804 says a month is "a calendar month, unless otherwise expressed" and nothing more.
  § 6800 excludes the first day.
- Readings: (1) corresponding day: n months from the 15th is the 15th, n calendar months on; (2) when the month reached is shorter, the last day of it (this is what daydate's `add months` does); (3) when it is shorter, spill into the next month by days.
- Taken: (1), and where the month reached has no day with the start day's number (a start on 31 January for one month; on 29, 30 or 31 January in a common year; on 31 March for one month), REFUSE: the text licenses neither (2) nor (3).
  The worked case "one month from 2025-01-31" is therefore refused.
  Start on the 31st reaching a month that has a 31st is answered (31 January plus two months is 31 March).
- Where: `before the rest-day rule, the last day of` n `months counted from` d.

**F-year: a year is 365 days.**
- Text: Gov. Code § 6803: "Year" means a period of 365 days; "half year," 182 days; "quarter of a year," 91 days.
  Three years from 2025-07-16 is 1,095 counted days.
  29 February 2028 lies in that period and the pair counts as one day (see F-pair), so the last day is 2028-07-16, which is 1,096 calendar days on.
- Taken: the lengths are 365, 182 and 91 days exactly, counted from the first day by § 6800.
  The text defines "year" nowhere as a calendar year, so a "year" in these modules is never "the same date next year".
- Where: `last day of n periods of fixed length`.

**F-pair: the leap-day pair.**
- Text: Gov. Code § 6803: "The added day of a leap year, and the day immediately preceding, if they occur in any such period, shall be reckoned together as one day."
  The added day is 29 February; the day immediately preceding it is 28 February.
- Question: does the pair "occur in" the period when 28 February is the excluded first day of the period (§ 6800)?
- Readings: (S) literal: both days must be counted days of the period, so a period whose first day is 28 February does not contain the pair; (P) purposive: the added day is in the period, so the pair counts as one day.
- Taken: (S) for the functions without a reading in their names; (P) is offered as `on the purposive reading of the leap-day pair, ...`.
  The two readings differ only for a period starting on 28 February of a leap year; the worked case "two years from 2024-02-28" ends on 2026-02-27 (S) or 2026-02-28 (P).
- A start on 29 February: 28 February is before the period on both readings, so no pair is counted for that year.

**F-29Feb: a start on 29 February.**
- Years: one year from 2024-02-29 ends on 2025-02-28 (365 days from 29 February; no pair, since 28 February is before the period).
- Months: a start on 29 February reaching a month with a 29th is answered (one month: 29 March; 48 months: 29 February 2028); reaching 2025-02 or 2026-02 (12 or 24 months) is refused under F-month.
- Half years and quarters are counted in days (182, 91), so they never refuse.

### Commencement and the moment of binding

**F-commence: counting the 90-day period of § 9600(a).**
- Text: "a statute enacted at a regular session shall go into effect on January 1 next following a 90-day period from the date of enactment of the statute".
- Questions: is the day of enactment inside the period (§ 6800 speaks of acts "to be done" and a commencement is not one); and what is "next following" when the 90th day is itself a January 1?
- Taken: the period is counted under § 6800, so the day of enactment is excluded and the 90th day is 90 days on.
  The January 1 next following the 90th day is the January 1 after it.
  When the 90th day is itself a January 1 (enactment on 3 October, in any year) the text does not say whether that January 1 is part of the period, and the function refuses.
  Enacted 2026-10-02: 2027-01-01.
  Enacted 2026-10-03: refused.
  Enacted 2026-10-04: 2028-01-01.
- If the day of enactment were counted as day 1, every boundary would move one day later: enactment on 3 October would give 1 January 2027, enactment on 4 October would be the refused case, and 5 October would give the following 1 January.
  The text does not say that § 6800 applies to a commencement, so that reading cannot be ruled out, and the code does not offer it (open question Q-commence).
- Special session: "the 91st day after adjournment", counted from the day of adjournment with that day excluded, so adjournment plus 91 days.

**F-enactment: what is "the date of enactment"?**
- Text: § 9600(a) says "the date of enactment of the statute" without saying whether it is the day a bill is passed, signed or published.
- Taken: the caller supplies the moment of enactment it means (`the moment of enactment`); the code does not choose.

**F-own-day: an Act that names its own day of effect.**
- Text: § 9600(a) says a statute "shall go into effect on January 1 next following a 90-day period"; the exceptions in (b) are statutes calling elections, tax levies, appropriations for the usual current expenses of the state, and urgency statutes.
  The text neither lets a statute's own day displace (a) nor forbids it.
- Taken: REFUSE.
  The worked case "an Act whose day is to be fixed later, fixed as 2026-06-01" is therefore refused for the day and for the moment.
  A caller who takes the day the Act names to govern can call `the day a statute goes into effect, taking the day it names itself to govern`, which is that assumption and nothing more.

**F-subordinate: subordinate legislation.**
- Text: § 9600 speaks of statutes and § 9602 of concurrent and joint resolutions; no deposited section says when a regulation, rule or order takes effect.
- Taken: REFUSE.
  The worked case "subordinate legislation made 2026-03-10 and silent" is refused.

**F-moment: the moment within the day a statute binds.**
- Text: § 9600(a) names a day.
  § 6806 says a day is the period between any midnight and the midnight following.
  Civ. Code § 2 and Code Civ. Proc. § 2 name noon on 1 January 1873 for those codes alone.
- Readings: (1) from the midnight that begins the day; (2) from some other moment, for example the moment of enactment on the day; (3) at the end of the day.
- Taken: for a statute under (a): REFUSE.
  For a statute under (b) ("immediately upon their enactment"): the moment of enactment, which is the caller's input.
  `the moment a statute goes into effect, taking it to bind from the midnight that begins its day` is offered as the explicit assumption (1).
- The two codes: noon on 1 January 1873, from their own text.
  The Government Code's own day is not in the deposit (§§ 1-26 say "this code takes effect" in § 4 without a day): REFUSE.

**F-midnight: who owns the midnight instant?**
- Text: § 6806 says a day runs between "any midnight and the midnight following" and does not say which day the instant of midnight belongs to.
- Taken: a representation chosen here and not a rule of the text: the instant that ends one day and begins the next is the beginning (0 seconds) of the later day.
  A moment is a day and a count of seconds after the midnight that begins it, and a moment lies within the day it names.

**F-language: which language version is authoritative?**
- Text: Gov. Code § 8 says a notice, report, statement or record required or authorized by the code "shall be made in writing in the English language unless it is expressly provided otherwise".
  The Legislature publishes the codes in English only, and the deposit has no sentence about a version in another language.
- Taken: the form of such a record is computed (writing, English, unless otherwise provided); which of two language versions has authority is REFUSED, with a message that names the gap.

**F-deemed-service: deemed service or notice.**
- The deposit has no general rule deeming service or notice made on any day.
  Civ. Code § 17 and Code Civ. Proc. § 11 say only that certified mail is a sufficient compliance where registered mail is required; Civ. Code §§ 18 and 19 define actual and constructive notice without a day; Code Civ. Proc. § 12c(b) counts days added for a method of service backward from a hearing, which is not a deeming rule.
- Taken: `the day service by mail is deemed made, the document having been mailed on` and `the day a notice is deemed given, the notice having been sent on` both REFUSE, with messages that say so.
  Nothing was invented to fill the gap.

**F-backward: counting backward from a hearing (Code Civ. Proc. § 12c).**
- Text: § 12c(a): an act due a number of days before a hearing counts back from the hearing date, the hearing day excluded; (b): days added for a method of service count back from the resulting day.
- Questions: (1) which way a backward-counted last day on a holiday moves, given that § 12a(a) moves it forward (toward the hearing) and § 12 excludes it (which backward is earlier); (2) whether the day § 12c(a) gives is itself checked against the calendar before the (b) days are counted.
- Taken: (1) REFUSE when it arises; (2) not checked.

### Rules about particular days and the like

**F-13ab: acts on a special holiday or on a Saturday.**
- Text: § 13a (a special holiday as § 6705 of the Government Code uses the term) and § 13b (a Saturday): the act "may be performed (but is not hereby required to be performed) ... with like effect as if performed on a day which is not a holiday".
- Taken: TRUE for each; REFUSE for a Sunday or another holiday, to which these two sections say nothing.

**F-6700a19: Good Friday "from 12 noon until 3 p.m.".**
- Taken: a function of the moment; at noon it has begun; at exactly 3 p.m. the text does not say whether "until" includes the instant, and the function refuses.
- Civ. Code § 7.1(o) (Good Friday "from 12 noon until closing"): the bank's closing second is an input.

**F-6701c: March 31 observed on another day.**
- Text: § 6701(c): when March 31 falls on a Tuesday, Wednesday or Thursday, "the Legislature may observe the holiday on" the preceding Friday, the preceding Monday or the following Friday.
- Question: does March 31 itself then stop being a holiday?
- Taken: the caller says (`March 31 itself stays a holiday in a year in which it is observed on another day`), and the observed day is a list the caller supplies.

**F-6701d: a county's alternate day.**
- Text: § 6701(d): if a § 6700 holiday falls on a Saturday, a county board may by ordinance or resolution provide that an alternate day is a holiday for county employees, except court attaches.
- Question: does the Saturday stop being a holiday for them?
- Taken: the alternate days are a list the caller supplies; nothing is taken away from the Saturday.
  The function does not check that the alternate day was provided for a Saturday holiday, which is the board's fact.

**F-6702city: "those holidays enumerated in Section 6700" for a city's offices.**
- Text: § 6702, third sentence: "Public offices of a city shall be closed on those holidays enumerated in Section 6700 unless otherwise provided by charter, ordinance or resolution."
- Question: are the Monday after a Sunday holiday and the Friday before a Saturday November 11 (§ 6701(a), (b)) "enumerated in Section 6700"?
- Taken: no.
  The days of § 6700 that apply to a city under (a)(20)(B), nothing from § 6701.
  When a charter, ordinance or resolution provides otherwise, REFUSE: what it provides is not in the text.
  A reader who wants the § 6701 days as well can use `a holiday under Gov. Code § 6700 and § 6701 for a city, county or district`.

**F-hol-6: the commemorative proclamations, §§ 6708-6736.**
- Each directs the Governor to proclaim a day or month (for example § 6709 for 15 January, while § 6700(a)(3) makes the third Monday in January the holiday).
  None says the day is a holiday, and § 6700(a)(20)(A) makes holidays of "every day appointed by the President or Governor for a public fast, thanksgiving, or holiday".
- Question: is a day proclaimed under one of these sections "appointed ... for a ... holiday"?
- Taken: not decided in code.
  The sections are `not applicable`, and a caller who treats a proclamation as such an appointment supplies the day in `days appointed by the President or Governor for a public fast, thanksgiving or holiday`.
  § 6705 (a special or limited holiday applies only to a special class and courts and offices stay open) is encoded as the constant `TRUE` of its second paragraph.

**F-6802: a hundredth year before 1900.**
- Text: § 6802 names 1900, 2100, 2200, 2300 "or any other future hundredth year" as common years, and 2000, 2400, 2800 and every fourth hundredth year after 2000 as leap years; "every fourth year ... which, by usage in this State is considered a leap year" is a leap year.
- Taken: for a hundredth year before 1900 (1800, 1700, ...) the text names no rule, so REFUSE; every other year follows § 6802.
- Gov. Code § 6801 (the Gregorian calendar) is what daydate's day numbers are; no date is checked against 1752.

**F-dst: daylight saving time.**
- Text: § 6808(a), (b): standard time is Pacific standard time; daylight saving time advances the clock one hour from 2 a.m. on the second Sunday in March to 2 a.m. on the first Sunday in November.
- Taken: the clock readings from 2 a.m. up to 3 a.m. on the March day do not occur and are refused; the readings from 1 a.m. up to 2 a.m. on the November day occur twice and are refused (a reading alone cannot say which).
  The November change is read as 2 a.m. on the daylight clock; the text does not say which clock.

**F-daytime: sunrise and sunset themselves.**
- Text: § 6807: daytime is "between sunrise and sunset" and nighttime "between sunset and sunrise".
- Taken: sunrise and sunset are inputs (seconds after midnight); the instant of sunrise or of sunset is refused, as is a day on which sunset does not follow sunrise.

### The operation of statutes

**F-9605b: two amending statutes of one session (Gov. Code § 9605(b)).**
- Text: (1) the statute enacted last is conclusively presumed to prevail absent a contrary provision in it; (2) the statute with the higher chapter number is presumed to prevail absent a contrary provision in it, and a statute enacted in the even-numbered year of a two-year regular session is deemed to bear a higher chapter number than any statute of the odd-numbered year.
- Question: the text does not rank (1) against (2) when they point at different statutes.
- Taken: REFUSE when both are open and point at different statutes; the one that is open when only one is; REFUSE when neither is.

**F-9607b: the date of termination.**
- Text: § 9607(b): a later statute that deletes or extends the date of termination or repeal, if "chaptered before such date of termination or repeal", revives the law "when the later enacted statute becomes operative".
- Question: is the date of termination the last day the law operates or the first day it does not?
- Taken: the dates are compared as stated: chaptered strictly earlier than the stated date revives the law on the day the later statute becomes operative; otherwise the answer is `NOTHING` (§ 9607(b) says nothing about a statute chaptered on or after that date).

**F-9611: when a temporary provision expires.**
- Text: § 9611: "upon the expiration of the time of the temporary suspension or the effectiveness of the inconsistent provision, the original provision shall have the same force and effect".
- Taken: the input is the last day the temporary provision is effective; the original has full force from the day after.
  The text says "upon the expiration" and not on which day.

**F-ccp9: Code Civ. Proc. § 9.**
- Text: where a limitation "has begun to run before this code goes into effect", the time already run "shall be deemed part of the time prescribed".
- Question: are the days already run counted with or without the day the code took effect?
- Taken: the days already run are the difference of the two dates (the day the code took effect minus the day the limitation began), which is the count whichever of the two end days is left out; the text does not say which.
  That difference is taken off the days the code prescribes.
  A limitation that did not begin before the code is refused.

**F-23.6: Civ. Code § 23.6.**
- Text: "the sections last in numerical order shall prevail, unless such construction is inconsistent with the meaning of the chapter or article."
- Question: sections numbered with a letter (for example 12a) have no numerical place in the text.
- Taken: the section numbers are numbers (17.5 for section 17.5); a letter-numbered section cannot be given to the function, and two sections with one number are refused; an inconsistent construction is refused because the text does not say which section then prevails.

### Scope

**F-scope-1: the cluster itself.**
- California has no single interpretation act; § 9603 says "The general rules for the construction of statutes are contained in the preliminary provisions of the different codes".
  The scope (Gov. Code §§ 1-26, Civ. Code §§ 1-23.6, Code Civ. Proc. §§ 1-34, Gov. Code §§ 6700-6736, §§ 6800-6808, §§ 9600-9612) was fixed when the subject was stubbed; the stub calls it "an assumption ... not a ruling".
- Taken: the whole cluster, section by section, each rule tagged with its section; the Penal Code and the Evidence Code preliminary provisions and the many sections on construction found outside the six deposited files are not in scope.
- Consequence: the rules for "another State statute" (F-governs) are the least secure part, since a statute in a code whose preliminary provisions are not deposited may carry its own definitions.

## Answer table (worked cases)

Every cell below is the value as run; it equals the value written down before the run.

How these were made.
The expected values were written down on 2026-10-21 from the statute text and an independent forward-simulating script (not part of the deposit), before the first run of `usca-interpretation-time.l4`.
They were then evaluated with `l4 run` (one `#EVAL` per cell, 63 in all, the first six sections of `test-usca-worked.l4` and the month-end neighbours of the one-month case) and compared with the values written down.
Result: 63 evaluations, 0 differences.
The same cells are `#ASSERT`s in `test-usca-worked.l4`, all satisfied, so a later change that moves a cell turns the file red.
No cell of this table was edited after a run.
Expectations elsewhere that were corrected after a failing run are listed under "What `check.sh` prints".

Calendars used for the rest-day input (the caller supplies one; the module hard-codes none):

- **G**: Gov. Code § 6800 / Civ. Code §§ 7, 10: Sundays and the days Gov. Code §§ 6700(a) and 6701(a)-(b) fix by the calendar; no Saturdays; no appointed or lunar days.
- **C**: Code Civ. Proc. §§ 10, 12a(a): every Saturday and every Sunday; no § 135 days (§ 135 is not deposited) and no § 12b closures.
- **C+**: C, with the days of G supplied as the § 135 days. That supply is an assumption of the test, not a reading of the text, which does not say what § 135 contains.

"run" is the run-extending reading of the last-day rule (CCP § 12a(a): "to and including the next day that is not a holiday"); "step" is the one-step reading of "it is also excluded" (Gov. Code § 6800, Civ. Code § 10, CCP § 12) applied once.

| period, counted from | last day before the rest-day rule | G (run / step) | C (run / step) | C+ (run / step) | licensed by |
|---|---|---|---|---|---|
| three years from 2025-07-16 | 2028-07-16 (Sunday) | 2028-07-17 / 2028-07-17 | 2028-07-17 / 2028-07-17 | 2028-07-17 / 2028-07-17 | Gov. § 6803 (365 days; the leap day 2028-02-29 and 2028-02-28 are in the period and count as one, so 1096 calendar days), § 6800 |
| five years from 2025-01-15 | 2030-01-15 (Tuesday) | same | same | same | § 6803, § 6800 (leap day of 2028 in the period; 2032 is not) |
| five years from 2025-09-01 | 2030-09-01 (Sunday) | 2030-09-03 / 2030-09-02 | 2030-09-02 / 2030-09-02 | 2030-09-03 / 2030-09-02 | § 6803, § 6800; Monday 2030-09-02 is the first Monday in September (Gov. § 6700(a)(13)) |
| thirty days from 2026-01-01 | 2026-01-31 (Saturday) | 2026-01-31 / 2026-01-31 | 2026-02-02 / 2026-02-01 | 2026-02-02 / 2026-02-01 | § 6800; CCP § 12a(a) makes Saturday a holiday, Gov. § 6700 does not |
| two years from 2024-02-28 | reading S: 2026-02-27 (Friday); reading P: 2026-02-28 (Saturday) | S: 2026-02-27 both; P: 2026-02-28 both | S: 2026-02-27 both; P: 2026-03-02 / 2026-03-01 | S: 2026-02-27; P: 2026-03-02 / 2026-03-01 | § 6803: the day before the added day is 2024-02-28, the excluded first day (§ 6800), so under S the pair does not "occur in" the period |
| one year from 2024-02-29 | 2025-02-28 (Friday) | same | same | same | § 6803 (2024-02-28 is before the period; no pair), § 6800 |
| one month from 2025-01-31 | the text does not say (no 31 February; § 6804 says only "calendar month") | REFUSED | REFUSED | REFUSED | § 6804, § 6800 |

Commencement (Gov. Code § 9600, § 9602):

| case | expected from the text |
|---|---|
| an Act enacted 2026-03-10 at a regular session, none of the § 9600(b) kinds, saying nothing about its own commencement | day: 2027-01-01 (the 90-day period from 2026-03-10 ends 2026-06-08; the next January 1 following it); moment within the day: the text does not say, REFUSED |
| the same Act is an urgency statute, calls an election, levies a tax or appropriates for the usual current expenses | day: 2026-03-10, "immediately upon their enactment", at the moment of enactment (a supplied input) |
| an Act that fixes its own day, later fixed as 2026-06-01 | the text does not say (§ 9600 names no exception for an Act that fixes its own day): day REFUSED, moment REFUSED. A caller who takes the Act's own day to govern gets 2026-06-01, by that assumption alone |
| subordinate legislation made 2026-03-10 and silent | the deposited text has no provision (§ 9600 speaks of statutes, § 9602 of resolutions): REFUSED |
| Civil Code and Code of Civil Procedure themselves | noon, 1873-01-01 (Civ. § 2, CCP § 2); the Government Code's own day is not in the deposit: REFUSED |
| boundary of § 9600(a) | enacted 2026-10-02: 2027-01-01; enacted 2026-10-03: REFUSED (the 90th day is 2027-01-01 itself, and the text does not say whether a January 1 that ends the period is "followed" by that January 1); enacted 2026-10-04: 2028-01-01 |

## What `check.sh` prints

**Target: `unstable`.**
Run as `L4_TARGET=unstable L4=/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4 ./check.sh`; the default target of this copy of `check.sh` is `unstable`, where the skill's own default is `main`.
`l4 --version` prints `dev`; the binary's sha256 is `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`.
With the target `unstable`, `check.sh` skips the `main` comparison, so there are no main columns and no main build to name.

The output of the final run on 2026-10-22, verbatim (standard output, then the one line on standard error and the exit status):

```
module                                    errors satisfied  failed  refused  expected
test-usca-general.l4                           0        98       0        0         0
test-usca-holidays.l4                          0       627       0        0         0
test-usca-operation.l4                         0       123       0        0         0
test-usca-rules.l4                             0       334       0        0         0
test-usca-time.l4                              0       425       0        0         0
test-usca-worked.l4                            0        89       0        0         0
tests-red.l4                                   8         0       8        0         8
usca-general-provisions.l4                     0         0       0        0         0
usca-holidays.l4                               0         0       0        0         0
usca-interpretation-time.l4                    0         0       0        0         0
usca-operation-of-statutes.l4                  0         0       0        0         0
TOTAL (11 modules)                             8      1696       8        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
[stderr] check.sh: the target is unstable, so the main check was skipped.
[exit status 0]
```

**How to read it.**
The `errors` column counts error diagnostics, and a failed assertion is also one, so in `tests-red.l4` the 8 errors are the 8 failed assertions; `expected` is the count `check.sh` was told to expect for that file.
Every other file has 0 errors, 0 failed and 0 refused.
A refused assertion would make the run red, and there is none.
The run is green exactly when every `failed` equals its `expected`.

**Expected failures: `tests-red.l4`, 8 assertions.**
Each states the answer a naive reading gives and the text does not support, so a failure is the module disagreeing with the naive reading.
`check.sh` carries the count in its `expected_failed` table and `encoding.json` in `expected_red`.

| # | The naive answer asserted | The answer the text supports |
|---|---|---|
| 1 | three years from 2025-07-16 end 2028-07-15 (1,095 days) | 2028-07-16: the leap pair of 2028 counts once (Gov. Code § 6803) |
| 2 | five years from 2025-01-15 end 2030-01-14 | 2030-01-15, same reason |
| 3 | five years from 2025-09-01 end 2030-08-31 | 2030-09-01, same reason |
| 4 | ten days from 2026-03-10 end 2026-03-19 (the first day counts) | 2026-03-20 (Gov. Code § 6800 excludes the first day) |
| 5 | thirty days from 2026-01-01 end 2026-02-02 on a calendar of Sundays only | 2026-01-31: a Saturday is not a holiday on that calendar, and § 6700 names no Saturday |
| 6 | the one-step function gives the run answer, 2026-03-17 (last day Saturday 2026-03-14, with Sunday 15 and Monday 16 March also holidays) | the run reading of Code Civ. Proc. § 12a(a) gives 2026-03-17, from the run function; the one-step function returns 2026-03-15, so the assertion fails |
| 7 | a statute enacted 2026-03-10 takes effect 2026-06-08 | 2027-01-01 (Gov. Code § 9600(a)) |
| 8 | daylight saving time is not in effect at 3 a.m. on 8 March 2026 | it is (Gov. Code § 6808(b): commences at 2 a.m.) |

**Findings during the run.**
- **L4's `MODULO` fails on a non-integer operand.**
  The first version of the whole-number test used `n MODULO 1 EQUALS 0`, which crashed on 1.5 ("Expected an Integer").
  The module now uses `FLOOR n EQUALS n`, and the same for the added days of Code Civ. Proc. § 12c(b).
  Reported here for whoever maintains the runtime; not a finding about the statute.
- **My own expectations that were wrong against the text, corrected from the text and not from the module**:
  1 November 2025 is on daylight saving time (the first Sunday of that November is 2 November, so the change has not happened);
  8 November 2026 is a Sunday and so a Civ. Code § 7.1(c) day;
  4 July 2026 is a Saturday and so a Code Civ. Proc. § 12a(a) holiday;
  1 January 2026 is not a Code of Civil Procedure holiday unless § 135 is supplied.
  The working notes record no other change of an expected value after a run, and none in the answer table.
- **No assertion in any file but `tests-red.l4` fails, and none is refused.**
  No disagreement between the code and a value derived from the text was left standing.

**What else was checked, and with what result** (measured on 2026-10-22 against the files as they stand):
- `srcrefs.py check --refs` (the skill's tool, /Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/srcrefs.py; every quotation is the deposited line, and every `@ref` locator names lines that exist): 0 problems in each of the four modules.
  `--strict`, which also wants the lines each locator cites to be the lines quoted in the run directly above it, reports 23, 13, 0 and 5 problems in the time, holiday, operation and general modules (23 + 12 + 4 "cites lines not quoted in the run above it" and 1 + 1 "the run quotes fewer lines than its locator reaches", and no orphan quotation).
  In each case the locator cites lines that the same module quotes somewhere other than directly above the locator (checked: no non-blank line that any locator cites is missing from the quotations of its module), or cites a whole section where the run above it quotes part.
  No quoted line differs from the file.
  The brief does not ask for the strict mode; the skill recommends it for a row whose `@ref`s are kept to the layout convention, and this row's are not, in the places counted.
  They were left as they are.
- Coverage: the `.txt` files hold 159 sections; the coverage table above has 159 rows, plus a second table for the 7 numbers missing from the text.
- **Mutation check of the tests** (a scratch script, written for this run, removed at the end, so it is not in the row; run on 2026-10-22 on the files as shipped; afterwards only the header comments of `test-usca-time.l4` and `test-usca-holidays.l4` were reworded, and no assertion changed).
  It applies one change at a time to a module (swap `PLUS` and `MINUS`, `AND` and `OR`, `GREATER THAN` and `AT LEAST`, `LESS THAN` and `AT MOST`, `EQUALS` and `GREATER THAN`, `THEN TRUE` and `THEN FALSE`; add 1 to a constant such as 365, 91, 43200, 54000, 7, 28, 29), runs the tests that import the module, and counts the mutant killed if any assertion fails or is refused, or the run errors.
  It leaves out comments, names in backticks and the text of refusal messages.
  Result: 366 mutants, 357 killed (356 by a failed or refused assertion, 1 by another error), 9 survived.

  | module | mutants | killed | survived |
  |---|---|---|---|
  | `usca-interpretation-time.l4` | 131 | 128 | 3 |
  | `usca-holidays.l4` | 191 | 188 | 3 |
  | `usca-operation-of-statutes.l4` | 21 | 18 | 3 |
  | `usca-general-provisions.l4` | 23 | 23 | 0 |

  The 9 survivors, each read and none a hole in a test:
  - `usca-holidays.l4`, the two `PLUS 7` to `MINUS 7` mutants in the helpers for "the n-th" and "the last" weekday of a month (lines 55 and 62): the number sits inside `( ... ) MODULO 7`, and `MODULO` takes the floor, so adding or subtracting 7 leaves the remainder as it was (measured with a probe of `(0 MINUS 3) MODULO 7`, which is 4).
  - `usca-holidays.l4` line 244, `LESS THAN 54000` to `AT MOST 54000`: the two readings differ only at the instant 3 p.m., which the line above refuses ("does not say whether the instant of 3 p.m. is inside"). The neighbouring mutant, 54000 to 54001, did not survive: half-second readings test it.
  - `usca-interpretation-time.l4` line 175, the starting guess `Day firstDay PLUS units` of the search that finds the day on which a count of units ends: the search repeats until its guess reproduces itself, so a different start reached the same day on every input the tests use. Not proved for every input.
  - `usca-interpretation-time.l4` line 409, `GREATER THAN sunrise` and `LESS THAN sunset` each to the inclusive form: they differ only at the instants of sunrise and sunset themselves, which an earlier line refuses (fork F-daytime).
  - `usca-operation-of-statutes.l4` lines 189 and 426, `GREATER THAN` to `AT LEAST` on the order of enactment and on the section number: they differ only when the two are equal, which an earlier line refuses.
  - `usca-operation-of-statutes.l4` line 191, the same mutation on the chapter rank: the value is read only when the two ranks differ.
  Earlier runs on earlier states of the files left more survivors, and they changed the tests.
  A first run of the holiday module (189 mutants) had 29 survivors, 24 of them in Civ. Code § 7.1, 23 of those in its rules (q) and (r) (a Monday after a Sunday holiday, a Friday before a Saturday holiday), which only a few hand-picked dates tested; whole-year tests of § 7.1 against a Python rendering of the section were added.
  A second run, on the lines then changed, still had survivors in the same rule, because no year from 2024 to 2030 has January 1 on a Sunday (2023 and 2034 do), so the range of the whole-year tests was widened to 2022-2035.
  It also had a survivor at the Good Friday boundary (54000 to 54001) that only a reading between whole seconds can tell apart; half-second tests were added.
- Not run: the independent test pass of the skill (step 8) and any run against `main`.

## Open questions for a domain expert

Each question is one the deposited text does not answer, with the way the code leaves it.
The numbers are the fork or question identifiers used elsewhere in this file.

1. **Q-135.** What are the judicial holidays "specified in Section 135" of the Code of Civil Procedure?
   § 135 is not deposited.
   They are an input, and a caller who supplies none gets Saturdays and Sundays only under the Code of Civil Procedure calendars.
   Should the holiday function refuse unless the caller says the list is complete?
2. **Q-contract.** Do Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. §§ 12 and 12a reach a period fixed by contract ("within 30 days of signing")?
   The sections speak of an act "provided by law"; only §§ 6706, 11 and 13 mention contract, and only for an act on a particular day.
3. **Q-commence.** Does § 6800 apply to the 90-day period of Gov. Code § 9600(a), so that the day of enactment is excluded?
   The code excludes it; counting the day of enactment as day 1 moves every boundary one day later, and the refused case from 3 October to 4 October.
   What is "next following" when the 90th day is itself a January 1?
4. **Q-own-day.** May a statute name its own day of effect, and if so does that displace § 9600(a)?
   The text of § 9600 neither allows nor forbids it, and the code refuses.
   (The Constitution is not deposited.)
5. **Q-enactment.** Is "the date of enactment" the day a bill is passed, signed or chaptered?
   It is an input.
6. **Q-moment.** From which moment of its day does a statute under § 9600(a) bind: the midnight that begins it, or another moment?
   Refused; the helper for the midnight reading is an explicit assumption.
7. **Q-governs.** Which definitions of "holiday" and "month" reach a statute of another code, and an ordinance, rule or regulation?
   The code gives another State statute the Government Code's, as an assumption, and refuses for an ordinance, rule or regulation.
8. **Q-pair.** Does the leap-day pair of Gov. Code § 6803 "occur in" a period whose excluded first day is 28 February?
   Two readings are offered; the literal one is the headline.
9. **Q-month.** What is the last day of one month from 31 January, or from the 29th to 31st of another month, when the month reached is shorter?
   The text says only "a calendar month"; the code refuses.
10. **Q-run.** After a last day that is a holiday, does the one-step exclusion of § 6800 stop at the next day, or carry on as § 12a(a) does?
    Both are offered; the run reading is the headline.
11. **Q-vintage.** Which version of each section governs a date before the deposited version took effect?
    Only the current version is deposited; the holiday list in § 6700 was last amended with effect from 26 March 2026.
12. **Q-1752.** What does § 6801 require of a date before 1752, and which hundredth years before 1900 are leap years?
    The leap-year function refuses a hundredth year before 1900; no other date is checked against 1752.
13. **Q-service.** Where is the rule that deems service or notice made on a day?
    None is in the deposit.
    If one exists it is in a part of the codes outside the six files, so both functions refuse.
14. **Q-hol-6.** Is a day proclaimed under one of Gov. Code §§ 6708-6736 a day "appointed ... for a public fast, thanksgiving, or holiday" within § 6700(a)(20)(A)?
15. **Q-6701.** Does March 31 stop being a holiday when the Legislature observes it on another day (§ 6701(c))?
    Does the Saturday stop being one for county employees when a board names an alternate day (§ 6701(d))?
    Are the days § 6701(a) and (b) add "enumerated in Section 6700" for a city's offices (§ 6702)?
16. **Q-9605b.** Which presumption of § 9605(b) governs when the statute enacted last and the statute with the higher chapter number are different statutes?
17. **Q-9607b, Q-9611.** Is the "date of termination" in § 9607(b) the last day the law operates or the first it does not?
    On which day does the original provision resume under § 9611?
18. **Q-ccp9.** In Code Civ. Proc. § 9, are the days already run counted with or without the day the code took effect?
19. **Q-12c.** Which way does a last day move that falls on a holiday when counted backward from a hearing?
    Refused.
20. **Q-scope.** Is the cluster the right one?
    The Penal Code and Evidence Code preliminary provisions, and every other code's general provisions, are outside it, and § 9603 says the rules are spread across "the different codes".
21. **Q-source.** The six `.txt` files are converter-made; is any section different in the official text?
22. **Q-FALSE.** Is the convention that `FALSE` means "this section does not give this result" the one a reviewer wants, or should those functions refuse?
    It is used, as a constant `FALSE`, for Gov. Code § 9605(a)(1) (an amended section is not repealed and re-enacted), § 9610 (a statute fixing a salary is not an appropriation), § 9611 (a temporarily suspended law is not repealed), Civ. Code § 20 and Code Civ. Proc. § 18 (the repeal by the code revives no former law) and Civ. Code § 23.2 (one of the four codes does not prevail over another by being later).
