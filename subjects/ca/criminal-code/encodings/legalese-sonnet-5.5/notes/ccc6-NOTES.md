# NOTES.md (ccc6): the Criminal Code of Canada, Part V, ss 150 to 182 (sexual offences, public morals and disorderly conduct)

Source: R.S.C., 1985, c. C-46, lines 2990-3518 of `inputs/R.S.C.-1985-c.-C-46.txt` (a plain-text rendering of the Justice Laws Website consolidation, reproduced under the Open Government Licence - Canada; `inputs/SOURCES.md` records its origin and hashes).
**The text is a plain-text rendering made by a converter script. It is not the official text, and nothing here is "verified against the official text".**

Status (2026-11-16, checked in this session): layer 1 (15 modules, 14 test modules and `ccc6-tests-support.l4`), the seat (`ccc6-seat.l4`, 175 questions) and its cases (`ccc6-cases-seat.l4`, 331 assertions) run clean on 1.6.110 and on 1.6.109; the numbers are the output of `check.sh` printed in the last section. `srcrefs.py check --refs` and `--strict` report 0 problems over every `ccc6-*.l4` file, and the kind lint (every `FALSE-kind` and `NOTHING-kind` comment carries one quoted fragment that is in the text) reports none missing and none not found.
Each claim of this document that names a line of the text was read from the text in this session. The coverage table, the sweep lists (checked against the function names in the tree), the relations, the marginal-readings tables, the seat list and the audit counts are computed from the tree by `work/mknotes.py` when this file is written; the prose of the fork register, the findings and the binary limits was written by hand, with the text lines it cites checked against the text.

## Coverage (ccc6)

One row per heading, section, subsection, paragraph and defined term of lines 2990-3518 (subparagraphs and continuation lines fold into the row they belong to). The rows were produced by `work/covrows.py` from the text, and `work/mknotes.py` checked that **every one of the 523 non-blank lines of the range (11074 words) falls in exactly one row**.

Audit counts: text units counted 345 (523 non-blank lines); rows in the table before the audit 345, after the audit 345 (the table is generated from the text, so the audit changed no row); every `encoded by` name was checked to be defined in the layer-1 modules.

| disposition | rows |
| --- | --- |
| encoded | 231 |
| fork | 87 |
| inert | 8 |
| repealed or blank in this text | 19 |
| total | 345 |

Inert rows by reason: inert (reason 1: not operative): 8. The brief's three reasons are 1 not operative (title, enacting words, headings), 2 machinery (commencement, staffing, regulation-making powers, savings, amendments of other Acts) and 3 text shown repealed or blank; this part uses reason 1 for its 8 inert rows and none for 2, and the rows that reason 3 would cover carry the disposition `repealed or blank in this text` (19 rows).

A row marked `fork` is encoded and has a line in the fork register below; a row is `fork` when its tags include any of F5 to F19, and stays `encoded` when its tags are only F1 to F4, which apply to every offence, bar and defence of the part and are listed in the register with their rows. So 231 and 87 are not a count of ambiguous provisions. The `asserts` column counts the layer-1 assertions that name one of the row's functions.

| row | text lines | text (first words) | disposition | encoded by | readings and tags | asserts |
| --- | --- | --- | --- | --- | --- | --- |
| heading: PART V | 2990-2990 | PART V Sexual Offences, Public Morals and Disorderly Conduct | inert (reason 1: not operative) | - | heading | - |
| heading: Interpretation | 2992-2992 | Interpretation | inert (reason 1: not operative) | - | heading | - |
| s 150 | 2993-2994 | Definitions 150 In this Part, | inert (reason 1: not operative) | - | the enacting words "In this Part," and the marginal note; they scope the four definitions below | - |
| s 150 "guardian" | 2995-2995 | guardian includes any person who has in law or in fact the custody or ... | encoded | `s 150 guardian` | includes: NOTHING outside the list | 4 |
| s 150 "public place" | 2996-2996 | public place includes any place to which the public have access as of ... | encoded | `s 150 public place` | includes | 5 |
| s 150 "sexual organs" | 2997-2997 | sexual organs includes genital organs, breasts that are or appear to b... | encoded | `s 150 sexual organs` | includes | 5 |
| s 150 "theatre" | 2998-2998 | theatre includes any place that is open to the public where entertainm... | encoded | `s 150 theatre` | includes | 4 |
| heading: Sexual Offences | 3000-3000 | Sexual Offences | inert (reason 1: not operative) | - | heading | - |
| s 150.1(1) | 3001-3002 | Consent no defence 150.1 (1) Subject to subsections (2) to (2.2), when... | fork | `s 150.1(1) it is not a defence that the complainant consented`<br>`s 150.1(1) the offence is under section 151 or 152 or subsection 153(1), 160(3) or 173(2)`<br>`s 150.1(1) the offence is under section 271, 272 or 273`<br>`s 150.1 whether it is a defence that the complainant consented` | F2, F5, F7 | 25 |
| s 150.1(2) | 3003-3004 | Exception — complainant aged 12 or 13 (2) When an accused is charged w... | fork | `s 150.1(2) it is a defence that the complainant consented, complainant aged 12 or 13`<br>`s 150.1(2) the offence is under section 151 or 152, subsection 173(2) or section 271` | F3, F8 | 13 |
| s 150.1(2)(a) | 3005-3005 | (a) is less than two years older than the complainant; and | fork | `s 150.1(2) it is a defence that the complainant consented, complainant aged 12 or 13` | F8 | 13 |
| s 150.1(2)(b) | 3006-3006 | (b) is not in a position of trust or authority towards the complainant... | encoded | `s 150.1(2)(b) the accused is in none of the three relationships` | F3 | 0 |
| s 150.1(2.1) | 3007-3008 | Exception — complainant aged 14 or 15 (2.1) If an accused is charged w... | fork | `s 150.1(2.1) it is a defence that the complainant consented, complainant aged 14 or 15`<br>`s 150.1(2.1) the offence is under section 151 or 152, subsection 173(2) or section 271` | F3, F8 | 8 |
| s 150.1(2.1)(a) | 3009-3009 | (a) is less than five years older than the complainant; and | fork | `s 150.1(2.1) it is a defence that the complainant consented, complainant aged 14 or 15` | F8 | 8 |
| s 150.1(2.1)(b) | 3010-3010 | (b) is not in a position of trust or authority towards the complainant... | encoded | `s 150.1(2)(b) the accused is in none of the three relationships` | F3 | 0 |
| s 150.1(2.2) | 3011-3012 | Exception for transitional purposes (2.2) When the accused referred to... | encoded | `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or more years older`<br>`s 150.1(2.2) the charge is one that subsection (2.2) speaks to` | F3 | 11 |
| s 150.1(2.2)(a) | 3013-3013 | (a) the accused is the common-law partner of the complainant, or has b... | encoded | `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or more years older` | F3 | 11 |
| s 150.1(2.2)(b) | 3014-3014 | (b) the accused is not in a position of trust or authority towards the... | encoded | `s 150.1(2)(b) the accused is in none of the three relationships` | F3 | 0 |
| s 150.1(2.3) | 3015-3016 | Exception for transitional purposes (2.3) If, immediately before the d... | fork | `s 150.1(2.3) it is a defence that the complainant consented, the accused being married to the complainant`<br>`s 150.1 whether it is a defence that the complainant consented` | F7 | 10 |
| s 150.1(3) | 3017-3018 | Exemption for accused aged twelve or thirteen (3) No person aged twelv... | encoded | `s 150.1(3) no person aged twelve or thirteen shall be tried: the bar applies`<br>`s 150.1(3) the offence is under section 151 or 152 or subsection 173(2)` | F2, F4 | 9 |
| s 150.1(4) | 3019-3020 | Mistake of age (4) It is not a defence to a charge under section 151 o... | encoded | `s 150.1(4) the belief that the complainant was 16 or more is not a defence: the bar applies`<br>`s 150.1(4) the offence is under section 151 or 152, subsection 160(3) or 173(2), or section 271, 272 or 273` | F2, F4 | 6 |
| s 150.1(5) | 3021-3022 | Idem (5) It is not a defence to a charge under section 153, 170, 171, ... | encoded | `s 150.1(5) the belief that the complainant was 18 or more is not a defence: the bar applies`<br>`s 150.1(5) the offence is under section 153, 170, 171, 172 or 279.011 or subsection 279.02(2), 279.03(2), 286.1(2), 286.2(2) or 286.3(2)` | F2, F4 | 14 |
| s 150.1(6) | 3023-3024 | Mistake of age (6) An accused cannot raise a mistaken belief in the ag... | encoded | `s 150.1(6) the accused cannot raise a mistaken belief in the age of the complainant to invoke subsection (2) or (2.1): the bar applies` | F4 | 4 |
| s 151 | 3025-3026 | Sexual interference 151 Every person who, for a sexual purpose, touche... | encoded | `s 151 the conduct is sexual interference`<br>`s 151 the class of the offence` | F1 | 7 |
| s 151(a) | 3027-3027 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 151(a) the punishment on indictment` | - | 1 |
| s 151(b) | 3028-3028 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 151(b) the punishment on summary conviction` | - | 1 |
| s 152(1) | 3029-3030 | Invitation to sexual touching or exposure 152 (1) Every person commits... | encoded | `s 152(1) the conduct is the offence of invitation to sexual touching or exposure` | F1 | 6 |
| s 152(1)(a) | 3031-3031 | (a) touch, directly or indirectly, with a part of the body or with an ... | encoded | `s 152(1) the conduct is the offence of invitation to sexual touching or exposure` | F1 | 6 |
| s 152(1)(b) | 3032-3032 | (b) expose their own sexual organs. | encoded | `s 152(1) the conduct is the offence of invitation to sexual touching or exposure` | F1 | 6 |
| s 152(2) | 3033-3034 | Punishment (2) Every person who commits an offence under subsection (1... | encoded | `s 152 the class of the offence` | - | 1 |
| s 152(2)(a) | 3035-3035 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 152(2)(a) the punishment on indictment` | - | 1 |
| s 152(2)(b) | 3036-3036 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 152(2)(b) the punishment on summary conviction` | - | 1 |
| s 153(1) | 3037-3038 | Sexual exploitation 153 (1) Every person commits an offence who is in ... | encoded | `s 153(1) the conduct is the offence of sexual exploitation` | F1 | 7 |
| s 153(1)(a) | 3039-3039 | (a) for a sexual purpose, touches, directly or indirectly, with a part... | encoded | `s 153(1) the conduct is the offence of sexual exploitation` | F1 | 7 |
| s 153(1)(b) | 3040-3040 | (b) for a sexual purpose, invites, counsels or incites a young person ... | encoded | `s 153(1) the conduct is the offence of sexual exploitation` | F1 | 7 |
| s 153(1)(c) | 3041-3041 | (c) for a sexual purpose, invites, counsels or incites the young perso... | encoded | `s 153(1) the conduct is the offence of sexual exploitation` | F1 | 7 |
| s 153(1.1) | 3042-3043 | Punishment (1.1) Every person who commits an offence under subsection ... | encoded | `s 153 the class of the offence` | - | 1 |
| s 153(1.1)(a) | 3044-3044 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 153(1.1)(a) the punishment on indictment` | - | 1 |
| s 153(1.1)(b) | 3045-3045 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 153(1.1)(b) the punishment on summary conviction` | - | 1 |
| s 153(1.2) | 3046-3047 | Inference of sexual exploitation (1.2) A judge may infer that a person... | fork | `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young person` | F15; F19 | 6 |
| s 153(1.2)(a) | 3048-3048 | (a) the age of the young person; | fork | `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young person` | F15; F19 | 6 |
| s 153(1.2)(b) | 3049-3049 | (b) the age difference between the person and the young person; | fork | `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young person` | F15; F19 | 6 |
| s 153(1.2)(c) | 3050-3050 | (c) the evolution of the relationship; and | fork | `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young person` | F15; F19 | 6 |
| s 153(1.2)(d) | 3051-3051 | (d) the degree of control or influence by the person over the young pe... | fork | `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young person` | F15; F19 | 6 |
| s 153(2) | 3052-3053 | Definition of young person (2) In this section, young person means a p... | encoded | `s 153(2) young person` | means: JUST FALSE outside | 4 |
| s 153.1(1) | 3054-3055 | Sexual exploitation of person with disability 153.1 (1) Every person c... | encoded | `s 153.1(1) the conduct is the offence of sexual exploitation of a person with a disability` | F1 | 7 |
| s 153.1(1)(a) | 3056-3056 | (a) touch their own body, the body of the person who so counsels or in... | encoded | `s 153.1(1) the conduct is the offence of sexual exploitation of a person with a disability` | F1 | 7 |
| s 153.1(1)(b) | 3057-3057 | (b) expose their own sexual organs. | encoded | `s 153.1(1) the conduct is the offence of sexual exploitation of a person with a disability` | F1 | 7 |
| s 153.1(1.1) | 3058-3059 | Punishment (1.1) Every person who commits an offence under subsection ... | encoded | `s 153.1 the class of the offence` | - | 1 |
| s 153.1(1.1)(a) | 3060-3060 | (a) an indictable offence and liable to imprisonment for a term not ex... | encoded | `s 153.1(1.1)(a) the punishment on indictment` | - | 1 |
| s 153.1(1.1)(b) | 3061-3061 | (b) an offence punishable on summary conviction. | encoded | `s 153.1(1.1)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 2 |
| s 153.1(2) | 3062-3063 | Definition of consent (2) Subject to subsection (3), consent means, fo... | encoded | `s 153.1(2) consent` | - | 6 |
| s 153.1(2.1) | 3064-3065 | Consent (2.1) Consent must be present at the time the sexual activity ... | encoded | `s 153.1(2) consent` | the same function: "Consent must be present at the time" | 6 |
| s 153.1(2.2) | 3066-3067 | Question of law (2.2) The question of whether no consent is obtained u... | encoded | `s 153.1(2.2) the question is a question of law` | - | 2 |
| s 153.1(3) | 3068-3069 | When no consent obtained (3) For the purposes of this section, no cons... | encoded | `s 153.1(3) no consent is obtained` | list not closed (subsection (4)) | 8 |
| s 153.1(3)(a) | 3070-3070 | (a) the agreement is expressed by the words or conduct of a person oth... | encoded | `s 153.1(3) no consent is obtained` | list not closed (subsection (4)) | 8 |
| s 153.1(3)(a.1) | 3071-3071 | (a.1) the complainant is unconscious; | encoded | `s 153.1(3) no consent is obtained` | list not closed (subsection (4)) | 8 |
| s 153.1(3)(b) | 3072-3072 | (b) the complainant is incapable of consenting to the activity for any... | encoded | `s 153.1(3) no consent is obtained` | list not closed (subsection (4)) | 8 |
| s 153.1(3)(c) | 3073-3073 | (c) the accused counsels or incites the complainant to engage in the a... | encoded | `s 153.1(3) no consent is obtained` | list not closed (subsection (4)) | 8 |
| s 153.1(3)(d) | 3074-3074 | (d) the complainant expresses, by words or conduct, a lack of agreemen... | encoded | `s 153.1(3) no consent is obtained` | list not closed (subsection (4)) | 8 |
| s 153.1(3)(e) | 3075-3075 | (e) the complainant, having consented to engage in sexual activity, ex... | encoded | `s 153.1(3) no consent is obtained` | list not closed (subsection (4)) | 8 |
| s 153.1(4) | 3076-3077 | Subsection (3) not limiting (4) Nothing in subsection (3) shall be con... | encoded | `s 153.1(4) subsection (3) limits the circumstances in which no consent is obtained` | - | 1 |
| s 153.1(5) | 3078-3079 | When belief in consent not a defence (5) It is not a defence to a char... | encoded | `s 153.1(5) the belief that the complainant consented is not a defence: the bar applies` | F3 | 7 |
| s 153.1(5)(a) | 3080-3083 | (a) the accused’s belief arose from (i) the accused’s self-induced int... | encoded | `s 153.1(5) the belief that the complainant consented is not a defence: the bar applies` | F3 | 7 |
| s 153.1(5)(b) | 3084-3084 | (b) the accused did not take reasonable steps, in the circumstances kn... | encoded | `s 153.1(5) the belief that the complainant consented is not a defence: the bar applies` | F3 | 7 |
| s 153.1(5)(c) | 3085-3085 | (c) there is no evidence that the complainant’s voluntary agreement to... | encoded | `s 153.1(5) the belief that the complainant consented is not a defence: the bar applies` | F3 | 7 |
| s 153.1(6) | 3086-3087 | Accused’s belief as to consent (6) If an accused alleges that he or sh... | fork | `s 153.1(6) the judge must instruct the jury to consider the presence or absence of reasonable grounds for the belief`<br>`s 153.1(6) the judge's duty to instruct the jury` | F6 | 3 |
| s 154 | 3088-3088 | 154 [Repealed, R.S., 1985, c. 19 (3rd Supp.), s. 1] | repealed or blank in this text | `s 154 as the text shows it` | - | 1 |
| s 155(1) | 3089-3090 | Incest 155 (1) Every one commits incest who, knowing that another pers... | encoded | `s 155(1) the conduct is incest` | F1 | 11 |
| s 155(2) | 3091-3092 | Punishment (2) Everyone who commits incest is guilty of an indictable ... | fork | `s 155(2) the punishment`<br>`s 155 the class of the offence` | F17 | 5 |
| s 155(3) | 3093-3094 | Defence (3) No accused shall be determined by a court to be guilty of ... | encoded | `s 155(3) section 155 gives the accused a defence` | F3 | 4 |
| s 155(4) | 3095-3096 | Definition of brother and sister (4) In this section, brother and sist... | encoded | `s 155(4) brother and sister include half-brother and half-sister` | includes | 6 |
| s 156 | 3097-3098 | Historical offences 156 No person shall be convicted of any sexual off... | encoded | `s 156 no person shall be convicted: the bar applies` | F2, F4 | 4 |
| ss 157 and 158 | 3099-3099 | 157 and 158 [Repealed, R.S., 1985, c. 19 (3rd Supp.), s. 2] | repealed or blank in this text | `ss 157 and 158 as the text shows it` | - | 1 |
| s 159 | 3100-3100 | 159 [Repealed, 2019, c. 25, s. 54] | repealed or blank in this text | `s 159 as the text shows it` | - | 1 |
| s 160(1) | 3101-3102 | Bestiality 160 (1) Every person who commits bestiality is guilty of an... | encoded | `s 160(1) the conduct is the offence of bestiality`<br>`s 160(1) the punishment on indictment`<br>`s 160(1) the punishment on summary conviction`<br>`s 160(1) the class of the offence` | F1; summary penalty from s 787(1) (seam) | 6 |
| s 160(2) | 3103-3104 | Compelling the commission of bestiality (2) Every person who compels a... | encoded | `s 160(2) the conduct is the offence of compelling the commission of bestiality`<br>`s 160(2) the punishment on indictment`<br>`s 160(2) the punishment on summary conviction`<br>`s 160(2) the class of the offence` | F1; summary penalty from s 787(1) (seam) | 7 |
| s 160(3) | 3105-3106 | Bestiality in presence of or by child (3) Despite subsection (1), ever... | encoded | `s 160(3) the conduct is the offence of bestiality in the presence of, or by inciting, a person under 16`<br>`s 160(3) the class of the offence` | F1 | 6 |
| s 160(3)(a) | 3107-3107 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 160(3)(a) the punishment on indictment` | - | 1 |
| s 160(3)(b) | 3108-3108 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 160(3)(b) the punishment on summary conviction` | - | 1 |
| s 160(3.1) | 3109-3110 | Representation of bestiality (3.1) Every person commits an offence who... | encoded | `s 160(3.1) the conduct is the offence of publishing or distributing a representation of bestiality` | F1 | 9 |
| s 160(3.2) | 3111-3112 | Defence of public good (3.2) No person shall be convicted of an offenc... | encoded | `s 160(3.2) section 160 gives a defence of public good against a charge under subsection (3.1)` | F3 | 3 |
| s 160(3.3) | 3113-3114 | Question of law and fact, motives (3.3) For the purposes of subsection... | encoded | `s 160(3.3)(a) the question is a question of law`<br>`s 160(3.3)(b) the motives of the accused are relevant` | - | 6 |
| s 160(3.3)(a) | 3115-3115 | (a) it is a question of law whether the conduct served the public good... | encoded | `s 160(3.3)(a) the question is a question of law` | - | 4 |
| s 160(3.3)(b) | 3116-3116 | (b) the motives of the accused are irrelevant. | encoded | `s 160(3.3)(b) the motives of the accused are relevant` | - | 2 |
| s 160(3.4) | 3117-3118 | Punishment — representation of bestiality (3.4) Every person who commi... | encoded | `s 160(3.4) the class of the offence` | - | 1 |
| s 160(3.4)(a) | 3119-3119 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 160(3.4)(a) the punishment on indictment` | - | 1 |
| s 160(3.4)(b) | 3120-3120 | (b) is guilty of an offence punishable on summary conviction. | encoded | `s 160(3.4)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 160(4) | 3121-3122 | Order of prohibition or restitution (4) The court may, in addition to ... | fork | `s 160(4)(a) the court may make an order prohibiting the accused`<br>`s 160(4)(b) the court may order the accused to pay the reasonable costs of the animal's care` | power with limits in its own wording: NOTHING outside; F9, F19 | 10 |
| s 160(4)(a) | 3123-3123 | (a) make an order prohibiting the accused from owning, having the cust... | fork | `s 160(4)(a) the court may make an order prohibiting the accused`<br>`s 160(4)(a) the shortest period of the order` | F19 | 7 |
| s 160(4)(b) | 3124-3124 | (b) on application of the Attorney General or on its own motion, order... | fork | `s 160(4)(b) the court may order the accused to pay the reasonable costs of the animal's care` | if-gate on a power: NOTHING (F19); F9, F19 | 5 |
| s 160(5) | 3125-3126 | Breach of order (5) Every person who contravenes an order made under p... | encoded | `s 160(5) the conduct is the offence of contravening an order made under paragraph (4)(a)`<br>`s 160(5) the punishment on summary conviction`<br>`s 160(5) the class of the offence` | F1; penalty from s 787(1) (seam) | 4 |
| s 160(6) | 3127-3128 | Application (6) Sections 740 to 741.2 apply, with any modifications th... | encoded | `s 160(6) sections 740 to 741.2 apply to the order` | - | 2 |
| s 160(7) | 3129-3130 | Definition of bestiality (7) In this section, bestiality means any con... | encoded | `s 160(7) bestiality` | means | 3 |
| s 161(1) | 3131-3132 | Order of prohibition 161 (1) When an offender is convicted, or is disc... | fork | `s 161(1) the court sentences or discharges the offender in the case the subsection describes`<br>`s 161(1) the court shall consider making an order of prohibition`<br>`s 161(1) the court may make an order of prohibition` | F6, F9; F9 | 9 |
| s 161(1)(a) | 3133-3133 | (a) attending a public park or public swimming area where persons unde... | fork | `s 161(1)(a) to (d) the order may prohibit the offender from` | a list without "only": NOTHING outside; F19 | 6 |
| s 161(1)(a.1) | 3134-3134 | (a.1) being within two kilometres, or any other distance specified in ... | fork | `s 161(1)(a) to (d) the order may prohibit the offender from`<br>`s 161(1)(a.1) the order may prohibit the offender from being near the place`<br>`s 161(1)(a.1) the distance in kilometres` | seam: s 2 dwelling-house; F19 | 13 |
| s 161(1)(b) | 3135-3135 | (b) seeking, obtaining or continuing any employment, whether or not th... | fork | `s 161(1) the court sentences or discharges the offender in the case the subsection describes`<br>`s 161(1) the court shall consider making an order of prohibition`<br>`s 161(1) the court may make an order of prohibition` | F6, F9; F9 | 9 |
| s 161(1)(c) | 3136-3136 | (c) having any contact — including communicating by any means — with a... | fork | `s 161(1) the court sentences or discharges the offender in the case the subsection describes`<br>`s 161(1) the court shall consider making an order of prohibition`<br>`s 161(1) the court may make an order of prohibition` | F6, F9; F9 | 9 |
| s 161(1)(d) | 3137-3137 | (d) using the Internet or other digital network, unless the offender d... | fork | `s 161(1) the court sentences or discharges the offender in the case the subsection describes`<br>`s 161(1) the court shall consider making an order of prohibition`<br>`s 161(1) the court may make an order of prohibition` | F6, F9; F9 | 9 |
| s 161(1.1) | 3138-3139 | Offences (1.1) The offences for the purpose of subsection (1) are | fork | `s 161(1.1) the offence is one referred to in subsection (1.1)` | F10 | 56 |
| s 161(1.1)(a) | 3140-3140 | (a) an offence under section 151, 152, 153 or 155, subsection 160(2) o... | fork | `s 161(1.1) the offence is one referred to in subsection (1.1)` | F10 | 56 |
| s 161(1.1)(b) | 3141-3141 | (b) an offence under section 144 (rape), 145 (attempt to commit rape),... | fork | `s 161(1.1) the offence is one referred to in subsection (1.1)` | F10 | 56 |
| s 161(1.1)(c) | 3142-3142 | (c) an offence under subsection 146(1) (sexual intercourse with a fema... | fork | `s 161(1.1) the offence is one referred to in subsection (1.1)` | F10 | 56 |
| s 161(1.1)(d) | 3143-3143 | (d) an offence under subsection 212(1) (procuring), 212(2) (living on ... | fork | `s 161(1.1) the offence is one referred to in subsection (1.1)` | F10 | 56 |
| s 161(2) | 3144-3145 | Duration of prohibition (2) The prohibition may be for life or for any... | fork | `s 161(2) the prohibition may be for the duration`<br>`s 161(2) the date on which the prohibition begins` | F19 | 7 |
| s 161(2)(a) | 3146-3146 | (a) the date on which the order is made; and | fork | `s 161(2) the prohibition may be for the duration`<br>`s 161(2) the date on which the prohibition begins` | F19 | 7 |
| s 161(2)(b) | 3147-3147 | (b) where the offender is sentenced to a term of imprisonment, the dat... | fork | `s 161(2) the prohibition may be for the duration`<br>`s 161(2) the date on which the prohibition begins` | F19 | 7 |
| s 161(3) | 3148-3149 | Court may vary order (3) A court that makes an order of prohibition or... | fork | `s 161(3) the court may vary the conditions prescribed in the order` | if-gate on a power: NOTHING (F19); F9, F19 | 5 |
| s 161(4) | 3150-3151 | Offence (4) Every person who is bound by an order of prohibition and w... | encoded | `s 161(4) the conduct is the offence of not complying with an order of prohibition`<br>`s 161(4) the class of the offence`<br>`s 161(4) the offender SHANT do what the order of prohibition forbids` | F1 | 4 |
| s 161(4)(a) | 3152-3152 | (a) an indictable offence and is liable to imprisonment for a term of ... | encoded | `s 161(4)(a) the punishment on indictment` | - | 1 |
| s 161(4)(b) | 3153-3153 | (b) an offence punishable on summary conviction. | encoded | `s 161(4)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 162(1) | 3154-3155 | Voyeurism 162 (1) Every one commits an offence who, surreptitiously, o... | encoded | `s 162(1) the conduct is the offence of voyeurism` | F1 | 10 |
| s 162(1)(a) | 3156-3156 | (a) the person is in a place in which a person can reasonably be expec... | encoded | `s 162(1) the conduct is the offence of voyeurism` | F1 | 10 |
| s 162(1)(b) | 3157-3157 | (b) the person is nude, is nearly nude, is exposing their sexual organ... | encoded | `s 162(1) the conduct is the offence of voyeurism` | F1 | 10 |
| s 162(1)(c) | 3158-3158 | (c) the observation or recording is done for a sexual purpose. | encoded | `s 162(1) the conduct is the offence of voyeurism` | F1 | 10 |
| s 162(2) | 3159-3160 | Definition of visual recording (2) In this section, visual recording i... | encoded | `s 162(2) visual recording` | includes | 5 |
| s 162(3) | 3161-3162 | Exemption (3) Paragraphs (1)(a) and (b) do not apply to a peace office... | encoded | `s 162(3) paragraphs (1)(a) and (1)(b) apply to the person` | seam: s 2 peace officer | 5 |
| s 162(4) | 3163-3164 | Printing, publication, etc., of voyeuristic recordings (4) Every one c... | encoded | `s 162(4) the conduct is the offence of printing, publishing, etc. a voyeuristic recording` | F1 | 11 |
| s 162(5) | 3165-3166 | Punishment (5) Every one who commits an offence under subsection (1) o... | encoded | `s 162 the class of the offence` | - | 1 |
| s 162(5)(a) | 3167-3167 | (a) is guilty of an indictable offence and liable to imprisonment for ... | encoded | `s 162(5)(a) the punishment on indictment` | - | 1 |
| s 162(5)(b) | 3168-3168 | (b) is guilty of an offence punishable on summary conviction. | encoded | `s 162(5)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 162(6) | 3169-3170 | Defence (6) No person shall be convicted of an offence under this sect... | encoded | `s 162(6) section 162 gives a defence of public good` | F3 | 3 |
| s 162(7) | 3171-3172 | Question of law, motives (7) For the purposes of subsection (6), | encoded | `s 162(7)(a) the question is a question of law`<br>`s 162(7)(b) the motives of an accused are relevant` | - | 6 |
| s 162(7)(a) | 3173-3173 | (a) it is a question of law whether an act serves the public good and ... | encoded | `s 162(7)(a) the question is a question of law` | - | 4 |
| s 162(7)(b) | 3174-3174 | (b) the motives of an accused are irrelevant. | encoded | `s 162(7)(b) the motives of an accused are relevant` | - | 2 |
| s 162.1(1) | 3175-3176 | Publication, etc., of an intimate image without consent 162.1 (1) Ever... | encoded | `s 162.1(1) the conduct is the offence of publishing an intimate image without consent`<br>`s 162.1(1) the class of the offence` | F1 | 12 |
| s 162.1(1)(a) | 3177-3179 | (a) of an indictable offence and liable to imprisonment (i) for a term... | fork | `s 162.1(1)(a) the punishment on indictment` | F17: two maxima, 10 and 14 years | 2 |
| s 162.1(1)(b) | 3180-3180 | (b) of an offence punishable on summary conviction. | encoded | `s 162.1(1)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 162.1(1.1) | 3181-3182 | Threat to publish, etc. (1.1) Everyone who, with the intent to intimid... | encoded | `s 162.1(1.1) the conduct is the offence of threatening to publish an intimate image`<br>`s 162.1(1.1) the class of the offence` | F1 | 8 |
| s 162.1(1.1)(a) | 3183-3183 | (a) guilty of an indictable offence and liable to imprisonment for a t... | encoded | `s 162.1(1.1)(a) the punishment on indictment` | - | 1 |
| s 162.1(1.1)(b) | 3184-3184 | (b) guilty of an offence punishable on summary conviction. | encoded | `s 162.1(1.1)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 162.1(2) | 3185-3186 | Definition of intimate image (2) In this section, intimate image means | encoded | `s 162.1(2) intimate image` | means | 8 |
| s 162.1(2)(a) | 3187-3190 | (a) a visual recording of a person made by any means including a photo... | encoded | `s 162.1(2) intimate image` | means | 8 |
| s 162.1(2)(b) | 3191-3191 | (b) a visual representation that is made by any electronic or mechanic... | encoded | `s 162.1(2) intimate image` | means | 8 |
| s 162.1(3) | 3192-3193 | Defence (3) No person shall be convicted of an offence under this sect... | encoded | `s 162.1(3) section 162.1 gives a defence of public good` | F3 | 3 |
| s 162.1(4) | 3194-3195 | Question of fact and law, motives (4) For the purposes of subsection (... | encoded | `s 162.1(4)(a) the question is a question of law`<br>`s 162.1(4)(b) the motives of an accused are relevant` | - | 6 |
| s 162.1(4)(a) | 3196-3196 | (a) it is a question of law whether the conduct serves the public good... | encoded | `s 162.1(4)(a) the question is a question of law` | - | 4 |
| s 162.1(4)(b) | 3197-3197 | (b) the motives of an accused are irrelevant. | encoded | `s 162.1(4)(b) the motives of an accused are relevant` | - | 2 |
| s 162.2(1) | 3198-3199 | Prohibition order 162.2 (1) When an offender is convicted, or is disch... | fork | `s 162.2(1) the court may make an order prohibiting the offender from using the Internet or other digital network` | F9; F9 | 5 |
| s 162.2(2) | 3200-3201 | Duration of prohibition (2) The prohibition may be for any period that... | fork | `s 162.2(2) the prohibition may be for the period` | F19 | 2 |
| s 162.2(3) | 3202-3203 | Court may vary order (3) A court that makes an order of prohibition or... | fork | `s 162.2(3) the court may vary the conditions prescribed in the order` | if-gate on a power: NOTHING (F19); F9, F19 | 4 |
| s 162.2(4) | 3204-3205 | Offence (4) Every person who is bound by an order of prohibition and w... | encoded | `s 162.2(4) the conduct is the offence of not complying with an order of prohibition`<br>`s 162.2(4) the class of the offence` | F1 | 3 |
| s 162.2(4)(a) | 3206-3206 | (a) an indictable offence and is liable to imprisonment for a term of ... | encoded | `s 162.2(4)(a) the punishment on indictment` | - | 1 |
| s 162.2(4)(b) | 3207-3207 | (b) an offence punishable on summary conviction. | encoded | `s 162.2(4)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| heading: Offences Tending to Corrupt Morals | 3209-3209 | Offences Tending to Corrupt Morals | inert (reason 1: not operative) | - | heading | - |
| s 163(1) | 3210-3211 | Obscene materials 163 (1) Every person commits an offence who makes, p... | encoded | `s 163(1) the conduct is the offence of making or publishing obscene matter` | F1; penalty in s 169 | 8 |
| s 163(2) | 3212-3213 | Idem (2) Every person commits an offence who knowingly, without lawful... | encoded | `s 163(2) the conduct is the offence of selling obscene matter or exhibiting an indecent show` | F1; penalty in s 169 | 9 |
| s 163(2)(a) | 3214-3214 | (a) sells, exposes to public view or has in their possession for that ... | encoded | `s 163(2) the conduct is the offence of selling obscene matter or exhibiting an indecent show` | F1; penalty in s 169 | 9 |
| s 163(2)(b) | 3215-3215 | (b) publicly exhibits a disgusting object or an indecent show. | encoded | `s 163(2) the conduct is the offence of selling obscene matter or exhibiting an indecent show` | F1; penalty in s 169 | 9 |
| s 163(2)(c) | 3216-3216 | (c) and (d) [Repealed, 2018, c. 29, s. 11] | repealed or blank in this text | `s 163(2)(c) and (d) as the text shows it` | - | 1 |
| s 163(3) | 3217-3218 | Defence of public good (3) No person shall be convicted of an offence ... | encoded | `s 163(3) section 163 gives a defence of public good` | F3 | 3 |
| s 163(4) | 3219-3220 | Question of law and question of fact (4) For the purposes of this sect... | encoded | `s 163(4) the question is a question of law` | - | 4 |
| s 163(5) | 3221-3222 | Motives irrelevant (5) For the purposes of this section, the motives o... | encoded | `s 163(5) the motives of an accused are relevant` | - | 2 |
| s 163(6) | 3223-3223 | (6) [Repealed, 1993, c. 46, s. 1] | repealed or blank in this text | `s 163(6) as the text shows it` | - | 1 |
| s 163(7) | 3224-3224 | (7) [Repealed, 2018, c. 29, s. 11] | repealed or blank in this text | `s 163(7) as the text shows it` | - | 1 |
| s 163(8) | 3225-3226 | Obscene publication (8) For the purposes of this Act, any publication ... | encoded | `s 163(8) the publication is deemed to be obscene` | a deeming rule: NOTHING outside | 4 |
| s 163.1(1) | 3227-3228 | Definition of child sexual abuse and exploitation material 163.1 (1) I... | encoded | `s 163.1(1) child sexual abuse and exploitation material` | means | 12 |
| s 163.1(1)(a) | 3229-3231 | (a) a photographic, film, video or other visual representation, whethe... | encoded | `s 163.1(1) child sexual abuse and exploitation material` | means | 12 |
| s 163.1(1)(b) | 3232-3232 | (b) any written material, visual representation or audio recording tha... | encoded | `s 163.1(1) child sexual abuse and exploitation material` | means | 12 |
| s 163.1(1)(c) | 3233-3233 | (c) any written material whose dominant characteristic is the descript... | encoded | `s 163.1(1) child sexual abuse and exploitation material` | means | 12 |
| s 163.1(1)(d) | 3234-3234 | (d) any audio recording that has as its dominant characteristic the de... | encoded | `s 163.1(1) child sexual abuse and exploitation material` | means | 12 |
| s 163.1(2) | 3235-3236 | Making child sexual abuse and exploitation material (2) Every person w... | encoded | `s 163.1(2) the conduct is the offence of making, printing or publishing child sexual abuse and exploitation material`<br>`s 163.1(2) the punishment`<br>`s 163.1(2) the class of the offence` | F1 | 9 |
| s 163.1(3) | 3237-3238 | Distribution, etc. of child sexual abuse and exploitation material (3)... | encoded | `s 163.1(3) the conduct is the offence of distributing child sexual abuse and exploitation material`<br>`s 163.1(3) the punishment`<br>`s 163.1(3) the class of the offence` | F1 | 12 |
| s 163.1(4) | 3239-3240 | Possession of child sexual abuse and exploitation material (4) Every p... | encoded | `s 163.1(4) the conduct is the offence of possessing child sexual abuse and exploitation material`<br>`s 163.1(4) the class of the offence` | F1 | 4 |
| s 163.1(4)(a) | 3241-3241 | (a) an indictable offence and is liable to imprisonment for a term of ... | encoded | `s 163.1(4)(a) the punishment on indictment` | - | 1 |
| s 163.1(4)(b) | 3242-3242 | (b) an offence punishable on summary conviction and is liable to impri... | encoded | `s 163.1(4)(b) the punishment on summary conviction` | - | 1 |
| s 163.1(4.1) | 3243-3244 | Accessing child sexual abuse and exploitation material (4.1) Every per... | encoded | `s 163.1(4.1) the conduct is the offence of accessing child sexual abuse and exploitation material`<br>`s 163.1(4.1) the class of the offence` | F1 | 4 |
| s 163.1(4.1)(a) | 3245-3245 | (a) an indictable offence and is liable to imprisonment for a term of ... | encoded | `s 163.1(4.1)(a) the punishment on indictment` | - | 1 |
| s 163.1(4.1)(b) | 3246-3246 | (b) an offence punishable on summary conviction and is liable to impri... | encoded | `s 163.1(4.1)(b) the punishment on summary conviction` | - | 1 |
| s 163.1(4.2) | 3247-3248 | Interpretation (4.2) For the purposes of subsection (4.1), a person ac... | fork | `s 163.1(4.2) the person accesses child sexual abuse and exploitation material` | F11 | 2 |
| s 163.1(4.21) | 3249-3250 | Threat to publish, etc. (4.21) Every person who, with the intent to in... | encoded | `s 163.1(4.21) the conduct is the offence of threatening to publish child sexual abuse and exploitation material`<br>`s 163.1(4.21) the class of the offence` | F1 | 7 |
| s 163.1(4.21)(a) | 3251-3251 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 163.1(4.21)(a) the punishment on indictment` | - | 1 |
| s 163.1(4.21)(b) | 3252-3252 | (b) is guilty of an offence punishable on summary conviction and liabl... | encoded | `s 163.1(4.21)(b) the punishment on summary conviction` | - | 1 |
| s 163.1(4.3) | 3253-3254 | Aggravating factor (4.3) If a person is convicted of an offence under ... | fork | `s 163.1(4.3) the court must consider the intent to make a profit as an aggravating factor`<br>`s 163.1(4.3) the sentencing court's duty to consider the intent to make a profit` | F6 | 3 |
| s 163.1(5) | 3255-3256 | Defence (5) It is not a defence to a charge under subsection (2) in re... | encoded | `s 163.1(5) the belief that the person shown was eighteen or more is not a defence: the bar applies` | F2, F4 | 6 |
| s 163.1(6) | 3257-3258 | Defence (6) No person shall be convicted of an offence under this sect... | encoded | `s 163.1(6) section 163.1 gives a defence` | F3 | 3 |
| s 163.1(6)(a) | 3259-3259 | (a) has a legitimate purpose related to the administration of justice ... | encoded | `s 163.1(6) section 163.1 gives a defence` | F3 | 3 |
| s 163.1(6)(b) | 3260-3260 | (b) does not pose an undue risk of harm to persons under the age of ei... | encoded | `s 163.1(6) section 163.1 gives a defence` | F3 | 3 |
| s 163.1(7) | 3261-3262 | Question of law (7) For greater certainty, for the purposes of this se... | encoded | `s 163.1(7) the question is a question of law` | - | 2 |
| s 164(1) | 3263-3264 | Warrant of seizure 164 (1) A judge may issue a warrant authorizing sei... | fork | `s 164(1) a judge may issue a warrant authorizing seizure of copies of the material` | if-gate on a power: NOTHING (F19); F19 | 5 |
| s 164(1)(a) | 3265-3265 | (a) the material is illicit material; and | fork | `s 164(1) a judge may issue a warrant authorizing seizure of copies of the material` | if-gate on a power: NOTHING (F19); F19 | 5 |
| s 164(1)(b) | 3266-3266 | (b) copies of the material are kept in premises within the jurisdictio... | fork | `s 164(1) a judge may issue a warrant authorizing seizure of copies of the material` | if-gate on a power: NOTHING (F19); F19 | 5 |
| s 164(2) | 3267-3268 | Summons to occupier (2) Within seven days of the day on which the warr... | fork | `s 164(2) the judge issued the summons within seven days of the day on which the warrant was issued`<br>`s 164(2) the judge's duty to issue the summons` | F6; period (a) | 4 |
| s 164(3) | 3269-3270 | Owner and maker may appear (3) The owner and the maker of the seized t... | fork | `s 164(3) the person may appear and be represented in the proceedings to oppose the forfeiture` | F19 | 4 |
| s 164(4) | 3271-3272 | Order of forfeiture (4) If the court is satisfied, on a balance of pro... | fork | `s 164(4) the court may make an order declaring the thing forfeited to His Majesty in right of the province` | if-gate on a power: NOTHING (F19); F19 | 2 |
| s 164(5) | 3273-3274 | Restoration (5) If the court is not satisfied that the seized thing is... | fork | `s 164(5) the court must order the thing restored to the person from whom it was seized`<br>`s 164(5) the thing is to be restored now` | F6 | 5 |
| s 164(6) | 3275-3276 | Appeal (6) An appeal lies from an order made under subsection (4) or (... | encoded | `s 164(6) an appeal lies from the order` | - | 6 |
| s 164(6)(a) | 3277-3277 | (a) on any ground of appeal that involves a question of law alone, | encoded | `s 164(6) an appeal lies from the order` | - | 6 |
| s 164(6)(b) | 3278-3278 | (b) on any ground of appeal that involves a question of fact alone, or | encoded | `s 164(6) an appeal lies from the order` | - | 6 |
| s 164(6)(c) | 3279-3280 | (c) on any ground of appeal that involves a question of mixed law and ... | encoded | `s 164(6) an appeal lies from the order` | - | 6 |
| s 164(7) | 3281-3282 | Consent (7) If an order is made under this section by a judge in a pro... | encoded | `s 164(7) no proceedings shall be instituted or continued without the consent of the Attorney General: the bar applies` | F2, F4 | 11 |
| s 164(8) | 3283-3284 | Definitions (8) In this section, | inert (reason 1: not operative) | - | the enacting words "In this section," that scope the definitions below | - |
| s 164(8) "advertisement for conversion therapy" | 3285-3285 | advertisement for conversion therapy [Repealed, 2026, c. 19, s. 18] | repealed or blank in this text | `s 164(8) "advertisement for conversion therapy" as the text shows it` | - | 1 |
| s 164(8) "advertisement of sexual services" | 3286-3286 | advertisement of sexual services [Repealed, 2026, c. 19, s. 18] | repealed or blank in this text | `s 164(8) "advertisement of sexual services" as the text shows it` | - | 1 |
| s 164(8) "court" | 3287-3287 | court means | fork | `s 164(8) court` | F12 | 21 |
| s 164(8) "court" (a) | 3288-3288 | (a) in the Province of Quebec, the Court of Quebec, the municipal cour... | fork | `s 164(8) court` | F12 | 21 |
| s 164(8) "court" (a.1) | 3289-3289 | (a.1) in the Province of Ontario, the Superior Court of Justice, | fork | `s 164(8) court` | F12 | 21 |
| s 164(8) "court" (b) | 3290-3290 | (b) in the Provinces of New Brunswick, Manitoba, Saskatchewan and Albe... | fork | `s 164(8) court` | F12 | 21 |
| s 164(8) "court" (c) | 3291-3291 | (c) [Repealed, 2026, c. 11, s. 5] | repealed or blank in this text | `s 164(8) court (c) as the text shows it` | - | 1 |
| s 164(8) "court" (c.1) | 3292-3292 | (c.1) [Repealed, 1992, c. 51, s. 34] | repealed or blank in this text | `s 164(8) court (c.1) as the text shows it` | - | 1 |
| s 164(8) "court" (d) | 3293-3293 | (d) in the Provinces of Nova Scotia, British Columbia, Prince Edward I... | fork | `s 164(8) court` | F12 | 21 |
| s 164(8) "court" (e) | 3294-3294 | (e) in Nunavut, the Nunavut Court of Justice; (tribunal) | fork | `s 164(8) court` | F12 | 21 |
| s 164(8) "crime comic" | 3295-3295 | crime comic [Repealed, 2018, c. 29, s. 12] | repealed or blank in this text | `s 164(8) "crime comic" as the text shows it` | - | 1 |
| s 164(8) "illicit material" | 3296-3296 | illicit material means | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "illicit material" (a) | 3297-3297 | (a) any visual representation that is or is likely to be mistaken for ... | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "illicit material" (b) | 3298-3298 | (b) a visual recording, as defined in subsection 162(2), that is made ... | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "illicit material" (c) | 3299-3299 | (c) an intimate image, as defined in subsection 162.1(2), in relation ... | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "illicit material" (d) | 3300-3300 | (d) a publication that is obscene, within the meaning of subsection 16... | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "illicit material" (e) | 3301-3301 | (e) child sexual abuse and exploitation material, as defined in subsec... | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "illicit material" (f) | 3302-3302 | (f) any material — including a photographic, film, video, audio or oth... | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "illicit material" (g) | 3303-3303 | (g) any material — including a photographic, film, video, audio or oth... | encoded | `s 164(8) illicit material` | means; limbs are inputs (seams) | 11 |
| s 164(8) "intimate image" | 3304-3304 | intimate image [Repealed, 2026, c. 19, s. 18] | repealed or blank in this text | `s 164(8) "intimate image" as the text shows it` | - | 1 |
| s 164(8) "judge" | 3305-3305 | judge means a judge of a court. (juge) | encoded | `s 164(8) judge` | means | 4 |
| s 164(8) "voyeuristic recording" | 3306-3306 | voyeuristic recording [Repealed, 2026, c. 19, s. 18] | repealed or blank in this text | `s 164(8) "voyeuristic recording" as the text shows it` | - | 1 |
| s 164.1(1) | 3307-3308 | Warrant of seizure — material on computer system 164.1 (1) If a judge ... | fork | `s 164.1(1) the judge may order the custodian of the computer system` | if-gate on a power: NOTHING (F19); F19 | 5 |
| s 164.1(1)(a) | 3309-3309 | (a) give an electronic copy of the material to the court; | fork | `s 164.1(1) the judge may order the custodian of the computer system` | if-gate on a power: NOTHING (F19); F19 | 5 |
| s 164.1(1)(b) | 3310-3310 | (b) ensure that the material is no longer stored on and made available... | fork | `s 164.1(1) the judge may order the custodian of the computer system` | if-gate on a power: NOTHING (F19); F19 | 5 |
| s 164.1(1)(c) | 3311-3311 | (c) provide the information necessary to identify and locate the perso... | fork | `s 164.1(1) the judge may order the custodian of the computer system` | if-gate on a power: NOTHING (F19); F19 | 5 |
| s 164.1(2) | 3312-3313 | Notice to person who posted the material (2) Within a reasonable time ... | fork | `s 164.1(2) the judge must cause notice to be given to the person who posted the material`<br>`s 164.1(2) the judge may order the custodian to post the text of the notice` | F13; F19 | 4 |
| s 164.1(3) | 3314-3315 | Person who posted the material may appear (3) The person who posted th... | fork | `s 164.1(3) the person may appear and be represented in the proceedings to oppose the order` | F19 | 2 |
| s 164.1(4) | 3316-3317 | Non-appearance (4) If the person who posted the material does not appe... | fork | `s 164.1(4) the court may proceed ex parte` | if-gate on a power: NOTHING (F19); F19 | 2 |
| s 164.1(5) | 3318-3319 | Order (5) If the court is satisfied, on a balance of probabilities, th... | fork | `s 164.1(5) the court may order the custodian to delete the material` | if-gate on a power: NOTHING (F19); F19 | 2 |
| s 164.1(5.1) | 3320-3321 | Order — intimate image (5.1) If the illicit material is an intimate im... | fork | `s 164.1(5.1) the court must order the custodian to delete the material within 48 hours`<br>`s 164.1(5.1) the material was deleted within 48 hours after the order was made`<br>`s 164.1(5.1) the custodian's duty to delete the intimate image` | F6; period (a) | 7 |
| s 164.1(6) | 3322-3323 | Destruction of copy (6) When the court makes the order for the deletio... | fork | `s 164.1(6) the court may order the destruction of the electronic copy in the court's possession` | F9; F9 | 2 |
| s 164.1(7) | 3324-3325 | Return of material (7) If the court is not satisfied that the material... | fork | `s 164.1(7) the court must order the electronic copy returned and terminate the order made under paragraph (1)(b)` | F6 | 2 |
| s 164.1(8) | 3326-3327 | Other provisions to apply (8) Subsections 164(6) and (7) apply, with a... | encoded | `s 164.1(8) subsections 164(6) and (7) apply to the proceedings` | - | 2 |
| s 164.1(9) | 3328-3329 | When order takes effect (9) No order made under subsections (5) to (7)... | encoded | `s 164.1(9) the order cannot yet take effect` | the "until" bar (ruling (d)) | 3 |
| s 164.1(10) | 3330-3331 | Definitions (10) In this section, computer data and computer system ha... | encoded | `s 164.1(10) the term has the meaning given by subsection 342.1(2) or subsection 164(8)` | borrowed meaning (s 342.1(2) is in another part) | 6 |
| s 164.2(1) | 3332-3333 | Forfeiture after conviction 164.2 (1) On application of the Attorney G... | fork | `s 164.2(1) the court may order the thing forfeited to Her Majesty` | if-gate on a power: NOTHING (F19); F9, F19 | 9 |
| s 164.2(1)(a) | 3334-3334 | (a) was used in the commission of the offence; and | fork | `s 164.2(1) the court may order the thing forfeited to Her Majesty` | if-gate on a power: NOTHING (F19); F9, F19 | 9 |
| s 164.2(1)(b) | 3335-3337 | (b) is the property of (i) the convicted person or another person who ... | fork | `s 164.2(1) the court may order the thing forfeited to Her Majesty` | if-gate on a power: NOTHING (F19); F9, F19 | 9 |
| s 164.2(2) | 3338-3339 | Third party rights (2) Before making an order under subsection (1), th... | fork | `s 164.2(2) the court must cause notice to be given to the person`<br>`s 164.2(2) the court may hear the person and declare the nature and extent of the person's interest` | F6; F19 | 5 |
| s 164.2(3) | 3340-3341 | Right of appeal — third party (3) A person who was heard in response t... | fork | `s 164.2(3) the person may appeal to the court of appeal` | F19 | 3 |
| s 164.2(4) | 3342-3343 | Right of appeal — Attorney General (4) The Attorney General may appeal... | fork | `s 164.2(4) the Attorney General may appeal to the court of appeal` | F19 | 2 |
| s 164.2(5) | 3344-3345 | Application of Part XXI (5) Part XXI applies, with any modifications t... | encoded | `s 164.2(5) Part XXI applies to the appeal` | - | 2 |
| s 164.3(1) | 3346-3347 | Relief from forfeiture 164.3 (1) Within thirty days after an order und... | fork | `s 164.3(1) the person may apply for relief from forfeiture`<br>`s 164.3(1) the claimant's permission to apply` | period (a); F9, F19 | 6 |
| s 164.3(2) | 3348-3349 | Hearing of application (2) The judge shall fix a day — not less than t... | fork | `s 164.3(2) the day fixed for the hearing is one the judge may fix` | F6; period (a) | 3 |
| s 164.3(3) | 3350-3351 | Notice to Attorney General (3) At least fifteen days before the hearin... | fork | `s 164.3(3) the applicant served notice on the Attorney General at least fifteen days before the hearing`<br>`s 164.3(3) the applicant's duty to serve notice on the Attorney General` | F6; period (a) | 3 |
| s 164.3(4) | 3352-3353 | Order (4) The judge may make an order declaring that the applicant’s i... | fork | `s 164.3(4) the judge may declare that the applicant's interest in the thing is not affected by the forfeiture` | if-gate on a power: NOTHING (F19); F19 | 3 |
| s 164.3(4)(a) | 3354-3354 | (a) was not a party to the offence; and | fork | `s 164.3(4) the judge may declare that the applicant's interest in the thing is not affected by the forfeiture` | if-gate on a power: NOTHING (F19); F19 | 3 |
| s 164.3(4)(b) | 3355-3355 | (b) did not acquire the thing from a person who was a party to the off... | fork | `s 164.3(4) the judge may declare that the applicant's interest in the thing is not affected by the forfeiture` | if-gate on a power: NOTHING (F19); F19 | 3 |
| s 164.3(5) | 3356-3357 | Appeal to court of appeal (5) A person referred to in subsection (4) o... | fork | `s 164.3(5) the person may appeal to the court of appeal` | F19 | 3 |
| s 164.3(6) | 3358-3359 | Powers of Attorney General (6) On application by a person who obtained... | fork | `s 164.3(6) the Attorney General must direct that the thing be returned or its value paid` | F6, F14 | 5 |
| s 164.3(6)(a) | 3360-3360 | (a) the thing be returned to the person; or | fork | `s 164.3(6) the Attorney General must direct that the thing be returned or its value paid` | F6, F14 | 5 |
| s 164.3(6)(b) | 3361-3361 | (b) an amount equal to the value of the extent of the person’s interes... | fork | `s 164.3(6) the Attorney General must direct that the thing be returned or its value paid` | F6, F14 | 5 |
| s 165 | 3362-3362 | 165 [Repealed, 2018, c. 29, s. 13] | repealed or blank in this text | `s 165 as the text shows it` | - | 1 |
| s 166 | 3363-3363 | 166 [Repealed, 1994, c. 44, s. 9] | repealed or blank in this text | `s 166 as the text shows it` | - | 1 |
| s 167(1) | 3364-3365 | Immoral theatrical performance 167 (1) Every one commits an offence wh... | encoded | `s 167(1) the conduct is the offence of presenting an immoral theatrical performance` | F1; penalty in s 169 | 7 |
| s 167(2) | 3366-3367 | Person taking part (2) Every one commits an offence who takes part or ... | encoded | `s 167(2) the conduct is the offence of taking part in an immoral theatrical performance` | F1; penalty in s 169 | 4 |
| s 168(1) | 3368-3369 | Mailing obscene matter 168 (1) Every one commits an offence who makes ... | encoded | `s 168(1) the conduct is the offence of mailing obscene matter` | F1; penalty in s 169 | 4 |
| s 168(2) | 3370-3371 | Exceptions (2) Subsection (1) does not apply to a person who | fork | `s 168(2) subsection (1) applies to the person` | F18: a flat negative: JUST FALSE for the four persons, NOTHING for others | 5 |
| s 168(2)(a) | 3372-3372 | (a) prints or publishes any matter for use in connection with any judi... | fork | `s 168(2) subsection (1) applies to the person` | F18: a flat negative: JUST FALSE for the four persons, NOTHING for others | 5 |
| s 168(2)(b) | 3373-3373 | (b) prints or publishes a notice or report under the direction of a co... | fork | `s 168(2) subsection (1) applies to the person` | F18: a flat negative: JUST FALSE for the four persons, NOTHING for others | 5 |
| s 168(2)(c) | 3374-3376 | (c) prints or publishes any matter (i) in a volume or part of a genuin... | fork | `s 168(2) subsection (1) applies to the person` | F18: a flat negative: JUST FALSE for the four persons, NOTHING for others | 5 |
| s 169 | 3377-3378 | Punishment 169 Every one who commits an offence under section 163, 165... | fork | `s 169 the offence is one under section 163, 165, 167 or 168`<br>`s 169 the class of an offence under section 163, 165, 167 or 168` | F16 | 8 |
| s 169(a) | 3379-3379 | (a) an indictable offence and is liable to imprisonment for a term not... | encoded | `s 169(a) the punishment on indictment` | - | 1 |
| s 169(b) | 3380-3380 | (b) an offence punishable on summary conviction. | encoded | `s 169(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 169.1(1) | 3381-3382 | Recruitment — young person 169.1 (1) Every person is guilty of an offe... | encoded | `s 169.1(1) the conduct is the offence of recruiting a young person to an offence`<br>`s 169.1 the class of the offence` | F1 | 11 |
| s 169.1(2) | 3383-3384 | Position of trust, power or authority (2) For the purposes of subsecti... | encoded | `s 169.1(2) the person is considered to be in a position of trust, power or authority towards the young person` | "among others": list not closed | 3 |
| s 169.1(3) | 3385-3386 | No defence (3) It is not a defence to a charge under subsection (1) th... | encoded | `s 169.1(3) the belief that the young person was at least 18 is not a defence: the bar applies` | F4 | 3 |
| s 169.1(4) | 3387-3388 | Punishment (4) Every person who commits an offence under subsection (1... | encoded | `s 169.1 the class of the offence` | - | 1 |
| s 169.1(4)(a) | 3389-3389 | (a) guilty of an indictable offence and liable to imprisonment for a t... | encoded | `s 169.1(4)(a) the punishment on indictment` | - | 1 |
| s 169.1(4)(b) | 3390-3390 | (b) guilty of an offence punishable on summary conviction. | encoded | `s 169.1(4)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 169.1(5) | 3391-3392 | Definition of young person (5) In this section, young person means a p... | encoded | `s 169.1(5) young person` | means | 3 |
| s 170 | 3393-3394 | Parent or guardian procuring sexual activity 170 Every parent or guard... | encoded | `s 170 the conduct is the offence of a parent or guardian procuring a person under 18 for sexual activity`<br>`s 170 the punishment`<br>`s 170 the class of the offence` | F1 | 8 |
| s 171 | 3395-3396 | Householder permitting prohibited sexual activity 171 Every owner, occ... | encoded | `s 171 the conduct is the offence of a householder permitting prohibited sexual activity`<br>`s 171 the punishment`<br>`s 171 the class of the offence` | F1 | 7 |
| s 171.1(1) | 3397-3398 | Making sexually explicit material available to child 171.1 (1) Every p... | encoded | `s 171.1(1) the conduct is the offence of making sexually explicit material available to a child`<br>`s 171.1(1) the person is, or the accused believes the person is, under the age` | F1 | 15 |
| s 171.1(1)(a) | 3399-3399 | (a) a person who is, or who the accused believes is, under the age of ... | encoded | `s 171.1(1)(a) the offence is one under subsection 153(1), section 155, 163.1, 170, 171 or 279.011 or subsection 279.02(2), 279.03(2), 286.1(2), 286.2(2) or 286.3(2)` | - | 15 |
| s 171.1(1)(b) | 3400-3400 | (b) a person who is, or who the accused believes is, under the age of ... | encoded | `s 171.1(1)(b) the offence is one under section 151 or 152, subsection 160(3) or 173(2) or section 271, 272, 273 or 280` | - | 11 |
| s 171.1(1)(c) | 3401-3401 | (c) a person who is, or who the accused believes is, under the age of ... | encoded | `s 171.1(1)(c) the offence is one under section 281` | - | 2 |
| s 171.1(2) | 3402-3403 | Punishment (2) Every person who commits an offence under subsection (1... | encoded | `s 171.1 the class of the offence` | - | 1 |
| s 171.1(2)(a) | 3404-3404 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 171.1(2)(a) the punishment on indictment` | - | 1 |
| s 171.1(2)(b) | 3405-3405 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 171.1(2)(b) the punishment on summary conviction` | - | 1 |
| s 171.1(3) | 3406-3407 | Presumption (3) Evidence that the person referred to in paragraph (1)(... | encoded | `s 171.1(3) the evidence is proof that the accused believed that the person was under that age` | a rebuttable presumption | 3 |
| s 171.1(4) | 3408-3409 | No defence (4) It is not a defence to a charge under paragraph (1)(a),... | encoded | `s 171.1(4) the belief that the person was at least the age is not a defence: the bar applies` | F2, F4 | 3 |
| s 171.1(5) | 3410-3411 | Definition of sexually explicit material (5) In subsection (1), sexual... | encoded | `s 171.1(5) sexually explicit material` | means; seam: s 163.1(1) | 8 |
| s 171.1(5)(a) | 3412-3414 | (a) a photographic, film, video or other visual representation, whethe... | encoded | `s 171.1(5) sexually explicit material` | means; seam: s 163.1(1) | 8 |
| s 171.1(5)(b) | 3415-3415 | (b) written material whose dominant characteristic is the description,... | encoded | `s 171.1(5) sexually explicit material` | means; seam: s 163.1(1) | 8 |
| s 171.1(5)(c) | 3416-3416 | (c) an audio recording whose dominant characteristic is the descriptio... | encoded | `s 171.1(5) sexually explicit material` | means; seam: s 163.1(1) | 8 |
| s 171.1(6) | 3417-3418 | For greater certainty (6) For greater certainty, a reference to sexual... | encoded | `s 171.1(6) the activity is sexual activity for the purposes of subsection (5)` | includes | 3 |
| s 172(1) | 3419-3420 | Corrupting children 172 (1) Every person who, in the home of a child, ... | encoded | `s 172(1) the conduct is the offence of corrupting children`<br>`s 172 the class of the offence` | F1 | 9 |
| s 172(1)(a) | 3421-3421 | (a) an indictable offence and liable to imprisonment for a term of not... | encoded | `s 172(1)(a) the punishment on indictment` | - | 1 |
| s 172(1)(b) | 3422-3422 | (b) an offence punishable on summary conviction. | encoded | `s 172(1)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 172(2) | 3423-3423 | (2) [Repealed, R.S., 1985, c. 19 (3rd Supp.), s. 6] | repealed or blank in this text | `s 172(2) as the text shows it` | - | 1 |
| s 172(3) | 3424-3425 | Definition of child (3) For the purposes of this section, child means ... | encoded | `s 172(3) child` | means | 3 |
| s 172(4) | 3426-3427 | Who may institute prosecutions (4) No proceedings shall be commenced u... | encoded | `s 172(4) no proceedings shall be commenced without the consent of the Attorney General: the bar applies` | F4 | 4 |
| s 172.1(1) | 3428-3429 | Luring a child 172.1 (1) Every person commits an offence who, by a mea... | encoded | `s 172.1(1) the conduct is the offence of luring a child` | F1 | 9 |
| s 172.1(1)(a) | 3430-3430 | (a) a person who is, or who the accused believes is, under the age of ... | encoded | `s 172.1(1) the conduct is the offence of luring a child` | F1 | 9 |
| s 172.1(1)(b) | 3431-3431 | (b) a person who is, or who the accused believes is, under the age of ... | encoded | `s 172.1(1) the conduct is the offence of luring a child` | F1 | 9 |
| s 172.1(1)(c) | 3432-3432 | (c) a person who is, or who the accused believes is, under the age of ... | encoded | `s 172.1(1) the conduct is the offence of luring a child` | F1 | 9 |
| s 172.1(2) | 3433-3434 | Punishment (2) Every person who commits an offence under subsection (1... | encoded | `s 172.1 the class of the offence` | - | 1 |
| s 172.1(2)(a) | 3435-3435 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 172.1(2)(a) the punishment on indictment` | - | 1 |
| s 172.1(2)(b) | 3436-3436 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 172.1(2)(b) the punishment on summary conviction` | - | 1 |
| s 172.1(3) | 3437-3438 | Presumption re age (3) Evidence that the person referred to in paragra... | encoded | `s 172.1(3) the evidence is proof that the accused believed that the person was under that age` | a rebuttable presumption | 3 |
| s 172.1(4) | 3439-3440 | No defence (4) It is not a defence to a charge under paragraph (1)(a),... | encoded | `s 172.1(4) the belief that the person was at least the age is not a defence: the bar applies` | F2, F4 | 3 |
| heading: Disorderly Conduct | 3442-3442 | Disorderly Conduct | inert (reason 1: not operative) | - | heading | - |
| s 172.2(1) | 3443-3444 | Agreement or arrangement — sexual offence against child 172.2 (1) Ever... | encoded | `s 172.2(1) the conduct is the offence of agreeing or arranging to commit a sexual offence against a child` | F1 | 7 |
| s 172.2(1)(a) | 3445-3445 | (a) under subsection 153(1), section 155, 163.1, 170, 171 or 279.011 o... | encoded | `s 172.2(1) the conduct is the offence of agreeing or arranging to commit a sexual offence against a child` | F1 | 7 |
| s 172.2(1)(b) | 3446-3446 | (b) under section 151 or 152, subsection 160(3) or 173(2) or section 2... | encoded | `s 172.2(1) the conduct is the offence of agreeing or arranging to commit a sexual offence against a child` | F1 | 7 |
| s 172.2(1)(c) | 3447-3447 | (c) under section 281 with respect to another person who is, or who th... | encoded | `s 172.2(1) the conduct is the offence of agreeing or arranging to commit a sexual offence against a child` | F1 | 7 |
| s 172.2(2) | 3448-3449 | Punishment (2) Every person who commits an offence under subsection (1... | encoded | `s 172.2 the class of the offence` | - | 1 |
| s 172.2(2)(a) | 3450-3450 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 172.2(2)(a) the punishment on indictment` | - | 1 |
| s 172.2(2)(b) | 3451-3451 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 172.2(2)(b) the punishment on summary conviction` | - | 1 |
| s 172.2(3) | 3452-3453 | Presumption (3) Evidence that the person referred to in paragraph (1)(... | encoded | `s 172.2(3) the evidence is proof that the accused believed that the person was under that age` | a rebuttable presumption | 3 |
| s 172.2(4) | 3454-3455 | No defence (4) It is not a defence to a charge under paragraph (1)(a),... | encoded | `s 172.2(4) the belief that the person was at least the age is not a defence: the bar applies` | F2, F4 | 3 |
| s 172.2(5) | 3456-3457 | No defence (5) It is not a defence to a charge under paragraph (1)(a),... | encoded | `s 172.2(5)(a) it is not a defence that the person with whom the accused agreed was a peace officer or acting under the direction of one`<br>`s 172.2(5)(b) it is not a defence that the person referred to did not exist` | seam: s 2 peace officer | 9 |
| s 172.2(5)(a) | 3458-3458 | (a) that the person with whom the accused agreed or made an arrangemen... | encoded | `s 172.2(5)(a) it is not a defence that the person with whom the accused agreed was a peace officer or acting under the direction of one` | seam: s 2 peace officer | 5 |
| s 172.2(5)(b) | 3459-3459 | (b) that, if the person with whom the accused agreed or made an arrang... | encoded | `s 172.2(5)(b) it is not a defence that the person referred to did not exist` | - | 4 |
| s 173(1) | 3460-3461 | Indecent acts 173 (1) Everyone who wilfully does an indecent act in a ... | encoded | `s 173(1) the conduct is the offence of an indecent act`<br>`s 173(1) the class of the offence` | F1 | 7 |
| s 173(1)(a) | 3462-3462 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 173(1)(a) the punishment on indictment` | - | 1 |
| s 173(1)(b) | 3463-3463 | (b) is guilty of an offence punishable on summary conviction. | encoded | `s 173(1)(b) the punishment on summary conviction` | penalty from s 787(1) (seam) | 1 |
| s 173(2) | 3464-3465 | Exposure (2) Every person who, in any place, for a sexual purpose, exp... | encoded | `s 173(2) the conduct is the offence of exposure to a person under 16`<br>`s 173(2) the class of the offence` | F1 | 7 |
| s 173(2)(a) | 3466-3466 | (a) is guilty of an indictable offence and is liable to imprisonment f... | encoded | `s 173(2)(a) the punishment on indictment` | - | 1 |
| s 173(2)(b) | 3467-3467 | (b) is guilty of an offence punishable on summary conviction and is li... | encoded | `s 173(2)(b) the punishment on summary conviction` | - | 1 |
| s 174(1) | 3468-3469 | Nudity 174 (1) Every one who, without lawful excuse, | encoded | `s 174(1) the conduct is the offence of nudity`<br>`s 174(1) the punishment on summary conviction`<br>`s 174(1) the class of the offence` | F1; penalty from s 787(1) (seam) | 7 |
| s 174(1)(a) | 3470-3470 | (a) is nude in a public place, or | encoded | `s 174(1) the conduct is the offence of nudity`<br>`s 174(1) the punishment on summary conviction`<br>`s 174(1) the class of the offence` | F1; penalty from s 787(1) (seam) | 7 |
| s 174(1)(b) | 3471-3472 | (b) is nude and exposed to public view while on private property, whet... | encoded | `s 174(1) the conduct is the offence of nudity`<br>`s 174(1) the punishment on summary conviction`<br>`s 174(1) the class of the offence` | F1; penalty from s 787(1) (seam) | 7 |
| s 174(2) | 3473-3474 | Nude (2) For the purposes of this section, a person is nude who is so ... | fork | `s 174(2) the person is nude` | F11 | 2 |
| s 174(3) | 3475-3476 | Consent of Attorney General (3) No proceedings shall be commenced unde... | encoded | `s 174(3) no proceedings shall be commenced without the consent of the Attorney General: the bar applies` | F4 | 3 |
| s 175(1) | 3477-3478 | Causing disturbance, indecent exhibition, loitering, etc. 175 (1) Ever... | encoded | `s 175(1) the punishment on summary conviction`<br>`s 175(1) the class of the offence` | penalty from s 787(1) (seam) | 2 |
| s 175(1)(a) | 3479-3482 | (a) not being in a dwelling-house, causes a disturbance in or near a p... | encoded | `s 175(1)(a) the conduct is the offence of causing a disturbance in or near a public place` | F1; seams: s 2 dwelling-house | 13 |
| s 175(1)(b) | 3483-3483 | (b) openly exposes or exhibits an indecent exhibition in a public plac... | encoded | `s 175(1)(b) the conduct is the offence of an indecent exhibition in a public place` | F1 | 3 |
| s 175(1)(c) | 3484-3484 | (c) loiters in a public place and in any way obstructs persons who are... | encoded | `s 175(1)(c) the conduct is the offence of loitering in a public place and obstructing persons` | F1 | 4 |
| s 175(1)(d) | 3485-3486 | (d) disturbs the peace and quiet of the occupants of a dwelling-house ... | encoded | `s 175(1)(d) the conduct is the offence of disturbing the peace and quiet of the occupants of a dwelling-house` | F1 | 7 |
| s 175(2) | 3487-3488 | Evidence of peace officer (2) In the absence of other evidence, or by ... | fork | `s 175(2) a summary conviction court may infer from the evidence of a peace officer that the disturbance or obstruction occurred` | a power with limits in its own wording: NOTHING outside; seam: s 2 peace officer; F9, F19 | 6 |
| s 176(1) | 3489-3490 | Obstructing or violence to or arrest of officiating clergyman 176 (1) ... | encoded | `s 176(1) the punishment on indictment`<br>`s 176(1) the punishment on summary conviction`<br>`s 176(1) the class of the offence` | penalty from s 787(1) (seam) | 3 |
| s 176(1)(a) | 3491-3491 | (a) by threats or force, unlawfully obstructs or prevents or endeavour... | encoded | `s 176(1)(a) the conduct is the offence of obstructing an officiant by threats or force` | F1 | 8 |
| s 176(1)(b) | 3492-3494 | (b) knowing that an officiant is about to perform, is on their way to ... | encoded | `s 176(1)(b) the conduct is the offence of assaulting or arresting an officiant` | F1 | 4 |
| s 176(2) | 3495-3496 | Disturbing religious worship or certain meetings (2) Every one who wil... | encoded | `s 176(2) the conduct is the offence of disturbing religious worship or certain meetings`<br>`s 176(2) the punishment on summary conviction`<br>`s 176(2) the class of the offence` | F1; penalty from s 787(1) (seam) | 5 |
| s 176(3) | 3497-3498 | Idem (3) Every one who, at or near a meeting referred to in subsection... | encoded | `s 176(3) the conduct is the offence of disturbing the order or solemnity of a meeting`<br>`s 176(3) the punishment on summary conviction`<br>`s 176(3) the class of the offence` | F1; penalty from s 787(1) (seam) | 5 |
| s 177 | 3499-3500 | Trespassing at night 177 Every person who, without lawful excuse, loit... | encoded | `s 177 the conduct is the offence of trespassing at night`<br>`s 177 the punishment on summary conviction`<br>`s 177 the class of the offence` | F1; seams: s 2 night, s 2 dwelling-house | 8 |
| s 178 | 3501-3501 | 178 [Repealed, 2018, c. 29, s. 14] | repealed or blank in this text | `s 178 as the text shows it` | - | 1 |
| s 179 | 3502-3502 | 179 [Repealed, 2019, c. 25, s. 60] | repealed or blank in this text | `s 179 as the text shows it` | - | 1 |
| heading: Nuisances | 3504-3504 | Nuisances | inert (reason 1: not operative) | - | heading | - |
| s 180(1) | 3505-3506 | Common nuisance 180 (1) Every person is guilty of an indictable offenc... | encoded | `s 180(1) the conduct is the offence of committing a common nuisance`<br>`s 180(1) the punishment on indictment`<br>`s 180(1) the punishment on summary conviction`<br>`s 180 the class of the offence` | F1; penalty from s 787(1) (seam) | 8 |
| s 180(1)(a) | 3507-3507 | (a) endangers the lives, safety or health of the public, or | encoded | `s 180(1) the conduct is the offence of committing a common nuisance`<br>`s 180(1) the punishment on indictment`<br>`s 180(1) the punishment on summary conviction`<br>`s 180 the class of the offence` | F1; penalty from s 787(1) (seam) | 8 |
| s 180(1)(b) | 3508-3508 | (b) causes physical injury to any person. | encoded | `s 180(1) the conduct is the offence of committing a common nuisance`<br>`s 180(1) the punishment on indictment`<br>`s 180(1) the punishment on summary conviction`<br>`s 180 the class of the offence` | F1; penalty from s 787(1) (seam) | 8 |
| s 180(2) | 3509-3510 | Definition (2) For the purposes of this section, every one commits a c... | fork | `s 180(2) the person commits a common nuisance` | F11 | 8 |
| s 180(2)(a) | 3511-3511 | (a) endangers the lives, safety, health, property or comfort of the pu... | fork | `s 180(2) the person commits a common nuisance` | F11 | 8 |
| s 180(2)(b) | 3512-3512 | (b) obstructs the public in the exercise or enjoyment of any right tha... | fork | `s 180(2) the person commits a common nuisance` | F11 | 8 |
| s 181 | 3513-3513 | 181 [Repealed, 2019, c. 25, s. 62] | repealed or blank in this text | `s 181 as the text shows it` | - | 1 |
| s 182 | 3514-3515 | Dead body 182 Every person is guilty of an indictable offence and liab... | encoded | `s 182 the conduct is the offence concerning a dead human body`<br>`s 182 the punishment on indictment`<br>`s 182 the punishment on summary conviction`<br>`s 182 the class of the offence` | F1; penalty from s 787(1) (seam) | 6 |
| s 182(a) | 3516-3516 | (a) neglects, without lawful excuse, to perform any duty that is impos... | encoded | `s 182 the conduct is the offence concerning a dead human body`<br>`s 182 the punishment on indictment`<br>`s 182 the punishment on summary conviction`<br>`s 182 the class of the offence` | F1; penalty from s 787(1) (seam) | 6 |
| s 182(b) | 3517-3517 | (b) improperly or indecently interferes with or offers any indignity t... | encoded | `s 182 the conduct is the offence concerning a dead human body`<br>`s 182 the punishment on indictment`<br>`s 182 the punishment on summary conviction`<br>`s 182 the class of the offence` | F1; penalty from s 787(1) (seam) | 6 |

## Fork register (ccc6)

Every ambiguity, the readings seen, the one taken and the text that licenses each. Where a reading is a matter for a lawyer the other reading is stated. A caller must never turn NOTHING into FALSE.

### F1. An offence function whose elements are not all met
- Taken: JUST TRUE when every element is met, NOTHING otherwise ("not covered": the prohibition is limited by its own wording and the case falls outside the limit). A bar or a duty is not an offence function.
- The other reading: JUST FALSE for a person who does less than the offence describes.
- Licensed by: the guide's "In short" sentence: a prohibition limited by its own wording and the case falls outside the limit answers NOTHING; the offence sections say "Every one commits an offence who ..." followed by the elements.
- Rows (71): s 151, s 152(1), s 152(1)(a), s 152(1)(b), s 153(1), s 153(1)(a), s 153(1)(b), s 153(1)(c), s 153.1(1), s 153.1(1)(a), s 153.1(1)(b), s 155(1), s 160(1), s 160(2), s 160(3), s 160(3.1), s 160(5), s 161(4), s 162(1), s 162(1)(a), s 162(1)(b), s 162(1)(c), s 162(4), s 162.1(1), s 162.1(1.1), s 162.2(4), s 163(1), s 163(2), s 163(2)(a), s 163(2)(b), s 163.1(2), s 163.1(3), s 163.1(4), s 163.1(4.1), s 163.1(4.21), s 167(1), s 167(2), s 168(1), s 169.1(1), s 170, s 171, s 171.1(1), s 172(1), s 172.1(1), s 172.1(1)(a), s 172.1(1)(b), s 172.1(1)(c), s 172.2(1), s 172.2(1)(a), s 172.2(1)(b), s 172.2(1)(c), s 173(1), s 173(2), s 174(1), s 174(1)(a), s 174(1)(b), s 175(1)(a), s 175(1)(b), s 175(1)(c), s 175(1)(d), s 176(1)(a), s 176(1)(b), s 176(2), s 176(3), s 177, s 180(1), s 180(1)(a), s 180(1)(b), s 182, s 182(a), s 182(b)

### F2. A scope limit written "when an accused is charged with ..." or "in respect of a complainant under ..."
- Taken: outside the named offences or the age band: NOTHING (ruling (c) of 2026-11-05, a scope limit with no "only").
- The other reading: JUST FALSE, counting "when" as "where" under rulings (b) and (c) of 2026-11-05 (the other reading of limit (3) of 2026-11-12).
- Licensed by: the opening words of the subsections listed in the rows below.
- Rows (10): s 150.1(1), s 150.1(3), s 150.1(4), s 150.1(5), s 156, s 163.1(5), s 164(7), s 171.1(4), s 172.1(4), s 172.2(4)

### F3. A defence whose gate ("if", "where") is unmet inside its scope
- Taken: JUST FALSE, worded "this section gives no defence on these facts", never "no defence at all" (delegated-defences ruling (b) of 2026-11-05).
- The other reading: NOTHING, because a failed "if" is not the text's no in its own words (marginal reading (a) below).
- Licensed by: subsections of the form "it is a defence that ... if ..." and "No person shall be convicted ... if ...".
- Rows (19): s 150.1(2), s 150.1(2)(b), s 150.1(2.1), s 150.1(2.1)(b), s 150.1(2.2), s 150.1(2.2)(a), s 150.1(2.2)(b), s 153.1(5), s 153.1(5)(a), s 153.1(5)(b), s 153.1(5)(c), s 155(3), s 160(3.2), s 162(6), s 162.1(3), s 163(3), s 163.1(6), s 163.1(6)(a), s 163.1(6)(b)

### F4. A bar written "unless" or "except" once the exception is met
- Taken: JUST FALSE when the "unless" is met (the bar does not apply); JUST TRUE when the bar applies; NOTHING outside the bar's own scope. A bar is a prohibition, so the function answers "does the bar apply", never "is there a defence".
- The other reading: NOTHING when the "unless" is met (an exception is not a flat negative).
- Licensed by: the "unless" in each row below; one of the six case-by-case sites of the ruling typed 2026-11-05T10:25:24Z.
- Rows (13): s 150.1(3), s 150.1(4), s 150.1(5), s 150.1(6), s 156, s 163.1(5), s 164(7), s 169.1(3), s 171.1(4), s 172(4), s 172.1(4), s 172.2(4), s 174(3)

### F5. Section 150.1(1) is "Subject to subsections (2) to (2.2)" and the exceptions apply
- Taken: `s 150.1(1) it is not a defence that the complainant consented` answers JUST FALSE when the defence of subsection (2), (2.1) or (2.2) applies.
- The other reading: NOTHING, as the exceptions are in other subsections.
- Licensed by: the words "Subject to subsections (2) to (2.2)".
- Rows (1): s 150.1(1)

### F6. A duty of a court or judge ("shall") whose "if" or "where" is unmet
- Taken: JUST FALSE (limit (2) of the ruling of 2026-11-12: a duty and the provision's own question keep JUST FALSE).
- The other reading: NOTHING.
- Licensed by: the "shall" in each row below.
- Rows (16): s 153.1(6), s 161(1), s 161(1)(b), s 161(1)(c), s 161(1)(d), s 163.1(4.3), s 164(2), s 164(5), s 164.1(5.1), s 164.1(7), s 164.2(2), s 164.3(2), s 164.3(3), s 164.3(6), s 164.3(6)(a), s 164.3(6)(b)

### F7. Section 150.1(1) is not made subject to subsection (2.3), and (2.3) gives a defence to the married accused
- Taken: where both apply the composite `s 150.1 whether it is a defence that the complainant consented` returns a constructor of its own, `s 150.1 subsection (1) says consent is not a defence and subsection (2.3) says it is, and the text does not say which prevails`.
- The other reading: the later subsection prevails (consent is a defence), or the earlier does.
- Licensed by: the text names (2) to (2.2) in (1) and not (2.3) (src:3002, src:3016); finding 1.
- Rows (2): s 150.1(1), s 150.1(2.3)

### F8. "less than two years older" in the exceptions of subsections (2) and (2.1)
- Taken: the age difference is LESS THAN 2 (a younger accused is included).
- The other reading: the accused is older by less than two years (a younger accused is outside).
- Licensed by: the words "is less than two years older than the complainant" read as a difference.
- Rows (4): s 150.1(2), s 150.1(2)(a), s 150.1(2.1), s 150.1(2.1)(a)

### F9. A function named "may" whose gate is "where", "when" or "upon" (the limb of a mixed gate included)
- Taken: JUST FALSE for the failed gate, as the guide's ruling (b) of 2026-11-05 gives, which counts "when", "upon" and "whenever" as "where". LISTED, not decided, in the Name-test sweep subsection below with a count: 3 whole-gate functions and 6 mixed-gate functions answered limb by limb.
- The other reading: NOTHING, as the guide's line on grants points ("a question for a lawyer", brief, limit (3)).
- Licensed by: ruling (b) of 2026-11-05 and limit (3) of 2026-11-12.
- Rows (15): s 160(4), s 160(4)(b), s 161(1), s 161(1)(b), s 161(1)(c), s 161(1)(d), s 161(3), s 162.2(1), s 162.2(3), s 164.1(6), s 164.2(1), s 164.2(1)(a), s 164.2(1)(b), s 164.3(1), s 175(2)

### F10. Section 161(1.1): "The offences for the purpose of subsection (1) are (a) ... (d)"
- Taken: a closed list, as the keel reads s 2.3(1): an offence none of (a) to (d) names is JUST FALSE.
- The other reading: NOTHING (the list is not closed with "only").
- Licensed by: the words "The offences for the purpose of subsection (1) are".
- Rows (5): s 161(1.1), s 161(1.1)(a), s 161(1.1)(b), s 161(1.1)(c), s 161(1.1)(d)

### F11. An interpretation written "a person is X who ..." and not "X means" (s 163.1(4.2), s 174(2), s 180(2))
- Taken: NOTHING for a case outside it (the clause is limited by its own wording).
- The other reading: JUST FALSE, reading it as a "means" definition.
- Licensed by: the words "a person accesses ... who", "a person is nude who", "every one commits a common nuisance who".
- Rows (5): s 163.1(4.2), s 174(2), s 180(2), s 180(2)(a), s 180(2)(b)

### F12. Section 164(8) "court means (a) in the Province of Quebec ... (e) in Nunavut ..."
- Taken: a "means" list: a court that is not named for the province is JUST FALSE.
- The other reading: NOTHING (the list is not closed with "only").
- Licensed by: the word "means".
- Rows (6): s 164(8) "court", s 164(8) "court" (a), s 164(8) "court" (a.1), s 164(8) "court" (b), s 164(8) "court" (d), s 164(8) "court" (e)

### F13. Section 164.1(2): "Within a reasonable time after receiving the information ..., the judge shall cause notice to be given"
- Taken: the function answers whether the duty has arisen (the judge has received the information); "a reasonable time" is not a number and is not computed.
- The other reading: an input for the time taken.
- Licensed by: the words "a reasonable time".
- Rows (1): s 164.1(2)

### F14. Section 164.3(6): the Attorney General "shall direct that (a) the thing be returned ... or (b) an amount equal to its value be paid"
- Taken: the function answers whether the Attorney General must direct one or the other; it does not say which, or when.
- The other reading: two functions, one for (a) and one for (b).
- Licensed by: the words "the thing be returned to the applicant ... or ... an amount equal to the value".
- Rows (3): s 164.3(6), s 164.3(6)(a), s 164.3(6)(b)

### F15. Section 153(1.2): the judge "may infer ... from the nature and circumstances of the relationship, including (a) to (d)"
- Taken: JUST TRUE for the four named matters and "another circumstance of the relationship"; NOTHING for a matter that is not part of the nature and circumstances of the relationship.
- The other reading: JUST FALSE for the matter outside.
- Licensed by: the word "including" (an open list).
- Rows (5): s 153(1.2), s 153(1.2)(a), s 153(1.2)(b), s 153(1.2)(c), s 153(1.2)(d)

### F16. Section 169: "an offence under section 163, 165, 167 or 168"
- Taken: section 165 stays named, as the text names it, though it is repealed in this text (finding 5).
- The other reading: section 165 dropped as repealed.
- Licensed by: src:3378.
- Rows (1): s 169

### F17. Two punishments in one limb: s 155(2) (a minimum of five years if the other person is under 16, none otherwise) and s 162.1(1)(a) (a maximum of 10 years, or 14 if the accused knew or ought to have known that aggravated sexual assault was being or had just been committed)
- Taken: both are listed, one function each for the cases the text gives, and the seat asks the fact that picks one.
- The other reading: one function carrying the greater penalty.
- Licensed by: src:3092 and src:3177-3179.
- Rows (2): s 155(2), s 162.1(1)(a)

### F18. Section 168(2): "Subsection (1) does not apply to a person who (a) ... (b) ... or (c) ..."
- Taken: a flat negative: JUST FALSE for a person within one of the four limbs ((a), (b), (c)(i), (c)(ii)), NOTHING for anyone else (the subsection says nothing of them).
- The other reading: JUST FALSE for everyone not within a limb.
- Licensed by: the words "does not apply to a person who".
- Rows (4): s 168(2), s 168(2)(a), s 168(2)(b), s 168(2)(c)

### F19. A function named "may" whose gate is an "if" or a scope limit
- Taken: NOTHING (limit (1) of the ruling of 2026-11-12: a grant turned into a bar is the error the ruling guards against). 25 functions: the 19 listed in the Name-test sweep subsection and the "if" and scope limbs of the 6 mixed-gate functions.
- The other reading: JUST FALSE.
- Licensed by: the ruling of 2026-11-12, limit (1); the guide's sentence "limits a grant or prohibition in its own wording and the case falls outside the limit".
- Rows (41): s 153(1.2), s 153(1.2)(a), s 153(1.2)(b), s 153(1.2)(c), s 153(1.2)(d), s 160(4), s 160(4)(a), s 160(4)(b), s 161(1)(a), s 161(1)(a.1), s 161(2), s 161(2)(a), s 161(2)(b), s 161(3), s 162.2(2), s 162.2(3), s 164(1), s 164(1)(a), s 164(1)(b), s 164(3), s 164(4), s 164.1(1), s 164.1(1)(a), s 164.1(1)(b), s 164.1(1)(c), s 164.1(2), s 164.1(3), s 164.1(4), s 164.1(5), s 164.2(1), s 164.2(1)(a), s 164.2(1)(b), s 164.2(2), s 164.2(3), s 164.2(4), s 164.3(1), s 164.3(4), s 164.3(4)(a), s 164.3(4)(b), s 164.3(5), s 175(2)

### Name-test sweep of 2026-11-12

The class is every layer-1 function whose name says "may" (a grant or a power): 29 in this range, found by a scan of the function names and checked against the lists below. No function in the range is named "it is lawful ..." and none is named "entitled".

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 0 | 1 | 9 (3 whole-gate, 6 answered limb by limb) | 0 |

Outside the sweep: functions named "it is lawful ...": scoped name kept 0, unscoped name retitled to the scoped form 0. Already NOTHING with an "if" or scope gate, so nothing to flip: 19, and the "if" and scope limbs of the 6 limb-by-limb functions.

Names scanned: every layer-1 function name containing "may", "permitted", "power", "authorised", "authorized" or "entitled". "may" gives the 29 above; the other words give `s 169.1(2) the person is considered to be in a position of trust, power or authority towards the young person`, which is a status ("a position of trust, power or authority"), not a grant or a power, and so is outside the class.

Arithmetic: 29 = 19 already NOTHING + 3 whole-gate + 6 limb by limb + 1 closed by the text.

**Flipped to NOTHING (0).** Every "may" function with an "if" or scope gate already answered NOTHING when the sweep began, so no function was flipped and no caller changed. These 19 are listed because they are the class the first limit of the ruling governs:

- `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young person`
- `s 160(4)(a) the court may make an order prohibiting the accused`
- `s 161(1)(a) to (d) the order may prohibit the offender from`
- `s 161(1)(a.1) the order may prohibit the offender from being near the place`
- `s 161(2) the prohibition may be for the duration`
- `s 162.2(2) the prohibition may be for the period`
- `s 164(1) a judge may issue a warrant authorizing seizure of copies of the material`
- `s 164(3) the person may appear and be represented in the proceedings to oppose the forfeiture`
- `s 164(4) the court may make an order declaring the thing forfeited to His Majesty in right of the province`
- `s 164.1(1) the judge may order the custodian of the computer system`
- `s 164.1(2) the judge may order the custodian to post the text of the notice`
- `s 164.1(3) the person may appear and be represented in the proceedings to oppose the order`
- `s 164.1(4) the court may proceed ex parte`
- `s 164.1(5) the court may order the custodian to delete the material`
- `s 164.2(2) the court may hear the person and declare the nature and extent of the person's interest`
- `s 164.2(3) the person may appeal to the court of appeal`
- `s 164.2(4) the Attorney General may appeal to the court of appeal`
- `s 164.3(4) the judge may declare that the applicant's interest in the thing is not affected by the forfeiture`
- `s 164.3(5) the person may appeal to the court of appeal`

**Kept JUST FALSE because the text closes the gate itself (1).**

- `s 164.3(2) the day fixed for the hearing is one the judge may fix`: the text is a duty with a floor, "The judge shall fix a day -- not less than thirty days after the application is made -- for its hearing" (src:3349), so the function keeps JUST FALSE as a duty and as the provision's own question (test 2), not as a grant whose gate failed.

**Listed: where / when / upon-kind gate, the whole gate (3).** JUST FALSE when the gate fails, as the guide's ruling (b) of 2026-11-05 gives; the other reading is NOTHING (fork F9).

- `s 161(1) the court may make an order of prohibition`
- `s 162.2(1) the court may make an order prohibiting the offender from using the Internet or other digital network`
- `s 164.1(6) the court may order the destruction of the electronic copy in the court's possession`

**Listed: mixed gates, answered limb by limb (6).** The upon-kind or period limb answers JUST FALSE (ruling (b) or the periods ruling (a)); the "if" and scope limbs answer NOTHING (limit (1) and ruling (c)). In each of the five functions this sweep edited the first branch is the upon-kind limb and a `LIMB BY LIMB` comment sits above its GIVEN block; `s 164.3(1)`, already split before the sweep, tests its scope limbs first and its period limb last.

- `s 160(4)(b) the court may order the accused to pay the reasonable costs of the animal's care`: the application or own-motion limb ("on application of the Attorney General or on its own motion"); changed by this sweep.
- `s 161(3) the court may vary the conditions prescribed in the order`: the application limb ("on application of the offender or the prosecutor"); changed by this sweep.
- `s 162.2(3) the court may vary the conditions prescribed in the order`: the application limb ("on application of the offender or the prosecutor"); changed by this sweep.
- `s 164.2(1) the court may order the thing forfeited to Her Majesty`: the application limb ("On application of the Attorney General"); changed by this sweep.
- `s 175(2) a summary conviction court may infer from the evidence of a peace officer that the disturbance or obstruction occurred`: the evidence limb ("In the absence of other evidence, or by way of corroboration of other evidence"); changed by this sweep.
- `s 164.3(1) the person may apply for relief from forfeiture`: the period limb ("Within thirty days after an order ... is made", period ruling (a)); already limb by limb before the sweep.

**Listed as "entitled" (0).** No function in the range is named for an entitlement.

**Outside the sweep: named "it is lawful ..." (scoped 0, unscoped retitled 0).** No layer-1 function and no seat question in the range has that name.

Assertions restated by the sweep, each in place with a `RECONCILED 2026-11-12` comment: four in the layer-1 tests (s 160(4)(b), s 161(3), s 164.2(1) and s 175(2)) and one in the seat cases (the s 164.2(1) case in which the Attorney General did not apply: NOTHING before, JUST FALSE now). Two layer-1 assertions were added: s 161(3) with another court and no application (JUST FALSE), and s 162.2(3) with no application by the offender or the prosecutor (JUST FALSE). Four seat cases were added for the limb-by-limb functions, each JUST FALSE for the upon-kind limb: s 160(4)(b), s 161(3), s 162.2(3) (a case of a seat question added in this pass) and s 175(2).

### Reading a result: FALSE and NOTHING (ccc6)

- A **no** (`JUST FALSE`) in this part is the text saying no in its own words: a "means" definition (a court, a young person, a child) that the case is outside; a flat negative ("does not apply to a person who", "No person shall be convicted", "It is not a defence"); an "unless" that is met; a period or a "where / when" gate that has failed for a duty or for the provision's own question; and a defence whose condition is not proved ("this section gives no defence on these facts", never "no defence at all").
- **Not covered** (`NOTHING`, or a constructor that says so) is everything the text does not answer: an offence in which an element is not met (the text prohibits an act of a described kind and a person who does less is outside it); a power or a bar limited by its own wording where the case falls outside the limit; an open list ("includes"); a term the Act leaves to another Part (s 2, s 286.4, s 320.103, s 787(1)); a matter on which the section is silent.
- A result of NOTHING is **not** "not an offence" and **not** "no defence". A caller never turns it into FALSE; the seat questions say "does the bar apply" or "does the section give me a defence" and return the function's answer unchanged.
- The guide's sentence, copied from the brief: Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

## Jural relations (ccc6)

One row per provision that creates a relation, from the coverage table; the party columns are generated by `work/mknotes.py` from the form of the encoded function (an offence, a punishment, a power, a duty, a bar, a defence), and the rule column names the function. Hohfeld's correlatives: claim / duty, privilege / no-right, power / liability, immunity / disability. Each relation is stated once, from the side of its holder.

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | relation | L4 rule |
| --- | --- | --- | --- | --- |
| s 150.1(1) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the ground | `s 150.1(1) it is not a defence that the complainant consented`<br>`s 150.1(1) the offence is under section 151 or 152 or subsection 153(1), 160(3) or 173(2)`<br>`s 150.1(1) the offence is under section 271, 272 or 273` (and 1 more) |
| s 150.1(2) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 150.1(2) it is a defence that the complainant consented, complainant aged 12 or 13`<br>`s 150.1(2) the offence is under section 151 or 152, subsection 173(2) or section 271` |
| s 150.1(2)(a) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 150.1(2) it is a defence that the complainant consented, complainant aged 12 or 13` |
| s 150.1(2.1) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 150.1(2.1) it is a defence that the complainant consented, complainant aged 14 or 15`<br>`s 150.1(2.1) the offence is under section 151 or 152, subsection 173(2) or section 271` |
| s 150.1(2.1)(a) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 150.1(2.1) it is a defence that the complainant consented, complainant aged 14 or 15` |
| s 150.1(2.2) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or more years older`<br>`s 150.1(2.2) the charge is one that subsection (2.2) speaks to` |
| s 150.1(2.2)(a) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or more years older` |
| s 150.1(2.3) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 150.1(2.3) it is a defence that the complainant consented, the accused being married to the complainant`<br>`s 150.1 whether it is a defence that the complainant consented` |
| s 150.1(3) | the accused | the prosecutor | immunity / disability: no trial or proceeding without the condition | `s 150.1(3) no person aged twelve or thirteen shall be tried: the bar applies`<br>`s 150.1(3) the offence is under section 151 or 152 or subsection 173(2)` |
| s 150.1(4) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 150.1(4) the belief that the complainant was 16 or more is not a defence: the bar applies`<br>`s 150.1(4) the offence is under section 151 or 152, subsection 160(3) or 173(2), or section 271, 272 or 273` |
| s 150.1(5) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 150.1(5) the belief that the complainant was 18 or more is not a defence: the bar applies`<br>`s 150.1(5) the offence is under section 153, 170, 171, 172 or 279.011 or subsection 279.02(2), 279.03(2), 286.1(2), 286.2(2) or 286.3(2)` |
| s 150.1(6) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 150.1(6) the accused cannot raise a mistaken belief in the age of the complainant to invoke subsection (2) or (2.1): the bar applies` |
| s 151 | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 151 the conduct is sexual interference`<br>`s 151 the class of the offence` |
| s 151(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 151(a) the punishment on indictment` |
| s 151(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 151(b) the punishment on summary conviction` |
| s 152(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 152(1) the conduct is the offence of invitation to sexual touching or exposure` |
| s 152(2)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 152(2)(a) the punishment on indictment` |
| s 152(2)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 152(2)(b) the punishment on summary conviction` |
| s 153(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 153(1) the conduct is the offence of sexual exploitation` |
| s 153(1.1)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 153(1.1)(a) the punishment on indictment` |
| s 153(1.1)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 153(1.1)(b) the punishment on summary conviction` |
| s 153(1.2) | the court | the accused | power / liability: the court may draw the inference | `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young person` |
| s 153.1(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 153.1(1) the conduct is the offence of sexual exploitation of a person with a disability` |
| s 153.1(1.1)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 153.1(1.1)(a) the punishment on indictment` |
| s 153.1(1.1)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 153.1(1.1)(b) the punishment on summary conviction` |
| s 153.1(5) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 153.1(5) the belief that the complainant consented is not a defence: the bar applies` |
| s 153.1(6) | the person affected | the court or judge | claim / duty | `s 153.1(6) the judge must instruct the jury to consider the presence or absence of reasonable grounds for the belief`<br>`s 153.1(6) the judge's duty to instruct the jury` |
| s 155(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 155(1) the conduct is incest` |
| s 155(2) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 155(2) the punishment`<br>`s 155 the class of the offence` |
| s 160(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 160(1) the conduct is the offence of bestiality`<br>`s 160(1) the punishment on indictment`<br>`s 160(1) the punishment on summary conviction` (and 1 more) |
| s 160(2) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 160(2) the conduct is the offence of compelling the commission of bestiality`<br>`s 160(2) the punishment on indictment`<br>`s 160(2) the punishment on summary conviction` (and 1 more) |
| s 160(3) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 160(3) the conduct is the offence of bestiality in the presence of, or by inciting, a person under 16`<br>`s 160(3) the class of the offence` |
| s 160(3)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 160(3)(a) the punishment on indictment` |
| s 160(3)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 160(3)(b) the punishment on summary conviction` |
| s 160(3.1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 160(3.1) the conduct is the offence of publishing or distributing a representation of bestiality` |
| s 160(3.2) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 160(3.2) section 160 gives a defence of public good against a charge under subsection (3.1)` |
| s 160(3.4)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 160(3.4)(a) the punishment on indictment` |
| s 160(3.4)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 160(3.4)(b) the punishment on summary conviction` |
| s 160(4) | the court | the person against whom the order is made | power / liability | `s 160(4)(a) the court may make an order prohibiting the accused`<br>`s 160(4)(b) the court may order the accused to pay the reasonable costs of the animal's care` |
| s 160(4)(a) | the court | the person against whom the order is made | power / liability | `s 160(4)(a) the court may make an order prohibiting the accused`<br>`s 160(4)(a) the shortest period of the order` |
| s 160(4)(b) | the court | the person against whom the order is made | power / liability | `s 160(4)(b) the court may order the accused to pay the reasonable costs of the animal's care` |
| s 160(5) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 160(5) the conduct is the offence of contravening an order made under paragraph (4)(a)`<br>`s 160(5) the punishment on summary conviction`<br>`s 160(5) the class of the offence` |
| s 161(1) | the court | the person against whom the order is made | power / liability | `s 161(1) the court sentences or discharges the offender in the case the subsection describes`<br>`s 161(1) the court shall consider making an order of prohibition`<br>`s 161(1) the court may make an order of prohibition` |
| s 161(1)(a) | the court | the person against whom the order is made | power / liability | `s 161(1)(a) to (d) the order may prohibit the offender from` |
| s 161(1)(a.1) | the court | the person against whom the order is made | power / liability | `s 161(1)(a) to (d) the order may prohibit the offender from`<br>`s 161(1)(a.1) the order may prohibit the offender from being near the place`<br>`s 161(1)(a.1) the distance in kilometres` |
| s 161(2) | the court | the person against whom the order is made | power / liability | `s 161(2) the prohibition may be for the duration`<br>`s 161(2) the date on which the prohibition begins` |
| s 161(3) | the court | the person against whom the order is made | power / liability | `s 161(3) the court may vary the conditions prescribed in the order` |
| s 161(4) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 161(4) the conduct is the offence of not complying with an order of prohibition`<br>`s 161(4) the class of the offence`<br>`s 161(4) the offender SHANT do what the order of prohibition forbids` |
| s 161(4)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 161(4)(a) the punishment on indictment` |
| s 161(4)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 161(4)(b) the punishment on summary conviction` |
| s 162(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 162(1) the conduct is the offence of voyeurism` |
| s 162(3) | a peace officer acting under a warrant issued under section 487.01 | the Crown (the public, through the prosecutor) | immunity / disability: paragraphs (1)(a) and (b) do not apply to the officer | `s 162(3) paragraphs (1)(a) and (1)(b) apply to the person` |
| s 162(4) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 162(4) the conduct is the offence of printing, publishing, etc. a voyeuristic recording` |
| s 162(5)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162(5)(a) the punishment on indictment` |
| s 162(5)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162(5)(b) the punishment on summary conviction` |
| s 162(6) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 162(6) section 162 gives a defence of public good` |
| s 162.1(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 162.1(1) the conduct is the offence of publishing an intimate image without consent`<br>`s 162.1(1) the class of the offence` |
| s 162.1(1)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162.1(1)(a) the punishment on indictment` |
| s 162.1(1)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162.1(1)(b) the punishment on summary conviction` |
| s 162.1(1.1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 162.1(1.1) the conduct is the offence of threatening to publish an intimate image`<br>`s 162.1(1.1) the class of the offence` |
| s 162.1(1.1)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162.1(1.1)(a) the punishment on indictment` |
| s 162.1(1.1)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162.1(1.1)(b) the punishment on summary conviction` |
| s 162.1(3) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 162.1(3) section 162.1 gives a defence of public good` |
| s 162.2(1) | the court | the person against whom the order is made | power / liability | `s 162.2(1) the court may make an order prohibiting the offender from using the Internet or other digital network` |
| s 162.2(2) | the court | the person against whom the order is made | power / liability | `s 162.2(2) the prohibition may be for the period` |
| s 162.2(3) | the court | the person against whom the order is made | power / liability | `s 162.2(3) the court may vary the conditions prescribed in the order` |
| s 162.2(4) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 162.2(4) the conduct is the offence of not complying with an order of prohibition`<br>`s 162.2(4) the class of the offence` |
| s 162.2(4)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162.2(4)(a) the punishment on indictment` |
| s 162.2(4)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 162.2(4)(b) the punishment on summary conviction` |
| s 163(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 163(1) the conduct is the offence of making or publishing obscene matter` |
| s 163(2) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 163(2) the conduct is the offence of selling obscene matter or exhibiting an indecent show` |
| s 163(3) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 163(3) section 163 gives a defence of public good` |
| s 163.1(2) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 163.1(2) the conduct is the offence of making, printing or publishing child sexual abuse and exploitation material`<br>`s 163.1(2) the punishment`<br>`s 163.1(2) the class of the offence` |
| s 163.1(3) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 163.1(3) the conduct is the offence of distributing child sexual abuse and exploitation material`<br>`s 163.1(3) the punishment`<br>`s 163.1(3) the class of the offence` |
| s 163.1(4) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 163.1(4) the conduct is the offence of possessing child sexual abuse and exploitation material`<br>`s 163.1(4) the class of the offence` |
| s 163.1(4)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 163.1(4)(a) the punishment on indictment` |
| s 163.1(4)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 163.1(4)(b) the punishment on summary conviction` |
| s 163.1(4.1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 163.1(4.1) the conduct is the offence of accessing child sexual abuse and exploitation material`<br>`s 163.1(4.1) the class of the offence` |
| s 163.1(4.1)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 163.1(4.1)(a) the punishment on indictment` |
| s 163.1(4.1)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 163.1(4.1)(b) the punishment on summary conviction` |
| s 163.1(4.21) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 163.1(4.21) the conduct is the offence of threatening to publish child sexual abuse and exploitation material`<br>`s 163.1(4.21) the class of the offence` |
| s 163.1(4.21)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 163.1(4.21)(a) the punishment on indictment` |
| s 163.1(4.21)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 163.1(4.21)(b) the punishment on summary conviction` |
| s 163.1(4.3) | the person affected | the court or judge | claim / duty | `s 163.1(4.3) the court must consider the intent to make a profit as an aggravating factor`<br>`s 163.1(4.3) the sentencing court's duty to consider the intent to make a profit` |
| s 163.1(5) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 163.1(5) the belief that the person shown was eighteen or more is not a defence: the bar applies` |
| s 163.1(6) | the accused | the Crown and the court | immunity / disability: no conviction on these facts | `s 163.1(6) section 163.1 gives a defence` |
| s 164(1) | the court | the person against whom the order is made | power / liability | `s 164(1) a judge may issue a warrant authorizing seizure of copies of the material` |
| s 164(2) | the occupier of the premises | the judge | claim / duty | `s 164(2) the judge issued the summons within seven days of the day on which the warrant was issued`<br>`s 164(2) the judge's duty to issue the summons` |
| s 164(3) | the person | the court | privilege / no-right: the person may take part | `s 164(3) the person may appear and be represented in the proceedings to oppose the forfeiture` |
| s 164(4) | the court | the person against whom the order is made | power / liability | `s 164(4) the court may make an order declaring the thing forfeited to His Majesty in right of the province` |
| s 164(5) | the person affected | the court or judge | claim / duty | `s 164(5) the court must order the thing restored to the person from whom it was seized`<br>`s 164(5) the thing is to be restored now` |
| s 164(6) | a person who appeared in the proceedings | the court of appeal | power / liability: the court of appeal must hear the appeal | `s 164(6) an appeal lies from the order` |
| s 164(7) | the accused | the prosecutor | immunity / disability: no trial or proceeding without the condition | `s 164(7) no proceedings shall be instituted or continued without the consent of the Attorney General: the bar applies` |
| s 164.1(1) | the court | the person against whom the order is made | power / liability | `s 164.1(1) the judge may order the custodian of the computer system` |
| s 164.1(2) | the person affected | the court or judge | claim / duty | `s 164.1(2) the judge must cause notice to be given to the person who posted the material`<br>`s 164.1(2) the judge may order the custodian to post the text of the notice` |
| s 164.1(3) | the person | the court | privilege / no-right: the person may take part | `s 164.1(3) the person may appear and be represented in the proceedings to oppose the order` |
| s 164.1(4) | the court | the person against whom the order is made | power / liability | `s 164.1(4) the court may proceed ex parte` |
| s 164.1(5) | the court | the person against whom the order is made | power / liability | `s 164.1(5) the court may order the custodian to delete the material` |
| s 164.1(5.1) | the person affected | the court or judge | claim / duty | `s 164.1(5.1) the court must order the custodian to delete the material within 48 hours`<br>`s 164.1(5.1) the material was deleted within 48 hours after the order was made`<br>`s 164.1(5.1) the custodian's duty to delete the intimate image` |
| s 164.1(6) | the court | the person against whom the order is made | power / liability | `s 164.1(6) the court may order the destruction of the electronic copy in the court's possession` |
| s 164.1(7) | the person affected | the court or judge | claim / duty | `s 164.1(7) the court must order the electronic copy returned and terminate the order made under paragraph (1)(b)` |
| s 164.1(9) | the person against whom the order is made | the court | immunity / disability: the order does not take effect yet | `s 164.1(9) the order cannot yet take effect` |
| s 164.2(1) | the court | the person against whom the order is made | power / liability | `s 164.2(1) the court may order the thing forfeited to Her Majesty` |
| s 164.2(2) | the person affected | the court or judge | claim / duty | `s 164.2(2) the court must cause notice to be given to the person`<br>`s 164.2(2) the court may hear the person and declare the nature and extent of the person's interest` |
| s 164.2(3) | the person | the court | power / liability: the court must hear it | `s 164.2(3) the person may appeal to the court of appeal` |
| s 164.2(4) | the person | the court | power / liability: the court must hear it | `s 164.2(4) the Attorney General may appeal to the court of appeal` |
| s 164.3(1) | the person | the court | power / liability: the court must hear it | `s 164.3(1) the person may apply for relief from forfeiture`<br>`s 164.3(1) the claimant's permission to apply` |
| s 164.3(2) | the court | the person against whom the order is made | power / liability | `s 164.3(2) the day fixed for the hearing is one the judge may fix` |
| s 164.3(3) | the Attorney General | the applicant for relief | claim / duty | `s 164.3(3) the applicant served notice on the Attorney General at least fifteen days before the hearing`<br>`s 164.3(3) the applicant's duty to serve notice on the Attorney General` |
| s 164.3(4) | the court | the person against whom the order is made | power / liability | `s 164.3(4) the judge may declare that the applicant's interest in the thing is not affected by the forfeiture` |
| s 164.3(5) | the person | the court | power / liability: the court must hear it | `s 164.3(5) the person may appeal to the court of appeal` |
| s 164.3(6) | the person who obtained the order | the Attorney General | claim / duty | `s 164.3(6) the Attorney General must direct that the thing be returned or its value paid` |
| s 167(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 167(1) the conduct is the offence of presenting an immoral theatrical performance` |
| s 167(2) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 167(2) the conduct is the offence of taking part in an immoral theatrical performance` |
| s 168(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 168(1) the conduct is the offence of mailing obscene matter` |
| s 168(2) | a person who prints or publishes the matter in one of the four ways | the Crown (the public, through the prosecutor) | immunity / disability: s 168(1) does not apply to the person | `s 168(2) subsection (1) applies to the person` |
| s 169(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 169(a) the punishment on indictment` |
| s 169(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 169(b) the punishment on summary conviction` |
| s 169.1(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 169.1(1) the conduct is the offence of recruiting a young person to an offence`<br>`s 169.1 the class of the offence` |
| s 169.1(3) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 169.1(3) the belief that the young person was at least 18 is not a defence: the bar applies` |
| s 169.1(4)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 169.1(4)(a) the punishment on indictment` |
| s 169.1(4)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 169.1(4)(b) the punishment on summary conviction` |
| s 170 | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 170 the conduct is the offence of a parent or guardian procuring a person under 18 for sexual activity`<br>`s 170 the punishment`<br>`s 170 the class of the offence` |
| s 171 | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 171 the conduct is the offence of a householder permitting prohibited sexual activity`<br>`s 171 the punishment`<br>`s 171 the class of the offence` |
| s 171.1(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 171.1(1) the conduct is the offence of making sexually explicit material available to a child`<br>`s 171.1(1) the person is, or the accused believes the person is, under the age` |
| s 171.1(2)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 171.1(2)(a) the punishment on indictment` |
| s 171.1(2)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 171.1(2)(b) the punishment on summary conviction` |
| s 171.1(3) | the prosecutor | the accused | power / liability: the presumption works for the prosecutor | `s 171.1(3) the evidence is proof that the accused believed that the person was under that age` |
| s 171.1(4) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 171.1(4) the belief that the person was at least the age is not a defence: the bar applies` |
| s 172(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 172(1) the conduct is the offence of corrupting children`<br>`s 172 the class of the offence` |
| s 172(1)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 172(1)(a) the punishment on indictment` |
| s 172(1)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 172(1)(b) the punishment on summary conviction` |
| s 172(4) | the accused | the prosecutor | immunity / disability: no trial or proceeding without the condition | `s 172(4) no proceedings shall be commenced without the consent of the Attorney General: the bar applies` |
| s 172.1(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 172.1(1) the conduct is the offence of luring a child` |
| s 172.1(2)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 172.1(2)(a) the punishment on indictment` |
| s 172.1(2)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 172.1(2)(b) the punishment on summary conviction` |
| s 172.1(3) | the prosecutor | the accused | power / liability: the presumption works for the prosecutor | `s 172.1(3) the evidence is proof that the accused believed that the person was under that age` |
| s 172.1(4) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 172.1(4) the belief that the person was at least the age is not a defence: the bar applies` |
| s 172.2(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 172.2(1) the conduct is the offence of agreeing or arranging to commit a sexual offence against a child` |
| s 172.2(2)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 172.2(2)(a) the punishment on indictment` |
| s 172.2(2)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 172.2(2)(b) the punishment on summary conviction` |
| s 172.2(3) | the prosecutor | the accused | power / liability: the presumption works for the prosecutor | `s 172.2(3) the evidence is proof that the accused believed that the person was under that age` |
| s 172.2(4) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the belief | `s 172.2(4) the belief that the person was at least the age is not a defence: the bar applies` |
| s 172.2(5) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the ground | `s 172.2(5)(a) it is not a defence that the person with whom the accused agreed was a peace officer or acting under the direction of one`<br>`s 172.2(5)(b) it is not a defence that the person referred to did not exist` |
| s 172.2(5)(a) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the ground | `s 172.2(5)(a) it is not a defence that the person with whom the accused agreed was a peace officer or acting under the direction of one` |
| s 172.2(5)(b) | the Crown (the public, through the prosecutor) | the accused | immunity / disability: the accused cannot rely on the ground | `s 172.2(5)(b) it is not a defence that the person referred to did not exist` |
| s 173(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 173(1) the conduct is the offence of an indecent act`<br>`s 173(1) the class of the offence` |
| s 173(1)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 173(1)(a) the punishment on indictment` |
| s 173(1)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 173(1)(b) the punishment on summary conviction` |
| s 173(2) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 173(2) the conduct is the offence of exposure to a person under 16`<br>`s 173(2) the class of the offence` |
| s 173(2)(a) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 173(2)(a) the punishment on indictment` |
| s 173(2)(b) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 173(2)(b) the punishment on summary conviction` |
| s 174(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 174(1) the conduct is the offence of nudity`<br>`s 174(1) the punishment on summary conviction`<br>`s 174(1) the class of the offence` |
| s 174(3) | the accused | the prosecutor | immunity / disability: no trial or proceeding without the condition | `s 174(3) no proceedings shall be commenced without the consent of the Attorney General: the bar applies` |
| s 175(1) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 175(1) the punishment on summary conviction`<br>`s 175(1) the class of the offence` |
| s 175(1)(a) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 175(1)(a) the conduct is the offence of causing a disturbance in or near a public place` |
| s 175(1)(b) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 175(1)(b) the conduct is the offence of an indecent exhibition in a public place` |
| s 175(1)(c) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 175(1)(c) the conduct is the offence of loitering in a public place and obstructing persons` |
| s 175(1)(d) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 175(1)(d) the conduct is the offence of disturbing the peace and quiet of the occupants of a dwelling-house` |
| s 175(2) | the court | the accused | power / liability: the court may draw the inference | `s 175(2) a summary conviction court may infer from the evidence of a peace officer that the disturbance or obstruction occurred` |
| s 176(1) | the sentencing court | the offender | power / liability: the court may impose up to the stated punishment | `s 176(1) the punishment on indictment`<br>`s 176(1) the punishment on summary conviction`<br>`s 176(1) the class of the offence` |
| s 176(1)(a) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 176(1)(a) the conduct is the offence of obstructing an officiant by threats or force` |
| s 176(1)(b) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 176(1)(b) the conduct is the offence of assaulting or arresting an officiant` |
| s 176(2) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 176(2) the conduct is the offence of disturbing religious worship or certain meetings`<br>`s 176(2) the punishment on summary conviction`<br>`s 176(2) the class of the offence` |
| s 176(3) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 176(3) the conduct is the offence of disturbing the order or solemnity of a meeting`<br>`s 176(3) the punishment on summary conviction`<br>`s 176(3) the class of the offence` |
| s 177 | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 177 the conduct is the offence of trespassing at night`<br>`s 177 the punishment on summary conviction`<br>`s 177 the class of the offence` |
| s 180(1) | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 180(1) the conduct is the offence of committing a common nuisance`<br>`s 180(1) the punishment on indictment`<br>`s 180(1) the punishment on summary conviction` (and 1 more) |
| s 182 | the Crown (the public, through the prosecutor) | every person (the accused) | claim / duty: the duty not to do the act; a flat prohibition, so the prohibition is derived (ruling N2) | `s 182 the conduct is the offence concerning a dead human body`<br>`s 182 the punishment on indictment`<br>`s 182 the punishment on summary conviction` (and 1 more) |

**none** (a definition, a heading, a counting rule or a deeming rule, a test of a class of offence, an application clause, a repealed provision, or a rule that allocates a question or limits the court's inquiry): heading: PART V, heading: Interpretation, s 150, s 150 "guardian", s 150 "public place", s 150 "sexual organs", s 150 "theatre", heading: Sexual Offences, s 150.1(2)(b), s 150.1(2.1)(b), s 150.1(2.2)(b), s 152(2), s 153(1.1), s 153(2), s 153.1(1.1), s 153.1(2), s 153.1(2.1), s 153.1(2.2), s 153.1(3), s 153.1(3)(a), s 153.1(3)(a.1), s 153.1(3)(b), s 153.1(3)(c), s 153.1(3)(d), s 153.1(3)(e), s 153.1(4), s 154, s 155(3), s 155(4), s 156, ss 157 and 158, s 159, s 160(3.3), s 160(3.3)(a), s 160(3.3)(b), s 160(3.4), s 160(6), s 160(7), s 161(1.1), s 161(1.1)(a), s 161(1.1)(b), s 161(1.1)(c), s 161(1.1)(d), s 162(2), s 162(5), s 162(7), s 162(7)(a), s 162(7)(b), s 162.1(2), s 162.1(2)(a), s 162.1(2)(b), s 162.1(4), s 162.1(4)(a), s 162.1(4)(b), heading: Offences Tending to Corrupt Morals, s 163(2)(c), s 163(4), s 163(5), s 163(6), s 163(7), s 163(8), s 163.1(1), s 163.1(1)(a), s 163.1(1)(b), s 163.1(1)(c), s 163.1(1)(d), s 163.1(4.2), s 163.1(7), s 164(8), s 164(8) "advertisement for conversion therapy", s 164(8) "advertisement of sexual services", s 164(8) "court", s 164(8) "court" (a), s 164(8) "court" (a.1), s 164(8) "court" (b), s 164(8) "court" (c), s 164(8) "court" (c.1), s 164(8) "court" (d), s 164(8) "court" (e), s 164(8) "crime comic", s 164(8) "illicit material", s 164(8) "illicit material" (a), s 164(8) "illicit material" (b), s 164(8) "illicit material" (c), s 164(8) "illicit material" (d), s 164(8) "illicit material" (e), s 164(8) "illicit material" (f), s 164(8) "illicit material" (g), s 164(8) "intimate image", s 164(8) "judge", s 164(8) "voyeuristic recording", s 164.1(8), s 164.1(10), s 164.2(5), s 165, s 166, s 169, s 169.1(2), s 169.1(4), s 169.1(5), s 171.1(1)(a), s 171.1(1)(b), s 171.1(1)(c), s 171.1(2), s 171.1(5), s 171.1(5)(a), s 171.1(5)(b), s 171.1(5)(c), s 171.1(6), s 172(2), s 172(3), s 172.1(2), heading: Disorderly Conduct, s 172.2(2), s 174(2), s 178, s 179, heading: Nuisances, s 180(2), s 180(2)(a), s 180(2)(b), s 181.

## Marginal readings for a lawyer (ccc6)

Two readings are left to a lawyer (brief, "For a lawyer, not for you to decide"): (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not. The status quo is taken. Every branch that rests on one is listed here with the other reading.

**Reading (a): all 93 branches that answer JUST FALSE are listed, with the kind of words they rest on.** 54 rest on a condition the text states (a "where", "when", "if", "unless", period or "within" gate, or a duty not done), 8 of them also on a flat negative; 39 are flat negatives or "means" definitions and are not marginal. The other reading of the first two kinds is NOTHING. The kind is assigned by the quoted words.

| module | function | quoted words | kind | other reading |
| --- | --- | --- | --- | --- |
| bestiality | `s 160(7) bestiality` | "bestiality means any contact, for a sexual purpose, with an animal" | flat negative or "means": not marginal | none (flat) |
| bestiality | `s 160(3.2) section 160 gives a defence of public good against a charge under subsection (3...` | "No person shall be convicted of an offence under subsection (3.1) if the conduct that forms the subject-matter..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| bestiality | `s 160(3.3)(a) the question is a question of law` | "but it is a question of fact whether the conduct did or did not extend beyond what served the public good" | flat negative or "means": not marginal | none (flat) |
| bestiality | `s 160(3.3)(b) the motives of the accused are relevant` | "the motives of the accused are irrelevant" | flat negative or "means": not marginal | none (flat) |
| bestiality | `s 160(4)(b) the court may order the accused to pay the reasonable costs of the animal's ca...` | "on application of the Attorney General or on its own motion" | condition: reading (a) | NOTHING |
| children | `s 169.1(5) young person` | "young person means a person under the age of 18 years" | flat negative or "means": not marginal | none (flat) |
| children | `s 169.1(3) the belief that the young person was at least 18 is not a defence: the bar appl...` | "unless the accused took reasonable steps to ascertain the age of the young person" | condition: reading (a) | NOTHING |
| children | `s 171.1(5) sexually explicit material` | "sexually explicit material means material that is not child sexual abuse and exploitation material, as defined..." | flat negative or "means": not marginal | none (flat) |
| children | `s 171.1(5) sexually explicit material` | "sexually explicit material means material that is not child sexual abuse and exploitation material ... and tha..." | flat negative or "means": not marginal | none (flat) |
| children | `s 171.1(3) the evidence is proof that the accused believed that the person was under that ...` | "in the absence of evidence to the contrary" | condition: reading (a) | NOTHING |
| children | `s 171.1(4) the belief that the person was at least the age is not a defence: the bar appli...` | "unless the accused took reasonable steps to ascertain the age of the person" | condition: reading (a) | NOTHING |
| children | `s 172(3) child` | "child means a person who is or appears to be under the age of eighteen years" | flat negative or "means": not marginal | none (flat) |
| children | `s 172(4) no proceedings shall be commenced without the consent of the Attorney General: th...` | "without the consent of the Attorney General" | flat negative or "means": not marginal | none (flat) |
| children | `s 172(4) no proceedings shall be commenced without the consent of the Attorney General: th...` | "unless they are instituted by or at the instance of a recognized society for the protection of children or by ..." | condition: reading (a) | NOTHING |
| children | `s 172.1(3) the evidence is proof that the accused believed that the person was under that ...` | "in the absence of evidence to the contrary" | condition: reading (a) | NOTHING |
| children | `s 172.1(4) the belief that the person was at least the age is not a defence: the bar appli...` | "unless the accused took reasonable steps to ascertain the age of the person" | condition: reading (a) | NOTHING |
| children | `s 172.2(3) the evidence is proof that the accused believed that the person was under that ...` | "in the absence of evidence to the contrary" | condition: reading (a) | NOTHING |
| children | `s 172.2(4) the belief that the person was at least the age is not a defence: the bar appli...` | "unless the accused took reasonable steps to ascertain the age of the person" | condition: reading (a) | NOTHING |
| csaem | `s 163.1(1) child sexual abuse and exploitation material` | "In this section, child sexual abuse and exploitation material means (a) a photographic, film, video or other v..." | flat negative or "means": not marginal | none (flat) |
| csaem | `s 163.1(4.3) the court must consider the intent to make a profit as an aggravating factor` | "If a person is convicted of an offence under this section, the court that imposes the sentence shall consider ..." | condition: reading (a) | NOTHING |
| csaem | `s 163.1(5) the belief that the person shown was eighteen or more is not a defence: the bar...` | "unless the accused took all reasonable steps to ascertain the age of that person and took all reasonable steps..." | condition: reading (a) | NOTHING |
| csaem | `s 163.1(6) section 163.1 gives a defence` | "No person shall be convicted of an offence under this section if the act that is alleged to constitute the off..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| disorderly | `s 174(3) no proceedings shall be commenced without the consent of the Attorney General: th...` | "without the consent of the Attorney General" | flat negative or "means": not marginal | none (flat) |
| disorderly | `s 175(2) a summary conviction court may infer from the evidence of a peace officer that th...` | "In the absence of other evidence, or by way of corroboration of other evidence" | condition: reading (a) | NOTHING |
| morals | `s 163(3) section 163 gives a defence of public good` | "No person shall be convicted of an offence under this section if the public good was served by the acts that a..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| morals | `s 163(4) the question is a question of law` | "but it is a question of fact whether the acts did or did not extend beyond what served the public good" | flat negative or "means": not marginal | none (flat) |
| morals | `s 163(5) the motives of an accused are relevant` | "the motives of an accused are irrelevant" | flat negative or "means": not marginal | none (flat) |
| morals | `s 168(2) subsection (1) applies to the person` | "Subsection (1) does not apply to a person who (a) prints or publishes any matter for use in connection with an..." | flat negative or "means": not marginal | none (flat) |
| prohibition-orders | `s 161(1.1) the offence is one referred to in subsection (1.1)` | "The offences for the purpose of subsection (1) are (a) an offence under section 151, 152, 153 or 155, subsecti..." | flat negative or "means": not marginal | none (flat) |
| prohibition-orders | `s 161(1.1) the offence is one referred to in subsection (1.1)` | "(b) an offence under section 144 (rape), 145 (attempt to commit rape), 149 (indecent assault on female), 156 (..." | condition: reading (a) | NOTHING |
| prohibition-orders | `s 161(1.1) the offence is one referred to in subsection (1.1)` | "(c) an offence under subsection 146(1) (sexual intercourse with a female under 14) or section 153 (sexual inte..." | condition: reading (a) | NOTHING |
| prohibition-orders | `s 161(1.1) the offence is one referred to in subsection (1.1)` | "(d) an offence under subsection 212(1) (procuring), 212(2) (living on the avails of prostitution of person und..." | condition: reading (a) | NOTHING |
| prohibition-orders | `s 161(1.1) the offence is one referred to in subsection (1.1)` | "The offences for the purpose of subsection (1) are" | flat negative or "means": not marginal | none (flat) |
| prohibition-orders | `s 161(1) the court shall consider making an order of prohibition` | "When an offender is convicted, or is discharged on the conditions prescribed in a probation order under sectio..." | condition: reading (a) | NOTHING |
| prohibition-orders | `s 161(1) the court may make an order of prohibition` | "When an offender is convicted, or is discharged on the conditions prescribed in a probation order under sectio..." | condition: reading (a) | NOTHING |
| prohibition-orders | `s 161(3) the court may vary the conditions prescribed in the order` | "on application of the offender or the prosecutor" | condition: reading (a) | NOTHING |
| prohibition-orders | `s 162.2(1) the court may make an order prohibiting the offender from using the Internet or...` | "When an offender is convicted, or is discharged on the conditions prescribed in a probation order under sectio..." | condition: reading (a) | NOTHING |
| prohibition-orders | `s 162.2(3) the court may vary the conditions prescribed in the order` | "on application of the offender or the prosecutor" | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(1) it is not a defence that the complainant consented` | "Subject to subsections (2) to (2.2)" | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(2) it is a defence that the complainant consented, complainant aged 12 or 13` | "it is a defence that the complainant consented to the activity that forms the subject-matter of the charge if ..." | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(2.1) it is a defence that the complainant consented, complainant aged 14 or 15` | "it is a defence that the complainant consented to the activity that forms the subject-matter of the charge if ..." | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or mor...` | "it is a defence that the complainant consented to the activity that forms the subject-matter of the charge if,..." | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or mor...` | "the accused is the common-law partner of the complainant, or has been cohabiting with the complainant in a con..." | flat negative or "means": not marginal | none (flat) |
| s150-1-consent | `s 150.1(2.3) it is a defence that the complainant consented, the accused being married to ...` | "If, immediately before the day on which this subsection comes into force, the accused referred to in subsectio..." | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(3) no person aged twelve or thirteen shall be tried: the bar applies` | "unless the person is in a position of trust or authority towards the complainant, is a person with whom the co..." | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(4) the belief that the complainant was 16 or more is not a defence: the bar applie...` | "unless the accused took all reasonable steps to ascertain the age of the complainant" | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(5) the belief that the complainant was 18 or more is not a defence: the bar applie...` | "unless the accused took all reasonable steps to ascertain the age of the complainant" | condition: reading (a) | NOTHING |
| s150-1-consent | `s 150.1(6) the accused cannot raise a mistaken belief in the age of the complainant to inv...` | "unless the accused took all reasonable steps to ascertain the age of the complainant" | condition: reading (a) | NOTHING |
| s153-1 | `s 153.1(4) subsection (3) limits the circumstances in which no consent is obtained` | "Nothing in subsection (3) shall be construed as limiting the circumstances in which no consent is obtained" | flat negative or "means": not marginal | none (flat) |
| s153-1 | `s 153.1(2) consent` | "Subject to subsection (3), consent means, for the purposes of this section, the voluntary agreement of the com..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| s153-1 | `s 153.1(2) consent` | "consent means, for the purposes of this section, the voluntary agreement of the complainant to engage in the s..." | flat negative or "means": not marginal | none (flat) |
| s153-1 | `s 153.1(2) consent` | "Consent must be present at the time the sexual activity in question takes place" | flat negative or "means": not marginal | none (flat) |
| s153-1 | `s 153.1(5) the belief that the complainant consented is not a defence: the bar applies` | "is not a defence ... if (a) the accused’s belief arose from ... (b) the accused did not take reasonable steps ..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| s153-1 | `s 153.1(6) the judge must instruct the jury to consider the presence or absence of reasona...` | "If an accused alleges that he or she believed that the complainant consented to the conduct that is the subjec..." | condition: reading (a) | NOTHING |
| seizure | `s 164(8) court` | "court means (a) in the Province of Quebec, the Court of Quebec, the municipal court of Montreal and the munici..." | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) court` | "in the Province of Quebec, the Court of Quebec, the municipal court of Montreal and the municipal court of Que..." | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) court` | "in the Province of Quebec, the Court of Quebec, the municipal court of Montreal and the municipal court of Que..." | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) court` | "(a.1) in the Province of Ontario, the Superior Court of Justice" | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) court` | "(b) in the Provinces of New Brunswick, Manitoba, Saskatchewan and Alberta, the Court of Queen’s Bench" | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) court` | "(d) in the Provinces of Nova Scotia, British Columbia, Prince Edward Island and Newfoundland and Labrador, in ..." | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) court` | "(e) in Nunavut, the Nunavut Court of Justice" | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) court` | "court means" | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) judge` | "judge means a judge of a court" | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(8) illicit material` | "illicit material means" | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(2) the judge issued the summons within seven days of the day on which the warrant wa...` | "Within seven days of the day on which the warrant is issued, the judge shall issue a summons to the occupier o..." | condition: reading (a) | NOTHING |
| seizure | `s 164(5) the court must order the thing restored to the person from whom it was seized` | "If the court is not satisfied that the seized thing is illicit material, it shall order that the thing be rest..." | condition: reading (a) | NOTHING |
| seizure | `s 164(5) the thing is to be restored now` | "it shall order that the thing be restored to the person from whom it was seized without delay after the time f..." | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164(7) no proceedings shall be instituted or continued without the consent of the Attorn...` | "without the consent of the Attorney General" | flat negative or "means": not marginal | none (flat) |
| seizure | `s 164.1(2) the judge must cause notice to be given to the person who posted the material` | "Within a reasonable time after receiving the information referred to in paragraph (1)(c), the judge shall caus..." | condition: reading (a) | NOTHING |
| seizure | `s 164.1(5.1) the court must order the custodian to delete the material within 48 hours` | "If the illicit material is an intimate image, as defined in subsection 162.1(2), in relation to which an offen..." | condition: reading (a) | NOTHING |
| seizure | `s 164.1(5.1) the material was deleted within 48 hours after the order was made` | "to delete the material within 48 hours after the order is made" | condition: reading (a) | NOTHING |
| seizure | `s 164.1(6) the court may order the destruction of the electronic copy in the court's posse...` | "When the court makes the order for the deletion of the material, it may order the destruction of the electroni..." | condition: reading (a) | NOTHING |
| seizure | `s 164.1(7) the court must order the electronic copy returned and terminate the order made ...` | "If the court is not satisfied that the material is illicit material or computer data that makes illicit materi..." | condition: reading (a) | NOTHING |
| seizure | `s 164.1(9) the order cannot yet take effect` | "until the time for final appeal has expired" | condition: reading (a) | NOTHING |
| seizure | `s 164.2(1) the court may order the thing forfeited to Her Majesty` | "On application of the Attorney General" | condition: reading (a) | NOTHING |
| seizure | `s 164.2(2) the court must cause notice to be given to the person` | "Before making an order under subsection (1), the court shall cause notice to be given to, and may hear, any pe..." | condition: reading (a) | NOTHING |
| seizure | `s 164.3(1) the person may apply for relief from forfeiture` | "Within thirty days after an order under subsection 164.2(1) is made" | condition: reading (a) | NOTHING |
| seizure | `s 164.3(2) the day fixed for the hearing is one the judge may fix` | "The judge shall fix a day — not less than thirty days after the application is made — for its hearing" | condition: reading (a) | NOTHING |
| seizure | `s 164.3(3) the applicant served notice on the Attorney General at least fifteen days befor...` | "At least fifteen days before the hearing, the applicant shall cause notice of the application and of the heari..." | condition: reading (a) | NOTHING |
| seizure | `s 164.3(6) the Attorney General must direct that the thing be returned or its value paid` | "On application by a person who obtained an order under subsection (4), made after the expiration of the time a..." | condition: reading (a) | NOTHING |
| sexual-offences | `s 153(2) young person` | "young person means a person 16 years of age or more but under the age of eighteen years" | flat negative or "means": not marginal | none (flat) |
| sexual-offences | `s 155(3) section 155 gives the accused a defence` | "if the accused was under restraint, duress or fear of the person with whom the accused had the sexual intercou..." | condition: reading (a) | NOTHING |
| sexual-offences | `s 156 no person shall be convicted: the bar applies` | "unless the conduct alleged would be an offence under this Act if it occurred on the day on which the charge wa..." | condition: reading (a) | NOTHING |
| voyeurism | `s 162(3) paragraphs (1)(a) and (1)(b) apply to the person` | "Paragraphs (1)(a) and (b) do not apply to a peace officer who, under the authority of a warrant issued under s..." | flat negative or "means": not marginal | none (flat) |
| voyeurism | `s 162(6) section 162 gives a defence of public good` | "No person shall be convicted of an offence under this section if the acts that are alleged to constitute the o..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| voyeurism | `s 162(7)(a) the question is a question of law` | "but it is a question of fact whether the act does or does not extend beyond what serves the public good" | flat negative or "means": not marginal | none (flat) |
| voyeurism | `s 162(7)(b) the motives of an accused are relevant` | "the motives of an accused are irrelevant" | flat negative or "means": not marginal | none (flat) |
| voyeurism | `s 162.1(2) intimate image` | "intimate image means (a) a visual recording of a person made by any means including a photographic, film or vi..." | flat negative or "means": not marginal | none (flat) |
| voyeurism | `s 162.1(2) intimate image` | "(b) a visual representation that is made by any electronic or mechanical means, including by means of artifici..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| voyeurism | `s 162.1(2) intimate image` | "intimate image means" | flat negative or "means": not marginal | none (flat) |
| voyeurism | `s 162.1(3) section 162.1 gives a defence of public good` | "No person shall be convicted of an offence under this section if the conduct that forms the subject-matter of ..." | flat negative with a condition: reading (a) for the condition | NOTHING |
| voyeurism | `s 162.1(4)(a) the question is a question of law` | "but it is a question of fact whether the conduct does or does not extend beyond what serves the public good" | flat negative or "means": not marginal | none (flat) |
| voyeurism | `s 162.1(4)(b) the motives of an accused are relevant` | "the motives of an accused are irrelevant" | flat negative or "means": not marginal | none (flat) |

**Reading (b): 115 branches answer NOTHING because a prohibition or grant is limited by its own wording**; the other reading is JUST FALSE. The offence functions (fork F1) and the powers of fork F19 are in this list.

| module | function | quoted words | other reading |
| --- | --- | --- | --- |
| bestiality | `s 160(1) the conduct is the offence of bestiality` | "Every person who commits bestiality is guilty of an indictable offence" | JUST FALSE |
| bestiality | `s 160(2) the conduct is the offence of compelling the commission of bestiality` | "Every person who compels another to commit bestiality is guilty of an indictable offence" | JUST FALSE |
| bestiality | `s 160(3) the conduct is the offence of bestiality in the presence of, or by inciting, a pe...` | "every person who commits bestiality in the presence of a person under the age of 16 years, or who incites a pe..." | JUST FALSE |
| bestiality | `s 160(3.1) the conduct is the offence of publishing or distributing a representation of be...` | "Every person commits an offence who knowingly publishes, distributes, transmits, sells, makes available or adv..." | JUST FALSE |
| bestiality | `s 160(3.3)(a) the question is a question of law` | "For the purposes of subsection (3.2), (a) it is a question of law whether the conduct served the public good a..." | JUST FALSE |
| bestiality | `s 160(4)(a) the court may make an order prohibiting the accused` | "in addition to any other sentence that it may impose under any of subsections (1) to (3) and (3.4), (a) make a..." | JUST FALSE |
| bestiality | `s 160(4)(b) the court may order the accused to pay the reasonable costs of the animal's ca...` | "on application of the Attorney General or on its own motion, order that the accused pay to a person or an orga..." | JUST FALSE |
| bestiality | `s 160(5) the conduct is the offence of contravening an order made under paragraph (4)(a)` | "Every person who contravenes an order made under paragraph (4)(a) is guilty of an offence punishable on summar..." | JUST FALSE |
| bestiality | `s 160(6) sections 740 to 741.2 apply to the order` | "Sections 740 to 741.2 apply, with any modifications that the circumstances require, to orders made under parag..." | JUST FALSE |
| children | `s 169.1(1) the conduct is the offence of recruiting a young person to an offence` | "Every person is guilty of an offence who — being in a position of trust, power or authority towards a young pe..." | JUST FALSE |
| children | `s 169.1(3) the belief that the young person was at least 18 is not a defence: the bar appl...` | "It is not a defence to a charge under subsection (1) that the accused believed that the young person was at le..." | JUST FALSE |
| children | `s 170 the conduct is the offence of a parent or guardian procuring a person under 18 for s...` | "Every parent or guardian of a person under the age of 18 years who procures the person for the purpose of enga..." | JUST FALSE |
| children | `s 171 the conduct is the offence of a householder permitting prohibited sexual activity` | "Every owner, occupier or manager of premises, or any other person who has control of premises or assists in th..." | JUST FALSE |
| children | `s 171.1(1) the conduct is the offence of making sexually explicit material available to a ...` | "Every person commits an offence who transmits, makes available, distributes or sells sexually explicit materia..." | JUST FALSE |
| children | `s 171.1(3) the evidence is proof that the accused believed that the person was under that ...` | "Evidence that the person ... was represented to the accused as being under the age of 18, 16 or 14 years" | JUST FALSE |
| children | `s 171.1(4) the belief that the person was at least the age is not a defence: the bar appli...` | "It is not a defence to a charge under paragraph (1)(a), (b) or (c) that the accused believed that the person r..." | JUST FALSE |
| children | `s 172(1) the conduct is the offence of corrupting children` | "Every person who, in the home of a child, participates in adultery or sexual immorality or indulges in habitua..." | JUST FALSE |
| children | `s 172(4) no proceedings shall be commenced without the consent of the Attorney General: th...` | "No proceedings shall be commenced under subsection (1)" | JUST FALSE |
| children | `s 172.1(1) the conduct is the offence of luring a child` | "Every person commits an offence who, by a means of telecommunication, communicates with (a) a person who is, o..." | JUST FALSE |
| children | `s 172.1(3) the evidence is proof that the accused believed that the person was under that ...` | "Evidence that the person referred to in paragraph (1)(a), (b) or (c) was represented to the accused as being u..." | JUST FALSE |
| children | `s 172.1(4) the belief that the person was at least the age is not a defence: the bar appli...` | "It is not a defence to a charge under paragraph (1)(a), (b) or (c) that the accused believed that the person r..." | JUST FALSE |
| children | `s 172.2(1) the conduct is the offence of agreeing or arranging to commit a sexual offence ...` | "Every person commits an offence who, by a means of telecommunication, agrees with a person, or makes an arrang..." | JUST FALSE |
| children | `s 172.2(3) the evidence is proof that the accused believed that the person was under that ...` | "Evidence that the person referred to in paragraph (1)(a), (b) or (c) was represented to the accused as being u..." | JUST FALSE |
| children | `s 172.2(4) the belief that the person was at least the age is not a defence: the bar appli...` | "It is not a defence to a charge under paragraph (1)(a), (b) or (c) that the accused believed that the person r..." | JUST FALSE |
| children | `s 172.2(5)(a) it is not a defence that the person with whom the accused agreed was a peace...` | "It is not a defence to a charge under paragraph (1)(a), (b) or (c)" | JUST FALSE |
| children | `s 172.2(5)(a) it is not a defence that the person with whom the accused agreed was a peace...` | "(a) that the person with whom the accused agreed or made an arrangement was a peace officer or a person acting..." | JUST FALSE |
| children | `s 172.2(5)(b) it is not a defence that the person referred to did not exist` | "(b) that, if the person with whom the accused agreed or made an arrangement was a peace officer or a person ac..." | JUST FALSE |
| csaem | `s 163.1(2) the conduct is the offence of making, printing or publishing child sexual abuse...` | "Every person who makes, prints, publishes or possesses for the purpose of publication any child sexual abuse a..." | JUST FALSE |
| csaem | `s 163.1(3) the conduct is the offence of distributing child sexual abuse and exploitation ...` | "Every person who transmits, makes available, distributes, sells, advertises, imports, exports or possesses for..." | JUST FALSE |
| csaem | `s 163.1(4) the conduct is the offence of possessing child sexual abuse and exploitation ma...` | "Every person who possesses any child sexual abuse and exploitation material is guilty of" | JUST FALSE |
| csaem | `s 163.1(4.2) the person accesses child sexual abuse and exploitation material` | "a person accesses child sexual abuse and exploitation material who knowingly causes child sexual abuse and exp..." | JUST FALSE |
| csaem | `s 163.1(4.1) the conduct is the offence of accessing child sexual abuse and exploitation m...` | "Every person who accesses any child sexual abuse and exploitation material is guilty of" | JUST FALSE |
| csaem | `s 163.1(4.21) the conduct is the offence of threatening to publish child sexual abuse and ...` | "Every person who, with the intent to intimidate or to be taken seriously, knowingly threatens to publish, dist..." | JUST FALSE |
| csaem | `s 163.1(5) the belief that the person shown was eighteen or more is not a defence: the bar...` | "It is not a defence to a charge under subsection (2) in respect of a visual representation that the accused be..." | JUST FALSE |
| csaem | `s 163.1(7) the question is a question of law` | "it is a question of law whether any written material, visual representation or audio recording advocates or co..." | JUST FALSE |
| disorderly | `s 173(1) the conduct is the offence of an indecent act` | "Everyone who wilfully does an indecent act in a public place in the presence of one or more persons, or in any..." | JUST FALSE |
| disorderly | `s 173(2) the conduct is the offence of exposure to a person under 16` | "Every person who, in any place, for a sexual purpose, exposes their sexual organs to a person who is under the..." | JUST FALSE |
| disorderly | `s 174(2) the person is nude` | "a person is nude who is so clad as to offend against public decency or order" | JUST FALSE |
| disorderly | `s 174(1) the conduct is the offence of nudity` | "Every one who, without lawful excuse, (a) is nude in a public place, or (b) is nude and exposed to public view..." | JUST FALSE |
| disorderly | `s 174(3) no proceedings shall be commenced without the consent of the Attorney General: th...` | "No proceedings shall be commenced under this section" | JUST FALSE |
| disorderly | `s 175(1)(a) the conduct is the offence of causing a disturbance in or near a public place` | "Every one who (a) not being in a dwelling-house, causes a disturbance in or near a public place, (i) by fighti..." | JUST FALSE |
| disorderly | `s 175(1)(b) the conduct is the offence of an indecent exhibition in a public place` | "(b) openly exposes or exhibits an indecent exhibition in a public place" | JUST FALSE |
| disorderly | `s 175(1)(c) the conduct is the offence of loitering in a public place and obstructing pers...` | "(c) loiters in a public place and in any way obstructs persons who are in that place" | JUST FALSE |
| disorderly | `s 175(1)(d) the conduct is the offence of disturbing the peace and quiet of the occupants ...` | "(d) disturbs the peace and quiet of the occupants of a dwelling-house by discharging firearms or by other diso..." | JUST FALSE |
| disorderly | `s 175(2) a summary conviction court may infer from the evidence of a peace officer that th...` | "In the absence of other evidence, or by way of corroboration of other evidence, a summary conviction court may..." | JUST FALSE |
| disorderly | `s 176(1)(a) the conduct is the offence of obstructing an officiant by threats or force` | "(a) by threats or force, unlawfully obstructs or prevents or endeavours to obstruct or prevent an officiant fr..." | JUST FALSE |
| disorderly | `s 176(1)(b) the conduct is the offence of assaulting or arresting an officiant` | "(b) knowing that an officiant is about to perform, is on their way to perform or is returning from the perform" | JUST FALSE |
| disorderly | `s 176(2) the conduct is the offence of disturbing religious worship or certain meetings` | "Every one who wilfully disturbs or interrupts an assemblage of persons met for religious worship or for a mora..." | JUST FALSE |
| disorderly | `s 176(3) the conduct is the offence of disturbing the order or solemnity of a meeting` | "Every one who, at or near a meeting referred to in subsection (2), wilfully does anything that disturbs the or..." | JUST FALSE |
| disorderly | `s 177 the conduct is the offence of trespassing at night` | "Every person who, without lawful excuse, loiters or prowls at night on the property of another person near a d..." | JUST FALSE |
| disorderly | `s 180(2) the person commits a common nuisance` | "every one commits a common nuisance who does an unlawful act or fails to discharge a legal duty and thereby (a..." | JUST FALSE |
| disorderly | `s 180(1) the conduct is the offence of committing a common nuisance` | "who commits a common nuisance and by doing so (a) endangers the lives, safety or health of the public, or (b) ..." | JUST FALSE |
| disorderly | `s 182 the conduct is the offence concerning a dead human body` | "who (a) neglects, without lawful excuse, to perform any duty that is imposed on him by law or that he undertak..." | JUST FALSE |
| morals | `s 163(1) the conduct is the offence of making or publishing obscene matter` | "Every person commits an offence who makes, prints, publishes, distributes, circulates or has in their possessi..." | JUST FALSE |
| morals | `s 163(2) the conduct is the offence of selling obscene matter or exhibiting an indecent sh...` | "Every person commits an offence who knowingly, without lawful justification or excuse, (a) sells, exposes to p..." | JUST FALSE |
| morals | `s 163(4) the question is a question of law` | "For the purposes of this section, it is a question of law whether an act served the public good and whether th..." | JUST FALSE |
| morals | `s 163(8) the publication is deemed to be obscene` | "any publication a dominant characteristic of which is the undue exploitation of sex, or of sex and any one or ..." | JUST FALSE |
| morals | `s 167(1) the conduct is the offence of presenting an immoral theatrical performance` | "Every one commits an offence who, being the lessee, manager, agent or person in charge of a theatre, presents ..." | JUST FALSE |
| morals | `s 167(2) the conduct is the offence of taking part in an immoral theatrical performance` | "Every one commits an offence who takes part or appears as an actor, a performer or an assistant in any capacit..." | JUST FALSE |
| morals | `s 168(1) the conduct is the offence of mailing obscene matter` | "Every one commits an offence who makes use of the mails for the purpose of transmitting or delivering anything..." | JUST FALSE |
| morals | `s 168(2) subsection (1) applies to the person` | "does not apply to a person who (a) ... (b) ... or (c)" | JUST FALSE |
| prohibition-orders | `s 161(1)(a) to (d) the order may prohibit the offender from` | "an order prohibiting the offender from (a) attending a public park ... (d) using the Internet" | JUST FALSE |
| prohibition-orders | `s 161(1)(a.1) the order may prohibit the offender from being near the place` | "of any dwelling-house where the victim identified in the order ordinarily resides or of any other place specif..." | JUST FALSE |
| prohibition-orders | `s 161(2) the prohibition may be for the duration` | "The prohibition may be for life or for any shorter duration that the court considers desirable" | JUST FALSE |
| prohibition-orders | `s 161(3) the court may vary the conditions prescribed in the order` | "may, on application of the offender or the prosecutor, require the offender to appear before it at any time an..." | JUST FALSE |
| prohibition-orders | `s 161(4) the conduct is the offence of not complying with an order of prohibition` | "Every person who is bound by an order of prohibition and who does not comply with the order is guilty of" | JUST FALSE |
| prohibition-orders | `s 162.2(2) the prohibition may be for the period` | "The prohibition may be for any period that the court considers appropriate, including any period to which the ..." | JUST FALSE |
| prohibition-orders | `s 162.2(3) the court may vary the conditions prescribed in the order` | "may, on application of the offender or the prosecutor, require the offender to appear before it at any time an..." | JUST FALSE |
| prohibition-orders | `s 162.2(4) the conduct is the offence of not complying with an order of prohibition` | "Every person who is bound by an order of prohibition and who does not comply with the order is guilty of" | JUST FALSE |
| s150-1-consent | `s 150.1(1) it is not a defence that the complainant consented` | "when an accused is charged with an offence under section 151 or 152 or subsection 153(1), 160(3) or 173(2) or ..." | JUST FALSE |
| s150-1-consent | `s 150.1(2) it is a defence that the complainant consented, complainant aged 12 or 13` | "When an accused is charged with an offence under section 151 or 152, subsection 173(2) or section 271 in respe..." | JUST FALSE |
| s150-1-consent | `s 150.1(2.1) it is a defence that the complainant consented, complainant aged 14 or 15` | "in respect of a complainant who is 14 years of age or more but under the age of 16 years" | JUST FALSE |
| s150-1-consent | `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or mor...` | "When the accused referred to in subsection (2.1) is five or more years older than the complainant" | JUST FALSE |
| s150-1-consent | `s 150.1(2.3) it is a defence that the complainant consented, the accused being married to ...` | "the accused referred to in subsection (2.1)" | JUST FALSE |
| s150-1-consent | `s 150.1(3) no person aged twelve or thirteen shall be tried: the bar applies` | "No person aged twelve or thirteen years shall be tried for an offence under section 151 or 152 or subsection 1..." | JUST FALSE |
| s150-1-consent | `s 150.1(4) the belief that the complainant was 16 or more is not a defence: the bar applie...` | "to a charge under section 151 or 152, subsection 160(3) or 173(2), or section 271, 272 or 273 that the accused..." | JUST FALSE |
| s150-1-consent | `s 150.1(5) the belief that the complainant was 18 or more is not a defence: the bar applie...` | "to a charge under section 153, 170, 171, 172 or 279.011 or subsection 279.02(2), 279.03(2), 286.1(2), 286.2(2)..." | JUST FALSE |
| s150-1-consent | `s 150.1(6) the accused cannot raise a mistaken belief in the age of the complainant to inv...` | "An accused cannot raise a mistaken belief in the age of the complainant in order to invoke a defence under sub..." | JUST FALSE |
| s153-1 | `s 153.1(2.2) the question is a question of law` | "The question of whether no consent is obtained under subsection (3) or (4) or 265(3) is a question of law" | JUST FALSE |
| s153-1 | `s 153.1(1) the conduct is the offence of sexual exploitation of a person with a disability` | "Every person commits an offence who is in a position of trust or authority towards a person with a mental or p..." | JUST FALSE |
| s153-1 | `s 153.1(5) the belief that the complainant consented is not a defence: the bar applies` | "It is not a defence to a charge under this section that the accused believed that the complainant consented to..." | JUST FALSE |
| seizure | `s 164(1) a judge may issue a warrant authorizing seizure of copies of the material` | "A judge may issue a warrant authorizing seizure of copies of any material ... if the judge is satisfied by inf..." | JUST FALSE |
| seizure | `s 164(3) the person may appear and be represented in the proceedings to oppose the forfeit...` | "The owner and the maker of the seized thing that is alleged to be illicit material may appear and be represent..." | JUST FALSE |
| seizure | `s 164(4) the court may make an order declaring the thing forfeited to His Majesty in right...` | "If the court is satisfied, on a balance of probabilities, that the seized thing is illicit material, it may ma..." | JUST FALSE |
| seizure | `s 164(6) an appeal lies from the order` | "An appeal lies from an order made under subsection (4) or (5) by any person who appeared in the proceedings (a..." | JUST FALSE |
| seizure | `s 164(7) no proceedings shall be instituted or continued without the consent of the Attorn...` | "If an order is made under this section by a judge in a province with respect to one or more copies of any mate..." | JUST FALSE |
| seizure | `s 164.1(1) the judge may order the custodian of the computer system` | "If a judge is satisfied by information on oath that there are reasonable grounds to believe that material, con..." | JUST FALSE |
| seizure | `s 164.1(2) the judge may order the custodian to post the text of the notice` | "If the person cannot be identified or located or does not reside in Canada, the judge may order the custodian ..." | JUST FALSE |
| seizure | `s 164.1(3) the person may appear and be represented in the proceedings to oppose the order` | "The person who posted the material may appear and be represented in the proceedings" | JUST FALSE |
| seizure | `s 164.1(4) the court may proceed ex parte` | "If the person who posted the material does not appear for the proceedings, the court may proceed ex parte" | JUST FALSE |
| seizure | `s 164.1(5) the court may order the custodian to delete the material` | "If the court is satisfied, on a balance of probabilities, that the material is illicit material or computer da..." | JUST FALSE |
| seizure | `s 164.1(8) subsections 164(6) and (7) apply to the proceedings` | "Subsections 164(6) and (7) apply, with any modifications that the circumstances require, to this section" | JUST FALSE |
| seizure | `s 164.1(9) the order cannot yet take effect` | "No order made under subsections (5) to (7) takes effect until the time for final appeal has expired" | JUST FALSE |
| seizure | `s 164.1(10) the term has the meaning given by subsection 342.1(2) or subsection 164(8)` | "computer data and computer system have the same meanings as in subsection 342.1(2) and court, illicit material..." | JUST FALSE |
| seizure | `s 164.2(1) the court may order the thing forfeited to Her Majesty` | "On application of the Attorney General, a court that convicts a person of an offence under section 162.1, 163...." | JUST FALSE |
| seizure | `s 164.2(2) the court may hear the person and declare the nature and extent of the person's...` | "may hear, any person whom it considers to have an interest in the thing, and may declare the nature and extent..." | JUST FALSE |
| seizure | `s 164.2(3) the person may appeal to the court of appeal` | "A person who was heard in response to a notice given under subsection (2) may appeal to the court of appeal ag..." | JUST FALSE |
| seizure | `s 164.2(4) the Attorney General may appeal to the court of appeal` | "The Attorney General may appeal to the court of appeal against the refusal of a court to make an order under s..." | JUST FALSE |
| seizure | `s 164.2(5) Part XXI applies to the appeal` | "Part XXI applies, with any modifications that the circumstances require, with respect to the procedure for an ..." | JUST FALSE |
| seizure | `s 164.3(1) the person may apply for relief from forfeiture` | "a person who claims an interest in the thing forfeited may apply in writing to a judge" | JUST FALSE |
| seizure | `s 164.3(4) the judge may declare that the applicant's interest in the thing is not affecte...` | "The judge may make an order declaring that the applicant’s interest in the thing is not affected by the forfei..." | JUST FALSE |
| seizure | `s 164.3(5) the person may appeal to the court of appeal` | "A person referred to in subsection (4) or the Attorney General may appeal to the court of appeal against an or..." | JUST FALSE |
| sexual-offences | `s 151 the conduct is sexual interference` | "Every person who, for a sexual purpose, touches, directly or indirectly, with a part of the body or with an ob..." | JUST FALSE |
| sexual-offences | `s 152(1) the conduct is the offence of invitation to sexual touching or exposure` | "Every person commits an offence who, for a sexual purpose, invites, counsels or incites a person under the age..." | JUST FALSE |
| sexual-offences | `s 153(1) the conduct is the offence of sexual exploitation` | "Every person commits an offence who is in a position of trust or authority towards a young person, who is a pe..." | JUST FALSE |
| sexual-offences | `s 153(1.2) a judge may infer from it that the relationship is exploitative of the young pe...` | "from the nature and circumstances of the relationship, including" | JUST FALSE |
| sexual-offences | `s 155(1) the conduct is incest` | "Every one commits incest who, knowing that another person is by blood relationship his or her parent, child, b..." | JUST FALSE |
| sexual-offences | `s 156 no person shall be convicted: the bar applies` | "No person shall be convicted of any sexual offence under this Act as it read from time to time before January ..." | JUST FALSE |
| voyeurism | `s 162(1) the conduct is the offence of voyeurism` | "Every one commits an offence who, surreptitiously, observes — including by mechanical or electronic means — or..." | JUST FALSE |
| voyeurism | `s 162(3) paragraphs (1)(a) and (1)(b) apply to the person` | "do not apply to a peace officer who, under the authority of a warrant issued under section 487.01" | JUST FALSE |
| voyeurism | `s 162(4) the conduct is the offence of printing, publishing, etc. a voyeuristic recording` | "Every one commits an offence who, knowing that a recording was obtained by the commission of an offence under ..." | JUST FALSE |
| voyeurism | `s 162(7)(a) the question is a question of law` | "For the purposes of subsection (6), (a) it is a question of law whether an act serves the public good" | JUST FALSE |
| voyeurism | `s 162.1(1) the conduct is the offence of publishing an intimate image without consent` | "Everyone who knowingly publishes, distributes, transmits, sells, makes available or advertises an intimate ima..." | JUST FALSE |
| voyeurism | `s 162.1(1.1) the conduct is the offence of threatening to publish an intimate image` | "Everyone who, with the intent to intimidate or to be taken seriously, knowingly threatens to publish, distribu..." | JUST FALSE |
| voyeurism | `s 162.1(4)(a) the question is a question of law` | "For the purposes of subsection (3), (a) it is a question of law whether the conduct serves the public good" | JUST FALSE |

## Seams (ccc6)

Named as `inputs/PLAN.md` sections 3 and 6 name them.

- **[T] asked by this part:** `s 787(1) the general penalty for an offence punishable on summary conviction`: `Punishment`, the answer of ccc29 s 787(1). 24 functions take it as an input (one per limb "guilty of an offence punishable on summary conviction" that states no penalty): `s 153.1(1.1)(b) the punishment on summary conviction`, `s 160(1) the punishment on summary conviction`, `s 160(2) the punishment on summary conviction`, `s 160(3.4)(b) the punishment on summary conviction`, `s 160(5) the punishment on summary conviction`, `s 161(4)(b) the punishment on summary conviction`, `s 162(5)(b) the punishment on summary conviction`, `s 162.1(1)(b) the punishment on summary conviction`, `s 162.1(1.1)(b) the punishment on summary conviction`, `s 162.2(4)(b) the punishment on summary conviction`, `s 169(b) the punishment on summary conviction`, `s 169.1(4)(b) the punishment on summary conviction`, `s 172(1)(b) the punishment on summary conviction`, `s 173(1)(b) the punishment on summary conviction`, `s 174(1) the punishment on summary conviction`, `s 175(1) the punishment on summary conviction`, `s 176(1) the punishment on summary conviction`, `s 176(2) the punishment on summary conviction`, `s 176(3) the punishment on summary conviction`, `s 177 the punishment on summary conviction`, `s 180(1) the punishment on summary conviction`, `s 182 the punishment on summary conviction`, `ss 150 to 182 the punishment on summary conviction that s 787(1) fixes`, `ss 151 to 182 the punishments of the offence under the provision`. The seat passes the placeholder `ss 150 to 182 the penalty of s 787(1) is not stated in Part V`, which says that Part V states none.
- **Section 2 terms taken as facts (inputs of type `MAYBE BOOLEAN`):** `s 2 dwelling-house`, `s 2 night`, `s 2 peace officer` and `s 2 common-law partner`; the seat asks each as a yes or no and passes JUST TRUE or JUST FALSE, so a NOTHING of the keel's definition is not reachable from the seat (the layer-1 tests cover that path).
- **Other parts' offences named in this part's rules:** `s 286.4` (advertising sexual services) and `s 320.103` (promoting conversion therapy) are limbs (f) and (g) of `s 164(8) illicit material`, each an input of type `MAYBE BOOLEAN`; `s 342.1(2)` is a cross-reference only (s 164.1(10)). Offences named by section number are tested against the core `Provision of the Code` (seam rule R1).
- **[H] asked of this part by others** (PLAN.md section 6): the punishment and the class of an offence section, for ss 718.2, 718.3, 743.1 (ccc26), ss 463 to 465 (ccc14), ss 21 to 24 (ccc1), ss 515 and 522 (ccc20), ss 553 to 555 (ccc21). They are answered by `ccc6-offence-table.l4`, which, given a core `Provision of the Code`, returns the class of the offence and the punishments of its limbs; a provision that is not an offence of Part V answers NOTHING.
- **Seams the plan lacks:** none found.

## Seat (ccc6)

The seat is a person who is, or may be, accused of an offence under the Criminal Code. It is generated by `work/seatgen.py` from the question specs; every question begins "Under section N," and asks what its body answers, in the same direction. A provision that addresses only an official has no seat question (there is never a seat for an official); the layer-1 functions the seat text does not name are listed, with a count, at the end of this section, so that the limit can be seen. The regulative rules (`PARTY ... MUST`) are read by `#TRACE` in layer 1; the seat calls the decision functions that carry the same duties. Gravity is asked through the punishments of each offence; the class of an offence is answered by the offence table of layer 1 for other parts and is not asked separately in the seat.

175 questions in 12 groups, 331 case assertions; 147 questions at the start of the second audit, 28 added after it (see the note below).

### s 150 -- the words of this Part

- Under section 150, am I a guardian of the other person? (returns A MAYBE BOOLEAN)
- Under section 150, is the place a public place? (returns A MAYBE BOOLEAN)
- Under section 150, is the place a theatre? (returns A MAYBE BOOLEAN)
- Under section 150, is the part of the body in question a sexual organ? (returns A MAYBE BOOLEAN)

### s 150.1 -- consent as a defence, and mistake of age

- Under section 150.1, what does the section say about whether the complainant's consent is a defence? (returns A `s 150.1 consent as a defence`)
- Under section 150.1(3), does the bar apply so that I may not be tried because I was aged twelve or thirteen? (returns A MAYBE BOOLEAN)
- Under section 150.1(4), does the bar apply so that my belief that the complainant was 16 or older is no defence? (returns A MAYBE BOOLEAN)
- Under section 150.1(5), does the bar apply so that my belief that the complainant was 18 or older is no defence? (returns A MAYBE BOOLEAN)
- Under section 150.1(6), does the bar apply so that I cannot raise a mistaken belief in the complainant's age to rely on the exceptions? (returns A MAYBE BOOLEAN)

### ss 151 to 156 -- sexual interference, invitation, exploitation, incest, historical offences

- Under section 151, is what I did sexual interference? (returns A MAYBE BOOLEAN)
- Under section 151, what punishments am I liable to for sexual interference? (returns A LIST OF Punishment)
- Under section 152(1), is what I did an invitation to sexual touching or exposure? (returns A MAYBE BOOLEAN)
- Under section 152(2), what punishments am I liable to for inviting a person under 16 to sexual touching or exposure? (returns A LIST OF Punishment)
- Under section 153(1), is what I did sexual exploitation of a young person? (returns A MAYBE BOOLEAN)
- Under section 153(1.1), what punishments am I liable to for sexual exploitation of a young person? (returns A LIST OF Punishment)
- Under section 153(1.2), may a judge infer from this that my relationship with the young person is exploitative? (returns A MAYBE BOOLEAN)
- Under section 153.1(3), was no consent obtained? (returns A MAYBE BOOLEAN)
- Under section 153.1(1), is what I did sexual exploitation of a person with a disability? (returns A MAYBE BOOLEAN)
- Under section 153.1(1.1), what punishments am I liable to for sexual exploitation of a person with a disability? (returns A LIST OF Punishment)
- Under section 153.1(5), does the bar apply so that my belief that the complainant consented is no defence? (returns A MAYBE BOOLEAN)
- Under section 153.1(6), must the judge instruct the jury to consider whether I had reasonable grounds for my belief? (returns A MAYBE BOOLEAN)
- Under section 155(1), is what I did incest? (returns A MAYBE BOOLEAN)
- Under section 155(2), what punishment am I liable to for incest? (returns A Punishment)
- Under section 155(3), does section 155 give me a defence? (returns A MAYBE BOOLEAN)
- Under section 156, does the bar apply so that I may not be convicted of an old sexual offence? (returns A MAYBE BOOLEAN)

### s 160 -- bestiality

- Under section 160(1), is what I did bestiality? (returns A MAYBE BOOLEAN)
- Under section 160(1), what punishments am I liable to for bestiality? (returns A LIST OF Punishment)
- Under section 160(2), is what I did compelling another person to commit bestiality? (returns A MAYBE BOOLEAN)
- Under section 160(2), what punishments am I liable to for compelling another person to commit bestiality? (returns A LIST OF Punishment)
- Under section 160(3), is what I did bestiality in the presence of, or by inciting, a person under 16? (returns A MAYBE BOOLEAN)
- Under section 160(3), what punishments am I liable to for bestiality in the presence of, or by inciting, a person under 16? (returns A LIST OF Punishment)
- Under section 160(3.1), is what I did publishing or distributing a representation of bestiality? (returns A MAYBE BOOLEAN)
- Under section 160(3.2), does section 160 give me a defence of public good? (returns A MAYBE BOOLEAN)
- Under section 160(3.3)(b), are my motives relevant to the defence of public good? (returns A MAYBE BOOLEAN)
- Under section 160(3.4), what punishments am I liable to for publishing or distributing a representation of bestiality? (returns A LIST OF Punishment)
- Under section 160(4)(a), may the court make an order prohibiting me from owning, having the custody or control of, or residing in the same premises as an animal? (returns A MAYBE BOOLEAN)
- Under section 160(4), what is the shortest period of a prohibition order made against me? (returns A MAYBE (`Length of time`))
- Under section 160(4), may the court order me to pay the reasonable costs of an animal's care? (returns A MAYBE BOOLEAN)
- Under section 160(5), is contravening a prohibition order made under paragraph (4)(a) an offence? (returns A MAYBE BOOLEAN)
- Under section 160(5), what punishment am I liable to for contravening a prohibition order made under paragraph (4)(a)? (returns A Punishment)
- Under section 160(6), do sections 740 to 741.2 apply to the order that I pay the costs of an animal's care? (returns A MAYBE BOOLEAN)

### s 161 -- orders of prohibition after a conviction

- Under section 161(1), may the court make an order of prohibition against me for an offence listed in subsection (1.1)(a)? (returns A MAYBE BOOLEAN)
- Under section 161(1), must the court consider making an order of prohibition against me for an offence listed in subsection (1.1)(a)? (returns A MAYBE BOOLEAN)
- Under section 161(1)(a) to (d), may the order of prohibition prohibit me from this? (returns A MAYBE BOOLEAN)
- Under section 161(1)(a.1), may the order of prohibition prohibit me from being near a place? (returns A MAYBE BOOLEAN)
- Under section 161(1.1)(a), is my offence one of the offences the paragraph lists? (returns A MAYBE BOOLEAN)
- Under section 161(2), may my prohibition be for life or for a shorter duration that the court considers desirable? (returns A MAYBE BOOLEAN)
- Under section 161(2), on what date does my prohibition begin? (returns A MAYBE DATE)
- Under section 161(3), may the court vary the conditions of my prohibition order? (returns A MAYBE BOOLEAN)
- Under section 161(4), is not complying with my order of prohibition an offence? (returns A MAYBE BOOLEAN)
- Under section 161(4), what punishments am I liable to for not complying with an order of prohibition? (returns A LIST OF Punishment)

### ss 162 to 162.2 -- voyeurism, intimate images and the Internet prohibition

- Under section 162(1), is what I did voyeurism? (returns A MAYBE BOOLEAN)
- Under section 162(3), do paragraphs (1)(a) and (b) apply to me as a peace officer acting under a warrant? (returns A MAYBE BOOLEAN)
- Under section 162(4), is what I did printing, publishing or circulating a voyeuristic recording? (returns A MAYBE BOOLEAN)
- Under section 162(5), what punishments am I liable to for voyeurism or for printing, publishing or circulating a voyeuristic recording? (returns A LIST OF Punishment)
- Under section 162(6), does section 162 give me a defence of public good? (returns A MAYBE BOOLEAN)
- Under section 162(7)(b), are my motives relevant to the defence of public good? (returns A MAYBE BOOLEAN)
- Under section 162.1(2), is the image an intimate image? (returns A MAYBE BOOLEAN)
- Under section 162.1(1), is what I did publishing an intimate image without consent? (returns A MAYBE BOOLEAN)
- Under section 162.1(1), what punishments am I liable to for publishing an intimate image without consent? (returns A LIST OF Punishment)
- Under section 162.1(1.1), is what I did threatening to publish an intimate image? (returns A MAYBE BOOLEAN)
- Under section 162.1(1.1), what punishments am I liable to for threatening to publish an intimate image? (returns A LIST OF Punishment)
- Under section 162.1(3), does section 162.1 give me a defence of public good? (returns A MAYBE BOOLEAN)
- Under section 162.1(4)(b), are my motives relevant to the defence of public good? (returns A MAYBE BOOLEAN)
- Under section 162.2(1), may the court make an order prohibiting me from using the Internet? (returns A MAYBE BOOLEAN)
- Under section 162.2(2), may my Internet prohibition be for the period the court considers appropriate? (returns A MAYBE BOOLEAN)
- Under section 162.2(3), may the court vary the conditions of my Internet prohibition order? (returns A MAYBE BOOLEAN)
- Under section 162.2(4), is not complying with my Internet prohibition order an offence? (returns A MAYBE BOOLEAN)
- Under section 162.2(4), what punishments am I liable to for not complying with my Internet prohibition order? (returns A LIST OF Punishment)

### s 163 -- obscene materials

- Under section 163(1), is what I did making or publishing obscene matter? (returns A MAYBE BOOLEAN)
- Under section 163(2), is what I did selling obscene matter or exhibiting an indecent show? (returns A MAYBE BOOLEAN)
- Under section 163(3), does section 163 give me a defence of public good? (returns A MAYBE BOOLEAN)
- Under section 163(5), are my motives relevant to the defence of public good? (returns A MAYBE BOOLEAN)
- Under section 163(8), is the publication deemed to be obscene? (returns A MAYBE BOOLEAN)

### s 163.1 -- child sexual abuse and exploitation material

- Under section 163.1(1), is the material child sexual abuse and exploitation material? (returns A MAYBE BOOLEAN)
- Under section 163.1(2), is what I did making, printing or publishing child sexual abuse and exploitation material? (returns A MAYBE BOOLEAN)
- Under section 163.1(2), what punishment am I liable to for making, printing or publishing child sexual abuse and exploitation material? (returns A Punishment)
- Under section 163.1(3), is what I did distributing child sexual abuse and exploitation material? (returns A MAYBE BOOLEAN)
- Under section 163.1(3), what punishment am I liable to for distributing child sexual abuse and exploitation material? (returns A Punishment)
- Under section 163.1(4), is what I did possessing child sexual abuse and exploitation material? (returns A MAYBE BOOLEAN)
- Under section 163.1(4), what punishments am I liable to for possessing child sexual abuse and exploitation material? (returns A LIST OF Punishment)
- Under section 163.1(4.1), is what I did accessing child sexual abuse and exploitation material? (returns A MAYBE BOOLEAN)
- Under section 163.1(4.1), what punishments am I liable to for accessing child sexual abuse and exploitation material? (returns A LIST OF Punishment)
- Under section 163.1(4.21), is what I did threatening to publish child sexual abuse and exploitation material? (returns A MAYBE BOOLEAN)
- Under section 163.1(4.21), what punishments am I liable to for threatening to publish child sexual abuse and exploitation material? (returns A LIST OF Punishment)
- Under section 163.1(4.3), must the court consider my intent to make a profit as an aggravating factor? (returns A MAYBE BOOLEAN)
- Under section 163.1(5), does the bar apply so that my belief that the person shown was eighteen or older is no defence? (returns A MAYBE BOOLEAN)
- Under section 163.1(6), does section 163.1 give me a defence? (returns A MAYBE BOOLEAN)

### ss 164 to 164.3 -- seizure, forfeiture, deletion orders and relief

- Under section 164(8), is the court one that counts as a court for section 164? (returns A MAYBE BOOLEAN)
- Under section 164(8), is the person a judge for section 164? (returns A MAYBE BOOLEAN)
- Under section 164(8), is the material illicit material? (returns A MAYBE BOOLEAN)
- Under section 164(1), may a judge issue a warrant to seize copies of the material? (returns A MAYBE BOOLEAN)
- Under section 164(2), did the judge issue the summons in time? (returns A MAYBE BOOLEAN)
- Under section 164(3), may I appear and be represented in the proceedings to oppose the forfeiture? (returns A MAYBE BOOLEAN)
- Under section 164(4), may the court order the seized thing forfeited to His Majesty? (returns A MAYBE BOOLEAN)
- Under section 164(5), must the court order the thing restored to the person it was seized from? (returns A MAYBE BOOLEAN)
- Under section 164(5), is the thing to be restored to me now? (returns A MAYBE BOOLEAN)
- Under section 164(6), does an appeal lie from the order? (returns A MAYBE BOOLEAN)
- Under section 164(7), does the bar apply so that proceedings may not be brought without the consent of the Attorney General? (returns A MAYBE BOOLEAN)
- Under section 164.1(1), may a judge order the custodian of the computer system to act? (returns A MAYBE BOOLEAN)
- Under section 164.1(2), must the judge cause notice to be given to the person who posted the material? (returns A MAYBE BOOLEAN)
- Under section 164.1(3), may I appear and be represented in the proceedings to oppose the order? (returns A MAYBE BOOLEAN)
- Under section 164.1(5), may the court order the custodian to delete the material? (returns A MAYBE BOOLEAN)
- Under section 164.1(2), may the judge order the custodian to post the text of the notice? (returns A MAYBE BOOLEAN)
- Under section 164.1(4), may the court proceed ex parte? (returns A MAYBE BOOLEAN)
- Under section 164.1(7), must the court order the electronic copy returned and terminate the order? (returns A MAYBE BOOLEAN)
- Under section 164.1(5.1), must the court order the custodian to delete the intimate image within 48 hours? (returns A MAYBE BOOLEAN)
- Under section 164.1(5.1), was the material deleted within 48 hours after the order? (returns A MAYBE BOOLEAN)
- Under section 164.1(9), is the order unable to take effect yet? (returns A MAYBE BOOLEAN)
- Under section 164.2(1), may the court order the thing forfeited to Her Majesty? (returns A MAYBE BOOLEAN)
- Under section 164.2(2), must the court cause notice to be given to me? (returns A MAYBE BOOLEAN)
- Under section 164.2(2), may the court hear me and declare the nature and extent of my interest in the thing? (returns A MAYBE BOOLEAN)
- Under section 164.2(3), may I appeal to the court of appeal? (returns A MAYBE BOOLEAN)
- Under section 164.3(1), may I apply for relief from forfeiture? (returns A MAYBE BOOLEAN)
- Under section 164.3(3), did I serve notice on the Attorney General at least fifteen days before the hearing? (returns A MAYBE BOOLEAN)
- Under section 164.3(4), may the judge declare that my interest in the thing is not affected by the forfeiture? (returns A MAYBE BOOLEAN)
- Under section 164.3(5), may I appeal to the court of appeal? (returns A MAYBE BOOLEAN)
- Under section 164.3(6), must the Attorney General direct that the thing be returned or its value paid to me? (returns A MAYBE BOOLEAN)

### ss 167 to 169 -- theatrical performances and the mails

- Under section 167(1), is what I did presenting an immoral theatrical performance? (returns A MAYBE BOOLEAN)
- Under section 167(2), is what I did taking part in an immoral theatrical performance? (returns A MAYBE BOOLEAN)
- Under section 168(1), is what I did mailing obscene matter? (returns A MAYBE BOOLEAN)
- Under section 168(2), does subsection (1) apply to me? (returns A MAYBE BOOLEAN)
- Under section 169, what punishments am I liable to for an offence under section 163, 167 or 168? (returns A LIST OF Punishment)

### ss 169.1 to 172.2 -- offences against children

- Under section 169.1(5), is the person a young person? (returns A MAYBE BOOLEAN)
- Under section 169.1(1), is what I did recruiting a young person to an offence? (returns A MAYBE BOOLEAN)
- Under section 169.1(3), does the bar apply so that my belief that the young person was at least 18 is no defence? (returns A MAYBE BOOLEAN)
- Under section 169.1(4), what punishments am I liable to for recruiting a young person? (returns A LIST OF Punishment)
- Under section 170, is what I did a parent or guardian procuring a person under 18 for sexual activity? (returns A MAYBE BOOLEAN)
- Under section 170, what punishment am I liable to for procuring a person under 18? (returns A Punishment)
- Under section 171, is what I did a householder permitting prohibited sexual activity? (returns A MAYBE BOOLEAN)
- Under section 171, what punishment am I liable to for permitting prohibited sexual activity on my premises? (returns A Punishment)
- Under section 171.1(5), is the material sexually explicit material? (returns A MAYBE BOOLEAN)
- Under section 171.1(1), is what I did making sexually explicit material available to a child? (returns A MAYBE BOOLEAN)
- Under section 171.1(2), what punishments am I liable to for making sexually explicit material available to a child? (returns A LIST OF Punishment)
- Under section 171.1(3), is the evidence proof that I believed the person was under the age? (returns A MAYBE BOOLEAN)
- Under section 171.1(4), does the bar apply so that my belief about the person's age is no defence? (returns A MAYBE BOOLEAN)
- Under section 172(1), is what I did corrupting children? (returns A MAYBE BOOLEAN)
- Under section 172(1), what punishments am I liable to for corrupting children? (returns A LIST OF Punishment)
- Under section 172(4), does the bar apply so that proceedings may not begin without the consent of the Attorney General? (returns A MAYBE BOOLEAN)
- Under section 172.1(1), is what I did luring a child? (returns A MAYBE BOOLEAN)
- Under section 172.1(2), what punishments am I liable to for luring a child? (returns A LIST OF Punishment)
- Under section 172.1(3), is the evidence proof that I believed the person was under the age? (returns A MAYBE BOOLEAN)
- Under section 172.1(4), does the bar apply so that my belief about the person's age is no defence? (returns A MAYBE BOOLEAN)
- Under section 172.2(1), is what I did agreeing or arranging to commit a sexual offence against a child? (returns A MAYBE BOOLEAN)
- Under section 172.2(2), what punishments am I liable to for agreeing or arranging to commit a sexual offence against a child? (returns A LIST OF Punishment)
- Under section 172.2(3), is the evidence proof that I believed the person was under the age? (returns A MAYBE BOOLEAN)
- Under section 172.2(4), does the bar apply so that my belief about the person's age is no defence? (returns A MAYBE BOOLEAN)
- Under section 172.2(5)(a), is it no defence that the other person was a peace officer or acting under the direction of one? (returns A MAYBE BOOLEAN)
- Under section 172.2(5)(b), is it no defence that the other person did not exist? (returns A MAYBE BOOLEAN)

### ss 173 to 182 -- disorderly conduct and nuisances

- Under section 173(1), is what I did an indecent act? (returns A MAYBE BOOLEAN)
- Under section 173(1), what punishments am I liable to for an indecent act? (returns A LIST OF Punishment)
- Under section 173(2), is what I did exposure to a person under 16? (returns A MAYBE BOOLEAN)
- Under section 173(2), what punishments am I liable to for exposure to a person under 16? (returns A LIST OF Punishment)
- Under section 174(1), is what I did nudity? (returns A MAYBE BOOLEAN)
- Under section 174(1), what punishment am I liable to for nudity? (returns A Punishment)
- Under section 174(3), does the bar apply so that proceedings may not begin without the consent of the Attorney General? (returns A MAYBE BOOLEAN)
- Under section 175(1), is what I did causing a disturbance in or near a public place? (returns A MAYBE BOOLEAN)
- Under section 175(1)(b), is what I did an indecent exhibition in a public place? (returns A MAYBE BOOLEAN)
- Under section 175(1)(c), is what I did loitering in a public place and obstructing persons? (returns A MAYBE BOOLEAN)
- Under section 175(1)(d), is what I did disturbing the peace and quiet of the occupants of a dwelling-house? (returns A MAYBE BOOLEAN)
- Under section 175(2), may a summary conviction court infer from a peace officer's evidence that the disturbance or obstruction occurred? (returns A MAYBE BOOLEAN)
- Under section 175(1), what punishment am I liable to for an offence under any of paragraphs (a) to (d)? (returns A Punishment)
- Under section 176(1), is what I did obstructing an officiant by threats or force? (returns A MAYBE BOOLEAN)
- Under section 176(1)(b), is what I did assaulting or arresting an officiant? (returns A MAYBE BOOLEAN)
- Under section 176(1), what punishments am I liable to for obstructing, assaulting or arresting an officiant? (returns A LIST OF Punishment)
- Under section 176(2), is what I did disturbing religious worship or certain meetings? (returns A MAYBE BOOLEAN)
- Under section 176(2), what punishment am I liable to for disturbing religious worship or certain meetings? (returns A Punishment)
- Under section 176(3), is what I did disturbing the order or solemnity of a meeting? (returns A MAYBE BOOLEAN)
- Under section 176(3), what punishment am I liable to for disturbing the order or solemnity of a meeting? (returns A Punishment)
- Under section 177, is what I did trespassing at night? (returns A MAYBE BOOLEAN)
- Under section 177, what punishment am I liable to for trespassing at night? (returns A Punishment)
- Under section 180(1), is what I did committing a common nuisance? (returns A MAYBE BOOLEAN)
- Under section 180(1), what punishments am I liable to for a common nuisance? (returns A LIST OF Punishment)
- Under section 182, is what I did an offence concerning a dead human body? (returns A MAYBE BOOLEAN)
- Under section 182, what punishments am I liable to for an offence concerning a dead human body? (returns A LIST OF Punishment)

### Layer-1 functions the seat text does not name (108 of 317)

Many are helpers that a function the seat does name already calls (the class tests of the offence table, the limb tests of a composite, the definitions); the others address an official (a question of law, the application of Part XXI to an appeal, a judge's duty written as a regulative rule) or are tests of a class of offence. Listed so that no gap is hidden; a name is listed when it does not appear in `ccc6-seat.l4`.

- bestiality (6): `s 160(1) the class of the offence`; `s 160(2) the class of the offence`; `s 160(3) the class of the offence`; `s 160(3.3)(a) the question is a question of law`; `s 160(3.4) the class of the offence`; `s 160(5) the class of the offence`
- builders (3): `ss 150 to 182 the provision is in the section`; `ss 150 to 182 the provision is the subsection`; `ss 150 to 182 the punishment on summary conviction that s 787(1) fixes`
- children (12): `s 169.1 the class of the offence`; `s 170 the class of the offence`; `s 171 the class of the offence`; `s 171.1 the class of the offence`; `s 171.1(1) the person is, or the accused believes the person is, under the age`; `s 171.1(1)(a) the offence is one under subsection 153(1), section 155, 163.1, 170, 171 or 279.011 or subsection 279.02(2), 279.03(2), 286.1(2), 286.2(2) or 286.3(2)`; `s 171.1(1)(b) the offence is one under section 151 or 152, subsection 160(3) or 173(2) or section 271, 272, 273 or 280`; `s 171.1(1)(c) the offence is one under section 281`; `s 171.1(6) the activity is sexual activity for the purposes of subsection (5)`; `s 172 the class of the offence`; `s 172.1 the class of the offence`; `s 172.2 the class of the offence`
- csaem (7): `s 163.1(2) the class of the offence`; `s 163.1(3) the class of the offence`; `s 163.1(4) the class of the offence`; `s 163.1(4.1) the class of the offence`; `s 163.1(4.21) the class of the offence`; `s 163.1(4.3) the sentencing court's duty to consider the intent to make a profit`; `s 163.1(7) the question is a question of law`
- disorderly (10): `s 173(1) the class of the offence`; `s 173(2) the class of the offence`; `s 174(1) the class of the offence`; `s 175(1) the class of the offence`; `s 176(1) the class of the offence`; `s 176(2) the class of the offence`; `s 176(3) the class of the offence`; `s 177 the class of the offence`; `s 180 the class of the offence`; `s 182 the class of the offence`
- morals (3): `s 163(4) the question is a question of law`; `s 169 the class of an offence under section 163, 165, 167 or 168`; `s 169 the offence is one under section 163, 165, 167 or 168`
- offence-table (3): `ss 151 to 182 the class of the offence under the provision`; `ss 151 to 182 the provision is an offence of the section given as one of the subsections`; `ss 151 to 182 the punishments of the offence under the provision`
- prohibition-orders (5): `s 161(1) the court sentences or discharges the offender in the case the subsection describes`; `s 161(1)(a.1) the distance in kilometres`; `s 161(4) the class of the offence`; `s 161(4) the offender SHANT do what the order of prohibition forbids`; `s 162.2(4) the class of the offence`
- repealed (19): `s 154 as the text shows it`; `s 159 as the text shows it`; `s 163(2)(c) and (d) as the text shows it`; `s 163(6) as the text shows it`; `s 163(7) as the text shows it`; `s 164(8) "advertisement for conversion therapy" as the text shows it`; `s 164(8) "advertisement of sexual services" as the text shows it`; `s 164(8) "crime comic" as the text shows it`; `s 164(8) "intimate image" as the text shows it`; `s 164(8) "voyeuristic recording" as the text shows it`; `s 164(8) court (c) as the text shows it`; `s 164(8) court (c.1) as the text shows it`; `s 165 as the text shows it`; `s 166 as the text shows it`; `s 172(2) as the text shows it`; `s 178 as the text shows it`; `s 179 as the text shows it`; `s 181 as the text shows it`; `ss 157 and 158 as the text shows it`
- s150-1-consent (14): `s 150.1(1) it is not a defence that the complainant consented`; `s 150.1(1) the offence is under section 151 or 152 or subsection 153(1), 160(3) or 173(2)`; `s 150.1(1) the offence is under section 271, 272 or 273`; `s 150.1(2) it is a defence that the complainant consented, complainant aged 12 or 13`; `s 150.1(2) the offence is under section 151 or 152, subsection 173(2) or section 271`; `s 150.1(2)(b) the accused is in none of the three relationships`; `s 150.1(2.1) it is a defence that the complainant consented, complainant aged 14 or 15`; `s 150.1(2.1) the offence is under section 151 or 152, subsection 173(2) or section 271`; `s 150.1(2.2) it is a defence that the complainant consented, the accused being five or more years older`; `s 150.1(2.2) the charge is one that subsection (2.2) speaks to`; `s 150.1(2.3) it is a defence that the complainant consented, the accused being married to the complainant`; `s 150.1(3) the offence is under section 151 or 152 or subsection 173(2)`; `s 150.1(4) the offence is under section 151 or 152, subsection 160(3) or 173(2), or section 271, 272 or 273`; `s 150.1(5) the offence is under section 153, 170, 171, 172 or 279.011 or subsection 279.02(2), 279.03(2), 286.1(2), 286.2(2) or 286.3(2)`
- s153-1 (4): `s 153.1 the class of the offence`; `s 153.1(2.2) the question is a question of law`; `s 153.1(4) subsection (3) limits the circumstances in which no consent is obtained`; `s 153.1(6) the judge's duty to instruct the jury`
- seizure (10): `s 164(2) the judge's duty to issue the summons`; `s 164.1(10) the term has the meaning given by subsection 342.1(2) or subsection 164(8)`; `s 164.1(5.1) the custodian's duty to delete the intimate image`; `s 164.1(6) the court may order the destruction of the electronic copy in the court's possession`; `s 164.1(8) subsections 164(6) and (7) apply to the proceedings`; `s 164.2(4) the Attorney General may appeal to the court of appeal`; `s 164.2(5) Part XXI applies to the appeal`; `s 164.3(1) the claimant's permission to apply`; `s 164.3(2) the day fixed for the hearing is one the judge may fix`; `s 164.3(3) the applicant's duty to serve notice on the Attorney General`
- sexual-offences (6): `s 151 the class of the offence`; `s 152 the class of the offence`; `s 153 the class of the offence`; `s 153(2) young person`; `s 155 the class of the offence`; `s 155(4) brother and sister include half-brother and half-sister`
- voyeurism (6): `s 162 the class of the offence`; `s 162(2) visual recording`; `s 162(7)(a) the question is a question of law`; `s 162.1(1) the class of the offence`; `s 162.1(1.1) the class of the offence`; `s 162.1(4)(a) the question is a question of law`

### Seat audit note (second pass, against the bodies of the layer-1 functions)

Read: 147 seat questions, each name and `@export` text against the body of the function it calls (the 28 added in this pass were written against their bodies and are not counted as read). Mismatched and retitled: 10 (direction: 0; subject: 9; type of the answer: 1). Read and left: 137. The instruction's four criteria were applied: a different limb, route or scope; a premise, qualifier or consequence the function does not compute or the text does not say; a wrong polarity or modal; a different type of answer.

**Retitled (10).** Each title, its `@export` text and its `DECIDE` name changed together; the inputs' `@desc` texts did not carry the changed words and did not change. The cases are generated by question name and carry the new names.

| section | old name | new name | why |
| --- | --- | --- | --- |
| 150 | Under section 150, are the parts of the body I exposed or touched sexual organs | Under section 150, is the part of the body in question a sexual organ | subject: the title carried "I exposed or touched", which the function does not compute (the function takes one part of the body), and asked about "parts" where it answers for one |
| 150.1 | Under section 150.1, is it a defence that the complainant consented | Under section 150.1, what does the section say about whether the complainant's consent is a defence | type of the answer: a yes or no title over a four-way answer (consent is not a defence by subsection (1); is a defence by (2), (2.1), (2.2) or (2.3); (1) and (2.3) both apply and the text does not say which prevails; the section does not say) |
| 160(3) | Under section 160(3), what punishments am I liable to for bestiality in the presence of a child | Under section 160(3), what punishments am I liable to for bestiality in the presence of, or by inciting, a person under 16 | subject: the title named one limb of subsection (3); the punishments are those of the whole subsection, which also covers inciting a person under 16 |
| 160(4) | Under section 160(4), may the court make an order prohibiting me from owning an animal | Under section 160(4)(a), may the court make an order prohibiting me from owning, having the custody or control of, or residing in the same premises as an animal | subject: the title named one of the three prohibitions of paragraph (4)(a) and carried the subsection without the paragraph the function answers |
| 161(1) | Under section 161(1), must the court consider making an order of prohibition against me | Under section 161(1), must the court consider making an order of prohibition against me for an offence listed in subsection (1.1)(a) | subject: the seat reads the offence through paragraph (1.1)(a) only (an offence of the Act as it now stands), so JUST FALSE would be misread for a person convicted of one of the historical offences of (1.1)(b) to (d) |
| 161(1) | Under section 161(1), may the court make an order of prohibition against me | Under section 161(1), may the court make an order of prohibition against me for an offence listed in subsection (1.1)(a) | subject: the same route limit as the must-consider question above (the seat reads the offence through paragraph (1.1)(a) only), found on the check of every question that hard-wires the (1.1)(a) constructor |
| 161(1.1) | Under section 161(1.1), is my offence one for which an order of prohibition may be considered | Under section 161(1.1)(a), is my offence one of the offences the paragraph lists | subject: the same route limit (paragraph (a) only), and a consequence ("an order of prohibition may be considered") that the function does not compute |
| 162(5) | Under section 162(5), what punishments am I liable to for voyeurism | Under section 162(5), what punishments am I liable to for voyeurism or for printing, publishing or circulating a voyeuristic recording | subject: subsection (5) fixes the punishments for an offence under subsection (1) or (4); the title named (1) only |
| 168(2) | Under section 168(2), does subsection (1) apply to me as a person who prints or publishes legal or medical material | Under section 168(2), does subsection (1) apply to me | subject: "legal or medical material" compresses four limbs of the text into words the text does not use (matter for judicial proceedings, a notice or report under the direction of a court, a series of law reports, a technical publication for the legal or medical profession) |
| 175(1) | Under section 175(1), what punishment am I liable to for a disturbance offence | Under section 175(1), what punishment am I liable to for an offence under any of paragraphs (a) to (d) | subject: the title named the disturbance of paragraph (a); the punishment is that of all four paragraphs |

**Read and left, in doubt (6), keyed by section and question text.**

- Under section 160(6), do sections 740 to 741.2 apply to the order that I pay the costs of an animal's care: the title restates as a given what the function tests ("the order is made under paragraph (4)(b)") but the words are the text's own, the answer NOTHING is not misread, and the function's own name carries "the order".
- Under section 162(3), do paragraphs (1)(a) and (b) apply to me as a peace officer acting under a warrant: the three conditions in the title are the three the function tests as inputs, in the text's own words ("a peace officer who, under the authority of a warrant issued under section 487.01, is carrying out any activity referred to in those paragraphs").
- Under section 164.1(5.1), must the court order the custodian to delete the intimate image within 48 hours: the status "the intimate image" is the one the function tests, and the text says "If the illicit material is an intimate image"; JUST FALSE for a material that is not one reads as "not required".
- Under section 169, what punishments am I liable to for an offence under section 163, 167 or 168: the text names section 165 too, but section 165 is repealed in this text (finding 5), so no person can be accused under it.
- Under section 175(1), is what I did causing a disturbance in or near a public place: names subsection (1), not paragraph (1)(a); the failing answer is NOTHING, so nothing is misread.
- Under section 176(1), is what I did obstructing an officiant by threats or force: names subsection (1), not paragraph (1)(a); the failing answer is NOTHING, so nothing is misread.

**Read and left without doubt (131):** the title restates the function's own name, or differs from it by a status the function tests as a separate input while its own name carries the same words, or by wording only.

**Added (28), as part of finishing the seat:** an offence, a punishment, a defence, a bar or a power of the person that had no seat question.

- Under section 160(2), is what I did compelling another person to commit bestiality?
- Under section 160(2), what punishments am I liable to for compelling another person to commit bestiality?
- Under section 160(3.3)(b), are my motives relevant to the defence of public good?
- Under section 160(3.4), what punishments am I liable to for publishing or distributing a representation of bestiality?
- Under section 160(5), what punishment am I liable to for contravening a prohibition order made under paragraph (4)(a)?
- Under section 161(1)(a) to (d), may the order of prohibition prohibit me from this?
- Under section 161(1)(a.1), may the order of prohibition prohibit me from being near a place?
- Under section 161(2), may my prohibition be for life or for a shorter duration that the court considers desirable?
- Under section 162(7)(b), are my motives relevant to the defence of public good?
- Under section 162.1(1.1), is what I did threatening to publish an intimate image?
- Under section 162.1(1.1), what punishments am I liable to for threatening to publish an intimate image?
- Under section 162.1(4)(b), are my motives relevant to the defence of public good?
- Under section 162.2(2), may my Internet prohibition be for the period the court considers appropriate?
- Under section 162.2(3), may the court vary the conditions of my Internet prohibition order?
- Under section 162.2(4), what punishments am I liable to for not complying with my Internet prohibition order?
- Under section 163(5), are my motives relevant to the defence of public good?
- Under section 164.2(2), may the court hear me and declare the nature and extent of my interest in the thing?
- Under section 169.1(3), does the bar apply so that my belief that the young person was at least 18 is no defence?
- Under section 172.2(3), is the evidence proof that I believed the person was under the age?
- Under section 172.2(4), does the bar apply so that my belief about the person's age is no defence?
- Under section 174(1), what punishment am I liable to for nudity?
- Under section 175(1)(d), is what I did disturbing the peace and quiet of the occupants of a dwelling-house?
- Under section 176(1)(b), is what I did assaulting or arresting an officiant?
- Under section 176(1), what punishments am I liable to for obstructing, assaulting or arresting an officiant?
- Under section 176(2), what punishment am I liable to for disturbing religious worship or certain meetings?
- Under section 176(3), is what I did disturbing the order or solemnity of a meeting?
- Under section 176(3), what punishment am I liable to for disturbing the order or solemnity of a meeting?
- Under section 177, what punishment am I liable to for trespassing at night?

**Assertions restated (1):** in `ccc6-cases-seat.l4`, the s 164.2(1) case in which the Attorney General did not apply, now JUST FALSE, with a `RECONCILED 2026-11-12` comment (fork F9, name-test sweep).

## Findings: what the text turns out to say

1. **Section 150.1(1) is not made subject to subsection (2.3).** Subsection (1) opens "Subject to subsections (2) to (2.2)" (src:3002); subsection (2.3) (src:3016) gives a defence to an accused married to the complainant immediately before the day it comes into force. The text states no rule of priority, so for that accused the text gives two answers. The composite function returns a constructor that says so (fork F7).
2. **The converted text is not uniform in the monarch or the court names.** Section 164(4) (src:3272) says "His Majesty in right of the province"; section 164.2(1) (src:3333) says "Her Majesty"; section 180(2)(b) (src:3512) says "the subjects of Her Majesty in Canada"; section 164(8)(b) (src:3290) says "the Court of Queen's Bench". Each function name copies the wording of its own provision.
3. **Repealed provisions inside the range.** 19 rows of the coverage table read "[Repealed ...": s 154 (src:3088-3088); ss 157 and 158 (src:3099-3099); s 159 (src:3100-3100); s 163(2)(c) (src:3216-3216); s 163(6) (src:3223-3223); s 163(7) (src:3224-3224); s 164(8) "advertisement for conversion therapy" (src:3285-3285); s 164(8) "advertisement of sexual services" (src:3286-3286); s 164(8) "court" (c) (src:3291-3291); s 164(8) "court" (c.1) (src:3292-3292); s 164(8) "crime comic" (src:3295-3295); s 164(8) "intimate image" (src:3304-3304); s 164(8) "voyeuristic recording" (src:3306-3306); s 165 (src:3362-3362); s 166 (src:3363-3363); s 172(2) (src:3423-3423); s 178 (src:3501-3501); s 179 (src:3502-3502); s 181 (src:3513-3513). They have the disposition "repealed or blank in this text" and are asserted in `ccc6-tests-repealed.l4`.
4. **A DEONTIC value cannot be asserted on the stable binary.** An `#ASSERT` over a regulative rule's result gives `eval/unsupported-equality`; each regulative rule is therefore read with `#TRACE`, and the same duty is also written as a decision function that carries the assertions (for example `s 153.1(6)`). The twelve `#TRACE` directives give the same outcomes on 1.6.110 and 1.6.109 (see "What check.sh prints").
5. **Section 169 names section 165, which is repealed.** Section 169 (src:3378) says "an offence under section 163, 165, 167 or 168"; section 165 is "[Repealed, 2018, c. 29, s. 13]" (src:3362). The function `s 169 the offence is one under section 163, 165, 167 or 168` keeps 165 named (fork F16).
6. **Two maxima in section 162.1(1)(a), and a conditional minimum in section 155(2).** Section 162.1(1)(a) (src:3177-3179) is "(i) ... not more than 10 years, or (ii) ... not more than 14 years if the accused knew or ought to have known that, at the time the intimate image was made, aggravated sexual assault was being, or had just been, committed against the person depicted"; section 155(2) (src:3092) carries a minimum of five years "if the other person is under the age of 16 years" and none otherwise. The offence table lists both cases (fork F17).
7. **Four defined terms of section 164(8) are shown repealed.** "advertisement for conversion therapy" and "advertisement of sexual services" (src:3285-3286), "intimate image" and "voyeuristic recording" (src:3304, 3306) are "[Repealed, 2026, c. 19, s. 18]", and paragraph (c) of "court" is "[Repealed, 2026, c. 11, s. 5]" (src:3291). Paragraphs (c) and (f) of the definition "illicit material" still read "intimate image, as defined in subsection 162.1(2)" and "advertise sexual services contrary to section 286.4" (src:3299, 3302); both are encoded as the text reads.

## What the stable binary does not accept

Carried from the first-pass probes (`work/probe/*.l4`, 2026-11-13); they were not re-run on 2026-11-16, except the item on an empty `JL4_LIBRARY_PATH`, which was seen in this session.

- **`NOT (x) AND y` on one line parses as `NOT (x AND y)`.** Write the NOT and the AND on separate lines, or `(NOT (x)) AND y`. Found through a failing test in `ccc6-csaem.l4` (probes `work/probe/p5.l4`, `p6.l4`).
- **A `CONSIDER` pattern with fields is positional.** Write `WHEN ctor a b THEN`, not `WITH`.
- **A DEONTIC value cannot be compared in `#ASSERT`.** `eval/unsupported-equality`; read the `#TRACE` instead (finding 4).
- **`REFUSE` does not exist.** "Not covered" is `NOTHING` or a named constructor, asserted.
- **A genitive after a function application needs parentheses.** Put the application in parentheses before the genitive.
- **An empty `JL4_LIBRARY_PATH` is not an unset one (seen in this session, 2026-11-16).** With `JL4_LIBRARY_PATH=` (empty) the 1.6.109 build printed nothing for a module, which made a first comparison of `#TRACE` outputs read "different"; the comparison was redone with the variable unset on both sides and the number of satisfied assertions checked first (the run must have happened before two outputs are compared).

## Rulings (copied word for word from the brief)

Each ruling is recorded again, word for word, here, because this row carries the `NOTHING-kind` tags that cite it (the fork register above is where each is applied; the guide's sentence is in "Reading a result").

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

**A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (ruling of 2026-11-12, three limits).** A layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar. The guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". (1) Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading. (2) Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question. (3) Do NOT decide two groups by yourself; list them in the fork register with a count and leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer), and "entitled"-named functions (a claim, not a power).

In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

## What check.sh prints

Run in the deposit folder as `L4=<1.6.110> L4_MAIN=<1.6.109> ./check.sh`; the numbers it replaced are the keel's baseline (`inputs/KEEL-NOTES.md`, line 270: TOTAL 5 modules, 691 satisfied) and the baseline taken on resume on 2026-11-16, before the sweep, the retitles and the seat additions: 1367 satisfied over the same 35 modules, 0 errors, on both builds.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc6-bestiality.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc6-builders.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc6-cases-seat.l4                             0       331       0        0         0 |      0       331       0        0  same
ccc6-children.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc6-csaem.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc6-disorderly.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc6-morals.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc6-offence-table.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc6-prohibition-orders.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc6-repealed.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc6-s150-1-consent.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc6-s150-definitions.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc6-s153-1.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc6-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ccc6-seizure.l4                                0         0       0        0         0 |      0         0       0        0  same
ccc6-sexual-offences.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc6-tests-bestiality.l4                       0        63       0        0         0 |      0        63       0        0  same
ccc6-tests-children.l4                         0       161       0        0         0 |      0       161       0        0  same
ccc6-tests-csaem.l4                            0        70       0        0         0 |      0        70       0        0  same
ccc6-tests-disorderly.l4                       0       120       0        0         0 |      0       120       0        0  same
ccc6-tests-morals.l4                           0        60       0        0         0 |      0        60       0        0  same
ccc6-tests-offence-table.l4                    0        31       0        0         0 |      0        31       0        0  same
ccc6-tests-prohibition-orders.l4               0       112       0        0         0 |      0       112       0        0  same
ccc6-tests-repealed.l4                         0        19       0        0         0 |      0        19       0        0  same
ccc6-tests-s150-1-consent.l4                   0        94       0        0         0 |      0        94       0        0  same
ccc6-tests-s150-definitions.l4                 0        18       0        0         0 |      0        18       0        0  same
ccc6-tests-s153-1.l4                           0        38       0        0         0 |      0        38       0        0  same
ccc6-tests-seizure.l4                          0       154       0        0         0 |      0       154       0        0  same
ccc6-tests-sexual-offences.l4                  0        68       0        0         0 |      0        68       0        0  same
ccc6-tests-support.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc6-tests-voyeurism.l4                        0        85       0        0         0 |      0        85       0        0  same
ccc6-voyeurism.l4                              0         0       0        0         0 |      0         0       0        0  same
TOTAL (35 modules)                             0      1424       0        0           |      0      1424       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`TOTAL (35 modules)                             0      1424       0        0           |      0      1424       0        0`

check.sh exit status: 0 (as run by the wrapper that wrote the log; check.sh itself prints nothing about it).

`#TRACE`: the 12 directives (`ccc6-tests-csaem.l4` 1, `ccc6-tests-prohibition-orders.l4` 2, `ccc6-tests-s153-1.l4` 2, `ccc6-tests-seizure.l4` 7) give the same evaluation sections on 1.6.110 and 1.6.109, with the same numbers of satisfied assertions (140, 224, 76 and 308 lines in the two sections of the output) and the same outcomes.
