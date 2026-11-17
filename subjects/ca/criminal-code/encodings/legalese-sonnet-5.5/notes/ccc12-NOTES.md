# NOTES.md -- ccc12: the Criminal Code (Canada), Part IX, Offences Against Rights of Property (ss 321 to 378), text lines 6511-7144

**Status (2026-11-13).** Layer 1 (nine section modules, a helper module, a regulative module and their tests) and layer 2 (`ccc12-seat.l4` and `ccc12-cases-seat.l4`) are written. Every number below was read from `check.sh`, from `python3 -I srcrefs.py check` (with and without `--strict`) or from a script in `work/` run on the files as they stand, on the stable build 1.6.110 with the main build 1.6.109 as the second reader; the last section prints `check.sh` as it ran. Run by agent `ccc12`, run `dst-ccc12`, model Sonnet 5.5, alone (no subagents).

**About the text.** The English text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation of the Criminal Code (R.S.C., 1985, c. C-46); it is not the official text, and nothing here is claimed verified against the official text. The French version is equally authoritative and is not among the sources. Every `-- src:` line is script-copied from that file, and `srcrefs.py check` and `check --strict` report 0 problems.

**Seat.** A person who is, or may be, accused of an offence under the Criminal Code (the accused), asking on facts they can state whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply, and what follows from a conviction. (Assumed, not ruled: Singapore's Penal Code is the model, as the maintainer instructed on 2026-11-09, but this is a plain seat layer; no charge-generator contract.) Provisions that address only an official (the Governor in Council in ss 347.1(3) and (4), the Attorney General in s 353(2.1), the court in ss 333.11, 334.1, 346.1, 348.1) are encoded in layer 1 for what they decide and reach layer 2 only for what they mean to the person; no question is asked from an official's seat.

## Where this part departs from the brief or the plan (stated, not hidden)

1. **Helper names begin `ccc12 `, not with a section label.** The brief wants every top-level name to begin with its provision's label. The three-valued connectives (`ccc12 and`, `ccc12 or`, `ccc12 not`, `ccc12 holds`), the limb and class helpers in `ccc12-logic.l4` the fixtures `ccc12 fixture ...` in `ccc12-tests-fixtures.l4`, the seat-side helper `ccc12 seat the general penalty of s 787(1) as the person states it` (in `ccc12-seat.l4`) and the case fixture `ccc12 fixture seat summary penalty` (in `ccc12-cases-seat.l4`) belong to no section; they carry the part prefix, which no other part can use. These are all the names in this part that do not begin with a section label (every other top-level name, type and constructor does). Every function, type and constructor that implements a provision begins `s <label> ...`.
2. **Layer 1 imports `ccc-core` only** (and `daydate` in `ccc12-part9-robbery-extortion.l4`, for the ten-year count). PLAN.md section 3 rule R4 makes an answer taken from another section an input named `s <label> <what is asked>`; the brief also says to IMPORT `ccc-definitions`. Both are followed where they can be: layer 1 takes every section 2 answer as an input (`s 2 <term>: ...`, MAYBE BOOLEAN, never turned from NOTHING into FALSE), and the seat layer imports `ccc-definitions` and calls `s 2 motor vehicle` and `s 2 steal` from facts the person can state. Elsewhere the person's yes or no is wrapped as `JUST b`.
3. **"PLAN.md section 8" does not exist.** The plan has six sections. The ccc12 seam lists are in section 6 (`### ccc12`) and the seam rules R1 to R5 in section 3; "Seams" below follows those.
4. **Punishment functions return `LIST OF Punishment`** (one limb per mode of proceeding), or `MAYBE (LIST OF Punishment)` where an input can be NOTHING, where PLAN.md R2 types the answer `Punishment`. A section such as s 334 states two limbs, so one `Punishment` cannot carry it; a consumer picks the limb by mode of proceeding, and `ccc12 the class of the offence from its limbs` gives the `Class of offence`.
5. **`s 342.1(2)` is two functions**, `s 342.1(2) computer data` and `s 342.1(2) computer system`, where PLAN.md names one ("computer data and computer system").
6. **Two inputs the plan does not list:** `s 52.1(2) essential infrastructure` (s 334.1(2)) and `s 25.1(1) public officer` (s 368.2), both from ccc1.

## The five rulings, copied word for word from the brief

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Where this part applies them: **E1** option C (per-section answers) everywhere, with one legal effect gathered by hand because the plan asks for a single answer: `s 322 the person commits theft` joins ss 322(1) and (2), which s 2 "steal" asks for (option B as guidance, no pilot); `s 362(1)` joins its own four paragraphs. **N2** option A: a flat negative counts as the text's no inside its own limit (the Hohfeld kinds stay in "Jural relations (ccc12)"; no `SHANT` rule is derived, because no flat negative in this range names a person it forbids: they are exceptions ("is not guilty", "does not apply", "is not a false pretence", "shall not be received", "no order of forfeiture may be made"), and the offence provisions ("Every one commits ... who ...") are decision functions). **Periods, where and scope**: every "where", "when" and period, and every scope limit with no "only" (NOTHING). **Delegated definitions, defences and until bars**: no site in this range (no definition hands itself to a list; no "it is a defence" and no "until" bar occurs; s 335(2) and s 347.1(1) hand a word to another section, not to a list, and take that section's answer as an input). **Case by case**: one fork line per site below.

## Coverage (ccc12)

**221 rows** cover all 624 non-blank lines of 6511-7144 (`work/checkrows.py`: no line missing, no line in two rows). Dispositions: **encoded 158**, **fork 31**, **inert 19** (reason 1: 17; reason 2: 2; reason 3: 0), **repealed or blank in this text 13**; total 221.

**Audit.** Rows before the audit: 221 (built by script from the text); after: 221 (the audit changed no row). Units counted independently by `work/audit.py` over the same lines: 77 sections (the plan says 77 section headings; 77 distinct section numbers in the text and in the rows), 135 subsection markers, 40 sections with no subsections, 34 defined terms (lines ending in a French equivalent), 13 repealed items; the 9 headings are PART IX and the eight division headings (Theft, Resembling Theft, Robbery and Extortion, Criminal Interest Rate, Breaking and Entering, Possession and Trafficking, False Pretences, Forgery). They reconcile with the rows: 9 headings + 8 lead-ins + 35 definitions (34 live + the repealed `data` of s 342.1(2)) + 167 section or subsection rows (135 markers + 40 undivided sections = 175, less the 8 lead-ins that are themselves a marker or a section line) + 2 repealed paragraphs `(a.1)` = 221. Paragraphs `(a)`, `(b)` ... fold into their subsection's row, and each is tested individually.

Each row has exactly one disposition. An `inert` row names its reason (1 not operative; 2 machinery; 3 repealed or blank text, none here because every repealed item is its own `repealed` row with the text as a constant). A `fork` row names its register entry. The L4 names are those of layer 1; a duty has its decision function and its regulative twin.

| row | text lines | what | disposition | L4 name(s) |
| --- | --- | --- | --- | --- |
| head IX | 6511-6514 | PART IX Offences Against Rights of Property; headings Interpretation, Definitions | inert: reason 1 (not operative) | - |
| s 321 lead-in | 6515 | 321 In this Part, | inert: reason 1 (not operative) | - |
| s 321 break | 6516-6518 | definition: break | encoded | `s 321 the person breaks` |
| s 321 credit card | 6519-6521 | definition: credit card | encoded | `s 321 the thing is a credit card` |
| s 321 document | 6522 | definition: document | encoded | `s 321 the thing is a document` |
| s 321 exchequer bill | 6523 | definition: exchequer bill | encoded | `s 321 the thing is an exchequer bill` |
| s 321 exchequer bill paper | 6524 | definition: exchequer bill paper | encoded | `s 321 the paper is exchequer bill paper` |
| s 321 false document | 6525-6530 | definition: false document | encoded | `s 321 the document is a false document` |
| s 321 revenue paper | 6531 | definition: revenue paper | encoded | `s 321 the paper is revenue paper` |
| head Theft | 6533 | division heading: Theft | inert: reason 1 (not operative) | - |
| s 322(1) | 6534-6539 | Theft: commits theft, (a)-(d) intents | encoded | `s 322(1) the person commits theft` |
| s 322(2) | 6540-6541 | Time when theft completed | fork: F-322-2 | `s 322(2) the person commits theft by moving the thing` |
| s 322(3) | 6542-6543 | Secrecy | encoded | `s 322(3) the absence of secrecy prevents the taking or conversion from being fraudulent` |
| s 322(4) | 6544-6545 | Purpose of taking | encoded | `s 322(4) the question is material` |
| s 322(5) | 6546-6547 | Wild living creature | encoded | `s 322(5) the person is deemed to have a special property or interest in the creature` |
| s 323(1) | 6548-6549 | Oysters: special property deemed | encoded | `s 323(1) the person is deemed to have a special property or interest in the oysters and oyster brood` |
| s 323(2) | 6550-6551 | Oyster bed: indictment sufficient | encoded | `s 323(2) the indictment is sufficient` |
| s 324 | 6552-6553 | Theft by bailee of things under seizure | encoded | `s 324 the bailee steals the thing under seizure` |
| s 325 | 6554-6557 | Agent pledging goods, when not theft | encoded | `s 325 the factor or agent commits theft by pledging or giving a lien on goods or documents of title to goods` |
| s 326(1) | 6558-6561 | Theft of telecommunication service | encoded | `s 326(1) the person commits theft of electricity, gas or a telecommunication service` |
| s 326(2) | 6562 | [Repealed, 2014, c. 31, s. 14] | repealed or blank in this text | `s 326(2) as the text shows it` |
| s 327(1) | 6563-6566 | Possession of device to obtain use of telecommunication facility or service | encoded | `s 327(1) the person commits the offence of possessing a device to obtain the use of a telecommunication facility or service`, `s 327(1) the punishment for the offence` |
| s 327(2) | 6567-6568 | Forfeiture | encoded | `s 327(2) the court may order the device forfeited to Her Majesty`, `s 327(2) the device may be ordered forfeited to Her Majesty`, `s 327(2) the device may be disposed of as the Attorney General directs` |
| s 327(3) | 6569-6570 | Limitation | encoded | `s 327(3) an order for forfeiture is barred` |
| s 327(4) | 6571-6574 | Definition of device | encoded | `s 327(4) the thing is a device` |
| s 328 | 6575-6581 | Theft by or from person having special property or interest | encoded | `s 328 the person may be convicted of theft notwithstanding the circumstance` |
| s 329 | 6582 | [Repealed, 2000, c. 12, s. 94] | repealed or blank in this text | `s 329 as the text shows it` |
| s 330(1) | 6583-6584 | Theft by person required to account | encoded | `s 330(1) the person commits theft by failing to account` |
| s 330(2) | 6585-6586 | Effect of entry in account | encoded | `s 330(2) a fraudulent conversion of the thing or the proceeds is deemed to have taken place` |
| s 331 | 6587-6588 | Theft by person holding power of attorney | encoded | `s 331 the person commits theft by disposing of property held under a power of attorney` |
| s 332(1) | 6589-6590 | Misappropriation of money held under direction | encoded | `s 332(1) the person commits theft by misappropriating money held under direction` |
| s 332(2) | 6591-6592 | Effect of entry in account | fork: F-UNLESS-N | `s 332(2) section 332 applies to the receipt` |
| s 333 | 6593-6594 | Taking ore for scientific purpose | encoded | `s 333 the person commits theft by reason only of taking a specimen of ore or mineral for exploration or scientific investigation` |
| s 333.1(1) | 6595-6598 | Motor vehicle theft: punishment limbs (a), (b) | encoded | `s 333.1(1) the person is guilty of the offence of motor vehicle theft`, `s 333.1(1) the punishment for motor vehicle theft` |
| s 333.1(2) | 6599-6600 | Subsequent offences | encoded | `s 333.1(2) the earlier conviction is considered to be an earlier offence` |
| s 333.1(3) | 6601-6602 | Motor vehicle theft when violence used, threatened or attempted | encoded | `s 333.1(3) the person is guilty of the offence of motor vehicle theft with violence`, `s 333.1(3) the punishment for motor vehicle theft with violence` |
| s 333.1(4) | 6603-6604 | Motor vehicle theft for criminal organization | encoded | `s 333.1(4) the person is guilty of the offence of motor vehicle theft for a criminal organization`, `s 333.1(4) the punishment for motor vehicle theft for a criminal organization` |
| s 333.11(1) | 6605-6606 | Sentences to be served consecutively -- breaking and entering | fork: F-DUTY-1 | `s 333.11(1) the court must order that the sentence be served consecutively`, `s 333.11(1) the sentence shall be served consecutively to the other sentence` |
| s 333.11(2) | 6607-6608 | Sentences to be served consecutively -- other offences | fork: F-DUTY-1 | `s 333.11(2) the court must order that the sentence be served consecutively`, `s 333.11(2) the sentence shall be served consecutively to the other sentence` |
| s 333.2(1) | 6609-6610 | Possession of device for purpose of committing theft | encoded | `s 333.2(1) the person commits the offence of possessing an electronic device for the purpose of committing motor vehicle theft` |
| s 333.2(2) | 6611-6612 | Distribution of device linked to theft | encoded | `s 333.2(2) the person commits the offence of distributing a device linked to motor vehicle theft` |
| s 333.2(3) | 6613-6616 | Punishment | encoded | `s 333.2(3) the punishment for the offence` |
| s 333.2(4) | 6617-6618 | Forfeiture | encoded | `s 333.2(4) the electronic device may be ordered forfeited to His Majesty` |
| s 333.2(5) | 6619-6620 | Limitation | encoded | `s 333.2(5) an order of forfeiture is barred` |
| s 334 | 6621-6628 | Punishment for theft | fork: F-334 | `s 334 the punishment for the person who commits theft` |
| s 334.1(1) | 6629-6630 | Aggravating circumstance -- stolen property | fork: F-DUTY-2 | `s 334.1(1) the court must consider the intent to sell or barter as an aggravating circumstance`, `s 334.1(1) the court shall consider as an aggravating circumstance that the offence was committed with intent to sell or barter the stolen property or to fraudulently return it to a retail merchant` |
| s 334.1(2) | 6631-6632 | Aggravating circumstance -- essential infrastructure | fork: F-DUTY-2 | `s 334.1(2) the court must consider the interference with an essential infrastructure as an aggravating circumstance`, `s 334.1(2) the court shall consider as an aggravating circumstance that the offence interfered with the access to or functioning of an essential infrastructure or caused it to be unsafe or unfit for use` |
| head Resembling Theft | 6634 | division heading: Offences Resembling Theft | inert: reason 1 (not operative) | - |
| s 335(1) | 6635-6636 | Taking motor vehicle or vessel or found therein without consent | encoded | `s 335(1) the person is guilty of the offence of taking a motor vehicle or vessel without consent, or of being an occupant of one taken without consent`, `s 335(1) the punishment for the offence` |
| s 335(1.1) | 6637-6638 | Exception | encoded | `s 335(1.1) subsection (1) applies to an occupant` |
| s 335(2) | 6639-6640 | Definition of vessel | encoded | `s 335(2) the thing is a vessel for the purposes of subsection (1)` |
| s 336 | 6641-6642 | Criminal breach of trust | encoded | `s 336 the person commits criminal breach of trust`, `s 336 the punishment for the offence` |
| s 337 | 6643 | [Repealed, 2018, c. 29, s. 33] | repealed or blank in this text | `s 337 as the text shows it` |
| s 338(1) | 6644-6649 | Fraudulently taking cattle or defacing brand | encoded | `s 338(1) the person is guilty of fraudulently taking cattle or defacing a brand`, `s 338(1) the punishment for the offence` |
| s 338(2) | 6650-6653 | Punishment for theft of cattle | encoded | `s 338(2) the person commits theft of cattle`, `s 338(2) the punishment for theft of cattle` |
| s 338(3) | 6654-6655 | Evidence of property in cattle | fork: F-UNLESS-P | `s 338(3) the evidence is proof that the cattle are owned by the registered owner of the brand or mark` |
| s 338(4) | 6656-6657 | Presumption from possession | fork: F-UNLESS-P | `s 338(4) the burden of proving that the cattle came lawfully into possession is on the accused` |
| s 339(1) | 6658-6662 | Taking possession, etc., of drift timber | encoded | `s 339(1) the person is guilty of the offence of taking possession of drift timber`, `s 339(1) the punishment for the offence` |
| s 339(2) | 6663-6664 | Dealer in second-hand goods | encoded | `s 339(2) the dealer in second-hand goods is guilty of an offence`, `s 339(2) the punishment for the offence` |
| s 339(3) | 6665-6666 | Search for timber unlawfully detained | encoded | `s 339(3) the peace officer may enter the place`, `s 339(3) the peace officer may enter into or on the place to ascertain whether the lumber is detained there` |
| s 339(4) | 6667-6668 | Evidence of property in timber | fork: F-UNLESS-P | `s 339(4) the mark or brand is proof that the lumber or lumbering equipment is the property of the registered owner` |
| s 339(5) | 6669-6670 | Presumption from possession | encoded | `s 339(5) the burden of proving that the lumber or lumbering equipment came lawfully into possession is on the accused` |
| s 339(6) lead-in | 6671-6672 | Definitions: In this section, | inert: reason 1 (not operative) | - |
| s 339(6) coastal waters of Canada | 6673 | definition | encoded | `s 339(6) the waters are coastal waters of Canada` |
| s 339(6) lumber | 6674 | definition | encoded | `s 339(6) the thing is lumber` |
| s 339(6) lumbering equipment | 6675 | definition | encoded | `s 339(6) the thing is lumbering equipment` |
| s 340 | 6676-6680 | Destroying documents of title | encoded | `s 340 the person commits the offence of destroying documents of title`, `s 340 the punishment for the offence` |
| s 341 | 6681-6684 | Fraudulent concealment | encoded | `s 341 the person commits the offence of fraudulent concealment`, `s 341 the punishment for the offence` |
| s 342(1) | 6685-6695 | Theft, forgery, etc., of credit card | encoded | `s 342(1) the person commits the offence of theft, forgery, etc., of a credit card`, `s 342(1) the punishment for the offence` |
| s 342(2) | 6696-6697 | Jurisdiction | encoded | `s 342(2) the accused may be tried and punished by the court in the place`, `s 342(2) proceedings in the place may not be commenced without the consent of the Attorney General of the province` |
| s 342(3) | 6698-6701 | Unauthorized use of credit card data | encoded | `s 342(3) the person commits the offence of unauthorized use of credit card data`, `s 342(3) the punishment for the offence` |
| s 342(4) lead-in | 6702-6703 | Definitions: In this section, | inert: reason 1 (not operative) | - |
| s 342(4) personal authentication information | 6704 | definition | encoded | `s 342(4) the information is personal authentication information` |
| s 342(4) traffic | 6705 | definition | encoded | `s 342(4) the person traffics in the credit card or credit card data` |
| s 342.01(1) | 6706-6709 | Instruments for copying credit card data or forging or falsifying credit cards | encoded | `s 342.01(1) the person commits the offence of possessing instruments for copying credit card data or forging or falsifying credit cards`, `s 342.01(1) the punishment for the offence` |
| s 342.01(2) | 6710-6711 | Forfeiture | fork: F-MAY-WHERE | `s 342.01(2) the thing may be ordered forfeited to Her Majesty` |
| s 342.01(3) | 6712-6713 | Limitation | encoded | `s 342.01(3) an order of forfeiture is barred` |
| s 342.1(1) | 6714-6719 | Unauthorized use of computer | encoded | `s 342.1(1) the person commits the offence of unauthorized use of a computer`, `s 342.1(1) the punishment for the offence` |
| s 342.1(2) lead-in | 6720-6721 | Definitions: In this section, | inert: reason 1 (not operative) | - |
| s 342.1(2) computer data | 6722 | definition | encoded | `s 342.1(2) computer data` |
| s 342.1(2) computer password | 6723 | definition | encoded | `s 342.1(2) computer password` |
| s 342.1(2) computer program | 6724 | definition | encoded | `s 342.1(2) computer program` |
| s 342.1(2) computer service | 6725 | definition | encoded | `s 342.1(2) computer service` |
| s 342.1(2) computer system | 6726-6730 | definition | encoded | `s 342.1(2) computer system` |
| s 342.1(2) data | 6731 | definition: data [Repealed, 2014, c. 31, s. 16] | repealed or blank in this text | `s 342.1(2) data as the text shows it` |
| s 342.1(2) electro-magnetic, acoustic, mechanical or other device | 6732 | definition | encoded | `s 342.1(2) electro-magnetic, acoustic, mechanical or other device` |
| s 342.1(2) function | 6733 | definition | encoded | `s 342.1(2) function` |
| s 342.1(2) intercept | 6734 | definition | encoded | `s 342.1(2) intercept` |
| s 342.1(2) traffic | 6735 | definition | encoded | `s 342.1(2) the person traffics in the computer password` |
| s 342.2(1) | 6736-6739 | Possession of device to obtain unauthorized use of computer system or to commit mischief | encoded | `s 342.2(1) the person commits the offence of possessing a device to obtain unauthorized use of a computer system or to commit mischief`, `s 342.2(1) the punishment for the offence` |
| s 342.2(2) | 6740-6741 | Forfeiture | encoded | `s 342.2(2) the device may be ordered forfeited to Her Majesty` |
| s 342.2(3) | 6742-6743 | Limitation | encoded | `s 342.2(3) an order of forfeiture is barred` |
| s 342.2(4) | 6744-6747 | Definition of device | encoded | `s 342.2(4) the thing is a device` |
| head Robbery and Extortion | 6749 | division heading: Robbery and Extortion | inert: reason 1 (not operative) | - |
| s 343 | 6750-6755 | Robbery | encoded | `s 343 the person commits robbery` |
| s 344(1) | 6756-6760,6762 | Robbery: punishment (a), (b) | encoded | `s 344(1)(a)(ii) seven years`, `s 344(1) the punishment for robbery`, `s 344(1)(a.1) as the text shows it` |
| s 344(1)(a.1) | 6761 | (a.1) [Repealed, 2022, c. 15, s. 12] | repealed or blank in this text | `s 344(1)(a.1) as the text shows it` |
| s 344(2) | 6763-6768 | Subsequent offences | fork: F-DATE, F-344-C | `s 344(2) ten years have elapsed between the convictions, not taking into account any time in custody`, `s 344(2) the earlier conviction is considered as an earlier offence` |
| s 344(3) | 6769-6770 | Sequence of convictions only | encoded | `s 344(3) the matter is to be considered for the purposes of subsection (2)` |
| s 345 | 6771-6772 | Stopping mail with intent | encoded | `s 345 the person commits the offence of stopping mail with intent`, `s 345 the punishment for the offence` |
| s 346(1) | 6773-6774 | Extortion | encoded | `s 346(1) the person commits extortion` |
| s 346(1.1) | 6775-6779,6781 | Extortion: punishment (a), (b) | encoded | `s 346(1.1)(a)(ii) seven years`, `s 346(1.1) the punishment for extortion`, `s 346(1.1)(a.1) as the text shows it` |
| s 346(1.1)(a.1) | 6780 | (a.1) [Repealed, 2022, c. 15, s. 13] | repealed or blank in this text | `s 346(1.1)(a.1) as the text shows it` |
| s 346(1.2) | 6782-6787 | Subsequent offences | fork: F-DATE, F-344-C | `s 346(1.2) the earlier conviction is considered as an earlier offence` |
| s 346(1.3) | 6788-6789 | Sequence of convictions only | encoded | `s 346(1.3) the matter is to be considered for the purposes of subsection (1.2)` |
| s 346(1.4) | 6790-6791 | Aggravating factor | fork: F-DUTY-3 | `s 346(1.4) the court must consider the sexual nature of the offence as an aggravating factor`, `s 346(1.4) the court must consider as an aggravating factor that the offence was of a sexual nature or committed for a sexual purpose` |
| s 346(2) | 6792-6793 | Saving | encoded | `s 346(2) the threat is a threat for the purposes of section 346` |
| s 346.1 | 6794-6795 | Sentences to be served consecutively | fork: F-DUTY-3 | `s 346.1 the court must order that the sentence be served consecutively`, `s 346.1 the sentence shall be served consecutively to the other sentence` |
| head Criminal Interest Rate | 6797 | division heading: Criminal Interest Rate | inert: reason 1 (not operative) | - |
| s 347(1) | 6798-6801 | Criminal interest rate | encoded | `s 347(1) the person commits the offence of receiving interest at a criminal rate`, `s 347(1) the punishment for the offence` |
| s 347(2) lead-in | 6802-6803 | Definitions: In this section, | inert: reason 1 (not operative) | - |
| s 347(2) credit advanced | 6804 | definition | encoded | `s 347(2) credit advanced` |
| s 347(2) criminal rate | 6805 | definition | encoded | `s 347(2) the rate is a criminal rate` |
| s 347(2) insurance charge | 6806 | definition | encoded | `s 347(2) the cost is an insurance charge` |
| s 347(2) interest | 6807 | definition | fork: F-INTEREST | `s 347(2) interest` |
| s 347(2) official fee | 6808 | definition | encoded | `s 347(2) the fee is an official fee` |
| s 347(2) overdraft charge | 6809 | definition | encoded | `s 347(2) the charge is an overdraft charge` |
| s 347(2) required deposit balance | 6810 | definition | encoded | `s 347(2) the amount is a required deposit balance` |
| s 347(3) | 6811-6812 | Presumption | fork: F-UNLESS-P | `s 347(3) the person is deemed to have knowledge of the nature of the payment and that it was received at a criminal rate` |
| s 347(4) | 6813-6814 | Proof of annual percentage rate | fork: F-UNLESS-P | `s 347(4) the certificate is proof of the annual percentage rate of interest without proof of the signature or official character of the person appearing to have signed it` |
| s 347(5) | 6815-6816 | Notice | fork: F-UNLESS-N | `s 347(5) the certificate may be received in evidence` |
| s 347(6) | 6817-6818 | Cross-examination with leave | encoded | `s 347(6) the accused or defendant may require the attendance of the actuary for the purposes of cross-examination`, `s 347(6) the accused may require the attendance of the actuary` |
| s 347(7) | 6819 | [Repealed, 2024, c. 17, s. 336] | repealed or blank in this text | `s 347(7) as the text shows it` |
| s 347(8) | 6820-6821 | Application | encoded | `s 347(8) section 347 applies to the transaction` |
| s 347.01(1) | 6822-6823 | Non-application -- agreements or arrangements | encoded | `s 347.01(1) section 347 applies to the agreement, arrangement, offer or advertisement` |
| s 347.01(2) | 6824-6825 | Non-application -- offers and advertisements | encoded | `s 347.01(2) section 347 applies to the offer or advertisement of an offer` |
| s 347.01(3) | 6826-6829 | Regulations | inert: reason 2 (machinery) | - |
| s 347.1(1) lead-in | 6830-6831 | Definitions: The following definitions apply in subsection (2) | inert: reason 1 (not operative) | - |
| s 347.1(1) interest | 6832 | definition | fork: F-INTEREST | `s 347.1(1) interest` |
| s 347.1(1) payday loan | 6833 | definition | encoded | `s 347.1(1) the advancement of money is a payday loan` |
| s 347.1(2) | 6834-6839 | Non-application -- person (payday loans) | fork: F-NEG-IF | `s 347.1(2) section 347 and section 2 of the Interest Act apply to the person` |
| s 347.1(2.1) | 6840-6841 | Regulation -- limit | inert: reason 2 (machinery) | - |
| s 347.1(2.2) | 6842-6843 | Clarification | encoded | `s 347.1(2.2) section 347 applies to the person` |
| s 347.1(3) | 6844-6845 | Designation of province | fork: F-DUTY-6 | `s 347.1(3) the Governor in Council shall designate the province`, `s 347.1(3) the Governor in Council must designate the province` |
| s 347.1(4) | 6846-6847 | Revocation | fork: F-DUTY-6 | `s 347.1(4) the Governor in Council shall revoke the designation`, `s 347.1(4) the Governor in Council must revoke the designation` |
| head Breaking and Entering | 6849 | division heading: Breaking and Entering | inert: reason 1 (not operative) | - |
| s 348(1) | 6850-6859 | Breaking and entering with intent, committing offence or breaking out | encoded | `s 348(1) the person commits the offence of breaking and entering, or of breaking out`, `s 348(1) the punishment for the offence` |
| s 348(2) | 6860-6865 | Presumptions | fork: F-UNLESS-P | `s 348(2)(a) the evidence is proof that the accused broke and entered the place or attempted to do so with intent to commit an indictable offence therein`, `s 348(2)(b) the evidence is proof that the accused broke out after committing an indictable offence therein or after entering with intent to commit one` |
| s 348(3) | 6866-6871 | Definition of place | encoded | `s 348(3) the thing is a place` |
| s 348.1 | 6872-6875 | Aggravating circumstance -- home invasion | fork: F-DUTY-4 | `s 348.1 the court shall consider as an aggravating circumstance that the dwelling-house was occupied`, `s 348.1 the court must consider the occupation of the dwelling-house as an aggravating circumstance` |
| s 349(1) | 6876-6877 | Being unlawfully in dwelling-house | encoded | `s 349(1) the person commits the offence of being unlawfully in a dwelling-house`, `s 349(1) the punishment for the offence` |
| s 349(2) | 6878-6879 | Presumption | fork: F-UNLESS-P | `s 349(2) the evidence is proof that the accused entered or was in the dwelling-house with intent to commit an indictable offence therein` |
| s 350 | 6880-6885 | Entrance | encoded | `s 350(a) the person enters`, `s 350(b) the person is deemed to have broken and entered` |
| s 351(1) | 6886-6889 | Possession of break-in instrument | encoded | `s 351(1) the person commits the offence of possessing a break-in instrument`, `s 351(1) the punishment for the offence` |
| s 351(2) | 6890-6893 | Disguise with intent | encoded | `s 351(2) the person commits the offence of being disguised with intent to commit an indictable offence`, `s 351(2) the punishment for the offence` |
| s 352 | 6894-6897 | Possession of instruments for breaking into coin-operated or currency exchange devices | encoded | `s 352 the person commits the offence of possessing an instrument for breaking into a coin-operated or currency exchange device`, `s 352 the punishment for the offence` |
| s 353(1) | 6898-6901 | Selling, etc., automobile master key | encoded | `s 353(1) the person commits the offence of dealing in an automobile master key without a licence`, `s 353(1) the punishment for the offence` |
| s 353(1.1) | 6902-6903 | Exception | encoded | `s 353(1.1) the police officer is guilty of an offence under subsection (1) by reason only of possessing an automobile master key for the purposes of the execution of the police officer's duties` |
| s 353(2) | 6904-6905 | Terms and conditions of licence | encoded | `s 353(2) the licence may contain the term or condition` |
| s 353(2.1) | 6906-6907 | Fees | encoded | `s 353(2.1) the Attorney General of a province may prescribe the fee` |
| s 353(3) | 6908-6911 | Record to be kept | fork: F-DUTY-5 | `s 353(3) the person shall keep a record of the transaction and produce it for inspection`, `s 353(3)(a) the record kept is a record of the transaction showing what the paragraph requires`, `s 353(3)(b) the person shall produce the record for inspection`, `s 353(3)(a) the seller must keep a record of the transaction`, `s 353(3)(b) the seller must produce the record for inspection at the request of a peace officer` |
| s 353(4) | 6912-6913 | Failure to comply with subsection (3) | encoded | `s 353(4) the person commits the offence of failing to comply with subsection (3)`, `s 353(4) the punishment for the offence` |
| s 353(5) lead-in | 6914-6915 | Definitions: The definitions in this subsection apply in this section | inert: reason 1 (not operative) | - |
| s 353(5) automobile master key | 6916 | definition | encoded | `s 353(5) the thing is an automobile master key` |
| s 353(5) licence | 6917 | definition | encoded | `s 353(5) the thing is a licence` |
| s 353.1(1) | 6918-6919 | Tampering with vehicle identification number | encoded | `s 353.1(1) the person commits the offence of tampering with a vehicle identification number` |
| s 353.1(2) | 6920-6921 | Definition of vehicle identification number | encoded | `s 353.1(2) the number or mark is a vehicle identification number` |
| s 353.1(3) | 6922-6923 | Exception | encoded | `s 353.1(3) the person commits an offence under subsection (1) by altering, removing or obliterating the number during regular maintenance or repair done for a legitimate purpose` |
| s 353.1(4) | 6924-6927 | Punishment | encoded | `s 353.1(4) the punishment for the offence` |
| head Possession and Trafficking | 6929 | division heading: Possession and Trafficking | inert: reason 1 (not operative) | - |
| s 354(1) | 6930-6933 | Possession of property obtained by crime | encoded | `s 354(1) the person commits the offence of possession of property obtained by crime` |
| s 354(2) | 6934-6937 | Obliterated vehicle identification number | fork: F-UNLESS-P | `s 354(2) the evidence is proof that the motor vehicle or part was obtained by an offence punishable by indictment` |
| s 354(3) | 6938-6939 | Definition of vehicle identification number | encoded | `s 354(3) the number or mark is a vehicle identification number` |
| s 354(4) | 6940-6941 | Exception | encoded | `s 354(4) the person is guilty of an offence under section 354 by reason only of possessing the property for the purposes of an investigation or in the execution of the peace officer's duties` |
| s 355 | 6942-6949 | Punishment | encoded | `s 355 the punishment for the offence under section 354` |
| s 355.1 | 6950-6951 | Definition of traffic | encoded | `s 355.1 the person traffics` |
| s 355.2 | 6952-6955 | Trafficking in property obtained by crime | encoded | `s 355.2 the person commits the offence of trafficking in property obtained by crime` |
| s 355.3 | 6956-6959 | In rem prohibition | encoded | `s 355.3 the importation or exportation is prohibited` |
| s 355.4 | 6960-6963 | Possession of property obtained by crime -- trafficking | encoded | `s 355.4 the person commits the offence of possession of property obtained by crime for the purpose of trafficking` |
| s 355.5 | 6964-6969 | Punishment | encoded | `s 355.5 the punishment for the offence under section 355.2 or 355.4` |
| s 356(1) | 6970-6978 | Theft from mail | encoded | `s 356(1) the person commits the offence of theft from mail` |
| s 356(2) | 6979-6980 | Allegation of value not necessary | encoded | `s 356(2) it is necessary to allege in the indictment or to prove on the trial that the thing had any value` |
| s 356(3) | 6981-6984 | Punishment | encoded | `s 356(3) the punishment for the offence` |
| s 357 | 6985-6988 | Bringing into Canada property obtained by crime | encoded | `s 357 the person commits the offence of bringing into Canada property obtained by crime`, `s 357 the punishment for the offence` |
| s 358 | 6989-6990 | Having in possession when complete | encoded | `s 358 the offence of having in possession is complete` |
| s 359 | 6991 | [Repealed, 2018, c. 29, s. 40] | repealed or blank in this text | `s 359 as the text shows it` |
| s 360 | 6992 | [Repealed, 2018, c. 29, s. 40] | repealed or blank in this text | `s 360 as the text shows it` |
| head False Pretences | 6994 | division heading: False Pretences | inert: reason 1 (not operative) | - |
| s 361(1) | 6995-6996 | False pretence | encoded | `s 361(1) the representation is a false pretence` |
| s 361(2) | 6997-6998 | Exaggeration | fork: F-UNLESS-N | `s 361(2) the exaggerated commendation or depreciation is a false pretence` |
| s 361(3) | 6999-7000 | Question of fact | encoded | `s 361(3) the question is a question of fact` |
| s 362(1) | 7001-7012 | False pretence or false statement | encoded | `s 362(1)(a) the person commits the offence of obtaining a thing by a false pretence`, `s 362(1)(b) the person commits the offence of obtaining credit by a false pretence or by fraud`, `s 362(1)(c) the person commits the offence of making a false statement in writing about financial condition or means to procure a benefit`, `s 362(1)(d) the person commits the offence of procuring a benefit on the faith of a false statement in writing`, `s 362(1) the person commits the offence of false pretence or false statement` |
| s 362(2) | 7013-7020 | Punishment (paragraph (1)(a)) | encoded | `s 362(2) the punishment for an offence under paragraph (1)(a)` |
| s 362(3) | 7021-7024 | Idem (paragraphs (1)(b), (c), (d)) | encoded | `s 362(3) the punishment for an offence under paragraph (1)(b), (c) or (d)` |
| s 362(4) | 7025-7026 | Presumption from cheque issued without funds | fork: F-UNLESS-P | `s 362(4) the thing is presumed to have been obtained by a false pretence` |
| s 362(5) | 7027-7028 | Definition of cheque | encoded | `s 362(5) the instrument is a cheque` |
| s 363 | 7029-7032 | Obtaining execution of valuable security by fraud | encoded | `s 363 the person commits the offence of obtaining execution of a valuable security by fraud`, `s 363 the punishment for the offence` |
| s 364(1) | 7033-7034 | Fraudulently obtaining food, beverage or accommodation | encoded | `s 364(1) the person commits the offence of fraudulently obtaining food, beverage or accommodation`, `s 364(1) the punishment for the offence` |
| s 364(2) | 7035-7043 | Presumption | fork: F-UNLESS-P | `s 364(2) the evidence is proof of fraud` |
| s 364(3) | 7044-7045 | Definition of cheque | encoded | `s 364(3) the instrument is a cheque` |
| s 365 | 7046 | [Repealed, 2018, c. 29, s. 41] | repealed or blank in this text | `s 365 as the text shows it` |
| head Forgery | 7048 | division heading: Forgery and Offences Resembling Forgery | inert: reason 1 (not operative) | - |
| s 366(1) | 7049-7052 | Forgery | encoded | `s 366(1) the person commits forgery` |
| s 366(2) | 7053-7057 | Making false document | encoded | `s 366(2) the act is making a false document` |
| s 366(3) | 7058-7059 | When forgery complete | encoded | `s 366(3) forgery is complete` |
| s 366(4) | 7060-7061 | Forgery complete though document incomplete | encoded | `s 366(4) forgery is complete notwithstanding that the false document is incomplete or does not purport to be binding in law` |
| s 366(5) | 7062-7063 | Exception | encoded | `s 366(5) the person commits forgery by reason only of making a false document in good faith at the request of a police force, the Canadian Forces or a government department or agency` |
| s 367 | 7064-7067 | Punishment for forgery | encoded | `s 367 the punishment for forgery` |
| s 368(1) | 7068-7073 | Use, trafficking or possession of forged document | encoded | `s 368(1) the person commits the offence of using, trafficking in or possessing a forged document` |
| s 368(1.1) | 7074-7077 | Punishment | encoded | `s 368(1.1) the punishment for the offence` |
| s 368(2) | 7078-7079 | Wherever forged | encoded | `s 368(2) the place where the document was forged is material` |
| s 368.1 | 7080-7081 | Forgery instruments | encoded | `s 368.1 the person commits the offence of possessing a forgery instrument`, `s 368.1 the punishment for the offence` |
| s 368.2 | 7082-7083 | Public officers acting in the course of their duties or employment | encoded | `s 368.2 the public officer is guilty of an offence under any of sections 366 to 368.1` |
| s 369 | 7084-7089 | Exchequer bill paper, public seals, etc. | encoded | `s 369 the person commits the offence of dealing in exchequer bill paper, revenue paper or public seals`, `s 369 the punishment for the offence` |
| s 370 | 7090 | [Repealed, 2018, c. 29, s. 42] | repealed or blank in this text | `s 370 as the text shows it` |
| s 371 | 7091 | [Repealed, 2018, c. 29, s. 42] | repealed or blank in this text | `s 371 as the text shows it` |
| s 372(1) | 7092-7093 | False information | encoded | `s 372(1) the person commits the offence of conveying false information` |
| s 372(2) | 7094-7095 | Indecent communications | encoded | `s 372(2) the person commits the offence of making an indecent communication` |
| s 372(3) | 7096-7097 | Harassing communications | encoded | `s 372(3) the person commits the offence of making harassing communications` |
| s 372(4) | 7098-7101 | Punishment | encoded | `s 372(4) the punishment for an offence under section 372` |
| s 373 | 7102 | [Repealed, R.S., 1985, c. 27 (1st Supp.), s. 53] | repealed or blank in this text | `s 373 as the text shows it` |
| s 374 | 7103-7107 | Drawing document without authority, etc. | encoded | `s 374 the person commits the offence of drawing or using a document without authority`, `s 374 the punishment for the offence` |
| s 375 | 7108-7109 | Obtaining, etc., by instrument based on forged document | encoded | `s 375 the person commits the offence of obtaining a thing by an instrument based on a forged document`, `s 375 the punishment for the offence` |
| s 376(1) | 7110-7116 | Counterfeiting stamp, etc. | encoded | `s 376(1) the person commits the offence of counterfeiting a stamp`, `s 376(1) the punishment for the offence` |
| s 376(2) | 7117-7123 | Counterfeiting mark | encoded | `s 376(2) the person commits the offence of counterfeiting a mark`, `s 376(2) the punishment for the offence` |
| s 376(3) lead-in | 7124-7125 | Definitions: In this section, | inert: reason 1 (not operative) | - |
| s 376(3) mark | 7126-7129 | definition | encoded | `s 376(3) the thing is a mark` |
| s 376(3) stamp | 7130 | definition | encoded | `s 376(3) the thing is a stamp` |
| s 377(1) | 7131-7136 | Damaging documents | encoded | `s 377(1) the person commits the offence of damaging documents`, `s 377(1) the punishment for the offence` |
| s 377(2) | 7137-7138 | Definition of election document | encoded | `s 377(2) the document is an election document` |
| s 378 | 7139-7143 | Offences in relation to registers | encoded | `s 378 the person commits an offence in relation to registers`, `s 378 the punishment for the offence` |

### What is inert, with its reason

- Reason 1 (not operative), 17 rows: head IX, s 321 lead-in, head Theft, head Resembling Theft, s 339(6) lead-in, s 342(4) lead-in, s 342.1(2) lead-in, head Robbery and Extortion, head Criminal Interest Rate, s 347(2) lead-in, s 347.1(1) lead-in, head Breaking and Entering, s 353(5) lead-in, head Possession and Trafficking, head False Pretences, head Forgery, s 376(3) lead-in.
- Reason 2 (machinery), 2 rows: s 347.01(3), s 347.1(2.1) (each is a power of the Governor in Council to make a regulation; the figure or type they would fix is an input where a rule turns on it: `the total cost of borrowing under the agreement does not or would not exceed the limit fixed by regulation` in s 347.1(2), and "provided for by regulation" in s 347.01(1) and (2)).
- Reason 3: none.
- Repealed or blank, 13 rows: s 326(2), s 329, s 337, s 342.1(2) data, s 344(1)(a.1), s 346(1.1)(a.1), s 347(7), s 359, s 360, s 365, s 370, s 371, s 373. Each is a constant `... as the text shows it` holding the text's own words (lint: each is a substring of the text).

## Fork register (ccc12)

Every ambiguity, the reading taken, the other reading, and the text that licenses each. `fork` rows in the coverage table point here. The case-by-case ruling (2026-11-05) asks for one fork line per site of an "unless" once met and of a duty whose "if" or "where" is unmet; those sites are listed one by one below. The conventions that rest on the rulings, not on a choice made here, are in "Marginal readings".

| id | rows | function | reading taken | other reading | text that licenses it |
| --- | --- | --- | --- | --- | --- |
| F-322-2 | s 322(2) | `s 322(2) the person commits theft by moving the thing`, joined with s 322(1) in `s 322 the person commits theft` | a second route to theft: where, with intent to steal anything, the person moves it, causes it to move or to be moved, or begins to cause it to become movable, the answer is JUST TRUE whether or not the elements of s 322(1) are met | s 322(2) only says when the theft that s 322(1) describes is complete, and adds no route: then moving a thing with intent to steal is, by itself, NOTHING and `s 322 the person commits theft` follows s 322(1) alone | heading "Time when theft completed"; "(2) A person commits theft when, with intent to steal anything, he moves it or causes it to move or to be moved, or begins to cause it to become movable." |
| F-334 | s 334 | `s 334 the punishment for the person who commits theft` | "Except where otherwise provided by law" is an input (`another provision of law provides the punishment`); when it is TRUE the answer is NOTHING (this part does not say what the other law provides) | the carve-out is read as the sections of this Part that state their own punishment for theft (s 333.1, s 338(2)), tested by section number: then the function would answer NOTHING for those and JUST TRUE otherwise, and an unnamed "other law" would be ignored | "334 Except where otherwise provided by law, every one who commits theft" |
| F-DATE | s 344(2), s 346(1.2) | `s 344(2) ten years have elapsed between the convictions, not taking into account any time in custody`; the same rule in `s 346(1.2)` | ten years have elapsed when the day of the later conviction, less the number of days in custody between the two convictions (an input), falls on or after the tenth anniversary of the day of the earlier conviction; the boundary day itself counts as elapsed (tested on both sides of the day) | the ten years are measured between the dates of commission, or between the dates of sentence; or the days in custody are added to the ten years rather than taken out of the interval (the two arithmetic readings differ by the custody days only) | "if 10 years have elapsed between the day on which the person was convicted of the earlier offence and the day on which the person was convicted of the offence for which sentence is being imposed, not taking into account any time in custody" |
| F-344-C | s 344(2), s 346(1.2) | paragraph (c) of `s 344(2) the earlier conviction is considered as an earlier offence` and of `s 346(1.2) ...` | "if a firearm was used in the commission of the offence" qualifies every offence that paragraph (c) names (ss 220, 236, 239, 272, 273, 279(1), 279.1 and, in s 344(2), 346; in s 346(1.2), 344) | the qualifier attaches only to the last-named offence (s 346 in s 344(2)(c); s 344 in s 346(1.2)(c)); the earlier ones would then count without a firearm | "(c) an offence under section 220, 236, 239, 272 or 273, subsection 279(1) or section 279.1 or 346 if a firearm was used in the commission of the offence." (s 346(1.2)(c) ends "or 344 if a firearm was used ...") |
| F-INTEREST | s 347(2) interest, s 347.1(1) interest | `s 347(2) interest` (s 347.1(1) says "interest has the same meaning as in subsection 347(2)" and calls it) | the person states the aggregate of all charges and expenses and, separately, the part of it that is each excluded kind (repayment of credit advanced, insurance charge, official fee, overdraft charge, required deposit balance and, for a mortgage or hypothec transaction, property taxes); the interest is the aggregate less those parts | the excluded kinds are not inside the aggregate the person states, so nothing is subtracted; or the property-tax exclusion is subtracted whether or not the transaction is a mortgage or hypothec transaction | "the aggregate of all charges and expenses ... but does not include any repayment of credit advanced or any insurance charge, official fee, overdraft charge, required deposit balance or, in the case of a mortgage or hypothec transaction, any amount required to be paid on account of property taxes" |
| F-UNLESS-N | s 332(2), s 347(5), s 361(2) | `s 332(2) section 332 applies to the receipt`; `s 347(5) the certificate may be received in evidence`; `s 361(2) the exaggerated commendation or depreciation is a false pretence` | a flat negative with an "unless" that has been met: NOTHING (the text stops excluding but does not itself say the opposite). Where the "unless" is not met the flat negative answers JUST FALSE | once the "unless" is met the answer is JUST TRUE (section 332 applies; the certificate may be received; the commendation is a false pretence) | s 332(2) "This section does not apply where ... unless the direction is in writing."; s 347(5) "shall not be received in evidence unless the party ... has given ... reasonable notice ... together with a copy"; s 361(2) "is not a false pretence unless it is carried to such an extent that it amounts to a fraudulent misrepresentation of fact" |
| F-UNLESS-P | s 338(3), s 338(4), s 339(4), s 347(3), s 347(4), s 348(2), s 349(2), s 354(2), s 362(4), s 364(2) | `s 338(3)`, `s 338(4)`, `s 339(4)`, `s 347(3)`, `s 347(4)`, `s 348(2)(a)` and `(b)`, `s 349(2)`, `s 354(2)`, `s 362(4)`, `s 364(2)` | a positive presumption or burden with "unless" or "in the absence of (any) evidence to the contrary", once the contrary is shown or the "unless" is met: JUST FALSE (the presumption does not operate, so the evidence is not proof / the burden is not on the accused) | NOTHING: the presumption does not operate, but the text does not say that the fact is not proved or that the burden is elsewhere | s 338(4) "... unless it appears that possession ... was without the knowledge and authority, sanction or approval of the accused"; s 362(4) "it shall be presumed to have been obtained by a false pretence, unless the court is satisfied by evidence that ..."; the others: "is, in the absence of (any) evidence to the contrary, proof ..." |
| F-DUTY-1 | s 333.11(1), s 333.11(2) | `s 333.11(1) the sentence shall be served consecutively to the other sentence` and `(2)`, with the regulative twins `s 333.11(1) the court must order ...` | a duty whose gate is unmet answers JUST FALSE (the text does not impose the duty), the regulative rule is then FULFILLED outright | NOTHING (the text neither imposes nor denies the duty on other facts) | "333.11 (1) A sentence imposed on a person for an offence under subsection 333.1(3) or (4) shall be served consecutively to any other sentence imposed on the person for an offence under section 348 arising out of the same event or series of events." (s 333.11(1): "... for an offence under section 348 arising out of the same event or series of events"; (2): a second or subsequent offence, "any other sentence ... for an offence arising out of the same event or series of events") |
| F-DUTY-2 | s 334.1(1), s 334.1(2) | `s 334.1(1)` and `s 334.1(2) the court shall consider as an aggravating circumstance ...`, with twins | gate unmet (an offence named in the subsection but the fact absent) answers JUST FALSE; an offence outside the named sections answers NOTHING (the list is not closed with "only") | NOTHING for an unmet gate | s 334.1(1) "when a court imposes a sentence for an offence referred to in section 322, 343, 348, 351 or 354, it shall consider as an aggravating circumstance the fact that the offence was committed with intent to sell or barter the stolen property or to fraudulently return it to a retail merchant"; (2) "... an offence referred to in section 322, 343 or 430, it shall consider as an aggravating circumstance the fact that the offence interfered with the access to or functioning of an essential infrastructure ..." |
| F-DUTY-3 | s 346(1.4), s 346.1 | `s 346(1.4) the court must consider as an aggravating factor ...` and `s 346.1 the sentence shall be served consecutively to the other sentence`, with twins | gate unmet answers JUST FALSE; an offence outside the named sections answers NOTHING | NOTHING for an unmet gate | s 346(1.4) "If a person has been determined by a court to be guilty of an offence under this section, the court that imposes the sentence must consider as an aggravating factor the fact that the offence was of a sexual nature or committed for a sexual purpose."; s 346.1 "A sentence imposed on a person for an offence under section 346 shall be served consecutively to any other sentence imposed on the person for an offence under any of sections 433 to 436 arising out of the same event or series of events." |
| F-DUTY-4 | s 348.1 | `s 348.1 the court shall consider as an aggravating circumstance that the dwelling-house was occupied`, with twin | gate unmet (offence named, a dwelling-house, occupied, knew or reckless, violence) answers JUST FALSE; an offence outside the named sections answers NOTHING | NOTHING for an unmet gate | s 348.1 "If a person is convicted of an offence under section 98 or 98.1, subsection 279(2) or section 343, 346 or 348 in relation to a dwelling-house, the court imposing the sentence on the person shall consider as an aggravating circumstance the fact that the dwelling-house was occupied at the time of the commission of the offence and that the person, in committing the offence, (a) knew that or was reckless as to whether the dwelling-house was occupied; and (b) used violence or threats of violence to a person or property." |
| F-DUTY-5 | s 353(3) | `s 353(3) the person shall keep a record of the transaction and produce it for inspection`, `s 353(3)(a)`, `s 353(3)(b)`, with twins | a person who has not sold an automobile master key is under no duty: JUST FALSE; the twin for (b) makes the peace officer's request the event that makes the duty to produce run (the text states no time for the request or the production) | NOTHING for a person who has not sold a key | "(3) Every one who sells an automobile master key (a) shall keep a record of the transaction ... (b) shall produce the record for inspection at the request of a peace officer." (s 353(4): failure to comply is an offence punishable on summary conviction) |
| F-DUTY-6 | s 347.1(3), s 347.1(4) | `s 347.1(3) the Governor in Council shall designate the province` and `(4) ... shall revoke the designation`, with twins | gate unmet (no request, no protective legislative measures, no limits on the total cost of borrowing; for (4) no request and the measures still in force) answers JUST FALSE | NOTHING for an unmet gate | s 347.1(3) "shall, by order and at the request of the lieutenant governor in council of a province, designate the province ... if the province has legislative measures ..."; (4) "shall, by order, revoke the designation ... if requested ... or if the legislative measures ... are no longer in force" |
| F-NEG-IF | s 347.1(2) | `s 347.1(2) section 347 and section 2 of the Interest Act apply to the person` | a flat negative with its own conditions ("do not apply to a person ... if (a) ... (a.1) ... (b) ... and (c)"): all four hold: JUST FALSE (the text says they do not apply); any fails: NOTHING (the subsection then says nothing, and s 347 itself decides) | JUST TRUE ("applies") when a condition fails, because the exclusion no longer holds | "(2) Section 347 and section 2 of the Interest Act do not apply to a person, other than a financial institution ..., who has entered into or has offered to enter into a payday loan agreement ... if (a) the amount of money that is or would be advanced under the agreement is $1,500 or less and the term of the agreement is or would be 62 days or less; (a.1) the total cost of borrowing under the agreement does not or would not exceed the limit fixed by regulation; (b) the person is licensed or otherwise specifically authorized under the laws of a province to enter into the agreement; and (c) the province is designated under subsection (3)." |
| F-MAY-WHERE | s 342.01(2) | `s 342.01(2) the thing may be ordered forfeited to Her Majesty` | a "may" function gated by "Where": a failed "Where a person is convicted of an offence under subsection (1)" answers JUST FALSE (ruling (b) of 2026-11-05); a thing not connected with the offence answers NOTHING. COUNT of "may" functions gated by "where", "when" or "upon" in this range: 1. COUNT of functions named "entitled": 0. Left for a lawyer, not decided here | NOTHING for the failed gate (the line of 2026-11-12 on functions named for a grant or power) | "(2) Where a person is convicted of an offence under subsection (1), any instrument, device, apparatus, material or thing in relation to which the offence was committed ... may, in addition to any other punishment that may be imposed, be ordered forfeited to Her Majesty" |

**Applications of the rulings, recorded so that a reviewer can find them** (no fork: the ruling decides): offence provisions ("Every one commits ... who ...") answer JUST FALSE when an element fails (the provision's own question); "when" and "as soon as" count as "where" (periods ruling (c)): `s 322(2)`, `s 350(a)`, `s 358`, `s 366(3)`; deeming provisions gated by "where" or "if" (`s 322(5)`, `s 323(1)`, `s 350(b)`) answer JUST FALSE when the gate is unmet; a bar whose gate is unmet answers JUST FALSE (`s 327(3)`, `s 333.2(5)`, `s 342.01(3)`, `s 342.2(3)`, `s 342(2)` second function); a flat negative with its own limit answers JUST FALSE inside the limit and NOTHING outside (`s 325`, `s 330(2)`, `s 333`, `s 335(1.1)`, `s 353(1.1)`, `s 353.1(3)`, `s 354(4)`, `s 366(5)`, `s 368.2`); an offence named by section number in a list the text does not close with "only" answers NOTHING when it is outside the list (`s 334.1`, `s 344(2)`, `s 346(1.2)`, `s 346.1`, `s 348.1`, `s 358`, `s 368.2`); "means ... and includes" is read as closed (the keel's F2: `s 321` document, "means any paper ... and includes a credit card, but does not include trademarks ..."); a bare "includes" is not closed (`s 327(4)`, `s 342.1(2)` computer service, function and intercept, `s 339(6)` lumbering equipment and coastal waters, `s 353(5)`).

### Name-test sweep of 2026-11-12

Every function of this part whose name contains "may", "permitted", "power", "entitled" or "authorized" or "authorised" was found by a substring grep over the names in the layer-1 modules and the seat (13 grant-named or bar-named functions that answer MAYBE BOOLEAN, three regulative twins in `ccc12-part9-duties.l4`, four names that only contain a word of the list), and tested against the three tests of `name-test-sweep.md`. Function names were not changed by the sweep.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 0 | 2 | 1 | 0 |

- **Flipped to NOTHING: 0.** No grant-named function answers JUST FALSE for a failed "if" gate. The brief carried the line of 2026-11-12, so the grants were written as NOTHING from the start; the one site that was first written the other way, `s 339(3)`, was corrected from JUST FALSE to NOTHING in the first pass (for a person who is not a peace officer), before this sweep. No fork line, assertion or coverage row changed.
- **Kept JUST FALSE, the text closes the gate: 2.** `s 347(5) the certificate may be received in evidence` (a grant-named function whose gate the text closes itself: "shall not be received in evidence unless the party ... has given ... reasonable notice"; JUST FALSE without the notice, NOTHING once the "unless" is met (fork F-UNLESS-N)); `s 342(2) proceedings in the place may not be commenced without the consent of the Attorney General of the province` (a bar, not a grant ("no proceedings ... shall be commenced in that place without the consent"); JUST FALSE where the place is not outside the province (a "where" gate unmet, ruling (b) of 2026-11-05), NOTHING once the consent is given).
- **Listed, "may" with a where/when/upon-kind gate: 1.** `s 342.01(2) the thing may be ordered forfeited to Her Majesty` (fork F-MAY-WHERE (the row above): "Where a person is convicted of an offence under subsection (1)"; a failed "Where" answers JUST FALSE by ruling (b) of 2026-11-05, and NOTHING is the other reading (the line of 2026-11-12 on grants)). ASSUMED, NOT RULED: the gates of the ten functions in the next line (a relative clause, "with leave of the court", a limit on the subject) are read as "if"-kind and not as the equivalents of "where", "when" or "upon" that the sweep lists, so their answer stays NOTHING; if a lawyer reads any of them as where-kind, ruling (b) of 2026-11-05 would give JUST FALSE for a failed gate, and the row above shows the cost: this is a question for the maintainer or a lawyer, not one to settle by sweep.
- **Listed, "entitled": 0.** No function name contains "entitled"; the word occurs once, inside an input name of `s 324` ("another person entitled thereto"), which is not a function.
- **Grants that already answered NOTHING outside their gate (10, not a column of the table because there was nothing to flip or list):** `s 327(2) the device may be ordered forfeited to Her Majesty` ("If a person is convicted of an offence under subsection (1) or paragraph 326(1)(b)"); `s 327(2) the device may be disposed of as the Attorney General directs` (the same sentence: a device "ordered forfeited" (an "if" gate)); `s 328 the person may be convicted of theft notwithstanding the circumstance` ("notwithstanding that anything ... was stolen" by one of five persons; the list is not closed with "only"); `s 333.2(4) the electronic device may be ordered forfeited to His Majesty` ("If a person is convicted of an offence under subsection (1) or (2)"); `s 339(3) the peace officer may enter into or on the place to ascertain whether the lumber is detained there` ("A peace officer who suspects, on reasonable grounds ..." (a relative clause; corrected from JUST FALSE to NOTHING in the first pass, before this sweep)); `s 342(2) the accused may be tried and punished by the court in the place` ("An accused who is charged with an offence under subsection (1)" (a relative clause), and four named places); `s 342.2(2) the device may be ordered forfeited to Her Majesty` ("If a person is convicted of an offence under subsection (1)"); `s 347(6) the accused or defendant may require the attendance of the actuary for the purposes of cross-examination` ("An accused or a defendant against whom a certificate ... is produced may, with leave of the court": a relative clause and "with leave of the court", assumed not a where/when/upon-kind gate; answer left NOTHING); `s 353(2) the licence may contain the term or condition` ("A licence issued by the Attorney General of a province as described in paragraph (1)(a) or (b)" (a limit on the subject)); `s 353(2.1) the Attorney General of a province may prescribe the fee` ("fees for the issue or renewal of licences as described in paragraph (1)(a) or (b)" (a limit on the object)).
- **Regulative twins (3, no MAYBE answer, so no JUST FALSE to flip):** `s 327(2) the court may order the device forfeited to Her Majesty`; `s 339(3) the peace officer may enter the place`; `s 347(6) the accused may require the attendance of the actuary`. Each is `IF the power exists EQUALS JUST TRUE THEN PARTY ... MAY ... ELSE FULFILLED`.
- **Names that only contain a word of the list (4, not grants):** s 331 the person commits theft by disposing of property held under a power of attorney ("power" is the instrument, not a grant); s 342(3) ... unauthorized use of credit card data; s 342.1(1) ... unauthorized use of a computer; s 342.2(1) ... unauthorized use of a computer system (all three are offences).
- **Seat questions named "may": 12.** Each answers as its layer-1 function does: 10 answer JUST TRUE or NOTHING, the question on `s 342.01(2)` JUST TRUE, JUST FALSE or NOTHING (F-MAY-WHERE) and the question on `s 347(5)` JUST FALSE or NOTHING (the bar).
- **"It is lawful ...": outside the sweep; scoped ("s N makes it lawful ..."): 0; unscoped and retitled: 0.** A grep of every `ccc12-*.l4` file for "it is lawful", "makes it lawful" and "lawful for" finds no hit, in a name or a comment, so nothing was retitled and no assertion carries a RECONCILED note for this.

## Jural relations (ccc12)

One row per provision that creates a relation, naming the holder of the right, privilege, power or immunity and the bearer of the correlative duty, no-right, liability or disability; each relation is stated once, neutrally. A row with `none` is a definition, a heading, a repealed item or a counting rule that creates no relation. Most provisions of Part IX create one: the Crown against the person (an offence), the court against the person convicted (a punishment, a forfeiture), the person against the Crown (an exception).

133 rows carry a relation and 88 are `none` (of 221).

| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| head IX | none | none | none | - |
| s 321 lead-in | none | none | none | - |
| s 321 break | none | none | none | - |
| s 321 credit card | none | none | none | - |
| s 321 document | none | none | none | - |
| s 321 exchequer bill | none | none | none | - |
| s 321 exchequer bill paper | none | none | none | - |
| s 321 false document | none | none | none | - |
| s 321 revenue paper | none | none | none | - |
| head Theft | none | none | none | - |
| s 322(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 322(1) the person commits theft` |
| s 322(2) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 322(2) the person commits theft by moving the thing` |
| s 322(3) | none | none | none | - |
| s 322(4) | none | none | none | - |
| s 322(5) | the person who keeps a wild living creature in captivity (deemed special property or interest) | everyone else | claim / duty (not to steal it) | `s 322(5) the person is deemed to have a special property or interest in the creature` |
| s 323(1) | the owner of marked oyster beds, layings or fisheries (deemed special property or interest) | everyone else | claim / duty (not to steal) | `s 323(1) the person is deemed to have a special property or interest in the oysters and oyster brood` |
| s 323(2) | the Crown (privilege to frame the indictment without naming the territorial division) | the accused | privilege / no-right | `s 323(2) the indictment is sufficient` |
| s 324 | the Crown (the public) | a bailee of things under lawful seizure | claim / duty (to produce and deliver) | `s 324 the bailee steals the thing under seizure` |
| s 325 | a factor or agent | the Crown | immunity / disability (a pledge within the limit is not theft) | `s 325 the factor or agent commits theft by pledging or giving a lien on goods or documents of title to goods` |
| s 326(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 326(1) the person commits theft of electricity, gas or a telecommunication service` |
| s 326(2) | none | none | none | - |
| s 327(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 327(1) the person commits the offence of possessing a device to obtain the use of a telecommunication facility or service`, `s 327(1) the punishment for the offence` |
| s 327(2) | the court (power to order forfeiture); the Attorney General (power to direct disposal) | the person whose thing it is | power / liability | `s 327(2) the device may be ordered forfeited to Her Majesty`, `s 327(2) the device may be disposed of as the Attorney General directs` (+ twin) |
| s 327(3) | the owner of the thing who was not a party to the offence | the court | immunity / disability (no order of forfeiture may be made) | `s 327(3) an order for forfeiture is barred` |
| s 327(4) | none | none | none | - |
| s 328 | the court (power to convict) | the person charged | power / liability | `s 328 the person may be convicted of theft notwithstanding the circumstance` |
| s 329 | none | none | none | - |
| s 330(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 330(1) the person commits theft by failing to account` |
| s 330(2) | a person who made a proper entry in a debtor and creditor account | the Crown | immunity / disability (no fraudulent conversion deemed) | `s 330(2) a fraudulent conversion of the thing or the proceeds is deemed to have taken place` |
| s 331 | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 331 the person commits theft by disposing of property held under a power of attorney` |
| s 332(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 332(1) the person commits theft by misappropriating money held under direction` |
| s 332(2) | a person who receives money on debtor-and-creditor terms | the Crown | immunity / disability (s 332 does not apply, unless the direction is in writing) | `s 332(2) section 332 applies to the receipt` |
| s 333 | a person who takes a specimen of ore or mineral for exploration or scientific investigation | the Crown | immunity / disability (not theft by reason only of that) | `s 333 the person commits theft by reason only of taking a specimen of ore or mineral for exploration or scientific investigation` |
| s 333.1(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 333.1(1) the person is guilty of the offence of motor vehicle theft`, `s 333.1(1) the punishment for motor vehicle theft` |
| s 333.1(2) | the court (power to count the earlier conviction) | the person being sentenced | power / liability | `s 333.1(2) the earlier conviction is considered to be an earlier offence` |
| s 333.1(3) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 333.1(3) the person is guilty of the offence of motor vehicle theft with violence`, `s 333.1(3) the punishment for motor vehicle theft with violence` |
| s 333.1(4) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 333.1(4) the person is guilty of the offence of motor vehicle theft for a criminal organization`, `s 333.1(4) the punishment for motor vehicle theft for a criminal organization` |
| s 333.11(1) | not named by the text | the court, or the person the section names | duty (the text names no holder of the correlative claim) | `s 333.11(1) the sentence shall be served consecutively to the other sentence` (+ twin) |
| s 333.11(2) | not named by the text | the court, or the person the section names | duty (the text names no holder of the correlative claim) | `s 333.11(2) the sentence shall be served consecutively to the other sentence` (+ twin) |
| s 333.2(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 333.2(1) the person commits the offence of possessing an electronic device for the purpose of committing motor vehicle theft` |
| s 333.2(2) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 333.2(2) the person commits the offence of distributing a device linked to motor vehicle theft` |
| s 333.2(3) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 333.2(3) the punishment for the offence` |
| s 333.2(4) | the court (power to order forfeiture); the Attorney General (power to direct disposal) | the person whose thing it is | power / liability | `s 333.2(4) the electronic device may be ordered forfeited to His Majesty` |
| s 333.2(5) | the owner of the thing who was not a party to the offence | the court | immunity / disability (no order of forfeiture may be made) | `s 333.2(5) an order of forfeiture is barred` |
| s 334 | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 334 the punishment for the person who commits theft` |
| s 334.1(1) | not named by the text | the court, or the person the section names | duty (the text names no holder of the correlative claim) | `s 334.1(1) the court shall consider as an aggravating circumstance that the offence was committed with intent to sell or barter the stolen property or to fraudulently return it to a retail merchant` (+ twin) |
| s 334.1(2) | not named by the text | the court, or the person the section names | duty (the text names no holder of the correlative claim) | `s 334.1(2) the court shall consider as an aggravating circumstance that the offence interfered with the access to or functioning of an essential infrastructure or caused it to be unsafe or unfit for use` (+ twin) |
| head Resembling Theft | none | none | none | - |
| s 335(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 335(1) the person is guilty of the offence of taking a motor vehicle or vessel without consent, or of being an occupant of one taken without consent`, `s 335(1) the punishment for the offence` |
| s 335(1.1) | an occupant who attempted to leave, or left | the Crown | immunity / disability (s 335(1) does not apply) | `s 335(1.1) subsection (1) applies to an occupant` |
| s 335(2) | none | none | none | - |
| s 336 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 336 the person commits criminal breach of trust`, `s 336 the punishment for the offence` |
| s 337 | none | none | none | - |
| s 338(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 338(1) the person is guilty of fraudulently taking cattle or defacing a brand`, `s 338(1) the punishment for the offence` |
| s 338(2) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 338(2) the person commits theft of cattle`, `s 338(2) the punishment for theft of cattle` |
| s 338(3) | the Crown (the benefit of the presumption of ownership) | the accused | power / liability (rebuttable) | `s 338(3) the evidence is proof that the cattle are owned by the registered owner of the brand or mark` |
| s 338(4) | the Crown (claim that the accused prove lawful possession) | the accused | claim / duty (the burden of proof) | `s 338(4) the burden of proving that the cattle came lawfully into possession is on the accused` |
| s 339(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 339(1) the person is guilty of the offence of taking possession of drift timber`, `s 339(1) the punishment for the offence` |
| s 339(2) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 339(2) the dealer in second-hand goods is guilty of an offence`, `s 339(2) the punishment for the offence` |
| s 339(3) | a peace officer who suspects on reasonable grounds | the occupier of the place | power / liability | `s 339(3) the peace officer may enter into or on the place to ascertain whether the lumber is detained there` (+ twin) |
| s 339(4) | the Crown (the benefit of the presumption of ownership) | the accused | power / liability (rebuttable) | `s 339(4) the mark or brand is proof that the lumber or lumbering equipment is the property of the registered owner` |
| s 339(5) | the Crown (claim that the accused prove lawful possession) | the accused | claim / duty (the burden of proof) | `s 339(5) the burden of proving that the lumber or lumbering equipment came lawfully into possession is on the accused` |
| s 339(6) lead-in | none | none | none | - |
| s 339(6) coastal waters of Canada | none | none | none | - |
| s 339(6) lumber | none | none | none | - |
| s 339(6) lumbering equipment | none | none | none | - |
| s 340 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 340 the person commits the offence of destroying documents of title`, `s 340 the punishment for the offence` |
| s 341 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 341 the person commits the offence of fraudulent concealment`, `s 341 the punishment for the offence` |
| s 342(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 342(1) the person commits the offence of theft, forgery, etc., of a credit card`, `s 342(1) the punishment for the offence` |
| s 342(2) | the court in the place named (power to try and punish); the Attorney General of the province of the offence (power to consent) | the accused | power / liability | `s 342(2) the accused may be tried and punished by the court in the place`, `s 342(2) proceedings in the place may not be commenced without the consent of the Attorney General of the province` |
| s 342(3) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 342(3) the person commits the offence of unauthorized use of credit card data`, `s 342(3) the punishment for the offence` |
| s 342(4) lead-in | none | none | none | - |
| s 342(4) personal authentication information | none | none | none | - |
| s 342(4) traffic | none | none | none | - |
| s 342.01(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 342.01(1) the person commits the offence of possessing instruments for copying credit card data or forging or falsifying credit cards`, `s 342.01(1) the punishment for the offence` |
| s 342.01(2) | the court (power to order forfeiture); the Attorney General (power to direct disposal) | the person whose thing it is | power / liability | `s 342.01(2) the thing may be ordered forfeited to Her Majesty` |
| s 342.01(3) | the owner of the thing who was not a party to the offence | the court | immunity / disability | `s 342.01(3) an order of forfeiture is barred` |
| s 342.1(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 342.1(1) the person commits the offence of unauthorized use of a computer`, `s 342.1(1) the punishment for the offence` |
| s 342.1(2) lead-in | none | none | none | - |
| s 342.1(2) computer data | none | none | none | - |
| s 342.1(2) computer password | none | none | none | - |
| s 342.1(2) computer program | none | none | none | - |
| s 342.1(2) computer service | none | none | none | - |
| s 342.1(2) computer system | none | none | none | - |
| s 342.1(2) data | none | none | none | - |
| s 342.1(2) electro-magnetic, acoustic, mechanical or other device | none | none | none | - |
| s 342.1(2) function | none | none | none | - |
| s 342.1(2) intercept | none | none | none | - |
| s 342.1(2) traffic | none | none | none | - |
| s 342.2(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 342.2(1) the person commits the offence of possessing a device to obtain unauthorized use of a computer system or to commit mischief`, `s 342.2(1) the punishment for the offence` |
| s 342.2(2) | the court (power to order forfeiture); the Attorney General (power to direct disposal) | the person whose thing it is | power / liability | `s 342.2(2) the device may be ordered forfeited to Her Majesty` |
| s 342.2(3) | the owner of the thing who was not a party to the offence | the court | immunity / disability (no order of forfeiture may be made) | `s 342.2(3) an order of forfeiture is barred` |
| s 342.2(4) | none | none | none | - |
| head Robbery and Extortion | none | none | none | - |
| s 343 | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 343 the person commits robbery` |
| s 344(1) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 344(1)(a)(ii) seven years`, `s 344(1) the punishment for robbery`, `s 344(1)(a.1) as the text shows it` |
| s 344(1)(a.1) | none | none | none | - |
| s 344(2) | the court (power to count the earlier offence for the minimum) | the person being sentenced | power / liability | `s 344(2) ten years have elapsed between the convictions, not taking into account any time in custody`, `s 344(2) the earlier conviction is considered as an earlier offence` |
| s 344(3) | none | none | none | - |
| s 345 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 345 the person commits the offence of stopping mail with intent`, `s 345 the punishment for the offence` |
| s 346(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 346(1) the person commits extortion` |
| s 346(1.1) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 346(1.1)(a)(ii) seven years`, `s 346(1.1) the punishment for extortion`, `s 346(1.1)(a.1) as the text shows it` |
| s 346(1.1)(a.1) | none | none | none | - |
| s 346(1.2) | the court (power to count the earlier offence for the minimum) | the person being sentenced | power / liability | `s 346(1.2) the earlier conviction is considered as an earlier offence` |
| s 346(1.3) | none | none | none | - |
| s 346(1.4) | none | none | none | - |
| s 346(2) | a person who threatens to institute civil proceedings | the Crown | immunity / disability (not an extortion threat) | `s 346(2) the threat is a threat for the purposes of section 346` |
| s 346.1 | not named by the text | the court, or the person the section names | duty (the text names no holder of the correlative claim) | `s 346.1 the sentence shall be served consecutively to the other sentence` (+ twin) |
| head Criminal Interest Rate | none | none | none | - |
| s 347(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 347(1) the person commits the offence of receiving interest at a criminal rate`, `s 347(1) the punishment for the offence` |
| s 347(2) lead-in | none | none | none | - |
| s 347(2) credit advanced | none | none | none | - |
| s 347(2) criminal rate | none | none | none | - |
| s 347(2) insurance charge | none | none | none | - |
| s 347(2) interest | none | none | none | - |
| s 347(2) official fee | none | none | none | - |
| s 347(2) overdraft charge | none | none | none | - |
| s 347(2) required deposit balance | none | none | none | - |
| s 347(3) | the Crown (the benefit of the presumption of knowledge) | a person who receives interest at a criminal rate | power / liability (a presumption the person may rebut) | `s 347(3) the person is deemed to have knowledge of the nature of the payment and that it was received at a criminal rate` |
| s 347(4) | the Crown (the benefit of the actuary's certificate as proof) | the accused or defendant | power / liability | `s 347(4) the certificate is proof of the annual percentage rate of interest without proof of the signature or official character of the person appearing to have signed it` |
| s 347(5) | the accused or defendant (claim to reasonable notice and a copy) | the party intending to produce the certificate | claim / duty | `s 347(5) the certificate may be received in evidence` |
| s 347(6) | the accused or defendant (power, with leave of the court, to require the actuary to attend) | the party who produced the certificate (and the actuary) | power / liability | `s 347(6) the accused or defendant may require the attendance of the actuary for the purposes of cross-examination` (+ twin) |
| s 347(7) | none | none | none | - |
| s 347(8) | a person whose transaction the Tax Rebate Discounting Act governs | the Crown | immunity / disability (s 347 does not apply) | `s 347(8) section 347 applies to the transaction` |
| s 347.01(1) | a party to an agreement or arrangement, offer or advertisement provided for by regulation | the Crown | immunity / disability (s 347 does not apply) | `s 347.01(1) section 347 applies to the agreement, arrangement, offer or advertisement` |
| s 347.01(2) | a person who makes the offer or advertisement | the Crown | immunity / disability (s 347 does not apply) | `s 347.01(2) section 347 applies to the offer or advertisement of an offer` |
| s 347.01(3) | none | none | none | - |
| s 347.1(1) lead-in | none | none | none | - |
| s 347.1(1) interest | none | none | none | - |
| s 347.1(1) payday loan | none | none | none | - |
| s 347.1(2) | a non-financial-institution payday lender within the four conditions | the Crown | immunity / disability (s 347 and s 2 of the Interest Act do not apply) | `s 347.1(2) section 347 and section 2 of the Interest Act apply to the person` |
| s 347.1(2.1) | none | none | none | - |
| s 347.1(2.2) | the payday lender protected before a new regulation | the Crown | immunity / disability (continues not to apply) | `s 347.1(2.2) section 347 applies to the person` |
| s 347.1(3) | the lieutenant governor in council of the province (claim to designation) | the Governor in Council | claim / duty | `s 347.1(3) the Governor in Council shall designate the province` (+ twin) |
| s 347.1(4) | the lieutenant governor in council of the province (claim to revocation on request) | the Governor in Council | claim / duty | `s 347.1(4) the Governor in Council shall revoke the designation` (+ twin) |
| head Breaking and Entering | none | none | none | - |
| s 348(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 348(1) the person commits the offence of breaking and entering, or of breaking out`, `s 348(1) the punishment for the offence` |
| s 348(2) | the Crown (the benefit of the presumption) | the accused | power / liability (a presumption the accused may rebut) | `s 348(2)(a) the evidence is proof that the accused broke and entered the place or attempted to do so with intent to commit an indictable offence therein`, `s 348(2)(b) the evidence is proof that the accused broke out after committing an indictable offence therein or after entering with intent to commit one` |
| s 348(3) | none | none | none | - |
| s 348.1 | not named by the text | the court | duty (the text names no holder of the correlative claim) | `s 348.1 the court shall consider as an aggravating circumstance that the dwelling-house was occupied` (+ twin) |
| s 349(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 349(1) the person commits the offence of being unlawfully in a dwelling-house`, `s 349(1) the punishment for the offence` |
| s 349(2) | the party relying on the evidence (the Crown) | the accused | power / liability (a presumption the accused may rebut) | `s 349(2) the evidence is proof that the accused entered or was in the dwelling-house with intent to commit an indictable offence therein` |
| s 350 | the person the text deems to hold the interest, or whose act is deemed | everyone else, and the court that must treat the fact as deemed | claim / duty (a deemed fact) | `s 350(a) the person enters`, `s 350(b) the person is deemed to have broken and entered` |
| s 351(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 351(1) the person commits the offence of possessing a break-in instrument`, `s 351(1) the punishment for the offence` |
| s 351(2) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 351(2) the person commits the offence of being disguised with intent to commit an indictable offence`, `s 351(2) the punishment for the offence` |
| s 352 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 352 the person commits the offence of possessing an instrument for breaking into a coin-operated or currency exchange device`, `s 352 the punishment for the offence` |
| s 353(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 353(1) the person commits the offence of dealing in an automobile master key without a licence`, `s 353(1) the punishment for the offence` |
| s 353(1.1) | a police officer specially authorized by the chief of the police force | the Crown | immunity / disability (not guilty by reason only of possession for the duties) | `s 353(1.1) the police officer is guilty of an offence under subsection (1) by reason only of possessing an automobile master key for the purposes of the execution of the police officer's duties` |
| s 353(2) | the Attorney General of a province (power to set terms and conditions) | the holder or applicant for a licence | power / liability | `s 353(2) the licence may contain the term or condition` |
| s 353(2.1) | the Attorney General of a province (power to prescribe fees) | the applicant for the issue or renewal of a licence | power / liability | `s 353(2.1) the Attorney General of a province may prescribe the fee` |
| s 353(3) | (a) the Crown (claim to a record); (b) a peace officer (claim to inspection on request) | a seller of an automobile master key | claim / duty | `s 353(3) the person shall keep a record of the transaction and produce it for inspection`, `s 353(3)(a) the record kept is a record of the transaction showing what the paragraph requires`, `s 353(3)(b) the person shall produce the record for inspection` (+ twin) |
| s 353(4) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 353(4) the person commits the offence of failing to comply with subsection (3)`, `s 353(4) the punishment for the offence` |
| s 353(5) lead-in | none | none | none | - |
| s 353(5) automobile master key | none | none | none | - |
| s 353(5) licence | none | none | none | - |
| s 353.1(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 353.1(1) the person commits the offence of tampering with a vehicle identification number` |
| s 353.1(2) | none | none | none | - |
| s 353.1(3) | a person who alters, removes or obliterates a number during regular maintenance or repair for a legitimate purpose | the Crown | immunity / disability (not an offence) | `s 353.1(3) the person commits an offence under subsection (1) by altering, removing or obliterating the number during regular maintenance or repair done for a legitimate purpose` |
| s 353.1(4) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 353.1(4) the punishment for the offence` |
| head Possession and Trafficking | none | none | none | - |
| s 354(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 354(1) the person commits the offence of possession of property obtained by crime` |
| s 354(2) | the party relying on the evidence (the Crown) | the accused | power / liability (a presumption the accused may rebut) | `s 354(2) the evidence is proof that the motor vehicle or part was obtained by an offence punishable by indictment` |
| s 354(3) | none | none | none | - |
| s 354(4) | a peace officer, or a person acting under a peace officer's direction | the Crown | immunity / disability (not guilty by reason only of that possession) | `s 354(4) the person is guilty of an offence under section 354 by reason only of possessing the property for the purposes of an investigation or in the execution of the peace officer's duties` |
| s 355 | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 355 the punishment for the offence under section 354` |
| s 355.1 | none | none | none | - |
| s 355.2 | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 355.2 the person commits the offence of trafficking in property obtained by crime` |
| s 355.3 | none | none | none | - |
| s 355.4 | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 355.4 the person commits the offence of possession of property obtained by crime for the purpose of trafficking` |
| s 355.5 | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 355.5 the punishment for the offence under section 355.2 or 355.4` |
| s 356(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 356(1) the person commits the offence of theft from mail` |
| s 356(2) | the Crown (privilege not to allege or prove value) | the accused | privilege / no-right | `s 356(2) it is necessary to allege in the indictment or to prove on the trial that the thing had any value` |
| s 356(3) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 356(3) the punishment for the offence` |
| s 357 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 357 the person commits the offence of bringing into Canada property obtained by crime`, `s 357 the punishment for the offence` |
| s 358 | none | none | none | - |
| s 359 | none | none | none | - |
| s 360 | none | none | none | - |
| head False Pretences | none | none | none | - |
| s 361(1) | none | none | none | - |
| s 361(2) | a person who exaggerates commendation or depreciation of quality | the Crown | immunity / disability (not a false pretence unless carried far enough) | `s 361(2) the exaggerated commendation or depreciation is a false pretence` |
| s 361(3) | none | none | none | - |
| s 362(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 362(1)(a) the person commits the offence of obtaining a thing by a false pretence`, `s 362(1)(b) the person commits the offence of obtaining credit by a false pretence or by fraud`, `s 362(1)(c) the person commits the offence of making a false statement in writing about financial condition or means to procure a benefit` |
| s 362(2) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 362(2) the punishment for an offence under paragraph (1)(a)` |
| s 362(3) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 362(3) the punishment for an offence under paragraph (1)(b), (c) or (d)` |
| s 362(4) | the party relying on the evidence (the Crown) | the accused | power / liability (a presumption the accused may rebut) | `s 362(4) the thing is presumed to have been obtained by a false pretence` |
| s 362(5) | none | none | none | - |
| s 363 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 363 the person commits the offence of obtaining execution of a valuable security by fraud`, `s 363 the punishment for the offence` |
| s 364(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 364(1) the person commits the offence of fraudulently obtaining food, beverage or accommodation`, `s 364(1) the punishment for the offence` |
| s 364(2) | the party relying on the evidence (the Crown) | the accused | power / liability (a presumption the accused may rebut) | `s 364(2) the evidence is proof of fraud` |
| s 364(3) | none | none | none | - |
| s 365 | none | none | none | - |
| head Forgery | none | none | none | - |
| s 366(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 366(1) the person commits forgery` |
| s 366(2) | none | none | none | - |
| s 366(3) | none | none | none | - |
| s 366(4) | none | none | none | - |
| s 366(5) | a person who makes a false document in good faith at the request of a police force, the Canadian Forces or a government department or agency | the Crown | immunity / disability | `s 366(5) the person commits forgery by reason only of making a false document in good faith at the request of a police force, the Canadian Forces or a government department or agency` |
| s 367 | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 367 the punishment for forgery` |
| s 368(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 368(1) the person commits the offence of using, trafficking in or possessing a forged document` |
| s 368(1.1) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 368(1.1) the punishment for the offence` |
| s 368(2) | the Crown (privilege: the place of forging need not be shown) | the accused | privilege / no-right | `s 368(2) the place where the document was forged is material` |
| s 368.1 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 368.1 the person commits the offence of possessing a forgery instrument`, `s 368.1 the punishment for the offence` |
| s 368.2 | a public officer acting only to establish or maintain a covert identity | the Crown | immunity / disability | `s 368.2 the public officer is guilty of an offence under any of sections 366 to 368.1` |
| s 369 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 369 the person commits the offence of dealing in exchequer bill paper, revenue paper or public seals`, `s 369 the punishment for the offence` |
| s 370 | none | none | none | - |
| s 371 | none | none | none | - |
| s 372(1) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 372(1) the person commits the offence of conveying false information` |
| s 372(2) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 372(2) the person commits the offence of making an indecent communication` |
| s 372(3) | the Crown (the public, through the prosecution) | any person | claim / duty (not to do the act described) | `s 372(3) the person commits the offence of making harassing communications` |
| s 372(4) | the court (power to impose the stated punishment on conviction) | the person convicted | power / liability | `s 372(4) the punishment for an offence under section 372` |
| s 373 | none | none | none | - |
| s 374 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 374 the person commits the offence of drawing or using a document without authority`, `s 374 the punishment for the offence` |
| s 375 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 375 the person commits the offence of obtaining a thing by an instrument based on a forged document`, `s 375 the punishment for the offence` |
| s 376(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 376(1) the person commits the offence of counterfeiting a stamp`, `s 376(1) the punishment for the offence` |
| s 376(2) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 376(2) the person commits the offence of counterfeiting a mark`, `s 376(2) the punishment for the offence` |
| s 376(3) lead-in | none | none | none | - |
| s 376(3) mark | none | none | none | - |
| s 376(3) stamp | none | none | none | - |
| s 377(1) | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 377(1) the person commits the offence of damaging documents`, `s 377(1) the punishment for the offence` |
| s 377(2) | none | none | none | - |
| s 378 | the Crown (the public, through the prosecution); the court (power to impose the stated punishment on conviction) | any person; the person convicted | claim / duty (not to do the act described); power / liability | `s 378 the person commits an offence in relation to registers`, `s 378 the punishment for the offence` |

## Marginal readings for a lawyer (ccc12)

Two readings the brief leaves to a lawyer, taken here as the status quo. **(a)** A failed "if" (and "where", "when") counts as the text's own no, clause by clause, within the provision that holds it; flat negatives count as the text saying no. **(b)** A prohibition or grant limited by its own wording does not. The other reading of (a): a failed gate is silent, NOTHING. The other reading of (b): a case outside the limit is the text's no, JUST FALSE.

**Tally over the 267 layer-1 functions** (`work/lint.py` reads the `FALSE-kind` and `NOTHING-kind` comments; the classes are assigned by the first matching word of the quoted text, so they are a guide, not a proof): 182 JUST FALSE branches (37 "means" definitions; 56 offence elements; 29 "if", "where", "when", "unless" or "until" gates [reading (a)]; 23 flat negatives [reading (a), N2]; 37 other), 125 NOTHING branches (51 "limited by its own wording" [reading (b)]).

The branches that rest on (a) are the `gate` and `negative` counts above, function by function in the table; those that rest on (b) are the NOTHING branches tagged `limited by its own wording`. A reviewer who takes the other reading changes exactly those branches and no others.

| function | JUST FALSE on a gate (a) | JUST FALSE on a flat negative (a) | NOTHING, limited by its own wording (b) |
| --- | --- | --- | --- |
| s 321 the thing is a document | 0 | 1 | 0 |
| s 322(4) the question is material | 0 | 2 | 0 |
| s 322(5) the person is deemed to have a special property or interest in the creature | 1 | 0 | 0 |
| s 323(1) the person is deemed to have a special property or interest in the oysters and oyster brood | 1 | 0 | 0 |
| s 323(2) the indictment is sufficient | 0 | 0 | 1 |
| s 324 the bailee steals the thing under seizure | 2 | 0 | 0 |
| s 325 the factor or agent commits theft by pledging or giving a lien on goods or documents of title to goods | 0 | 1 | 1 |
| s 327(2) the device may be disposed of as the Attorney General directs | 0 | 0 | 1 |
| s 327(2) the device may be ordered forfeited to Her Majesty | 0 | 0 | 1 |
| s 330(2) a fraudulent conversion of the thing or the proceeds is deemed to have taken place | 0 | 1 | 1 |
| s 332(2) section 332 applies to the receipt | 1 | 0 | 1 |
| s 333 the person commits theft by reason only of taking a specimen of ore or mineral for exploration or scientific investigation | 0 | 0 | 1 |
| s 333.2(4) the electronic device may be ordered forfeited to His Majesty | 0 | 0 | 1 |
| s 333.2(5) an order of forfeiture is barred | 0 | 1 | 0 |
| s 334 the punishment for the person who commits theft | 0 | 0 | 1 |
| s 334.1(1) the court shall consider as an aggravating circumstance that the offence was committed with intent to sell or barter the stolen property or to fraudulently return it to a retail merchant | 0 | 0 | 1 |
| s 334.1(2) the court shall consider as an aggravating circumstance that the offence interfered with the access to or functioning of an essential infrastructure or caused it to be unsafe or unfit for use | 0 | 0 | 1 |
| s 335(1.1) subsection (1) applies to an occupant | 0 | 1 | 1 |
| s 338(4) the burden of proving that the cattle came lawfully into possession is on the accused | 3 | 0 | 0 |
| s 339(3) the peace officer may enter into or on the place to ascertain whether the lumber is detained there | 0 | 0 | 2 |
| s 339(4) the mark or brand is proof that the lumber or lumbering equipment is the property of the registered owner | 0 | 0 | 1 |
| s 339(5) the burden of proving that the lumber or lumbering equipment came lawfully into possession is on the accused | 1 | 0 | 0 |
| s 342(2) proceedings in the place may not be commenced without the consent of the Attorney General of the province | 1 | 0 | 1 |
| s 342(2) the accused may be tried and punished by the court in the place | 0 | 0 | 2 |
| s 342.01(2) the thing may be ordered forfeited to Her Majesty | 1 | 0 | 1 |
| s 342.01(3) an order of forfeiture is barred | 0 | 1 | 0 |
| s 342.1(2) electro-magnetic, acoustic, mechanical or other device | 0 | 1 | 0 |
| s 342.2(2) the device may be ordered forfeited to Her Majesty | 0 | 0 | 1 |
| s 342.2(3) an order of forfeiture is barred | 0 | 1 | 0 |
| s 344(2) ten years have elapsed between the convictions, not taking into account any time in custody | 1 | 0 | 0 |
| s 344(2) the earlier conviction is considered as an earlier offence | 1 | 0 | 0 |
| s 344(3) the matter is to be considered for the purposes of subsection (2) | 0 | 2 | 0 |
| s 346(1.2) the earlier conviction is considered as an earlier offence | 1 | 0 | 0 |
| s 346(1.3) the matter is to be considered for the purposes of subsection (1.2) | 0 | 2 | 0 |
| s 346(1.4) the court must consider as an aggravating factor that the offence was of a sexual nature or committed for a sexual purpose | 1 | 0 | 0 |
| s 346(2) the threat is a threat for the purposes of section 346 | 0 | 1 | 0 |
| s 346.1 the sentence shall be served consecutively to the other sentence | 0 | 0 | 1 |
| s 347(3) the person is deemed to have knowledge of the nature of the payment and that it was received at a criminal rate | 1 | 0 | 0 |
| s 347(4) the certificate is proof of the annual percentage rate of interest without proof of the signature or official character of the person appearing to have signed it | 0 | 0 | 1 |
| s 347(5) the certificate may be received in evidence | 1 | 0 | 1 |
| s 347(6) the accused or defendant may require the attendance of the actuary for the purposes of cross-examination | 0 | 0 | 1 |
| s 347(8) section 347 applies to the transaction | 0 | 1 | 1 |
| s 347.01(1) section 347 applies to the agreement, arrangement, offer or advertisement | 0 | 1 | 0 |
| s 347.01(2) section 347 applies to the offer or advertisement of an offer | 1 | 0 | 1 |
| s 347.1(2) section 347 and section 2 of the Interest Act apply to the person | 0 | 1 | 1 |
| s 347.1(2.2) section 347 applies to the person | 1 | 0 | 1 |
| s 347.1(3) the Governor in Council shall designate the province | 1 | 0 | 0 |
| s 347.1(4) the Governor in Council shall revoke the designation | 1 | 0 | 0 |
| s 348(2)(a) the evidence is proof that the accused broke and entered the place or attempted to do so with intent to commit an indictable offence therein | 0 | 0 | 1 |
| s 348(2)(b) the evidence is proof that the accused broke out after committing an indictable offence therein or after entering with intent to commit one | 0 | 0 | 1 |
| s 348.1 the court shall consider as an aggravating circumstance that the dwelling-house was occupied | 0 | 0 | 1 |
| s 349(2) the evidence is proof that the accused entered or was in the dwelling-house with intent to commit an indictable offence therein | 0 | 0 | 1 |
| s 350(a) the person enters | 1 | 0 | 0 |
| s 350(b) the person is deemed to have broken and entered | 1 | 0 | 0 |
| s 353(1.1) the police officer is guilty of an offence under subsection (1) by reason only of possessing an automobile master key for the purposes of the execution of the police officer's duties | 0 | 1 | 1 |
| s 353(2) the licence may contain the term or condition | 0 | 0 | 1 |
| s 353(2.1) the Attorney General of a province may prescribe the fee | 0 | 0 | 1 |
| s 353.1(3) the person commits an offence under subsection (1) by altering, removing or obliterating the number during regular maintenance or repair done for a legitimate purpose | 0 | 1 | 1 |
| s 354(2) the evidence is proof that the motor vehicle or part was obtained by an offence punishable by indictment | 0 | 0 | 1 |
| s 354(4) the person is guilty of an offence under section 354 by reason only of possessing the property for the purposes of an investigation or in the execution of the peace officer's duties | 0 | 1 | 2 |
| s 355.3 the importation or exportation is prohibited | 1 | 0 | 1 |
| s 356(2) it is necessary to allege in the indictment or to prove on the trial that the thing had any value | 0 | 1 | 1 |
| s 358 the offence of having in possession is complete | 1 | 0 | 1 |
| s 361(2) the exaggerated commendation or depreciation is a false pretence | 0 | 1 | 2 |
| s 361(3) the question is a question of fact | 0 | 0 | 1 |
| s 362(4) the thing is presumed to have been obtained by a false pretence | 1 | 0 | 0 |
| s 364(2) the evidence is proof of fraud | 0 | 0 | 1 |
| s 366(3) forgery is complete | 1 | 0 | 0 |
| s 366(4) forgery is complete notwithstanding that the false document is incomplete or does not purport to be binding in law | 1 | 0 | 1 |
| s 366(5) the person commits forgery by reason only of making a false document in good faith at the request of a police force, the Canadian Forces or a government department or agency | 0 | 0 | 1 |
| s 368(2) the place where the document was forged is material | 1 | 0 | 1 |
| s 368.2 the public officer is guilty of an offence under any of sections 366 to 368.1 | 0 | 0 | 2 |

### Reading a result: FALSE and NOTHING (ccc12)

In this Part, **JUST TRUE** is the text's yes on the facts given. **JUST FALSE** is the text's own no, in the words the layer-1 comment quotes: an offence whose element is absent ("Every one commits theft who ..."), a "means" definition the thing does not fit, an "if", "where", "when" or "unless" the facts do not meet, a flat negative ("does not commit theft by pledging ...", "is not a false pretence"), a bar ("no order of forfeiture may be made"). **NOTHING** means the text does not answer on these facts: the list is not closed with "only" (an offence outside the sections a rule names), "includes", a term left undefined, a power or a duty limited by its own wording and the facts fall outside it, an answer that belongs to another section or to a regulation and was not given. A caller must never turn NOTHING into FALSE: "not an offence under s 322" is JUST FALSE, "the text of Part IX does not say" is NOTHING. For a punishment, the answer is the list of limbs the section states, one per mode of proceeding; a limb that says only "an offence punishable on summary conviction" takes its figures from s 787(1), which is outside Part IX, so the person (or the form) supplies them. A duty's regulative rule is FULFILLED outright where its gate is not JUST TRUE, so FULFILLED there means "no duty arose", not "the duty was performed".

## Seams (ccc12)

PLAN.md section 6 (`### ccc12`) and rules R1 to R5 of section 3. R1: offences named by section number are tested against the core record `Provision of the Code` (`section` as a decimal, `subsection` as a string): done in ss 334.1, 344(2), 346(1.2), 346.1, 348.1, 358, 368.2 (368.1 is inside "366 to 368.1" and 369 is outside). R3: Part-scoped definitions are encoded here under their own label. R4: answers from another section are inputs.

**This part provides (names other parts ask for).** `s 322 the person commits theft` (MAYBE BOOLEAN; what s 2 "steal" asks); `s 321 the person breaks`; `s 321 the thing is a document`; `s 342.1(2) computer data`; `s 342.1(2) computer system` (two functions where the plan names one); `s 321 the document is a false document`, `s 321 the thing is a credit card`; and, for ss 718.2, 718.3, 743.1 (ccc26), ss 463 to 465 (ccc14), ss 21 to 24 (ccc1), ss 515 and 522 (ccc20) and ss 553 to 555 (ccc21), the function that states the punishment of each offence of the Part, in the offence's own section or in the section that states it (`s 334` for the forms of theft, `s 344(1)` for robbery, `s 346(1.1)` for extortion, `s 355` for s 354, `s 355.5` for ss 355.2 and 355.4, `s 367` for forgery; `LIST OF Punishment`, see the departures), and the helper `ccc12 the class of the offence from its limbs`. Each name above was checked to exist as a top-level name in the `.l4` files when this file was generated.

**This part asks (inputs taken, each named for the section it comes from; counted from the signatures by `work/sigs.py`).**

| input | type | functions that take it | sections |
| --- | --- | --- | --- |
| s 2 cattle | MAYBE BOOLEAN | 2 | 338(1), 338(2) |
| s 2 criminal organization | MAYBE BOOLEAN | 3 | 333.1(4), 344(1), 346(1.1) |
| s 2 document of title to goods | MAYBE BOOLEAN | 1 | 340 |
| s 2 document of title to lands | MAYBE BOOLEAN | 1 | 340 |
| s 2 dwelling-house | MAYBE BOOLEAN | 3 | 348(1), 348.1, 349(1) |
| s 2 firearm | MAYBE BOOLEAN | 2 | 344(1), 346(1.1) |
| s 2 motor vehicle | MAYBE BOOLEAN | 5 | 333.1(1), 333.1(3), 333.1(4), 335(1), 353.1(1) |
| s 2 offensive weapon | MAYBE BOOLEAN | 1 | 343 |
| s 2 peace officer | MAYBE BOOLEAN | 3 | 324, 339(3), 354(4) |
| s 2 public officer | MAYBE BOOLEAN | 1 | 324 |
| s 2 steal | MAYBE BOOLEAN | 3 | 342(1), 343, 356(1) |
| s 2 testamentary instrument | MAYBE BOOLEAN | 4 | 334, 340, 355, 362(2) |
| s 2 trustee | MAYBE BOOLEAN | 1 | 336 |
| s 2 valuable security | MAYBE BOOLEAN | 3 | 332(1), 340, 363 |
| s 2.1 prohibited firearm | MAYBE BOOLEAN | 2 | 344(1), 346(1.1) |
| s 2.1 restricted firearm | MAYBE BOOLEAN | 2 | 344(1), 346(1.1) |
| s 25.1(1) public officer | MAYBE BOOLEAN | 1 | 368.2 |
| s 320.11 the thing is a vessel | MAYBE BOOLEAN | 1 | 335(2) |
| s 52.1(2) essential infrastructure | MAYBE BOOLEAN | 1 | 334.1(2) |
| s 787(1) general penalty | Punishment | 37 | 327(1), 333.2(3), 334, 335(1), 338(1), 338(2), 339(1), 339(2), 340, 341, 342(1), 342(3), 342.01(1), 342.1(1), 342.2(1), 348(1), 349(1), 351(1), 351(2), 352, 353(1), 353(4), 353.1(4), 355, 355.5, 356(3), 357, 362(2), 362(3), 363, 364(1), 367, 368(1.1), 368.1, 372(4), 377(1), 378 |

Inputs from sections outside the sources, so asked and never supplied: the Bank Act (the definition of financial institution, s 347.1(2)), the Interest Act s 2, the Tax Rebate Discounting Act (s 347(8)), the regulations under ss 347.01 and 347.1(2.1), the designation of a province under s 347.1(3), and every figure the text leaves to the general penalty of s 787(1).

The seat layer uses `ccc-definitions` for `s 2 motor vehicle` and `s 2 steal` only; the other section 2 terms are asked as a yes or no and wrapped in `JUST`. Two sections of this part hand a definition to another section: s 335(2) ("vessel has the same meaning as in section 320.11") and s 347.1(1) ("interest has the same meaning as in subsection 347(2)"); the first takes the answer of s 320.11 as an input, the second calls `s 347(2) interest`.

## What the text turns out to say (numbered findings)

1. **s 322(2) can be read two ways.** The text puts the sentence "A person commits theft when, with intent to steal anything, he moves it ..." under the heading "Time when theft completed". It is either a second definition of theft or a statement of when s 322(1) theft is complete. Fork F-322-2. (Text: lines 6540-6541.)
2. **s 344(2)(c) and s 346(1.2)(c) cross-refer to each other.** Paragraph (c) of the "Subsequent offences" subsection of s 344 names s 346, and the same paragraph of s 346 names s 344, each with "if a firearm was used in the commission of the offence". Whether the qualifier reaches every offence in the paragraph is fork F-344-C. (Text: lines 6763-6768 and 6782-6787.)
3. **s 344(1)(a.1) and s 346(1.1)(a.1) are shown repealed.** Paragraph 344(1)(a.1) reads "(a.1) [Repealed, 2022, c. 15, s. 12]" and 346(1.1)(a.1) reads "(a.1) [Repealed, 2022, c. 15, s. 13]"; each is a coverage row with the repealed text; the minimum penalties stated in paragraph (a)(i) and (ii) (five years for a first offence, seven years for a second or subsequent offence) remain. (Text: lines 6761 and 6780.)
4. **s 358 does not list the new trafficking offences.** Section 358 says "For the purposes of sections 342 and 354 and paragraph 356(1)(b), the offence of having in possession is complete when ...". Sections 355.2 (trafficking) and 355.4 (possession for the purpose of trafficking), which sit between them, are not named. The function answers NOTHING for them (the list is not closed with "only"). (Text: line 6989.)
5. **s 368.2 covers only ss 366 to 368.1.** The covert-identity exception for a public officer reaches "any of sections 366 to 368.1". Sections 369 to 378 are not named: for them the function answers NOTHING. (Text: lines 7082-7083.)
6. **Her Majesty and His Majesty.** In this Part, ss 327(2), 342.01(2) and 342.2(2) say "Her Majesty" and s 333.2(4) says "His Majesty". Each seat question uses its own section's wording. (Text: lines 6567, 6617, 6710, 6740.)
7. **Penalty shapes differ between look-alike sections.** Section 355 (possession) offers a summary-conviction limb for both value bands, but s 355.5 (trafficking) has no summary limb for a value above $5,000 (indictable only, 14 years). Sections 369, 374, 375, 376(1) and 376(2) are indictable only; s 364(1) is summary only. The punishment functions return the limbs the text states, as a list. (Text: lines 6942-6969, 7084-7089, 7103-7123, 7033-7034.)
8. **s 347.1(2) has numbers in the text and one outside it.** The $1,500 and 62-day limits in paragraph (a) are in the text and are encoded; the "limit fixed by regulation" of paragraph (a.1), the province designation of paragraph (c) (s 347.1(3)) and the fixing of the limit (s 347.1(2.1), a regulation-making power) are not: the first two are inputs and the last is machinery (inert, reason 2). (Text: lines 6834-6843.)
9. **The criminal rate is 35 per cent a year, on the credit advanced.** s 347(2) defines "criminal rate" as an annual percentage rate calculated in accordance with generally accepted actuarial practices and principles that exceeds 35 per cent on the credit advanced. The rate itself is an input (the person states it); the threshold, 35, is the text's. A rate of exactly 35 is not a criminal rate. (Text: line 6805.)
10. **s 335(2) hands "vessel" to s 320.11.** "vessel has the same meaning as in section 320.11" (ccc11): the answer of s 320.11 is taken as an input; this part does not restate it. (Text: line 6640.)
11. **s 365, s 370, s 371 and s 373 are repealed; s 359 and s 360 too.** Each is a coverage row of repealed text (with s 326(2), s 329, s 337, s 347(7) and the definition "data" of s 342.1(2)), 13 repealed items in all, each a constant that shows the text and no rule. (Text: lines 6562, 6582, 6643, 6731, 6761, 6780, 6819, 6991, 6992, 7046, 7090, 7091, 7102.)
12. **The general penalty of s 787(1) is an input.** Where a section says only "an offence punishable on summary conviction", the penalty is the general penalty of s 787(1) (ccc29), outside Part IX and outside the sources: it is an input in every punishment function (37 functions take it), never a number this part supplies. (Text: passim.)

## What the stable binary does not accept (or reads in a way that surprises)

1. **Unparenthesised `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`. This part wrote `NOT <x> AND <y>` once, in `s 378`; three assertions failed (the tests caught it) and the fix was `((NOT <x>) AND <y>)`. Loud, because a test failed; silent in a module with no test on that branch.
2. **A DEONTIC value cannot be compared in an `#ASSERT`.** A regulative `PARTY ... MUST ... HENCE FULFILLED LEST BREACH BECAUSE ...` rule compiles and `#TRACE` runs it, but `#ASSERT rule ... EQUALS FULFILLED` reports `eval/unsupported-equality`. Every duty in `ccc12-part9-duties.l4` therefore has a twin decision function (the gate, in the section's own module) that is asserted, and the rule is run with `#TRACE` in `ccc12-tests-duties.l4` (20 directives, 16 `#TRACE` and 4 `#EVAL`, no assertion). The two builds give the same outcome for every one (18 FULFILLED and 2 outstanding obligations), compared by hand because `check.sh` cannot see a trace.
3. **A `§` heading takes one backtick name.** `§ `a` and `b`` is a parse error; a heading is one backtick name. Loud.
4. **A record needs a backticked name to be constructed.** `Provision of the Code OF 322, ""` does not parse; `` `Provision of the Code` OF 322, "" `` does. Loud.
5. **Named-argument calls.** ``f WITH `a` IS x`` must be wrapped in parentheses before `EQUALS`; every seat question calls its layer-1 rule by named arguments so that no argument can be passed in the wrong place. Loud when wrong.
6. **Not used, so not tested here.** `REFUSE`, `TYPICALLY` and `WAIT UNTIL` (spelled `WAITUNTIL`) are not used in any file of this part. `YMD` is not defined; dates are `Date day month year` (daydate).

## Tests and the seat layer

Layer 1 is tested module by module (`ccc12-tests-*.l4`; positional one-line `#ASSERT`s, the expected value written beside the section it comes from, fixtures in `ccc12-tests-fixtures.l4` written as raw `Punishment OF ...` values, never taken from the encoding's own output). The seat layer has **233 questions** (every one `@export`ed, every input with an `@desc` worded as the accused would be asked) and **667 cases** in `ccc12-cases-seat.l4`, each written from the text. Of the 233 questions, 180 answer MAYBE BOOLEAN, 53 answer a punishment list or a number (each has at least one case, with the figures written by hand). Every MAYBE BOOLEAN question has a case that answers JUST FALSE or NOTHING; 158 also have a JUST TRUE case, and the other 22 cannot answer JUST TRUE at all, because the section says only "no" (exceptions and saving clauses such as ss 322(3), 325, 333, 335(1.1), 347(8), 353(1.1), 354(4), 366(5), 368.2: the layer-1 body has no JUST TRUE result). 104 of the MAYBE BOOLEAN questions call a layer-1 body that has a NOTHING branch; 65 of those have a NOTHING case, and the other 39 reach NOTHING only when an answer borrowed from another provision is not given, which the seat never leaves out (it wraps the person's yes or no as `JUST`), so NOTHING is unreachable there. (Checked by `work/casecheck.py`.) Each question is named "Under section N, ..." and was read against the layer-1 function it calls for direction and subject (the titles of the questions on ss 334.1, 342(2), 344(3), 346(1.3), 346(1.4), 348.1 and 328 were changed in that read; a "may" or "must" title is used only where the body answers the same way). A second reading of all of them on 2026-11-12 is recorded below.

### Second seat-question audit of 2026-11-12

All **233** seat questions were read a second time, each against the BODY of the layer-1 function it calls (its branches, its inputs and its answers), not against its own title, using the four tests of `seat-audit-second-pass.md`. **4 were retitled; 229 were read and left.** Every retitled question asked less than its body answers (test 1, limb); no question was found with the wrong modal, polarity or answer type. The cases of `ccc12-cases-seat.l4` are generated by question name, so they carry the new names; no expected value changed and no assertion broke, so no `RECONCILED` line was needed, and `check.sh` read the same before and after (1746 satisfied, 0 failed, every module `same` on both builds). The numbers below are the order of the questions in `ccc12-seat.l4`.

| old title | new title (exactly as in `@export`) | why |
| --- | --- | --- |
| Under section 333.1(1), what is the most I can be sentenced to for motor vehicle theft? | Under section 333.1(1), what is the most and the least I can be sentenced to for motor vehicle theft? | test 1 (limb): the body states a minimum of six months for a third or subsequent offence, which "the most" does not ask; its siblings on ss 344(1) and 346(1.1) already say "the most and the least" |
| Under section 338(1), have I fraudulently taken cattle or defaced a brand? | Under section 338(1), have I committed the offence of fraudulently taking cattle found astray, or of defacing a brand or mark on cattle or making a false one? | test 1 (limb): the body answers paragraphs (a), (b)(i) and (b)(ii); the old title named the first two as acts and left out making a false brand, so a "no" would have been misread (the seat inputs already ask all three) |
| Under section 339(1), have I taken possession of drift timber? | Under section 339(1), have I committed the offence of taking possession of drift timber, defacing its mark or refusing to deliver it up? | test 1 (limb): the body is true for paragraph (b) (removing a mark) and paragraph (c) (refusing to deliver up) as well as taking possession; the old title asked a fact narrower than the offence |
| Under section 348(1), if I am convicted of breaking and entering, what is the most I can be sentenced to? | Under section 348(1), if I am convicted of breaking and entering, or of breaking out, what is the most I can be sentenced to? | test 1 (limb): paragraphs (d) and (e) fix the punishment for the whole offence, breaking out (paragraph (c)) included, as the title of the question on the offence itself already says |

Read and left, where the call was close (one line of reason each):

- s 342(2) consent (question 76, "need the consent"): the title restates the bar's own name; on the branch where the Attorney General has consented the body answers NOTHING (the prohibition is "without the consent"; once it is given the subsection says nothing more), which reads oddly under "need" and equally under "barred", so a retitle would move the oddity, not remove it.
- s 347(5) (125, "may the certificate be received"): the title restates the function's name; F/N reads correctly as "may it be received" over a "shall not ... unless" bar (F-UNLESS-N).
- s 332(2) (28, "my receipt of money"): the body's gate names "anything mentioned in subsection (1)", the title the text's own "all money paid"; the answer is the same for money; the omitted "direction not in writing" is an input.
- s 339(4), s 339(5), s 348(2)(a), s 349(2), s 354(2) (64, 65, 136, 142, 168): the title names the principal case ("lumber", "broke and entered", "entered", "a motor vehicle"); the function takes one compound fact ("lumber or lumbering equipment", "or attempted", "or was in", "or part"), and the answer does not depend on which alternative holds.
- s 323(2) (13): the "though it does not say in which territorial division" clause is the text's own words.
- s 335(1) (47): the title names both limbs; intent to drive and the exception of s 335(1.1) are inputs and a separate question.
- s 333.11(1), s 333.11(2), s 346.1, s 353(3) (37, 38, 113, 156): the other sentence, the other offence or the sale is a status the function tests as an input and its own name carries.
- s 335(1.1), s 347(8), s 347.01(1), s 347.01(2), s 347.1(2), s 347.1(2.2) (49, 127, 128, 129, 132, 133): "does section 347 apply" is the function's own name over an exemption: JUST FALSE is the subsection's no, NOTHING is its silence; the title names the subsection.
- s 325, s 353.1(3) (15, 165): the title leaves out "factor or agent", the amount limit, "for a legitimate purpose"; the function's name carries them and they are inputs.
- s 322(5), s 323(1), s 324 (11, 12, 14): the title restates the function's own name; "marked" for "marked out or known" is wording.

Negative control: six expectations of `ccc12-cases-seat.l4` were flipped on a scratch copy (three JUST TRUE to JUST FALSE, three NOTHING to JUST FALSE); the run reported 638 satisfied and 6 failed, so a wrong expectation is reported. The scratch copy was deleted.

The regulative rules (`ccc12-part9-duties.l4`, 14 rules, one per duty or power of ss 327(2), 333.11, 334.1, 339(3), 346(1.4), 346.1, 347(6), 347.1(3) and (4), 348.1 and 353(3)) are run with `#TRACE` in `ccc12-tests-duties.l4` (no assertion: see "What the stable binary does not accept"); the two builds give the same outcome for every trace. No rule has a `WITHIN`, because the text states no time; each `MUST` ends `LEST BREACH BECAUSE "<what was not done>"`, which names the omission and invents no sanction (the only consequence the text states is the offence of s 353(4)); no `MAY` has a `LEST`.

**Lint.** `work/lint.py` checked, over the 267 layer-1 functions, that every `FALSE-kind` quote is a substring of the text (whitespace and quotation marks normalised; elisions marked `...`), that every function with a JUST FALSE result carries a `FALSE-kind` comment and every function with a NOTHING result a `NOTHING-kind` comment whose reason is one of the six allowed, and that each of the 13 `as the text shows it` constants is a substring of the text: 0 problems.

## What `check.sh` prints

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc12-cases-seat.l4                            0       667       0        0         0 |      0       667       0        0  same
ccc12-logic.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-break-enter.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-criminal-interest.l4               0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-duties.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-false-pretences.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-forgery.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-interpretation.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-possession.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-resembling-theft.l4                0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-robbery-extortion.l4               0         0       0        0         0 |      0         0       0        0  same
ccc12-part9-theft.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc12-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc12-tests-break-enter.l4                     0       125       0        0         0 |      0       125       0        0  same
ccc12-tests-criminal-interest.l4               0        90       0        0         0 |      0        90       0        0  same
ccc12-tests-duties.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc12-tests-false-pretences.l4                 0        82       0        0         0 |      0        82       0        0  same
ccc12-tests-fixtures.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc12-tests-forgery.l4                         0       137       0        0         0 |      0       137       0        0  same
ccc12-tests-interpretation.l4                  0        41       0        0         0 |      0        41       0        0  same
ccc12-tests-logic.l4                           0        28       0        0         0 |      0        28       0        0  same
ccc12-tests-possession.l4                      0        75       0        0         0 |      0        75       0        0  same
ccc12-tests-resembling-theft.l4                0       216       0        0         0 |      0       216       0        0  same
ccc12-tests-robbery-extortion.l4               0       103       0        0         0 |      0       103       0        0  same
ccc12-tests-theft.l4                           0       182       0        0         0 |      0       182       0        0  same
TOTAL (28 modules)                             0      1746       0        0           |      0      1746       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Command: `L4=<stable 1.6.110> L4_MAIN=<main 1.6.109> ./check.sh`. `ccc-core.l4`, `ccc-definitions.l4` and `ccc-interpretation.l4` are the keel's read-only files and show no assertions. The check cannot see a different `#TRACE` outcome; the traces of `ccc12-tests-duties.l4` were compared by hand on both builds (identical). No test fails on purpose: there is no `expected_failed`.

## Files

`ccc12-cases-seat.l4`, `ccc12-logic.l4`, `ccc12-part9-break-enter.l4`, `ccc12-part9-criminal-interest.l4`, `ccc12-part9-duties.l4`, `ccc12-part9-false-pretences.l4`, `ccc12-part9-forgery.l4`, `ccc12-part9-interpretation.l4`, `ccc12-part9-possession.l4`, `ccc12-part9-resembling-theft.l4`, `ccc12-part9-robbery-extortion.l4`, `ccc12-part9-theft.l4`, `ccc12-seat.l4`, `ccc12-tests-break-enter.l4`, `ccc12-tests-criminal-interest.l4`, `ccc12-tests-duties.l4`, `ccc12-tests-false-pretences.l4`, `ccc12-tests-fixtures.l4`, `ccc12-tests-forgery.l4`, `ccc12-tests-interpretation.l4`, `ccc12-tests-logic.l4`, `ccc12-tests-possession.l4`, `ccc12-tests-resembling-theft.l4`, `ccc12-tests-robbery-extortion.l4`, `ccc12-tests-theft.l4`, `NOTES.md`, `PROGRESS.md`. (`check.sh`, `srcrefs.py` and `fetch-main-l4.sh` are supplied.) No `NEEDS-CORE.md`: every type and constructor this part needed is declared under its own label.
