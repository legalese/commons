# Terrorism (Suppression of Misuse of Radioactive Material) Act 2017 — naive encoding

**Method: naive.** Straight from the deposited text with the conventions of the
`writing-l4-rules` example rows and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/7/2022"), deposited at `../../registers/source-bundle/TSMRMA2017.txt`. The revised
edition "incorporates all amendments up to and including 1 December 2021"; the latest
amendment annotated is Act 17 of 2022 wef 01/07/2022, all of it in s 13 (extradition).
The arrangement of sections at the top of the deposit is out of step by one with the
body (it numbers "Short title" as 2); this row follows the body.

**Checks:** one case file, 51 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0122** in `subjects/sg/requirements.jsonl`: Tier 2 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet.

The Act is short (14 sections) and almost entirely criminal. This row takes the
definitions of nuclear and radioactive material, the s 3 exclusions, every offence
(ss 4 to 10) and its punishment, the definition of "nuclear terrorism offence" and its
reach outside Singapore (s 11), the political-offence exception (ss 12(1), 13(7)(c))
and the Public Prosecutor's consent (s 14). Not encoded: the extradition machinery of
s 13(2) to (6) (Gazette notifications, declared Commonwealth territories, treaties),
the definitions of "conveyance", "government", "ionising radiation" and "military
forces of a State" beyond flags, and the Penal Code provisions the Act points to
(ss 34, 35, 300(a)), whose content is not in the deposit.

## What the Act turns out to say

### 1. Using radioactive material to coerce is a life sentence; possessing it to coerce is no offence under ss 4 or 5

s 6(1)(b)(iii) and s 7(1)(b)(iii) complete the use and nuclear-facility offences with
an intent "to compel any other person, or any international organisation or
government, to do or refrain from doing any act". ss 4 (possession) and 5 (making)
list only the intents to cause death, serious bodily injury or substantial damage.
Possessing material intending only to coerce falls outside s 4; using it the same way
is an offence punishable with imprisonment for life. Asserted.

### 2. Life imprisonment is a ceiling in ss 4 and 5 and a fixed sentence in ss 6 and 7

ss 4 and 5: "liable on conviction to imprisonment for a term which may extend to life
imprisonment". ss 6(2)(b) and 7(2)(b): "shall on conviction ... be punished with
imprisonment for life". Where the person intended death "and death is caused", ss
6(2)(a) and 7(2)(a) apply "the same punishment as an act under section 300(a) of the
Penal Code 1871". The deposit does not say what that punishment is (that it is the
punishment for murder is an inference from outside the deposit). An intent only to
injure that ends in a death is "any other case": life imprisonment. Asserted.

### 3. Only threats to USE are offences under s 8

s 8 covers threats "to do any act that would be an offence under section 6 or 7". A
threat to possess or make a device (ss 4, 5) is not within it. Threats and demands
(s 9) carry 10 years; an attempt (s 10) carries 15. Asserted.

### 4. Abetting or conspiring to commit an attempt is left out of "nuclear terrorism offence"

The s 2 definition takes "(a) an offence under section 4, 5, 6, 7, 8, 9 or 10" but
only "(b) an abetment of or a conspiracy to commit an offence under section 4, 5, 6,
7, 8 or 9". Read literally, abetting an attempt (s 10) is not a nuclear terrorism
offence, so the s 11 extraterritorial deeming and the s 13(1) extradition deeming do
not reach it. Whether the Penal Code catches it some other way is not in the deposit.
Asserted (on the literal reading).

### 5. Nuclear material is radioactive material without any harm test; depleted uranium is not nuclear material

"Radioactive material" is "any nuclear material or any other radioactive substance".
A radioactive substance must both emit ionising radiation and, "owing to its
radiological or fissile properties", be capable of causing death, serious injury or
substantial damage. Nuclear material needs neither limb. Plutonium is nuclear material
unless its plutonium-238 concentration is "exceeding 80%" (so at exactly 80% it still
is). Uranium is nuclear material only if enriched above the natural ratio, or natural
"but not in the form of ore or ore residue". Depleted uranium meets neither
paragraph, so it counts only if it passes the harm test as a substance. Asserted.

### 6. Every offence turns on "intentionally and without lawful authority"

ss 4 to 7 and 9 each open with these words. The Act does not say what lawful authority
is or who grants it (presumably licensing under other legislation, an inference).
The armed-forces and military exclusions of s 3 apply only "to the extent" the
activities are governed by international humanitarian law or other rules of
international law, and "armed conflict" excludes riots. No prosecution may start
without the Public Prosecutor's consent (s 14). Asserted.

## What would need doing before this is worth anything

- The Penal Code provisions the Act imports (ss 34, 35, 300(a), and the abetment and
  conspiracy provisions) were not read, so finding 4 and the s 6(2)(a) punishment rest
  on the Act's own words alone.
- What "lawful authority" means in practice (radiation-protection licensing) was not
  traced.
- The s 13 extradition machinery, amended in 2022, is encoded only as s 13(1) and
  (7)(c).
- No case law or Convention travaux were searched.
