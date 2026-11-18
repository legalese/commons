# PLAN: the Companies Act 1967 (Singapore), keel

The keel agent's plan for the 11 part agents of wave 1 and the later waves. Text: the Singapore Statutes Online informal consolidation, 2020 Revised Edition, in force 6 May to 20 October 2026, as `inputs/CoA1967.txt` renders it. It is a rendering of the Act, not the official text; nothing here claims to be checked against the official text.


## 1. Purpose and how to read this plan

**What this is.** The keel is the shared vocabulary and definitional core of the whole Act, in L4 on the stable build (1.6.110; it must also pass on 1.6.109). It covers Part 1 (ss 1 to 7A: the opening, the repeals, the interpretation section with its 92 defined terms, subsidiary, holding company, wholly owned subsidiary, related corporations, interests in shares, the solvency statement) and s 10 (who may be a company's auditor), and it holds the one place where the Act's periods are counted.
You, a part agent, cannot talk to the keel or to another part. This plan is all you share. Read it before opening the text, then read `sg-core.l4` and the module files named in your row (section 6), which sit read-only beside your own files.

**How the modules fit.** Import `prelude`, `daydate` and `sg-core`, then only the keel modules your row names (a name defined in two imported modules cannot be used at all, and the keel's names are made not to collide with a part's, section 2). Never edit a keel file; a part that lacks a type or a constructor defines its own under its own provision label and records it in `NEEDS-CORE.md` for the lead to hoist at the merge.

**What every function answers.** Almost every function of the keel answers `MAYBE BOOLEAN`: `JUST TRUE` is yes, `JUST FALSE` is the text saying no in its own words, `NOTHING` is "the text does not say". A caller must never turn `NOTHING` into `FALSE`. The few plain `BOOLEAN`, `NUMBER`, `STRING` and `DATE` functions say so in section 3. The rule of 2026-10-29 (assumed, not ruled by a lawyer) and the keel's use of it are in `NOTES.md`, "Reading a result: FALSE and NOTHING (keel)".

**What is assumed, not ruled.** The counting of periods (Interpretation Act 1965 is not a source): P1 to P9 in `sg-periods.l4` and `NOTES.md`. The two readings "for a lawyer" (a failed "if" counts as the text's no; a prohibition or grant limited by its own wording does not). Every site is listed in `NOTES.md`.

**Where to look.** Section 2 is the naming rule; section 3 the names and types, module by module; section 4 the seams (what your provision needs from another part, as an input); section 5 the traps on the stable binary; section 6 your row; section 7 the seat layer and the input names every seat shares; section 8 the `NOTES.md` sections you must write and the two split-site questions.


## 2. Naming rule

1. **Every top-level name a part defines begins with the label of the provision it implements**, in the Act's own numbering: `s 76B(1)(a) the company may acquire its own shares`, `sch 13 para 2 the company is a small company`. This covers functions, constants, types and constructors, not only functions: write `` DECLARE `s 76 assistance status` IS ONE OF `s 76 assistance permitted`, `s 76 assistance not covered` ``, never a bare `Not entitled`. Parentheses inside a backtick name parse on the stable binary.
2. **The keel's names begin** `s 4(`, `s 5`, `s 5(`, `s 5A`, `s 5B`, `s 6`, `s 7`, `s 7A`, `s 10`, `period:` or `Period`, `the day ...` (two constants) or are the unprefixed nouns of `sg-core.l4` (`Party`, `Corporation`, `Liability of members`, `Kind of share`, `Class of shares`, `Kind of resolution`, `Kind of meeting`, `Proposal needing a solvency statement`, `Solvency statement`, with their constructors and field names). **A part never defines a name that begins with one of those, and never defines a bare noun**; its own section numbers keep its names apart (`s 76B` is not `s 7`, and not `s 7A`).
3. **A part never edits a keel module and never waits for one.** A type or constructor it needs and the core lacks is defined in its own module under its own label and recorded in `NEEDS-CORE.md`.
4. **File names.** Every module of part `X` begins `X-` (`sga1-`, `sgb2-`, ...), every module of the keel begins `sg-`. A `.l4` file cannot import a module sharing its own basename (a silent `GraphException`).
5. **Input names.** An input is named for the FACT, in the person's words, never for a default or the rule it feeds (`the company has more than one class of shares`, not `presumed single class`). The same fact keeps the same name and the same `@desc` everywhere. Section 7 fixes the names shared by every seat.
6. **Dates** are `Date day month year`; never define `YMD`. **Money** is a `NUMBER` in Singapore dollars. **Periods** are counted by `period:` functions only (section 3); a part never writes its own date arithmetic.


## 3. The core and the keel's modules: names, types, one-line glosses, and the exact function names a part would call

Every function name below is copied from the code by script (`work/gen_plan.py`); the argument lists are in the order the function takes them. Every `s 4(1) "TERM"` function is one function per defined term; a term that points at another Act takes the fact that the other Act's test is met as a `BOOLEAN`, named for the fact.

**sg-core.l4** (imports `prelude`, `daydate` only; no rule). Types, one line each:
- `Party`: who a regulative rule is about. Constructors with a name (`STRING`): `Individual` (`the name of the person`), `Company` (`the name of the company`), `Director` (`the name of the director`), `Officer` (`the name of the officer`), `Secretary` (`the name of the secretary`), `Member` (`the name of the member`), `Creditor` (`the name of the creditor`), `Auditor` (`the name of the auditor`); without a name: `Registrar`, `Minister`, `Court`, `Authority` (offices of the State: they appear only as what they mean to the individual).
- `Corporation`: a corporation known by its name (`the name of the corporation`); groups are lists of these.
- `Liability of members`: `limited by shares`, `limited by guarantee`, `limited by shares and by guarantee` (exists only until the end of the period in s 17(6)), `unlimited`.
- `Kind of share`: `an ordinary share`, `a preference share`, `a redeemable preference share`, `a treasury share`.
- `Class of shares`: record `the name of the class`, `the kind of share in the class`, `the number of issued shares in the class`.
- `Kind of resolution`: `an ordinary resolution`, `a special resolution`, `a resolution of the directors`.
- `Kind of meeting`: `an annual general meeting`, `an extraordinary general meeting`, `the statutory meeting`, `a meeting of a class of members`, `a meeting of creditors`.
- `Proposal needing a solvency statement`: `a redemption of preference shares out of capital under section 70`, `a giving of financial assistance under section 76(9A) or (9B)`, `a reduction of share capital under section 78B or 78C`, `some other proposal`.
- `Solvency statement`: record of what a statement says and how it was made out: `the proposal it concerns`, `the date of the statement`, `it is a statement by the directors of the company`, the four opinions (a), (b)(i), (b)(ii), (c) now and (c) after the proposal, `the directors intend to commence winding up of the company within the 12 months immediately after its date`, `the number of directors of the company`, `the number of directors who have signed it as a written declaration`, `it is accompanied by a report from the company's auditor ...`. It carries no rule; `s 7A(1) the statement is a solvency statement` decides.
- Constants: `the day 29 December 1967` (s 3(2), s 4(1) "private company") and `the day 3 January 2016` (s 4(1) "constitution", s 4(13)).

A rule such as "is the company private?" is not in the core: it is a rule (`s 4(1) "private company" ...`), asked in a seat as the input `the company is a private company` (section 7).

**sg-periods.l4** (imports `prelude`, `daydate` only). The one place where periods are counted. `Period unit` is one of `Days`, `Weeks`, `Months`, `Years`. Conventions P1 to P9 are in the module header and the fork register of `NOTES.md` (assumed, not ruled).

- `period: the last day of a period after`
  - takes: the day of the event (DATE); the number of units (NUMBER); the unit (Period unit)
  - answers: DATE. The last day on which an act "within N units after X" may be done: the day of the event is not counted (P1).
- `period: the date is within a period after`
  - takes: the day of the event (DATE); the day the act is done (DATE); the number of units (NUMBER); the unit (Period unit)
  - answers: BOOLEAN. TRUE from the day after the event to the last day, both ends included; an act on the day of the event itself is not within it (P2).
- `period: the date is not later than the end of a period after`
  - takes: the day of the event (DATE); the day the act is done (DATE); the number of units (NUMBER); the unit (Period unit)
  - answers: BOOLEAN. TRUE on every day up to and including the last day, an early act included (P2); use it for "not later than N days after".
- `period: the latest day for an act a period before`
  - takes: the day of the event (DATE); the number of units (NUMBER); the unit (Period unit)
  - answers: DATE. The last day on which an act "not less than N units before X" may be done (P5).
- `period: the date is at least a period before`
  - takes: the day the act is done (DATE); the day of the event (DATE); the number of units (NUMBER); the unit (Period unit)
  - answers: BOOLEAN. TRUE where the act is done on or before the latest day (P5).
- `period: the date is within a period before`
  - takes: the day the act is done (DATE); the day of the event (DATE); the number of units (NUMBER); the unit (Period unit)
  - answers: BOOLEAN. TRUE for "within N months before X": from the corresponding date N months earlier up to the day before X (P6).
- `period: the latest day for an act at least a number of clear days before`
  - takes: the day of the event (DATE); the number of clear days (NUMBER)
  - answers: DATE. "N clear days before X": excludes both the day of the act and the day of the event (P7, the alternative to P5).
- `period: the earliest day for an act after a number of clear days from`
  - takes: the day of the event (DATE); the number of clear days (NUMBER)
  - answers: DATE. "N clear days from X": the earliest day (P7).
- `period: the last day of the calendar month containing`
  - takes: the date (DATE)
  - answers: DATE. The last day of the month the date falls in.
- `period: the date is a business day`
  - takes: the date (DATE); the public holidays (LIST OF DATE)
  - answers: BOOLEAN. Plain BOOLEAN over a supplied list of public holidays: not a Saturday, a Sunday or a listed public holiday.
- `s 4(1) "business day" the date is a business day`
  - takes: the date (DATE); the public holidays (LIST OF DATE)
  - answers: MAYBE BOOLEAN. The s 4(1) definition itself: JUST TRUE for a day other than a Saturday, Sunday or listed public holiday; JUST FALSE otherwise ("means").
- `period: the day reached counting business days`
  - takes: the day counted from (DATE); the business days still to count (NUMBER); the public holidays (LIST OF DATE)
  - answers: DATE. Counts business days from the day after `the day counted from`, skipping weekends and the listed public holidays (P8).
- `period: the last day of a number of business days after`
  - takes: the day of the event (DATE); the number of business days (NUMBER); the public holidays (LIST OF DATE)
  - answers: DATE. The last day of "within N business days after X" (P8).
- `period: the date is within a number of business days after`
  - takes: the day of the event (DATE); the day the act is done (DATE); the number of business days (NUMBER); the public holidays (LIST OF DATE)
  - answers: BOOLEAN. TRUE from the day after X up to the last day of the N business days (P2, P8).

**sg-definitions.l4** (imports `prelude`, `daydate`, `sg-core`). s 4(1), 90 of its 92 terms (the other two are `"business day"` in `sg-periods.l4` and `"related corporation"` in `sg-groups.l4`; one more entry of s 4(1) is shown deleted), and s 4(2). Types: `s 4(1) body` (ten facts about a body: incorporated outside Singapore, a cooperative society, a limited liability partnership, and so on; it feeds `"corporation"` and `"foreign company"`), `s 4(1) "officer" what the person is`, `s 4(1) "identification" kind of person`, `s 4(1) "commencement of winding up" kind of winding up`. A closed ("means") term answers `JUST FALSE` off its definition; an open ("includes") term answers `NOTHING` off its list. Call these as functions of the facts a witness could state; where a term hands a matter to another Act, the fact "that Act's test is met" is the argument.

- `s 4(1) "accounting corporation" the company is an accounting corporation`
  - takes: the company is approved, or deemed to be approved, as an accounting corporation under the Accountants Act 2004 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "accounting entity" the person is an accounting entity`
  - takes: the person is a public accountant (BOOLEAN); the person is an accounting corporation (BOOLEAN); the person is an accounting firm (BOOLEAN); the person is an accounting limited liability partnership (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "accounting firm" the firm is an accounting firm`
  - takes: the firm is approved, or deemed to be approved, as an accounting firm under the Accountants Act 2004 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "accounting limited liability partnership" the limited liability partnership is an accounting limited liability partnership`
  - takes: the limited liability partnership is approved as an accounting limited liability partnership under the Accountants Act 2004 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "accounting records" the paper or document is within the accounting records of the corporation`
  - takes: the paper or document is a working paper or other document necessary to explain the methods and calculations by which the accounts of the corporation are made up (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "Accounting Standards" the standards are the Accounting Standards`
  - takes: the standards are made or formulated by the Accounting Standards Committee under Part 3 of the Accounting Standards Act 2007 (BOOLEAN); the standards are applicable to companies and to foreign companies in respect of their operations in Singapore for the purposes of this Act (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "accounts" the thing is within the word accounts`
  - takes: the thing is a profit and loss account or a balance sheet (BOOLEAN); the thing is a note attached or intended to be read with a profit and loss account or balance sheet (BOOLEAN); the note is an auditors' report or a directors' report (BOOLEAN)
  - answers: MAYBE BOOLEAN. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.
- `s 4(1) "ACRA administered Act" the written law is an ACRA administered Act`
  - takes: the written law is the Accounting and Corporate Regulatory Authority Act 2004 (BOOLEAN); the written law is specified in the Second Schedule to the Accounting and Corporate Regulatory Authority Act 2004 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "Act" the instrument is within the word Act`
  - takes: the instrument is a regulation made under this Act (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "annual general meeting" the meeting is an annual general meeting of the company`
  - takes: the meeting is a meeting of the company required to be held by section 175 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "annual return" the return is the annual return`
  - takes: the return is the return required to be lodged under section 197(1) (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "approved exchange in Singapore" the exchange is an approved exchange in Singapore`
  - takes: the exchange is an approved exchange as defined in section 2(1) of the Securities and Futures Act 2001 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "audit requirements" the requirement is within the audit requirements`
  - takes: the requirement is a requirement of section 201(8) or (9) (BOOLEAN); the requirement is a requirement of section 207 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "Authority" the body is the Authority`
  - takes: the body is the Accounting and Corporate Regulatory Authority established under the Accounting and Corporate Regulatory Authority Act 2004 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "Authority's website" the website is the Authority's website`
  - takes: the website is the Authority's Internet website (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "banking corporation" the body is a banking corporation`
  - takes: the body is a bank or merchant bank licensed under the Banking Act 1970 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "book-entry securities" the securities are book-entry securities`
  - takes: the securities are book-entry securities as section 81SF of the Securities and Futures Act 2001 gives that meaning (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "books" the record is within the books of the corporation`
  - takes: the record is an account, deed, writing or document (BOOLEAN); the record is any other record of information, however compiled, recorded or stored, whether in written or printed form or on microfilm or by electronic process or otherwise (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "borrowing corporation" the corporation is a borrowing corporation`
  - takes: the corporation is or will be under a liability (whether or not present or future) to repay money (BOOLEAN); the money was received, or is to be received, by the corporation in response to an invitation to the public to subscribe for or purchase debentures of the corporation (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "branch register" the register is a branch register of the company`
  - takes: the register is a branch register of members of the company kept pursuant to section 196 (BOOLEAN); the register is a branch register of holders of debentures kept pursuant to section 93 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "certified" the copy or translation is certified`
  - takes: the document is a copy of a document and is certified in the prescribed manner to be a true copy of it (BOOLEAN); the document is a translation of a document and is certified in the prescribed manner to be a correct translation of it into the English language (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "charge" the thing is within the word charge`
  - takes: the thing is a mortgage (BOOLEAN); the thing is an agreement to give or execute a charge or mortgage, whether upon demand or otherwise (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "chief executive officer" the person is a chief executive officer of the company`
  - takes: the person is in direct employment of, or acting for or by arrangement with, the company (BOOLEAN); the person is principally responsible for the management and conduct of the business of the company, or part of the business of the company (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "commencement of winding up" the date the winding up commences`
  - takes: kind (s 4(1) "commencement of winding up" kind of winding up); the date section 126 of the Insolvency, Restructuring and Dissolution Act 2018 gives as the commencement of the winding up by the Court (DATE); the date section 161(6) of the Insolvency, Restructuring and Dissolution Act 2018 gives as the commencement of the voluntary winding up (DATE)
  - answers: MAYBE DATE. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "company" the body is a company`
  - takes: the body is a company incorporated under this Act (BOOLEAN); the body is a company incorporated under a corresponding previous written law (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "company having a share capital" the company is within the words company having a share capital`
  - takes: the company is an unlimited company with a share capital (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "company limited by guarantee" the company is a company limited by guarantee`
  - takes: liability (Liability of members)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "company limited by shares" the company is a company limited by shares`
  - takes: liability (Liability of members)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "constitution" the document is the constitution of the company`
  - takes: the document is the constitution of the company registered with the Registrar under section 19, as amended from time to time (BOOLEAN); the date the company was incorporated (DATE); the document is the memorandum of association, the articles of association, or both, of the company in force immediately before 3 January 2016 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "contact address" the address is a contact address of the individual`
  - takes: the address is a physical address at which the individual can be physically found or contacted by post (BOOLEAN); the address is a post office box number (BOOLEAN); the address is located in the same jurisdiction as the individual's residential address (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "contributory" the person is within the word contributory`
  - takes: the person is liable to contribute to the assets of the company in the event of its being wound up (BOOLEAN); the person is the holder of fully paid shares in the company (BOOLEAN); the persons who are contributories have not yet been finally determined and the person is alleged to be a contributory (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "corporation" the body is a corporation`
  - takes: body (s 4(1) body)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "Court" the court is the Court`
  - takes: the court is the General Division of the High Court (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "corresponding previous written law" the law is a corresponding previous written law`
  - takes: the law is a written law relating to companies (BOOLEAN); the law has at any time been in force in Singapore (BOOLEAN); the law corresponds with a provision in this Act (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "debenture" the instrument is a debenture`
  - takes: the instrument is debenture stock, a bond, a note or any other security of a corporation, whether constituting a charge on the assets of the corporation or not (BOOLEAN); the instrument is a cheque, a letter of credit, an order for the payment of money or a bill of exchange (BOOLEAN); the instrument is a promissory note (BOOLEAN); the face value of the promissory note, in Singapore dollars (NUMBER); the maturity period of the promissory note, in months (NUMBER); the regulations made under this Act change the terms on which a promissory note is excluded (BOOLEAN); the instrument is a document that regulations made under this Act prescribe, for the provision in question, as one the word debenture does not include (BOOLEAN)
  - answers: MAYBE BOOLEAN. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.
- `s 4(1) "default penalty" the penalty is a default penalty`
  - takes: the penalty is a default penalty within the meaning of section 408 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "Depository" the body is the Depository`
  - takes: the body is the Depository as section 81SF of the Securities and Futures Act 2001 gives that meaning (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "director" the person is within the word director`
  - takes: the person occupies the position of director of the corporation, by whatever name called (BOOLEAN); the directors or the majority of the directors of the corporation are accustomed to act in accordance with the person's directions or instructions (BOOLEAN); the directors or the majority of the directors act on advice the person gives in a professional capacity, and that is the only reason they follow the person (BOOLEAN); the person is an alternate or substitute director (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "document" the thing is within the word document`
  - takes: the thing is a summons, order or other legal process (BOOLEAN); the thing is a notice (BOOLEAN); the thing is a register (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "electronic communication" the communication is an electronic communication`
  - takes: the communication is transmitted (from one person to another, from one device to another, from a person to a device or from a device to a person) by means of a telecommunication system (BOOLEAN); the communication is transmitted (from one person to another, from one device to another, from a person to a device or from a device to a person) by other means but while in an electronic form (BOOLEAN); it can (where particular conditions are met) be received in legible form or be made legible following receipt in non-legible form (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "electronic transaction system" the system is the electronic transaction system`
  - takes: the system is the electronic transaction system mentioned in section 12A(1) (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "emoluments" the payment is within the emoluments of the director or auditor`
  - takes: the payment is a fee, percentage or other payment made, or consideration given, including the money value of any allowances or perquisites (BOOLEAN); the payment is made or given, directly or indirectly, to the director or auditor (BOOLEAN); the payment is made or given by the company, or by a holding company or a subsidiary of the company (BOOLEAN); the payment is made or given to the director or auditor in that capacity, or otherwise in connection with the affairs of the company or of the holding company or the subsidiary (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "exempt private company" the company is an exempt private company`
  - takes: the company is a private company (BOOLEAN); no beneficial interest in the shares of the company is held directly or indirectly by any corporation, as s 4(1) defines the word (BOOLEAN); the number of members of the company (NUMBER); the company is wholly owned by the Government (BOOLEAN); the Minister, in the national interest, has declared the company by notification in the Gazette to be an exempt private company (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "expert" the person is within the word expert`
  - takes: the person is an engineer (BOOLEAN); the person is a valuer (BOOLEAN); the person is an accountant (BOOLEAN); the person is another whose profession or reputation gives authority to a statement made by him or her (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "filed" the document is filed`
  - takes: the document is filed under this Act (BOOLEAN); the document is filed under a corresponding previous written law (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "financial year" the period is a financial year of the corporation`
  - takes: the period is the period in respect of which the financial statements of the corporation are made up, whether that period is a year or not (BOOLEAN); the corporation is a company (BOOLEAN); the period is a financial year of the company as section 198 determines (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "foreign company" the body is a foreign company`
  - takes: body (s 4(1) body)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "full name" the full name of the individual`
  - takes: the individual is registered under the National Registration Act 1965 (BOOLEAN); the name as it appears in the latest identity card issued to the individual under section 9 of that Act (STRING); the name as it appears in the latest passport issued to the individual, or such other similar evidence of identification as is available (STRING)
  - answers: STRING. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.
- `s 4(1) "identification" the identification of the person`
  - takes: kind (s 4(1) "identification" kind of person); the number of the individual's identity card (STRING); the particulars of the individual's passport, or of such other similar evidence of identity as is acceptable to the Registrar (STRING); the unique entity number of the person issued by a public agency (STRING); the unique entity number of the person issued by the Registrar (STRING); the identification number or registration number of the person on the corporate entity register of the jurisdiction where it is formed or incorporated, or other similar evidence of identity acceptable to the Registrar (STRING)
  - answers: STRING. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.
- `s 4(1) "liquidator" the person is within the word liquidator`
  - takes: the person is the Official Receiver acting as the liquidator of a corporation (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "limited company" the company is a limited company`
  - takes: liability (Liability of members); the period of 2 years specified in section 17(6) has expired (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "limited liability partnership" the partnership is a limited liability partnership`
  - takes: the partnership is a limited liability partnership as section 2(1) of the Limited Liability Partnerships Act 2005 gives that meaning (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "listed" the company or corporation is listed`
  - takes: the company or corporation has been admitted to the official list of an approved exchange in Singapore (BOOLEAN); the company or corporation has been removed from that official list (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "lodged" the document is lodged`
  - takes: the document is lodged under this Act (BOOLEAN); the document is lodged under a corresponding previous written law (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "marketable securities" the thing is within the marketable securities`
  - takes: the thing is a debenture, fund, stock, share or bond of a government, a local authority, or a corporation or society (BOOLEAN); the thing is a right or option in respect of shares in a corporation (BOOLEAN); the thing is a unit in a collective investment scheme within the meaning of section 2 of the Securities and Futures Act 2001 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "minimum subscription" the minimum subscription`
  - takes: the shares are offered to the public for subscription (BOOLEAN); the amount stated in the prospectus relating to the offer as the minimum amount which in the opinion of the directors must be raised by the issue of the shares offered, in Singapore dollars (NUMBER)
  - answers: MAYBE NUMBER. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "office copy" the copy is an office copy`
  - takes: the copy is a copy of a Court order or other Court document (BOOLEAN); the copy is authenticated under the hand or seal of the Registrar or other proper officer of the Court (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "officer" the person is an officer of the corporation`
  - takes: position (s 4(1) "officer" what the person is)
  - answers: MAYBE BOOLEAN. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.
- `s 4(1) "Official Assignee" the person is within the words Official Assignee`
  - takes: the person is the Official Assignee appointed under section 16(1) of the Insolvency, Restructuring and Dissolution Act 2018 (BOOLEAN); the person is a Deputy Official Assignee, a Senior Assistant Official Assignee or an Assistant Official Assignee (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "Official Receiver" the person is within the words Official Receiver`
  - takes: the person is the Official Receiver appointed under section 17(1) of the Insolvency, Restructuring and Dissolution Act 2018 (BOOLEAN); the person is a Deputy Official Receiver, a Senior Assistant Official Receiver or an Assistant Official Receiver (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "prescribed" the matter is prescribed`
  - takes: the matter is prescribed under this Act (BOOLEAN); the matter is prescribed by the rules (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "principal register" the register is the principal register of the company`
  - takes: the register is the register of members of the company kept pursuant to section 190 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "printed" the thing is within the word printed`
  - takes: the thing is typewritten (BOOLEAN); the thing is lithographed (BOOLEAN); the thing is reproduced by any mechanical means (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "private company" the company is a private company`
  - takes: the company, immediately before 29 December 1967, was a private company under the repealed written laws (BOOLEAN); the company was incorporated as a private company by virtue of section 18 (BOOLEAN); the company was converted into a private company pursuant to section 31(1) (BOOLEAN); the company has ceased to be a private company under section 31 or 32 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "profit and loss account" the account is within the words profit and loss account`
  - takes: the account is an income and expenditure account or a revenue account (BOOLEAN); the account is any other account showing the results of the business of a corporation for a period (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "prospectus" the document is a prospectus`
  - takes: the document is a prospectus, notice, circular, material, advertisement, publication or other document (BOOLEAN); the document invites applications or offers from the public to subscribe for or purchase, or offers to the public for subscription or purchase (BOOLEAN); the document concerns shares in or debentures of, or units of shares in or debentures of, a corporation or proposed corporation (BOOLEAN); the document is deemed to be a prospectus under section 257 of the Securities and Futures Act 2001 (BOOLEAN); the document is a profile statement (BOOLEAN); the document is material, an advertisement or a publication authorised by section 251 (other than subsection (5)) of the Securities and Futures Act 2001 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "public accountant" the person is a public accountant`
  - takes: the person is registered, or deemed to be registered, under the Accountants Act 2004 as a public accountant (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "public agency" the body is a public agency`
  - takes: the body is a public officer (BOOLEAN); the body is an Organ of State (BOOLEAN); the body is a ministry or department of the Government (BOOLEAN); the body is a body or authority established by or under a public Act to perform or discharge a public function (BOOLEAN); the body is a member, an officer or an employee of any of these, or any department of any of these (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "public company" the company is a public company`
  - takes: the body is a company (BOOLEAN); the company is a private company (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "registered" the thing is registered`
  - takes: the thing is registered under this Act (BOOLEAN); the thing is registered under a corresponding previous enactment (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "registered corporate service provider" the person is a registered corporate service provider`
  - takes: the person is a registered corporate service provider as section 2(1) of the Corporate Service Providers Act 2024 gives that meaning (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "registered qualified individual" the person is a registered qualified individual`
  - takes: the person is a registered qualified individual as section 2(1) of the Corporate Service Providers Act 2024 gives that meaning (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "Registrar" the person is within the word Registrar`
  - takes: the person is the Registrar of Companies appointed under this Act (BOOLEAN); the person is a Deputy or Assistant Registrar of Companies (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "regulations" the instrument is within the word regulations`
  - takes: the instrument is a regulation made under this Act (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "repealed written laws" the written law is one of the repealed written laws`
  - takes: the written law is a written law repealed by this Act (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "residential address" the residential address of the person`
  - takes: the person is registered under the National Registration Act 1965 (BOOLEAN); the place of residence of the person as registered under that Act (STRING); the usual residential address of the person (STRING)
  - answers: STRING. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.
- `s 4(1) "Rules" the rules are the Rules`
  - takes: the rules are Rules of Court (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "share" the thing is a share`
  - takes: the thing is a share in the share capital of a corporation (BOOLEAN); the thing is stock (BOOLEAN); a distinction between stocks and shares is expressed or implied (BOOLEAN)
  - answers: MAYBE BOOLEAN. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.
- `s 4(1) "solicitor" the person is a solicitor`
  - takes: the person is an advocate and solicitor of the Supreme Court (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "statutory meeting" the meeting is the statutory meeting`
  - takes: the meeting is the meeting mentioned in section 174 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "statutory report" the report is the statutory report`
  - takes: the report is the report mentioned in section 174 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "summary financial statement" the statement is a summary financial statement`
  - takes: the statement is a summary financial statement referred to in section 203A (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "telecommunication system" the system is a telecommunication system`
  - takes: the system is a telecommunication system as the Telecommunications Act 1999 gives that meaning (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "treasury share" the share is a treasury share`
  - takes: the share was, or is treated as having been, purchased by a company in circumstances in which section 76H applies (BOOLEAN); the share has been held by the company continuously since it was so purchased (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "unit" the right or option is within the word unit`
  - takes: the thing is a right or interest, whether legal or equitable, in the share, debenture or other interest, by whatever name called (BOOLEAN); the thing is an option to acquire any such right or interest in the share, debenture or other interest (BOOLEAN)
  - answers: MAYBE BOOLEAN. Open ("includes"): JUST TRUE where a listed limb holds, NOTHING otherwise.
- `s 4(1) "unlimited company" the company is an unlimited company`
  - takes: liability (Liability of members)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "VCC" the company is a VCC`
  - takes: the company is a VCC or variable capital company as defined in section 2(1) of the VCC Act (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "VCC Act" the Act is the VCC Act`
  - takes: the Act is the Variable Capital Companies Act 2018 (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "virtual meeting technology" the technology is virtual meeting technology`
  - takes: the technology allows a person to participate in a meeting without being physically present at the place of meeting (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(1) "voting share" the share is a voting share`
  - takes: the share is an issued share in the body corporate (BOOLEAN); no right to vote is attached to the share in any circumstances (BOOLEAN); a right to vote is attached to the share only in one or more of these circumstances: a dividend (or part of a dividend) in respect of the share is in arrear; a proposal to reduce the share capital of the body corporate; a proposal that affects rights attached to the share; a proposal to wind up the body corporate; a proposal for the disposal of the whole of the property, business and undertakings of the body corporate; the winding up of the body corporate (BOOLEAN)
  - answers: MAYBE BOOLEAN. Closed ("means"): JUST TRUE where the definition holds, JUST FALSE otherwise.
- `s 4(2) the person is regarded as one in accordance with whose directions the directors are accustomed to act`
  - takes: the directors or the majority of the directors act on advice the person gives in a professional capacity, and that is the only reason they follow the person (BOOLEAN)
  - answers: MAYBE BOOLEAN. Mixed: JUST FALSE where the text says no in its own words (an exclusion or a closing "means"), JUST TRUE where a listed limb holds, NOTHING where the list is open or the text points outside.

**sg-interpretation.l4** (imports `prelude`, `daydate`, `sg-core`). The opening words of s 4(1) and s 4(3) to (13) (the rules of reading and deeming). `s 4(2)` is in `sg-definitions.l4` beside "director"; `s 4(6)` is deleted. Contrary intention is a plain input. Outside what a subsection names the answer is `NOTHING`.

- `s 4(1) the definition in subsection (1) governs the word where it is used`
  - takes: the word is one that subsection (1) defines (BOOLEAN); a contrary intention appears in the provision where the word is used (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(3) the statement is deemed to be untrue`
  - takes: the statement is included in a statement in lieu of prospectus (BOOLEAN); the statement is misleading in the form and context in which it is included (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(4) the statement is deemed to be included in a statement in lieu of prospectus`
  - takes: the statement is contained in a report or memorandum (BOOLEAN); the report or memorandum appears on the face of the statement in lieu of prospectus (BOOLEAN); the report or memorandum is incorporated in the statement in lieu of prospectus by reference (BOOLEAN); the report or memorandum is issued with the statement in lieu of prospectus (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(5) the invitation is deemed to be an invitation to subscribe for or purchase debentures of the corporation`
  - takes: the invitation is an invitation to the public to deposit money with or lend money to a corporation (BOOLEAN); the corporation is a prescribed entity mentioned in section 239(4) of the Securities and Futures Act 2001 (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(5A) the document is deemed to be a debenture`
  - takes: the document is issued, or is intended or required to be issued, by a corporation (BOOLEAN); the document acknowledges or evidences or constitutes an acknowledgment of the indebtedness of the corporation (BOOLEAN); the indebtedness is in respect of money that is or may be deposited with or lent to the corporation in response to an invitation that subsection (5) treats as an invitation to subscribe for or purchase debentures (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(7) a reference to a person being or becoming bankrupt covers the person being or becoming insolvent`
  - takes: a contrary intention appears in the provision where the reference is used (BOOLEAN); the person is, or is becoming, bankrupt or insolvent under a written law relating to bankruptcy or insolvency (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(7) a reference to a person assigning the person's estate for the benefit of creditors or making an arrangement with them covers the same under any written law relating to bankruptcy or insolvency`
  - takes: a contrary intention appears in the provision where the reference is used (BOOLEAN); the person has made an assignment of the person's estate for the benefit of the person's creditors, or an arrangement with the person's creditors, under any written law relating to bankruptcy or insolvency (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(7) a reference to a person being an undischarged bankrupt covers the person being an undischarged bankrupt or insolvent`
  - takes: a contrary intention appears in the provision where the reference is used (BOOLEAN); the person is an undischarged bankrupt or insolvent under a written law relating to bankruptcy or insolvency (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(7) a reference to a status, condition, act, matter or thing under the law of bankruptcy covers the corresponding one under any written law relating to bankruptcy or insolvency`
  - takes: a contrary intention appears in the provision where the reference is used (BOOLEAN); the status, condition, act, matter or thing corresponds to one under or in relation to the law of bankruptcy, and arises under a written law relating to bankruptcy or insolvency (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(8) the matter is one that the subsection says the affairs of a corporation include`
  - takes: matter (s 4(8) matter); the corporation is a trustee and is not a trustee corporation (BOOLEAN); the act or thing was done at a time when a receiver, or a receiver and manager, was in possession of or had control over property of the corporation, the corporation was under judicial management, a compromise or an arrangement between the corporation and another person was being administered, or the corporation was being wound up (BOOLEAN); the corporation has issued interests (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(8) a reference to the affairs of a corporation covers the matter`
  - takes: the reference is in section 8A, 8C, 8D, 216, Part 9 or section 402 (BOOLEAN); a contrary intention appears in the provision where the reference is used (BOOLEAN); matter (s 4(8) matter); the corporation is a trustee and is not a trustee corporation (BOOLEAN); the act or thing was done at a time when a receiver, or a receiver and manager, was in possession of or had control over property of the corporation, the corporation was under judicial management, a compromise or an arrangement between the corporation and another person was being administered, or the corporation was being wound up (BOOLEAN); the corporation has issued interests (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(9) a reference to the affairs of a company or a foreign company covers the matter`
  - takes: the reference is to the affairs of a company or a foreign company (BOOLEAN); matter (s 4(8) matter); the corporation is a trustee and is not a trustee corporation (BOOLEAN); the act or thing was done at a time when a receiver, or a receiver and manager, was in possession of or had control over property of the corporation, the corporation was under judicial management, a compromise or an arrangement between the corporation and another person was being administered, or the corporation was being wound up (BOOLEAN); the corporation has issued interests (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(10) a reference to the directors of the company is a reference to its only director`
  - takes: the number of directors of the company (NUMBER)
  - answers: MAYBE BOOLEAN.
- `s 4(11) the act of the only director counts as the doing of the act by 2 or more directors`
  - takes: the number of directors of the company (NUMBER); the act has been done by the only director of the company (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(12) the reference to the Minister includes the Minister of State`
  - takes: the provision in which the reference to the Minister appears (STRING); the person is a Minister of State for the Minister's Ministry (BOOLEAN); the Minister has authorised the person to hear an appeal under that section (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(13)(a)(i) the memorandum and articles in force immediately before 3 January 2016 are deemed to be the company's constitution`
  - takes: the date asked (DATE); the memorandum of association and the articles of association of the company were in force for it immediately before 3 January 2016 (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(13)(a)(ii) the company may amend the memorandum and articles in the same manner as a constitution`
  - takes: the date asked (DATE); the memorandum of association and the articles of association of the company were in force for it immediately before 3 January 2016 (BOOLEAN)
  - answers: MAYBE BOOLEAN.
- `s 4(13)(b) a reference to the memorandum or articles of association is deemed to refer to the company's constitution`
  - takes: the date asked (DATE); the reference is in a written law, or in a contract or other document having legal effect (BOOLEAN)
  - answers: MAYBE BOOLEAN.

**sg-groups.l4** (imports `prelude`, `daydate`, `sg-core`). ss 5, 5A, 5B, 6 and s 4(1) "related corporation". A group is a LIST of direct control links `s 5(1) control link` (record `the parent`, `the subsidiary`, both `Corporation`); the list is taken as complete. Types: `s 5(2) director` (four facts), `s 5(3) who holds the shares or exercises the power` (five constructors), `s 5(3) holding` (who holds it, the votes, four flags), `s 5B kind of member`, `s 5B member`. Use the functions "by the links" when you hold the whole group; use the limb-fact functions when the person states the limbs.

- `s 5(2) the other corporation has, or is deemed to have, power to appoint the director`
  - takes: director (s 5(2) director)
  - answers: BOOLEAN. One director: has the power, or is deemed to have it by s 5(2)(a) or (b); not where the other corporation holds it only in a fiduciary capacity.
- `s 5(2) the other corporation controls the composition of the board`
  - takes: directors (LIST OF `s 5(2) director)
  - answers: MAYBE BOOLEAN. More than half of the listed directors are ones over whom the other corporation has the power (s 5(2) "all or a majority"; fork F-G1).
- `s 5(3) the votes counted as held or exercisable by the other corporation`
  - takes: holding (s 5(3) holding)
  - answers: NUMBER. One holding: the votes that count under s 5(3)(a) to (d), 0 where the holding does not count.
- `s 5(3) the total votes counted as held or exercisable by the other corporation`
  - takes: holdings (LIST OF `s 5(3) holding)
  - answers: NUMBER. The sum over a list of holdings.
- `s 5(1)(a)(ii) the other corporation controls more than half of the voting power`
  - takes: holdings (LIST OF `s 5(3) holding); the total votes of the firstmentioned corporation (NUMBER)
  - answers: MAYBE BOOLEAN. The counted votes against the corporation's total votes (supplied).
- `s 5(1) the corporation is deemed to be a subsidiary of the other corporation`
  - takes: the other corporation controls the composition of the board of the firstmentioned corporation (BOOLEAN); the other corporation controls more than half of the voting power of the firstmentioned corporation (BOOLEAN); the firstmentioned corporation is a subsidiary of a corporation which is the other corporation's subsidiary (BOOLEAN)
  - answers: MAYBE BOOLEAN. The three limbs of s 5(1) as facts: board control, more than half of the voting power, subsidiary of a subsidiary.
- `s 5(1)(b) the names of the corporations controlled through`
  - takes: links (LIST OF `s 5(1) control link); the names reached so far (LIST OF STRING); the steps still allowed (NUMBER)
  - answers: LIST OF STRING. Helper: follows the control links down a chain, bounded by `the steps still allowed` so that a cyclic list ends.
- `s 5(1) the names of the subsidiaries of`
  - takes: links (LIST OF `s 5(1) control link); parent (Corporation)
  - answers: LIST OF STRING. Helper: the names of every corporation reached down the links from one parent, with fuel equal to the number of links.
- `s 5(1) the corporation is a subsidiary of the other corporation, by the links`
  - takes: links (LIST OF `s 5(1) control link); subsidiary (Corporation); parent (Corporation)
  - answers: MAYBE BOOLEAN. Subsidiary at any depth, over a list of direct control links, taken as complete (F-G2). Argument order: links, the subsidiary, the parent.
- `s 5(4) the corporation is the holding company of the other corporation, by the links`
  - takes: links (LIST OF `s 5(1) control link); the corporation (Corporation); the other corporation (Corporation)
  - answers: MAYBE BOOLEAN. Holding company at any depth. Argument order: links, the holding company, the other corporation.
- `s 5(5) the corporation is to be regarded as a holding company`
  - takes: the corporation is the Depository (BOOLEAN); its only ground for being a holding company is shares it holds as a bare trustee (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST FALSE for the Depository whose only ground is shares held as bare trustee; NOTHING otherwise.
- `s 5A the corporation is the ultimate holding company of the other corporation, by the links`
  - takes: links (LIST OF `s 5(1) control link); the corporation (Corporation); the other corporation (Corporation)
  - answers: MAYBE BOOLEAN. Subsidiary of it at any depth, and itself the subsidiary of no link.
- `s 5A the firstmentioned corporation is the ultimate holding company of the other corporation`
  - takes: the other corporation is a subsidiary of the firstmentioned corporation (BOOLEAN); the firstmentioned corporation is itself a subsidiary of a corporation (BOOLEAN)
  - answers: MAYBE BOOLEAN. The two limbs of s 5A as facts.
- `s 5B the member of a subsidiary is the other corporation or its nominee`
  - takes: kind (s 5B kind of member)
  - answers: BOOLEAN. Helper for s 5B(c): one member of the member-subsidiary.
- `s 5B the member is within paragraphs (a) to (d)`
  - takes: member (s 5B member)
  - answers: BOOLEAN. One member of the corporation: the other corporation, its nominee, a closed subsidiary of it, or a nominee of one.
- `s 5B the corporation is a wholly owned subsidiary of the other corporation`
  - takes: members (LIST OF `s 5B member)
  - answers: MAYBE BOOLEAN. None of the listed members is outside (a) to (d); an empty list is TRUE (F-G4).
- `s 6 the corporation and the other corporation are deemed to be related, by the links`
  - takes: links (LIST OF `s 5(1) control link); the corporation (Corporation); the other corporation (Corporation)
  - answers: MAYBE BOOLEAN. Holding company, subsidiary, or two subsidiaries of one holding company, over the links.
- `s 6 the corporations are deemed to be related to each other`
  - takes: the corporation is the holding company of the other corporation (BOOLEAN); the corporation is a subsidiary of the other corporation (BOOLEAN); the corporation is a subsidiary of the holding company of the other corporation (BOOLEAN)
  - answers: MAYBE BOOLEAN. The three limbs of s 6 as facts.
- `s 4(1) "related corporation" the other corporation is a related corporation of the corporation, by the links`
  - takes: links (LIST OF `s 5(1) control link); the corporation (Corporation); the other corporation (Corporation)
  - answers: MAYBE BOOLEAN. The s 6 relation, from the point of view of the firstmentioned corporation.
- `s 4(1) "related corporation" the other corporation is a related corporation of the corporation`
  - takes: the other corporation is deemed to be related to the corporation by virtue of section 6 (BOOLEAN)
  - answers: MAYBE BOOLEAN. The same, with the s 6 answer supplied as one fact.

**sg-interests.l4** (imports `prelude`, `daydate`, `sg-core`). s 7: interests in shares. Types: `s 7(1) purpose` (`s 7(1) Division 4 of Part 4`, `s 7(1) section 163`, `s 7(1) section 164`, `s 7(1) section 165`, `s 7(1) section 244`, `s 7(1) some other provision`), `s 7 interest facts` (14 facts and a list of bodies corporate), `s 7(4) body corporate`.

- `s 7(1) the subsections other than (6A) have effect for the purposes of`
  - takes: purpose (s 7(1) purpose)
  - answers: MAYBE BOOLEAN. JUST TRUE for Division 4 of Part 4 and ss 163 to 165; NOTHING for s 244 and any other provision.
- `s 7(1) subsection (6A) has effect for the purposes of`
  - takes: purpose (s 7(1) purpose)
  - answers: MAYBE BOOLEAN. JUST TRUE for Division 4 of Part 4, ss 163 to 165 and s 244; NOTHING for any other provision.
- `s 7(1B) the restraint on the authority matters to whether the person has authority`
  - takes: the authority is, or is capable of being made, subject to restraint or restriction (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST FALSE where the authority is subject to restraint: it does not matter (s 7(1B)); NOTHING otherwise.
- `s 7(3) the thing is a unit that does not constitute an interest in a share`
  - takes: facts (s 7 interest facts)
  - answers: BOOLEAN. A collective-investment-scheme unit on an offer of units: not an interest (reads the `unit` field of the facts).
- `s 7(9) the interest is to be disregarded`
  - takes: facts (s 7 interest facts)
  - answers: BOOLEAN. Bare trustee, lender holding only as security, prescribed office, a company's own shares, a prescribed interest.
- `s 7(10) the ground is a reason to disregard the interest`
  - takes: the only ground for disregarding the interest is its remoteness, the manner in which it arose, or a restraint on exercising a right it confers (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST FALSE where the only ground is remoteness, the manner it arose, or a restraint on a right it confers.
- `s 7(5) the firstmentioned person is an associate of the other person`
  - takes: the firstmentioned person is a subsidiary of the other person (BOOLEAN); the firstmentioned person is accustomed or under an obligation, formal or informal, to act in accordance with the directions, instructions or wishes of the other person in relation to the share (BOOLEAN); the firstmentioned person is a body corporate that is, or a majority of the directors of which are, accustomed or under an obligation, formal or informal, to act in accordance with the directions, instructions or wishes of the other person in relation to the share (BOOLEAN)
  - answers: MAYBE BOOLEAN. Subsidiary, accustomed or obliged to act on the other's directions in relation to the share, or a body corporate whose directors are.
- `s 7 the direct limbs give the person an interest`
  - takes: facts (s 7 interest facts)
  - answers: BOOLEAN. Authority to dispose (1A); a trust interest the person knows of (2); a contract to purchase, a right to transfer, an option, a right to vote (6).
- `s 7 the person has an interest apart from subsection (4A)`
  - takes: facts (s 7 interest facts)
  - answers: BOOLEAN. The direct limbs and s 7(4), taking a body corporate's interest by any route; (3) and (9) taken out. Plain BOOLEAN.
- `s 7 the person has an interest`
  - takes: facts (s 7 interest facts)
  - answers: BOOLEAN. As above with s 7(4A) (20% of the voting power, alone, with associates, or together); (4A) takes the body's interest apart from (4A) (F-G7). Plain BOOLEAN.
- `s 7 the person has an interest in the shares`
  - takes: purpose (s 7(1) purpose); facts (s 7 interest facts)
  - answers: MAYBE BOOLEAN. The answer in the Act's terms: JUST TRUE or JUST FALSE where s 7(1) names the provision; NOTHING otherwise. A debenture or participatory interest (ss 164(14), 165(7)) calls `s 7 the person has an interest` with the `unit` field FALSE.
- `s 7(6A) the book-entry security is treated as an interest in a share`
  - takes: purpose (s 7(1) purpose); the thing is a book-entry security (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST TRUE for a book-entry security where (6A) applies for the provision; NOTHING otherwise.
- `s 7(7) the joint holding is a reason to find that the person has no interest`
  - takes: the person has the interest jointly with another person (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST FALSE: holding jointly is not a reason (the text says a person is not deemed not to have an interest by reason only of it); NOTHING otherwise.
- `s 7(8) that the interest cannot be related to a particular share matters`
  - takes: the interest cannot be related to a particular share (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST FALSE: it is immaterial; NOTHING otherwise.

**sg-solvency.l4** (imports `prelude`, `daydate`, `sg-core`). s 7A. The thing the directors make is the core's `Solvency statement`. Types here: `s 7A(6) penalty` (`the highest fine, in Singapore dollars`, `the longest imprisonment, in years`, `the court may impose both the fine and the imprisonment`) and `s 7A act`.

- `s 7A(1)(b) the statement gives the opinion that the intention calls for`
  - takes: statement (Solvency statement)
  - answers: BOOLEAN. Plain BOOLEAN: limb (i) or (ii) of (b), chosen by whether winding up is intended within 12 months.
- `s 7A(1) the statement has the content the section requires`
  - takes: statement (Solvency statement)
  - answers: MAYBE BOOLEAN. Content (a) to (c) for one of the three proposals; NOTHING for `some other proposal`.
- `s 7A(2) the statement is in the form the subsection requires`
  - takes: statement (Solvency statement); the company is exempt from audit requirements under section 205B or 205C (BOOLEAN)
  - answers: MAYBE BOOLEAN. Signed by every director, or (for a company not exempt from audit) accompanied by the auditor's report.
- `s 7A(1) the statement is a solvency statement`
  - takes: statement (Solvency statement); the company is exempt from audit requirements under section 205B or 205C (BOOLEAN)
  - answers: MAYBE BOOLEAN. Content and form together. Call this from s 70, s 76(9A)/(9B), ss 78B and 78C.
- `s 7A(3) the directors have formed the opinion as the subsection requires`
  - takes: the directors took into account all liabilities of the company (including contingent liabilities) (BOOLEAN)
  - answers: MAYBE BOOLEAN. All liabilities, contingent ones included, were taken into account.
- `s 7A(4)(a) the directors have had regard to what the paragraph requires`
  - takes: the directors had regard to the most recent financial statements of the company that comply with section 201(2) and (5), as the case may be (BOOLEAN); the directors had regard to all other circumstances that they know or ought to know affect, or may affect, the value of the company's assets and the value of its liabilities (including contingent liabilities) (BOOLEAN)
  - answers: MAYBE BOOLEAN. Regard to the latest s 201(2), (5) financial statements and to all other circumstances.
- `s 7A(4)(b) the directors may rely on the valuation or estimate`
  - takes: the valuation or estimate is reasonable in the circumstances (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST TRUE where reasonable; NOTHING otherwise (a grant whose limit is not met: F-S3).
- `s 7A(5) the directors may take the matter into account in valuing a contingent liability`
  - takes: the matter is the likelihood of the contingency occurring (BOOLEAN); the matter is a claim the company is entitled to make and can reasonably expect to be met to reduce or extinguish the contingent liability (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST TRUE for the likelihood of the contingency or a claim reasonably expected to be met; NOTHING for any other matter.
- `s 7A(6) the director is guilty of the offence this subsection creates`
  - takes: the person is a director of the company (BOOLEAN); the person made the solvency statement (BOOLEAN); the director had reasonable grounds for the opinions expressed in it (BOOLEAN)
  - answers: MAYBE BOOLEAN. A director who made a solvency statement without reasonable grounds (F-S1).
- `s 7A(6) the most the director may be sentenced to on conviction`
  - takes: the person is a director of the company (BOOLEAN); the person made the solvency statement (BOOLEAN); the director had reasonable grounds for the opinions expressed in it (BOOLEAN)
  - answers: MAYBE `s 7A(6) penalty. JUST (the penalty record: fine 100000, imprisonment 3 years, both allowed) for the guilty director; NOTHING otherwise.
- `s 7A(3) a director must take into account all liabilities`
  - takes: the name of the director (STRING)
  - answers: DEONTIC Party `s 7A act. Regulative: MUST, no deadline, so no breach path (NOTES.md, Rules with no breach path).
- `s 7A(4)(a) a director must have regard to the financial statements`
  - takes: the name of the director (STRING)
  - answers: DEONTIC Party `s 7A act. Regulative: MUST (i) then (ii), no deadline, so no breach path.
- `s 7A(6) a director must not make a solvency statement without reasonable grounds`
  - takes: the name of the director (STRING)
  - answers: DEONTIC Party `s 7A act. Regulative: SHANT; making the statement without reasonable grounds is BREACH.

**sg-auditors.l4** (imports `prelude`, `daydate`, `sg-core`). s 10. It takes the answer "the person is an accounting entity" as an input (`s 4(1) "accounting entity" ...` in `sg-definitions.l4` produces it; this module imports only the core). Types: `s 10(1) act`, `s 10(4) kind of accounting entity`.

- `s 10(1) the person may consent to be appointed, or act, as auditor for a company`
  - takes: the person is an accounting entity (BOOLEAN); the person acts knowingly (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST FALSE for a person who is not an accounting entity and acts knowingly; NOTHING otherwise (F-S2).
- `s 10(1) a person who is not an accounting entity must not knowingly consent to be appointed as auditor`
  - takes: the name of the person (STRING)
  - answers: DEONTIC Party `s 10(1) act. Regulative: SHANT; the act is BREACH.
- `s 10(1) a person who is not an accounting entity must not knowingly act as auditor`
  - takes: the name of the person (STRING)
  - answers: DEONTIC Party `s 10(1) act. Regulative: SHANT; the act is BREACH.
- `s 10(2) the person acts as an auditor for the company`
  - takes: the person prepares a report required by this Act to be prepared by an auditor of the company (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST TRUE where the person prepares a report this Act requires of an auditor; NOTHING otherwise ("without limiting (1)(b)").
- `s 10(3) the company or person may appoint the accounting entity as an auditor of the company`
  - takes: the prior consent of the accounting entity has been obtained (BOOLEAN)
  - answers: MAYBE BOOLEAN. JUST FALSE without the entity's prior consent; NOTHING where consent was obtained (F-S2).
- `s 10(3) no person may appoint an accounting entity as auditor without its prior consent`
  - takes: the name of the person (STRING)
  - answers: DEONTIC Party `s 10(1) act. Regulative: SHANT; appointing without consent is BREACH.
- `s 10(4) the consent has the form the subsection requires`
  - takes: kind (s 10(4) kind of accounting entity); the consent is in writing (BOOLEAN); it is signed by the public accountant (BOOLEAN); it is signed by at least one partner of the firm or limited liability partnership (BOOLEAN); it is signed by at least one director of the accounting corporation (BOOLEAN)
  - answers: MAYBE BOOLEAN. In writing and signed by the public accountant, a partner, or a director, by kind of accounting entity.
- `s 10(4) who must sign the consent`
  - takes: kind (s 10(4) kind of accounting entity)
  - answers: STRING. A STRING naming the signatory required for the kind.
- `s 10(5) the person is appointed as an auditor of the company by the appointment of the accounting firm`
  - takes: the accounting firm was appointed as auditor of the company in the name of the firm (BOOLEAN); the person was a partner of the firm at the time of the appointment (BOOLEAN); the person was a public accountant at that time (BOOLEAN)
  - answers: MAYBE BOOLEAN. A partner at the time of the appointment who was then a public accountant; a later joiner is NOTHING (F-S4).
- `s 10(6) the person is appointed as an auditor of the company by the appointment of the accounting corporation`
  - takes: the accounting corporation was appointed as auditor of the company in the name of the corporation (BOOLEAN); the person is a director of the corporation practising as a public accountant in the corporation, whether a director when the corporation was appointed or later (BOOLEAN); the person is an employee of the corporation practising as a public accountant in the corporation, whether employed when the corporation was appointed or later (BOOLEAN)
  - answers: MAYBE BOOLEAN. A director or an employee practising as a public accountant in the corporation, then or later.
- `s 10(5) and (6) the person is appointed as an auditor of the company by the appointment of the accounting limited liability partnership`
  - takes: the accounting limited liability partnership was appointed as auditor of the company in its own name (BOOLEAN); the person is a partner of the limited liability partnership (BOOLEAN)
  - answers: MAYBE BOOLEAN. Always NOTHING: neither subsection names an accounting limited liability partnership (F-S4).

**sg-seat-keel.l4** and **sg-cases-seat-keel.l4**: the keel's own seat, 37 questions (section 7). Parts do not import them.


## 3A. Core additions after wave 1 (2026-11-18): names you may use and never define

Wave 1 (the keel and parts sga1 to sgg) is encoded and gated; you cannot see its modules. Since then the keel has gained, from the NEEDS-CORE requests of wave 1:
- **`Party`** (`sg-core.l4`) has five more constructors: `Official Receiver` (no name); `Board of directors` (field `the name of the company whose board it is`, a STRING); `Foreign corporate entity` (`the name of the foreign corporate entity`); `Foreign company` (`the name of the foreign company`); `Authorised representative` (`the name of the authorised representative`). Use them; never declare a type of your own for the same body.
- **`Penalty`** (`sg-core.l4`), a record with four fields: `penalty: the highest fine, in Singapore dollars` (NUMBER), `penalty: the longest imprisonment, in months` (NUMBER), `penalty: the text allows both the fine and the imprisonment` (BOOLEAN), `penalty: the person is also liable to a default penalty` (BOOLEAN; the default penalty's amount is not encoded here). Every offence provision's penalty function returns a `Penalty` where the text states one.
- **`sg-periods.l4`** has two more functions, convention P10: `period: the last day of a period beginning with` (a day, a count, a unit: the day given is day 1) and `period: the first day of a period ending with` (a day, a count, a unit: the day given is the last day). Use them for "N days beginning with" and "N days ending with"; never write your own date arithmetic.
A role type for offence provisions is NOT in the core (proposed by a wave-1 part, not landed): if you need one, declare it under your own label and record it in `NEEDS-CORE.md`.

## 4. Seams

A part cannot import another part (separate sandboxes until the merge), so the dependent part takes the other part's answer as an INPUT fact, named for the fact and the section it comes from. A part may import the keel. Each seam below is: asking provision, answering provision, input (name and type). **Confirmed in the text** means the keel read the citing lines in the other part's range; **seen only from XREFS and headings** means the part must check it against the text.

**A. Seams where the keel asks and a part answers** (the keel's functions take these as inputs; the part's own seat asks the same fact under the same name, section 7).

| asking (keel) | answering | input, name and type | seen |
| --- | --- | --- | --- |
| s 7A(2) `sg-solvency` | s 205B, s 205C (sgc2) | `the company is exempt from audit requirements under section 205B or 205C` BOOLEAN | text (2327-2342) and XREFS |
| s 7A(4)(a)(i) `sg-solvency` | s 201(2) and (5) (sgc1) | `the directors had regard to the most recent financial statements of the company that comply with section 201(2) and (5), as the case may be` BOOLEAN | text (2357-2359) and XREFS |
| s 4(1) "audit requirements" | s 201(8), (9) (sgc1); s 207 (sgc2) | `the requirement is a requirement of section 201(8) or (9)` BOOLEAN; `the requirement is a requirement of section 207` BOOLEAN | text and XREFS |
| s 4(1) "summary financial statement" | s 203A (sgc1) | `the statement is a summary financial statement referred to in section 203A` BOOLEAN | XREFS |
| s 4(1) "limited company" | s 17(6) (later wave) | `the period of 2 years specified in section 17(6) has expired` BOOLEAN | text |
| s 4(1) "private company" | ss 18, 31, 32 (later wave) | the three facts the function takes (incorporated as private by s 18; converted under s 31; ceased to be private under s 31 or 32), BOOLEAN each | text and XREFS |
| s 4(1) "constitution" | s 19 (later wave) | `the document is the constitution of the company registered with the Registrar under section 19, as amended from time to time` BOOLEAN | XREFS |
| s 4(1) "annual general meeting", "annual return", "financial year", "statutory meeting", "statutory report", "principal register", "branch register", "electronic transaction system", "default penalty" | ss 175, 197, 198, 174, 190, 93 and 196, 12A, 408 (later waves) | one `BOOLEAN` each, named for the fact (`the return is the return required to be lodged under section 197(1)`) | XREFS |
| s 7(9)(ca) `sg-interests` | ss 76B to 76G (sga3) | `the interest is a company's interest in its own shares purchased or otherwise acquired in accordance with sections 76B to 76G (including treasury shares)` BOOLEAN | text (2266) and XREFS |
| s 7(1) `sg-interests` | ss 163, 164, 165 (sgb2); s 244 (later) | the choice `s 7(1) purpose` (constructors above) | text |
| s 4(8) `sg-interpretation` | ss 8A, 8C, 8D, 402, Part 9 (later), s 216 (sgf) | `the reference is in section 8A, 8C, 8D, 216, Part 9 or section 402` BOOLEAN | text (1859) and XREFS |
| s 4(1) "debenture", "prescribed" and the terms handed to regulations | the regulations (not a source) | `the regulations made under this Act change the terms on which a promissory note is excluded` BOOLEAN; `the matter is prescribed under this Act` BOOLEAN | text |
| s 4(5) | s 239(4) of the Securities and Futures Act 2001 | `the corporation is a prescribed entity mentioned in section 239(4) of the Securities and Futures Act 2001` BOOLEAN | text |

**B. Seams where a part asks and the keel answers** (the part imports the keel module and calls the function; no input is needed).

| asking part and provision | answering keel function | confirmed |
| --- | --- | --- |
| sga1 s 70 (redeemable preference shares out of capital) | `s 7A(1) the statement is a solvency statement` with the core's `Solvency statement`, proposal `a redemption of preference shares out of capital under section 70` | text (2291) |
| sga2 s 76(9A), (9B) (financial assistance) | the same, proposal `a giving of financial assistance under section 76(9A) or (9B)` | text (2297) |
| sga3 ss 78B, 78C (reduction of share capital) | the same, proposal `a reduction of share capital under section 78B or 78C` | text (2298) |
| sgb1 line 11757 (a company that employs the person, or one related to a corporation that employs the person); line 12994 (a transaction with a corporation related to the company) | `s 4(1) "related corporation" the other corporation is a related corporation of the corporation` (the s 6 answer as one fact) or `s 6 the corporations are deemed to be related to each other` (the three limbs) | text |
| sgb2 lines 13418, 13446, 13741, 14448 ("by virtue of section 6 is deemed to be related to the company") | the same | text |
| sgc2 line 19911 (the auditor of a company deemed related to the company) | the same | text |
| sgg line 24382 (a company deemed by s 6 to be related to the foreign company) | the same | text |
| sgb2 lines 13793, 13795 (ss 163 to 165 "interest in shares" has the meaning in s 7), 14157 (s 164(14)) and 14365 (s 165(7)): "the provisions of section 7, except subsections (1) and (3) thereof, have effect and in applying those provisions a reference to a share is a reference to a debenture or participatory interest" | `s 7 the person has an interest` (not `... in the shares`, which carries s 7(1)), called with the `unit` field of the facts FALSE (s 7(3) is excluded); for a share, `s 7 the person has an interest in the shares` with purpose `s 7(1) section 163`, `s 7(1) section 164` or `s 7(1) section 165` | text. **A part must not call the purpose version for a debenture.** |
| sga3 line 8805 (a person who would, by virtue of s 7(5), be treated as an associate) | `s 7(5) the firstmentioned person is an associate of the other person` (three facts) | text |
| sge lines 23371, 23449 (a foreign corporate entity "is deemed to be a company as defined in section 4(1)"; "ceases to be a company as defined in section 4(1)") | `s 4(1) "company" the body is a company` | text |
| sgg (foreign companies) | `s 4(1) "foreign company" the body is a foreign company` with the `s 4(1) body` record; `s 4(1) "corporation"` | XREFS only |
| any part using "director", "officer", "share", "debenture", "private company", "public company", "exempt private company", "listed", "prescribed", "Court", "Registrar" | the `s 4(1) "TERM" ...` function of the same name (section 3) | XREFS: s 4 is cited 6 times outside the keel (later wave: 3623, 9910, 25925, 25928; sge: 23371, 23449) |
| any part counting a period | the `period:` functions (section 3) | by design |
| any part asking who may be an auditor | `s 10(1) ...`, `s 10(4) ...` and the s 10(5), (6) functions of `sg-auditors` | XREFS: s 10 is cited once outside the keel, at line 5739, and that is a false hit ("sections 10 and 14 of the Residential Property Act 1976") |

**C. XREFS hits that are not seams** (checked in the text). `sgb2: 13796` cites "section 2(6) of the VCC Act", not s 2 of this Act. `later: 5739` is the heading of a section of this Act that cites "sections 10 and 14 of Residential Property Act 1976", not s 10 of this Act. The keel read under 1,000 words outside its ranges, in the lines listed above; every other seam in the table is from XREFS and headings alone and must be checked against the text by the part that owns the asking provision.

**D. A seam the keel could not close.** s 5(3)(b)(ii) counts shares held by "a subsidiary of that other corporation" as the other corporation's, while s 5(1) is the question whether a corporation is a subsidiary at all: the test is circular. The keel takes who holds the shares (`s 5(3) who holds the shares or exercises the power`) as a supplied fact (fork F-G3).


## 5. Traps on the stable binary that the keel met

**Loud** (the binary says so; the message teaches).
- `YMD`, `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` (outside `LEST BREACH ... BECAUSE`), `TYPICALLY` on a record field, sets, `EVERY` and section-level `GIVEN` are not available. A file that defines its own `YMD` fails with "multiple definitions" where daydate carries one; do not define it, write `Date day month year`.
- The keel writes one record field per line (a one-line, comma-separated list of two plain fields also checked in a probe on 1.6.110; longer lists were not tried). Positional `OF` needs commas (`r OF a, b, c`); a `LIST` written vertically is one parenthesised element per line with no commas (a leading comma gives `parse/unexpected-comma`), written inline it needs commas (`LIST (a), (b)`).
- **A continuation line that begins with `(` and sits to the left of the function it continues gives `parse/unexpected-open-paren`** (probe on 1.6.110: `q MEANS append (append xs xs)` with `(append xs xs)` on the next line at a smaller indent fails; the same call with `append` on its own line and each argument indented under it checks). The keel keeps a long `append (...) (...)` or `LIST (...), (...)` on one line.
- `JUST x's field` reads as `(JUST x)'s field` and fails with "not a function": write `JUST (x's field)`.
- There is no `length`; count with `count`, or `sum (map (GIVEN x YIELD 1) xs)`.
- A name defined in two imported modules cannot be used at all, and a file cannot import a module with its own basename (a silent `GraphException`, not a "not found").
- `DECIDE name IF` takes a `BOOLEAN`; a `MAYBE BOOLEAN` result is written `DECIDE name IS`.
- `l4 run` prints diagnostics on stderr and evaluations on stdout: a harness that reads only stdout counts nothing (it reports 0 and 0).

**Silent** (a wrong answer, exit code 0). These are the ones that cost.
- **`NOT a AND b` parses as `NOT (a AND b)`, and `NOT x OR y` as `NOT (x OR y)`.** It typechecks and answers wrongly. Write `(NOT a) AND b`, and test an input that tells the two apart (checked on 1.6.110: `NOT x OR y` answers `NOT (x OR y)` on all four input pairs).
- `l4 run` exits 0 when an `#ASSERT` fails: read the satisfied and failed counts, never the exit code. A test file whose expected values came from the code's own output proves nothing; the keel wrote each expected value from the text and mutation-tested two boundaries to see the harness fail.
- `x DIVIDED BY w` at the end of a line followed by `TIMES 100` on the next line divides by `w TIMES 100`.
- `Date 29 2 2023` rolls forward to 1 March 2023, and `add months` / `add years` clamp to the last day of a short month, both without a message. `sg-periods.l4` documents the clamping (P4); test the 31st and 29 February.
- A regulative rule `MUST ... HENCE FULFILLED LEST BREACH` with no deadline can never reach `BREACH`: a late act still reads `FULFILLED`. A `SHANT` traced with no events reads as a standing obligation (`RESIDUAL`), which is not a pass. Say so in `Rules with no breach path`.
- An `-- EXPECT` comment is checked by hand against the `#TRACE` output on both builds; `check.sh` does not compare traces (the keel did, by script, for its 12 traces: all agree).
- Two builds agreeing on counts do not agree on everything: `check.sh` target `main` sees four counts per module and no difference in a `#TRACE` result or in anything no assertion exercises.
- The `srcrefs.py --strict` gate fails an `@ref` that cites lines not in the nearest quote run above it: re-quote with a fresh run rather than citing a wider range.


## 6. One row per part

One row per wave-2 part (wave 1's rows are left out; its ranges are in `PARTS.md`). Ranges are copied unchanged from `inputs/PARTS.md`. "Keel names" are the functions and types you should expect to use; "seams" are what you take or give, with the table of section 4.

### sga1

- **Ranges:** 6135-7320, 28514-28876 (a1 share capital: issue and kinds of shares, alteration, Sixth Schedule)
- **Keel names:** The Act's own definitions of `"share"`, `"company limited by shares"`, `"company having a share capital"`, `"limited company"`, `"voting share"`, `"treasury share"`, `"constitution"`, `"private company"`, `"public company"`, `"exempt private company"`, `"prospectus"`, `"minimum subscription"`, `"debenture"`, `"prescribed"`, `"lodged"`, `"filed"`, `"registered"`; `Class of shares` and `Kind of share` from the core; the `period:` functions for any "within N days" of an allotment or alteration; s 7A for s 70 (see seam B).
- **Seams:** Takes: s 7A(1) the statement is a solvency statement (calls it for s 70, proposal `a redemption of preference shares out of capital under section 70`). Asks the later wave for ss 18, 31, 32 (private company), s 17(6) and s 19 as inputs (seams A).

### sga2

- **Ranges:** 7321-8311 (a2 financial assistance (s 76, 76A))
- **Keel names:** `s 7A(1) the statement is a solvency statement` for s 76(9A) and (9B) (proposal `a giving of financial assistance under section 76(9A) or (9B)`); the group functions for "holding company" and "subsidiary" (`s 5(1) ...`, `s 5(4) ...`); `s 6 ...` / `s 4(1) "related corporation" ...` (lines 7577 and 8293 were seen only as search hits for the word "related"; check them against the text); `"director"`, `"officer"`, `"share"`, `"public company"`, `"private company"`; the `period:` functions.
- **Seams:** Takes: the solvency-statement function; the s 5 and s 6 group functions. The related-corporation lines were seen only by their cross-reference to s 6 and must be checked against the text.

### sga3

- **Ranges:** 8312-9881 (a3 buy-back, treasury shares, reduction of capital (ss 76B-78K))
- **Keel names:** `"treasury share"`, `"share"`, `"voting share"`, `"listed"`, `"approved exchange in Singapore"`, `"constitution"`, `"book-entry securities"`; `s 7(5) the firstmentioned person is an associate of the other person` (line 8805); `s 7A(1) the statement is a solvency statement` for ss 78B and 78C (proposal `a reduction of share capital under section 78B or 78C`); the `period:` functions for notice periods and "within 14 days"; `s 7(9)(ca)` is a seam the other way (A): the part answers the fact `the interest is a company's interest in its own shares purchased ... in accordance with sections 76B to 76G`.
- **Seams:** Takes: the associate function; the solvency-statement function. Gives: the s 7(9)(ca) fact (seam A).

### sgb1

- **Ranges:** 11592-13354 (b1 directors: appointment to duties (ss 145-160D))
- **Keel names:** `"director"` (and `s 4(2) ...`), `"officer"`, `"chief executive officer"`, `"company"`, `"public company"`, `"private company"`, `"full name"`, `"identification"`, `"residential address"`, `"contact address"`; `s 4(10)` and `s 4(11)` for a company with one director (take the number of directors from the seat input `the number of directors of the company`); `s 4(1) "related corporation" ...` (lines 11757, 12994); the `period:` functions.
- **Seams:** Takes: the related-corporation function (seam B); the single-director functions. `ss 163 to 165` are sgb2's, not this part's.

### sgb2

- **Ranges:** 13355-15410 (b2 directors: approvals, loans, loss of office, secretary, indemnity (ss 161-173I))
- **Keel names:** `s 7 the person has an interest in the shares` with purpose `s 7(1) section 163`, `s 7(1) section 164` or `s 7(1) section 165` for a share, and `s 7 the person has an interest` (facts with the `unit` field FALSE) for a debenture or participatory interest under s 164(14) and s 165(7) (seam B: **not** the purpose version); `s 6` and `s 4(1) "related corporation"` (lines 13418, 13446, 13741, 14448); `"emoluments"`, `"director"`, `"officer"`, `"chief executive officer"`; `s 4(10)` and `s 4(11)`; the `period:` functions.
- **Seams:** Takes: the interest-in-shares functions (the s 7(1) purposes are `s 7(1) section 163`, `164`, `165`); the related-corporation function; the single-director functions. XREFS line 13796 is a false hit (section 2(6) of the VCC Act).

### sgc1

- **Ranges:** 17849-19068, 28897-29012 (c1 financial statements (ss 199-204, Twelfth Schedule))
- **Keel names:** `"accounts"`, `"accounting records"`, `"Accounting Standards"`, `"financial year"`, `"profit and loss account"`, `"books"`, `"summary financial statement"`, `"approved exchange in Singapore"`, `"listed"`, `"private company"`, `"public company"`; `s 5(1) ...` and `s 5(4) ...` (the group functions, for consolidated statements); `s 6 ...`; the `period:` functions.
- **Seams:** Gives: the facts `the directors had regard to the most recent financial statements of the company that comply with section 201(2) and (5), as the case may be` and the s 201(8), (9) requirement fact (seam A). Takes: the group functions.

### sgc2

- **Ranges:** 19069-20182, 29013-29310 (c2 audit and the audit exemptions (ss 205-209B, Thirteenth Schedule))
- **Keel names:** `s 10(1) ...`, `s 10(2)`, `s 10(3)`, `s 10(4)` (`s 10(4) the consent has the form the subsection requires`, `s 10(4) who must sign the consent`), `s 10(5)`, `s 10(6)` and the LLP gap function; `"accounting entity"`, `"public accountant"`, `"accounting firm"`, `"accounting corporation"`, `"accounting limited liability partnership"`, `"audit requirements"`, `"approved exchange in Singapore"`; `s 6` for the auditor of a related company (line 19911); the group functions for the group tests of the small-company exemption; the `period:` functions.
- **Seams:** Gives: `the company is exempt from audit requirements under section 205B or 205C` (the seam to s 7A(2)); the s 207 requirement fact. Takes: the s 10 functions and the related-corporation function.

### sgd

- **Ranges:** 20183-21697 (d arrangements, reconstructions, amalgamations, compulsory acquisition (ss 210-215K))
- **Keel names:** `s 5B the corporation is a wholly owned subsidiary of the other corporation` (where the part's text speaks of a wholly owned subsidiary: the keel's reading is that a corporation with no members is vacuously wholly owned and that s 5B does not itself require the corporation to be a subsidiary, fork F-G4, so a part that needs "being a subsidiary" must also ask the s 5(1) function); `s 5(1) ...`, `s 5(4) ...`, `s 5A ...`; `"Court"`, `"liquidator"`, `"commencement of winding up"`, `"company"`, `"corporation"`, `"debenture"`, `"officer"`; `s 7(5)` for "associate" in the compulsory-acquisition provisions; the `period:` functions.
- **Seams:** Takes: the group functions (including 5B) and the associate function. Winding up has moved to the Insolvency, Restructuring and Dissolution Act 2018: take its outcomes as inputs.

### sgf

- **Ranges:** 21698-21885 (f minority remedies (ss 216-216B))
- **Keel names:** `s 4(8) a reference to the affairs of a corporation covers the matter` (s 216 is one of the provisions it names; pass `the reference is in section 8A, 8C, 8D, 216, Part 9 or section 402` TRUE) and `s 4(9)` for a company or foreign company; `"company"`, `"member"` (Party `Member`), `"officer"`, `"Court"`; the `period:` functions.
- **Seams:** Takes: the affairs-of-a-corporation functions of `sg-interpretation`. The list is open ("including a reference to"): a matter off it is NOTHING, never FALSE.

### sge

- **Ranges:** 23148-23607 (e transfer of registration (Part 10A))
- **Keel names:** `s 4(1) "company" the body is a company` (lines 23371, 23449), `"foreign company"` (the `s 4(1) body` record), `"corporation"`, `"constitution"`, `s 4(13)` for the memorandum and articles deemed the constitution, `"Registrar"`, `"private company"`, `"public company"`; the `period:` functions.
- **Seams:** Takes: the s 4(1) functions named. Transfer of registration brings a foreign corporate entity within "company" by regulation: take that as the input the function asks.

### sgg

- **Ranges:** 23608-25371 (g foreign companies (Part 11))
- **Keel names:** `s 4(1) "foreign company" the body is a foreign company` and `s 4(1) "corporation" the body is a corporation` over the `s 4(1) body` record (a foreign cooperative society is excluded: fork F-C1); `s 6` / `s 4(1) "related corporation"` (line 24382: a company deemed related to the foreign company); `"director"`, `"officer"`, `"chief executive officer"` (line 25925 in the later wave modifies it for a foreign company), `"residential address"`, `"Court"`, `"Registrar"`, `"company"`; the `period:` functions.
- **Seams:** Takes: the foreign-company and corporation functions; the related-corporation function. XREFS only for the `s 4(1) body` use; check it against the text.


### sgh

- **Ranges:** 2390-2735, 2802-4174 (h administration of the Act, registers and rectification, incorporation (Part 2, ss 12-16A, Part 3 Division 1))
- **Keel names:** the `s 4(1) "TERM"` functions of the terms your ranges use ("company", "private company", "constitution", "Registrar", "Authority", "prescribed", "lodged"); the core's `Party`, including `Registrar`, `Minister` and `Authority`; the `period:` functions.
- **Seams:** Gives (table A): ss 17(6), 18, 19 (the constitution registered under s 19) and s 12A; s 4(8)'s list (ss 8A, 8C, 8D). Takes the keel's definitions; asks later parts nothing.

### sgi

- **Ranges:** 4175-6134 (i capacity and powers, constitution, names, conversion, seal (Part 3 Division 2))
- **Keel names:** `s 4(1) "constitution"`, `"private company"`, `"public company"`, `"limited company"`, `"company limited by guarantee"`; the core's `Kind of resolution` and `Liability of members`; the `period:` functions.
- **Seams:** Gives (table A): ss 31 and 32 (a private company converted, or ceased to be private). Takes: the kind of resolution from the core; what a general meeting is (sgl) as an input named for the fact.

### sgj

- **Ranges:** 9882-11038, 11493-11591 (j substantial shareholdings, debentures, title and transfers, office and name (Part 4 Divisions 4-7A, Part 5 Division 1))
- **Keel names:** `s 7 ...` of `sg-interests.l4` (whether a person has an interest in a share, the substantial-shareholding test); `s 4(1) "share"`, `"debenture"`, `"voting share"`; the core's `Party` (`Member`, `Registrar`); the `period:` functions.
- **Seams:** Gives (table A): s 93 (the principal register of debenture holders). Takes: `s 7` functions; the registered office and name rules of Part 5 Division 1 are yours.

### sgk

- **Ranges:** 11039-11492, 21886-22626 (k registration of charges, judicial management (Part 4 Division 8, Parts 8, 8A, 9))
- **Keel names:** `s 4(1) "charge"`-type terms if the keel defines them (read `inputs/KEEL-NOTES.md`); `s 4(1) "Court"`, `"Registrar"`, `"prescribed"`; the core's `Party`, including `Court`, `Registrar`, `Minister`; the `period:` functions.
- **Seams:** Gives (table A): s 4(8)'s reference to Part 9. Takes: the Insolvency, Restructuring and Dissolution Act 2018 as inputs named for the fact.

### sgl

- **Ranges:** 15411-17092 (l meetings and proceedings (Part 5 Division 3))
- **Keel names:** the core's `Kind of meeting`, `Kind of resolution`; `s 4(1) "special resolution"`-type definitions if the keel defines them; `s 4(1) "member"`, `"annual general meeting"` input; the `period:` functions (clear days of notice, the periods before a meeting).
- **Seams:** Gives (table A): ss 174 (statutory meeting, statutory report) and 175 (annual general meeting). Takes: the register of members (sgm) as an input.

### sgm

- **Ranges:** 17093-17848, 22627-23147, 28877-28896, 29311-30828 (m registers of members, annual return, Part 10, the other Schedules, Legislative History (Part 5 Divisions 4-5, Part 10, Schedules 7-11, 14-16))
- **Keel names:** `s 4(1) "member"`, `"public company"`, `"financial year"` (an input the keel asks of you); the core's `Party`; the `period:` functions.
- **Seams:** Gives (table A): ss 196 (branch register), 197 (annual return) and 198 (financial year). The Legislative History is inert.

### sgn

- **Ranges:** 25372-27069 (n Part 11A)
- **Keel names:** `s 4(1) "company"`, `"foreign company"`, `"corporation"`, `"nominee director"`-type terms if the keel defines them; the core's `Party`, including the new `Foreign company`; `s 7` (interest in shares) and `s 5` (subsidiary and holding company) where the text calls them; the `period:` functions.
- **Seams:** Takes the keel's group and interest functions. Asks later parts nothing.

### sgo

- **Ranges:** 27070-28513 (o enforcement, offences, miscellaneous, First to Fifth Schedules (Part 12))
- **Keel names:** `s 4(1) "Court"`, `"Registrar"`, `"prescribed"`, `"company"`; the core's `Party`, `Penalty` and the offence-related shapes in `sg-core.l4`; the `period:` functions.
- **Seams:** Gives (table A): s 402 (the reference list of s 4(8)) and s 408 (default penalty). Takes: other parts' offences are theirs; your penalty provisions are called by them as inputs.

## 7. The seat layer

**The seat.** An individual who is, or is about to become, a director, the company secretary or a member (shareholder) of a company incorporated under the Act, or of a foreign company registered under it, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership. There is never a seat for the Registrar, the Minister, the Authority or the Court.)

**The question-name form.** Every question is named `Under section N, ...` (the provision first, then the question in the person's words, in the direction the body answers): `Under section 5(1), is the corporation a subsidiary of the other corporation`, `Under section 7A(6), am I guilty of the offence of making a solvency statement without reasonable grounds`. The name asks what the body answers: `JUST TRUE` is yes, `JUST FALSE` is the text's no, `NOTHING` is "the text does not say". Each question has `@export <the name>?` and, on every input, `@desc` worded as the person would be asked. Plain inputs only (yes/no, numbers, strings, dates, and the modules' own choices); the records and lists a module wants are built inside the question from those answers, and the module's function is called: a seat never restates a rule.

**Input names every seat shares** (exact name, type, `@desc`). The keel's seat uses the first, the eighth and the ninth; the others are reserved so that two parts that ask the same fact use one name.

| name | type | `@desc` |
| --- | --- | --- |
| `I am a director of the company` | BOOLEAN | Are you a director of the company? |
| `I am the secretary of the company` | BOOLEAN | Are you the secretary of the company? |
| `I am a member of the company` | BOOLEAN | Are you a member (shareholder) of the company? |
| `the company is a private company` | BOOLEAN | Is the company a private company, as section 4(1) of the Companies Act uses the word? |
| `the company is a public company` | BOOLEAN | Is the company a public company, as section 4(1) of the Companies Act uses the word? |
| `the liability of the company's members` | `Liability of members` | Is the liability of the company's members limited by shares, limited by guarantee, limited by both, or unlimited? |
| `the company is a foreign company registered under Part 11` | BOOLEAN | Is the company a foreign company registered under Part 11 of the Companies Act? |
| `the number of directors of the company` | NUMBER | How many directors does the company have? |
| `the company is exempt from audit requirements under section 205B or 205C` | BOOLEAN | Is the company exempt from audit requirements under section 205B or 205C? |
| `the other corporation is deemed to be related to the corporation by virtue of section 6` | BOOLEAN | Is the other corporation one that section 6 deems related to the corporation? |
| `the directors have made a solvency statement that complies with section 7A` | BOOLEAN | Have the directors made a solvency statement for this proposal that complies with section 7A? |
| `the date asked` | DATE | On what date are you asking? |

The keel's modules take the same names: `sg-interpretation.l4` takes `the date asked` (s 4(13)); `sg-solvency.l4` and the seat take `the number of directors of the company` and `the company is exempt from audit requirements under section 205B or 205C`; the seat's s 7A(6) questions take `I am a director of the company`. A seat that wants a fact not in this table names it for the fact and keeps the same `@desc` wherever it asks it.

**The keel's seat** (`sg-seat-keel.l4`, `sg-cases-seat-keel.l4`): 37 questions for ss 5, 5A, 5B, 6, 7, 7A and 10, 175 cases (a yes case, the text's no case where there is one, a not-covered case where there is one). Chains of control through several corporations take a list of links, which is not a plain input; the seat asks the same questions through their limb facts, and says so in its header.


## 8. The NOTES sections every part must write, and the split sites

**Sections of the part's `NOTES.md`** (the part's id in the heading, as the keel's end in `(keel)`):
1. `## Coverage (<id>)`: one row per section, subsection, paragraph, defined term and table row of the part's own ranges, exactly one disposition each (`encoded`, `inert` for reasons 1 to 3 only, `fork`, `repealed or blank in this text`) and the L4 name; check by script that every non-blank line of the ranges falls in some row.
2. `## Fork register (<id>)`: one line per site where the text can be read two ways with different outcomes: the provision, the function, the answer taken, the other reading, the text that licenses each.
3. `## Jural relations (<id>)`: one row per provision creating a right, privilege, power or immunity, with the correlative; `none` for a definition.
4. `## Marginal readings for a lawyer (<id>)`: every branch resting on the status-quo readings (a) a failed "if" counts as the text's no; (b) a prohibition or grant limited by its own wording does not; with the other reading.
5. `### Reading a result: FALSE and NOTHING (<id>)`, in the part's subject's terms.
6. `## Split sites (<id>)`: the count of sites of types (i) and (ii) below, each with the answer taken, pointing at its fork line, and quoting the Guide.
7. `## Rules with no breach path (<id>)`: every regulative `MUST` with no time limit and no stated consequence (no trace can show it breached).
8. Numbered findings ("What the text turns out to say"); `What the stable binary does not accept`; what `check.sh` prints; and a statement that the text is a rendering of the Act and not the official text. Also `NEEDS-CORE.md` where the core lacks a type or constructor.

**Every regulative rule needs a trace that reaches `BREACH`**, with a `-- EXPECT <word>` comment (`FULFILLED`, `BREACH` or `RESIDUAL`) above each `#TRACE`; compare each trace on both builds. A penalty provision is a function over the facts returning the maximum fine, the maximum term and whether the offence applies, with the amounts copied from the text.

**The two split sites, recorded site by site; do not harmonise** (a part cannot see the others). (i) **An unmet element of an offence or a contravention**: `JUST FALSE` or `NOTHING`? (ii) **A "may" gated by "where", "when", "upon", "on application", "with the consent of"**: `JUST FALSE` (the periods ruling's rule (b)) or `NOTHING` (the grant ruling)? Each split site gets one fork line (the provision, the function, the answer taken, the other reading) that names the line of `inputs/ENCODING-GUIDE.md` section 5, or the dated ruling in it, that the answer relies on, quoting the Guide's own words: line 93 (the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"), line 87 and lines 96 to 99 (the grant rule: `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit"), line 92 (N2: flat negatives count as a no). A site that fits none of those lines says so and is listed under `## Marginal readings for a lawyer`. **What the keel took** is in `NOTES.md`, `## Split sites (keel)`, for information only: do not change an answer to match it.
