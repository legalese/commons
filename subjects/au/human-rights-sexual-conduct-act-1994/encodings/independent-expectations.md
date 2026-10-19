# Independent expectations: Human Rights (Sexual Conduct) Act 1994 (Cth)

Written from BRIEF.md and `../registers/source-bundle/C2004A04852.txt` only, before reading any `.l4` file.

## The Act's words relied on

- s 4(1): "Sexual conduct involving only consenting adults acting in private is not to be subject, by or under any law of the Commonwealth, a State or a Territory, to any arbitrary interference with privacy within the meaning of Article 17 of the International Covenant on Civil and Political Rights."
- s 4(2): "For the purposes of this section, an adult is a person who is 18 years old or more."
- s 3: "This Act extends to every external Territory."
- s 2: "This Act commences on the day on which it receives the Royal Assent." (The compilation does not state the assent date.)

## Concepts tested

- **adult(birth, on)**: 18 years old or more on the conduct date. 18 on the eighteenth birthday; a 29 February birthday falls on 28 February in a common year (brief's rule).
- **protected(conduct)**: s 4(1) covers the conduct: everyone involved is an adult, everyone consented, they acted in private.
- **interference permitted?**: if the conduct is protected and the interference is under a law of the Commonwealth/State/Territory and is arbitrary, s 4 says it is not to happen (not permitted). If the conduct is protected but the interference is not arbitrary, s 4 does not forbid it. If the conduct is not protected, s 4 says nothing.

## Scenarios

| # | Facts | Expected | Basis |
|---|---|---|---|
| 1 | Born 15 Mar 2008; date 15 Mar 2026 (18th birthday) | adult | s 4(2) "18 years old or more"; 18 on the birthday |
| 2 | Born 15 Mar 2008; date 14 Mar 2026 (day before) | not adult | s 4(2) |
| 3 | Born 15 Mar 2008; date 16 Mar 2026 | adult | s 4(2) |
| 4 | Born 29 Feb 2008; date 28 Feb 2026 (common year) | adult | brief: 29 Feb birthday falls on 28 Feb in a common year |
| 5 | Born 29 Feb 2008; date 27 Feb 2026 | not adult | s 4(2) |
| 6 | Born 29 Feb 2008; date 1 Mar 2026 | adult | s 4(2) |
| 7 | Born 29 Feb 2000; date 29 Feb 2018? (2018 not leap) -> use 28 Feb 2018 | adult | brief rule |
| 8 | Born 31 Dec 2007; date 31 Dec 2025 | adult | s 4(2) |
| 9 | Two adults (born 1990, 1985), both consent, private, date 1 Jun 2026 | protected | s 4(1) |
| 10 | As 9 but one is born 15 Mar 2008 and the conduct is 14 Mar 2026 | not protected ("only ... adults") | s 4(1),(2) |
| 11 | As 9 but one is born 15 Mar 2008 and the conduct is 15 Mar 2026 | protected | s 4(1),(2) |
| 12 | As 9 but one did not consent | not protected ("only consenting adults") | s 4(1) |
| 13 | As 9 but not in private | not protected ("acting in private") | s 4(1) |
| 14 | Three consenting adults in private | protected (no limit on number) | s 4(1) |
| 15 | One adult alone, consenting, private | protected ("involving only consenting adults" is satisfied by one) | s 4(1) — see note |
| 16 | Scenario 9 + interference under a State law, arbitrary | not permitted (s 4 forbids it) | s 4(1) |
| 17 | Scenario 9 + interference under a Territory law (incl. an external Territory), arbitrary | not permitted | s 4(1), s 3 |
| 18 | Scenario 9 + Commonwealth law, not arbitrary | s 4 does not forbid it (permitted so far as s 4 goes) | s 4(1) "arbitrary" |
| 19 | Scenario 10 (minor involved) + State law, arbitrary | s 4 gives no protection; it neither forbids nor authorises (no answer / not forbidden by s 4) | s 4(1) |
| 20 | Scenario 9 + interference not under any Australian law (e.g. a private act) | s 4 does not apply (not forbidden by s 4) | s 4(1) "by or under any law of ..." |
| 21 | No one involved (empty list) | no answer (NOTHING) or not protected — the Act does not contemplate it | — |

## Where I read the Act differently from the brief, or where it is silent

- **29 February birthdays.** The Act does not say when someone born on 29 February turns 18 in a common year. The brief picks 28 February. Common law (*birthday rule*) and some State age-of-majority statutes would give 1 March, or say the person attains the age at the first moment of the anniversary day. I test the brief's rule (scenario 4) and note it as a choice the Act does not make.
- **Consequence when not protected.** Section 4 only restricts interference with protected conduct. When the conduct is not protected (a minor, no consent, not private), the Act does not say a law *may* interfere; it simply says nothing. "Not forbidden by s 4" is the correct answer, not "permitted".
- **Arbitrariness and "law of the Commonwealth, a State or a Territory"** are inputs per the brief; s 3 means an external Territory's law counts as a Territory law.
- **Commencement (s 2).** The compilation does not give the assent date (19 December 1994 per the legislation register, not in the source), so conduct dated before commencement cannot be resolved from the source. Not tested.
- **Solo conduct.** "Involving only consenting adults" — one adult acting alone satisfies the words literally. I expect protected.
