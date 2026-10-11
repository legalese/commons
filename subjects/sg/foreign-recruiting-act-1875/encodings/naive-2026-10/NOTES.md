# Foreign Recruiting Act 1875 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/FRA1875.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021 and came into operation on 31 December
2021. It carries no amendment annotations; its Legislative History ends with the 2014
Revised Edition (operation 28 February 2014). The deposit's metadata calls it the current
version as at 1 October 2026. The Arrangement of Sections agrees with the body (ss 1 to 5).

**Checks:** one case file, 48 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0137** in `subjects/sg/requirements.jsonl`: tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet. The Act
has five sections, so this row encodes ss 2 to 5 whole: the definition of "foreign State"
(s 2), the President's two order-making powers (ss 3, 4), and the offence and penalty
(s 5). Not encoded: the content of any order actually made (none was looked for), what
"service of any foreign State" covers beyond governments and would-be governments,
whether s 5 reaches conduct outside Singapore, and any other law that may catch the same
conduct.

## What the Act turns out to say

### 1. The Act forbids nothing by itself: no order, no offence

s 5 makes it an offence to induce recruits or aid their engagement only "in violation of
the prohibition of the President, or of any condition subject to which permission to
recruit has been accorded". The prohibitions come from orders: a written order against
one person under s 3, or a general order notified in the Gazette under s 4. Where no
order exists, a recruiter for a foreign army commits no offence under this Act. Where a
Gazette general prohibition exists, the same conduct is an offence. Asserted.

### 2. The fine is unlimited and the prison term is up to 7 years

s 5: liable on conviction "to a fine or to imprisonment for a term not exceeding 7 years
or to both". The Act states no maximum fine. Whether some general law caps it was not
looked at. Asserted.

### 3. "Foreign State" includes would-be governments

s 2 extends "foreign State" to "any person or persons exercising, or assuming to
exercise, the powers of government" over any country, colony, province or people beyond
Singapore. A self-proclaimed government abroad counts, so recruiting fighters for one is
caught as fully as recruiting for a recognised army. That a private foreign company (for
instance a security firm) and the Government of Singapore fall outside the definition is
an inference from the text, not something it says. Asserted.

### 4. An attempt, or persuading someone just to travel, is enough

s 5(a) catches whoever "induces or attempts to induce" a person to accept, agree to
accept, "or to proceed to any place with a view of obtaining" a commission or employment
in a foreign State's service. An unsuccessful attempt to persuade someone to travel
abroad to seek a commission is an offence under a general prohibition. Asserted.

### 5. Helpers are caught, but only if they know

s 5(b) reaches anyone who "knowingly aids" the engagement of a person so induced, "by
forwarding or conveying him, or by advancing money, or in any other way whatever". A
travel agent who knowingly books the recruits' passages, or a friend who knowingly lends
the fare, commits the offence; a travel agent who books the same passages without
knowing their purpose does not. Asserted.

### 6. A s 3 order reaches only "that person" (an inference) and has a form

s 3 lets the President, when a person within Singapore is obtaining or attempting to
obtain recruits for a foreign State "in any capacity", prohibit "that person" or permit
him subject to conditions, "by order in writing, signed by the Minister". The power does
not arise for a recruiter working from outside Singapore. The encoding reads a s 3
prohibition as not binding anyone else, so an assistant not named in the order is not
"in violation of the prohibition" (an inference). A permitted recruiter who breaks a
condition commits the offence; one who keeps every condition does not. Asserted.

## What would need doing before this is worth anything

- No order under s 3 or s 4 was looked for. Whether any general prohibition is in force
  decides finding 1 and therefore almost every case.
- s 3 speaks of recruits "in any capacity", while s 5(a) speaks of "commission or
  employment in the service of any foreign State". Whether a foreign state-owned company,
  hospital or school is "the service of" a foreign State is not decided here.
- The reading that a s 3 order binds only the person named, and that an aider must act
  "in violation" of a prohibition that binds him, is an inference from the sentence's
  structure and could be wrong.
- Whether s 5 applies to inducement done outside Singapore, and whether other law (on
  terrorism, mercenaries or the armed forces) also catches the conduct, was not examined.
- No case law, prosecution history or general sentencing law was searched.
