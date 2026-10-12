# Singapore Academy of Law Act 1988 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the finished naive rows. The `writing-l4-rules` skill was not available in this
session, so the example rows stood in for it. No pipeline, no coverage table, no
independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SALA1988.txt`. The cover says it "incorporates all
amendments up to and including 1 December 2021"; the deposit is marked "Informal
Consolidation – version in force from 17/4/2025". The latest amendment annotated is
Act 37 of 2023, in force 17 April 2025, which brought in lawyers (NP).

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0206** in `subjects/sg/requirements.jsonl`. It sits in Tier 3
of the remaining Singapore Acts, which are ordered by how much they touch everyday
life. The requirement asks what the Act decides for a person or business it applies
to. No scenario has asked anything more specific yet.

For an individual, what the Act decides is mostly membership. This row covers who is a
member and who a Fellow (ss 11, 12, 14), disqualification, suspension and reinstatement
(s 16), interest on late subscriptions (s 17), termination (s 18), who can be appointed
to the Senate (s 5(2), (3)), the Senate's size, quorum and votes (ss 5(1), 9), the Law
Society nominee on committees (s 10(5), (6)), the offence of obstructing the auditor
(s 22(7)) and the bar on actions (s 26).

Not encoded: the Academy's functions and powers (s 4, including appointing notaries
public and commissioners for oaths and authenticating documents for use abroad), the
Senate's general powers and staff (ss 7, 8), accounts and financial statements
(ss 19–21), the auditor's other duties (s 22(1)–(6)), the tax exemption (s 23), the
seal (s 24), debt recovery (s 25) and rule-making (s 27).

## What the Act turns out to say

### 1. Membership is automatic, and so is the bar on suing

Under s 14, every advocate and solicitor (with or without a practising certificate),
lawyer (NP), Judicial Service, Legal Service or PD Officer, and registered or approved
foreign lawyer becomes an ordinary member "without election, admission or appointment
by the Senate". Under s 17(1) every member must pay the annual subscription the Senate
sets. Under s 26(1), no action can be "maintained against the Academy and the members
of the Senate" by an advocate and solicitor, lawyer (NP), member, qualified person or
eligible person over the Senate's official acts. The bar lists who it covers, so a
member of the public is not barred by this section. Asserted.

### 2. A lawyer admitted ad hoc is not a member

The s 2 definition of "advocate and solicitor" "excludes any person admitted ad hoc
under section 15 of the Legal Profession Act 1966", so admission ad hoc does not bring
a person into s 14(a). Asserted.

### 3. Striking off ends membership, but reinstatement restores it automatically

Under s 16(1)(a), a person who "has been struck off" ceases to be a member. Under
s 16(4) and (4A), the person "on being reinstated to the roll ... becomes a member of
the Academy". Section 16(5) keeps the Senate's power to terminate that membership under
s 18. The encoding reads reinstatement as curing paragraph (a) only, so a reinstated
lawyer who also has a fraud conviction stays disqualified. That is an inference: the
text does not say how (4) interacts with the other paragraphs. Asserted.

### 4. An ordinary member cannot be "elected" a Fellow

Section 12(d) lets the Senate elect only "honorary or associate members" as Fellows.
An ordinary member becomes a Fellow through office (paragraphs (a)–(c)) or by being
appointed Senior Counsel (paragraph (e)). Holding high office since 1 January 1980
counts only after "at least 2 years", so a Solicitor-General who served 18 months does
not qualify by that route. Asserted.

### 5. Suspension from practice suspends membership, and so does a bar on re-applying

Under s 16(3), membership is "deemed to be suspended" for the period of a suspension
from practice. Section 16(3A), added in 2023, does the same while an order prohibits
the member from applying for admission. Asserted.

### 6. Late subscriptions: 30 days' grace, then interest at a rate the Senate sets

Under s 17(3), interest is payable only if the subscription is not paid "within 30
days" of falling due, and only "(if any)" at the Senate's rate. Under s 17(4) the
Senate may waive the subscription altogether. The encoding treats payment on day 30 as
within time, which is an inference. Under s 18(2), a member cannot be expelled without
first being given "an opportunity to give an explanation in writing". Asserted.

### 7. The Senate grows with the Bench, and a tie goes to the chair

The Senate (s 5(1)) is made up of the Chief Justice, every Supreme Court Judge, the
Attorney-General, every Deputy Attorney-General, the Solicitor-General, the president
of the Law Society, three law deans and nine appointees. With 20 Judges and 3 Deputy
Attorneys-General, that is 39 members. Counting the Chief Justice separately from the
Judges is an inference. A quorum is "a majority of the members" (s 9(2)), and the
presiding member has a casting vote on a tie (s 9(4)). Each appointee must be a member
of the Academy and a citizen, and serves for one year (s 5(2), (3)). Asserted.

### 8. Obstructing the auditor: reasonable cause excuses refusing, not hindering

Under s 22(7), an officer commits an offence by refusing or failing "without any
reasonable cause" to give the auditor access or information, or by otherwise
hindering, obstructing or delaying the auditor. The "otherwise hinders" limb has no
reasonable-cause words attached. The maximum fine is $5,000 plus up to $100 "for every
day or part of a day" the offence continues after conviction. Asserted.

### 9. Every committee needs a Law Society nominee with 7 years' standing

Under s 10(5), every committee or board must include a practising advocate and
solicitor with an aggregate of 7 years as a practitioner, Judicial Service Officer or
Legal Service Officer, nominated by the Law Society Council. That requirement does not
apply if a Council member already sits on it (s 10(6)). Asserted.

## What would need doing before this is worth anything

- The Legal Profession Act 1966 definitions this Act borrows ("qualified person",
  "eligible person", "lawyer (NP)", "foreign lawyer", the rolls) were not read, so
  the s 14 and s 26 categories are taken at face value.
- No rules made under s 27 (subscription classes, interest rate, circulation of
  financial statements) were retrieved.
- The interaction of s 16(4) reinstatement with the other paragraphs of s 16(1), and
  the question of whether s 16 reaches ex officio Fellows, are inferences that need a
  lawyer's reading.
- No case law was searched.
