# Local Forces (Relief of Financial Hardship) Act 1953 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/LFRFHA1953.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on 31 December
2021. The last amending law in its Legislative History is Act 24 of 2004 (Police Force
Act 2004, in force 12 October 2004); the Schedule is annotated [24/2004].

**Checks:** one case file, 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0183** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person it applies to; no scenario has asked a sharper question
yet. The Act has seven sections and a one-page Schedule, so the whole operative text
(ss 2-7 and the Schedule) is encoded. What it does not contain — the rules under s 5
and the Gazette notifications under ss 3 and 6 — was not deposited and is not encoded.

## What the Act turns out to say

### 1. The Act grants a right whose content is entirely in rules that were not deposited

s 4(1) says a person to whom the Act applies "shall be entitled in accordance with any
rules made under section 5" to relief. The Act fixes no amount, no conditions, no
application form and no deciding body; s 5(2)(a)-(e) leave every one of these to the
Minister's rules. With no rules deposited, the encoding makes entitlement conditional
on an input, "rules under s 5 provide for the case": with every other condition met and
that input false, there is no entitlement. Asserted.

### 2. The Act switches on force by force, and only from a Gazetted date

s 3(1) applies the Act to a member called out for actual, active or full-time service
"but only from such date as the Minister may, by notification in the Gazette,
appoint", and s 3(2) allows different dates for different forces. Without an
appointed date for the member's force, there is no qualifying service at all. Service
on the appointed day counts ("on and after", s 4(2)); service the day before does
not. Asserted. Which forces have an appointed date, and from when, the deposit does
not say.

### 3. Switching it off does not take away relief already earned

s 3(3) lets the Minister declare that the Act ceases to apply to a force "from and
after" a date, "without prejudice to any right of relief arising out of the service of
those members before that date". The encoding counts service the day before cessation
and excludes service on the cessation day and after. The claim date is not an input:
service before cessation keeps its relief whenever it is claimed. Asserted (as to the
service-day boundary; the claim-date point is built into the shape of the rule, not
tested).

### 4. The regular police are not a local force; the Special Constabulary is

The Schedule lists the Singapore Civil Defence Force, the Special Constabulary (Part 8
of the Police Force Act 2004), the Singapore Armed Forces and the Vigilante Corps. The
regular Police Force is not listed, so it is outside the Act unless added by
notification under s 6; equally a listed force deleted under s 6 falls outside.
Asserted.

### 5. "His wife or children or other dependants" — the text is gendered

s 4(1) covers hardship "suffered by him or his wife or children or other dependants".
A relative who is not a dependant is outside it (asserted). Whether the husband of a
female member is within "wife", or only within "other dependants" when he is in fact a
dependant, the deposit does not settle; the Interpretation Act was not consulted. The
encoding does not have a husband value. Not asserted.

### 6. The civil defence Minister must be consulted before the Civil Defence Force is touched

The Act's "Minister" is the Minister for defence (s 2). s 7 forbids exercising the
powers in ss 3, 5 and 6 "so as to affect" the Civil Defence Force or its members
without previous consultation with the Minister responsible for civil defence. So
deleting the Civil Defence Force from the Schedule without that consultation does not
comply; with it, it does. Powers outside ss 3, 5 and 6 are not caught. Asserted.

### 7. Parliament can annul a rule only at the next sitting, and only going forward

s 5(3): a rule presented to Parliament may be annulled by resolution "at the next
sitting of Parliament after the order is presented"; it is then void "thenceforth but
without prejudice to the validity of anything done thereunder". The encoding treats
the rule as void from the annulment day on (the boundary day is an inference) and
keeps acts done before it valid. The text says "the order" although the instrument is
a rule — apparently a drafting carry-over. Asserted.

## What would need doing before this is worth anything

- Retrieve any rules made under s 5 (amount, conditions, who applies and who decides).
  Without them the encoding answers only the threshold question.
- Retrieve the Gazette notifications appointing dates under s 3(1) for each local
  force, any cessation declarations under s 3(3), and any additions or deletions under
  s 6.
- Read the force Acts (Civil Defence Act 1986, Police Force Act 2004 Part 8, Singapore
  Armed Forces Act 1972, Vigilante Corps Act 1967) for what "actual service", "active
  service" and "full-time service" mean for each force.
- Consult the Interpretation Act 1965 on gendered words for the "wife" question.
- No case law was searched.
