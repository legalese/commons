# National Symbols Act 2022 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 29 of 2022, informal consolidation ("version in force from
10/10/2025"), as deposited at `../../registers/source-bundle/NSA2022.txt`. The only
amendment annotated in the text is "[S 671/2025 wef 10/10/2025]", at the end of
First Schedule Part 3 (the National Pledge); the text does not say what it changed.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0130** in `subjects/sg/requirements.jsonl`: tier 2 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act is 19 sections and two Schedules, so nearly all of it is encoded: which
things are national or presidential symbols (ss 3 to 12), the flag's description
(First Schedule Part 1, Second Schedule Part 1), the national flower (Part 7), who
keeps the seals, who may amend the Schedules and make regulations (ss 13, 14(1)),
the penalty ceiling for offences under regulations (s 14(2)), the Public Prosecutor's
consent (s 15), and the consequential amendments (ss 17, 19). Not encoded: s 1, the
Anthem's lyrics and music, the Pledge's words, the symbolism paragraphs, the Lion Head
symbol's depiction (an image, absent from the text layer), s 16 (repeal of the 1959
Act) and s 18 (a renaming in the Foreign Interference (Countermeasures) Act 2021).

## What the Act turns out to say

### 1. The Act itself forbids nothing

Nothing in the Act tells a person how they may or may not use the flag, the anthem or
any other symbol, and the Act creates no offence of its own. Every rule of use is left
to regulations made by the President: s 14(2)(a) lets them "regulate the
circumstances and manner in which a national symbol or presidential symbol may be
used", (b) lets a prescribed person permit or prohibit use (with appeals), and (c)
lets them make a contravention an offence. A use is punishable only when a regulation
is contravened **and** that regulation is made an offence. For the question REQ-0130
asks, the Act's real answer is in subsidiary legislation this row did not retrieve.
Asserted.

### 2. The ceiling is $30,000 or 6 months, or both

s 14(2)(d): the penalty prescribed by regulations "must not exceed a fine of $30,000
or imprisonment for a term not exceeding 6 months or both". A regulation setting
$30,001, or 7 months, would be outside the power. Asserted.

### 3. The President, not a Minister, controls the symbols

s 13: the President may amend any Schedule "in relation to any aspect or description"
of a symbol, by Proclamation in the Gazette — so the flag's design or the national
flower can change without an Act of Parliament. s 14(1): the President makes the
regulations. A Minister appears only in s 1, to appoint commencement. Asserted.

### 4. Ten symbols, in two classes

Seven national symbols (ss 3 to 9): the National Flag, the National Anthem, the
National Pledge, the National Coat of Arms (also "the State Crest"), the public seal,
the Lion Head symbol and the national flower. Three presidential symbols (ss 10 to
12): the Presidential Standard, the Presidential Coat of Arms (also "the Presidential
Crest") and the seal of the President. The Merlion is not among them. Asserted.

### 5. The flag is a checkable description

Red above white in two equal horizontal sections, a white crescent moon beside 5
white stars in the canton (the top left quarter of the obverse, s 2), width to length
2:3. A 60 x 90 flag matches; 60 x 120, four stars, or white above red does not. The
Presidential Standard also has the 2:3 ratio. The national flower is the Vanda Miss
Joaquim (Papilionanthe Miss Joaquim). Asserted.

### 6. Only the President keeps things, and only the seals are judicially noticed

The public seal and the seal of the President "are to be kept by the President" (ss
7(3), 12(3)). s 17 rewrites Evidence Act 1893 s 59(1)(f) so that courts take judicial
notice of those two seals. s 19 renames the National Emblems (Control of Display) Act
1949 to concern "foreign national emblems". Asserted, except that whether the 1949
Act's redefined "any state" still reaches Singapore's own flag is not decided.

### 7. The deposit is missing a language

s 5(1) says the Pledge is set out "in each of the 4 official languages"; the deposit's
text layer has English, Malay and Chinese only. The Tamil text is presumably in the
PDF but not extracted (inference; the PDF was not inspected). The count of 4 is
asserted from s 5(1).

## What would need doing before this is worth anything

- Retrieve the regulations made under s 14 (if any are deposited) — they hold every
  rule a person actually meets about using a symbol.
- Find out what S 671/2025 changed in the Pledge Part.
- Check the PDF for the Tamil Pledge and the Lion Head image.
- No case law or Gazette Proclamations under s 13 were searched.
