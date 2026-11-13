# NEEDS-CORE (all parts)

Status: **proposed, not landed.** Nothing below is in `coa-core.l4`. Each part that found the core lacking a type, a constructor or a field declared what it needed under its own prefix in its own module, so every module compiles as it stands; this file gathers the parts' requests in one place so that a later change to the core can take them in one go.
Taking a request into the core would mean editing the part modules that carry the local copy and running the gate again; the merge did not do that.
Each section is the part's own `NEEDS-CORE.md`, unchanged; the same text is under `notes/<part>-NEEDS-CORE.md`.

## coa1

The core cannot be extended from another module, so each is declared in this part's own module under its own label, and recorded here for the lead to hoist at the merge. All are constructors for `Party` (an actor a deontic rule names) unless said otherwise.

| wanted in the core | what this part declared instead | sections that need it | text |
| --- | --- | --- | --- |
| `Party` constructor for the person who affixes an official seal | `s 49(6) party` with the constructor `s 49(6) the person affixing the official seal`, in `coa1-part4-capacity.l4` | s 49(6) | "The person affixing the official seal must certify in writing on the deed or other document to which the seal is affixed the date on which, and place at which, it is affixed." |
| `Party` constructor for "an officer of a company, or a person acting on behalf of a company" | `s 45(4) party` with the constructor `s 45(4) an officer of a company, or a person acting on behalf of a company`, in `coa1-part4-capacity.l4` | s 45(4) | "An officer of a company, or a person acting on behalf of a company, commits an offence if he uses, or authorises the use of, a seal purporting to be a seal of the company on which its name is not engraved" |
| `Party` constructor for a liquidator (treated as an officer for ss 30 and 36) | none: s 30(4) and s 36(5) are decision functions over a plain fact (`the person is a liquidator of the company`) | s 30(4), s 36(5) | "For the purposes of this section, a liquidator of the company is treated as an officer of it." |
| `Party` constructors for the Charity Commission (England and Wales) and the Department for Social Development (Northern Ireland) | none: s 42(4) takes the consent as a plain fact (`the prior written consent ... has been given`) | s 42(4) | "the affirmation of a transaction to which section 41 applies ... is ineffective without the prior written consent of— (a) in England and Wales, the Charity Commission; (b) in Northern Ireland, the Department for Social Development" |
| a `Fine limit` for "level 3 on the standard scale" with a one-tenth fraction already exists (`a fine not exceeding a level on the standard scale` 3 0.1) | used as it is (`Penalty` constants in ss 26(4), 30(3), 32(4), 34(6), 35(4), 36(4), 45(5)) | none needed | |

No new type was needed in the core beyond these constructors. The record types of this part (`s 10(2)(c) statement for a class of shares`, `s 32(2)(c) statement for a class of shares` and the like) are specific to their sections and stay in the part's modules.

## coa2

What this part wanted from the core and did not find.
Nothing was added to or extended from the core: the keel's `coa-core.l4` and `coa-definitions.l4` are untouched.

## 1. A `Fine limit` constructor for "the greater of an amount in pounds and a level on the standard scale"

Wanted by s 63(3) and s 64(6) (lines 701 and 728): "... a daily default fine not exceeding one-tenth of the greater of £5,000 or level 4 on the standard scale."
The core's `Fine limit` (`coa-core.l4`, line 200) has four constructors: `a fine without a stated limit`, `a fine not exceeding the statutory maximum` (fraction), `a fine not exceeding a level on the standard scale` (level, fraction of the level) and `a fine not exceeding an amount in pounds` (pounds).
None can say "the greater of £5,000 or level 4".

Suggested constructor (not declared here, because a name in another module's type cannot be extended):

```
`a fine not exceeding the greater of an amount in pounds and a level on the standard scale` HAS pounds IS A NUMBER, level IS A NUMBER, `fraction of the greater` IS A NUMBER
```

What this part did instead: the daily default fine in `Penalty` is `NOTHING` for s 63(3) and s 64(6) (the text as rendered gives two wordings and does not choose: NOTES.md, fork 1), and each wording is a `NUMBER` function of the levels, under this part's prefix:
`s 63(3) the daily default fine in pounds on the first wording`, `s 63(3) the daily default fine in pounds on the second wording`, `s 64(6) the daily default fine in pounds on the first wording`, `s 64(6) the daily default fine in pounds on the second wording`.
If the core gains the constructor and the lead decides which wording stands, the two functions fold into the `Penalty` value.

## 2. Nothing else

No core type or constructor other than the one above was missing for ss 53 to 111.
(A note for the keel, not a need: pattern variables named `level` or `pounds` clash with the core's `Fine limit` field names, "multiple definitions for the identifier"; this part uses `lvl`, `frac` and `amt`.)

## coa4

What this part had to build itself because `coa-core.l4` lacks it. Each item says what was built, where, and what the lead could hoist so that every part uses one definition. None of them stops the part from working; each is a duplication risk at the merge.

1. **A constructor of `Fine limit` for "one-tenth of the greater of an amount in pounds or a level on the standard scale".** `s 156(7)` (second wording, src:2052) fixes the daily default fine at "one-tenth of the greater of £5,000 or level 4 on the standard scale". `Fine limit` has `a fine not exceeding a level on the standard scale` (a level and a fraction) and `a fine not exceeding an amount in pounds`, but no "the greater of" constructor. Built in `coa4-requirements.l4` as the function `s 156(7) the daily default fine limit in pounds under the wording one-tenth of the greater of 5000 pounds or level 4 on the standard scale`, which returns pounds directly. Wanted: a constructor with an amount, a level and a fraction, and a function in the core that turns any `Fine limit` into pounds.
2. **The pounds a level on the standard scale stands for.** The Act names levels (level 4, level 5) and the statutory maximum but does not give their pounds; the sources do not either. Built in `coa4-requirements.l4`: the record `s 156(7) standard scale in pounds` (fields `the statutory maximum in pounds`, `level 4 on the standard scale in pounds`, `level 5 on the standard scale in pounds`) and the function `s 156(7) the fine limit in pounds`, which read a `Fine limit` against a record the caller supplies (the seat asks the person for the three figures). Wanted: one such record and function in the core, so that every part's penalty question uses the same.
3. **A calendar for periods counted in working days.** The core has `Working days` as a constructor of `Unit of time`, and the keel answers `s 1173(1) the day is a working day for the company` for one day, but nothing adds n working days to a date. `s 188(3)` can hit a contract whose notice period is in working days; `s 188(3) the day on which a period beginning on the start day ends` answers NOTHING for that unit (a NOTHING-kind branch). Wanted: a function in the core that adds a number of working days to a date using the keel's `s 1173(1)` answer.

## coa6

One constructor the core lacks, declared meanwhile under my own prefix.

1. A `Fine limit` constructor for "one-tenth of the greater of £5,000 or level 4 on the standard scale" (s 272(7), second wording of the daily default fine, line 3598 of `ukpga-2006-46.txt`).
   Suggested name: `a fine not exceeding a fraction of the greater of an amount in pounds and a level on the standard scale`, with fields `fraction of the greater amount` (a NUMBER, 0.1 here), `amount in pounds` (a NUMBER, 5000 here) and `level` (a NUMBER, 4 here).
   Declared in `coa6-private-and-public.l4` as `s 272(7) a fraction of the greater of an amount in pounds and a level on the standard scale`, a constructor of `s 272(7) daily default fine limit`, and used by the record `s 272(7) penalty` (the core's `Penalty` cannot hold it, because its `daily default fine for continued contravention` is a `MAYBE` of the core's `Fine limit`).
   The keel's own `NEEDS-CORE` note mentions a "greater of £500 and one-tenth of level 4" fine (two uses elsewhere in the Act): a different shape, which the lead may hoist under the same constructor if it is generalised.
   If the constructor is hoisted, `s 272(7) the penalty on a person guilty of an offence under section 272` can return the core's `Penalty` and the `s 272(7)` types can be deleted; the two `s 272(7)` pounds functions would then read the core constructor.

Nothing else is needed: level 5 on the standard scale (`a fine not exceeding a level on the standard scale` 5 1), one-tenth of level 5 (`... 5 0.1`) and "a fine" with no stated limit (`a fine without a stated limit`) are core constructors and are used as they are in `coa6-offence-of-failure-to-notify.l4` (s 279M(3)).
The types and constructors declared in my own modules (`s 273(3) body`, `s 273(2)(c) calling`, `s 279G change in the secretaries`, `s 279G notice given`, `s 279H notice given`, `s 279I notice given`, `s 279J(1) item of the required information about an individual`, `s 279J(3) name`, `s 279K(1) item of the required information about a body corporate or firm`) are specific to Part 12 and need no hoisting.

## coa8

Nothing in this range was blocked on the core.
One shape is a hoist candidate for the lead: `s 383(6) the accounts the figures are taken from` (a choice between Companies Act accounts and IAS accounts, with the figure adjustment that follows), declared in `coa8-part15-small.l4` under this range's prefix.
The medium-sized company and group tests of ss 465 to 467 (another part) will need the same choice; two copies under two prefixes would both compile, because every top-level name carries its section label.

## coa9

Types or constructors this part needed and the core (`coa-core.l4`) lacks, for the lead to hoist at the merge.
This part declared its own under its own prefix and uses it; nothing here blocks the part.

## 1. A `Fine limit` constructor for "one-tenth of the greater of an amount in pounds and a level on the standard scale"

- **Wanted:** a constructor of `Fine limit`, for example `a fine not exceeding a fraction of the greater of an amount in pounds and a level on the standard scale`, with fields `pounds` (NUMBER), `level` (NUMBER) and `fraction of the greater` (NUMBER).
- **Sections that need it:** s 438(4), second version of the daily default fine: "one-tenth of the greater of £5,000 or level 4 on the standard scale" (line 5851 of `ukpga-2006-46.txt`). The PLAN's section 3 records two uses of a "greater of" fine in the whole Act ("greater of £500 and one-tenth of level 4").
- **What this part did instead:** declared `s 438(4) version of the daily default fine` (two constructors: the first version, one-tenth of level 5, and the second) in `coa9-laying.l4`, and a function `s 438(4) the most the daily default fine may be in pounds on the version`. The `Penalty` returned by `s 438(4) the penalty for an offence under section 438` leaves the daily default fine `NOTHING` because the text carries both versions and does not say which is in force (fork F30).

## 2. Nothing else

The core's `Penalty`, `Fine limit`, `Mode of conviction`, `Period`, `Party` and `Unit of time` were enough for every offence and penalty of the range, and no further type or constructor is wanted.

## coa10

## Needed: a `Fine limit` constructor for "the greater of an amount in pounds and a level on the standard scale"

Where: s 451(4), the second text printed at line 6128 of `ukpga-2006-46.txt`: "a daily default fine not exceeding one-tenth of the greater of £5,000 or level 4 on the standard scale".
What the core has: `Fine limit` (coa-core.l4, line 200) offers `a fine without a stated limit`, `a fine not exceeding the statutory maximum` (with a fraction), `a fine not exceeding a level on the standard scale` (with a level and a fraction of the level) and `a fine not exceeding an amount in pounds`.
None of them says "the greater of an amount in pounds and a level, times a fraction", and `Penalty` holds its daily default fine as a `Fine limit`, so the core's `Penalty` cannot carry this text.
What coa10 did instead: it declares its own `s 451 daily default fine limit` (two constructors, one per printed text) and `s 451 the penalty in the second text`, so that the first text uses the core's `Penalty` and the second does not.
Constructor wanted, for the lead to hoist (the name is the lead's to choose; the shape is what s 451(4) needs):

```
`a fine not exceeding a fraction of the greater of an amount in pounds and a level on the standard scale`
    HAS pounds IS A NUMBER, level IS A NUMBER, `fraction of the greater` IS A NUMBER
```

Once it exists, coa10's `s 451 daily default fine limit` and `s 451 the penalty in the second text` can be deleted and `s 451(4) the penalty in the second text` can return the core's `Penalty`.
One more constructor would have saved this part a small type of its own: the core's `Party` has `Secretary of State` and `Registrar` (coa-core.l4, lines 85-101) but no party for a person authorised by the Secretary of State under s 457, who may be the applicant under s 456(1)(b).
coa10 declares `s 456 party` (`s 456 the applicant`, standing for either applicant, and `s 456 the registrar`) for the one regulative rule that needs it (s 456(7)), so nothing in the core is needed for the part to run.
The constructor wanted is `Person authorised under section 457` in `Party`; the entry is a note for the lead, not a blocker.

## coa11

The core (`coa-core.l4`) lacks the following; this part declared a small type of its own under its own prefix and records here what the lead could hoist at the merge.

1. **A constructor for the audit committee in `Party`.**
   Wanted: `Audit committee` (and, if the lead wants it, `Scottish Ministers` and `Competent authority` is already there).
   Sections: s 485A(3) (the audit committee must make a recommendation to the directors before an appointment) and s 489A(3), the same for a public company; s 494ZA(2) to (4) name "the competent authority" (the core has `Competent authority`), and s 483 names "the Scottish Ministers" (not a regulative rule here: it is a power, encoded as a decision function).
   Declared locally instead: `s 485A party` (`s 485A the audit committee`, `s 485A the directors`), `s 489A party`, `s 485B party`, `s 489B party`, each with its own action type (`s 485A act` and so on), because the core's `Party` has `Director` but no audit committee.
2. **Used from the core where it fitted:** `Party` (`Company`, for the four "give notice to the Secretary of State" duties of ss 486(2), 486A(4), 490(2), 490A(4)), `Penalty` and `Fine limit` (the offence penalties of ss 486(4), 486A(6), 490(4), 490A(6): `a fine not exceeding a level on the standard scale` with level 3 and fraction 1 or 0.1), `Mode of conviction` (`on summary conviction`), `Form of document` (s 488(3)(a)).
3. **A type for "a list of financial years of a company"** is declared locally (`s 494ZA financial year`: first day, last day, whether the auditor was appointed for it following a qualifying selection procedure); another part that needs the company's financial years (Part 15, coa8 and coa9) may want the same record in the core.

## coa12

The core (`coa-core.l4`, the keel's, read-only) lacks the constructors and helpers below.
Each was replaced by a stand-in or defined under the `coa12` prefix so that nothing here collides with another part; the lead hoists what it wants at the merge and the stand-ins are then replaced.
Every claim below was read from `coa-core.l4` and the layer-1 sources of this folder when the file was written.

## Constructors of `Party` (core lines 85 to 101)

| wanted | stand-in used | sections that need it | where |
| --- | --- | --- | --- |
| `Appropriate audit authority` (the body that receives an auditor's statement and a company's notice: the Secretary of State, a delegate, the Financial Reporting Council Limited, a supervisory body or the Independent Supervisor, by s 525(1)) | `Competent authority` (as the recipient of the action) | ss 522(1) and 523(2) | `coa12-ch4b-resignation.l4`, the two deontic rules of ss 522(1) and 523(2) |
| `Person proposed to be appointed as auditor` (the person the company must send a copy of a proposed resolution or special notice to, besides the outgoing auditor) | `Auditor`, which stands for the outgoing auditor only; the person proposed is named in the action text and is not a recipient of the rule | s 514(3) and s 515(3) | `coa12-ch4a-removal.l4`, the deontic rules of s 514(3) and s 515(3) |

The other parties of the Chapters (the senior statutory auditor of s 503 and s 504, the Attorney General of s 508, the Lord Advocate of s 509, the Financial Reporting Council Limited, a supervisory body, the Independent Supervisor) are not parties to any deontic rule of this part, so they are not constructors of `Party` here: s 525(1) answers "who is the appropriate audit authority" with the type `s 525(1) audit authority` of this part, and ss 508 and 509 are encoded as decision functions.
If the lead prefers one `Party` constructor per authority, `s 525(1) audit authority` is the list of what would be wanted.

## Helpers (defined in `coa12-logic.l4`; wanted as shared helpers)

| name | signature | used by | what it is |
| --- | --- | --- | --- |
| `coa12 either answer holds` | `MAYBE BOOLEAN` x `MAYBE BOOLEAN` to `MAYBE BOOLEAN` | ss 510(2), 519(2A), 519A(1), 519A(3), 523(1), 532(4), 539 | three-valued OR: `JUST TRUE` if either is; else `NOTHING` if either is; else `JUST FALSE` |
| `coa12 both answers hold` | the same | ss 510(2), 518(1), 519(2B), 519A(1), 519A(3), 520(1), 521(A1), 534(2), 539 | three-valued AND: `JUST FALSE` if either is; else `NOTHING` if either is; else `JUST TRUE` |
| `coa12 the opposite answer` | `MAYBE BOOLEAN` to `MAYBE BOOLEAN` | ss 519A(1), 523(1), 539 | swaps `JUST TRUE` and `JUST FALSE`, keeps `NOTHING` |
| `coa12 the answer for the fact` | `BOOLEAN` to `MAYBE BOOLEAN` | the seat layer (every yes/no fact passed to a `MAYBE BOOLEAN` input) | `JUST TRUE` or `JUST FALSE` |
| `coa12 the largest fine the penalty allows, in pounds` | `Penalty` x `NUMBER` (the statutory maximum) x `NUMBER` (level 3) to `MAYBE NUMBER` | the penalty questions of the seat layer | the pound value of a penalty's fine limit; `NOTHING` where the penalty states none |
| `coa12 the act was done within the number of days after the day` | `MAYBE DATE` x `DATE` x `NUMBER` to `BOOLEAN` | ss 518(5), 520(2), 520(4), 520(5), 521(1), 521(2), 522(1), 523(3) | counts both ends in (fork F9); `NOTHING` as the date means "not done" |

The core's `Penalty` has `Fine limit` constructors for "the statutory maximum" and "level 3" but not their pound values (the Act does not state them), so the pound conversion takes both as inputs.

## Types of this part that other parts could share

| name | what it is | sections |
| --- | --- | --- |
| `s 529(3) time` | a date and an hour of the day (a `DATETIME` comparison did not check on either stable build) | s 529(3); any "not later than the time" rule |
| `s 525(1) audit authority` | the five authorities of s 525(1) | ss 522 to 524 |
| `s 506(1) kind of copy of the report`, `s 519A(3) reason for ceasing to hold office`, `s 495(3A) what the auditors do with the provision`, `s 532(3) where the provision is contained`, `s 534(3)(b) section of the Unfair Contract Terms Act 1977` | types local to one section | their own sections |

## coa13

Types or constructors the core (`coa-core.l4`) lacks that coa13 wanted. None was declared under the `coa13` prefix except where stated; the lead decides what to hoist.

1. **A `Fine limit` constructor for "one-tenth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale for summary offences"** (s 557(2)(b), s 597(4)(b)). Fields wanted: `a sum in pounds` (NUMBER), `level on the standard scale` (NUMBER), `fraction` (NUMBER). (PLAN.md section 3 asks for a constructor for a different fine, "greater of £500 and one-tenth of level 4", whose two uses are outside this part: NOTES.md finding 14.) Not declared: the text of both sections shows this wording run together with "one-tenth of the statutory maximum" and does not choose between them (fork F-557(2)(b) in NOTES.md), so the `Penalty` the modules build carries NOTHING as the daily default fine, and each reading has its own NUMBER function in pounds (`s 557(2)(b) the most the daily default fine can be, in pounds, on the reading ...`, `s 597(4)(b) ...`). If the lead hoists the constructor, the two sites should carry both readings as two `Penalty` values.
2. **`Party` constructors for the persons these sections name** and for which the Jural relations table in NOTES.md uses plain words: allottee, applicant for shares, valuer (the "independent valuer" of Chapter 6), purchaser for value, holder of shares, other party to an agreement (the person referred to in s 598(1)(a)). `Subscriber to the memorandum`, `Director`, `Member`, `Company`, `Court`, `Registrar` and `Officer in default` exist and are enough for the deontic rules in `coa13-regulative.l4`, which declare their own action types under the `coa13` prefix.
3. **A core type for "a period measured from a date"** (the periods of this Part: one month, two months, 15 days, 28 days, 40 days, 48 days, six months, five years, two years). The modules use the library's `add months` / `add years` and `DATE PLUS days` on a plain `DATE`; the core `Period` is not used for date arithmetic. Nothing needs hoisting unless the lead wants one shared "end of period" function (fork F-periods).

## coa14

Written 2026-11-13 by part agent coa14. Nothing here is a request to change a type the core already has.

## 1. A statement of capital (proposed for the core; declared under this part's prefix in `coa14-nouns.l4`)

Six sections of my range require a statement of capital with the same content: ss 619(3), 621(3), 625(3), 627(3), 644(2) and 649(2) (23 lines of the range mention one). The content in each is: (a) the total number of shares of the company, (b) the aggregate nominal value of those shares, (ba) the aggregate amount (if any) unpaid on those shares, and (c) for each class of shares (i) prescribed particulars of the rights attached, (ii) the total number of shares of the class and (iii) the aggregate nominal value of shares of the class. Paragraph (d) is shown as a row of dots in all six.
s 652(1)(a) cites statements of capital delivered under ss 644, 649, 1028A and 1032A and under paragraph 7 of Schedule 4 to the 2015 Act, so the shape recurs outside my range.
The core has no such type, so I declared two under my prefix: `s 619(3) statement of capital` (fields `s 619(3)(a) states the total number of shares of the company`, `s 619(3)(b) states the aggregate nominal value of those shares`, `s 619(3)(ba) states the aggregate amount (if any) unpaid on those shares`, `s 619(3)(c) the entries for each class of shares`, `s 619(3) is stated with respect to the share capital at the moment the section names`; all BOOLEAN except the list) and `s 619(3)(c) class entry in a statement of capital` (three BOOLEAN fields for (c)(i) to (iii)).
What to hoist: one core type `Statement of capital` with those fields, so that the six sections here and any other part that requires one share it; then `coa14-nouns.l4` loses the two declarations and `s 619(3) the statement of capital states what the section requires` and its five wrappers change their type name only.
The fields are yes/no facts ("states the total number of shares") and not numbers, because the seam is what the statement says, not the capital's arithmetic; a part that wants to check the numbers needs a richer type than the one proposed.

## 2. Not needed

- A "greater of" fine: no penalty in lines 8206-8744 is the greater of two amounts (`grep -i 'greater of'` over the range: 0 lines). PLAN.md's note that the core has no constructor for it does not touch this range.
- A constructor for a fine without a stated limit, a level on the standard scale, the statutory maximum or imprisonment: the core's `Fine limit`, `Penalty`, `Period` and `Mode of conviction` carry every penalty in the range (ss 619(5), 621(5), 625(5), 627(8), 635(3), 636(3) to 640(3), 643(5), 644(9), 647(2), 656(5)).

## coa15

Each item below was met while encoding ss 658 to 737. In each case coa15 declares a small type of its own under its prefix (`coa15-nouns.l4`) and uses it; the lead may hoist the type into the core so that other parts can share it.

1. **A fine limit of "the greater of an amount in pounds and the amount corresponding to a level on the standard scale".** ss 707(7)(b) and 728(5)(b) say "one-tenth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale for summary offences" for the daily default fine. The core's `Fine limit` has constructors for a fine without a stated limit, a fraction of the statutory maximum, a fraction of a level on the standard scale and an amount in pounds, but none that takes the greater of a fixed sum and a level. coa15 declares `s 707(7) daily default fine limit` (one-tenth of the statutory maximum, or one-tenth of the greater of an amount in pounds and a level).
2. **A penalty whose daily default fine can be of that kind.** The core's `Penalty` carries its daily default fine as a core `Fine limit`, so it cannot carry item 1. coa15 declares `s 707(7) penalty`, a record with the mode of conviction, a fine not exceeding (a core `Fine limit`) and a daily default fine of the type in item 1.
3. **A statement of capital.** ss 663(3), 689(3), 708(3), 720B(2) and 730(5) require the same items. The core has no record for it. coa15 declares `s 663(3) statement of capital` and `s 663(3) class entry`, and a helper that tests one.
4. **A name for the person an offence charges, before it is known whether the officer is in default.** Most offences of Part 18 charge "the company and every officer in default", and s 715 charges "every director in default". The core's `Party` has `Company`, `Director` and `Officer in default`, but the rule has to take an officer whose default is not yet known (the answer is `NOTHING` until s 1121 says), and "any other person". coa15 declares `s 658(2) person charged` (the company, an officer of the company, a director of the company, any other person) and takes default as the separate input `s 1121 the officer is in default`.
5. **A nominee of the company as a party.** ss 660 to 662 and 668 speak of a nominee of the company. The core's `Party` has no `Nominee` (it has `Subscriber to the memorandum`, `Member` and others); the facts about a nominee are plain inputs of the rules instead.

## coa18

Written 2026-11-12 by part agent coa18.
Status: both entries describe types already declared inside coa18's own modules under the `s 853L` and `s 831(3)` prefixes; nothing in coa18 waits on the core.
How each was checked: `grep -n "Fine limit" coa-core.l4` (lines 200-204) and `grep -n "DECLARE" coa18-part24.l4 coa18-part23-ch1.l4`.

## 1. A fine limit of "the greater of an amount in pounds and a fraction of a level on the standard scale"

- **Where the text needs it:** s 853L(2)(a) and s 853L(6)(a) (lines 11570-11572 and 11576-11577 of `ukpga-2006-46.txt`): "a daily default fine not exceeding the greater of £500 and one-tenth of level 4 on the standard scale".
- **What the core has:** `Fine limit` (`coa-core.l4`:200-204) has four constructors: `a fine without a stated limit`, `a fine not exceeding the statutory maximum`, `a fine not exceeding a level on the standard scale` (level and fraction of the level), `a fine not exceeding an amount in pounds`. None says "the greater of" two amounts, so the pound floor of 500 cannot be written in it.
- **What coa18 declared instead:** `s 853L(2) daily default fine limit` with the constructor `s 853L(2)(a) the greater of an amount in pounds and a fraction of a level on the standard scale` (pounds, level, fraction), and a constructor `s 853L(2)(b) a fraction of a level on the standard scale` for the Scotland and Northern Ireland limb, which the core's `a fine not exceeding a level on the standard scale` could also have carried; and `s 853L(2) penalty`, a copy of the core's `Penalty` whose daily-fine field has that type.
- **What to hoist:** a fifth `Fine limit` constructor, for example `a fine not exceeding the greater of an amount in pounds and a fraction of a level on the standard scale` (pounds, level, fraction of the level).
  Then `s 853L(2) penalty` and `s 853L(2) daily default fine limit` can be deleted from coa18-part24 and the core's `Penalty` used as it is.
- **What the Act does not give:** the number of pounds a level on the standard scale stands for.
  The amount is an input in coa18 (`the pounds that the level on the standard scale named in the limit stands for`, s 853L(2) function `s 853L(2) the daily default fine limit in pounds`).

## 2. One shared type for "Companies Act accounts" and "IAS accounts"

- **Where the text needs it:** ss 831(3), 832, 836, 841 and 844 (lines 11142, 11162, 11241, 11309 and 11357 of `ukpga-2006-46.txt`, found with `grep -n "Companies Act accounts"`) distinguish "Companies Act accounts" from "IAS accounts" (the Act defines both in s 395, which is coa8's range).
- **What coa18 declared:** `s 831(3) kind of relevant accounts` (`coa18-part23-ch1.l4`:22) with the constructors `s 831(3)(a) Companies Act accounts` and `s 831(3)(b) IAS accounts`; ch2 and ch3 import ch1 for it.
- **Why it is listed here:** coa8 (s 395) owns the definitions and may declare its own type for the same distinction; at the merge two parts would then carry two types for one idea.
  The lead may hoist one type into the core and rewrite the two constructors' users in coa18-part23-ch1, ch2 and ch3.
  Nothing breaks if it is not hoisted: the names are prefixed and cannot collide.

## coa19

Constructors this part wanted in the core's `Party` and did not find.
It could not extend the core type from another module, so it declared small types of its own under its `s ...` prefix and used those; the lead may hoist the constructors and delete the local types.

Core `Party` (`coa-core.l4`, lines 85-101) has: `Company`, `Director`, `Shadow director`, `Company secretary`, `Member`, `Subscriber to the memorandum`, `Officer in default`, `Auditor`, `Creditor`, `Debenture holder`, `Person with significant control`, `Registrar`, `Secretary of State`, `Court`, `Takeover Panel`, `Competent authority`.

| wanted in `Party` | where the text uses it | the local type that stands in for it |
| --- | --- | --- |
| a liquidator of a company | s 859H(3)(a), s 874(1), s 889(1): a charge is void against "a liquidator" | `s 859H(3) party against whom the charge may be void`, `s 874(1) party against whom the charge may be void`, `s 889(1) party against whom the charge may be void` (in `coa19-a1-after.l4`, `coa19-ch1-registrar.l4`, `coa19-ch2-scotland.l4`) |
| an administrator of a company | the same three provisions | the same three types |
| the person who obtains an order for the appointment of a receiver or manager, or appoints one under an instrument | s 859K(2), s 871(1): the person who must give notice to the registrar within 7 days | `s 859K party` in `coa19-regulative.l4` (it also carries the company and the registrar, so that one DEONTIC type serves every rule in that module) |
| a person interested in a charge | ss 859A(2), 859F(3), 859J(1), 860(2), 878(2): "the company or a person interested in the charge" | plain BOOLEAN inputs ("I am the company or a person interested") |
| the Registrar of Titles and the Registrar of Deeds (Northern Ireland) | s 868(1), (2), (4): the officials who must cause copies to be delivered to the registrar | not modelled as parties; the duties are encoded for what reaches the company (`s 868(1) ...`, `s 868(2) ...`, `s 868(4) ...`) |

No new `Fine limit`, `Mode of conviction`, `Penalty` or `Place of registration` constructor was needed: every penalty in this range is a `Penalty OF ...` built from the core's constructors, and Chapters 1 and 2 use the core `Place of registration`.

## coa21

Part coa21, Companies Act 2006, ss 942 to 993.
Each item names what was wanted, where it was needed, and the own type this part declared instead (every name begins with its section label, so nothing collides at the merge).
The lead may hoist any of them into `coa-core.l4`; if one is hoisted, the own type below can be replaced by the core's.

1. **Party constructors for "a person" and for "the offeror".**
   The core `Party` (`Company`, `Director`, `Member`, `Takeover Panel`, and so on) has no constructor for an arbitrary person required to act by a Panel notice (s 947) or for the person making a takeover offer (ss 981 and 984).
   Own types: `s 947 party` (`s 947 the person required by the notice`), `s 981 party` (`s 981 the offeror`) and `s 984 party` (`s 984 the offeror`), each with its own action type (`s 947 act`, `s 981 act`, `s 984 act`).
   The regulative rule in `coa21-ch2-opting-in.l4` (s 970) uses the core's `Company`, `Takeover Panel` and `Action of a party`.
2. **A "greater of an amount and a level" daily default fine.**
   The core `Fine limit` has `a fine not exceeding the statutory maximum`, `... a level on the standard scale` and `... an amount in pounds`, but no variant for "one-fiftieth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale" (s 980(8)(b)(i) and s 984(7)(b), fork F2).
   Own type: `s 980(8) daily default fine limit` with two constructors (a fraction of the statutory maximum; a fraction of the greater of an amount in pounds and a level), and, because the core `Penalty` types its daily fine as `MAYBE Fine limit`, a record `s 980(8) penalty` with the same fields as `Penalty` and the own limit type for the daily fine.
   The wanted core change: a `Fine limit` constructor `a fine not exceeding the greater of an amount in pounds and a level on the standard scale`, taking a fraction, the pounds and the level.

## coa22

Status (2026-11-13): one item. Nothing here has been hoisted into `coa-core.l4`; the part works without it because the type is declared under this part's own prefix.

## 1. A fine of "one-tenth of the greater of a sum and a level on the standard scale"

**What the text needs.** Section 1033(7) (`src:14514`) ends with a daily default fine written "one-tenth of the greater of £5,000 or level 4 on the standard scale", run together on the same line with the earlier wording "one-tenth of level 5 on the standard scale" (finding 1 and fork F14 in `NOTES.md`). The core's `Fine limit` has no constructor for "the greater of a sum and a level on the standard scale", and a constructor of a core type cannot be added from another module.

**What this part declares instead** (`coa22-part31-ch3.l4`, under the section's label):

```
DECLARE `s 1033(7) one-tenth of the greater of a sum and a level on the standard scale` HAS
    `s 1033(7) the sum in pounds` IS A NUMBER
    `s 1033(7) the level on the standard scale` IS A NUMBER
```

used as `` `s 1033(7) the daily default fine on the second wording` `` (the value `... OF 5000, 4`).

**What the lead would hoist.** A constructor of `Fine limit`, for example

```
`a fine not exceeding one-tenth of the greater of a sum in pounds and a level on the standard scale`
    HAS `the sum in pounds` IS A NUMBER, `the level on the standard scale` IS A NUMBER
```

(the fraction one-tenth is part of the name, as in the text; a second constructor would be needed for any other fraction). The pounds a level on the standard scale stands for are not in the Act and stay an input, as for every other `Fine limit`; the function `s 998(4) the amount in pounds of the fine limit` in `coa22-part30.l4` converts the existing constructors to pounds and does not handle this one, which would then need a branch.

**Sections that need it:** s 1033(7) only, in this range. PLAN.md section 3 mentions a "greater of £500 and one-tenth of level 4" fine with 2 uses in the Act and no constructor; that is a differently worded formula, and I have not checked whether it shares a constructor with this one.

## coa23

Constructors and types the core lacks, which the coa23 modules declare under their own prefix (`coa23-nouns.l4`); the lead may hoist them into `coa-core.l4` at the merge.

| wanted in the core | declared now as | sections that need it |
| --- | --- | --- |
| `Party`: `Any person` | `s 1065 any person` (type `s 1065 person dealing with the registrar`) | ss 1065, 1085(1), 1086(1): "Any person may ..." |
| `Party`: `Individual who delivers a document to the registrar` | `s 1067A an individual who delivers a document to the registrar` (same type) | ss 1067A, 1067B |
| a registrar-for-a-place type | `s 1060 registrar of companies` with `s 1060(1)(a)`, `(b)`, `(c)` | ss 1060(3), 1060(4) |
| `Penalty`: a constructor for "imprisonment for a term not exceeding the general limit in a magistrates' court" | not needed: `s 1092B(3) the penalty for the offence` takes the limit as an input in months and builds the core's `Period OF n, Months` | s 1092B(3) |

No type or constructor of the core was missing for the rest of the range: `Place of registration`, `Form of document`, `Period`, `Unit of time`, `Penalty`, `Mode of conviction`, `Fine limit`, `Party` (Registrar, Company, Director) and `Action of a party` are used as they are.

## coa24

Types or constructors the keel's `coa-core.l4` lacks, for the lead to hoist at the merge. Each was worked around in the part's own modules under its own prefix; nothing in the core was edited.

1. **`Fine limit` has no "one-tenth of the greater of an amount and a level".** Needed by s 1093(4) in one of the two versions of the text it carries ("a daily default fine not exceeding one-tenth of the greater of £5,000 or level 4 on the standard scale"; the plan's section 3 notes a related gap, "greater of £500 and one-tenth of level 4", a different shape: here the "greater of" sits inside the one-tenth). Workaround: `s 1093(4) the punishment for the offence under subsection (3)` computes the pounds from an input (level 4) and builds `a fine not exceeding an amount in pounds`. Wanted: a constructor with two fields, the fixed pounds and the level, and the fraction.
2. **`Period` cannot carry "the general limit in a magistrates' court".** Needed by ss 1110B(4)(b)(i) and 1112A(3)(b)(i). The number is not in the Act, and s 1131(2) substitutes "six months" for an offence committed before 2 May 2022. Workaround: a `MAYBE Period` input and `s 1131(2) the term of imprisonment the provision refers to` in `coa24-penalty.l4`. Wanted: a `Unit of time` constructor (or a `Period` constructor) for "the general limit in a magistrates' court", so that a `Penalty` can say it without an input.
3. **`Place of registration` is used for the place of conviction or proceedings (a naming gap, not a capability gap).** `s 1098E(5)`, `s 1098G(5)`, `s 1112(3)`, `s 1126(2)-(3)`, `s 1130(2)(b)` and `s 1132(1)` turn on England and Wales, Scotland or Northern Ireland as the place of the court or the proceedings, not of a company's registration, and they take a `Place of registration` input (checked: `grep -n "Place of registration" coa24-*.l4`). The three constructors are the right ones; the type's name is not. Wanted, if the lead agrees: an alias or a second type `Place` with the same three constructors.
4. **`Party` has no authorised corporate service provider (a convenience gap).** The core `Party` has `Company`, `Registrar`, `Creditor`, `Member` and `Court`, but not an authorised corporate service provider. The three regulative rules of this part (`s 1093(3)`, `s 1098E(1)`, `s 1113(3)`) declare their own party types under their section labels (`s 1093(3) party`, `s 1098E(1) party`, `s 1113(3) party`), which also keeps each rule's `PARTY` readable; they do not need the core type, so this is listed only in case the merge wants one.

## coa25

The core (`coa-core.l4`) was not edited. This part declared the following under its own prefix because the core lacks them; the lead may hoist any of them at the merge (each is used by the sections named).

| what the core lacks | declared here as | sections that need it |
| --- | --- | --- |
| `Party` constructors for the persons a regulative rule names: the valuer; an officer of the company (as the person a valuer questions); a judicial factor; the Charity Commission; the Charity Commission for Northern Ireland; the Regulator of Community Interest Companies; the applicant for approval of a business name; the person issuing out process; the person to whom Chapter 2 of Part 41 applies | `s 1150 party` (the valuer, an officer), `s 1154 party` (judicial factor, the two Commissions, the Regulator), `s 1195 party`, `s 1139 party`, `s 1202 party` | ss 1139(4), 1150(4), 1154, 1155(1), 1195, 1202, 1204 |
| a typed list of "the court" for each part of the United Kingdom (the core has the generic `Court` party only) | `s 1156 court`, `s 1183 court` (two identical lists: s 1156(1) and s 1183 each define "the court", for the Companies Acts and for Part 40) | ss 1156(1), 1183 |
| an instant (a day and an hour of the day) for periods counted in hours | `s 1147 instant` | s 1147 |
| a way to say "the general limit in a magistrates' court" as a period (the Act does not state it) | a plain NUMBER of months, asked as an input; no type | ss 1186(2), 1191(2) |
| a kind of direction to change a company's name (ss 67, 75, 76, 76A, 76B) | `s 1198A direction` | ss 1198A(5), 1198B(7) |

No constructor of a core type was needed beyond these; `Penalty`, `Fine limit`, `Mode of conviction`, `Period`, `Unit of time`, `Form of document` and `Place of registration` were used as the core declares them.

## coa26

Constructors and types that `coa-core.l4` lacks and that coa26 declared under its own prefix instead (the lead may hoist them at the merge).

| wanted in the core | used by | what coa26 declared instead |
| --- | --- | --- |
| `Party`: `Recognised supervisory body`, `Recognised qualifying body`, `Independent Supervisor`, `Auditor General`, `Approved third country competent authority` | ss 1223A, 1224A, 1225-1225G, 1227-1237 (the duties and powers of these parties; their duties are decision functions only, since `Auditor` is the only one of them the core has a constructor for) | nothing: the duties of these parties are asked as decision functions, and the regulative rules use the core `Auditor` (an Auditor General holding office is a statutory auditor) |
| `Fine limit`: a constructor for "one-tenth of the greater of an amount and the amount corresponding to a level on the standard scale, for each day" (2 uses in this Part: ss 1213(7) and 1215(6)) | ss 1213(7), 1215(6) | `s 1213(7) fine for continuing` IS ONE OF `s 1213(7) a fine without a stated limit`, `s 1213(7) a fine not exceeding a sum for each day on which the act or the failure continues` HAS `s 1213(7) pounds for each day` |
| a court type with `the High Court` and `the Court of Session` ("the court" means the High Court or, in Scotland, the Court of Session: ss 1225C(3), 1225F(10), 1236(3)) | those three subsections | `s 1225C(3) court`, `s 1225F(10) court`, `s 1236(3) court` (three identical two-constructor types, one per subsection, so that no name is shared) |
| `Mode of conviction`: "on summary conviction in England and Wales or Northern Ireland" as one mode (s 1224B(2)(b)(ii)) | s 1224B(2) | the core's separate modes for England and Wales and for Northern Ireland, with the same answer for each |

## coa27

Types and constructors the core (`coa-core.l4`) lacks that this part needed or wanted. Each is declared, where used, under this part's own prefix; the lead may hoist them at the merge.

1. **A `Fine limit` for "one-tenth of the greater of £5,000 or level 4 on the standard scale".** Wanted: a constructor such as `a fine not exceeding a fraction of the greater of an amount in pounds and a level on the standard scale` HAS `fraction` (NUMBER), `pounds` (NUMBER), `level` (NUMBER). Needed by s 1248(8)(b), second extent of the text (src:17671; fork F-G). Not declared in this part: the amount is computed as a NUMBER by `s 1248(8)(b) the daily fine on the second extent in pounds`, with the pounds of level 4 an input.
2. **A per-day fine that is not s 1125's "daily default fine".** Section 1248(8)(b) says "for each day on which the failure continues" and does not use the words "daily default fine". The core `Penalty` has only the `daily default fine for continued contravention` slot, and `s 1248(8) the penalty on the first extent of the text for` uses it with a comment. Wanted: a `Fine limit` wrapper such as `a fine for each day on which the failure continues` HAS a `Fine limit`.
3. **`Party` constructors** the offences and Part 43 name and the core lacks: the issuer, the voteholder, the registered third country auditor, the recognised supervisory body, the Independent Supervisor, the third country competent authority, the Tribunal, the Treasury, the statutory auditor. Not needed in this part: the three regulative rules (`s 1248(5)(a)`, `s 1248(7)(a)`, `s 1253B(2)`) use `Company` and `Secretary of State`, which the core has.

## coa28

Constructors and types I wanted from `coa-core.l4` and did not find.
Each is declared under my own prefix in `coa28-part44.l4` or `coa28-sch1b.l4` instead, as the brief requires, so nothing here blocks the merge; the lead may hoist them.

## Needed by a rule in layer 1 (declared locally)

- **A `Party` for "the person to whom information is disclosed".**
  Core `Party` has `Member`, `Creditor`, `Registrar`, `Secretary of State`, `Court` and others, but no recipient of information and no public authority.
  `s 1281 241A(5)` (the new s 241A(5) of the Enterprise Act 2002) forbids "the person to whom it is disclosed" to use the information for another purpose, and the discloser in s 241A(1) is "a public authority".
  Wanted constructors: `Public authority` and `Recipient of information`.
  Declared locally as `s 1281 241A(5) party` with the one constructor `s 1281 241A(5) the person to whom the information is disclosed`, in `coa28-part44.l4`.
- **Typed actions.**
  Core has one generic action, `Action of a party` (a performer, a recipient and a `STRING`), and no action types.
  A `MUST` or `SHANT` over a `STRING` cannot be told from any other string, so each regulative rule here declares an action type of its own: `s 1281 241A(5) action` (`coa28-part44.l4`), `sch 1B para 1(6) action` and `sch 1B para 11 action` (`coa28-sch1b.l4`).
  Wanted from the core, if the family wants shared actions: `Has regard to the effect on third parties` (the company, sch 1B para 1(6)), `Withdraws a restrictions notice` (the company, sch 1B para 11), `Uses information for a purpose other than the permitted ones` (the recipient, s 241A(5)).

## Wanted only if a merged jural layer names the parties (not used by layer 1)

The jural relations in `NOTES.md` name parties the core `Party` lacks: each House of Parliament, the Treasury, the holder of a relevant interest (sch 1B), a person aggrieved (sch 1B paras 4, 8), the offeror, the offeree company, the board of the offeree company and the employees' representatives (sch 1C).
Layer 1 does not need them as `Party` constructors, because the rules that use a `Party` are the three above and the other provisions are decision functions.

## coa29

Things the shared core `coa-core.l4` would need for this part's modules to use it instead of declaring their own copies.
None of them blocks anything: each module declares its own types under its own prefix and compiles and passes on 1.6.110 and 1.6.109.
The core is read-only for this part, so these are requests to the lead, to be decided at the merge.

1. **`Form of document` has two constructors; the Schedules need four.**
   `coa-core.l4:160` declares `hard copy form` and `electronic form` (from s 1168(2) and (3)).
   Schedule 4 para 8 speaks of a communication "otherwise than in hard copy form or electronic form", Schedule 5 para 15 of one "otherwise than in hard copy or electronic form or by means of a website", and Schedule 5 para 8 of a document "made available on a website".
   Own copies: `sch 4 form of the document or information` (hard copy form, electronic form, neither hard copy form nor electronic form; `coa29-sch4.l4`) and `sch 5 form of the document or information` (hard copy form, electronic form, made available on a website, none of those forms; `coa29-sch5.l4`).
   Wanted in the core: two more constructors (`made available on a website`, `neither of those forms`); the two copies would then be deleted.
2. **There is no core type for how a document is sent.**
   Section 1168(3)(a) names "electronic means (for example, by e-mail or fax)" and Schedules 4 and 5 add "by hand", "by post" and (Schedule 5) "handed to the intended recipient".
   Own copies: `sch 4 means of sending or supplying` (by hand, by post, by electronic means, by some other means) and `sch 5 means of sending or supplying` (handed to the intended recipient, by hand to an address, by post, by electronic means, by some other means).
   Wanted in the core: one type with these constructors, if another part needs it.
3. **The core's `Period` has a length but no first and last day.**
   `coa-core.l4:176` is `Period` (number of units, unit).
   Schedule 5 para 14(1) needs "the period throughout which" a document must be on a website, by its first and last day (the period specified by another provision, or the 28 days beginning with the notification date).
   Own copy: the record `sch 5 period of availability` (first day of the period, last day of the period; `coa29-sch5.l4`).
   Wanted in the core: a `Dated period` (first day, last day), if other parts count periods by their days.
4. **Nothing is needed for the penalties of Schedule 3.**
   Schedule 3 is inert here (fork F12).
   If it is encoded later, the core's `Penalty` (`coa-core.l4:210`) and `Fine limit` (`coa-core.l4:200`) fit its text: `on conviction on indictment`, `on summary conviction in England and Wales`, `on summary conviction in Scotland` and `on summary conviction in Northern Ireland` (two constructors), the fraction of the statutory maximum for the daily default fine.
   The pounds the statutory maximum stands for would be an input, as the core says.

## coa30

Types and constructors `coa-core.l4` lacks that this part needed. Each is declared in `coa30-regulative.l4` under this part's own prefix; the lead may hoist them into the core at the merge (a `DEONTIC` takes one party type, the core's `Party` has no constructor for the supervisory body, the registered third country auditor, the delegated body or a person within paragraph 3(6), and a part cannot extend a core type; the core does have `Secretary of State`, which is therefore re-declared here under this part's prefix beside those actors rather than mixed with `Party`).

| what | where declared | constructors or fields | sections that need it |
| --- | --- | --- | --- |
| `Party` constructors for the supervisory-body Schedules | `sch 10 para 2(4) party` in `coa30-regulative.l4` | the Secretary of State (the core has this one: it is repeated so that one party type serves every rule); the recognised supervisory body; a person within paragraph 3(6); the registered third country auditor; the body designated by the delegation order; the person who wishes to cite an instrument | Schedule 10 paras 2(4), 3(3), 3(5), 3(11), 13(12), 20ZA; Schedule 12 para 4; Schedule 13 paras 8(1), 9(3), 10(1), 10(3) |
| an action type for those duties | `sch 10 para 2(4) act` in `coa30-regulative.l4` | one nullary constructor per duty (give written notice of refusal; give written notice of the intention to revoke; take reasonably practicable steps; publish the notice; make representations; give notice of the making of the order; deliver a summary of inspections; pay the costs; print and make available; endorse a copy; make a report; lay the report) | the same |

Proposed for the core, if the lead wants a shared version: `Party` constructors `Supervisory body`, `Recognised qualifying body`, `Registered third country auditor`, `Delegated body`. Not needed by this part: a `Fine limit`, `Penalty` or `Mode of conviction` (Schedules 10 to 16 create no offence and fix no fine; the core names expected for them in PLAN.md section 6 were not used).
