# Registration of Births and Deaths Act 2021 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** Act 17 of 2021, informal consolidation ("version in force from
30/9/2026"), with amendments by Act 2 of 2024 (16 April 2024), Act 20 of 2022
(15 October 2024) and Act 16 of 2026 (30 September 2026) shown. This Act has no
2020 Revised Edition; it post-dates it.

**Checks:** two case files, 162 assertions satisfied (108 in `rbda-cases-reporting.l4`, 54 in
`rbda-cases-father-particulars.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**10 of the 527 Singapore Acts** deposited here cite it. This row takes what an
ordinary person, doctor, hospital or ship's or aircraft's master meets: who must
report a birth, death or stillbirth, to whom, the 42-day duty to give birth
particulars, the rules on a child's name, the definition of a stillborn child,
registering a citizen's or PR's death abroad, the false-statement offence, and the
maximum penalties (ss 2(1), 7, 8, 10, 19-23, 26, 28, 32, 33, 35, 42, 48, 51).
Administration, the Registrar-General's own registration duties, adoption,
legitimation and assisted-reproduction re-registration, corrections and
cancellation, investigation powers and register and certificate offences are not
encoded.

## What the Act turns out to say

### 1. Parents of a child born in hospital have no duty to report the birth — but do have a duty to give the particulars

s 7(2)(a): for a birth in a hospital, the people responsible for reporting are
"every medical practitioner who attends to the birth, and the hospital". Parents are
listed only for births in other premises, in conveyances and elsewhere. But s 8
puts the separate duty to give the birth particulars within 42 days on "every parent"
or a legal guardian, not on the doctor or hospital. A home birth is reported by the
parents and the occupier who knows of it; if the baby is brought to hospital within
24 hours, the hospital and its doctors become responsible as well, without releasing
the parents (s 7(3)). Asserted.

### 2. Who you report to depends on where it happened

A birth goes to the Registrar-General (ss 7(4), 10(4)). A death or stillbirth in
Singapore that is not a reportable death goes to "a medical practitioner" (ss 22(3),
32(3)), who must examine the body and send the particulars to the Registrar-General
within 24 hours (ss 23(2), 33(1)(b)). A death or stillbirth on an aircraft, vessel or
train bound for Singapore goes "to the police" (ss 26(3), 35(3)). Section 22 applies
only where the death "is not, or does not appear to be, a reportable death"; s 31
leaves the Coroners Act duties untouched. Asserted.

### 3. In a hospital, the hospital alone reports a death; outside, the circle widens

s 22(2): a hospital death is reported by the hospital. In other premises, by a
relative present at the death and an occupier who knows of it. In "any other place",
by every relative who knows, every person present, and every person who takes charge
of the body — so a bystander at a street death is responsible, but a bystander in a
house is not. s 32(2) repeats the list word for word for stillbirths. Asserted.

### 4. A child's name can be changed once, in the first year, while the child lives

s 21: a name entered at registration may be altered on an application made "within
one year after the child's birth", only if it "has not been altered before" under s 21
and "the child is not deceased". A birth registered without a name can have one added
for 7 years (s 20), and the duty to supply it runs for the same 7 years (s 8(1A)(a),
added by Act 2 of 2024). The Registrar-General may refuse a name resembling a title,
rank or award, an obscene or offensive name, one contrary to the public interest, or a
patronymic or matronymic marker that does not match the child's sex (s 19(2)). The
name must be in the modern English alphabet, plus any "permitted character" gazetted by
the Registrar-General (s 19(1), s 2(1)); the length limit is that of the electronic
register and is not stated in the Act. Asserted.

### 5. No duty to give particulars for a child who dies within 42 days

s 8(2): "Subsection (1) does not apply in the case of a child who dies within 42 days
after the child's birth." The 42-day offence carries $1,500 or one month, and $50 a day
for continuing after conviction (s 8(4)). Asserted (the daily fine is not).

### 6. A stillbirth is 24 weeks, no sign of life, and not a termination

s 2(1): a stillborn child "issues from the child's mother after the twenty-fourth week
of pregnancy" and shows no sign of life after delivery, and the definition excludes "a
foetus that is aborted by or through treatment carried out for termination of
pregnancy" (the definition carries an Act 2 of 2024 annotation; which words that
amendment added is not shown in the deposit). READING: "after the twenty-fourth week" is
taken as 24 or more completed weeks; the text could also be read as more than 24.
Asserted on that reading.

### 7. The penalties are light for reporting, heavy for lying

Failing to report: $1,500 or one month. A doctor late with death or stillbirth
particulars: a fine up to $1,000 and no imprisonment (ss 23(3), 33(2)). A false or
misleading statement made knowingly or recklessly: $10,000 or 10 years (s 48).
Obstruction: $2,500 or 3 months (s 51). The reporting offences carry a "without
reasonable excuse" defence, but, unlike s 5 of the Coroners Act 2010, the Act does not
say who must prove it. Asserted.

### 8. A consequential amendment points at a provision that no longer exists

s 68(b) inserted into the National Registration Act 1965 a definition of "permitted
character" by reference to "section 19(3) of the Registration of Births and Deaths Act
2021". s 19(3) is marked "[Deleted by Act 2 of 2024 wef 16/04/2024]", and the
definition now sits in s 2(1). Whether the National Registration Act was itself updated
was not checked. Not asserted.

## The father's particulars (added 11 October 2026 for REQ-0272)

REQ-0272 (Jun Hao scenario, event j051, 22 January 2033) asks: a child is born to
parents not married to each other; may the father's name and particulars be entered
in the register, and on whose request? The expectation was "yes, at the joint request
of both parents". Module `rbda-father-particulars.l4`, cases
`rbda-cases-father-particulars.l4` (54 assertions; the first four are REQ-0272's own).

### 1. The Act does not answer the question; it hands it to regulations and the Registrar-General's website

There is no provision on registering a father's particulars where the parents are not
married. The word "father" does not occur in the Act, nor does "joint request". The
particulars to be entered are "birth particulars" (s 2(1)): those "required by or
under this Act" and those the Registrar-General "specifies on a prescribed website",
which may differ "for children in different circumstances" (s 2(2)). The Minister's
power to prescribe "particulars to be recorded in registers" and "recording of
particulars in registers after registration" is s 61(2)(a). So the answer is in the
Registration of Births and Deaths Regulations and/or on the Registrar-General's
website, neither of which is deposited. **REQ-0272 is addressed, not satisfied.**
The "joint request of both parents" rule is, from memory and not checked, s 10 of the
repealed Registration of Births and Deaths Act (Cap. 267), repealed by s 62; it was
not carried into the 2021 Act's text. Asserted (as "the Act does not say" and "the
Act requires no joint request").

### 2. On whose request: anyone may give the particulars, and the father is himself under the duty

s 9(1): the Registrar-General must register "after receiving the child's birth
particulars (whether from a responsible person mentioned in section 8(1) or any other
person)". s 8(5)(a) makes "every parent" a responsible person who must give the
particulars within 42 days (s 8(1)); one parent's compliance discharges the other
(s 8(3)). INFERENCE: "parent" is undefined, and nothing reads out an unmarried father,
so Jun Hao is under the duty and may give the particulars alone. Whether the
Registrar-General will then *enter* him without the mother's concurrence is the point
left to the regulations. Asserted.

### 3. The parents' marriage changes nothing the Act says at first registration

The only provision of the Act that rules on whose particulars go in as parents is
s 16, and it is about the Status of Children (Assisted Reproduction Technology) Act
2013: a court order under that Act governs; otherwise that Act governs if the
Registrar-General is satisfied and hears of no dispute; failing that, the birth may be
registered under s 9(2) "without entering the particulars of either or both of the
parents". Asserted, with the marriage flag shown to be inert.

### 4. Registration may go ahead with the father missing, and the duty to supply him runs on

s 9(2) lets the Registrar-General register on incomplete particulars; s 8(1A)(b) keeps
a responsible person's duty to give any missing particular alive until it is given;
s 38(2) treats recording an omitted particular later as an "alteration", lawful only
"as authorised by or under this Act" (s 38(1)). INFERENCE: these bite on the father's
particulars only if the regulations or website make them a birth particular in his
case. s 40(3) also lets "any person" ask for an error of fact in the births register to
be corrected. Asserted.

### 5. If the parents later marry, one parent alone may apply to re-register, and the child's name may change to reflect paternity

s 15: a child legitimated under the Legitimacy Act 1934 by the parents' marriage after
registration may be re-registered on the application of "a parent" while a minor (the
child, or a parent with the child's consent, once adult). The application may change
the name "only to the extent of altering the subject person's name ... to reflect the
paternity" (s 15(3)), subject to s 19. This is the only place the Act touches the
child's surname following the father. Asserted. Whether the child is legitimated is a
Legitimacy Act question, not encoded here.

### Needs subsidiary legislation

The Registration of Births and Deaths Regulations made under s 61 (the 2022
Regulations, name from memory, not deposited), and the Registrar-General's
prescribed-website specification of birth particulars under s 2(1)(b) and (2) --
specifically, whether and on whose request or consent an unmarried father's
particulars are entered at first registration or added later.

## What would need doing before this is worth anything

- The Registrar-General's discretions (refusing a name, registering on incomplete
  particulars, s 9(2)) are modelled as plain conditions; nothing on how they are used.
- Registration in conveyance cases (ss 11-13) and the adoption and legitimation
  routes (ss 14-18) were read only in passing and are not encoded.
- "Within one year" and "within 3 months" are tested on whole months away from the
  boundary; exact day-counting is not modelled.
- No regulations, prescribed websites or Registrar-General notifications were read.
