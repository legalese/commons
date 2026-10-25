# NOTES: piece ic1, the Israeli Companies Law, 5759-1999 (חוק החברות, התשנ״ט–1999), Part 2 and Part 3 chapters 1 to 3 (sections 2 to 118ב)
Written by piece agent `ic1`.
Status: draft. No domain expert has read it against the Law, and it has not been reviewed by anyone but its author.
Encoding model: Claude Sonnet 5.5 (the folder is `legalese-sonnet-5.5`).

**The source and its status.**
- Text used: `companies-law-5759-1999.he.wiki.txt`, lines 263 to 947 (`ic1`'s range), as the brief fixes them.
- It is the raw MediaWiki source of the Hebrew Wikisource page "חוק החברות", with its markup (`{{ח:סעיף|…}}`, `{{ח:ת}}`, `{{ח:תת|(א)}}`, `{{ח:פנימי|…}}`).
- It is an unofficial consolidation. Israel publishes no free official consolidated text. Nothing here is verified against the official text, and nothing here claims to be.
- Every `-- src:N |` line copies line N of that file, markup included, by `srcrefs.py quote`; no wording is reconstructed from memory. `python3 -I srcrefs.py check --refs` over every `ic1-*.l4` file reports 0 problems (522 `src:` lines, 281 runs, 297 locators).
- Laws the text cites (the Companies Ordinance, the Securities Law, the Trade Marks Ordinance, the Insolvency Law, the Government Companies Law, the Computers Law) are not among the inputs. Where a rule depends on one, its outcome is a plain input with a comment `-- out of range: ...` (see "Cross-references out of my ranges").

**Dates.** The range carries no date of enactment, no assent date and no commencement rule, so no date value is defined here.
The one place a commencement matters is section 24 ("a company that was incorporated before the commencement of this Law"): that is a plain yes/no input, `החברה התאגדה לפני תחילתו של חוק זה`, because the commencement date is in section 377 (piece ic6, which carries it).
Section 5 uses a day the Registrar writes in the certificate of incorporation; section 21(a) uses a day the company chooses; these are inputs, not dates the text fixes.

## Seat
The seat is **a person who founds, directs or holds shares in a company under the Companies Law**: a founder, a director or officer, a shareholder (a minority shareholder included), asking what the Law lets them do, what it requires of them, what they may require of the company, and what can be done to them.
Why: Commons writes every encoding from the seat of the individual to whom the law is applied (ruled 2026-10-18), and the brief fixes this seat for piece ic1.
"I" is that person and "my company" is the company they found, direct or hold shares in.
There is no seat for an official. The Registrar, the court and the Minister appear only as the other side of the person's relations: what the Registrar must do for my company ("Must the Registrar register my company?"), what a court may do to me ("May a court attribute a debt of the company to me?"), what I may require of an official.
A company is also a party, never a seat; where the Law puts a duty on the company the question is what the company owes me or what I may require of it, and where it puts a duty on a director or shareholder the question is the paired one ("As the director responsible for not convening the meeting, must I repay the company?").

**Files.**
- `ic1-seat.l4`: 268 questions, each with `@export` and `@desc`, grouped under 7 `§` and 37 `§§` headings (one of the `§§` headings introduces the six helper rules) in the text's order; every `@desc` is worded as the person would be asked and carries ` / ` and a plain English gloss.
- `ic1-cases-seat.l4`: 805 worked cases, at least one per question, with every expected value written by hand from the text beside the case (a one-line reason above each `#ASSERT`).
- The seat layer imports the layer-1 modules and calls their rules. It restates no rule, and no layer-1 module was changed to suit it. One layer-1 rule did change during the seat pass, for a reason of law and not of convenience: writing the cases for section 48(d) showed that the rule limited "all the organs" to the three principal organs, so it now calls section 46 (fork F-ic1-20); its tests were extended.

**How the questions take their facts.**
- Every input is plain: yes/no, a number, a date, or a choice from a list (an enumeration declared in layer 1, such as which organ or which matter).
- The records that layer 1 expects (the facts about a company, a vote, a certificate of incorporation) are built inside each question by six helper rules at the top of `ic1-seat.l4`. Their names end `- חלק 2 וחלק 3 פרקים 1 עד 3` so that they cannot collide with another piece's helpers after the merge.
- Whether a company is public, private or a bond company is the Law's own definition (section 1), worked out by the core from facts. A question asks the four share facts only when the rule it calls reads them (listed on a bourse; offered to the public under a prospectus; offered to the public abroad; held by the public), and the four bond facts only where a rule reads bonds. A field a called rule never reads is given a fixed placeholder (FALSE) with a comment saying so.
- A figure the articles may vary is asked as a yes/no ("do the articles fix another majority?") plus the figure; a fraction of capital or votes is a number such as 0.05 for five percent; a period is the count of days or months the person states.
- A judgment the Law leaves to the court or the Registrar is asked as a finding ("did the court find it just and right?"), never guessed.
- Questions the Law does not decide return `MAYBE` with `NOTHING` and each has a case that asserts `NOTHING`: section 3 (no shareholder), 11 (a public-benefit company), 13(a) (the parties contracted out under 13(c)), 21(a) (a section 40 change), 40 (an act the section does not list), 63(c) (a private company), 74(c) (not an adjournment of 21 days or less with an unchanged agenda), 78(b) (a quorum was present).
- Situational comments (`-- SITUATION: ...`) head the groups whose questions arise only in one situation (a court asked to pierce the veil; a promoter's act; an older company; a name demanded changed; a defective meeting; the audit committee).

**Not asked.** Section 6(d) (what "the court" means for sections 6 and 7) decides nothing the person could ask. The three majority helpers and the shared company-kind helper of layer 1 are not provisions. Every `inert` provision of the coverage table is a title, an editorial note or an official's regulation-making power. No other provision of the range is left without a question.

**Polarity.** A rule of layer 1 returns TRUE when the relation holds. Two questions were reworded after a check of what the rule returns: s 20(c) is asked "is an amendment that harms my class permitted?" (TRUE when no class approval is needed or it was given), and s 20(d) is asked "does an amendment bind me as a shareholder?" (TRUE unless it adds to my shares or liability without my consent).

## Jural relations
One row per provision (or group of provisions that state one relation) that creates a Hohfeldian relation: the holder of the claim, privilege, power or immunity, the bearer of the correlative duty, no-right, liability or disability, and the L4 rule that encodes it.
A provision that creates no such relation (a definition, a counting rule) is listed once as `none`.
The seat layer asks the holder's question and, where the text also binds the person, the paired question.
| provision | holder (claim / privilege / power / immunity) | bearer (duty / no-right / liability / disability) | L4 rule |
| --- | --- | --- | --- |

| s 2 | privilege: any person who founds a company whose purposes are lawful, moral and consistent with public policy | no-right: everyone else, including the Registrar (no claim to stop such a founder) | ic1-part2-ch1-incorporation.l4: `סעיף 2 - כל אדם רשאי לייסד חברה` |
| s 3 | privilege: the founders and the company to have one shareholder only | no-right: the Registrar and others (no claim to require more shareholders) | `סעיף 3 - לחברה יכול שיהיה בעל מניה אחד` |
| s 4 | power: the company (capacity for every right, duty and act consistent with its nature as a body corporate) | liability: those who deal with it (they are bound by, and may rely on, its acts within that capacity) | `סעיף 4 - החברה כשרה לזכות, לחובה ולפעולה` |
| s 5 | none (a counting rule: it fixes the period during which the company exists) | none | `סעיף 5 - החברה קיימת ביום` |
| s 6(a) | power: the court (to attribute a debt of the company to a shareholder); claim of the company's creditor against the shareholder once attributed | liability: the shareholder who knowingly used the separate personality abusively | `סעיף 6(א) - בית משפט רשאי לייחס חוב של חברה לבעל מניה בה` |
| s 6(a)(2) | none (a definition of awareness) | none | `סעיף 6(א)(2) - יראו אדם כמודע לשימוש` |
| s 6(b) | power: the court (to attribute a trait, right or duty between shareholder and company) | liability: the shareholder and the company | `סעיף 6(ב) - בית משפט רשאי לייחס תכונה, זכות או חובה של בעל מניה לחברה או להפך` |
| s 6(c) | power: the court (to suspend the shareholder's right to be repaid his own debt); claim of the other creditors to be paid first | liability: the shareholder | `סעיף 6(ג) - בית משפט רשאי להשעות את זכות בעל המניה לפירעון חובו מאת החברה` |
| s 6(d) | none (a definition of "the court" for sections 6 and 7) | none | `סעיף 6(ד) - בית המשפט לענין סעיפים 6 ו־7` |
| s 7(a) | power: the court (to bar the shareholder for up to five years from being a director or general manager or involved in founding or running a company) | liability: the shareholder | `סעיף 7(א) - בית משפט רשאי להורות על צו הגבלה` |
| s 7(b) | claim: the Registrar (to be notified of the order) | duty: the court that gave the order | `סעיף 7(ב) - על בית המשפט לשלוח לרשם הודעה על צו ההגבלה` |
| s 7(c) | claim: the company's creditors (for debts arising in the restriction period) | duty: the person who breached the order | `סעיף 7(ג) - המפר צו הגבלה חב בחובות החברה` |
| s 8(a) | none (it states what a proper application is; the applicant's duty to file it that way is the correlative of the Registrar's power to refuse an improper one, section 10(a)) | none | `סעיף 8(א) - הבקשה לרישום חברה הוגשה כדין` |
| s 8(b) | power: the Registrar (to allow a non-electronic filing) | liability: the applicant | `סעיף 8(ב) - הרשם רשאי לאפשר הגשת בקשה שלא בדרך אלקטרונית` |
| s 9(a) | claim: the State (the Registrar), to the registration fee | duty: the applicant | `סעיף 9(א) - על המבקש לרשום חברה לשלם אגרת רישום בעת הגשת הבקשה` |
| s 9(b),(c) | claim: the State (the Registrar), to the annual fee | duty: the company or foreign company | `סעיף 9(ב) - חברה משלמת בכל שנה אגרה שנתית` |
| s 10(a) | claim: the applicant, to be registered once the requirements are met | duty: the Registrar | `סעיף 10(א) - הרשם ירשום חברה` |
| s 10(b) | claim: the company, to a registration number stated in its certificate | duty: the Registrar | `סעיף 10(ב) - הרשם ייתן לחברה מספר רישום ויציין אותו בתעודת ההתאגדות` |
| s 10(c) | claim: the registered company, to a certificate of incorporation | duty: the Registrar | `סעיף 10(ג) - הרשם ימסור לחברה שנרשמה תעודת התאגדות` |
| s 10(d) | immunity: the company (its registration cannot be attacked on the ground that a requirement was not met) | disability: any person who would dispute that the requirements were met | `סעיף 10(ד) - תעודת התאגדות ראיה חלוטה לקיום דרישות הרישום` |
| s 10(e) | none (the section states that subsection (d) confers no immunity from a defect in the articles) | none | `סעיף 10(ה) - הצורך בתיקון פגם בתקנון נשאר אף לאחר התעודה` |
| s 11(a) first limb | none (it states the purpose of a company and what may be weighed in pursuing it) | none | `סעיף 11(א) - אפשר להביא בחשבון בשיקולים עסקיים להשאת רווחים` |
| s 11(a) second limb | privilege: the company (to donate a reasonable sum to a worthy cause if the articles so provide) | no-right: its shareholders and creditors (no claim to stop such a donation) | `סעיף 11(א) - חברה רשאית לתרום למטרה ראויה` |
| s 11(b) | none (a scope rule: subsection (a) does not apply to a public-benefit company) | none | `סעיף 11(ב) - הוראת סעיף קטן (א) חלה על החברה` |
| s 12(a) | power: the company (to ratify a promoter's act) | liability: the promoter and the third party | `סעיף 12(א) - החברה רשאית לאשר פעולה של יזם שנעשתה לפני התאגדותה` |
| s 12(b) | immunity: the third party who acquired a right in good faith and for consideration before the ratification | disability: the company (it cannot impair that right by ratifying) | `סעיף 12(ב) - האישור בדיעבד רשאי לפגוע בזכות של צד שלישי` |
| s 13(a) | power: the third party who knew of the promotion (to treat the promoter as the counterparty, or withdraw and claim damages) | liability: the promoter | `סעיף 13(א) - לצד שלישי שידע על היזמות הברירה לראות ביזם בעל דברו או לחזור בו` |
| s 13(b) | immunity: the promoter (no longer liable or entitled once the company approves) | disability: the third party (can no longer hold the promoter to the act) | `סעיף 13(ב) - היזם חייב או זכאי עוד בשל הפעולה` |
| s 13(c) | power: the promoter and the third party together (to stipulate otherwise) | liability: each of them to the terms they agree | `סעיף 13(ג) - הוראות סעיף 13 חלות` |
| s 14(1) | claim: the third party who did not know (against the promoter); claim of the promoter where the act entitles him | duty: the promoter (or the third party, where the act entitles the promoter) | `סעיף 14(1) - פעולת היזם מחייבת או מזכה את היזם` |
| s 14(2) first limb | power: the incorporated company (to approve the act) | liability: the third party and the promoter | `סעיף 14(2) - החברה שהתאגדה רשאית לאשר את הפעולה` |
| s 14(2) second limb | claim: the third party, against the company and the promoter jointly and severally | duty: the company and the promoter | `סעיף 14(2) - הפעולה מחייבת את החברה ואת היזם ביחד ולחוד לאחר האישור` |
| s 14(2) third limb | claim: the company only, to the benefit of the act | no-right: the promoter (no claim to the benefit once the company approves) | `סעיף 14(2) - הפעולה מזכה את היזם` |
| s 15 | claim: the Registrar and the shareholders, that the company has articles | duty: the company | ic1-part2-ch2-articles.l4: `סעיף 15 - לחברה יש תקנון` |
| s 16 | none (a counting rule: it fixes from when the registered articles are valid) | none | `סעיף 16 - התקנון שנרשם עם ההתאגדות תקף` |
| s 17(a) | claim: the company against each shareholder, each shareholder against the company, each shareholder against every other shareholder, to the performance of the articles | duty: the other party of each such pair | `סעיף 17(א) - דין התקנון כדין חוזה בין הצדדים` |
| s 17(b) | none (it states that the articles change only in the ways the Law provides) | none | `סעיף 17(ב) - שינוי התקנון נעשה בדרכים הקבועות בחוק זה` |
| s 18 | claim: the Registrar (and the public), to articles with the four mandatory items | duty: the company and its founders | `סעיף 18 - התקנון כולל את הפרטים שחובה לכלול בו` |
| s 19 | privilege: the company and its shareholders (to include any matter that concerns the company or its shareholders) | no-right: the Registrar and anyone else (no claim to keep such a matter out) | `סעיף 19 - חברה רשאית לכלול בתקנון נושא` |
| s 19(2א) Minister's power | none (inert: a power to amend a Schedule) | none | none |
| s 20(a) | power: the company, by its general meeting, to amend the articles by an ordinary majority | liability: every shareholder (bound by the amendment) | `סעיף 20(א) - חברה רשאית לשנות את תקנונה בהחלטה ברוב רגיל באסיפה הכללית` |
| s 20(b) | immunity: the shareholders benefiting from an entrenched provision (it changes only by the higher of the two majorities) | disability: the company and the general meeting | `סעיף 20(ב) - שינוי הוראה מוגנת ברוב המסוים או ברוב המוצע לפי הגבוה` |
| s 20(c) | immunity: the holders of a class of shares (no harmful amendment without their class meeting's approval) | disability: the company and the general meeting | `סעיף 20(ג) - שינוי הפוגע בזכויות סוג מניות טעון אישור אסיפת הסוג` |
| s 20(d) | immunity: the shareholder (no new purchase or liability without his consent) | disability: the company and the majority | `סעיף 20(ד) - שינוי בתקנון מחייב בעל מניה` |
| s 21(a) | none (a counting rule: it fixes the day from which an amendment is valid) | none | `סעיף 21(א) - היום שבו שינוי התקנון תקף` |
| s 21(b) | claim: the Registrar, to the text of the resolution within fourteen days | duty: the company | `סעיף 21(ב) - החברה מסרה לרשם את נוסח ההחלטה בתוך ארבעה עשר ימים` |
| s 22(a) | power: the company, by its general meeting, to restrict its own power to amend | liability: the company's future general meetings and shareholders | `סעיף 22(א) - חברה רשאית להגביל את סמכותה לשנות את התקנון` |
| s 22(b) | none (it assimilates a restricting resolution to an amending resolution) | none | `סעיף 22(ב) - החלטה להגביל את סמכות השינוי דינה כדין החלטה לשינוי התקנון` |
| s 23(a) | claim: the Registrar, to articles signed by the first shareholders and stating their shares and particulars | duty: the first shareholders | `סעיף 23(א) - התקנון נחתם ופורטו בו בעלי המניות הראשונים` |
| s 23(b) | claim: the Registrar, to verification of the signatories' identity | duty: the first shareholders (who must have a lawyer or an online verification verify it) | `סעיף 23(ב) - זהות החותמים על התקנון אומתה` |
| s 24(1) | power: a company incorporated before commencement (to amend its memorandum by the Ordinance's way, or on capital and name by 75 percent); immunity: the company (no Minister's consent for a change of name) | liability: its shareholders; disability: the Minister | `סעיף 24(1) - ...` (three rules) |
| s 24(2) | power: a company incorporated before commencement (to amend or cancel its memorandum under section 350) | liability: its shareholders | `סעיף 24(2) - חברה שהתאגדה לפני תחילת החוק רשאית לשנות את תזכירה או לבטלו` |
| s 24(3) | power: such a company (to amend its articles by 75 percent or the majority fixed) | liability: its shareholders | `סעיף 24(3) - חברה שהתאגדה לפני תחילת החוק רשאית לשנות את הוראות תקנונה` |
| s 24(4) | power: such a company (to fix in its articles the majority needed to amend them) | liability: its shareholders | `סעיף 24(4) - חברה שהתאגדה לפני תחילת החוק רשאית לקבוע בתקנון הוראה בדבר הרוב הדרוש לשינויו` |
| s 24(5) | power: such a company (to fix in its memorandum the majority needed to change it) | liability: its shareholders | `סעיף 24(5) - חברה שהתאגדה לפני תחילת החוק רשאית לקבוע בתזכיר הוראה בדבר שינוי הרוב הדרוש לשינוי התזכיר` |
| s 25 | privilege: the company and its founders (to register under any name that meets the sub-chapter and other law) | no-right: the Registrar (no claim to refuse such a name) | ic1-part2-ch2-name-capital.l4: `סעיף 25 - חברה רשאית להירשם בכל שם` |
| s 26 | claim: the public dealing with the company, to the designation at the end of the name | duty: the company with limited liability | `סעיף 26 - שם חברה בערבון מוגבל כולל בסופו את הציון` |
| s 27(a)(1) | claim: a corporation registered in Israel, that no company be registered under its name or a misleading likeness | duty: the Registrar | `סעיף 27(א)(1) - השם אסור לרישום בשל שם של תאגיד קיים` |
| s 27(a)(2) | claim: the owner of a registered trade mark, that no company with similar purposes be registered under it without his written consent | duty: the Registrar | `סעיף 27(א)(2) - השם אסור לרישום בשל סימן מסחר רשום` |
| s 27(b) | claim: the public, that no company be registered under a deceptive name | duty: the Registrar | `סעיף 27(ב) - השם אסור לרישום בשל תרמית או הטעיה` |
| s 28 | claim: the public, that no company be registered under a name harming public policy or the public's feelings | duty: the Registrar | `סעיף 28 - השם אסור לרישום מפני שעלול לפגוע בתקנת הציבור או ברגשותיו` |
| s 29(a) | power: the Registrar (to require a change of name) | liability: the company | `סעיף 29(א) - הרשם רשאי לדרוש מחברה לשנות את שמה` |
| s 29(b) | power: the Registrar (to change the name himself after four months) | liability: the company | `סעיף 29(ב) - הרשם רשאי לשנות את שם החברה לשם שיבחר` |
| s 29(c) | claim: the company, to a certificate of change of name | duty: the Registrar | `סעיף 29(ג) - הרשם ישלח לחברה תעודת שינוי שם והשינוי נחשב כהחלטת החברה והרשם` |
| s 29(d) | none (inert: a regulation-making power) | none | none |
| s 30 | power: the court (to order a person or a company to refrain from using a name) | liability: the defendant (the person who took the name, or the company registered under it) | `סעיף 30 - בית המשפט רשאי להורות להימנע משימוש בשם` |
| s 31(a) | power: the company, with the Registrar's approval (to change its name) | liability: the Registrar (bound by his approval to register it, under (b)) | `סעיף 31(א) - חברה רשאית באישור הרשם לשנות את שמה` |
| s 31(b) | claim: the company, to registration of the new name and a certificate | duty: the Registrar | `סעיף 31(ב) - הרשם ירשום את השם החדש ויתן לחברה תעודת שינוי שם` |
| s 32 | claim: the Registrar and the public, to purposes stated in one of the three ways | duty: the company | `סעיף 32 - החברה ציינה את מטרותיה בתקנון באחד האופנים שבחוק` |
| s 33 | claim: the Registrar and the public, to a stated registered share capital | duty: the company | `סעיף 33 - החברה קבעה בתקנונה את הון המניות הרשום` |
| s 34(a) | none (it states that shares are all with or all without par value) | none | `סעיף 34(א) - מניות החברה כולן בעלות ערך נקוב או כולן ללא ערך נקוב` |
| s 34(b) | claim: the Registrar and the public, to a statement of the number of shares (and the par value, if any) | duty: the company | `סעיף 34(ב) - התקנון מציין את מספר המניות ואת ערכן הנקוב` |
| s 34(c) | none (a counting rule: registered and issued capital of no-par shares) | none | `סעיף 34(ג) - ...` (two rules) |
| s 35(a) | claim: the company's creditors, to a statement of whether and how the shareholders' liability is limited | duty: the company | `סעיף 35(א) - התקנון מציין שהאחריות בלתי מוגבלת או מפרט את אופן ההגבלה` |
| s 35(b) | claim: the company and its creditors, to the par value of the shares | duty: the shareholders | `סעיף 35(ב) - בעלי המניות אחראים לפירעון הערך הנקוב לפחות` |
| s 36(a) | none (it states who the Registrar is; the Minister's appointment is the source of the Registrar's powers over a company) | none | ic1-part2-ch3-registrar.l4: `סעיף 36(א) - האדם הוא רשם החברות` |
| s 36(b) | power: the Minister (to appoint and authorise a deputy) | liability: the deputy appointed | `סעיף 36(ב) - האדם הוא סגן הרשם ויש לו סמכויות הרשם` |
| s 36(c) | power: the Minister (to authorise a Ministry of Justice employee when the Registrar is unable) | liability: the employee authorised | `סעיף 36(ג) - עובד משרד המשפטים מוסמך בסמכויות הרשם כשנבצר מהרשם למלא את תפקידו` |
| s 37(a) | power: the Registrar (to determine whether the requirements were met) | liability: the applicant or company | `סעיף 37(א) - הרשם קובע אם נתמלאו התנאים והדרישות בענין` |
| s 37(b) | power: the Registrar (to order the registers and books produced) | liability: the company | `סעיף 37(ב) - הרשם רשאי לדרוש המצאת מרשמים ופנקסים בתוך תקופה של ארבעה עשר ימים לפחות` |
| s 37(c) | power: the Registrar (to order the registers updated) | liability: the company | `סעיף 37(ג) - הרשם רשאי להורות לחברה לעדכן את המרשמים והפנקסים` |
| s 38(a) | claim: every company, to a record kept for it and to the receipt of its filings | duty: the Registrar | `סעיף 38(א) - הרשם ינהל רישום לגבי כל חברה ויקבל מסמכים ודיווחים` |
| s 38(b) | power: the Registrar (to allow a non-electronic filing) | liability: the filing company | `סעיף 38(ב) - המסמך או הדיווח נמסר כדין` |
| s 38(c) | claim: every company, to registration in the register and an identity number | duty: the Registrar | `סעיף 38(ג) - הרשם ירשום כל חברה במרשם החברות ויתן לה מספר זהות` |
| s 39(a) | claim: the Registrar, that every filing bears the identity number and is signed by an office-holder | duty: the company | `סעיף 39(א) - המסמך או הדיווח נושא את מספר הזהות וחתום בידי נושא משרה` |
| s 39(b) | privilege: the receiver, liquidator or trustee of a company in insolvency (to sign its filings) | no-right: the Registrar (no claim that an office-holder sign) | `סעיף 39(ב) - מסמך או דיווח של חברה בכינוס, בפירוק או בהליכי חדלות פירעון יכול שייחתם בידי כונס הנכסים או הנאמן` |
| s 39(c) | none (a scope rule: the section yields to a different provision of law) | none | `סעיף 39(ג) - הוראות סעיף 39 חלות` |
| s 39(d) | none (inert: a regulation-making power) | none | none |
| s 40 | immunity: anyone dealing with the company (an unregistered change of name, purposes or status has no validity) | disability: the company | `סעיף 40 - לפעולה יש תוקף רק אם נרשמה` |
| s 41(a) | claim: whoever relies on a certified copy, to have it accepted as an original and as conclusive evidence that the original is in the office | duty: the court and the other party | `סעיף 41(א) - ...` (two rules) |
| s 41(b) | none (it extends (a) to printouts of electronic filings) | none | `סעיף 41(ב) - הוראות סעיף 41(א) חלות על פלט של דיווח אלקטרוני` |
| s 42 | immunity: whoever deals with the company or the Registrar (the registration of a document is not, alone, evidence that he knew its contents) | disability: whoever would rely on the registration to prove that he knew | `סעיף 42 - רישום או קיום של מסמך כשלעצמו ראיה לידיעת תוכנו` |
| s 43(a) | claim: any person, to inspect the registers and obtain certified copies | duty: the Registrar | `סעיף 43(א) - כל אדם רשאי לעיין במרשמים ולקבל העתקים מאושרים` |
| s 43(b) | privilege: a public body sending digital messages (to inspect item (2) of the Fourth Schedule) | no-right: any other person (no claim to inspect item (2)) | `סעיף 43(ב) - פרט (2) לתוספת הרביעית פתוח לעיון גוף ציבורי השולח מסרים דיגיטליים בלבד` |
| s 44 | none (inert: the Minister's regulation-making powers) | none | none |
| s 45 | none (repealed in this text) | none | none |
| s 46 | none (a definition: which bodies are organs of the company) | none | ic1-part3-ch1-organs.l4: `סעיף 46 - הגוף הוא אורגן של החברה` |
| s 47 | claim: whoever dealt with the organ, that its acts and intentions are the company's | duty: the company | `סעיף 47 - מעשי אורגן וכוונותיו הם מעשי החברה וכוונותיה` |
| s 48(a)-(c) | power: the general meeting, the board, the general manager (each the powers listed for it) | liability: the company and those affected | `סעיף 48(א) עד (ג) - הסמכות נתונה לאורגן` |
| s 48(d) | power: every organ (the ancillary powers needed to exercise its powers) | liability: the company | `סעיף 48(ד) - סמכויות העזר נתונות לכל האורגנים` |
| s 49 | power: the board (the residual power) | liability: the company's other organs | `סעיף 49 - הדירקטוריון רשאי להפעיל סמכות של החברה שלא הוקנתה לאורגן אחר` |
| s 50(a) | power: the company, by its articles (to move powers between organs) | liability: the organ whose power moves | `סעיף 50(א) - חברה רשאית לקבוע בתקנונה העברת סמכויות בין האורגנים` |
| s 50(b) | claim: the company, its creditors and the other shareholders, to directors' standard of conduct from shareholders who took the board's powers | duty: the shareholders who took them (in proportion to their participation and vote) | `סעיף 50(ב) - על בעלי המניות חלים זכויות, חובות ואחריות של דירקטורים` |
| s 51 first limb | power: the board (to instruct the general manager) | liability: the general manager | `סעיף 51 - הדירקטוריון רשאי להורות למנהל הכללי כיצד לפעול לענין מסוים` |
| s 51 second limb | power: the board (to act in the manager's place when he does not comply) | liability: the general manager | `סעיף 51 - הדירקטוריון רשאי להפעיל במקום המנהל הכללי את הסמכות הנדרשת לביצוע ההוראה` |
| s 52(a) | power: the general meeting (to exercise the board's essential power when the board is unable) | liability: the board | `סעיף 52(א) - האסיפה הכללית רשאית להפעיל סמכות של הדירקטוריון שנבצר ממנו להפעילה` |
| s 52(b) | power: the board (to exercise the general manager's powers when he is unable) | liability: the general manager | `סעיף 52(ב) - הדירקטוריון רשאי להפעיל סמכויות של המנהל הכללי שנבצר ממנו להפעילן` |
| s 53(a) | claim: the victim of a tort of an organ, directly against the company | duty: the company | `סעיף 53(א) - חברה חבה במישרין באחריות בנזיקין על עוולה שבוצעה בידי אורגן שלה` |
| s 53(b) | claim: the victim, to the company's vicarious liability under any law | duty: the company | `סעיף 53(ב) - אחריותה השילוחית של חברה בנזיקין נשמרת` |
| s 54(a) | claim: whoever is harmed, against the individual of the organ who acted | duty: that individual | `סעיף 54(א) - ייחוס פעולת אורגן לחברה אינו גורע מאחריותם האישית של יחידי האורגן` |
| s 54(b) | none (repealed in this text) | none | none |
| s 55(a) | claim: the company, its shareholders and creditors, that no act exceeds the purposes or the authorisation | duty: the company and whoever acts for it | `סעיף 55(א) - הפעולה אסורה על החברה ועל מי שפועל מטעמה` |
| s 55(b) | power: the court (to order an excessive act stopped or prevented); claim to apply: the company, a shareholder, a creditor with cause | liability: the company and whoever acts for it | `סעיף 55(ב) - בית המשפט רשאי לתת צו להפסקת פעולה חורגת או למניעתה` |
| s 56(a) | immunity: the company (an act in excess of purposes or authority does not bind it) | disability: the party dealing with it, unless approval or innocence | `סעיף 56(א) - לפעולה יש תוקף כלפי החברה` |
| s 56(b) | power: the general meeting (to approve an act in excess of purposes), or the organ authorised to give the authorisation (for an unauthorised act) | liability: the company | `סעיף 56(ב) - אישור החברה בדיעבד לפעולה חורגת` |
| s 56(c) | immunity: another person who acquired a right in good faith and for consideration before the approval | disability: the company | `סעיף 56(ג) - האישור רשאי לפגוע בזכות שרכש אדם אחר` |
| s 57 | claim: every shareholder, that the eight listed decisions are taken in the general meeting | duty: the company and its board | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 57 - סעיף זה מחייב לקבל את ההחלטה באסיפה הכללית` |
| s 58(a) | immunity: the shareholders (the company cannot stipulate against section 57) | disability: the company | `סעיף 58(א) - חברה רשאית להתנות על הוראות סעיף 57` |
| s 58(b) | power: the company, by its articles (to add matters for the general meeting; to move powers to it by the route of section 50) | liability: the board and the other organs | `סעיף 58(ב) - ...` (two rules) |
| s 59 | power: the annual general meeting (to appoint the directors) | liability: the directors appointed | `סעיף 59 - האסיפה הכללית השנתית ממנה את הדירקטורים` |
| s 60(a) | claim: every shareholder (and director), to an annual meeting within fifteen months of the last | duty: the company | `סעיף 60(א) - החברה קיימה אסיפה שנתית בתוך חמישה עשר חודשים` |
| s 60(b) | claim: every shareholder, that the annual meeting's agenda includes the financial statements and the board's report | duty: the board, which sets the agenda | `סעיף 60(ב) - ...` (two rules) |
| s 61(a) | privilege: a private company whose articles so provide (not to hold an annual meeting); claim: a shareholder or director who demands one | no-right: the shareholders, unless they demand; duty: the company, once one demands | `סעיף 61(א) - החברה חייבת לקיים אסיפה שנתית` |
| s 61(b) | claim: the registered shareholders, to yearly financial statements | duty: the company that holds no annual meeting | `סעיף 61(ב) - החברה שלחה לבעלי המניות הרשומים דוחות כספיים במועד` |
| s 62(a) | power: the court (to order an annual meeting convened); claim to apply: a shareholder or director | liability: the company and the directors | `סעיף 62(א) - בית המשפט רשאי להורות על כינוס אסיפה שנתית` |
| s 62(b) | claim: the applicant (to reasonable expenses from the company); claim: the company (to reimbursement from the responsible directors) | duty: the company; duty: the responsible directors | `סעיף 62(ב) - ...` (two rules) |
| s 63(a) | claim: a director, or shareholders holding the stated fractions, that the board of a private company convene a special meeting | duty: the board | `סעיף 63(א) - הדירקטוריון של חברה פרטית חייב לכנס אסיפה מיוחדת` |
| s 63(b) | claim: two directors or a quarter of the serving directors, or shareholders holding the stated fractions, that the board of a public company convene a special meeting | duty: the board | `סעיף 63(ב) - הדירקטוריון של חברה ציבורית חייב לכנס אסיפה מיוחדת` |
| s 63(c) | claim: the demander, to a call within twenty-one days and (public company) a meeting within thirty-five days of the notice | duty: the board | `סעיף 63(ג) - ...` (two rules) |
| s 64(a) | power: the demander (or the majority of the demanding shareholders by votes) to convene the meeting himself, within three months | liability: the company | `סעיף 64(א) - הדורש רשאי לכנס את האסיפה בעצמו` |
| s 64(b) | claim: the demander (to expenses from the company); claim: the company (to reimbursement from the responsible directors) | duty: the company; duty: the responsible directors | `סעיף 64(ב) - ...` (two rules) |
| s 65(a) | power: the court (to order a demanded special meeting convened); claim to apply: the demander | liability: the company | `סעיף 65(א) - בית המשפט רשאי להורות על כינוס אסיפה מיוחדת שנדרשה` |
| s 65(b) | claim: the applicant (expenses from the company); claim: the company (reimbursement from the responsible directors) | duty: the company; duty: the responsible directors | `סעיף 65(ב) - ...` (two rules) |
| s 66(a) | claim: the demanding or requesting shareholders, that their matter be on the agenda | duty: the board | ic1-part3-ch2-gm-convening.l4: `סעיף 66(א) - הנושא חייב להיכלל בסדר היום` |
| s 66(b) | claim: shareholders holding one percent of the voting rights, to ask the board to include a suitable matter | duty: the board (to consider and include it) | `סעיף 66(ב) - בעלי מניות רשאים לבקש מהדירקטוריון לכלול נושא בסדר היום` |
| s 66(c) | immunity: every shareholder (no decision on a matter not detailed in the agenda binds him) | disability: the meeting | `סעיף 66(ג) - באסיפה כללית מתקבלות החלטות בנושאים שפורטו בסדר היום בלבד` |
| s 67 | claim: every shareholder entitled to participate in a private company's meeting, to an invitation in time | duty: the company (its board) | `סעיף 67 - ההזמנה לאסיפה כללית בחברה פרטית נמסרה במועד` |
| s 68(a),(b) | claim: every shareholder entitled to participate, to an invitation with the date, place, agenda and wording of any proposed amendment | duty: the company (its board) | `סעיף 68(א)`, `סעיף 68(ב)` |
| s 69(a),(c) | claim: every shareholder of a public company, to a notice published or delivered as set, with the agenda, proposed resolutions and voting-deed arrangements | duty: the company (its board) | `סעיף 69(א)`, `סעיף 69(ג)` |
| s 69(b) | none (repealed in this text) | none | none |
| s 69(d) | none (inert: a regulation-making power) | none | none |
| s 70 | none (inert: a regulation-making power) | none | none |
| s 71 | claim: a shareholder in a public company who wishes to vote, to a certificate of ownership | duty: the bourse member through which the share is held | `סעיף 71 - בעל מניה בחברה ציבורית זכאי לאישור בעלות מחבר הבורסה` |
| s 72 | power: the court (to order a meeting convened and conducted in a way it fixes); claim to apply: the company, a shareholder entitled to vote, a director | liability: the company | `סעיף 72 - בית המשפט רשאי להורות על כינוס וניהול אסיפה בדרך שיקבע` |
| s 73 | claim: the shareholders of a public company, to a general meeting in Israel | duty: the company | `סעיף 73 - חברה ציבורית תקיים אסיפה כללית בישראל` |
| s 74(a) | power: a general meeting that has a quorum (to postpone itself, a discussion or a decision) | liability: the shareholders | `סעיף 74(א) - ...` (two rules) |
| s 74(b),(c) | claim: the shareholders, to notices of a postponed meeting in time | duty: the company | `סעיף 74(ב)`, `סעיף 74(ג)` |
| s 75 | none (it assimilates a class meeting to a general meeting) | none | `סעיף 75 - הוראות סימנים ג׳ עד ו׳ חלות על אסיפת סוג` |
| s 76 | privilege: all the shareholders of a private company together (to decide without an invitation or a meeting) | no-right: none (nobody can demand a meeting if all agree) | ic1-part3-ch2-gm-conduct.l4: `סעיף 76 - בחברה פרטית ניתן לקבל החלטה באסיפה כללית ללא הזמנה וללא התכנסות` |
| s 77 | privilege: a private company (to hold the meeting by any means of communication) | no-right: its shareholders (unless the articles forbid it) | `סעיף 77 - חברה פרטית רשאית לקיים אסיפה כללית באמצעי תקשורת` |
| s 78(a) | claim: the shareholders present, that the meeting not be held without the quorum | duty: the company (its chair) | `סעיף 78(א) - באסיפה כללית נכח מנין חוקי` |
| s 78(b) | none (a counting rule: the postponement when there is no quorum) | none | `סעיף 78(ב) - האסיפה נדחית לשבוע ימים או למועד מאוחר יותר שצויין` |
| s 78(c) | none (a scope rule: a company with one shareholder is outside the sub-chapter) | none | `סעיף 78(ג) - הוראות סימן ה׳ חלות על החברה` |
| s 79(a) | none (a counting rule: the postponed meeting is held with any number) | none | `סעיף 79(א) - האסיפה הנדחית מתקיימת בכל מספר משתתפים` |
| s 79(b) | claim: the demanding shareholders, that a postponed meeting they demanded be held only if enough shareholders are present | duty: the company | `סעיף 79(ב) - ...` |
| s 80(a),(b) | claim: every shareholder, to a chair chosen at the start of the discussion | duty: the company (the chair of the board or the authorised director, who opens the meeting) | `סעיף 80(א)`, `סעיף 80(ב)` |
| s 81 | power: the company, by its articles (to stipulate against sub-chapter E) | liability: its shareholders | `סעיף 81 - ניתן להתנות בתקנון על הוראות סימן ה׳` |
| s 82(a) | power: the company, by its articles (to fix different voting rights for different classes) | liability: its shareholders | `סעיף 82(א)` |
| s 82(b) | none (other enactments are preserved) | none | `סעיף 82(ב)` |
| s 82(c) | claim: every shareholder, to one vote per share where the articles fix no different rights | duty: the company | `סעיף 82(ג) - מספר הקולות של מניה` |
| s 83(a) | privilege: a shareholder of a public company (to vote in person, by proxy or by a voting deed) | no-right: the company (it cannot refuse one of these ways) | `סעיף 83(א) - בעל מניה בחברה ציבורית רשאי להצביע בדרך` |
| s 83(b) | privilege: a shareholder of a private company (to vote in person or by proxy unless the articles say otherwise) | no-right: the company | `סעיף 83(ב)` |
| s 83(c) | privilege: a shareholder of a private company (to vote in writing if the articles so provide) | no-right: the company | `סעיף 83(ג)` |
| s 83(d) | none (a counting rule: which of two votes is counted) | none | `סעיף 83(ד)` |
| s 84 | none (a counting rule: a resolution is adopted by the count of votes; a private company may fix another) | none | `סעיף 84` |
| s 85 | none (a counting rule: ordinary majority unless another is fixed) | none | `סעיף 85` |
| s 86 | claim: whoever relies on the chair's declaration (it is prima facie evidence) | duty (a burden): whoever disputes it | `סעיף 86` |
| s 87(a) | privilege: a shareholder of a public company (to vote by a voting deed on the listed matters) | no-right: the company | `סעיף 87(א)` |
| s 87(b) | claim: every shareholder, to be sent a voting deed | duty: the company | `סעיף 87(ב)` |
| s 87(c),(d) | none (counting rules: a voting deed counts as presence for the quorum, as an abstention on a matter not voted on, and in the postponed meeting) | none | `סעיף 87(ג)`, `סעיף 87(ד)` |
| s 87(e) | privilege: a shareholder as section 177(1) describes (to vote on any matter by the electronic voting system) | no-right: the company | `סעיף 87(ה)` |
| s 88(a) | privilege: the board and the demander of a special meeting (to send a position notice); claim: that the company send it at its expense with the voting deed | no-right: the shareholders; duty: the company | `סעיף 88(א) - ...` (two rules) |
| s 88(b) | claim: a shareholder, to ask the company to send a position notice for him; who bears the cost as the Minister fixed or the company decided | duty: the company | `סעיף 88(ב) - ...` (two rules) |
| s 88(c) | privilege: the board (to respond with a position notice) | no-right: the shareholders | `סעיף 88(ג)` |
| s 88(d) | claim: a shareholder as section 177(1) describes, to a voting deed and position notices from the bourse member | duty: the bourse member | `סעיף 88(ד)` |
| s 89 | none (inert: a regulation-making power) | none | none |
| s 90(a) | claim: every shareholder, to minutes kept for seven years | duty: the company | `סעיף 90(א) - ...` (two rules) |
| s 90(b) | none (an evidence rule: signed minutes are prima facie evidence) | none | `סעיף 90(ב)` |
| s 90(c) | claim: a shareholder, to inspect the minutes register and to be sent a copy on request | duty: the company | `סעיף 90(ג) - ...` (two rules) |
| s 91(a) | power: the court (to cancel a resolution of a defective meeting); claim to apply: a shareholder | liability: the company and the resolution | `סעיף 91(א) - בית המשפט רשאי להורות על ביטול החלטה שהתקבלה באסיפה פגומה` |
| s 91(b) | disability: a shareholder who came to the meeting despite a defect in the notice of place or date (he cannot demand cancellation) | immunity: the company and the resolution, as against him | `סעיף 91(ב) - בעל מניה רשאי לדרוש את ביטול ההחלטה` |
| s 92(a) | none (a statement of the functions and powers of the board; its duty to carry them out is owed to the company and the shareholders) | none | ic1-part3-ch3-board.l4: `סעיף 92(א) - התפקיד או הסמכות הם של הדירקטוריון לפי סעיף 92(א)` |
| s 92(a)(12) | claim: the shareholders, that the board fix a minimum number of directors with accounting and financial expertise | duty: the board of a public company or a private bond company | `סעיף 92(א)(12) - ...` (two rules) |
| s 92(b) | immunity: the shareholders (the board's powers cannot be passed to the general manager) | disability: the board | `סעיף 92(ב) - סמכות של הדירקטוריון לפי סעיף 92 ניתנת לאצילה למנהל הכללי` |
| s 93(a) | privilege: a private company that is not a bond company (to have a board of one person) | no-right: the Registrar and others | `סעיף 93(א) - ...` |
| s 93(b) | none (a scope rule: which provisions apply to a board of one person) | none | `סעיף 93(ב) - ההוראות חלות על דירקטוריון המונה אדם אחד` |
| s 94(a) | claim: the shareholders, that the board of a public company or private bond company elect a chair | duty: the board | `סעיף 94(א) - הדירקטוריון יבחר אחד מחבריו לכהן כיושב ראש` |
| s 94(b) | privilege: a private non-bond company (not to appoint a chair); power: each director, if none is appointed (to convene the board and fix its agenda) | no-right: the shareholders; liability: the other directors | `סעיף 94(ב) - ...` (two rules) |
| s 95(a) | claim: the shareholders, that the chair of the board of a public company or private bond company is not the general manager, his relative, or a person subordinate to him | duty: the company and the person who would serve | `סעיף 95(א) - המועמד רשאי לכהן כיושב ראש הדירקטוריון` |
| s 95(b) | claim: the shareholders, that the chair is not vested with the general manager's powers or those of his subordinates and holds no other office in the company | duty: the company and the chair | `סעיף 95(ב) - ...` (three rules) |
| s 95(c),(d) | none (a scope rule and an extension to a private bond company) | none | `סעיף 95(א)`, `סעיף 95(ב)` |
| s 96(a),(b) | claim: the directors, that the chair (or the director chosen in his absence) manage the meeting; no additional vote for the director chosen in the chair's absence unless the articles give one | duty: the chair, or the board that chooses another to manage | `סעיף 96(א)`, `סעיף 96(ב) - ...` (two rules) |
| s 97 | claim: the shareholders and directors, to board meetings as often as the company's needs and the statutory frequency require | duty: the board and its chair | `סעיף 97 - הדירקטוריון התכנס בתדירות הנדרשת` |
| s 98(a) | power: the chair of the board (to convene the board at any time) | liability: the other directors | `סעיף 98(א)` |
| s 98(b) | claim: two directors (or one in a board of up to five, or one if the articles or section 257 so provide), that the board meet | duty: the board | `סעיף 98(ב) - הדירקטוריון יקיים ישיבה לדרישת דירקטורים` |
| s 98(c) | claim: the directors and the general manager and the external auditor who gave notice, that the chair convene the board | duty: the chair of the board | `סעיף 98(ג) - יושב ראש הדירקטוריון יכנס את הדירקטוריון` |
| s 98(d) | power: those who demanded or gave notice (to convene the board themselves after fourteen days) | liability: the chair of the board | `סעיף 98(ד) - רשאי לכנס בעצמו ישיבת דירקטוריון שלא כונסה בזמן` |
| s 99 | claim: a director or the general manager who asked in reasonable time, that a matter be on the agenda | duty: the chair of the board | `סעיף 99 - הנושא יכלל בסדר היום של ישיבת הדירקטוריון` |
| s 100(a),(b) | claim: each director, to notice a reasonable time before the meeting, at his address, with the place, date and a reasonable detail of the agenda | duty: the company (the chair of the board) | `סעיף 100(א)`, `סעיף 100(ב)` |
| s 100(c) | immunity: the directors of a public company and a private bond company (their right to notice and detail cannot be varied by the articles) | disability: the company | `סעיף 100(ג) - ניתן להתנות בתקנון על חובת הפירוט וחובת מסירת ההודעה במועד` |
| s 101 | privilege: the board (to meet by any means of communication) | no-right: the directors (unless the articles deny it) | `סעיף 101` |
| s 102 | privilege: the board of a private non-bond company (with all directors' consent), or of any company in urgent cases (with a majority) (to meet without notice) | no-right: the directors who were not given notice | `סעיף 102 - ...` (two rules) |
| s 103(a) | privilege: all the directors entitled to take part (to decide without meeting) | no-right: none (nobody can demand a meeting if all agree) | `סעיף 103(א)` |
| s 103(b),(c),(d) | claim: the directors, to a signed record of the decisions; duty: the chair of the board | duty: the chair of the board | `סעיף 103(ב)`, `סעיף 103(ג)`, `סעיף 103(ד)` |
| s 104 | none (a counting rule: the quorum of a board meeting) | none | `סעיף 104 - נכח מנין חוקי לפתיחת ישיבת דירקטוריון` |
| s 105 | none (a counting rule: one vote per director) | none | `סעיף 105` |
| s 106(a) | claim: the company, to the director's independent judgment and freedom from voting agreements | duty: the director | `סעיף 106(א) - הדירקטור הפר חובת אמונים` |
| s 106(b) | claim: the company and the directors, that only duly appointed directors act as directors and that no one impairs their independent judgment | duty: every person | `סעיף 106(ב)` |
| s 106(c) | claim: the company and the shareholders, to the standard of conduct of a director from whoever breached (b) | duty: the person who breached (b) | `סעיף 106(ג)` |
| s 107 | none (a counting rule: ordinary majority and the chair's additional vote) | none | `סעיף 107 - החלטת הדירקטוריון התקבלה` |
| s 108(a) | claim: the shareholders and directors, to minutes kept for seven years | duty: the company | `סעיף 108(א) - ...` (three rules) |
| s 108(b) | none (an evidence rule) | none | `סעיף 108(ב)` |
| s 109(a) | power: a director present who demanded abstention, or a director entitled to be invited who was absent (to demand cancellation of a resolution) | liability: the company and the resolution | `סעיף 109(א)(1)`, `סעיף 109(א)(2)`, `סעיף 109(א)(3)` |
| s 109(b) | immunity: the party towards whom an act was done innocently (its validity is preserved) | disability: the company and the directors who would cancel | `סעיף 109(ב)` |
| s 110(a) | power: the board (to set up committees) | liability: the directors | ic1-part3-ch3-committees.l4: `סעיף 110(א) - הדירקטוריון רשאי להקים ועדות דירקטוריון` |
| s 110(b),(c) | none (rules on who may serve on a committee) | none | `סעיף 110(ב)`, `סעיף 110(ג)` |
| s 111(a) | none (an attribution rule: a committee's decision is the board's) | none | `סעיף 111(א)` |
| s 111(b) | claim: the board, to reports from its committees and to their recommendations in good time | duty: the committee | `סעיף 111(ב) - ...` (two rules) |
| s 111(c),(d) | none (they extend other sub-chapters and section 108 to committees) | none | `סעיף 111(ג)`, `סעיף 111(ד)` |
| s 112(a) | immunity: the shareholders (seven matters stay with the full board) | disability: the board | `סעיף 112(א) - הדירקטוריון רשאי להאציל לועדה את הסמכות בנושא` |
| s 112(b) | immunity: the shareholders (the articles cannot vary (a)); power: the company (to add matters for the board only) | disability: the company | `סעיף 112(ב) - ...` (two rules) |
| s 112(c) | privilege: the board (to set up recommending committees on the listed matters) | no-right: the shareholders | `סעיף 112(ג)` |
| s 113 | power: the board (to cancel a committee's decision); immunity: a person who dealt with the company on the decision without knowing of the cancellation | liability: the committee; disability: the board | `סעיף 113 - ...` (two rules) |
| s 114 | claim: the shareholders, that the board of a public company or private bond company appoint an audit committee | duty: the board | `סעיף 114` |
| s 115(a)-(d) | claim: the shareholders, to an audit committee of at least three, with all external directors, a majority of independent directors, and none of the barred persons, chaired by an external director | duty: the board | `סעיף 115(א)`, `סעיף 115(ב)(1)`, `סעיף 115(ב)(2)`, `סעיף 115(ג)`, `סעיף 115(ד)` |
| s 115(e),(f) | privilege: a person within the exceptions (to be present at a meeting); the committee's chair (to admit a person to present a matter) | no-right: the committee's members | `סעיף 115(ה)`, `סעיף 115(ו)` |
| s 116(a) | claim and privilege: the internal auditor (to notices of committee meetings and to take part) | duty: the committee's chair | `סעיף 116(א)` |
| s 116(b) | power: the internal auditor (to ask for a meeting); claim: the internal auditor, that the chair convene it if the chair saw reason | duty: the chair of the committee | `סעיף 116(ב) - ...` (two rules) |
| s 116(c) | claim and privilege: the external auditor (to notice of a meeting on the audit of the financial statements and to take part) | duty: the committee's chair | `סעיף 116(ג)` |
| s 116A | none (a counting rule: the quorum of the audit committee) | none | `סעיף 116א` |
| s 117 | none (a statement of the audit committee's functions; the material-defect meeting is the committee's duty to the board) | none | `סעיף 117`, `סעיף 117(1)`, `סעיף 117(2א)` |
| s 118(a) | privilege: the board of a private non-bond company (to appoint an audit committee); immunity: that company's directors who are not employed by or serving the company | no-right: the shareholders; disability: the controlling shareholder (he and his relative cannot chair it) | `סעיף 118(א) - ...` (three rules) |
| s 118(b) | immunity: the shareholders of a private non-bond company (no such committee whose majority are material shareholders or their relatives) | disability: the board | `סעיף 118(ב)` |
| s 118A(a) | claim: the shareholders, that the board of a public company or private bond company appoint a compensation committee | duty: the board | `סעיף 118א(א)` |
| s 118A(b) | claim: the shareholders, to a compensation committee of at least three, the external directors the majority and the chair an external director | duty: the board | `סעיף 118א(ב)` |
| s 118A(c),(d) | none (they extend sub-chapter H and section 115(b)-(e) to the compensation committee and let an audit committee serve) | none | `סעיף 118א(ג)`, `סעיף 118א(ד)` |
| s 118B | none (a statement of the compensation committee's functions) | none | `סעיף 118ב` |

## Coverage table
The range is lines 263 to 947: 45 headings (the Part, the chapters and the sub-chapters of Parts 2 and 3 up to chapter 3) and 120 sections (2 to 118ב). The table has one row per heading (45 rows) and one row per section or subsection where the subsections differ in disposition (so 308 rows in all).
**Counts: encoded 224, fork 20, inert 60, repealed or blank in this text 4.** A `fork` row is one whose reading rests on an entry of the fork register below; it names the entry in its note and encodes the reading taken.
Every non-blank line from 263 to 947 falls inside the source-lines cell of some row (checked by script: 0 uncovered lines).
An `inert` row is a pure title (a heading), an editorial note of Wikisource ("a pure citation"), or machinery (a Minister's regulation-making power); each says which and what the provision does.
The repealed rows are the sub-chapter C heading "ערעור (בוטל)" (src:508), section 45 (src:510-511), section 54(b) (src:555) and section 69(b) (src:637).

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| heading: חלק 2 (Part 2) | src:263 | inert | none | A pure title (a heading): "Part 2: formation of the company"; it states no rule. |
| heading: חלק 2 פרק 1 (Part 2 chapter 1) | src:264 | inert | none | A pure title (a heading): "Chapter 1: incorporation". |
| heading: חלק 2 פרק 1 סימן א (sub-chapter A) | src:265 | inert | none | A pure title (a heading): "Sub-chapter A: the right to incorporate". |
| s 2 | src:267-268 | fork | ic1-part2-ch1-incorporation.l4: `סעיף 2 - כל אדם רשאי לייסד חברה` | Any person may found a company if no purpose is unlawful, immoral or against public policy. Fork F-ic1-1. |
| s 3 | src:270-271 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 3 - לחברה יכול שיהיה בעל מניה אחד` | A company may have one shareholder; zero shareholders is not answered (NOTHING). |
| heading: סימן ב (sub-chapter B) | src:273 | inert | none | A pure title (a heading): "Sub-chapter B: legal personality". |
| s 4 | src:275-276 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 4 - החברה כשרה לזכות, לחובה ולפעולה` | A company is a legal person capable of every right, duty and act consistent with its nature. |
| s 5 | src:278-279 | fork | ic1-part2-ch1-incorporation.l4: `סעיף 5 - החברה קיימת ביום` | Existence from the day of incorporation in the certificate to the lapse of incorporation. Fork F-ic1-2. |
| s 6(a)(1) | src:281-285 | fork | ic1-part2-ch1-incorporation.l4: `סעיף 6(א) - בית משפט רשאי לייחס חוב של חברה לבעל מניה בה` | Lifting the veil. Forks F-ic1-3 (the court's regard), F-ic1-5 (limb (b) is cumulative). |
| s 6(a)(2) | src:286 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 6(א)(2) - יראו אדם כמודע לשימוש` | Awareness includes suspicion plus refraining from checking, unless merely negligent. |
| s 6(b) | src:287 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 6(ב) - בית משפט רשאי לייחס תכונה, זכות או חובה של בעל מניה לחברה או להפך` | The court's finding is the input. |
| s 6(c) | src:288 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 6(ג) - בית משפט רשאי להשעות את זכות בעל המניה לפירעון חובו מאת החברה` | Depends on the conditions of 6(a) being met. |
| s 6(d) | src:289 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 6(ד) - בית המשפט לענין סעיפים 6 ו־7` | "The court" in sections 6 and 7 is the court with jurisdiction over the claim (section 1's own definition is deleted). |
| s 7(a) | src:291-292 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 7(א) - בית משפט רשאי להורות על צו הגבלה` | Restriction order up to five years after an attribution order under 6(a). |
| s 7(b) | src:293 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 7(ב) - על בית המשפט לשלוח לרשם הודעה על צו ההגבלה` | The court notifies the Registrar of a restriction order. |
| s 7(c) | src:294 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 7(ג) - המפר צו הגבלה חב בחובות החברה` | A breacher of a restriction order is liable for the company's debts arising in the restriction period. |
| heading: סימן ג (sub-chapter C) | src:296 | inert | none | A pure title (a heading): "Sub-chapter C: setting up a company and registering it". |
| s 8(a) | src:298-301 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 8(א) - הבקשה לרישום חברה הוגשה כדין` | Application for registration: electronic, in the Minister's form, with articles and first directors' declaration. |
| s 8(b) | src:302 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 8(ב) - הרשם רשאי לאפשר הגשת בקשה שלא בדרך אלקטרונית` | The Registrar's judgment is an input. |
| note after s 8(b) | src:303 | inert | none | A pure citation: an editorial note of Wikisource ("the Companies Regulations (Reporting, Registration Details and Forms), 5760-1999 were published"); it is not text of the Law. |
| s 9(a) | src:305-306 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 9(א) - על המבקש לרשום חברה לשלם אגרת רישום בעת הגשת הבקשה` | Registration fee on filing; the amount is set outside the Law. |
| s 9(b),(c) | src:307-308 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 9(ב) - חברה משלמת בכל שנה אגרה שנתית` | Annual fee; "company" includes a foreign company (core `חברת חוץ`). |
| s 10(a) | src:310-311 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 10(א) - הרשם ירשום חברה` | The Registrar's finding is an input. |
| s 10(b) | src:312 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 10(ב) - הרשם ייתן לחברה מספר רישום ויציין אותו בתעודת ההתאגדות` | Registration number (section 38(c)). |
| s 10(c) | src:313 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 10(ג) - הרשם ימסור לחברה שנרשמה תעודת התאגדות` |  |
| s 10(d) | src:314 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 10(ד) - תעודת התאגדות ראיה חלוטה לקיום דרישות הרישום` | Conclusive evidence; uses the core `תעודת התאגדות`. |
| s 10(e) | src:315 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 10(ה) - הצורך בתיקון פגם בתקנון נשאר אף לאחר התעודה` | The certificate does not cure a defect in the articles. |
| heading: סימן ד (sub-chapter D) | src:317 | inert | none | A pure title (a heading): "Sub-chapter D: the purpose of the company". |
| s 11(a) | src:319-320 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 11(א) - אפשר להביא בחשבון בשיקולים עסקיים להשאת רווחים` and `סעיף 11(א) - חברה רשאית לתרום למטרה ראויה` | Two rules: the considerations that may be weighed (open list) and the donation permission. |
| s 11(b) | src:321 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 11(ב) - הוראת סעיף קטן (א) חלה על החברה` | Does not apply to a public-benefit company. |
| heading: סימן ה (sub-chapter E) | src:323 | inert | none | A pure title (a heading): "Sub-chapter E: acts done by a promoter". |
| s 12(a) | src:325-326 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 12(א) - החברה רשאית לאשר פעולה של יזם שנעשתה לפני התאגדותה` | Uses the core `יזם`. |
| s 12(b) | src:327 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 12(ב) - האישור בדיעבד רשאי לפגוע בזכות של צד שלישי` | Ratification as authorisation in advance, without impairing a third party's right acquired in good faith and for consideration. |
| s 13(a) | src:329-333 | fork | ic1-part2-ch1-incorporation.l4: `סעיף 13(א) - לצד שלישי שידע על היזמות הברירה לראות ביזם בעל דברו או לחזור בו` | Three alternative triggers. Fork F-ic1-4 (time limits). |
| s 13(b) | src:334 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 13(ב) - היזם חייב או זכאי עוד בשל הפעולה` |  |
| s 13(c) | src:335 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 13(ג) - הוראות סעיף 13 חלות` | The parties may stipulate otherwise; the variation is an input. |
| s 14(1) | src:337-339 | encoded | ic1-part2-ch1-incorporation.l4: `סעיף 14(1) - פעולת היזם מחייבת או מזכה את היזם` | Third party unaware of the promotion. |
| s 14(2) | src:340 | encoded | ic1-part2-ch1-incorporation.l4: three rules `סעיף 14(2) - ...` | May approve; binds company and promoter jointly and severally; entitles only the company. |
| heading: חלק 2 פרק 2 (Part 2 chapter 2) | src:342 | inert | none | A pure title (a heading): "Chapter 2: the articles". |
| heading: חלק 2 פרק 2 סימן א (sub-chapter A) | src:343 | inert | none | A pure title (a heading): "Sub-chapter A: the contents of the articles and their amendment". |
| s 15 | src:345-346 | encoded | ic1-part2-ch2-articles.l4: `סעיף 15 - לחברה יש תקנון` | Every company has articles. |
| s 16 | src:348-349 | encoded | ic1-part2-ch2-articles.l4: `סעיף 16 - התקנון שנרשם עם ההתאגדות תקף` | Valid from incorporation; uses the core `יום ההתאגדות`. |
| s 17(a) | src:351-352 | encoded | ic1-part2-ch2-articles.l4: `סעיף 17(א) - דין התקנון כדין חוזה בין הצדדים` | Uses the core `צד`. |
| s 17(b) | src:353 | encoded | ic1-part2-ch2-articles.l4: `סעיף 17(ב) - שינוי התקנון נעשה בדרכים הקבועות בחוק זה` | The amendment must be made in the ways this Law provides. |
| s 18 | src:355-360 | encoded | ic1-part2-ch2-articles.l4: `סעיף 18 - התקנון כולל את הפרטים שחובה לכלול בו` | Four mandatory items. |
| s 19 lead-in, (1), (2) | src:362-365 | encoded | ic1-part2-ch2-articles.l4: `סעיף 19 - חברה רשאית לכלול בתקנון נושא` | Open list ("including"). |
| s 19(2א) governance provisions | src:366 | encoded | ic1-part2-ch2-articles.l4: `סעיף 19 - חברה רשאית לכלול בתקנון נושא` | The first clause: recommended governance provisions of the First Schedule (the Schedule is piece ic6's). |
| s 19(2א) Minister's power to amend the First Schedule | src:366 | inert | none | Machinery: a power of the Minister, with the approval of the Knesset Constitution, Law and Justice Committee and (for public and bond companies) after consulting the Securities Authority chairperson, to amend the First Schedule. It decides nothing for a person in the seat. |
| s 19(3) | src:367 | encoded | ic1-part2-ch2-articles.l4: `סעיף 19 - חברה רשאית לכלול בתקנון נושא` | Any other matter the shareholders see fit. |
| s 20(a) | src:369-370 | fork | ic1-part2-ch2-articles.l4: `סעיף 20(א) - חברה רשאית לשנות את תקנונה בהחלטה ברוב רגיל באסיפה הכללית` | Ordinary majority unless the articles fix another or a section 22 resolution exists. Fork F-ic1-6. |
| s 20(b) | src:371 | fork | ic1-part2-ch2-articles.l4: `סעיף 20(ב) - שינוי הוראה מוגנת ברוב המסוים או ברוב המוצע לפי הגבוה` | Fork F-ic1-7. |
| s 20(c) | src:372 | encoded | ic1-part2-ch2-articles.l4: `סעיף 20(ג) - שינוי הפוגע בזכויות סוג מניות טעון אישור אסיפת הסוג` | Class protection. |
| s 20(d) | src:373 | encoded | ic1-part2-ch2-articles.l4: `סעיף 20(ד) - שינוי בתקנון מחייב בעל מניה` | No new liability without consent. |
| s 21(a) | src:375-376 | encoded | ic1-part2-ch2-articles.l4: `סעיף 21(א) - היום שבו שינוי התקנון תקף` | NOTHING for a section 40 amendment. |
| s 21(b) | src:377 | encoded | ic1-part2-ch2-articles.l4: `סעיף 21(ב) - החברה מסרה לרשם את נוסח ההחלטה בתוך ארבעה עשר ימים` | Fourteen days; the last day is inside. |
| s 22(a) | src:379-380 | encoded | ic1-part2-ch2-articles.l4: `סעיף 22(א) - חברה רשאית להגביל את סמכותה לשנות את התקנון` |  |
| s 22(b) | src:381 | encoded | ic1-part2-ch2-articles.l4: `סעיף 22(ב) - החלטה להגביל את סמכות השינוי דינה כדין החלטה לשינוי התקנון` |  |
| s 23(a) | src:383-384 | encoded | ic1-part2-ch2-articles.l4: `סעיף 23(א) - התקנון נחתם ופורטו בו בעלי המניות הראשונים` |  |
| s 23(b) | src:385 | encoded | ic1-part2-ch2-articles.l4: `סעיף 23(ב) - זהות החותמים על התקנון אומתה` | The regulations on online verification are not among the inputs. |
| s 24 lead-in and (1) | src:387-389 | encoded | ic1-part2-ch2-articles.l4: `סעיף 24(1) - חברה שהתאגדה לפני תחילת החוק רשאית לשנות את תזכירה`, `סעיף 24(1) - היום שבו שינוי ההון הרשום תקף`, `סעיף 24(1) - שינוי שם החברה לפי פסקה זו טעון הסכמת השר` | Three rules for the three clauses of paragraph (1). |
| s 24(2) | src:390 | encoded | ic1-part2-ch2-articles.l4: `סעיף 24(2) - חברה שהתאגדה לפני תחילת החוק רשאית לשנות את תזכירה או לבטלו` | Section 350 is piece ic6's. |
| s 24(3) | src:391 | encoded | ic1-part2-ch2-articles.l4: `סעיף 24(3) - חברה שהתאגדה לפני תחילת החוק רשאית לשנות את הוראות תקנונה` |  |
| s 24(4) | src:392 | encoded | ic1-part2-ch2-articles.l4: `סעיף 24(4) - חברה שהתאגדה לפני תחילת החוק רשאית לקבוע בתקנון הוראה בדבר הרוב הדרוש לשינויו` |  |
| s 24(5) | src:393 | encoded | ic1-part2-ch2-articles.l4: `סעיף 24(5) - חברה שהתאגדה לפני תחילת החוק רשאית לקבוע בתזכיר הוראה בדבר שינוי הרוב הדרוש לשינוי התזכיר` |  |
| heading: חלק 2 פרק 2 סימן ב (sub-chapter B) | src:395 | inert | none | A pure title (a heading): "Sub-chapter B: the name of the company". |
| s 25 | src:397-398 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 25 - חברה רשאית להירשם בכל שם` |  |
| s 26 | src:400-401 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 26 - שם חברה בערבון מוגבל כולל בסופו את הציון` |  |
| s 27(a)(1) | src:403-405 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 27(א)(1) - השם אסור לרישום בשל שם של תאגיד קיים` |  |
| s 27(a)(2) | src:406 | fork | ic1-part2-ch2-name-capital.l4: `סעיף 27(א)(2) - השם אסור לרישום בשל סימן מסחר רשום` | Fork F-ic1-8 (the consent exception). |
| s 27(b) | src:407 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 27(ב) - השם אסור לרישום בשל תרמית או הטעיה` | The Registrar's opinion is the input. |
| s 28 | src:409-410 | fork | ic1-part2-ch2-name-capital.l4: `סעיף 28 - השם אסור לרישום מפני שעלול לפגוע בתקנת הציבור או ברגשותיו` | Fork F-ic1-9. |
| s 29(a) | src:412-413 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 29(א) - הרשם רשאי לדרוש מחברה לשנות את שמה` |  |
| s 29(b) | src:414 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 29(ב) - הרשם רשאי לשנות את שם החברה לשם שיבחר` | Four months. |
| s 29(c) | src:415 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 29(ג) - הרשם ישלח לחברה תעודת שינוי שם והשינוי נחשב כהחלטת החברה והרשם` |  |
| s 29(d) | src:416 | inert | none | Machinery: a power of the Minister to set provisions on the publication of a change of name (a regulation-making power). |
| s 30 | src:418-419 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 30 - בית המשפט רשאי להורות להימנע משימוש בשם` |  |
| s 31(a) | src:421-422 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 31(א) - חברה רשאית באישור הרשם לשנות את שמה` |  |
| s 31(b) | src:423 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 31(ב) - הרשם ירשום את השם החדש ויתן לחברה תעודת שינוי שם` |  |
| heading: חלק 2 פרק 2 סימן ג (sub-chapter C) | src:425 | inert | none | A pure title (a heading): "Sub-chapter C: the purposes of the company". |
| s 32 | src:427-431 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 32 - החברה ציינה את מטרותיה בתקנון באחד האופנים שבחוק` | A closed list of three. |
| heading: חלק 2 פרק 2 סימן ד (sub-chapter D) | src:433 | inert | none | A pure title (a heading): "Sub-chapter D: the registered share capital and its division". |
| s 33 | src:435-436 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 33 - החברה קבעה בתקנונה את הון המניות הרשום` |  |
| s 34(a) | src:438-439 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 34(א) - מניות החברה כולן בעלות ערך נקוב או כולן ללא ערך נקוב` |  |
| s 34(b) | src:440 | fork | ic1-part2-ch2-name-capital.l4: `סעיף 34(ב) - התקנון מציין את מספר המניות ואת ערכן הנקוב` | Fork F-ic1-10. |
| s 34(c) | src:441 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 34(ג) - הון המניות הרשום בחברה שמניותיה ללא ערך נקוב` and `סעיף 34(ג) - ההון המונפק בחברה שמניותיה ללא ערך נקוב` |  |
| heading: חלק 2 פרק 2 סימן ה (sub-chapter E) | src:443 | inert | none | A pure title (a heading): "Sub-chapter E: the limit on liability". |
| s 35(a) | src:445-446 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 35(א) - התקנון מציין שהאחריות בלתי מוגבלת או מפרט את אופן ההגבלה` |  |
| s 35(b) | src:447 | encoded | ic1-part2-ch2-name-capital.l4: `סעיף 35(ב) - בעלי המניות אחראים לפירעון הערך הנקוב לפחות` | Section 304 is piece ic3's. |
| heading: חלק 2 פרק 3 (Part 2 chapter 3) | src:449 | inert | none | A pure title (a heading): "Chapter 3: the Registrar of Companies". |
| heading: חלק 2 פרק 3 סימן א (sub-chapter A) | src:450 | inert | none | A pure title (a heading): "Sub-chapter A: the Companies Registration Office". |
| s 36(a) | src:452-453 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 36(א) - האדם הוא רשם החברות` | Who the Registrar is: a State employee qualified to be a magistrates' court judge, appointed by the Minister. |
| s 36(b) | src:454 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 36(ב) - האדם הוא סגן הרשם ויש לו סמכויות הרשם` |  |
| s 36(c) | src:455 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 36(ג) - עובד משרד המשפטים מוסמך בסמכויות הרשם כשנבצר מהרשם למלא את תפקידו` |  |
| s 37(a) | src:457-462 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 37(א) - הרשם קובע אם נתמלאו התנאים והדרישות בענין` | A closed list of four matters. |
| s 37(b) | src:463 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 37(ב) - הרשם רשאי לדרוש המצאת מרשמים ופנקסים בתוך תקופה של ארבעה עשר ימים לפחות` | At least fourteen days. |
| s 37(c) | src:464 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 37(ג) - הרשם רשאי להורות לחברה לעדכן את המרשמים והפנקסים` | The Registrar's satisfaction is the input. |
| heading: חלק 2 פרק 3 סימן ב (sub-chapter B) | src:466 | inert | none | A pure title (a heading): "Sub-chapter B: keeping the registers". |
| s 38(a) | src:468-469 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 38(א) - הרשם ינהל רישום לגבי כל חברה ויקבל מסמכים ודיווחים` |  |
| s 38(b) | src:470 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 38(ב) - המסמך או הדיווח נמסר כדין` | Electronic unless the Registrar allows otherwise. |
| note after s 38(b) | src:471 | inert | none | A pure citation: an editorial note of Wikisource that the Companies Regulations (Reporting, Registration Details and Forms), 5760-1999 were published; it is not text of the Law. |
| s 38(c) | src:472 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 38(ג) - הרשם ירשום כל חברה במרשם החברות ויתן לה מספר זהות` |  |
| s 39(a) | src:474-475 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 39(א) - המסמך או הדיווח נושא את מספר הזהות וחתום בידי נושא משרה` | Uses the core `נושא משרה`. |
| s 39(b) | src:476 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 39(ב) - מסמך או דיווח של חברה בכינוס, בפירוק או בהליכי חדלות פירעון יכול שייחתם בידי כונס הנכסים או הנאמן` |  |
| s 39(c) | src:477 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 39(ג) - הוראות סעיף 39 חלות` |  |
| s 39(d) | src:478 | inert | none | Machinery: a power of the Minister, where he has set a provision on electronic reporting, to provide that the signature requirement of (a) does not apply to documents so filed (a regulation-making power). |
| s 40 | src:480-484 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 40 - לפעולה יש תוקף רק אם נרשמה` | A closed list of three acts; NOTHING for any other. |
| s 41(a) | src:486-487 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 41(א) - ...` (two rules) | A certified copy is accepted as an original and is conclusive evidence that the original is in the office. |
| s 41(b) | src:488 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 41(ב) - הוראות סעיף 41(א) חלות על פלט של דיווח אלקטרוני` |  |
| s 42 | src:490-491 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 42 - רישום או קיום של מסמך כשלעצמו ראיה לידיעת תוכנו` | The constant FALSE. |
| s 43(a) | src:493-494 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 43(א) - כל אדם רשאי לעיין במרשמים ולקבל העתקים מאושרים` |  |
| s 43(b) | src:495 | encoded | ic1-part2-ch3-registrar.l4: `סעיף 43(ב) - פרט (2) לתוספת הרביעית פתוח לעיון גוף ציבורי השולח מסרים דיגיטליים בלבד` | Item (2) of the Fourth Schedule is piece ic6's. |
| s 44 | src:497-504 | inert | none | Machinery: the Minister's regulation-making powers (procedures of registration and filing, the keeping of the registers, forms, the particulars companies must give about shareholders, creditors and office-holders, and the amounts of the registration fee and the annual fee, with interest and arrears on unpaid fees). The amounts are inputs wherever a rule needs them (sections 9(a) and 9(b)). |
| notes after s 44 | src:505-506 | inert | none | A pure citation: two editorial notes of Wikisource that the Companies Regulations (Reporting, Registration Details and Forms), 5760-1999 and the Companies Regulations (Fees), 5761-2001 were published; they are not text of the Law. |
| heading: חלק 2 פרק 3 סימן ג (sub-chapter C, appeal) | src:508 | repealed or blank in this text | none | The heading reads "ערעור {{ח:הערה\|(בוטל)}}": the sub-chapter on appeals is marked repealed ("(בוטל)"). |
| s 45 | src:510-511 | repealed or blank in this text | none | The section opens with no heading and its text is "{{ח:הערה\|(בוטל).}}" (repealed). |
| heading: חלק 3 (Part 3) | src:513 | inert | none | A pure title (a heading): "Part 3: the structure of the company". |
| heading: חלק 3 פרק 1 (Part 3 chapter 1) | src:514 | inert | none | A pure title (a heading): "Chapter 1: the organs of the company, their powers and liability for their acts". |
| heading: חלק 3 פרק 1 סימן א (sub-chapter A) | src:515 | inert | none | A pure title (a heading): "Sub-chapter A: the organs". |
| s 46 | src:517-518 | encoded | ic1-part3-ch1-organs.l4: `סעיף 46 - הגוף הוא אורגן של החברה` | Uses the core `צד`. |
| s 47 | src:520-521 | encoded | ic1-part3-ch1-organs.l4: `סעיף 47 - מעשי אורגן וכוונותיו הם מעשי החברה וכוונותיה` |  |
| heading: חלק 3 פרק 1 סימן ב (sub-chapter B) | src:523 | inert | none | A pure title (a heading): "Sub-chapter B: the division of powers between the principal organs". |
| s 48(a)-(c) | src:525-528 | encoded | ic1-part3-ch1-organs.l4: `סעיף 48(א) עד (ג) - הסמכות נתונה לאורגן` | Whether a power is listed in the sub-chapter or chapter concerned is a plain input. |
| s 48(d) | src:529 | fork | ic1-part3-ch1-organs.l4: `סעיף 48(ד) - סמכויות העזר נתונות לכל האורגנים` | "All the organs" is every organ of section 46, not only the three principal ones. Fork F-ic1-20. |
| s 49 | src:531-532 | encoded | ic1-part3-ch1-organs.l4: `סעיף 49 - הדירקטוריון רשאי להפעיל סמכות של החברה שלא הוקנתה לאורגן אחר` |  |
| s 50(a) | src:534-535 | encoded | ic1-part3-ch1-organs.l4: `סעיף 50(א) - חברה רשאית לקבוע בתקנונה העברת סמכויות בין האורגנים` | The period may not exceed the period required in the circumstances. |
| s 50(b) | src:536 | encoded | ic1-part3-ch1-organs.l4: `סעיף 50(ב) - על בעלי המניות חלים זכויות, חובות ואחריות של דירקטורים` | Part 6 chapters 3 to 5 (piece ic3) give the content. |
| s 51 | src:538-539 | encoded | ic1-part3-ch1-organs.l4: `סעיף 51 - הדירקטוריון רשאי להורות למנהל הכללי כיצד לפעול לענין מסוים` and `סעיף 51 - הדירקטוריון רשאי להפעיל במקום המנהל הכללי את הסמכות הנדרשת לביצוע ההוראה` |  |
| s 52(a) | src:541-542 | encoded | ic1-part3-ch1-organs.l4: `סעיף 52(א) - האסיפה הכללית רשאית להפעיל סמכות של הדירקטוריון שנבצר ממנו להפעילה` | Section 50(b) applies to this exercise (see s 50(b)). |
| s 52(b) | src:543 | encoded | ic1-part3-ch1-organs.l4: `סעיף 52(ב) - הדירקטוריון רשאי להפעיל סמכויות של המנהל הכללי שנבצר ממנו להפעילן` |  |
| heading: חלק 3 פרק 1 סימן ג (sub-chapter C) | src:545 | inert | none | A pure title (a heading): "Sub-chapter C: the company's liability for the acts of the organs". |
| s 53(a) | src:547-548 | encoded | ic1-part3-ch1-organs.l4: `סעיף 53(א) - חברה חבה במישרין באחריות בנזיקין על עוולה שבוצעה בידי אורגן שלה` |  |
| s 53(b) | src:549 | encoded | ic1-part3-ch1-organs.l4: `סעיף 53(ב) - אחריותה השילוחית של חברה בנזיקין נשמרת` |  |
| heading: חלק 3 פרק 1 סימן ד (sub-chapter D) | src:551 | inert | none | A pure title (a heading): "Sub-chapter D: the liability of the individuals who make up the organ". |
| s 54(a) | src:553-554 | encoded | ic1-part3-ch1-organs.l4: `סעיף 54(א) - ייחוס פעולת אורגן לחברה אינו גורע מאחריותם האישית של יחידי האורגן` |  |
| s 54(b) | src:555 | repealed or blank in this text | none | The subsection reads "{{ח:הערה\|(בוטל).}}" (repealed). |
| heading: חלק 3 פרק 1 סימן ה (sub-chapter E) | src:557 | inert | none | A pure title (a heading): "Sub-chapter E: preventing an act in excess of authority". |
| s 55(a) | src:559-560 | encoded | ic1-part3-ch1-organs.l4: `סעיף 55(א) - הפעולה אסורה על החברה ועל מי שפועל מטעמה` |  |
| s 55(b) | src:561 | fork | ic1-part3-ch1-organs.l4: `סעיף 55(ב) - בית המשפט רשאי לתת צו להפסקת פעולה חורגת או למניעתה` | Fork F-ic1-11. |
| s 56(a) | src:563-564 | encoded | ic1-part3-ch1-organs.l4: `סעיף 56(א) - לפעולה יש תוקף כלפי החברה` | The party's two states of mind are cumulative. |
| s 56(b) | src:565 | encoded | ic1-part3-ch1-organs.l4: `סעיף 56(ב) - אישור החברה בדיעבד לפעולה חורגת` | The majority is the one needed to change the purposes (section 20). |
| s 56(c) | src:566 | encoded | ic1-part3-ch1-organs.l4: `סעיף 56(ג) - האישור רשאי לפגוע בזכות שרכש אדם אחר` |  |
| heading: חלק 3 פרק 2 (Part 3 chapter 2) | src:568 | inert | none | A pure title (a heading): "Chapter 2: the general meeting". |
| heading: חלק 3 פרק 2 סימן א (sub-chapter A) | src:569 | inert | none | A pure title (a heading): "Sub-chapter A: the powers of the general meeting". |
| s 57 | src:571-580 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 57 - סעיף זה מחייב לקבל את ההחלטה באסיפה הכללית` | Eight kinds of matter; whether a matter falls under a listed section of another piece is the caller's fact. |
| s 58(a) | src:582-583 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 58(א) - חברה רשאית להתנות על הוראות סעיף 57` | The constant FALSE. |
| s 58(b) | src:584 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 58(ב) - חברה רשאית להוסיף בתקנון נושאים שהחלטות בהם יתקבלו באסיפה הכללית` and `סעיף 58(ב) - העברת סמכות לאסיפה הכללית בתקנון נעשתה כדין` |  |
| s 59 | src:586-587 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 59 - האסיפה הכללית השנתית ממנה את הדירקטורים` | Unless the articles say otherwise. |
| heading: חלק 3 פרק 2 סימן ב (sub-chapter B) | src:589 | inert | none | A pure title (a heading): "Sub-chapter B: the annual meeting and the special meeting". |
| s 60(a) | src:591-592 | fork | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 60(א) - החברה קיימה אסיפה שנתית בתוך חמישה עשר חודשים` | Fork F-ic1-12. |
| s 60(b) | src:593 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 60(ב) - סדר היום באסיפה השנתית כולל דיון בדוחות הכספיים ובדיווח הדירקטוריון` and `סעיף 60(ב) - הנושא יכול להיכלל בסדר היום של האסיפה השנתית` |  |
| s 61(a) | src:595-596 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 61(א) - החברה חייבת לקיים אסיפה שנתית` | Uses the core `חברה פרטית`. |
| s 61(b) | src:597 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 61(ב) - החברה שלחה לבעלי המניות הרשומים דוחות כספיים במועד` | The statements are those of section 172 (piece ic2). |
| s 62(a) | src:599-600 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 62(א) - בית המשפט רשאי להורות על כינוס אסיפה שנתית` |  |
| s 62(b) | src:601 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 62(ב) - החברה נושאת בהוצאות הסבירות של המבקש` and `סעיף 62(ב) - הדירקטור האחראי לאי כינוס האסיפה חייב להשיב את ההוצאות לחברה` |  |
| s 63(a) | src:603-606 | fork | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 63(א) - הדירקטוריון של חברה פרטית חייב לכנס אסיפה מיוחדת` | Fork F-ic1-13 (the holdings of several demanders). |
| s 63(b) | src:607-609 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 63(ב) - הדירקטוריון של חברה ציבורית חייב לכנס אסיפה מיוחדת` |  |
| s 63(c) | src:610 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 63(ג) - הדירקטוריון זימן את האסיפה המיוחדת בתוך עשרים ואחד ימים` and `סעיף 63(ג) - מועד הכינוס של אסיפה מיוחדת בחברה ציבורית` | For a private company the date is governed by section 67 (NOTHING here). |
| s 64(a) | src:612-613 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 64(א) - הדורש רשאי לכנס את האסיפה בעצמו` |  |
| s 64(b) | src:614 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 64(ב) - החברה מכסה את ההוצאות הסבירות של הדורש` and `סעיף 64(ב) - הדירקטור האחראי לאי כינוס האסיפה חייב להשיב את ההוצאות לחברה` |  |
| s 65(a) | src:616-617 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 65(א) - בית המשפט רשאי להורות על כינוס אסיפה מיוחדת שנדרשה` |  |
| s 65(b) | src:618 | encoded | ic1-part3-ch2-gm-powers-and-calling.l4: `סעיף 65(ב) - החברה נושאת בהוצאות הסבירות של המבקש בהליך` and `סעיף 65(ב) - הדירקטור האחראי לאי כינוס האסיפה חייב להשיב את ההוצאות לחברה` |  |
| heading: חלק 3 פרק 2 סימן ג (sub-chapter C) | src:620 | inert | none | A pure title (a heading): "Sub-chapter C: calling the general meeting and conducting it". |
| s 66(a) | src:622-623 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 66(א) - הנושא חייב להיכלל בסדר היום` |  |
| s 66(b) request | src:624 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 66(ב) - בעלי מניות רשאים לבקש מהדירקטוריון לכלול נושא בסדר היום` | One percent of the voting rights; the matter must be suitable for a general meeting. |
| s 66(b) Minister's power | src:624 | inert | none | Machinery: the Minister's power to set provisions for the section, including the time for submitting the request (a regulation-making power). |
| note after s 66(b) | src:625 | inert | none | A pure citation: an editorial note of Wikisource that the Companies Regulations (Notice and Advertisement of a General Meeting and a Class Meeting in a Public Company and Adding a Matter to the Agenda), 5760-2000 were published; it is not text of the Law. |
| s 66(c) | src:626 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 66(ג) - באסיפה כללית מתקבלות החלטות בנושאים שפורטו בסדר היום בלבד` |  |
| s 67 | src:628-629 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 67 - ההזמנה לאסיפה כללית בחברה פרטית נמסרה במועד` | Seven days at least and forty-five days at most, unless the articles fix otherwise (two inputs). |
| s 68(a) | src:631-632 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 68(א) - ההזמנה לאסיפה כללית בחברה פרטית כוללת את הפרטים הנדרשים` |  |
| s 68(b) | src:633 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 68(ב) - בהזמנה פורט נוסח השינוי המוצע בתקנון` |  |
| s 69(a) | src:635-636 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 69(א) - ההודעה על אסיפה כללית בחברה ציבורית פורסמה או נמסרה כדין` | What the Minister set is out of range. |
| s 69(b) | src:637 | repealed or blank in this text | none | The subsection reads "{{ח:הערה\|(בוטל).}}" (repealed). |
| s 69(c) | src:638 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 69(ג) - ההודעה כוללת את סדר היום, ההחלטות המוצעות והסדרי ההצבעה בכתב` |  |
| s 69(d) | src:639 | inert | none | Machinery: the Minister's power, after consulting the Securities Authority, to set provisions on the detailing of matters and on further contents of the notice (a regulation-making power). |
| s 70 | src:641-642 | inert | none | Machinery: the Minister's power to provide that, where the text of the resolutions was detailed in the invitation or notice, the general meeting may adopt resolutions different from it, in matters and by criteria he fixes (a regulation-making power). |
| note after s 70 | src:643 | inert | none | A pure citation: an editorial note of Wikisource that the Companies Regulations (Changing a Resolution Detailed in a Notice of a General Meeting), 5764-2004 were published; it is not text of the Law. |
| s 71 entitlement | src:645-646 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 71 - בעל מניה בחברה ציבורית זכאי לאישור בעלות מחבר הבורסה` | A bourse member is the Securities Law's term (a plain fact). |
| s 71 Minister's power | src:646 | inert | none | Machinery: the Minister's power to fix the manner of the certificate of ownership and the conditions, circumstances and amount of any payment for it (a regulation-making power). |
| note after s 71 | src:647 | inert | none | A pure citation: an editorial note of Wikisource that the Companies Regulations (Proof of Ownership of a Share for Voting in the General Meeting), 5760-2000 were published; it is not text of the Law. |
| s 72 | src:649-650 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 72 - בית המשפט רשאי להורות על כינוס וניהול אסיפה בדרך שיקבע` |  |
| s 73 | src:652-653 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 73 - חברה ציבורית תקיים אסיפה כללית בישראל` |  |
| s 74(a) | src:655-656 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 74(א) - אסיפה כללית שיש בה מנין חוקי רשאית להחליט על דחיית האסיפה` and `סעיף 74(א) - באסיפה נדחית נדון נושא שהיה על סדר היום ולא נתקבלה לגביו החלטה` |  |
| s 74(b) | src:657 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 74(ב) - על הודעות והזמנות לאסיפה שנדחתה ליותר מעשרים ואחד ימים חלים סעיפים 67 עד 69` |  |
| s 74(c) | src:658 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 74(ג) - ההודעה על המועד החדש ניתנה לא יאוחר משבעים ושתיים שעות לפני האסיפה` | NOTHING where the agenda was changed or the date is more than 21 days off. |
| s 75 | src:660-661 | encoded | ic1-part3-ch2-gm-convening.l4: `סעיף 75 - הוראות סימנים ג׳ עד ו׳ חלות על אסיפת סוג` |  |
| heading: חלק 3 פרק 2 סימן ד (sub-chapter D) | src:663 | inert | none | A pure title (a heading): "Sub-chapter D: a general meeting in a private company". |
| s 76 | src:665-666 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 76 - בחברה פרטית ניתן לקבל החלטה באסיפה כללית ללא הזמנה וללא התכנסות` |  |
| s 77 | src:668-669 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 77 - חברה פרטית רשאית לקיים אסיפה כללית באמצעי תקשורת` |  |
| heading: חלק 3 פרק 2 סימן ה (sub-chapter E) | src:671 | inert | none | A pure title (a heading): "Sub-chapter E: the quorum in a general meeting and the chair of the meeting". |
| s 78(a) | src:673-674 | fork | ic1-part3-ch2-gm-conduct.l4: `סעיף 78(א) - באסיפה כללית נכח מנין חוקי` | Fork F-ic1-14. The articles' own quorum (section 81) is an input. |
| s 78(b) | src:675 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 78(ב) - האסיפה נדחית לשבוע ימים או למועד מאוחר יותר שצויין` |  |
| s 78(c) | src:676 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 78(ג) - הוראות סימן ה׳ חלות על החברה` |  |
| s 79(a) | src:678-679 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 79(א) - האסיפה הנדחית מתקיימת בכל מספר משתתפים` |  |
| s 79(b) | src:680 | fork | ic1-part3-ch2-gm-conduct.l4: `סעיף 79(ב) - האסיפה הנדחית שכונסה על פי דרישה מתקיימת רק אם נכחו בעלי מניות במספר הדרוש` | Fork F-ic1-15. |
| s 80(a) | src:682-683 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 80(א) - באסיפה כללית ייבחר יושב ראש לאותה אסיפה` |  |
| s 80(b) | src:684 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 80(ב) - הדיון שבו נבחר יושב ראש האסיפה נפתח כדין` |  |
| s 81 | src:686-687 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 81 - ניתן להתנות בתקנון על הוראות סימן ה׳` | The constant TRUE; the sub-chapter's rules take the articles' variation as an input. |
| heading: חלק 3 פרק 2 סימן ו (sub-chapter F) | src:689 | inert | none | A pure title (a heading): "Sub-chapter F: voting in the general meeting". |
| s 82(a) | src:691-692 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 82(א) - חברה רשאית לקבוע בתקנונה זכויות הצבעה שונות לסוגים שונים של מניות` |  |
| s 82(b) | src:693 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 82(ב) - זכויות הצבעה שונות בתקנון תקפות כל עוד הן עומדות בהוראת חיקוק אחר` |  |
| s 82(c) | src:694 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 82(ג) - מספר הקולות של מניה` |  |
| s 83(a) | src:696-697 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 83(א) - בעל מניה בחברה ציבורית רשאי להצביע בדרך` |  |
| s 83(b) | src:698 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 83(ב) - בעל מניה בחברה פרטית רשאי להצביע בעצמו או באמצעות שלוח` |  |
| s 83(c) | src:699 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 83(ג) - בעל מניה בחברה פרטית רשאי להצביע בכתב` |  |
| s 83(d) | src:700 | fork | ic1-part3-ch2-gm-conduct.l4: `סעיף 83(ד) - ההצבעה הנמנית של בעל מניה שהצביע ביותר מדרך אחת` | Fork F-ic1-16. |
| s 84 | src:702-703 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 84 - החלטה באסיפה הכללית מתקבלת בהצבעה במנין קולות` | Uses the core `מנין קולות` through the helpers of ic1-majorities.l4. |
| s 85 | src:705-706 | fork | ic1-part3-ch2-gm-conduct.l4: `סעיף 85 - החלטת האסיפה הכללית התקבלה ברוב הנדרש` | Ordinary majority: fork F-ic1-6. |
| s 86 | src:708-709 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 86 - הכרזת היושב ראש ראיה לכאורה לכך שההחלטה נתקבלה` |  |
| heading: חלק 3 פרק 2 סימן ז (sub-chapter G) | src:711 | inert | none | A pure title (a heading): "Sub-chapter G: voting in writing and position notices". |
| s 87(a) | src:713-720 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 87(א) - בעל מניה בחברה ציבורית רשאי להצביע בכתב הצבעה בענין` | Seven kinds of matter. |
| s 87(b) | src:721 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 87(ב) - על החברה לשלוח כתב הצבעה לכל בעלי מניותיה` |  |
| s 87(c) | src:722 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 87(ג) - כתב הצבעה נחשב כנוכחות באסיפה לענין המנין החוקי` | Produces the core input `בעל המניות נוכח באמצעות כתב הצבעה כאמור בסעיף 87`. |
| s 87(d) | src:723 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 87(ד) - ...` (two rules) |  |
| s 87(e) | src:724 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 87(ה) - בעל מניה רשאי להצביע במערכת ההצבעה האלקטרונית גם בכל נושא אחר שעל סדר היום` | Section 177(1) is piece ic2's. |
| s 88(a) | src:726-727 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 88(א) - רשאים לפנות לבעלי המניות בהודעת עמדה` and `סעיף 88(א) - החברה שולחת את הודעות העמדה על חשבונה ביחד עם כתב ההצבעה` |  |
| s 88(b) | src:728 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 88(ב) - בעל מניה רשאי לבקש מהחברה לשלוח הודעת עמדה מטעמו` and `סעיף 88(ב) - הודעת עמדה של בעל מניה היא על חשבון החברה` | What the Minister fixed (section 89) is an input. |
| s 88(c) | src:729 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 88(ג) - הדירקטוריון רשאי לשלוח הודעת עמדה בתגובה` |  |
| s 88(d) | src:730 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 88(ד) - בעל מניה זכאי לקבל מחבר הבורסה כתב הצבעה והודעות עמדה` |  |
| s 89 | src:732-741 | inert | none | Machinery: the Minister's power, in consultation with the Minister of Finance and the Securities Authority, to set provisions on voting deeds and position notices (additional matters, exemptions, delivery, payment, publication, supervision, form) (a regulation-making power). |
| note after s 89 | src:742 | inert | none | A pure citation: an editorial note of Wikisource that the Companies Regulations (Voting in Writing and Position Notices), 5766-2005 were published; it is not text of the Law. |
| heading: חלק 3 פרק 2 סימן ח (sub-chapter H) | src:744 | inert | none | A pure title (a heading): "Sub-chapter H: the minutes of the meeting". |
| s 90(a) | src:746-747 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 90(א) - על החברה לערוך פרוטוקולים של ההליכים באסיפה הכללית` and `סעיף 90(א) - על החברה לשמור את הפרוטוקולים במשרדה הרשום` |  |
| s 90(b) | src:748 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 90(ב) - פרוטוקול חתום בידי יושב ראש האסיפה ראיה לכאורה לאמור בו` |  |
| s 90(c) | src:749 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 90(ג) - בעל מניות רשאי לעיין במרשם הפרוטוקולים של האסיפות הכלליות` and `סעיף 90(ג) - על החברה לשלוח העתק מהמרשם לבעל מניה שביקש` |  |
| heading: חלק 3 פרק 2 סימן ט (sub-chapter I) | src:751 | inert | none | A pure title (a heading): "Sub-chapter I: defects in convening the meeting". |
| s 91(a) | src:753-754 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 91(א) - בית המשפט רשאי להורות על ביטול החלטה שהתקבלה באסיפה פגומה` |  |
| s 91(b) | src:755 | encoded | ic1-part3-ch2-gm-conduct.l4: `סעיף 91(ב) - בעל מניה רשאי לדרוש את ביטול ההחלטה` |  |
| heading: חלק 3 פרק 3 (Part 3 chapter 3) | src:757 | inert | none | A pure title (a heading): "Chapter 3: the board of directors". |
| heading: חלק 3 פרק 3 סימן א (sub-chapter A) | src:758 | inert | none | A pure title (a heading): "Sub-chapter A: the powers of the board". |
| s 92(a) | src:760-773 | encoded | ic1-part3-ch3-board.l4: `סעיף 92(א) - התפקיד או הסמכות הם של הדירקטוריון לפי סעיף 92(א)`, `סעיף 92(א)(12) - על הדירקטוריון לקבוע מספר מזערי של דירקטורים בעלי מומחיות חשבונאית ופיננסית`, `סעיף 92(א)(12) - המספר המזערי שקבע הדירקטוריון עומד במספר הדירקטורים שבתקנון` | Twelve functions and powers; the minimum number of expert directors in a public company or private bond company. |
| s 92(b) | src:774 | encoded | ic1-part3-ch3-board.l4: `סעיף 92(ב) - סמכות של הדירקטוריון לפי סעיף 92 ניתנת לאצילה למנהל הכללי` | Section 288(b)(2) is piece ic3's. |
| s 93(a) | src:776-777 | encoded | ic1-part3-ch3-board.l4: `סעיף 93(א) - בחברה פרטית שאינה חברת איגרות חוב יכול שיהיה דירקטוריון המונה אדם אחד` |  |
| s 93(b) | src:778 | encoded | ic1-part3-ch3-board.l4: `סעיף 93(ב) - ההוראות חלות על דירקטוריון המונה אדם אחד` |  |
| heading: חלק 3 פרק 3 סימן ב (sub-chapter B) | src:780 | inert | none | A pure title (a heading): "Sub-chapter B: the chair of the board". |
| s 94(a) | src:782-783 | encoded | ic1-part3-ch3-board.l4: `סעיף 94(א) - הדירקטוריון יבחר אחד מחבריו לכהן כיושב ראש` and the shared rule `חברה ציבורית או חברה פרטית שהיא חברת איגרות חוב` | The helper rule cites src:783. |
| s 94(b) | src:784 | encoded | ic1-part3-ch3-board.l4: `סעיף 94(ב) - אין חובה למנות יושב ראש דירקטוריון` and `סעיף 94(ב) - כל דירקטור זכאי לכנס את הדירקטוריון ולקבוע את סדר יומו` |  |
| s 95(a),(c),(d) | src:786-787 | fork | ic1-part3-ch3-board.l4: `סעיף 95(א) - המועמד רשאי לכהן כיושב ראש הדירקטוריון` | Subsections (c) and (d) are folded in (src:789-790). Fork F-ic1-17. |
| s 95(b) | src:788 | encoded | ic1-part3-ch3-board.l4: `סעיף 95(ב) - ניתן להקנות ליושב ראש או לקרובו סמכויות של המנהל הכללי`, `סעיף 95(ב) - ניתן להקנות ליושב ראש סמכויות הנתונות למי שכפוף למנהל הכללי`, `סעיף 95(ב) - יושב ראש הדירקטוריון רשאי לכהן בתפקיד אחר` | Three limbs. |
| s 95(c) | src:789 | encoded | ic1-part3-ch3-board.l4: `סעיף 95(א) - המועמד רשאי לכהן כיושב ראש הדירקטוריון` | The first three months after becoming public are exempt from (a). |
| s 95(d) | src:790 | encoded | ic1-part3-ch3-board.l4: `סעיף 95(א)`, `סעיף 95(ב)` (and the shared rule) | Applies to a private bond company, with section 121(d) in place of 121(c): the input `הכהונה מותרת לפי סעיף 121` is whichever applies. |
| s 96(a) | src:792-793 | encoded | ic1-part3-ch3-board.l4: `סעיף 96(א) - יושב ראש הדירקטוריון מנהל את הישיבה` |  |
| s 96(b) | src:794 | encoded | ic1-part3-ch3-board.l4: `סעיף 96(ב) - הדירקטוריון יבחר באחד מחבריו לנהל את הישיבה ולחתום על הפרוטוקול` and `סעיף 96(ב) - לדירקטור שנבחר לנהל את הישיבה יש קול נוסף בהצבעות הדירקטוריון` |  |
| heading: חלק 3 פרק 3 סימן ג (sub-chapter C) | src:796 | inert | none | A pure title (a heading): "Sub-chapter C: convening board meetings". |
| s 97 | src:798-799 | encoded | ic1-part3-ch3-board.l4: `סעיף 97 - הדירקטוריון התכנס בתדירות הנדרשת` |  |
| s 98(a) | src:801-802 | encoded | ic1-part3-ch3-board.l4: `סעיף 98(א) - יושב ראש הדירקטוריון רשאי לכנס את הדירקטוריון בכל עת` |  |
| s 98(b) | src:803-805 | encoded | ic1-part3-ch3-board.l4: `סעיף 98(ב) - הדירקטוריון יקיים ישיבה לדרישת דירקטורים` |  |
| s 98(c) | src:806 | encoded | ic1-part3-ch3-board.l4: `סעיף 98(ג) - יושב ראש הדירקטוריון יכנס את הדירקטוריון` |  |
| s 98(d) | src:807 | encoded | ic1-part3-ch3-board.l4: `סעיף 98(ד) - רשאי לכנס בעצמו ישיבת דירקטוריון שלא כונסה בזמן` | Fourteen days unless the articles fix another time. |
| heading: חלק 3 פרק 3 סימן ד (sub-chapter D) | src:809 | inert | none | A pure title (a heading): "Sub-chapter D: board meetings and how they are run". |
| s 99 | src:811-815 | encoded | ic1-part3-ch3-board.l4: `סעיף 99 - הנושא יכלל בסדר היום של ישיבת הדירקטוריון` |  |
| s 100(a) | src:817-818 | encoded | ic1-part3-ch3-board.l4: `סעיף 100(א) - הודעה על ישיבת דירקטוריון נמסרה במועד` |  |
| s 100(b) | src:819 | encoded | ic1-part3-ch3-board.l4: `סעיף 100(ב) - תוכן ההודעה על ישיבת דירקטוריון ומענה` |  |
| s 100(c) | src:820 | encoded | ic1-part3-ch3-board.l4: `סעיף 100(ג) - ניתן להתנות בתקנון על חובת הפירוט וחובת מסירת ההודעה במועד` |  |
| s 101 | src:822-823 | encoded | ic1-part3-ch3-board.l4: `סעיף 101 - הדירקטוריון רשאי לקיים ישיבה באמצעי תקשורת` |  |
| s 102 | src:825-826 | encoded | ic1-part3-ch3-board.l4: `סעיף 102 - הדירקטוריון רשאי להתכנס בלא הודעה בהסכמת כל הדירקטורים` and `סעיף 102 - הדירקטוריון רשאי להתכנס בלא הודעה במקרה דחוף בהסכמת רוב הדירקטורים` |  |
| s 103(a) | src:828-829 | encoded | ic1-part3-ch3-board.l4: `סעיף 103(א) - הדירקטוריון רשאי לקבל החלטות ללא התכנסות בפועל` |  |
| s 103(b) | src:830 | encoded | ic1-part3-ch3-board.l4: `סעיף 103(ב) - ייערך פרוטוקול ההחלטות וייחתם בידי יושב ראש הדירקטוריון` |  |
| s 103(c) | src:831 | encoded | ic1-part3-ch3-board.l4: `סעיף 103(ג) - על החלטה ללא התכנסות חלות הוראות סעיף 108` |  |
| s 103(d) | src:832 | encoded | ic1-part3-ch3-board.l4: `סעיף 103(ד) - יושב ראש הדירקטוריון אחראי לביצוע הוראות סעיף 103` |  |
| s 104 | src:834-835 | encoded | ic1-part3-ch3-board.l4: `סעיף 104 - נכח מנין חוקי לפתיחת ישיבת דירקטוריון` |  |
| heading: חלק 3 פרק 3 סימן ה (sub-chapter E) | src:837 | inert | none | A pure title (a heading): "Sub-chapter E: voting in the board". |
| s 105 | src:839-840 | encoded | ic1-part3-ch3-board.l4: `סעיף 105 - מספר הקולות של דירקטור בהצבעה בדירקטוריון` |  |
| s 106(a) | src:842-843 | encoded | ic1-part3-ch3-board.l4: `סעיף 106(א) - הדירקטור הפר חובת אמונים` |  |
| s 106(b) | src:844 | encoded | ic1-part3-ch3-board.l4: `סעיף 106(ב) - האדם הפר את איסור מילוי תפקיד דירקטור שלא כדין או הפגיעה בשיקול דעת עצמאי` |  |
| s 106(c) | src:845 | encoded | ic1-part3-ch3-board.l4: `סעיף 106(ג) - על המפר חלים החובות והאחריות החלות על דירקטורים` |  |
| s 107 | src:847-848 | fork | ic1-part3-ch3-board.l4: `סעיף 107 - החלטת הדירקטוריון התקבלה` | Ordinary majority (fork F-ic1-6); a tie goes to the chair's additional vote. |
| heading: חלק 3 פרק 3 סימן ו (sub-chapter F) | src:850 | inert | none | A pure title (a heading): "Sub-chapter F: minutes of board meetings". |
| s 108(a) | src:852-853 | encoded | ic1-part3-ch3-board.l4: `סעיף 108(א) - החברה תערוך פרוטוקולים של ההליכים בישיבות הדירקטוריון`, `סעיף 108(א) - הפרוטוקולים נשמרים במקום הנדרש`, `סעיף 108(א) - על החברה לשמור את פרוטוקולי הדירקטוריון` |  |
| s 108(b) | src:854 | encoded | ic1-part3-ch3-board.l4: `סעיף 108(ב) - פרוטוקול שאושר ונחתם ראיה לכאורה לאמור בו` |  |
| heading: חלק 3 פרק 3 סימן ז (sub-chapter G) | src:856 | inert | none | A pure title (a heading): "Sub-chapter G: defects in convening a board meeting". |
| s 109(a)(1) | src:858-860 | encoded | ic1-part3-ch3-board.l4: `סעיף 109(א)(1) - דירקטור שנכח בישיבה רשאי לדרוש ביטול ההחלטה` |  |
| s 109(a)(2) | src:861 | encoded | ic1-part3-ch3-board.l4: `סעיף 109(א)(2) - דירקטור שהיה זכאי להיות מוזמן ולא נכח רשאי לדרוש ביטול ההחלטה` |  |
| s 109(a)(3) | src:862 | encoded | ic1-part3-ch3-board.l4: `סעיף 109(א)(3) - דירקטור רשאי לדרוש את ביטול ההחלטות` |  |
| s 109(b) | src:863 | encoded | ic1-part3-ch3-board.l4: `סעיף 109(ב) - תוקפה של פעולה שנעשתה עבור החברה לא נפגע` | Section 56(a) last part: the innocent party. |
| heading: חלק 3 פרק 3 סימן ח (sub-chapter H) | src:865 | inert | none | A pure title (a heading): "Sub-chapter H: committees of the board". |
| s 110(a) | src:867-868 | encoded | ic1-part3-ch3-committees.l4: `סעיף 110(א) - הדירקטוריון רשאי להקים ועדות דירקטוריון` |  |
| s 110(b) | src:869 | encoded | ic1-part3-ch3-committees.l4: `סעיף 110(ב) - האדם רשאי לכהן בוועדה שהואצלו לה סמכויות הדירקטוריון` |  |
| s 110(c) | src:870 | encoded | ic1-part3-ch3-committees.l4: `סעיף 110(ג) - האדם רשאי לכהן בוועדה שתפקידה לייעץ או להמליץ בלבד` |  |
| s 111(a) | src:872-873 | encoded | ic1-part3-ch3-committees.l4: `סעיף 111(א) - החלטה או פעולה של ועדה כמוה כהחלטה או פעולה של הדירקטוריון` |  |
| s 111(b) | src:874 | encoded | ic1-part3-ch3-committees.l4: `סעיף 111(ב) - ועדת דירקטוריון תדווח לדירקטוריון באורח שוטף` and `סעיף 111(ב) - החלטות והמלצות של הוועדה הובאו לידיעת הדירקטורים זמן סביר לפני הדיון` |  |
| s 111(c) | src:875 | encoded | ic1-part3-ch3-committees.l4: `סעיף 111(ג) - על כינוס ישיבות הוועדות ואופן ניהולן חלים סימנים ב׳ עד ז׳` |  |
| s 111(d) | src:876 | encoded | ic1-part3-ch3-committees.l4: `סעיף 111(ד) - פרוטוקולים של ועדות הדירקטוריון ייערכו וייישמרו כאמור בסעיף 108` |  |
| s 112(a) | src:878-886 | encoded | ic1-part3-ch3-committees.l4: `סעיף 112(א) - הדירקטוריון רשאי להאציל לועדה את הסמכות בנושא` | Seven matters that cannot be delegated, with the exceptions of items (2) and (5). |
| s 112(b) | src:887 | encoded | ic1-part3-ch3-committees.l4: `סעיף 112(ב) - חברה רשאית להתנות בתקנונה על הוראות סעיף קטן (א)` and `סעיף 112(ב) - חברה רשאית לקבוע בתקנונה נושאים נוספים שבהם יתקבלו החלטות בידי הדירקטוריון בלבד` |  |
| s 112(c) | src:888 | encoded | ic1-part3-ch3-committees.l4: `סעיף 112(ג) - הדירקטוריון רשאי להקים ועדות בנושאים המנויים בסעיף 112(א) לשם המלצה בלבד` |  |
| s 113 | src:890-891 | encoded | ic1-part3-ch3-committees.l4: `סעיף 113 - הדירקטוריון רשאי לבטל החלטה של ועדה שמונתה על ידיו` and `סעיף 113 - ביטול החלטת הוועדה אינו פוגע בתוקפה כלפי אדם שלא ידע על הביטול` |  |
| heading: חלק 3 פרק 3 סימן ט (sub-chapter I) | src:893 | inert | none | A pure title (a heading): "Sub-chapter I: the audit committee". |
| s 114 | src:895-896 | encoded | ic1-part3-ch3-committees.l4: `סעיף 114 - הדירקטוריון חייב למנות מבין חבריו ועדת ביקורת` |  |
| s 115(a) | src:898-899 | encoded | ic1-part3-ch3-committees.l4: `סעיף 115(א) - הרכב ועדת הביקורת` |  |
| s 115(b)(1) | src:900 | encoded | ic1-part3-ch3-committees.l4: `סעיף 115(ב)(1) - האדם אינו רשאי להיות חבר בוועדת ביקורת` |  |
| s 115(b)(2) | src:901 | encoded | ic1-part3-ch3-committees.l4: `סעיף 115(ב)(2) - הוראות פסקה (1) אינן חלות על עובד המדינה בחברה ממשלתית` |  |
| s 115(c) | src:902 | encoded | ic1-part3-ch3-committees.l4: `סעיף 115(ג) - האדם רשאי להיות חבר בוועדת ביקורת` |  |
| s 115(d) | src:903 | encoded | ic1-part3-ch3-committees.l4: `סעיף 115(ד) - האדם רשאי לכהן כיושב ראש ועדת הביקורת` |  |
| s 115(e) | src:904-906 | fork | ic1-part3-ch3-committees.l4: `סעיף 115(ה) - מי שאינו רשאי להיות חבר רשאי להיות נוכח בישיבה` | Fork F-ic1-18. |
| s 115(f) | src:907 | encoded | ic1-part3-ch3-committees.l4: `סעיף 115(ו) - בדיון בדוחות הכספיים חלות הוראות סעיף 171(ה)` |  |
| s 116(a) | src:909-910 | encoded | ic1-part3-ch3-committees.l4: `סעיף 116(א) - המבקר הפנימי מקבל הודעות על ישיבות ועדת הביקורת ורשאי להשתתף בהן` |  |
| s 116(b) | src:911 | encoded | ic1-part3-ch3-committees.l4: `סעיף 116(ב) - המבקר הפנימי רשאי לבקש מיושב ראש ועדת הביקורת לכנס את הוועדה` and `סעיף 116(ב) - יושב ראש ועדת הביקורת יכנס את הוועדה בתוך זמן סביר` |  |
| s 116(c) | src:912 | encoded | ic1-part3-ch3-committees.l4: `סעיף 116(ג) - הודעה על הישיבה תומצא לרואה החשבון המבקר והוא רשאי להשתתף בה` |  |
| s 116א | src:914-915 | encoded | ic1-part3-ch3-committees.l4: `סעיף 116א - נכח מנין חוקי בוועדת הביקורת` |  |
| s 117 | src:917-927 | encoded | ic1-part3-ch3-committees.l4: `סעיף 117 - התפקיד הוא מתפקידי ועדת הביקורת`, `סעיף 117(1) - הוועדה קיימה ישיבה בענין ליקוי מהותי כנדרש`, `סעיף 117(2א) - עסקה שאינה זניחה` | Nine functions; the material-defect meeting of paragraph (1); the definition of paragraph (2a). The sections cited in the paragraphs (255, 270, 149, 155, 165, 171) are other pieces'. |
| s 118(a) | src:929-930 | encoded | ic1-part3-ch3-committees.l4: `סעיף 118(א) - הדירקטוריון רשאי למנות ועדת ביקורת בחברה פרטית שאינה חברת איגרות חוב`, `סעיף 118(א) - דירקטור רשאי לכהן בוועדת ביקורת בחברה פרטית שאינה חברת איגרות חוב`, `סעיף 118(א) - האדם רשאי לכהן כיושב ראש ועדת ביקורת בחברה פרטית שאינה חברת איגרות חוב` |  |
| s 118(b) | src:931 | encoded | ic1-part3-ch3-committees.l4: `סעיף 118(ב) - ניתן למנות את הוועדה בחברה פרטית שאינה חברת איגרות חוב` |  |
| heading: חלק 3 פרק 3 סימן י (sub-chapter J) | src:933 | inert | none | A pure title (a heading): "Sub-chapter J: the compensation committee". |
| s 118א(a) | src:935-936 | encoded | ic1-part3-ch3-committees.l4: `סעיף 118א(א) - הדירקטוריון חייב למנות מבין חבריו ועדת תגמול` |  |
| s 118א(b) | src:937 | encoded | ic1-part3-ch3-committees.l4: `סעיף 118א(ב) - הרכב ועדת התגמול` | Section 244 and the Government Companies Law are out of range. |
| s 118א(c) | src:938 | encoded | ic1-part3-ch3-committees.l4: `סעיף 118א(ג) - על ועדת תגמול חלים סימן ח׳ וסעיף 115(ב) עד (ה)` |  |
| s 118א(d) | src:939 | encoded | ic1-part3-ch3-committees.l4: `סעיף 118א(ד) - ועדת ביקורת יכולה לשמש גם ועדת תגמול` |  |
| s 118ב | src:941-946 | encoded | ic1-part3-ch3-committees.l4: `סעיף 118ב - התפקיד הוא מתפקידי ועדת התגמול` | Four functions. |

## Fork register
Every place where the text does not settle the reading, the readings seen, the one taken and the text that licenses it.
I looked for ambiguity in every cumulative-or-alternative list ("or" between negations, "and while"), every time limit (from what event, and whether the last day is inside), every threshold (more than, at least), every cross-reference to a provision of another piece, every deeming sentence, and every place where the articles may vary a rule.
The register has 20 entries.
**F-ic1-1. The three bars in section 2 (src:268).**
Text: "ובלבד שמטרה ממטרות החברה אינה נוגדת את החוק, אינה בלתי מוסרית או אינה נוגדת את תקנת הציבור" (provided that a purpose of the company is not contrary to the law, is not immoral, or is not contrary to public policy).
Readings: (a) none of the three bars applies to any purpose (the founder may found only if every purpose is clear of all three); (b) a literal "or" between three negations: it is enough that one of the three negations holds.
Taken: (a). A list of negations closed by "or" is the ordinary Hebrew way to say "neither X, nor Y, nor Z"; reading (b) would let a founder with an unlawful purpose found a company whenever the purpose was not immoral.
Effect: the rule is `NOT (A OR B OR C)`; a purpose that breaches any one bar defeats the privilege (tested for each bar). Also open: "a purpose" is read as any one of the company's purposes ("מטרה ממטרות"), so one bad purpose among several bars the founding.

**F-ic1-2. The last day of existence in section 5 (src:279).**
Text: "מיום ההתאגדות המצוין בתעודת ההתאגדות ועד לפקיעת ההתאגדות" (from the day of incorporation stated in the certificate until the lapse of incorporation).
Readings: (a) the day on which incorporation lapses is a day on which the company still exists; (b) existence ends the day before.
Taken: (a), for day-granularity: the company existed during part of that day. The first day counts ("מיום").
Effect: `סעיף 5 - החברה קיימת ביום` is TRUE on the lapse day and FALSE the day after (tested).

**F-ic1-3. "In view of his holdings and the fulfilment of his duties" in section 6(a)(1) (src:285).**
Text: "ובשים לב לאחזקותיו ולמילוי חובותיו כלפי החברה לפי סעיפים 192 ו־193 ובשים לב ליכולת החברה לפרוע את חובותיה".
Readings: (a) a further condition: the court may attribute only if these were weighed or are satisfied in a stated way; (b) a direction on how the court is to form its finding that attribution is "just and right" (the finding is already an input).
Taken: (b). The words "בשים לב" (having regard to) tell the court what to weigh; they are not facts the shareholder can state. Sections 192 and 193 (duties of a shareholder) belong to piece ic2.
Effect: the rule does not read them, so the seat layer does not ask them; a reader who takes (a) adds one conjunct.

**F-ic1-4. Time limits in section 13(a) (src:331-333).**
Text: "בתוך שנה מיום עשייתה", "שלושים ימים מראש", "בתוך שלושים ימים מיום שדרש".
Readings for the last day: (a) the last day of the period is inside it, so approval on day 30 is in time and the option arises only after day 30; (b) the option arises on day 30.
Taken: (a) for "within" (limbs (1) and (3): the option arises when the count is GREATER THAN 12 months or 30 days); "thirty days in advance" (limb (2)) is read as at least thirty days' notice (the count AT LEAST 30).
A year is counted as 12 months elapsed since the day the act was done; the caller counts whole months.
Effect: 12 months and 30 days are still in time; 13 months and 31 days are not (tested at both edges).

**F-ic1-5. Limb (b) of section 6(a)(1) (src:284).**
Text: "באופן הפוגע בתכלית החברה ותוך נטילת סיכון בלתי סביר באשר ליכולתה לפרוע את חובותיה" (in a manner that harms the purpose of the company and while taking an unreasonable risk as to its ability to pay its debts).
Readings: (a) harm to the purpose AND an unreasonable risk (cumulative); (b) either.
Taken: (a). "ותוך" (and while) joins one manner of use, not two alternatives; the alternatives are limbs (a) and (b), separated by the sentence break and the end of the list with a closing comma.
Effect: harm to the purpose without an unreasonable risk does not satisfy limb (b) (tested).

**F-ic1-6. "Ordinary majority" (sections 20(a), 85 and 107; src:370, 706, 848).**
Text: "רוב רגיל" appears in sections 20(a), 85 and 107 and is not defined in section 1 (the keel notes say so, instruction 13).
Readings: (a) more votes for than against in the count of votes of section 84 (abstentions set aside, core fork F2); a tie fails; (b) more than half of all the voting rights present, abstentions counted against; (c) more than half of the voting rights of the company.
Taken: (a). Section 84 (src:703) fixes the count as the count of votes "מנין קולות", which the core reads as votes for plus votes against.
Effect: `רוב רגיל בהצבעה` is `קולות בעד GREATER THAN קולות נגד`; a tie is not a majority (tested).

**F-ic1-7. "The proposed majority" in section 20(b) (src:371).**
Text: "באותו רוב מסוים או ברוב המוצע, לפי הגבוה מבין השניים" (by that certain majority or by the proposed majority, whichever is higher).
Readings: (a) the proposed majority is the majority that the resolution itself proposes to require, for the provision, from then on; (b) the majority by which the resolution is proposed to be adopted; (c) a majority proposed in the articles.
Taken: (a). The sentence is about amending a provision that the Law lets be stipulated otherwise or that the articles entrench; the only majority "proposed" in an amending resolution is one that it proposes to set for the provision.
Effect: the rule takes both figures as inputs and requires votes for as a share of the count of votes at least the higher; a resolution that proposes none passes 0. A reader of (b) would need a different input; NOTES.md asks a domain expert.

**F-ic1-8. The consent exception in section 27(a)(2) (src:406).**
Text: "...או שם הדומה לו עד כדי להטעות, אלא אם כן הוכח לרשם כי בעל סימן המסחר הסכים לכך בכתב".
Readings: (a) the exception applies to the whole paragraph (the registered mark and a name similar to it); (b) only to the similar name.
Taken: (a). The "unless" follows the whole sentence and the consent is the mark owner's, which is the same for both limbs.
Effect: a name identical to a registered mark is registrable if the owner consented in writing (tested).

**F-ic1-9. "Its feelings" in section 28 (src:410).**
Text: "עלול לפגוע בתקנת הציבור או ברגשותיו" (liable to harm public policy or its/his feelings).
Readings: (a) the feelings of the public; (b) the feelings of the Registrar.
Taken: (a). The pronoun follows "הציבור", the last noun.
Effect: the rule has two inputs, one for each limb; both are the Registrar's opinions.

**F-ic1-10. "Their number only" in section 34(b) (src:440).**
Text: "היו מניות החברה ללא ערך נקוב יצויין בתקנון מספרן בלבד".
Readings: (a) "only" excludes a par value: stating a par value for no-par shares fails the section; (b) "only" says the number is the one mandatory item.
Taken: (a). The words contrast with the next clause, which requires the par value "in addition".
Effect: `סעיף 34(ב)` is FALSE for no-par shares when the articles state a par value (tested).

**F-ic1-11. "Who has reason to fear harm to his rights" in section 55(b) (src:561).**
Text: "לבקשת החברה, בעל מניה, או נושה של החברה שיש חשש לפגיעה בזכויותיו" (at the request of the company, a shareholder, or a creditor of the company with reason to fear harm to his rights).
Readings: (a) the clause qualifies the creditor only; (b) it qualifies all three applicants.
Taken: (a). The clause follows the last noun and the singular "זכויותיו" fits one applicant; a shareholder and the company are named without a condition.
Effect: a shareholder or the company may apply without showing a fear of harm; a creditor may apply only with one (tested). A reader of (b) adds one conjunct for the company and the shareholder.

**F-ic1-12. "Every year, and no later than the end of fifteen months" in section 60(a) (src:592).**
Text: "חברה תקיים אסיפה שנתית בכל שנה ולא יאוחר מתום חמישה עשר חודשים לאחר האסיפה השנתית האחרונה".
Readings: (a) the fifteen months are the measurable bound: one meeting in every period of up to fifteen months; (b) two cumulative duties: one meeting in every calendar year, and no gap above fifteen months (a meeting in December of one year and March of the year after next breaks the first although it keeps the second).
Taken: (a). "Every year" is the rule and the fifteen months the outer limit that the Law itself measures; a calendar-year count is not stated.
Effect: `סעיף 60(א)` is `months AT MOST 15` (tested at 15 and 16); the calendar-year reading would add a conjunct.

**F-ic1-13. The holdings of "one or more shareholders" in section 63 (src:606, 609).**
Text: "בעל מניה, אחד או יותר, שלו לפחות עשרה אחוזים ..." (one or more shareholders, who has at least ten percent ...).
Readings: (a) the holdings of all the demanding shareholders are added together; (b) each demander must hold the fraction alone.
Taken: (a). "אחד או יותר" (one or more) in the singular "שלו" treats the group as one shareholder for the count.
Effect: the inputs `חלקם של הדורשים בהון המונפק` and `חלקם של הדורשים בזכויות ההצבעה` are the combined shares of those who demand; the thresholds are AT LEAST (tested at 10, 5 and 1 percent and just below).

**F-ic1-14. "Two shareholders who have twenty-five percent" in section 78(a) (src:674).**
Text: "המנין החוקי לקיום אסיפה כללית הוא נוכחות של לפחות שני בעלי מניות שלהם עשרים וחמישה אחוזים לפחות מזכויות ההצבעה, תוך מחצית השעה מן המועד שנקבע לפתיחת האסיפה".
Readings: (a) at least two shareholders are present and together they hold at least 25 percent of the voting rights; the quorum must be reached within half an hour of the set time (30 minutes are inside); (b) each of the two holds 25 percent.
Taken: (a). "שלהם" (whose, plural) refers to the shareholders together.
Effect: the inputs are the number present, their combined share and the minutes until the quorum; one shareholder with 90 percent is not a quorum, two with 24.9 percent are not (tested).

**F-ic1-15. "The number needed to convene a meeting under section 63" in section 79(b) (src:680).**
Text: "תתקיים האסיפה הנדחית רק אם נכחו בה לפחות בעלי מניות במספר הדרוש לצורך כינוס אסיפה כאמור בסעיף 63".
Readings: (a) the shareholders' route of section 63 only (10 percent / 1 percent, or 10 percent of the votes for a private company; 5 percent / 1 percent, or 5 percent for a public one); (b) the directors' route as well.
Taken: (a). The subsection speaks of shareholders ("בעלי מניות") present.
Effect: the rule tests the combined shares of the shareholders present against the section 63 thresholds for the kind of company (tested).

**F-ic1-16. A shareholder who voted in more than one way, section 83(d) (src:700).**
Text: "הצביע בעל מניה ביותר מדרך אחת, תימנה הצבעתו המאוחרת; לעניין זה, הצבעה של בעל מניה בעצמו או באמצעות שלוח תיחשב מאוחרת להצבעה באמצעות כתב הצבעה".
Readings: for two ways that are not (a deed and one of the others), (a) the later in fact counts; (b) a vote in person always outranks a vote by proxy.
Taken: (a). The deeming sentence orders only the deed against the other two.
Effect: a vote in person and a vote by proxy are ordered by time; a vote by deed never outranks one of the others (tested).

**F-ic1-17. A director in a controlled corporation as chair, section 95(a) (src:787).**
Text: "לא יכהן כיושב ראש הדירקטוריון בחברה ציבורית מי שכפוף למנהל הכללי, במישרין או בעקיפין; דירקטור בתאגיד בשליטת חברה ציבורית רשאי לכהן כיושב ראש הדירקטוריון בחברה הציבורית".
Readings: (a) the second clause says that being a director of a corporation the public company controls does not by itself make a person "subordinate to the general manager", so it removes the bar only for a person subordinate by that status alone; (b) it is a stand-alone permission that overrides the bar even for a person who is subordinate in some other way.
Taken: (a). Reading (b) would let the second clause cancel the first for anyone who also sits on a subsidiary's board.
Effect: the rule has an input `כפיפותו למנהל הכללי נובעת רק מכהונתו כדירקטור בתאגיד בשליטת החברה`; with it TRUE the subordination bar does not apply (tested).

**F-ic1-18. "Needed to present a particular matter" in section 115(e) (src:904).**
Text: "מי שאינו רשאי להיות חבר בוועדת ביקורת לא יהיה נוכח בישיבות הוועדה בעת הדיון ובעת קבלת ההחלטות, אלא אם כן קבע יושב ראש הוועדה כי הוא נדרש לשם הצגת נושא מסוים".
Readings: (a) the chair's determination lets the person be present at the discussion and at the decision; (b) only at the discussion.
Taken: (a). The sentence names both stages in its prohibition and gives one exception; paragraphs (1) and (2) then give the narrower exceptions (discussion only for an employee; both for the legal adviser and the secretary).
Effect: the chair's determination admits the person at either stage (tested); the employee exception admits him at the discussion only (tested).

**F-ic1-19. A section 22 resolution and the ordinary route of section 20(a) (src:370, 379-381).**
Text: section 20(a) lets a company amend its articles by an ordinary majority "unless ... a resolution as in section 22 was adopted"; section 22(a) lets a company restrict its power to amend "the articles or a provision of them".
Readings: (a) a section 22 resolution closes the ordinary route only for the provision (or provisions) it restricts, so other provisions may still be amended by an ordinary majority; (b) any section 22 resolution closes the ordinary route for every amendment of the articles.
Taken: (a). The restriction of section 22(a) may be of one provision, and subsection (b) of section 20 then gives the majority for that provision.
Effect: the input of `סעיף 20(א)` is named `נתקבלה החלטה כאמור בסעיף 22 המגבילה את שינוי ההוראה הנדונה` (a section 22 resolution restricts amendment of the provision at issue); a section 22 resolution that concerns another provision is answered FALSE and does not close the route (tested by the input being FALSE).

**F-ic1-20. "All the organs of the company" in section 48(d) (src:529).**
Text: "לכל האורגנים בחברה נתונות כל סמכויות העזר הדרושות להפעלת סמכויותיהם" (all the organs of the company hold all the ancillary powers needed to exercise their powers).
Readings: (a) every organ of section 46, which includes any body whose act law or the articles treat as the company's act in a matter (the third limb of section 46); (b) only the three principal organs of section 48(a) to (c).
Taken: (a). Section 46 defines "the organs of the company" and section 48(d) says "all" of them.
Effect: `סעיף 48(ד)` calls `סעיף 46` with the same facts; an audit committee that the articles treat as an organ for a matter holds the ancillary powers, and one that is not so treated does not (tested, and in the seat cases).

## Cross-references out of my ranges
Each reference to a provision of another piece, or of another law, is taken as a plain input named for the fact, with a comment `-- out of range: section N (piece X)` above the rule in the module.
There are 33 rows; 26 of them depend on a provision of another piece (rows naming ic2: 12, ic3: 8, ic4: 5, ic5: 2, ic6: 3; a row may name more than one piece) and the rest on another law or on the core.
The ones that matter most to a merged encoding are section 377 (when the Law commenced, for section 24), sections 121, 122(d), 169, 177(1), 219 and 239 to 249ג (piece ic2) which decide who may chair the board, when the board must meet and who counts as an external or independent director, and sections 257, 288(b) and 304 (piece ic3).
| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |

| s 5 | Part 8A, dissolution (the incorporation lapses "as a result of the liquidation of the company") | ic4 | `תאריך פקיעת ההתאגדות` (MAYBE DATE) |
| s 6(a)(1) | ss 192 and 193 (a shareholder's duties to the company), which the court takes into account | ic2 | none: the court's finding `בית המשפט מצא שבנסיבות הענין צודק ונכון...` carries it (fork F-ic1-3) |
| s 11(a),(b) | Part 9 chapter 1A, the public-benefit company (s 345א onwards) | ic5 | core field `חברה לתועלת הציבור`; the donation rule answers NOTHING for such a company |
| s 24(1) to (5) | s 377 (the commencement of the Law) | ic6 | `החברה התאגדה לפני תחילתו של חוק זה` |
| s 24(1) | the Companies Ordinance [New Version], 5743-1983, as it read on the eve of commencement (another law) | none | `השינוי נעשה בדרך ובתנאים שבפקודת החברות כנוסחה ערב תחילת החוק` |
| s 24(2) | s 350 | ic6 | `השינוי או הביטול נעשה בדרך הקבועה לפי סעיף 350` |
| s 27(a)(2) | the Trade Marks Ordinance [New Version], 5732-1972 (another law) | none | `השם הוא סימן מסחר רשום או דומה לו עד כדי להטעות`; `הסימן רשום לגבי טובין או שירותים ...` |
| s 35(b) | s 304 | ic3 | `מתקיים האמור בסעיף 304` |
| s 39(b) | Part 8A (liquidation) and the Insolvency and Economic Rehabilitation Law (another law) | ic4 | `החברה בכינוס נכסים`; `החברה בפירוק`; `ניתן לגבי החברה צו לפתיחת הליכים` |
| s 40(3) | s 345ב(ג) (an amendment that makes a company a public-benefit company) | ic5 | enumeration constructor `שינוי תקנון שהופך את החברה לחברה לתועלת הציבור`; `הפעולה נרשמה` |
| s 41(b) | the Computers Law, 5755-1995 (another law), for "printout" | none | `המסמך הוא פלט של דיווח אלקטרוני` |
| s 43(b) | the Fourth Schedule, item (2) | ic6 | `הפרט הוא פרט (2) לתוספת הרביעית` |
| s 48(c) | Part 3 chapter 4, the general manager's powers | ic2 | `הסמכות מפורטת בסימן או בפרק שהחוק מייחד לאורגן` |
| s 50(b) | Part 6 chapters 3 to 5 (rights and duties of directors, which apply to shareholders who take the board's powers) | ic3 | none: the rule says only that they apply |
| s 57 | ss 154 to 167, 239 (ic2); 255, 268 to 275, 286, 287 (ic3); 320, 342ו, 342כד, 342מב (ic4): the matters the section lists | ic2, ic3, ic4 | enumeration constructors of `ענין שסעיף 57 מחייב לקבל בו החלטה באסיפה הכללית` |
| s 71; s 88(d) | the Securities Law (a bourse member), another law | none | `המניה מוחזקת באמצעות חבר בורסה`; `המניות מוחזקות באמצעות חבר בורסה` |
| s 82(b) | another enactment on voting rights (for example the Securities Law) | none | `זכויות ההצבעה שנקבעו בתקנון עומדות בהוראת חיקוק אחר` |
| s 87(a) | ss 255 and 268 to 275 (ic3); s 320 (ic4); s 121(c) (ic2); the Minister's s 89 (in range, inert) | ic2, ic3, ic4 | enumeration constructors of `ענין שאפשר להצביע בו בכתב הצבעה בחברה ציבורית` |
| s 87(e); s 88(d) | s 177(1) | ic2 | `בעל המניה הוא בעל מניה כאמור בסעיף 177(1)` |
| s 92(a)(12) | s 219 (the number of directors in the articles) | ic2 | `מספר הדירקטורים שנקבע בתקנון לפי סעיף 219` |
| s 92(b) | s 288(b)(2) | ic3 | `האצילה היא כמפורט בסעיף 288(ב)(2)` |
| s 95(a) | s 121(c) and (d) | ic2 | `הכהונה מותרת לפי סעיף 121` |
| s 95(b) | s 121 | ic2 | `ההקניה מותרת לפי סעיף 121` |
| s 98(b) | s 257 | ic3 | `התקיים האמור בסעיף 257` |
| s 98(c) | s 122(d); s 169 | ic2 | `התקיים האמור בסעיף 122(ד) בשל הודעה או דיווח של המנהל הכללי`; `התקבלה הודעת רואה החשבון המבקר לפי סעיף 169` |
| s 112(a)(5) | s 288(b) | ic3 | `ההנפקה או ההקצאה היא כמפורט בסעיף 288(ב)` |
| s 112(a)(3) | s 329 (the board's position or opinion on a matter for the general meeting) | ic4 | enumeration constructor of `נושא שהדירקטוריון אינו רשאי להאציל לועדה` |
| s 115(a), (b)(1), (d); s 116A; s 118A(b) | Part 6 chapter 1 sub-chapter E, ss 239 to 249ג (external and independent directors) | ic2 | counts and yes/no facts: `מספר חברי הוועדה שהם דירקטורים בלתי תלויים`, `האדם הוא דירקטור חיצוני`, ... |
| s 115(b)(1), (c), (e); s 118(a), (b); s 118A | section 1 definitions: controlling shareholder, relative, material shareholder (the core) | core | yes/no facts: `האדם הוא בעל השליטה או קרובו`, `מספר חברי הוועדה שהם או קרוביהם בעלי מניות מהותיים`, ... |
| s 115(b)(2) | the Government Companies Law, 5735-1975 (another law): the Minister responsible for the company | none | `השר האחראי לענייני החברה הוא השר האחראי על המשרד שבו מועסק עובד המדינה` |
| s 115(f) | s 171(e) | ic2 | `הוועדה משמשת כוועדה לבחינת הדוחות הכספיים לפי סעיף 171(ה)` |
| s 117(2א) | s 270(4) and (4A) | ic3 | `העסקה היא עסקה כאמור בסעיף 270(4) רישה או (4א) רישה` |
| s 118A(b) | s 244; section 19 of the Government Companies Law (another law) | ic2 | `תנאי כהונתם והעסקתם של שאר החברים הם בהתאם להוראות שנקבעו לפי סעיף 244 או לפי סעיף 19 לחוק החברות הממשלתיות` |

## Needs from the core
Nothing in the core was edited. These are what ic1 defined locally under specific names, for the lead to promote or leave.
1. **A majority helper.** Section 1 does not define "רוב רגיל" (an ordinary majority), and sections 20(a), 85 and 107 use it; sections 20(b), 22(a), 24, 56(b) and 85 also need "a share of those voting, abstainers set aside". Three rules in `ic1-majorities.l4` do this arithmetic: `רוב רגיל בהצבעה`, `שיעור הקולות בעד מקולות המשתתפים בהצבעה למעט הנמנעים`, `ההצבעה קיבלה את הרוב הנדרש`. Pieces ic2, ic3 and ic4 need the same arithmetic for their approvals and cannot import ic1, so the lead should promote them to the core (fork F-ic1-6 says what an ordinary majority is taken to be).
2. **A shared kind of company.** `חברה ציבורית או חברה פרטית שהיא חברת איגרות חוב` (in `ic1-part3-ch3-board.l4`) is the pair of companies on which sections 94 to 102, 114, 118 and 118A turn; pieces after ic1 will meet the same pair ("a public company or a bond company").
3. **Local enumerations**, each declared where it is used and named for the matter it lists: `ענין שחברה רשאית להביא בחשבון בשיקוליה העסקיים`; `נושא שחברה רשאית לכלול בתקנון`; `הוראה בתזכיר של חברה שהתאגדה לפני תחילת החוק`; `אופן ציון מטרות החברה בתקנון`; `ענין שהרשם קובע בו אם נתמלאו התנאים והדרישות`; `פעולה של חברה שתוקפה מותנה ברישום`; `החריגה שהחברה מאשרת בדיעבד`; `דרך הצבעה של בעל מניה באסיפה כללית`; `ענין שאפשר להצביע בו בכתב הצבעה בחברה ציבורית`; `ענין שסעיף 57 מחייב לקבל בו החלטה באסיפה הכללית`; `נושא שיכול להיכלל בסדר היום של אסיפה שנתית`; `תפקיד או סמכות של הדירקטוריון לפי סעיף 92(א)`; `חלק בפרק הדירקטוריון`; `נושא שהדירקטוריון אינו רשאי להאציל לועדה`; `שלב בישיבת ועדת הביקורת`; `תפקיד של ועדת הביקורת`; `תפקיד של ועדת התגמול`. They are matter lists the Law names (an organ's function, a kind of vote, an item the Registrar decides); a core `צד`-style promotion is not needed unless another piece lists the same matters.
4. **Terms of section 1 asked as facts.** The core has `קרוב`, `בעל מניה מהותי` and `דירקטור בלתי תלוי`, but no rule for "בעל שליטה" (a controlling shareholder), and the rules it has need more facts than the committee rules of ss 115 and 118 can ask a person. ic1 therefore takes "the controlling shareholder or his relative", "an external director" and "an independent director" as plain yes/no facts or counts. If the lead adds a core rule for "בעל שליטה" and for the external director of Part 6 chapter 1 sub-chapter E, sections 94 to 118A can call them.

## What the text turns out to say
Numbered findings. Each ends "Asserted." where a test in an `ic1-tests-*.l4` file or a case in `ic1-cases-seat.l4` asserts it; every expected value was written from the text before the run.

1. Section 2: a founder is barred by any one of the three bars (unlawful, immoral, against public policy), and one bad purpose among several is enough to bar the founding (fork F-ic1-1). Asserted.
2. Section 3 says a company may have one shareholder and says nothing about a company with none; that case is answered NOTHING, not FALSE. Asserted.
3. Section 5: a company exists from the day of incorporation the certificate states until the incorporation lapses, both days included (fork F-ic1-2); a document the Registrar has not signed is no certificate of incorporation. Asserted.
4. Section 6(a)(1): harm to the purpose and an unreasonable risk are cumulative in limb (b) (fork F-ic1-5), and suspicion plus a refusal to check counts as awareness unless the shareholder was merely negligent (6(a)(2)). Asserted.
5. Section 7(a) allows a restriction order of up to five years, and 7(c) makes the person who breaches it liable only for the debts of the company concerned that arose in the restriction period. Asserted.
6. Section 9(c): "company" for the annual fee includes a foreign company, which is a body corporate incorporated abroad that is not a partnership. Asserted.
7. Section 11(b): the donation rule of 11(a) does not apply to a public-benefit company; the encoding answers NOTHING for it, because that chapter is in piece ic5. Asserted.
8. Section 13(a): twelve months and thirty days are still in time; the option arises at thirteen months, thirty-one days after a demand, and thirty days after the promoter was notified that the company will not incorporate (fork F-ic1-4); 13(c) lets the parties contract out, so the Law does not then decide (NOTHING). Asserted.
9. Section 14(2): once the company approves a promoter's act, it binds both the company and the promoter jointly and severally and entitles only the company. Asserted.
10. Sections 20(a), 85 and 107: "ordinary majority" is not defined in section 1; a tie is not a majority and abstentions are not counted (fork F-ic1-6). Asserted.
11. Section 20(b): the majority needed is the higher of the specific one and the proposed one; a resolution that proposes none uses the specific one alone (fork F-ic1-7). Asserted.
12. Section 21(a): a later date the company fixes counts only if it is later than the day of the resolution, and a change of the kind section 40 deals with is excluded from the rule (NOTHING). Asserted.
13. Section 24(1): the 75 percent route is only for a provision on the capital or the name, a change of name needs no Minister's consent, and a change of the registered capital is valid from the day of the resolution. Asserted.
14. Section 27(a)(2): written consent of the owner of the mark lifts the bar for the whole paragraph (fork F-ic1-8). Asserted.
15. Section 29(b): the Registrar may change a name himself only when more than four months have passed since his demand with no notice of a resolution; four months exactly is still in time. Asserted.
16. Section 34(b): shares without par value state their number only; a stated par value fails the section (fork F-ic1-10). Asserted.
17. Section 37(b): the period the Registrar gives to produce the registers is at least fourteen days. Asserted.
18. Section 39(a): a signatory in "another position" counts as an office-holder only if he is the company secretary or one the company authorised. Asserted.
19. Section 40: an act the section does not list is not decided by it (NOTHING). Asserted.
20. Section 42: registration or existence of a document is not in itself evidence that I knew its contents. Asserted.
21. Section 48(d): "all the organs" includes a body treated as an organ under the third limb of section 46 (fork F-ic1-20). Asserted.
22. Section 50(a): a provision moving powers between organs is valid only if limited to a matter or to a period not longer than the circumstances need. Asserted.
23. Section 55(b): a shareholder or the company may apply for an order without showing a fear of harm, a creditor only with one (fork F-ic1-11). Asserted.
24. Section 56(a): an excessive act is valid against the company if the other party neither knew nor should have known, or if the company approved it. Asserted.
25. Section 58(a): a company may not vary section 57 in its articles, though it may add matters decided by the general meeting (58(b)). Asserted.
26. Section 60(a): fifteen months is still in time and sixteen is not (fork F-ic1-12). Asserted.
27. Section 61(a): only a private company may dispense with the annual meeting, and then a shareholder's or director's demand, or the need to appoint an auditor, brings the duty back. Asserted.
28. Section 63: the holdings of the demanding shareholders are added together (fork F-ic1-13); in a private company one director suffices, in a public company two directors or a quarter of those serving; the date of a public company's special meeting is at most thirty-five days from the notice, and the rule does not decide it for a private company. Asserted.
29. Section 64(a): requesters who hold exactly half of the requesters' voting rights may not convene; more than half is needed. Asserted.
30. Section 67: with no provision in the articles, an invitation to a private company's general meeting is in time from seven to forty-five days before the meeting. Asserted.
31. Section 74(c): the seventy-two-hour rule applies to an adjournment of twenty-one days or less with an unchanged agenda; otherwise the rule does not decide (NOTHING), and longer adjournments fall under 74(b). Asserted.
32. Section 78: one shareholder with 90 percent is not a quorum, 30 minutes is inside the half hour (fork F-ic1-14), and an adjournment is to seven days unless the notice names a later date. Asserted.
33. Section 79(b): the numbers needed at an adjourned meeting convened on a demand are those of the shareholders' route of section 63, by kind of company (fork F-ic1-15). Asserted.
34. Section 83(d): a vote in person or by proxy is deemed later than a voting deed; between person and proxy the later in fact counts (fork F-ic1-16). Asserted.
35. Section 84: a private company's articles may fix a different deciding rule; a public company's may not. Asserted.
36. Section 90(a): the minutes of a general meeting are kept for seven years. Asserted.
37. Section 95(a): the three-month grace after becoming a public company or a bond company applies to the bars of 95(a) only, and a director in a controlled corporation is not by that status alone "subordinate" (fork F-ic1-17). Asserted.
38. Section 98: one director may demand a board meeting only in a board of five or fewer, or if the articles or section 257 allow; absent a different period in the articles, a person may convene the meeting himself once more than fourteen days have passed. Asserted.
39. Section 100(a) to (c): the articles may vary the board's notice rules only in a private company that is not a bond company. Asserted.
40. Section 104 and 107: absent a quorum fixed in the articles, more than half the directors must be present; a tie goes to the additional vote of a chair who is present. Asserted.
41. Section 115(e): the committee chair's determination admits a person at the discussion or at the decision, an employee only at the discussion (fork F-ic1-18). Asserted.
42. Section 118(b): a private company's audit committee in which exactly half the members are material shareholders or their relatives may be appointed; more than half may not. Asserted.
43. An unexpected finding of the seat pass: the question for section 20(c) and 20(d) must be asked as "permitted" and "binds me" because the rules return TRUE when the requirement is satisfied; asked the other way round, "yes" would have meant the opposite. Asserted.

## What the stable binary does not accept
Run with the stable build 1.6.98.
- **Nothing in Hebrew was rejected**: Hebrew backticked names (rule names such as `סעיף 20(א) - ...`, constructors, parameters), `@export` and `@desc` lines in Hebrew followed by ` / ` and English, Hebrew `§` headings, and `@ref סעיף N (src:A-B)` over `-- src:N |` quote lines that carry `{{ח:ת}}` templates all compile, and `srcrefs.py check --refs` reports 0 problems.
- **Loud: `%` is not a comment marker.** A template line that began `% Holder of ...` was read as code and failed; comments are `--`.
- **Loud: a chain of `ELSE IF ... THEN` laid out over several lines gives "incorrect indentation"** (section 83(d)); written as `BRANCH IF ... THEN ... OTHERWISE`, it compiles.
- **Loud: `AND` and `OR` at the same indentation level is a warning**, and `check.sh` counts a warning as red; the board module bracketed the mix by a helper rule instead (`חברה ציבורית או חברה פרטית שהיא חברת איגרות חוב`).
- **Loud: a name defined in two imported modules cannot be used.** Several enumeration constructors (`מיזוג`, `חלוקה`, "another matter") clashed with the core's rules and with each other, and were renamed with the section they belong to (`מיזוג לענין סעיף 57(7)`, `חלוקה לענין סעיף 112(א)(2)`, `ענין אחר שאינו מנוי בסעיף 57`).
- **Silent: a percentage written after a call must be bracketed**, `(75%)`; unbracketed it attaches to the wrong operand.
- A rule head with no parameter names (`MEANS`) and a zero-arity constant (`MEANS TRUE`) both compile.
- `l4 run` of `ic1-cases-seat.l4` takes about one minute, because the file imports seventeen modules; `check.sh` over the folder takes about four minutes.

## What check.sh prints
Run as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` in this folder, on 2026-10-25. The words "the target is unstable" tell the script not to compare with a second binary.
```

check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
ic-core-company-kinds.l4                       0         0       0        0         0
ic-core-deals.l4                               0         0       0        0         0
ic-core-meetings.l4                            0         0       0        0         0
ic-core-people.l4                              0         0       0        0         0
ic-core-securities.l4                          0         0       0        0         0
ic-core.l4                                     0         0       0        0         0
ic1-cases-seat.l4                              0       805       0        0         0
ic1-majorities.l4                              0         0       0        0         0
ic1-part2-ch1-incorporation.l4                 0         0       0        0         0
ic1-part2-ch2-articles.l4                      0         0       0        0         0
ic1-part2-ch2-name-capital.l4                  0         0       0        0         0
ic1-part2-ch3-registrar.l4                     0         0       0        0         0
ic1-part3-ch1-organs.l4                        0         0       0        0         0
ic1-part3-ch2-gm-conduct.l4                    0         0       0        0         0
ic1-part3-ch2-gm-convening.l4                  0         0       0        0         0
ic1-part3-ch2-gm-powers-and-calling.l4         0         0       0        0         0
ic1-part3-ch3-board.l4                         0         0       0        0         0
ic1-part3-ch3-committees.l4                    0         0       0        0         0
ic1-seat.l4                                    0         0       0        0         0
ic1-tests-majorities.l4                        0        17       0        0         0
ic1-tests-part2-ch1-incorporation.l4           0       120       0        0         0
ic1-tests-part2-ch2-articles.l4                0        90       0        0         0
ic1-tests-part2-ch2-name-capital.l4            0        63       0        0         0
ic1-tests-part2-ch3-registrar.l4               0        65       0        0         0
ic1-tests-part3-ch1-organs.l4                  0        73       0        0         0
ic1-tests-part3-ch2-gm-conduct.l4              0       130       0        0         0
ic1-tests-part3-ch2-gm-convening.l4            0        57       0        0         0
ic1-tests-part3-ch2-gm-powers-and-calling.l4       0        90       0        0         0
ic1-tests-part3-ch3-board.l4                   0       184       0        0         0
ic1-tests-part3-ch3-committees.l4              0       135       0        0         0
TOTAL (30 modules)                             0      1829       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Reading it: the 1024 assertions of the layer-1 tests and the 805 cases of the seat layer are all satisfied (1829 in all, over 30 modules); none failed and none was refused; no file has an error or a warning. No test is meant to fail, so `expected` is 0 throughout.

## Before this is worth relying on
- **A domain expert must read it.** No Israeli corporate lawyer has read these modules against the Law. The source is an unofficial Wikisource consolidation, not the Reshumot text, and nothing was verified against the official text; amendments after the page was last edited are not known to be in it.
- **The forks must be ruled.** Above all F-ic1-6 (an ordinary majority is more votes for than against), F-ic1-7 (the "proposed majority" of s 20(b)), F-ic1-12 (the fifteen months of s 60(a)), F-ic1-17 and F-ic1-20 (who is an organ and who is subordinate).
- **The expected values were decided by the same author as the rules.** Every seat case passed on its first run, which shows that the questions are wired to the right rules and inputs; it does not show that the reading of the text is right. The independent test pass the lead plans is the real check.
- **Figures that regulations may change are taken as the Law states them**: the Minister may set the notice rules of ss 66, 69 and 71 and the voting-deed rules of s 89 (all inert here), and the fees of ss 9 and 44. Nothing here follows a regulation.
- **Terms taken as facts.** The controlling shareholder, a relative, an external director and an independent director are yes/no facts or counts in ss 94 to 118A, not computed by the core; the merged encoding should tie them to Part 6 chapter 1 (piece ic2) and to the core.
- **Out-of-range inputs.** Section 24 turns on section 377 (piece ic6), ss 94 to 102 on sections 121, 122(d), 169, 219 and 257, and s 57 and s 87(a) name matters whose rules are in later pieces; the merge should connect the yes/no inputs listed above to those rules.
- **The English glosses** of the `@desc` texts are the model's; a native reviewer should read the Hebrew phrasing of the questions, which a person is meant to answer.
- **Calendar and counting conventions.** Days and months are counts the person states; a year is twelve months elapsed; the last day of a period counts as inside it (F-ic1-4). A court's or the Registrar's judgment is always an input.

