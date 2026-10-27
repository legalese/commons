# NOTES: the Israeli Companies Law, 5759-1999 (חוק החברות, התשנ״ט–1999), the keel (`ic-core`)

Written by the keel agent `ic-g0` for the six part agents (`ic1` to `ic6`), who import these modules and take their facts about the whole text from this file.
Status: draft. No domain expert has read it against the source, and it has not been reviewed.
Encoding model: Claude Sonnet 5.5 (the folder is `legalese-sonnet-5.5`).

## What this folder holds

- `ic-core.l4`: the shared vocabulary. `DECLARE`s only (9 types), plus the one date shim `YMD`. It imports `prelude` and `daydate`.
- Five layer-1 modules that import `ic-core` and work out the definitions of section 1 from facts: `ic-core-company-kinds.l4`, `ic-core-securities.l4`, `ic-core-people.l4`, `ic-core-meetings.l4`, `ic-core-deals.l4`.
- Five test files, one per layer-1 module: `ic-core-tests-company-kinds.l4`, `ic-core-tests-securities.l4`, `ic-core-tests-people.l4`, `ic-core-tests-meetings.l4`, `ic-core-tests-deals.l4`. Assertions written in each: ic-core-tests-company-kinds.l4: 27, ic-core-tests-deals.l4: 42, ic-core-tests-meetings.l4: 37, ic-core-tests-people.l4: 84, ic-core-tests-securities.l4: 66.
- `NOTES.md` (this file), `PROGRESS.md`, and the two tools that were already here, `check.sh` and `srcrefs.py`.

## The source and its status

- Subject: the Companies Law, 5759-1999, Sefer HaChukim 5759, p 189.
- Text used: `companies-law-5759-1999.he.wiki.txt`, 3,555 lines by `wc -l`. Its sha256 is `8d44f234a79dca23ef8058859084ba64bb7a69437b88e94aee036b3f1ab21279`, as `../../registers/source-bundle/*.meta.json` records (re-computed here with `shasum -a 256`).
- It is the raw MediaWiki source of the Hebrew Wikisource page "חוק החברות" (page revision 3088229, last edited 2026-10-12), with its markup: `{{ח:סעיף|…}}` opens a section, `{{ח:ת|סוג=הגדרה}}` a definition, `{{ח:תתת|(1)}}` a paragraph, `{{ח:פנימי|…}}` and `{{ח:חיצוני|…}}` links.
- It is an unofficial consolidation. Israel publishes no free official consolidated text; the official version is the original publication in Reshumot together with every amending Act. Nothing here is verified against the official text.
- Every `-- src:N |` line in the modules copies line N of that file, markup included, by `srcrefs.py quote`; no wording is reconstructed from memory.
- Laws that the text cites (the Securities Law, the Trust Law, the Companies Ordinance, the Insolvency Law and others) are not among the inputs. Where a rule depends on one, its outcome is a plain input, named for what it is, with a comment.

## Seat

The individual to whom the Law is applied: a person who founds, directs or holds shares in a company (a founder, a director or officer, a shareholder including a minority shareholder), asking what the Law lets them do, what it requires of them, what they may require of the company, and what can be done to them (the seat given in the brief).
The keel writes no seat layer and no `@export`.
It chooses types a person in that seat can supply facts for: a holding as a fraction, whether a company's shares are listed and held by the public, whether the person is a spouse, a sibling or a parent of a director, and so on.
The Registrar, the court, the Minister and the Securities Authority are parties in `צד` so that a piece can say what may be done to the person, but none is a seat.

## Dates

The range contains no date of enactment, no assent date and no commencement rule.
The title (src:2) carries only the year, `התשנ״ט–1999`, which is not a date, so the keel defines no date value.
The two dates a piece may need are both in piece `ic6`'s range:

- passing by the Knesset: the signature block, src:3549, "נתקבל בכנסת ביום ג׳ באייר התשנ״ט (19 באפריל 1999)";
- commencement: section 377, src:3358-3359, "ביום כ״ה בשבט התש״ס (1 בפברואר 2000)", with the exceptions listed under it (for example sections 87 to 89, which come into force on a date set by regulations).

Piece `ic6` carries both as defined values with `@ref`.
No piece imports a date from the keel.

## Vocabulary

Every type and enumeration constructor of `ic-core.l4`, with `YMD`.
A name here is taken in every piece: see "Instructions to the pieces", item 2.
The English in the third column is a gloss of the Hebrew name, not part of it.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `צד` | enumeration (25 constructors) | the parties and bodies the Law names, in the form its operative text uses ("the Registrar", "the board") | section 1 (src:211, 234, 247-248, 250, 261) and section 46 (src:517-518); the audit committee, internal auditor, chairperson, controlling shareholder, creditor and compensation committee are named in sections 94, 114, 146, 268, 318 and 118א (section index only, not quoted) |
| `החברה` | constructor of `צד` | the company | as `צד` |
| `האסיפה הכללית` | constructor of `צד` | the general meeting | as `צד` |
| `אסיפת הסוג` | constructor of `צד` | a class meeting | as `צד` |
| `הדירקטוריון` | constructor of `צד` | the board of directors | as `צד` |
| `יושב ראש הדירקטוריון` | constructor of `צד` | the chairperson of the board | as `צד` |
| `המנהל הכללי` | constructor of `צד` | the general manager | as `צד` |
| `ועדת הביקורת` | constructor of `צד` | the audit committee | as `צד` |
| `ועדת התגמול` | constructor of `צד` | the compensation committee | as `צד` |
| `המבקר הפנימי` | constructor of `צד` | the internal auditor | as `צד` |
| `רואה החשבון המבקר` | constructor of `צד` | the external auditor | as `צד` |
| `הדירקטור` | constructor of `צד` | a director | as `צד` |
| `הדירקטור החיצוני` | constructor of `צד` | an external director | as `צד` |
| `נושא המשרה` | constructor of `צד` | an office-holder | as `צד` |
| `בעל המניות` | constructor of `צד` | a shareholder | as `צד` |
| `בעל השליטה` | constructor of `צד` | the controlling shareholder | as `צד` |
| `היזם` | constructor of `צד` | the promoter | as `צד` |
| `המציע` | constructor of `צד` | the offeror in a tender offer | as `צד` |
| `הניצע` | constructor of `צד` | the offeree in a tender offer | as `צד` |
| `בעל איגרת החוב` | constructor of `צד` | a bondholder | as `צד` |
| `הנושה` | constructor of `צד` | a creditor of the company | as `צד` |
| `הרשם` | constructor of `צד` | the Registrar of Companies | as `צד` |
| `בית המשפט` | constructor of `צד` | the court | as `צד` |
| `השר` | constructor of `צד` | the Minister (of Justice) | as `צד` |
| `רשות ניירות ערך` | constructor of `צד` | the Securities Authority | as `צד` |
| `אדם אחר` | constructor of `צד` | any other person | as `צד` |
| `סוג אדם` | enumeration (5 constructors) | the five kinds of person that "identity number" and "address" tell apart | section 1, ”מספר זהות“ and ”מען“ (src:217-228) |
| `יחיד תושב ישראל` | constructor of `סוג אדם` | an individual resident in Israel | as `סוג אדם` |
| `יחיד שאינו תושב ישראל` | constructor of `סוג אדם` | an individual not resident in Israel | as `סוג אדם` |
| `חברה הרשומה בישראל` | constructor of `סוג אדם` | a company registered in Israel | as `סוג אדם` |
| `חברה הרשומה מחוץ לישראל` | constructor of `סוג אדם` | a company registered outside Israel | as `סוג אדם` |
| `תאגיד אחר` | constructor of `סוג אדם` | any other corporation | as `סוג אדם` |
| `קרבה` | enumeration (10 constructors) | the ways of being related that "relative" lists | section 1, ”קרוב“ (src:246) |
| `בן זוג` | constructor of `קרבה` | spouse | as `קרבה` |
| `אח או אחות` | constructor of `קרבה` | brother or sister | as `קרבה` |
| `הורה` | constructor of `קרבה` | parent | as `קרבה` |
| `הורה של הורה` | constructor of `קרבה` | parent of a parent | as `קרבה` |
| `צאצא` | constructor of `קרבה` | descendant | as `קרבה` |
| `צאצא של בן הזוג` | constructor of `קרבה` | descendant of the spouse | as `קרבה` |
| `אח או אחות של בן הזוג` | constructor of `קרבה` | brother or sister of the spouse | as `קרבה` |
| `הורה של בן הזוג` | constructor of `קרבה` | parent of the spouse | as `קרבה` |
| `בן זוג של אחד מאלה` | constructor of `קרבה` | spouse of any person in this list | as `קרבה` |
| `קרבה אחרת` | constructor of `קרבה` | any other relationship | as `קרבה` |
| `משרה` | enumeration (8 constructors) | the offices "office-holder" lists, and "director" | section 1, ”דירקטור“ and ”נושא משרה“ (src:176, 234) |
| `מנהל כללי` | constructor of `משרה` | general manager | as `משרה` |
| `מנהל עסקים ראשי` | constructor of `משרה` | chief business manager (CEO in the usual sense) | as `משרה` |
| `משנה למנהל כללי` | constructor of `משרה` | deputy general manager | as `משרה` |
| `סגן מנהל כללי` | constructor of `משרה` | vice general manager | as `משרה` |
| `ממלא תפקיד כאמור בחברה אף אם תוארו שונה` | constructor of `משרה` | a person filling such a role even if the title differs | as `משרה` |
| `דירקטור` | constructor of `משרה` | a director: a member of the board | as `משרה` |
| `מנהל הכפוף במישרין למנהל הכללי` | constructor of `משרה` | a manager directly subordinate to the general manager | as `משרה` |
| `משרה אחרת` | constructor of `משרה` | any other position | as `משרה` |
| `דין ההתאגדות` | enumeration (5 constructors) | the Law or Ordinance a company was incorporated under | section 1, ”חברה“ (src:189) |
| `לפי חוק זה` | constructor of `דין ההתאגדות` | under this Law | as `דין ההתאגדות` |
| `לפי פקודת החברות` | constructor of `דין ההתאגדות` | under the Companies Ordinance | as `דין ההתאגדות` |
| `לפי פקודת החברות 1921` | constructor of `דין ההתאגדות` | under the Companies Ordinance 1921 | as `דין ההתאגדות` |
| `לפי פקודת החברות 1919` | constructor of `דין ההתאגדות` | under the Companies Ordinance 1919 | as `דין ההתאגדות` |
| `לפי דין אחר` | constructor of `דין ההתאגדות` | under any other law: not a company in the sense of this Law | as `דין ההתאגדות` |
| `עובדות על חברה` | record (12 fields) | the facts that decide what kind of company a company is, and three statuses taken as plain inputs. Fields: `הדין שלפיו התאגדה` (`דין ההתאגדות`); `מניותיה רשומות למסחר בבורסה` (BOOLEAN); `מניותיה הוצעו לציבור על פי תשקיף` (BOOLEAN); `מניותיה הוצעו לציבור מחוץ לישראל על פי מסמך הצעה לציבור` (BOOLEAN); `מניותיה מוחזקות בידי הציבור` (BOOLEAN); `איגרות החוב שלה רשומות למסחר בבורסה` (BOOLEAN); `איגרות החוב שלה הוצעו לציבור על פי תשקיף` (BOOLEAN); `איגרות החוב שלה הוצעו לציבור מחוץ לישראל על פי מסמך הצעה לציבור` (BOOLEAN); `איגרות החוב שלה מוחזקות בידי הציבור` (BOOLEAN); `חברה לתועלת הציבור` (BOOLEAN); `חברה ממשלתית` (BOOLEAN); `תאגיד מדווח` (BOOLEAN) | section 1 (src:189-190, 193-194, 196-197, 254) |
| `קשר לחברה` | record (7 fields) | one person's tie to one company: holdings, powers to appoint, offices held, control. Fields: `החזקה בהון המניות המונפק` (NUMBER); `החזקה בזכויות ההצבעה` (NUMBER); `סמכות למנות דירקטור אחד או יותר` (BOOLEAN); `סמכות למנות את המנהל הכללי` (BOOLEAN); `מכהן כדירקטור` (BOOLEAN); `מכהן כמנהל כללי` (BOOLEAN); `שליטה לפי חוק ניירות ערך` (BOOLEAN) | section 1, ”בעל מניה מהותי“, ”בעל ענין“, ”שליטה“ (src:172-173, 253) |
| `הצבעה` | record (3 fields) | the votes cast on one resolution, in voting rights. Fields: `קולות בעד` (NUMBER); `קולות נגד` (NUMBER); `קולות נמנעים` (NUMBER) | section 1, ”מנין קולות“ (src:216) |
| `מסמך שהרשם הוציא` | record (3 fields) | a document the Registrar issues: signed, attesting registration, with the day of incorporation. Fields: `חתום בחתימת הרשם` (BOOLEAN); `מעיד על רישומה של חברה` (BOOLEAN); `היום שקבע הרשם כיום ההתאגדות` (DATE) | section 1, ”יום ההתאגדות“ and ”תעודת התאגדות“ (src:210, 258) |
| `YMD` | function (date shim) | `YMD year month day` builds a DATE; the stable prelude has none. The one rule in the core; a piece must not define it again | the brief: `YMD` is missing from the stable prelude |

The layer-1 modules declare a few more types, used by their own rules only (a type used by one piece only does not belong in the core, so these stay beside the rule that reads them).
They are still taken names.

| name | declared in | kind | constructors or fields | licensed by |
| --- | --- | --- | --- | --- |
| `מקום מסחר` | `ic-core-company-kinds.l4` | enumeration (3 constructors) | `בורסה בישראל`; `בורסה מחוץ לישראל`; `שוק מוסדר כהגדרתו בחוק השקעות משותפות בנאמנות` | section 1, ”בורסה“ and ”בורסה בישראל“ (src:168-169) |
| `עובדות על מסמך חוב` | `ic-core-securities.l4` | record (8 fields) | `מסמך שהנפיקה חברה`; `מעיד על קיומה של התחייבות כספית שחבה החברה`; `מגדיר את תנאי ההתחייבות`; `שטר חוב או שטר חליפין שנתנה חברה במהלך עסקיה`; `ההתחייבות מובטחת במשכון על נכסי החברה, כולם או מקצתם`; `רשום למסחר בבורסה`; `הוצע לציבור על פי תשקיף`; `הוצע לציבור מחוץ לישראל על פי מסמך הצעה לציבור` | section 1, ”איגרת חוב“, ”איגרת חוב מובטחת“, ”בעל איגרת חוב“ (src:159, 160, 170) |
| `זכות בחברה` | `ic-core-securities.l4` | enumeration (3 constructors) | `זכות ההצבעה באסיפה כללית של חברה`; `הזכות למנות דירקטור של חברה`; `זכות אחרת` | section 1, ”אמצעי שליטה“ (src:161-163) |
| `עובדות על נתינה לבעל מניה` | `ic-core-securities.l4` | record (4 fields) | `נכס שניתן על ידי החברה לבעל מניה`; `הועבר ללא תמורה שוות ערך`; `ניתן מכוח זכותו כבעל מניה`; `הנתינה היא במניות הטבה` | section 1, ”דיבידנד“ (src:175) |
| `עובדות על חלוקה` | `ic-core-securities.l4` | record (6 fields) | `מתן דיבידנד`; `התחייבות לתת דיבידנד`; `רכישה או מתן מימון לרכישה של מניות החברה או של ניירות ערך הניתנים להמרה או למימוש במניותיה, בידי החברה, חברה בת שלה או תאגיד אחר בשליטתה`; `פדיון של ניירות ערך בני פדיון שהם חלק מהונה העצמי של החברה בהתאם לסעיף 312(ד)`; `התחייבות לעשיית אחד מאלה`; `המוכר הוא החברה עצמה או תאגיד אחר בבעלותה המלאה` | section 1, ”חלוקה“ (src:209) |
| `עובדות על הצעה לניירות ערך` | `ic-core-securities.l4` | record (3 fields) | `הצעה להנפקת ניירות ערך של חברה ציבורית`; `הצעה של חברה ציבורית למכירה של ניירות ערך שלה שנרכשו על ידה לפי סעיף 308`; `הצעה לציבור` | section 1, ”הצעה פרטית“, ”הצעה פרטית מהותית“ (src:184-185) |
| `עניין` | `ic-core-people.l4` | record (2 fields) | `עניין בפעולה או בעסקה של החברה`; `העניין נובע מעצם החזקת מניות בחברה` | section 1, ”ענין אישי“ (src:238) |
| `עובדות לענין אישי` | `ic-core-people.l4` | record (3 fields) | `עניינו של האדם`; `עניינו של קרובו`; `עניינו של תאגיד אחר שהאדם או קרובו הם בעלי ענין בו` | section 1, ”ענין אישי“ (src:238) |
| `פרט זיהוי` | `ic-core-people.l4` | enumeration (5 constructors) | `מספר הרישום`; `המדינה שבה החברה רשומה`; `מספר הזהות במרשם האוכלוסין`; `המדינה שבה הוצא הדרכון`; `מספר הדרכון` | section 1, ”מספר זהות“ (src:217-222) |
| `סוג המען` | `ic-core-people.l4` | enumeration (7 constructors) | `המען הרשום במרשם האוכלוסין`; `המען שהאדם מסר`; `מען המגורים`; `מען המשרד הרשום`; `מען המשרד מחוץ לישראל`; `המען בישראל שהחברה מסרה`; `המען הרשום על פי דין` | section 1, ”מען“ (src:223-228) |
| `פריט בתנאי כהונה והעסקה` | `ic-core-people.l4` | enumeration (8 constructors) | `תנאי כהונה או העסקה כשלעצמם`; `מתן פטור`; `ביטוח`; `התחייבות לשיפוי`; `שיפוי לפי היתר שיפוי`; `מענק פרישה כפריט בתנאי כהונה`; `הטבה, תשלום אחר או התחייבות לתשלום`; `פריט אחר` | section 1, ”תנאי כהונה והעסקה“ (src:257) |
| `עובדות לדירקטור בלתי תלוי` | `ic-core-people.l4` | record (6 fields) | `דירקטור חיצוני לפי חלק 6 פרק 1 סימן ה`; `יחיד המכהן כדירקטור`; `מונה או סווג ככזה לפי חלק 6 פרק 1`; `מתקיימים תנאי הכשירות לפי סעיף 240(ב) עד (ו)`; `ועדת הביקורת אישרה זאת`; `שנות כהונה רצופות כדירקטור בחברה` | section 1, ”דירקטור בלתי תלוי“ (src:177-179) |
| `עובדות על אסיפה` | `ic-core-meetings.l4` | record (3 fields) | `אסיפה של בעלי המניות`; `אסיפה של בעלי סוג מניות`; `אסיפה לפי סעיף 60` | section 1, the four meetings (src:164-167) |
| `עובדות על עסקה` | `ic-core-deals.l4` | record (5 fields) | `חוזה או התקשרות`; `החלטה חד צדדית של חברה בדבר הענקת זכות או טובת הנאה אחרת`; `במהלך העסקים הרגיל של החברה`; `בתנאי שוק`; `עשויה להשפיע באופן מהותי על רווחיות החברה, רכושה או התחייבויותיה` | section 1, ”עסקה“ and ”עסקה חריגה“ (src:239-240) |
| `עובדות על הצעה לרכישת מניות` | `ic-core-deals.l4` | record (2 fields) | `הצעה לרכישת מניות`; `מופנית לציבור בעלי המניות של חברה` | section 1, ”הצעת רכש“ (src:186) |
| `עובדות על מיזוג` | `ic-core-deals.l4` | record (3 fields) | `העברה של כלל הנכסים והחיובים, לרבות חיובים מותנים, עתידיים, ידועים ובלתי ידועים, של חברת יעד לחברה קולטת`; `כתוצאה מההעברה מתחסלת חברת היעד`; `ההעברה היא בהתאם לסעיף 323` | section 1, ”מיזוג“ (src:213) |

## Naming conventions

All of these are assumed here, not ruled: nobody has ruled on how an Israeli encoding should name things, except the ` / ` English gloss in `@export` and `@desc`, which the brief takes from the existing Israeli Penal Law encoding and also marks as assumed.

- **A rule** that works out a section 1 definition is named by the defined term exactly as the Law writes it, as a bare noun phrase: `` `חברה ציבורית` ``, `` `בעל ענין` ``, `` `קרוב` ``. A call is prefix: `` `חברה ציבורית` `העובדות` ``.
  The head of a rule carries no parameter names: the inputs are the `GIVEN` list, in order, and the "Rule signatures" table in "Instructions to the pieces" lists them.
  A rule that a piece writes for a provision is named `` `סעיף N - …` ``, with N the section label in ASCII digits and, if it has one, the Hebrew letter (`` `סעיף 116א - …` ``), then the Law's own words. That keeps the pieces' names apart even if their modules are ever imported together.
- **A record of facts** is named `` `עובדות על <the thing>` `` or `` `עובדות ל<the thing>` ``, and its fields are the facts in the Law's words, each a noun phrase or a complete predicate, with no leading "is" or "has". A boolean field reads as a statement: `` `מניותיה רשומות למסחר בבורסה` ``.
  A record is built with `WITH`, every field given. A field a rule does not read is given a fixed placeholder, with a comment saying so.
- **An input** (a `GIVEN` name) is a descriptive phrase for the fact, one input per fact. It never starts with the article ה followed by a party noun, and it is never equal to a constructor of `צד`, a rule name, a type name or a field name. The generic name for the facts record in the layer-1 modules is `` `העובדות` ``.
- **An enumeration constructor** is the Law's noun phrase for the kind. The constructors of `צד` are in the definite form the operative text uses (`` `הדירקטוריון` ``, `` `הרשם` ``), and the rule or constructor for a defined term is in the bare form, so the two never collide. A constructor is never also a rule, type or field name (checked by script; see "Instructions", item 2).
- **A question** (in a seat layer, which the pieces write) is named by its Hebrew question as the person asks it, beginning with the question word: `` `האם אני רשאי …` ``, `` `מה …` ``, `` `כמה …` ``. Its `@export` and `@desc` texts are Hebrew followed by ` / ` and a plain English gloss; the `§` headings are Hebrew only.
- **An amount of money** is a `NUMBER` of new shekels (שקלים חדשים), whole shekels, no agorot. "Ten million" is `10_000_000`, written with `_`.
- **A percentage or share** is a `NUMBER` that is a fraction of one, written with the postfix `%`: `5%` is 0.05 and "twenty-five percent" is `25%`. A percentage that follows a call needs brackets: `` f x AT LEAST (25%) ``, because `` f 25% `` reads as `(f 25)%` and fails to type-check. A seat input for "7 percent" takes 0.07.
- **Days** are a `NUMBER` of calendar days, and a time limit "within N days" is `WITHIN N`. "A week" is 7, "thirty days" is 30. **Months and years** are a `NUMBER` of months or years, and the unit is in the name of the input (`` `שנות כהונה רצופות כדירקטור בחברה` ``).
- **Dates** are `DATE`, written `YMD year month day` (civil calendar). `YMD` is defined once, in `ic-core.l4`; pieces must not define it again. Dates built with it compare with `AT LEAST`, `GREATER THAN` and `AT MOST`.
- **A fact outside a piece** (a result of another piece's section, or of another Law) is a plain `BOOLEAN` or `NUMBER` input, named for what it says with the section it comes from in the name (`` `אסיפה לפי סעיף 60` ``), and listed in that piece's `NOTES.md`. The inputs the keel already takes this way are in the table in "Instructions", item 10.
- **A judgment the Law hands to someone else** ("if the Registrar is satisfied that …") is answered conditionally, as a `BOOLEAN` input named for the judgment (`` `הרשם השתכנע ש…` ``); it is never guessed.
- **A case the encoding does not cover** returns `NOTHING` from a `MAYBE`, never `FALSE` or 0, and a test asserts it (`` `פרמיה` 1_000_000 1_000_000 EQUALS NOTHING ``).

## Defined terms

94 terms on 89 definition lines (src:159-261); two of the lines are deleted in this text, so they define nothing.
"Encoded in" gives the module and rule, or "by reference: encoded by piece X, section N, taken there as an input" when the definition points at another piece's provision, or "by reference: not encoded by any piece (…), taken as a plain input" when it points at another Law.
Counted by definition line and kind: C 8, D 2, P 2, R 57, T 9, X 11 (R rule in a layer-1 module; T core vocabulary or a constructor; P by reference to a piece; X external Law, taken as an input; C citation only; D deleted).

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| `איגרת חוב` (bond) | section 1, src:159 | `ic-core-securities.l4`: rule `איגרת חוב` | Facts in `עובדות על מסמך חוב`; promissory notes and bills of exchange a company gives in its business are excluded. |
| `איגרת חוב מובטחת` (secured bond) | section 1, src:160 | `ic-core-securities.l4`: rule `איגרת חוב מובטחת` | A bond whose obligation is secured by a pledge on all or some of the assets. |
| `אמצעי שליטה` (means of control (lead-in)) | section 1, src:161 | `ic-core-securities.l4`: rule `אמצעי שליטה` | True of each of the two rights listed in paragraphs (1) and (2); `זכות אחרת` stands for any other right. |
| `אסיפה כללית` (general meeting) | section 1, src:164 | `ic-core-meetings.l4`: rule `אסיפה כללית` | An annual or a special meeting of the shareholders. |
| `אסיפה מיוחדת` (special meeting) | section 1, src:165 | `ic-core-meetings.l4`: rule `אסיפה מיוחדת` | A general meeting of the shareholders that is not annual. Entry F12 on the circle with `אסיפה כללית`. |
| `אסיפת סוג` (class meeting) | section 1, src:166 | `ic-core-meetings.l4`: rule `אסיפת סוג` |  |
| `אסיפה שנתית` (annual meeting) | section 1, src:167 | `ic-core-meetings.l4`: rule `אסיפה שנתית`; the words "under section 60" are by reference: encoded by piece ic1, section 60, taken in `ic-core-meetings.l4` as the input `אסיפה לפי סעיף 60` |  |
| `בורסה` (bourse) | section 1, src:168 | `ic-core-company-kinds.l4`: rule `בורסה` | A bourse abroad counts only if approved by whoever may approve it by law in that country; the approval is a plain input. |
| `בורסה בישראל` (bourse in Israel) | section 1, src:169 | `ic-core-company-kinds.l4`: constructor `בורסה בישראל`; the Securities Law meaning is by reference: not encoded by any piece (the Securities Law is not among the inputs), a caller says which place of trading it is |  |
| `בעל איגרת חוב` (bondholder, in a bond company) | section 1, src:170 | `ic-core-securities.l4`: rule `בעל איגרת חוב` |  |
| `בית המשפט` (the court (deleted)) | section 1, src:171 | none: deleted in the text ("(נמחקה)"); see the stub and, for sections 6 and 7, the note in "Instructions to the pieces" | The source marks the definition deleted; section 6(d) (src:289, piece ic1) gives "the court" a meaning for sections 6 and 7. |
| `בעל מניה מהותי` (material shareholder) | section 1, src:172 | `ic-core-people.l4`: rule `בעל מניה מהותי` | 5% or more of the issued share capital or of the voting rights; "holds" is as the Securities Law counts holding (src:182 points there), so the caller supplies the fractions (entry F13). |
| `בעל ענין` (interested party) | section 1, src:173 | `ic-core-people.l4`: rule `בעל ענין` |  |
| `דבוקת שליטה` (control block (shares giving 25% or more of the voting rights)) | section 1, src:174 | `ic-core-people.l4`: rule `דבוקת שליטה` |  |
| `דיבידנד` (dividend) | section 1, src:175 | `ic-core-securities.l4`: rule `דיבידנד` | A transfer without equal consideration counts as given; bonus shares are excluded. |
| `דירקטור` (director: a member of the board) | section 1, src:176 | `ic-core.l4`: constructor `דירקטור` of `משרה` (and `הדירקטור` of `צד`); no separate rule |  |
| `דירקטור בלתי תלוי` (independent director (lead-in)) | section 1, src:177 | `ic-core-people.l4`: rule `דירקטור בלתי תלוי`; the conditions that point at section 240 and Part 6 chapter 1 are by reference: encoded by piece ic2, taken as inputs | Fork F4 (what "appointed or classified as such" qualifies) and entry F14. |
| `דירקטור חיצוני` (external director) | section 1, src:180 | by reference: encoded by piece ic2, Part 6 chapter 1 sub-chapter E (sections 239 to 249ג), taken in `ic-core-people.l4` as an input |  |
| `דמי פיגורים` , `ריבית שקלית` (arrears charges and shekel interest) | section 1, src:181 | by reference: not encoded by any piece (the Interest and Linkage Adjudication Law, 5721-1961 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:181 |
| `החזקה` , `רכישה` (holding and acquisition (as in the Securities Law)) | section 1, src:182 | by reference: not encoded by any piece (the Securities Law, 5728-1968 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:182 |
| `הליכי חדלות פירעון` (insolvency proceedings) | section 1, src:183 | by reference: not encoded by any piece (the Insolvency and Economic Rehabilitation Law, 5778-2018 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:183 |
| `הצעה פרטית` (private offer) | section 1, src:184 | `ic-core-securities.l4`: rule `הצעה פרטית`; the securities "acquired under section 308" are by reference: encoded by piece ic3, section 308, taken as an input | "Public offer" has its Securities Law meaning and is a plain input. |
| `הצעה פרטית מהותית` (material private offer) | section 1, src:185 | `ic-core-securities.l4`: rule `הצעה פרטית מהותית`; the condition in section 270(5) is by reference: encoded by piece ic3, section 270, taken as the input `מתקיים בה האמור בסעיף 270(5)` |  |
| `הצעת רכש` (tender offer) | section 1, src:186 | `ic-core-deals.l4`: rule `הצעת רכש` |  |
| `ועדת דירקטוריון` (board committee) | section 1, src:187 | `ic-core-meetings.l4`: rule `ועדת דירקטוריון`; the words "under section 110" are by reference: encoded by piece ic1, section 110, taken as an input |  |
| `חבר בורסה` (member of a bourse) | section 1, src:188 | by reference: not encoded by any piece (the Securities Law, 5728-1968 (section 46) is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:188 |
| `חברה` (company) | section 1, src:189 | `ic-core-company-kinds.l4`: rule `חברה` | A company is one incorporated under this Law, the Ordinance, or the 1921 or 1919 Ordinance. |
| `חברת איגרות חוב` (bond company) | section 1, src:190 | `ic-core-company-kinds.l4`: rule `חברת איגרות חוב` | Fork F1 (the scope of "and held by the public"). |
| `חברה בת` (subsidiary) | section 1, src:191 | by reference: not encoded by any piece (the Securities Law, 5728-1968 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:191 |
| `חברה לרישומים` (registration (nominee) company) | section 1, src:192 | by reference: not encoded by any piece (the Securities Law, 5728-1968 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:192 |
| `חברה לתועלת הציבור` (public-benefit company) | section 1, src:193 | by reference: encoded by piece ic5, Part 9 chapter 1A, taken in `ic-core.l4` as the field `חברה לתועלת הציבור` |  |
| `חברה ממשלתית` , `חברת בת ממשלתית` (government company and government subsidiary) | section 1, src:194 | by reference: not encoded by any piece (the Government Companies Law, 5735-1975 is not among the inputs), taken as a plain input: the field `חברה ממשלתית` of `עובדות על חברה` covers both terms | One field for both terms; a piece that must tell a government subsidiary apart takes its own input. |
| `חברה מתמזגת` (merging company) | section 1, src:195 | `ic-core-deals.l4`: rule `חברה מתמזגת` | A target company or an absorbing company (entry F9). |
| `חברה פרטית` (private company) | section 1, src:196 | `ic-core-company-kinds.l4`: rule `חברה פרטית` | A company that is not public; a body that is not a company is not a private company either. |
| `חברה ציבורית` (public company) | section 1, src:197 | `ic-core-company-kinds.l4`: rule `חברה ציבורית` | Fork F1 (the scope of "and held by the public"). |
| `חברה קולטת` (absorbing company) | section 1, src:198 | `ic-core-deals.l4`: rule `חברה קולטת` |  |
| `חברה קשורה` (affiliated company) | section 1, src:199 | by reference: not encoded by any piece (the Securities Law, 5728-1968 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:199 |
| `חברת חוץ` (foreign company) | section 1, src:200 | `ic-core-company-kinds.l4`: rule `חברת חוץ` |  |
| `חברת יעד` (target company of a merger) | section 1, src:201 | `ic-core-deals.l4`: rule `חברת יעד` |  |
| `חברת מטרה` (target company of a tender offer) | section 1, src:202 | `ic-core-deals.l4`: rule `חברת מטרה` |  |
| `חוק הנאמנות` (short name of the Trust Law, 5739-1979) | section 1, src:203 | citation only: not encoded by any piece (the Trust Law, 5739-1979 is not among the inputs) | inert; the reason is in the coverage row for src:203 |
| `חוק העמותות` (short name of the Associations Law, 5740-1980) | section 1, src:204 | citation only: not encoded by any piece (the Associations Law, 5740-1980 is not among the inputs) | inert; the reason is in the coverage row for src:204 |
| `חוק חדלות פירעון ושיקום כלכלי` (short name of the Insolvency and Economic Rehabilitation Law, 5778-2018) | section 1, src:205 | citation only: not encoded by any piece (the Insolvency and Economic Rehabilitation Law, 5778-2018 is not among the inputs) | inert; the reason is in the coverage row for src:205 |
| `חוק ניירות ערך` (short name of the Securities Law, 5728-1968) | section 1, src:206 | citation only: not encoded by any piece (the Securities Law, 5728-1968 is not among the inputs) | inert; the reason is in the coverage row for src:206 |
| `חוק פסיקת ריבית והצמדה` (short name of the Interest and Linkage Adjudication Law, 5721-1961) | section 1, src:207 | citation only: not encoded by any piece (the Interest and Linkage Adjudication Law, 5721-1961 is not among the inputs) | inert; the reason is in the coverage row for src:207 |
| `חוק תקשורת דיגיטלית עם גופים ציבוריים` (short name of the Digital Communication with Public Bodies Law, 5778-2018) | section 1, src:208 | citation only: not encoded by any piece (the Digital Communication with Public Bodies Law, 5778-2018 is not among the inputs) | inert; the reason is in the coverage row for src:208 |
| `חלוקה` (distribution (with the inner definition of "acquisition")) | section 1, src:209 | `ic-core-securities.l4`: rule `חלוקה` and `ic-core-securities.l4`: rule `רכישה לענין חלוקה`; the redemption "under section 312(d)" is by reference: encoded by piece ic3, section 312, taken as an input | Fork F3 (the scope of the proviso about the seller). The inner "acquisition" is named apart from the Securities Law's (src:182). |
| `יום ההתאגדות` (day of incorporation) | section 1, src:210 | `ic-core-meetings.l4`: rule `יום ההתאגדות` | The date the Registrar fixed in the certificate; NOTHING for a document that is not a certificate of incorporation (entry F16). |
| `יזם` (promoter) | section 1, src:211 | `ic-core-people.l4`: rule `יזם` |  |
| `מדד` (index (the consumer price index)) | section 1, src:212 | by reference: not encoded by any piece (the Central Bureau of Statistics' consumer price index (no Law is cited) is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:212 |
| `מיזוג` (merger (for Part 8)) | section 1, src:213 | `ic-core-deals.l4`: rule `מיזוג`; "in accordance with section 323" is by reference: encoded by piece ic4, section 323, taken as the input `ההעברה היא בהתאם לסעיף 323` |  |
| `מניה` (share) | section 1, src:214 | `ic-core-securities.l4`: rule `מניה` | A bundle of rights in the company fixed by law and by the articles. |
| `מניות הטבה` (bonus shares) | section 1, src:215 | `ic-core-securities.l4`: rule `מניות הטבה` |  |
| `מנין קולות` (count of votes) | section 1, src:216 | `ic-core-meetings.l4`: rule `מנין קולות` | Fork F2 (abstentions). |
| `מספר זהות` (identity number (lead-in)) | section 1, src:217 | `ic-core-people.l4`: rule `מספר זהות` | Returns the list of details that identify that kind of person, or NOTHING. |
| `מען` (address (lead-in)) | section 1, src:223 | `ic-core-people.l4`: rule `מען` | Returns which address counts for that kind of person, or NOTHING. |
| `מען דיגיטלי` (digital address) | section 1, src:229 | by reference: encoded by piece ic6, Fourth Schedule (items 1 and 2), taken as a plain input by any piece that needs it (piece ic2, section 123א) | inert; the reason is in the coverage row for src:229 |
| `מענק פרישה` (severance grant) | section 1, src:230 | `ic-core-people.l4`: rule `מענק פרישה` |  |
| `מציע` (offeror in a tender offer) | section 1, src:231 | `ic-core-deals.l4`: rule `מציע` |  |
| `משכון` (pledge) | section 1, src:232 | `ic-core-securities.l4`: rule `משכון` | A pledge as the Pledges Law means it (a plain input) or a floating charge. |
| `נוכחות בעל מניות` (presence of a shareholder) | section 1, src:233 | `ic-core-meetings.l4`: rule `נוכחות בעל מניות`; the voting deed "under section 87" is by reference: encoded by piece ic1, section 87, taken as an input |  |
| `נושא משרה` (office-holder) | section 1, src:234 | `ic-core-people.l4`: rule `נושא משרה` |  |
| `נייר ערך` (security) | section 1, src:235 | `ic-core-securities.l4`: rule `נייר ערך` | "Includes" leaves the list open, so the last input is the caller's word for any other security (entry F8). |
| `ניצע` (offeree in a tender offer) | section 1, src:236 | `ic-core-deals.l4`: rule `ניצע` |  |
| `סדרת איגרות חוב` (series of bonds) | section 1, src:237 | `ic-core-securities.l4`: rule `סדרת איגרות חוב` |  |
| `ענין אישי` (personal interest) | section 1, src:238 | `ic-core-people.l4`: rule `ענין אישי` (and the power-of-attorney limb in `הצבעה שנחשבת הצבעה של בעל עניין אישי`) | Fork F7 (what the exclusion for share-holding applies to). |
| `עסקה` (transaction) | section 1, src:239 | `ic-core-deals.l4`: rule `עסקה` |  |
| `עסקה חריגה` (extraordinary transaction) | section 1, src:240 | `ic-core-deals.l4`: rule `עסקה חריגה` |  |
| `פעולה` (act) | section 1, src:241 | `ic-core-deals.l4`: rule `פעולה` |  |
| `פעולה מהותית` (material act) | section 1, src:242 | `ic-core-deals.l4`: rule `פעולה מהותית` |  |
| `פקודת החברות` (short name of the Companies Ordinance [new version], 5743-1983) | section 1, src:243 | citation only: not encoded by any piece (the Companies Ordinance [new version], 5743-1983 is not among the inputs) | inert; the reason is in the coverage row for src:243 |
| `פרמיה` (premium) | section 1, src:244 | `ic-core-securities.l4`: rule `פרמיה` | NOTHING when the consideration does not exceed the par value (entry F11). |
| `צו לפתיחת הליכים` (order opening proceedings) | section 1, src:245 | by reference: not encoded by any piece (the Insolvency and Economic Rehabilitation Law, 5778-2018 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:245 |
| `קרוב` (relative) | section 1, src:246 | `ic-core-people.l4`: rule `קרוב` | Fork F5 ("the spouse of each of these"). |
| `רואה חשבון מבקר` (external auditor) | section 1, src:247 | `ic-core-meetings.l4`: rule `רואה חשבון מבקר`; the appointment "as stated in section 154" is by reference: encoded by piece ic2, section 154, taken as an input |  |
| `רשות ניירות ערך` (Securities Authority) | section 1, src:248 | `ic-core.l4`: constructor `רשות ניירות ערך` of `צד`; its powers are the Securities Law's: by reference, not encoded by any piece | The Authority as an actor; the definition adds no condition. |
| `רשם ההקדשות` , `הקדש ציבורי` (Registrar of Endowments and public endowment) | section 1, src:249 | by reference: not encoded by any piece (the Trust Law, 5739-1979 is not among the inputs), taken as a plain input | inert; the reason is in the coverage row for src:249 |
| `רשם החברות` , `הרשם` (Registrar of Companies, the Registrar) | section 1, src:250 | `ic-core.l4`: constructor `הרשם` of `צד`; the office is by reference: encoded by piece ic1, section 36 | The office as an actor. |
| `שטר מניה` (share warrant (deleted)) | section 1, src:251 | none: deleted in the text ("(נמחקה)") | The source marks the definition deleted. |
| `שעבוד צף` (floating charge) | section 1, src:252 | by reference: not encoded by any piece (the Companies Ordinance [new version], 5743-1983 is not among the inputs), taken as a plain input | The Ordinance is not among the inputs; whether a charge is a floating charge is a plain input of `משכון`. |
| `שליטה` (control) | section 1, src:253 | by reference: not encoded by any piece (the Securities Law, 5728-1968 is not among the inputs), taken as a plain input: the field `שליטה לפי חוק ניירות ערך` of `קשר לחברה` |  |
| `תאגיד מדווח` (reporting corporation) | section 1, src:254 | by reference: not encoded by any piece (the Securities Law, 5728-1968 is not among the inputs), taken as a plain input: the field `תאגיד מדווח` of `עובדות על חברה` (true if the Securities Law defines it as a reporting corporation, or chapter E3 of that Law applies to it) |  |
| `תביעה נגזרת` (derivative claim) | section 1, src:255 | `ic-core-deals.l4`: rule `תביעה נגזרת` |  |
| `תזכיר` (memorandum of association (as in the Ordinance before this Law's commencement)) | section 1, src:256 | citation only: the Companies Ordinance as worded on the eve of commencement; not encoded by any piece, taken as a plain input (piece ic1, section 24, uses it) | inert; the reason is in the coverage row for src:256 |
| `תנאי כהונה והעסקה` (terms of service and employment of an office-holder) | section 1, src:257 | `ic-core-people.l4`: rule `תנאי כהונה והעסקה` | Fork F6 (what "given by reason of such service or employment" qualifies). |
| `תעודת התאגדות` (certificate of incorporation) | section 1, src:258 | `ic-core-meetings.l4`: rule `תעודת התאגדות` |  |
| `תעודת מניה` (share certificate) | section 1, src:259 | `ic-core-securities.l4`: rule `תעודת מניה` |  |
| `תקנון` (articles of association) | section 1, src:260 | `ic-core-meetings.l4`: rule `תקנון` |  |
| `השר` (the Minister (of Justice)) | section 1, src:261 | `ic-core.l4`: constructor `השר` of `צד` | The office as an actor; the Minister's powers are each piece's, as judgments handed to someone else. |

## Instructions to the pieces

1. **Files and imports.** The `ic-core*.l4` modules are copied into your folder; a module is found only in the importing file's own folder. Write `` IMPORT `ic-core` `` yourself (a hyphenated module name needs backticks) and each layer-1 module whose rules you call; do not rely on one import bringing another. Never edit a file whose name begins `ic-core`, and never create one. Your tests import the core and the modules they call, as `ic-core-tests-*.l4` do.
2. **Taken names.** A name defined in two imported modules cannot be used at all, so you never define a type, constructor, field or rule whose name is in the Vocabulary tables, the Rule signatures table or the Defined terms table above. Name your own rules `` `סעיף N - …` `` (see Naming conventions). An input (a `GIVEN` name) must not equal a constructor of `צד` (`` `החברה` ``, `` `הדירקטור` ``, `` `הרשם` ``, `` `בית המשפט` ``) or any rule, type or field name; the parameter names in the Rule signatures table are local to their rules and may be reused. This was checked for the keel with a script that lists every name defined in the non-test modules and found no name used in two roles, after three clashes were renamed (a field named like its type, a field named like a rule, a constructor named like a rule).
3. **Call the definitions; do not restate them.** Section 1 applies "in this Law", so wherever your section says "public company", "office-holder", "relative", "interested party", "transaction" and so on, build the facts record and call the core rule. The "Rule signatures" table below lists every rule, its inputs in order, and its result.
4. **Extend by composition, never by editing.** A fact your piece needs that no core record carries is your own `GIVEN` or your own record, passed beside the core one. If you need a party that `צד` lacks, say so in your `NOTES.md` and use your own enumeration for that rule; do not copy `צד` and add to it, because a copy repeats the core's constructor names.
5. **Parties.** A regulative rule takes its `PARTY` from `צד`; the action type is your own. On the stable build a `PARTY` that is not the performer of the action is not reported, so check it by eye. An input named in an action is read as a fresh name that matches any payload: write `PROVIDED payee EQUALS …` instead (dialects.md).
6. **Units, as in the Naming conventions.** Fractions with `%`, shekels as whole numbers, days as numbers, dates through `YMD`.
7. **The Wikisource notes are not the Act.** The text carries editorial notes in `{{ח:הערה|…}}`, for example src:1161: "500,000 שקלים חדשים {{ח:הערה|(מתואם לשנת 2005; בשנת 2026, 731,660 ש״ח)}}". The Act's own figure (500,000) is the constant; the note's updated figure goes in a comment and is registered as a fork in your `NOTES.md`; say whether the Act lets a Minister or an index update the figure.
8. **Dates and duplicates that belong to `ic6`.** Passing (src:3549) and commencement (section 377, src:3358-3359) are `ic6`'s to carry. The section label `351ו` opens two sections (src:3135 and src:3140): `ic6` quotes each by its own lines. Section 6(d) (src:289, piece `ic1`) gives "the court" a meaning for sections 6 and 7 only, the court with jurisdiction over the claim, while section 1's definition of "the court" is deleted (src:171).
9. **The stub `הגדרות שנמחקו מסעיף 1`** in `ic-core-company-kinds.l4` keeps the deleted definitions of section 1 in the file as inert text. It evaluates to `TRUE` (an inert string in a boolean context) and must not be called.
10. **Inputs that the keel takes from your pieces.** Each is a plain input in the keel and is yours to encode; a piece's own rule should be what produces the value a seat layer passes in.

    | input (record or rule, module) | what it stands for | piece | section (source line) |
    | --- | --- | --- | --- |
    | `אסיפה לפי סעיף 60` (`עובדות על אסיפה`, meetings) | the meeting is the annual meeting under section 60 | ic1 | 60 (src:591) |
    | `בעל המניות נוכח באמצעות כתב הצבעה כאמור בסעיף 87` (`נוכחות בעל מניות`, meetings) | presence by a voting deed | ic1 | 87 (src:713) |
    | `הוקמה לפי הוראות סעיף 110` (`ועדת דירקטוריון`, meetings) | the committee was set up under section 110 | ic1 | 110 (src:867) |
    | constructor `הרשם` of `צד` | the office of the Registrar of Companies | ic1 | 36 (src:452) |
    | `תזכיר` (not encoded, a citation) | the memorandum as the Ordinance read before this Law | ic1 | 24 (src:387) |
    | `מונה לשם ביצוע פעולת ביקורת כאמור בסעיף 154` (`רואה חשבון מבקר`, meetings) | the accountant was appointed to audit under section 154 | ic2 | 154 (src:1145) |
    | `דירקטור חיצוני לפי חלק 6 פרק 1 סימן ה`, `מונה או סווג ככזה לפי חלק 6 פרק 1`, `מתקיימים תנאי הכשירות לפי סעיף 240(ב) עד (ו)` (`עובדות לדירקטור בלתי תלוי`, people) | external director; appointed or classified as independent; the section 240(b) to (f) qualifications | ic2 | Part 6 chapter 1 sub-chapter E, 239 to 249ג (src:1596-1683); 240 (src:1607) |
    | `מתקיים בה האמור בסעיף 270(5)` (`הצעה פרטית מהותית`, securities) | what section 270(5) says applies to the private offer | ic3 | 270 (src:1828) |
    | `הצעה של חברה ציבורית למכירה של ניירות ערך שלה שנרכשו על ידה לפי סעיף 308` (`עובדות על הצעה לניירות ערך`, securities) | the securities were acquired by the company under section 308 | ic3 | 308 (src:2045) |
    | `פדיון של ניירות ערך בני פדיון … בהתאם לסעיף 312(ד)` (`עובדות על חלוקה`, securities) | redemption under section 312(d) | ic3 | 312 (src:2072) |
    | `ההעברה היא בהתאם לסעיף 323` (`עובדות על מיזוג`, deals) | the transfer is a merger under section 323 | ic4 | 323 (src:2127) |
    | `חברה לתועלת הציבור` (`עובדות על חברה`, core) | the company is a public-benefit company | ic5 | Part 9 chapter 1A (src:2516-2955) |
    | digital address (not a type here) | each detail listed in the Fourth Schedule: an e-mail address; a mobile number or a different e-mail address | ic6 (the Schedule); ic2 uses it in section 123א | Fourth Schedule (src:3540-3547); 123א (src:982) |

11. **Building a core record from plain inputs.** `עובדות על חברה` has 12 fields and every field must be given; give a fixed placeholder to a field your rule does not read, with a comment. The same goes for `קשר לחברה` (7 fields). The core rules read only what their definitions read, so a placeholder does not change an answer; the tests in `ic-core-tests-*.l4` show a record built field by field.
12. **Open lists.** Where the Law says "includes" (`נייר ערך`, `תנאי כהונה והעסקה`), the core rule is true for the listed things and takes a caller's input for anything else the Law does not list. Do the same for an open list in your piece (phrasebook entry 2.7), and never close it.
13. **Votes.** `הצבעה` holds the votes for, against and abstaining in voting rights; `מנין קולות` returns for plus against (fork F2). "Ordinary majority" is not defined in section 1 (it is used in sections 20, 85 and 107): a piece that needs it states its reading as a fork and builds it from `הצבעה`.
14. **Section 249ב (src:1680).** Piece `ic2` should check fork F4 against it: classification as an independent director is the step for a director who qualifies under paragraphs (1) and (2) of the definition, so the keel reads "appointed or classified as such" as qualifying the individual limb only.
15. **Dialect.** Target `main` build 98. Read "What the stable binary does not accept" before you write.

### Rule signatures

| rule | module | inputs, in order (GIVEN) | returns |
| --- | --- | --- | --- |
| `חברה` | `ic-core-company-kinds.l4` | `העובדות` : `עובדות על חברה` | BOOLEAN |
| `חברה ציבורית` | `ic-core-company-kinds.l4` | `העובדות` : `עובדות על חברה` | BOOLEAN |
| `חברה פרטית` | `ic-core-company-kinds.l4` | `העובדות` : `עובדות על חברה` | BOOLEAN |
| `חברת איגרות חוב` | `ic-core-company-kinds.l4` | `העובדות` : `עובדות על חברה` | BOOLEAN |
| `בורסה` | `ic-core-company-kinds.l4` | `המקום` : `מקום מסחר`; `קיבל אישור מידי מי שרשאי לתתו על פי דין במדינה שבה הוא פועל` : BOOLEAN | BOOLEAN |
| `חברת חוץ` | `ic-core-company-kinds.l4` | `הגוף הוא תאגיד` : BOOLEAN; `הגוף הוא שותפות` : BOOLEAN; `הגוף התאגד מחוץ לישראל` : BOOLEAN | BOOLEAN |
| `איגרת חוב` | `ic-core-securities.l4` | `המסמך` : `עובדות על מסמך חוב` | BOOLEAN |
| `איגרת חוב מובטחת` | `ic-core-securities.l4` | `המסמך` : `עובדות על מסמך חוב` | BOOLEAN |
| `בעל איגרת חוב` | `ic-core-securities.l4` | `המסמך` : `עובדות על מסמך חוב`; `החברה היא חברת איגרות חוב` : BOOLEAN; `האדם מחזיק במסמך` : BOOLEAN | BOOLEAN |
| `סדרת איגרות חוב` | `ic-core-securities.l4` | `מספר איגרות החוב` : NUMBER; `שוות דרגה לענין ההתחייבות הכספית והערובה לתשלומה` : BOOLEAN | BOOLEAN |
| `נייר ערך` | `ic-core-securities.l4` | `הוא מניה` : BOOLEAN; `הוא איגרת חוב` : BOOLEAN; `הוא זכות לרכוש, להמיר או למכור מניה או איגרת חוב` : BOOLEAN; `הוא נייר ערך אחר שהחוק אינו מונה` : BOOLEAN | BOOLEAN |
| `מניה` | `ic-core-securities.l4` | `אגד של זכויות בחברה` : BOOLEAN; `הזכויות נקבעות בדין ובתקנון` : BOOLEAN | BOOLEAN |
| `מניות הטבה` | `ic-core-securities.l4` | `מניות שהחברה מקצה` : BOOLEAN; `ללא תמורה` : BOOLEAN; `לבעלי מניותיה הזכאים לכך` : BOOLEAN | BOOLEAN |
| `תעודת מניה` | `ic-core-securities.l4` | `מצוין בה שמו של הבעלים הרשום במרשמי החברה` : BOOLEAN; `מצוין בה מספר המניות שבבעלותו` : BOOLEAN | BOOLEAN |
| `פרמיה` | `ic-core-securities.l4` | `התמורה בעבור ההקצאה` : NUMBER; `הערך הנקוב של המניות` : NUMBER | MAYBE NUMBER |
| `משכון` | `ic-core-securities.l4` | `משכון כמשמעותו בחוק המשכון` : BOOLEAN; `שעבוד צף` : BOOLEAN | BOOLEAN |
| `אמצעי שליטה` | `ic-core-securities.l4` | `הזכות` : `זכות בחברה` | BOOLEAN |
| `דיבידנד` | `ic-core-securities.l4` | `הנתינה` : `עובדות על נתינה לבעל מניה` | BOOLEAN |
| `רכישה לענין חלוקה` | `ic-core-securities.l4` | `המעשה` : `עובדות על חלוקה` | BOOLEAN |
| `חלוקה` | `ic-core-securities.l4` | `המעשה` : `עובדות על חלוקה` | BOOLEAN |
| `הצעה פרטית` | `ic-core-securities.l4` | `ההצעה` : `עובדות על הצעה לניירות ערך` | BOOLEAN |
| `הצעה פרטית מהותית` | `ic-core-securities.l4` | `ההצעה` : `עובדות על הצעה לניירות ערך`; `מתקיים בה האמור בסעיף 270(5)` : BOOLEAN | BOOLEAN |
| `נושא משרה` | `ic-core-people.l4` | `המשרה` : `משרה` | BOOLEAN |
| `קרוב` | `ic-core-people.l4` | `הקרבה` : `קרבה` | BOOLEAN |
| `בעל מניה מהותי` | `ic-core-people.l4` | `הקשר` : `קשר לחברה` | BOOLEAN |
| `בעל ענין` | `ic-core-people.l4` | `הקשר` : `קשר לחברה` | BOOLEAN |
| `דבוקת שליטה` | `ic-core-people.l4` | `חלק מכלל זכויות ההצבעה באסיפה הכללית שהמניות מקנות` : NUMBER | BOOLEAN |
| `ענין אישי` | `ic-core-people.l4` | `העובדות` : `עובדות לענין אישי` | BOOLEAN |
| `הצבעה שנחשבת הצבעה של בעל עניין אישי` | `ic-core-people.l4` | `העובדות` : `עובדות לענין אישי`; `ההצבעה היא על פי ייפוי כוח שניתן על ידי אחר` : BOOLEAN; `לנותן ייפוי הכוח יש עניין אישי` : BOOLEAN | BOOLEAN |
| `מספר זהות` | `ic-core-people.l4` | `סוגו של האדם` : `סוג אדם`; `יש לו מספר רישום על פי דין` : BOOLEAN | MAYBE (LIST OF `פרט זיהוי`) |
| `מען` | `ic-core-people.l4` | `סוגו של האדם` : `סוג אדם`; `מסר מען אחר` : BOOLEAN; `יש לו מען רשום על פי דין` : BOOLEAN | MAYBE `סוג המען` |
| `יזם` | `ic-core-people.l4` | `עושה פעולה בשמה או במקומה של חברה` : BOOLEAN; `החברה טרם התאגדה` : BOOLEAN | BOOLEAN |
| `מענק פרישה` | `ic-core-people.l4` | `משרתו של המקבל` : `משרה`; `מענק, תשלום, גמול, פיצוי או הטבה אחרת` : BOOLEAN; `בזיקה לסיום תפקידו בחברה` : BOOLEAN | BOOLEAN |
| `תנאי כהונה והעסקה` | `ic-core-people.l4` | `משרתו של המקבל` : `משרה`; `הפריט` : `פריט בתנאי כהונה והעסקה`; `ניתן בשל כהונה או העסקה` : BOOLEAN | BOOLEAN |
| `דירקטור בלתי תלוי` | `ic-core-people.l4` | `העובדות` : `עובדות לדירקטור בלתי תלוי` | BOOLEAN |
| `אסיפה שנתית` | `ic-core-meetings.l4` | `האסיפה` : `עובדות על אסיפה` | BOOLEAN |
| `אסיפה מיוחדת` | `ic-core-meetings.l4` | `האסיפה` : `עובדות על אסיפה` | BOOLEAN |
| `אסיפה כללית` | `ic-core-meetings.l4` | `האסיפה` : `עובדות על אסיפה` | BOOLEAN |
| `אסיפת סוג` | `ic-core-meetings.l4` | `האסיפה` : `עובדות על אסיפה` | BOOLEAN |
| `מנין קולות` | `ic-core-meetings.l4` | `ההצבעה` : `הצבעה` | NUMBER |
| `נוכחות בעל מניות` | `ic-core-meetings.l4` | `בעל המניות נוכח בעצמו` : BOOLEAN; `בעל המניות נוכח באמצעות שלוח` : BOOLEAN; `בעל המניות נוכח באמצעות כתב הצבעה כאמור בסעיף 87` : BOOLEAN | BOOLEAN |
| `ועדת דירקטוריון` | `ic-core-meetings.l4` | `ועדה שהקים הדירקטוריון` : BOOLEAN; `הוקמה לפי הוראות סעיף 110` : BOOLEAN | BOOLEAN |
| `רואה חשבון מבקר` | `ic-core-meetings.l4` | `רואה חשבון` : BOOLEAN; `מונה לשם ביצוע פעולת ביקורת כאמור בסעיף 154` : BOOLEAN | BOOLEAN |
| `תעודת התאגדות` | `ic-core-meetings.l4` | `המסמך` : `מסמך שהרשם הוציא` | BOOLEAN |
| `יום ההתאגדות` | `ic-core-meetings.l4` | `המסמך` : `מסמך שהרשם הוציא` | MAYBE DATE |
| `תקנון` | `ic-core-meetings.l4` | `תקנון של חברה` : BOOLEAN; `הוגש לרשם בראשונה עם התאגדותה` : BOOLEAN; `שונה לפי דין` : BOOLEAN | BOOLEAN |
| `עסקה` | `ic-core-deals.l4` | `העסקה` : `עובדות על עסקה` | BOOLEAN |
| `עסקה חריגה` | `ic-core-deals.l4` | `העסקה` : `עובדות על עסקה` | BOOLEAN |
| `פעולה` | `ic-core-deals.l4` | `פעולה משפטית, בין במעשה ובין במחדל` : BOOLEAN | BOOLEAN |
| `פעולה מהותית` | `ic-core-deals.l4` | `פעולה משפטית, בין במעשה ובין במחדל` : BOOLEAN; `עשויה להשפיע באופן מהותי על רווחיות החברה, רכושה או התחייבויותיה` : BOOLEAN | BOOLEAN |
| `תביעה נגזרת` | `ic-core-deals.l4` | `תובענה שהגיש תובע` : BOOLEAN; `הוגשה בשם חברה` : BOOLEAN; `בשל עילת תביעה של החברה` : BOOLEAN | BOOLEAN |
| `הצעת רכש` | `ic-core-deals.l4` | `ההצעה` : `עובדות על הצעה לרכישת מניות` | BOOLEAN |
| `מציע` | `ic-core-deals.l4` | `ההצעה` : `עובדות על הצעה לרכישת מניות`; `האדם מציע את ההצעה` : BOOLEAN | BOOLEAN |
| `ניצע` | `ic-core-deals.l4` | `ההצעה` : `עובדות על הצעה לרכישת מניות`; `האדם הוא בעל מניות שמוצע לרכוש את מניותיו` : BOOLEAN | BOOLEAN |
| `חברת מטרה` | `ic-core-deals.l4` | `ההצעה` : `עובדות על הצעה לרכישת מניות`; `הצעת הרכש מופנית לבעלי מניותיה של החברה` : BOOLEAN | BOOLEAN |
| `מיזוג` | `ic-core-deals.l4` | `המיזוג` : `עובדות על מיזוג` | BOOLEAN |
| `חברת יעד` | `ic-core-deals.l4` | `עומדת להתמזג עם חברה קולטת` : BOOLEAN; `באופן שיביא לחיסולה` : BOOLEAN | BOOLEAN |
| `חברה קולטת` | `ic-core-deals.l4` | `כל נכסיה והתחייבויותיה של חברת היעד עוברים אליה במיזוג` : BOOLEAN | BOOLEAN |
| `חברה מתמזגת` | `ic-core-deals.l4` | `היא חברת יעד` : BOOLEAN; `היא חברה קולטת` : BOOLEAN | BOOLEAN |

## Coverage table

One row per provision of the range, src:1-261 (line 262 is blank): the title block and table of contents (one `inert` row), the Part heading, section 1's heading and lead-in, then one row per line of section 1's definitions, and one per paragraph where the paragraphs of a definition differ (`אמצעי שליטה`, `דירקטור בלתי תלוי`, `מספר זהות`, `מען`).
The range has one section (section 1), one Part heading, and the title block.
107 rows. Dispositions: encoded 74, fork 8, inert 23, repealed or blank in this text 2.
Every non-blank line of src:1-261 falls in the source-lines cell of some row (checked by script, see "What check.sh prints").
A row marked `fork` is encoded under one reading chosen in the fork register: `fork` marks a reading the text leaves open between two defensible alternatives that give different answers (F1 to F7). F8 to F17 are also in the register, but they are drafting defaults, or edge cases where one reading is plainly closer to the words, and their rows stay `encoded`.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| title block and table of contents (the title `חוק החברות, התשנ״ט–1999`, the citation box, the heading `תוכן עניינים` and the table of contents of 139 links) | src:1-153 | inert | nowhere (no rule) | A pure citation and title. Lines 1, 8 and 9 are structural markers of the page; line 2 is the title; lines 4-7 are the box of Sefer HaChukim references and amending Acts (links, no provision); line 11 is the heading `תוכן עניינים`; lines 13-153 are a table of contents made only of links to the Law's own headings (139 entries). Nothing in them states a condition, a right or a duty. The Law's date is not in them: the title carries only the year 5759-1999 (see "Dates"). |
| Part 1 heading `חלק ראשון: פרשנות` (Part 1: interpretation) | src:155 | inert | nowhere (no rule) | A pure title (a heading). It names Part 1, which has the single section 1. |
| section 1 heading `הגדרות` (definitions), with the list of amending years | src:157 | inert | nowhere (no rule) | A pure title (a heading) of section 1; the `תיקון:` field only lists the years of the Acts that amended it, and carries no provision. |
| section 1 lead-in `בחוק זה –` (in this Law –) | src:158 | inert | nowhere (no rule); see "Instructions to the pieces", item 3 | The lead-in only says that the definitions below apply throughout this Law. It states no condition. Its effect is a convention, not a rule: every piece reads these terms in the sense of this section, by calling the core's rules. |
| סעיף 1, ”איגרת חוב“ (bond) | src:159 | encoded | `ic-core-securities.l4`: rule `איגרת חוב` | Facts in `עובדות על מסמך חוב`; promissory notes and bills of exchange a company gives in its business are excluded. |
| סעיף 1, ”איגרת חוב מובטחת“ (secured bond) | src:160 | encoded | `ic-core-securities.l4`: rule `איגרת חוב מובטחת` | A bond whose obligation is secured by a pledge on all or some of the assets. |
| סעיף 1, ”אמצעי שליטה“ (means of control (lead-in)) | src:161 | encoded | `ic-core-securities.l4`: type `זכות בחברה` and rule `אמצעי שליטה` | True of each of the two rights listed in paragraphs (1) and (2); `זכות אחרת` stands for any other right. |
| סעיף 1, means of control, paragraph (1): the right to vote in a general meeting of a company | src:162 | encoded | `ic-core-securities.l4`: constructor `זכות ההצבעה באסיפה כללית של חברה` |  |
| סעיף 1, means of control, paragraph (2): the right to appoint a director of a company | src:163 | encoded | `ic-core-securities.l4`: constructor `הזכות למנות דירקטור של חברה` |  |
| סעיף 1, ”אסיפה כללית“ (general meeting) | src:164 | encoded | `ic-core-meetings.l4`: rule `אסיפה כללית` | An annual or a special meeting of the shareholders. |
| סעיף 1, ”אסיפה מיוחדת“ (special meeting) | src:165 | encoded | `ic-core-meetings.l4`: rule `אסיפה מיוחדת` | A general meeting of the shareholders that is not annual. Entry F12 on the circle with `אסיפה כללית`. |
| סעיף 1, ”אסיפת סוג“ (class meeting) | src:166 | encoded | `ic-core-meetings.l4`: rule `אסיפת סוג` |  |
| סעיף 1, ”אסיפה שנתית“ (annual meeting) | src:167 | encoded | `ic-core-meetings.l4`: rule `אסיפה שנתית` |  |
| סעיף 1, ”בורסה“ (bourse) | src:168 | encoded | `ic-core-company-kinds.l4`: rule `בורסה` and type `מקום מסחר` | A bourse abroad counts only if approved by whoever may approve it by law in that country; the approval is a plain input. |
| סעיף 1, ”בורסה בישראל“ (bourse in Israel) | src:169 | encoded | `ic-core-company-kinds.l4`: constructor `בורסה בישראל` of `מקום מסחר` |  |
| סעיף 1, ”בעל איגרת חוב“ (bondholder, in a bond company) | src:170 | encoded | `ic-core-securities.l4`: rule `בעל איגרת חוב` |  |
| סעיף 1, ”בית המשפט“ (the court (deleted)) | src:171 | repealed or blank in this text | `ic-core-company-kinds.l4`: stub rule `הגדרות שנמחקו מסעיף 1` | The source marks the definition deleted; section 6(d) (src:289, piece ic1) gives "the court" a meaning for sections 6 and 7. |
| סעיף 1, ”בעל מניה מהותי“ (material shareholder) | src:172 | encoded | `ic-core-people.l4`: rule `בעל מניה מהותי` | 5% or more of the issued share capital or of the voting rights; "holds" is as the Securities Law counts holding (src:182 points there), so the caller supplies the fractions (entry F13). |
| סעיף 1, ”בעל ענין“ (interested party) | src:173 | encoded | `ic-core-people.l4`: rule `בעל ענין` |  |
| סעיף 1, ”דבוקת שליטה“ (control block (shares giving 25% or more of the voting rights)) | src:174 | encoded | `ic-core-people.l4`: rule `דבוקת שליטה` |  |
| סעיף 1, ”דיבידנד“ (dividend) | src:175 | encoded | `ic-core-securities.l4`: rule `דיבידנד` | A transfer without equal consideration counts as given; bonus shares are excluded. |
| סעיף 1, ”דירקטור“ (director: a member of the board) | src:176 | encoded | `ic-core.l4`: constructor `דירקטור` of `משרה` |  |
| סעיף 1, ”דירקטור בלתי תלוי“ (independent director (lead-in)) | src:177 | fork | `ic-core-people.l4`: rule `דירקטור בלתי תלוי` | Fork F4 (what "appointed or classified as such" qualifies) and entry F14. |
| סעיף 1, independent director, condition (1): the qualifications of an external director in section 240(b) to (f), and the audit committee approved | src:178 | encoded | `ic-core-people.l4`: the inputs `מתקיימים תנאי הכשירות לפי סעיף 240(ב) עד (ו)` and `ועדת הביקורת אישרה זאת` of `עובדות לדירקטור בלתי תלוי` | Section 240 is piece ic2's; its outcome is a plain input here. The source says "(ב) עד (ו)" in src:178; this encoding uses the Law's words. |
| סעיף 1, independent director, condition (2): not more than nine consecutive years as a director, a break of up to two years not interrupting | src:179 | encoded | `ic-core-people.l4`: the input `שנות כהונה רצופות כדירקטור בחברה` (at most 9) | Entry F14: the count of years, with breaks of up to two years treated as continuous, is the caller's. |
| סעיף 1, ”דירקטור חיצוני“ (external director) | src:180 | encoded | `ic-core-people.l4`: the input `דירקטור חיצוני לפי חלק 6 פרק 1 סימן ה` of `עובדות לדירקטור בלתי תלוי` |  |
| סעיף 1, ”דמי פיגורים“; ”ריבית שקלית“ (arrears charges and shekel interest) | src:181 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Interest and Linkage Adjudication Law, 5721-1961, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. No module reads it; a piece that needs it takes a plain NUMBER input. |
| סעיף 1, ”החזקה“; ”רכישה“ (holding and acquisition (as in the Securities Law)) | src:182 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Securities Law, 5728-1968, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. Not the same as the distribution-specific "acquisition" inside src:209, which is encoded as `רכישה לענין חלוקה`. |
| סעיף 1, ”הליכי חדלות פירעון“ (insolvency proceedings) | src:183 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Insolvency and Economic Rehabilitation Law, 5778-2018, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. No module reads it; a piece that needs it takes a plain BOOLEAN input. |
| סעיף 1, ”הצעה פרטית“ (private offer) | src:184 | encoded | `ic-core-securities.l4`: rule `הצעה פרטית` | "Public offer" has its Securities Law meaning and is a plain input. |
| סעיף 1, ”הצעה פרטית מהותית“ (material private offer) | src:185 | encoded | `ic-core-securities.l4`: rule `הצעה פרטית מהותית` |  |
| סעיף 1, ”הצעת רכש“ (tender offer) | src:186 | encoded | `ic-core-deals.l4`: rule `הצעת רכש` |  |
| סעיף 1, ”ועדת דירקטוריון“ (board committee) | src:187 | encoded | `ic-core-meetings.l4`: rule `ועדת דירקטוריון` |  |
| סעיף 1, ”חבר בורסה“ (member of a bourse) | src:188 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Securities Law, 5728-1968 (section 46), which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. No module reads it. |
| סעיף 1, ”חברה“ (company) | src:189 | encoded | `ic-core-company-kinds.l4`: rule `חברה` and the core type `דין ההתאגדות` | A company is one incorporated under this Law, the Ordinance, or the 1921 or 1919 Ordinance. |
| סעיף 1, ”חברת איגרות חוב“ (bond company) | src:190 | fork | `ic-core-company-kinds.l4`: rule `חברת איגרות חוב` | Fork F1 (the scope of "and held by the public"). |
| סעיף 1, ”חברה בת“ (subsidiary) | src:191 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Securities Law, 5728-1968, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. A caller states it where a rule needs it (it is a limb of the input `רכישה או מתן מימון לרכישה …` of `עובדות על חלוקה`). |
| סעיף 1, ”חברה לרישומים“ (registration (nominee) company) | src:192 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Securities Law, 5728-1968, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. No module reads it. |
| סעיף 1, ”חברה לתועלת הציבור“ (public-benefit company) | src:193 | encoded | `ic-core.l4`: field `חברה לתועלת הציבור` of `עובדות על חברה` |  |
| סעיף 1, ”חברה ממשלתית“; ”חברת בת ממשלתית“ (government company and government subsidiary) | src:194 | encoded | `ic-core.l4`: field `חברה ממשלתית` of `עובדות על חברה` | One field for both terms; a piece that must tell a government subsidiary apart takes its own input. |
| סעיף 1, ”חברה מתמזגת“ (merging company) | src:195 | encoded | `ic-core-deals.l4`: rule `חברה מתמזגת` | A target company or an absorbing company (entry F9). |
| סעיף 1, ”חברה פרטית“ (private company) | src:196 | encoded | `ic-core-company-kinds.l4`: rule `חברה פרטית` | A company that is not public; a body that is not a company is not a private company either. |
| סעיף 1, ”חברה ציבורית“ (public company) | src:197 | fork | `ic-core-company-kinds.l4`: rule `חברה ציבורית` | Fork F1 (the scope of "and held by the public"). |
| סעיף 1, ”חברה קולטת“ (absorbing company) | src:198 | encoded | `ic-core-deals.l4`: rule `חברה קולטת` |  |
| סעיף 1, ”חברה קשורה“ (affiliated company) | src:199 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Securities Law, 5728-1968, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. No module reads it. |
| סעיף 1, ”חברת חוץ“ (foreign company) | src:200 | encoded | `ic-core-company-kinds.l4`: rule `חברת חוץ` |  |
| סעיף 1, ”חברת יעד“ (target company of a merger) | src:201 | encoded | `ic-core-deals.l4`: rule `חברת יעד` |  |
| סעיף 1, ”חברת מטרה“ (target company of a tender offer) | src:202 | encoded | `ic-core-deals.l4`: rule `חברת מטרה` |  |
| סעיף 1, ”חוק הנאמנות“ (short name of the Trust Law, 5739-1979) | src:203 | inert | nowhere (no rule) | A pure citation: the definition only gives a short name to another Law (Trust Law, 5739-1979) so that later sections can cite it briefly. It states no condition, so there is nothing to compute; no piece encodes the cited Law. |
| סעיף 1, ”חוק העמותות“ (short name of the Associations Law, 5740-1980) | src:204 | inert | nowhere (no rule) | A pure citation: the definition only gives a short name to another Law (Associations Law, 5740-1980) so that later sections can cite it briefly. It states no condition, so there is nothing to compute; no piece encodes the cited Law. |
| סעיף 1, ”חוק חדלות פירעון ושיקום כלכלי“ (short name of the Insolvency and Economic Rehabilitation Law, 5778-2018) | src:205 | inert | nowhere (no rule) | A pure citation: the definition only gives a short name to another Law (Insolvency and Economic Rehabilitation Law, 5778-2018) so that later sections can cite it briefly. It states no condition, so there is nothing to compute; no piece encodes the cited Law. |
| סעיף 1, ”חוק ניירות ערך“ (short name of the Securities Law, 5728-1968) | src:206 | inert | nowhere (no rule) | A pure citation: the definition only gives a short name to another Law (Securities Law, 5728-1968) so that later sections can cite it briefly. It states no condition, so there is nothing to compute; no piece encodes the cited Law. |
| סעיף 1, ”חוק פסיקת ריבית והצמדה“ (short name of the Interest and Linkage Adjudication Law, 5721-1961) | src:207 | inert | nowhere (no rule) | A pure citation: the definition only gives a short name to another Law (Interest and Linkage Adjudication Law, 5721-1961) so that later sections can cite it briefly. It states no condition, so there is nothing to compute; no piece encodes the cited Law. |
| סעיף 1, ”חוק תקשורת דיגיטלית עם גופים ציבוריים“ (short name of the Digital Communication with Public Bodies Law, 5778-2018) | src:208 | inert | nowhere (no rule) | A pure citation: the definition only gives a short name to another Law (Digital Communication with Public Bodies Law, 5778-2018) so that later sections can cite it briefly. It states no condition, so there is nothing to compute; no piece encodes the cited Law. |
| סעיף 1, ”חלוקה“ (distribution (with the inner definition of "acquisition")) | src:209 | fork | `ic-core-securities.l4`: rule `חלוקה` and `ic-core-securities.l4`: rule `רכישה לענין חלוקה` | Fork F3 (the scope of the proviso about the seller). The inner "acquisition" is named apart from the Securities Law's (src:182). |
| סעיף 1, ”יום ההתאגדות“ (day of incorporation) | src:210 | encoded | `ic-core-meetings.l4`: rule `יום ההתאגדות` | The date the Registrar fixed in the certificate; NOTHING for a document that is not a certificate of incorporation (entry F16). |
| סעיף 1, ”יזם“ (promoter) | src:211 | encoded | `ic-core-people.l4`: rule `יזם` |  |
| סעיף 1, ”מדד“ (index (the consumer price index)) | src:212 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Central Bureau of Statistics' consumer price index (no Law is cited), which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. A piece that needs the index takes a plain NUMBER input, in index points. |
| סעיף 1, ”מיזוג“ (merger (for Part 8)) | src:213 | encoded | `ic-core-deals.l4`: rule `מיזוג` |  |
| סעיף 1, ”מניה“ (share) | src:214 | encoded | `ic-core-securities.l4`: rule `מניה` | A bundle of rights in the company fixed by law and by the articles. |
| סעיף 1, ”מניות הטבה“ (bonus shares) | src:215 | encoded | `ic-core-securities.l4`: rule `מניות הטבה` |  |
| סעיף 1, ”מנין קולות“ (count of votes) | src:216 | fork | `ic-core-meetings.l4`: rule `מנין קולות` and the core type `הצבעה` | Fork F2 (abstentions). |
| סעיף 1, ”מספר זהות“ (identity number (lead-in)) | src:217 | encoded | `ic-core-people.l4`: rule `מספר זהות` and the core type `סוג אדם` | Returns the list of details that identify that kind of person, or NOTHING. |
| סעיף 1, identity number, paragraph (1): a company registered in Israel: the registration number | src:218 | encoded | `ic-core-people.l4`: branch `חברה הרשומה בישראל` of `מספר זהות` |  |
| סעיף 1, identity number, paragraph (2): a company registered outside Israel: the country and the registration number, if it has one | src:219 | encoded | `ic-core-people.l4`: branch `חברה הרשומה מחוץ לישראל` of `מספר זהות` | The source says "חברה רשומה הרשומה מחוץ לישראל" ("a registered company registered outside Israel"); read as a company registered outside Israel (entry F10). |
| סעיף 1, identity number, paragraph (3): another corporation that has a registration number by law | src:220 | encoded | `ic-core-people.l4`: branch `תאגיד אחר` of `מספר זהות` | A corporation with no registration number by law has no identity number under the definition: NOTHING. |
| סעיף 1, identity number, paragraph (4): an individual resident in Israel: the number in the population register | src:221 | encoded | `ic-core-people.l4`: branch `יחיד תושב ישראל` of `מספר זהות` |  |
| סעיף 1, identity number, paragraph (5): an individual not resident in Israel: the country that issued the passport and its number | src:222 | encoded | `ic-core-people.l4`: branch `יחיד שאינו תושב ישראל` of `מספר זהות` |  |
| סעיף 1, ”מען“ (address (lead-in)) | src:223 | encoded | `ic-core-people.l4`: rule `מען` and type `סוג המען` | Returns which address counts for that kind of person, or NOTHING. |
| סעיף 1, address, paragraph (1): an individual resident in Israel: the address in the population register, or the one he gave | src:224 | encoded | `ic-core-people.l4`: branch `יחיד תושב ישראל` of `מען` |  |
| סעיף 1, address, paragraph (2): an individual not resident in Israel: the residential address, or the one he gave | src:225 | encoded | `ic-core-people.l4`: branch `יחיד שאינו תושב ישראל` of `מען` |  |
| סעיף 1, address, paragraph (3): a company registered in Israel: its registered office | src:226 | encoded | `ic-core-people.l4`: branch `חברה הרשומה בישראל` of `מען` | The registered office is section 123 (piece ic2). |
| סעיף 1, address, paragraph (4): a company registered outside Israel: the address of its office abroad, or the one it gave in Israel | src:227 | encoded | `ic-core-people.l4`: branch `חברה הרשומה מחוץ לישראל` of `מען` |  |
| סעיף 1, address, paragraph (5): another corporation that has a registered address by law | src:228 | encoded | `ic-core-people.l4`: branch `תאגיד אחר` of `מען` | A corporation with no registered address by law has no address under the definition: NOTHING. |
| סעיף 1, ”מען דיגיטלי“ (digital address) | src:229 | inert | nowhere (no rule) | The definition only says that a digital address is each of the details listed in the Fourth Schedule; the Schedule is another piece's text and the definition adds no condition, so there is nothing to compute here. |
| סעיף 1, ”מענק פרישה“ (severance grant) | src:230 | encoded | `ic-core-people.l4`: rule `מענק פרישה` |  |
| סעיף 1, ”מציע“ (offeror in a tender offer) | src:231 | encoded | `ic-core-deals.l4`: rule `מציע` |  |
| סעיף 1, ”משכון“ (pledge) | src:232 | encoded | `ic-core-securities.l4`: rule `משכון` | A pledge as the Pledges Law means it (a plain input) or a floating charge. |
| סעיף 1, ”נוכחות בעל מניות“ (presence of a shareholder) | src:233 | encoded | `ic-core-meetings.l4`: rule `נוכחות בעל מניות` |  |
| סעיף 1, ”נושא משרה“ (office-holder) | src:234 | encoded | `ic-core-people.l4`: rule `נושא משרה` and the core type `משרה` |  |
| סעיף 1, ”נייר ערך“ (security) | src:235 | encoded | `ic-core-securities.l4`: rule `נייר ערך` | "Includes" leaves the list open, so the last input is the caller's word for any other security (entry F8). |
| סעיף 1, ”ניצע“ (offeree in a tender offer) | src:236 | encoded | `ic-core-deals.l4`: rule `ניצע` |  |
| סעיף 1, ”סדרת איגרות חוב“ (series of bonds) | src:237 | encoded | `ic-core-securities.l4`: rule `סדרת איגרות חוב` |  |
| סעיף 1, ”ענין אישי“ (personal interest) | src:238 | fork | `ic-core-people.l4`: rule `ענין אישי` and `ic-core-people.l4`: rule `הצבעה שנחשבת הצבעה של בעל עניין אישי` | Fork F7 (what the exclusion for share-holding applies to). |
| סעיף 1, ”עסקה“ (transaction) | src:239 | encoded | `ic-core-deals.l4`: rule `עסקה` |  |
| סעיף 1, ”עסקה חריגה“ (extraordinary transaction) | src:240 | encoded | `ic-core-deals.l4`: rule `עסקה חריגה` |  |
| סעיף 1, ”פעולה“ (act) | src:241 | encoded | `ic-core-deals.l4`: rule `פעולה` |  |
| סעיף 1, ”פעולה מהותית“ (material act) | src:242 | encoded | `ic-core-deals.l4`: rule `פעולה מהותית` |  |
| סעיף 1, ”פקודת החברות“ (short name of the Companies Ordinance [new version], 5743-1983) | src:243 | inert | nowhere (no rule) | A pure citation: the definition only gives a short name to another Law (Companies Ordinance [new version], 5743-1983) so that later sections can cite it briefly. It states no condition, so there is nothing to compute; no piece encodes the cited Law. |
| סעיף 1, ”פרמיה“ (premium) | src:244 | encoded | `ic-core-securities.l4`: rule `פרמיה` | NOTHING when the consideration does not exceed the par value (entry F11). |
| סעיף 1, ”צו לפתיחת הליכים“ (order opening proceedings) | src:245 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Insolvency and Economic Rehabilitation Law, 5778-2018, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. No module reads it. |
| סעיף 1, ”קרוב“ (relative) | src:246 | fork | `ic-core-people.l4`: rule `קרוב` and the core type `קרבה` | Fork F5 ("the spouse of each of these"). |
| סעיף 1, ”רואה חשבון מבקר“ (external auditor) | src:247 | encoded | `ic-core-meetings.l4`: rule `רואה חשבון מבקר` |  |
| סעיף 1, ”רשות ניירות ערך“ (Securities Authority) | src:248 | encoded | `ic-core.l4`: constructor `רשות ניירות ערך` of `צד` | The Authority as an actor; the definition adds no condition. |
| סעיף 1, ”רשם ההקדשות“; ”הקדש ציבורי“ (Registrar of Endowments and public endowment) | src:249 | inert | nowhere (no rule) | A pure citation: the definition only says that the term has the meaning given in the Trust Law, 5739-1979, which is not among the inputs, and it adds no condition of its own, so there is nothing to compute. No module reads it. |
| סעיף 1, ”רשם החברות“; ”הרשם“ (Registrar of Companies, the Registrar) | src:250 | encoded | `ic-core.l4`: constructor `הרשם` of `צד` | The office as an actor. |
| סעיף 1, ”שטר מניה“ (share warrant (deleted)) | src:251 | repealed or blank in this text | `ic-core-company-kinds.l4`: stub rule `הגדרות שנמחקו מסעיף 1` | The source marks the definition deleted. |
| סעיף 1, ”שעבוד צף“ (floating charge) | src:252 | encoded | `ic-core-securities.l4`: the input `שעבוד צף` of rule `משכון` | The Ordinance is not among the inputs; whether a charge is a floating charge is a plain input of `משכון`. |
| סעיף 1, ”שליטה“ (control) | src:253 | encoded | `ic-core.l4`: field `שליטה לפי חוק ניירות ערך` of `קשר לחברה` |  |
| סעיף 1, ”תאגיד מדווח“ (reporting corporation) | src:254 | encoded | `ic-core.l4`: field `תאגיד מדווח` of `עובדות על חברה` |  |
| סעיף 1, ”תביעה נגזרת“ (derivative claim) | src:255 | encoded | `ic-core-deals.l4`: rule `תביעה נגזרת` |  |
| סעיף 1, ”תזכיר“ (memorandum of association (as in the Ordinance before this Law's commencement)) | src:256 | inert | nowhere (no rule) | A pure citation: the definition only sends the reader to the Ordinance as it read before this Law began. The Ordinance is not among the inputs and the definition states no condition. |
| סעיף 1, ”תנאי כהונה והעסקה“ (terms of service and employment of an office-holder) | src:257 | fork | `ic-core-people.l4`: rule `תנאי כהונה והעסקה` and type `פריט בתנאי כהונה והעסקה` | Fork F6 (what "given by reason of such service or employment" qualifies). |
| סעיף 1, ”תעודת התאגדות“ (certificate of incorporation) | src:258 | encoded | `ic-core-meetings.l4`: rule `תעודת התאגדות` and the core type `מסמך שהרשם הוציא` |  |
| סעיף 1, ”תעודת מניה“ (share certificate) | src:259 | encoded | `ic-core-securities.l4`: rule `תעודת מניה` |  |
| סעיף 1, ”תקנון“ (articles of association) | src:260 | encoded | `ic-core-meetings.l4`: rule `תקנון` |  |
| סעיף 1, ”השר“ (the Minister (of Justice)) | src:261 | encoded | `ic-core.l4`: constructor `השר` of `צד` | The office as an actor; the Minister's powers are each piece's, as judgments handed to someone else. |

## Fork register

Each entry gives the readings seen, the one taken, and the text that licenses each reading.
No authority (a court decision, a commentary, the official text) was consulted: every entry rests on the wording of the Hebrew text deposited here and on the sections named, and each is open to a domain expert.

**F1. "And held by the public" in `חברה ציבורית` and `חברת איגרות חוב` (src:197, src:190).**
Readings: (a) the closing words qualify all three limbs (registered for trading; offered to the public under a prospectus; offered to the public abroad); (b) they qualify the last limb only.
Taken: (a). Both definitions are built alike, and the closing words follow a comma that ends the list of limbs.
Under (b), a company whose shares are only registered for trading would be public whether or not the public holds them.
Effect: a company with listed shares that the public does not hold is private (tested). The other reading is a change of the bracketing of `AND`/`OR` in two rules.

**F2. Abstentions in `מנין קולות` (src:216).**
Readings: (a) the count is the votes of those who vote, for plus against; (b) it includes the abstentions.
Taken: (a). The definition counts "המצביעים" (those who vote), and elsewhere the Law speaks of "המשתתפים בהצבעה, למעט הנמנעים" (participants in the vote, excluding abstainers, src:391), which treats abstainers as set aside.
Effect: `הצבעה` carries the abstentions in a field of their own, so a piece can apply either reading.

**F3. The proviso about the seller in `חלוקה` (src:209).**
Readings: (a) "ובלבד שהמוכר אינו החברה עצמה או תאגיד אחר בבעלותה המלאה" limits the whole definition of distribution; (b) it limits only the inner definition of "acquisition".
Taken: (b). A seller exists only in an acquisition; a dividend, or an undertaking to give one, has none. The proviso sits at the end of the inner definition, after "והכל".
Effect: a dividend is a distribution whoever receives it; a purchase from the company itself or from a wholly owned corporation is not an acquisition (tested).

**F4. "Appointed or classified as such" in `דירקטור בלתי תלוי` (src:177).**
Readings: (a) it qualifies both the external director and the individual limb; (b) it qualifies the individual limb only.
Taken: (b). Section 249ב (src:1680) lets a public company or bond company "classify a director as an independent director" if he qualifies under paragraphs (1) and (2) of this definition: classification is the step for the individual limb, and an external director is appointed under his own provisions (Part 6 chapter 1, sub-chapter E) and needs none.
Effect: an external director is an independent director with no classification (tested). Piece `ic2` encodes sections 249ב and 249ג and should confirm. The input `מונה או סווג ככזה לפי חלק 6 פרק 1` is read only for the individual limb.

**F5. "The spouse of each of these" in `קרוב` (src:246).**
Readings: (a) "בן זוגו של כל אחד מאלה" is the spouse of every person listed before it, both groups (spouse, sibling, parent, grandparent, descendant; and descendant, sibling and parent of the spouse); (b) the spouse of the first group only.
Taken: (a). "Each of these" carries no restriction and follows the whole list.
Effect: the spouse of a spouse's sibling is a relative (`בן זוג של אחד מאלה`). A caller who reads (b) gives `קרבה אחרת` for that person.

**F6. "Given by reason of such service or employment" in `תנאי כהונה והעסקה` (src:257).**
Readings: (a) it qualifies every item (exemption, insurance, indemnification, severance grant, any other benefit); (b) it qualifies only the last item, "any benefit, other payment or undertaking to pay".
Taken: (a). The participle "הניתנים" (given) is plural and follows the whole list.
Effect: an exemption or insurance given for some other reason than the office is not a term of service (tested).

**F7. The exclusion in `ענין אישי` (src:238).**
Readings: (a) "excluding a personal interest that arises from the mere holding of shares in the company" applies to each of the three interests (the person's, a relative's, another corporation's); (b) it applies to the person's own interest only.
Taken: (a). It is stated as an exclusion from the concept, after the whole list.
Effect: a relative's interest that arises only from the relative's holding of shares does not count (tested). The power-of-attorney limb reads the voter's own facts and never the giver's, as "even if the other has no personal interest" says.

**F8. "Includes" in `נייר ערך` and `תנאי כהונה והעסקה` (src:235, src:257).**
Readings: (a) the list is closed; (b) it is open, the listed things being securities (or terms) and anything else being left to the ordinary meaning.
Taken: (b), with a caller's input for the residue (phrasebook entry 2.7). A closed list would answer "no" to every security the Law does not name.
Effect: the rule is true for the listed things and for a caller's `הוא נייר ערך אחר שהחוק אינו מונה`.

**F9. "Merging company" is a target company and an absorbing company (src:195).**
Readings: (a) a company that is either; (b) the pair, the two taken together.
Taken: (a). A rule that asks about one company cannot ask about a pair.
Effect: `חברה מתמזגת` is true of a target company and of an absorbing company.

**F10. A typo in `מספר זהות`, paragraph (2) (src:219).**
The text reads "חברה רשומה הרשומה מחוץ לישראל" ("a registered company registered outside Israel").
Taken: a company registered outside Israel (the first "רשומה" is repeated by mistake or means "registered company").
Effect: none visible; the branch is `חברה הרשומה מחוץ לישראל`.

**F11. `פרמיה` when the consideration does not exceed the par value (src:244).**
Readings: (a) there is no premium (NOTHING); (b) the premium is zero.
Taken: (a). The definition is "the sum by which the consideration exceeds the par value"; when it does not exceed it, there is no such sum.
Effect: the answer is NOTHING, not 0 (tested for equal and for lower).

**F12. The circle between `אסיפה כללית` and `אסיפה מיוחדת` (src:164, src:165).**
"General meeting" is an annual or a special meeting of the shareholders, and "special meeting" is a general meeting that is not annual.
Taken: the base fact is that the meeting is a meeting of the shareholders (`אסיפה של בעלי המניות`); annual is such a meeting under section 60; special is such a meeting that is not annual; general is annual or special. A class meeting is a meeting of the holders of a class, not of the shareholders as a body.
Effect: the circle is broken without changing what any of the three says.

**F13. "Holds" in `בעל מניה מהותי` (src:172).**
"Holding" has its meaning in the Securities Law (src:182), which is not among the inputs, and may count holdings indirectly or together with others.
Taken: the caller supplies the two fractions, counted as the Securities Law counts them.
Effect: the core adds nothing to the Securities Law's way of counting.

**F14. The nine-year limb of `דירקטור בלתי תלוי` (src:179).**
"Does not serve more than nine consecutive years, and a break of up to two years does not interrupt the run."
Taken: exactly nine years is allowed (`AT MOST 9`; tested at 9 and 9.5), and the caller counts the run with breaks of up to two years treated as not interrupting it.
The first condition (src:178) points at section 240(b) to (f), which is piece `ic2`'s: a plain input.

**F15. The office in `מענק פרישה` (src:230).**
"Given to an office-holder in connection with the end of his function in the company."
Taken: the recipient is judged by the office that ended (the input `משרתו של המקבל`).
Effect: a grant to someone who was never an office-holder is not a severance grant (tested).

**F16. `יום ההתאגדות` for a document that is not a certificate of incorporation (src:210).**
Taken: NOTHING. The day is "the date the Registrar fixed as the day of incorporation in the certificate"; a document that is not signed by the Registrar or does not attest a registration fixes no such day.

**F17. `חברה ציבורית` and `חברה פרטית` are kinds of "company" (src:196, src:197).**
Both definitions begin "חברה …". A body that is not a company in the sense of src:189 (incorporated under another law) is therefore neither public nor private (tested).
A foreign company is `חברת חוץ`, a different term (src:200).

## What the stable binary does not accept

The binary is `l4` 1.6.98 (`1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`).

- **Nothing in Hebrew was rejected.** Backticked Hebrew names for types, constructors, fields and rules compile; so do rule names with ` - `, `:` and an en dash; so does an `@ref` line with the quotation marks `”…“` and `;` between locators; so does a quote line carrying `{{ח:ת|סוג=הגדרה}}` (a `|` inside the markup). `srcrefs.py check --refs` reports 0 problems on every module and `--strict` on every non-test module (the test files carry no quotations).
- **`YMD` is missing**, so `ic-core.l4` defines `YMD y m d MEANS Date d m y`. Dates built with it compare with `AT LEAST`, `GREATER THAN` and `AT MOST` (tested in `ic-core-tests-meetings.l4`).
- **`%` after a call.** `` f 25% `` reads as `(f 25)%` and gives "The argument of '%' is expected to be of type NUMBER"; write `` f (25%) ``. `` x AT LEAST 5% `` is fine.
- **A rule head may omit the parameter names.** `` `חברה ציבורית` MEANS `` after a `GIVEN` is accepted; the keel writes heads that way. The head with parameter names also compiles.
- **A type and a field of the same name compile** (the keel had `דין ההתאגדות` as both) and were renamed anyway, to keep the rule "no name in two roles".
- Not used because `main` rejects or misreads them (dialects.md): a section `GIVEN`, `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` outside `LEST BREACH`, `TYPICALLY`, `@lang`, `@nlg`, `SET OF`, `EVERY`, `WITHIN … OF THE DEADLINE`, an input named in an action, `MAY … LEST`, the ledger, `RULES EFFECTIVE DATE`, an opaque `DECLARE`, `IS INTEGER`, `WAIT UNTIL`. The keel has no regulative rule, so none of the trace-level differences applies to it.
- **The target comparison with a `main` build was not run.** `fetch-main-l4.sh` is not in this folder, so `check.sh` was run with `L4_TARGET=unstable`, as the brief says. The `l4` that ran every module is itself a `main` build (1.6.98), so the modules were compiled and evaluated by the compiler that has to read them; there is no second binary to compare with.

## What check.sh prints

Command, from this folder: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`. Output, copied as printed:

```
module                                    errors satisfied  failed  refused  expected
ic-core-company-kinds.l4                       0         0       0        0         0
ic-core-deals.l4                               0         0       0        0         0
ic-core-meetings.l4                            0         0       0        0         0
ic-core-people.l4                              0         0       0        0         0
ic-core-securities.l4                          0         0       0        0         0
ic-core-tests-company-kinds.l4                 0        27       0        0         0
ic-core-tests-deals.l4                         0        42       0        0         0
ic-core-tests-meetings.l4                      0        37       0        0         0
ic-core-tests-people.l4                        0        84       0        0         0
ic-core-tests-securities.l4                    0        66       0        0         0
ic-core.l4                                     0         0       0        0         0
TOTAL (11 modules)                             0       256       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
check.sh: the target is unstable, so the main check was skipped.
```

Assertions written equal assertions satisfied in every test file: ic-core-tests-company-kinds.l4: 27, ic-core-tests-deals.l4: 42, ic-core-tests-meetings.l4: 37, ic-core-tests-people.l4: 84, ic-core-tests-securities.l4: 66 (each count is `grep -c '^#ASSERT'`; the table above counts satisfied ones).
No module prints a `DiagnosticSeverity_Warning`, and no `@ref` is dangling (`l4 check` prints neither "is at the end of the file" nor "follows code on its line").

`srcrefs.py`, from this folder, `python3 -I srcrefs.py check --refs <the raw text> ic-core*.l4`:

```
srcrefs check: 116 src: lines, 71 runs, 84 locators, 0 problems
```

and the stricter `--strict`, over the non-test modules:

```
srcrefs check: 116 src: lines, 71 runs, 84 locators, 0 problems
```

## Open questions for a domain expert

- F1: does "and held by the public" qualify all three limbs of "public company" and "bond company"?
- F4: is an external director an independent director without classification (section 249ב, src:1680)?
- F5: is the spouse of each of the persons listed in "relative" a relative, including the spouse of a spouse's sibling?
- F6: does "given by reason of such service or employment" qualify every item of "terms of service and employment"?
- F7: does the exclusion for share-holding apply to a relative's interest and to another corporation's?
- The Wikisource text is an unofficial consolidation: has any amendment since the revision of 2026-10-12 changed section 1?

## Peeked

Nothing forbidden was opened.
One thing to disclose: the harness saved two large outputs of files I was allowed to read (`drafting-patterns.md` and `source-patterns/01-definitions-and-scope.md`) to its own spill folder under `~/.claude/projects/…/tool-results/`, and I read them there with the Read tool; they hold only that skill content.
