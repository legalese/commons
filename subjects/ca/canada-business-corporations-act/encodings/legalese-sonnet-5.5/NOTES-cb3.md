# NOTES -- the Canada Business Corporations Act (R.S.C. 1985, c. C-44), piece cb3: Parts XI to XIV.1

Written by the piece agent cb3, 2026-10-22, from the English text in `../../registers/source-bundle/R.S.C.-1985-c.-C-44.txt` (lines 1550-2095).
The text is a plain-text rendering, made by a converter script, of the Department of Justice Canada consolidation current to 2026-09-30 (last amended 2026-03-26), English version only.
It is not the official text, it is not marked up, and nothing here has been verified against the official text.
The French version, equally authoritative, was not read.
Contains information licensed under the Open Government Licence - Canada.
`src:N` in this folder means line N of that text file.

Target compiler: `main`, build 1.6.98 (`1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44ad...263e`), the only binary run; `JL4_LIBRARY_PATH` unset.
Nothing in this folder is a legal opinion or has been read against the Act by a lawyer: status `draft`.

What is encoded: every provision of ss 126 to 172.1 (Part XI insider trading, Part XII shareholders, Part XIII proxies, Part XIV financial disclosure, Part XIV.1 diversity).
Layer 1 is the law, objectively, in the modules `cb3-part*.l4` (and `cb3-nouns.l4`), each rule named `<what it decides> within s N` and cited with `@ref` and a `src:` locator.
Layer 2 is the seat layer `cb3-seat.l4`, with its cases `cb3-cases-seat.l4`.
Tests of layer 1 are `cb3-tests-*.l4`; expected values were written from the text.
The keel's modules `cbca-core*.l4` are used as they are, unchanged.

Dates: the range holds no enactment, assent or commencement provision and no commencement rule, so no date is carried as a value and nothing depends on one.

Design choices that apply everywhere (each is also a decision in PROGRESS.md):
- A duty is encoded as a decision, not as a state machine: whether it arises, by when, and whether it was met. The stable binary's `check.sh` counts assertions and a `#TRACE` moves no count.
- Every "prescribed" thing (a period, a number, a form, a class of corporation) is a plain input: the regulations are not among the sources. Where the shape of the prescribed period is not known (before or after an event, one limit or two) the input is a yes-or-no "within the prescribed period".
- A court's or the Director's discretion ("as it thinks fit", "if satisfied") is never decided. The rule decides who may apply and on what ground; the order itself is the official's.
- Hours, business days and trading days are not in the core's `Unit of time`: the cut-off or average is a plain input (see "Needs from the core").

## Seat

The seat is one person who incorporates, directs or holds shares in a corporation under the Canada Business Corporations Act: an incorporator, a director or officer, or a shareholder, including a minority shareholder.
Asked from that position: what the Act lets them do, what it requires of them, what they may require of the corporation, and what can be done to them.
Why: the Act governs a corporation and the people around it, and Commons asks every text from the position of the individual to whom the law applies (CLAUDE.md of Commons, ruled 2026-10-18).
Parts XI to XIV.1 are about the individual as insider, shareholder at a meeting, proposer, requisitioner, proxy-giver, or director and officer; there is no seat for the court, the Director or the auditor, whose powers appear only as what they mean for the person.

The seat layer is `cb3-seat.l4` and its cases are `cb3-cases-seat.l4`.
It has 299 questions in 28 groups under one `§` heading and 28 `§§` headings, in the order of the text, and 687 hand-written cases.
Every question has `@ref`, `@export` and, on each plain input, `@desc` worded as that person would be asked; every question is answered by one call, or a few calls, of the layer-1 rules, and no rule is restated.
Where the text states a duty with an offence, the layer asks it in a set: whether the duty arises ("Must ...?"), whether it was met ("Have I ...?"), whether failing it is an offence ("Am I guilty ...?") and the two ceilings ("What is the most I can be fined ...?", "What is the longest imprisonment ..., in months?").
Where the text gives the person a claim, the other party's side is a plain input (what the corporation or the intermediary did or failed to do), as the brief asks, and the paired question asks what is owed by the person.
There is no seat for the court, the Director, an intermediary or the auditor: their powers and duties appear as what the person is owed, may ask for, or is exposed to.

Assumptions made in the layer, each assumed and not ruled by anyone:
- Every "prescribed" thing is a plain input of the question (a period, a form, a percentage, a class of corporation), because the regulations are not a source.
- A value that may be absent (a date or a number that "may" exist) is asked as a yes-or-no flag and a value, and rebuilt inside the question as a `MAYBE`.
- A legal conclusion the person cannot state is not asked for: the question calls the layer-1 rule that decides it, with the same inputs. For example `Must management send me a form of proxy` asks for the corporation's class and the number of voting shareholders, and calls the s 149(2) exception inside.
- The first input of `insider within s 126(1)` (the term is used in section 131) is fixed `FALSE` in the s 126 question, because section 131 has its own definition and its own question.
- Questions about a court or the Director ask whether the person may apply, or whether the official may do a kind of thing; they never say what the official will do.
- A penalty ceiling is a ceiling and not a sentence: the fine ceiling is a NUMBER and the imprisonment ceiling is a `MAYBE NUMBER`, which is `NOTHING` where the text states a fine only (asserted for ss 149(3), 159(2) and 160(3)).
- The 22 questions that take no input (the penalty ceilings) carry their description in `@export` and have no `@desc`, which describes an input; the form of an annotation was checked in the skill's table (`@export` publishes with a description, a bare `@desc` is internal only).
- The appointment of an auditor (s 162(1)) counts the votes at a meeting only. A resolution in writing signed by every voting shareholder is as valid as one passed at a meeting under s 142(1)(a), and is asked about there (finding 56).

Cases: every question has at least one case, each written from the text before any output was seen, except that two expectations were wrong and were corrected from the text after a failing run: the reimbursement under s 143(6) (finding 26) and the unanimous written resolution under s 162(1) (finding 56); there are 303 negative assertions, and 11 cases assert `NOTHING` (for example `What is the record date if the directors fix none` for voting, `How many votes does each share carry`, and `Is what I did a solicitation of proxies` for an act in none of the lists).
The case file ends with 687 assertions, written equal to the 687 that `check.sh` reports satisfied.

The questions, by group, in the text's order:

### Who is an insider, and what the Act counts as mine (ss 126 and 131)

- Am I an insider of a distributing corporation (s 126(1))?
- Am I an officer for the purposes of Part XI (s 126(1))?
- Is what I hold a share for the purposes of Part XI (s 126(1))?
- Am I deemed an insider because my body corporate holds a large block of voting shares (s 126(2)(a))?
- Am I deemed an insider of the holding corporation because I run its subsidiary (s 126(2)(b))?
- How many shares am I deemed to own beneficially (s 126(2)(c))?
- How many shares is my body corporate deemed to own beneficially (s 126(2)(d))?
- Is my acquisition or disposition of an option treated as a change in my beneficial ownership (s 126(2)(e))?

### Selling short, puts and calls (s 130)

- Am I barred from selling a security short (s 130(1))?
- Am I barred from selling a call or buying a put (s 130(2))?
- Does the exception for owners of a convertible security or option apply to my sale (s 130(3))?
- Am I guilty of an offence for a short sale, call or put (s 130(4))?
- What is the most I can be fined for a short sale, call or put (s 130(4))?
- What is the longest imprisonment I can face for a short sale, call or put, in months (s 130(4))?

### Insiders under section 131, and trading or tipping on confidential information (s 131)

- Am I an insider of the corporation for section 131 (s 131(1))?
- Does section 131 treat what I hold or traded as a security of the corporation (s 131(2))?
- Am I deemed an insider because I propose a take-over bid or a business combination (s 131(3))?
- Am I an insider because I am connected to a person who proposes a take-over bid or a business combination (s 131(3.1))?
- Am I an insider of the corporation with respect to the confidential information (s 131(1), (3) and (3.1))?
- Must I compensate the person I traded with because I traded on confidential information (s 131(4))?
- Am I owed compensation by an insider who traded with me on confidential information (s 131(4))?
- Am I accountable to the corporation for the benefit I got from my trade (s 131(5))?
- Is an insider who traded accountable to my corporation for the benefit they got (s 131(5))?
- Must I compensate someone because I disclosed confidential information (s 131(6))?
- Am I owed compensation because an insider disclosed confidential information that led to my trade (s 131(6))?
- Am I accountable to the corporation for the benefit I got from disclosing confidential information (s 131(7))?
- Is an insider who disclosed confidential information accountable to my corporation (s 131(7))?
- Must the court compare my price with the market price after disclosure (s 131(8))?
- As a purchaser, what amount must the court consider (s 131(8)(a))?
- As a seller, what amount must the court consider (s 131(8)(b))?
- If several insiders are liable to me, is each liable for the whole (s 131(9))?
- By when must I start my action under section 131 (s 131(10))?
- May I still start my action under section 131 (s 131(10))?

### Where and how a shareholders' meeting is held (s 132)

- Is the place of the meeting lawful (s 132(1))?
- May the meeting be held outside Canada (s 132(2))?
- Am I taken to have agreed to a meeting held outside Canada because I attended (s 132(3))?
- May I take part in the meeting by telephone or other electronic means (s 132(4))?
- Am I treated as present at the meeting if I take part by electronic means (s 132(4))?
- May we hold the meeting entirely by electronic means (s 132(5))?

### Calling the annual meeting and special meetings (s 133)

- By when must the directors call the first annual meeting (s 133(1)(a))?
- Did the directors call the first annual meeting in time (s 133(1)(a))?
- By when must the directors call the next annual meeting (s 133(1)(b))?
- Did the directors call the next annual meeting in time (s 133(1)(b))?
- May the directors call a special meeting whenever they like (s 133(2))?
- May the corporation ask the court for more time to call the annual meeting (s 133(3))?

### Record dates and notice of a meeting (ss 134 to 136)

- May the directors fix a record date (s 134(1))?
- What is the record date if the directors fix none (s 134(2))?
- Must notice of the record date be given (s 134(3))?
- Has notice of the record date been given as the Act requires (s 134(3))?
- Am I owed notice of the meeting (s 135(1))?
- Was notice of the meeting sent in time (s 135(1) and (1.1))?
- Can the corporation leave me off the notice because I was not registered on the record date (s 135(2))?
- Do I keep my right to vote even though I did not receive notice (s 135(2))?
- Can the adjourned meeting be announced at the meeting without a fresh notice (s 135(3))?
- Must notice of the adjourned meeting be given as for an original meeting (s 135(4))?
- Does management have to send a new form of proxy for the adjourned meeting (s 135(4))?
- Is this business special business (s 135(5))?
- Does the notice of meeting say what the Act requires about the business (s 135(6))?
- May I waive notice of the meeting (s 136)?
- Does my attendance at the meeting waive notice (s 136)?

### Raising a matter at the annual meeting: shareholder proposals (s 137)

- May I submit a proposal to the shareholders (s 137(1)(a))?
- May I discuss a matter at the annual meeting (s 137(1)(b))?
- Am I eligible to submit a proposal (s 137(1.1))?
- Does my proposal carry the information the Act requires (s 137(1.2))?
- How many words of mine count toward the word limit (s 137(1.3))?
- Must I prove that I am eligible to submit a proposal (s 137(1.4))?
- Have I met my duty to prove my eligibility (s 137(1.4))?
- Is the corporation excused from circulating my proposal (s 137(5))?
- Is the corporation excused from setting out my later proposal because I stopped holding shares (s 137(5.1))?
- Must the corporation circulate my proposal in its management proxy circular (s 137(2))?
- Has the corporation done what s 137(2) requires of it for my proposal?
- Must the corporation include my supporting statement (s 137(3))?
- Has the corporation done what s 137(3) requires for my supporting statement?
- Is my proposal with its statement within the word limit (s 137(3))?
- May my proposal include nominations for directors (s 137(4))?
- Is the corporation free of liability for merely circulating a proposal (s 137(6))?
- Must the corporation tell me if it refuses to include my proposal (s 137(7))?
- Has the corporation notified me of its refusal as the Act requires (s 137(7))?
- May I ask the court for relief because the corporation refused my proposal (s 137(8))?
- May the corporation, or a person aggrieved by a proposal, ask the court to let it be omitted (s 137(9))?
- May the court let the corporation omit the proposal (s 137(9))?
- Must I give the Director notice of my court application (s 137(10))?
- Have I met my duty to notify the Director (s 137(10))?
- Is the Director entitled to appear and be heard on my application (s 137(10))?

### Lists of shareholders, quorum and voting at the meeting (ss 138 to 141)

- By when must the corporation prepare the list of shareholders entitled to receive notice (s 138(1))?
- Does the list of shareholders entitled to receive notice comply (s 138(1))?
- By when must the corporation prepare the list of shareholders entitled to vote (s 138(2) and (3))?
- Does the list of shareholders entitled to vote comply (s 138(2) and (3))?
- How many shares may I vote at the meeting (s 138(3.1))?
- May I examine the list of shareholders (s 138(4))?
- Is there a quorum of shareholders at the meeting (s 139(1))?
- May the meeting go on if people leave and the quorum is lost (s 139(2))?
- May the shareholders present adjourn the meeting if there is no quorum (s 139(3))?
- May the shareholders present transact other business if there is no quorum (s 139(3))?
- Does a lone shareholder constitute a meeting (s 139(4))?
- How many votes does each share carry (s 140(1))?
- How many votes may I cast at the meeting (s 140(1))?
- Must the corporation recognize my representative at the meeting (s 140(2))?
- May my representative exercise all my powers at the meeting (s 140(3))?
- May I vote jointly held shares if the other joint holders are absent (s 140(4))?
- Must joint holders who are both present vote as one (s 140(4))?
- Will the vote be by show of hands (s 141(1))?
- May I demand a ballot (s 141(2))?
- May the vote be held entirely by electronic means (s 141(3))?
- May I vote by electronic means from where I am (s 141(4))?

### Written resolutions and the minutes (s 142)

- Is a resolution that every voting shareholder signed as valid as one passed at a meeting (s 142(1)(a))?
- Does a written resolution satisfy the requirement to hold a meeting (s 142(1)(b))?
- Must the corporation keep a copy of the written resolution with the minutes (s 142(2))?
- Has the corporation kept a copy of the resolution as required (s 142(2))?
- Is the minutes entry proof that the resolution was carried or defeated (s 142(3))?

### Requisitioning a meeting and calling one yourself (s 143)

- May we requisition the directors to call a meeting (s 143(1))?
- Does our requisition take the form the Act requires (s 143(2))?
- Must the directors call the meeting we requisitioned (s 143(3))?
- By when must the directors call the requisitioned meeting (s 143(4))?
- May I call the meeting myself because the directors have not (s 143(4))?
- Is the meeting we called under section 143 called in the manner the Act requires (s 143(5))?
- Must the corporation reimburse my expenses for requisitioning and calling the meeting (s 143(6))?
- How much must the corporation reimburse me (s 143(6))?

### Asking the court for a meeting (s 144)

- May I ask the court to order a meeting to be called (s 144(1))?
- May the court order the meeting to be called, held and conducted (s 144(1))?
- May the court vary or dispense with the quorum at that meeting (s 144(2))?
- Is a meeting held on the court's order a valid meeting (s 144(3))?

### Disputes about the election or appointment of a director or auditor (s 145)

- May I ask the court to settle a dispute about an election or appointment of a director or auditor (s 145(1))?
- May the court make this kind of order on my application (s 145(2))?

### Agreements among shareholders (ss 145.1 and 146)

- May we agree in writing how our shares are voted (s 145.1)?
- Is our shareholders' agreement that restricts the directors valid (s 146(1))?
- Is my written declaration as sole owner treated as a unanimous shareholder agreement (s 146(2))?
- Is there a unanimous shareholder agreement (s 146(1) and (2))?
- Am I bound by the unanimous shareholder agreement as a buyer of shares (s 146(3))?
- By when must I rescind my purchase of shares that turned out to be subject to a unanimous shareholder agreement (s 146(4))?
- May I rescind my purchase because nobody told me about the unanimous shareholder agreement (s 146(4))?
- Do I take on a director's rights, powers, duties and liabilities because the agreement gives me the power to manage (s 146(5))?
- Are the directors relieved of a duty or liability that the agreement gives to the shareholders (s 146(5))?
- May shareholders who exercise a director's powers under the agreement bind themselves in advance (s 146(6))?

### What a proxy is and who is an intermediary (s 147)

- Is this document a form of proxy (s 147)?
- Is this completed form a proxy (s 147)?
- Is the person who holds my shares an intermediary (s 147)?
- Is what I did a solicitation of proxies (s 147)?
- Is this a solicitation by or on behalf of the management (s 147)?

### Appointing, executing and revoking a proxy (s 148)

- May I appoint a proxyholder to vote for me (s 148(1))?
- Is my proxy properly executed (s 148(2))?
- Is my proxy valid at this meeting (s 148(3))?
- Have I revoked my proxy (s 148(4))?
- May the directors set a deadline for depositing proxies (s 148(5))?

### Management's duty to send a form of proxy (s 149)

- Is the corporation excused from sending me a form of proxy (s 149(2))?
- Must management send me a form of proxy with the notice of the meeting (s 149(1))?
- Did management send the form of proxy as the Act requires (s 149(1))?
- Is the corporation guilty of an offence for not sending me a form of proxy (s 149(3))?
- What is the most the corporation can be fined for that (s 149(3))?
- Am I guilty of the corporation's offence under s 149(3) as a director or officer (s 149(4))?
- What is the most I can be fined as a director or officer under s 149(4)?
- What is the longest imprisonment I can face as a director or officer under s 149(4), in months?
- What is the longest imprisonment the corporation faces under s 149(3), in months?

### Circulars when soliciting proxies (ss 150 and 151)

- Have I sent the circular the Act requires before soliciting proxies (s 150(1))?
- May I solicit proxies (s 150(1), (1.1) and (1.2))?
- Have I sent the Director the copy the Act requires (s 150(2))?
- Am I guilty of an offence for soliciting proxies without the circulars (s 150(3))?
- What is the most I can be fined under s 150(3)?
- What is the longest imprisonment I can face under s 150(3), in months?
- Am I guilty of my company's offence under s 150(3) as a director or officer (s 150(4))?
- What is the most I can be fined as a director or officer under s 150(4)?
- What is the longest imprisonment I can face as a director or officer under s 150(4), in months?
- May I ask the Director to exempt me from the proxy requirements (s 151(1))?
- May the Director's exemption have retroactive effect (s 151(1))?

### Acting as a proxyholder (s 152)

- Must I attend the meeting and follow the shareholder's directions as proxyholder (s 152(1))?
- Have I done what s 152(1) requires of me as proxyholder?
- May I speak at the meeting as proxyholder (s 152(2))?
- May I vote by ballot as proxyholder (s 152(2))?
- May I vote by show of hands as proxyholder (s 152(2))?
- May the chairperson take the vote by show of hands despite the proxies (s 152(3)(a))?
- May I, as proxyholder, vote by show of hands when the chairperson allows it (s 152(3)(b))?
- Am I guilty of an offence for not following the shareholder's directions as proxyholder (s 152(4))?
- What is the most I can be fined as a proxyholder under s 152(4)?
- What is the longest imprisonment I can face as a proxyholder under s 152(4), in months?

### Shares held by an intermediary (s 153)

- May my intermediary vote my shares (s 153(1))?
- Is my intermediary barred from voting my shares without my written instructions (s 153(2))?
- Must I give an intermediary copies of my solicitation documents (s 153(3))?
- Have I done what s 153(3) requires about copies?
- Must my intermediary vote my shares as I instructed (s 153(4))?
- Has my intermediary done what s 153(4) requires?
- Must my intermediary appoint me or my nominee as proxyholder if I ask (s 153(5))?
- Does my intermediary's failure make the meeting or its decisions void (s 153(6))?
- Does section 153 give my intermediary the right to vote shares it is otherwise barred from voting (s 153(7))?
- Is my intermediary guilty of an offence for not complying with section 153 (s 153(8))?
- What is the most my intermediary can be fined under s 153(8)?
- What is the longest imprisonment my intermediary can face under s 153(8), in months?
- Am I guilty of my company's offence as a director or officer of an intermediary (s 153(9))?
- What is the most I can be fined as a director or officer of an intermediary under s 153(9)?
- What is the longest imprisonment I can face as a director or officer of an intermediary under s 153(9), in months?

### Misleading proxy documents: asking the court (s 154)

- May I ask the court to act because a proxy circular is misleading (s 154(1))?
- May the court make this kind of order (s 154(1))?
- Must I give the Director notice of my application (s 154(2))?
- Have I met my duty to notify the Director (s 154(2))?
- Is the Director entitled to appear and be heard on my application (s 154(2))?

### The annual financial statements (ss 155 to 158)

- Is the first period of the statements the one the Act requires (s 155(1)(a)(i))?
- Are the statements placed before the shareholders the ones the Act requires (s 155(1)(a))?
- Have the directors placed everything before the shareholders that s 155(1) requires?
- May the corporation ask the Director to exempt it from the financial disclosure requirements (s 156)?
- Must the corporation keep a copy of this body corporate's financial statements at its registered office (s 157(1))?
- Has the corporation kept the copy at its registered office as required (s 157(1))?
- May I examine the subsidiary statements and make extracts free of charge (s 157(2))?
- By when may the corporation ask the court to bar my examination (s 157(3))?
- May the corporation still ask the court to bar my examination (s 157(3))?
- May the court bar my examination (s 157(3))?
- Must the corporation tell me and the Director that it is applying to bar my examination (s 157(4))?
- Has the corporation notified me and the Director of its application (s 157(4))?
- May the Director and I appear and be heard on the corporation's application (s 157(4))?
- Are the statements approved and signed as the Act requires (s 158(1))?
- Is the corporation barred from issuing copies of the statements as they stand (s 158(2))?

### Copies of the financial statements for shareholders and the Director (ss 159 and 160)

- Must the corporation send me a copy of the annual financial statements (s 159(1))?
- By when must the corporation send me the documents (s 159(1))?
- Were the documents sent to me in time (s 159(1))?
- Is the corporation guilty of an offence for not sending me the documents (s 159(2))?
- What is the most the corporation can be fined under s 159(2)?
- What is the longest imprisonment under s 159(2), in months?
- Is the subsidiary corporation excused from sending the documents to the Director (s 160(2))?
- Must the corporation send the financial statements to the Director (s 160(1))?
- Were the documents sent to the Director in time for the meeting (s 160(1)(a))?
- By when must the documents reach the Director in any event (s 160(1)(b))?
- Were the documents sent to the Director in time in any event (s 160(1)(b))?
- Is the corporation guilty of an offence for not sending the documents to the Director (s 160(3))?
- What is the most the corporation can be fined under s 160(3)?
- What is the longest imprisonment under s 160(3), in months?

### Who may be the auditor (s 161)

- Is this person my business partner for the independence rule (s 161(2.1))?
- Is this person deemed not independent of the corporation (s 161(2)(b))?
- Is this person disqualified from being our auditor (s 161(1) and (2))?
- Must our auditor resign (s 161(3))?
- Has our auditor done what s 161(3) requires?
- May I ask the court to declare our auditor disqualified (s 161(4))?
- May I ask the court to exempt our auditor from disqualification (s 161(5))?
- May the court exempt our auditor from disqualification (s 161(5))?
- May the exemption have retrospective effect (s 161(5))?

### Appointing, replacing and removing the auditor (ss 162 to 167)

- Must the shareholders appoint an auditor at the annual meeting (s 162(1))?
- Has the auditor been validly appointed by ordinary resolution (s 162(1))?
- Does the auditor still hold office on this date (s 162(1))?
- Is the auditor the directors appointed under section 104 eligible for appointment by the shareholders (s 162(2))?
- Does our incumbent auditor stay on if no auditor is appointed at the meeting (s 162(3))?
- May the directors fix the auditor's remuneration (s 162(4))?
- May we decide not to have an auditor (s 163(1))?
- Is our resolution not to appoint an auditor still valid (s 163)?
- Has our auditor ceased to hold office (s 164(1))?
- When does our auditor's resignation take effect (s 164(2))?
- May the shareholders remove our auditor (s 165(1))?
- May we fill the vacancy at the meeting at which the auditor is removed (s 165(2))?
- If we do not fill the vacancy at the removal meeting, may it be filled under section 166 (s 165(2))?
- Must we, the directors, fill the vacancy in the office of auditor (s 166(1))?
- Have the directors filled the vacancy as required (s 166(1))?
- May our articles reserve the filling of an auditor vacancy to the shareholders (s 166(3))?
- By when must the directors in office call a special meeting to fill the vacancy (s 166(2))?
- Must the directors in office call a special meeting to fill the vacancy (s 166(2))?
- May I, as a shareholder, call the meeting to fill the vacancy (s 166(2))?
- When does the term of the auditor appointed to fill the vacancy end (s 166(4))?
- May the court appoint an auditor for us on my application (s 167)?

### The auditor's rights, the statements and the examination (ss 168 to 170)

- Must the corporation give the auditor notice of the shareholders' meetings and let them attend (s 168(1))?
- Does the corporation bear the cost of the auditor's attendance at the meeting (s 168(1))?
- Must the auditor attend the meeting and answer questions because I gave written notice (s 168(2))?
- Has the auditor done what s 168(2) requires?
- Have I sent the corporation its copy of my notice to the auditor (s 168(3))?
- Is the auditor guilty of an offence for not attending when I asked (s 168(4))?
- What is the most our auditor can be fined under s 168(4)?
- What is the longest imprisonment our auditor can face under s 168(4), in months?
- Is our auditor entitled to submit a written statement of reasons (s 168(5))?
- Must the corporation give reasons for replacing the auditor (s 168(5.1)(a))?
- May the proposed replacement auditor comment on the corporation's reasons (s 168(5.1)(b))?
- Must the corporation send me a copy of the statements about the auditor's replacement (s 168(6))?
- Has the corporation sent the copies as required (s 168(6))?
- May I accept appointment as the new auditor now (s 168(7) and (8))?
- By when must the retiring auditor reply to my request (s 168(8))?
- Is my appointment as auditor void because I did not first get the retiring auditor's statement (s 168(9))?
- Must our auditor examine these statements (s 169(1))?
- May our auditor rely on another auditor's report on a subsidiary's accounts (s 169(2) to (4))?
- Must I give the auditor the information or access the auditor demands (s 170(1))?
- Must we, the directors, obtain and furnish the subsidiary's information to the auditor (s 170(2))?
- Have the directors done what s 170(2) requires?
- Am I free of civil liability for what I tell the auditor in good faith (s 170(3))?

### The audit committee (s 171)

- Must our corporation have an audit committee (s 171(1))?
- May our corporation have an audit committee although it is not required to (s 171(1))?
- Is our audit committee composed as the Act requires (s 171(1))?
- May the Director authorize us to dispense with an audit committee (s 171(2))?
- May the Director permit us to dispense with an audit committee on conditions (s 171(2))?
- Did the audit committee review the statements before they were approved (s 171(3))?
- Must the audit committee give the auditor notice of its meetings and let them attend (s 171(4))?
- Must the auditor attend the audit committee's meeting if I ask (s 171(4))?
- May I call a meeting of the audit committee (s 171(5))?
- Must I notify the audit committee and the auditor of an error I found in the statements (s 171(6))?
- Have I notified the committee and the auditor as required (s 171(6))?
- Must the auditor tell each director about a material error (s 171(7))?
- Must we, the directors, act when the auditor tells us of a material error (s 171(8))?
- Have the directors done what s 171(8) requires?
- Am I guilty of an offence for knowingly not complying with s 171(6) or (8) (s 171(9))?
- What is the most I can be fined under s 171(9)?
- What is the longest imprisonment I can face under s 171(9), in months?

### Qualified privilege (s 172)

- Does the auditor's statement or report have qualified privilege (s 172)?

### Diversity information (Part XIV.1, s 172.1)

- Must we, the directors, place the diversity information before the shareholders (s 172.1(1))?
- Have the directors placed the diversity information before the shareholders as required (s 172.1(1))?
- Must the corporation give me the diversity information (s 172.1(2))?
- Was the diversity information given to me in a way the Act allows (s 172.1(2))?
- Must the corporation send the diversity information to the Director (s 172.1(3))?
- Was the diversity information sent to the Director at the same time as to the shareholders (s 172.1(3))?

## Jural relations

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | section | L4 rule |
| --- | --- | --- | --- | --- |
| a definition or counting rule (none) | none | none | s 126(1) business combination; ss 126(1) insider, officer, share (definitions) | none |
| the directors place the diversity information before the shareholders | the shareholders (claim) | the directors (duty), where the corporation is a prescribed corporation and the meeting is annual | s 172.1(1) | `cb3-part14-1-diversity.l4` `the directors must place the diversity information before the shareholders within s 172.1(1)` |
| the information goes to each shareholder who has not opted out | each shareholder who has not opted out in writing (claim) | the corporation (duty); the opted-out shareholder has a power to release the corporation | s 172.1(2) | `the corporation must provide the diversity information to a shareholder within s 172.1(2)` |
| the information goes to the Director | the Director (claim) | the corporation (duty) | s 172.1(3) | `the corporation must send the diversity information to the Director within s 172.1(3)` |
| prohibition of short sale | the market and the Crown (claim, enforced by the offence in (4); the text names no private holder) | the insider (duty) | s 130(1) | `cb3-part11-insider-trading.l4` `a short sale is prohibited within s 130(1)` |
| exception for a convertible holder | the insider (privilege to sell what they do not own) | everyone else (no-right) | s 130(3) | `the exception to a short sale applies within s 130(3)` |
| prohibition of calls and puts | the market and the Crown (claim) | the insider (duty) | s 130(2) | `selling a call or buying a put is prohibited within s 130(2)` |
| the offence and the sentence | the court (power to sentence within the ceiling) | the insider (liability) | s 130(4) | `the insider is guilty of an offence within s 130(4)`; `the penalty ceiling within s 130(4)` |
| compensation for insider trading | the seller or purchaser who traded with the insider (claim) | the insider (duty to compensate) | s 131(4) | `compensation is owed to the counterparty of the trade within s 131(4)` |
| defences (a) to (c) of s 131(4) | the insider (immunity if established) | the counterparty (disability) | s 131(4)(a)-(c) | the three `the insider establishes that ...` inputs of the same rule |
| account of benefit from insider trading | the corporation (claim) | the insider (duty to account) | s 131(5) | `the insider is accountable to the corporation within s 131(5)` |
| compensation for tipping | a person who subsequently traded with a recipient of the information (claim) | the insider who disclosed (duty to compensate) | s 131(6) | `compensation is owed to the claimant of the disclosure within s 131(6)` |
| account of benefit from tipping | the corporation (claim) | the insider (duty to account) | s 131(7) | `the insider is accountable to the corporation for the disclosure within s 131(7)` |
| assessment of damages | the court (power to choose a measure; duty to consider the two comparisons for a distributing corporation) | the insider and the claimant (liability to the court's assessment) | s 131(8) | `the court must consider the comparison with the post-disclosure price within s 131(8)`; the two amount rules |
| joint and several liability | each claimant (claim to the whole against any one liable insider) | each liable insider (duty for the whole) | s 131(9) | `liability is joint and several within s 131(9)` |
| limitation of actions | the insider (immunity after two years) | the claimant and the corporation (disability to sue) | s 131(10) | `an action may be commenced within s 131(10)` |
| the definitions and deeming rules of Part XI (none) | none | none | s 126(1), s 126(2), s 131(1), s 131(2), s 131(3), s 131(3.1) | `insider within s 126(1)` and the other `... within s 126(...)`/`s 131(...)` definition rules; they create no relation themselves |
| a meeting at a lawful place | the shareholders (claim) | the corporation, through its directors (duty) | s 132(1), (2) | `the place of the meeting complies with s 132(1)`; `a meeting may be held outside Canada within s 132(2)` |
| deemed agreement of an attending shareholder | the corporation (immunity from an objection) | the attending shareholder (disability to object) | s 132(3) | `the shareholder is deemed to have agreed to the meeting being held outside Canada within s 132(3)` |
| participation by electronic means | a person entitled to attend (privilege to participate, where the corporation makes a facility available) | the corporation (no-right to refuse a facility it has made available) | s 132(4) | `a person may participate by electronic means within s 132(4)` |
| the callers' power to hold a meeting entirely by electronic means | the directors or the shareholders who call the meeting (power) | the shareholders and others entitled to attend (liability) | s 132(5) | `the callers may determine that the meeting is held entirely by electronic means within s 132(5)` |
| calling the annual meeting | the shareholders (claim) | the directors (duty) | s 133(1) | the rules named `... within s 133(1)(a)` and `... within s 133(1)(b)` |
| calling a special meeting | the directors (power) | the corporation and the shareholders (liability) | s 133(2) | `the directors may call a special meeting at any time within s 133(2)` |
| application to extend the time to call an annual meeting | the corporation (power to apply) | the court (liability: the application will be heard) | s 133(3) | `the corporation may apply to the court to extend the time for calling an annual meeting within s 133(3)` |
| fixing a record date | the directors (power) | the shareholders (liability) | s 134(1) | `the directors may fix a record date within s 134(1)` |
| notice of a record date | the holders of the class or series affected (claim) | the corporation (duty) | s 134(3) | `notice of the record date must be given within s 134(3)`; `notice of the record date is given as s 134(3) requires within s 134(3)` |
| notice of a meeting | each shareholder entitled to vote, each director and the auditor (claim) | the corporation (duty) | s 135(1), (1.1) | `notice of the meeting is owed to a person within s 135(1)`; `the notice of the meeting was sent in time within s 135(1) and (1.1)` |
| exception for unregistered shareholders; retained vote | the corporation (immunity from the duty to send the notice); the shareholder (claim to vote though no notice was received) | the unregistered shareholder (no-right to notice); the corporation (no-right to refuse the vote) | s 135(2) | `notice need not be sent to the shareholder within s 135(2)`; `the shareholder keeps the right to vote without having received notice within s 135(2)` |
| notice of an adjourned meeting | the shareholders (claim to notice as for an original meeting, where the aggregate is thirty days or more) | the corporation (duty) | s 135(3), (4) | the rules named `... within s 135(3)` and `... within s 135(4)` |
| the content of a notice of special business | the shareholder (claim to a notice that lets a reasoned judgment be formed) | the corporation (duty) | s 135(6) | `the notice of the meeting has the content s 135(6) requires within s 135(6)` |
| waiver of notice | the shareholder or other person entitled to attend (power to waive) | the corporation (liability: its duty to give notice is discharged) | s 136 | `a person may waive notice of the meeting within s 136`; `attendance is a waiver of notice within s 136` |
| submitting a proposal | the registered holder or beneficial owner (power) | the corporation (liability: it receives the proposal) | s 137(1)(a), (1.1) | `a person may submit a proposal within s 137(1)(a)`; `the person is eligible to submit a proposal within s 137(1.1)` |
| discussing a matter at the meeting | the registered holder or beneficial owner (privilege) | the corporation and the meeting (no-right to prevent) | s 137(1)(b) | `a person may discuss a matter at the meeting within s 137(1)(b)` |
| information accompanying a proposal | the corporation (claim) | the proposer (duty) | s 137(1.2) | `the proposal is accompanied by the information s 137(1.2) requires within s 137(1.2)` |
| proof of eligibility | the corporation (power to request; claim to the proof) | the proposer (liability to the request; duty to give proof) | s 137(1.4) | `the person must provide proof of eligibility within s 137(1.4)`; `the duty to provide proof of eligibility is met within s 137(1.4)` |
| circulating the proposal | the proposer (claim) | the corporation that solicits proxies (duty) | s 137(2) | `the corporation must circulate the proposal within s 137(2)`; `the duty to circulate the proposal is met within s 137(2)` |
| the supporting statement | the proposer (claim, on request) | the corporation (duty) | s 137(3) | `the corporation must include the supporting statement within s 137(3)`; `the duty to include the supporting statement is met within s 137(3)` |
| nominations in a proposal | the signing holders (power to include nominations) | the corporation (liability) | s 137(4) | `a proposal may include nominations of directors within s 137(4)` |
| exemption from circulating | the corporation (immunity) | the proposer (disability) | s 137(5), (5.1) | `the corporation is not required to comply with s 137(2) and (3) within s 137(5)`; `the corporation is not required to set out the person's later proposal within s 137(5.1)` |
| immunity for circulating | the corporation and persons acting on its behalf (immunity) | persons who would sue by reason only of the circulating (disability) | s 137(6) | `no liability is incurred by reason only of circulating within s 137(6)` |
| notice of refusal | the proposer (claim) | the corporation (duty) | s 137(7) | `the corporation must notify the person of the refusal within s 137(7)`; `the duty to notify the person of the refusal is met within s 137(7)` |
| application to restrain the meeting | the aggrieved proposer (power to apply) | the court (liability to hear); the corporation (liability to the order) | s 137(8) | `a person may apply to the court within s 137(8)` |
| application to omit a proposal | the corporation or an aggrieved person (power to apply) | the court (liability to hear); the proposer (liability to the order) | s 137(9) | `the corporation or an aggrieved person may apply to the court within s 137(9)`; `the court may make an order on the application within s 137(9)` |
| notice to the Director; appearing | the Director (claim to notice; privilege to appear and be heard) | the applicant (duty to give notice) | s 137(10) | `the applicant must give the Director notice within s 137(10)`; `the duty to give the Director notice is met within s 137(10)`; `the Director is entitled to appear and be heard within s 137(10)` |
| the list of shareholders entitled to receive notice | the shareholders entitled to receive notice (claim) | the corporation (duty) | s 138(1) | `the list of shareholders entitled to receive notice complies with s 138(1)` |
| the list of shareholders entitled to vote | the shareholders entitled to vote (claim) | the corporation (duty) | s 138(2), (3) | `the list of shareholders entitled to vote complies with s 138(2) and (3)` |
| voting the shares shown on the list | the named shareholder (power to vote the shares shown) | the corporation and the meeting (liability) | s 138(3.1) | `the shares the shareholder may vote at the meeting within s 138(3.1)` |
| examining the list | the shareholder (privilege to examine) | the corporation (duty to allow; no-right to refuse) | s 138(4) | `a shareholder may examine the list within s 138(4)` |
| quorum and what a quorum may do | the shareholders present (power to proceed; power to adjourn) | the absent shareholders (liability) | s 139(1)-(4) | the rules named `... within s 139(1)` to `(4)` |
| one vote a share | the shareholder (claim to the votes) | the corporation (duty to count them) | s 140(1) | `the votes each share carries within s 140(1)`; `the votes a holder may cast within s 140(1)` |
| recognising a representative | the body corporate or association (claim); the authorized individual (power to exercise its powers) | the corporation (duty to recognise) | s 140(2), (3) | `the corporation must recognize the individual as the representative within s 140(2)`; `the representative may exercise all the powers of an individual shareholder within s 140(3)` |
| joint holders voting | the joint holder present (privilege to vote in the others' absence) | the other joint holders (no-right to object); those voting (duty to vote as one) | s 140(4) | `one joint holder present may vote the shares in the absence of the others within s 140(4)`; `the joint holders who vote must vote as one within s 140(4)` |
| a show of hands, and demanding a ballot | the shareholder or proxyholder entitled to vote (power to demand a ballot) | the meeting (liability) | s 141(1), (2) | `voting is by show of hands within s 141(1)`; `a ballot may be demanded within s 141(2)` |
| voting by electronic means | the shareholders and participants (privilege to vote electronically) | the corporation (duty to make the facility available where it holds the vote that way) | s 141(3), (4) | `a vote may be held entirely by electronic means within s 141(3)`; `a participant may vote by the facility within s 141(4)` |
| the written resolution | the shareholders who all sign (power to pass a resolution without a meeting) | the corporation (liability: bound by it) | s 142(1) | the two rules named `a written resolution ... within s 142(1)(a)` and `(b)` |
| keeping the resolution with the minutes | the shareholders (claim) | the corporation (duty) | s 142(2) | `the corporation must keep a copy of the resolution with the minutes within s 142(2)`; `the duty to keep a copy of the resolution is met within s 142(2)` |
| the minutes as proof | the corporation (immunity from having to prove the count) | the person disputing the declaration (disability, absent contrary evidence) | s 142(3) | `the minutes entry is proof of the declaration within s 142(3)` |
| requisitioning a meeting | the holders of not less than five per cent (power) | the directors (liability) | s 143(1), (2) | `holders may requisition the directors to call a meeting within s 143(1)`; `the requisition complies with s 143(2)` |
| calling the requisitioned meeting | the requisitioners (claim) | the directors (duty), unless excused | s 143(3) | `the directors must call the meeting within s 143(3)` |
| calling the meeting themselves | the shareholder who signed (power) | the corporation (liability) | s 143(4) | `a shareholder who signed may call the meeting within s 143(4)` |
| reimbursement | the shareholders (claim) | the corporation (duty) | s 143(6) | `the corporation must reimburse the shareholders' expenses within s 143(6)`; `the amount to reimburse within s 143(6)` |
| applying for a court meeting; the court's order | the director, the voting shareholder, the Director (power to apply); the court (power to order) | the corporation (liability to the order) | s 144(1), (2) | `a person may apply to the court for a meeting within s 144(1)`; `the court may order a meeting to be called, held and conducted within s 144(1)`; `the court may vary or dispense with the quorum within s 144(2)` |
| the court-called meeting is valid | everyone relying on its acts (immunity from challenge) | those who would challenge it (disability) | s 144(3) | `the meeting is for all purposes a meeting duly called, held and conducted within s 144(3)` |
| applying about an election; the court's orders | the corporation, a shareholder, a director (power to apply); the court (power) | the challenged director or auditor and the corporation (liability) | s 145(1), (2) | `a person may apply to the court to determine a controversy within s 145(1)`; `the court may make an order of a kind within s 145(2)` |
| the pooling agreement | the parties (power to bind their votes) | each party (liability to be bound) | s 145.1 | `an agreement may bind the shares to be voted as provided within s 145.1` |
| the unanimous shareholder agreement | the parties (power to restrict the directors) | the directors (liability: their powers are restricted) | s 146(1), (2) | `the agreement is valid within s 146(1)`; `the declaration is deemed to be a unanimous shareholder agreement within s 146(2)` |
| the purchaser or transferee | the purchaser or transferee (power to rescind; deemed party) | the transferor and the corporation (liability to rescission) | s 146(3), (4) | `the purchaser or transferee is deemed to be a party within s 146(3)`; `the purchaser or transferee may rescind the transaction within s 146(4)` |
| the shift of directors' rights and duties | the party given the power (power; and the liabilities that go with it) | the directors (relieved: immunity to that extent) | s 146(5) | `the party has the right, power, duty or liability of a director within s 146(5)`; `the directors are relieved of the right, power, duty or liability within s 146(5)` |
| fettering discretion | the shareholders (privilege) | none | s 146(6) | `shareholders may fetter their discretion within s 146(6)` |
| appointing a proxyholder | the shareholder entitled to vote (power) | the corporation and the meeting (liability to recognise the proxyholder) | s 148(1), (2), (3) | `a shareholder may appoint a proxyholder within s 148(1)`; `the proxy is executed as s 148(2) requires within s 148(2)`; `the proxy is valid at the meeting within s 148(3)` |
| revoking a proxy | the shareholder (power) | the proxyholder (liability) | s 148(4) | `the proxy is revoked within s 148(4)` |
| the deposit time | the directors (power to specify the time) | the shareholders and proxyholders (liability to deposit by it) | s 148(5) | `the directors may specify the time for depositing proxies within s 148(5)` |
| sending a form of proxy | each shareholder entitled to receive notice (claim) | the management (duty) | s 149(1), (2) | `management must send a form of proxy within s 149(1)`; `management is not required to send a form of proxy within s 149(2)` |
| the offences of ss 149, 150, 152, 153 | the Crown (claim to obedience; power to prosecute) | the corporation, the person soliciting, the proxyholder, the intermediary, and the director or officer who knowingly authorized, permitted or acquiesced (liability) | s 149(3), (4); s 150(3), (4); s 152(4); s 153(8), (9) | the rules named `... is guilty of an offence within s N(k)` and `the penalty ceiling within s N(k)` |
| the circular | the auditor, each shareholder whose proxy is solicited, each director, and for a dissident's circular the corporation (claim) | the person soliciting (duty) | s 150(1) | `the circular required by s 150(1) is sent within s 150(1)` |
| soliciting without a dissident's circular | the person soliciting other than the management (privilege) | the shareholders solicited (no-right to a circular) | s 150(1.1), (1.2) | `a person may solicit proxies within s 150(1), (1.1) and (1.2)` |
| the copy to the Director | the Director (claim) | the person required to send a circular (duty) | s 150(2) | `the copy to the Director complies with s 150(2)` |
| the Director's exemption | the interested person (power to apply; immunity if exempted) | the Director (liability to the application; power to exempt) | s 151(1) | `the Director may exempt the person within s 151(1)`; `the exemption may have retroactive effect within s 151(1)` |
| the soliciting proxyholder's duty | the appointing shareholder (claim) | the proxyholder (duty) | s 152(1) | `the proxyholder must attend and comply with the directions within s 152(1)`; `the duty to attend and comply with the directions is met within s 152(1)` |
| the proxyholder's rights | the proxyholder (privileges: to speak and to vote by ballot; to vote by a show of hands save with conflicting instructions) | the meeting (no-right to refuse) | s 152(2) | the three `a proxyholder has the shareholder's right to ... within s 152(2)` rules |
| the chairperson's show of hands | the chairperson (power); the proxyholder (privilege) | the shareholders and proxyholders who might demand a ballot (liability, unless they do) | s 152(3) | `the chairperson may conduct the vote by a show of hands within s 152(3)(a)`; `a proxyholder may vote by a show of hands within s 152(3)(b)` |
| the intermediary's duties to the beneficial owner | the beneficial owner (claim to the documents, the request, the voting in accordance with instructions, and the appointment as proxyholder) | the intermediary (duty) | s 153(1), (2), (4), (5) | the rules named `... within s 153(1)`, `(2)`, `(4)`, `(5)` |
| copies for the intermediary | the intermediary (claim) | the person by or on behalf of whom a solicitation is made (duty) | s 153(3) | `the person must provide copies to the intermediary within s 153(3)`; `the duty to provide copies is met within s 153(3)` |
| no voiding of a meeting | the corporation and the meeting (immunity from being void) | those who would challenge the meeting on that ground (disability) | s 153(6) | `the failure renders a meeting or an action void within s 153(6)` |
| the restraining order | an interested person or the Director (power to apply); the court (power) | the person who sent the document and the corporation (liability) | s 154(1) | `a person may apply to the court within s 154(1)`; `the court may make an order of a kind within s 154(1)` |
| notice to the Director | the Director (claim; privilege to appear) | the applicant (duty) | s 154(2) | `the applicant must give the Director notice within s 154(2)`; `the duty to give the Director notice is met within s 154(2)`; `the Director is entitled to appear and be heard within s 154(2)` |
| placing the statements before the shareholders | the shareholders (claim) | the directors (duty) | s 155(1) | `the directors have complied with s 155(1) within s 155(1)`; `the statements placed are as s 155(1)(a) requires within s 155(1)(a)`; `the first period of the statements is as s 155(1)(a)(i) requires within s 155(1)(a)(i)` |
| omitting the preceding year's statements | the directors and the corporation (privilege, if the reason is set out) | the shareholders (no-right to the omitted statements) | s 155(2) | the last disjunct of `the statements placed are as s 155(1)(a) requires within s 155(1)(a)` |
| exemption from the requirements | the corporation (power to apply); the Director (power to exempt) | the shareholders and the public (liability to the loss of the disclosure) | s 156 | `the Director may exempt the corporation within s 156` |
| keeping subsidiaries' statements | the shareholders (claim) | the corporation (duty) | s 157(1) | `the corporation must keep a copy of the statements within s 157(1)`; `the duty to keep a copy at the registered office is met within s 157(1)` |
| examining them | the shareholder and the personal representative (privilege to examine and to make extracts free) | the corporation (duty to allow; no-right to refuse unless barred) | s 157(2) | `a shareholder may examine the statements and make extracts free of charge within s 157(2)` |
| barring the examination | the corporation (power to apply); the court (power to bar) | the person asking to examine (liability to be barred) | s 157(3) | `the corporation may apply to the court within s 157(3)`; `the court may bar the right to examine within s 157(3)` |
| notice of the application | the Director and the person asking (claim to notice; privilege to appear) | the corporation (duty) | s 157(4) | `the corporation must give notice of the application within s 157(4)`; `the duty to give notice of the application is met within s 157(4)`; `the Director and the person may appear and be heard within s 157(4)` |
| approval of the statements | the shareholders (claim) | the directors (duty) | s 158(1) | `the approval is evidenced as s 158(1) requires within s 158(1)` |
| the condition for issuing copies | the shareholders and the public (claim to approved, audited statements) | the corporation (duty not to issue otherwise) | s 158(2) | `the condition for issuing copies is met within s 158(2)`; `issuing copies is prohibited within s 158(2)` |
| copies to the shareholders | each shareholder who wants a copy (claim) | the corporation (duty) | s 159(1) | the three rules named `... within s 159(1)` |
| copies to the Director | the Director (claim) | the distributing corporation (duty) | s 160(1) | the rules named `... within s 160(1)(a)` and `(b)` |
| the offences of ss 159 and 160 | the Crown (claim; power to prosecute) | the corporation (liability) | s 159(2), s 160(3) | `the corporation is guilty of an offence within s 159(2)`; `... s 160(3)`; the two `the penalty ceiling` rules |
| the subsidiary exemption | the subsidiary corporation (immunity) | the Director (no-right to the subsidiary's own copy) | s 160(2) | `the subsidiary corporation is not required to comply with s 160 within s 160(2)` |
| disqualification of the auditor | the shareholders and the interested person (claim that the auditor be independent; power to apply) | the auditor (duty to resign; liability to the disqualification order) | s 161(1), (3), (4) | `a person is disqualified from being an auditor within s 161(1)`; `the auditor must resign forthwith within s 161(3)`; `an interested person may apply for a disqualification order within s 161(4)` |
| exemption from disqualification | the auditor and the interested person (power to apply; immunity if exempted) | the court (power); the shareholders (liability to the exemption) | s 161(5) | the three rules named `... within s 161(5)` |
| appointing the auditor | the corporation (claim) | the shareholders (duty) | s 162(1) | `the shareholders must appoint an auditor within s 162(1)`; `the auditor is appointed by ordinary resolution within s 162(1)` |
| the incumbent continues; remuneration | the incumbent auditor (privilege to continue); the shareholders and the directors (power to fix remuneration) | the corporation (liability) | s 162(3), (4) | `the incumbent auditor continues in office within s 162(3)`; `the directors may fix the remuneration of the auditor within s 162(4)` |
| resolving not to appoint | the shareholders of a non-distributing corporation (power) | the auditor and the Director (liability: no auditor) | s 163 | `shareholders may resolve not to appoint an auditor within s 163(1)`; `the resolution not to appoint an auditor is valid within s 163` |
| ceasing to hold office | the auditor (power to resign) | the corporation (liability) | s 164 | `the auditor ceases to hold office within s 164(1)`; `the date the resignation becomes effective within s 164(2)` |
| removing the auditor | the shareholders (power) | the auditor (liability); a court-appointed auditor (immunity from this removal) | s 165 | `the shareholders may remove the auditor within s 165(1)` |
| filling the vacancy | the corporation (claim) | the directors (duty); the shareholder (power to call, on default) | s 166 | the rules named `... within s 166(1)` and `(2)` |
| court-appointed auditor | the shareholder or the Director (power to apply); the court (power) | the corporation (liability) | s 167 | `the court may appoint an auditor and fix the remuneration within s 167` |
| the auditor's rights at meetings | the auditor (claim to notice; privilege to attend and be heard at the corporation's expense) | the corporation (duty) | s 168(1) | the two rules named `... within s 168(1)` |
| the auditor's duty to attend | the director or shareholder who gave notice (claim) | the auditor or former auditor (duty) | s 168(2), (4) | the rules named `... within s 168(2)` and `s 168(4)` |
| the auditor's statement; the corporation's statement | the auditor (privilege to submit); the replacement auditor (privilege to comment); the shareholders and the Director (claim to a copy) | the corporation (duty to make a statement and to send copies) | s 168(5), (5.1), (6) | the rules named `... within s 168(5)`, `s 168(5.1)(a)`, `(b)` and `s 168(6)` |
| accepting a replacement appointment | the retiring auditor (claim to be asked first); the shareholders (claim to the statement) | the would-be replacement (duty not to accept early); the appointment is void otherwise | s 168(7), (8), (9) | `a person may accept the appointment within s 168(7) and (8)`; `the appointment is void within s 168(9)` |
| the examination and the right to information | the auditor (claim to information and access; power to rely on another auditor) | the present and former directors, officers, employees and agents; the directors (duty) | s 169, s 170(1), (2) | the rules named `... within s 169(1)`, `s 169(2)`, `s 170(1)`, `s 170(2)` |
| the communicator's immunity | the person who communicates in good faith (immunity) | whoever would sue (disability) | s 170(3) | `the person is not liable in the civil proceeding within s 170(3)` |
| the audit committee | the shareholders (claim to a committee of the required kind); the Director (power to authorize dispensing) | the corporation described in s 102(2) (duty) | s 171(1), (2) | the rules named `... within s 171(1)` and `s 171(2)` |
| the committee's review; the auditor's attendance | the shareholders (claim to a review before approval); the committee (claim to the auditor's attendance on request) | the committee (duty to review); the auditor (duty to attend on request) | s 171(3), (4) | `the audit committee reviewed the statements before they were approved within s 171(3)`; the two rules named `... within s 171(4)` |
| errors in the statements | the committee and the auditor (claim to be told); the directors (claim to be informed); the shareholders (claim to be informed) | the director or officer (duty to notify); the auditor (duty to inform); the directors (duty to act) | s 171(6), (7), (8) | the rules named `... within s 171(6)`, `(7)` and `(8)` |
| the offences of ss 168 and 171 | the Crown (claim; power to prosecute) | the auditor or former auditor; the director or officer (liability) | s 168(4), s 171(9) | the two `is guilty of an offence` rules and their `penalty ceiling` rules |
| qualified privilege | the auditor or former auditor (immunity from defamation liability, qualified) | whoever would sue (disability) | s 172 | `the statement or report has qualified privilege within s 172` |

## Coverage table

Counts, by disposition, as of this run: 252 rows: {'inert': 5, 'encoded': 212, 'repealed or blank in this text': 7, 'fork': 28}.
One row per section, subsection or paragraph of ss 126 to 172.1, plus one row for each of the five Part headings.
Each marginal-note heading (the short title above a subsection, for example "Calling annual meetings") is the first line of the subsection it heads: it falls inside that subsection's row and is named in the row's provision cell, so no heading line is without a row.
Where the paragraphs of a subsection state different rules they have a row each; where they are limbs of one rule they are one row.
The lines of a row are `src:` lines of the raw text file; a script checked that every non-blank line from 1550 to 2095 falls inside at least one row.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| PART XI Insider Trading (Part heading) | src:1550 | inert | - | The title of Part XI, which holds ss 126 to 131; it states no rule and carries no condition, so there is nothing to encode (the rules of the Part are in the rows below, in cb3-part11-insider-trading.l4). |
| s 126(1) (heading: "Definitions"; lead-in "In this Part,") | src:1551-1552 | encoded | `cb3-part11-insider-trading.l4`, the rules named `... within s 126(1)` | "In this Part," limits the definitions to Part XI. That scope is carried by the module name and by each rule's name suffix, as in the keel for s 2(1). |
| s 126(1) "business combination" | src:1553 | encoded | `cb3-part11-insider-trading.l4` `business combination within s 126(1)` | Three alternatives; whether an acquisition is of "all or substantially all" the property is the caller's fact. |
| s 126(1) "distributing corporation" | src:1554 | repealed or blank in this text | - | The text shows "distributing corporation [Repealed, 2001, c. 14, s. 52]" (src:1554): the Part now uses the s 2(1) term, which the keel encodes as `distributing corporation within s 2(1)`. |
| s 126(1) "insider", paragraphs (a) to (d) | src:1555-1559 | encoded | `cb3-part11-insider-trading.l4` `insider within s 126(1)` | Four limbs; "except in section 131" is an input (the term is used in section 131) that switches the definition off. The s 131(1) definition is a separate rule. |
| s 126(1) "officer" | src:1560 | fork | `cb3-part11-insider-trading.l4` `officer within s 126(1)` | Fork F-126-officer: "of an entity" read as qualifying every listed office. No "appointed under section 121" limb (finding 1). |
| s 126(1) "share", paragraphs (a) and (b) | src:1561-1563 | encoded | `cb3-part11-insider-trading.l4` `share within s 126(1)` | Voting share, plus convertible security, plus exercisable option or right. |
| s 126(2) (heading and lead-in) (heading: "Further interpretation") | src:1564-1565 | encoded | `cb3-part11-insider-trading.l4`, the rules named `... within s 126(2)(a)` to `(e)` | "For the purposes of this Part," is again carried by the names. |
| s 126(2)(a) | src:1566 | encoded | `cb3-part11-insider-trading.l4` `deemed insider within s 126(2)(a)` | "More than the prescribed percentage": the percentage is an input; exactly equal is not enough (finding 10). |
| s 126(2)(b) | src:1567 | encoded | `cb3-part11-insider-trading.l4` `deemed insider within s 126(2)(b)` | Director or officer of a subsidiary is deemed an insider of the holding distributing corporation. |
| s 126(2)(c) | src:1568 | encoded | `cb3-part11-insider-trading.l4` `shares deemed beneficially owned by a person within s 126(2)(c)` | Counts the shares: the person's own plus each controlled body corporate's. |
| s 126(2)(d) | src:1569 | encoded | `cb3-part11-insider-trading.l4` `shares deemed beneficially owned by a body corporate within s 126(2)(d)` | Counts the shares: its own plus each affiliate's. |
| s 126(2)(e) | src:1570 | encoded | `cb3-part11-insider-trading.l4` `change in beneficial ownership deemed within s 126(2)(e)` | An insider's acquisition or disposition of an option or right is a deemed change in beneficial ownership. |
| s 126(3) and (4) (both repealed) | src:1571 | repealed or blank in this text | - | The text shows "(3) and (4) [Repealed, 2001, c. 14, s. 52]" (src:1571). |
| ss 127 to 129 | src:1572 | repealed or blank in this text | - | The text shows "127 to 129 [Repealed, 2001, c. 14, s. 53]" (src:1572). |
| s 130(1) (heading: "Prohibition of short sale") | src:1573-1574 | encoded | `cb3-part11-insider-trading.l4` `a short sale is prohibited within s 130(1)` | Insider, knowing sale, security of a distributing corporation or affiliate, not owned OR not fully paid for. |
| s 130(2) (heading: "Calls and puts") | src:1575-1576 | fork | `cb3-part11-insider-trading.l4` `selling a call or buying a put is prohibited within s 130(2)` | Fork F-130-2: "the corporation" read as the distributing corporation of subsection (1). |
| s 130(3) (heading and lead-in) (heading: "Exception") | src:1577-1578 | fork | `cb3-part11-insider-trading.l4` `the exception to a short sale applies within s 130(3)` | Fork F-130-3: the exception is read as reaching only an insider who does not own the security; it does not touch s 130(2) (finding 4). |
| s 130(3)(a) | src:1579 | encoded | `cb3-part11-insider-trading.l4` `the exception to a short sale applies within s 130(3)`; `done in time after the sale within s 130(3)` | Exercise of the conversion privilege, option or right and delivery to the purchaser within ten days after the sale. |
| s 130(3)(b) | src:1580 | encoded | `cb3-part11-insider-trading.l4` `the exception to a short sale applies within s 130(3)`; `done in time after the sale within s 130(3)` | Transfer of the convertible security, option or right to the purchaser within ten days after the sale. (a) and (b) are alternatives ("or"). |
| s 130(4) (heading: "Offence") | src:1581-1582 | encoded | `cb3-part11-insider-trading.l4` `the insider contravenes s 130(1) or (2) within s 130(4)`; `the insider is guilty of an offence within s 130(4)`; `the penalty ceiling within s 130(4)` | The offence, and its ceiling: fine not exceeding the greater of $1,000,000 and three times the profit, or imprisonment not exceeding six months, or both (finding 5). |
| s 131(1) (heading and lead-in) (heading: "Definitions") | src:1583-1584 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)`; `Connection of a person to a corporation under s 131(1)` | "In this section, insider means, with respect to a corporation," : the rules named `... within s 131(1)` work on one record of facts about the person's connection to the corporation. |
| s 131(1)(a) | src:1585 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(a)` | The corporation itself. |
| s 131(1)(b) | src:1586 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(b)` | An affiliate of the corporation. |
| s 131(1)(c) | src:1587 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(c)` | Director or officer of the corporation, or of a person described in (b), (d) or (f). |
| s 131(1)(d) | src:1588 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(d)` | More than the prescribed percentage of the voting rights, not counting shares held as underwriter in the course of a distribution to the public. |
| s 131(1)(e) | src:1589 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(e)` | Employed or retained by the corporation or by an (f) person, other than a person described in (f). |
| s 131(1)(f) | src:1590 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(f)` | Engages in or proposes to engage in business or professional activity with or on behalf of the corporation. |
| s 131(1)(g) | src:1591 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(g)` | Received material confidential information while a person described in (a) to (f). |
| s 131(1)(h) | src:1592 | fork | `cb3-part11-insider-trading.l4` `insider within s 131(1)(h)` | Fork F-131-1h: received it from a described person (itself possibly a (h) person) and knows or ought to have known; the giver's status is a fact, so the chain's depth is not computed. |
| s 131(1)(i) | src:1593 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(1)(i)` | A prescribed person (the regulations are not a source). |
| s 131(2) (heading: "Expanded definition of security") | src:1594-1597 | encoded | `cb3-part11-insider-trading.l4` `security of the corporation within s 131(2)` | A put, call, option or right to purchase or sell a security of the corporation, or a security of another entity whose price varies materially with the corporation's, is deemed a security of the corporation. |
| s 131(3) (heading: "Deemed insiders") | src:1598-1599 | fork | `cb3-part11-insider-trading.l4` `deemed insider within s 131(3)`; `insider with respect to the information within s 131(1), (3) and (3.1)` | Fork F-131-3: the (3) person is an insider only as to information obtained from the corporation; (3.1) persons are insiders without that limit. |
| s 131(3.1) (heading: "Deemed insiders") | src:1600-1601 | encoded | `cb3-part11-insider-trading.l4` `insider within s 131(3.1)` | (1)(b) to (i) applied to the (3) person, plus an affiliate or associate of that person. |
| s 131(4) (heading: "Insider trading — compensation to persons") | src:1602-1606 | encoded | `cb3-part11-insider-trading.l4` `trade described in s 131(4)`; `compensation is owed to the counterparty of the trade within s 131(4)` | The trade, the three defences (a) to (c) which the insider must establish. |
| s 131(5) (heading: "Insider trading — compensation to corporation") | src:1607-1608 | encoded | `cb3-part11-insider-trading.l4` `the insider is accountable to the corporation within s 131(5)` | Only defence (4)(a) defeats it (finding 2). |
| s 131(6) (heading: "Tipping — compensation to persons") | src:1609-1614 | encoded | `cb3-part11-insider-trading.l4` `disclosure described in s 131(6)`; `compensation is owed to the claimant of the disclosure within s 131(6)` | Tipping; defences (a) to (d), of which (c) is closed to a (3) or (3.1) person and (d) is open only to one (finding 6). |
| s 131(7) (heading: "Tipping — compensation to corporation") | src:1615-1616 | encoded | `cb3-part11-insider-trading.l4` `the insider is accountable to the corporation for the disclosure within s 131(7)` | Defences (6)(a), (c) and (d) only; (6)(b) does not help (finding 3). |
| s 131(8) (heading and lead-in) (heading: "Measure of damages") | src:1617-1618 | fork | `cb3-part11-insider-trading.l4` `the court must consider the comparison with the post-disclosure price within s 131(8)` | Fork F-131-8: "must consider" is a duty to take the two comparisons into account, not an award; the court may use any measure. |
| s 131(8)(a) | src:1619 | encoded | `cb3-part11-insider-trading.l4` `amount the court must consider where the plaintiff is a purchaser within s 131(8)(a)` | Price paid less the twenty-trading-day average after general disclosure; the average is an input. |
| s 131(8)(b) | src:1620 | encoded | `cb3-part11-insider-trading.l4` `amount the court must consider where the plaintiff is a seller within s 131(8)(b)` | The twenty-trading-day average less the price received. |
| s 131(9) (heading: "Liability") | src:1621-1622 | encoded | `cb3-part11-insider-trading.l4` `liability is joint and several within s 131(9)` | More than one insider liable under (4) or (6) for the same transaction or series: joint and several, or solidary. |
| s 131(10) (heading: "Limitation") | src:1623-1624 | encoded | `cb3-part11-insider-trading.l4` `the last day to commence an action within s 131(10)`; `an action may be commenced within s 131(10)` | Two years after discovery of the facts, for a right created by (4) to (7); counted by the keel's rules (fork F1 of the keel). |
| PART XII Shareholders (Part heading) | src:1626 | inert | - | The title of Part XII, which holds ss 132 to 146 (shareholders: meetings, proposals, lists, quorum, voting, requisitions, court orders and agreements); it states no rule and carries no condition. |
| s 132(1) (heading: "Place of meetings") | src:1627-1628 | encoded | `cb3-part12-meetings.l4` `the place of the meeting complies with s 132(1)` | The place provided in the by-laws; absent that, the place the directors determine; both within Canada. |
| s 132(2) (heading: "Meeting outside Canada") | src:1629-1630 | encoded | `cb3-part12-meetings.l4` `a meeting may be held outside Canada within s 132(2)` | Specified in the articles, or every shareholder entitled to vote agrees. |
| s 132(3) (heading: "Exception") | src:1631-1632 | encoded | `cb3-part12-meetings.l4` `the shareholder is deemed to have agreed to the meeting being held outside Canada within s 132(3)` | Attendance is agreement unless the shareholder attends only to object that the meeting is not lawfully held. |
| s 132(4) (heading: "Participation in meeting by electronic means") | src:1633-1634 | encoded | `cb3-part12-meetings.l4` `a person may participate by electronic means within s 132(4)`; `a person participating by electronic means is present at the meeting within s 132(4)` | A default the by-laws may displace; the facility must be made available and permit adequate communication; the regulations are an input. |
| s 132(5) (heading: "Meeting held by electronic means") | src:1635-1636 | encoded | `cb3-part12-meetings.l4` `the callers may determine that the meeting is held entirely by electronic means within s 132(5)` | Only if the by-laws so provide. |
| s 133(1) (heading: "Calling annual meetings") | src:1637-1640 | fork | `cb3-part12-meetings.l4` `the last day to call the first annual meeting within s 133(1)(a)`; `the first annual meeting is called in time within s 133(1)(a)`; `the last day to call a subsequent annual meeting within s 133(1)(b)`; `a subsequent annual meeting is called in time within s 133(1)(b)` | Fork F-133-call: the deadline is for CALLING the meeting, not holding it. Fork F-133-earlier: the two limits of (b) both apply, so the later meeting must be called by the earlier of the two days. |
| s 133(2) (heading: "Calling special meetings") | src:1641-1642 | encoded | `cb3-part12-meetings.l4` `the directors may call a special meeting at any time within s 133(2)` | A permission without a time limit or a condition; the rule decides who holds it. |
| s 133(3) (heading: "Order to delay calling of annual meeting") | src:1643-1644 | encoded | `cb3-part12-meetings.l4` `the corporation may apply to the court to extend the time for calling an annual meeting within s 133(3)` | Who may apply and for what. Whether the court makes the order is its discretion and is not decided. |
| s 134(1) (heading: "Fixing record date") | src:1645-1651 | encoded | `cb3-part12-meetings.l4` `the directors may fix a record date within s 134(1)`; `Purpose of a record date under s 134(1)` (in `cb3-nouns.l4`) | The five purposes (a) to (e) are the constructors of the enumeration; "within the prescribed period" is a yes-or-no input. |
| s 134(2) (heading and lead-in) (heading: "No record date fixed") | src:1652-1653 | fork | `cb3-part12-meetings.l4` `the record date when none is fixed within s 134(2)` | Fork F-134-vote: the text gives a default for notice (a) and for every purpose other than notice or voting (b), and none for voting; the rule returns NOTHING for voting. |
| s 134(2)(a) | src:1654-1656 | encoded | `cb3-part12-meetings.l4` `the record date for notice of a meeting when none is fixed within s 134(2)(a)` | The day before the notice is given, or the meeting day if no notice is given; "close of business" is the time of that day and is not carried. |
| s 134(2)(b) | src:1657 | encoded | `cb3-part12-meetings.l4` `the record date for a purpose other than notice or voting when none is fixed within s 134(2)(b)` | The day the directors pass the resolution relating to the purpose. |
| s 134(3) (heading: "When record date fixed") | src:1658-1661 | encoded | `cb3-part12-meetings.l4` `notice of the record date must be given within s 134(3)`; `notice of the record date is given as s 134(3) requires within s 134(3)` | Unless every holder waives in writing; the newspaper advertisement AND the written notice to each stock exchange; the prescribed period is an input. |
| s 134(4) | src:1662 | repealed or blank in this text | - | The text shows "(4) [Repealed, 2001, c. 14, s. 57]" (src:1662). |
| s 135(1) (heading: "Notice of meeting") | src:1663-1667 | encoded | `cb3-part12-meetings.l4` `notice of the meeting is owed to a person within s 135(1)`; `the notice of the meeting was sent in time within s 135(1) and (1.1)` | Owed to each shareholder entitled to vote, each director and the auditor; the prescribed period is an input. |
| s 135(1.1) (heading: "Exception — not a distributing corporation") | src:1668-1669 | encoded | `cb3-part12-meetings.l4` `the notice of the meeting was sent in time within s 135(1) and (1.1)` | A corporation that is not a distributing corporation may send the notice within a shorter period if its articles or by-laws so specify. |
| s 135(2) (heading: "Exception — shareholders not registered") | src:1670-1671 | encoded | `cb3-part12-meetings.l4` `notice need not be sent to the shareholder within s 135(2)`; `the shareholder keeps the right to vote without having received notice within s 135(2)` | An unregistered shareholder on the record date need not be sent a notice; failing to receive one does not take away the right to vote. |
| s 135(3) (heading: "Adjournment") | src:1672-1673 | fork | `cb3-part12-meetings.l4` `notice of the adjourned meeting other than by announcement is unnecessary within s 135(3)` | Fork F-135-adjourn: "adjourned for less than thirty days" is read as the aggregate of the adjournments, as in (4). |
| s 135(4) (heading: "Notice of adjourned meeting") | src:1674-1675 | fork | `cb3-part12-meetings.l4` `notice of the adjourned meeting is required as for an original meeting within s 135(4)`; `subsection 149(1) applies to the adjourned meeting within s 135(4)` | Fork F-135-adjourn: thirty days or more gives notice as for an original meeting; more than ninety (not ninety) brings in s 149(1); between thirty and ninety days s 149(1) does not apply. |
| s 135(5) (heading: "Business") | src:1676-1677 | encoded | `cb3-part12-meetings.l4` `the business is deemed to be special business within s 135(5)` | Everything at a special meeting; at an annual meeting everything but the four named items. |
| s 135(6) (heading: "Notice of business") | src:1678-1681 | encoded | `cb3-part12-meetings.l4` `the notice of the meeting has the content s 135(6) requires within s 135(6)` | The nature of the special business in sufficient detail ("sufficient" is the caller's judgment) and the text of any special resolution. |
| s 136 (heading: "Waiver of notice") | src:1682-1683 | encoded | `cb3-part12-meetings.l4` `a person may waive notice of the meeting within s 136`; `attendance is a waiver of notice within s 136` | Waiver in any manner; attendance is a waiver unless the person attends only to object that the meeting is not lawfully called. |
| s 137(1) (heading and lead-in) (heading: "Proposals") | src:1684-1685 | encoded | `cb3-part12-proposals.l4` `a person may submit a proposal within s 137(1)(a)`; `a person may discuss a matter at the meeting within s 137(1)(b)` | Registered holder or beneficial owner of shares entitled to be voted at an annual meeting; "subject to (1.1) and (1.2)" is carried by the eligibility input and by the separate (1.2) rule. |
| s 137(1)(a) | src:1686 | encoded | `cb3-part12-proposals.l4` `a person may submit a proposal within s 137(1)(a)` | The power to submit notice of a matter to be raised at the meeting (a "proposal"). |
| s 137(1)(b) | src:1687 | fork | `cb3-part12-proposals.l4` `a person may discuss a matter at the meeting within s 137(1)(b)` | Fork F-137-1b: "would have been entitled to submit a proposal" takes in the (1.1) eligibility; one input carries it. |
| s 137(1.1) (heading and lead-in) (heading: "Persons eligible to make proposals") | src:1688-1689 | encoded | `cb3-part12-proposals.l4` `the person is eligible to submit a proposal within s 137(1.1)` | Two routes, (a) or (b), joined by "or". |
| s 137(1.1)(a) | src:1690 | encoded | `cb3-part12-proposals.l4` `the person is eligible to submit a proposal within s 137(1.1)` | At least the prescribed number of outstanding shares held or owned for at least the prescribed period; the caller counts the shares held that long. |
| s 137(1.1)(b) | src:1691 | encoded | `cb3-part12-proposals.l4` `the person is eligible to submit a proposal within s 137(1.1)` | The support of persons who in the aggregate, counting the proposer or not, held or owned at least the prescribed number for at least the prescribed period. |
| s 137(1.2) (heading: "Information to be provided") | src:1692-1695 | encoded | `cb3-part12-proposals.l4` `the proposal is accompanied by the information s 137(1.2) requires within s 137(1.2)` | Name and address, and the shares held or owned with the date acquired, of the person and, if applicable, the supporters; "paragraph (1)(a)" read as every proposal (finding 13). |
| s 137(1.3) (heading: "Information not part of proposal") | src:1696-1697 | encoded | `cb3-part12-proposals.l4` `the words that count toward the prescribed maximum within s 137(1.3)` | The (1.2) information is not part of the proposal or the statement and is not counted toward the word limit; its word count is an input that is left out of the sum. |
| s 137(1.4) (heading: "Proof may be required") | src:1698-1699 | encoded | `cb3-part12-proposals.l4` `the person must provide proof of eligibility within s 137(1.4)`; `the duty to provide proof of eligibility is met within s 137(1.4)` | A request in time brings a duty to give proof in time that the (1.1) requirements are met; the periods are inputs. |
| s 137(2) (heading: "Information circular") | src:1700-1701 | fork | `cb3-part12-proposals.l4` `the corporation must circulate the proposal within s 137(2)`; `the duty to circulate the proposal is met within s 137(2)` | Fork F-137-2: the duty is read as excused by (5) and by (5.1), and as owed only for a proposal submitted by a person who may submit it. Only a corporation that solicits proxies is under it. |
| s 137(3) (heading: "Supporting statement") | src:1702-1703 | encoded | `cb3-part12-proposals.l4` `the corporation must include the supporting statement within s 137(3)`; `the duty to include the supporting statement is met within s 137(3)`; `the proposal and the statement are within the word limit within s 137(3)` | On the proposer's request; statement and proposal together not over the prescribed maximum number of words. |
| s 137(4) (heading: "Nomination for director") | src:1704-1705 | encoded | `cb3-part12-proposals.l4` `a proposal may include nominations of directors within s 137(4)` | Signed by holders of not less than five per cent of the shares, or of a class of shares, entitled to vote at the meeting; the fraction is the caller's (one for all shares, one for each class); nominations made at the meeting are not precluded (the rule does not exclude them). |
| s 137(5) (heading and lead-in) (heading: "Exemptions") | src:1706-1707 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to comply with s 137(2) and (3) within s 137(5)` | Any one of the limbs excuses the corporation from (2) and (3). |
| s 137(5)(a) | src:1708 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to comply with s 137(2) and (3) within s 137(5)` | Not submitted within the prescribed period (input). |
| s 137(5)(b) | src:1709 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to comply with s 137(2) and (3) within s 137(5)` | "It clearly appears" that the primary purpose is a personal claim or grievance (input; the judgment is the corporation's). |
| s 137(5)(b.1) | src:1710 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to comply with s 137(2) and (3) within s 137(5)` | "It clearly appears" that the proposal does not relate in a significant way to the business or affairs of the corporation (input). |
| s 137(5)(c) | src:1711 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to comply with s 137(2) and (3) within s 137(5)` | Not more than the prescribed period before receipt, the person failed to present a proposal that was included in a circular at their request (input). |
| s 137(5)(d) | src:1712 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to comply with s 137(2) and (3) within s 137(5)` | Substantially the same proposal submitted in a circular for a meeting within the prescribed period and short of the prescribed minimum support (input). |
| s 137(5)(e) | src:1713 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to comply with s 137(2) and (3) within s 137(5)` | The rights conferred are being abused to secure publicity (input). |
| s 137(5.1) (heading: "Corporation may refuse to include proposal") | src:1714-1715 | encoded | `cb3-part12-proposals.l4` `the corporation is not required to set out the person's later proposal within s 137(5.1)` | The person failed to continue to hold or own the (1.1) number of shares to the day of the meeting, and the later meeting is held within the prescribed period following it. |
| s 137(6) (heading: "Immunity") | src:1716-1717 | encoded | `cb3-part12-proposals.l4` `no liability is incurred by reason only of circulating within s 137(6)` | Immunity for circulating a proposal or statement in compliance with the section; a liability on another ground is not touched. |
| s 137(7) (heading: "Notice of refusal") | src:1718-1719 | fork | `cb3-part12-proposals.l4` `the corporation must notify the person of the refusal within s 137(7)`; `the duty to notify the person of the refusal is met within s 137(7)` | Fork F-137-7: "as the case may be" (the day of receipt of the proposal or of the proof) is folded into the one input on the period. In writing, stating the intention to omit and the reasons. |
| s 137(8) (heading: "Person may apply to court") | src:1720-1721 | encoded | `cb3-part12-proposals.l4` `a person may apply to the court within s 137(8)` | Who may apply: the person who submitted the proposal and claims to be aggrieved by the refusal under (7). The court's order is its discretion and is not decided. |
| s 137(9) (heading: "Corporation’s application to court") | src:1722-1723 | encoded | `cb3-part12-proposals.l4` `the corporation or an aggrieved person may apply to the court within s 137(9)`; `the court may make an order on the application within s 137(9)` | The corporation or any person claiming to be aggrieved by a proposal may apply; the court may make an order only if satisfied that (5) applies (finding 15). |
| s 137(10) (heading: "Director entitled to notice") | src:1724-1725 | encoded | `cb3-part12-proposals.l4` `the applicant must give the Director notice within s 137(10)`; `the duty to give the Director notice is met within s 137(10)`; `the Director is entitled to appear and be heard within s 137(10)` | An applicant under (8) or (9) gives the Director notice; the Director may appear and be heard. |
| s 138(1) (heading and lead-in) (heading: "List of shareholders entitled to receive notice") | src:1726-1727 | encoded | `cb3-part12-voting.l4` `the list of shareholders entitled to receive notice complies with s 138(1)` | An alphabetical list of the shareholders entitled to receive notice, showing the shares each holds; two inputs say so. |
| s 138(1)(a) | src:1728 | encoded | `cb3-part12-voting.l4` `the last day to prepare the list of shareholders entitled to receive notice within s 138(1)` | Record date fixed under 134(1)(c): not later than ten days after it (the keel's counting). |
| s 138(1)(b) | src:1729 | fork | `cb3-part12-voting.l4` `the list of shareholders entitled to receive notice complies with s 138(1)` | Fork F-138-1b: no record date fixed: "on the record date established under 134(2)(a)", read as that day exactly (finding 19). |
| s 138(2) (heading: "Voting list — if record date fixed") | src:1730-1731 | encoded | `cb3-part12-voting.l4` `the last day to prepare the list of shareholders entitled to vote within s 138(2) and (3)`; `the list of shareholders entitled to vote complies with s 138(2) and (3)` | A voting record date fixed under 134(1)(d): ten days after it. |
| s 138(3) (heading: "Voting list — if no record date fixed") | src:1732-1733 | fork | `cb3-part12-voting.l4` `the last day to prepare the list of shareholders entitled to vote within s 138(2) and (3)` | Fork F-138-3: "as the case may be" is read as the 134(1)(c) date if one was fixed, otherwise the 134(2)(a) date, by which (not on which) the list is prepared. |
| s 138(3.1) (heading: "Entitlement to vote") | src:1734-1735 | encoded | `cb3-part12-voting.l4` `the shares the shareholder may vote at the meeting within s 138(3.1)` | A shareholder named on the list may vote the shares shown; a shareholder not named gets NOTHING, not nought shares (finding 21). |
| s 138(4) (heading: "Examination of list") | src:1736-1739 | encoded | `cb3-part12-voting.l4` `a shareholder may examine the list within s 138(4)` | During usual business hours at the registered office or the place of the central register, or at the meeting. |
| s 139(1) (heading: "Quorum") | src:1740-1741 | fork | `cb3-part12-voting.l4` `a quorum of shareholders is present within s 139(1)` | Fork F-139-tie: a majority is more than half of the shares entitled to vote, so exactly half is not a quorum. The by-laws may otherwise provide (input). |
| s 139(2) (heading: "Opening quorum sufficient") | src:1742-1743 | encoded | `cb3-part12-voting.l4` `the shareholders present may proceed with the business within s 139(2)` | A quorum at the opening suffices for the whole meeting unless the by-laws otherwise provide. |
| s 139(3) (heading: "Adjournment") | src:1744-1745 | encoded | `cb3-part12-voting.l4` `the shareholders present may adjourn the meeting to a fixed time and place within s 139(3)`; `the shareholders present may transact other business within s 139(3)` | No quorum at the opening: adjourn, and no other business (JUST FALSE); with a quorum the subsection is silent (NOTHING; finding 20). |
| s 139(4) (heading: "One shareholder meeting") | src:1746-1747 | encoded | `cb3-part12-voting.l4` `the shareholder present constitutes a meeting within s 139(4)` | One shareholder, or one holder of a class or series, present in person or by proxy. |
| s 140(1) (heading: "Right to vote") | src:1748-1749 | encoded | `cb3-part12-voting.l4` `the votes each share carries within s 140(1)`; `the votes a holder may cast within s 140(1)` | One vote a share unless the articles otherwise provide; where they do and no figure is given, NOTHING (finding 22). |
| s 140(2) (heading: "Representative") | src:1750-1751 | encoded | `cb3-part12-voting.l4` `the corporation must recognize the individual as the representative within s 140(2)` | A body corporate or association's individual authorized by a resolution of its directors or governing body. |
| s 140(3) (heading: "Powers of representative") | src:1752-1753 | encoded | `cb3-part12-voting.l4` `the representative may exercise all the powers of an individual shareholder within s 140(3)` | The authorized individual has all the powers the body could exercise as an individual shareholder. |
| s 140(4) (heading: "Joint shareholders") | src:1754-1755 | encoded | `cb3-part12-voting.l4` `one joint holder present may vote the shares in the absence of the others within s 140(4)`; `the joint holders who vote must vote as one within s 140(4)` | Unless the by-laws otherwise provide: one present holder votes in the absence of the others; two or more who vote vote as one. |
| s 141(1) (heading: "Voting") | src:1756-1757 | encoded | `cb3-part12-voting.l4` `voting is by show of hands within s 141(1)` | A show of hands unless the by-laws otherwise provide or a shareholder or proxyholder entitled to vote demands a ballot. |
| s 141(2) (heading: "Ballot") | src:1758-1759 | encoded | `cb3-part12-voting.l4` `a ballot may be demanded within s 141(2)` | A shareholder or proxyholder, before or after any vote by show of hands; (2) carries no "entitled to vote" qualification (finding 18). |
| s 141(3) (heading: "Electronic voting") | src:1760-1761 | encoded | `cb3-part12-voting.l4` `a vote may be held entirely by electronic means within s 141(3)` | Unless the by-laws otherwise provide, in accordance with the regulations if any, if the corporation makes a facility available. |
| s 141(4) (heading: "Voting while participating electronically") | src:1762-1763 | encoded | `cb3-part12-voting.l4` `a participant may vote by the facility within s 141(4)` | A person participating under 132(4) or (5) and entitled to vote may vote by the facility, unless the by-laws otherwise provide. |
| s 142(1) (heading and lead-in) (heading: "Resolution in lieu of meeting") | src:1764-1765 | encoded | `cb3-part12-voting.l4` `a written resolution is as valid as if passed at a meeting within s 142(1)(a)`; `a written resolution satisfies the requirements relating to meetings within s 142(1)(b)` | Neither route is open where a director has submitted a statement under 110(2) or an auditor under 168(5): both are inputs of both rules. |
| s 142(1)(a) | src:1766 | encoded | `cb3-part12-voting.l4` `a written resolution is as valid as if passed at a meeting within s 142(1)(a)` | In writing, signed by all the shareholders entitled to vote on it at a meeting. |
| s 142(1)(b) | src:1767 | encoded | `cb3-part12-voting.l4` `a written resolution satisfies the requirements relating to meetings within s 142(1)(b)` | In writing, dealing with all matters required to be dealt with at a meeting, signed by all the shareholders entitled to vote at it (finding 23). |
| s 142(2) (heading: "Filing resolution") | src:1768-1769 | encoded | `cb3-part12-voting.l4` `the corporation must keep a copy of the resolution with the minutes within s 142(2)`; `the duty to keep a copy of the resolution is met within s 142(2)` | A copy of every (1) resolution is kept with the minutes of the meetings of shareholders. |
| s 142(3) (heading: "Evidence") | src:1770-1771 | encoded | `cb3-part12-voting.l4` `the minutes entry is proof of the declaration within s 142(3)` | Unless a ballot is demanded, the entry is proof of the chairperson's declaration, absent evidence to the contrary. |
| s 143(1) (heading: "Requisition of meeting") | src:1772-1773 | encoded | `cb3-part12-requisition-agreements.l4` `holders may requisition the directors to call a meeting within s 143(1)` | Not less than five per cent of the issued shares carrying the right to vote at the meeting sought; the fraction is the caller's. |
| s 143(2) (heading: "Form") | src:1774-1775 | encoded | `cb3-part12-requisition-agreements.l4` `the requisition complies with s 143(2)` | States the business, sent to each director and to the registered office; several documents of like form each signed by one or more shareholders. |
| s 143(3) (heading: "Directors calling meeting") | src:1776-1780 | fork | `cb3-part12-requisition-agreements.l4` `the directors must call the meeting within s 143(3)` | Fork F-143-3c: "paragraphs 137(5)(b) to (e)" is read to include (b.1). The three exceptions (a), (b), (c) each excuse the directors; (a) needs both the record date and the notice of it. |
| s 143(4) (heading: "Shareholder calling meeting") | src:1781-1782 | fork | `cb3-part12-requisition-agreements.l4` `the last day for the directors to call the meeting within s 143(4)`; `a shareholder who signed may call the meeting within s 143(4)` | Fork F-143-4: the shareholders' power is read as arising only where the directors were required to call by (3); twenty-one days counted by the keel's convention. |
| s 143(5) (heading: "Procedure") | src:1783-1784 | encoded | `cb3-part12-requisition-agreements.l4` `the meeting is called as s 143(5) requires within s 143(5)` | As nearly as possible in the manner in which meetings are called pursuant to the by-laws, Part XII and Part XIII; "as nearly as possible" is the caller's judgment. |
| s 143(6) (heading: "Reimbursement") | src:1785-1786 | fork | `cb3-part12-requisition-agreements.l4` `the corporation must reimburse the shareholders' expenses within s 143(6)`; `the amount to reimburse within s 143(6)` | Fork F-143-6: the duty arises on a requisition; the shareholders can resolve otherwise only at a meeting they called under (4). |
| s 144(1) (heading: "Meeting called by court") | src:1787-1791 | encoded | `cb3-part12-requisition-agreements.l4` `a person may apply to the court for a meeting within s 144(1)`; `the court may order a meeting to be called, held and conducted within s 144(1)` | A director, a shareholder entitled to vote, or the Director may apply; the three grounds (a), (b), (c); the order itself is the court's. |
| s 144(2) (heading: "Varying quorum") | src:1792-1793 | encoded | `cb3-part12-requisition-agreements.l4` `the court may vary or dispense with the quorum within s 144(2)` | The court's power at a meeting called pursuant to the section. |
| s 144(3) (heading: "Valid meeting") | src:1794-1795 | encoded | `cb3-part12-requisition-agreements.l4` `the meeting is for all purposes a meeting duly called, held and conducted within s 144(3)` | A meeting called, held and conducted pursuant to the section is for all purposes duly so. |
| s 145(1) (heading: "Court review of election") | src:1796-1797 | encoded | `cb3-part12-requisition-agreements.l4` `a person may apply to the court to determine a controversy within s 145(1)` | The corporation, a shareholder or a director; any controversy about an election or appointment of a director or auditor. |
| s 145(2) (heading: "Powers of court") | src:1798-1803 | encoded | `cb3-part12-requisition-agreements.l4` `the court may make an order of a kind within s 145(2)`; `Kind of order under s 145(2)` | The four listed kinds (a) to (d) and "any other order" are the constructors; the power arises on an application under the section. |
| s 145.1 (heading: "Pooling agreement") | src:1804-1805 | encoded | `cb3-part12-requisition-agreements.l4` `an agreement may bind the shares to be voted as provided within s 145.1` | A written agreement between two or more shareholders may provide how their shares are voted. |
| s 146(1) (heading: "Unanimous shareholder agreement") | src:1806-1807 | encoded | `cb3-part12-requisition-agreements.l4` `the agreement is valid within s 146(1)` | Written, otherwise lawful, among all the shareholders (and perhaps others), restricting the directors' powers in whole or in part. |
| s 146(2) (heading: "Declaration by single shareholder") | src:1808-1809 | encoded | `cb3-part12-requisition-agreements.l4` `the declaration is deemed to be a unanimous shareholder agreement within s 146(2)`; `there is a unanimous shareholder agreement within s 146(1) and (2)` | The sole beneficial owner's written declaration restricting the directors' powers is deemed a unanimous shareholder agreement; the second rule answers the keel's input. |
| s 146(3) (heading: "Constructive party") | src:1810-1811 | encoded | `cb3-part12-requisition-agreements.l4` `the purchaser or transferee is deemed to be a party within s 146(3)` | A purchaser or transferee of shares subject to the agreement is deemed a party. |
| s 146(4) (heading: "When no notice given") | src:1812-1813 | encoded | `cb3-part12-requisition-agreements.l4` `the last day to rescind within s 146(4)`; `the purchaser or transferee may rescind the transaction within s 146(4)` | No notice of the agreement: rescission no later than thirty days after becoming aware; s 49(8) is out of range. |
| s 146(5) (heading: "Rights of shareholder") | src:1814-1815 | encoded | `cb3-part12-requisition-agreements.l4` `the party has the right, power, duty or liability of a director within s 146(5)`; `the directors are relieved of the right, power, duty or liability within s 146(5)` | To the extent the agreement takes a power from the directors, the party given it has the directors' rights, powers, duties and liabilities (with their defences) and the directors are relieved of them, including their s 119 liabilities (finding 31). |
| s 146(6) (heading: "Discretion of shareholders") | src:1816-1817 | encoded | `cb3-part12-requisition-agreements.l4` `shareholders may fetter their discretion within s 146(6)` | Nothing in s 146 prevents shareholders from fettering their discretion when exercising the powers of directors under the agreement. |
| PART XIII Proxies (Part heading) | src:1819 | inert | - | The title of Part XIII, which holds ss 147 to 154 (proxies); it states no rule and carries no condition. |
| s 147 (heading: "Definitions"; lead-in "In this Part,") | src:1820-1821 | encoded | `cb3-part13-proxies.l4`, the rules named `... within s 147` | "In this Part," limits the definitions to Part XIII; the scope is carried by the module name and by each rule's name suffix. |
| s 147 "form of proxy" | src:1822 | encoded | `cb3-part13-proxies.l4` `form of proxy within s 147` | A written or printed form that on completion and execution (signing, in Quebec) by or on behalf of a shareholder becomes a proxy. |
| s 147 "intermediary", paragraphs (a) to (g) | src:1823-1830 | fork | `cb3-part13-proxies.l4` `intermediary within s 147` | Fork F-147-includes: the listed kinds (a) to (g) are read as intermediaries whether or not the general description fits; (g) needs both its limbs. |
| s 147 "proxy" | src:1831 | encoded | `cb3-part13-proxies.l4` `proxy within s 147` | A completed and executed (signed) form of proxy by which a shareholder appoints a proxyholder to attend and act at a meeting. |
| s 147 "registrant" | src:1832 | repealed or blank in this text | - | The text shows "registrant [Repealed, 2001, c. 14, s. 67]" (src:1832). |
| s 147 "solicit or solicitation", paragraphs (a) and (b) | src:1833-1846 | fork | `cb3-part13-proxies.l4` `act within the inclusions of solicit within s 147`; `act within the exclusions of solicit within s 147`; `solicitation within s 147` | Fork F-147-solicit: "includes" is open-ended, so an act in no limb of (a) or (b) is NOTHING; an act in (b) is not a solicitation even if it is in (a). The prescribed announcement and circumstances are inputs. |
| s 147 "solicitation by or on behalf of the management of a corporation" | src:1847 | encoded | `cb3-part13-proxies.l4` `solicitation by or on behalf of the management of a corporation within s 147` | A solicitation by any person pursuant to a resolution or instructions of, or with the acquiescence of, the directors or a committee of them. |
| s 148(1) (heading: "Appointing proxyholder") | src:1848-1849 | encoded | `cb3-part13-proxies.l4` `a shareholder may appoint a proxyholder within s 148(1)` | A shareholder entitled to vote may appoint, by a proxy, a proxyholder who need not be a shareholder: no input names the proxyholder's status. |
| s 148(2) (heading: "Execution or signing of proxy") | src:1850-1851 | encoded | `cb3-part13-proxies.l4` `the proxy is executed as s 148(2) requires within s 148(2)` | Executed (signed) by the shareholder or by a personal representative authorized in writing. |
| s 148(3) (heading: "Validity of proxy") | src:1852-1853 | encoded | `cb3-part13-proxies.l4` `the proxy is valid at the meeting within s 148(3)` | Valid only at the meeting for which it is given or an adjournment. |
| s 148(4) (heading and lead-in) (heading: "Revocation of proxy") | src:1854-1855 | encoded | `cb3-part13-proxies.l4` `the proxy is revoked within s 148(4)` | The shareholder may revoke by (a) or (b). |
| s 148(4)(a) | src:1856-1858 | encoded | `cb3-part13-proxies.l4` `the proxy is revoked within s 148(4)` | Depositing an executed instrument at the registered office up to and including the last business day before the meeting (a DATE input), or with the chairman on the day of the meeting or an adjournment. |
| s 148(4)(b) | src:1859 | encoded | `cb3-part13-proxies.l4` `the proxy is revoked within s 148(4)` | Any other manner permitted by law (a BOOLEAN input). |
| s 148(5) (heading: "Deposit of proxies") | src:1860-1861 | encoded | `cb3-part13-proxies.l4` `the directors may specify the time for depositing proxies within s 148(5)` | A time specified in the notice calling the meeting, not more than 48 hours (Saturdays and holidays excluded) before it; the hours are the caller's. |
| s 149(1) (heading: "Mandatory solicitation") | src:1862-1863 | encoded | `cb3-part13-proxies.l4` `management must send a form of proxy within s 149(1)`; `the duty to send a form of proxy is met within s 149(1)` | Concurrently with the notice, in prescribed form, to each shareholder entitled to receive notice, unless (2) applies. |
| s 149(2) (heading: "Exception") | src:1864-1867 | encoded | `cb3-part13-proxies.l4` `management is not required to send a form of proxy within s 149(2)` | Not a distributing corporation and fifty or fewer shareholders entitled to vote, joint holders counted as one. |
| s 149(3) (heading: "Offence") | src:1868-1869 | encoded | `cb3-part13-proxies.l4` `the corporation is guilty of an offence within s 149(3)`; `the penalty ceiling within s 149(3)` | Failure without reasonable cause; fine not exceeding $5,000 and no imprisonment ceiling stated (NOTHING; finding 34). |
| s 149(4) (heading: "Officers, etc., of corporations") | src:1870-1871 | encoded | `cb3-part13-proxies.l4` `a director or officer is a party to and guilty of the offence within s 149(4)`; `the penalty ceiling within s 149(4)` | Knowingly authorized, permitted or acquiesced; whether or not the corporation has been prosecuted or convicted (finding 35); $5,000 or six months or both. |
| s 150(1) (heading and lead-in) (heading: "Soliciting proxies") | src:1872-1873 | encoded | `cb3-part13-proxies.l4` `the circular required by s 150(1) is sent within s 150(1)` | A person shall not solicit proxies unless the circular for the case is sent to the auditor, each shareholder whose proxy is solicited and each director. |
| s 150(1)(a) | src:1874 | encoded | `cb3-part13-proxies.l4` `the circular required by s 150(1) is sent within s 150(1)` | For a solicitation by or on behalf of the management: a management proxy circular in prescribed form, as an appendix or a separate document accompanying the notice. |
| s 150(1)(b) | src:1875-1876 | encoded | `cb3-part13-proxies.l4` `the circular required by s 150(1) is sent within s 150(1)` | For any other solicitation: a dissident's proxy circular in prescribed form stating the purposes, and sent to the corporation too. |
| s 150(1.1) (heading: "Exception — solicitation to fifteen or fewer shareholders") | src:1877-1878 | encoded | `cb3-part13-proxies.l4` `a person may solicit proxies within s 150(1), (1.1) and (1.2)` | Not the management; fifteen or fewer shareholders whose proxies are solicited, joint holders counted as one. |
| s 150(1.2) (heading: "Exception — solicitation by public broadcast") | src:1879-1880 | encoded | `cb3-part13-proxies.l4` `a person may solicit proxies within s 150(1), (1.1) and (1.2)` | Not the management; conveyed by public broadcast, speech or publication in the prescribed circumstances. |
| s 150(2) (heading: "Copy to Director") | src:1881-1882 | encoded | `cb3-part13-proxies.l4` `the copy to the Director complies with s 150(2)` | A copy sent concurrently with a statement in prescribed form, the form of proxy, other documents and, for a management circular, the notice of the meeting. |
| s 150(3) (heading: "Offence") | src:1883-1884 | fork | `cb3-part13-proxies.l4` `a person is guilty of an offence within s 150(3)`; `the penalty ceiling within s 150(3)` | Fork F-150-3: "fails to comply with subsections (1) and (2)" is read as failing either; $5,000 or six months or both. |
| s 150(4) (heading: "Officers, etc., of bodies corporate") | src:1885-1886 | encoded | `cb3-part13-proxies.l4` `a director or officer of a body corporate is a party to and guilty of the offence within s 150(4)`; `the penalty ceiling within s 150(4)` | Knowingly authorized, permitted or acquiesced, where the body corporate commits the (3) offence; $5,000 or six months or both. |
| s 151(1) (heading: "Exemption") | src:1887-1888 | encoded | `cb3-part13-proxies.l4` `the Director may exempt the person within s 151(1)`; `the exemption may have retroactive effect within s 151(1)` | An interested person may be exempted from s 149, s 150(1) or s 153(1), on any terms, retroactively; whether the Director does is the Director's discretion and is not decided. |
| s 151(2) | src:1889 | repealed or blank in this text | - | The text shows "(2) [Repealed, 2018, c. 8, s. 18]" (src:1889). |
| s 152(1) (heading: "Attendance at meeting") | src:1890-1891 | encoded | `cb3-part13-proxies.l4` `the proxyholder must attend and comply with the directions within s 152(1)`; `the duty to attend and comply with the directions is met within s 152(1)` | A person who solicits a proxy and is appointed proxyholder attends in person or causes an alternate to attend, and complies with the appointing shareholder's directions. |
| s 152(2) (heading: "Right of a proxyholder") | src:1892-1893 | encoded | `cb3-part13-proxies.l4` `a proxyholder has the shareholder's right to speak within s 152(2)`; `a proxyholder has the shareholder's right to vote by ballot within s 152(2)`; `a proxyholder has the shareholder's right to vote by a show of hands within s 152(2)` | Speak, ballot, and a show of hands except with conflicting instructions from more than one shareholder (finding 37). |
| s 152(3) (heading: "Show of hands") | src:1894-1897 | encoded | `cb3-part13-proxies.l4` `the chairperson may conduct the vote by a show of hands within s 152(3)(a)`; `a proxyholder may vote by a show of hands within s 152(3)(b)` | On the chairperson's declaration, with the votes to be cast against under five per cent (strictly less), unless a ballot is demanded. |
| s 152(4) (heading: "Offence") | src:1898-1899 | encoded | `cb3-part13-proxies.l4` `a proxyholder is guilty of an offence within s 152(4)`; `the penalty ceiling within s 152(4)` | Failure without reasonable cause to comply with a shareholder's directions; $5,000 or six months or both. |
| s 153(1) (heading: "Duty of intermediary") | src:1900-1901 | encoded | `cb3-part13-proxies.l4` `the shares must not be voted unless s 153(1) is met within s 153(1)`; `the shares may be voted within s 153(1)` | Shares registered in the name of an intermediary or its nominee and not beneficially owned by it may be voted only if it sends the documents without delay and a request for instructions (unless it has the instructions). |
| s 153(2) (heading: "Restriction on voting") | src:1902-1903 | encoded | `cb3-part13-proxies.l4` `voting is prohibited within s 153(2)` | An intermediary, or its proxyholder, may not vote shares it does not beneficially own without the beneficial owner's written instructions; (1) and (2) are cumulative (finding 40). |
| s 153(3) (heading: "Copies") | src:1904-1905 | encoded | `cb3-part13-proxies.l4` `the person must provide copies to the intermediary within s 153(3)`; `the duty to provide copies is met within s 153(3)` | The soliciting person provides the copies on request, without delay and at their own expense. |
| s 153(4) (heading: "Instructions to intermediary") | src:1906-1907 | encoded | `cb3-part13-proxies.l4` `the intermediary must vote in accordance with the instructions within s 153(4)`; `the duty to vote in accordance with the instructions is met within s 153(4)` | Vote, or appoint a proxyholder to vote, in accordance with the written instructions received. |
| s 153(5) (heading: "Beneficial owner as proxyholder") | src:1908-1909 | encoded | `cb3-part13-proxies.l4` `the intermediary must appoint the beneficial owner or a nominee as proxyholder within s 153(5)` | On the beneficial owner's request and appropriate documentation. |
| s 153(6) (heading: "Validity") | src:1910-1911 | encoded | `cb3-part13-proxies.l4` `the failure renders a meeting or an action void within s 153(6)` | The intermediary's failure never voids a meeting or an action: the rule is FALSE (finding 38). |
| s 153(7) (heading: "Limitation") | src:1912-1913 | encoded | `cb3-part13-proxies.l4` `s 153 gives the intermediary the right to vote within s 153(7)` | JUST FALSE where the intermediary is otherwise prohibited, NOTHING otherwise (finding 38). |
| s 153(8) (heading: "Offence") | src:1914-1915 | encoded | `cb3-part13-proxies.l4` `an intermediary is guilty of an offence within s 153(8)`; `the penalty ceiling within s 153(8)` | Knowing failure to comply; $5,000 or six months or both. |
| s 153(9) (heading: "Officers, etc., of bodies corporate") | src:1916-1917 | encoded | `cb3-part13-proxies.l4` `a director or officer of an intermediary is a party to and guilty of the offence within s 153(9)`; `the penalty ceiling within s 153(9)` | Where an intermediary that is a body corporate commits the (8) offence; $5,000 or six months or both. |
| s 154(1) (heading: "Restraining order") | src:1918-1922 | encoded | `cb3-part13-proxies.l4` `a person may apply to the court within s 154(1)`; `the court may make an order of a kind within s 154(1)`; `Kind of order under s 154(1)` | An interested person or the Director may apply where a form of proxy or circular has an untrue statement or an omission of a material fact; orders (a) to (c) and any other are the constructors; the order is the court's. |
| s 154(2) (heading: "Notice to Director") | src:1923-1924 | encoded | `cb3-part13-proxies.l4` `the applicant must give the Director notice within s 154(2)`; `the duty to give the Director notice is met within s 154(2)`; `the Director is entitled to appear and be heard within s 154(2)` | An applicant gives the Director notice; the Director may appear and be heard. |
| PART XIV Financial Disclosure (Part heading) | src:1926 | inert | - | The title of Part XIV, which holds ss 155 to 172 (financial disclosure: statements, auditors, audit committee); it states no rule and carries no condition. |
| s 155(1) (heading and lead-in) (heading: "Annual financial statements") | src:1927-1928 | encoded | `cb3-part14-statements.l4` `the directors have complied with s 155(1) within s 155(1)` | The directors place the three things before the shareholders at every annual meeting. |
| s 155(1)(a) | src:1929-1931 | encoded | `cb3-part14-statements.l4` `the statements placed are as s 155(1)(a) requires within s 155(1)(a)`; `the first period of the statements is as s 155(1)(a)(i) requires within s 155(1)(a)(i)` | Prescribed comparative statements for (i) the first period (the date the period began and ended, six months counted by the keel) and (ii) the immediately preceding financial year (finding 41). |
| s 155(1)(b) | src:1932 | encoded | `cb3-part14-statements.l4` `the directors have complied with s 155(1) within s 155(1)` | The report of the auditor, if any: required only where the corporation has an auditor. |
| s 155(1)(c) | src:1933 | encoded | `cb3-part14-statements.l4` `the directors have complied with s 155(1) within s 155(1)` | Further information required by the articles, the by-laws or a unanimous shareholder agreement: required only where they require it. |
| s 155(2) (heading: "Exception") | src:1934-1935 | encoded | `cb3-part14-statements.l4` `the statements placed are as s 155(1)(a) requires within s 155(1)(a)` | The (ii) statements may be omitted if the reason is set out in the statements or a note to them. |
| s 156 (heading: "Application for exemption") | src:1936-1937 | fork | `cb3-part14-statements.l4` `the Director may exempt the corporation within s 156` | Fork F-156-public: the benefit weighed is the shareholders' for a corporation that is not distributing and the public's for one that is. The Director's discretion is not decided. |
| s 157(1) (heading: "Consolidated statements") | src:1938-1939 | encoded | `cb3-part14-statements.l4` `the corporation must keep a copy of the statements within s 157(1)`; `the duty to keep a copy at the registered office is met within s 157(1)` | A copy of the statements of each subsidiary and each body corporate whose accounts are consolidated, kept at the registered office. |
| s 157(2) (heading: "Examination") | src:1940-1941 | encoded | `cb3-part14-statements.l4` `a shareholder may examine the statements and make extracts free of charge within s 157(2)` | A shareholder or a personal representative, on request, during the usual business hours, unless the court has barred the right. |
| s 157(3) (heading: "Barring examination") | src:1942-1943 | encoded | `cb3-part14-statements.l4` `the last day to apply to bar the examination within s 157(3)`; `the corporation may apply to the court within s 157(3)`; `the court may bar the right to examine within s 157(3)` | Within fifteen days of the request (the keel's counting); the court may bar if satisfied that the examination would be detrimental to the corporation or a subsidiary. |
| s 157(4) (heading: "Notice to Director") | src:1944-1945 | encoded | `cb3-part14-statements.l4` `the corporation must give notice of the application within s 157(4)`; `the duty to give notice of the application is met within s 157(4)`; `the Director and the person may appear and be heard within s 157(4)` | Notice to the Director and to the person asking to examine; both may appear and be heard. |
| s 158(1) (heading: "Approval of financial statements") | src:1946-1947 | encoded | `cb3-part14-statements.l4` `the approval is evidenced as s 158(1) requires within s 158(1)` | Evidenced by the manual signature of one or more directors, or a facsimile of the signatures reproduced in the statements. |
| s 158(2) (heading: "Condition precedent") | src:1948-1951 | encoded | `cb3-part14-statements.l4` `the condition for issuing copies is met within s 158(2)`; `issuing copies is prohibited within s 158(2)` | A corporation shall not issue, publish or circulate copies unless approved and signed under (1) and accompanied by the auditor's report, if any. |
| s 159(1) (heading: "Copies to shareholders") | src:1952-1953 | fork | `cb3-part14-statements.l4` `the corporation must send the documents to the shareholder within s 159(1)`; `the last day to send the documents to the shareholders within s 159(1)`; `the documents were sent in time within s 159(1)` | Fork F-159-before: "not less than twenty-one days before" counts back from the meeting (or signing) day, which is day 0; a shareholder who has said in writing that they do not want a copy is not owed one. |
| s 159(2) (heading: "Offence") | src:1954-1955 | encoded | `cb3-part14-statements.l4` `the corporation is guilty of an offence within s 159(2)`; `the penalty ceiling within s 159(2)` | Without reasonable cause; fine not exceeding $5,000, no imprisonment ceiling stated (NOTHING). |
| s 160(1) (heading: "Copies to Director") | src:1956-1959 | fork | `cb3-part14-statements.l4` `the corporation must send the documents to the Director within s 160(1)`; `the documents were sent to the Director in time within s 160(1)(a)`; `the last day to send the documents to the Director within s 160(1)(b)`; `the documents were sent to the Director in any event in time within s 160(1)(b)` | Fork F-160-earlier: (b)'s two limits both apply and the copy is due by the earlier day, read as in s 133(1)(b); (a) is twenty-one days before the meeting or, for a resolution in lieu, without delay after signing. |
| s 160(2) (heading: "Subsidiary corporation exemption") | src:1960-1963 | encoded | `cb3-part14-statements.l4` `the subsidiary corporation is not required to comply with s 160 within s 160(2)` | The holding corporation's consolidated or combined statements include the subsidiary and are included in what it sent the Director. |
| s 160(3) (heading: "Offence") | src:1964-1965 | encoded | `cb3-part14-statements.l4` `the corporation is guilty of an offence within s 160(3)`; `the penalty ceiling within s 160(3)` | Fine not exceeding $5,000, no imprisonment ceiling stated (NOTHING). |
| s 161(1) (heading: "Qualification of auditor") | src:1966-1967 | encoded | `cb3-part14-auditor.l4` `a person is disqualified from being an auditor within s 161(1)` | Not independent, subject to an exemption order under (5). |
| s 161(2) (heading: "Independence") | src:1968-1974 | encoded | `cb3-part14-auditor.l4` `the person is not independent within s 161(2)`; `the person is deemed not independent within s 161(2)(b)` | Independence is a question of fact (input); (b) deems a person not independent on any of three limbs; (iii) within two years of the proposed appointment, counted by the keel. |
| s 161(2.1) (heading: "Business partners") | src:1975-1976 | encoded | `cb3-part14-auditor.l4` `a business partner within s 161(2.1)` | A business partner includes a shareholder of the person; the ordinary meaning is the caller's. |
| s 161(3) (heading: "Duty to resign") | src:1977-1978 | encoded | `cb3-part14-auditor.l4` `the auditor must resign forthwith within s 161(3)`; `the duty to resign is met within s 161(3)` | A disqualified auditor, subject to (5), resigns forthwith after becoming aware; "forthwith" is the caller's judgment. |
| s 161(4) (heading: "Disqualification order") | src:1979-1980 | encoded | `cb3-part14-auditor.l4` `an interested person may apply for a disqualification order within s 161(4)` | Who may apply; the order is the court's. |
| s 161(5) (heading: "Exemption order") | src:1981-1982 | encoded | `cb3-part14-auditor.l4` `an interested person may apply for an exemption order within s 161(5)`; `the court may make an exemption order within s 161(5)`; `the exemption order may have retrospective effect within s 161(5)` | The court's power arises only if satisfied that the exemption would not unfairly prejudice the shareholders; the terms are the court's. |
| s 162(1) (heading: "Appointment of auditor") | src:1983-1984 | encoded | `cb3-part14-auditor.l4` `the shareholders must appoint an auditor within s 162(1)`; `the auditor is appointed by ordinary resolution within s 162(1)`; `the appointed auditor holds office within s 162(1)` | At each annual meeting, by ordinary resolution (the keel's rule; a tie is not a majority), unless s 163; the term runs to the close of the next annual meeting. |
| s 162(2) (heading: "Eligibility") | src:1985-1986 | encoded | `cb3-part14-auditor.l4` `the auditor appointed under section 104 is eligible within s 162(2)` | Eligible by this subsection; s 161 still applies. |
| s 162(3) (heading: "Incumbent auditor") | src:1987-1988 | encoded | `cb3-part14-auditor.l4` `the incumbent auditor continues in office within s 162(3)` | If an auditor is not appointed at a meeting, the incumbent continues until a successor is appointed. |
| s 162(4) (heading: "Remuneration") | src:1989-1990 | encoded | `cb3-part14-auditor.l4` `the directors may fix the remuneration of the auditor within s 162(4)` | Fixed by ordinary resolution or, if not so fixed, by the directors. |
| s 163(1) (heading: "Dispensing with auditor") | src:1991-1992 | encoded | `cb3-part14-auditor.l4` `shareholders may resolve not to appoint an auditor within s 163(1)` | Only a corporation that is not a distributing corporation. |
| s 163(2) (heading: "Limitation") | src:1993-1994 | fork | `cb3-part14-auditor.l4` `the resolution not to appoint an auditor is valid within s 163` | Fork F-163-until: valid "only until the next succeeding annual meeting" is read as valid on the days before the meeting day, not on it (the wording differs from s 162(1)'s "until the close of"). |
| s 163(3) (heading: "Unanimous consent") | src:1995-1996 | encoded | `cb3-part14-auditor.l4` `the resolution not to appoint an auditor is valid within s 163` | Not valid unless consented to by all the shareholders, including those not otherwise entitled to vote. |
| s 163(4) | src:1997 | repealed or blank in this text | - | The text shows "(4) [Repealed, 1994, c. 24, s. 18]" (src:1997). |
| s 164(1) (heading: "Ceasing to hold office") | src:1998-2001 | encoded | `cb3-part14-auditor.l4` `the auditor ceases to hold office within s 164(1)` | Dies, resigns, or is removed under s 165. |
| s 164(2) (heading: "Effective date of resignation") | src:2002-2003 | encoded | `cb3-part14-auditor.l4` `the date the resignation becomes effective within s 164(2)` | The later of the day the written resignation is sent and the day it specifies. |
| s 165(1) (heading: "Removal of auditor") | src:2004-2005 | encoded | `cb3-part14-auditor.l4` `the shareholders may remove the auditor within s 165(1)` | By ordinary resolution at a special meeting, unless the auditor was appointed by a court under s 167. |
| s 165(2) (heading: "Vacancy") | src:2006-2007 | encoded | `cb3-part14-auditor.l4` `the vacancy may be filled at the meeting of removal within s 165(2)`; `the vacancy may be filled under section 166 within s 165(2)` | At the removal meeting, or, if not so filled, under s 166. |
| s 166(1) (heading: "Filling vacancy") | src:2008-2009 | encoded | `cb3-part14-auditor.l4` `the directors must fill the vacancy forthwith within s 166(1)`; `the duty to fill the vacancy is met within s 166(1)` | The directors fill a vacancy forthwith unless the articles reserve it to the shareholders; "forthwith" is the caller's judgment. |
| s 166(2) (heading: "Calling meeting") | src:2010-2011 | encoded | `cb3-part14-auditor.l4` `the last day for the directors in office to call the meeting within s 166(2)`; `the directors then in office must call a special meeting within s 166(2)`; `any shareholder may call the meeting within s 166(2)` | Without a quorum of directors, the directors in office call a special meeting within twenty-one days (the keel's counting); if they fail, or there are no directors, any shareholder may call it. |
| s 166(3) (heading: "Shareholders filling vacancy") | src:2012-2013 | encoded | `cb3-part14-auditor.l4` `the articles may so provide within s 166(3)` | The articles may provide that a vacancy is filled only by the shareholders; the effect is carried by the input of the rule for (1). |
| s 166(4) (heading: "Unexpired term") | src:2014-2015 | encoded | `cb3-part14-auditor.l4` `the date the term of the auditor appointed to fill the vacancy ends within s 166(4)` | The unexpired term of the predecessor. |
| s 167(1) (heading: "Court appointed auditor") | src:2016-2017 | encoded | `cb3-part14-auditor.l4` `the court may appoint an auditor and fix the remuneration within s 167` | The corporation has no auditor; on the application of a shareholder or the Director; the order is the court's. |
| s 167(2) (heading: "Exception") | src:2018-2019 | encoded | `cb3-part14-auditor.l4` `the court may appoint an auditor and fix the remuneration within s 167` | Not if the shareholders have resolved under s 163 not to appoint an auditor. |
| s 168(1) (heading: "Right to attend meeting") | src:2020-2021 | encoded | `cb3-part14-auditor.l4` `the auditor is entitled to notice of and to attend and be heard at shareholders' meetings within s 168(1)`; `the corporation bears the expense of the auditor's attendance within s 168(1)` | Notice of every meeting, and attendance at the corporation's expense. |
| s 168(2) (heading: "Duty to attend") | src:2022-2023 | encoded | `cb3-part14-auditor.l4` `the auditor or former auditor must attend the meeting within s 168(2)`; `the duty to attend and answer questions is met within s 168(2)` | On written notice by a director or shareholder not less than ten days before the meeting (counted back, as in s 159(1)), at the corporation's expense. |
| s 168(3) (heading: "Notice to corporation") | src:2024-2025 | encoded | `cb3-part14-auditor.l4` `the copy of the notice to the corporation is sent as s 168(3) requires within s 168(3)` | A copy to the corporation, concurrently (the same day). |
| s 168(4) (heading: "Offence") | src:2026-2027 | encoded | `cb3-part14-auditor.l4` `the auditor or former auditor is guilty of an offence within s 168(4)`; `the penalty ceiling within s 168(4)` | Failure without reasonable cause to comply with (2); $5,000 or six months or both. |
| s 168(5) (heading: "Statement of auditor") | src:2028-2033 | encoded | `cb3-part14-auditor.l4` `the auditor is entitled to submit a statement within s 168(5)` | On (a) resigning, (b) learning of a removal meeting, (c) learning of a meeting to appoint a replacement, or (d) learning of a s 163 meeting. |
| s 168(5.1) (heading and lead-in) (heading: "Other statements") | src:2034-2035 | encoded | `cb3-part14-auditor.l4` `the corporation must make a statement on the reasons for the replacement within s 168(5.1)(a)`; `the proposed replacement auditor may comment within s 168(5.1)(b)` | Applies on a proposed replacement, by removal or at the end of the term. |
| s 168(5.1)(a) | src:2036 | encoded | `cb3-part14-auditor.l4` `the corporation must make a statement on the reasons for the replacement within s 168(5.1)(a)` | The corporation shall make a statement on the reasons. |
| s 168(5.1)(b) | src:2037 | encoded | `cb3-part14-auditor.l4` `the proposed replacement auditor may comment within s 168(5.1)(b)` | The replacement auditor may comment on those reasons. |
| s 168(6) (heading: "Circulating statement") | src:2038-2039 | encoded | `cb3-part14-auditor.l4` `the corporation must send a copy of the statements within s 168(6)`; `the duty to send a copy of the statements is met within s 168(6)` | Without delay to every shareholder entitled to notice and to the Director, unless included in or attached to a management proxy circular under s 150. |
| s 168(7) (heading: "Replacing auditor") | src:2040-2041 | encoded | `cb3-part14-auditor.l4` `a person may accept the appointment within s 168(7) and (8)` | No acceptance until the person has requested and received the retiring auditor's written statement. |
| s 168(8) (heading: "Exception") | src:2042-2043 | encoded | `cb3-part14-auditor.l4` `the last day for the auditor to reply within s 168(8)`; `a person may accept the appointment within s 168(7) and (8)` | A person otherwise qualified may accept if they get no reply within fifteen days after the request: only once the fifteenth day has passed. |
| s 168(9) (heading: "Effect of non-compliance") | src:2044-2045 | encoded | `cb3-part14-auditor.l4` `the appointment is void within s 168(9)` | Void unless (7) or (8) is met. |
| s 169(1) (heading: "Examination") | src:2046-2047 | encoded | `cb3-part14-auditor.l4` `the auditor must examine the statements within s 169(1)` | The statements required to be placed before the shareholders, except those relating to the preceding financial year (s 155(1)(a)(ii)). |
| s 169(2) (heading: "Reliance on other auditor") | src:2048-2049 | encoded | `cb3-part14-auditor.l4` `an auditor may rely on the report of another auditor within s 169(2)` | Reasonable reliance on another auditor's report where that body's accounts are included in whole or in part. |
| s 169(3) (heading: "Reasonableness") | src:2050-2051 | encoded | `cb3-part14-auditor.l4` `an auditor may rely on the report of another auditor within s 169(2)` | Reasonableness is a question of fact: the second input. |
| s 169(4) (heading: "Application") | src:2052-2053 | encoded | `cb3-part14-auditor.l4` `an auditor may rely on the report of another auditor within s 169(2)` | Applies whether or not the statements are consolidated: the rule has no input on consolidation. |
| s 170(1) (heading: "Right to information") | src:2054-2058 | encoded | `cb3-part14-auditor.l4` `the person must provide it on the auditor's demand within s 170(1)` | Present or former directors, officers, employees, agents or mandataries; information, explanations and access, that the auditor considers necessary and the person is reasonably able to provide. |
| s 170(2) (heading: "Idem") | src:2059-2062 | encoded | `cb3-part14-auditor.l4` `the directors must obtain and furnish the information within s 170(2)`; `the duty to obtain and furnish the information is met within s 170(2)` | The directors obtain the subsidiaries' information on demand and furnish it to the auditor. |
| s 170(3) (heading: "No civil liability") | src:2063-2064 | encoded | `cb3-part14-auditor.l4` `the person is not liable in the civil proceeding within s 170(3)` | Good faith communication under (1) or (2): no liability in any civil proceeding. |
| s 171(1) (heading: "Audit committee") | src:2065-2066 | encoded | `cb3-part14-auditor.l4` `the corporation must have an audit committee within s 171(1)`; `a corporation not described in subsection 102(2) may have an audit committee within s 171(1)`; `the audit committee is composed as s 171(1) requires within s 171(1)` | A corporation described in s 102(2) must, any other may; not fewer than three directors, a majority not officers or employees (more than half). |
| s 171(2) (heading: "Exemption") | src:2067-2068 | encoded | `cb3-part14-auditor.l4` `the Director may authorize the corporation to dispense with an audit committee within s 171(2)`; `the Director may permit the corporation to dispense with an audit committee on conditions within s 171(2)` | Authorize on application; permit on conditions if satisfied the shareholders will not be prejudiced; the Director's discretion is not decided. |
| s 171(3) (heading: "Duty of committee") | src:2069-2070 | fork | `cb3-part14-auditor.l4` `the audit committee reviewed the statements before they were approved within s 171(3)` | Fork F-171-before: a date has no time of day, so a review on the day of the approval is read as before it. |
| s 171(4) (heading: "Auditor’s attendance") | src:2071-2072 | encoded | `cb3-part14-auditor.l4` `the auditor is entitled to notice of and to attend and be heard at the committee's meetings within s 171(4)`; `the auditor must attend the committee's meeting within s 171(4)` | Notice and attendance at the corporation's expense; attendance is a duty if a member requests and the meeting is in the auditor's term. |
| s 171(5) (heading: "Calling meeting") | src:2073-2074 | encoded | `cb3-part14-auditor.l4` `a person may call a meeting of the audit committee within s 171(5)` | The auditor or a member. |
| s 171(6) (heading: "Notice of errors") | src:2075-2076 | encoded | `cb3-part14-auditor.l4` `the director or officer must notify the committee and the auditor within s 171(6)`; `the duty to notify the committee and the auditor is met within s 171(6)` | Forthwith, of any error or mis-statement in a statement the auditor or a former auditor reported on. |
| s 171(7) (heading: "Error in financial statements") | src:2077-2078 | encoded | `cb3-part14-auditor.l4` `the auditor or former auditor must inform each director within s 171(7)` | If, in their opinion, the error or mis-statement is material. |
| s 171(8) (heading: "Duty of directors") | src:2079-2082 | encoded | `cb3-part14-auditor.l4` `the directors must act on the error or mis-statement within s 171(8)`; `the duty of the directors is met within s 171(8)` | Revised statements issued, or the shareholders informed and, for a corporation required to comply with s 160, the Director informed in the same manner. |
| s 171(9) (heading: "Offence") | src:2083-2084 | encoded | `cb3-part14-auditor.l4` `a director or officer is guilty of an offence within s 171(9)`; `the penalty ceiling within s 171(9)` | Knowingly failing to comply with (6) or (8); $5,000 or six months or both. |
| s 172 (heading: "Qualified privilege (defamation)") | src:2085-2086 | encoded | `cb3-part14-auditor.l4` `the statement or report has qualified privilege within s 172` | A statement or report made under the Act by the auditor or a former auditor. |
| PART XIV.1 Disclosure Relating to Diversity (Part heading) | src:2088 | inert | - | The title of Part XIV.1, which holds s 172.1 only (disclosure relating to diversity); it states no rule and carries no condition. |
| s 172.1(1) (heading: "Diversity in corporations") | src:2089-2090 | encoded | `cb3-part14-1-diversity.l4` `the directors must place the diversity information before the shareholders within s 172.1(1)`; `the directors have complied with s 172.1(1)` | Duty of the directors to the shareholders at an annual meeting. "Prescribed corporation", "prescribed information" and "senior management as defined by regulation" are plain inputs (regulations are not a source). |
| s 172.1(2) (heading: "Information to shareholders and Director") | src:2091-2092 | encoded | `cb3-part14-1-diversity.l4` `the corporation must provide the diversity information to a shareholder within s 172.1(2)`; `the information was provided in a manner the section allows within s 172.1(2)` | Duty of the corporation to each shareholder who has not opted out in writing; the two manners are alternatives ("or"). |
| s 172.1(3) (heading: "Information to Director") | src:2093-2094 | fork | `cb3-part14-1-diversity.l4` `the corporation must send the diversity information to the Director within s 172.1(3)`; `the information was sent to the Director concurrently within s 172.1(3)` | Fork F-CONC: "concurrently" read as the same day as the information is provided under (2). |

## Fork register

### F-CONC: "concurrently" (s 172.1(3), `cb3-part14-1-diversity.l4`)

- The text, src:2094: "The corporation shall concurrently send the information referred to in subsection (1) to the Director."
- Readings: (i) on the same calendar day as the information is provided to the shareholders under subsection (2) [taken]; (ii) at the same instant; (iii) within a short, unstated time of it.
- Taken because the encoding works in dates; an input of two dates gives a boundary that can be tested (the day before and the day after fail).
- To change it: the one comparison in `the information was sent to the Director concurrently within s 172.1(3)`.

### F-126-officer: "of an entity" in "officer" (s 126(1), `officer within s 126(1)`)

- The text, src:1560: "officer means the chairperson of the board of directors, the president, a vice-president, the secretary, the treasurer, the comptroller, the general counsel, the general manager, a managing director, of an entity, or any other individual who performs functions for an entity similar to those normally performed by an individual occupying any of those offices".
- Readings: (i) "of an entity" qualifies every listed office, and the last limb needs an individual [taken]; (ii) it qualifies only "a managing director", the nearest item.
- Taken because the comma-separated list is read as one list followed by one qualifier, as the keel reads "of a corporation" in s 2(1) "officer" (src:54), and because the last limb repeats "for an entity".
- To change it: the `entity within s 2(1)` conjunct of the rule.

### F-130-2: "the corporation" in s 130(2) (`selling a call or buying a put is prohibited within s 130(2)`)

- The text, src:1576: "An insider shall not knowingly, directly or indirectly, sell a call or buy a put in respect of a security of the corporation or any of its affiliates." Subsection (1) speaks of "a distributing corporation"; no corporation has been named in (2).
- Readings: (i) "the corporation" is the distributing corporation of which the person is an insider [taken]; (ii) any corporation.
- Taken because "insider" in this Part is defined only by reference to a distributing corporation (s 126(1), src:1555-1559).
- To change it: the last conjunct of the rule.

### F-130-3: what the s 130(3) exception covers (`the exception to a short sale applies within s 130(3)`)

- The text, src:1578: "Despite subsection (1), an insider may sell a security they do not own if they own another security convertible into the security sold or an option or right to acquire the security sold and, within ten days after the sale, they (a) ... or (b) ...".
- Readings: (i) the exception covers only the case where the insider does not own the security; an insider who owns it but has not fully paid for it is not relieved [taken]; (ii) it covers every case caught by (1).
- Taken on the words "a security they do not own".
- It does not relieve s 130(2) (calls and puts): "Despite subsection (1)" names (1) only (finding 4).
- To change it: drop the first conjunct of the rule.

### F-131-1h: the tippee chain (s 131(1)(h), `insider within s 131(1)(h)`)

- The text, src:1592: a person "who receives material confidential information from a person described in this subsection or in subsection (3) or (3.1), including a person described in this paragraph, and who knows or who ought reasonably to have known that the person giving the information is a person described in this subsection or in subsection (3) or (3.1), including a person described in this paragraph".
- The definition is recursive: a tippee of a tippee is an insider. Readings: (i) the giver's status is a fact about the giver, and the rule takes it as an input (`received ... from a person described in subsection 131(1), (3) or (3.1)`); the depth of the chain is not computed [taken]; (ii) the rule recurses over a list of persons.
- Taken because the facts of the chain are the caller's; recursion would need the whole chain of persons as input, with nothing in the text to say where it stops.
- To change it: replace the two fields of the record by a list of givers.

### F-131-3: how far a (3) person is an insider (`insider with respect to the information within s 131(1), (3) and (3.1)`)

- The text, src:1599: a person who proposes a take-over bid or a business combination "is an insider of the corporation with respect to material confidential information obtained from the corporation and is an insider of the corporation for the purposes of subsection (6)". Subsection (3.1) (src:1601): an insider of such a person, and an affiliate or associate of such a person, "is an insider of the corporation".
- Readings: (i) a (3) person is an insider only as to information obtained from the corporation (for ss 131(4) and (5)), and an insider for the purposes of (6) without that limit; a (3.1) person is an insider without limit [taken for (4), (5) and (3.1); (6) and (7) take the status as a plain input]; (ii) a (3) person is an insider for every purpose of the section.
- Taken on the words "with respect to material confidential information obtained from the corporation".
- To change it: the last conjunct of `insider with respect to the information within s 131(1), (3) and (3.1)`.

### F-131-8: "must consider" (s 131(8), `the court must consider the comparison with the post-disclosure price within s 131(8)`)

- The text, src:1618: "The court may assess damages under subsection (4) or (6) in accordance with any measure of damages that it considers relevant in the circumstances. However, in assessing damages in a situation involving a security of a distributing corporation, the court must consider the following: (a) ... (b) ...".
- Readings: (i) the court must take the two comparisons into account and may still choose any measure; the encoding gives the two amounts and says when they must be considered [taken]; (ii) the amounts are the measure of damages.
- Taken on "any measure" and "must consider" (not "must award").
- To change it: nothing in the rules; a reader who takes (ii) reads the two amounts as the award.

### F-126-scope: "except in section 131" is an input (s 126(1), `insider within s 126(1)`)

- The text, src:1555: "insider means, except in section 131, ...". The definition does not apply to section 131, which has its own (src:1584-1593).
- Readings: (i) the scope is a fact about where the word is used, carried as the input `the term is used in section 131`, which switches the s 126(1) definition off [taken]; (ii) the scope is carried by the rule names only (`... within s 126(1)` against `... within s 131(1)`) and the rule has no such input.
- Taken so that the exclusion is asserted and not only commented. The seat layer always passes FALSE (it asks about Part XI outside s 131) and uses the s 131(1) rules for s 131; the input is a scoping fact dressed as a runtime input, and a reader who prefers (ii) can delete the first conjunct and the input.
- To change it: the first conjunct of the rule, and the first argument of its calls.

### F-133-call: "call" and not "hold" (s 133(1), `the last day to call the first annual meeting within s 133(1)(a)`)

- The text, src:1638-1640: "The directors of a corporation shall call an annual meeting of shareholders (a) not later than eighteen months after the corporation comes into existence; and (b) subsequently, not later than fifteen months after holding the last preceding annual meeting but no later than six months after the end of the corporation's preceding financial year."
- Readings: (i) the deadline is for calling the meeting, and the date of the last preceding annual meeting is the date it was HELD [taken, on the words]; (ii) the deadline is for holding it.
- Taken because the section says "call" in the lead-in and "holding" only for the last preceding meeting. The Act does not say how long after the call the meeting may be held.
- To change it: rename the input `the date the directors call the annual meeting` and the rule heads.

### F-133-earlier: the two limits of s 133(1)(b) (`the last day to call a subsequent annual meeting within s 133(1)(b)`)

- The text, src:1640: "not later than fifteen months after holding the last preceding annual meeting but no later than six months after the end of the corporation's preceding financial year".
- Readings: (i) both limits apply, so the meeting must be called by the earlier of the two days [taken]; (ii) either is enough, so by the later.
- Taken because "but" joins two "not later than" limits as cumulative conditions; the later-day reading would make the second limit idle whenever the first ran out first.
- To change it: swap the comparison in the rule's IF.

### F-134-vote: no default record date for voting (s 134(2), `the record date when none is fixed within s 134(2)`)

- The text, src:1654-1657: (a) the record date to receive notice is the day before the notice is given (or the meeting day if none is given); (b) for "any purpose other than to establish a shareholder's right to receive notice of a meeting or to vote" it is the day the directors pass the resolution.
- Neither (a) nor (b) covers voting. The rule returns NOTHING for that purpose and asserts it; it does not invent a default (the meeting day is the natural guess, but the text does not say it).
- To change it: a ruling from the lead or the source consolidation; the one `WHEN` line of the rule.

### F-135-adjourn: aggregate days (s 135(3) and (4), `notice of the adjourned meeting other than by announcement is unnecessary within s 135(3)`)

- The text, src:1673 and 1675: (3) "adjourned for less than thirty days" and (4) "adjourned by one or more adjournments for an aggregate of thirty days or more"; s 149(1) "does not apply" unless the aggregate is "more than ninety days".
- Readings: (i) the single input is the aggregate days of adjournment, for both subsections [taken]; (ii) (3) is about one adjournment and (4) about the aggregate.
- Taken because (3) and (4) are the two halves of one scheme (under thirty and thirty or more) and the section would have a gap for several short adjournments adding up to thirty days under (ii).
- The thresholds are tested at 29, 30, 90 and 91 days.
- To change it: the argument of `notice of the adjourned meeting other than by announcement is unnecessary within s 135(3)`.

### F-137-1b: what the discussing right takes in (s 137(1)(b), `a person may discuss a matter at the meeting within s 137(1)(b)`)

- The text, src:1687: the holder or owner may "discuss at the meeting any matter in respect of which the person would have been entitled to submit a proposal".
- Readings: (i) "would have been entitled" takes in the (1.1) eligibility and the (1)(a) status, so the right is the right to submit, exercised at the meeting [taken]; (ii) only the status of holder or owner.
- Taken because the opening of (1) says "Subject to subsections (1.1) and (1.2)" and (1)(b) is built on (1)(a). One input carries it, so a seat that has computed the (1.1) result passes it.
- To change it: the second input of the rule.

### F-137-2: when the circulating duty arises (s 137(2), `the corporation must circulate the proposal within s 137(2)`)

- The text, src:1701 and 1707: "A corporation that solicits proxies shall set out the proposal in the management proxy circular required by section 150 or attach the proposal thereto"; "A corporation is not required to comply with subsections (2) and (3) if ..." and, by (5.1), is "not required to set out in the management proxy circular, or attach to it, any proposal submitted by that person".
- Readings: (i) the duty exists only for a corporation that solicits proxies, for a proposal submitted by a person who may submit it, and is excused by either exemption [taken]; (ii) the duty is unconditional apart from (5).
- Taken because (5.1) says "not required" of the same act.
- To change it: drop the last conjunct of the rule.

### F-137-7: which day starts the period for the refusal notice (s 137(7), `the duty to notify the person of the refusal is met within s 137(7)`)

- The text, src:1719: "within the prescribed period after the day on which it receives the proposal or the day on which it receives the proof of ownership under subsection (1.4), as the case may be".
- The text does not say which day "the case" is: presumably the later where proof was asked for, the proposal day where it was not. The encoding does not decide: the one input (`the notice is given within the prescribed period after the day ... as the case may be`) is the caller's after the caller has chosen the day.
- To change it: split the input into two dates and a rule of the lead's choosing.

### F-138-1b: "on the record date" (s 138(1)(b), `the list of shareholders entitled to receive notice complies with s 138(1)`)

- The text, src:1729: where no record date is fixed, the list is prepared "on the record date established under paragraph 134(2)(a)". Contrast s 138(3), src:1733, which for the same date says "not later than".
- Readings: (i) "on" is the day itself, so a list prepared a day early or a day late does not comply [taken, on the words]; (ii) "on" means by.
- Taken because the section uses "not later than" for (a) and for (3) and "on" only here. The list is of the shareholders entitled to receive notice at the date, so a list prepared before that date is hard to see as complying.
- To change it: the `EQUALS` in the NOTHING branch of the rule becomes `AT MOST`.

### F-138-3: "as the case may be" (s 138(3), `the last day to prepare the list of shareholders entitled to vote within s 138(2) and (3)`)

- The text, src:1733: "not later than 10 days after the record date that is fixed under paragraph 134(1)(c) or not later than the record date that is established under paragraph 134(2)(a), as the case may be".
- Readings: (i) the 134(1)(c) date governs where a record date for notice was fixed, and the 134(2)(a) date where none was [taken]; (ii) the corporation chooses.
- Taken because s 134(2)(a) is the default "if no record date is fixed".
- To change it: the inner `CONSIDER` of the rule.

### F-139-tie: "majority" (s 139(1), `a quorum of shareholders is present within s 139(1)`)

- The text, src:1741: a quorum is present "if the holders of a majority of the shares entitled to vote at the meeting are present in person or represented by proxy".
- Readings: (i) a majority is more than half, so exactly half is not a quorum [taken]; (ii) at least half.
- Taken on the ordinary meaning of "majority" (more than half). Asserted at 500 of 1000 and 501 of 1000.
- To change it: `GREATER THAN` to `AT LEAST`.

### F-143-3c: "paragraphs 137(5)(b) to (e)" (s 143(3)(c), `the directors must call the meeting within s 143(3)`)

- The text, src:1780: "the business of the meeting as stated in the requisition includes matters described in paragraphs 137(5)(b) to (e)".
- Section 137(5) has limbs (a), (b), (b.1), (c), (d), (e). The range "(b) to (e)" is read by position, so it takes in (b.1) [taken]; the alternative is to read it as (b), (c), (d), (e) only.
- Taken because a range of paragraphs in the Act includes the paragraphs numbered between its ends. Limb (a) (not submitted in time) is left out in both readings.
- To change it: the meaning of the one input `the business stated in the requisition includes matters described in paragraphs 137(5)(b) to (e)`; the seat takes it as the OR of the five limbs.

### F-143-4: the shareholders' power to call and the directors' excuses (s 143(4), `a shareholder who signed may call the meeting within s 143(4)`)

- The text, src:1782: "If the directors do not within twenty-one days after receiving the requisition referred to in subsection (1) call a meeting, any shareholder who signed the requisition may call the meeting." Subsection (3) says the directors shall call "unless" (a), (b) or (c).
- Readings: (i) the power arises only where the directors were required to call by (3) (they were not excused) [taken]; (ii) it arises whenever the directors have not called within twenty-one days, excused or not.
- Taken because (ii) would let the requisitioners call a meeting on business that (3)(c) says the directors need not call, which would defeat the purpose of the exception.
- To change it: drop the second conjunct of the rule.

### F-143-6: when the reimbursement duty arises (s 143(6), `the corporation must reimburse the shareholders' expenses within s 143(6)`)

- The text, src:1786: "Unless the shareholders otherwise resolve at a meeting called under subsection (4), the corporation shall reimburse the shareholders the expenses reasonably incurred by them in requisitioning, calling and holding the meeting."
- Readings: (i) the duty arises on a requisition under (1), including one where the directors then called the meeting, and the shareholders can resolve otherwise only at a meeting they called under (4) [taken]; (ii) the duty exists only for a meeting called under (4).
- Taken because "requisitioning" is an expense the shareholders incur in either case, and "calling and holding" only in the (4) case.
- To change it: the rule's second conjunct.

### F-147-includes: "and includes" in "intermediary" (s 147, `intermediary within s 147`)

- The text, src:1823-1830: "intermediary means a person who holds a security on behalf of another person who is not the registered holder of the security, and includes (a) a securities broker or dealer ... (g) a person who carries out functions similar to those carried out by individuals or entities referred to in any of paragraphs (a) to (e) and that holds a security registered in its name, or in the name of its nominee, on behalf of another person who is not the registered holder of the security."
- Readings: (i) the listed kinds are intermediaries whether or not the general description fits them [taken]; (ii) the list only illustrates the general description.
- Taken because "includes" extends a definition; reading (ii) would make the list idle for the kinds, such as a securities depositary, that need not hold for a particular other person.
- (g) alone has a condition of its own, and both its limbs are needed.
- To change it: drop the (a) to (f) disjuncts of the rule.

### F-147-solicit: the open definition of "solicit" (s 147, `solicitation within s 147`)

- The text, src:1833-1846: "solicit or solicitation (a) includes (i) ... (iv) ...; but (b) does not include (i) ... (vii) ...".
- Readings: (i) the definition is open-ended: an act in a limb of (a) and in none of (b) is a solicitation; an act in a limb of (b) is not one, even if it is also in (a); an act in neither is not decided by this section, and the rule returns NOTHING [taken]; (ii) an act in no limb is not a solicitation.
- Taken because "includes" leaves the ordinary meaning in place and (b) is introduced by "but", cutting back (a).
- To change it: the NOTHING branch of the rule.

### F-150-3: "subsections (1) and (2)" (s 150(3), `a person is guilty of an offence within s 150(3)`)

- The text, src:1884: "A person who fails to comply with subsections (1) and (2) is guilty of an offence".
- Readings: (i) failing either subsection is an offence [taken]; (ii) only a person who fails both is guilty.
- Taken because (ii) would leave a failure to send the copy to the Director (s 150(2)) without a sanction whenever the circular itself was sent.
- To change it: `OR` to `AND` in the rule.

### F-156-public: whose benefit is weighed (s 156, `the Director may exempt the corporation within s 156`)

- The text, src:1937: "if the Director reasonably believes that the detriment that may be caused to the corporation by the requirement outweighs its benefit to the shareholders or, in the case of a distributing corporation, to the public".
- Readings: (i) for a distributing corporation the benefit weighed is the public's, for any other the shareholders' [taken]; (ii) for a distributing corporation both are weighed.
- Taken because "in the case of a distributing corporation" substitutes the public for the shareholders in the same sentence.
- To change it: the `IF` in the rule.

### F-159-before: "not less than twenty-one days before" (s 159(1), `the last day to send the documents to the shareholders within s 159(1)`; also s 160(1)(a))

- The text, src:1953: send "not less than twenty-one days before each annual meeting of shareholders or before the signing of a resolution under paragraph 142(1)(b) in lieu of the annual meeting".
- Readings: (i) the meeting day is day 0 and sending on the twenty-first day before it, or earlier, is in time, the mirror of the keel's counting for "within N days after" [taken]; (ii) "clear days": neither the day of sending nor the day of the meeting counts, so the twenty-second day before is the last.
- Taken for symmetry with the keel's convention (fork F1). The Interpretation Act is not a source, and its clear-days rule is not applied.
- To change it: `MINUS 21` to `MINUS 22` in both rules.

### F-160-earlier: the two limits of s 160(1)(b) (`the last day to send the documents to the Director within s 160(1)(b)`)

- The text, src:1959: "within fifteen months after the last preceding annual meeting should have been held or a resolution in lieu of the meeting should have been signed, but no later than six months after the end of the corporation's preceding financial year".
- Read as s 133(1)(b) is: both limits apply, so the copy is due by the earlier of the two days (F-133-earlier). The date the meeting "should have been held" is the caller's: it is not the date it was held.
- To change it: swap the comparison in the rule's IF.

### F-163-until: "valid only until the next succeeding annual meeting" (s 163(2), `the resolution not to appoint an auditor is valid within s 163`)

- The text, src:1994: "A resolution under subsection (1) is valid only until the next succeeding annual meeting of shareholders." Section 162(1), src:1984, says an auditor holds office "until the close of the next annual meeting".
- Readings: (i) the resolution is valid on the days before the meeting day and not on it [taken]; (ii) it is valid through the meeting, as an auditor's term is.
- Taken because s 162(1) says "the close of" and s 163(2) does not, and at the meeting an auditor must be appointed or a new resolution passed. Asserted at the day before, the day of and the day after.
- To change it: `LESS THAN` to `AT MOST` in the rule.

### F-171-before: "before such financial statements are approved" (s 171(3), `the audit committee reviewed the statements before they were approved within s 171(3)`)

- The text, src:2070: "An audit committee shall review the financial statements of the corporation before such financial statements are approved under section 158."
- Readings: (i) the review date is on or before the approval date: a date carries no time of day, so a same-day review is read as in order [taken]; (ii) the review date is strictly earlier.
- Taken because the encoding has no time of day. A reader who wants (ii) loses nothing but a same-day case, which the encoding cannot order anyway.
- To change it: `AT MOST` to `LESS THAN` in the rule.

## Cross-references out of my ranges

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| s 172.1(2) | s 135(1) (notice of a meeting) | cb3 (own range) | `the information was sent along with the notice referred to in subsection 135(1)` (BOOLEAN; same piece, taken as a fact because the notice is the caller's) |
| s 126(1) insider, s 130(1), s 131(1)(b) | s 2(1) "distributing corporation", "subsidiary", "affiliate", "director" | keel (cbca-g0) | plain BOOLEANs, for example `the person is a director or officer of a distributing corporation`; the keel's rules are named in the comments |
| s 126(2)(c), (d) | s 2(2) to (5) (control, affiliate) | keel (cbca-g0) | the lists `the shares beneficially owned by each body corporate the person controls directly or indirectly` and `... by each affiliate of the body corporate`: who controls or is affiliated is the caller's |
| s 130(1), s 131(2) | s 2(1) "security", "call", "put" | keel (cbca-g0) | plain BOOLEANs (`the security is a security of a distributing corporation or of any of its affiliates`) |
| s 126(2)(a), s 131(1)(d) | the regulations ("the prescribed percentage") | not a source | `the prescribed percentage` (NUMBER, a fraction) |
| s 131(1)(i) | the regulations ("a prescribed person") | not a source | `a prescribed person` (BOOLEAN, a field) |
| s 131(3) | the regulations ("take-over bid (as defined in the regulations)") | not a source | `the person proposes to make a take-over bid, as defined in the regulations, for securities of the corporation` |
| s 131(4)(c) | the regulations ("the prescribed circumstances") | not a source | `the insider establishes that the purchase or sale took place in the prescribed circumstances` |
| s 131(3.1) | s 2(1) "associate" and "affiliate" | keel (cbca-g0) | `the person is an affiliate or associate of a person described in subsection 131(3)` |
| s 133(1)(a) | s 9 (the date the corporation comes into existence, on the certificate of incorporation) | piece cb1 or cb2 | the DATE input `the date the corporation comes into existence` |
| s 133(1)(b) | the corporation's financial year (Part XIV, s 155; the year end is a fact of the corporation) | own range (ss 155 and following) and the by-laws | the DATE input `the date the corporation's preceding financial year ended` |
| s 134(1), s 134(3) | the regulations ("within the prescribed period") | not a source | the BOOLEANs `the date is fixed within the prescribed period`, `the notice is given within the prescribed period` |
| s 135(1) | the regulations ("within the prescribed period") | not a source | the BOOLEAN `the notice was sent within the prescribed period` |
| s 135(1.1) | the articles and by-laws of the corporation | facts of the corporation (s 6, s 103) | the BOOLEAN `the articles or by-laws specify a shorter period` |
| s 135(4) | s 149(1) (the form of proxy and information circular, own range) | own range (Part XIII) | the BOOLEAN output `subsection 149(1) applies to the adjourned meeting within s 135(4)`; the Part XIII module takes it as an input |
| s 135(5) | s 155 and s 163 (financial statements, auditor's report; the business named is their consideration at the meeting) | own range | plain BOOLEANs on the kind of business |
| s 132(4), (5) | the regulations (participation by electronic means "in accordance with the regulations, if any") | not a source | the BOOLEANs `the participation is in accordance with the regulations, if any` and `the meeting is held in accordance with the regulations, if any` |
| s 137(2), (3), (5)(c), (5)(d), (7) | s 150 (the management proxy circular) and s 147 ("dissident's proxy circular") | own range (Part XIII) | the BOOLEANs `the proposal is set out in the management proxy circular`, `... attached to ...`, and the like |
| s 137(1.1), (1.4), (5), (5.1), (7) | the regulations (prescribed period, number, word limit, minimum support) | not a source | plain inputs named `... the prescribed ...` |
| s 137(8), (9), (10) | s 2(1) "court" and "Director" | keel (cbca-g0) | plain BOOLEANs on who the applicant is |
| s 137(1) | s 2(1) "beneficial owner", "registered holder"; the annual meeting (s 133(1)) | keel and own range | the BOOLEAN `the person is a registered holder or beneficial owner of shares entitled to be voted at an annual meeting of shareholders` |
| s 138(1), (2), (3) | s 134(1)(c), (d) and s 134(2)(a) (record dates) | own range (the meetings module) | the DATE inputs `the record date fixed under paragraph 134(1)(c), if one is fixed` and the like; `the record date for notice of a meeting when none is fixed within s 134(2)(a)` computes the last |
| s 141(4) | s 132(4), (5) | own range (the meetings module) | the BOOLEAN `the person participates in the meeting under subsection 132(4) or (5)` |
| s 142(1) | s 110(2) (a director's written statement) | out of range: section 110 (piece for the directors' Part) | the BOOLEAN `a written statement is submitted by a director under subsection 110(2)` |
| s 142(1) | s 168(5) (the auditor's written statement) | own range (the auditor module) | the BOOLEAN `a written statement is submitted by an auditor under subsection 168(5)` |
| s 141(3), (4) | the regulations ("in accordance with the regulations, if any") | not a source | the BOOLEANs `the vote is held in accordance with the regulations, if any` and `the vote is cast in accordance with the regulations, if any` |
| s 140(4) | ss 149(2) and 150(1.1) (joint holders counted as one) | own range (Part XIII) | the count of joint holders present is the caller's |
| s 143(3) | s 134(1)(c), s 134(3), s 135 | own range (the meetings module) | the BOOLEANs `a record date has been fixed under paragraph 134(1)(c)`, `notice of the record date has been given under subsection 134(3)`, `the directors have called a meeting of shareholders and have given notice of it under section 135` |
| s 143(3)(c) | s 137(5)(b) to (e) | own range (the proposals module) | the BOOLEAN `the business stated in the requisition includes matters described in paragraphs 137(5)(b) to (e)` |
| s 143(5) | Part XIII (the manner of calling meetings) | own range | the BOOLEAN `it is called as nearly as possible in the manner in which meetings are to be called pursuant to the by-laws, this Part and Part XIII` |
| s 144(1) | s 2(1) "Director" and "court" | keel (cbca-g0) | the BOOLEAN `the applicant is the Director` |
| s 146(4) | s 49(8) (notice of a restriction on a share certificate) | out of range: section 49 (piece for Part VI) | the BOOLEAN `notice of the existence of the agreement was given to the purchaser or transferee, in the manner referred to in subsection 49(8) or otherwise` |
| s 146(5) | s 119 (directors' liability for wages) | out of range: section 119 (piece for the directors' Part) | none; the rule names it in a comment and the relief is shown only by the shared input |
| s 146 | s 2(1) "unanimous shareholder agreement" and the keel's `there is a unanimous shareholder agreement` | keel (cbca-g0) | `there is a unanimous shareholder agreement within s 146(1) and (2)` is the answer to that input |
| s 147 "solicit", exclusion (iii) | s 153 (the documents an intermediary sends) | own range | the BOOLEAN `it is the sending by an intermediary of the documents referred to in section 153` |
| s 147 "solicit", exclusion (vi) | s 137(1.1) (shareholder proposal) | own range (the proposals module) | the BOOLEAN `it is a communication for the purposes of obtaining the number of shares required for a shareholder proposal under subsection 137(1.1)` |
| s 147 "solicit", exclusions (v), (vii) | the regulations ("as prescribed", "in any circumstances that may be prescribed") | not a source | plain BOOLEANs |
| s 147 "solicit", inclusion (iv) | s 149 (sending a form of proxy) | own range | the BOOLEAN `it is the sending of a form of proxy to a shareholder under section 149` |
| s 147 "intermediary", (e) | the Income Tax Act (registered plans) | out of range: another statute | the BOOLEAN `the person is a trustee or administrator of a self-administered retirement savings plan ... registered under the Income Tax Act` |
| s 148(4), (5) | business days, Saturdays and holidays (the calendar) | not in the core's units | the DATE `the last business day preceding the day of the meeting ...` and the NUMBER `the hours, excluding Saturdays and holidays, ...` |
| s 149(2), s 150(1) and (1.1), s 150(1) | s 2(1) "distributing corporation", "management" | keel (cbca-g0) | the BOOLEAN `the corporation is a distributing corporation` |
| s 149, s 150, s 152 | "prescribed form", "prescribed circumstances" | not a source (the regulations) | plain BOOLEANs: `the form of proxy is in the prescribed form`, `the solicitation is conveyed by public broadcast, speech or publication in the prescribed circumstances` |
| s 150(2), s 151(1), s 154 | s 2(1) "Director" | keel (cbca-g0) | plain BOOLEANs on who the applicant is |
| s 151(1) | ss 149, 150(1), 153(1) | own range | the BOOLEAN `the requirement is a requirement of section 149, subsection 150(1) or subsection 153(1)` |
| s 153(1) | s 150, financial statements (Part XIV) | own range | the rule takes "each document" as one fact |
| s 155, s 158, s 159, s 160 | the regulations ("prescribed comparative financial statements", "prescribed requirements") | not a source | the BOOLEAN `the statements are the prescribed comparative financial statements and conform to the prescribed requirements` |
| s 155(1)(a)(i) | the corporation's financial year (a fact of the corporation, by-laws or s 155) and the date it came into existence (s 9) | the corporation; piece for Part II | the DATE inputs `the end of the last completed financial year` and `the date the corporation came into existence` |
| s 155(1)(c) | unanimous shareholder agreement (s 146, own range) | own range (the requisition/agreements module) | the BOOLEAN `the articles, the by-laws or a unanimous shareholder agreement require further information ...`; `there is a unanimous shareholder agreement within s 146(1) and (2)` answers the agreement limb |
| s 156 | s 2(1) "Director", "distributing corporation" | keel (cbca-g0) | plain BOOLEANs |
| s 157(3), (4) | s 2(1) "court", "Director" | keel (cbca-g0) | plain BOOLEANs |
| s 159(1), s 160(1)(a) | s 142(1)(b) (resolution in lieu of the annual meeting) | own range (the voting module) | the DATE input `the date of the annual meeting, or of the signing of the resolution in lieu of it` and the BOOLEAN `a resolution under paragraph 142(1)(b) is signed in lieu of the annual meeting` |
| s 160(1) | s 2(1) "subsidiary", "holding corporation" | keel (cbca-g0) | plain BOOLEANs |
| s 161 | s 2(1) "affiliate", "business partner" (s 161(2.1)), "director", "officer", "employee", "material interest" | keel (cbca-g0) and this module | plain BOOLEANs; `a business partner within s 161(2.1)` is the one rule |
| s 162(1), s 165(1) | s 2(1) "ordinary resolution" | keel (cbca-g0) | the keel's `ordinary resolution within s 2(1)` takes the `Vote tally` |
| s 162(1), s 168(5)(d), s 167(2) | s 163 (dispensing with the auditor) | own range | the BOOLEAN `the shareholders have resolved under section 163 not to appoint an auditor` |
| s 162(2) | s 104 (an auditor appointed by the directors for the first year) | out of range: section 104 (piece for the directors' Part) | the BOOLEAN `the auditor was appointed under section 104` |
| s 165(1) | s 167 (a court-appointed auditor) | own range | the BOOLEAN `the auditor was appointed by a court under section 167` |
| s 168(6), s 165(2) | s 150 (the management proxy circular), s 166 (filling a vacancy) | own range | BOOLEANs |
| s 169(1), s 170 | s 155(1)(a)(ii) (the preceding financial year), s 169 (the examination and report) | own range | BOOLEANs `the statements or the part relate to the period referred to in subparagraph 155(1)(a)(ii)` and `in the opinion of the auditor it is necessary to enable the auditor to make the examination and report required under section 169` |
| s 171(1) | s 102(2) (the corporations that must have an audit committee) | out of range: section 102 (piece for the directors' Part) | the BOOLEAN `the corporation is one described in subsection 102(2)` |
| s 171(3) | s 158 (approval of the statements) | own range | the DATE input `the date the financial statements were approved under section 158` |
| s 171(8) | s 160 (copies to the Director) | own range | the BOOLEAN `the corporation is required to comply with section 160`; `the corporation must send the documents to the Director within s 160(1)` computes it |
| s 161(4), (5), s 167, s 171(2) | s 2(1) "court", "Director", "interested person" | keel (cbca-g0) | plain BOOLEANs on who the applicant is |

## Needs from the core

Nothing needs changing in the core. Gaps found, each taken as a plain input in cb3 (the lead decides whether to promote a unit):

- The core's `Unit of time` has calendar days, weeks, months and years only. Part XII and XIII also count in other units: "forty-eight hours, excluding Saturdays and holidays" (s 148(5)), "the last business day preceding the day of the meeting" (s 148(4)(a)(i)) and "twenty trading days" (s 131(8)). cb3 takes the computed cut-off date, or the computed average, as a plain input in each of these.

- Part XII (s 133(1)(a)): the date a corporation comes into existence (s 9, the certificate of incorporation) is a plain DATE input here; the keel has no type for the corporation's own dates. A shared `Corporate dates` record would let every piece take it once.
- Part XII (s 134(2)(a)): "close of business" is a time of day; the keel has dates only. The rule answers with the DATE.
- `cbca-core` does not import `cbca-core-definitions`, so a piece needing `entity within s 2(1)` imports it by name (listed again under "What the stable binary does not accept").

- Part XIII (s 148(4), (5)): "business day", "Saturdays and holidays" and "hours" are not in the core's `Unit of time`; the computed cut-off DATE (`the last business day preceding the day of the meeting`) and the computed NUMBER of hours are plain inputs. A calendar of holidays, or business-day and hour units, would let the caller drop them.

## What the text turns out to say


1. The definition of "officer" for Part XI (s 126(1), src:1560) has no limb for "an individual appointed as an officer under section 121", which the general definition (s 2(1), src:54) has. A person appointed an officer under s 121 who holds none of the listed offices and performs no similar function is an officer under s 2(1) but not under s 126(1). Asserted.
2. Under s 131(5) an insider is accountable to the corporation for the benefit of a trade described in s 131(4) unless the insider establishes the circumstance in paragraph (4)(a) only. That the counterparty knew the information (4)(b), or that the trade was in the prescribed circumstances (4)(c), defeats the counterparty's claim under (4) and does not defeat the corporation's claim under (5). Asserted.
3. Under s 131(7) the insider is accountable to the corporation unless the insider establishes the circumstances in (6)(a), (c) or (d). Defence (6)(b), that the person alleging damages knew the information, defeats that person's claim under (6) and does not defeat the corporation's claim under (7). Asserted.
4. The s 130(3) exception begins "Despite subsection (1)": it does not relieve an insider who sells a call or buys a put contrary to s 130(2). An insider who has the convertible security and delivers in time is clear of (1) and still guilty under (2) if the sale is of a call or the purchase of a put. Asserted.
5. The fine ceiling of s 130(4) is the greater of one million dollars and three times the profit: a profit of 333,333 gives a ceiling of 1,000,000 (3 x 333,333 = 999,999), a profit of 333,334 gives 1,000,002, and a loss gives 1,000,000. Asserted.
6. Under s 131(6) defence (c) (the disclosure was necessary in the course of the insider's business) is closed to a person described in (3) or (3.1), and defence (d) (necessary to effect the take-over bid or business combination) is open only to such a person; the same holds in (7) for (c) and (d). Asserted.
7. Where "insider" is used in section 131, the definition of s 126(1) does not apply at all ("except in section 131"), whatever limbs are met. Asserted.
8. A person described in s 131(3) (proposing a take-over bid or a business combination) is an insider of the corporation, for ss 131(4) and (5), only as to information obtained from the corporation. Asserted.
9. The ten days of s 130(3) run from the sale: an exercise and delivery, or a transfer, on the day before the sale is not "within ten days after the sale". Asserted.
10. "More than the prescribed percentage" (s 126(2)(a), s 131(1)(d)): a holding exactly equal to the prescribed percentage does not make a person an insider by those limbs. Asserted.
11. The joint and several liability of s 131(9) arises only when more than one insider is liable: with two or more, each answers for the whole; with one, the rule is not in point. Asserted.
12. The limitation of s 131(10) covers "a right created by subsections (4) to (7)": it runs against the counterparty's and the claimant's claims for damages and against the corporation's claims to an account. Not asserted separately: the rule is one function of two dates.
13. The accompanying information of s 137(1.2) is required of "a proposal submitted under paragraph (1)(a)"; paragraph (1)(a) is the right to submit a proposal, so every proposal is covered, including one that relies on supporters under (1.1)(b), where the supporters' details are needed too ("if applicable"). If the reference was meant to be to (1.1)(a) only, a supporters' proposal would escape the duty, which (1.2)(a) and (b) ("the person's supporters, if applicable") show is not intended. Asserted on the first reading.
14. The information provided under s 137(1.2) is not counted toward the prescribed maximum number of words of s 137(3), however long it is. Asserted: the same proposal and statement give the same count whatever the third input is.
15. The court's power under s 137(9) to permit the corporation to omit a proposal depends on its being satisfied that s 137(5) applies; the corporation is excused from (2) and (3) by (5) itself, without an order. An order under (9) is the corporation's way of being certain. Asserted: the power is not available when (5) does not apply.
16. The five-per-cent test of s 137(4) is satisfied by five per cent of all the shares entitled to vote at the meeting or five per cent of the shares of any one class, and "not less than" makes exactly five per cent enough. Asserted at 0.05 and 0.0499.
17. The immunity of s 137(6) is for liability "by reason only of circulating"; a liability on another ground (for example, a false statement in the proposal) is not touched. Asserted by the third input.
18. The ballot of s 141(1) displaces a show of hands only if it is demanded by "a shareholder or proxyholder entitled to vote at the meeting"; s 141(2) lets "a shareholder or proxyholder" demand a ballot "either before or after any vote by show of hands" without that qualification. So a person who is not entitled to vote may be allowed to demand a ballot by (2) without that demand displacing the show of hands under (1). Asserted: the two rules take two different inputs.
19. For the same record date, s 138(1)(b) says the list is prepared "on" it and s 138(3) says "not later than" it. Asserted as the words stand (F-138-1b).
20. When a quorum is not present at the opening, the shareholders present may adjourn but may not transact any other business (s 139(3)); when a quorum is present the subsection says nothing about other business, which the rule returns as NOTHING and asserts.
21. A shareholder whose name appears on the voting list may vote the shares shown (s 138(3.1)); the subsection does not say a shareholder whose name does not appear may not. The rule returns NOTHING for such a shareholder, not nought shares, and asserts it.
22. Where the articles otherwise provide, s 140(1) leaves the number of votes per share to them; the rule returns NOTHING when the input is not given, and the votes a holder may cast are NOTHING then too. Asserted.
23. A written resolution can satisfy the Act in two ways: s 142(1)(a), a resolution signed by all shareholders entitled to vote on that resolution, is as valid as one passed at a meeting; s 142(1)(b), a resolution dealing with all matters required to be dealt with at a meeting, signed by all entitled to vote at that meeting, satisfies all the requirements relating to meetings. The first is valid for a resolution; the second discharges the meeting itself (for example the annual meeting). Both are shut off by a director's statement under s 110(2) or an auditor's under s 168(5). Asserted.
24. Section 143(3)(c) refers to "paragraphs 137(5)(b) to (e)"; s 137(5) has a limb (b.1) between (b) and (c), which the range takes in by its place. Limb (a) (a proposal not submitted in time) is outside the range. Asserted by the input's comment and by the proposals module's five limbs; not a separate assertion.
25. The shareholders' power under s 143(4) is stated on the directors' failure to call within twenty-one days, without mention of the excuses in (3). Read with (3), it arises only where the directors were required to call. Asserted (F-143-4).
26. The reimbursement of s 143(6) arises on a requisition and not only on a meeting called under (4), and the shareholders can resolve against it only at a meeting called under (4). Asserted (F-143-6).
27. Where there is no duty to reimburse under s 143(6), the section gives no amount: the rule returns NOTHING and asserts it.
28. Under s 144(1) only a director, a shareholder entitled to vote at a meeting, or the Director may apply; a shareholder who holds only non-voting shares may not. Asserted.
29. A purchaser or transferee is deemed a party to a unanimous shareholder agreement by s 146(3) even if no notice was given; the remedy of s 146(4) is rescission within thirty days of becoming aware. Asserted: notice given, no right to rescind.
30. The keel's input `there is a unanimous shareholder agreement` is answered by a valid s 146(1) agreement or a s 146(2) declaration. Asserted.
31. Section 146(5) shifts a right, power, duty or liability to the party given the power only "to the extent" the agreement restricts the directors' powers, and relieves the directors of it to the same extent, including their liabilities under s 119. Asserted by the shared first input.
32. The definition of "solicit or solicitation" (s 147) is open-ended ("includes"): an act in none of its four inclusions and none of its seven exclusions is not decided by the definition. The rule returns NOTHING for it, JUST TRUE for an included act, and JUST FALSE for an excluded act even if it is also included. Asserted for all four cases.
33. The exceptions of s 150(1.1) (fifteen or fewer shareholders) and (1.2) (public broadcast) are open only to a person who is not the management; the management has neither, whatever the number of shareholders. Asserted.
34. Section 149(3) states a fine ceiling of $5,000 and no imprisonment, which the rule returns as NOTHING (not nought months); ss 149(4), 150(3), 150(4), 152(4), 153(8) and 153(9) state both. Asserted.
35. Sections 149(4), 150(4) and 153(9) make the director or officer guilty "whether or not" the corporation has been prosecuted or convicted: the rule requires that the corporation commits the offence, not that anyone was prosecuted. Asserted by the first input.
36. Section 150(3) is read as an offence for failing either subsection (F-150-3). Asserted.
37. Under s 152(2) a proxyholder has the shareholder's right to vote on a show of hands except with conflicting instructions from more than one shareholder; the right to speak and to vote on a ballot are not so qualified. Under s 152(3) the chairperson's route to a show of hands needs a fraction of the votes against that is strictly less than five per cent, and no demand for a ballot. Asserted at 0.049, 0.05 and 0.04.
38. The failure of an intermediary to comply with s 153 never makes a meeting or action void (s 153(6)), and s 153 gives an intermediary no right to vote shares it is otherwise prohibited from voting (s 153(7)). The first is a rule that is FALSE for every input; the second returns JUST FALSE or NOTHING. Asserted.
39. The deposit of a revocation under s 148(4)(a)(i) is in time on the last business day preceding the day of the meeting, itself ("up to and including"), and not on the day after it, unless the instrument is deposited with the chairman on the day (ii). Asserted at 9, 10 and 11 June 2027.
40. Section 153(1) (the intermediary sends the documents and a request for instructions) and s 153(2) (no voting without written instructions) are cumulative: sending the request satisfies (1) and does not on its own permit voting under (2). Not asserted jointly: the two rules are separate.
41. Section 155(1)(a)(i) fixes both ends of the first period: it began on the date the corporation came into existence, or immediately after the last completed financial year, and ended not more than six months before the annual meeting. The rule asserts the start (the day after the previous year end, not that day and not two days after), the end at the boundary (the meeting on the last day is in time, the day after is not), and that the period cannot end after the meeting.
42. Section 158(2) is a prohibition on issuing, publishing or circulating copies; its condition is met by approval and signature under (1) and, where there is an auditor, the auditor's report. Asserted: the condition and the prohibition are separate rules.
43. Where a corporation has no auditor, the auditor's report required by s 155(1)(b) and s 158(2)(b) is not required ("if any"). Asserted.
44. A shareholder who has informed the corporation in writing that they do not want a copy is not owed one under s 159(1). Asserted.
45. For a resolution in lieu of an annual meeting, the copy to the Director is due "without delay after" it is signed (s 160(1)(a)), not twenty-one days before; the encoded rule takes the caller's judgment of "without delay". Asserted.
46. A person is disqualified from being an auditor (s 161(1)) when not independent, whether by the finding of fact or the deeming of (2)(b), and an exemption order under (5) lifts the disqualification and the duty to resign of (3). Asserted for each combination.
47. A s 163 resolution not to appoint an auditor does not last through the next annual meeting itself (F-163-until), and needs every shareholder's consent, including shareholders with no vote. Asserted.
48. A resignation takes effect on the later of the day the written resignation is sent and the day it specifies (s 164(2)); a specified day earlier than the sending day does not bring it forward. Asserted.
49. The shareholders' power to call a special meeting to fill an auditor vacancy (s 166(2)) arises at once if there are no directors, and otherwise only where there is no quorum of directors and the directors in office have not called within twenty-one days; with a quorum, the directors fill the vacancy under s 166(1). Asserted.
50. A person may accept appointment as replacement auditor without the retiring auditor's statement only once the fifteenth day after the request has passed with no reply (s 168(8)): on the fifteenth day itself the auditor can still reply. Asserted at 16 and 17 March.
51. Section 168(7) needs no qualification of the person (it is a bar until the statement is received); s 168(8) is for a person "otherwise qualified". Asserted: a person with the statement may accept whether or not otherwise qualified.
52. Section 169(2) lets an auditor rely on another auditor's report whether or not the statements are consolidated (s 169(4)); the rule has no input on consolidation, and that is the assertion.
53. A "majority" of the audit committee under s 171(1) is more than half of its members: two of four is not a majority. Asserted.
54. The offence of s 171(9) covers a director or officer who knowingly fails to comply with (6) or (8); an auditor's failure to inform the directors under (7) is not an offence under that subsection. Not asserted separately: there is no offence rule for (7).
55. A corporation is required to inform the Director of an error under s 171(8)(b) only if it is required to comply with s 160 (a distributing corporation with securities held by more than one person). Asserted.
56. An appointment of an auditor by a resolution in writing signed by every voting shareholder is not an "ordinary resolution" in the sense of s 2(1) (a majority of the votes cast); it is as valid as a resolution passed at a meeting because s 142(1)(a) says so, unless an auditor has submitted a statement under s 168(5). `the auditor is appointed by ordinary resolution within s 162(1)` counts the votes at a meeting only, and a meeting with no votes cast gives `FALSE`; the written route is answered by `a written resolution is as valid as if passed at a meeting within s 142(1)(a)`. The seat's appointment question asserts the no-votes case (it was first written the other way and was wrong). Asserted.

## What the stable binary does not accept

These are facts of the stable binary (1.6.98) that cost a rerun.

1. A genitive on the result of a call needs parentheses: `(`rule` arg)'s field`, not `` `rule` arg's field ``. The second is a parse error at the `'s` (`unexpected 's`). Found in `cb3-tests-part11-insider-trading.l4`, on `the penalty ceiling within s 130(4)`.
2. `cbca-core` does not re-export `cbca-core-definitions`. A module that uses `entity within s 2(1)` or `officer within s 2(1)` must `IMPORT `cbca-core-definitions`` explicitly, or the rule is "not found". `cb3-part11-insider-trading.l4` and its tests do this. The lead should expect it when merging.
3. A top-level definition named like a `Party` constructor (`the corporation`) compiled in a test file written with that name, and which of the two an argument resolved to was not checked; the fixtures are named `a connection: ...` so that the question does not arise.
4. The brief's rule is to bracket every `NOT`; every `NOT` in the module bodies is written `(NOT ...)`. The `#ASSERT NOT rule args` form is the one place a bare `NOT` heads a line, and it is the form the brief's own examples use.
5. A `DATE` minus a plain number is a `DATE` (days): `the record date for notice of a meeting when none is fixed within s 134(2)(a)` takes the day before the notice by `given MINUS 1`, and the month-end and leap-day cases are asserted.
6. A type whose name has a space must be in backticks where a record is built with `WITH`: `` (`Time limit` WITH `number of units` IS 18, `unit of time` IS `calendar months`) `` is accepted and `(Time limit WITH ...)` is a parser error at the next `(` (`unexpected (`). Both were run on 2026-10-22 against the keel's `the last day of`.
7. A list literal is `(LIST 4000, 2500)` and the empty list is `EMPTY`; both are in `cb3-tests-part12-proposals.l4` and `cb3-cases-seat.l4`.
8. A rule with no `GIVEN` is called as a bare name and read with a parenthesised genitive, `` (`the penalty ceiling within s 149(3)`)'s `maximum fine in dollars` ``; the seat's penalty-ceiling questions have no inputs and so no `GIVEN` line.
9. No restriction on how a nested call is laid out across lines was found: a call on one line with a nested call in parentheses, a call with the name alone on its line and the arguments on the next lines, and a call with arguments continued on a following indented line all parsed on 1.6.98 (three probes, 2026-10-22). An earlier belief in this piece that a layout rule existed could not be reproduced and is not relied on.

## What check.sh prints

Run as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` in this folder on 2026-10-22, with the stable binary 1.6.98 (sha256 `82ea44ad...263e`) and `JL4_LIBRARY_PATH` unset. It printed this, and exited 0:

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
cb3-cases-seat.l4                              0       687       0        0         0
cb3-nouns.l4                                   0         0       0        0         0
cb3-part11-insider-trading.l4                  0         0       0        0         0
cb3-part12-meetings.l4                         0         0       0        0         0
cb3-part12-proposals.l4                        0         0       0        0         0
cb3-part12-requisition-agreements.l4           0         0       0        0         0
cb3-part12-voting.l4                           0         0       0        0         0
cb3-part13-proxies.l4                          0         0       0        0         0
cb3-part14-1-diversity.l4                      0         0       0        0         0
cb3-part14-auditor.l4                          0         0       0        0         0
cb3-part14-statements.l4                       0         0       0        0         0
cb3-seat.l4                                    0         0       0        0         0
cb3-tests-part11-insider-trading.l4            0       193       0        0         0
cb3-tests-part12-meetings.l4                   0       109       0        0         0
cb3-tests-part12-proposals.l4                  0       109       0        0         0
cb3-tests-part12-requisition-agreements.l4       0        97       0        0         0
cb3-tests-part12-voting.l4                     0       110       0        0         0
cb3-tests-part13-proxies.l4                    0       224       0        0         0
cb3-tests-part14-1-diversity.l4                0        22       0        0         0
cb3-tests-part14-auditor.l4                    0       239       0        0         0
cb3-tests-part14-statements.l4                 0       110       0        0         0
cbca-core-control.l4                           0         0       0        0         0
cbca-core-definitions.l4                       0         0       0        0         0
cbca-core-isc.l4                               0         0       0        0         0
cbca-core.l4                                   0         0       0        0         0
TOTAL (25 modules)                             0      1900       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs ../../registers/source-bundle/R.S.C.-1985-c.-C-44.txt cb3-*.l4` printed `srcrefs check: 373 src: lines, 208 runs, 335 locators, 0 problems`.
The 1900 satisfied are 687 in the seat's cases and 1213 in the tests of layer 1; no assertion failed or was refused, and none is expected to fail.

## Before this is worth relying on

Nothing in this folder has been read against the Act by a lawyer, and the text it was written from is a converter's plain-text rendering of the English version only, current to 2026-09-30; the French version, equally authoritative, was not read. Status: `draft`.

1. Read the fork register. Twenty-nine entries mark where the text does not settle the reading and a reading was taken. The ones whose answer changes a duty or a deadline are F-133-earlier and F-160-earlier (two limits read as the earlier day), F-135-adjourn (adjournments counted in aggregate, at 30 and 90 days), F-139-tie (a tie is not a majority), F-143-6 (when the reimbursement arises), F-159-before (the day of the meeting is day 0), F-163-until (a resolution not to appoint an auditor is valid until, and not through, the next annual meeting) and F-150-3 ("(1) and (2)" read as either one). A lawyer should confirm each against the official text.
2. Every "prescribed" thing is a plain input because the regulations were not a source: the periods, forms, percentages and classes of corporation of ss 126 to 172.1 must come from the regulations, and an answer is only as good as the figure the caller supplies.
3. A court's or the Director's discretion is never decided; the layer says who may apply and on what ground, and the order is not predicted.
4. The seat questions have been run only against this encoding. Their wording has not been put in front of anyone in the seat, and the website's Interact form has not been tried on the inputs: eighteen of the questions have inputs that are a pair (a yes-or-no flag and a date or a number), and the form's handling of that pair is unchecked.
5. The questions' names are specific, but no check has been run against the other five pieces' names: after the merge into one folder a name defined by two modules cannot be used at all, and only the merge will show it.
6. `check.sh` was run with `L4_TARGET=unstable`, so its comparison against a second binary was skipped; nothing here was run on the `unstable` build of the language.
7. Layer 1 assumes `cbca-core*.l4` as it is: if the keel changes the meaning of `Time limit`, `Vote tally`, `Office` or the `s 2(1)` definitions, the deadlines and the voting answers move with it.

