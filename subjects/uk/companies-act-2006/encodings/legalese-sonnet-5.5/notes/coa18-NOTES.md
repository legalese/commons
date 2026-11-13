# NOTES (coa18): Companies Act 2006 (United Kingdom), Parts 22 to 24, ss 791 to 859 (lines 10757-11596 of `ukpga-2006-46.txt`)

Written 2026-11-12 by part agent coa18 (Sonnet 5.5) for run `dst-coa18`, on the stable binary 1.6.110 (main, e51181d, 2026-11-11), cross-checked on 1.6.109.

**Status and how each kind of claim here was checked.**

- Claims about the code (names, counts, branch tags) were taken from the files in this folder on the day this file was assembled, by `work/build-notes.py`, which reads them; none is copied from an earlier note.
- Claims about the text were checked against `inputs/ukpga-2006-46.txt`: the quoted words in every `FALSE-kind` and `NOTHING-kind` comment of the layer-1 modules (490 quoted pieces, 0 not found, by `work/check-quotes.py`), the quoted licence of every fork (checked the same way), and every `@ref` locator (`srcrefs.py check --refs` and `--strict`, 0 problems per module).
- Expected values in the tests were decided from the text before each run and are written beside their assertion; a failing assertion was treated as a finding (see "What the text turns out to say", finding 12, for the one expected value I had miscounted).
- The scratch scripts in `../work/` (expand, gentests, coverage, forks, build-notes, check-quotes) are not shipped; the `.l4` files and this file are.
- **About this text.** The source is a plain-text rendering of the Act made by a converter script from legislation.gov.uk (Open Government Licence v3.0, `inputs/STUB-SOURCE-LICENSE.md`).
  It is not the official text, and nothing here is "verified against the official text".
  The converter shows a provision it could not render, or that is omitted, as a line of dots (`. . . .`); those rows are `repealed or blank in this text`.

## Where PLAN.md and the brief differ (the brief governs)

1. **The ranges.** The task message called this range "Parts 22 and 23"; the brief and PLAN.md section 6 give lines 10757-11596, ss 791 to 859, which also hold Part 24 (annual confirmation of accuracy of information on register, ss 853A to 859).
   I encoded all of it: the coverage table has a row for every non-blank line of 10757-11596 (840 lines).
2. **`REFUSE` and `YMD`.** PLAN.md section 5 records that both supplied builds (1.6.109 and 1.6.110) check and run `REFUSE`, `#ASSERT REFUSED` and `YMD`, although the brief says the stable line does not have them.
   The brief governs: coa18 uses none of the three (`grep -c "REFUSE\|YMD" coa18-*.l4` finds no occurrence in any file, checked at assembly), writes `NOTHING` for "not covered" and `Date day month year` for dates.
3. **Where PLAN.md and the brief agree but I added a rule of my own.** Every top-level name, constructor and field type in coa18 begins with its section label; PLAN.md section 2 says the same.
   A test fixture name also begins with the section label: PLAN.md section 5 records that two fixtures with one name are a "multiple definitions" error.
4. **Seams.** PLAN.md section 4 names the default input type `MAYBE BOOLEAN`; I used it for every seam whose answering section can itself answer "not covered", and plain `BOOLEAN` where PLAN.md section 4 allows it (a fact a witness can state: ss 9(5)(c), 86(2), 87, 88A(2), 88B) and for the keel answers that never answer `NOTHING` (ss 4(2), 1163(1), 1165(2), 1167); the table under "Seams (coa18)" gives each input and its type.

## Seat

The seat is the one the brief assumes (assumed, not ruled): an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows if it is not done.
There is never a seat for an official: where a provision addresses only the registrar, the Secretary of State or the court, it is in layer 1 for what it decides and in the seat only where it means something to the person.

`coa18-seat.l4` holds 65 questions, every one named "Under section N, ...", each with `@export` and `@desc`, grouped under `§` headings in the text's order; `coa18-cases-seat.l4` has 139 assertions (at least one per question, checked by script; they include cases outside the encoding that assert `NOTHING`).
The seat question about the company's power to give a notice (s 793(1)) asks `s 791` first, and so does the question about s 791 itself; the gate is not threaded into the other Part 22 questions or into ss 792 to 828 (fork F1), which take the facts the person states.

- **The Companies Act 2006, Parts 22 to 24 -- the questions of a director, secretary, member or person dealing with a company**
- **Part 22 -- information about interests in a public company's shares**
  - *A notice requiring information about interests in shares (ss 791 to 796)*
    - Under section 791, does Part 22 apply to this company?
    - Under section 793(1), may the company give me a notice requiring information about my interest in its shares?
    - Under section 793(1)(b), was my interest within the three years before the notice?
    - Under section 793(2)(b), may the notice require me to give further information about my interest?
    - Under section 793(4), may the notice require me to give particulars of another interest in the shares?
    - Under section 793(7), did I give the information within the time the notice specified?
    - Under section 794(1), may the company apply to the court for an order restricting my shares?
    - Under section 795(1)(a), do I commit an offence by failing to comply with the notice?
    - Under section 795(1)(b), do I commit an offence by a false statement in purported compliance with the notice?
    - Under section 795(3), what is the longest prison term, in months, on conviction?
    - Under section 796(1), am I not obliged to comply with a notice under section 793?
  - *The effects of an order restricting shares, and the court's powers (ss 797 to 802)*
    - Under section 797(1)(a), is a transfer of my shares void?
    - Under section 797(1)(b), are no voting rights exercisable in respect of my shares?
    - Under section 797(1)(d), is no payment to be made of sums due from the company on my shares?
    - Under section 798(2)(a), do I commit an offence by disposing of shares subject to restrictions?
    - Under section 798(2)(b), do I commit an offence by voting shares subject to restrictions?
    - Under section 799(2), may I apply to the court to relax the restrictions on shares?
    - Under section 800(3), is the court barred from ordering that the shares cease to be subject to restrictions?
    - Under section 802(3), how much of the proceeds of sale must the court order paid to me?
  - *Members' power to require the company to investigate, and the report (ss 803 to 807)*
    - Under section 803(2), is the company required to investigate interests in its shares?
    - Under section 803(3), does our request meet the requirements?
    - Under section 805(1), by what date must the company make the report available for inspection?
    - Under section 805(2), how many interim reports must the company prepare?
    - Under section 805(6), by what date must the company notify the members where the report is available?
    - Under section 806(1), does the company commit an offence by failing to notify the registrar of the place of the reports?
    - Under section 806(1)(b), do I as an officer commit an offence?
    - Under section 807(1), must a report the company prepared on its investigation be open to inspection by any person without charge?
    - Under section 807(2), am I entitled to a copy of the report?
    - Under section 807(2), by what date must the company provide the copy?
  - *The register of interests disclosed (ss 808 to 819)*
    - Under section 808(2), by what date must the company enter the information in the register?
    - Under section 811(2), am I entitled to a copy of an entry in the register?
    - Under section 811(4), does my request contain the information required?
    - Under section 812(1), must the company comply with my request or refuse it?
    - Under section 813(1)(a), does the company commit an offence by refusing me inspection of the register?
    - Under section 814(2), do I commit an offence by disclosing information obtained from the register?
    - Under section 816, may the company remove an entry made more than six years ago?
    - Under section 817(2), may I apply to the company for the removal of an entry about me?
    - Under section 819(1), must the company that has ceased to be public keep the register?
  - *Whether a person has an interest in shares (ss 820 to 825)*
    - Under section 820(4), am I treated as having an interest in the shares?
    - Under section 822(1), am I taken to be interested in shares in which my family is interested?
    - Under section 823(1), am I taken to be interested in shares in which a company I control is interested?
    - Under section 824(2), does section 824 apply to our agreement?
    - Under section 825(4), does my notification contain what is required?
- **Part 23 -- distributions**
  - *What a distribution is and what profits are available (ss 829 to 835)*
    - Under section 829(1), is this a distribution?
    - Under section 830(1), is the distribution within the profits available for the purpose?
    - Under section 830(2), what are the company's profits available for distribution?
    - Under section 831(1), is the distribution within the net asset restriction on public companies?
    - Under section 831(4), what are the company's undistributable reserves?
    - Under section 832(3), does the distribution leave the investment company with enough assets?
  - *The accounts that justify a distribution, and successive distributions (ss 836 to 840)*
    - Under section 836(2)(a), may the company justify the distribution by reference to interim accounts?
    - Under section 836(2)(b), may the company justify the distribution by reference to initial accounts?
    - Under section 840(1), what amount counts as the proposed distribution?
  - *Distributions in kind, unlawful distributions and the savings (ss 841 to 853)*
    - Under section 845(2), what is the amount of the distribution in kind?
    - Under section 847(2), what am I liable to do about the distribution I received?
    - Under section 849, may the company apply the profit in paying up debentures or unpaid amounts on its shares?
    - Under section 853(6), is the asset a fixed asset?
- **Part 24 -- annual confirmation of accuracy of information on register**
  - *The confirmation statement and its timing (ss 853A to 853G)*
    - Under section 853A(1), by what day must the company deliver its confirmation statement?
    - Under section 853A(5), on what day does the review period end?
    - Under section 853A(6), on what day does the next review period begin?
    - Under section 853C(2), must the company notify the registrar of a change in its principal business activities?
    - Under section 853D(2), must the company deliver a statement of capital with its confirmation statement?
    - Under section 853G(6)(a), must my name and address be delivered as a holder of 5% or more of a class?
  - *Failing to deliver the confirmation statement (s 853L)*
    - Under section 853L(1)(a), has the company committed an offence by not delivering its confirmation statement in time?
    - Under section 853L(1)(b), have I as an officer committed an offence by the company's late confirmation statement?
    - Under section 853L(6), what is the most the daily default fine can be in pounds?

### Seat audit of 2026-11-12

The lead asked for every seat question's name and `@export` text to be read against the layer-1 function its body calls, for a direction mismatch (a permission title over a bar, or the reverse) or a subject mismatch ("must I" over "have I", a duty over a privilege).
I read all 65 questions.
Three needed a change; the other 62 match their function in direction and subject.

- **Section 797(1)(d), direction (wording of the `@export` only).** The `@export` asked "May no payment be made ...?", a permission-form title over a bar (`s 797(1)(d) no payment may be made of sums due from the company on the shares`, JUST TRUE meaning payment is barred).
  It now reads "Is it the case that no payment may be made of sums due from the company on my shares ...? True means payment is barred; false means a liquidation, a court direction or the terms of an interim order displaces the bar." The question name is unchanged.
- **Section 807(1), subject.** The `@export` asked "May I inspect a report ... without charge?", the person's privilege, over a function that states a duty on the report (`s 807(1) the report must be open to inspection by any person without charge`).
  The question is now named "Under section 807(1), must a report the company prepared on its investigation be open to inspection by any person without charge?" and its `@export` asks the same, with "True means it must; false means the report is not one prepared under section 805".
- **Section 847(2), subject.** The question "must I repay the distribution?" sat over a function that answers what the member is liable to do (`s 847(2) what the member is liable to do`: repay, pay the value, or not liable), so a "pay its value" answer read as a "no".
  It is now named "Under section 847(2), what am I liable to do about the distribution I received?" and its `@export` asks the three-way question.

Judged consistent and left alone, because the answer space is the same on both sides:

- **Section 849, "may the company apply the profit in paying up debentures or unpaid amounts on its shares?"** The function is named as a permission but returns only `JUST FALSE` (an unrealised profit: the company must not) or `NOTHING` (a realised profit: the section says nothing); it never returns `JUST TRUE`, so the question is not read as a grant.
  Re-titling it as a bar would invert the answers, so the title stays and the `@export` already says "False means it must not".
- **Section 800(3), "is the court barred ..."** is a bar on both sides (`JUST TRUE` is barred).
- **Section 796(1), "am I not obliged ..."** is the function's own wording (`JUST TRUE` is not obliged).

The three assertion groups that used the old names are restated in place in `coa18-cases-seat.l4` with a `-- RECONCILED 2026-11-12: was ...` line above each; their facts and expected values are unchanged.

### Name-test sweep of 2026-11-12

The sweep looked at every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised": 59 functions.
A function named for a grant or a power that answered `JUST FALSE` because an "if" gate failed now answers `NOTHING` (the Guide's "In short": a grant limited by its own wording, outside the limit).
A gate closed by the text ("only if", "only", "may not ... unless"), a bar, a duty and the provision's own question keep `JUST FALSE`.
A "may" function gated by "where", "when", "upon" or an equivalent, and every "entitled" function, are listed in the fork register and not flipped.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 7 | 11 | 14 | 7 |

The other 20 functions of the 59 already answered only `NOTHING` or are regulative rules, so the sweep changed nothing for them.
The "kept" column counts every function kept at `JUST FALSE` by the sweep's second test: the text closes the gate, or the function is a bar, a duty or the provision's own question.

**Flipped to `NOTHING`** (one fork line each, F42 to F48):

- F42: `s 793(2)(b) the notice may require the person to give further information`
- F43: `s 794(2) the court may direct that acts set out in the order shall not constitute a breach of the restrictions`
- F44: `s 799(3) the court may direct that acts set out in the order do not constitute a breach of the restrictions`
- F45: `s 812(6) the court may direct that the company is not to comply with any such request`
- F46: `s 816 the company may remove the entry from the register`
- F47: `s 817(4) the applicant may apply to the court for an order directing the company to remove the entry`
- F48: `s 818(3) the applicant may apply to the court for an order directing the company to include the information in the register`

**Kept `JUST FALSE`:**

- `s 801(2) the person may apply for an order under subsection (1)`: closed with "only"
- `s 815(1) the deletion of the entry is permitted`: "must not be deleted except in accordance with" (a bar with its own exceptions)
- `s 797(1)(c) no further shares may be issued in right of the shares or in pursuance of an offer made to their holder`: a bar
- `s 797(1)(d) no payment may be made of sums due from the company on the shares`: a bar
- `s 831(5) the company may include uncalled share capital as an asset in any accounts relevant for the purposes of this section`: a bar ("must not")
- `s 832(7) the company may include uncalled share capital as an asset in any accounts relevant for the purposes of this section`: a bar ("must not")
- `s 836(4) the accounts may not be relied on for the purposes of this Part and the distribution is treated as contravening this Part`: a bar ("may not be relied on")
- `s 849 the company may apply the profit in paying up debentures or any amounts unpaid on its issued shares`: a bar ("must not")
- `s 803(2) the company is required to exercise its powers under section 793`: a duty ("is required")
- `s 804(1) the company must exercise those powers in the manner specified in the requests`: a duty ("must")
- `s 832(1) the investment company may make the distribution out of its accumulated, realised revenue profits`: the conditions are closed by the text itself: (2) "only if", (3) "only", (5) "must also be met", (7) "must not"

**Listed: "may" with where, when or upon (or an equivalent):**

- `s 793(4) the notice may require the person to give such particulars with respect to that other interest as the notice requires` (where)
- `s 793(6) the notice may require the person to give particulars of the identity of the person who held that interest immediately upon his ceasing to hold it` (where)
- `s 794(1) the company may apply to the court for an order directing that the shares in question be subject to restrictions` (where)
- `s 794(3) the court may make an interim order` (on such an application)
- `s 800(5)(a) an application may be made for an order directing that the shares shall cease to be subject to those restrictions` (where)
- `s 801(3) the court may make such further order relating to the sale or transfer of the shares as it thinks fit` (where)
- `s 801(5) the court may order that the applicant's costs (in Scotland, expenses) be paid out of the proceeds of sale` (on)
- `s 807(5) the court may by order compel an immediate inspection or direct that the copy required be sent to the person requiring it` (in the case of)
- `s 813(3) the court may by order compel an immediate inspection or direct that the copy required be sent to the person requesting it` (in the case of)
- `s 817(2) that other person may apply to the company for the removal of the entry from the register` (where (the scope of subsection (1)))
- `s 836(2)(a) the distribution may be justified by reference to interim accounts` (where)
- `s 836(2)(b) the distribution may be justified by reference to initial accounts` (where)
- `s 850(1) the directors may treat the profit as realised` (where)
- `s 850(2) the directors may treat the loss as unrealised` (where)

**Listed: "entitled":**

- `s 820(5) the person is entitled to exercise or control the exercise of a right conferred by the holding of shares`
- `s 823(2) the person is treated as entitled to exercise or control the exercise of the voting power`
- `s 823(3) the person is treated as entitled to exercise or control the exercise of the voting power`
- `s 802(4) the applicant under section 801 is entitled to payment of his costs out of the proceeds before any person interested in the shares receives any part`
- `s 807(2) the person is entitled to be provided with a copy of the report or any part of it`
- `s 811(2) the person is entitled to be provided with a copy of any entry in the register`
- `s 853A(7) the company is entitled to assume that information that has been delivered to the registrar has been properly delivered`

Two seat questions call a flipped function and now answer null where they answered false: `Under section 793(2)(b), may the notice require me to give further information about my interest?` (no interest held) and `Under section 816, may the company remove an entry made more than six years ago?` (an entry six years old or less); their cases are restated in place with a `-- RECONCILED 2026-11-12` line.
No flipped function is called by another layer-1 function (checked by `grep` at assembly), so no caller's answer changed.

## What is encoded and what is not

- **Layer 1** (7 modules and 7 test modules): ss 791 to 853L, every subsection and paragraph that is not blank, with the Act's own words quoted above each rule and a `@ref` locator on each.
- **Layer 2** (`coa18-seat.l4`, `coa18-cases-seat.l4`): the questions above.
- **Regulative rules** (`PARTY ... MUST / SHANT ... WITHIN ... LEST BREACH`), 24, s 793(7), s 804(1), s 805(1), s 805(5), s 805(6), s 807(2), s 808(1), s 808(2), s 809(2), s 810(1), s 810(2), s 815(2), s 849, s 853A(1), s 853BA, s 853C(2), s 853CA(2), s 853CB(2), s 853D(2), s 853E(2), s 853F(3), s 853G(4), s 853H(2), s 853L(1); each is run with `#TRACE` in its test module except none.
  Where the text fixes a period or a condition for a duty, the same duty is also a decision function over the facts, so that it can be asserted.
- **Not encoded:** nothing in the range is left without a row; the rows that are `inert` are listed under "Coverage".

## Coverage (coa18)

One row per text unit of the range (heading, section, subsection, paragraph, sub-paragraph) and per quoted defined term, built by script from the text (`work/coverage.py`), each with exactly one disposition.
Every one of the 840 non-blank lines of 10757-11596 falls in some unit (the script checks it).
A row of disposition `fork` points at the fork-register entry that names the rule that encodes the chosen reading; a row of disposition `encoded` points at its rule.
A section row whose text is only its title is `inert` under reason 1 (a heading): its operative text is in the subsection rows beneath it.

Counts by disposition: encoded 398, fork 256, inert 125, repealed or blank in this text 27; total rows 806 (text units 761, defined-term rows 45).

| unit | lines | disposition | L4 name(s) and note |
| --- | --- | --- | --- |
| heading 10757 | 10757 | inert | reason 1 (heading) |
| heading 10758 | 10758 | inert | reason 1 (heading) |
| s 791 | 10759-10760 | fork | fork F1. section row: its text is in the subsection rows. `s 791 this Part applies to the company` |
| s 792 | 10761 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 792(1) | 10762 | encoded | `s 792(1) the shares are the company's shares for the purposes of this Part` |
| s 792(2) | 10763 | encoded | `s 792(2) a suspension of voting rights affects the application of this Part to interests in those or any other shares` |
| heading 10764 | 10764 | inert | reason 1 (heading) |
| s 793 | 10765 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 793(1) | 10766 | encoded | `s 793(1) the company may give notice to the person`; `s 793(1)(b) the date is within the three years immediately preceding the date on which the notice is issued` |
| s 793(1)(a) | 10767 | encoded | `s 793(1) the company may give notice to the person` |
| s 793(1)(b) | 10768 | fork | fork F2. `s 793(1) the company may give notice to the person`; `s 793(1)(b) the date is within the three years immediately preceding the date on which the notice is issued` |
| s 793(2) | 10769 | encoded | `s 793(2)(a) the notice may require the person to confirm that fact or to state whether or not it is the case`; `s 793(2)(b) the notice may require the person to give further information` |
| s 793(2)(a) | 10770 | encoded | `s 793(2)(a) the notice may require the person to confirm that fact or to state whether or not it is the case` |
| s 793(2)(b) | 10771 | fork | fork F42. `s 793(2)(b) the notice may require the person to give further information` |
| s 793(3) | 10772 | encoded | `s 793(3) the notice may require the person to give particulars of his own present or past interest` |
| s 793(4) | 10773 | encoded | `s 793(4) the notice may require the person to give such particulars with respect to that other interest as the notice requires` |
| s 793(4)(a) | 10774 | encoded | `s 793(4) the notice may require the person to give such particulars with respect to that other interest as the notice requires` |
| s 793(4)(b) | 10775-10776 | encoded | `s 793(4) the notice may require the person to give such particulars with respect to that other interest as the notice requires` |
| s 793(5) | 10777 | fork | fork F4. `s 793(5) kind of particular`; `s 793(5) the particulars referred to in subsections (3) and (4) include` |
| s 793(5)(a) | 10778 | fork | fork F4. `s 793(5) kind of particular`; `s 793(5) the particulars referred to in subsections (3) and (4) include` |
| s 793(5)(b) | 10779 | fork | fork F4. `s 793(5) kind of particular`; `s 793(5) the particulars referred to in subsections (3) and (4) include` |
| s 793(5)(b)(i) | 10780 | fork | fork F4. `s 793(5) kind of particular`; `s 793(5) the particulars referred to in subsections (3) and (4) include` |
| s 793(5)(b)(ii) | 10781 | fork | fork F4. `s 793(5) kind of particular`; `s 793(5) the particulars referred to in subsections (3) and (4) include` |
| s 793(6) | 10782 | encoded | `s 793(6) the notice may require the person to give particulars of the identity of the person who held that interest immediately upon his ceasing to hold it` |
| s 793(7) | 10783 | fork | fork F3. `s 793(7) the information required by the notice was given within the time specified`; `s 793(7) party`; `s 793(7) action`; `s 793(7) the person addressed must give the information required by the notice` |
| s 794 | 10784 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 794(1) | 10785 | encoded | `s 794(1) the company may apply to the court for an order directing that the shares in question be subject to restrictions` |
| s 794(1)(a) | 10786 | encoded | `s 794(1) the company may apply to the court for an order directing that the shares in question be subject to restrictions` |
| s 794(1)(b) | 10787-10789 | encoded | `s 794(1) the company may apply to the court for an order directing that the shares in question be subject to restrictions` |
| s 794(2) | 10790 | fork | fork F43. `s 794(2) the court may direct that acts set out in the order shall not constitute a breach of the restrictions` |
| s 794(3) | 10791-10792 | encoded | `s 794(3) the court may make an interim order`; `s 794(3) way of making an interim order`; `s 794(3) the interim order may be made in this way` |
| s 794(4) | 10793 | inert | reason 1 (not operative: a signpost, "Sections 798 to 802 make further provision"; fork-register note N1) |
| s 795 | 10794 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 795(1) | 10795 | fork | fork F4. `s 795(1)(a) the person commits an offence by failing to comply with the notice`; `s 795(1)(b) the person commits an offence by a false statement in purported compliance with the notice` |
| s 795(1)(a) | 10796 | fork | fork F4. `s 795(1)(a) the person commits an offence by failing to comply with the notice` |
| s 795(1)(b) | 10797 | fork | fork F4. `s 795(1)(b) the person commits an offence by a false statement in purported compliance with the notice` |
| s 795(1)(b)(i) | 10798 | fork | fork F4. `s 795(1)(b) the person commits an offence by a false statement in purported compliance with the notice` |
| s 795(1)(b)(ii) | 10799-10800 | fork | fork F4. `s 795(1)(b) the person commits an offence by a false statement in purported compliance with the notice` |
| s 795(2) | 10801 | encoded | the defence is an input of s 795(1)(a). `s 795(1)(a) the person commits an offence by failing to comply with the notice` |
| s 795(3) | 10802 | encoded | `s 795(3) the penalty on conviction` |
| s 795(3)(a) | 10803 | encoded | `s 795(3) the penalty on conviction` |
| s 795(3)(b) | 10804 | encoded | `s 795(3) the penalty on conviction` |
| s 795(3)(b)(i) | 10805 | encoded | `s 795(3) the penalty on conviction` |
| s 795(3)(b)(ii) | 10806 | encoded | `s 795(3) the penalty on conviction` |
| s 796 | 10807 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 796(1) | 10808 | encoded | `s 796(1) the person is not obliged to comply with a notice under section 793` |
| s 796(2) | 10809 | fork | fork F5. `s 796(2) the Secretary of State is barred from granting the exemption`; `s 796(2) the Secretary of State must not grant the exemption unless the conditions are met` |
| s 796(2)(a) | 10810 | fork | fork F5. `s 796(2) the Secretary of State is barred from granting the exemption`; `s 796(2) the Secretary of State must not grant the exemption unless the conditions are met` |
| s 796(2)(b) | 10811 | fork | fork F5. `s 796(2) the Secretary of State is barred from granting the exemption`; `s 796(2) the Secretary of State must not grant the exemption unless the conditions are met` |
| heading 10812 | 10812 | inert | reason 1 (heading) |
| s 797 | 10813 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 797(1) | 10814 | fork | fork F6. `s 797(1)(a) any transfer of the shares is void`; `s 797(1)(b) no voting rights are exercisable in respect of the shares`; `s 797(1)(c) no further shares may be issued in right of the shares or in pursuance of an offer made to their holder`; `s 797(1)(d) no payment may be made of sums due from the company on the shares` |
| s 797(1)(a) | 10815 | fork | fork F6. `s 797(1)(a) any transfer of the shares is void` |
| s 797(1)(b) | 10816 | fork | fork F6. `s 797(1)(b) no voting rights are exercisable in respect of the shares` |
| s 797(1)(c) | 10817 | fork | fork F6. `s 797(1)(c) no further shares may be issued in right of the shares or in pursuance of an offer made to their holder` |
| s 797(1)(d) | 10818 | fork | fork F6. `s 797(1)(d) no payment may be made of sums due from the company on the shares` |
| s 797(2) | 10819-10820 | fork | fork F6. `s 797(2) an agreement to transfer the shares is void` |
| s 797(3) | 10821-10822 | fork | fork F6. `s 797(3) an agreement to transfer any such right is void` |
| s 797(4) | 10823 | fork | fork F6. `s 797(4) the provisions of section 797 are displaced for the act` |
| s 797(4)(a) | 10824 | fork | fork F6. `s 797(4) the provisions of section 797 are displaced for the act` |
| s 797(4)(b) | 10825 | fork | fork F6. `s 797(4) the provisions of section 797 are displaced for the act` |
| s 798 | 10826 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 798(1) | 10827 | encoded | `s 798(1) this section applies` |
| s 798(2) | 10828 | fork | fork F4. `s 798(2)(a) the person commits an offence by exercising a right to dispose`; `s 798(2)(b) the person commits an offence by voting or appointing a proxy`; `s 798(2)(c) the holder commits an offence by failing to notify the restrictions`; `s 798(2)(d) the person commits an offence by entering into a void agreement` |
| s 798(2)(a) | 10829 | fork | fork F4, F7. `s 798(2)(a) the person commits an offence by exercising a right to dispose` |
| s 798(2)(a)(i) | 10830 | fork | fork F4, F7. `s 798(2)(a) the person commits an offence by exercising a right to dispose` |
| s 798(2)(a)(ii) | 10831 | fork | fork F4, F7. `s 798(2)(a) the person commits an offence by exercising a right to dispose` |
| s 798(2)(b) | 10832 | fork | fork F4, F7. `s 798(2)(b) the person commits an offence by voting or appointing a proxy` |
| s 798(2)(c) | 10833 | fork | fork F4, F7. `s 798(2)(c) the holder commits an offence by failing to notify the restrictions` |
| s 798(2)(d) | 10834 | fork | fork F4. `s 798(2)(d) the person commits an offence by entering into a void agreement` |
| s 798(3) | 10835 | encoded | `s 798(3)(a) the company commits an offence`; `s 798(3)(b) the officer of the company commits an offence` |
| s 798(3)(a) | 10836 | encoded | `s 798(3)(a) the company commits an offence` |
| s 798(3)(b) | 10837 | encoded | `s 798(3)(b) the officer of the company commits an offence` |
| s 798(4) | 10838 | encoded | `s 798(4) the penalty on conviction` |
| s 798(4)(a) | 10839 | encoded | `s 798(4) the penalty on conviction` |
| s 798(4)(b) | 10840 | encoded | `s 798(4) the penalty on conviction` |
| s 798(5) | 10841 | fork | fork F6. `s 798(5) the provisions of section 798 are displaced for the act` |
| s 798(5)(a) | 10842-10844 | fork | fork F6. `s 798(5) the provisions of section 798 are displaced for the act` |
| s 798(5)(b) | 10845 | fork | fork F6. `s 798(5) the provisions of section 798 are displaced for the act` |
| s 799 | 10846 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 799(1) | 10847 | encoded | `s 799(1) an application may be made to the court on that ground` |
| s 799(2) | 10848 | encoded | `s 799(2) the person may make an application for an order under section 799` |
| s 799(3) | 10849 | fork | fork F44. `s 799(3) the court may direct that acts set out in the order do not constitute a breach of the restrictions` |
| s 800 | 10850 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 800(1) | 10851 | encoded | `s 800(1) an application may be made to the court for an order directing that the shares shall cease to be subject to restrictions` |
| s 800(2) | 10852 | encoded | `s 800(2) the person may make an application for an order under section 800` |
| s 800(3) | 10853 | fork | fork F5. `s 800(3) the court is barred from making an order under section 800` |
| s 800(3)(a) | 10854 | fork | fork F5. `s 800(3) the court is barred from making an order under section 800` |
| s 800(3)(b) | 10855 | fork | fork F5. `s 800(3) the court is barred from making an order under section 800` |
| s 800(4) | 10856 | encoded | `s 800(4) the order may continue the restrictions` |
| s 800(5) | 10857 | encoded | `s 800(5)(a) an application may be made for an order directing that the shares shall cease to be subject to those restrictions`; `s 800(5)(b) subsection (3) does not apply in relation to the making of such an order` |
| s 800(5)(a) | 10858 | encoded | `s 800(5)(a) an application may be made for an order directing that the shares shall cease to be subject to those restrictions` |
| s 800(5)(b) | 10859 | encoded | `s 800(5)(b) subsection (3) does not apply in relation to the making of such an order` |
| s 801 | 10860 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 801(1) | 10861 | encoded | `s 801(1) the court may order that the shares subject to restrictions be sold, subject to the court's approval as to the sale` |
| s 801(2) | 10862 | encoded | `s 801(2) the person may apply for an order under subsection (1)` |
| s 801(3) | 10863 | encoded | `s 801(3) the court may make such further order relating to the sale or transfer of the shares as it thinks fit` |
| s 801(4) | 10864 | encoded | `s 801(4) the person may apply for an order under subsection (3)` |
| s 801(4)(a) | 10865 | encoded | `s 801(4) the person may apply for an order under subsection (3)` |
| s 801(4)(b) | 10866 | encoded | `s 801(4) the person may apply for an order under subsection (3)` |
| s 801(4)(c) | 10867 | encoded | `s 801(4) the person may apply for an order under subsection (3)` |
| s 801(5) | 10868 | encoded | `s 801(5) the court may order that the applicant's costs (in Scotland, expenses) be paid out of the proceeds of sale` |
| s 802 | 10869 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 802(1) | 10870 | fork | fork F41. `s 802(1) the sum to be paid into court for the benefit of the persons who are beneficially interested in the shares` |
| s 802(2) | 10871 | fork | fork F4. `s 802(2) the person may apply to the court for the whole or part of those proceeds to be paid to him` |
| s 802(3) | 10872 | encoded | `s 802(3) the amount the court shall order paid to the applicant` |
| s 802(3)(a) | 10873 | encoded | `s 802(3) the amount the court shall order paid to the applicant` |
| s 802(3)(b) | 10874-10875 | encoded | `s 802(3) the amount the court shall order paid to the applicant` |
| s 802(4) | 10876 | encoded | `s 802(4) the applicant under section 801 is entitled to payment of his costs out of the proceeds before any person interested in the shares receives any part` |
| heading 10877 | 10877 | inert | reason 1 (heading) |
| s 803 | 10878 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 803(1) | 10879 | encoded | `s 803(1) the persons may require the company to exercise its powers under section 793` |
| s 803(2) | 10880 | fork | fork F8. `s 803(2) the company is required to exercise its powers under section 793` |
| s 803(3) | 10881 | fork | fork F9. `s 803(3) the request meets the requirements of this subsection` |
| s 803(3)(a) | 10882 | fork | fork F9. `s 803(3) the request meets the requirements of this subsection` |
| s 803(3)(b) | 10883 | fork | fork F9. `s 803(3) the request meets the requirements of this subsection` |
| s 803(3)(b)(i) | 10884 | fork | fork F9. `s 803(3) the request meets the requirements of this subsection` |
| s 803(3)(b)(ii) | 10885 | fork | fork F9. `s 803(3) the request meets the requirements of this subsection` |
| s 803(3)(b)(iii) | 10886 | fork | fork F9. `s 803(3) the request meets the requirements of this subsection` |
| s 803(3)(c) | 10887 | fork | fork F9. `s 803(3) the request meets the requirements of this subsection` |
| s 804 | 10888 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 804(1) | 10889 | encoded | `s 804(1) the company must exercise those powers in the manner specified in the requests`; `s 804(1) the company that is required under section 803 must exercise its powers in the manner specified` |
| s 804(2) | 10890 | encoded | `s 804(2) the officer of the company commits an offence` |
| s 804(3) | 10891 | encoded | `s 804(3) the penalty on conviction` |
| s 804(3)(a) | 10892 | encoded | `s 804(3) the penalty on conviction` |
| s 804(3)(b) | 10893 | encoded | `s 804(3) the penalty on conviction` |
| s 805 | 10894 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 805(1) | 10895-10896 | fork | fork F11. `s 805(1) the report was made available for inspection within a reasonable period (not more than 15 days) after the conclusion of the investigation`; `s 805(1) the last day for making the report available for inspection`; `s 805(1) the company must make the report available for inspection after the conclusion of the investigation` |
| s 805(2) | 10897 | fork | fork F13. `s 805(2) the number of interim reports the company must cause to be prepared` |
| s 805(2)(a) | 10898 | fork | fork F13. `s 805(2) the number of interim reports the company must cause to be prepared` |
| s 805(2)(b) | 10899-10900 | fork | fork F13. `s 805(2) the number of interim reports the company must cause to be prepared` |
| s 805(3) | 10901 | fork | fork F11. `s 805(3) each such report was made available for inspection within a reasonable period (not more than 15 days) after the end of the period to which it relates`; `s 805(3) the last day for making the report available for inspection` |
| s 805(4) | 10902 | fork | fork F12. `s 805(4) the reports must still be retained and kept available for inspection`; `s 805(4) the place at which the reports are kept is a place at which they must be kept available for inspection` |
| s 805(4)(a) | 10903 | fork | fork F12. `s 805(4) the reports must still be retained and kept available for inspection`; `s 805(4) the place at which the reports are kept is a place at which they must be kept available for inspection` |
| s 805(4)(b) | 10904 | fork | fork F12. `s 805(4) the reports must still be retained and kept available for inspection`; `s 805(4) the place at which the reports are kept is a place at which they must be kept available for inspection` |
| s 805(5) | 10905 | encoded | `s 805(5) the company must give notice to the registrar of the place and of any change in that place`; `s 805(5) the company must give notice to the registrar of the place at which the reports are kept` |
| s 805(5)(a) | 10906 | encoded | `s 805(5) the company must give notice to the registrar of the place and of any change in that place`; `s 805(5) the company must give notice to the registrar of the place at which the reports are kept` |
| s 805(5)(b) | 10907-10908 | encoded | `s 805(5) the company must give notice to the registrar of the place and of any change in that place`; `s 805(5) the company must give notice to the registrar of the place at which the reports are kept` |
| s 805(6) | 10909 | fork | fork F11. `s 805(6) the company notified the members who made the requests where the report is available within three days`; `s 805(6) the last day for notifying the members who made the requests`; `s 805(6) the company must notify the members who made the requests where the report is available` |
| s 805(7) | 10910 | encoded | `s 805(7) inquiry`; `s 805(7) the investigation carried out by the company in pursuance of a requirement under section 803 is concluded` |
| s 805(7)(a) | 10911 | encoded | `s 805(7) inquiry`; `s 805(7) the investigation carried out by the company in pursuance of a requirement under section 803 is concluded` |
| s 805(7)(b) | 10912 | encoded | `s 805(7) inquiry`; `s 805(7) the investigation carried out by the company in pursuance of a requirement under section 803 is concluded` |
| s 805(7)(b)(i) | 10913 | encoded | `s 805(7) inquiry`; `s 805(7) the investigation carried out by the company in pursuance of a requirement under section 803 is concluded` |
| s 805(7)(b)(ii) | 10914 | encoded | `s 805(7) inquiry`; `s 805(7) the investigation carried out by the company in pursuance of a requirement under section 803 is concluded` |
| s 806 | 10915 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 806(1) | 10916 | fork | fork F10. `s 806(1)(a) the company commits an offence`; `s 806(1)(b) the officer of the company commits an offence` |
| s 806(1)(a) | 10917 | fork | fork F10. `s 806(1)(a) the company commits an offence` |
| s 806(1)(b) | 10918 | fork | fork F10. `s 806(1)(b) the officer of the company commits an offence` |
| s 806(2) | 10919 | encoded | `s 806(2) the penalty on summary conviction` |
| s 806(3) | 10920 | encoded | `s 806(3) the officer of the company commits an offence` |
| s 806(4) | 10921 | encoded | `s 806(4) the penalty on conviction` |
| s 806(4)(a) | 10922 | encoded | `s 806(4) the penalty on conviction` |
| s 806(4)(b) | 10923 | encoded | `s 806(4) the penalty on conviction` |
| s 807 | 10924 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 807(1) | 10925 | encoded | `s 807(1) the report must be open to inspection by any person without charge` |
| s 807(2) | 10926-10927 | fork | fork F11, F40. `s 807(2) the person is entitled to be provided with a copy of the report or any part of it`; `s 807(2) the copy was provided within ten days after the request was received`; `s 807(2) the last day for providing the copy`; `s 807(2) the company must provide the copy after the request is received` |
| s 807(3) | 10928 | encoded | `s 807(3)(a) the company commits an offence`; `s 807(3)(b) the officer of the company commits an offence` |
| s 807(3)(a) | 10929 | encoded | `s 807(3)(a) the company commits an offence` |
| s 807(3)(b) | 10930 | encoded | `s 807(3)(b) the officer of the company commits an offence` |
| s 807(4) | 10931 | encoded | `s 807(4) the penalty on summary conviction` |
| s 807(5) | 10932 | encoded | `s 807(5) the court may by order compel an immediate inspection or direct that the copy required be sent to the person requiring it` |
| heading 10933 | 10933 | inert | reason 1 (heading) |
| s 808 | 10934 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 808(1) | 10935 | encoded | `s 808(1) the company must keep a register of the information received` |
| s 808(2) | 10936 | fork | fork F11. `s 808(2) the company entered the information in the register within three days of the receipt`; `s 808(2) the last day for entering the information in the register`; `s 808(2) the company that receives the information must enter it in the register within three days of the receipt`; `s 808(2)(a) the entry contains the particulars the company must enter` |
| s 808(2)(a) | 10937 | fork | fork F11. `s 808(2) the company entered the information in the register within three days of the receipt`; `s 808(2) the last day for entering the information in the register`; `s 808(2) the company that receives the information must enter it in the register within three days of the receipt`; `s 808(2)(a) the entry contains the particulars the company must enter` |
| s 808(2)(b) | 10938 | fork | fork F11. `s 808(2) the company entered the information in the register within three days of the receipt`; `s 808(2) the last day for entering the information in the register`; `s 808(2) the company that receives the information must enter it in the register within three days of the receipt` |
| s 808(3) | 10939 | fork | fork F9. `s 808(3) the information is entered against the name the subsection requires` |
| s 808(4) | 10940 | fork | fork F9. `s 808(4) the register is made up as the subsection requires` |
| s 808(5) | 10941 | encoded | `s 808(5)(a) the company commits an offence`; `s 808(5)(b) the officer of the company commits an offence` |
| s 808(5)(a) | 10942 | encoded | `s 808(5)(a) the company commits an offence` |
| s 808(5)(b) | 10943 | encoded | `s 808(5)(b) the officer of the company commits an offence` |
| s 808(6) | 10944 | encoded | `s 808(6) the penalty on summary conviction` |
| s 808(7) | 10945 | encoded | `s 808(7) the company is affected with notice of, or put upon inquiry as to, the rights of any person in relation to any shares` |
| s 809 | 10946 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 809(1) | 10947 | encoded | `s 809(1) the place at which the register is kept available for inspection is a place the subsection allows` |
| s 809(1)(a) | 10948 | encoded | `s 809(1) the place at which the register is kept available for inspection is a place the subsection allows` |
| s 809(1)(b) | 10949 | encoded | `s 809(1) the place at which the register is kept available for inspection is a place the subsection allows` |
| s 809(2) | 10950 | encoded | `s 809(2) the company must give notice to the registrar of companies of the place where the register is kept and of any change in that place`; `s 809(2) the company must give notice to the registrar of the place where the register is kept` |
| s 809(3) | 10951 | encoded | `s 809(3) no such notice is required` |
| s 809(4) | 10952 | fork | fork F10. `s 809(4)(a) the company commits an offence`; `s 809(4)(b) the officer of the company commits an offence` |
| s 809(4)(a) | 10953 | fork | fork F10. `s 809(4)(a) the company commits an offence` |
| s 809(4)(b) | 10954 | fork | fork F10. `s 809(4)(b) the officer of the company commits an offence` |
| s 809(5) | 10955 | encoded | `s 809(5) the penalty on summary conviction` |
| s 810 | 10956 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 810(1) | 10957 | encoded | `s 810(1) the company must keep an index of the names entered in the register` |
| s 810(2) | 10958 | fork | fork F11. `s 810(2) the company made the entry or alteration in the index within ten days`; `s 810(2) the last day for making the entry or alteration in the index`; `s 810(2) the company must make any necessary entry or alteration in the index within ten days` |
| s 810(3) | 10959 | fork | fork F9. `s 810(3) the index is made up as the subsection requires` |
| s 810(4) | 10960 | fork | fork F9. `s 810(4) the index is kept as the subsection requires` |
| s 810(5) | 10961 | encoded | `s 810(5)(a) the company commits an offence`; `s 810(5)(b) the officer of the company commits an offence` |
| s 810(5)(a) | 10962 | encoded | `s 810(5)(a) the company commits an offence` |
| s 810(5)(b) | 10963 | encoded | `s 810(5)(b) the officer of the company commits an offence` |
| s 810(6) | 10964 | encoded | `s 810(6) the penalty on summary conviction` |
| s 811 | 10965 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 811(1) | 10966 | encoded | `s 811(1) the document must be open to inspection by any person without charge` |
| s 811(2) | 10967 | fork | fork F40. `s 811(2) the person is entitled to be provided with a copy of any entry in the register` |
| s 811(3) | 10968 | encoded | `s 811(3) the person has made the request the subsection requires` |
| s 811(4) | 10969 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 811(4)(a) | 10970 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 811(4)(b) | 10971 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 811(4)(c) | 10972 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 811(4)(d) | 10973 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 811(4)(d)(i) | 10974 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 811(4)(d)(ii) | 10975 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 811(4)(d)(iii) | 10976 | fork | fork F9. `s 811(4) kind of person`; `s 811(4) the request contains the information the subsection requires` |
| s 812 | 10977 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 812(1) | 10978 | encoded | `s 812(1) what the company must do with the request`; `s 812(1) what the company must do with a request under section 811` |
| s 812(1)(a) | 10979 | encoded | `s 812(1) what the company must do with the request`; `s 812(1) what the company must do with a request under section 811` |
| s 812(1)(b) | 10980 | encoded | `s 812(1) what the company must do with the request`; `s 812(1) what the company must do with a request under section 811` |
| s 812(2) | 10981 | encoded | `s 812(2) the company must inform the person making the request, stating the reason why it is not satisfied` |
| s 812(3) | 10982 | encoded | `s 812(3) the person may apply to the court` |
| s 812(4) | 10983 | encoded | `s 812(4)(a) the person who made the request must notify the company`; `s 812(4)(b) the company must use its best endeavours to notify any persons whose details would be disclosed` |
| s 812(4)(a) | 10984 | encoded | `s 812(4)(a) the person who made the request must notify the company` |
| s 812(4)(b) | 10985 | encoded | `s 812(4)(b) the company must use its best endeavours to notify any persons whose details would be disclosed` |
| s 812(5) | 10986 | encoded | `s 812(5) the court shall direct the company not to comply with the request` |
| s 812(6) | 10987-10988 | fork | fork F45. `s 812(6) the court may direct that the company is not to comply with any such request`; `s 812(6) the order is made as the subsection requires` |
| s 812(7) | 10989 | encoded | `s 812(7) the company must comply with the request immediately upon the court giving its decision or the proceedings being discontinued` |
| s 813 | 10990 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 813(1) | 10991 | encoded | `s 813(1)(a) the company commits an offence`; `s 813(1)(b) the officer of the company commits an offence` |
| s 813(1)(a) | 10992 | encoded | `s 813(1)(a) the company commits an offence` |
| s 813(1)(b) | 10993 | encoded | `s 813(1)(b) the officer of the company commits an offence` |
| s 813(2) | 10994 | encoded | `s 813(2) the penalty on summary conviction` |
| s 813(3) | 10995 | encoded | `s 813(3) the court may by order compel an immediate inspection or direct that the copy required be sent to the person requesting it` |
| s 814 | 10996 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 814(1) | 10997 | fork | fork F4. `s 814(1) the person commits an offence by a misleading, false or deceptive statement in a request` |
| s 814(2) | 10998 | fork | fork F4. `s 814(2) the person commits an offence by disclosing the information` |
| s 814(2)(a) | 10999 | fork | fork F4. `s 814(2) the person commits an offence by disclosing the information` |
| s 814(2)(b) | 11000-11001 | fork | fork F4. `s 814(2) the person commits an offence by disclosing the information` |
| s 814(3) | 11002 | encoded | `s 814(3) the penalty on conviction` |
| s 814(3)(a) | 11003 | encoded | `s 814(3) the penalty on conviction` |
| s 814(3)(b) | 11004 | encoded | `s 814(3) the penalty on conviction` |
| s 814(3)(b)(i) | 11005 | encoded | `s 814(3) the penalty on conviction` |
| s 814(3)(b)(ii) | 11006 | encoded | `s 814(3) the penalty on conviction` |
| s 815 | 11007 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 815(1) | 11008-11010 | encoded | `s 815(1) the deletion of the entry is permitted` |
| s 815(2) | 11011 | encoded | `s 815(2) the company must restore the entry as soon as reasonably practicable`; `s 815(2) the company must restore an entry deleted in contravention of subsection (1)` |
| s 815(3) | 11012 | encoded | `s 815(3)(a) the company commits an offence`; `s 815(3)(b) the officer of the company commits an offence` |
| s 815(3)(a) | 11013 | encoded | `s 815(3)(a) the company commits an offence` |
| s 815(3)(b) | 11014 | encoded | `s 815(3)(b) the officer of the company commits an offence` |
| s 815(4) | 11015 | encoded | `s 815(4) the penalty on summary conviction` |
| s 816 | 11016-11017 | fork | fork F14, F46. section row: its text is in the subsection rows. `s 816 the company may remove the entry from the register` |
| s 817 | 11018 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 817(1) | 11019 | encoded | `s 817(1) this section applies` |
| s 817(2) | 11020 | encoded | `s 817(2) that other person may apply to the company for the removal of the entry from the register` |
| s 817(3) | 11021 | encoded | `s 817(3) the company shall remove the entry` |
| s 817(4) | 11022-11023 | fork | fork F47. `s 817(4) the applicant may apply to the court for an order directing the company to remove the entry` |
| s 818 | 11024 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 818(1) | 11025 | encoded | `s 818(1) the person may apply to the company for the inclusion of that information in the register` |
| s 818(2) | 11026 | encoded | `s 818(2) the company shall record that information in every place where his name appears in the register as a party to the agreement` |
| s 818(3) | 11027-11028 | fork | fork F48. `s 818(3) the applicant may apply to the court for an order directing the company to include the information in the register` |
| s 819 | 11029 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 819(1) | 11030 | fork | fork F14. `s 819(1) the company must continue to keep the register and any associated index` |
| s 819(2) | 11031 | encoded | `s 819(2)(a) the company commits an offence`; `s 819(2)(b) the officer of the company commits an offence` |
| s 819(2)(a) | 11032 | encoded | `s 819(2)(a) the company commits an offence` |
| s 819(2)(b) | 11033 | encoded | `s 819(2)(b) the officer of the company commits an offence` |
| s 819(3) | 11034 | encoded | `s 819(3) the penalty on summary conviction` |
| heading 11035 | 11035 | inert | reason 1 (heading) |
| s 820 | 11036 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 820(1) | 11037 | encoded | `s 820(1) this section applies to determine whether the person has an interest in the shares` |
| s 820(2) | 11038 | encoded | `s 820(2)(a) the person has an interest in the shares`; `s 820(2)(b) the restraint or restriction is disregarded` |
| s 820(2)(a) | 11039 | encoded | `s 820(2)(a) the person has an interest in the shares` |
| s 820(2)(b) | 11040 | encoded | `s 820(2)(b) the restraint or restriction is disregarded` |
| s 820(3) | 11041 | fork | fork F15. `s 820(3) the person is treated as having an interest in the shares` |
| s 820(4) | 11042 | fork | fork F15. `s 820(4) the person is treated as having an interest in the shares` |
| s 820(4)(a) | 11043 | fork | fork F15. `s 820(4) the person is treated as having an interest in the shares` |
| s 820(4)(b) | 11044 | fork | fork F15. `s 820(4) the person is treated as having an interest in the shares` |
| s 820(4)(b)(i) | 11045 | fork | fork F15. `s 820(4) the person is treated as having an interest in the shares` |
| s 820(4)(b)(ii) | 11046 | fork | fork F15. `s 820(4) the person is treated as having an interest in the shares` |
| s 820(5) | 11047 | fork | fork F15. `s 820(5) the person is entitled to exercise or control the exercise of a right conferred by the holding of shares` |
| s 820(5)(a) | 11048 | fork | fork F15. `s 820(5) the person is entitled to exercise or control the exercise of a right conferred by the holding of shares` |
| s 820(5)(b) | 11049 | fork | fork F15. `s 820(5) the person is entitled to exercise or control the exercise of a right conferred by the holding of shares` |
| s 820(6) | 11050 | fork | fork F15. `s 820(6) the person is treated as having an interest in shares`; `s 820(6) it is immaterial whether the right or obligation is conditional or absolute` |
| s 820(6)(a) | 11051 | fork | fork F15. `s 820(6) the person is treated as having an interest in shares`; `s 820(6) it is immaterial whether the right or obligation is conditional or absolute` |
| s 820(6)(b) | 11052-11053 | fork | fork F15. `s 820(6) the person is treated as having an interest in shares`; `s 820(6) it is immaterial whether the right or obligation is conditional or absolute` |
| s 820(7) | 11054 | encoded | `s 820(7) the persons are treated as each having that interest` |
| s 820(8) | 11055 | encoded | `s 820(8) it is immaterial that the shares are unidentifiable` |
| s 821 | 11056 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 821(1) | 11057 | encoded | `s 821(1) section 793 applies in relation to the person as it applies to a person who is or was interested in shares` |
| s 821(2) | 11058 | encoded | `s 821(2) references in section 793 to an interest in shares are read as including the right to subscribe` |
| s 822 | 11059 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 822(1) | 11060 | encoded | `s 822(1) the person is taken to be interested in the shares` |
| s 822(1)(a) | 11061 | encoded | `s 822(1) the person is taken to be interested in the shares` |
| s 822(1)(b) | 11062-11063 | encoded | `s 822(1) the person is taken to be interested in the shares` |
| s 822(2) | 11064 | fork | fork F16. `s 822(2) the person is an infant` |
| s 823 | 11065 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 823(1) | 11066 | fork | fork F15. `s 823(1) the person is taken to be interested in the shares` |
| s 823(1)(a) | 11067 | fork | fork F15. `s 823(1) the person is taken to be interested in the shares` |
| s 823(1)(b) | 11068 | fork | fork F15. `s 823(1) the person is taken to be interested in the shares` |
| s 823(2) | 11069 | fork | fork F15. `s 823(2) the person is treated as entitled to exercise or control the exercise of the voting power` |
| s 823(2)(a) | 11070 | fork | fork F15. `s 823(2) the person is treated as entitled to exercise or control the exercise of the voting power` |
| s 823(2)(b) | 11071 | fork | fork F15. `s 823(2) the person is treated as entitled to exercise or control the exercise of the voting power` |
| s 823(3) | 11072 | fork | fork F15. `s 823(3) the person is treated as entitled to exercise or control the exercise of the voting power` |
| s 823(3)(a) | 11073 | fork | fork F15. `s 823(3) the person is treated as entitled to exercise or control the exercise of the voting power` |
| s 823(3)(b) | 11074 | fork | fork F15. `s 823(3) the person is treated as entitled to exercise or control the exercise of the voting power` |
| s 824 | 11075 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 824(1) | 11076 | encoded | `s 824(1) an interest in shares may arise from the agreement` |
| s 824(2) | 11077 | encoded | `s 824(2) this section applies to the agreement` |
| s 824(2)(a) | 11078 | encoded | `s 824(2) this section applies to the agreement` |
| s 824(2)(b) | 11079 | encoded | `s 824(2) this section applies to the agreement` |
| s 824(3) | 11080 | encoded | `s 824(3) act`; `s 824(3) the use of interests in shares includes the act` |
| s 824(4) | 11081-11082 | encoded | `s 824(4) this section continues to apply to the agreement`; `s 824(4) circumstance`; `s 824(4) it is immaterial to the continued application of this section whether the circumstance occurs`; `s 824(4) a reference in subsection (4) to the agreement includes the other agreement` |
| s 824(4)(a) | 11083 | encoded | `s 824(4) this section continues to apply to the agreement`; `s 824(4) circumstance`; `s 824(4) it is immaterial to the continued application of this section whether the circumstance occurs`; `s 824(4) a reference in subsection (4) to the agreement includes the other agreement` |
| s 824(4)(b) | 11084 | encoded | `s 824(4) this section continues to apply to the agreement`; `s 824(4) circumstance`; `s 824(4) it is immaterial to the continued application of this section whether the circumstance occurs`; `s 824(4) a reference in subsection (4) to the agreement includes the other agreement` |
| s 824(4)(c) | 11085-11086 | encoded | `s 824(4) this section continues to apply to the agreement`; `s 824(4) circumstance`; `s 824(4) it is immaterial to the continued application of this section whether the circumstance occurs`; `s 824(4) a reference in subsection (4) to the agreement includes the other agreement` |
| s 824(5) | 11087 | encoded | `s 824(5)(a) the arrangement is an agreement`; `s 824(5)(b) the provision is a provision of the agreement`; `s 824(5) the reference has a corresponding meaning` |
| s 824(5)(a) | 11088 | encoded | `s 824(5)(a) the arrangement is an agreement`; `s 824(5) the reference has a corresponding meaning` |
| s 824(5)(b) | 11089 | encoded | `s 824(5)(b) the provision is a provision of the agreement`; `s 824(5) the reference has a corresponding meaning` |
| s 824(5)(b)(i) | 11090 | encoded | `s 824(5)(b) the provision is a provision of the agreement`; `s 824(5) the reference has a corresponding meaning` |
| s 824(5)(b)(ii) | 11091-11092 | encoded | `s 824(5)(b) the provision is a provision of the agreement`; `s 824(5) the reference has a corresponding meaning` |
| s 824(6) | 11093 | fork | fork F17. `s 824(6)(a) this section does not apply to the agreement`; `s 824(6)(b) this section does not apply to the agreement` |
| s 824(6)(a) | 11094 | fork | fork F17. `s 824(6)(a) this section does not apply to the agreement` |
| s 824(6)(b) | 11095 | fork | fork F17. `s 824(6)(b) this section does not apply to the agreement` |
| s 825 | 11096 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 825(1) | 11097 | encoded | `s 825(1) the person is treated as interested in the shares` |
| s 825(2) | 11098 | fork | fork F15. `s 825(2) the interest of the party in shares in the target company is an interest apart from the agreement` |
| s 825(3) | 11099 | encoded | `s 825(3) the interest is included in the interest of the person apart from the agreement` |
| s 825(4) | 11100 | fork | fork F9. `s 825(4) the notification contains what the subsection requires` |
| s 825(4)(a) | 11101 | fork | fork F9. `s 825(4) the notification contains what the subsection requires` |
| s 825(4)(b) | 11102 | fork | fork F9. `s 825(4) the notification contains what the subsection requires` |
| s 825(4)(c) | 11103 | fork | fork F9. `s 825(4) the notification contains what the subsection requires` |
| heading 11104 | 11104 | inert | reason 1 (heading) |
| s 826 | 11105 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 826(1) | 11106 | fork | fork F39. `s 826(1)(a) the information must not be included in a report under section 805`; `s 826(1)(b) the information must not be made available under section 811` |
| s 826(1)(a) | 11107 | fork | fork F39. `s 826(1)(a) the information must not be included in a report under section 805` |
| s 826(1)(b) | 11108 | fork | fork F39. `s 826(1)(b) the information must not be made available under section 811` |
| s 826(2) | 11109 | encoded | `s 826(2) the fact that the information is omitted must be stated in the report` |
| s 827 | 11110-11111 | fork | fork F11. section row: its text is in the subsection rows. `s 827 a day that is not a working day is disregarded in reckoning the period`; `s 827 the last day of a period of days counting only working days`; `s 827 the number of working days after one date up to and including another` |
| s 828 | 11112 | inert | reason 2 (machinery: a regulation-making power) |
| s 828(1) | 11113 | inert | reason 2 (machinery: a regulation-making power) |
| s 828(1)(a) | 11114 | inert | reason 2 (machinery: a regulation-making power) |
| s 828(1)(b) | 11115 | inert | reason 2 (machinery: a regulation-making power) |
| s 828(1)(c) | 11116 | inert | reason 2 (machinery: a regulation-making power) |
| s 828(2) | 11117 | inert | reason 2 (machinery: a regulation-making power) |
| s 828(3) | 11118 | inert | reason 2 (machinery: affirmative resolution procedure for the regulations) |
| heading 11119 | 11119 | inert | reason 1 (heading) |
| heading 11120 | 11120 | inert | reason 1 (heading) |
| heading 11121 | 11121 | inert | reason 1 (heading) |
| s 829 | 11122 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 829(1) | 11123 | encoded | `s 829(1) the act is a distribution` |
| s 829(2) | 11124 | encoded | `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part` |
| s 829(2)(a) | 11125 | encoded | `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part` |
| s 829(2)(b) | 11126 | encoded | `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part` |
| s 829(2)(b)(i) | 11127 | encoded | `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part` |
| s 829(2)(b)(ii) | 11128 | encoded | `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part` |
| s 829(2)(c) | 11129 | fork | fork F18. `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part` |
| s 829(2)(d) | 11130 | encoded | `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part` |
| heading 11131 | 11131 | inert | reason 1 (heading) |
| s 830 | 11132 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 830(1) | 11133 | fork | fork F19. `s 830(1) the distribution is within the profits available for the purpose` |
| s 830(2) | 11134 | encoded | `s 830(2) the profits available for distribution` |
| s 830(3) | 11135 | encoded | `s 830(3) subsection (2) has effect subject to sections 832, 833A and 835` |
| s 831 | 11136 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 831(1) | 11137 | fork | fork F20. `s 831(1) the distribution is within the net asset restriction` |
| s 831(1)(a) | 11138 | fork | fork F20. `s 831(1) the distribution is within the net asset restriction` |
| s 831(1)(b) | 11139 | fork | fork F20. `s 831(1) the distribution is within the net asset restriction` |
| s 831(2) | 11140 | encoded | `s 831(2) the company's net assets` |
| s 831(3) | 11141 | encoded | `s 831(3) kind of relevant accounts`; `s 831(3) the provision is included in liabilities` |
| s 831(3)(a) | 11142 | encoded | `s 831(3) kind of relevant accounts`; `s 831(3) the provision is included in liabilities` |
| s 831(3)(b) | 11143 | encoded | `s 831(3) kind of relevant accounts`; `s 831(3) the provision is included in liabilities` |
| s 831(4) | 11144 | encoded | `s 831(4) the company's undistributable reserves` |
| s 831(4)(a) | 11145 | encoded | `s 831(4) the company's undistributable reserves` |
| s 831(4)(b) | 11146 | encoded | `s 831(4) the company's undistributable reserves` |
| s 831(4)(c) | 11147 | fork | fork F21. `s 831(4) the company's undistributable reserves` |
| s 831(4)(d) | 11148 | encoded | `s 831(4) the company's undistributable reserves` |
| s 831(4)(d)(i) | 11149 | encoded | `s 831(4) the company's undistributable reserves` |
| s 831(4)(d)(ii) | 11150-11151 | encoded | `s 831(4) the company's undistributable reserves` |
| s 831(5) | 11152 | fork | fork F20. `s 831(5) the company may include uncalled share capital as an asset in any accounts relevant for the purposes of this section` |
| s 831(6) | 11153 | encoded | `s 831(6) subsection (1) has effect subject to sections 832 and 835` |
| heading 11154 | 11154 | inert | reason 1 (heading) |
| s 832 | 11155 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 832(1) | 11156 | fork | fork F22. `s 832(1) the investment company may make the distribution out of its accumulated, realised revenue profits` |
| s 832(2) | 11157 | encoded | `s 832(2) the distribution is within the accumulated, realised revenue profits` |
| s 832(3) | 11158 | encoded | `s 832(3) the distribution is within the asset cover the subsection requires` |
| s 832(3)(a) | 11159 | encoded | `s 832(3) the distribution is within the asset cover the subsection requires` |
| s 832(3)(b) | 11160 | encoded | `s 832(3) the distribution is within the asset cover the subsection requires` |
| s 832(4) | 11161 | encoded | `s 832(4) the provision is included in the company's liabilities to creditors` |
| s 832(4)(a) | 11162 | encoded | `s 832(4) the provision is included in the company's liabilities to creditors` |
| s 832(4)(b) | 11163 | encoded | `s 832(4) the provision is included in the company's liabilities to creditors` |
| s 832(5) | 11164 | encoded | `s 832(5) the further conditions are met` |
| s 832(5)(a) | 11165 | encoded | `s 832(5) the further conditions are met` |
| s 832(5)(b) | 11166 | encoded | `s 832(5) the further conditions are met` |
| s 832(5)(b)(i) | 11167 | repealed or blank in this text | the text shows only dots |
| s 832(5)(b)(ii) | 11168 | encoded | `s 832(5) the further conditions are met` |
| s 832(5)(c) | 11169 | encoded | `s 832(5) the further conditions are met` |
| s 832(5)(c)(i) | 11170 | encoded | `s 832(5) the further conditions are met` |
| s 832(5)(c)(ii) | 11171 | encoded | `s 832(5) the further conditions are met` |
| s 832(6) | 11172 | encoded | `s 832(6)(b) the first day of the relevant period` |
| s 832(6)(a) | 11173 | repealed or blank in this text | the text shows only dots |
| s 832(6)(b) | 11174 | encoded | `s 832(6)(b) the first day of the relevant period` |
| s 832(6)(b)(i) | 11175 | encoded | `s 832(6)(b) the first day of the relevant period` |
| s 832(6)(b)(ii) | 11176-11177 | encoded | `s 832(6)(b) the first day of the relevant period` |
| s 832(7) | 11178 | encoded | `s 832(7) the company may include uncalled share capital as an asset in any accounts relevant for the purposes of this section` |
| s 833 | 11179 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 833(1) | 11180 | encoded | `s 833(1) the company is an investment company` |
| s 833(1)(a) | 11181 | encoded | `s 833(1) the company is an investment company` |
| s 833(1)(b) | 11182 | encoded | `s 833(1) the company is an investment company` |
| s 833(2) | 11183 | encoded | `s 833(2)(a) the requirement is met` |
| s 833(2)(a) | 11184 | encoded | `s 833(2)(a) the requirement is met` |
| s 833(2)(b) | 11185 | repealed or blank in this text | the text shows only dots |
| s 833(2)(c) | 11186 | repealed or blank in this text | the text shows only dots |
| s 833(2)(d) | 11187 | repealed or blank in this text | the text shows only dots |
| s 833(3) | 11188 | repealed or blank in this text | the text shows only dots |
| s 833(4) | 11189 | encoded | `s 833(4) the notice to the registrar of intention to carry on business as an investment company is revoked` |
| s 833(5) | 11190 | encoded | `s 833(5) the company ceases to be an investment company` |
| s 833A | 11191 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 833A(1) | 11192 | encoded | `s 833A(1) this section applies in relation to the company` |
| s 833A(2) | 11193 | encoded | `s 833A(2) the amount is taken to be a realised profit`; `s 833A(2) the realised profit (positive) or realised loss (negative) of the company for the period of its relevant accounts` |
| s 833A(3) | 11194 | encoded | `s 833A(3) the company's profits available for distribution as limited by the subsection` |
| s 833A(4) | 11195-11200 | encoded | `s 833A(4) the amount given by the formula A - L - D` |
| s 833A(5) | 11201 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(a) | 11202 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(b) | 11203 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(c) | 11204 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(d) | 11205 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(e) | 11206 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(e)(i) | 11207 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(e)(ii) | 11208-11209 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(f) | 11210 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(f)(i) | 11211 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(f)(ii) | 11212 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(f)(iii) | 11213 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(5)(f)(iv) | 11214 | fork | fork F21. `s 833A(5) the total value of the items within the subsection` |
| s 833A(6) | 11215 | fork | fork F23. "taken into account only once": the overlap is an input of s 833A(5). `s 833A(5) the total value of the items within the subsection` |
| s 833A(7) | 11216 | encoded | `s 833A(7) the company's assets and liabilities are valued as the subsection requires` |
| s 833A(7)(a) | 11217 | encoded | `s 833A(7) the company's assets and liabilities are valued as the subsection requires` |
| s 833A(7)(b) | 11218 | encoded | `s 833A(7) the company's assets and liabilities are valued as the subsection requires` |
| s 833A(7)(c) | 11219 | encoded | `s 833A(7) the company's assets and liabilities are valued as the subsection requires` |
| s 833A(7)(d) | 11220 | encoded | `s 833A(7) the company's assets and liabilities are valued as the subsection requires` |
| s 833A(8) | 11221 | encoded | `s 833A(8)(a) this section is applied on the assumption that the company carries on only the long-term business`; `s 833A(8)(b) the remainder of this Part is applied on the assumption that the company carries on only that other insurance business`; `s 833A(8) the amount apportioned to the business concerned` |
| s 833A(8)(a) | 11222 | encoded | `s 833A(8)(a) this section is applied on the assumption that the company carries on only the long-term business`; `s 833A(8) the amount apportioned to the business concerned` |
| s 833A(8)(b) | 11223-11224 | encoded | `s 833A(8)(b) the remainder of this Part is applied on the assumption that the company carries on only that other insurance business`; `s 833A(8) the amount apportioned to the business concerned` |
| s 833A(9) | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 834 | 11231-11232 | repealed or blank in this text | the text shows only dots under the heading |
| s 835 | 11233-11234 | repealed or blank in this text | the text shows only dots under the heading |
| heading 11235 | 11235 | inert | reason 1 (heading) |
| heading 11236 | 11236 | inert | reason 1 (heading) |
| s 836 | 11237 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 836(1) | 11238 | fork | fork F27. `s 836(1) item stated in the relevant accounts`; `s 836(1) whether a distribution may be made is determined by reference to the item as stated in the relevant accounts` |
| s 836(1)(a) | 11239 | fork | fork F27. `s 836(1) item stated in the relevant accounts`; `s 836(1) whether a distribution may be made is determined by reference to the item as stated in the relevant accounts` |
| s 836(1)(b) | 11240 | fork | fork F27. `s 836(1) item stated in the relevant accounts`; `s 836(1) whether a distribution may be made is determined by reference to the item as stated in the relevant accounts` |
| s 836(1)(b)(i) | 11241 | fork | fork F27. `s 836(1) item stated in the relevant accounts`; `s 836(1) whether a distribution may be made is determined by reference to the item as stated in the relevant accounts` |
| s 836(1)(b)(ii) | 11242 | fork | fork F27. `s 836(1) item stated in the relevant accounts`; `s 836(1) whether a distribution may be made is determined by reference to the item as stated in the relevant accounts` |
| s 836(1)(c) | 11243 | fork | fork F27. `s 836(1) item stated in the relevant accounts`; `s 836(1) whether a distribution may be made is determined by reference to the item as stated in the relevant accounts` |
| s 836(2) | 11244 | fork | fork F24. `s 836(2) accounts`; `s 836(2) the relevant accounts are the company's last annual accounts`; `s 836(2)(a) the distribution may be justified by reference to interim accounts`; `s 836(2)(b) the distribution may be justified by reference to initial accounts` |
| s 836(2)(a) | 11245 | fork | fork F24. `s 836(2) accounts`; `s 836(2) the relevant accounts are the company's last annual accounts`; `s 836(2)(a) the distribution may be justified by reference to interim accounts` |
| s 836(2)(b) | 11246 | fork | fork F24. `s 836(2) accounts`; `s 836(2) the relevant accounts are the company's last annual accounts`; `s 836(2)(b) the distribution may be justified by reference to initial accounts` |
| s 836(3) | 11247-11251 | encoded | `s 836(3) section whose requirements must be complied with`; `s 836(3) the section whose requirements must be complied with as regards the accounts` |
| s 836(4) | 11252 | encoded | `s 836(4) the accounts may not be relied on for the purposes of this Part and the distribution is treated as contravening this Part` |
| heading 11253 | 11253 | inert | reason 1 (heading) |
| s 837 | 11254 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 837(1) | 11255 | encoded | `s 837(1) the accounts are the company's last annual accounts` |
| s 837(1)(a) | 11256 | encoded | `s 837(1) the accounts are the company's last annual accounts` |
| s 837(1)(b) | 11257 | repealed or blank in this text | the text shows only dots |
| s 837(2) | 11258 | fork | fork F9. `s 837(2) the accounts were prepared as the subsection requires` |
| s 837(3) | 11259 | fork | fork F9. `s 837(3) the audit requirement is met` |
| s 837(4) | 11260 | fork | fork F25. `s 837(4) the requirements as to a qualified report are met` |
| s 837(4)(a) | 11261 | fork | fork F25. `s 837(4) the requirements as to a qualified report are met` |
| s 837(4)(b) | 11262 | fork | fork F25. `s 837(4) the requirements as to a qualified report are met` |
| s 837(4)(b)(i) | 11263 | fork | fork F25. `s 837(4) the requirements as to a qualified report are met` |
| s 837(4)(b)(ii) | 11264 | fork | fork F25. `s 837(4) the requirements as to a qualified report are met` |
| s 837(5) | 11265 | encoded | `s 837(5) the auditor's statement is sufficient for the purposes of a distribution` |
| s 838 | 11266 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 838(1) | 11267 | fork | fork F9. `s 838(1) the interim accounts are accounts of the kind the subsection requires` |
| s 838(2) | 11268 | fork | fork F26. `s 838(2) the requirements of subsections (3) to (6) apply` |
| s 838(3) | 11269 | encoded | `s 838(3) the interim accounts were prepared as the subsection requires` |
| s 838(4) | 11270 | encoded | `s 838(4) the interim accounts are properly prepared` |
| s 838(5) | 11271 | encoded | `s 838(5) the balance sheet was signed as the subsection requires` |
| s 838(6) | 11272-11273 | encoded | `s 838(6) the accounts were delivered to the registrar as the subsection requires` |
| s 839 | 11274 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 839(1) | 11275 | fork | fork F9. `s 839(1) the initial accounts are accounts of the kind the subsection requires` |
| s 839(2) | 11276 | fork | fork F26. `s 839(2) the requirements of subsections (3) to (7) apply` |
| s 839(3) | 11277 | encoded | `s 839(3) the initial accounts were prepared as the subsection requires` |
| s 839(4) | 11278 | encoded | `s 839(4) the initial accounts are properly prepared` |
| s 839(5) | 11279 | fork | fork F9. `s 839(5) the auditor's report was made as the subsection requires` |
| s 839(6) | 11280 | fork | fork F25. `s 839(6) the requirements as to a qualified report are met` |
| s 839(6)(a) | 11281 | fork | fork F25. `s 839(6) the requirements as to a qualified report are met` |
| s 839(6)(b) | 11282 | fork | fork F25. `s 839(6) the requirements as to a qualified report are met` |
| s 839(7) | 11283-11284 | encoded | `s 839(7) the documents were delivered to the registrar as the subsection requires` |
| heading 11285 | 11285 | inert | reason 1 (heading) |
| s 840 | 11286 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 840(1) | 11287 | encoded | `s 840(1) the amount of the proposed distribution as increased for the purposes of this Part` |
| s 840(1)(a) | 11288 | encoded | `s 840(1) the amount of the proposed distribution as increased for the purposes of this Part` |
| s 840(1)(b) | 11289-11290 | encoded | `s 840(1) the amount of the proposed distribution as increased for the purposes of this Part` |
| s 840(2) | 11291 | fork | fork F27. `s 840(2) kind of financial assistance or payment`; `s 840(2) the financial assistance or payment is relevant for the purposes of subsection (1)` |
| s 840(2)(a) | 11292 | fork | fork F27. `s 840(2) kind of financial assistance or payment`; `s 840(2) the financial assistance or payment is relevant for the purposes of subsection (1)` |
| s 840(2)(b) | 11293 | fork | fork F27. `s 840(2) kind of financial assistance or payment`; `s 840(2) the financial assistance or payment is relevant for the purposes of subsection (1)` |
| s 840(2)(c) | 11294 | fork | fork F27. `s 840(2) kind of financial assistance or payment`; `s 840(2) the financial assistance or payment is relevant for the purposes of subsection (1)` |
| s 840(2)(d) | 11295 | fork | fork F27. `s 840(2) kind of financial assistance or payment`; `s 840(2) the financial assistance or payment is relevant for the purposes of subsection (1)` |
| s 840(3) | 11296 | encoded | `s 840(3) the assistance is financial assistance for the purposes of this section` |
| s 840(4) | 11297 | fork | fork F21. `s 840(4)(a) the company's net assets`; `s 840(4)(b) the company's net liabilities` |
| s 840(4)(a) | 11298 | fork | fork F21. `s 840(4)(a) the company's net assets` |
| s 840(4)(b) | 11299-11300 | fork | fork F21. `s 840(4)(b) the company's net liabilities` |
| s 840(5) | 11301 | encoded | `s 840(5) the amount retained is included in the company's liabilities` |
| s 840(5)(a) | 11302 | encoded | `s 840(5) the amount retained is included in the company's liabilities` |
| s 840(5)(b) | 11303 | encoded | `s 840(5) the amount retained is included in the company's liabilities` |
| heading 11304 | 11304 | inert | reason 1 (heading) |
| heading 11305 | 11305 | inert | reason 1 (heading) |
| s 841 | 11306 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 841(1) | 11307 | inert | reason 1 (not operative: a lead-in, "The following provisions have effect for the purposes of this Part"; fork-register note N1) |
| s 841(2) | 11308 | fork | fork F27. `s 841(2) the provision is treated as a realised loss` |
| s 841(2)(a) | 11309 | fork | fork F27. `s 841(2) the provision is treated as a realised loss` |
| s 841(2)(b) | 11310 | fork | fork F27. `s 841(2) the provision is treated as a realised loss` |
| s 841(3) | 11311 | encoded | `s 841(3) the provision is a revaluation provision` |
| s 841(4) | 11312 | encoded | `s 841(4) the consideration by the directors of the value of a fixed asset is treated as a revaluation` |
| s 841(4)(a) | 11313 | encoded | `s 841(4) the consideration by the directors of the value of a fixed asset is treated as a revaluation` |
| s 841(4)(b) | 11314 | encoded | `s 841(4) the consideration by the directors of the value of a fixed asset is treated as a revaluation` |
| s 841(4)(b)(i) | 11315 | encoded | `s 841(4) the consideration by the directors of the value of a fixed asset is treated as a revaluation` |
| s 841(4)(b)(ii) | 11316 | encoded | `s 841(4) the consideration by the directors of the value of a fixed asset is treated as a revaluation` |
| s 841(4)(b)(iii) | 11317 | encoded | `s 841(4) the consideration by the directors of the value of a fixed asset is treated as a revaluation` |
| s 841(5) | 11318 | fork | fork F21. `s 841(5) the amount treated as a realised profit made over that period` |
| s 841(5)(a) | 11319 | fork | fork F21. `s 841(5) the amount treated as a realised profit made over that period` |
| s 841(5)(b) | 11320-11321 | fork | fork F21. `s 841(5) the amount treated as a realised profit made over that period` |
| s 842 | 11322-11323 | encoded | section row: its text is in the subsection rows. `s 842 the cost of the asset taken for the purposes of determining profit or loss` |
| s 842(a) | 11324 | encoded | `s 842 the cost of the asset taken for the purposes of determining profit or loss` |
| s 842(b) | 11325-11326 | encoded | `s 842 the cost of the asset taken for the purposes of determining profit or loss` |
| s 843 | 11327 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 843(1) | 11328 | fork | fork F28. `s 843(1) the provisions of this section have effect in relation to the company` |
| s 843(1)(a) | 11329 | fork | fork F28. `s 843(1) the provisions of this section have effect in relation to the company` |
| s 843(1)(b) | 11330 | fork | fork F28. `s 843(1) the provisions of this section have effect in relation to the company` |
| s 843(2) | 11331 | encoded | `s 843(2) the amount is treated as a realised profit` |
| s 843(2)(a) | 11332 | encoded | `s 843(2) the amount is treated as a realised profit` |
| s 843(2)(b) | 11333-11334 | encoded | `s 843(2) the amount is treated as a realised profit` |
| s 843(3) | 11335 | encoded | `s 843(3)(a) the part of the balance sheet is the relevant part`; `s 843(3)(b) the surplus in the fund or funds maintained by the company in respect of its long-term business` |
| s 843(3)(a) | 11336 | encoded | `s 843(3)(a) the part of the balance sheet is the relevant part` |
| s 843(3)(b) | 11337 | fork | fork F21. `s 843(3)(b) the surplus in the fund or funds maintained by the company in respect of its long-term business` |
| s 843(4) | 11338-11339 | fork | fork F21. `s 843(4) the deficit in the fund or funds maintained by the company in respect of its long-term business, treated as a realised loss` |
| s 843(5) | 11340 | encoded | `s 843(5) the profit or loss is left out of account` |
| s 843(6) | 11341 | encoded | `s 843(6) the investigation is an actuarial investigation` |
| s 843(6)(a) | 11342 | encoded | `s 843(6) the investigation is an actuarial investigation` |
| s 843(6)(b) | 11343-11344 | encoded | `s 843(6) the investigation is an actuarial investigation` |
| s 843(7) | 11345-11346 | encoded | `s 843(7) the business is long-term business` |
| s 843(8) | 11347 | encoded | `s 843(8) the vehicle is an insurance special purpose vehicle` |
| s 844 | 11348 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 844(1) | 11349 | fork | fork F29. `s 844(1)(a) the amount shown or included in respect of the development costs is treated, for the purposes of section 830, as a realised loss`; `s 844(1)(b) the amount shown or included in respect of the development costs is treated, for the purposes of section 832, as a realised revenue loss` |
| s 844(1)(a) | 11350 | fork | fork F29. `s 844(1)(a) the amount shown or included in respect of the development costs is treated, for the purposes of section 830, as a realised loss` |
| s 844(1)(b) | 11351-11352 | fork | fork F29. `s 844(1)(b) the amount shown or included in respect of the development costs is treated, for the purposes of section 832, as a realised revenue loss` |
| s 844(2) | 11353 | fork | fork F29. `s 844(2) subsection (1) does not apply to the part of the amount` |
| s 844(3) | 11354 | fork | fork F29. `s 844(3) subsection (1) does not apply` |
| s 844(3)(a) | 11355 | fork | fork F29. `s 844(3) subsection (1) does not apply` |
| s 844(3)(b) | 11356 | fork | fork F29. `s 844(3) subsection (1) does not apply` |
| s 844(3)(b)(i) | 11357 | fork | fork F29. `s 844(3) subsection (1) does not apply` |
| s 844(3)(b)(ii) | 11358-11359 | fork | fork F29. `s 844(3) subsection (1) does not apply` |
| s 844(3)(c) | 11360 | fork | fork F29. `s 844(3) subsection (1) does not apply` |
| heading 11361 | 11361 | inert | reason 1 (heading) |
| s 845 | 11362 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 845(1) | 11363 | encoded | `s 845(1) this section applies for determining the amount of the distribution` |
| s 845(1)(a) | 11364 | encoded | `s 845(1) this section applies for determining the amount of the distribution` |
| s 845(1)(b) | 11365 | encoded | `s 845(1) this section applies for determining the amount of the distribution` |
| s 845(2) | 11366 | encoded | `s 845(2) the amount of the distribution or the relevant part of it` |
| s 845(2)(a) | 11367 | encoded | `s 845(2) the amount of the distribution or the relevant part of it` |
| s 845(2)(b) | 11368 | encoded | `s 845(2) the amount of the distribution or the relevant part of it` |
| s 845(3) | 11369 | encoded | `s 845(3) the company's profits available for distribution for the purposes of subsection (1)(a)` |
| s 845(4) | 11370 | encoded | `s 845(4) the book value of the asset` |
| s 845(4)(a) | 11371 | encoded | `s 845(4) the book value of the asset` |
| s 845(4)(b) | 11372 | encoded | `s 845(4) the book value of the asset` |
| s 845(5) | 11373 | encoded | `s 845(5) the provisions of Chapter 2 have effect subject to this section` |
| s 846 | 11374 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 846(1) | 11375 | encoded | `s 846(1) this section applies` |
| s 846(1)(a) | 11376 | encoded | `s 846(1) this section applies` |
| s 846(1)(b) | 11377 | encoded | `s 846(1) this section applies` |
| s 846(2) | 11378 | encoded | `s 846(2)(a) that profit is treated as a realised profit for the purpose of determining the lawfulness of the distribution`; `s 846(2)(b) that profit is treated as a realised profit for the purpose of applying that provision of the regulations` |
| s 846(2)(a) | 11379 | encoded | `s 846(2)(a) that profit is treated as a realised profit for the purpose of determining the lawfulness of the distribution` |
| s 846(2)(b) | 11380 | encoded | `s 846(2)(b) that profit is treated as a realised profit for the purpose of applying that provision of the regulations` |
| heading 11381 | 11381 | inert | reason 1 (heading) |
| s 847 | 11382 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 847(1) | 11383 | encoded | the gate is an input of s 847(2). `s 847(2) liability of the member`; `s 847(2) what the member is liable to do` |
| s 847(2) | 11384 | fork | fork F30. `s 847(2) liability of the member`; `s 847(2) what the member is liable to do` |
| s 847(2)(a) | 11385 | fork | fork F30. `s 847(2) liability of the member`; `s 847(2) what the member is liable to do` |
| s 847(2)(b) | 11386 | fork | fork F30. `s 847(2) liability of the member`; `s 847(2) what the member is liable to do` |
| s 847(3) | 11387 | encoded | `s 847(3) the obligation imposed apart from this section is unaffected` |
| s 847(4) | 11388 | encoded | the exclusion is an input of s 847(2). `s 847(2) liability of the member`; `s 847(2) what the member is liable to do` |
| s 847(4)(a) | 11389 | encoded | the exclusion is an input of s 847(2). `s 847(2) liability of the member`; `s 847(2) what the member is liable to do` |
| s 847(4)(b) | 11390 | encoded | the exclusion is an input of s 847(2). `s 847(2) liability of the member`; `s 847(2) what the member is liable to do` |
| heading 11391 | 11391 | inert | reason 1 (heading) |
| s 848 | 11392 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 848(1) | 11393 | fork | fork F31. `s 848(1) that provision continues as authority for those profits to be so applied after the relevant date` |
| s 848(2) | 11394 | encoded | `s 848(2) the relevant date for a company registered in the place` |
| s 848(2)(a) | 11395 | encoded | `s 848(2) the relevant date for a company registered in the place` |
| s 848(2)(b) | 11396 | encoded | `s 848(2) the relevant date for a company registered in the place` |
| s 849 | 11397-11398 | encoded | section row: its text is in the subsection rows. `s 849 the company may apply the profit in paying up debentures or any amounts unpaid on its issued shares`; `s 849 the company must not apply an unrealised profit in paying up debentures or amounts unpaid on its issued shares` |
| s 850 | 11399 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 850(1) | 11400 | encoded | `s 850(1) the directors may treat the profit as realised` |
| s 850(2) | 11401 | encoded | `s 850(2) the directors may treat the loss as unrealised` |
| s 850(3) | 11402 | encoded | `s 850(3) the relevant date for a company registered in the place` |
| s 850(3)(a) | 11403 | encoded | `s 850(3) the relevant date for a company registered in the place` |
| s 850(3)(b) | 11404 | encoded | `s 850(3) the relevant date for a company registered in the place` |
| s 851 | 11405 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 851(1) | 11406 | fork | fork F32. `s 851(1) the provisions of this Part are without prejudice to the rule of law` |
| s 851(2) | 11407 | encoded | `s 851(2)(a) section 845 applies to determine the amount of the distribution or return of capital`; `s 851(2)(b) section 846 applies as it applies for the purposes of this Part` |
| s 851(2)(a) | 11408 | encoded | `s 851(2)(a) section 845 applies to determine the amount of the distribution or return of capital` |
| s 851(2)(b) | 11409 | encoded | `s 851(2)(b) section 846 applies as it applies for the purposes of this Part` |
| s 851(3) | 11410 | encoded | `s 851(3) the reference is to amounts regarded as distributions for the purposes of the rule of law` |
| s 852 | 11411-11412 | encoded | section row: its text is in the subsection rows. `s 852 the provisions of this Part are without prejudice to the restriction` |
| s 853 | 11413 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853(1) | 11414 | inert | reason 1 (not operative: a lead-in, "The following provisions apply for the purposes of this Part"; fork-register note N1) |
| s 853(2) | 11415 | encoded | `s 853(2)(a) the profit or loss is within the reference, whenever it was made`; `s 853(2)(b) the profit or loss is within the reference` |
| s 853(2)(a) | 11416 | encoded | `s 853(2)(a) the profit or loss is within the reference, whenever it was made` |
| s 853(2)(b) | 11417 | encoded | `s 853(2)(b) the profit or loss is within the reference` |
| s 853(3) | 11418 | encoded | `s 853(3) operation`; `s 853(3) the operation is capitalisation` |
| s 853(3)(a) | 11419 | encoded | `s 853(3) operation`; `s 853(3) the operation is capitalisation` |
| s 853(3)(b) | 11420 | encoded | `s 853(3) operation`; `s 853(3) the operation is capitalisation` |
| s 853(4) | 11421 | encoded | `s 853(4) the profit or loss is a realised profit or loss in relation to the company's accounts` |
| s 853(5) | 11422 | encoded | `s 853(5) subsection (4) is without prejudice to the matter` |
| s 853(5)(a) | 11423 | encoded | `s 853(5) subsection (4) is without prejudice to the matter` |
| s 853(5)(b) | 11424 | encoded | `s 853(5) subsection (4) is without prejudice to the matter` |
| s 853(6) | 11425 | encoded | `s 853(6) the asset is a fixed asset` |
| heading 11426 | 11426 | inert | reason 1 (heading) |
| s 853A | 11427 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853A(1) | 11428 | fork | fork F33. `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(1) the last day of the period of 14 days after the end of the review period`; `s 853A(1) the company must deliver a confirmation statement to the registrar after the end of each review period`; `s 853A(1)(a) the company delivered the information necessary to make the confirmation statement`; `s 853A(1)(b) the confirmation statement confirms what the paragraph requires` |
| s 853A(1)(a) | 11429 | fork | fork F33. `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(1) the last day of the period of 14 days after the end of the review period`; `s 853A(1) the company must deliver a confirmation statement to the registrar after the end of each review period`; `s 853A(1)(a) the company delivered the information necessary to make the confirmation statement` |
| s 853A(1)(b) | 11430 | fork | fork F33. `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(1) the last day of the period of 14 days after the end of the review period`; `s 853A(1) the company must deliver a confirmation statement to the registrar after the end of each review period`; `s 853A(1)(b) the confirmation statement confirms what the paragraph requires` |
| s 853A(1)(b)(i) | 11431 | fork | fork F33. `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(1) the last day of the period of 14 days after the end of the review period`; `s 853A(1) the company must deliver a confirmation statement to the registrar after the end of each review period`; `s 853A(1)(b) the confirmation statement confirms what the paragraph requires` |
| s 853A(1)(b)(ii) | 11432 | fork | fork F33. `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(1) the last day of the period of 14 days after the end of the review period`; `s 853A(1) the company must deliver a confirmation statement to the registrar after the end of each review period`; `s 853A(1)(b) the confirmation statement confirms what the paragraph requires` |
| s 853A(1)(b)(iii) | 11433 | fork | fork F33. `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(1) the last day of the period of 14 days after the end of the review period`; `s 853A(1) the company must deliver a confirmation statement to the registrar after the end of each review period`; `s 853A(1)(b) the confirmation statement confirms what the paragraph requires` |
| s 853A(2) | 11434 | repealed or blank in this text | the text shows only dots |
| s 853A(3) | 11435 | encoded | `s 853A(3) the first day of the confirmation period`; `s 853A(3) the confirmation date and the last day of the confirmation period` |
| s 853A(3)(a) | 11436 | encoded | `s 853A(3) the first day of the confirmation period`; `s 853A(3) the confirmation date and the last day of the confirmation period` |
| s 853A(3)(b) | 11437 | encoded | `s 853A(3) the first day of the confirmation period`; `s 853A(3) the confirmation date and the last day of the confirmation period` |
| s 853A(4) | 11438 | encoded | `s 853A(4) the confirmation date is no later than the last day of the review period concerned` |
| s 853A(5) | 11439 | fork | fork F34. `s 853A(5) the last day of the review period beginning on the day` |
| s 853A(5)(a) | 11440 | fork | fork F34. `s 853A(5) the last day of the review period beginning on the day` |
| s 853A(5)(b) | 11441 | fork | fork F34. `s 853A(5) the last day of the review period beginning on the day` |
| s 853A(6) | 11442 | encoded | `s 853A(6) the first day of the next review period` |
| s 853A(7) | 11443 | encoded | `s 853A(7) the company is entitled to assume that information that has been delivered to the registrar has been properly delivered` |
| s 853B | 11444-11445 | fork | fork F27. section row: its text is in the subsection rows. `s 853B duty`; `s 853B the duty is a duty to notify a relevant event` |
| s 853B(a) | 11446 | repealed or blank in this text | the text shows only dots |
| s 853B(b) | 11447 | repealed or blank in this text | the text shows only dots |
| s 853B(c) | 11448 | fork | fork F27. `s 853B duty`; `s 853B the duty is a duty to notify a relevant event` |
| s 853B(d) | 11449 | repealed or blank in this text | the text shows only dots |
| s 853B(e) | 11450 | fork | fork F27. `s 853B duty`; `s 853B the duty is a duty to notify a relevant event` |
| s 853B(f) | 11451 | repealed or blank in this text | the text shows only dots |
| s 853B(fa) | 11452 | repealed or blank in this text | the text shows only dots |
| s 853B(g) | 11453 | fork | fork F27. `s 853B duty`; `s 853B the duty is a duty to notify a relevant event` |
| s 853B(h) | 11454 | fork | fork F27. `s 853B duty`; `s 853B the duty is a duty to notify a relevant event` |
| s 853BA | 11455-11456 | encoded | section row: its text is in the subsection rows. `s 853BA the company must deliver at the same time a statement that the intended future activities of the company are lawful`; `s 853BA the company must deliver a statement that its intended future activities are lawful` |
| s 853C | 11457 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853C(1) | 11458 | encoded | `s 853C(1) this section applies` |
| s 853C(1)(a) | 11459 | encoded | `s 853C(1) this section applies` |
| s 853C(1)(b) | 11460 | encoded | `s 853C(1) this section applies` |
| s 853C(1A) | 11461 | encoded | `s 853C(1A) this section also applies` |
| s 853C(1A)(a) | 11462 | encoded | `s 853C(1A) this section also applies` |
| s 853C(1A)(b) | 11463 | encoded | `s 853C(1A) this section also applies` |
| s 853C(2) | 11464 | encoded | `s 853C(2) the company must give notice to the registrar of the change at the same time as it delivers the confirmation statement`; `s 853C(2) the company must give notice to the registrar of the change in its principal business activities` |
| s 853C(3) | 11465 | encoded | `s 853C(3) the information may be given by reference to one or more categories of the system` |
| s 853CA | 11466 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853CA(1) | 11467 | encoded | `s 853CA(1) this section applies` |
| s 853CA(1)(a) | 11468 | encoded | `s 853CA(1) this section applies` |
| s 853CA(1)(b) | 11469 | encoded | `s 853CA(1) this section applies` |
| s 853CA(1)(c) | 11470 | encoded | `s 853CA(1) this section applies` |
| s 853CA(2) | 11471 | encoded | `s 853CA(2) the company must deliver a notice under section 87 at the same time as it delivers the confirmation statement`; `s 853CA(2) the company must deliver a notice under section 87 with the confirmation statement` |
| s 853CB | 11472 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853CB(1) | 11473 | encoded | `s 853CB(1) this section applies` |
| s 853CB(1)(a) | 11474 | encoded | `s 853CB(1) this section applies` |
| s 853CB(1)(b) | 11475 | encoded | `s 853CB(1) this section applies` |
| s 853CB(1)(c) | 11476 | encoded | `s 853CB(1) this section applies` |
| s 853CB(2) | 11477 | encoded | `s 853CB(2) the company must deliver a notice under section 88B at the same time as it delivers the confirmation statement`; `s 853CB(2) the company must deliver a notice under section 88B with the confirmation statement` |
| s 853D | 11478 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853D(1) | 11479 | encoded | `s 853D(1) this section applies` |
| s 853D(2) | 11480 | encoded | `s 853D(2) the company must deliver a statement of capital to the registrar at the same time as it delivers the confirmation statement`; `s 853D(2) the company must deliver a statement of capital with the confirmation statement` |
| s 853D(3) | 11481 | fork | fork F35. the exception is an input of s 853D(2). `s 853D(2) the company must deliver a statement of capital to the registrar at the same time as it delivers the confirmation statement`; `s 853D(2) the company must deliver a statement of capital with the confirmation statement` |
| s 853D(4) | 11482 | fork | fork F9. `s 853D(4)(d) statement about a class of shares`; `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853D(4)(a) | 11483 | fork | fork F9. `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853D(4)(b) | 11484 | fork | fork F9. `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853D(4)(c) | 11485 | fork | fork F9. `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853D(4)(d) | 11486 | fork | fork F9. `s 853D(4)(d) statement about a class of shares`; `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853D(4)(d)(i) | 11487 | fork | fork F9. `s 853D(4)(d) statement about a class of shares`; `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853D(4)(d)(ii) | 11488 | fork | fork F9. `s 853D(4)(d) statement about a class of shares`; `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853D(4)(d)(iii) | 11489 | fork | fork F9. `s 853D(4)(d) statement about a class of shares`; `s 853D(4) the statement of capital states what the subsection requires with respect to the company's share capital at the confirmation date` |
| s 853E | 11490 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853E(1) | 11491 | encoded | `s 853E(1) this section applies` |
| s 853E(2) | 11492 | encoded | `s 853E(2) the company must deliver to the registrar a statement dealing with the matters mentioned in subsection (4) at the same time as it delivers the confirmation statement`; `s 853E(2) the company must deliver a statement of the trading status of its shares with the confirmation statement` |
| s 853E(3) | 11493 | fork | fork F35. the exception is an input of s 853E(2). `s 853E(2) the company must deliver to the registrar a statement dealing with the matters mentioned in subsection (4) at the same time as it delivers the confirmation statement`; `s 853E(2) the company must deliver a statement of the trading status of its shares with the confirmation statement` |
| s 853E(4) | 11494 | encoded | `s 853E(4) trading status`; `s 853E(4) the matters the statement must deal with` |
| s 853E(4)(a) | 11495 | encoded | `s 853E(4) trading status`; `s 853E(4) the matters the statement must deal with` |
| s 853E(4)(b) | 11496 | encoded | `s 853E(4) trading status`; `s 853E(4) the matters the statement must deal with` |
| s 853E(5) | 11497 | encoded | `s 853E(5) both conditions were satisfied throughout the confirmation period concerned` |
| s 853E(5)(a) | 11498 | encoded | `s 853E(5) both conditions were satisfied throughout the confirmation period concerned` |
| s 853E(5)(b) | 11499 | encoded | `s 853E(5) both conditions were satisfied throughout the confirmation period concerned` |
| s 853E(6) | 11500-11502 | encoded | `s 853E(6) the issuer is a DTR5 issuer`; `s 853E(6) the market is a relevant market` |
| s 853E(6)(a) | 11503 | encoded | `s 853E(6) the issuer is a DTR5 issuer`; `s 853E(6) the market is a relevant market` |
| s 853E(6)(b) | 11504-11505 | encoded | `s 853E(6) the issuer is a DTR5 issuer`; `s 853E(6) the market is a relevant market` |
| s 853F | 11506 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853F(1) | 11507 | encoded | `s 853F(1) this section applies` |
| s 853F(1)(a) | 11508 | encoded | `s 853F(1) this section applies` |
| s 853F(1)(b) | 11509 | repealed or blank in this text | the text shows only dots |
| s 853F(2) | 11510 | fork | fork F36. `s 853F(2) the company is a non-traded company` |
| s 853F(3) | 11511 | encoded | `s 853F(3) the company must deliver the information falling within subsection (5) to the registrar at the same time as it delivers the confirmation statement`; `s 853F(3) the non-traded company must deliver the shareholder information with the confirmation statement` |
| s 853F(4) | 11512 | fork | fork F35. the exception is an input of s 853F(3). `s 853F(3) the company must deliver the information falling within subsection (5) to the registrar at the same time as it delivers the confirmation statement`; `s 853F(3) the non-traded company must deliver the shareholder information with the confirmation statement` |
| s 853F(5) | 11513 | fork | fork F9. `s 853F(5) the information delivered is the information the subsection requires` |
| s 853F(5)(a) | 11514 | fork | fork F9. `s 853F(5) the information delivered is the information the subsection requires` |
| s 853F(5)(b) | 11515 | fork | fork F9. `s 853F(5) the information delivered is the information the subsection requires` |
| s 853F(5)(c) | 11516 | fork | fork F9. `s 853F(5) the information delivered is the information the subsection requires` |
| s 853F(5)(d) | 11517 | fork | fork F9. `s 853F(5) the information delivered is the information the subsection requires` |
| s 853F(6) | 11518 | encoded | `s 853F(6) the registrar may impose the requirement` |
| s 853G | 11519 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853G(1) | 11520 | encoded | `s 853G(1) this section applies` |
| s 853G(2) | 11521 | fork | fork F36. `s 853G(2) the company is a traded company` |
| s 853G(3) | 11522 | fork | fork F36. the exception is a limb of s 853G(2). `s 853G(2) the company is a traded company` |
| s 853G(3)(a) | 11523 | fork | fork F36. a limb of s 853G(2). `s 853G(2) the company is a traded company` |
| s 853G(3)(b) | 11524 | fork | fork F36. a limb of s 853G(2). `s 853G(2) the company is a traded company` |
| s 853G(4) | 11525 | encoded | `s 853G(4) the company must deliver the information falling within subsection (6) to the registrar at the same time as it delivers the confirmation statement`; `s 853G(4) the traded company must deliver the shareholder information with the confirmation statement` |
| s 853G(5) | 11526 | fork | fork F35. the exception is an input of s 853G(4). `s 853G(4) the company must deliver the information falling within subsection (6) to the registrar at the same time as it delivers the confirmation statement`; `s 853G(4) the traded company must deliver the shareholder information with the confirmation statement` |
| s 853G(6) | 11527 | encoded | `s 853G(6)(a) the person is a person whose name and address must be delivered`; `s 853G(6) the information delivered is the information the subsection requires` |
| s 853G(6)(a) | 11528 | encoded | `s 853G(6)(a) the person is a person whose name and address must be delivered`; `s 853G(6) the information delivered is the information the subsection requires` |
| s 853G(6)(b) | 11529 | fork | fork F9. `s 853G(6) the information delivered is the information the subsection requires` |
| s 853H | 11530 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853H(1) | 11531 | encoded | `s 853H(1) this section applies` |
| s 853H(2) | 11532 | encoded | `s 853H(2) the company must deliver to the registrar a statement of the fact that it is a company to which Part 21A does not apply at the same time as it delivers the confirmation statement`; `s 853H(2) the company must deliver a statement of the fact that Part 21A does not apply to it with the confirmation statement` |
| s 853H(2A) | 11533 | encoded | `s 853H(2A) description of company`; `s 853H(2A) the statement under subsection (2) specifies what the subsection requires` |
| s 853H(2A)(a) | 11534 | encoded | `s 853H(2A) description of company`; `s 853H(2A) the statement under subsection (2) specifies what the subsection requires` |
| s 853H(2A)(b) | 11535 | encoded | `s 853H(2A) description of company`; `s 853H(2A) the statement under subsection (2) specifies what the subsection requires` |
| s 853H(3) | 11536 | fork | fork F35. the exception is an input of s 853H(2). `s 853H(2) the company must deliver to the registrar a statement of the fact that it is a company to which Part 21A does not apply at the same time as it delivers the confirmation statement`; `s 853H(2) the company must deliver a statement of the fact that Part 21A does not apply to it with the confirmation statement` |
| s 853I | 11537-11538 | repealed or blank in this text | the text shows only dots under the heading |
| s 853J | 11539 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide is no rule until they are made) |
| s 853J(1) | 11540 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(2) | 11541 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(2)(a) | 11542 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(2)(b) | 11543 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(3) | 11544 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4) | 11545 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(a) | 11546 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(a)(i) | 11547 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(a)(ii) | 11548 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(b) | 11549 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(b)(i) | 11550 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(b)(ii) | 11551 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(c) | 11552 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(d) | 11553 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(d)(i) | 11554 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(4)(d)(ii) | 11555 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(5) | 11556 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853J(6) | 11557 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |
| s 853K | 11558 | inert | reason 2 (machinery: a regulation-making power) |
| s 853K(1) | 11559 | inert | reason 2 (machinery: a regulation-making power) |
| s 853K(2) | 11560 | inert | reason 2 (machinery: a regulation-making power) |
| s 853K(2)(a) | 11561 | inert | reason 2 (machinery: a regulation-making power) |
| s 853K(2)(b) | 11562 | inert | reason 2 (machinery: a regulation-making power) |
| s 853K(3) | 11563 | inert | reason 2 (machinery: a regulation-making power) |
| s 853K(4) | 11564 | inert | reason 2 (machinery: a regulation-making power) |
| s 853L | 11565 | inert | reason 1 (heading: the section title; the operative text is in the rows beneath it) |
| s 853L(1) | 11566 | fork | fork F33, F37. `s 853L(1) the company has failed to deliver a confirmation statement before the end of the period of 14 days after the end of the review period`; `s 853L(1) the person is treated as a director for the purposes of subsection (1)`; `s 853L(1) the company must not fail to deliver a confirmation statement before the end of the period of 14 days after the end of a review period`; `s 853L(1)(a) the company commits an offence`; `s 853L(1)(b) the officer of the company commits an offence` |
| s 853L(1)(a) | 11567 | fork | fork F33, F37. `s 853L(1) the company has failed to deliver a confirmation statement before the end of the period of 14 days after the end of the review period`; `s 853L(1) the person is treated as a director for the purposes of subsection (1)`; `s 853L(1) the company must not fail to deliver a confirmation statement before the end of the period of 14 days after the end of a review period`; `s 853L(1)(a) the company commits an offence` |
| s 853L(1)(b) | 11568-11569 | fork | fork F33, F37. `s 853L(1) the company has failed to deliver a confirmation statement before the end of the period of 14 days after the end of the review period`; `s 853L(1) the person is treated as a director for the purposes of subsection (1)`; `s 853L(1) the company must not fail to deliver a confirmation statement before the end of the period of 14 days after the end of a review period`; `s 853L(1)(b) the officer of the company commits an offence` |
| s 853L(2) | 11570 | encoded | `s 853L(2) daily default fine limit`; `s 853L(2) penalty`; `s 853L(2) the penalty on summary conviction`; `s 853L(2) the daily default fine limit in pounds` |
| s 853L(2)(a) | 11571 | encoded | `s 853L(2) daily default fine limit`; `s 853L(2) penalty`; `s 853L(2) the penalty on summary conviction`; `s 853L(2) the daily default fine limit in pounds` |
| s 853L(2)(b) | 11572 | encoded | `s 853L(2) daily default fine limit`; `s 853L(2) penalty`; `s 853L(2) the penalty on summary conviction`; `s 853L(2) the daily default fine limit in pounds` |
| s 853L(3) | 11573 | encoded | `s 853L(3) the contravention continues` |
| s 853L(4) | 11574 | repealed or blank in this text | the text shows only dots |
| s 853L(5) | 11575 | fork | fork F38. `s 853L(5) the officer commits an offence in relation to the continued contravention` |
| s 853L(6) | 11576 | encoded | `s 853L(6) the fine for each day on which the contravention continues and the person is in default does not exceed` |
| s 853L(6)(a) | 11577 | encoded | `s 853L(6) the fine for each day on which the contravention continues and the person is in default does not exceed` |
| s 853L(6)(b) | 11578 | encoded | `s 853L(6) the fine for each day on which the contravention continues and the person is in default does not exceed` |
| s 854 | 11579-11580 | repealed or blank in this text | the text shows only dots under the heading |
| s 855 | 11581-11582 | repealed or blank in this text | the text shows only dots under the heading |
| s 855A | 11583-11584 | repealed or blank in this text | the text shows only dots under the heading |
| s 856 | 11585-11586 | repealed or blank in this text | the text shows only dots under the heading |
| s 856A | 11587-11588 | repealed or blank in this text | the text shows only dots under the heading |
| s 856B | 11589-11590 | repealed or blank in this text | the text shows only dots under the heading |
| s 857 | 11591-11592 | repealed or blank in this text | the text shows only dots under the heading |
| s 858 | 11593-11594 | repealed or blank in this text | the text shows only dots under the heading |
| s 859 | 11595-11596 | repealed or blank in this text | the text shows only dots under the heading |
| s 822(2) “infant” | 11064 | fork | fork F16. `s 822(2) the person is an infant` |
| s 824(1) “target company” | 11076 | encoded | `s 824(1) an interest in shares may arise from the agreement` |
| s 824(5)(a) “agreement” | 11088 | encoded | `s 824(5) the reference has a corresponding meaning` |
| s 829 “distribution” | 11122 | encoded | `s 829(2) description of act`; `s 829(2) the act is not a distribution for the purposes of this Part`; `s 829(1) the act is a distribution` |
| s 829(1) “distribution” | 11123 | encoded | `s 829(1) the act is a distribution` |
| s 831(2) “net assets” | 11140 | encoded | `s 831(2) the company's net assets` |
| s 831(3) “Liabilities” | 11141 | encoded | `s 831(3) kind of relevant accounts`; `s 831(3) the provision is included in liabilities` |
| s 832(6)(b) “relevant period” | 11174 | encoded | `s 832(6)(b) the first day of the relevant period` |
| s 833 “investment company” | 11179 | encoded | `s 833(2)(a) the requirement is met`; `s 833(1) the company is an investment company`; `s 833(4) the notice to the registrar of intention to carry on business as an investment company is revoked`; `s 833(5) the company ceases to be an investment company` |
| s 833(1) “investment company” | 11180 | encoded | `s 833(1) the company is an investment company` |
| s 833A(4) “A” | 11195-11200 | encoded | `s 833A(4) the amount given by the formula A - L - D` |
| s 833A(4) “L” | 11195-11200 | encoded | `s 833A(4) the amount given by the formula A - L - D` |
| s 833A(4) “D” | 11195-11200 | encoded | `s 833A(4) the amount given by the formula A - L - D` |
| s 833A(9) “best estimate” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “paid-in ordinary share capital” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “paid-in preference shares” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “relevant risk-free interest rate term structure” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “ring-fenced fund” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “defined benefit pension scheme” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “long-term business” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “qualifying investment subsidiary” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 833A(9) “Solvency 2 Directive” | 11225-11230 | encoded | `s 833A(9) the term has the meaning given by the Prudential Regulation Authority's rules`; `s 833A(9) the scheme is a defined benefit pension scheme`; `s 833A(9) the business is long-term business`; `s 833A(9) the undertaking is a qualifying investment subsidiary`; `s 833A(9) the instrument is the Solvency 2 Directive` |
| s 838(4) “Properly prepared” | 11270 | encoded | `s 838(4) the interim accounts are properly prepared` |
| s 839(4) “Properly prepared” | 11278 | encoded | `s 839(4) the initial accounts are properly prepared` |
| s 840(3) “financial assistance” | 11296 | encoded | `s 840(3) the assistance is financial assistance for the purposes of this section` |
| s 840(4)(a) “net assets” | 11298 | fork | fork F21. `s 840(4)(a) the company's net assets` |
| s 840(4)(b) “net liabilities” | 11299-11300 | fork | fork F21. `s 840(4)(b) the company's net liabilities` |
| s 841(3) “revaluation provision” | 11311 | encoded | `s 841(3) the provision is a revaluation provision` |
| s 843(6) “actuarial investigation” | 11341 | encoded | `s 843(6) the investigation is an actuarial investigation` |
| s 843(7) “long-term business” | 11345-11346 | encoded | `s 843(7) the business is long-term business` |
| s 843(8) “insurance special purpose vehicle” | 11347 | encoded | `s 843(8) the vehicle is an insurance special purpose vehicle` |
| s 845(4) “book value” | 11370 | encoded | `s 845(4) the book value of the asset` |
| s 853(3) “Capitalisation” | 11418 | encoded | `s 853(3) operation`; `s 853(3) the operation is capitalisation` |
| s 853(4) “realised profits” | 11421 | encoded | `s 853(4) the profit or loss is a realised profit or loss in relation to the company's accounts` |
| s 853(4) “realised losses” | 11421 | encoded | `s 853(4) the profit or loss is a realised profit or loss in relation to the company's accounts` |
| s 853(6) “Fixed assets” | 11425 | encoded | `s 853(6) the asset is a fixed asset` |
| s 853A(1)(b) “confirmation statement” | 11430 | fork | fork F33. `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(1) the last day of the period of 14 days after the end of the review period`; `s 853A(1) the company must deliver a confirmation statement to the registrar after the end of each review period` |
| s 853A(3) “confirmation period” | 11435 | encoded | `s 853A(3) the first day of the confirmation period`; `s 853A(3) the confirmation date and the last day of the confirmation period` |
| s 853A(3)(a) “the confirmation date” | 11436 | encoded | `s 853A(3) the first day of the confirmation period`; `s 853A(3) the confirmation date and the last day of the confirmation period` |
| s 853E(6) “DTR5 issuer” | 11500-11502 | encoded | `s 853E(6) the issuer is a DTR5 issuer`; `s 853E(6) the market is a relevant market` |
| s 853E(6) “relevant market” | 11500-11502 | encoded | `s 853E(6) the issuer is a DTR5 issuer`; `s 853E(6) the market is a relevant market` |
| s 853E(6)(a) “the Act” | 11503 | encoded | `s 853E(6) the issuer is a DTR5 issuer`; `s 853E(6) the market is a relevant market` |
| s 853F(2) “non-traded company” | 11510 | fork | fork F36. `s 853F(2) the company is a non-traded company` |
| s 853G(2) “traded company” | 11521 | fork | fork F36. `s 853G(2) the company is a traded company` |
| s 853J(1) “relevant information” | 11540 | inert | reason 2 (machinery: a regulation-making power; what regulations may provide, including the daily default fine of the greater of 500 pounds and one-tenth of level 4, is no rule until they are made) |

## Fork register (coa18)

Each entry gives the provision and rule, the reading taken, the text that licenses it, and the other reading.
"Marginal reading (a)" and "(b)" are the two readings the brief leaves to a lawyer: (a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
The six sites the maintainer ruled on 2026-11-05 to be decided case by case (an "unless" once met, a bare "must" not done, "listed in Schedule N", a duty whose "if" or "where" is unmet, "(other than X)", a missing event in the state ledger) each have a fork line here: F5 (unless met), F9 (bare "must"), F15 (a deeming "if"), F28 ("other than"); no site of "listed in Schedule N" or of a state ledger occurs in this range.

- **F1** (s 791; `s 791 this Part applies to the company`): Taken: The "only" closes: a private company answers JUST FALSE and a public company JUST TRUE.
  The gate is NOT threaded into ss 792 to 828 (it would repeat one rule dozens of times): the seat layer asks s 791 itself and in the s 793(1) question about the company's power to give a notice, and the other seat questions take the facts the person states.
  Licence: "This Part applies only to public companies." Other reading: "only" states a necessary condition, so a public company answers NOTHING.
- **F2** (s 793(1)(b); `s 793(1)(b) the date is within the three years immediately preceding the date on which the notice is issued`): Taken: The window runs from the date three years before the notice (`add years`, clamped on 29 February) up to, but not including, the notice date; a present interest on the notice date is limb (a).
  Inside: JUST TRUE; outside: JUST FALSE (a period the text fixes in its own words, ruling of 2026-11-05 (a)).
  Licence: "at any time during the three years immediately preceding the date on which the notice is issued" Other reading: The notice date itself falls within the period.
- **F3** (s 793(7); `s 793(7) the information required by the notice was given within the time specified`): Taken: Whether the time the notice specifies is reasonable is a judgment the text leaves open: an input.
  An unreasonable time answers NOTHING; a reasonable one is a fixed period (late: JUST FALSE).
  Licence: "within such reasonable time as may be specified in the notice" Other reading: The time specified binds whatever its length, so lateness is JUST FALSE even when the time was unreasonable.
- **F4** (ss 795(1)(a) and (b), 798(2)(a) to (d), 814(1), 814(2): offences created by "A person who ..." or "It is an offence for a person ..."): Taken: A person outside the description (did not fail to comply; did none of the listed things; made no such statement) answers NOTHING ("limited by its own wording", reading (b)): the text says what the described person commits and says nothing of anyone else.
  A flat negative (the defence of s 795(2): "does not commit an offence ... if he proves") answers JUST FALSE.
  Licence: "A person who— (a) fails to comply with a notice under section 793"; "A person commits an offence if he—"; "It is an offence for a person" Other reading: Treat "A person who ... commits an offence" as an "if": the person outside it answers JUST FALSE (reading (a)).
- **F5** (s 796(2) `s 796(2) the Secretary of State is barred from granting the exemption`; s 800(3) `s 800(3) the court is barred from making an order under section 800` (an "unless" once it is met: one of the six sites of the ruling of 2026-11-05)): Taken: The function is the bar itself: JUST TRUE where the conditions of the "unless" are not met ("must not"), JUST FALSE where one is met (the bar does not apply).
  The text does not say the Secretary of State or the court must grant, so the bar is never turned into a grant.
  A regulative rule (`s 796(2) the Secretary of State must not grant the exemption unless the conditions are met`) carries the same bar.
  Licence: "The Secretary of State must not grant any such exemption unless—"; "The court must not make an order under this section unless—" Other reading: Where the "unless" is met the answer is NOTHING, because lifting the bar does not say the order may be made.
- **F6** (s 797(1)(a) to (d), (2), (3), (4); s 798(5)): Taken: Under an order, the effect applies (JUST TRUE); where the act is within a direction under s 794(2), 799(3) (or 799, 800 for s 798) or the terms of an interim order, the effect does not (JUST FALSE: "subject to" read as an exception); with no order, (1) answers NOTHING (the effect of an order is stated, nothing of other shares) but (2) and (3) answer JUST FALSE ("Where shares are subject to the restriction").
  Licence: "The provisions of this section are subject— (a) to any directions under section 794(2) or section 799(3)"; "Where shares are subject to the restriction in subsection (1)(a), an agreement to transfer the shares is void." Other reading: "subject to" is a limit of the grant, so a direction answers NOTHING; and with no order (1) answers JUST FALSE.
- **F7** (s 798(2)(a)(ii), (b), (c)): Taken: "any such shares" is read as "shares that to his knowledge, are for the time being subject to restrictions" of (a)(i), so knowledge is an element of (a) and (b).
  Licence: "to dispose of shares that to his knowledge, are for the time being subject to restrictions"; "votes in respect of any such shares" Other reading: "such shares" means shares under an order, with no knowledge needed for (b) (voting or appointing a proxy).
- **F8** (s 803(2); `s 803(2) the company is required to exercise its powers under section 793`): Taken: "once it has received requests" is read like "where": below 10% of the paid-up voting capital the answer is JUST FALSE; exactly 10% is enough ("at least").
  Licence: "A company is required to do so once it has received requests (to the same effect) from members of the company holding at least 10%" Other reading: "once" is not on the list of words that close, so below 10% answers NOTHING.
- **F9** (requirements stated with a bare "must" (a duty whose condition is unmet: one of the six sites of the ruling of 2026-11-05): ss 803(3), 808(3), (4), 810(3), (4), 811(4), 825(4), 837(2), (3), 838(1), 839(1), (5), 853D(4), 853F(5), 853G(6)): Taken: The function is named for compliance ("the request meets the requirements of this subsection"), and an unmet requirement answers JUST FALSE ("does not meet"), which claims nothing about what follows.
  Licence: "A request ... (b) must— (i) state that the company is requested to exercise its powers under section 793"; "The register must be made up so that the entries against the names entered in it appear in chronological order." Other reading: A bare "must" not done answers NOTHING, since the text says nothing of the consequence.
- **F10** (ss 806(1) and 809(4): "default is made for 14 days"): Taken: The 14 days are a fact the person states (a BOOLEAN: has the company been in default for 14 days), not reckoned by s 827, which concerns "the period allowed by any provision of this Part for fulfilling an obligation".
  Licence: "If default is made for 14 days in complying with section 805(5)"; "Where the period allowed by any provision of this Part for fulfilling an obligation is expressed as a number of days" Other reading: The 14 days are reckoned in working days under s 827.
- **F11** (the periods of ss 805(1), (3), (6), 807(2), 808(2), 810(2) and s 827): Taken: The first day counted is the day after the trigger; a day that is not a working day is disregarded (`s 827 the last day of a period of days counting only working days`, a stepper).
  Whether a day is a working day is the keel's rule (s 1173(1)), which a part may not import: the stepper takes it as a function from a date to BOOLEAN, and the duty functions take the count of working days as an input. s 805(1) and (3) take "not more than 15 days" as the outer limit of "a reasonable period"; both limbs must hold.
  Licence: "any day that is not a working day shall be disregarded in reckoning that period"; "within three days of the receipt" Other reading: The day of the trigger counts as day 1.
- **F12** (s 805(4); `s 805(4) the reports must still be retained and kept available for inspection`): Taken: The sixth anniversary of the first day of availability is still inside the retention period; the day after is outside (JUST FALSE).
  Licence: "for at least six years from the date on which they are first made available for inspection" Other reading: The period ends before the anniversary.
- **F13** (s 805(2); `s 805(2) the number of interim reports the company must cause to be prepared`): Taken: One interim report for each three-month period (by `add months`, clamped) that ends strictly before the day the investigation concludes; a conclusion on the last day of a period is "within" it.
  Licence: "is not concluded within three months after the date on which the company became subject to the requirement"; "each succeeding period of three months ending before the conclusion of the investigation" Other reading: A report for each period that has begun by the conclusion.
- **F14** (s 816 `s 816 the company may remove the entry from the register`; s 819(1)): Taken: "more than six years": strictly more than the sixth anniversary (clamped on 29 February); "until the end of the period of six years": the sixth anniversary is still inside.
  Licence: "if more than six years have elapsed since the entry was made"; "until the end of the period of six years after it ceased to be such a company" Other reading: Exactly six years suffices for s 816.
- **F15** (deeming provisions introduced by "if" or "where": ss 820(3) to (6), 823(1) to (3), 825(2) (marginal reading (a))): Taken: JUST TRUE where the limb holds; where the "if" or "where" fails, JUST FALSE for that provision alone.
  Ruling E1, option C: the sections answer one by one, and no function gathers ss 820 to 825 into "has an interest in shares"; a caller asks each and takes any JUST TRUE.
  Licence: "A person is treated as having an interest in shares if—"; "Where an interest in shares is comprised in property held on trust" Other reading: A failed limb answers NOTHING, since another provision of ss 820 to 825 may give the interest.
- **F16** (s 822(2); `s 822(2) the person is an infant`): Taken: In relation to Scotland, under 18 is JUST TRUE and 18 or over JUST FALSE ("means"); elsewhere the Part does not define "infant", so NOTHING.
  The part of the United Kingdom is asked with the core's `Place of registration`.
  Licence: "In relation to Scotland “infant” means a person under the age of 18 years." Other reading: JUST FALSE elsewhere.
- **F17** (s 824(6)(a), (b); `s 824(6)(a) this section does not apply to the agreement`): Taken: Not legally binding and no mutuality: JUST TRUE (the section does not apply); not binding but with mutuality: JUST FALSE ("unless" met); a binding agreement: NOTHING.
  Underwriting agreement confined to that purpose: JUST TRUE; not confined ("provided"): JUST FALSE; not an underwriting agreement: NOTHING.
  Licence: "to an agreement that is not legally binding unless it involves mutuality"; "provided the agreement is confined to that purpose" Other reading: The "unless" met answers NOTHING.
- **F18** (s 829(1), (2)(c)): Taken: The exception for a redemption or purchase out of capital or unrealised profits is "in accordance with Chapter 3, 4 or 5 of Part 18": an input from Part 18. Not shown to be in accordance: NOTHING for both (2) and (1), since the exception does not reach it and the text does not say it is a distribution.
  Licence: "the redemption or purchase of any of the company's own shares out of capital (including the proceeds of any fresh issue of shares) or out of unrealised profits in accordance with Chapter 3, 4 or 5 of Part 18" Other reading: Not in accordance: JUST TRUE for (1) (it is a distribution of assets to members).
- **F19** (s 830(1); `s 830(1) the distribution is within the profits available for the purpose`): Taken: Within the profits available: JUST TRUE, meaning only that this limit is not exceeded (ss 831 and 832 also restrict); above: JUST FALSE ("may only").
  The name does not claim the company may make the distribution.
  Licence: "A company may only make a distribution out of profits available for the purpose." Other reading: Within: NOTHING (a necessary condition does not grant).
- **F20** (s 831(1), (5)): Taken: "A public company may only ..." and "A public company must not ...": a private company is not mentioned, so NOTHING (section 830 still applies to it); contrast s 791 (F1).
  Licence: "A public company may only make a distribution—" Other reading: JUST TRUE (or JUST FALSE) for a private company as for a public one.
- **F21** ("the amount by which X exceeds Y": ss 831(4)(c), 833A(5)(a), (c), (e), 840(4), 841(5), 843(3)(b), (4)): Taken: Where X does not exceed Y there is no such amount: zero (never a negative figure).
  Licence: "the amount by which its accumulated, unrealised profits (so far as not previously utilised by capitalisation) exceed its accumulated, unrealised losses" Other reading: A negative figure (the shortfall).
- **F22** (s 832(1); `s 832(1) the investment company may make the distribution out of its accumulated, realised revenue profits`): Taken: "if the following conditions are met": the answers of subsections (2), (3), (5) and (7) are inputs; any JUST FALSE (or an uncalled-capital asset) answers JUST FALSE, all JUST TRUE answers JUST TRUE, else NOTHING.
  A company that is not an investment company answers NOTHING.
  Licence: "An investment company may make a distribution out of its accumulated, realised revenue profits if the following conditions are met." Other reading: The conditions are restated in (1).
- **F23** (s 833A(5), (6)): Taken: "So far as anything falls within more than one of the above paragraphs ... only once": the caller supplies the value counted twice, which is subtracted once.
  Licence: "its value is to be taken into account only once" Other reading: A function that detects the overlap from the item list.
- **F24** (s 836(2); `s 836(2) the relevant accounts are the company's last annual accounts`): Taken: "The relevant accounts are the last annual accounts, except that ... it may be justified by reference to interim accounts": where an exception applies, which accounts are used is a permission, so NOTHING; where neither applies, JUST TRUE.
  The two permissions answer JUST FALSE when their "where" fails.
  Licence: "where the distribution would be found to contravene this Part by reference to the company's last annual accounts, it may be justified by reference to interim accounts" Other reading: The relevant accounts are the interim or initial accounts whenever the exception applies.
- **F25** (s 837(4), s 839(6)): Taken: When the report was not qualified no requirement arises, and the function answers JUST TRUE ("the requirements ... are met") without a FALSE-kind or NOTHING-kind tag.
  Licence: "If that report was qualified—" Other reading: NOTHING when the report was not qualified, since the subsection then says nothing.
- **F26** (s 838(2), s 839(2)): Taken: "Where interim (initial) accounts are prepared for a proposed distribution by a public company, the following requirements apply": a private company answers JUST FALSE (reading (a)/(b) of the periods ruling).
  Licence: "Where interim accounts are prepared for a proposed distribution by a public company, the following requirements apply." Other reading: NOTHING for a private company.
- **F27** (lists introduced by "are", "include" or "the following" that do not say "only": ss 836(1), 840(2), 841(2), 853B): Taken: An item or kind not listed answers NOTHING (list not closed).
  Licence: "is determined by reference to the following items"; "The following duties are duties to notify a relevant event—" Other reading: The list is closed by the words "the following", so JUST FALSE.
- **F28** (s 843(1); `s 843(1) the provisions of this section have effect in relation to the company` (an "(other than X)" site)): Taken: A company to which s 833A applies, or an insurance special purpose vehicle, answers JUST FALSE ("other than"); a company that is not an authorised insurance company with long-term business answers NOTHING.
  Licence: "other than— (a) a person to whom section 833A applies; or (b) an insurance special purpose vehicle" Other reading: NOTHING for the excluded companies (the exclusion only removes them from the scope).
- **F29** (s 844(1) to (3); `s 844(1)(a)`, `s 844(1)(b)`, `s 844(2) subsection (1) does not apply to the part of the amount`, `s 844(3) subsection (1) does not apply`): Taken: (1)(a) and (b): development costs not shown as an asset: JUST FALSE ("Where"); where the exception of (2) or (3) applies: JUST FALSE ("This is subject to the following exceptions", which the text itself calls exceptions: marginal reading (a)); otherwise JUST TRUE.
  (2): the part that represents an unrealised profit on revaluation: JUST TRUE; any other part: NOTHING (a scope limit with no "only").
  (3): a condition of the "if" unmet: JUST FALSE; the note required by regulations under s 396 is a seam, and a NOTHING seam stays NOTHING.
  Licence: "Where development costs are shown or included as an asset in a company's accounts, any amount shown or included in respect of those costs is treated"; "This is subject to the following exceptions." Other reading: "subject to" limits the grant, so the exception answers NOTHING (reading (b)); and (1) answers NOTHING when the costs are not shown as an asset.
- **F30** (s 847(2); `s 847(2) what the member is liable to do`): Taken: The answer is a constructor: repay (cash), pay the value (not cash), or "not liable under this subsection" where the member neither knew nor had reasonable grounds ("If ... knows", a failed "if", reading (a)) or the s 847(4) exclusions apply or the distribution was not made in contravention of the Part (s 847(1)).
  Licence: "If at the time of the distribution the member knows or has reasonable grounds for believing that it is so made, he is liable" Other reading: NOTHING where the member did not know (the subsection is silent about him).
- **F31** (s 848(1); `s 848(1) that provision continues as authority for those profits to be so applied after the relevant date`): Taken: Authorised before the relevant date and the provision not altered: JUST TRUE; not authorised: JUST FALSE ("Where"); altered: NOTHING ("subject to any alteration of the articles").
  Licence: "that provision continues (subject to any alteration of the articles) as authority for those profits to be so applied after that date" Other reading: An altered provision still continues (JUST TRUE).
- **F32** (s 851(1)): Taken: "Except as provided in this section" is an exception met: the matter provided for in the section answers JUST FALSE.
  Licence: "Except as provided in this section, the provisions of this Part are without prejudice to any rule of law" Other reading: NOTHING when the exception is met.
- **F33** (s 853A(1), s 853L(1); `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`): Taken: The 14 days are calendar days (s 827 is limited to Part 22), counted from the day after the last day of the review period; a statement delivered on the fourteenth day is in time.
  Licence: "before the end of the period of 14 days after the end of each review period" Other reading: "before the end of the period" excludes the fourteenth day; or the 14 days are working days.
- **F34** (s 853A(5); `s 853A(5) the last day of the review period beginning on the day`): Taken: 12 months beginning with a day end on the day before its anniversary; for a day of 29 February the anniversary in a year that is not a leap year is taken as 1 March, so the period ends on 28 February.
  Licence: "the period of 12 months beginning with the day of the company's incorporation" Other reading: The period ends on 27 February (the clamped anniversary 28 February less a day).
- **F35** (ss 853D(3), 853E(3), 853F(4), 853G(5), 853H(3): "if and to the extent that"): Taken: All or nothing: a BOOLEAN input says whether the earlier statement applies equally; where it does the duty answers JUST FALSE.
  Licence: "Subsection (2) does not apply if and to the extent that the last statement delivered to the registrar under this section applies equally to the confirmation period concerned." Other reading: A partial exception: only the part of the information that applies equally is excused.
- **F36** (ss 853F(2), 853G(2), (3)): Taken: A "non-traded company" is a company none of whose shares were admitted to trading (any admitted: JUST FALSE); a "traded company" any of whose shares were (none: JUST FALSE), except one that satisfied both conditions throughout (JUST FALSE).
  Licence: "A “traded company” is a company any of whose shares were, at any time during the confirmation period concerned, shares admitted to trading on a relevant market" Other reading: NOTHING for the cases outside each definition.
- **F37** (s 853L(1); `s 853L(1) the company has failed to deliver a confirmation statement before the end of the period of 14 days after the end of the review period`): Taken: Delivered in time, or not yet due: JUST FALSE ("If a company fails"); delivered late, or not delivered and due: JUST TRUE.
  An officer's offence is the seam `s 1121 the officer is in default`; a shadow director is treated as a director by `s 853L(1) the person is treated as a director for the purposes of subsection (1)`.
  Licence: "If a company fails to deliver a confirmation statement before the end of the period of 14 days after the end of a review period an offence is committed by—" Other reading: NOTHING while the period has not ended.
- **F38** (s 853L(5), (6)): Taken: The officer who did not commit an offence under (1) but is in default in relation to the continued contravention: the seam passes through; any other officer: JUST FALSE.
  Licence: "an offence is also committed by every officer of the company who did not commit an offence under subsection (1) in relation to the initial contravention" Other reading: NOTHING for any other officer.
- **F39** (s 826(1); `s 826(1)(a) the information must not be included in a report under section 805`): Taken: "Information in respect of which a company is for the time being entitled to any exemption conferred by regulations under section 409(3)": the entitlement is the seam; JUST TRUE where the seam says so, NOTHING otherwise (the sentence is about that information only).
  Licence: "Information in respect of which a company is for the time being entitled to any exemption conferred by regulations under section 409(3)" Other reading: JUST FALSE where the company is not entitled.
- **F40** (s 807(2), s 811(2): "on request and on payment of such fee as may be prescribed"): Taken: "on" counts as "where": no request or no fee answers JUST FALSE.
  The fee is the input "paid the prescribed fee" (the amount is s 1167).
  Licence: "Any person is entitled, on request and on payment of such fee as may be prescribed, to be provided with a copy" Other reading: NOTHING.
- **F41** (s 802(1)): Taken: The passive "must be paid into court" names no payer, so no regulative rule is written; the sum is computed (proceeds less costs) and NOTHING where the sale was not under a court order.
  Licence: "the proceeds of the sale, less the costs of the sale, must be paid into court for the benefit of the persons who are beneficially interested in the shares" Other reading: A duty of the company.
- **F42** (s 793(2)(b); `s 793(2)(b) the notice may require the person to give further information` (name-test sweep of 2026-11-12)): Taken: A function named for a power ("may require") whose gate is "if he holds, or has during that time held, any such interest": a person with no such interest answers NOTHING (the grant is limited by its own wording; the text does not say the notice may not require the information).
  Licence: "if he holds, or has during that time held, any such interest, to give such further information" Other reading: JUST FALSE for a person with no such interest (a failed "if" read as the text's own no: marginal reading (a)).
- **F43** (s 794(2); `s 794(2) the court may direct that acts set out in the order shall not constitute a breach of the restrictions` (name-test sweep of 2026-11-12)): Taken: A power ("the court may") gated by "If the court is satisfied that such an order may unfairly affect the rights of third parties": where the court is not satisfied the answer is NOTHING.
  Licence: "If the court is satisfied that such an order may unfairly affect the rights of third parties in respect of the shares, the court may" Other reading: JUST FALSE when the court is not satisfied (a failed "if" read as the text's no).
- **F44** (s 799(3); `s 799(3) the court may direct that acts set out in the order do not constitute a breach of the restrictions` (name-test sweep of 2026-11-12)): Taken: A power ("it may") gated by "If the court is satisfied that the application is well-founded": where it is not satisfied the answer is NOTHING.
  Licence: "If the court is satisfied that the application is well-founded, it may" Other reading: JUST FALSE when the application is not well-founded (a failed "if" read as the text's no).
- **F45** (s 812(6); `s 812(6) the court may direct that the company is not to comply with any such request` (name-test sweep of 2026-11-12)): Taken: A power ("it may direct") gated by "If the court makes such a direction and it appears to the court that the company is or may be subject to other requests made for a similar purpose": where either part fails the answer is NOTHING.
  Licence: "If the court makes such a direction and it appears to the court that the company is or may be subject to other requests made for a similar purpose" Other reading: JUST FALSE where either part of the gate fails (a failed "if" read as the text's no).
- **F46** (s 816; `s 816 the company may remove the entry from the register` (name-test sweep of 2026-11-12; the boundary is F14)): Taken: A permission ("A company may remove an entry ... if more than six years have elapsed") whose gate is "if": an entry that is six years old or less answers NOTHING (the text does not forbid removal; s 815(1) is the bar, with its own exceptions).
  Licence: "if more than six years have elapsed since the entry was made" Other reading: JUST FALSE for an entry that is six years old or less (a failed "if" read as the text's no).
- **F47** (s 817(4); `s 817(4) the applicant may apply to the court for an order directing the company to remove the entry` (name-test sweep of 2026-11-12)): Taken: A power ("the applicant may apply") gated by "If an application under subsection (3) is refused": where it was not refused the answer is NOTHING.
  Licence: "If an application under subsection (3) is refused, the applicant may apply to the court" Other reading: JUST FALSE where the application was not refused (a failed "if" read as the text's no).
- **F48** (s 818(3); `s 818(3) the applicant may apply to the court for an order directing the company to include the information in the register` (name-test sweep of 2026-11-12)): Taken: A power ("the applicant may apply") gated by "If an application under this section is refused (otherwise than on the ground that the information has already been recorded)": where it was not refused, or was refused only on that ground, the answer is NOTHING.
  Licence: "If an application under this section is refused (otherwise than on the ground that the information has already been recorded), the applicant may apply to the court" Other reading: JUST FALSE in both cases (a failed "if" read as the text's no).
- **N1** (ss 794(4), 841(1), 853(1) (and the sentence "For the effect of such an order see section 797." inside s 794(1))): Taken: Signposts and lead-ins ("Sections 798 to 802 make further provision", "The following provisions have effect for the purposes of this Part", "The following provisions apply for the purposes of this Part") are inert under reason 1: each says only what the section does and creates no rule.
  That is a judgment, not one of the brief's three reasons read literally: the keel took the same judgment for its own signposts and lead-ins (KEEL-NOTES.md, fork F7).
  Other reading: Operative lead-ins that fix the scope of the provisions beneath them (each would be a function answering JUST TRUE).

### Name-test sweep of 2026-11-12: named for a power or grant, answers `JUST FALSE`, listed and not flipped

Assumed, not ruled: a "may" function whose gate is "where", "when", "upon" or an equivalent condition (in the case of, on such an application, on ...) goes with this list, and so does every function named "entitled".
Ruling (b) of the Guide's "Periods, where and scope limits" paragraph (and ruling (c) of the 2026-11-05 delegated ruling) says `JUST FALSE`; the Guide's line on grants points the other way.
This is a question for the maintainer or a lawyer, not one to settle by sweep.
The other reading for the "may" rows is `NOTHING` (a grant limited by its own wording does not say the power is lacking when the gate fails); the reading taken is `JUST FALSE` (a failed "where", "when" or "upon" is the text's no).
The other reading for the "entitled" rows is that an entitlement is a claim the Guide does not settle, so a failed gate would answer `NOTHING`; the reading taken is `JUST FALSE`.

| function | module | group | gate in the text |
| --- | --- | --- | --- |
| `s 793(4) the notice may require the person to give such particulars with respect to that other interest as the notice...` | part22-notice | "may" with where | "The notice may require the person to whom it is addressed, where— (a) his interest is a present interest and another interest in the shares subsists, or (b) ..." |
| `s 793(6) the notice may require the person to give particulars of the identity of the person who held that interest i...` | part22-notice | "may" with where | "where his interest is a past interest" |
| `s 794(1) the company may apply to the court for an order directing that the shares in question be subject to restrict...` | part22-notice | "may" with where | "Where— (a) a notice under section 793 ... is served by a company on a person who is or was interested in shares in the company, and (b) that person fails to give the company the information required" |
| `s 794(3) the court may make an interim order` | part22-notice | "may" with on such an application | "On an application under this section the court may make an interim order." |
| `s 800(5)(a) an application may be made for an order directing that the shares shall cease to be subject to those rest...` | part22-notice | "may" with where | "Where any restrictions continue in force under subsection (4)— (a) an application may be made under this section" |
| `s 801(3) the court may make such further order relating to the sale or transfer of the shares as it thinks fit` | part22-notice | "may" with where | "Where the court has made an order under this section, it may make such further order" |
| `s 801(5) the court may order that the applicant's costs (in Scotland, expenses) be paid out of the proceeds of sale` | part22-notice | "may" with on | "On making an order under subsection (1) or (3) the court may order that the applicant's costs" |
| `s 807(5) the court may by order compel an immediate inspection or direct that the copy required be sent to the person...` | part22-notice | "may" with in the case of | "In the case of any such refusal or default the court may by order compel an immediate inspection" |
| `s 813(3) the court may by order compel an immediate inspection or direct that the copy required be sent to the person...` | part22-register | "may" with in the case of | "In the case of any such refusal or default the court may by order compel an immediate inspection" |
| `s 817(2) that other person may apply to the company for the removal of the entry from the register` | part22-register | "may" with where (the scope of subsection (1)) | "This section applies where in pursuance of an obligation imposed by a notice under section 793 ... a person gives to a company the name and address of another person" |
| `s 836(2)(a) the distribution may be justified by reference to interim accounts` | part23-ch2 | "may" with where | "where the distribution would be found to contravene this Part by reference to the company's last annual accounts, it may be justified by reference to interim accounts" |
| `s 836(2)(b) the distribution may be justified by reference to initial accounts` | part23-ch2 | "may" with where | "where the distribution is proposed to be declared during the company's first accounting reference period, or before any accounts have been circulated in respect of that period, it may be justified by reference to initial accounts" |
| `s 850(1) the directors may treat the profit as realised` | part23-ch3 | "may" with where | "Where the directors of a company are, after making all reasonable enquiries, unable to determine whether a particular profit made before the relevant date is realised or unrealised, they may treat the profit as realised." |
| `s 850(2) the directors may treat the loss as unrealised` | part23-ch3 | "may" with where | "Where the directors of a company, after making all reasonable enquiries, are unable to determine whether a particular loss made before the relevant date is realised or unrealised, they may treat the loss as unrealised." |
| `s 820(5) the person is entitled to exercise or control the exercise of a right conferred by the holding of shares` | part22-interest | "entitled" | a deeming definition ("is entitled ... if he— (a) has a right ... or (b) is under an obligation ...") rather than a claim |
| `s 823(2) the person is treated as entitled to exercise or control the exercise of the voting power` | part22-interest | "entitled" | a deeming provision ("is treated as entitled ... if") rather than a claim |
| `s 823(3) the person is treated as entitled to exercise or control the exercise of the voting power` | part22-interest | "entitled" | a deeming provision ("is treated as entitled ... if") rather than a claim |
| `s 802(4) the applicant under section 801 is entitled to payment of his costs out of the proceeds before any person in...` | part22-notice | "entitled" | a claim gated by "If the court has ordered under section 801(5) that the costs ... are to be paid out of the proceeds of sale" |
| `s 807(2) the person is entitled to be provided with a copy of the report or any part of it` | part22-notice | "entitled" | a claim gated by "on request and on payment of such fee as may be prescribed" |
| `s 811(2) the person is entitled to be provided with a copy of any entry in the register` | part22-register | "entitled" | a claim gated by "on request and on payment of such fee as may be prescribed" |
| `s 853A(7) the company is entitled to assume that information that has been delivered to the registrar has been proper...` | part24 | "entitled" | a claim closed by "unless the registrar has notified the company otherwise" |

### Rulings applied (copied word for word from the brief)

Each ruling below is recorded again here because this part carries `NOTHING-kind` tags that rest on it.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run.
  The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04.
  Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said.
  The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written.
  Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04.
  Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.
  The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed.
  The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling.
  Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger.
  Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover.
  The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Jural relations (coa18)

Hohfeld's correlatives: right / duty (claim), privilege / no-right (liberty), power / liability, immunity / disability.
Each provision that creates a relation is stated once, as a relation between two parties.
A row that creates none is `none`, once, with its reason.
The Act names no prosecutor: the holder of the right in an offence is written "the State (the Act names no prosecutor)", which is a description of who benefits, not an actor the text names.
The table covers every section from s 791 to s 859 (the script refuses to run if one is missing).

| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | relation | L4 rule(s) |
| --- | --- | --- | --- | --- |
| s 791 | - | - | none: a scope rule (the Part applies only to public companies) | `s 791 this Part applies to the company` |
| s 792 | - | - | none: a definition ("share") | `s 792(1) the shares are the company's shares for the purposes of this Part` |
| s 793(1) to (6) | a public company | a person the company knows or has reasonable cause to believe is, or was within three years, interested in its shares | power / liability (the company may require information by notice; the person is liable to be so required) | `s 793(1) the company may give notice to the person`; `s 793(2)(a) the notice may require the person to confirm that fact or to state whether or not it is the case`; `s 793(3) the notice may require the person to give particulars of his own present or past interest`; `s 793(4) the notice may require the person to give such particulars with respect to that other interest as the notice requires`; `s 793(5) kind of particular`; `s 793(6) the notice may require the person to give particulars of the identity of the person who held that interest immediately upon his ceasing to hold it` |
| s 793(7) | the company that gave the notice | the person addressed | right / duty (the information must be given within the reasonable time the notice specifies) | `s 793(7) the information required by the notice was given within the time specified` |
| s 794(1) to (3) | the company (to apply); the court (to order) | the holder of the shares in question | power / liability (the shares may be made subject to restrictions; third parties may be protected by direction) | `s 794(1) the company may apply to the court for an order directing that the shares in question be subject to restrictions`; `s 794(2) the court may direct that acts set out in the order shall not constitute a breach of the restrictions`; `s 794(3) the court may make an interim order` |
| s 794(4) | - | - | none: a signpost (inert, reason 1; fork note N1) | - |
| s 795(1) to (5) | the State (the Act names no prosecutor) | a person who fails to comply with a s 793 notice, or makes a false statement in purported compliance | right / duty (the offence; the defence of s 795(2); the penalty of s 795(3) and (4)) | `s 795(1)(a) the person commits an offence by failing to comply with the notice`; `s 795(1)(b) the person commits an offence by a false statement in purported compliance with the notice`; `s 795(3) the penalty on conviction` |
| s 796(1) | a person the Secretary of State has for the time being exempted | the company that would require the information | immunity / disability (the exempted person is not obliged to comply with a s 793 notice) | `s 796(1) the person is not obliged to comply with a notice under section 793` |
| s 796(2) | anyone affected by the grant of an exemption | the Secretary of State | right / duty (the Secretary of State must not grant an exemption unless the conditions are met) | `s 796(2) the Secretary of State is barred from granting the exemption` |
| s 797(1) to (4) | the company and anyone dealing in or relying on the shares | the holder of shares under an order | immunity / disability (the holder cannot transfer, vote, be issued further shares or be paid; an agreement to transfer is void; subject to directions and interim terms) | `s 797(1)(a) any transfer of the shares is void`; `s 797(1)(b) no voting rights are exercisable in respect of the shares`; `s 797(1)(c) no further shares may be issued in right of the shares or in pursuance of an offer made to their holder`; `s 797(1)(d) no payment may be made of sums due from the company on the shares` |
| s 798(1) to (6) | the State (the Act names no prosecutor) | a person who disposes of, votes, or fails to notify about shares known to be subject to restrictions | right / duty (the offences of (2), (3) and the penalties) | `s 798(2)(a) the person commits an offence by exercising a right to dispose`; `s 798(2)(b) the person commits an offence by voting or appointing a proxy`; `s 798(2)(c) the holder commits an offence by failing to notify the restrictions` |
| s 799 | the company; a person aggrieved (to apply); the court (to direct) | the holder of the shares | power / liability (restrictions may be relaxed to protect third parties) | `s 799(2) the person may make an application for an order under section 799`; `s 799(3) the court may direct that acts set out in the order do not constitute a breach of the restrictions` |
| s 800 | the company; a person aggrieved (to apply) | the court (barred from ordering unless a condition of (3) is met) | privilege / no-right (to apply); disability of the court to order otherwise ("must not unless") | `s 800(3) the court is barred from making an order under section 800` |
| s 801 | the company (only the company may apply under (2)); the court (to order a sale) | the holder of the shares | power / liability | `s 801(2) the person may apply for an order under subsection (1)` |
| s 802 | the persons beneficially interested in the shares | the court (the proceeds, less costs, must be paid into court and then paid out under (3)) | right / duty | `s 802(1) the sum to be paid into court for the benefit of the persons who are beneficially interested in the shares`; `s 802(3) the amount the court shall order paid to the applicant` |
| s 803(1) to (3) | members holding at least 10% of the voting paid-up capital | the company | power / liability (the members may require the company to exercise its s 793 powers; the request must meet (3)) | `s 803(2) the company is required to exercise its powers under section 793`; `s 803(3) the request meets the requirements of this subsection` |
| s 804(1) | the members who made the requests | the company | right / duty (the company must exercise its powers as the requirement specifies) | `s 804(1) the company must exercise those powers in the manner specified in the requests` |
| s 804(2) to (3) | the State (the Act names no prosecutor) | every officer of the company in default | right / duty (the offence and penalty) | `s 804(2) the officer of the company commits an offence`; `s 804(3) the penalty on conviction` |
| s 805(1) to (3), (6) | the members who made the requests | the company | right / duty (a report on conclusion; interim reports; the report made available within 15 days; members told where within three days) | `s 805(1) the report was made available for inspection within a reasonable period (not more than 15 days) after the conclusion of the investigation`; `s 805(2) the number of interim reports the company must cause to be prepared`; `s 805(3) each such report was made available for inspection within a reasonable period (not more than 15 days) after the end of the period to which it relates`; `s 805(6) the company notified the members who made the requests where the report is available within three days` |
| s 805(4), (5) | the registrar; any person entitled to inspect | the company | right / duty (retention for six years; notice to the registrar of the place the reports are kept) | `s 805(4) the reports must still be retained and kept available for inspection`; `s 805(5) the company must give notice to the registrar of the place and of any change in that place` |
| s 805(7) | - | - | none: a definition of when an investigation is concluded | `s 805(7) inquiry` |
| s 806 | the State (the Act names no prosecutor) | the company and every officer in default | right / duty (the offences for default of 14 days in complying with s 805(5); penalties) | `s 806(1)(a) the company commits an offence`; `s 806(1)(b) the officer of the company commits an offence`; `s 806(2) the penalty on summary conviction` |
| s 807(1), (2) | any person | the company | right / duty (inspect the reports without charge; a copy on request and fee within ten days) | `s 807(1) the report must be open to inspection by any person without charge`; `s 807(2) the person is entitled to be provided with a copy of the report or any part of it` |
| s 807(3) to (5) | the State (the Act names no prosecutor) | the company and every officer in default; the court may compel inspection | right / duty (the offences of refusal); power / liability (the court order of (5)) | `s 807(3)(a) the company commits an offence`; `s 807(3)(b) the officer of the company commits an offence`; `s 807(5) the court may by order compel an immediate inspection or direct that the copy required be sent to the person requiring it` |
| s 808 | any person who may inspect the register (s 811) | the company | right / duty (information received must be entered in the register within three days; the register is kept in the form (3) and (4) require) | `s 808(2) the company entered the information in the register within three days of the receipt`; `s 808(3) the information is entered against the name the subsection requires`; `s 808(4) the register is made up as the subsection requires` |
| s 809 | the registrar; any person entitled to inspect | the company | right / duty (the register kept available at the registered office or a place specified in regulations; notice to the registrar) | `s 809(1) the place at which the register is kept available for inspection is a place the subsection allows`; `s 809(2) the company must give notice to the registrar of companies of the place where the register is kept and of any change in that place`; `s 809(3) no such notice is required` |
| s 809(4), (5) | the State (the Act names no prosecutor) | the company and every officer in default | right / duty (the offences and penalty) | `s 809(4)(a) the company commits an offence`; `s 809(4)(b) the officer of the company commits an offence`; `s 809(5) the penalty on summary conviction` |
| s 810 | any person who may inspect the register | the company | right / duty (the associated index and its updating within ten days) | `s 810(1) the company must keep an index of the names entered in the register`; `s 810(2) the company made the entry or alteration in the index within ten days`; `s 810(3) the index is made up as the subsection requires` |
| s 811(1) to (3) | any person | the company | right / duty (inspect the register and index without charge; a copy of an entry on request and fee) | `s 811(1) the document must be open to inspection by any person without charge`; `s 811(2) the person is entitled to be provided with a copy of any entry in the register` |
| s 811(4) to (5) | - | - | none: what the request must contain; the consequence (the request is made under this section) is a counting rule | `s 811(4) kind of person` |
| s 812(1), (2) | the person who made the request | the company | right / duty (the company must comply if satisfied the request is for a proper purpose, refuse if not, and give its reason on refusal) | `s 812(1) what the company must do with the request`; `s 812(2) the company must inform the person making the request, stating the reason why it is not satisfied` |
| s 812(3) to (7) | a person whose request is refused (to apply to the court); the court (to direct) | the company (notice duties; to comply immediately if the court does not direct otherwise) | power / liability (the court may direct the company not to comply) and right / duty (the company's duties of (4)(b) and (7)) | `s 812(3) the person may apply to the court`; `s 812(4)(a) the person who made the request must notify the company`; `s 812(5) the court shall direct the company not to comply with the request`; `s 812(7) the company must comply with the request immediately upon the court giving its decision or the proceedings being discontinued` |
| s 813 | the State (the Act names no prosecutor) | the company and every officer in default | right / duty (the offence of refusing inspection or failing to provide a copy; penalties) | `s 813(1)(a) the company commits an offence`; `s 813(1)(b) the officer of the company commits an offence` |
| s 814 | the State (the Act names no prosecutor) | a person who discloses information obtained from the register | right / duty (the offences of (1) and (2); penalty) | `s 814(1) the person commits an offence by a misleading, false or deceptive statement in a request`; `s 814(2) the person commits an offence by disclosing the information` |
| s 815 | any person who relies on the register; the State (the offence of (3)) | the company and every officer in default | right / duty (entries must not be deleted except under s 816 or s 817 and a wrongly deleted entry must be restored); the offence and penalty of (3) and (4) | `s 815(1) the deletion of the entry is permitted`; `s 815(2) the company must restore the entry as soon as reasonably practicable`; `s 815(3)(a) the company commits an offence`; `s 815(3)(b) the officer of the company commits an offence` |
| s 816 | the company | - | privilege / no-right (it may remove an entry after more than six years) | `s 816 the company may remove the entry from the register` |
| s 817 | the other person named in an entry given in answer to a s 793 notice; the court (to order removal) | the company | power / liability ((2): the person may apply) and right / duty ((3): the company shall remove an incorrect entry; (4): the court may order removal) | `s 817(2) that other person may apply to the company for the removal of the entry from the register`; `s 817(3) the company shall remove the entry`; `s 817(4) the applicant may apply to the court for an order directing the company to remove the entry` |
| s 818 | a person identified in the register as a party to a s 824 agreement who has ceased to be a party; the court | the company | power / liability ((1): the person may apply) and right / duty ((2): the company shall record the cessation; (3): the court may order it) | `s 818(1) the person may apply to the company for the inclusion of that information in the register`; `s 818(2) the company shall record that information in every place where his name appears in the register as a party to the agreement`; `s 818(3) the applicant may apply to the court for an order directing the company to include the information in the register` |
| s 819 | any person who may inspect the register; the State (the Act names no prosecutor) | a company that has ceased to be public, and every officer in default | right / duty ((1): the register and index kept for six years; (2) and (3): the offence and penalty) | `s 819(1) the company must continue to keep the register and any associated index`; `s 819(2)(a) the company commits an offence`; `s 819(2)(b) the officer of the company commits an offence`; `s 819(3) the penalty on summary conviction` |
| s 820 to s 823 | - | - | none: rules for counting who has an interest in shares (E1 option C: answered section by section) | `s 820(4) the person is treated as having an interest in the shares`; `s 822(1) the person is taken to be interested in the shares`; `s 823(1) the person is taken to be interested in the shares` |
| s 824 | - | - | none: scope of the share acquisition agreement rule (who is treated as interested) | `s 824(2) this section applies to the agreement` |
| s 825 | the company that gave a s 793 notice | a party to a share acquisition agreement | right / duty (the notification that must be given) | `s 825(4) the notification contains what the subsection requires` |
| s 826 | the person or company entitled to an exemption under s 409(3) | the company (it must not include or disclose the information) | immunity / disability (the protected information stays out of the report and the register) | `s 826(1)(a) the information must not be included in a report under section 805`; `s 826(1)(b) the information must not be made available under section 811`; `s 826(2) the fact that the information is omitted must be stated in the report` |
| s 827 | - | - | none: a counting rule (working days) | `s 827 a day that is not a working day is disregarded in reckoning the period` |
| s 828 | the Secretary of State (power to make regulations) | persons subject to the regulations | power / liability, but inert (machinery, reason 2); no L4 rule | - |
| s 829 | - | - | none: a definition ("distribution") | `s 829(1) the act is a distribution` |
| s 830 | creditors and members | the company | immunity / disability (the company may only distribute out of profits available for the purpose) | `s 830(1) the distribution is within the profits available for the purpose`; `s 830(2) the profits available for distribution` |
| s 831 | creditors and members of a public company | the public company | immunity / disability (the net asset restriction) | `s 831(1) the distribution is within the net asset restriction`; `s 831(4) the company's undistributable reserves` |
| s 832 | an investment company | creditors and members | privilege / no-right (it may distribute out of accumulated realised revenue profits if the conditions are met) | `s 832(1) the investment company may make the distribution out of its accumulated, realised revenue profits` |
| s 833, s 833A | - | - | none: definitions and rules of counting for investment and insurance companies | `s 833(1) the company is an investment company`; `s 833A(5) the total value of the items within the subsection` |
| s 834, s 835 | - | - | none: repealed or blank in this text | - |
| s 836 to s 839 | creditors and members | the company | immunity / disability (a distribution is justified only by accounts that meet the requirements; otherwise it counts as contravening the Part) | `s 836(2) accounts`; `s 836(4) the accounts may not be relied on for the purposes of this Part and the distribution is treated as contravening this Part`; `s 837(2) the accounts were prepared as the subsection requires`; `s 838(2) the requirements of subsections (3) to (6) apply`; `s 839(2) the requirements of subsections (3) to (7) apply` |
| s 840 | - | - | none: a counting rule (earlier distributions and payments are added to a proposed distribution) | `s 840(1) the amount of the proposed distribution as increased for the purposes of this Part` |
| s 841 to s 844 | - | - | none: counting rules (what is a realised profit or loss) | `s 841(2) the provision is treated as a realised loss`; `s 842 the cost of the asset taken for the purposes of determining profit or loss`; `s 843(1) the provisions of this section have effect in relation to the company`; `s 844(1)(a) the amount shown or included in respect of the development costs is treated, for the purposes of section 830, as a realised loss` |
| s 845, s 846 | - | - | none: counting rules (the amount of a distribution in kind) | `s 845(2) the amount of the distribution or the relevant part of it`; `s 846(1) this section applies` |
| s 847 | the company | a member who received a distribution made in contravention | right / duty (repay it, or pay its value, if the member knew or had reasonable grounds to believe) | `s 847(2) liability of the member` |
| s 848 | - | - | none: a saving for older articles (counting rule for authority) | `s 848(1) that provision continues as authority for those profits to be so applied after the relevant date` |
| s 849 | creditors and members | the company | immunity / disability (it must not apply an unrealised profit in paying up debentures or unpaid amounts) | `s 849 the company may apply the profit in paying up debentures or any amounts unpaid on its issued shares` |
| s 850 | the directors | - | privilege / no-right (they may treat an undetermined older profit or loss as realised or unrealised) | `s 850(1) the directors may treat the profit as realised` |
| s 851, s 852 | - | - | none: savings that leave other law in place | `s 851(1) the provisions of this Part are without prejudice to the rule of law` |
| s 853 | - | - | none: minor definitions | `s 853(2)(a) the profit or loss is within the reference, whenever it was made`; `s 853(4) the profit or loss is a realised profit or loss in relation to the company's accounts`; `s 853(6) the asset is a fixed asset` |
| s 853A | the registrar | the company | right / duty (deliver a confirmation statement within 14 days after each review period); the review-period rules of (3) to (6) are counting rules | `s 853A(1) the confirmation statement was delivered before the end of the period of 14 days after the end of the review period`; `s 853A(5) the last day of the review period beginning on the day`; `s 853A(6) the first day of the next review period` |
| s 853B | the registrar | the company | right / duty (the listed duties to notify a relevant event are duties of the confirmation statement) | `s 853B duty` |
| s 853BA | the registrar | the company | right / duty (a statement that its intended future activities are lawful) | `s 853BA the company must deliver at the same time a statement that the intended future activities of the company are lawful` |
| s 853C, s 853CA, s 853CB | the registrar | the company | right / duty (notice of a change in principal business activities, registered office, registered email address) | `s 853C(2) the company must give notice to the registrar of the change at the same time as it delivers the confirmation statement`; `s 853CA(2) the company must deliver a notice under section 87 at the same time as it delivers the confirmation statement`; `s 853CB(2) the company must deliver a notice under section 88B at the same time as it delivers the confirmation statement` |
| s 853D | the registrar | the company | right / duty (a statement of capital) | `s 853D(2) the company must deliver a statement of capital to the registrar at the same time as it delivers the confirmation statement` |
| s 853E | the registrar | the company | right / duty (notice of the trading status of its shares) | `s 853E(2) the company must deliver to the registrar a statement dealing with the matters mentioned in subsection (4) at the same time as it delivers the confirmation statement` |
| s 853F, s 853G | the registrar | the company | right / duty (shareholder information: non-traded companies; certain traded companies) | `s 853F(3) the company must deliver the information falling within subsection (5) to the registrar at the same time as it delivers the confirmation statement`; `s 853G(4) the company must deliver the information falling within subsection (6) to the registrar at the same time as it delivers the confirmation statement` |
| s 853H | the registrar | the company | right / duty (information about the exemption from Part 21A) | `s 853H(2) the company must deliver to the registrar a statement of the fact that it is a company to which Part 21A does not apply at the same time as it delivers the confirmation statement` |
| s 853I | - | - | none: repealed or blank in this text | - |
| s 853J, s 853K | the Secretary of State (power to make regulations) | companies subject to them | power / liability, but inert (machinery, reason 2); no L4 rule | - |
| s 853L | the State (the Act names no prosecutor) | the company and every officer in default (a shadow director counts as a director) | right / duty (the offences of (1) and (5); penalties of (2) and (6)) | `s 853L(1)(a) the company commits an offence`; `s 853L(1)(b) the officer of the company commits an offence`; `s 853L(5) the officer commits an offence in relation to the continued contravention`; `s 853L(6) the fine for each day on which the contravention continues and the person is in default does not exceed` |
| s 854 to s 859 | - | - | none: repealed or blank in this text (annual returns) | - |

## Marginal readings for a lawyer (coa18)

These are the two readings the brief leaves to a lawyer: **(a)** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; **(b)** a prohibition or grant limited by its own wording does not.
The status quo is taken: (a) is followed (the branch answers `JUST FALSE`), (b) is followed (the branch answers `NOTHING`).
Below is every branch of the layer-1 modules tagged `FALSE-kind` (228) or `NOTHING-kind (limited by its own wording)` (89), generated by `work/build-notes.py` from the tags in the code, with the class given by a keyword test on the quoted words.
The class is a first sort for the reader, not a ruling: where it says "other: read the quoted words", read them.
Every result-position `JUST FALSE`, `NOTHING` or "no" constructor in the layer-1 modules carries a tag: checked at assembly by `grep` for a `THEN`, `ELSE` or `OTHERWISE` arm that answers `JUST FALSE` or `NOTHING` without one.
It finds only the four `ELSE NOTHING` of the daily-fine field in the `Penalty` rows of s 815(4) in `coa18-part22-register.l4`, a field value (the text states no daily fine where the contravention is not a continued one of subsection (2)), not an answer.
The `NOTHING` in the imprisonment field of the other `Penalty` rows is a field value in the same sense (the text states no prison term).
Branches that pass a seam answer through (written `... -- JUST FALSE here is the text's "who is in default"; NOTHING stays NOTHING`) return the seam's own value, not a literal, and are not in the tables.
Branches whose class is "means" or "only" are the text's own no under the brief's rule and are not marginal; they are listed so that a mis-sorted branch cannot hide.

**The other reading, for every row of the first table:** the failed "if", "where", "when", "once", "unless" or "except" answers `NOTHING` instead of `JUST FALSE` (the text says what happens when the condition holds and is silent when it does not).
**The other reading, for every row of the second table:** the case outside the limit answers `JUST FALSE` (the text's limit is itself a no).

### Branches flipped to `NOTHING` by the name-test sweep of 2026-11-12 (7)

Each is a function named for a power or grant whose gate is "if"; before the sweep the failed gate answered `JUST FALSE`, and now it answers `NOTHING` (reading (b)).
The other reading, for every one of them, is `JUST FALSE` (a failed "if" read as the text's own no: reading (a)).
Each has one fork line in the fork register.

- **F42** `s 793(2)(b)`: `s 793(2)(b) the notice may require the person to give further information`
- **F43** `s 794(2)`: `s 794(2) the court may direct that acts set out in the order shall not constitute a breach of the restrictions`
- **F44** `s 799(3)`: `s 799(3) the court may direct that acts set out in the order do not constitute a breach of the restrictions`
- **F45** `s 812(6)`: `s 812(6) the court may direct that the company is not to comply with any such request`
- **F46** `s 816`: `s 816 the company may remove the entry from the register`
- **F47** `s 817(4)`: `s 817(4) the applicant may apply to the court for an order directing the company to remove the entry`
- **F48** `s 818(3)`: `s 818(3) the applicant may apply to the court for an order directing the company to include the information in the register`

### Branches that answer `JUST FALSE` (228)

| function | file:line | class | quoted words |
| --- | --- | --- | --- |
| `s 820(1) this section applies to determine whether the person has an interest in the sh...` | part22-interest.l4:29 | other: read the quoted words | This section applies to determine for the purposes of this Part whether a person has an interest ... |
| `s 820(3) the person is treated as having an interest in the shares` | part22-interest.l4:58 | failed "if" / "where" / "when" (reading (a)) | Where an interest in shares is comprised in property held on trust, every beneficiary of the trus... |
| `s 820(4) the person is treated as having an interest in the shares` | part22-interest.l4:77 | failed "if" / "where" / "when" (reading (a)) | A person is treated as having an interest in shares if— (a) he enters into a contract to acquire ... |
| `s 820(5) the person is entitled to exercise or control the exercise of a right conferre...` | part22-interest.l4:90 | failed "if" / "where" / "when" (reading (a)) | For the purposes of subsection (4)(b) a person is entitled to exercise or control the exercise of... |
| `s 820(6) the person is treated as having an interest in shares` | part22-interest.l4:106 | failed "if" / "where" / "when" (reading (a)) | A person is treated as having an interest in shares if— (a) he has a right to call for delivery o... |
| `s 822(2) the person is an infant` | part22-interest.l4:181 | means (the text's own no; not marginal) | In relation to Scotland “infant” means a person under the age of 18 years. |
| `s 823(1) the person is taken to be interested in the shares` | part22-interest.l4:199 | failed "if" / "where" / "when" (reading (a)) | a person is taken to be interested in shares if a body corporate is interested in them and— (a) t... |
| `s 823(2) the person is treated as entitled to exercise or control the exercise of the v...` | part22-interest.l4:212 | failed "if" / "where" / "when" (reading (a)) | a person is treated as entitled to exercise or control the exercise of voting power if— (a) anoth... |
| `s 823(3) the person is treated as entitled to exercise or control the exercise of the v...` | part22-interest.l4:225 | failed "if" / "where" / "when" (reading (a)) | a person is treated as entitled to exercise or control the exercise of voting power if— (a) he ha... |
| `s 824(2) this section applies to the agreement` | part22-interest.l4:252 | failed "if" / "where" / "when" (reading (a)) | This section applies to such an agreement if— (a) the agreement includes provision imposing oblig... |
| `s 824(3) the use of interests in shares includes the act` | part22-interest.l4:269 | other: read the quoted words | The reference in subsection (2) to the use of interests in shares in the target company is to the... |
| `s 824(4) this section continues to apply to the agreement` | part22-interest.l4:284 | failed "if" / "where" / "when" (reading (a)) | Once an interest in shares in the target company has been acquired in pursuance of the agreement,... |
| `s 824(6)(a) this section does not apply to the agreement` | part22-interest.l4:351 | unless / except met (reading (a); fork F5 where the text bars) | unless it involves mutuality in the undertakings, expectations or understandings of the parties t... |
| `s 824(6)(b) this section does not apply to the agreement` | part22-interest.l4:362 | failed "if" / "where" / "when" (reading (a)) | provided the agreement is confined to that purpose and any matters incidental to it |
| `s 825(2) the interest of the party in shares in the target company is an interest apart...` | part22-interest.l4:388 | failed "if" / "where" / "when" (reading (a)) | an interest of a party to such an agreement in shares in the target company is an interest apart ... |
| `s 825(4) the notification contains what the subsection requires` | part22-interest.l4:419 | failed "if" / "where" / "when" (reading (a)) | A notification ... must— (a) state that the person making the notification is a party to such an ... |
| `s 826(2) the fact that the information is omitted must be stated in the report` | part22-interest.l4:449 | failed "if" / "where" / "when" (reading (a)) | Where any such information is omitted from a report under section 805, that fact must be stated i... |
| `s 791 this Part applies to the company` | part22-notice.l4:45 | "only" closes (the text's own no; ruled E1/N2 family) | This Part applies only to public companies. |
| `s 792(1) the shares are the company's shares for the purposes of this Part` | part22-notice.l4:61 | other: read the quoted words | References in this Part to a company's shares are to the company's issued shares of a class carry... |
| `s 792(2) a suspension of voting rights affects the application of this Part to interest...` | part22-notice.l4:69 | flat negative (ruled N2 option A; reading (a) of the brief) | The temporary suspension of voting rights in respect of any shares does not affect the applicatio... |
| `s 793(1)(b) the date is within the three years immediately preceding the date on which ...` | part22-notice.l4:97 | other: read the quoted words | at any time during the three years immediately preceding the date on which the notice is issued |
| `s 793(4) the notice may require the person to give such particulars with respect to tha...` | part22-notice.l4:140 | failed "if" / "where" / "when" (reading (a)) | The notice may require the person to whom it is addressed, where— (a) his interest is a present i... |
| `s 793(6) the notice may require the person to give particulars of the identity of the p...` | part22-notice.l4:173 | failed "if" / "where" / "when" (reading (a)) | where his interest is a past interest |
| `s 793(7) the information required by the notice was given within the time specified` | part22-notice.l4:187 | other: read the quoted words | The information required by the notice must be given within such reasonable time as may be specif... |
| `s 794(1) the company may apply to the court for an order directing that the shares in q...` | part22-notice.l4:223 | failed "if" / "where" / "when" (reading (a)) | Where— (a) a notice under section 793 ... is served by a company on a person who is or was intere... |
| `s 794(3) the court may make an interim order` | part22-notice.l4:244 | other: read the quoted words | On an application under this section the court may make an interim order. |
| `s 795(1)(a) the person commits an offence by failing to comply with the notice` | part22-notice.l4:276 | failed "if" / "where" / "when" (reading (a)) | A person does not commit an offence under subsection (1)(a) if he proves that the requirement to ... |
| `s 796(2) the Secretary of State is barred from granting the exemption` | part22-notice.l4:335 | unless / except met (reading (a); fork F5 where the text bars) | The Secretary of State must not grant any such exemption unless— (a) he has consulted ... and (b)... |
| `s 797(1)(a) any transfer of the shares is void` | part22-notice.l4:370 | failed "if" / "where" / "when" (reading (a)) | (4) The provisions of this section are subject— (a) to any directions under section 794(2) or sec... |
| `s 797(1)(b) no voting rights are exercisable in respect of the shares` | part22-notice.l4:381 | failed "if" / "where" / "when" (reading (a)) | (4) The provisions of this section are subject— (a) to any directions under section 794(2) or sec... |
| `s 797(1)(c) no further shares may be issued in right of the shares or in pursuance of a...` | part22-notice.l4:392 | failed "if" / "where" / "when" (reading (a)) | (4) The provisions of this section are subject— (a) to any directions under section 794(2) or sec... |
| `s 797(1)(d) no payment may be made of sums due from the company on the shares` | part22-notice.l4:404 | unless / except met (reading (a); fork F5 where the text bars) | (d) except in a liquidation, no payment may be made of sums due from the company on the shares |
| `s 797(1)(d) no payment may be made of sums due from the company on the shares` | part22-notice.l4:405 | failed "if" / "where" / "when" (reading (a)) | (4) The provisions of this section are subject— (a) to any directions under section 794(2) or sec... |
| `s 797(2) an agreement to transfer the shares is void` | part22-notice.l4:419 | failed "if" / "where" / "when" (reading (a)) | Where shares are subject to the restriction in subsection (1)(a), an agreement to transfer the sh... |
| `s 797(2) an agreement to transfer the shares is void` | part22-notice.l4:420 | flat negative (ruled N2 option A; reading (a) of the brief) | This does not apply to an agreement to transfer the shares on the making of an order under sectio... |
| `s 797(2) an agreement to transfer the shares is void` | part22-notice.l4:421 | failed "if" / "where" / "when" (reading (a)) | (4) The provisions of this section are subject— (a) to any directions under section 794(2) or sec... |
| `s 797(3) an agreement to transfer any such right is void` | part22-notice.l4:435 | failed "if" / "where" / "when" (reading (a)) | Where shares are subject to the restriction in subsection (1)(c) or (d), an agreement to transfer... |
| `s 797(3) an agreement to transfer any such right is void` | part22-notice.l4:437 | flat negative (ruled N2 option A; reading (a) of the brief) | This does not apply to an agreement to transfer any such right on the making of an order under se... |
| `s 797(3) an agreement to transfer any such right is void` | part22-notice.l4:438 | failed "if" / "where" / "when" (reading (a)) | (4) The provisions of this section are subject— (a) to any directions under section 794(2) or sec... |
| `s 798(1) this section applies` | part22-notice.l4:466 | failed "if" / "where" / "when" (reading (a)) | This section applies where shares are subject to restrictions by virtue of an order under section... |
| `s 798(2)(a) the person commits an offence by exercising a right to dispose` | part22-notice.l4:487 | failed "if" / "where" / "when" (reading (a)) | (5) The provisions of this section are subject— (a) to any directions under— section 794(2) ..., ... |
| `s 798(2)(b) the person commits an offence by voting or appointing a proxy` | part22-notice.l4:499 | failed "if" / "where" / "when" (reading (a)) | (5) The provisions of this section are subject— (a) to any directions under— section 794(2) ..., ... |
| `s 798(2)(c) the holder commits an offence by failing to notify the restrictions` | part22-notice.l4:513 | failed "if" / "where" / "when" (reading (a)) | (5) The provisions of this section are subject— (a) to any directions under— section 794(2) ..., ... |
| `s 798(2)(d) the person commits an offence by entering into a void agreement` | part22-notice.l4:529 | failed "if" / "where" / "when" (reading (a)) | (5) The provisions of this section are subject— (a) to any directions under— section 794(2) ..., ... |
| `s 798(3)(a) the company commits an offence` | part22-notice.l4:543 | failed "if" / "where" / "when" (reading (a)) | If shares in a company are issued in contravention of the restrictions, an offence is committed b... |
| `s 798(3)(b) the officer of the company commits an offence` | part22-notice.l4:552 | failed "if" / "where" / "when" (reading (a)) | If shares in a company are issued in contravention of the restrictions, an offence is committed b... |
| `s 800(3) the court is barred from making an order under section 800` | part22-notice.l4:655 | unless / except met (reading (a); fork F5 where the text bars) | The court must not make an order under this section unless— (a) it is satisfied that ... or (b) t... |
| `s 800(5)(a) an application may be made for an order directing that the shares shall cea...` | part22-notice.l4:680 | failed "if" / "where" / "when" (reading (a)) | Where any restrictions continue in force under subsection (4)— (a) an application may be made und... |
| `s 800(5)(b) subsection (3) does not apply in relation to the making of such an order` | part22-notice.l4:688 | failed "if" / "where" / "when" (reading (a)) | Where any restrictions continue in force under subsection (4)— ... (b) subsection (3) does not apply |
| `s 801(2) the person may apply for an order under subsection (1)` | part22-notice.l4:708 | "only" closes (the text's own no; ruled E1/N2 family) | An application for an order under subsection (1) may only be made by the company. |
| `s 801(3) the court may make such further order relating to the sale or transfer of the ...` | part22-notice.l4:717 | failed "if" / "where" / "when" (reading (a)) | Where the court has made an order under this section, it may make such further order |
| `s 801(5) the court may order that the applicant's costs (in Scotland, expenses) be paid...` | part22-notice.l4:742 | other: read the quoted words | On making an order under subsection (1) or (3) the court may order that the applicant's costs ...... |
| `s 802(4) the applicant under section 801 is entitled to payment of his costs out of the...` | part22-notice.l4:796 | failed "if" / "where" / "when" (reading (a)) | If the court has ordered under section 801(5) that the costs ... of an applicant under that secti... |
| `s 803(2) the company is required to exercise its powers under section 793` | part22-notice.l4:823 | failed "if" / "where" / "when" (reading (a)) | A company is required to do so once it has received requests (to the same effect) from members of... |
| `s 803(3) the request meets the requirements of this subsection` | part22-notice.l4:846 | other: read the quoted words | A request ... (b) must— (i) state that the company is requested ..., (ii) specify the manner ...,... |
| `s 804(1) the company must exercise those powers in the manner specified in the requests` | part22-notice.l4:857 | other: read the quoted words | A company that is required under section 803 to exercise its powers under section 793 ... must ex... |
| `s 804(2) the officer of the company commits an offence` | part22-notice.l4:875 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with subsection (1) an offence is committed by every officer of t... |
| `s 805(1) the report was made available for inspection within a reasonable period (not m...` | part22-notice.l4:907 | flat negative (ruled N2 option A; reading (a) of the brief) | The report must be made available for inspection within a reasonable period (not more than 15 day... |
| `s 805(3) each such report was made available for inspection within a reasonable period ...` | part22-notice.l4:959 | flat negative (ruled N2 option A; reading (a) of the brief) | Each such report must be made available for inspection within a reasonable period (not more than ... |
| `s 805(4) the reports must still be retained and kept available for inspection` | part22-notice.l4:980 | other: read the quoted words | The reports must be retained by the company for at least six years from the date on which they ar... |
| `s 805(5) the company must give notice to the registrar of the place and of any change i...` | part22-notice.l4:1002 | unless / except met (reading (a); fork F5 where the text bars) | unless they have at all times been kept at the company's registered office |
| `s 805(6) the company notified the members who made the requests where the report is ava...` | part22-notice.l4:1020 | failed "if" / "where" / "when" (reading (a)) | The company must within three days of making any report prepared under this section available for... |
| `s 805(7) the investigation carried out by the company in pursuance of a requirement und...` | part22-notice.l4:1058 | failed "if" / "where" / "when" (reading (a)) | an investigation ... is concluded when— (a) the company has made all such inquiries ..., and (b) ... |
| `s 806(1)(a) the company commits an offence` | part22-notice.l4:1071 | failed "if" / "where" / "when" (reading (a)) | If default is made for 14 days in complying with section 805(5) ... an offence is committed by— (... |
| `s 806(1)(b) the officer of the company commits an offence` | part22-notice.l4:1080 | failed "if" / "where" / "when" (reading (a)) | If default is made for 14 days in complying with section 805(5) ... an offence is committed by— .... |
| `s 806(3) the officer of the company commits an offence` | part22-notice.l4:1103 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with any other provision of section 805 ..., an offence is commit... |
| `s 807(1) the report must be open to inspection by any person without charge` | part22-notice.l4:1130 | other: read the quoted words | Any report prepared under section 805 must be open to inspection by any person without charge. |
| `s 807(2) the person is entitled to be provided with a copy of the report or any part of it` | part22-notice.l4:1141 | failed "if" / "where" / "when" (reading (a)) | Any person is entitled, on request and on payment of such fee as may be prescribed, to be provide... |
| `s 807(2) the copy was provided within ten days after the request was received` | part22-notice.l4:1149 | failed "if" / "where" / "when" (reading (a)) | The copy must be provided within ten days after the request is received by the company. |
| `s 807(3)(a) the company commits an offence` | part22-notice.l4:1177 | failed "if" / "where" / "when" (reading (a)) | If an inspection required under subsection (1) is refused, or default is made in complying with s... |
| `s 807(3)(b) the officer of the company commits an offence` | part22-notice.l4:1186 | failed "if" / "where" / "when" (reading (a)) | If an inspection required under subsection (1) is refused, or default is made in complying with s... |
| `s 807(5) the court may by order compel an immediate inspection or direct that the copy ...` | part22-notice.l4:1208 | failed "if" / "where" / "when" (reading (a)) | In the case of any such refusal or default the court may by order compel an immediate inspection ... |
| `s 808(2) the company entered the information in the register within three days of the r...` | part22-register.l4:44 | other: read the quoted words | A company which receives any such information must, within three days of the receipt, enter in th... |
| `s 808(2)(a) the entry contains the particulars the company must enter` | part22-register.l4:53 | other: read the quoted words | must ... enter in the register— (a) the fact that the requirement was imposed and the date on whi... |
| `s 808(3) the information is entered against the name the subsection requires` | part22-register.l4:84 | other: read the quoted words | The information must be entered against the name of the present holder of the shares in question |
| `s 808(3) the information is entered against the name the subsection requires` | part22-register.l4:87 | failed "if" / "where" / "when" (reading (a)) | or, if there is no present holder or the present holder is not known, against the name of the per... |
| `s 808(4) the register is made up as the subsection requires` | part22-register.l4:96 | other: read the quoted words | The register must be made up so that the entries against the names entered in it appear in chrono... |
| `s 808(5)(a) the company commits an offence` | part22-register.l4:107 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with this section an offence is committed by— (a) the company |
| `s 808(5)(b) the officer of the company commits an offence` | part22-register.l4:116 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with this section an offence is committed by— ... (b) every offic... |
| `s 808(7) the company is affected with notice of, or put upon inquiry as to, the rights ...` | part22-register.l4:137 | flat negative (ruled N2 option A; reading (a) of the brief) | The company is not by virtue of anything done for the purposes of this section affected with noti... |
| `s 809(3) no such notice is required` | part22-register.l4:162 | failed "if" / "where" / "when" (reading (a)) | No such notice is required if the register has at all times been kept available for inspection at... |
| `s 809(2) the company must give notice to the registrar of companies of the place where ...` | part22-register.l4:170 | failed "if" / "where" / "when" (reading (a)) | (3) No such notice is required if the register has at all times been kept available for inspectio... |
| `s 809(4)(a) the company commits an offence` | part22-register.l4:191 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with subsection (1), or a company makes default for 14 days in co... |
| `s 809(4)(b) the officer of the company commits an offence` | part22-register.l4:201 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with subsection (1), or a company makes default for 14 days in co... |
| `s 810(1) the company must keep an index of the names entered in the register` | part22-register.l4:224 | unless / except met (reading (a); fork F5 where the text bars) | Unless the register kept under section 808 ... is kept in such a form as itself to constitute an ... |
| `s 810(2) the company made the entry or alteration in the index within ten days` | part22-register.l4:242 | other: read the quoted words | The company must make any necessary entry or alteration in the index within ten days after the da... |
| `s 810(3) the index is made up as the subsection requires` | part22-register.l4:268 | other: read the quoted words | The index must contain, in respect of each name, a sufficient indication to enable the informatio... |
| `s 810(4) the index is kept as the subsection requires` | part22-register.l4:277 | other: read the quoted words | The index must be at all times kept available for inspection at the same place as the register. |
| `s 810(5)(a) the company commits an offence` | part22-register.l4:288 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with this section, an offence is committed by— (a) the company |
| `s 810(5)(b) the officer of the company commits an offence` | part22-register.l4:297 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with this section, an offence is committed by— ... (b) every offi... |
| `s 811(2) the person is entitled to be provided with a copy of any entry in the register` | part22-register.l4:331 | failed "if" / "where" / "when" (reading (a)) | Any person is entitled, on request and on payment of such fee as may be prescribed, to be provide... |
| `s 811(3) the person has made the request the subsection requires` | part22-register.l4:340 | other: read the quoted words | A person seeking to exercise either of the rights conferred by this section must make a request t... |
| `s 811(4) the request contains the information the subsection requires` | part22-register.l4:374 | failed "if" / "where" / "when" (reading (a)) | The request must contain the following information— (a) in the case of an individual, his name an... |
| `s 812(2) the company must inform the person making the request, stating the reason why ...` | part22-register.l4:400 | failed "if" / "where" / "when" (reading (a)) | If the company refuses the request, it must inform the person making the request, stating the rea... |
| `s 812(4)(a) the person who made the request must notify the company` | part22-register.l4:420 | failed "if" / "where" / "when" (reading (a)) | If an application is made to the court— (a) the person who made the request must notify the company |
| `s 812(4)(b) the company must use its best endeavours to notify any persons whose detail...` | part22-register.l4:428 | failed "if" / "where" / "when" (reading (a)) | If an application is made to the court— ... (b) the company must use its best endeavours to notif... |
| `s 812(5) the court shall direct the company not to comply with the request` | part22-register.l4:437 | failed "if" / "where" / "when" (reading (a)) | If the court is not satisfied that the inspection or copy is sought for a proper purpose, it shal... |
| `s 812(6) the order is made as the subsection requires` | part22-register.l4:456 | other: read the quoted words | The order must contain such provision as appears to the court appropriate to identify the request... |
| `s 812(7) the company must comply with the request immediately upon the court giving its...` | part22-register.l4:465 | failed "if" / "where" / "when" (reading (a)) | If the court does not direct the company not to comply with the request, the company must comply ... |
| `s 813(1)(a) the company commits an offence` | part22-register.l4:479 | failed "if" / "where" / "when" (reading (a)) | If an inspection required under section 811 ... is refused or default is made in providing a copy... |
| `s 813(1)(b) the officer of the company commits an offence` | part22-register.l4:489 | other: read the quoted words | otherwise than in accordance with section 812, an offence is committed by— ... (b) every officer ... |
| `s 813(3) the court may by order compel an immediate inspection or direct that the copy ...` | part22-register.l4:511 | failed "if" / "where" / "when" (reading (a)) | In the case of any such refusal or default the court may by order compel an immediate inspection ... |
| `s 815(1) the deletion of the entry is permitted` | part22-register.l4:572 | unless / except met (reading (a); fork F5 where the text bars) | Entries in the register kept under section 808 ... must not be deleted except in accordance with—... |
| `s 815(2) the company must restore the entry as soon as reasonably practicable` | part22-register.l4:581 | failed "if" / "where" / "when" (reading (a)) | If an entry is deleted in contravention of subsection (1), the company must restore it as soon as... |
| `s 815(3)(a) the company commits an offence` | part22-register.l4:600 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with subsection (1) or (2), an offence is committed by— (a) the c... |
| `s 815(3)(b) the officer of the company commits an offence` | part22-register.l4:609 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with subsection (1) or (2), an offence is committed by— ... (b) e... |
| `s 817(1) this section applies` | part22-register.l4:647 | failed "if" / "where" / "when" (reading (a)) | This section applies where in pursuance of an obligation imposed by a notice under section 793 ..... |
| `s 817(2) that other person may apply to the company for the removal of the entry from t...` | part22-register.l4:656 | failed "if" / "where" / "when" (reading (a)) | This section applies where ... |
| `s 817(3) the company shall remove the entry` | part22-register.l4:665 | failed "if" / "where" / "when" (reading (a)) | If the company is satisfied that the information in pursuance of which the entry was made is inco... |
| `s 818(2) the company shall record that information in every place where his name appear...` | part22-register.l4:696 | failed "if" / "where" / "when" (reading (a)) | If the company is satisfied that he has ceased to be a party to the agreement, it shall record th... |
| `s 819(1) the company must continue to keep the register and any associated index` | part22-register.l4:722 | failed "if" / "where" / "when" (reading (a)) | until the end of the period of six years after it ceased to be such a company |
| `s 819(1) the company must continue to keep the register and any associated index` | part22-register.l4:723 | failed "if" / "where" / "when" (reading (a)) | If a company ceases to be a public company, it must continue to keep any register |
| `s 819(2)(a) the company commits an offence` | part22-register.l4:734 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with this section, an offence is committed by— (a) the company |
| `s 819(2)(b) the officer of the company commits an offence` | part22-register.l4:743 | failed "if" / "where" / "when" (reading (a)) | If default is made in complying with this section, an offence is committed by— ... (b) every offi... |
| `s 829(1) the act is a distribution` | part23-ch1.l4:69 | means (the text's own no; not marginal) | In this Part “distribution” means every description of distribution of a company's assets to its ... |
| `s 829(1) the act is a distribution` | part23-ch1.l4:73 | flat negative (ruled N2 option A; reading (a) of the brief) | The following are not distributions for the purposes of this Part |
| `s 830(1) the distribution is within the profits available for the purpose` | part23-ch1.l4:101 | "only" closes (the text's own no; ruled E1/N2 family) | A company may only make a distribution out of profits available for the purpose. |
| `s 831(1) the distribution is within the net asset restriction` | part23-ch1.l4:131 | failed "if" / "where" / "when" (reading (a)) | A public company may only make a distribution— (a) if the amount of its net assets is not less th... |
| `s 831(5) the company may include uncalled share capital as an asset in any accounts rel...` | part23-ch1.l4:198 | flat negative (ruled N2 option A; reading (a) of the brief) | A public company must not include any uncalled share capital as an asset in any accounts relevant... |
| `s 832(2) the distribution is within the accumulated, realised revenue profits` | part23-ch1.l4:244 | failed "if" / "where" / "when" (reading (a)) | It may make such a distribution only if, and to the extent that, its accumulated, realised revenu... |
| `s 832(3) the distribution is within the asset cover the subsection requires` | part23-ch1.l4:258 | failed "if" / "where" / "when" (reading (a)) | It may make such a distribution only— (a) if the amount of its assets is at least equal to one an... |
| `s 832(5) the further conditions are met` | part23-ch1.l4:305 | flat negative (ruled N2 option A; reading (a) of the brief) | The following conditions must also be met— (a) the company's shares must be shares admitted to tr... |
| `s 832(7) the company may include uncalled share capital as an asset in any accounts rel...` | part23-ch1.l4:313 | flat negative (ruled N2 option A; reading (a) of the brief) | The company must not include any uncalled share capital as an asset in any accounts relevant for ... |
| `s 832(1) the investment company may make the distribution out of its accumulated, reali...` | part23-ch1.l4:329 | failed "if" / "where" / "when" (reading (a)) | An investment company may make a distribution out of its accumulated, realised revenue profits if... |
| `s 833(2)(a) the requirement is met` | part23-ch1.l4:351 | other: read the quoted words | The requirement is— (a) that the business of the company consists of investing its funds in share... |
| `s 833(1) the company is an investment company` | part23-ch1.l4:369 | means (the text's own no; not marginal) | In this Part an “investment company” means a public company that— (a) has given notice (which has... |
| `s 833A(2) the amount is taken to be a realised profit` | part23-ch1.l4:479 | other: read the quoted words | with a positive figure taken to be a realised profit and a negative figure taken to be a realised... |
| `s 833A(7) the company's assets and liabilities are valued as the subsection requires` | part23-ch1.l4:522 | other: read the quoted words | The company’s assets and liabilities must be valued in accordance with— (a) Part 2 of the Insuran... |
| `s 833A(8)(a) this section is applied on the assumption that the company carries on only...` | part23-ch1.l4:534 | failed "if" / "where" / "when" (reading (a)) | If the company carries on both long-term business and other insurance business— (a) this section ... |
| `s 833A(8)(b) the remainder of this Part is applied on the assumption that the company c...` | part23-ch1.l4:542 | failed "if" / "where" / "when" (reading (a)) | If the company carries on both long-term business and other insurance business— ... (b) the remai... |
| `s 833A(9) the scheme is a defined benefit pension scheme` | part23-ch1.l4:570 | means (the text's own no; not marginal) | “defined benefit pension scheme” means a pension scheme (as defined by section 1(5) of the Pensio... |
| `s 833A(9) the business is long-term business` | part23-ch1.l4:578 | means (the text's own no; not marginal) | “long-term business” means business that consists of effecting or carrying out contracts of long-... |
| `s 833A(9) the undertaking is a qualifying investment subsidiary` | part23-ch1.l4:587 | means (the text's own no; not marginal) | “qualifying investment subsidiary” means an undertaking in which the company holds a participatio... |
| `s 833A(9) the instrument is the Solvency 2 Directive` | part23-ch1.l4:595 | means (the text's own no; not marginal) | “Solvency 2 Directive” means Directive 2009/138/EC of the European Parliament and of the Council ... |
| `s 836(2)(a) the distribution may be justified by reference to interim accounts` | part23-ch2.l4:65 | failed "if" / "where" / "when" (reading (a)) | where the distribution would be found to contravene this Part by reference to the company's last ... |
| `s 836(2)(b) the distribution may be justified by reference to initial accounts` | part23-ch2.l4:74 | failed "if" / "where" / "when" (reading (a)) | where the distribution is proposed to be declared during the company's first accounting reference... |
| `s 836(4) the accounts may not be relied on for the purposes of this Part and the distri...` | part23-ch2.l4:112 | failed "if" / "where" / "when" (reading (a)) | If any applicable requirement of those sections is not complied with, the accounts may not be rel... |
| `s 837(1) the accounts are the company's last annual accounts` | part23-ch2.l4:125 | means (the text's own no; not marginal) | The company's last annual accounts means the company's individual accounts |
| `s 837(2) the accounts were prepared as the subsection requires` | part23-ch2.l4:136 | "only" closes (the text's own no; ruled E1/N2 family) | The accounts must have been properly prepared in accordance with this Act, or have been so prepar... |
| `s 837(3) the audit requirement is met` | part23-ch2.l4:146 | unless / except met (reading (a); fork F5 where the text bars) | Unless the company is exempt from audit and the directors take advantage of that exemption, the a... |
| `s 837(4) the requirements as to a qualified report are met` | part23-ch2.l4:163 | other: read the quoted words | (a) the auditor must have stated in writing (either at the time of his report or subsequently) wh... |
| `s 837(4) the requirements as to a qualified report are met` | part23-ch2.l4:164 | failed "if" / "where" / "when" (reading (a)) | (b) a copy of that statement must— ... (ii) in the case of a public company, have been laid befor... |
| `s 838(1) the interim accounts are accounts of the kind the subsection requires` | part23-ch2.l4:185 | other: read the quoted words | Interim accounts must be accounts that enable a reasonable judgment to be made as to the amounts ... |
| `s 838(2) the requirements of subsections (3) to (6) apply` | part23-ch2.l4:195 | failed "if" / "where" / "when" (reading (a)) | Where interim accounts are prepared for a proposed distribution by a public company, the followin... |
| `s 838(3) the interim accounts were prepared as the subsection requires` | part23-ch2.l4:213 | flat negative (ruled N2 option A; reading (a) of the brief) | The accounts must have been properly prepared, or have been so prepared subject to matters that a... |
| `s 838(6) the accounts were delivered to the registrar as the subsection requires` | part23-ch2.l4:231 | other: read the quoted words | A copy of the accounts must have been delivered to the registrar. |
| `s 839(1) the initial accounts are accounts of the kind the subsection requires` | part23-ch2.l4:243 | other: read the quoted words | Initial accounts must be accounts that enable a reasonable judgment to be made as to the amounts ... |
| `s 839(2) the requirements of subsections (3) to (7) apply` | part23-ch2.l4:253 | failed "if" / "where" / "when" (reading (a)) | Where initial accounts are prepared for a proposed distribution by a public company, the followin... |
| `s 839(3) the initial accounts were prepared as the subsection requires` | part23-ch2.l4:271 | flat negative (ruled N2 option A; reading (a) of the brief) | The accounts must have been properly prepared, or have been so prepared subject to matters that a... |
| `s 839(5) the auditor's report was made as the subsection requires` | part23-ch2.l4:281 | other: read the quoted words | The company's auditor must have made a report stating whether, in his opinion, the accounts have ... |
| `s 839(6) the requirements as to a qualified report are met` | part23-ch2.l4:295 | other: read the quoted words | (a) the auditor must have stated in writing ... whether in his opinion the matters ... are materi... |
| `s 839(7) the documents were delivered to the registrar as the subsection requires` | part23-ch2.l4:305 | other: read the quoted words | A copy of the accounts, of the auditor's report and of any auditor's statement must have been del... |
| `s 840(2) the financial assistance or payment is relevant for the purposes of subsection...` | part23-ch2.l4:334 | failed "if" / "where" / "when" (reading (a)) | financial assistance given by the company in contravention of section 678 or 679 (prohibited fina... |
| `s 840(2) the financial assistance or payment is relevant for the purposes of subsection...` | part23-ch2.l4:337 | unless / except met (reading (a); fork F5 where the text bars) | except a payment lawfully made otherwise than out of distributable profits |
| `s 841(3) the provision is a revaluation provision` | part23-ch3.l4:32 | means (the text's own no; not marginal) | A “revaluation provision” means a provision in respect of a diminution in value of a fixed asset ... |
| `s 841(2) the provision is treated as a realised loss` | part23-ch3.l4:44 | unless / except met (reading (a); fork F5 where the text bars) | provisions of a kind specified ... (except revaluation provisions) |
| `s 841(4) the consideration by the directors of the value of a fixed asset is treated as...` | part23-ch3.l4:70 | failed "if" / "where" / "when" (reading (a)) | any consideration by the directors of the value at a particular time of a fixed asset is treated ... |
| `s 843(1) the provisions of this section have effect in relation to the company` | part23-ch3.l4:117 | other: read the quoted words | other than— (a) a person to whom section 833A applies; or (b) an insurance special purpose vehicle |
| `s 843(3)(a) the part of the balance sheet is the relevant part` | part23-ch3.l4:145 | other: read the quoted words | the relevant part of the balance sheet is that part of the balance sheet that represents accumula... |
| `s 843(5) the profit or loss is left out of account` | part23-ch3.l4:175 | other: read the quoted words | Subject to subsections (2) and (4), any profit or loss arising in the company's long-term busines... |
| `s 843(6) the investigation is an actuarial investigation` | part23-ch3.l4:194 | means (the text's own no; not marginal) | an “actuarial investigation” means an investigation made into the financial condition of an autho... |
| `s 843(7) the business is long-term business` | part23-ch3.l4:204 | means (the text's own no; not marginal) | In this section “long-term business” means business that consists of effecting or carrying out co... |
| `s 843(8) the vehicle is an insurance special purpose vehicle` | part23-ch3.l4:213 | means (the text's own no; not marginal) | In this section “ insurance special purpose vehicle ” means a special purpose vehicle within the ... |
| `s 844(3) subsection (1) does not apply` | part23-ch3.l4:247 | failed "if" / "where" / "when" (reading (a)) | Subsection (1) does not apply if— (a) there are special circumstances ..., (b) it is stated ... t... |
| `s 844(3) subsection (1) does not apply` | part23-ch3.l4:249 | failed "if" / "where" / "when" (reading (a)) | (ii) in the case of IAS accounts, in any note to the accounts |
| `s 844(3) subsection (1) does not apply` | part23-ch3.l4:253 | failed "if" / "where" / "when" (reading (a)) | (i) in the case of Companies Act accounts, in the note required by regulations under section 396 ... |
| `s 844(1)(a) the amount shown or included in respect of the development costs is treated...` | part23-ch3.l4:268 | failed "if" / "where" / "when" (reading (a)) | Where development costs are shown or included as an asset in a company's accounts, any amount sho... |
| `s 844(1)(a) the amount shown or included in respect of the development costs is treated...` | part23-ch3.l4:269 | other: read the quoted words | This is subject to the following exceptions. |
| `s 844(1)(b) the amount shown or included in respect of the development costs is treated...` | part23-ch3.l4:279 | failed "if" / "where" / "when" (reading (a)) | Where development costs are shown or included as an asset in a company's accounts, any amount sho... |
| `s 844(1)(b) the amount shown or included in respect of the development costs is treated...` | part23-ch3.l4:280 | other: read the quoted words | This is subject to the following exceptions. |
| `s 845(1) this section applies for determining the amount of the distribution` | part23-ch3.l4:300 | failed "if" / "where" / "when" (reading (a)) | This section applies for determining the amount of a distribution consisting of or including, or ... |
| `s 846(1) this section applies` | part23-ch3.l4:355 | failed "if" / "where" / "when" (reading (a)) | This section applies where— (a) a company makes a distribution consisting of or including ... a n... |
| `s 846(2)(b) that profit is treated as a realised profit for the purpose of applying tha...` | part23-ch3.l4:372 | failed "if" / "where" / "when" (reading (a)) | This section applies where ... |
| `s 847(2) what the member is liable to do` | part23-ch3.l4:397 | failed "if" / "where" / "when" (reading (a)) | This section applies where a distribution, or part of one, made by a company to one of its member... |
| `s 847(2) what the member is liable to do` | part23-ch3.l4:398 | flat negative (ruled N2 option A; reading (a) of the brief) | This section does not apply in relation to— (a) financial assistance given by a company in contra... |
| `s 847(2) what the member is liable to do` | part23-ch3.l4:399 | failed "if" / "where" / "when" (reading (a)) | If at the time of the distribution the member knows or has reasonable grounds for believing that ... |
| `s 848(1) that provision continues as authority for those profits to be so applied after...` | part23-ch3.l4:433 | failed "if" / "where" / "when" (reading (a)) | Where immediately before the relevant date a company was authorised by a provision of its article... |
| `s 849 the company may apply the profit in paying up debentures or any amounts unpaid on...` | part23-ch3.l4:446 | flat negative (ruled N2 option A; reading (a) of the brief) | A company must not apply an unrealised profit in paying up debentures or any amounts unpaid on it... |
| `s 850(1) the directors may treat the profit as realised` | part23-ch3.l4:481 | failed "if" / "where" / "when" (reading (a)) | Where the directors of a company are, after making all reasonable enquiries, unable to determine ... |
| `s 850(2) the directors may treat the loss as unrealised` | part23-ch3.l4:493 | failed "if" / "where" / "when" (reading (a)) | Where the directors of a company, after making all reasonable enquiries, are unable to determine ... |
| `s 851(1) the provisions of this Part are without prejudice to the rule of law` | part23-ch3.l4:504 | unless / except met (reading (a); fork F5 where the text bars) | Except as provided in this section, the provisions of this Part are without prejudice to any rule... |
| `s 853(2)(a) the profit or loss is within the reference, whenever it was made` | part23-ch3.l4:560 | other: read the quoted words | References to profit or losses of any description— (a) are to profits or losses of that descripti... |
| `s 853(2)(b) the profit or loss is within the reference` | part23-ch3.l4:570 | other: read the quoted words | are to profits or losses of a revenue or capital character |
| `s 853(3) the operation is capitalisation` | part23-ch3.l4:587 | means (the text's own no; not marginal) | “Capitalisation”, in relation to a company's profits, means any of the following operations (when... |
| `s 853(4) the profit or loss is a realised profit or loss in relation to the company's a...` | part23-ch3.l4:596 | failed "if" / "where" / "when" (reading (a)) | References to “realised profits” and “realised losses”, in relation to a company's accounts, are ... |
| `s 853(6) the asset is a fixed asset` | part23-ch3.l4:617 | means (the text's own no; not marginal) | “Fixed assets” means assets of a company which are intended for use on a continuing basis in the ... |
| `s 853A(4) the confirmation date is no later than the last day of the review period conc...` | part24.l4:57 | flat negative (ruled N2 option A; reading (a) of the brief) | The confirmation date of a confirmation statement must be no later than the last day of the revie... |
| `s 853A(1) the confirmation statement was delivered before the end of the period of 14 d...` | part24.l4:96 | other: read the quoted words | Every company must, before the end of the period of 14 days after the end of each review period, ... |
| `s 853A(1)(a) the company delivered the information necessary to make the confirmation s...` | part24.l4:120 | other: read the quoted words | Every company must ... deliver to the registrar— (a) such information as is necessary to ensure t... |
| `s 853A(1)(b) the confirmation statement confirms what the paragraph requires` | part24.l4:134 | failed "if" / "where" / "when" (reading (a)) | a statement (a “confirmation statement”) confirming— (i) that the company has delivered ... all o... |
| `s 853A(7) the company is entitled to assume that information that has been delivered to...` | part24.l4:142 | unless / except met (reading (a); fork F5 where the text bars) | a company is entitled to assume that information that has been delivered to the registrar has bee... |
| `s 853BA the company must deliver at the same time a statement that the intended future ...` | part24.l4:190 | failed "if" / "where" / "when" (reading (a)) | Where a company makes a confirmation statement it must at the same time deliver to the registrar ... |
| `s 853C(1) this section applies` | part24.l4:212 | failed "if" / "where" / "when" (reading (a)) | This section applies where— (a) a company makes a confirmation statement, and (b) there has been ... |
| `s 853C(1A) this section also applies` | part24.l4:224 | failed "if" / "where" / "when" (reading (a)) | This section also applies where— (a) a company makes its first confirmation statement, and (b) by... |
| `s 853C(2) the company must give notice to the registrar of the change at the same time ...` | part24.l4:235 | failed "if" / "where" / "when" (reading (a)) | (1) This section applies where ... |
| `s 853CA(1) this section applies` | part24.l4:271 | failed "if" / "where" / "when" (reading (a)) | This section applies where— (a) a company makes a confirmation statement, (b) the company’s regis... |
| `s 853CB(1) this section applies` | part24.l4:304 | failed "if" / "where" / "when" (reading (a)) | This section applies where— (a) a company makes a confirmation statement, (b) the company’s regis... |
| `s 853D(1) this section applies` | part24.l4:331 | failed "if" / "where" / "when" (reading (a)) | This section applies where a company having a share capital makes a confirmation statement. |
| `s 853D(2) the company must deliver a statement of capital to the registrar at the same ...` | part24.l4:341 | failed "if" / "where" / "when" (reading (a)) | This section applies where a company having a share capital makes a confirmation statement. |
| `s 853D(2) the company must deliver a statement of capital to the registrar at the same ...` | part24.l4:342 | failed "if" / "where" / "when" (reading (a)) | (3) Subsection (2) does not apply if there has been no change in any of the matters required to b... |
| `s 853D(4) the statement of capital states what the subsection requires with respect to ...` | part24.l4:379 | failed "if" / "where" / "when" (reading (a)) | The statement of capital must state with respect to the company's share capital at the confirmati... |
| `s 853E(1) this section applies` | part24.l4:391 | failed "if" / "where" / "when" (reading (a)) | This section applies where a company having a share capital makes a confirmation statement. |
| `s 853E(6) the issuer is a DTR5 issuer` | part24.l4:405 | means (the text's own no; not marginal) | “DTR5 issuer” means an issuer to which Chapter 5 of the Disclosure Rules and Transparency Rules s... |
| `s 853E(6) the market is a relevant market` | part24.l4:415 | means (the text's own no; not marginal) | “relevant market” means— (a) a recognised investment exchange ..., and (b) any other market which... |
| `s 853E(5) both conditions were satisfied throughout the confirmation period concerned` | part24.l4:427 | other: read the quoted words | The conditions are that— (a) there were shares of the company which were shares admitted to tradi... |
| `s 853E(2) the company must deliver to the registrar a statement dealing with the matter...` | part24.l4:457 | failed "if" / "where" / "when" (reading (a)) | This section applies where a company having a share capital makes a confirmation statement. |
| `s 853E(2) the company must deliver to the registrar a statement dealing with the matter...` | part24.l4:458 | failed "if" / "where" / "when" (reading (a)) | (3) Subsection (2) does not apply if and to the extent that the last statement delivered to the r... |
| `s 853F(2) the company is a non-traded company` | part24.l4:478 | other: read the quoted words | A “non-traded company” is a company none of whose shares were, at any time during the confirmatio... |
| `s 853F(1) this section applies` | part24.l4:490 | failed "if" / "where" / "when" (reading (a)) | This section applies where— (a) a non-traded company makes a confirmation statement, ... |
| `s 853F(3) the company must deliver the information falling within subsection (5) to the...` | part24.l4:501 | failed "if" / "where" / "when" (reading (a)) | This section applies where— (a) a non-traded company makes a confirmation statement |
| `s 853F(3) the company must deliver the information falling within subsection (5) to the...` | part24.l4:502 | failed "if" / "where" / "when" (reading (a)) | (4) Subsection (3) does not apply if and to the extent that the information most recently deliver... |
| `s 853F(5) the information delivered is the information the subsection requires` | part24.l4:531 | other: read the quoted words | The information is— (a) the name ... of every person who was at any time during the confirmation ... |
| `s 853G(2) the company is a traded company` | part24.l4:555 | other: read the quoted words | A “traded company” is a company any of whose shares were, at any time during the confirmation per... |
| `s 853G(2) the company is a traded company` | part24.l4:556 | failed "if" / "where" / "when" (reading (a)) | (3) But a company is not a traded company if throughout the confirmation period concerned— (a) th... |
| `s 853G(1) this section applies` | part24.l4:566 | failed "if" / "where" / "when" (reading (a)) | This section applies where a traded company makes a confirmation statement. |
| `s 853G(4) the company must deliver the information falling within subsection (6) to the...` | part24.l4:577 | failed "if" / "where" / "when" (reading (a)) | This section applies where a traded company makes a confirmation statement. |
| `s 853G(4) the company must deliver the information falling within subsection (6) to the...` | part24.l4:578 | failed "if" / "where" / "when" (reading (a)) | (5) Subsection (4) does not apply if and to the extent the information most recently delivered to... |
| `s 853G(6) the information delivered is the information the subsection requires` | part24.l4:610 | other: read the quoted words | The information is— (a) the name and address ... of each person who ... held at least 5% ..., and... |
| `s 853H(1) this section applies` | part24.l4:621 | failed "if" / "where" / "when" (reading (a)) | This section applies where a company ... to which Part 21A does not apply (information about peop... |
| `s 853H(2) the company must deliver to the registrar a statement of the fact that it is ...` | part24.l4:635 | failed "if" / "where" / "when" (reading (a)) | This section applies where a company ... to which Part 21A does not apply ... makes a confirmatio... |
| `s 853H(2) the company must deliver to the registrar a statement of the fact that it is ...` | part24.l4:636 | failed "if" / "where" / "when" (reading (a)) | (3) Subsection (2) does not apply if the last statement delivered to the registrar under this sec... |
| `s 853H(2A) the statement under subsection (2) specifies what the subsection requires` | part24.l4:662 | other: read the quoted words | The statement under subsection (2) must specify— (a) whether the company falls within the descrip... |
| `s 853H(2A) the statement under subsection (2) specifies what the subsection requires` | part24.l4:667 | failed "if" / "where" / "when" (reading (a)) | (b) if it falls within a description specified in regulations under section 790B(1)(b), what that... |
| `s 853L(1) the company has failed to deliver a confirmation statement before the end of ...` | part24.l4:699 | failed "if" / "where" / "when" (reading (a)) | If a company fails to deliver a confirmation statement before the end of the period of 14 days af... |
| `s 853L(1) the company has failed to deliver a confirmation statement before the end of ...` | part24.l4:704 | failed "if" / "where" / "when" (reading (a)) | If a company fails to deliver a confirmation statement before the end of the period of 14 days af... |
| `s 853L(1)(b) the officer of the company commits an offence` | part24.l4:719 | failed "if" / "where" / "when" (reading (a)) | If a company fails to deliver a confirmation statement before the end of the period of 14 days ..... |
| `s 853L(3) the contravention continues` | part24.l4:761 | failed "if" / "where" / "when" (reading (a)) | The contravention continues until such time as a confirmation statement specifying a confirmation... |
| `s 853L(5) the officer commits an offence in relation to the continued contravention` | part24.l4:773 | failed "if" / "where" / "when" (reading (a)) | In the case of continued contravention, an offence is also committed by every officer of the comp... |

### Branches that answer `NOTHING` because the text limits the grant or prohibition in its own words (89)

| function | file:line | quoted words |
| --- | --- | --- |
| `s 820(2)(b) the restraint or restriction is disregarded` | part22-interest.l4:48 | any restraints or restrictions to which the exercise of any right attached to the interest is or ... |
| `s 820(7) the persons are treated as each having that interest` | part22-interest.l4:124 | Persons having a joint interest are treated as each having that interest. |
| `s 820(8) it is immaterial that the shares are unidentifiable` | part22-interest.l4:133 | It is immaterial that shares in which a person has an interest are unidentifiable. |
| `s 821(1) section 793 applies in relation to the person as it applies to a person who is...` | part22-interest.l4:144 | Section 793 ... applies in relation to a person who has, or previously had, or is or was entitled... |
| `s 821(2) references in section 793 to an interest in shares are read as including the r...` | part22-interest.l4:153 | References in that section to an interest in shares shall be read accordingly |
| `s 822(1) the person is taken to be interested in the shares` | part22-interest.l4:168 | a person is taken to be interested in shares in which— (a) his spouse or civil partner, or (b) an... |
| `s 822(2) the person is an infant` | part22-interest.l4:182 | In relation to Scotland |
| `s 824(1) an interest in shares may arise from the agreement` | part22-interest.l4:237 | an interest in shares may arise from an agreement between two or more persons that includes provi... |
| `s 824(4) it is immaterial to the continued application of this section whether the circ...` | part22-interest.l4:300 | This applies irrespective of— (a) ... (b) ... (c) ... |
| `s 824(5) the reference has a corresponding meaning` | part22-interest.l4:339 | References elsewhere in this Part to an agreement to which this section applies have a correspond... |
| `s 824(6)(a) this section does not apply to the agreement` | part22-interest.l4:350 | This section does not apply— (a) to an agreement that is not legally binding |
| `s 824(6)(b) this section does not apply to the agreement` | part22-interest.l4:360 | This section does not apply— ... (b) to an agreement to underwrite or sub-underwrite an offer of ... |
| `s 825(1) the person is treated as interested in the shares` | part22-interest.l4:379 | each party to an agreement to which section 824 applies is treated as interested in all shares in... |
| `s 827 a day that is not a working day is disregarded in reckoning the period` | part22-interest.l4:463 | Where the period allowed by any provision of this Part for fulfilling an obligation is expressed ... |
| `s 792(2) a suspension of voting rights affects the application of this Part to interest...` | part22-notice.l4:70 | The temporary suspension of voting rights |
| `s 793(1) the company may give notice to the person` | part22-notice.l4:85 | to any person whom the company knows or has reasonable cause to believe |
| `s 793(2)(a) the notice may require the person to confirm that fact or to state whether ...` | part22-notice.l4:109 | The notice may require the person |
| `s 793(2)(b) the notice may require the person to give further information` | part22-notice.l4:117 | (b) if he holds, or has during that time held, any such interest, to give such further information |
| `s 793(3) the notice may require the person to give particulars of his own present or pa...` | part22-notice.l4:126 | (held by him at any time during the three year period mentioned in subsection (1)(b)) |
| `s 793(5) the particulars referred to in subsections (3) and (4) include` | part22-notice.l4:164 | The particulars referred to in subsections (3) and (4) |
| `s 793(7) the information required by the notice was given within the time specified` | part22-notice.l4:185 | within such reasonable time as may be specified in the notice |
| `s 794(2) the court may direct that acts set out in the order shall not constitute a bre...` | part22-notice.l4:233 | If the court is satisfied that such an order may unfairly affect the rights of third parties in r... |
| `s 795(1)(a) the person commits an offence by failing to comply with the notice` | part22-notice.l4:275 | A person who— (a) fails to comply with a notice under section 793 ... commits an offence |
| `s 795(1)(b) the person commits an offence by a false statement in purported compliance ...` | part22-notice.l4:289 | A person who— ... (b) in purported compliance with such a notice— (i) makes a statement that he k... |
| `s 795(3) the penalty on conviction` | part22-notice.l4:310 | (b) on summary conviction— (i) in England and Wales ... (ii) in Scotland or Northern Ireland |
| `s 796(1) the person is not obliged to comply with a notice under section 793` | part22-notice.l4:321 | if he is for the time being exempted |
| `s 797(1)(a) any transfer of the shares is void` | part22-notice.l4:369 | The effect of an order under section 794 that shares are subject to restrictions is as follows |
| `s 797(1)(b) no voting rights are exercisable in respect of the shares` | part22-notice.l4:380 | The effect of an order under section 794 that shares are subject to restrictions is as follows |
| `s 797(1)(c) no further shares may be issued in right of the shares or in pursuance of a...` | part22-notice.l4:391 | The effect of an order under section 794 that shares are subject to restrictions is as follows |
| `s 797(1)(d) no payment may be made of sums due from the company on the shares` | part22-notice.l4:403 | The effect of an order under section 794 that shares are subject to restrictions is as follows |
| `s 797(3) an agreement to transfer any such right is void` | part22-notice.l4:436 | an agreement to transfer any right to be issued with other shares in right of those shares, or to... |
| `s 797(4) the provisions of section 797 are displaced for the act` | part22-notice.l4:453 | The provisions of this section are subject— (a) to any directions ... (b) in the case of an inter... |
| `s 798(2)(a) the person commits an offence by exercising a right to dispose` | part22-notice.l4:489 | A person commits an offence if he— (a) exercises or purports to exercise any right— (i) to dispos... |
| `s 798(2)(b) the person commits an offence by voting or appointing a proxy` | part22-notice.l4:501 | A person commits an offence if he— ... (b) votes in respect of any such shares (whether as holder... |
| `s 798(2)(c) the holder commits an offence by failing to notify the restrictions` | part22-notice.l4:520 | A person commits an offence if he— ... (c) being the holder of any such shares, fails to notify o... |
| `s 798(2)(d) the person commits an offence by entering into a void agreement` | part22-notice.l4:531 | A person commits an offence if he— ... (d) being the holder of any such shares, or being entitled... |
| `s 798(5) the provisions of section 798 are displaced for the act` | part22-notice.l4:584 | The provisions of this section are subject— (a) to any directions ..., and (b) in the case of an ... |
| `s 799(1) an application may be made to the court on that ground` | part22-notice.l4:596 | An application may be made to the court on the ground that |
| `s 799(3) the court may direct that acts set out in the order do not constitute a breach...` | part22-notice.l4:615 | If the court is satisfied that the application is well-founded, it may |
| `s 800(4) the order may continue the restrictions` | part22-notice.l4:669 | An order under this section made by virtue of subsection (3)(b) may continue, in whole or in part... |
| `s 801(1) the court may order that the shares subject to restrictions be sold, subject t...` | part22-notice.l4:699 | The court may order that the shares subject to restrictions be sold |
| `s 802(1) the sum to be paid into court for the benefit of the persons who are beneficia...` | part22-notice.l4:756 | Where shares are sold in pursuance of an order of the court under section 801 |
| `s 802(2) the person may apply to the court for the whole or part of those proceeds to b...` | part22-notice.l4:765 | A person who is beneficially interested in the shares may apply |
| `s 803(1) the persons may require the company to exercise its powers under section 793` | part22-notice.l4:808 | The members of a company may require it to exercise its powers |
| `s 808(1) the company must keep a register of the information received` | part22-register.l4:25 | a register of information received by it in pursuance of a requirement imposed under section 793 |
| `s 808(7) the company is affected with notice of, or put upon inquiry as to, the rights ...` | part22-register.l4:138 | by virtue of anything done for the purposes of this section |
| `s 811(1) the document must be open to inspection by any person without charge` | part22-register.l4:321 | The register required to be kept under section 808 ..., and any associated index, must be open to... |
| `s 812(3) the person may apply to the court` | part22-register.l4:409 | A person whose request is refused may apply to the court. |
| `s 812(6) the court may direct that the company is not to comply with any such request` | part22-register.l4:448 | If the court makes such a direction and it appears to the court that the company is or may be sub... |
| `s 814(1) the person commits an offence by a misleading, false or deceptive statement in...` | part22-register.l4:523 | It is an offence for a person knowingly or recklessly to make in a request under section 811 ... ... |
| `s 814(2) the person commits an offence by disclosing the information` | part22-register.l4:541 | It is an offence for a person in possession of information obtained by exercise of either of the ... |
| `s 814(3) the penalty on conviction` | part22-register.l4:558 | (b) on summary conviction— (i) in England and Wales ... (ii) in Scotland or Northern Ireland |
| `s 816 the company may remove the entry from the register` | part22-register.l4:636 | A company may remove an entry from the register kept under section 808 ... if more than six years... |
| `s 817(4) the applicant may apply to the court for an order directing the company to rem...` | part22-register.l4:675 | If an application under subsection (3) is refused, the applicant may apply to the court for an or... |
| `s 818(1) the person may apply to the company for the inclusion of that information in t...` | part22-register.l4:687 | If a person who is identified in the register ... as being a party to an agreement to which secti... |
| `s 818(3) the applicant may apply to the court for an order directing the company to inc...` | part22-register.l4:707 | If an application under this section is refused (otherwise than on the ground that the informatio... |
| `s 830(3) subsection (2) has effect subject to sections 832, 833A and 835` | part23-ch1.l4:110 | Subsection (2) has effect subject to sections 832 , 833A and 835 (investment companies and Solven... |
| `s 831(1) the distribution is within the net asset restriction` | part23-ch1.l4:127 | A public company may only make a distribution |
| `s 831(5) the company may include uncalled share capital as an asset in any accounts rel...` | part23-ch1.l4:199 | A public company must not include |
| `s 831(6) subsection (1) has effect subject to sections 832 and 835` | part23-ch1.l4:208 | Subsection (1) has effect subject to sections 832 and 835 (investment companies etc: distribution... |
| `s 832(1) the investment company may make the distribution out of its accumulated, reali...` | part23-ch1.l4:328 | An investment company may make a distribution |
| `s 833(4) the notice to the registrar of intention to carry on business as an investment...` | part23-ch1.l4:380 | Notice to the registrar under this section may be revoked at any time by the company on giving no... |
| `s 833(5) the company ceases to be an investment company` | part23-ch1.l4:388 | On giving such a notice, the company ceases to be such a company. |
| `s 833A(1) this section applies in relation to the company` | part23-ch1.l4:404 | This section applies in relation to any authorised insurance company carrying on long-term busine... |
| `s 836(2) the relevant accounts are the company's last annual accounts` | part23-ch2.l4:84 | The relevant accounts are the company's last annual accounts, except that ... it may be justified... |
| `s 837(5) the auditor's statement is sufficient for the purposes of a distribution` | part23-ch2.l4:174 | An auditor's statement is sufficient for the purposes of a distribution if it relates to distribu... |
| `s 841(5) the amount treated as a realised profit made over that period` | part23-ch3.l4:85 | Where— (a) on the revaluation of a fixed asset, an unrealised profit is shown to have been made, ... |
| `s 842 the cost of the asset taken for the purposes of determining profit or loss` | part23-ch3.l4:101 | In determining ... whether a company has made a profit or loss in respect of an asset where— (a) ... |
| `s 843(1) the provisions of this section have effect in relation to the company` | part23-ch3.l4:116 | as it applies in relation to an authorised insurance company carrying on long-term business |
| `s 843(2) the amount is treated as a realised profit` | part23-ch3.l4:134 | An amount included in the relevant part of the company's balance sheet that— (a) represents a sur... |
| `s 843(5) the profit or loss is left out of account` | part23-ch3.l4:174 | any profit or loss arising in the company's long-term business is to be left out of account |
| `s 844(2) subsection (1) does not apply to the part of the amount` | part23-ch3.l4:225 | Subsection (1) does not apply to any part of that amount representing an unrealised profit made o... |
| `s 845(5) the provisions of Chapter 2 have effect subject to this section` | part23-ch3.l4:341 | The provisions of Chapter 2 ... have effect subject to this section |
| `s 847(3) the obligation imposed apart from this section is unaffected` | part23-ch3.l4:410 | This is without prejudice to any obligation imposed apart from this section on a member of a comp... |
| `s 848(1) that provision continues as authority for those profits to be so applied after...` | part23-ch3.l4:434 | that provision continues (subject to any alteration of the articles) |
| `s 849 the company may apply the profit in paying up debentures or any amounts unpaid on...` | part23-ch3.l4:447 | A company must not apply an unrealised profit |
| `s 851(1) the provisions of this Part are without prejudice to the rule of law` | part23-ch3.l4:506 | any rule of law restricting the sums out of which, or the cases in which, a distribution may be made |
| `s 851(2)(a) section 845 applies to determine the amount of the distribution or return o...` | part23-ch3.l4:518 | For the purposes of any rule of law requiring distributions to be paid out of profits or restrict... |
| `s 851(2)(b) section 846 applies as it applies for the purposes of this Part` | part23-ch3.l4:526 | For the purposes of any rule of law requiring distributions to be paid out of profits or restrict... |
| `s 851(3) the reference is to amounts regarded as distributions for the purposes of the ...` | part23-ch3.l4:535 | In this section references to distributions are to amounts regarded as distributions for the purp... |
| `s 852 the provisions of this Part are without prejudice to the restriction` | part23-ch3.l4:547 | any enactment, or any provision of a company's articles, restricting the sums out of which, or th... |
| `s 853(2)(b) the profit or loss is within the reference` | part23-ch3.l4:568 | except where the context otherwise requires |
| `s 853(5) subsection (4) is without prejudice to the matter` | part23-ch3.l4:608 | Subsection (4) is without prejudice to— (a) the construction of any other expression ..., (b) any... |
| `s 853B the duty is a duty to notify a relevant event` | part24.l4:177 | (h) in the case of a company which, in accordance with regulations under section 1136, keeps any ... |
| `s 853C(3) the information may be given by reference to one or more categories of the sy...` | part24.l4:253 | may be given by reference to one or more categories of any prescribed system of classifying busin... |
| `s 853F(6) the registrar may impose the requirement` | part24.l4:540 | The registrar may impose requirements about the form in which information of the kind mentioned i... |
| `s 853G(6)(a) the person is a person whose name and address must be delivered` | part24.l4:601 | each person who, at the end of the confirmation date concerned, held at least 5% of the issued sh... |
| `s 853L(2) the penalty on summary conviction` | part24.l4:753 | on summary conviction— (a) in England and Wales ... (b) in Scotland or Northern Ireland |
| `s 853L(6) the fine for each day on which the contravention continues and the person is ...` | part24.l4:786 | (6) A person guilty of an offence under subsection (5) is liable on summary conviction— (a) in En... |

### Reading a result: FALSE and NOTHING (coa18)

This section says the rule of 2026-10-29 in the terms of this subject, which is about who may require information about shares, what a company may distribute and what it must file.

- **`JUST FALSE` ("no") means the text itself says no to the case in its own words.**
  Here that is, for example: a private company is outside Part 22 ("This Part applies only to public companies", s 791); a person who proves the requirement was frivolous or vexatious does not commit the offence of failing to comply (s 795(2)); a distribution above the profits available for the purpose is not allowed ("may only", s 830(1)); a company that delivered its confirmation statement within 14 days after the review period has not failed to deliver it (s 853L(1)).
- **`NOTHING` ("not covered") means the text does not decide the case on these facts.**
  Here that is, for example: a private company asked about the net asset restriction (s 831(1) speaks of public companies only and does not say what applies to others); a person who did none of the listed things in s 798(2) (the text says what the described person commits and says nothing of anyone else); a conviction on indictment under s 853L(2) (the penalty is divided by place of summary conviction); an officer whose "default" is a seam answer that is itself `NOTHING` (s 1121).
- **A caller must never turn `NOTHING` into `FALSE`.** `NOTHING` is not "no": it is "the Act, in these provisions, is silent on this".
- **The seat layer passes both through**: a question that answers true says "the Act says yes", false says "the Act says no", and null says "the Act, in this Part, does not decide it", never "no".
- **A `NOTHING` that comes from a seam** (an input another part of the Act answers: whether an officer is "in default", whether accounts are properly prepared under s 396) means "not known from this Part"; supply the answering part's answer and the question can be answered.
- **Amounts and periods the Act leaves to others are inputs**: the pounds a level on the standard scale stands for, a prescribed fee, which days are not working days.

## Seams (coa18)

A seam is an answer another part of the Act gives, taken here as an input named for the section it comes from (PLAN.md section 4); the lead wires the answering part's function to it at the merge.
Seams are taken as inputs and never imported: no coa18 module imports another part.

| input (as named in the code) | type | asked by (module) |
| --- | --- | --- |
| `s 4(2) the company is a public company` | BOOLEAN | part22-notice, part23-ch1, part23-ch2 |
| `s 9(5)(c) by the time of its incorporation the company's principal business activities had changed from those specified in the statement under sect...` | BOOLEAN | part24 |
| `s 86(2) the company's registered office is at an appropriate address within the meaning given by section 86(2)` | BOOLEAN | part24 |
| `s 87 the company has given a notice under section 87 (change of registered office) that is awaiting registration by the registrar` | BOOLEAN | part24 |
| `s 88A(2) the company's registered email address is an appropriate email address within the meaning given by section 88A(2)` | BOOLEAN | part24 |
| `s 88B the company has given a notice under section 88B (change of registered email address) that is awaiting registration by the registrar` | BOOLEAN | part24 |
| `s 251 the person is a shadow director` | MAYBE BOOLEAN | part24 |
| `s 396 a provision of regulations under section 396 provides that only realised profits are to be included in or transferred to the profit and loss ...` | MAYBE BOOLEAN | part23-ch3 |
| `s 396 the accounts are prepared in accordance with sections 395 to 397 (requirements for company individual accounts), applying those requirements ...` | MAYBE BOOLEAN | part23-ch2 |
| `s 396 the provision is of a kind specified for the purposes of section 831(3) by regulations under section 396` | MAYBE BOOLEAN | part23-ch1 |
| `s 396 the provision is of a kind specified for the purposes of section 832(4) by regulations under section 396` | MAYBE BOOLEAN | part23-ch1 |
| `s 396 the provision is of a kind specified for the purposes of section 836(1) by regulations under section 396` | MAYBE BOOLEAN | part23-ch2 |
| `s 396 the provision is of a kind specified for the purposes of section 841(2)(a) by regulations under section 396` | MAYBE BOOLEAN | part23-ch3 |
| `s 396 the statement is made in the note required by regulations under section 396 as to the reasons for showing development costs as an asset` | MAYBE BOOLEAN | part23-ch3 |
| `s 409(3) the company is for the time being entitled to an exemption conferred by regulations under section 409(3) in respect of the information` | MAYBE BOOLEAN | part22-interest |
| `s 414 the balance sheet comprised in the accounts has been signed in accordance with section 414` | MAYBE BOOLEAN | part23-ch2 |
| `s 423 a copy of that statement was circulated to members in accordance with section 423` | MAYBE BOOLEAN | part23-ch2 |
| `s 423 the accounts were last circulated to members in accordance with section 423` | MAYBE BOOLEAN | part23-ch2 |
| `s 677 the assistance is financial assistance within the meaning of Chapter 2 of Part 18` | MAYBE BOOLEAN | part23-ch2 |
| `s 705 the payment is of a description specified in section 705 (payments apart from purchase price of shares to be made out of distributable profits)` | MAYBE BOOLEAN | part23-ch2 |
| `s 790B Part 21A does not apply to the company` | MAYBE BOOLEAN | part24 |
| `s 1121 the officer is in default` | MAYBE BOOLEAN | part22-notice, part22-register, part24 |
| `s 1121 the officer is in default in relation to the continued contravention` | MAYBE BOOLEAN | part24 |
| `s 1136 the place is specified in regulations under section 1136` | MAYBE BOOLEAN | part22-notice, part22-register |
| `s 1163(1) the asset is a non-cash asset` | BOOLEAN | part23-ch3 |
| `s 1165(2) the company is an authorised insurance company` | BOOLEAN | part23-ch1, part23-ch3 |
| `s 1167 the system of classifying business activities is prescribed` | BOOLEAN | part24 |
| `s 1173(1) the day is a working day for the company` | FUNCTION FROM DATE TO BOOLEAN | part22-interest, part22-notice, part22-register |
| `Part 18 Chapter 3, 4 or 5 the redemption or purchase of the shares out of capital or unrealised profits is in accordance with the Chapter` | MAYBE BOOLEAN | part23-ch1 |
| `Part 35 any requirement of Part 35 as to the delivery of a certified translation into English of any document forming part of the accounts has been...` | MAYBE BOOLEAN | part23-ch2 |
| `Part 35 any requirement of Part 35 as to the delivery of a certified translation into English of any of those documents has been met` | MAYBE BOOLEAN | part23-ch2 |

Seams taken because the text of this range cites another part (the list of PLAN.md section 6, `seams`), and what coa18 did with each:

- s 805 and s 809, s 1136 (coa25): the place specified in regulations is the input `s 1136 the place is specified in regulations under section 1136`.
- s 826, s 409 (coa8): `s 409(3) the company is for the time being entitled to an exemption conferred by regulations under section 409(3) in respect of the information`.
- s 829, Part 18 (coa15): `Part 18 Chapter 3, 4 or 5 the redemption or purchase of the shares out of capital or unrealised profits is in accordance with the Chapter` (a `MAYBE BOOLEAN`).
- ss 831, 832, 836, 841, 844, 846, s 396 (coa8): the `s 396` inputs in the table above (what regulations under s 396 specify, require or provide).
- s 837, s 423 (coa9); s 838, ss 395, 397 and 414 (coa8); s 839, ss 395 and 397 (coa8): `s 423 ...`, `s 396 the accounts are prepared in accordance with sections 395 to 397 ...` and `s 414 ...` as inputs.
- s 840, Part 18 and ss 677, 678, 679, 705 (coa15): `s 677 the assistance is financial assistance within the meaning of Chapter 2 of Part 18` and `s 705 the payment is of a description specified in section 705 ...` are inputs; ss 678 and 679 are named in the text's own list in s 840(2)(b) (constructor `s 840(2)(b) financial assistance given by the company in contravention of section 678 or 679`) and enter s 847(2) as a BOOLEAN fact the person can state (`it was financial assistance given in contravention of section 678 or 679, ...`).
- s 853A, ss 167I, 279I, 790LG (coa4, coa6, coa17): s 853A(1)(b)(iii) cites them as the source of the information a first confirmation statement must confirm has been delivered; coa18 asks the statement's content as a BOOLEAN (`the statement confirms that the company has delivered, or is delivering at the same time, any information that it is required to deliver under section 167I, 279I or 790LG`) and does not call the answering sections.
- s 853B: ss 790LA to 790LH (coa17), s 1136 (coa25), ss 167G, 167H (coa4), ss 279G, 279H (coa6): the duties are constructors of the enumeration `s 853B duty` as the text lists them (`s 853B(c)`, `(e)`, `(g)`, `(h)`); the function `s 853B the duty is a duty to notify a relevant event` answers about membership of the list and does not call the answering sections; the input `the company, in accordance with regulations under section 1136, keeps company records at a place other than its registered office` is the one fact (h) needs.
- s 853C, s 9 (coa1): `s 9(5)(c) by the time of its incorporation the company's principal business activities had changed from those specified in the statement under section 9(5)(c)` is a `BOOLEAN` fact.
- s 853CA, ss 86, 87 (coa2); s 853CB, ss 88A, 88B (coa2): `s 86(2) ...`, `s 87 ...`, `s 88A(2) ...`, `s 88B ...` are `BOOLEAN` facts about the registered office and email address.
- s 853E, s 285 (coa7), s 313 (coa7) and Part 18: the two sections cited are of the Financial Services and Markets Act 2000 ("section 285(1)(a) of the Financial Services and Markets Act 2000", "section 313 of that Act"), not of this Act; they are `BOOLEAN` facts of s 853E(6).
  (PLAN.md section 6 lists them as seams to coa7; they are not seams to another part of this Act.)
- s 853H, Part 21A and s 790B (coa17): `s 790B Part 21A does not apply to the company` is a `MAYBE BOOLEAN`.
- **Implicit seams** (terms defined in another part and used here): "officer ... in default" (s 1121, taken as `s 1121 the officer is in default`, `MAYBE BOOLEAN`); "working day" (s 1173(1), taken as a `FUNCTION FROM DATE TO BOOLEAN` by the s 827 stepper); "public company" (s 4(2), a `BOOLEAN`); "authorised insurance company" (s 1165(2), a `BOOLEAN`); "non-cash asset" (s 1163(1), a `BOOLEAN`); "shadow director" (s 251, `MAYBE BOOLEAN`); "prescribed" (s 1167, a `BOOLEAN`).
- **Seams I found that the plan lacks:** (1) s 853E(6)'s two cross-references to the Financial Services and Markets Act 2000 look like seams to coa7 in PLAN.md section 6 and are not; (2) s 833A(9) hands a definition to "rules made by the Prudential Regulation Authority under Part 9A of the Financial Services and Markets Act 2000": an input `the term has the same meaning as in rules made by the Prudential Regulation Authority ...`, in no part of this Act; (3) Part 35 (delivery of a certified translation into English) is cited in ss 838(6) and 839(7): inputs named `Part 35 ...`, not in the plan's list for coa18.

## What the text turns out to say

Numbered findings, each checked against `inputs/ukpga-2006-46.txt` (line numbers are of that file).

1. **Twelve sections of the range are shown only as dots, and fifteen paragraphs inside other sections.** Sections 834, 835, 853I and 854 to 859 (that is 834, 835, 853I, 854, 855, 855A, 856, 856A, 856B, 857, 858, 859) have a heading and a line of dots (lines 11232, 11234, 11538 and 11580 to 11596); the fifteen paragraphs are ss 832(5)(b)(i), 832(6)(a), 833(2)(b) to (d), 833(3), 837(1)(b), 853A(2), 853B(a), (b), (d), (f), (fa), 853F(1)(b) and 853L(4).
   Counted at assembly: `awk` over lines 10757-11596 finds 27 lines containing ". . . ." (12 dots-only plus 15 marker-and-dots), and the coverage table has 27 rows `repealed or blank in this text`.
   The annual-return provisions (ss 854 to 859) are the largest block.
2. **s 853L(2)(a): the offence by a company in England and Wales has no stated upper limit on the first fine.** The text says only "in England and Wales to a fine, and, for continued contravention, a daily default fine not exceeding the greater of £500 and one-tenth of level 4 on the standard scale" (line 11571); for Scotland and Northern Ireland it says "a fine not exceeding level 5" (line 11572).
   Encoded as `a fine without a stated limit` for England and Wales.
3. **s 853L(2) and (6): the daily limit has a pound floor in one limb only.** England and Wales: "the greater of £500 and one-tenth of level 4"; Scotland and Northern Ireland: "one-tenth of level 5", no pound floor (lines 11571-11572, 11577-11578).
   The Act does not say how many pounds a level is: an input.
4. **s 853L(3): the contravention ends only when a statement with a confirmation date no later than the last day of the review period is delivered.** A statement delivered late that specifies a later confirmation date does not end it (line 11573).
   The encoding asks this as one fact (`a confirmation statement specifying a confirmation date no later than the last day of the review period concerned has been delivered ...`); the caller does the date comparison.
5. **s 805(1) and (3): two limits on the time for the report, "a reasonable period (not more than 15 days)".** Both must hold; "reasonable" has no number; and s 827 disregards days that are not working days in a period "expressed as a number of days" (lines 10896, 10901, 11111), which fork F11 takes the 15 days to be.
6. **s 827 reaches only "any provision of this Part"**, that is Part 22: the 14 days of s 853A(1) and s 853L(1) (Part 24) are not reckoned in working days (line 11111).
   Forks F10 and F33.
7. **s 806(1) and s 809(4) turn on "default is made for 14 days"** (lines 10916 and 10952), a period that is not obviously one "allowed by any provision of this Part for fulfilling an obligation" in the words of s 827; whether s 827 reckons it is not stated.
   Fork F10.
8. **s 801(2): "may only be made by the company".** The text closes the list of applicants for the first sale order with "only", so `s 801(2)` answers `JUST FALSE` for anyone else (line 10862); s 801(4) lists three possible applicants for a further order under (3) (lines 10864-10867).
9. **s 797(4)(b) and s 798(5)(b): "in the case of an interim order under section 794(3), to the terms of the order" (lines 10825 and 10845).** The Act subjects the effect of an interim order to the order's own terms, which are the court's and not stated in the Act; the encoding takes "the terms of the interim order permit the act" as an input.
   Fork F6.
10. **s 853A(5) and (6): a 12-month review period beginning on 29 February has no anniversary in a year that is not a leap year.** The text says "the period of 12 months beginning with the day of the company's incorporation" and is silent on how a leap-day anniversary is reached; fork F34 takes 1 March (daydate rolls an impossible date forward) so the period ends on 28 February.
11. **s 849 is one sentence: "A company must not apply an unrealised profit in paying up debentures or any amounts unpaid on its issued shares." (line 11398).** It has no exception and no period in its own words.
    Encoded as a standing prohibition (a `PARTY Company` rule) and as a decision function (`s 849 the company may apply the profit in paying up debentures or any amounts unpaid on its issued shares`, `JUST FALSE` for an unrealised profit).
12. **A miscounted expectation caught by a test.** I first wrote 26 January 2026 as the last day for the s 805(1) report when the investigation concluded on Monday 5 January 2026 (15 working days, 6 January not a working day); the assertion failed; counting by weeks gives Tuesday 27 January 2026, which is what the text yields (3 days in the first week, 5 and 5 in the next two weeks, then Monday 26 and Tuesday 27).
    The expected value in `coa18-tests-part22-notice.l4` is the corrected one and the comment on it says so.
    No encoding was changed.

Findings 1 to 11 are readings of the text; 12 is a defect in my own expectation, found by the instrument, and is recorded because the brief asks that a failing assertion be reported.

## What the stable binary does not accept, and what it does

Loud (the binary refuses it, or errors at the assertion, so you find it):

- `Period OF 2 Years` (without a comma) is an arity error: write `Period OF 2, Years`.
- `LIST Date 6 1 2026` is mis-parsed; write `LIST (Date 6 1 2026)`.
  An argument `JUST TRUE` needs brackets in a call: `f (JUST TRUE)`.
- A chain of `ELSE IF` on separate lines is an indentation error: use `BRANCH`.
- An `#ASSERT` on a regulative (`DEONTIC`) value cannot compare it with `EQUALS` when the rule is a standing obligation or prohibition not yet run: "Trying to check equality on types that do not support it" (`eval/unsupported-equality`, measured on 1.6.110 on 2026-11-12 with a probe of `s 804(1) ... EQUALS FULFILLED`).
  A regulative rule that reduces to `FULFILLED` with its arguments given can be asserted equal to `FULFILLED` (one assertion, `s 796(2)` in `coa18-tests-part22-notice.l4`).
  Every other regulative rule is run with `#TRACE` and the expected outcome is written in a comment above it; the 35 traces of the tests were each compared with that comment at assembly (34 agree; the 35th, in `coa18-tests-part23-ch3.l4`, expects the standing prohibition to remain, and the output shows `PARTY Company MUST NOT ...` as the open prohibition).
  The same duty is also encoded as a decision function over the facts wherever the text fixes a period or a condition, and that function is asserted.

Silent (exit code 0, wrong answer):

- `NOT a AND b` reads as `NOT (a AND b)`: every `NOT` is bracketed in coa18; a test caught my first mistake (a `NOT (a) AND NOT (b)` that returned the wrong result).
- `l4 run` exits 0 when an assertion fails; `check.sh` prints the counts (below).

Accepted by the two supplied builds but not used (PLAN.md section 5): `REFUSE`, `#ASSERT REFUSED`, `YMD`.

Where the two builds differ: they did not differ on any count or on any output line of the 7 test modules (diff of the full `l4 run` output of 1.6.110 against 1.6.109 with file and range lines removed, 0 lines; checked 2026-11-12), including every `#TRACE` result.

## What `check.sh` printed

Command: `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`, run on 2026-11-12 after the last edit of any `.l4` file; exit status 0.
The baseline numbers it replaced: no earlier coa18 numbers exist (the supplied folder held only the keel's two modules, `coa-core.l4` and `coa-definitions.l4`, which the table shows at 0 errors and 0 assertions), so the TOTAL went from 2 modules and 0 assertions satisfied to 18 modules and the figure printed below.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa18-cases-seat.l4                            0       139       0        0         0 |      0       139       0        0  same
coa18-part22-interest.l4                       0         0       0        0         0 |      0         0       0        0  same
coa18-part22-notice.l4                         0         0       0        0         0 |      0         0       0        0  same
coa18-part22-register.l4                       0         0       0        0         0 |      0         0       0        0  same
coa18-part23-ch1.l4                            0         0       0        0         0 |      0         0       0        0  same
coa18-part23-ch2.l4                            0         0       0        0         0 |      0         0       0        0  same
coa18-part23-ch3.l4                            0         0       0        0         0 |      0         0       0        0  same
coa18-part24.l4                                0         0       0        0         0 |      0         0       0        0  same
coa18-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa18-tests-part22-interest.l4                 0       111       0        0         0 |      0       111       0        0  same
coa18-tests-part22-notice.l4                   0       234       0        0         0 |      0       234       0        0  same
coa18-tests-part22-register.l4                 0       165       0        0         0 |      0       165       0        0  same
coa18-tests-part23-ch1.l4                      0       110       0        0         0 |      0       110       0        0  same
coa18-tests-part23-ch2.l4                      0       103       0        0         0 |      0       103       0        0  same
coa18-tests-part23-ch3.l4                      0       140       0        0         0 |      0       140       0        0  same
coa18-tests-part24.l4                          0       169       0        0         0 |      0       169       0        0  same
TOTAL (18 modules)                             0      1171       0        0           |      0      1171       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`check.sh` does not print warnings.
I ran every module through `l4 run` separately for that (`work/run.sh`): 0 warnings and 0 errors on all 16 coa18 modules (the 18 rows of the table are those 16 and the keel's two, whose warnings I did not measure because they are not mine); and `srcrefs.py check --refs` and `--strict` report 0 problems for each layer-1 module (the layer-1 modules carry the `@ref` locators; the tests and the seat carry none).
