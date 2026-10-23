# Japan, AI Promotion Act (Act No. 53 of 2025), row `solo-2026-10`

**Not for use as advice.**
This is a draft encoding.
No domain expert and no lawyer qualified in Japan has read it against the source.
Status `draft`; human gates HG1 and HG2 not sought.

人工知能関連技術の研究開発及び活用の推進に関する法律（令和七年法律第五十三号）, in English (the Ministry of Justice's translation) "Act on Promotion of Research and Development, and Utilization of Artificial Intelligence-related Technology", promulgated 4 June 2025.

## Seat

The seat is **a business operator that develops, provides or uses AI-related technology**: the Act's 活用事業者, "utilization business operator" (Article 7).
A company or a small business owner.
Questions are phrased as that business would ask them ("Must I report …?", "Must I cooperate …?", "Can the government name me or fine me?"), with facts it can state.
Officials (the national government, the Artificial Intelligence Strategic Headquarters, the Prime Minister) have no seat; their provisions are encoded only for what they mean to the business.
Where the Act leaves a fact to an official (the day a Cabinet Order fixed; whether a request is made "under the provisions of Article 4"), the business is asked what it was told, and the answer says which reading it took.

## What is encoded, and what is not

Every Article (1 to 28) and every Supplementary Provision (1 to 4) is a row of the provisions table in `jp-ai-articles.l4`, quoted in English and Japanese, recording its addressee, its Japanese verb form, what it means for a business operator, and which searched-for mechanisms it carries (none does).
On top of that table, `jp-ai-operator.l4` encodes the provisions that speak to the business: Article 2 (the definition), Article 7 (who is an operator; its endeavor and its duty to cooperate), Article 6 (for a business that is also a research and development institute), Article 16 (the national government's research and its guidance), Article 25 (what the Headquarters may ask), and Supplementary Provisions Article 1 (commencement, with the date as an input).
The absence answers (no reporting duty, no penalty, no naming, no investigation or order power or duty to comply) are computed from the table, not written as constants.
`jp-ai-baseline.l4` asks the seat's twelve questions with `@export` and `@desc`.
Chapters III and IV are machinery (the AI Basic Plan; the Headquarters) and are `out-of-scope (machinery)` as operative rules, except Article 25, which reaches a private person; each still has its table row.
Supplementary Provisions Articles 3 and 4 amend the Act for Establishment of the Cabinet Office and are out of scope as operative rules for the same reason; they have table rows quoted from the English only.

I read all 28 Articles and all four Supplementary Provisions, in the English translation and, for every provision e-Gov carries, in the Japanese.
Where I looked for a reporting duty, a penalty, naming, or an investigation, inspection or order power affecting a private actor: every provision, row by row (the table), and by a mechanical search of both texts (the section "What the Act does not contain" below).

## Sources and edition

| id | what | status | where it came from |
| --- | --- | --- | --- |
| `ai-act-ja` | e-Gov XML of the current revision (`507AC0000000053_20250901_…`), rendered one sentence per line by `ai-act-ja-render.py` | **authoritative** | e-Gov 法令検索 law API v2, fetched 2026-10-23T23:06:17Z |
| `ai-act-ja-20250604.xml` | the earlier revision (`…_20250604_…`), deposited as evidence of the two in-force states | authoritative | same, 2026-10-23T23:12:52Z |
| `ai-act-en` | the Ministry of Justice translation, PDF and its `pdftotext -layout` text | **aid** | Japanese Law Translation Database System, fetched 2026-10-24 |

All are under `../../registers/source-bundle/`, with sha256 and provenance in the `.meta.json` files.
The Official Gazette (官報) was not consulted.

**Edition.** One text.
e-Gov records two revisions and no amending law: `20250604` (PreviousEnforced) and `20250901` (CurrentEnforced).
I fetched both XMLs and diffed them: they differ only by two insertion hunks carrying Chapters III and IV, which the earlier revision omits because they were not yet in force.
Nothing in Chapters I and II or in Supplementary Provisions Articles 1 and 2 differs.
So the encoding has one text and two in-force states, which Supplementary Provisions Article 1 explains, and which the encoding takes as a date input.
The e-Gov XML's Supplementary Provisions are an extract (`Extract="true"`): Articles 1 and 2 only.

**The translation's own metadata**, read from its history fragment on 2026-10-24: an entry dated "January 30, 2026"; "Last Version:" blank; "Translated Date: August 22, 2025"; "Dictionary Version: 18.0".
The brief's "last version date 30 Jan 2026" is the entry date; the "Last Version" field itself is empty.

**Where the text corrects the brief.** The brief's figures held: Act No. 53 of 4 June 2025; Articles 1 to 28 in four Chapters; Article 16 as the information-collection provision.
The "last version" date is as stated just above.
The secondary summary's claim that companies "will be named publicly" is not in the Act (finding 2).

## Method

The solo `encoding-a-subject` workflow, from a pinned brief, target compiler `main`.
Nouns first (`jp-ai-domain.l4`), then the provisions table (`jp-ai-articles.l4`), then the operator's rules (`jp-ai-operator.l4`), then the seat questions (`jp-ai-baseline.l4`), then tests written by hand from the source (`jp-ai-tests.l4`).
Every quotation was generated with the skill's `srcrefs.py quote`/`quoteid`, never retyped, and checked with `srcrefs.py check --strict` (output below).
The generator scripts that laid out the table and filled the quote runs are not deposited; the row values they carried are visible in `jp-ai-articles.l4`.
Identifiers are English; every row and rule carries the Japanese it rests on in a `-- src:ai-act-ja:N |` quote line, the article heading included.
A separate session then wrote `tests-independent.l4`; what it found and what changed is in "Independent test pass" below.

## Coverage table

Disposition "row" means the provision is a row of the provisions table, quoted, with its addressee, verb form, bearing on a business operator and an empty mechanism list.
"rule" means an operative rule in `jp-ai-operator.l4` as well.

| provision | heading (Japanese) | disposition | what it means for the business |
| --- | --- | --- | --- |
| Art 1 | （目的） purpose | inert; row | none |
| Art 2 | （定義） definition | encoded: row and rule | defines the technology that makes a business an operator |
| Art 3(1) to (3) | （基本理念） basic principles | inert; row | the principles Article 7 binds the business to act in accordance with |
| Art 3(4) | same | inert; row | as above; "must be taken", passive, addressee unnamed (fork F4) |
| Art 3(5) | same | inert; row | as above; Japan is to endeavor |
| Art 4(1) | （国の責務） | encoded: row; the Article 7 rule asks whether a measure is implemented under it | defines the national measures Article 7 makes the business cooperate with |
| Art 4(2) | same | row | none |
| Art 5 | （地方公共団体の責務） | encoded: row; the Article 7 rule asks whether a measure is implemented under it | defines the local measures Article 7 makes the business cooperate with |
| Art 6(1), (3) | （研究開発機関の責務等） | encoded: row and rule | endeavors, if the business is also a research and development institute (fork F6) |
| Art 6(2) | same | row | none (addressed to national and local government) |
| Art 7 | （活用事業者の責務） | encoded: row and rules | the operator definition; an endeavor; a duty to cooperate |
| Art 8 | （国民の責務） | row | none (citizens; fork F9) |
| Art 9 | （連携の強化） | row | names operators in a national coordination measure |
| Art 10 | （法制上の措置等） | row | none |
| Art 11 | （研究開発の推進等） | row | none |
| Art 12 | （施設及び設備等の整備及び共用の促進） | row | names operators as users of shared facilities |
| Art 13 | （適正性の確保） | row | the national government is to establish guidelines; no duty to follow them stated |
| Art 14 | （人材の確保等） | row | names operators as partners in human-resource measures |
| Art 15 | （教育の振興等） | row | none |
| Art 16 | （調査研究等） | encoded: row and rules | the national government analyzes rights-infringement cases and is to give guidance, advice and information |
| Art 17 | （国際協力） | row | none |
| Art 18 | Chapter III | out-of-scope (machinery); row | none |
| Arts 19 to 24 | Chapter IV | out-of-scope (machinery); rows | none |
| Art 25(1) | （資料の提出その他の協力） | encoded: row and rule | the Headquarters may request cooperation from the heads of the listed administrative bodies, local governments and agencies, and from the representatives of special corporations; a special corporation can itself be a business operator |
| Art 25(2) | same | encoded: row and rule | the Headquarters may ask any other person, so a business, for cooperation |
| Arts 26 to 28 | Chapter IV | out-of-scope (machinery); rows | none |
| Supp Art 1 | （施行期日） | encoded: row and rules | when each part takes effect |
| Supp Art 2 | （検討） review | row | none |
| Supp Art 3 | (amends the Cabinet Office Establishment Act) | out-of-scope (amends another Act); row, English only | none |
| Supp "Art 4" (two texts so numbered) | (amending items; adjustment provisions) | out-of-scope (amends or adjusts another Act); rows, English only | none |

No row is `deferred`.

## What the Act does not contain

Searched for, in every provision (the table) and by a mechanical search of both deposited texts on 2026-10-24.
Japanese counts are of `ai-act-ja.txt` (93 lines); English line numbers are of `ai-act-en.txt`, split on `\n`.

| searched for | Japanese searched | found | English searched | found |
| --- | --- | --- | --- | --- |
| a duty to report an AI incident or a case | 報告, 届出, 通知 | 0, 0, 0 | report, notif | none |
| a penalty, fine or sanction | 罰, 過料, 制裁, 違反 | 0, 0, 0, 0 | penalt, fine, sanction | none |
| naming or publication of a person | 公表, 氏名, 名称 | 公表 once (line 59, Art 18(4): the AI Basic Plan is made public); 0; 0 | name, publi | "publi" at 209 (Art 15, public relations) and 255 (Art 18(4), the Basic Plan) |
| an investigation, inspection or order | 立入, 検査, 命令, 勧告, 調査 | 0, 0, 0, 0; 調査 twice (lines 48-49, Art 16: the government's own research) | inspect, investigat, order | "order" at 189, 195 ("in order to"), 300 ("as ordered by the Prime Minister"), 340, 342, 353 ("Cabinet Order"); none to a private person |
| a duty owed by a private person | 義務, しなければならない | 義務 0; なければならない in Art 3(4) (passive), 6(2) (government), 7 (operators) | must, shall | "must" at 75 (Art 3(4)), 119-120 (Art 6(2)), 139 (Art 7); "shall" none |
| a duty to comply with a request | 求め, 依頼 | 求め at 58 (Art 18(3), the Prime Minister seeks a Cabinet decision) and 80 (Art 25(1)); 依頼 at 81 (Art 25(2)); no duty to comply attached | compl, request | "request" at 315 (Art 25(1)); "compl" none |

**Not found, in the Act as translated or in the Japanese:** any duty on a business to report an AI incident or a rights-infringement case; any penalty, fine or sanction; any provision for publishing a business's name; any investigation, inspection or order power over a private person; any duty to comply with a request.
The secondary summary's claim that companies concerned in human-rights violations "will be named publicly" has no provision behind it in this Act; it is not repeated here as law.
These statements are about this Act only; other Japanese laws, Cabinet Orders and the guidelines Article 13 contemplates were not read.

## Findings

1. **No reporting duty falls on a business under this Act.**
   The nearest provision, Article 16, runs the other way: the national government collects information and analyzes cases where citizens' rights and interests are infringed through AI used for a wrongful purpose or by an inappropriate method, and then gives guidance, advice and information.
   It addresses no duty to the business.
   Asserted (tests section 7, and the baseline question).
2. **No penalty, fine, naming, investigation or order power, or duty to comply, anywhere in the Act.**
   公表 ("make public") occurs once, in Article 18(4), and its object is the AI Basic Plan.
   Article 16's "other necessary measures" (その他の必要な措置) is undefined and does not mention naming (fork F8).
   Asserted (tests section 2).
3. **Article 7's "must cooperate" is in the Japanese, not only in the translation.**
   Article 7: 協力しなければならない ("must cooperate").
   Article 6(1), research and development institutes: 協力するよう努めるものとする ("endeavor to cooperate").
   Article 8, citizens: 協力するよう努めるものとする.
   The business operator's duty is the strongest verb the Act addresses to anyone outside government, and the Act attaches no consequence to it.
   Asserted (tests section 3).
4. **The translation renders one Japanese construction two ways.**
   Article 6(2) (努めるとともに、…配慮しなければならない) is translated "must endeavor … and must respect".
   Article 7 (努めるとともに、…協力しなければならない) is translated "is to endeavor … and must cooperate".
   The same structure, 〜に努めるとともに、〜しなければならない, gets "must endeavor" once and "is to endeavor" once; this is fork F1.
5. **The translation numbers two Supplementary Provisions "Article 4".**
   Line 375 begins "Article 4 The item (vii)-9 in paragraph (3), is amended…" (amending items that read as a continuation of Article 3), and line 391 begins "Article 4 When the date of the provisions…" (Adjustment Provisions).
   e-Gov's Japanese is an extract without Articles 3 and 4, so the numbering cannot be checked against deposited Japanese; both are rows, labelled as the translation numbers them.
6. **The translation doubles an "other" in Article 7.**
   It reads "or other persons who intend to utilize other artificial intelligence-related technology".
   The Japanese has その他の once (…提供をしようとする者その他の人工知能関連技術を事業活動において活用しようとする者); the encoding reads it as joining the two descriptions of persons (fork F2).
7. **Two-stage commencement, both stages now past.**
   Everything except Chapters III and IV took effect on promulgation, 2025-06-04 (Supplementary Provisions Article 1, main clause).
   Chapters III and IV, and Supplementary Articles 3 and 4, take effect "on the day specified by Cabinet Order within a period not exceeding three months from the date of promulgation".
   The Cabinet Order is not deposited; e-Gov's current revision carries the enforcement date 2025-09-01.
   The encoding takes the day as an input, but needs it only inside the window: from the text alone, Chapters III and IV are not in force before promulgation, need the Cabinet Order day from 2025-06-04 to 2025-09-03, and are in force from 2025-09-04, because the proviso lets the Order fix no later day (fork F11).
   A given day outside the window is flagged, not used.
   Asserted on both sides of each edge (tests section 5).
8. **Article 25 reaches a private business in both paragraphs, and states no duty to comply in either.**
   Paragraph (2): the Headquarters "may ask for necessary cooperation" (依頼することができる) from any person not listed in paragraph (1), "if it finds it particularly necessary".
   Paragraph (1) uses the stronger 求めることができる ("may request") toward the heads of relevant administrative bodies, local governments, incorporated administrative agencies and local incorporated administrative agencies (地方独立行政法人), **and the representatives of special corporations** (特殊法人の代表者).
   A special corporation is defined by how it was set up (directly by law, or by a special act of incorporation under a special law, within Article 4(1)(viii) of the Act for Establishment of the Ministry of Internal Affairs and Communications), not by what it does; nothing in that definition excludes a company, and one that uses AI in its business is an Article 7 operator too.
   I recall, without having checked it, that the Ministry of Internal Affairs and Communications' list of special corporations includes joint-stock companies set up by special statute; that list was not deposited or read.
   The first deposit called paragraph (1)'s addressees "public bodies" and gave the Article 25(1) row the bearing "none"; both were wrong, and the independent test pass caught both, the second with a failing assertion.
   Neither paragraph states a duty to comply or a consequence; whether Article 7 adds one is fork F5, asked in both paragraphs.
9. **Article 13's guidelines are the likeliest home of any incident expectations, and they are outside this Act.**
   Article 13 has the national government establish guidelines "in accordance with the purport of the international norms"; the Act states no duty to follow them.
   No guideline was fetched or read.

## Fork register

| fork | where | readings | taken | the text that licenses each |
| --- | --- | --- | --- | --- |
| F1 | Art 7, first limb | (a) the closing しなければならない governs only the cooperation limb, so the first limb is a bare endeavor (努める); (b) it distributes over both limbs: "must endeavor" | (a), as the translation renders Art 7 | 努めるとともに、…協力しなければならない (ja:30); the translation renders the same construction in Art 6(2) as reading (b) (en 117-122). The answer is unaffected: neither reading attaches a consequence. |
| F2 | Art 7, who is an operator | (a) その他の makes the developer/provider an instance of "persons who intend to use AI-related technology in business activities"; (b) two separate classes, with a second "other" qualifying the technology as the translation has it | (a); both limbs are asked and either makes an operator, so (a) and (b) give the same answers here | ja:30; en 133-136 |
| F2b | Art 7, "intends to" (しようとする) | (a) includes a business already doing it; (b) only one about to start | (a); the business is asked "do you, or do you intend to" | ja:30; en 133-135 |
| F3 | Art 2, what AI-related technology covers | the definition's two limbs are open-textured (does a rules engine "substitute intellectual abilities relating to … inference and judgement"?) | asked as two facts; not decided | ja:13; en 35-39 |
| F4 | Art 3(4), "must be implemented" | (a) addressed to whoever implements 施策, i.e. the national and local governments; (b) a duty on every developer and user to ensure transparency | (a); recorded as a principle, no rule | 必要な施策が講じられなければならない (ja:18): 施策 is the Act's word for government measures (Arts 4, 5, 6(1), 7, 8) |
| F5 | Art 25(1) and (2) with Art 7 | (a) a Headquarters request is a measure "implemented by the national government under the provisions of Article 4", so Art 7 makes cooperation a duty; (b) Art 25 is a separate power with no duty attached | neither decided: the business states whether the request was made as an Article 4 measure, and the answer names which reading it applied. Asked in paragraph (1) too, for a special corporation that is also an operator (the first deposit asked it only in paragraph (2); the independent test pass caught that) | ja:30, ja:80, ja:81; en 139-142, 313-331 |
| F6 | Art 6(1), "other institutes" (その他の…機関) | (a) a company doing AI research and development is an institute; (b) only universities, research and development corporations and similar bodies | asked as a fact | ja:26; en 106-110 |
| F7 | whether a statement of duty is enforceable | (a) "must cooperate" with no sanction is a duty in name only; (b) it may still matter, e.g. to an administrative body's guidance or a court's reading of other law | not decided; every answer says "the Act states no sanction", which is what the text shows | the whole Act (What the Act does not contain) |
| F8 | Art 16, "other necessary measures" (その他の必要な措置) | (a) open-ended, could include publishing names; (b) read with "guidance, advice, information", does not reach naming | not decided; the naming answer says "no provision of this Act provides for" it, not "the government cannot" | ja:49; en 225-227 |
| F9 | Art 8, citizens (国民) | (a) natural persons only; (b) includes a company | (a); Art 8 gets no rule for the business seat | ja:32; en 144-149 |
| F10 | promulgation date | the date in the Act's citation is its promulgation date | taken; e-Gov's register (`promulgation_date` 2025-06-04) and the XML attributes agree | en 5; ai-act-ja.meta.json |
| F11 | Supp Art 1 proviso, after the window closes, with no Cabinet Order day given | (a) the window binds the day, so once it has closed Chapters III and IV are in force whatever the Order says; (b) the Order is the trigger, so without its day the text cannot say, even after the window. And the window's last day: counting promulgation day as day one, as 起算して does, three months end on **2025-09-03**; leaving the first day out, on **2025-09-04** | (a), at the coordinator's direction, with the later day, 2025-09-04, as the cut, so that "in force" from that day holds on either count; a given day of 2025-09-04 is accepted, not flagged. A given day before promulgation or after 2025-09-04 is flagged, and the flag wins even on a date before promulgation (assumed, not ruled). On the facts the readings do not part: e-Gov records 2025-09-01, inside the window | 公布の日から起算して三月を超えない範囲内において政令で定める日 (ja:91); en 348-354; egov-law-revisions.json |
| F12 | Art 8, how far 努めるものとする reaches | (a) it governs both limbs: citizens are to endeavor to deepen their understanding and to cooperate, as the translation renders it; (b) it governs only the cooperation limb, and 深める is a bare "is to" | the verb-form label follows (b), the same choice F1 makes for Art 7; no answer for the business turns on it, because Art 8 is addressed to citizens (国民) | 深めるとともに、…協力するよう努めるものとする (ja:32); en 145-149 |

The English verb forms are the translator's choice; every one encoded was checked against the Japanese.
Verb-form register:

| provision | Japanese | translation | encoded as |
| --- | --- | --- | --- |
| Art 3(1)-(3), 4(2), 9-17, 18, Supp 2 | ものとする | "is to" / "is to be" | `is to (ものとする)` |
| Art 3(4) | 講じられなければならない (passive) | "must be implemented" | `measures must be taken, in the passive` |
| Art 3(5), 6(3) | 努めるものとする | "is to endeavor" | `is to endeavor` |
| Art 4(1), 5 | 責務を有する | "is responsible for" | `is responsible for` |
| Art 6(1) | 努めるとともに、協力するよう努めるものとする | "are to endeavor … as well as endeavor to cooperate" | `is to endeavor, and is to endeavor to cooperate` |
| Art 6(2) | 努めるとともに、配慮しなければならない | "must endeavor … and must respect … and give due consideration" | `endeavor, and must give due consideration` |
| Art 7 | 努めるとともに、協力しなければならない | "is to endeavor … and must cooperate" | `endeavor, and must cooperate` |
| Art 8 | 深めるとともに、協力するよう努めるものとする | "are to endeavor to deepen … and to cooperate" | `deepens, and is to endeavor to cooperate` |
| Art 25(1) | 求めることができる | "may request" | `may request` |
| Art 25(2) | 依頼することができる | "may ask for" | `may ask for` |

## Answer table: the reporting clocks

| question | answer | provision |
| --- | --- | --- |
| Must a business report an AI incident or a rights-infringement case? | No duty is stated | every row (none carries one); Art 16 is the government's own analysis |
| To whom? By when? In what form? | No recipient, no period, no form is stated | none |
| What if it does not? | No consequence is stated | none |
| Must it cooperate with a national or local measure? | "Must cooperate" (協力しなければならない), no sanction stated | Art 7 |
| Must it answer a Headquarters request? | The Headquarters "may ask" (依頼, paragraph (2)), or for a special corporation "may request" (求める, paragraph (1)); Art 25 states no duty to comply; Art 7 may apply if the request is an Art 4 measure (fork F5) | Art 25(1), (2), Art 7 |
| From when? | 2025-06-04 for Arts 1-17; Chapters III-IV from the Cabinet Order day (e-Gov: 2025-09-01; an input here), and in any case from 2025-09-04, when the proviso's window has closed (fork F11) | Supp Art 1 |

## Checks

Target compiler: `main`.
The `l4` used for every run: `L4=/Users/mengwong/.cache/l4-main/99/l4`, whose `--version` prints `1.6.99 (main, 6cc2c91, 2026-10-21)`; `JL4_LIBRARY_PATH` unset.
`check.sh` compared it with the main build `fetch-main-l4.sh` supplied, the same build.

```
$ L4=/Users/mengwong/.cache/l4-main/99/l4 ./check.sh
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.99 (main, 6cc2c91, 2026-10-21)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
jp-ai-articles.l4                              0         0       0        0         0 |      0         0       0        0  same
jp-ai-baseline.l4                              0         0       0        0         0 |      0         0       0        0  same
jp-ai-domain.l4                                0         0       0        0         0 |      0         0       0        0  same
jp-ai-operator.l4                              0         0       0        0         0 |      0         0       0        0  same
jp-ai-tests.l4                                 0       125       0        0         0 |      0       125       0        0  same
tests-independent.l4                           0       123       0        0         0 |      0       123       0        0  same
TOTAL (6 modules)                              0       248       0        0           |      0       248       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`check.sh` exit status 0, run 2026-10-24 after the independent-pass fixes.
`jp-ai-tests.l4` has 125 `#ASSERT` lines and 125 were satisfied; `tests-independent.l4` has 123 and 123 were satisfied; no assertion is expected to fail, so `encoding.json` has no `expected_red`.
No warnings: `l4 check` on every module printed no `Warning`, no "is at the end of the file" and no "follows code on its line".

```
$ python3 -I srcrefs.py check --strict ../../registers/source-bundle/ai-act-en.txt *.l4
srcrefs check: 462 src: lines, 102 runs, 104 locators, 0 problems
```

(`srcrefs.py` is the encoding-a-subject skill's copy, from `legalese/l4-ide` at `a27a409a4`.
The new constant for the end of the proviso's window carries a text-only `@ref`, so the locator count did not move.)

What the checks do not show: that a row's addressee, verb form or empty mechanism list is right (a person holding the text checks that, row by row); that a locator names the right provision; that the encoding means what the text says.

## Tests

`jp-ai-tests.l4`, 125 assertions, expected values written by hand from the deposited text (104 in the first deposit; 21 added with the independent-pass fixes, and two existing ones changed, as recorded below):

1. coverage: every Article 1-28 and Supplementary Provision 1-4 has a row; 41 rows; no Article 29;
2. the absences: no row carries any searched mechanism, and the penalty, naming and orders answers say so;
3. the verb forms of Articles 3(4), 6(1), 6(2), 7, 8, 25(1) and 25(2), and that Article 7's differs from Article 6(1)'s and Article 8's;
4. whom the Act addresses: Article 7 is the only provision addressed to operators; the bearings of Articles 4(1), 5, 9, 12, 13, 14, 16, 25(1) and 25(2);
5. commencement on both sides of 2025-06-04 and of a given Cabinet Order day; with no day given, inside the window (2025-06-04, 2025-07-01, 2025-09-03) and after it (2025-09-04, 2025-10-01, 2026-10-24); a given day after the window or before promulgation flagged, also on a date before promulgation; the window's own ends (2025-06-04, 2025-09-04) accepted;
6. Article 2's two limbs, and who is an operator;
7. the "no reporting duty on me" case, for an Article 16 case and two cases that are not, on both sides of promulgation; and a **synthetic row, labelled in its name as not in the Act**, that carries a reporting duty and a penalty and turns those two answers over while leaving naming and orders alone, so the absence answers are shown to be read from the table;
8. "must I cooperate with a national-government measure?", exactly as Article 7's verb allows, for national and local measures, a measure under some other law, a non-operator and a non-AI technology;
9. Article 7's endeavor and Article 6 for a business that is also an institute;
10. Article 16;
11. Article 25, for each answer it can give, including a special corporation that is an operator and one that is not, a request made as an Article 4 measure, no day given inside and after the window, and a given day outside it;
12. every baseline question called with plain inputs, including a Cabinet Order day outside the window and a special corporation answering through the plain inputs.

`tests-independent.l4`, 123 assertions, by a separate session (next section).

## Independent test pass

**Method.**
A separate session, which had not seen this encoding being built, read the deposited sources whole (`ai-act-ja.txt`, `ai-act-en.txt`, both XML vintages, the e-Gov metadata) and wrote its answers to the seat's questions in `tests-independent-answers-first.md` before, by its own account, opening anything in this folder.
It then read the encoding only to learn its names, wrote `tests-independent.l4` (123 assertions), and marked each assertion it expected to fail with a comment naming the provision and the reading behind it.
This encoding did not edit `tests-independent.l4`; the fixes below are to the encoding, and that file is as its author left it.
So its comments marked "EXPECTED TO FAIL (finding)" describe the first deposit; the assertions under them now pass.
The author was a model session, not a person qualified in Japanese law, so the pass checks this encoding against a second reading of the same text, not against an authority.

**Before.**
Against the first deposit (local commit `01a0bc0d8`, never pushed; the commit that adds this pass amends it), with the same `l4` (`1.6.99 (main, 6cc2c91, 2026-10-21)`): 123 assertions, **119 satisfied, 4 failed**, at `tests-independent.l4` lines 268, 272, 305 and 306.
I reproduced the author's count myself before changing anything.
Each failure was checked against the Japanese before it was fixed, and all four were encoding errors:

| line | what it asserts | the text | fix |
| --- | --- | --- | --- |
| 268 | a special corporation that uses AI, told a Headquarters request is an Art 4 measure, gets a different answer from one not told so | Art 25(1) reaches 特殊法人…の代表者 (ja:80); Art 7's 活用事業者 is anyone who uses the technology in business (ja:30), so a special corporation can be both | the Art 25 rule asks fork F5 in paragraph (1) as it already did in (2): a new answer, "(Article 25(1)); and if the request is an Article 4 measure, Article 7 says I must cooperate" |
| 272 | the Art 25(1) row's bearing is not "none: not addressed to a business operator" | as above | a new bearing, "the Headquarters may request cooperation from the representative of a special corporation, which can itself be a business operator" |
| 305, 306 | with no Cabinet Order day given, Chapters III and IV are in force on 2025-09-04 and on 2026-10-24 | 公布の日から起算して三月を超えない範囲内 (ja:91) caps the day | commencement is three-valued from the text alone (fork F11): not in force before promulgation; the day is needed from 2025-06-04 to 2025-09-03; in force from 2025-09-04. A given day outside the window is now flagged instead of being used silently |

Two of my own assertions encoded the old commencement reading and were changed with it: `jp-ai-tests.l4` had 2025-10-01 and 2026-01-01, with no day given, answering "that day was not given".

The tester also noted three things no assertion failed on, and each is fixed: Finding 8 called paragraph (1)'s addressees "public bodies", though they include special corporations; the domain field for paragraph (1)'s list omits local incorporated administrative agencies (地方独立行政法人); and Article 8's 努める scope was not recorded as a fork (now F12).
The field's name is kept, because `tests-independent.l4` uses it in its fixtures; a comment in `jp-ai-domain.l4` and the baseline question's `@desc` give the full list.
The baseline input once called `we are a public body listed in Article 25(1)` is now `Article 25(1) lists us`.

**After.**
`tests-independent.l4`: 123 assertions, **123 satisfied, 0 failed**; `jp-ai-tests.l4`: 125 satisfied; `check.sh` exit 0 (output under Checks).

**Negative control.**
The four failures show the independent suite can go red on this encoding.
To show the new commencement cut is pinned, I moved `the last day the Cabinet Order could fix` one day each way, ran both test files, and restored it:

- to 2025-09-03: `jp-ai-tests.l4` lines 213, 225 and 226 failed (2025-09-03 with no day given; and a given day of 2025-09-04, asked about on 2025-09-03 and on 2025-09-04, which the moved cut flags); `tests-independent.l4` stayed at 123 satisfied, so on this side the cut is held by my tests alone;
- to 2025-09-05: `jp-ai-tests.l4` line 215 (2025-09-04 with no day) and `tests-independent.l4` line 305 failed.

The absence answers have their own control, the synthetic row in `jp-ai-tests.l4` section 7.

## Open questions for a domain expert

- Does 協力しなければならない in Article 7 create any legal effect for a business (for example through administrative guidance or a court's reading of other law), given the Act attaches no sanction? (F7)
- Is a request from the Headquarters under Article 25 a measure "under the provisions of Article 4" for the purpose of Article 7? (F5)
- If a Cabinet Order fixing a day "within a period not exceeding three months" were never made, would the provisions take effect when the period ends, and on which count does 起算して end it, 2025-09-03 or 2025-09-04? (F11; moot on the facts, since e-Gov records 2025-09-01.)
- Is a private company that researches and develops AI one of Article 6's "other institutes"? (F6)
- Do the guidelines made under Article 13, or the AI Basic Plan under Article 18, contain incident-reporting expectations? They are outside this Act and were not read.
- The translation's numbering of the Supplementary Provisions (finding 5) and its rendering of Article 7 (findings 4 and 6) should be checked against the Official Gazette text.

## Before this is worth relying on

- An independent test pass has been done (above), but by a model session reading the same deposited text; it is not a review.
- A reader qualified in Japanese law checks every row of `jp-ai-articles.l4` against the Japanese, especially the empty mechanism lists, and rules on forks F1, F5, F7, F8 and F11.
- The Cabinet Order fixing the commencement of Chapters III and IV is deposited and its day replaces the input.
- The Official Gazette text of the Supplementary Provisions is deposited, so that Articles 3 and 4 can be read in Japanese.
