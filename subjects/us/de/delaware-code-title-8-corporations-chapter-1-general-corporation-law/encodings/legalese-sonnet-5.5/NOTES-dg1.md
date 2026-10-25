# NOTES -- dg1: the title lines and Subchapter I of the Delaware General Corporation Law (8 Del. C. §§ 101-116)

This folder encodes lines 1-239 of `de-code-t8-ch1-2026-10-01.txt` (the title lines, the chapter heading, Subchapter I and its sections 101 to 116, with their History lines).
The text is a plain-text rendering of the Delaware Code Online (version: through 85 Del. Laws, c. 550, as `../../registers/source-bundle/*.meta.json` records), made by a converter script.
It is not the official text, and nothing here is verified against the official text.
Every quotation in the `.l4` files is a mechanical slice of that file, checked by `srcrefs.py`, which checks that the quotation is in the file and not that the file is the statute.

The target is the stable `l4` 1.6.98 in the `main` dialect.
Layer 1 is the ten `dg1-s*.l4` modules (the law, objectively, in the text's own order), with ten `dg1-tests-*.l4` files beside them.
Layer 2 is `dg1-seat.l4` (the seat's questions) and `dg1-cases-seat.l4` (worked cases).

Dates.
The range holds no date of enactment and no commencement rule.
The application notes after the headings of sections 110 and 111 point to session-law clauses (82 Del. Laws, c. 256, § 23 and 80 Del. Laws, c. 265, § 17) that are not in the text; they are `inert` in the coverage table.
Two dates that the operative text itself states are carried as defined values with an `@ref`: 3 July 1967 (`s 102(b)(3) the date on which existing preemptive rights are preserved`) and 1 August 2011 (`s 103(j) the date before which a filed document need not be amended to comply with § 131(c)`).

The helper scripts these notes name (`inputs/work/dupnames.py`, `pairs.py`, `mutation/` and the others) are this piece's working tools; they sit beside the inputs, not in this folder, and `PROGRESS.md` gives their path.
`check.sh` is the lead's file with one line added, in `expected_failed`, for the one assertion in this piece that is meant to fail (F32).

## Seat

The seat is a person who incorporates, directs or holds stock in a Delaware corporation under the General Corporation Law: an incorporator, a director or officer, or a stockholder, including a minority stockholder.
It was given by the brief (the individual to whom the Law is applied), and `dg1-seat.l4` asks the Law's questions as that person would: "Do I have the power to adopt, amend or repeal the bylaws?", "Am I, as a stockholder, personally liable for the corporation's debts?", "Is the notice I was given of the organization meeting enough?", "Have I done everything that filing requires of me?".
Where an answer depends on whether the corporation is a stock or a nonstock corporation (the power over the bylaws, the right to apply for a meeting, the name requirement), the question takes the kind of corporation as an input, so a member of a nonstock corporation is served by the same question as a stockholder (section 114(a) reads "stockholder" as "member").

There is no seat for the Secretary of State, the Division of Corporations or the Court of Chancery.
What the Law makes them do is put to the seat as what it is owed ("Must the Secretary of State reserve the name for me?", "Must the Secretary of State certify my instrument as filed?") and what may be done to it ("May the Secretary of State hold my instrument in suspension?").
A judgment the Law hands to an official (a waiver, a finding that a name is available, the court's sanction, whether an extraordinary condition existed) is an input that the person states as a fact, never computed.

The layer has 147 questions, each with `@export` and `@desc`, grouped under `§` headings in the text's order: forming the corporation (101 to 107); what the certificate must set forth (102(a)); what it may also contain (102(b), (c), (d), (f)); reserving a name (102(e)); signing, acknowledging and filing (103); a failed filing attempt in an extraordinary condition (103(i)); the organization meeting (108); bylaws (109); emergency bylaws and powers (110); the Court of Chancery (111); proxy access and reimbursement (112, 113); nonstock corporations (114); forum selection (115); documents, signatures and delivery (116).
`dg1-cases-seat.l4` has at least one worked case for each of the 147 questions, in the facts a person in the seat would state, and an asserted `NOTHING` wherever the text does not decide.
A question whose answer the text leaves open returns a `MAYBE`: `NOTHING` means "the Law does not say" and is never turned into yes or no.

Questions that arise only in particular circumstances (name reservation, a failed filing, emergency powers, nonstock corporations) say so in their group heading.

## Jural relations

Layer 1 states each relation once, as a relation between two parties, and names the rule neutrally (`s 109(a) the holder has the power to adopt, amend or repeal bylaws`, never "my power"); the correlative is recorded here and in the seat's paired questions, not in a second rule.
The correlatives used are Hohfeld's: claim and duty; privilege and no-right; power and liability (being subject to the power, not an obligation); immunity and disability.
The Secretary of State, the Division of Corporations and the Court of Chancery are officials with no seat of their own: where one holds the power or bears the duty, the seat layer asks what it means for the person (what is owed to them, what may be done to them).
A row marked `none` is a provision that creates no relation (a definition, a counting rule, a list); each such provision is listed once.

| section | holds the right, privilege, power or immunity | bears the duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| title, chapter and subchapter headings, History lines, application notes | none | none | none | none (not provisions) |
| s 101(a) | the person, partnership, association or corporation that signs the certificate of incorporation | the State of Delaware (liable to have a corporation come into being on filing) | power / liability | `s 101(a) the entity may incorporate or organize a corporation under this chapter`; `s 101(a) the corporation has been incorporated by filing the certificate of incorporation` |
| s 101(b) | the corporation (any lawful business or purposes) | the State and any person who would object (no-right), except as the Constitution or other law of this State provides | privilege / no-right | `s 101(b) a corporation may be incorporated to conduct or promote the business or purposes` |
| s 101(c) | a public-utility corporation (may be organized under this chapter, in or outside this State) | the State, whose Title 26 regime reaches a utility operating in this State (liability to it) | privilege / no-right, and power / liability | `s 101(c) a corporation for operating public utilities, in or outside this State, may be organized under this chapter`; `s 101(c) the corporation is subject also to the special provisions and requirements of Title 26` |
| s 102(a)(1)-(3), (5), (6) | the State, to a certificate that sets out the name, registered office and agent, purposes, incorporators and (when the incorporators' powers end on filing) first directors | the incorporators who file it | claim / duty | `s 102(a)(1) the name of the corporation complies`; `s 102(a)(2) the certificate sets forth the registered office and registered agent`; `s 102(a)(3) the certificate sets forth the nature of the business or purposes`; `s 102(a)(5) the certificate sets forth the incorporators`; `s 102(a)(6) the certificate sets forth the first directors`; `s 102(a) the certificate of incorporation sets forth everything that subsection (a) requires` |
| s 102(a)(1)(i), (ii), (iv) waivers and consent | the Division of Corporations (to waive the name requirements on the grounds the text lists); the person who reserved a name, or the other entity (to consent to a similar name) | the corporation seeking the name (liable to have its duty waived or enlarged by their act) | power / liability | `s 102(a)(1)(i) the words one of which the name must contain`; `s 102(a)(1)(i) the name satisfies the requirement as to words`; `s 102(a)(1)(ii) the name satisfies the requirement as to distinction on the records`; `s 102(a)(1)(iv) the name satisfies the requirement as to the word bank` |
| s 102(a)(1)(iii) | the State (to a name without the word "trust" unless section 395 permits) | the incorporators | claim / duty | `s 102(a)(1)(iii) the name satisfies the requirement as to the word trust` |
| s 102(a)(3) (all lawful acts within the purposes) | the corporation (to do any lawful act within a general purposes statement) | anyone who would say the act is outside the corporation's purposes (no-right), except for express limitations | privilege / no-right | `s 102(a)(3) the act or activity is within the purposes of the corporation` |
| s 102(a)(4) (stock) | the State, to a certificate that states the authorized stock | the incorporators | claim / duty | `s 102(a)(4) the certificate sets forth the authorized stock` |
| s 102(a)(4) (nonstock) | the nonstock corporation (to provide classes of members and voting rights) | its members (no-right to equal voting) | privilege / no-right | `s 102(a)(4) the nonstock corporation may make the provision for its members` |
| s 102(a)(4) (nonstock, acts and existence) | the nonstock corporation (its acts stay valid and it is neither forfeited nor dissolved for want of members) | anyone who would attack an act or the corporation's existence on that ground (disability) | immunity / disability | `s 102(a)(4) the corporate act remains valid although the nonstock corporation has no members`; `s 102(a)(4) the nonstock corporation has forfeited its existence or is dissolved because it has no members` |
| s 102(a)(4) (nonstock, who are members) | none: a definition of membership | none | none | `s 102(a)(4) the person is a member of the nonstock corporation`; `s 102(a)(4) the certificate and the bylaws set forth what a nonstock corporation must state`; `s 102(a)(4) the certificate and the bylaws set forth what paragraph (a)(4) requires` |
| s 102(b) chapeau, (b)(1) | the incorporators and stockholders (to put the listed matters in the certificate) | the State (no-right to refuse them) | privilege / no-right | `s 102(b) the certificate of incorporation is required to contain the matter listed in subsection (b)`; `s 102(b)(1) the certificate of incorporation may contain the provision`; `s 102(b)(1) a provision that this chapter requires or permits to be stated in the bylaws may instead be stated in the certificate of incorporation` |
| s 102(b)(2) (application) | the corporation, a creditor or stockholder (member), a receiver under section 291, trustees in dissolution or a receiver under section 279 (to apply for a meeting) | the court (liable to be moved to order a meeting) | power / liability | `s 102(b)(2) the applicant may apply for a meeting to be summoned` |
| s 102(b)(2) (binding vote) | a majority in number representing three fourths in value of the creditors or class, or of the stockholders (members) or class, with the court's sanction (to bind all) | all the creditors or class, the stockholders (members) or class, and the corporation | power / liability | `s 102(b)(2) the compromise or arrangement and the reorganization are binding on all`; `s 102(b)(2) the certificate of incorporation contains the compromise or arrangement provision in haec verba` |
| s 102(b)(3) | the stockholder (to subscribe to new stock, if the certificate expressly grants it or the right was in existence on 3 July 1967) | the corporation (to offer it) | claim / duty | `s 102(b)(3) the stockholder has a preemptive right to subscribe to an additional issue of stock or to a convertible security`; `s 102(b)(3) the certificate of incorporation may contain the provision granting a preemptive right`; `s 102(b)(3) the date on which existing preemptive rights are preserved` |
| s 102(b)(4) | the corporation (to require, by its certificate, a larger vote or a larger number of directors than the Law does) | the stockholders and directors (no-right to act on the Law's lower figure) | privilege / no-right | `s 102(b)(4) the certificate of incorporation requires a larger portion of the stock or other securities having voting power than this chapter requires`; `s 102(b)(4) the certificate of incorporation requires a larger number of the directors than this chapter requires` |
| s 102(b)(5) | none: when the duration of the corporation's existence expires | none | none | `s 102(b)(5) the duration of the corporation's existence has expired`; `s 102(b)(5) the corporation has perpetual existence` |
| s 102(b)(6) | the stockholder (not personally liable for the corporation's debts, unless a provision or the stockholder's own conduct makes them so) | the corporation's creditors (disability to reach the stockholder's own assets) | immunity / disability | `s 102(b)(6) the stockholder is personally liable for the payment of the corporation's debts` |
| s 102(b)(7) | the director or officer (not liable for monetary damages for breach of fiduciary duty, if the certificate so provides, save the five excepted liabilities and acts before the provision took effect) | the corporation and its stockholders (disability to recover) | immunity / disability | `s 102(b)(7) the provision may eliminate or limit the person's personal liability`; `s 102(b)(7) the provision as it stood continues to apply to the act or omission despite the later amendment, repeal or elimination` |
| s 102(c) | none: it need not set out the powers the title confers | none | none | `s 102(c) the certificate of incorporation must set forth the power` |
| s 102(d) | none: which provisions may depend on facts outside the certificate | none | none | `s 102(d) the provision may be made dependent on facts ascertainable outside the certificate`; `s 102(d) the matter is a fact on which a provision may depend` |
| s 102(e) (reservation) | the applicant (to the exclusive use of an available name for 120 days) | the Secretary of State (to reserve it) | claim / duty | `s 102(e) the exclusive right to use the name may be reserved by or on behalf of the person`; `s 102(e) the Secretary of State must reserve the name for the applicant for a period of 120 days`; `s 102(e) the last day of the reservation` |
| s 102(e) (renewal, transfer, cancellation) | the applicant or transferee (to renew, transfer or cancel by filing) | the Secretary of State (liable to record it) | power / liability | `s 102(e) the application for renewal renews the reservation`; `s 102(e) the right to the exclusive use of the reserved name has been transferred`; `s 102(e) the reservation has been cancelled`; `s 102(e) the application to reserve a name is in the form required` |
| s 102(e) (copy, fee) | the filer (to a copy with a notation); the State (to the fee) | the Secretary of State (to return it); the filer (to pay) | claim / duty | `s 102(e) the Secretary of State must return a copy of the filed instrument with a notation of the action taken`; `s 102(e) the fee payable at the time of the filing` |
| s 102(f) | the stockholder (not liable under the certificate for the fees or expenses of an internal corporate claim, or of a claim the stockholder brought) | the corporation (disability to impose it by the certificate) | immunity / disability | `s 102(f) the certificate of incorporation may contain the provision` |
| s 103(a), (h) | the persons who sign an instrument (to execute it for filing, by manual, facsimile or electronically transmitted signature) | the Secretary of State (no-right to insist on another form); the corporation (bound by the instrument) | power / liability, privilege / no-right | `s 103(a)(1) the instrument is one that the incorporators sign`; `s 103(a)(1) the instrument is signed as required of the incorporators`; `s 103(a)(2) the instrument is signed as required for the corporation`; `s 103(a) the instrument is executed as required`; `s 103(h) the form of signature is permitted on an instrument authorized to be filed` |
| s 103(b) | the State (to a truthful affirmation) | the signatory (by signature alone, affirms under penalties of perjury) | claim / duty, power / liability | `s 103(b)(1) the formal acknowledgment has been made`; `s 103(b)(2) the signature alone is the acknowledgment`; `s 103(b) the requirement that the instrument be acknowledged is satisfied`; `s 103(b)(2) the signatory affirms under penalties of perjury that the facts stated are true`; `s 103(b)(2) the date as of which the facts stated by a signatory relying on the signature alone must be true` |
| s 103(c)(1)-(3) | the filer (to have the instrument certified as filed on delivery and tender) | the Secretary of State (to certify it) | claim / duty | `s 103(c)(1) and (2) the filer has done what filing requires of the filer`; `s 103(c)(3) the Secretary of State must certify the instrument as filed`; `s 103(c) the instrument has been filed`; `s 103(c)(3) the filing date of the instrument` |
| s 103(c)(4) | the Secretary of State (to hold an instrument in suspension for an error, omission or imperfection) | the filer (liable to have it held; may replace it within 5 business days); the corporation (no-right to a certificate of good standing meanwhile) | power / liability, privilege / no-right | `s 103(c)(4) the Secretary of State may hold the instrument in suspension`; `s 103(c)(4) the Secretary of State is barred from issuing a certificate of good standing` |
| s 103(c)(5)-(7) | the Secretary of State, the counties and the courthouse municipality (to the charges and fees) | the filer (to tender them) | claim / duty | `s 103(c)(5) the administrative charge the Secretary of State retains and pays to the General Fund`; `s 103(c)(6) the county assessment fee`; `s 103(c)(6) the county whose recorder's office receives the assessment fee`; `s 103(c)(7) the courthouse municipality fee`; `s 103(c)(7) the municipality that receives the courthouse municipality fee` |
| s 103(c)(8) | the Secretary of State (to grant the registered agent direct access); the registered agent (to use it on the stated condition) | the registered agent (liable to the grant); the Secretary of State (no-right to demand more) | power / liability, privilege / no-right | `s 103(c)(8) the instrument and its information must be permanently maintained as a public record`; `s 103(c)(8) the Secretary of State may grant the registered agent direct access to the system`; `s 103(c)(8) the registered agent granted direct access has complied with the condition on that access` |
| s 103(d) | the filer (to postpone the effect of an instrument by up to 90 days, and to terminate or amend a future-dated instrument before its date) | those affected by the instrument (liable to its effect from the date stated) | power / liability | `s 103(d) the instrument may become effective on the specified later date`; `s 103(d) the date on which the instrument is effective`; `s 103(d) the future effective instrument has been terminated or amended by a certificate in due form and time` |
| s 103(e) | none: another section that prescribes a manner or a time governs | none | none | `s 103(e) the other section governs` |
| s 103(f) | the filer (to correct or nullify a filed instrument by a certificate of correction); persons substantially and adversely affected (not bound before the correction's filing date) | persons affected (liable to the correction); the filer (disability to bind them earlier) | power / liability, immunity / disability | `s 103(f) the instrument may be corrected or nullified by a certificate of correction`; `s 103(f) the certificate of correction is in the form required`; `s 103(f) the corrected instrument is in the form required`; `s 103(f) the date from which the corrected or nullified instrument is effective as to the person` |
| s 103(g) | the Secretary of State (not liable for filing, indexing, delivering, certifying or failing to certify an instrument) | any person (disability to hold the Secretary of State liable for those acts) | immunity / disability | `s 103(g) the Secretary of State is liable to any person for the act` |
| s 103(i) | the Secretary of State (to establish an earlier filing date after an extraordinary condition); persons substantially and adversely affected (effective against them only from the date endorsed on the affidavit or waiver) | the filer; the Secretary of State and the filer (disability to bind those persons earlier) | power / liability, immunity / disability | `s 103(i)(1) the Secretary of State may establish the earlier date and time as the filing date`; `s 103(i)(1) the fee payable to the Secretary of State for receiving an affidavit of extraordinary condition`; `s 103(i)(2) there is an extraordinary condition`; `s 103(i)(2) the determination of the Secretary of State is conclusive`; `s 103(i)(3) the date from which the instrument is effective as to the person` |
| s 103(j) | the corporation with a document filed before 1 August 2011 (not required to amend it to comply with section 131(c)) | the State (disability to require it) | immunity / disability | `s 103(j) the date before which a filed document need not be amended to comply with § 131(c)`; `s 103(j) the corporation need not amend the document to comply with § 131(c)`; `s 103(j) the document must comply with § 131(c)` |
| s 104 | none: what counts as part of the certificate of incorporation | none | none | `s 104 the instrument is part of the certificate of incorporation` |
| s 105 | the party who offers a certified copy (to have it received as prima facie evidence) | courts, public offices and official bodies (to receive it) | claim / duty | `s 105 the certified copy is received as prima facie evidence of the matter` |
| s 106 | none: when and by what name the body corporate exists; the power to incorporate is section 101(a) | none | none | `s 106 the date from which the incorporators are a body corporate`; `s 106 the name by which the body corporate exists`; `s 106 the body corporate exists on the day` |
| s 107 | the incorporators (to manage the corporation's affairs until directors are elected, and to do what is necessary and proper) | the corporation (bound by what they do) | power / liability | `s 107 the incorporators manage the affairs of the corporation`; `s 107 the incorporators may do the act` |
| s 108(a) | a majority of the incorporators or directors (to call the organization meeting) | the other incorporators or directors (liable to be called) | power / liability | `s 108(a) the organization meeting is a meeting of the board of directors and not of the incorporators`; `s 108(a) the call of the organization meeting is made by a majority of the incorporators or directors`; `s 108(a) the organization meeting may be held at the place`; `s 108(a) the purpose may be pursued at the organization meeting` |
| s 108(b) | each other incorporator or director (to at least 2 days' notice; to waive it) | the persons calling the meeting (to give it) | claim / duty, power / liability | `s 108(b) the notice of the organization meeting is sufficient`; `s 108(b) notice of the meeting need not be given to the person` |
| s 108(c), (d) | each incorporator or director (to consent without a meeting; to consent at a future time; to revoke before it takes effect); the person for whom an unavailable incorporator acted (to take that incorporator's action) | the other incorporators or directors and the corporation (liable to the consent or action) | power / liability | `s 108(c) the action may be taken without a meeting`; `s 108(c) the consent given for a future time is deemed given at that time`; `s 108(c) the consent may still be revoked`; `s 108(d) the person may take the action that the incorporator would have been authorized to take under this section or § 107` |
| s 109(a) | the incorporators, the initial directors, the board (before any payment for stock), the stockholders or members entitled to vote, and directors on whom the certificate confers it (to adopt, amend or repeal bylaws) | the corporation and the other holders (liable to the bylaws); the directors (disability to divest the stockholders' or members' power by being given theirs) | power / liability, immunity / disability | `s 109(a) the holder has the power to adopt, amend or repeal bylaws`; `s 109(a) the conferral of the power on the directors or governing body divests the stockholders or members of the power` |
| s 109(b) | the corporation (to put in its bylaws any provision not inconsistent with law or the certificate); the stockholder (not liable under the bylaws for the fees or expenses of an internal corporate claim, or of a claim the stockholder brought) | stockholders (no-right to a bylaw-free corporation); the corporation (disability to impose that liability) | privilege / no-right, immunity / disability | `s 109(b) the bylaws may contain the provision`; `s 109(b) the bylaws may contain the provision on fees and expenses` |
| s 110(a) | the board (to adopt emergency bylaws, operative in an emergency); the stockholders (to repeal or change them) | the corporation and its people (liable to the emergency bylaws) | power / liability | `s 110(a) the emergency bylaws are operative`; `s 110(a) the emergency bylaws were validly adopted`; `s 110(a) the emergency bylaws are subject to repeal or change by action of the stockholders`; `s 110(a) the emergency bylaws may make the provision`; `s 110(a)(1) the person may call a meeting of the board of directors or a committee`; `s 110(a)(2) the directors in attendance constitute a quorum`; `s 110(a)(3) the person is deemed a director for the meeting` |
| s 110(b), (c), (e) | the board (to provide lines of succession and to change the head office, before or during the emergency) | the officers and the corporation (liable to the board's act) | power / liability | `s 110(b) the board of directors may provide, and from time to time modify, lines of succession`; `s 110(c) the board of directors may, effective in the emergency, change the head office or designate alternative head offices or regional offices, or authorize the officers to do so`; `s 110(e) the bylaw of the corporation remains in effect during the emergency` |
| s 110(d) | the officer, director or employee who acts under the emergency bylaws (not liable except for wilful misconduct) | those who would claim against them (disability) | immunity / disability | `s 110(d) the person is protected from liability` |
| s 110(f), (g) | the persons present or reached (notice only to those it is feasible to reach); the officer present (deemed a director to the extent a quorum requires) | directors not reached (no-right to further notice); the corporation | privilege / no-right, power / liability | `s 110(f) the notice of the meeting of the board of directors is sufficient`; `s 110(g) the officer present is deemed a director for the meeting` |
| s 110(h) | none: other provisions for emergency powers are not displaced | none | none | `s 110(h) the provision for emergency powers is permitted in addition to this section` |
| s 110(i) | the board (to postpone or alter a stockholders' meeting and to move a declared dividend's dates in an emergency condition); the corporation (to notify by SEC filing alone); any person (not liable for an impracticable stocklist) | the stockholders (liable to the board's act); anyone who would claim for the failure (disability) | power / liability, immunity / disability | `s 110(i) the action with respect to the meeting of stockholders is authorized`; `s 110(i)(i)(1) the record date that applies to the postponed meeting`; `s 110(i)(i)(2) the corporation may give the notice solely by a document publicly filed with the Securities and Exchange Commission`; `s 110(i)(ii) the board of directors may change the record date and the payment date of the declared dividend as it has`; `s 110(i) the corporation has given notice of the change in time`; `s 110(i) the failure to make a stocklist available is excused` |
| s 111(a), (b) | any party to a civil action on the listed subjects, or on a provision of the title (to bring it in the Court of Chancery) | the defendant (liable to suit there); a court, agency or tribunal with exclusive jurisdiction (subsection (a) only) | power / liability | `s 111(a) the civil action may be brought in the Court of Chancery`; `s 111(b) the civil action may be brought in the Court of Chancery` |
| s 112 | the stockholder (to have a nominee included in the proxy solicitation materials, if the bylaws so provide) | the corporation (to include it) | claim / duty | `s 112 the corporation may be required to include the stockholder's nominee in its proxy solicitation materials`; `s 112 the bylaws may impose the condition` |
| s 113 | the stockholder (to reimbursement of proxy-solicitation expenses, if the bylaws so provide) | the corporation (to reimburse) | claim / duty | `s 113(a) the corporation may be required to reimburse the stockholder's expenses`; `s 113(a) the bylaws may prescribe the condition`; `s 113(b) the bylaw applies to the election` |
| s 114(a)-(c) | none: how the Law's references to stockholders, board and stock are read for a nonstock corporation, and where they are not | none | none | `s 114(a) how the reference in the provision is read`; `s 114(b)(1) the provisions that apply to nonstock corporations by their terms`; `s 114(b)(2) the other provisions to which subsection (a) does not apply`; `s 114(b)(3) the subchapters to which subsection (a) does not apply`; `s 114(c)(2) the further provisions to which subsection (a) does not apply for a nonprofit nonstock corporation`; `s 114(c)(3) the subchapters to which subsection (a) does not apply for a nonprofit nonstock corporation`; `s 114(b) and (c) subsection (a) does not apply to the provision` (with the helpers `s 114 the whole of section`, `s 114 the part`, `s 114 the listed provision names the asked provision`, `s 114 the list names the provision`, `s 114 the list of subchapters reaches the provision`) |
| s 114(d) | none: definitions of nonstock, membership interest, nonprofit nonstock and charitable nonstock corporations | none | none | `s 114(d)(4) the corporation is a nonstock corporation`; `s 114(d)(2) the interest of the member is a membership interest`; `s 114(d)(3) the corporation is a nonprofit nonstock corporation`; `s 114(d)(1) the corporation is a charitable nonstock corporation`; `s 114(d) the kind of the corporation` |
| s 115(a) | the corporation (to require, by certificate or bylaws, that internal corporate claims be brought only in this State's courts); the stockholder (no provision may prohibit bringing them in this State's courts) | the stockholders (liable to the requirement); the corporation (disability to prohibit) | power / liability, immunity / disability | `s 115(a) the provision of the certificate of incorporation or the bylaws is permitted` |
| s 115(b) | none: defines internal corporate claims | none | none | `s 115(b) the claim is an internal corporate claim`; `s 115(b)(ii) this title confers jurisdiction upon the Court of Chancery as to the claim` |
| s 115(c) | the corporation (to prescribe forums for other claims); the stockholder (to at least one court in this State with jurisdiction) | the stockholders (liable to the requirement); the corporation (duty to allow one such court) | power / liability, claim / duty | `s 115(c) the certificate or the bylaws may require the stockholder to bring the claim only in the prescribed forums` |
| s 116(a)(1), (b) | none: what a document is, and which documents the section does not reach | none | none | `s 116(a)(1) the medium is a document`; `s 116(a)(1) the medium is deemed the equivalent of a written document`; `s 116(b) subsection (a) applies to the document`; `s 116(b) a presumption arises from the exclusions about the lawful means to document, sign or deliver` |
| s 116(a)(2) | the person who signs (to use a manual, facsimile, conformed or electronic signature) | anyone who would insist on another form (no-right) | privilege / no-right | `s 116(a)(2) the form of signature may be used`; `s 116(a)(2) the symbol or process is an electronic signature`; `s 116(a)(2) the person may execute a document with the person's signature` |
| s 116(a)(3), (a) last, (b) last | the sender (to deliver by entering the recipient's designated system); the parties (to conduct the transaction under Chapter 12A of Title 6); the certificate or bylaws (limiting subsection (a) only by an express restriction) | the recipient (deemed to have received, whether or not aware); the person who would say subsection (a) is limited (no-right unless expressly) | power / liability, privilege / no-right | `s 116(a)(3) the electronic transmission is deemed delivered to the person`; `s 116(a)(3) the person has designated the information processing system`; `s 116(a)(3) delivery requires that a person be aware of the receipt`; `s 116(a)(3) the electronic acknowledgement establishes that the electronic transmission was received`; `s 116(a)(3) the electronic acknowledgement by itself establishes that the content sent corresponds to the content received`; `s 116(a) this chapter does not prohibit conducting the transaction in accordance with Chapter 12A of Title 6`; `s 116(b) the provision of the certificate of incorporation or the bylaws limits the application of subsection (a)` |
| s 116(c) | none: which governs where the chapter and the federal Act meet | none | none | `s 116(c) this chapter controls` |

## Coverage table

The table has one row for each section heading, one for each provision (a subsection or paragraph wherever they differ in disposition or in the rule they state; a section whose subsections are encoded together is one row), one for each History line and one for each heading above section 101.
`source lines` is a locator into `de-code-t8-ch1-2026-10-01.txt`; every non-blank line of lines 1 to 239 falls inside the source-lines cell of at least one row (the script that built this file checks it).
`where` names the module and the rules.
Dispositions: `encoded`; `inert` (a pure title, a pure citation, or an application note that points to a session-law clause not in the text); `repealed or blank in this text`; `fork` (the text does not settle the reading; the row points to the Fork register, where the reading taken is stated).

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| file title lines | src:1-2 | inert | none | Pure title: the converter's two title lines for the whole chapter ("Delaware Code, Title 8, Chapter 1 - General Corporation Law" and "8 Del. C. ch. 1 (§§ 101-398)"). Not a provision. |
| source notices: URLs, currency, unofficial-version and kept-lines notices, and the rule line | src:4-27 | inert | none | A pure citation of where the text came from (the eighteen subchapter URLs and their retrieval times), the currency statement (acts enacted as of 2026-10-01, through 85 Del. Laws c. 550), the UNOFFICIAL VERSION and Kept: notices written by the converter, and the line of equals signs. None of it is the Law; the source is recorded in NOTES.md and in the core's notes. |
| TITLE 8, Corporations | src:29-30 | inert | none | Pure title (a heading): the title of the Delaware Code that holds the chapter. It states no rule. |
| CHAPTER 1. General Corporation Law | src:31 | inert | none | Pure title (a heading): the chapter's name. Its short title is stated again in section 398 (piece dg11); no rule here. |
| Subchapter I. Formation | src:32 | inert | none | Pure title (a heading) of the subchapter that holds sections 101 to 116. |
| s 101 heading | src:34 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Incorporators; how corporation formed; purposes. |
| s 101(a) | src:35 | fork | dg1-s101-formation.l4: `s 101(a) the entity may incorporate or organize a corporation under this chapter`; `s 101(a) the corporation has been incorporated by filing the certificate of incorporation` | Who may incorporate (F1: which kinds of entity "person, partnership, association or corporation" reaches; a limited liability company, statutory trust, real estate investment trust and common-law trust answer NOTHING) and that incorporation is by filing a certificate executed, acknowledged and filed in accordance with section 103 (calls the section 103 rules). Residence, domicile and state of incorporation are disregarded: no rule reads them. |
| s 101(b) | src:36 | encoded | dg1-s101-formation.l4: `s 101(b) a corporation may be incorporated to conduct or promote the business or purposes` | Any lawful business or purposes, except as the Constitution or other law of this State may otherwise provide (the outcome of that other law is an input). |
| s 101(c) | src:37 | encoded | dg1-s101-formation.l4: `s 101(c) a corporation for operating public utilities, in or outside this State, may be organized under this chapter`; `s 101(c) the corporation is subject also to the special provisions and requirements of Title 26` | Public utilities may be organized under the chapter, in or outside the State; one that operates within the State is also subject to Title 26 (Title 26 itself is not an input: only the fact of being subject to it is decided). |
| s 101 History | src:38 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 102 heading | src:40 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Contents of certificate of incorporation. |
| s 102(a) chapeau | src:41 | encoded | dg1-s102a-required-contents.l4: `s 102(a) the certificate of incorporation sets forth everything that subsection (a) requires` | The certificate "shall set forth" the six matters of paragraphs (a)(1) to (6): the rule is the conjunction of the six results. |
| s 102(a)(1)(i) | src:42 | fork | dg1-s102a-required-contents.l4: `s 102(a)(1)(i) the words one of which the name must contain`; `s 102(a)(1)(i) the name satisfies the requirement as to words` | The twelve words (carried as data), words of like import of foreign countries in roman characters, and the Division's waiver for a certificate of total assets of not less than $10,000,000 or, in its sole discretion, a nonprofit nonstock association of professionals (F2: the natural-person parenthetical limits both routes). Source line 42 is one 635-word line; the rows (a)(1)(i) to (iv) share it. |
| s 102(a)(1)(ii) | src:42 | encoded | dg1-s102a-required-contents.l4: `s 102(a)(1)(ii) the name satisfies the requirement as to distinction on the records` | The name must distinguish itself on the records from reserved names and from the names of the listed entities, except with the written consent of the person who reserved it or of the other entity, or on the Division's waiver after the three showings the text lists. |
| s 102(a)(1)(iii) | src:42 | encoded | dg1-s102a-required-contents.l4: `s 102(a)(1)(iii) the name satisfies the requirement as to the word trust` | No word "trust" except as section 395 (piece dg11) permits: the permission is an input. |
| s 102(a)(1)(iv) | src:42 | fork | dg1-s102a-required-contents.l4: `s 102(a)(1)(iv) the name satisfies the requirement as to the word bank`; `s 102(a)(1) the name of the corporation complies` | No word "bank" or variation, except four kinds of name; and the proviso about a context clearly not purporting to refer to a banking business (F3: "or otherwise likely to mislead" is read as the Division's finding that the use is not so likely). The four limbs together are `s 102(a)(1) the name of the corporation complies`. |
| s 102(a)(2) | src:43 | encoded | dg1-s102a-required-contents.l4: `s 102(a)(2) the certificate sets forth the registered office and registered agent` | The address of the registered office (stated in accordance with section 131(c), piece dg2, an input) and the name of the registered agent at that address. |
| s 102(a)(3) | src:44 | encoded | dg1-s102a-required-contents.l4: `s 102(a)(3) the certificate sets forth the nature of the business or purposes`; `s 102(a)(3) the act or activity is within the purposes of the corporation` | The statement of purposes; the general statement (any lawful act or activity) is sufficient and brings in all lawful acts and activities except express limitations. |
| s 102(a)(4) | src:45 | fork | dg1-s102a-required-contents.l4: `s 102(a)(4) the certificate sets forth the authorized stock`; `s 102(a)(4) the certificate and the bylaws set forth what a nonstock corporation must state`; `s 102(a)(4) the certificate and the bylaws set forth what paragraph (a)(4) requires`; `s 102(a)(4) the person is a member of the nonstock corporation`; `s 102(a)(4) the corporate act remains valid although the nonstock corporation has no members`; `s 102(a)(4) the nonstock corporation has forfeited its existence or is dissolved because it has no members`; `s 102(a)(4) the nonstock corporation may make the provision for its members` | One 594-word line: stock corporations (one class; more than one class; the statement of rights and the grant to the board, each only to the extent "desired", F22) and nonstock corporations (the statement that no capital stock may be issued; the conditions of membership; members deemed to be those entitled to vote for the governing body if none is stated; want of members does not affect valid acts; classes and voting of members). Section 151 (piece dg3) decides which rights may be fixed. |
| s 102(a)(5) | src:46 | encoded | dg1-s102a-required-contents.l4: `s 102(a)(5) the certificate sets forth the incorporators` | The name and mailing address of each incorporator. |
| s 102(a)(6) | src:47 | encoded | dg1-s102a-required-contents.l4: `s 102(a)(6) the certificate sets forth the first directors` | The first directors are named only if the incorporators' powers are to terminate upon the filing. |
| s 102(b) chapeau | src:48 | encoded | dg1-s102b-optional-provisions.l4: `s 102(b) the certificate of incorporation is required to contain the matter listed in subsection (b)` | "May also contain any or all of the following": none of the matters of paragraphs (b)(1) to (7) is required; the rule says so, and each paragraph below states what the matter is. |
| s 102(b)(1) | src:49 | encoded | dg1-s102b-optional-provisions.l4: `s 102(b)(1) the certificate of incorporation may contain the provision`; `s 102(b)(1) a provision that this chapter requires or permits to be stated in the bylaws may instead be stated in the certificate of incorporation` | Provisions for management and for the powers of the corporation, directors and stockholders (or governing body and members), if not contrary to the laws of this State; any provision that may be in the bylaws may instead be in the certificate. |
| s 102(b)(2) | src:50-53 | fork | dg1-s102b-optional-provisions.l4: `s 102(b)(2) the certificate of incorporation contains the compromise or arrangement provision in haec verba`; `s 102(b)(2) the applicant may apply for a meeting to be summoned`; `s 102(b)(2) the compromise or arrangement and the reorganization are binding on all` | The provision "in haec verba", (i) for a corporation other than a nonstock corporation and (ii) for a nonstock corporation: lines 50 and 52 introduce them, lines 51 and 53 are their text. Who may apply (sections 291 and 279 of piece dg9 are inputs for receivers and trustees), and the vote: a majority in number representing three fourths in value, with the court's sanction (F4). |
| s 102(b)(3) | src:54 | fork | dg1-s102b-optional-provisions.l4: `s 102(b)(3) the certificate of incorporation may contain the provision granting a preemptive right`; `s 102(b)(3) the date on which existing preemptive rights are preserved` (1967-07-03); `s 102(b)(3) the stockholder has a preemptive right to subscribe to an additional issue of stock or to a convertible security` | No preemptive right unless expressly granted in the certificate; rights in existence on July 3, 1967 remain unless changed or terminated by appropriate action that expressly provides for it (F31). |
| s 102(b)(4) | src:55 | fork | dg1-s102b-optional-provisions.l4: `s 102(b)(4) the certificate of incorporation requires a larger portion of the stock or other securities having voting power than this chapter requires`; `s 102(b)(4) the certificate of incorporation requires a larger number of the directors than this chapter requires` | A larger vote or a larger number of the directors than the chapter requires. The chapter's own requirement is a plain input (a `Vote requirement` of the core) (F28). |
| s 102(b)(5) | src:56 | fork | dg1-s102b-optional-provisions.l4: `s 102(b)(5) the duration of the corporation's existence has expired`; `s 102(b)(5) the corporation has perpetual existence` | A limit on the duration to a specified date; otherwise perpetual existence (F31). |
| s 102(b)(6) | src:57 | encoded | dg1-s102b-optional-provisions.l4: `s 102(b)(6) the stockholder is personally liable for the payment of the corporation's debts` | A provision may impose personal liability for the debts on stockholders to a specified extent and on specified conditions; otherwise no personal liability except by reason of their own conduct or acts. |
| s 102(b)(7) chapeau and (i) to (v) | src:58-63 | fork | dg1-s102b-optional-provisions.l4: `s 102(b)(7) the provision may eliminate or limit the person's personal liability` | May eliminate or limit a director's or officer's personal liability for monetary damages for breach of fiduciary duty, but not for (i) the duty of loyalty, (ii) bad faith, intentional misconduct or a knowing violation of law, (iii) a director under section 174 (piece dg3), (iv) an improper personal benefit, (v) an officer in an action by or in the right of the corporation (F16, F17). |
| s 102(b)(7) acts before the effective date | src:64 | encoded | dg1-s102b-optional-provisions.l4: `s 102(b)(7) the provision may eliminate or limit the person's personal liability` (the date comparison) | No such provision eliminates or limits liability for an act or omission before the date when it becomes effective (compared as dates: an act on that date is not before it). |
| s 102(b)(7) amendment or repeal | src:65 | encoded | dg1-s102b-optional-provisions.l4: `s 102(b)(7) the provision as it stood continues to apply to the act or omission despite the later amendment, repeal or elimination` | An amendment, repeal or elimination does not affect an act or omission before it, unless the provision provides otherwise at the time of the act. |
| s 102(b)(7) "director" | src:66 | encoded | dg1-s102b-optional-provisions.l4: `s 102(b)(7) Capacity` (the second constructor) and `s 102(b)(7) the provision may eliminate or limit the person's personal liability` | References to a director include a person who under the certificate, in accordance with section 141(a) (piece dg2), exercises the board's powers: that person is a capacity of its own, treated as a director. |
| s 102(b)(7) "officer" | src:67 | fork | dg1-s102b-optional-provisions.l4: `s 102(b)(7) the provision may eliminate or limit the person's personal liability` (the first branch) | An officer is only a person deemed to have consented to service under 10 Del. C. § 3114(b) (Title 10, an input). An officer who has not so consented is not within the paragraph: NOTHING (F16). |
| s 102(c) | src:68 | encoded | dg1-s102b-optional-provisions.l4: `s 102(c) the certificate of incorporation must set forth the power` | It is not necessary to set forth in the certificate any power the chapter confers on corporations. |
| s 102(d) | src:69 | fork | dg1-s102b-optional-provisions.l4: `s 102(d) the provision may be made dependent on facts ascertainable outside the certificate`; `s 102(d) the matter is a fact on which a provision may depend` | Provisions may depend on facts ascertainable outside the certificate, except the listed ones, if the manner in which the facts operate is clearly and explicitly set forth. The second sentence ("facts" includes any event and any determination or action by any person or body) is encoded, not left inert (F18). |
| s 102(e) chapeau and (1) to (4) | src:70-74 | fork | dg1-s102e-name-reservation.l4: `s 102(e) the exclusive right to use the name may be reserved by or on behalf of the person` | Who may reserve a name: the four kinds of person (F26: the list is read as exhaustive). |
| s 102(e) the procedure | src:75 | fork | dg1-s102e-name-reservation.l4: `s 102(e) the application to reserve a name is in the form required`; `s 102(e) the Secretary of State must reserve the name for the applicant for a period of 120 days`; `s 102(e) the last day of the reservation`; `s 102(e) the application for renewal renews the reservation`; `s 102(e) the right to the exclusive use of the reserved name has been transferred`; `s 102(e) the reservation has been cancelled`; `s 102(e) the Secretary of State must return a copy of the filed instrument with a notation of the action taken`; `s 102(e) the fee payable at the time of the filing` | The application, the 120-day reservation and its renewals (F5), transfer, cancellation, the copy returned and the fee (the amount is section 391, piece dg11, an input). |
| s 102(f) | src:76 | encoded | dg1-s102b-optional-provisions.l4: `s 102(f) the certificate of incorporation may contain the provision` | No provision imposing liability on a stockholder for the attorneys' fees or expenses of the corporation or any other party in an internal corporate claim (section 115(b), called) or in any other claim a stockholder has brought. |
| s 102 History | src:77 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 103 heading | src:79 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Execution, acknowledgment, filing, recording and effective date of original certificate of incorporation and other instruments; exceptions. |
| s 103(a) chapeau | src:80 | encoded | dg1-s103-filing.l4: `s 103(a) the instrument is executed as required` | Whenever an instrument is to be filed with the Secretary of State or in accordance with the section or chapter, it is executed as paragraphs (a)(1) and (2) say; the rule chooses between them. |
| s 103(a)(1) | src:81 | fork | dg1-s103-filing.l4: `s 103(a)(1) the instrument is one that the incorporators sign`; `s 103(a)(1) the instrument is signed as required of the incorporators` | The certificate, and any other instrument filed before the initial board is elected if the initial directors were not named, is signed by the incorporators (all of them: F12); another such instrument may be signed by their successors and assigns, or, if an incorporator is not available, by the person for whom the incorporator acted, with the three statements. |
| s 103(a)(2) | src:82-86 | fork | dg1-s103-filing.l4: `s 103(a)(2) the instrument is signed as required for the corporation` | All other instruments are signed by an authorized officer (a.); or, if it appears from the instrument that there are no officers, by a majority of the directors or those the board designates (b.); or, if no officers or directors, by the holders of record of a majority of the shares or those they designate (c.); or by the holders of record of all the shares (d.). Read as alternatives (F11). |
| s 103(b) chapeau, (1) and (2) | src:87-89 | fork | dg1-s103-filing.l4: `s 103(b)(1) the formal acknowledgment has been made`; `s 103(b)(2) the signature alone is the acknowledgment`; `s 103(b) the requirement that the instrument be acknowledged is satisfied`; `s 103(b)(2) the signatory affirms under penalties of perjury that the facts stated are true`; `s 103(b)(2) the date as of which the facts stated by a signatory relying on the signature alone must be true` | The acknowledgment requirement is satisfied by a formal acknowledgment before a person authorized to take acknowledgments of deeds (with the seal, if that person has one) or by the signature without more, which is then the signatory's affirmation under penalties of perjury that the facts stated will be true when the instrument becomes effective (F13). |
| s 103(c) chapeau, (1) and (2) | src:90-92 | encoded | dg1-s103-filing.l4: `s 103(c)(1) and (2) the filer has done what filing requires of the filer` | "Filed" means delivered to the office of the Secretary of State, with all taxes and fees tendered. |
| s 103(c)(3) | src:93 | fork | dg1-s103-filing.l4: `s 103(c)(3) the Secretary of State must certify the instrument as filed`; `s 103(c) the instrument has been filed`; `s 103(c)(3) the filing date of the instrument` | Upon delivery and tender the Secretary of State records the date and time, certifies the instrument as filed by endorsing "Filed", and the endorsement is the filing date, conclusive absent actual fraud; the filing date is the date of delivery except as (c)(4) and (i) provide (F6: the time of day is not carried). |
| s 103(c)(4) | src:94 | fork | dg1-s103-filing.l4: `s 103(c)(4) the Secretary of State may hold the instrument in suspension`; `s 103(c)(4) the Secretary of State is barred from issuing a certificate of good standing`; `s 103(c) Route to the filing date`; `s 103(c)(3) the filing date of the instrument` | A later date on request; the instrument held in suspension for an error, omission or imperfection and its replacement within 5 business days (F15); no certificate of good standing while an instrument is in suspension; the date the information was entered if the instrument is delivered the same date within 4 hours. |
| s 103(c)(5) | src:95 | encoded | dg1-s103-filing.l4: `s 103(c)(5) the administrative charge the Secretary of State retains and pays to the General Fund` | The Secretary of State acts as agent for the county recorders, collecting the county assessment fee and remitting it monthly; it retains 1 percent of the fees collected. The rule computes the 1 percent. |
| s 103(c)(6) | src:96 | encoded | dg1-s103-filing.l4: `s 103(c)(6) the county assessment fee`; `s 103(c)(6) the county whose recorder's office receives the assessment fee` | $24 for a 1-page instrument and $9.00 for each additional page; none for a qualifying certificate of dissolution (section 391(a)(5)b., piece dg11) or a subchapter XVI document (piece dg10); received by the recorder's office of the county of the registered office. |
| s 103(c)(7) | src:97 | encoded | dg1-s103-filing.l4: `s 103(c)(7) the courthouse municipality fee`; `s 103(c)(7) the municipality that receives the courthouse municipality fee` | $40 for each instrument, none for three kinds; received by the municipality designated in 10 Del. C. § 301 in the county of the registered office (Title 10, an input). |
| s 103(c)(8) | src:98 | encoded | dg1-s103-filing.l4: `s 103(c)(8) the instrument and its information must be permanently maintained as a public record`; `s 103(c)(8) the Secretary of State may grant the registered agent direct access to the system`; `s 103(c)(8) the registered agent granted direct access has complied with the condition on that access` | The Secretary of State enters information from each instrument into the Delaware Corporation Information System and permanently maintains it and a copy as a public record; it may grant registered agents direct access under an operating agreement, and an agent so granted must demonstrate the policies the text names. |
| s 103(d) | src:99 | fork | dg1-s103-filing.l4: `s 103(d) the instrument may become effective on the specified later date`; `s 103(d) the date on which the instrument is effective`; `s 103(d) the future effective instrument has been terminated or amended by a certificate in due form and time` | Effective on its filing date; a later time, not later than a time on the ninetieth day after the filing (F14); a future-dated instrument is terminated or amended by a certificate filed before the future date (F6: same date is NOTHING). |
| s 103(e) | src:100 | encoded | dg1-s103-filing.l4: `s 103(e) the other section governs` | If another section specifically prescribes a different manner or time for a specified instrument, the other section governs. |
| s 103(f) | src:101 | fork | dg1-s103-filing.l4: `s 103(f) the instrument may be corrected or nullified by a certificate of correction`; `s 103(f) the certificate of correction is in the form required`; `s 103(f) the corrected instrument is in the form required`; `s 103(f) the date from which the corrected or nullified instrument is effective as to the person` | A filed instrument that is inaccurate or defectively executed, sealed or acknowledged is corrected or nullified by a certificate of correction or a corrected instrument; effective as of the original filing date except as to persons substantially and adversely affected (F7: "the filing date"). |
| s 103(g) | src:102 | encoded | dg1-s103-filing.l4: `s 103(g) the Secretary of State is liable to any person for the act` | The Secretary of State has no liability to any person for preclearance, acceptance for filing, or filing and indexing of a defective instrument; any other act is not covered (NOTHING). |
| s 103(h) | src:103 | fork | dg1-s103-filing.l4: `s 103(h) the form of signature is permitted on an instrument authorized to be filed` | A signature may be a facsimile, a conformed signature or an electronically transmitted signature (a manual signature is the ordinary meaning of "signed") (F27). |
| s 103(i)(1) | src:104-108 | fork | dg1-s103-filing.l4: `s 103(i)(1) the Secretary of State may establish the earlier date and time as the filing date`; `s 103(i)(1) the fee payable to the Secretary of State for receiving an affidavit of extraordinary condition` | An affidavit of extraordinary condition (a.) or the Secretary of State's written waiver (b.), and the Secretary of State's three determinations (c.), including delivery within 2 business days of the end of the condition; then the Secretary of State may establish the earlier date. No fee is paid for receiving the affidavit (F23). |
| s 103(i)(2) | src:109 | encoded | dg1-s103-filing.l4: `s 103(i)(2) there is an extraordinary condition`; `s 103(i)(2) the determination of the Secretary of State is conclusive` | "Extraordinary condition" means (first limb) an emergency from the listed events or the immediate threat of one, or (second limb) a malfunction, outage, weather or other condition that closes the Secretary of State's office or makes filing possible only with extraordinary effort; the Secretary of State's determination is conclusive absent actual fraud. |
| s 103(i)(3) | src:110 | encoded | dg1-s103-filing.l4: `s 103(i)(3) the date from which the instrument is effective as to the person` | The instrument is effective as of the date established, except as to persons substantially and adversely affected, as to whom it is effective from the date endorsed on the affidavit or waiver. |
| s 103(j) | src:111 | encoded | dg1-s103-filing.l4: `s 103(j) the date before which a filed document need not be amended to comply with § 131(c)` (1 August 2011); `s 103(j) the corporation need not amend the document to comply with § 131(c)`; `s 103(j) the document must comply with § 131(c)` | A document filed before 1 August 2011 need not be amended to comply with section 131(c) (piece dg2); a document filed on or after it that changes the address of a registered office must comply. |
| s 103 History | src:112 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 104 heading | src:114 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Certificate of incorporation; definition. |
| s 104 | src:115 | encoded | dg1-s101-formation.l4: `s 104 the instrument is part of the certificate of incorporation` | "Certificate of incorporation" includes the original and every other instrument filed under any section of this title that amends or supplements it, unless the context requires otherwise. The listed sections are examples ("or any other section"), so the rule does not test the section number. |
| s 104 History | src:116 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 105 heading | src:118 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Certificate of incorporation and other certificates; evidence. |
| s 105 | src:119-122 | encoded | dg1-s101-formation.l4: `s 105 Matter evidenced`; `s 105 the certified copy is received as prima facie evidence of the matter` | A copy certified by the Secretary of State is received in all courts, public offices and official bodies as prima facie evidence of due execution, acknowledgment and filing; observance of the conditions precedent to effectiveness; and any other fact required or permitted by law to be stated in the instrument. |
| s 105 History | src:123 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 106 heading | src:125 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Commencement of corporate existence. |
| s 106 | src:126 | fork | dg1-s101-formation.l4: `s 106 the date from which the incorporators are a body corporate`; `s 106 the name by which the body corporate exists`; `s 106 the body corporate exists on the day` | Upon filing of the certificate, executed and acknowledged in accordance with section 103, the incorporators who signed it, and their successors and assigns, are from the date of filing a body corporate by the name in the certificate, subject to section 103(d) and to dissolution (F25: a later effective date postpones existence). |
| s 106 History | src:127 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 107 heading | src:129 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Powers of incorporators. |
| s 107 | src:130 | encoded | dg1-s101-formation.l4: `s 107 Act of the incorporators`; `s 107 the incorporators manage the affairs of the corporation`; `s 107 the incorporators may do the act` | If the first directors were not named in the certificate, the incorporators manage the affairs until the directors are elected and may do whatever is necessary and proper to perfect the organization, including adopting the original bylaws and electing directors. |
| s 107 History | src:131 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 108 heading | src:133 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Organization meeting of incorporators or directors named in certificate of incorporation. |
| s 108(a) | src:134 | fork | dg1-s108-organization.l4: `s 108(a) the organization meeting is a meeting of the board of directors and not of the incorporators`; `s 108(a) the call of the organization meeting is made by a majority of the incorporators or directors`; `s 108(a) Place of the organization meeting`; `s 108(a) the organization meeting may be held at the place`; `s 108(a) Purpose of the organization meeting`; `s 108(a) the purpose may be pursued at the organization meeting` | After filing, an organization meeting of the incorporators, or of the board if the initial directors were named, is held within or without the State at the call of a majority of them, for the purposes listed (electing directors if of the incorporators; electing officers if of the directors) (F30). |
| s 108(b) | src:135 | fork | dg1-s108-organization.l4: `s 108(b) the notice of the organization meeting is sufficient`; `s 108(b) notice of the meeting need not be given to the person` | At least 2 days' notice in writing or by electronic transmission stating the time, place and purposes (F10: counted in calendar days, the second day inside); none for one who attends or waives before or after. |
| s 108(c) | src:136 | fork | dg1-s108-organization.l4: `s 108(c) the action may be taken without a meeting`; `s 108(c) the consent given for a future time is deemed given at that time`; `s 108(c) the consent may still be revoked` | Action without a meeting by the unanimous consent of the incorporators or directors (or the sole one), unless the certificate restricts it; consents documented, signed and delivered as section 116 permits; a consent effective at a future time not later than 60 days after the instruction (F10), revocable before it becomes effective (F6). |
| s 108(d) | src:137 | encoded | dg1-s108-organization.l4: `s 108(d) the person may take the action that the incorporator would have been authorized to take under this section or § 107` | If an incorporator is not available, the person for whom the incorporator acted as employee or agent may take the incorporator's action, if the instrument or record states that the incorporator is not available and why, that the incorporator acted for that person, and that the person's signature or participation is otherwise authorized and not wrongful. |
| s 108 History | src:138 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 109 heading | src:140 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Bylaws. |
| s 109(a) | src:141 | fork | dg1-s109-bylaws-and-emergency-powers.l4: `s 109(a) Holder of the power over the bylaws`; `s 109(a) the holder has the power to adopt, amend or repeal bylaws`; `s 109(a) the conferral of the power on the directors or governing body divests the stockholders or members of the power` | Who holds the power to adopt, amend or repeal bylaws: the incorporators; the initial directors (or initial members of the governing body) if named; the board before any payment for stock; the stockholders (members) entitled to vote; and the directors or governing body if the certificate confers it, without divesting the stockholders or members (F8). |
| s 109(b) first sentence and the limit on fees | src:142 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 109(b) the bylaws may contain the provision`; `s 109(b) the bylaws may contain the provision on fees and expenses` | The bylaws may contain any provision, not inconsistent with law or the certificate, relating to the business, affairs, rights or powers of the corporation or of its stockholders, directors, officers or employees; but not one imposing liability on a stockholder for attorneys' fees or expenses in an internal corporate claim (section 115(b), called) or another claim a stockholder has brought. Line 142 holds both sentences; the "last sentence" is the one section 114(b)(2) names. |
| s 109 History | src:143 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 110 heading, with its application note | src:145 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. The bracketed note "[For application of this section, see 82 Del. Laws, c. 256, § 23]" points to an application clause of the session law that is not in the text; the clause itself is not among the inputs, so it is not encoded. |
| s 110(a) chapeau and adoption | src:146 | fork | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(a) Emergency`; `s 110(a) the emergency bylaws are operative`; `s 110(a) the emergency bylaws were validly adopted`; `s 110(a) the emergency bylaws are subject to repeal or change by action of the stockholders`; `s 110(a) the emergency bylaws may make the provision` | The board may adopt emergency bylaws, subject to repeal or change by the stockholders, operative during an attack, nuclear or atomic disaster, catastrophe (including an epidemic or pandemic and a declaration of a national emergency) or similar emergency, whether or not a quorum can be convened; adopted by the board or, if a quorum cannot be readily convened, by a majority of the directors present (F20). |
| s 110(a)(1) | src:147 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(a)(1) the person may call a meeting of the board of directors or a committee` | Emergency bylaws may let any officer or director call a meeting of the board or a committee in the manner and on the conditions they prescribe. |
| s 110(a)(2) | src:148 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(a)(2) the directors in attendance constitute a quorum` | The director or directors in attendance, or any greater number the emergency bylaws fix, are a quorum. |
| s 110(a)(3) | src:149 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(a)(3) the person is deemed a director for the meeting` | Officers or other persons on a list approved by the board before the emergency are deemed directors for a meeting, in the order of priority and on the conditions and for the period provided, to the extent required for a quorum. |
| s 110(b) | src:150 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(b) Time of the board's action`; `s 110(b) the board of directors may provide, and from time to time modify, lines of succession` | The board, before or during an emergency, may provide and modify lines of succession; after the emergency the subsection does not speak (NOTHING). |
| s 110(c) | src:151 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(c) the board of directors may, effective in the emergency, change the head office or designate alternative head offices or regional offices, or authorize the officers to do so` | The board, before or during an emergency, may change the head office or designate alternative offices, effective in the emergency, or authorize the officers to do so. |
| s 110(d) | src:152 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(d) the person is protected from liability` | No officer, director or employee acting in accordance with emergency bylaws is liable except for wilful misconduct (the immunity is encoded; liability for wilful misconduct is other law). |
| s 110(e) | src:153 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(e) the bylaw of the corporation remains in effect during the emergency`; `s 110(a) the emergency bylaws are operative` (termination) | The bylaws remain in effect during the emergency to the extent not inconsistent with the emergency bylaws; on its termination the emergency bylaws cease to be operative. |
| s 110(f) | src:154 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(f) the notice of the meeting of the board of directors is sufficient` | Unless the emergency bylaws provide otherwise, notice of a board meeting during an emergency may be given only to the directors it is feasible to reach, by means feasible at the time, including publication or radio. |
| s 110(g) | src:155 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(g) the officer present is deemed a director for the meeting` | To the extent required for a quorum, officers present are, unless the emergency bylaws provide otherwise, deemed directors for the meeting in order of rank and, within a rank, of seniority. |
| s 110(h) | src:156 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(h) the provision for emergency powers is permitted in addition to this section` | The section is not exclusive of other provisions for emergency powers consistent with other sections of the title. |
| s 110(i) | src:157 | fork | dg1-s109-bylaws-and-emergency-powers.l4: `s 110(i) the action with respect to the meeting of stockholders is authorized`; `s 110(i)(i)(1) the record date that applies to the postponed meeting`; `s 110(i)(i)(2) the corporation may give the notice solely by a document publicly filed with the Securities and Exchange Commission`; `s 110(i)(ii) the board of directors may change the record date and the payment date of the declared dividend as it has`; `s 110(i) the corporation has given notice of the change in time`; `s 110(i) the failure to make a stocklist available is excused` | In an emergency condition the board (or a majority of the directors present if no quorum can be convened) may take any practical and necessary action on a stockholders' meeting, including postponing it, and may move a declared dividend's record and payment dates later (the payment date not more than 60 days after the record date as changed), giving notice promptly and before the record date theretofore in effect; no one is liable, and no meeting is postponed or voided, for failing to make the stocklist available (section 219, piece dg4) if inspection was not practicable (F21). Federal securities law is an input (F32). |
| s 110 History | src:158 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 111 heading, with its application note | src:160 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. The bracketed note "[For application of this section, see 80 Del. Laws, c. 265, § 17]" points to an application clause of the session law that is not in the text; it is not encoded. |
| s 111(a) chapeau and (1) to (9) | src:161-171 | encoded | dg1-s111-s115-jurisdiction-and-forum.l4: `s 111(a) Subject of the action`; `s 111(a) the civil action may be brought in the Court of Chancery` | A civil action to interpret, apply, enforce or determine the validity of the nine kinds of instrument and provision listed may be brought in the Court of Chancery, except to the extent that a statute confers exclusive jurisdiction on another court, agency or tribunal. Lines 161 to 170 are the chapeau and the nine paragraphs; line 171 is the tail ("may be brought ..."). For a nonprofit nonstock corporation section 114(c)(2) takes (a)(2) and (3) out of the member reading (dg1-s114-nonstock.l4). |
| s 111(b) | src:172 | encoded | dg1-s111-s115-jurisdiction-and-forum.l4: `s 111(b) the civil action may be brought in the Court of Chancery` | Any civil action to interpret, apply or enforce a provision of this title may be brought in the Court of Chancery. |
| s 111 History | src:173 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 112 heading | src:175 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Access to proxy solicitation materials. |
| s 112 | src:176-182 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 112 the corporation may be required to include the stockholder's nominee in its proxy solicitation materials`; `s 112 Condition of access`; `s 112 the bylaws may impose the condition` | The bylaws may require a corporation that solicits proxies for an election of directors to include in its materials individuals nominated by a stockholder, on procedures and conditions that may include the five listed and any other lawful condition (lines 177 to 182 are conditions (1) to (6)). |
| s 112 History | src:183 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 113 heading | src:185 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Proxy expense reimbursement. |
| s 113(a) | src:186-190 | encoded | dg1-s109-bylaws-and-emergency-powers.l4: `s 113(a) the corporation may be required to reimburse the stockholder's expenses`; `s 113(a) Condition of reimbursement`; `s 113(a) the bylaws may prescribe the condition` | The bylaws may provide for reimbursement of a stockholder's expenses in soliciting proxies for an election of directors, on procedures and conditions that may include the three listed and any other lawful condition (lines 187 to 190 are conditions (1) to (4)). |
| s 113(b) | src:191 | fork | dg1-s109-bylaws-and-emergency-powers.l4: `s 113(b) the bylaw applies to the election` | No bylaw so adopted applies to an election for which any record date precedes its adoption (F29). |
| s 113 History | src:192 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 114 heading | src:194 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Application of chapter to nonstock corporations. |
| s 114(a) | src:195-199 | encoded | dg1-s114-nonstock.l4: `s 114(a) Kind of reference`; `s 114(a) Reading`; `s 114(a) how the reference in the provision is read` | Except as (b) and (c) provide, the chapter and chapter 5 apply to nonstock corporations with stockholders read as members, the board as the governing body, directors as members of the governing body, and stock as memberships (nonprofit nonstock) or membership interests (any other nonstock corporation). |
| s 114(b) | src:200-203 | fork | dg1-s114-nonstock.l4: `s 114(b)(1) the provisions that apply to nonstock corporations by their terms`; `s 114(b)(2) the other provisions to which subsection (a) does not apply`; `s 114(b)(3) the subchapters to which subsection (a) does not apply`; `s 114(b) and (c) subsection (a) does not apply to the provision` | Subsection (a) does not apply to the sections listed in (b)(1) and (b)(2) and to subchapters XIV and XVI; the lists are data (sections 503 and 502(a)(5) belong to chapter 5, not among the inputs). A part of a section is matched by its label at the level the list names it (F19). |
| s 114(c) | src:204-207 | encoded | dg1-s114-nonstock.l4: `s 114(c)(2) the further provisions to which subsection (a) does not apply for a nonprofit nonstock corporation`; `s 114(c)(3) the subchapters to which subsection (a) does not apply for a nonprofit nonstock corporation`; `s 114(b) and (c) subsection (a) does not apply to the provision` | For a nonprofit nonstock corporation subsection (a) also does not apply to the (c)(2) sections and to subchapters V, VI (other than sections 204 and 205) and XV. |
| s 114(d) chapeau | src:208 | encoded | dg1-s114-nonstock.l4: `s 114(d) the kind of the corporation` and the four rules of (d)(1) to (4) | "For purposes of this chapter": the four definitions that follow are chapter-wide, which is why the core's `Kind of corporation` is the type every other piece takes as an input and the rule here decides it. |
| s 114(d)(1) to (4) | src:209-212 | encoded | dg1-s114-nonstock.l4: `s 114(d)(1) the corporation is a charitable nonstock corporation`; `s 114(d)(2) the interest of the member is a membership interest`; `s 114(d)(3) the corporation is a nonprofit nonstock corporation`; `s 114(d)(4) the corporation is a nonstock corporation`; `s 114(d) the kind of the corporation` | Charitable nonstock corporation (exempt under 26 U.S.C. § 501(c)(3): an input); membership interest; nonprofit nonstock corporation; nonstock corporation. The four facts decide one of the core's four kinds, or NOTHING for a corporation not organized under the chapter. |
| s 114 History | src:213 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 115 heading | src:215 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Forum selection provisions. |
| s 115(a) | src:216 | fork | dg1-s111-s115-jurisdiction-and-forum.l4: `s 115(a) the provision of the certificate of incorporation or the bylaws is permitted` | The certificate or bylaws may require, consistent with jurisdictional requirements, that internal corporate claims be brought solely and exclusively in the courts in this State, and no provision may prohibit bringing them in the courts of this State. A provision that does neither is not addressed (NOTHING, F24). |
| s 115(b) | src:217 | fork | dg1-s111-s115-jurisdiction-and-forum.l4: `s 115(b) the claim is an internal corporate claim`; `s 115(b)(ii) this title confers jurisdiction upon the Court of Chancery as to the claim` | "Internal corporate claims": claims based on a violation of a duty by a current or former director, officer or stockholder in that capacity, or as to which this title confers jurisdiction on the Court of Chancery (F9: section 111 counts as conferring it). |
| s 115(c) | src:218 | encoded | dg1-s111-s115-jurisdiction-and-forum.l4: `s 115(c) the certificate or the bylaws may require the stockholder to bring the claim only in the prescribed forums` | For claims that are not internal corporate claims, the certificate or bylaws may require stockholders to bring them only in prescribed forums, if consistent with jurisdictional requirements and allowing at least one court in this State that has jurisdiction. |
| s 115 History | src:219 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |
| s 116 heading | src:221 | inert | none | A section heading: a pure title (a heading) that names the section; the section's operative text is in the rows below. Document form, signature and delivery. |
| s 116(a) chapeau and (a)(1) | src:222-225 | encoded | dg1-s116-documents.l4: `s 116(a)(1) Medium`; `s 116(a)(1) the medium is a document`; `s 116(a)(1) the medium is deemed the equivalent of a written document` | An act or transaction may be provided for in a document; an electronic transmission is deemed the equivalent of a written document; "document" is a tangible medium or an electronic transmission. |
| s 116(a)(2) | src:226 | encoded | dg1-s116-documents.l4: `s 116(a)(2) Form of signature`; `s 116(a)(2) the form of signature may be used`; `s 116(a)(2) the symbol or process is an electronic signature`; `s 116(a)(2) the person may execute a document with the person's signature` | A required or permitted signature may be manual, facsimile, conformed or electronic; "electronic signature" is defined; a person may execute a document with the person's signature. |
| s 116(a)(3) | src:227 | encoded | dg1-s116-documents.l4: `s 116(a)(3) the electronic transmission is deemed delivered to the person`; `s 116(a)(3) the person has designated the information processing system`; `s 116(a)(3) delivery requires that a person be aware of the receipt`; `s 116(a)(3) the electronic acknowledgement establishes that the electronic transmission was received`; `s 116(a)(3) the electronic acknowledgement by itself establishes that the content sent corresponds to the content received` | Unless otherwise agreed (and subject, for stockholder proxies and consents, to sections 212(c)(2) and (3), piece dg4, and 228(d)(1), piece dg5), an electronic transmission is delivered when it enters a designated information processing system in a processable form the person can retrieve; designation is shown by the certificate, bylaws or circumstances; awareness is not required; an acknowledgement shows receipt, not content. |
| s 116(a) closing paragraph | src:228 | encoded | dg1-s116-documents.l4: `s 116(a) this chapter does not prohibit conducting the transaction in accordance with Chapter 12A of Title 6` | The chapter does not prohibit a transaction under Chapter 12A of Title 6 (Title 6, an input) so long as the parts governed by this chapter are documented, signed and delivered in accordance with it. |
| s 116(b) chapeau and (1) to (4) | src:229-233 | encoded | dg1-s116-documents.l4: `s 116(b) Kind of document`; `s 116(b) subsection (a) applies to the document` | Subsection (a) does not apply to a document filed with the Secretary of State, the Register in Chancery, a court or other body; a document that is part of the stock ledger; a certificate representing a security; a document expressly referenced as a notice (or waiver of notice). |
| s 116(b)(5) | src:234 | repealed or blank in this text | none | The text shows "(5) [Repealed.]": paragraph (b)(5) is repealed and states nothing. No rule. |
| s 116(b)(6) and (7) | src:235-236 | encoded | dg1-s116-documents.l4: `s 116(b) Kind of document`; `s 116(b) subsection (a) applies to the document` | Subsection (a) does not apply to a ballot to vote on actions at a meeting of stockholders, nor to an act or transaction effected under section 280 (piece dg9) or subchapters III, XIII or XVI. |
| s 116(b) closing paragraph | src:237 | encoded | dg1-s116-documents.l4: `s 116(b) a presumption arises from the exclusions about the lawful means to document, sign or deliver`; `s 116(b) the provision of the certificate of incorporation or the bylaws limits the application of subsection (a)` | The exclusions create no presumption about the lawful means to document, sign or deliver; and no provision of the certificate or bylaws limits subsection (a) except one that expressly restricts or prohibits an electronic transmission or signature, or the delivery of one to an information processing system. |
| s 116(c) | src:238 | encoded | dg1-s116-documents.l4: `s 116(c) this chapter controls` | If a provision of the chapter is deemed to modify, limit or supersede the federal Electronic Signatures in Global and National Commerce Act (an input), the chapter controls to the fullest extent permitted by § 7002(a)(2) of that Act. |
| s 116 History | src:239 | inert | none | The History line cites the 1953 Code and the Laws of Delaware that enacted or amended the section. It is a citation, not a provision, and decides nothing for the person. |

## Fork register

Where I looked: every operative sentence of sections 101 to 116 was read for four kinds of ambiguity: who a term reaches; whether a list is exhaustive or an example; whether a condition is cumulative or alternative; and where a day or an amount is counted from and whether the named day is inside.
Thirty-two readings are recorded below.
Each row of the coverage table marked `fork` cites one or more of them (F1 to F32), and each reading is cited by at least one such row.
Where the text decides, nothing is recorded: for example, section 109(a) names the holders of the power over bylaws in a closed list, and section 116(a)(1) defines "document" with "means".
Each entry gives the readings seen, the reading taken, and the words of the text that license it; the rule that carries the reading is named so that a reviewer can change it in one place.
An open question the text does not settle is returned as an explicit `NOTHING` ("the Law does not say"), and each such case is asserted.

**F1. s 101(a): which entities "person, partnership, association or corporation" reaches.**
- Readings: (a) every business entity, including a limited liability company, a statutory trust, a real estate investment trust and a common-law trust; (b) only a natural person, the partnerships, the corporations and the associations the core lists.
- Taken: (b); the other four answer `NOTHING`.
- Licence: "Any person, partnership, association or corporation, singly or jointly with others, and without regard to such person's or entity's residence, domicile or state of incorporation, may incorporate or organize a corporation under this chapter" (src:35); the only definition of "person" nearby is in section 203, outside this piece's range (src:660, read only for this purpose): "any individual, corporation, partnership, unincorporated association or other entity", for that section.
- Where: `s 101(a) the entity may incorporate or organize a corporation under this chapter`.

**F2. s 102(a)(1)(i): what the parenthetical limits.**
- Readings: (a) "(unless it determines that such name is, or might otherwise appear to be, that of a natural person)" limits both grounds of waiver (total assets of $10,000,000; a nonprofit nonstock association of professionals); (b) only the first.
- Taken: (a).
- Licence: "may waive such requirement (unless it determines that such name is, or might otherwise appear to be, that of a natural person) if such corporation executes, acknowledges and files ... a certificate stating that its total assets ... are not less than $10,000,000, or, in the sole discretion of the Division ..., if the corporation is both a nonprofit nonstock corporation and an association of professionals" (src:42): the parenthetical follows "waive such requirement" and precedes both "if" conditions.
- Where: `s 102(a)(1)(i) the name satisfies the requirement as to words`.

**F3. s 102(a)(1)(iv): the proviso on the word "bank".**
- Readings: (a) the word may be used in a context that is clearly not banking and also not otherwise likely to mislead or to lead to a pattern of abuse; (b) the word may be used in a context clearly not banking, or in one otherwise likely to mislead.
- Taken: (a); reading (b) would allow the word where the Division finds it misleading.
- Licence: "shall not be construed to prevent the use of the word 'bank,' or any variation thereof, in a context clearly not purporting to refer to a banking business or otherwise likely to mislead the public ... as determined by the Division" (src:42).
- Where: `s 102(a)(1)(iv) the name satisfies the requirement as to the word bank`; both findings are the Division's, so both are inputs.

**F4. s 102(b)(2): "a majority in number representing three fourths in value".**
- Readings: the majority in number is of (a) all the creditors or class, or (b) those voting; "three fourths in value" is (c) at least three fourths, or (d) more than three fourths.
- Taken: the counts are the caller's (the persons the caller counts), so (a) and (b) are both available; "three fourths" is at least three fourths; a majority is more than half; counts that cannot be a vote answer `NOTHING`.
- Licence: "If a majority in number representing three fourths in value of the creditors or class of creditors, and/or of the stockholders or class of stockholders ... agree to any compromise or arrangement" (src:51, and "members" at src:53); the text says neither that the majority is of those voting nor that it is of all.
- Where: `s 102(b)(2) the compromise or arrangement and the reorganization are binding on all`.

**F5. s 102(e): "for a period of 120 days" and "prior to the expiration".**
- Readings: the reservation lasts (a) through the 120th day after the day it is made, or (b) through the 119th day; a renewal filed on the last day is (c) in time or (d) too late.
- Taken: (a) and (c); each renewal adds 120 days.
- Licence: "the Secretary shall reserve the name for the use of the applicant for a period of 120 days.
  The same applicant may renew for successive 120-day periods ... by filing ..., prior to the expiration of such reservation (or renewal thereof)" (src:75); a filing on the last day is before the reservation ends.
- Where: `s 102(e) the last day of the reservation`; `s 102(e) the application for renewal renews the reservation`.

**F6. The time of day (s 103(c)(3), s 103(d), s 108(c)).**
- Readings: (a) carry a date and a time of day; (b) carry the date only.
- Taken: (b), so every answer that turns on the time of day within one date is `NOTHING`: whether a later effective time is "subsequent" on the filing date, whether a termination certificate is "prior to" the future date on that date, whether a consent is revoked "prior to" its effective time on that date.
- Licence: the text says "date and time" throughout, but the core has no time of day; carrying one would invent a type the other pieces do not share (see `## Needs from the core`).
- Where: `s 103(c)(3) the filing date of the instrument`; `s 103(d) the instrument may become effective on the specified later date`; `s 103(d) the future effective instrument has been terminated or amended by a certificate in due form and time`; `s 108(c) the consent may still be revoked`.

**F7. s 103(f): "the filing date" in the last sentence.**
- Readings: the persons substantially and adversely affected are bound from (a) the filing date of the correction, or (b) the filing date of the original instrument.
- Taken: (a).
- Licence: "effective as of the date the original instrument was filed, except as to those persons who are substantially and adversely affected by the correction or nullification and as to those persons the instrument as corrected or nullified shall be effective from the filing date" (src:101); the exception contrasts with the original's date.
- Where: `s 103(f) the date from which the corrected or nullified instrument is effective as to the person`.

**F8. s 109(a): who holds the power over the bylaws, and when it ends.**
- Readings: for a corporation other than a nonstock corporation, "After ... the corporation has received any payment for any of its stock, the power ... shall be in the stockholders entitled to vote" (a) takes the power from the incorporators, initial directors and board, or (b) adds the stockholders to them; for a nonstock corporation the text names no event that ends the incorporators' or the initial members' power.
- Taken: (a) for a stock corporation; for a nonstock corporation nothing ends the earlier holders' power, so the rule does not end it.
- Licence: "or, before a corporation other than a nonstock corporation has received any payment for any of its stock, by its board of directors.
  After a corporation other than a nonstock corporation has received any payment for any of its stock, the power to adopt, amend or repeal bylaws shall be in the stockholders entitled to vote" (src:141).
- Where: `s 109(a) the holder has the power to adopt, amend or repeal bylaws`.

**F9. s 115(b)(ii): "this title confers jurisdiction upon the Court of Chancery".**
- Readings: (a) section 111 (which says an action "may be brought in the Court of Chancery") counts as the title conferring jurisdiction; (b) only a provision that says in terms that it confers jurisdiction.
- Taken: (a), together with the input for any other section that confers it.
- Licence: section 111(a) and (b) are the only operative sentences in Subchapter I besides section 115(b) that mention the Court of Chancery (src:171, 172, 217); a claim section 111 lets the court hear is one "as to which this title confers jurisdiction".
- Where: `s 115(b)(ii) this title confers jurisdiction upon the Court of Chancery as to the claim`.

**F10. s 108(b) and (c): counting days.**
- Readings: "at least 2 days' notice" and "no later than 60 days after" count (a) calendar days with the last day inside, or (b) clear days.
- Taken: (a): a notice given on 10 March supports a meeting on 12 March; a consent set to take effect on the 60th day after the instruction is in time.
- Licence: the text says "days", not "business days" or "clear days" (src:135, 136); where it means business days it says so (src:94).
- Where: `s 108(b) the notice of the organization meeting is sufficient`; `s 108(c) the consent given for a future time is deemed given at that time`.

**F11. s 103(a)(2): alternatives a. to d.**
- Readings: the four ways of signing an instrument for the corporation are (a) alternatives, or (b) a ladder in which each applies only if the one above fails.
- Taken: (a); b. and c. are open only where it appears from the instrument that there are no officers (b.) or no officers or directors (c.); d.
  (holders of all the shares) is open at all times.
- Licence: the lettered limbs are joined by semicolons and "or" with their own conditions (src:82-86).
- Where: `s 103(a)(2) the instrument is signed as required for the corporation`.

**F12. s 103(a)(1): "the incorporator or incorporators".**
- Readings: (a) every incorporator must sign; (b) one is enough.
- Taken: (a); if an incorporator is not available, the successors and assigns or the person for whom the incorporator acted may sign, with the three statements.
- Licence: "shall be signed by the incorporator or incorporators ... If any incorporator is not available then any such other instrument may be signed, with the same effect as if such incorporator had signed it" (src:81): the substitute is for "any incorporator", which means each one signs.
- Where: `s 103(a)(1) the instrument is signed as required of the incorporators`.

**F13. s 103(b): acknowledgment by signature alone.**
- Readings: the signature "without more" (a) is itself the acknowledgment and the affirmation under penalties of perjury, or (b) is a second act beyond signing.
- Taken: (a); the affirmed facts must be true when the instrument becomes effective (paragraph (b)(2)), and a later effective date more than 90 days after filing is not covered.
- Licence: "The signature, without more, of the person or persons signing the instrument, in which case such signature or signatures shall constitute the affirmation or acknowledgment of the signatory, under penalties of perjury, that the instrument is such person's act and deed or the act and deed of the corporation, and that the facts stated therein shall be true at the time such instrument becomes effective in accordance with this chapter" (src:89).
- Where: `s 103(b)(2) the signature alone is the acknowledgment`; `s 103(b)(2) the date as of which the facts stated by a signatory relying on the signature alone must be true`.

**F14. s 103(d): "not later than a time on the ninetieth day after the date of its filing".**
- Readings: the ninetieth day is (a) inside the period, or (b) outside it.
- Taken: (a).
- Licence: "such time shall not be later than a time on the ninetieth day after the date of its filing" (src:99): a time on the ninetieth day is allowed.
- Where: `s 103(d) the instrument may become effective on the specified later date`.

**F15. s 103(c)(4): the limits "within 5 business days" and "within 4 hours".**
- Readings: each limit is (a) inclusive of its last day or hour, or (b) exclusive; "business days" is (c) a count the person states, or (d) computed from a calendar of public holidays.
- Taken: (a) and (c); the text does not define a business day, and a calendar is not among the inputs.
- Licence: "upon delivery of a replacement instrument ... within 5 business days after notice of such suspension" (src:94).
- Where: `s 103(c) Route to the filing date`; `s 103(c)(3) the filing date of the instrument`.

**F16. s 102(b)(7): who is an "officer".**
- Readings: (a) any officer; (b) only a person deemed to have consented to service of process on the registered agent under 10 Del. C. § 3114(b), as the last part of paragraph (b)(7) says.
- Taken: (b); an officer who is not so deemed to have consented is not within the paragraph, and the rule answers `NOTHING`.
- Licence: "All references in this paragraph (b)(7) to an officer shall mean only a person who at the time of an act or omission as to which liability is asserted is deemed to have consented to service by the delivery of process to the registered agent of the corporation pursuant to § 3114(b) of Title 10" (src:67).
- Where: `s 102(b)(7) the provision may eliminate or limit the person's personal liability`.

**F17. s 102(b)(7)(v): "an officer in any action by or in the right of the corporation".**
- Readings: the carve-out reaches (a) officers only, or (b) directors and officers.
- Taken: (a); a director sued by or in the right of the corporation can still be protected by a provision.
- Licence: sub-paragraphs (i) and (ii) and (iv) say "a director or officer", (iii) says "a director" and (v) says "an officer" (src:58-63).
- Where: `s 102(b)(7) the provision may eliminate or limit the person's personal liability`.

**F18. s 102(d): the sentence defining "facts".**
- Readings: the sentence "The term 'facts,' as used in this subsection, includes, but is not limited to, the occurrence of any event, including a determination or action by any person or body, including the corporation" is (a) a definition to be encoded, or (b) an illustration left inert.
- Taken: (a), as a non-exhaustive list; a matter of another kind answers `NOTHING`.
- Licence: "includes, but is not limited to" (src:69); the keel's note recommends `inert` for the sentence, which the brief's list of inert reasons does not allow.
- Where: `s 102(d) the matter is a fact on which a provision may depend`.

**F19. s 114(b) and (c): provisions named by part.**
- Readings: when a list names "109(b) (last sentence)" or "102(a)(4)", the match is (a) by the label at the level the list names it, or (b) by the whole section.
- Taken: (a): a list that names the whole section names every part of it; a list that names a part names only that part.
- Licence: the lists in subsections (b) and (c) mix whole sections ("141") and parts ("109(b) (last sentence)", "102(a)(4)", "157(e)") (src:201-202, 206).
- Where: `s 114 the listed provision names the asked provision`; `s 114(b) and (c) subsection (a) does not apply to the provision`.

**F20. s 110(a): "a majority of the directors present" when no quorum can be convened.**
- Readings: (a) more than half of the directors present; (b) more than half of the whole board.
- Taken: (a).
- Licence: "or, if a quorum cannot be readily convened for a meeting, by a majority of the directors present" (src:146): the base is those present.
- Where: `s 110(a) the emergency bylaws were validly adopted`.

**F21. s 110(i): notice of a change to a declared dividend.**
- Readings: notice "as promptly as practicable thereafter (and in any event before the record date theretofore in effect)" is (a) given before that record date, so a notice given on it is too late, or (b) given by that date.
- Taken: (a); "as promptly as practicable" is a fact the person states.
- Licence: "(and in any event before the record date theretofore in effect)" (src:157).
- Where: `s 110(i) the corporation has given notice of the change in time`.

**F22. s 102(a)(4): "to the extent desired".**
- Readings: the statement of rights of a class or series and the grant of authority to the board are (a) required only if the incorporators desire to fix them in the certificate, or (b) always required.
- Taken: (a).
- Licence: "the fixing of which by the certificate of incorporation is desired" and "as it may then be desired to grant" (src:45).
- Where: `s 102(a)(4) the certificate sets forth the authorized stock`.

**F23. s 103(i)(1): the fee for an affidavit of extraordinary condition.**
- Readings: "No fee shall be paid to the Secretary of State for receiving an affidavit of extraordinary condition" means (a) the receiving of the affidavit is free and the instrument's own taxes and fees are still due, or (b) everything is free.
- Taken: (a): the instrument's taxes and fees are tendered with it under limbs a. and b., and the rule for the affidavit returns 0.
- Licence: "Together with the actual delivery of an instrument and tender of the required taxes and fees, there is delivered ... a separate affidavit" (src:105); "No fee shall be paid ... for receiving an affidavit" (src:108).
- Where: `s 103(i)(1) the fee payable to the Secretary of State for receiving an affidavit of extraordinary condition`.

**F24. s 115(a): a provision that prohibits, or that neither requires nor prohibits.**
- Readings: for a provision of the certificate or bylaws that (a) prohibits bringing internal corporate claims in the courts of this State, the text answers no; (b) requires the claims to be brought only in those courts, the text answers yes if consistent with jurisdictional requirements; (c) does neither, the text does not speak.
- Taken: as listed; a provision that both requires and prohibits is answered by the prohibition (no).
- Licence: "may require, consistent with applicable jurisdictional requirements, that any or all internal corporate claims shall be brought solely and exclusively in any or all of the courts in this State, and no provision of the certificate of incorporation or the bylaws may prohibit bringing such claims in the courts of this State" (src:216).
- Where: `s 115(a) the provision of the certificate of incorporation or the bylaws is permitted`.

**F25. s 106: "subject to § 103(d)".**
- Readings: a later effective date in the certificate (a) postpones the incorporators' becoming a body corporate to that date, or (b) leaves it at the filing date.
- Taken: (a).
- Licence: "shall, from the date of such filing, be and constitute a body corporate, by the name set forth in the certificate, subject to § 103(d) of this title" (src:126); section 103(d) makes an instrument effective at its stated later time.
- Where: `s 106 the date from which the incorporators are a body corporate`.

**F26. s 102(e): the four persons who may reserve a name.**
- Readings: the list in paragraphs (1) to (4) is (a) exhaustive, or (b) an example.
- Taken: (a): any other person answers `NOTHING`.
- Licence: "The exclusive right to the use of a name that is available ... may be reserved by or on behalf of:" followed by the four paragraphs (src:70-74); the text uses "including" where it means an example.
- Where: `s 102(e) the exclusive right to use the name may be reserved by or on behalf of the person`.

**F27. s 103(h): a manual signature.**
- Readings: the three forms named (facsimile, conformed, electronic transmission of a signature) are (a) additions to the ordinary signature, or (b) the only forms.
- Taken: (a): a manual signature is the ordinary meaning of "signed" in subsection (a); another form answers `NOTHING`.
- Licence: subsection (a) says "signed" without qualification (src:81-86); subsection (h) says what "signed" may include (src:103).
- Where: `s 103(h) the form of signature is permitted on an instrument authorized to be filed`.

**F28. s 102(b)(4): a "larger portion" of the stock.**
- Readings: a requirement is larger than the Law's when (a) it is a larger proportion of the same base, or (b) it is also larger when the bases differ.
- Taken: (a); where the Law's requirement is "more than" a proportion, a certificate that asks for exactly that proportion is not larger; different bases answer `NOTHING`.
- Licence: "larger portion of the stock or of any class or series thereof, or of any other securities having voting power, or a larger number of the directors, than is required by this chapter" (src:55): "a larger portion" has a base.
- Where: `s 102(b)(4) the certificate of incorporation requires a larger portion of the stock or other securities having voting power than this chapter requires`.

**F29. s 113(b): "any record date" that precedes the bylaw's adoption.**
- Readings: a bylaw adopted on the record date itself (a) applies to that election, or (b) does not.
- Taken: (a): a record date that falls on the day of adoption does not precede it.
- Licence: "No bylaw so adopted shall apply to elections for which any record date precedes its adoption" (src:191).
- Where: `s 113(b) the bylaw applies to the election`.

**F30. s 108(a): "a majority of the incorporators or directors".**
- Readings: the base is (a) all the incorporators, or all the directors named in the certificate (the whole board), or (b) those who attend.
- Taken: (a): more than half of all of them; a sole incorporator or director is the majority.
- Licence: "at the call of a majority of the incorporators or directors, as the case may be" (src:134): the call precedes the meeting, so there is nobody who "attends".
- Where: `s 108(a) the call of the organization meeting is made by a majority of the incorporators or directors`.

**F31. s 102(b)(3) and s 102(b)(5): the named date.**
- Readings: (a) a right "in existence on July 3, 1967" includes one that arose on that day, and the duration "specified" in the certificate includes its last day; (b) neither does.
- Taken: (a) for both: a right arising on 3 July 1967 is preserved; a corporation whose certificate limits its duration to a date still exists on that date and has expired on the day after.
- Licence: "All such rights in existence on July 3, 1967, shall remain in existence unaffected by this paragraph" and "duration of the corporation's existence to a specified date; otherwise, the corporation shall have perpetual existence" (src:54, 56).
- Where: `s 102(b)(3) the date on which existing preemptive rights are preserved`; `s 102(b)(5) the duration of the corporation's existence has expired`.

**F32. s 110(i): who may act when a quorum cannot be readily convened.**
- Readings: "the board of directors (or, if a quorum cannot be readily convened for a meeting, a majority of the directors present) may ..." means (a) that when no quorum can be convened only a majority of the directors present may act, or (b) that the parenthesis adds a second actor and the board's own action still counts.
- Taken: (b): with a quorum the board must act; without one, the board or a majority of the directors present may.
- Licence: the parenthesis is introduced by "or" and names a further actor for the case of no quorum; nothing in the sentence takes the power from the board (src:157).
- Found: a case written to expect (a) failed on its first run, because the rule had silently taken (b); the text does not decide between them.
- Kept: `dg1-cases-seat.l4` and a layer-1 test now assert the reading taken (b), and the first expectation is kept, failing on purpose, in `dg1-cases-seat-first-reading.l4`, which `check.sh` lists in `expected_failed` with the count 1.
- Where: `s 110(i) the action with respect to the meeting of stockholders is authorized`.

## Cross-references out of my ranges

Each provision outside the ranges is a plain input named for the fact and not for the section, with a comment `-- out of range: section N (piece X)` where the rule is in another piece of this text.
Outcomes of other chapters, other titles and federal statutes are also plain inputs; the text does not deposit them, so they have no piece.
The pieces are read from the brief's table: dg2 (sections 121 to 147), dg3 (151 to 203), dg4 (204 to 220), dg5 (221 to 246), dg9 (271 to 314), dg10 (321 to 385), dg11 (388 to 398).

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| s 102(a)(1)(i) (waiver of the name words) | § 503(i), "total assets, as defined in" | chapter 5 of Title 8, not deposited | `the total assets the certificate states, as defined in § 503(i) of this title, in dollars` |
| s 102(a)(1)(iii) (the word "trust") | § 395 | dg11 | `the use of the word trust is permitted by § 395` |
| s 102(a)(1)(iv) (the word "bank") | 12 U.S.C. § 1813 (bank and savings association); 12 U.S.C. §§ 1841 and 1461 (regulation as a holding company) | federal law | `the name is the name of a subsidiary of a bank or savings association, as those terms are defined in the Federal Deposit Insurance Act, 12 U.S.C. § 1813`; `the corporation is regulated under the Bank Holding Company Act of 1956, 12 U.S.C. § 1841 et seq., or the Home Owners' Loan Act, 12 U.S.C. § 1461 et seq.` |
| s 102(a)(2) (registered office and agent) | § 131(c), how an address is stated | dg2 | `that address is stated in accordance with § 131(c)` |
| s 102(a)(4) (authorized stock) | § 151, the rights, preferences and limitations that may be fixed | dg3 | `the incorporators desire to fix by the certificate the designations, powers, preferences and rights, and qualifications, limitations or restrictions, permitted by § 151 for a class or series` |
| s 102(b)(2) (who may apply for a meeting) | §§ 291 and 279, the appointment of a receiver or trustee | dg9 | `the receiver or trustee was appointed for this corporation under § 291 or § 279` |
| s 102(b)(7) (the five excepted liabilities) | § 174, liability of directors for unlawful payment of dividend or unlawful stock purchase or redemption | dg3 | `the liability is under § 174 of this title` |
| s 102(b)(7) ("director" includes a person who exercises the board's powers) | § 141(a), a provision of the certificate that confers the board's powers on another person | dg2 | the constructor `as a person who, pursuant to a provision of the certificate of incorporation in accordance with § 141(a), exercises or performs powers or duties otherwise conferred or imposed upon the board of directors` of `s 102(b)(7) Capacity` |
| s 102(b)(7) ("officer" means a person deemed to have consented to service) | 10 Del. C. § 3114(b) | Title 10, not deposited | `the officer was at the time of the act or omission deemed to have consented to service by the delivery of process to the registered agent of the corporation pursuant to § 3114(b) of Title 10` |
| s 102(e) (the fee) | § 391, the amounts payable to the Secretary of State | dg11 | `the amount payable under § 391 for the filing, in dollars` |
| s 103(c)(6) (the county assessment fee) | § 391(a)(5)b. (a certificate of dissolution); subchapter XVI (a foreign corporation's documents) | dg11; dg10 | `the instrument is a certificate of dissolution qualifying for treatment under § 391(a)(5)b.`; `the instrument is a document filed in accordance with subchapter XVI` |
| s 103(c)(7) (the courthouse municipality fee) | § 136 (resignation of an agent without a successor); § 391(a)(5)b.; subchapter XVI | dg2; dg11; dg10 | `the instrument is a resignation of agent without appointment of a successor under § 136`; the two inputs above |
| s 103(c)(7) (the municipality) | 10 Del. C. § 301, the municipality designated in each county | Title 10, not deposited | `the municipality designated in § 301 of Title 10 in the county in which the corporation's registered office in this State is, or is to be, located` |
| s 103(j) (documents filed on or after 1 August 2011) | § 131(c), how a registered office address is stated | dg2 | `the certificate or other document changes the address of a registered office`; and, for a new document, `that address is stated in accordance with § 131(c)` |
| s 110(i)(i)(1) (the record date of a postponed meeting) | § 213, how a record date is fixed | dg4 | `the record date fixed for the meeting before it was postponed` |
| s 110(i) (the stocklist) | § 219, the stocklist made available | dg4 | `it was not practicable to allow inspection of the stocklist during the emergency condition` |
| s 110(i)(i)(2) (notice by SEC filing) | §§ 13(a) and 15(d) of the Securities Exchange Act of 1934 | federal law | `the corporation is subject to the reporting requirements of § 13(a) or § 15(d) of the Securities Exchange Act of 1934` |
| s 114(d)(1) (a charitable nonstock corporation) | § 501(c)(3) of the Internal Revenue Code | federal law | `the corporation is exempt from taxation under § 501(c)(3) of the United States Internal Revenue Code, or any successor provisions` |
| s 114(b)(1), (b)(2) (lists of sections) | §§ 503 and 502(a)(5), sections that the lists name | chapter 5 of Title 8, not deposited | none: the numbers are data in the lists |
| s 115(b)(ii) (a section that confers jurisdiction) | any section of the title other than § 111 that confers jurisdiction on the Court of Chancery | whichever piece holds it | `another section of this title confers jurisdiction upon the Court of Chancery as to the claim` |
| s 111(a) (exclusive jurisdiction elsewhere) | any statute that confers exclusive jurisdiction on another court, agency or tribunal | outside the deposited text | `a statute confers exclusive jurisdiction on a court, agency or tribunal other than the Court of Chancery` |
| s 116(a)(3) (delivery of a stockholder's proxy or consent) | § 212(c)(2) and (3); § 228(d)(1), the additional requirements | dg4; dg5 | `the additional requirements of § 212(c)(2) and (3) or § 228(d)(1) are met` |
| s 116(a)(1) ("electronic transmission") | § 232(d)(1), the definition of "Electronic transmission" | dg5 | the constructor `an electronic transmission` of `s 116(a)(1) Medium` |
| s 116(a) (last sentence) | Chapter 12A of Title 6, the Uniform Electronic Transactions Act | Title 6, not deposited | `the parts of the transaction governed by this chapter are documented, signed and delivered in accordance with this subsection or otherwise in accordance with this chapter` |
| s 116(c) (federal override) | 15 U.S.C. § 7001 et seq., including § 7002(a)(2) | federal law | `controlling is permitted by § 7002(a)(2) of that Act` |
| s 101(c) (public utilities) | Title 26 | Title 26, not deposited | `s 101(c) the corporation is subject also to the special provisions and requirements of Title 26` is derived from the fact that the corporation operates within this State; the content of Title 26 is not encoded |
| s 110(a) (override of other law) | Chapters 3 and 5 of Title 26 and Chapter 7 of Title 5 | Titles 26 and 5, not deposited | none: the text itself says the emergency bylaws operate "notwithstanding" them, so no input is needed |
| s 108(c) (consent in writing) | § 116, documented, signed and delivered | this piece | none: section 116 is in this piece; section 108(c) takes its outcome as the fact that the consent was in writing or by electronic transmission |
| s 102(f), s 109(b) (internal corporate claims) | § 115(b) | this piece | none: the rule `s 115(b) the claim is an internal corporate claim` is called |

## Needs from the core

Nothing the core lacks stopped the encoding: every shared type and rule this piece uses is the core's (`Kind of corporation`, `Kind of entity`, `Vote requirement`, `Vote base`, `a majority of`, `at least`, `the vote carries`, `period in days`, and the kind tests).
The following would improve the merge, and each is recorded here, not decided:

1. **A time of day.**
   The text speaks of "the date and time" of delivery, filing and effect (sections 103(c)(3), 103(c)(4), 103(d), 108(c)).
   The core has a date (`YMD`) and no time of day, so this piece carries dates only and answers `NOTHING` where a question turns on the time within one date (Fork register, F6).
   A shared date-and-time type would let those cases answer, and would serve any piece whose text counts hours or fixes a rule by the time of an event.
2. **A convention for "business days".**
   The text uses "business days" (sections 103(c)(4), 103(i)(1)) without defining it; this piece takes the count as an input.
   A shared definition (or a shared calendar input) would let every piece that uses the term treat it alike.
3. **The decision of the kind of corporation.**
   The core names four kinds of corporation (`Kind of corporation`) and every piece takes the kind as an input.
   Section 114(d) is the text's rule for which kind a corporation is, from four facts; it is encoded here as `s 114(d) the kind of the corporation`, in `dg1-s114-nonstock.l4`.
   The lead may promote it to the core, or leave it here for the pieces to take as an input.
4. **The reading rule of section 114(a).**
   `s 114(a) how the reference in the provision is read` reads "stockholder" as "member" (and the board as the governing body, and stock as memberships) for a nonstock corporation, except for the provisions that subsections (b) and (c) list.
   Any piece whose text speaks of stockholders or the board could ask this rule; it is encoded once here and not repeated.
5. **The definition of an internal corporate claim.**
   `s 115(b) the claim is an internal corporate claim` is called by sections 102(f) and 109(b) in this piece; any piece that mentions an internal corporate claim could call it, if the merge keeps the name.

Local types: every type declared in the ten layer-1 modules has a name that begins with the section locator (`s 109(a) Holder of the power over the bylaws`), and the seat declares one, `How the filing date of my instrument is set`; none collides with the core or with another file of this piece (`inputs/work/dupnames.py`).
The constructors of those types are named in the text's own words; a check for a name defined in two of this piece's files, or in a file and the core, is described in `## What the stable binary does not accept` (it found six constructor names that collided and renamed them).

## What the text turns out to say

These are the places where reading the text closely turned up something a reader of the English would likely miss.
Each is stated from the text, with the question or rule where a case asserts it; "Asserted." closes a finding only where an assertion in `dg1-cases-seat.l4` or a `dg1-tests-*.l4` file states it.
No assertion in this piece is expected to fail, so there is no file of deliberately failing expectations.

1. **Section 101(a) does not say a limited liability company, a statutory trust, a real estate investment trust or a common-law trust may incorporate.**
   The words are "person, partnership, association or corporation", and the Law's own definition of "person" nearby (section 203) is for that section only.
   The encoding returns `NOTHING` for those four, and `JUST TRUE` for a natural person and for a corporation (question `May I incorporate a Delaware corporation`).
   Asserted.

2. **The five exceptions to a section 102(b)(7) provision do not reach the same people.**
   Exceptions (i), (ii) and (iv) name a director or officer, exception (iii) names a director only, and exception (v) names an officer only.
   So an officer who is within the paragraph can be protected even for a section 174 liability, a director sued by or in the right of the corporation can be protected, and an officer in the same action cannot (question `May the certificate eliminate or limit my personal liability for this breach`).
   Asserted.

3. **"Officer" in section 102(b)(7) means only a person deemed to have consented to service under 10 Del. C. § 3114(b).**
   An officer who has not so consented is outside the paragraph: the answer is `NOTHING`, not "not protected".
   Asserted.

4. **A section 102(b)(7) provision cannot protect an act or omission before the date it takes effect, and a later amendment, repeal or elimination does not change its application to an earlier act.**
   An act on 31 December 2025 under a provision effective 1 January 2026 is not protected; an act on 1 January 2026 is (questions `May the certificate eliminate or limit my personal liability for this breach` and `Does the exculpation provision as it stood at the time of my act still protect me`).
   Asserted.

5. **The proviso on the word "bank" in section 102(a)(1)(iv) requires two findings together.**
   The Division must find the context clearly not banking and also not otherwise likely to mislead the public or lead to a pattern and practice of abuse; one without the other is not enough (question `May my corporation's name contain the word bank`).
   Asserted.

6. **The waiver of the name words in section 102(a)(1)(i) has a hard threshold and a veto.**
   A certificate of total assets of $10,000,000 supports a waiver and $9,999,999 does not; the Division may not waive where it determines that the name is or might appear to be a natural person's; the second ground (a nonprofit nonstock corporation that is an association of professionals) is in the Division's sole discretion and is open only to a nonprofit nonstock corporation (question `Does my corporation's name contain a word the Law requires`, and `s 102(a)(1)(i) the name satisfies the requirement as to words`).
   Asserted.

7. **Section 102(a)(4) says nonstock corporations "shall have members", but the want of members affects neither an act's validity nor the corporation's existence.**
   Where the certificate and the bylaws give no criteria, the members are those entitled to vote for the governing body (questions `Am I a member of this nonstock corporation`, `Is an act of my nonstock corporation still valid although it has no members`).
   Asserted.

8. **The vote that binds under section 102(b)(2) is "a majority in number representing three fourths in value", and the text does not say of whom the majority is.**
   3 of 5 persons representing 75 of 100 in value, with the court's sanction, binds; 74 of 100 does not (question `Is the compromise or arrangement binding on me`).
   Asserted.

9. **A preemptive right exists only if the certificate expressly grants it or it existed on 3 July 1967.**
   A right that arose on 3 July 1967 is preserved; one that arose on 4 July 1967 is not (question `Do I have a preemptive right to subscribe to the corporation's new stock`).
   Asserted.

10. **The ban on fee-shifting in sections 102(f) and 109(b) is wider than internal corporate claims.**
    It also covers "any other claim that a stockholder, acting in its capacity as a stockholder or in the right of the corporation, has brought"; the only fee provision left open to the certificate or the bylaws is one that touches neither kind of claim (questions `May the certificate make a stockholder liable for fees or expenses in a claim`, `May the bylaws make me liable for fees or expenses in a claim`).
    Asserted.

11. **A name reserved under section 102(e) on 1 January 2026 is reserved through 1 May 2026, and one renewal runs through 29 August 2026.**
    A renewal filed on the last day of the reservation is in time and one filed the next day is not (questions `Through what date does my name reservation last`, `Does my application for renewal renew the reservation`).
    Asserted.

12. **Alternatives b. and c. of section 103(a)(2) are open only where "it appears from the instrument" that there are no officers (b.), or no officers or directors (c.).**
    A majority of the directors signing an instrument that does not show that there are no officers does not satisfy the section (question `Has this instrument been signed as the Law requires for the corporation`).
    Asserted.

13. **A replacement of an instrument held in suspension keeps the original delivery date only if delivered within 5 business days of the notice.**
    On the sixth business day the filing date is the date of the replacement (question `Under section 103(c), what is my instrument's filing date`).
    Asserted.

14. **A three-page instrument costs the counties $24 + 2 x $9 = $42 and the courthouse municipality $40; a certificate of dissolution that qualifies under section 391(a)(5)b. pays neither.**
    The fees are the text's figures; the other amounts payable are section 391's and are inputs (questions `What county assessment fee must I tender with my instrument`, `What courthouse municipality fee must I tender with my instrument`).
    Asserted.

15. **An instrument may be made effective on a later date up to and including the ninetieth day after its filing.**
    Filed 1 January 2026, the last permitted day is 1 April 2026.
    Whether an effective time on the filing date itself is "subsequent" depends on the time of day, which this piece does not carry, so it answers `NOTHING` (question `May my instrument say that it becomes effective on a later date`).
    Asserted.

16. **A correction is effective from the original filing date, but against persons substantially and adversely affected only from the correction's own filing date.**
    The text says "the filing date" in the second limb without saying whose (Fork register, F7) (question `From what date is a corrected or nullified instrument effective as against me`).
    Asserted.

17. **Section 103(g) protects the Secretary of State from liability only for the acts it lists; for any other act the text is silent.**
    Filing and indexing give `JUST FALSE`; any other act gives `NOTHING` (question `Can I hold the Secretary of State liable for this act`).
    Asserted.

18. **An affidavit of extraordinary condition under section 103(i) is received for no fee, but the earlier filing date needs the affidavit (a.) or the Secretary of State's waiver (b.), and the Secretary of State's three determinations (c.).**
    The determinations are that an extraordinary condition existed, that the earlier effort failed because of it, and that actual delivery was made within a reasonable period, not more than 2 business days, after the condition ended: delivery after 3 business days does not qualify (questions `May the Secretary of State give my instrument the earlier filing date`, and `What fee must I pay for the Secretary of State's receiving my affidavit of extraordinary condition`).
    Asserted.

19. **A document filed before 1 August 2011 need not be amended to comply with section 131(c); the text says nothing about a document filed on or after that date that does not change the registered office address.**
    The first answers `JUST FALSE` (the corporation need not amend) and the second `NOTHING` (questions `Must my corporation amend an old document to comply with section 131(c)`, `Must a new document that changes the registered office address comply with section 131(c)`).
    Asserted.

20. **A corporation exists from the date of filing of its certificate, "subject to § 103(d)": a later effective date postpones existence.**
    Filed 10 March 2026 with a stated effective date of 1 April 2026, it does not exist on 20 March and exists on 1 April (question `Does my corporation exist on this day`).
    Asserted.

21. **The incorporators manage the corporation only if the initial directors were not named in the certificate, and then only until directors are elected.**
    (question `As an incorporator, do I manage the corporation's affairs now`).
    Asserted.

22. **Section 108 counts days as calendar days and the last day is inside.**
    Notice given on 10 March 2026 supports a meeting on 12 March but not on 11 March; a consent that takes effect on the 60th day after the instruction (2 March 2026, from 1 January) is in time and 3 March is not (questions `Is the notice I was given of the organization meeting enough`, `Is my consent given for a future time deemed given at that time`).
    Asserted.

23. **The power over the bylaws moves to the stockholders on the first payment for stock, and conferring it on the directors does not take it from them.**
    Before payment the board holds it for a stock corporation; the certificate may confer it on the directors afterwards, without divesting the stockholders (questions `Do I have the power to adopt, amend or repeal the bylaws`, `Does giving the directors the power to amend the bylaws take that power away from the stockholders`).
    Asserted.

24. **The protection of section 110(d) for acting in accordance with emergency bylaws does not extend to wilful misconduct, and it covers an officer, director or employee only.**
    A stockholder who acted under the emergency bylaws gets `NOTHING` (question `Am I protected from liability for acting in accordance with the emergency bylaws`).
    Asserted.

25. **In an emergency condition the board may move a declared dividend's payment date to no more than 60 days after the record date as changed, and must give notice before the record date theretofore in effect.**
    Record date moved to 1 May: 30 June is allowed and 1 July is not; a notice given on the old record date is too late (questions `May the board move the record date and payment date of a declared dividend later`, `Has the corporation given notice of the change in time`).
    Asserted.

26. **Section 111(a) has an exception for exclusive jurisdiction elsewhere and reaches "determine the validity"; section 111(b) has neither.**
    A matter on which a statute gives exclusive jurisdiction to another body is answered `JUST FALSE` under 111(a); 111(b) takes no such fact (questions `May I bring my civil action about this instrument or provision in the Court of Chancery`, `May I bring my action to interpret, apply or enforce a provision of the Law in the Court of Chancery`).
    Asserted.

27. **A bylaw adopted on the record date applies to the election.**
    The text says no bylaw applies to an election for which "any record date precedes its adoption"; a record date on the same day does not precede it (question `Does the reimbursement bylaw apply to this election`).
    Asserted.

28. **Section 220 is in none of the lists of section 114, so a nonstock corporation reads "stockholders" there as "members"; section 141 is in the list of (b)(1) and is read as written; section 217 is in (c)(2), which excludes it for a nonprofit nonstock corporation only.**
    (questions `In this section, how is a reference read for my nonstock corporation`, `Does section 114(a)'s reading not apply to this provision`).
    Asserted.

29. **Section 115(a) forbids a provision that prohibits bringing internal corporate claims in the courts of this State, and permits one that requires them to be brought only there if consistent with jurisdictional requirements.**
    A provision that does neither is not addressed by the subsection (question `Is this forum provision for internal corporate claims permitted`).
    Asserted.

30. **Delivery of an electronic transmission under section 116(a)(3) needs no one's awareness, and an electronic acknowledgement proves receipt but not that the content received is the content sent.**
    (questions `Does delivery of an electronic transmission depend on anyone's being aware of its receipt`, `Does an electronic acknowledgement prove that the transmission was received`, `Does an electronic acknowledgement by itself prove that the content received is the content sent`).
    Asserted.

31. **Section 116(b) lists six kinds of document to which subsection (a) does not apply (paragraph (5) is repealed), and the exclusions create no presumption about the lawful means to document, sign or deliver.**
    A ballot to vote at a meeting of stockholders is excluded; any other document is included (question `Do the electronic document and signature rules apply to this document`).
    Asserted.

32. **The Law does not say whether a vote counted against a different base is a "larger portion".**
    The encoding compares proportions only against the same base, so a certificate that asks for two thirds of the votes cast, against the Law's majority of the outstanding stock entitled to vote, answers `NOTHING`; the same base with a larger proportion answers `JUST TRUE`, the same proportion `JUST FALSE`, and "at least one half" is not larger than "more than one half".
    This is asserted by the layer-1 tests of `s 102(b)(4) the certificate of incorporation requires a larger portion of the stock or other securities having voting power than this chapter requires` in `dg1-tests-s102b-optional-provisions.l4`; the seat's question `May the certificate require a larger vote than this Law requires` takes one base for both and cannot ask it.
    Asserted.

33. **Section 110(i) does not say whether, when a quorum cannot be readily convened, the board's own action still counts.**
    The parenthesis "(or, if a quorum cannot be readily convened for a meeting, a majority of the directors present)" names a second actor for that case and does not say the board loses its power.
    The first version of a case written for this piece expected that only a majority of the directors present could act; it failed on its first run, because the rule had taken the other reading without saying so.
    The text does not decide between the two readings, so the reading taken (the board's action still counts) is recorded as fork F32, and the case and a layer-1 test assert that reading, marked as a fork.
    The first expectation is kept, as the brief says to keep an expectation meant to fail, in its own file `dg1-cases-seat-first-reading.l4` (one assertion, listed in `check.sh` `expected_failed` with the count 1); it is the only assertion in this piece that fails, and the `TOTAL` row of `check.sh` counts it.
    (question `May the board act on the stockholders' meeting during an emergency condition`).
    Asserted.

## What the stable binary does not accept

The binary is the stable `l4` 1.6.98 in the `main` dialect.
The first group is what the binary rejected while this piece was written (loud: an error, so the mistake was fixed at once); the exact error texts were not kept, so each item names the construct and what was written instead.
The second group is what the binary accepted although the brief forbids it (silent: exit code 0 and no diagnostic), and how it was found.
The third is what the brief lists as unaccepted and this piece avoided without testing.

Loud, hit while writing:

- `LENGTH` of a list is not defined in the stable prelude; `count` is.
- `DECIDE ... IF` with `GIVETH A MAYBE BOOLEAN` is rejected; a rule that answers `MAYBE BOOLEAN` is written `DECIDE ... IS` and returns `JUST` or `NOTHING` (every seat question that answers `NOTHING` is written that way).
- A rule that is written as a mixfix head (the name read around its parameters) must list its parameters in the same order in the head and in `GIVEN`; reordering one without the other is an error.
- A `LIST` whose elements are themselves built with `OF` needs each element in parentheses.
- Records are built with `WITH` (a field, `IS`, an expression, one per line); positional `OF` is used only in tests, where a reader checks the order by comment.
- `srcrefs.py` takes one locator per `(src:...)`; a citation such as `(src:51, 53)` or `(src:58-64, 66-67)` is rejected, so each run of lines has its own `(src:...)`.

Silent, found by a script and not by the binary:

- **The same constructor name defined in two modules is accepted.**
  `check.sh` printed `0 errors` while six constructor names were defined twice: `the incorporators` (in the core's `Vote base` and in `s 109(a) Holder of the power over the bylaws`), `electing directors` (in `s 107 Act of the incorporators` and in `s 108(a) Purpose of the organization meeting`), and `a manual signature`, `a facsimile signature`, `a conformed signature` and `another form of signature` (in `s 103(h) Form of signature` and in `s 116(a)(2) Form of signature`).
  Every assertion passed, so the binary evidently resolved each use by the type of the argument; the brief forbids defining a name twice because "a name defined in two imported modules cannot be used at all", and a use that the type does not fix would fail after the merge.
  They were found by `inputs/work/dupnames.py`, which lists every name (type, rule, constructor, question) defined in more than one `dg*.l4` file; it now reports 592 names and none defined twice.
  The renamed constructors are `the incorporators as holders of the power to adopt, amend or repeal bylaws`, `electing directors while the incorporators manage the corporation`, and the four signature forms with `on an instrument to be filed` after them (section 103(h) only).
- **Same-typed arguments in the wrong order are accepted.**
  A `GIVEN` with several `BOOLEAN` facts takes them in the order written; transposing two compiles and runs.
  The seat builds each record by binding every field to a named seat parameter (`field IS parameter`) and not by position, so a transposition would have to be a wrong binding; a mutation check on those bindings is described in `## Before this is worth relying on`.
  In the cases file, which calls the questions positionally, the order of arguments is checked against the listing of each question's parameters (`inputs/work/seat-questions.txt`), and asymmetric facts are used wherever two arguments have the same type.

Listed in the brief as unaccepted, and avoided here without being tested: `REFUSE`, `#ASSERT REFUSED` and `BECAUSE`; `TYPICALLY` on a record field; `SET OF`; `EVERY`; an unparenthesised `NOT`; an `#ASSERT` over more than one line; a section-level `GIVEN`; `WAIT UNTIL` (spelled `WAITUNTIL`).
`YMD` is not in the stable prelude; it comes from `dg-core.l4`, which every file here imports.
`l4 check` only typechecks and `l4 run` also evaluates the assertions, so `check.sh` runs `l4 run` and counts the diagnostics; the exit code is not used.

## What check.sh prints

The command, run in the deposit folder with the stable binary and the target that skips the comparison with a second binary, was `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`.
It exited 0 and printed exactly this:

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
dg-core.l4                                     0         0       0        0         0
dg1-cases-seat-first-reading.l4                1         0       1        0         1
dg1-cases-seat.l4                              0       507       0        0         0
dg1-s101-formation.l4                          0         0       0        0         0
dg1-s102a-required-contents.l4                 0         0       0        0         0
dg1-s102b-optional-provisions.l4               0         0       0        0         0
dg1-s102e-name-reservation.l4                  0         0       0        0         0
dg1-s103-filing.l4                             0         0       0        0         0
dg1-s108-organization.l4                       0         0       0        0         0
dg1-s109-bylaws-and-emergency-powers.l4        0         0       0        0         0
dg1-s111-s115-jurisdiction-and-forum.l4        0         0       0        0         0
dg1-s114-nonstock.l4                           0         0       0        0         0
dg1-s116-documents.l4                          0         0       0        0         0
dg1-seat.l4                                    0         0       0        0         0
dg1-tests-s101-formation.l4                    0        57       0        0         0
dg1-tests-s102a-required-contents.l4           0       103       0        0         0
dg1-tests-s102b-optional-provisions.l4         0        97       0        0         0
dg1-tests-s102e-name-reservation.l4            0        41       0        0         0
dg1-tests-s103-filing.l4                       0       168       0        0         0
dg1-tests-s108-organization.l4                 0        55       0        0         0
dg1-tests-s109-bylaws-and-emergency-powers.l4       0       127       0        0         0
dg1-tests-s111-s115-jurisdiction-and-forum.l4       0        35       0        0         0
dg1-tests-s114-nonstock.l4                     0        94       0        0         0
dg1-tests-s116-documents.l4                    0        48       0        0         0
TOTAL (24 modules)                             1      1332       1        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

The `TOTAL` row shows 1 error and 1 failed.
Both come from `dg1-cases-seat-first-reading.l4`, whose single assertion is meant to fail (F32); `check.sh` lists it in `expected_failed` with the count 1 (the `expected` column), and so exits 0.
Every other module has 0 errors, 0 failed and 0 refused.

The other gates, run on the same files:

- `python3 -I srcrefs.py check --refs <the raw text> dg1-*.l4 dg-core.l4` printed `srcrefs check: 416 src: lines, 235 runs, 299 locators, 0 problems`.
- `l4 check` on every `dg1-*.l4` file, filtered for `DiagnosticSeverity_Warning`, `DiagnosticSeverity_Error`, an unknown annotation, or text after code on a line, printed nothing.
- `inputs/work/dupnames.py` printed `592 names; 0 defined in more than one file`.
- Assertions written (`grep -c '^#ASSERT'`) against assertions satisfied, per file: the ten test files have 57, 103, 97, 41, 168, 55, 127, 35, 94 and 48 of each, and `dg1-cases-seat.l4` has 507 of each; 1332 written and 1332 satisfied in all; `dg1-cases-seat-first-reading.l4` has 1 written and 0 satisfied, which is its purpose.

## Before this is worth relying on

These are the things a reader should settle before relying on this encoding.

1. **The text is not the official text.**
   It is a converter's plain-text rendering of the Delaware Code Online (through 85 Del. Laws, c. 550).
   `srcrefs.py` checks that every quotation is in that file; it cannot check that the file is the statute.
   Nothing here is verified against the official text.

2. **One author wrote the rules, the seat and the expectations, and no one else has tested them.**
   The brief gives this piece no independent test pass.
   Each expected value was written from the text before the code was run, and a failing assertion was treated as a finding.
   The first run of the original 403 seat cases passed all 403, which shows the expectations and the code agree, and may show only that one reader wrote both.
   The 104 cases added afterwards (one fact varied at a time) produced one failure, and it was a fork nobody had flagged (F32); that first expectation is kept, failing on purpose, in `dg1-cases-seat-first-reading.l4`, so that the `TOTAL` row of `check.sh` shows 1 error and 1 failed, both from that file, with exit status 0.
   An independent reader should check the forks first, then the seat's cases against the text.

3. **The forks are readings, and some of them change answers.**
   A lawyer should decide F1 (which entities may incorporate), F3 (the proviso on "bank"), F8 (who holds the power over bylaws after payment for stock), F9 (whether section 111 "confers jurisdiction" for section 115), F16 and F17 (who is an "officer" and whom exception (v) reaches in section 102(b)(7)), F20 and F32 (section 110, no quorum) before this is used to advise anyone.
   Every one is recorded with the readings seen, and each is carried by one rule, so a different reading is a change in one place.

4. **Where the text does not decide, the answer is `NOTHING`, and that is asserted.**
   The cases that return `NOTHING` are not errors: a limited liability company under section 101(a), an officer not deemed to have consented under section 102(b)(7), a form of signature outside sections 103(h) and 116(a)(2), an act of the Secretary of State outside section 103(g), a transaction outside section 116(c), and every question that turns on the time of day within one date.

5. **What the person is asked and the Law is not.**
   The time of day is not carried (F6).
   "Business days" is an input (F15).
   Every judgment of an official (a waiver, a finding that a name is available, the court's sanction, the Secretary of State's determinations) is an input the person states.
   The outcomes of other provisions, other titles and federal statutes are inputs, listed in `## Cross-references out of my ranges`.

6. **How well the cases pin the seat down.**
   The seat builds each record by binding every field to one named input, and calls the layer-1 rules with the remaining inputs by position, so the risk is a wrong binding or a transposition of two inputs of the same type.
   Two checks were run on the final files.
   The first is a mutation check on the seat's record bindings: swap the bindings of two fields of one record (267 swaps over 30 records, the harness and results in `inputs/work/mutation/`), run `dg1-cases-seat.l4` against each, and count a swap as caught if an assertion fails or the file stops compiling.
   Against the first 403 cases, 28 swaps were rejected by the typechecker (the two fields have different types), 142 were killed by a case, and 97 survived.
   The 104 cases added afterwards killed 18 of the 97: the name words (a name with words of like import), the proviso on "bank", the rights and the grant to the board in the authorized stock, signing for the corporation by designated directors or holders, the seal of an acknowledgment, a filed instrument that is only defectively executed, and a certificate of correction that nullifies.
   The other 79 are swaps between two operands of one AND chain or one OR chain of the rule that reads the record, so the rule gives the same answer whichever way the inputs are bound and no case can tell the swap from the original.
   I decided that by reading each rule, and not with a tool; 53 of the 79 were re-run against the final 507 cases and still survive, and the other 26, all swaps inside AND chains (the notice of cancellation, the route of an unavailable incorporator, the filing steps, a certificate of termination, a corrected instrument, the affidavit of extraordinary condition and the Secretary of State's determinations), were not re-run.
   The second is a static check on the positional calls: for each question, list the pairs of inputs of the same type that no case gives different values (`inputs/work/pairs.py`), since a transposition of such a pair would pass every case.
   With the first 403 cases there were 80 such pairs in 33 questions; with the final 507 there is one: the second and third inputs of `By signing alone, do I affirm under penalties of perjury that the facts stated are true` (a signer acknowledged it; before a person authorized to take acknowledgments), which are two conjuncts of one AND in `s 103(b)(1) the formal acknowledgment has been made`, so swapping them changes nothing.
   The mutation check covers the bindings of record fields only; the calls into layer-1 rules are covered by this static check and by the cases.

7. **Names.**
   `inputs/work/dupnames.py` reports that no name (type, rule, constructor or question) is defined in two files of this piece or in a file and the core: 592 names, none defined twice.
   It found six constructor names that collided, which the binary had accepted without a diagnostic (`## What the stable binary does not accept`).
   Fifteen question names that carried no distinctive noun were given an "Under section ..." prefix so that they stay specific after the merge.

8. **One seat.**
   This layer asks the questions of the individual who incorporates, directs or holds stock.
   The corporation, a creditor, a registered agent and an official have no seat of their own, by the brief.
   A seat for the corporation (what it must file, send and give) would draw on the same layer-1 rules and is not written.
