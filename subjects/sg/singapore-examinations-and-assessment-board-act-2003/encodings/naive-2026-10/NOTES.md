# Singapore Examinations and Assessment Board Act 2003 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition ("incorporates all amendments up to and including
1 December 2021"), informal consolidation marked "version in force from 1/4/2024",
as deposited at `../../registers/source-bundle/SEABA2003.txt`. The latest amendment
annotated is "[Act 4 of 2008 wef 01/04/2024]" on s 12(1)(c) and s 12A; S 461/2020 and
Act 5 of 2018 are also shown.

**Checks:** one case file, 52 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0209** in `subjects/sg/requirements.jsonl`: tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. It asks what the Act decides for a
person or business it applies to; no scenario has asked a sharper question yet.

This row takes what a candidate, a parent, a business or the Board's own people meet:
which examinations are national (s 2, Schedule), what the Board must and may conduct
(s 11), who sets the fees (s 12(1)(b), (c)), the validated late charges (s 12A), the
Board's size, terms, quorum and voting (ss 5, 7, 9), protection from suit (s 17), and
the offences and penalties (ss 40-43, 45(3)). Not encoded: the seal, delegation,
committees and staff (ss 4, 6, 8, 13-16), finance (ss 19-27) and the 2004 transfer from
the Ministry's Examinations Division (ss 32-38). No regulations under s 45 were
retrieved, so the actual fees and the list of compoundable offences are unknown here.

## What the Act turns out to say

### 1. Leaking Board information carries four times the prison term of faking its logo

Breach of secrecy (s 41(2)) is punishable by a fine of up to $2,000 **or imprisonment
up to 24 months**; using a symbol identical with or confusingly like the Board's
(s 40(2)) by a fine up to $10,000 or imprisonment up to 6 months. The secrecy duty
binds anyone who "is or has been" a member, officer, employee, agent or committee
member, so it survives leaving the Board, and yields only to the person's duties, a
court's lawful requirement, or written law. Asserted.

### 2. Only candidate fees for the four national examinations need the Minister

s 12(1)(b): the Board determines candidate fees for national examinations "with the
approval of the Minister". s 12(1)(c): fees for its other services, including conducting
any assessment and the use of its facilities, and late-payment charges, are imposed with
no approval mentioned. Read literally, the late charge in (c)(ii) attaches to "any such
fee or commission", that is a (c)(i) fee, and not to a national-examination candidate
fee under (b); whether regulations fill that gap was not checked. Asserted.

### 3. The national examinations are a closed list of four, and the Board cannot be sued on its duties

The Schedule names the PSLE and the Singapore-Cambridge GCE O-, N- and A-Levels; the
Minister may amend it by Gazette (s 44). Everything else that tests a person is an
"assessment" (s 2), which the Board may run only "on terms that may be mutually agreed"
(s 11(2)(a)). s 11(3) says nothing in s 11 imposes a duty "enforceable by proceedings
before any court" that the Board would not otherwise bear. Asserted.

### 4. A late charge collected before an undated commencement is validated, and the annotation looks odd

s 12A deems every late-payment charge collected before the commencement of the Statutes
(Miscellaneous Amendments) Act 2008 "always to have been validly collected" and bars
proceedings. The deposit does not state that commencement date; it annotates s 12(1)(c)
and s 12A "[Act 4 of 2008 wef 01/04/2024]", sixteen years after the amending Act. Inference:
the annotation may record the consolidation's own date rather than the 2008 commencement.
The encoding takes the commencement as a parameter. Asserted (as a date comparison only).

### 5. The symbol offence states no consent exception and no mental element

s 40(1) gives the Board "the exclusive right" to its symbol; s 40(2) makes it an offence
for "any person" to use one identical with it or likely to deceive or confuse. The
subsection says nothing about use with the Board's permission or about knowledge. Whether
a licence is implied by (1) is an inference the text does not settle. Asserted (on the
literal reading).

### 6. Composition is capped at $1,000 and needs regulations to exist

s 43(1): the chief executive or an officer he or she authorises may compound only an
offence "prescribed as a compoundable offence" (s 45(2)(d)), for at most $1,000. Regulations
may set penalties up to $10,000 or 12 months, plus $1,000 for every day "or part of a day"
a continuing offence goes on after conviction (s 45(3)). Asserted.

### 7. Smaller points

The Board has a Chairperson and 6 to 9 other members (s 5(1)), each for at most 3 years
(s 7(1)), removable "without giving any reason" (s 7(3)). A simple majority forms a quorum
(s 9(1)); the encoding reads "the members" as those in office, which the text does not
settle. The presiding member has a casting vote (s 9(5)). s 17(1) bars personal suits for
acts done in good faith; s 17(2) also shields the Board itself for good-faith errors in
information supplied to the public "pursuant to any written law". Officers, partners
(including a person "purporting to act as a partner") and association office-holders share
the entity's guilt on consent, connivance or neglect (s 42). Asserted.

## What would need doing before this is worth anything

- The regulations under s 45 (fees, conduct of examinations, compoundable offences) were
  not retrieved; examination misconduct by candidates lives there, not in the Act.
- Whether s 17(2) reaches the release of examination results (is that information supplied
  "pursuant to any written law"?) is unanswered.
- The commencement date of the Statutes (Miscellaneous Amendments) Act 2008 for s 12A, and
  the meaning of the "wef 01/04/2024" annotation, need checking against the 2008 Act.
- No case law was searched.
