# Canada Business Corporations Act (R.S.C. 1985, c. C-44), piece cb5: Parts XIX to XXI, the Schedule, the Related Provisions and the Amendments Not in Force

Status, 2026-10-22: layer 1 (eleven modules and ten test files) and layer 2 (`cb5-seat.l4` and `cb5-cases-seat.l4`) are written, and `check.sh` and `srcrefs.py` were run over them; their output is under `## What check.sh prints`.
Nothing here has been used by anyone yet.

The text this was encoded from is a plain-text rendering of the Department of Justice Canada consolidation current to 2026-09-30 (last amended 2026-03-26).
It is an unofficial rendering, and nothing here has been verified against the official text.
The encoded source is `../../registers/source-bundle/R.S.C.-1985-c.-C-44.txt`, lines 2862 to 3671, and the `src:N` locators are lines of that file.
Contains information licensed under the Open Government Licence - Canada.

Dates.
The range contains no date of enactment or of coming into force of the Act itself.
The Related Provisions leave the coming into force of several amending Acts to the text of those Acts, which is not among the sources, so every such date (for example the day section 115 of S.C. 2001, c. 14 came into force) is a stated input of the rule that needs it, named as such.
The amendments that the source shows as not in force carry no date either and are inert rows.

## Seat

The seat is a person who incorporates, directs or holds shares in a corporation under the Act: an incorporator, a director or officer, or a shareholder (including a minority shareholder), asking what the Act lets them do, what it requires of them, what they may require of the corporation, and what can be done to them.
Why this seat: Parts XIX to XXI are the Act's enforcement and housekeeping Parts.
They hold the investigation of a corporation, the court's remedies for a shareholder (the derivative action, the oppression remedy, rectifying the registers, compliance orders, appeals), the offences, the rules for electronic documents, the rules for notices and certificates, dealings with the Director, and the continuance of bodies incorporated under other Acts of Parliament.
Almost every question a person puts to these Parts begins with "may I apply to the court", "must I give notice", "what can be done to me" or "what is the Director bound to do for me".

How layer 2 is built.
Every question takes plain inputs (yes or no, a number, a date, or one of the module's own choices), each with an `@desc` worded as the person would be asked.
The records and parties that the layer-1 rules expect (a `Party`, a list of close-of-business positions, a `MAYBE` date) are built inside the question, in its `WHERE`, from those answers, and the same layer-1 rule is then called.
No rule is restated.
Where the Act hands a judgment to the court, the Director or an inspector ("it appears to the court that", "the Director is satisfied that", "the court considers it just and reasonable"), the question asks whether that judgment has been made, or would be, and the answer is conditional on it.
Where the Act leaves a number or a form to the regulations (the prescribed amount in s 237.5(1)(b), the fee and its time, the prescribed period for keeping documents), the question asks for it as a fact.
No official has a seat: the Director's, an inspector's and the court's powers and duties appear only as what the person is owed or exposed to.

Pairs (Hohfeld).
A claim of the person is asked beside the duty on the other side, and a power over the person beside the person's liability.
Examples: Q3 (must I give the Director notice of my application) with Q4 (have I complied) and Q5 (has the Director a right to be heard); Q15 (am I excused from giving evidence) with Q16 (can it be used against me); Q18 (the Director may require me to report ownership) with Q19 (have I made the report); Q36 and Q37 (the plaintiff's power to reallocate and the court's) with Q38 (my immunity above half of what was awarded against me); Q77 (the Director's notice of refusal) with Q78 (whether it was given in time) and Q79 (whether the Director is deemed to have refused); Q130 (what the Director owes me once I send articles) with Q140 and Q127 (what the Director may do to my documents).
The paired questions are listed here as numbers of the list below.

The questions, grouped under the same `§§` headings as `cb5-seat.l4`, in the text's order (185 in all):

**Investigation (Part XIX)**

1. May I apply to the court for an investigation of the corporation (s 229(1))?
2. May the court order an investigation of the corporation (s 229(2))?
3. Must I give the Director notice of my application for an investigation (s 229(3))?
4. Have I complied with my duty to give the Director notice of my application for an investigation (s 229(3))?
5. Is the Director entitled to appear and be heard on my application for an investigation (s 229(3))?
6. Must I give security for costs on my application for an investigation (s 229(4))?
7. Must my application for an investigation be heard in camera (s 229(5))?
8. May I publish something about ex parte proceedings for an investigation (s 229(6))?
9. May the court make this kind of order in an investigation of the corporation (s 230(1))?
10. Can the inspector use this power over me (s 231(1))?
11. May the inspector pass what I told them on to another public official (s 231(2))?
12. Am I entitled to a copy of the order that appointed the inspector (s 231(3))?
13. May I apply to the court for an in camera hearing and directions (s 232(1))?
14. Do I have a right to be represented by counsel at the inspector's hearing (s 232(2))?
15. Am I excused from giving evidence to an inspector because it may incriminate me (s 233)?
16. Can what I tell an inspector be used against me later (s 233)?
17. Am I protected by absolute privilege for what I say or write in an investigation (s 234)?
18. Can the Director require me to report who owns or controls a security (s 235(1))?
19. Have I made the report the Director required of me (s 235(1))?
20. Am I deemed to have an interest or right in a security (s 235(2))?
21. Will the Director publish the particulars I reported (s 235(3))?
22. Am I guilty of an offence if I do not give the report the Director requires (s 235(4))?
23. What is the largest fine I could face for failing to give the report (dollars) (s 235(4))?
24. What is the longest imprisonment I could face for failing to give the report (months) (s 235(4))?
25. As a director or officer, am I guilty when my body corporate fails to give the report (s 235(5))?
26. What is the largest fine I could face as a director or officer who authorized the failure to report (dollars) (s 235(5))?
27. What is the longest imprisonment I could face as a director or officer who authorized the failure to report (months) (s 235(5))?
28. Does the investigation Part take away my solicitor-client privilege (s 236)?
29. Can the Director make inquiries of me and require records (s 237(1))?
30. Have I complied with my duty to respond to the Director's inquiry (s 237(2))?

**Apportioning an award of damages (Part XIX.1)**

31. Is what I hold a financial interest for the apportionment Part (s 237.1)?
32. Is my loss a financial loss for the apportionment Part (s 237.1)?
33. Am I a third party for the apportionment Part (s 237.1)?
34. Does the apportionment Part govern the damages awarded in my claim (s 237.2; S.C. 2001, c. 14, s. 233)?
35. How much of the damages am I liable for as a defendant (dollars) (s 237.3(1))?
36. By what day may the plaintiff apply to reallocate an uncollectable amount (s 237.3(2))?
37. May the court reallocate an uncollectable amount to me as another responsible defendant (s 237.3(2))?
38. What is the most that can be reallocated to me (dollars) (s 237.3(3), (4))?
39. Can the plaintiff recover the whole of the damages from me because I acted fraudulently or dishonestly (s 237.4(1))?
40. Am I entitled to claim contribution from the other defendants after a fraud finding against me (s 237.4(2))?
41. Are the defendants jointly and severally liable to me as an investor (s 237.5)?
42. Is my body corporate a personal body corporate (s 237.5(2)(a))?
43. Am I in a common-law partnership with this person for the apportionment Part (s 237.5(2)(b))?
44. May the court hold the defendants jointly and severally liable to me even though my holding is above the prescribed amount (s 237.6)?
45. On what basis am I liable for the damages awarded (s 237.3(1), s 237.4 to s 237.6)?
46. What is the value of my security for the apportionment Part (dollars) (s 237.7)?
47. May the court adjust the value of my security (s 237.7(2))?
48. As of what day is the value of my security determined (s 237.7(3))?
49. Is this an organized market for my security (s 237.7(4))?
50. Must the court determine the value of my financial interest itself (s 237.8(1))?
51. May I ask the court to determine the value of my financial interest (s 237.9)?

**Remedies (Part XX)**

52. Am I a complainant who may use the remedies Part (s 238)?
53. Is this an action under the remedies Part (s 238)?
54. May I apply to the court for leave to bring an action in the corporation's name (s 239(1))?
55. Have I given the directors enough notice before applying for leave (s 239(2)(a))?
56. May the court let the action be brought for the corporation (s 239(2))?
57. May the court make this kind of order in a derivative action (s 240)?
58. May I apply to the court for relief from oppression (s 241(1))?
59. May the court make an order to rectify what I complain of as oppressive (s 241(2))?
60. May the court make this kind of order on my oppression application (s 241(3))?
61. As a director, must I comply forthwith with the articles-amendment duty after an oppression order (s 241(4)(a))?
62. Is another amendment to the articles or by-laws barred, without the court's consent, after such an order (s 241(4)(b))?
63. Am I barred from dissenting under section 190 from an amendment to the articles made under the oppression section (s 241(5))?
64. Must the corporation hold back a payment to me as a shareholder under an oppression order (s 241(6))?
65. May I apply in the alternative for a dissolution order when I apply for relief from oppression (s 241(7))?
66. Can my application or action be stayed or dismissed only because the shareholders approved the breach (s 242(1))?
67. May the court take the shareholders' approval of the breach into account (s 242(1))?
68. Do I need the court's approval to stay, discontinue, settle or abandon my application or action (s 242(2))?
69. May the court order notice to me before a step is taken in an application or action (s 242(2))?
70. Must I give security for costs in my application or action under the remedies Part (s 242(3))?
71. May the court order the corporation to pay my interim costs (s 242(4))?
72. Can I be held accountable for the interim costs when my case ends (s 242(4))?
73. May I apply to the court to rectify the registers or records of the corporation (s 243(1))?
74. Must I give the Director notice of my application to rectify the registers (s 243(2))?
75. Is the Director entitled to appear and be heard on my application to rectify the registers (s 243(2))?
76. May the court make this kind of order on an application to rectify the registers (s 243(3))?
77. By what day must the Director give me written notice that it has refused to file my document (s 245(1))?
78. Has the Director given me written notice of the refusal in time (s 245(1))?
79. Is the Director deemed to have refused to file my document (s 245(2))?
80. May I apply to the court about this decision of the Director (s 246)?
81. May the court make any order it thinks fit on my appeal from the Director's decision (s 246)?
82. May I apply to the court for an order that the corporation or one of its people comply with the Act (s 247)?
83. As a director or officer, can a complainant or creditor ask the court to order me to comply (s 247)?
84. May my application be made in a summary manner (s 248)?
85. Can I appeal an order made under the Act, and do I need leave (s 249)?

**Offences and punishment (Part XX)**

86. Am I guilty of an offence for a false or misleading report, return, notice or document (s 250(1), (3), (4))?
87. What is the largest fine I could face for a false or misleading document (dollars) (s 250(1))?
88. What is the longest imprisonment I could face for a false or misleading document (months) (s 250(1))?
89. As a director or officer, am I guilty when my body corporate files a false or misleading document (s 250(2))?
90. What is the largest fine I could face as a director or officer who authorized the false or misleading document (dollars) (s 250(2))?
91. What is the longest imprisonment I could face as a director or officer who authorized the false or misleading document (months) (s 250(2))?
92. Am I guilty of an offence for contravening a provision that has no stated punishment (s 251)?
93. Does the Act itself state a maximum punishment for the general offence (s 251)?
94. Can the court order me to comply with the Act after I am convicted (s 252(1))?
95. By what day can a prosecution be brought against me for an offence under the Act (s 252(2))?
96. Is it too late to prosecute me for an offence under the Act (s 252(2))?
97. Is my civil remedy suspended or affected because the same act is an offence under the Act (s 252(3))?

**Electronic documents (Part XX.1)**

98. Is this an electronic document within the electronic-document rules (s 252.1)?
99. Is this an information system within the electronic-document rules (s 252.1)?
100. Do the electronic-document rules cover this notice or document (s 252.2)?
101. Can the Act or the regulations force me to create or provide an electronic document (s 252.3(1))?
102. Does an electronic document count as my having been given a notice (s 252.3(2))?
103. As the corporation, have I satisfied my duty to give a shareholder a notice by sending an electronic document (s 252.3(2), s 252.4)?
104. Does my withdrawal of consent to electronic documents take effect (s 252.3(3))?
105. Can I use an electronic document to create or provide a document the Act requires (s 252.4)?
106. Does an electronic document satisfy a requirement that I create a document in writing (s 252.5(1))?
107. Does an electronic document satisfy a requirement that I be provided with a document in writing (s 252.5(2))?
108. Does one electronic version satisfy a requirement to give me several copies at once (s 252.5(3))?
109. Does sending an electronic document satisfy a requirement to send something by registered mail (s 252.5(4))?
110. May I make my statutory declaration or affidavit as an electronic document (s 252.6(1))?
111. Is this an electronic document for the purposes of a statutory declaration or affidavit (s 252.6(2))?
112. Does an electronic signature satisfy the Act's requirement for my signature (s 252.7)?

**Notices to and from the corporation (Part XXI)**

113. Has the corporation sent me a notice in a way the Act allows (s 253(1))?
114. Am I presumed to be a director of the corporation because I am named in a filed notice (s 253(2))?
115. On what day am I treated as having received a notice mailed to me (s 253(3))?
116. Can the corporation stop sending me notices because they keep coming back (s 253(4))?
117. May I send a notice or document to the corporation, or serve it, by registered mail (s 254)?
118. On what day is my notice to the corporation treated as received or served (s 254)?
119. Can the sending of a notice to me, or its time, be waived (s 255)?
120. Is a certificate of the Director signed validly (s 256(1))?
121. How much proof is a certificate of the Director (s 256(2))?
122. May a certificate issued for the corporation be signed by me (s 257(1))?
123. How much proof is a certificate, extract or minutes of the corporation (s 257(2))?
124. Does the securities register show that I own my shares (s 257(3))?

**Dealing with the Director (Part XXI)**

125. May I send the Director a photocopy of a document the Act requires (s 258)?
126. Can the Director excuse me from sending certain notices or documents (s 258.2)?
127. Can the Director require me to prove a document I sent (s 259(1))?
128. Is my document properly verified (s 259(2))?
129. When must I pay the Director's fee (s 261.1)?
130. Is the Director now bound to do this on my articles or statement (s 262(2))?
131. Is a statement of intent to dissolve, or of its revocation, a statement for the Director's certificate (s 262(1))?
132. Can the Director's certificate be dated as of the day I name (s 262(3))?
133. Can a certificate of discontinuance be dated as of the day I name (s 262(5))?
134. Is a mechanically reproduced signature on the Director's certificate allowed (s 262.1(1))?
135. If several of us sign separate copies, are they one document (s 262.1(3))?
136. Must the Director publish a notice that my application was granted (s 262.2)?
137. Has the corporation complied with its duty to send the Director an annual return (s 263)?
138. May I ask the Director for a certificate of this statement about a corporation (s 263.1(1))?
139. May the Director refuse me a certificate of existence because the corporation is in default (s 263.1(2))?
140. May the Director alter a document I sent (s 264)?
141. Must the directors or shareholders pass resolutions to correct an error the Director has pointed out (s 265(1))?
142. May the Director go ahead with a correction without those resolutions (s 265(2))?
143. May the Director accept the correction I have asked for (s 265(3))?
144. May I apply to the court for an order that a document be corrected (s 265(4))?
145. Must I give the Director notice of my application to the court to correct a document (s 265(5))?
146. Can the Director demand that I surrender the original document when it is corrected (s 265(6))?
147. What date does a corrected document bear (s 265(7))?
148. Must the Director tell people about a correction that materially changes a certificate (s 265(8))?
149. May the Director cancel articles and the related certificate (s 265.1(1))?
150. May the Director go ahead with a cancellation without further steps (s 265.1(2))?
151. May the Director cancel articles at my request (s 265.1(3))?
152. May I apply to the court for an order that articles be cancelled (s 265.1(4))?
153. Must I give the Director notice of my application to cancel articles (s 265.1(5))?
154. Can the Director demand that I surrender a cancelled certificate (s 265.1(6))?
155. Am I entitled to examine and copy a document the Director holds (s 266(1))?
156. Must the Director give me a copy or extract I ask for (s 266(2))?
157. Is what I tell the Director about wrongdoing a wrongdoing within the Act (s 266.1(3))?
158. Must the Director keep secret the information I gave about a wrongdoing (s 266.1(1))?
159. May the Director pass the information I gave on to this recipient (s 266.1(2))?
160. Must the Director keep the document I sent (s 267(1))?
161. If the Director keeps documents electronically, must I be given a copy in readable form (s 267(2)(a))?
162. Is a report reproduced from the Director's electronic records admissible in evidence (s 267(2)(b))?
163. Is the Director still required to keep or produce this document (s 267(3))?
164. May the Director make documents available by an electronic system (s 267.1)?

**Bodies incorporated under other Acts of Parliament (s 268)**

165. Is this document my body corporate's charter (s 268(1))?
166. Is my body corporate treated as incorporated under an Act of Parliament other than this Act or a special Act (s 268(4.2))?
167. Can the shareholders of my special-Act body corporate amend its charter by special resolution on a continuance (s 268(2))?
168. Can the shareholders of my other-Act body corporate amend its charter by special resolution on a continuance (s 268(2.1))?
169. Can the shareholders make this change to a class or series of shares by special resolution on a continuance (s 268(3))?
170. Can the directors of my special-Act body corporate apply for a certificate of continuance despite the charter (s 268(4))?
171. Can the directors of my other-Act body corporate apply for a certificate of continuance (s 268(4.1))?
172. Am I barred from dissenting under section 190 from an amendment made on a continuance under section 268 (s 268(5))?
173. Can the Governor in Council require my body corporate to apply for a certificate of continuance (s 268(6))?
174. Is my body corporate dissolved because it did not apply for continuance in time (s 268(9))?
175. Does my body corporate escape the continuance fees (s 268(8))?
176. Does the special Act stop applying to my body corporate once it is continued (s 268(8.1))?
177. May my body corporate apply for a certificate of continuance under the Act (s 268(10), (11))?

**The Schedule**

178. Is the offence in question one the Schedule lists?

**Related provisions**

179. Is my proceeding that began before the 1985 amendments continued under the amended provisions (R.S. 1985, c. 27 (2nd Supp.), s. 11)?
180. Is my proceeding that began before the 1990 amendments taken up under the amended provision (S.C. 1990, c. 17, s. 45(1))?
181. Is my proceeding that began before the 1998 amendments taken up under the amended provision (S.C. 1998, c. 30, s. 10)?
182. Does the 1994 amendment to subsection 125(1) apply to this year (S.C. 1994, c. 21, s. 125(2))?
183. Was the continuance of my railway company before 1996 valid despite its being incorporated under an Act of Parliament (S.C. 1996, c. 10, s. 214)?
184. By what day must my body corporate apply for continuance (S.C. 2009, c. 23, s. 297(6))?
185. Is my body corporate dissolved because it did not apply for continuance in the six months (S.C. 2009, c. 23, s. 297(6))?

One seat question answers less than its rule can: Q41 (s 237.5) builds the list of close-of-business positions that the layer-1 rule reads from at most one acquisition in the period, so a plaintiff with several acquisitions asks once for each; the rule's reading of `any day that the plaintiff acquired a financial interest` makes a yes for any one of them enough.
The cases, `cb5-cases-seat.l4`, have 551 assertions, at least one for every question, and most with an answer of yes and an answer of no.
The cases for which the Act gives no answer (a security with no price on an organized market, a notice that cannot be treated as received, a Schedule offence with no maximum figure) assert `NOTHING` or a plain no, and say so beside them.

## Jural relations

One row for each provision that creates a relation between two parties, then one row for each provision that creates none (marked `none`).
Where a provision creates two relations (for example s 229(3): a claim to notice, and a claim to be heard) it has two rows.
137 rows in all.
The Hohfeld names used: a claim is correlative to a duty, a privilege to a no-right, a power to a liability, an immunity to a disability.

| section | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | L4 rule |
| --- | --- | --- | --- |
| s 229(1) | power of a security holder or the Director to apply to the court for an order directing an investigation | liability of the corporation and its affiliated corporations to be investigated | `may apply for an order directing an investigation within s 229(1)` |
| s 229(2) | power of the court to order an investigation, once one of four grounds appears to it | liability of the corporation and its affiliated corporations | `the court may order an investigation within s 229(2)` |
| s 229(3) | claim of the Director to reasonable notice of the application | duty of the security holder who applies | `the applicant must give the Director reasonable notice within s 229(3)`; `the applicant has complied with the duty to notify the Director within s 229(3)` |
| s 229(3) | claim of the Director to appear and be heard in person or by counsel | duty of the court to hear the Director | `the Director is entitled to appear and be heard within s 229(3)` |
| s 229(4) | immunity of the applicant from any requirement to give security for costs | disability of the court and of the corporation to require it | `an applicant under s 229 is required to give security for costs within s 229(4)` |
| s 229(5) | claim of the applicant and the corporation to an in camera hearing of an ex parte application | duty of the court to hear it in camera | `the application must be heard in camera within s 229(5)` |
| s 229(6) | claim of the corporation being investigated that nothing about ex parte proceedings be published; the court's and the corporation's power to authorize or consent | duty of every person not to publish without the court's authorization or the corporation's written consent | `publishing anything relating to the proceedings is permitted within s 229(6)` |
| s 230(1) | power of the court to make any order it thinks fit in connection with an investigation, including the twelve listed kinds | liability of the corporation, the inspector, any interested person and any person ordered | `the court may make an order of the kind within s 230(1)` |
| s 230(2) | claim of the Director to a copy of every report of an inspector | duty of the inspector | `the inspector has complied with the duty to send the Director a copy of a report within s 230(2)` |
| s 231(1) | power of the inspector, of exactly the powers set out in the order appointing the inspector | liability of the persons the order reaches | `an inspector has the power within s 231(1)` |
| s 231(2) | privilege of the inspector to furnish information to, and cooperate with, a public official investigating the same or similar conduct | no-right of the corporation and the persons investigated to object | `an inspector may furnish information to or exchange it with the official within s 231(2)` |
| s 231(3) | claim of an interested person, on request, to a copy of any order made under s 230(1) | duty of the inspector | `the inspector must produce a copy of the order within s 231(3)` |
| s 232(1) | power of an interested person to apply to the court for an in camera hearing and for directions | liability of the inspector and of the other persons to the court's order | `an interested person may apply to the court for an in camera hearing and directions within s 232(1)` |
| s 232(2) | claim of a person whose conduct is being investigated, or who is being examined, to be represented by counsel | duty of the inspector (and the court) to allow it | `the person has a right to be represented by counsel within s 232(2)` |
| s 233 (first limb) | claim of the inspector to attendance, evidence and documents even though they tend to criminate | duty of every person called, who has no excuse by reason only that the evidence tends to criminate | `a person is excused from giving evidence by reason only that it tends to criminate within s 233` |
| s 233 (second limb) | immunity of the person against the later use of the evidence given, in a later proceeding under an Act of Parliament (not perjury under s 132 or s 136 of the Criminal Code) | disability of the prosecutor and the court to use or receive it | `the use of the evidence within s 233` |
| s 234 | immunity of the inspector and any other person from liability for what they say or write in an investigation (absolute privilege) | disability of anyone defamed to sue on it | `the statement or report has absolute privilege within s 234` |
| s 235(1) | power of the Director to require a report of interests and rights in a security (and claim to the report) | liability of the person the Director reasonably believes has or had an interest, and duty of that person to make the report | `the Director may require the person to report within s 235(1)`; `the person has made the report required within s 235(1)` |
| s 235(2) | none: a deeming rule: it widens the class of persons s 235(1) reaches; the relation is the one of s 235(1) | none | `the person is deemed to have an interest or right in the security within s 235(2)` |
| s 235(3) | claim of the public that the Director publish the particulars | duty of the Director | `the Director must publish the particulars within s 235(3)` |
| s 235(4) | power of the court to convict and to impose a fine up to $5,000, imprisonment up to six months, or both | liability of the person who fails to comply | `the person is guilty of an offence within s 235(4)`; `the most the court may impose within s 235(4)` |
| s 235(5) | power of the court to convict and punish as in s 235(4) | liability of the director or officer who knowingly authorized, permitted or acquiesced | `the director or officer is a party to and guilty of the offence within s 235(5)`; `the most the court may impose on a director or officer within s 235(5)` |
| s 236 | immunity of solicitor-client privilege and professional secrecy | disability of Part XIX to affect them | `Part XIX affects solicitor-client privilege or professional secrecy within s 236` |
| s 237(1) | power of the Director to make inquiries and require records or information | liability of any person | `the Director may make the inquiry and require records within s 237(1)` |
| s 237(2) | claim of the Director to a response | duty of the person inquired of | `the person has complied with the duty to respond within s 237(2)` |
| s 237.1 (three definitions), s 237.2(1) and (2) | none: definitions and the scope of the Part; they decide whether Part XIX.1 applies and create no relation of their own | none | `financial interest within s 237.1`; `financial loss within s 237.1`; `third party within s 237.1`; `Part XIX.1 applies to the apportionment within s 237.2(1)`; `Part XIX.1 does not apply to the plaintiff within s 237.2(2)` |
| s 237.3(1) | immunity of a responsible defendant or third party from liability beyond the portion matching their degree of responsibility | disability of the plaintiff to recover more from that defendant | `the portion of the damages for which a defendant or third party is liable within s 237.3(1)` |
| s 237.3(2) | power of the plaintiff, within one year after the judgment was made enforceable, to apply to reallocate an uncollectable amount; power of the court to do so | liability of the other responsible defendants and third parties | `the last day to apply to reallocate an uncollectable amount within s 237.3(2)`; `the court may reallocate the uncollectable amount within s 237.3(2)` |
| s 237.3(3), (4) | immunity of each other defendant from reallocation above fifty per cent of the amount originally awarded against them | disability of the plaintiff and the court | `the amount that may be reallocated to the other defendant or third party within s 237.3(3)`; `the most that may be reallocated to that defendant or third party within s 237.3(4)` |
| s 237.4(1) | claim of the plaintiff to the whole amount from a defendant who acted fraudulently or dishonestly | duty of that defendant | `the plaintiff may recover the whole amount of the damages from the defendant or third party within s 237.4(1)` |
| s 237.4(2) | claim of that defendant to contribution from any other defendant or third party held responsible | duty of the other defendants and third parties | `the defendant or third party is entitled to claim contribution within s 237.4(2)` |
| s 237.5(1), (1.1) | claim of an individual or personal body corporate plaintiff (a holding of at most the prescribed amount, from the day of the error or acquired before disclosure) to joint and several recovery | duty of the defendants and third parties; immunity of a partnership-member, association-member or trustee-type plaintiff's opponents under (1.1) | `the defendants and third parties are jointly and severally liable within s 237.5(1)`; `subsection 237.5(1) does not apply to the plaintiff within s 237.5(1.1)`; `the plaintiff had or acquired a financial interest in time within s 237.5(1)(a)`; `the value of the total financial interest was within the prescribed amount within s 237.5(1)(b)` |
| s 237.5(2) | none: two definitions (personal body corporate, common-law partnership) | none | `personal body corporate within s 237.5(2)(a)`; `common-law partnership within s 237.5(2)(b)` |
| s 237.6(1) | power of the court to hold the defendants and third parties jointly and severally liable where the plaintiff's holding is above the prescribed amount | liability of the defendants and third parties | `the court may hold the defendants and third parties jointly and severally liable within s 237.6(1)` |
| s 237.7(1), (3), (4) | none: valuation rules (which price, as of which day, what an organized market is); they fix a figure and create no relation | none | `the value of the security within s 237.7(1)`; `the day as of which the value is determined within s 237.7(3)`; `organized market within s 237.7(4)` |
| s 237.7(2) | power of the court to adjust the value where it considers it reasonable | liability of the parties to the adjusted value | `the court may adjust the value within s 237.7(2)` |
| s 237.8(1) | claim of the parties to a court determination of the value of an interest with resale restrictions or no organized market | duty of the court | `the court must determine the value within s 237.8(1)` |
| s 237.9 | power of the plaintiff to apply, before or during the proceedings, for the court to determine the value | liability of the defendants and third parties to the determination | `the plaintiff may apply for the court to determine the value of the financial interest within s 237.9` |
| s 238 (two definitions) | none: definitions of action and complainant; the second fixes who holds the powers of ss 239, 241, 247 | none | `action within s 238`; `complainant within s 238` |
| s 239(1) | power of a complainant to apply for leave to bring an action in the corporation's or a subsidiary's name or to intervene in one | liability of the corporation, the subsidiary and their directors | `a complainant may apply to a court for leave to act for the corporation within s 239(1)` |
| s 239(2) | claim of the directors to fourteen days' notice, and disability of the complainant to sue until the court is satisfied of notice, good faith and the corporation's interests | duty of the complainant to give notice; power of the court to grant leave | `the action may be brought or the intervention made within s 239(2)`; `the condition of notice to the directors is met within s 239(2)(a)`; `the condition of good faith is met within s 239(2)(b)`; `the condition of the interests of the corporation is met within s 239(2)(c)` |
| s 240 | power of the court to make any order it thinks fit in connection with a derivative action, including the four listed | liability of the corporation, its subsidiary and the defendants | `the court may make an order of the kind within s 240` |
| s 241(1) | power of a complainant to apply to the court for relief from oppression | liability of the corporation and its affiliates | `a complainant may apply to a court for an order within s 241(1)` |
| s 241(2) | power of the court to make an order to rectify the matters complained of | liability of the corporation and its affiliates | `the court may make an order to rectify the matters complained of within s 241(2)` |
| s 241(3) | power of the court to make any interim or final order, including the fourteen listed | liability of the corporation, the directors and any other person ordered | `the court may make an order of the kind within s 241(3)` |
| s 241(4) | claim of the court, and of the complainant who obtained the order, that the directors comply forthwith with s 191(4) and that the articles or by-laws are not amended again without the court's consent | duty of the directors; disability of the corporation to amend again without consent | `the directors must forthwith comply with subsection 191(4) within s 241(4)(a)`; `another amendment to the articles or by-laws is barred within s 241(4)(b)` |
| s 241(5) | immunity of the corporation from a dissenting shareholder's s 190 claim on an amendment under s 241 | disability of the shareholder to dissent | `a shareholder is not entitled to dissent under section 190 within s 241(5)` |
| s 241(6) | claim of the creditors that a payment to a shareholder under (3)(f) or (g) not be made when it would impair solvency | duty of the corporation not to pay | `the corporation must not make the payment within s 241(6)` |
| s 241(7) | power of the applicant to ask in the alternative for a dissolution order under s 214 | liability of the corporation | `the applicant may apply in the alternative for an order under section 214 within s 241(7)` |
| s 242(1) | immunity of the complainant's application or action from being stayed or dismissed by reason only of shareholder approval; privilege of the court to take that evidence into account in an order under s 214, 240 or 241 | disability of the court (to stay or dismiss on that ground alone) | `an application or action under Part XX is stayed or dismissed by reason only of approval by the shareholders within s 242(1)`; `the court may take evidence of approval by the shareholders into account within s 242(1)` |
| s 242(2) | claim of the complainant to the court's approval before a stay, discontinuance, settlement, dismissal or abandonment, and to notice; power of the court to order notice | duty of the parties to obtain approval; liability of a party to the court's order | `the approval of the court is required for the step within s 242(2)`; `the court may order a party to give notice to the complainant within s 242(2)` |
| s 242(3) | immunity of the complainant from any requirement to give security for costs | disability of the court and the other parties to require it | `a complainant is required to give security for costs within s 242(3)` |
| s 242(4) | power of the court at any time to order the corporation or its subsidiary to pay the complainant's interim costs, and to hold the complainant accountable at the end | liability of the corporation, its subsidiary and the complainant | `the court may order the corporation or its subsidiary to pay interim costs to the complainant within s 242(4)`; `the complainant may be held accountable for the interim costs within s 242(4)` |
| s 243(1) | power of the corporation, a security holder or an aggrieved person to apply to the court to rectify the registers or records | liability of the corporation and the persons named | `may apply to a court for an order that the registers or records be rectified within s 243(1)` |
| s 243(2) | claim of the Director to notice and to appear and be heard | duty of the applicant to give notice | `the applicant must give the Director notice within s 243(2)`; `the Director is entitled to appear and be heard within s 243(2)` |
| s 243(3) | power of the court to make orders on an application to rectify, including the four listed | liability of the corporation and the parties | `the court may make an order of the kind within s 243(3)` |
| s 244 | power of the Director to apply to the court for directions on the Director's duties | liability of the Director to the court's directions | `the Director may apply to a court for directions within s 244` |
| s 245(1) | claim of the person who sent the articles or document to written notice of the refusal, with reasons, within twenty days of receipt or of any required approval, whichever is later | duty of the Director | `the last day for the Director to give written notice of the refusal within s 245(1)`; `the Director has complied with the duty to give notice of the refusal within s 245(1)` |
| s 245(2) | power of the person to appeal under s 246 once the Director is deemed to have refused | liability of the Director (deemed refusal) | `the Director is deemed to have refused to file the document for the purposes of s 246 within s 245(2)` |
| s 246 | power of a person aggrieved by a listed decision of the Director to apply to the court, which may make any order it thinks fit | liability of the Director and the corporation to the order | `a person may apply to a court for an order on the decision within s 246`; `the court may make any order it thinks fit on the appeal within s 246` |
| s 247 | power of a complainant or creditor to apply for a restraining or compliance order | liability of the corporation and its directors, officers, employees, agents, auditors, trustees, receivers, receiver-managers, sequestrators and liquidators | `may apply to a court for a compliance or restraining order within s 247` |
| s 248 | privilege of any applicant under the Act to proceed in a summary manner | no-right of the respondent to insist on a trial | `the application may be made in a summary manner within s 248` |
| s 249 | power of a party to appeal an order made under the Act (as of right from a final order, otherwise with leave) | liability of the other party | `whether an appeal lies within s 249` |
| s 250(1), (3) | power of the court to convict and impose up to $5,000, six months, or both; immunity of one who did not know and could not have known | liability of the person who makes or assists in making a false or misleading document; disability of the court to convict the immune person | `the elements of the offence are met within s 250(1)`; `the person has the immunity within s 250(3)`; `the person is guilty of an offence within s 250(1) and s 250(3)`; `the most the court may impose within s 250(1)` |
| s 250(2) | power of the court to convict a director or officer who knowingly authorized, permitted or acquiesced | liability of the director or officer; immunity of s 250(3) also applies | `the director or officer is a party to and guilty of the offence within s 250(2)`; `the most the court may impose on a director or officer within s 250(2)` |
| s 250(4) | none: a scope rule: the register of individuals with significant control is not a report, return, notice or document for s 250 | none | `the document is a report, return, notice or other document for the purposes of s 250 within s 250(4)` |
| s 251 | power of the court to convict (summary conviction, no maximum stated in the section) | liability of the person who contravenes a provision with no punishment, without reasonable cause | `the person is guilty of an offence within s 251`; `the most the court may impose within s 251` |
| s 252(1) | power of the court to order a convicted person to comply with the Act | liability of the convicted person | `the court may order the person to comply within s 252(1)` |
| s 252(2) | immunity of the accused from prosecution begun more than two years after the subject-matter arose | disability of the prosecutor | `the last day to institute a prosecution within s 252(2)`; `the prosecution is instituted in time within s 252(2)` |
| s 252(3) | immunity of a civil remedy from being suspended or affected because the same act is an offence | disability of the defendant to rely on the offence to suspend it | `a civil remedy is suspended or affected by reason that the act or omission is an offence under this Act within s 252(3)` |
| s 252.1, s 252.2 | none: a definition of electronic document and information system, and the scope of the Part (what is sent to or issued by the Director is outside it) | none | `electronic document within s 252.1`; `information system within s 252.1`; `Part XX.1 applies within s 252.2` |
| s 252.3(1) | immunity of any person from being required by the Act or the regulations to create or provide an electronic document | disability of the Act, the regulations and the corporation to require it | `this Act or the regulations require a person to create or provide an electronic document within s 252.3(1)` |
| s 252.3(2) | claim of the addressee not to be treated as given a notice or document by electronic document unless they consented and designated an information system | duty of the person providing it | `the provision of an electronic document satisfies the requirement to provide it to the addressee within s 252.3(2)` |
| s 252.3(3) | power of the addressee to revoke the consent in the manner prescribed | liability of the person providing documents | `the revocation takes effect within s 252.3(3)` |
| s 252.4 | privilege of a person to create or provide information by electronic document where the by-laws or articles do not provide otherwise and the regulations are complied with | no-right of the addressee to insist on paper | `an electronic document satisfies the requirement to create or provide within s 252.4`; `an electronic document satisfies a requirement to provide a notice to a person within s 252.3(2) and s 252.4` |
| s 252.5(1) to (4) | privilege of a person to satisfy a requirement of writing, copies or registered mail by an electronic document on the stated conditions | no-right of the addressee to insist on paper | `an electronic document satisfies the requirement to create in writing within s 252.5(1)`; `an electronic document satisfies the requirement to provide in writing within s 252.5(2)`; `a single version of an electronic document satisfies the requirement for copies within s 252.5(3)`; `sending an electronic document satisfies the requirement to provide by registered mail within s 252.5(4)` |
| s 252.6(1) | power of the declarant and the authorized person to create a statutory declaration or affidavit as an electronic document | liability of the recipient of the document | `a statutory declaration or affidavit may be created or provided in an electronic document within s 252.6(1)` |
| s 252.6(2), (3) | none: definitions (electronic document, secure electronic signature, by reference to the federal electronic documents Act) and a clarification | none | `electronic document within s 252.6` |
| s 252.7 | power of a person to satisfy a signature or execution requirement by technology that is unique to them, attaches the signature and identifies them | liability of the recipient of the document | `a requirement for a signature or for a document to be executed is satisfied within s 252.7` |
| s 253(1) | privilege of the corporation to send a notice to a shareholder or director by prepaid mail or personal delivery to the latest address of record | no-right of the shareholder or director to insist on another way | `a notice or document may be sent in the way within s 253(1)` |
| s 253(2), (3) | none: a presumption of fact about who is a director, and a counting rule for the day of receipt | none | `the person is presumed to be a director of the corporation within s 253(2)`; `the date the notice is deemed received within s 253(3)` |
| s 253(4) | immunity of the corporation from the duty to send further notices to a shareholder whose notices twice came back unclaimed | disability of the shareholder to complain until they tell the corporation their new address | `the corporation is not required to send further notices to the shareholder within s 253(4)` |
| s 254 | privilege of any person to send a notice to, or serve a document on, a corporation by registered mail to its registered office | no-right of the corporation to insist on another way | `a notice or document may be sent to or served on a corporation within s 254` |
| s 255 | power of the person entitled to a notice to waive or abridge its sending or time by consent in writing | liability of the sender (released from the duty) | `the sending or the time may be waived or abridged within s 255` |
| s 256, s 257(2), (3) | none: rules of evidence (who signs the Director's certificate; how much a certificate, extract, minutes, register entry or security certificate proves); they allocate proof and create no relation | none | `the certificate of the Director is validly signed within s 256(1)`; `the strength of proof of a certificate of the Director within s 256(2)`; `the strength of proof of a corporation's certificate, extract or minutes within s 257(2)`; `the entry or certificate is proof that the registered person is the owner of the securities within s 257(3)` |
| s 257(1) | power of a director, officer or transfer agent to sign a certificate on behalf of the corporation | liability of the corporation (its certificate is made) | `a certificate issued on behalf of a corporation may be signed by the person within s 257(1)` |
| s 258 | privilege of a person sending to the Director to send a photostatic or photographic copy; power of the Director to accept it | no-right of the person to insist on the original; liability of the sender | `the Director may accept a photostatic or photographic copy within s 258` |
| s 258.2 | power of the Director to exempt notices or documents from being sent to the Director | liability of the person exempted (a benefit) | `the Director may exempt the notices or documents from being sent to the Director within s 258.2` |
| s 259(1) | power of the Director to require verification of a document or fact | liability of the person who sent it | `the Director may require verification within s 259(1)` |
| s 259(2) | none: a form-of-proof rule (affidavit, statutory declaration, before a commissioner) | none | `the document or fact is verified within s 259(2)` |
| s 261.1 | claim of the Director to the fee when due | duty of the person who must pay it | `when the fee must be paid to the Director within s 261.1` |
| s 262(1) | none: a definition of statement | none | `statement within s 262(1)` |
| s 262(2) | claim of the person who sent the articles or a statement that the Director record the date, issue the certificate, send it and publish notice | duty of the Director | `the duty is due within s 262(2)` |
| s 262(3), (5) | power of the court or the signer of the articles to specify the day a certificate is dated as of; power of the Director to date a certificate of discontinuance as of the day of amalgamation or continuance | liability of the corporation (the date binds it) | `a certificate may be dated as of the day within s 262(3)`; `a certificate of discontinuance may be dated as of the day within s 262(5)` |
| s 262.1(1) | privilege of the Director to print or mechanically reproduce a signature on a certificate | no-right of the recipient to insist on a handwritten signature | `a signature on a certificate issued by the Director is allowed within s 262.1(1)` |
| s 262.1(3) | none: an execution formality: documents of like form signed separately are one document | none | `the documents are deemed to constitute one document within s 262.1(3)` |
| s 262.2 | claim of the public that the Director publish a notice of the grant of the listed applications | duty of the Director | `the Director must publish a notice of the decision within s 262.2` |
| s 263 | claim of the Director to an annual return in the form and within the period the Director fixes | duty of the corporation | `the corporation has complied with the duty to send an annual return within s 263` |
| s 263.1(1) | privilege of the Director to provide any person with a certificate of a stated fact about a corporation | no-right of the person asking to demand it | `the Director may provide any person with a certificate of the statement within s 263.1(1)` |
| s 263.1(2) | privilege of the Director to refuse a certificate of existence where the corporation is known to be in default | no-right of the corporation (and the asker) to the certificate | `the Director may refuse to issue a certificate of existence within s 263.1(2)` |
| s 264 | power of the Director to alter a notice or document (an affidavit or statutory declaration only with authorization) | liability of the person who sent it | `the Director may alter a notice or document within s 264` |
| s 265(1), (2) | claim of the Director that the directors or shareholders pass resolutions and take the steps to correct an error; power of the Director to proceed without them where no one is prejudiced | duty of the directors or shareholders; liability of the corporation | `the directors or shareholders must pass the resolutions and take the steps within s 265(1)`; `the Director may proceed under subsection 265(1) within s 265(2)` |
| s 265(3) | power of the Director to accept a correction asked for by the corporation or an interested person | liability of the corporation and the shareholders and creditors (no prejudice) | `the Director may accept the correction within s 265(3)` |
| s 265(4), (5) | power of the Director or an interested person to apply to the court for an order that a document be corrected; claim of the Director to notice of the application and to be heard | liability of the corporation; duty of the applicant to give notice | `the applicant may apply to the court for an order that the document be corrected within s 265(4)`; `the applicant must give the Director notice within s 265(5)` |
| s 265(6) | power of the Director to demand surrender of the original document | liability of the holder of the original | `the Director may demand the surrender of the original document within s 265(6)` |
| s 265(7) | none: a rule for the date a corrected document bears | none | `the date the corrected document bears within s 265(7)` |
| s 265(8) | claim of the persons affected to notice of a correction that materially amends a certificate | duty of the Director | `the Director must without delay give notice of the correction within s 265(8)` |
| s 265.1(1), (2) | power of the Director to cancel articles and the related certificate in the prescribed circumstances, and to proceed where no one is prejudiced | liability of the corporation | `the Director may cancel the articles and related certificate within s 265.1(1)`; `the Director may proceed under subsection 265.1(1) within s 265.1(2)` |
| s 265.1(3) | power of the Director to cancel at the request of the corporation or an interested person | liability of the corporation and the shareholders and creditors (no prejudice) | `the Director may cancel at the request of the corporation or an interested person within s 265.1(3)` |
| s 265.1(4), (5) | power of the Director or an interested person to apply to the court for cancellation; claim of the Director to notice and to be heard | liability of the corporation; duty of the applicant to give notice | `the applicant may apply to the court for an order that the articles and certificate be cancelled within s 265.1(4)`; `the applicant must give the Director notice within s 265.1(5)` |
| s 265.1(6) | power of the Director to demand surrender of the cancelled certificate | liability of the holder of the certificate | `the Director may demand the surrender of the cancelled certificate within s 265.1(6)` |
| s 266(1) | claim of any person who pays the fee to examine a document the Director holds, in business hours, and make copies or extracts | duty of the Director | `a person is entitled to examine and make copies or extracts within s 266(1)` |
| s 266(2) | claim of that person to a copy, extract, certified copy or certified extract | duty of the Director | `the Director must provide the copy or extract within s 266(2)` |
| s 266.1(1) | immunity of the person who gave information about a wrongdoing on their own initiative (secrecy of the information and of the person's identity) | disability of the Director to make it available without consent | `the Director must not make the information available within s 266.1(1)` |
| s 266.1(2) | privilege of the Director to provide the information to an investigative body, FINTRAC or a prescribed entity | no-right of the informant to object | `the Director may provide the information to the recipient within s 266.1(2)` |
| s 266.1(3) | none: a definition of wrongdoing | none | `wrongdoing within s 266.1(3)` |
| s 267(1), (2)(a), (3) | claim of persons dealing with the Director that documents be kept, and furnished in intelligible form, for the prescribed period | duty of the Director | `the Director must keep the document within s 267(1)`; `the Director must furnish a copy in intelligible form within s 267(2)(a)`; `the Director is required to keep or produce the document within s 267(3)` |
| s 267(2)(b) | none: a rule of evidence: a certified report reproduced from non-written records is admissible as the originals would be | none | `the report is admissible in evidence to the same extent as the originals within s 267(2)(b)` |
| s 267.1 | privilege of the Director to make documents available or publish by an electronic or mechanical system or device that can reproduce them in intelligible form | no-right of the person to insist on paper | `information or notices may be made available or published by the system or device within s 267.1` |
| s 268(1), (4.2) | none: definitions of charter and of a body deemed incorporated or continued under an Act of Parliament other than this Act or a special Act | none | `charter within s 268(1)`; `the body corporate is deemed to be incorporated or continued by or under an Act of Parliament other than this Act or a special Act within s 268(4.2)` |
| s 268(2), (2.1), (3) | power of the shareholders to authorize the directors and to amend the charter by special resolution, despite the charter or subject to any other Act and the charter; claim of a class or series of shares to its own approval of a change of the nature in s 176(1) | liability of the body corporate; disability of the shareholders to change class rights without the class's approval | `the shareholders may authorize the directors and amend the charter by special resolution despite the charter within s 268(2)`; `the shareholders may authorize the directors and amend the charter by special resolution subject to any other Act and the charter within s 268(2.1)`; `the shareholders may make the change by special resolution under subsection 268(2) or (2.1) within s 268(3)` |
| s 268(4), (4.1) | power of the directors to apply for a certificate of continuance despite the charter (special Act) or subject to any other Act and the charter | liability of the body corporate | `the directors may apply for a certificate of continuance despite the charter within s 268(4)`; `the directors may apply for a certificate of continuance subject to any other Act and the charter within s 268(4.1)` |
| s 268(5) | immunity of the body corporate from a dissenting shareholder's s 190 claim on an amendment made under s 268 | disability of the shareholder to dissent | `a shareholder is not entitled to dissent under section 190 within s 268(5)` |
| s 268(6) | power of the Governor in Council to require the body corporate to apply for a certificate of continuance | liability of the body corporate | `the Governor in Council may require the body corporate to apply for a certificate of continuance within s 268(6)` |
| s 268(8) | immunity of the body corporate from the fees otherwise payable for the continuance | disability of the Director and the Crown to charge them | `the body corporate is not required to pay the fees otherwise payable for the continuance within s 268(8)` |
| s 268(8.1) | none: a consequence rule: the special Act ceases to apply on continuance | none | `the special Act ceases to apply to the corporation within s 268(8.1)` |
| s 268(9) | change of legal position by operation of the Act, with no act of any person: the body corporate is dissolved when the period expires; the claim is that of everyone dealing with it to treat it as dissolved | liability of the body corporate that did not apply in time | `the body corporate is dissolved on the expiration of the period within s 268(9)` |
| s 268(10), (11) | disability of a not-for-profit body, or a similar body incorporated otherwise than under an Act of Parliament, to apply for continuance; privilege of a body incorporated under a Special Act (railway companies) to apply | no-right of the excluded body corporate; liability of the Director to accept an application | `the body corporate may not apply for a certificate of continuance under section 187 within s 268(10)`; `the body corporate may apply for a certificate of continuance under section 187 within s 268(11)`; `the body corporate may apply for a certificate of continuance within s 268(10) and s 268(11)` |
| the Schedule | none: a list of offences used by s 21.31 (another piece); it creates no relation of its own, and who may receive what is decided in s 21.31 and s 266.1(2) | none | `an offence is in the Schedule`; `an offence is listed in items 1 to 8 of the Schedule`; `an offence is within item 9 of the Schedule` |
| S.C. 2001, c. 14, s. 233 | immunity of a proceeding commenced before s 115 of the 2001 Act came into force from Part XIX.1 | disability of the plaintiff and the court to apply Part XIX.1 to it | `Part XIX.1 applies to the proceeding within S.C. 2001, c. 14, s. 233`; `Part XIX.1 governs the apportionment of the damages` |
| R.S. 1985, c. 27 (2nd Supp.), s. 11; S.C. 1990, c. 17, s. 45(1); S.C. 1998, c. 30, s. 10 | none: transitional rules that say a proceeding begun earlier continues under the amended provisions; the relations are those of the amended provisions | none | `the proceeding is continued in accordance with the amended provisions within R.S. 1985, c. 27 (2nd Supp.), s. 11`; `the proceeding is taken up and continued under the amended provision within S.C. 1990, c. 17, s. 45(1)`; `the proceeding is taken up and continued under the amended provision within S.C. 1998, c. 30, s. 10` |
| S.C. 1994, c. 21, s. 125(2) | none: a rule for when subsection (1) (not in the text) applies | none | `subsection 125(1) applies to the year within S.C. 1994, c. 21, s. 125(2)` |
| S.C. 1994, c. 24, s. 33; S.C. 2001, c. 14, s. 136; S.C. 2018, c. 8, s. 107.1 | none: reviews of the Act by the Minister and parliamentary committees; duties between officials and Parliament, no relation to a shareholder, director or officer | none | `the period for the Minister to lay the report within S.C. 1994, c. 24, s. 33(1)`; `the Minister has laid the report in time within S.C. 1994, c. 24, s. 33(1)`; `the committee must review the report and the Act as soon as possible within S.C. 1994, c. 24, s. 33(2)(a)`; `the period for the committee to report within S.C. 1994, c. 24, s. 33(2)(b)`; `the last day for the committee to report within S.C. 1994, c. 24, s. 33(2)(b)`; `the last day for the review within S.C. 2001, c. 14, s. 136`; `the committee must cause a report to be laid before each House within a reasonable period within S.C. 2001, c. 14, s. 136`; `the day Part XIV.1 is to be referred to a committee within S.C. 2018, c. 8, s. 107.1(1)`; `the committee must submit a report within a reasonable time within S.C. 2018, c. 8, s. 107.1(2)` |
| S.C. 1996, c. 10, s. 214 | immunity of an earlier continuance of a railway company from invalidity on the ground that the company was incorporated under an Act of Parliament | disability of anyone who would challenge it | `the continuance is not invalid because the company was incorporated by or under an Act of Parliament within S.C. 1996, c. 10, s. 214` |
| S.C. 2009, c. 23, s. 297(6) | change of legal position by operation of the Act: the body corporate is dissolved at the end of six months if it has not applied; the claim is that of everyone dealing with it to treat it as dissolved | liability of the body corporate | `the last day to apply for continuance within S.C. 2009, c. 23, s. 297(6)`; `the body corporate is dissolved on the expiry of the period within S.C. 2009, c. 23, s. 297(6)` |
| S.C. 2011, c. 25, s. 42 | duty of the named Corporation (a Crown corporation) to submit an application for continuance, within four years, and to submit it to the authorities once approved; claim of the Minister | duty of the Corporation (not of the person) | `the Corporation may submit an application for continuance under the Act for the Minister's approval within S.C. 2011, c. 25, s. 42(1)`; `the last day to submit the application to the Minister within S.C. 2011, c. 25, s. 42(2)`; `the Corporation must submit the application to the applicable authorities within S.C. 2011, c. 25, s. 42(3)`; `the application is invalid solely because the Corporation is incorporated by an Act of Parliament within S.C. 2011, c. 25, s. 42(4)` |
| S.C. 2012, c. 19, s. 210 | none: a status rule: PPP Canada Inc. is an agent of Her Majesty in right of Canada | none | `PPP Canada Inc. is an agent of Her Majesty in right of Canada within S.C. 2012, c. 19, s. 210` |

## Coverage table

One row for each provision in the ranges: each section, and each subsection or paragraph where the subsections differ in disposition or in the rule they state.
234 rows: 174 encoded, 44 inert, 12 fork, 4 repealed or blank in this text.
The headings and sections of the ranges, counted against the rows: the 65 sections (ss 229 to 268 with their lettered additions: 9 + 9 + 15 + 7 + 25) have 177 section and subsection rows in the table; add 5 Part headings, 6 other headings (the three sub-headings of Part XIX.1, and the titles of the Schedule, of the Related Provisions and of the Amendments Not in Force), the Schedule's 9 items, 17 Related Provisions and 20 Amendments Not in Force, and the sum is the 234 rows.
Every `inert` row names what the provision does; every `repealed or blank in this text` row quotes what the text shows; every `fork` row names its entry in the fork register.
The `where` column names a module and a rule, and every name in it was checked against the module by a script that reads the file.
`Seat: Qn` points to the numbered list under `## Seat`.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| PART XIX Investigation (heading) | src:2862 | inert | - | a title; decides nothing. The Part's text is encoded in the module of the same name, whose § heading repeats the title. |
| s 229(1) | src:2863-2864 | encoded | `cb5-part19-investigation.l4`: `may apply for an order directing an investigation within s 229(1)` | Marginal note: Investigation. Seat: Q1. Tests: cb5-tests-part19.l4. |
| s 229(2) | src:2865-2871 | encoded | `cb5-part19-investigation.l4`: `the court may order an investigation within s 229(2)` | Marginal note: Grounds. Seat: Q2. Tests: cb5-tests-part19.l4. |
| s 229(3) | src:2872-2873 | encoded | `cb5-part19-investigation.l4`: `the applicant must give the Director reasonable notice within s 229(3)`; `the applicant has complied with the duty to notify the Director within s 229(3)`; `the Director is entitled to appear and be heard within s 229(3)` | Marginal note: Notice to Director. Seat: Q3, Q4, Q5. Tests: cb5-tests-part19.l4. |
| s 229(4) | src:2874-2875 | encoded | `cb5-part19-investigation.l4`: `an applicant under s 229 is required to give security for costs within s 229(4)` | Marginal note: No security for costs. Seat: Q6. Tests: cb5-tests-part19.l4. |
| s 229(5) | src:2876-2877 | encoded | `cb5-part19-investigation.l4`: `the application must be heard in camera within s 229(5)` | Marginal note: Hearings in camera. Seat: Q7. Tests: cb5-tests-part19.l4. |
| s 229(6) | src:2878-2879 | encoded | `cb5-part19-investigation.l4`: `publishing anything relating to the proceedings is permitted within s 229(6)` | Marginal note: Consent to publish proceedings required. Seat: Q8. Tests: cb5-tests-part19.l4. |
| s 230(1) | src:2880-2893 | encoded | `cb5-part19-investigation.l4`: `Kind of order in connection with an investigation (s 230(1))`; `the court may make an order of the kind within s 230(1)` | Marginal note: Powers of court. Seat: Q9. Tests: cb5-tests-part19.l4. |
| s 230(2) | src:2894-2895 | encoded | `cb5-part19-investigation.l4`: `the inspector has complied with the duty to send the Director a copy of a report within s 230(2)` | Marginal note: Copy of report. Layer 1 only: the duty is the inspector's to the Director, an official to an official; the person is neither party to it nor affected by what it decides. Tests: cb5-tests-part19.l4. |
| s 231(1) | src:2896-2897 | encoded | `cb5-part19-investigation.l4`: `an inspector has the power within s 231(1)` | Marginal note: Power of inspector. Seat: Q10. Tests: cb5-tests-part19.l4. |
| s 231(2) | src:2898-2899 | encoded | `cb5-part19-investigation.l4`: `an inspector may furnish information to or exchange it with the official within s 231(2)` | Marginal note: Exchange of information. Seat: Q11. Tests: cb5-tests-part19.l4. |
| s 231(3) | src:2900-2901 | encoded | `cb5-part19-investigation.l4`: `the inspector must produce a copy of the order within s 231(3)` | Marginal note: Court order. Seat: Q12. Tests: cb5-tests-part19.l4. |
| s 232(1) | src:2902-2903 | encoded | `cb5-part19-investigation.l4`: `an interested person may apply to the court for an in camera hearing and directions within s 232(1)` | Marginal note: Hearing in camera. Seat: Q13. Tests: cb5-tests-part19.l4. |
| s 232(2) | src:2904-2905 | encoded | `cb5-part19-investigation.l4`: `the person has a right to be represented by counsel within s 232(2)` | Marginal note: Right to counsel. Seat: Q14. Tests: cb5-tests-part19.l4. |
| s 233 | src:2906-2907 | encoded | `cb5-part19-investigation.l4`: `a person is excused from giving evidence by reason only that it tends to criminate within s 233`; `Use of evidence given to an inspector (s 233)`; `the use of the evidence within s 233` | Marginal note: Criminating statements. Seat: Q15, Q16. Tests: cb5-tests-part19.l4. |
| s 234 | src:2908-2909 | encoded | `cb5-part19-investigation.l4`: `the statement or report has absolute privilege within s 234` | Marginal note: Absolute privilege (defamation). Seat: Q17. Tests: cb5-tests-part19.l4. |
| s 235(1) | src:2910-2913 | encoded | `cb5-part19-investigation.l4`: `the Director may require the person to report within s 235(1)`; `the person has made the report required within s 235(1)` | Marginal note: Information respecting ownership and control. Seat: Q18, Q19. Tests: cb5-tests-part19.l4. |
| s 235(2) | src:2914-2918 | encoded | `cb5-part19-investigation.l4`: `the person is deemed to have an interest or right in the security within s 235(2)` | Marginal note: Presumption. Seat: Q20. Tests: cb5-tests-part19.l4. |
| s 235(3) | src:2919-2922 | encoded | `cb5-part19-investigation.l4`: `the Director must publish the particulars within s 235(3)` | Marginal note: Publication. Seat: Q21. Tests: cb5-tests-part19.l4. |
| s 235(4) | src:2923-2924 | encoded | `cb5-nouns.l4`, `cb5-part19-investigation.l4`: `Maximum punishment on summary conviction`; `the person is guilty of an offence within s 235(4)`; `the most the court may impose within s 235(4)` | Marginal note: Offence. Seat: Q22, Q23, Q24, Q26, Q27, Q87.... |
| s 235(5) | src:2925-2926 | encoded | `cb5-part19-investigation.l4`: `the director or officer is a party to and guilty of the offence within s 235(5)`; `the most the court may impose on a director or officer within s 235(5)` | Marginal note: Officers, etc., of bodies corporate. Seat: Q25, Q26, Q27. Tests: cb5-tests-part19.l4. |
| s 236 | src:2927-2928 | encoded | `cb5-part19-investigation.l4`: `Part XIX affects solicitor-client privilege or professional secrecy within s 236` | Marginal note: Solicitor-client privilege or professional secrecy. Seat: Q28. Tests: cb5-tests-part19.l4. |
| s 237(1) | src:2929-2930 | encoded | `cb5-part19-investigation.l4`: `the Director may make the inquiry and require records within s 237(1)` | Marginal note: Inquiries. Seat: Q29. Tests: cb5-tests-part19.l4. |
| s 237(2) | src:2931-2932 | encoded | `cb5-part19-investigation.l4`: `the person has complied with the duty to respond within s 237(2)` | Marginal note: Response. Seat: Q30. Tests: cb5-tests-part19.l4. |
| PART XIX.1 Apportioning Award of Damages (heading) | src:2934 | inert | - | a title; decides nothing. The Part's text is encoded in the module of the same name, whose § heading repeats the title. |
| Heading: Interpretation and Application | src:2936 | inert | - | A heading inside the Part (`Interpretation and Application`); decides nothing. It is repeated as a § heading in the module. |
| s 237.1 lead-in | src:2937-2938 | inert | - | Marginal note: Definitions. The lead-in only says that the definitions that follow apply in this Part: a pure citation of scope. Each definition is encoded on its own row below. |
| s 237.1 "financial interest" | src:2939-2949 | encoded | `cb5-part19-1-damages.l4`: `Kind of financial interest (s 237.1)`; `financial interest within s 237.1` | Seat: Q31. Tests: cb5-tests-part19-1.l4. |
| s 237.1 "financial loss" | src:2950 | encoded | `cb5-part19-1-damages.l4`: `financial loss within s 237.1` | Seat: Q32. Tests: cb5-tests-part19-1.l4. |
| s 237.1 "third party" | src:2951 | encoded | `cb5-part19-1-damages.l4`: `third party within s 237.1` | Seat: Q33. Tests: cb5-tests-part19-1.l4. |
| s 237.2(1) | src:2952-2953 | encoded | `cb5-part19-1-damages.l4`: `Part XIX.1 applies to the apportionment within s 237.2(1)` | Marginal note: Application of Part. Seat: Q34. Tests: cb5-tests-part19-1.l4. |
| s 237.2(2) | src:2954-2959 | encoded | `cb5-part19-1-damages.l4`: `Kind of plaintiff (s 237.2(2))`; `Part XIX.1 does not apply to the plaintiff within s 237.2(2)` | Marginal note: Non-application of Part. Seat: Q34. Tests: cb5-tests-part19-1.l4. |
| Heading: Apportionment of Damages | src:2961 | inert | - | A heading inside the Part (`Apportionment of Damages`); decides nothing. It is repeated as a § heading in the module. |
| s 237.3(1) | src:2962-2963 | encoded | `cb5-part19-1-damages.l4`: `the portion of the damages for which a defendant or third party is liable within s 237.3(1)`; `Basis of the liability of a defendant or third party (Part XIX.1)`; `the basis of the liability within s 237.3(1) and s 237.4 to s 237.6` | Marginal note: Degree of responsibility. Seat: Q35, Q45. Tests: cb5-tests-part19-1.l4. |
| s 237.3(2) | src:2964-2965 | encoded | `cb5-part19-1-damages.l4`: `the period for the plaintiff to apply to reallocate within s 237.3(2)`; `the last day to apply to reallocate an uncollectable amount within s 237.3(2)`; `the court may reallocate the uncollectable amount within s 237.3(2)` | Marginal note: Uncollectable amounts. Seat: Q36, Q37. Tests: cb5-tests-part19-1.l4. |
| s 237.3(3) | src:2966-2967 | encoded | `cb5-part19-1-damages.l4`: `the amount that may be reallocated to the other defendant or third party within s 237.3(3)` | Marginal note: Reallocation. Seat: Q38. Tests: cb5-tests-part19-1.l4. |
| s 237.3(4) | src:2968-2969 | encoded | `cb5-part19-1-damages.l4`: `the most that may be reallocated to that defendant or third party within s 237.3(4)` | Marginal note: Maximum amount. Seat: Q38. Tests: cb5-tests-part19-1.l4. |
| s 237.4(1) | src:2970-2971 | encoded | `cb5-part19-1-damages.l4`: `the plaintiff may recover the whole amount of the damages from the defendant or third party within s 237.4(1)`; `Basis of the liability of a defendant or third party (Part XIX.1)`; `the basis of the liability within s 237.3(1) and s 237.4 to s 237.6` | Marginal note: Exception — fraud. Seat: Q39, Q45. Tests: cb5-tests-part19-1.l4. |
| s 237.4(2) | src:2972-2973 | encoded | `cb5-part19-1-damages.l4`: `the defendant or third party is entitled to claim contribution within s 237.4(2)` | Marginal note: Contribution. Seat: Q40. Tests: cb5-tests-part19-1.l4. |
| Heading: Joint and Several, or Solidary, Liability | src:2975 | inert | - | A heading inside the Part (`Joint and Several, or Solidary, Liability`); decides nothing. It is repeated as a § heading in the module. |
| s 237.5(1) | src:2976-2979 | fork | `cb5-part19-1-damages.l4`: `Close of business position of a plaintiff (s 237.5(1))`; `the position is an acquisition in the period within s 237.5(1)(a)`; `the plaintiff had or acquired a financial interest in time within s 237.5(1)(a)` (+5 more) | Marginal note: Individual or personal body corporate. Fork F-237.5-1: both ends of `the period between` the day of the error and the day of general disclosure are read as inside the period. Seat: Q41, Q45. Tests: cb5-tests-part19-1.l4. |
| s 237.5(1.1) | src:2980-2981 | encoded | `cb5-part19-1-damages.l4`: `subsection 237.5(1) does not apply to the plaintiff within s 237.5(1.1)` | Marginal note: Exception. Seat: Q41. Tests: cb5-tests-part19-1.l4. |
| s 237.5(2) lead-in | src:2982-2983 | inert | - | Marginal note: Interpretation. The lead-in only says that the two definitions that follow apply for the purposes of the section: a pure citation of scope. Each definition is encoded on its own row. |
| s 237.5(2)(a) | src:2984 | encoded | `cb5-part19-1-damages.l4`: `personal body corporate within s 237.5(2)(a)` | Marginal note: (a) a personal body corporate is a body corporate that is not actively engaged in any financial, commercial or industrial business and that is controlled by an individual, or by a group of individuals who are connected by marriage, common-law partnership or any legal parent-child relationship or are connected indirectly by a combination of those relationships, whether or not the individuals through whom they are connected are members of the group; and. Seat: Q42. Tests: cb5-tests-part19-1.l4. |
| s 237.5(2)(b) | src:2985 | encoded | `cb5-part19-1-damages.l4`: `common-law partnership within s 237.5(2)(b)` | Marginal note: (b) a common-law partnership is a relationship between two persons who are cohabiting with each other in a conjugal relationship and have done so for a period of at least one year.. Seat: Q43. Tests: cb5-tests-part19-1.l4. |
| s 237.6(1) | src:2986-2987 | encoded | `cb5-part19-1-damages.l4`: `the court may hold the defendants and third parties jointly and severally liable within s 237.6(1)`; `Basis of the liability of a defendant or third party (Part XIX.1)`; `the basis of the liability within s 237.3(1) and s 237.4 to s 237.6` | Marginal note: Equitable grounds. Seat: Q44, Q45. Tests: cb5-tests-part19-1.l4. |
| s 237.6(2) | src:2988-2989 | inert | - | Marginal note: Factors. Machinery: a power of the Governor in Council to establish, by an instrument that is not among the sources, the factors the court must take into account when it decides whether to hold the defendants jointly and severally liable. The factors are not in the text, so nothing can be computed from them; the court's judgment that holding them so is just and reasonable is the input to the s 237.6(1) rule. |
| s 237.6(3) | src:2990-2991 | inert | - | Marginal note: Statutory Instruments Act. Machinery: it says the Statutory Instruments Act does not apply to the factors of s 237.6(2) and that they are published in Part I of the Canada Gazette. It states how a regulation-like instrument is published, and nothing that a case turns on. |
| s 237.7(1) | src:2992-2996 | fork | `cb5-part19-1-damages.l4`: `the average of two prices`; `the value of the security within s 237.7(1)` | Marginal note: Value of security. Fork F-237.7-1: (b) is read to apply to a traded security with no closing price, and (c) to a security not traded that day. Seat: Q46. Tests: cb5-tests-part19-1.l4. |
| s 237.7(2) | src:2997-2998 | encoded | `cb5-part19-1-damages.l4`: `the court may adjust the value within s 237.7(2)` | Marginal note: Court may adjust value. Seat: Q47. Tests: cb5-tests-part19-1.l4. |
| s 237.7(3) | src:2999-3000 | encoded | `cb5-part19-1-damages.l4`: `the day as of which the value is determined within s 237.7(3)` | Marginal note: Valuation day. Seat: Q48. Tests: cb5-tests-part19-1.l4. |
| s 237.7(4) | src:3001-3002 | encoded | `cb5-part19-1-damages.l4`: `organized market within s 237.7(4)` | Marginal note: Definition of organized market. Seat: Q49. Tests: cb5-tests-part19-1.l4. |
| s 237.8(1) | src:3003-3004 | encoded | `cb5-part19-1-damages.l4`: `the court must determine the value within s 237.8(1)` | Marginal note: Court determines value. Seat: Q50. Tests: cb5-tests-part19-1.l4. |
| s 237.8(2) | src:3005-3006 | inert | - | Marginal note: Factors. Machinery: a power of the Governor in Council to establish, by an instrument that is not among the sources, the factors the court may take into account in valuing an interest under s 237.8(1). The factors are not in the text; the court's own determination is the s 237.8(1) rule's subject. |
| s 237.8(3) | src:3007-3008 | inert | - | Marginal note: Statutory Instruments Act. Machinery: it says the Statutory Instruments Act does not apply to the factors of s 237.8(2) and that they are published in Part I of the Canada Gazette. It states how a regulation-like instrument is published. |
| s 237.9 | src:3009-3010 | encoded | `cb5-part19-1-damages.l4`: `the plaintiff may apply for the court to determine the value of the financial interest within s 237.9` | Marginal note: Application to determine value. Seat: Q51. Tests: cb5-tests-part19-1.l4. |
| PART XX Remedies, Offences and Punishment (heading) | src:3012 | inert | - | a title; decides nothing. The Part's text is encoded in the module of the same name, whose § heading repeats the title. |
| s 238 lead-in | src:3013-3014 | inert | - | Marginal note: Definitions. The lead-in only says that the definitions that follow apply in this Part: a pure citation of scope. Each definition is encoded on its own row. |
| s 238 "action" | src:3015 | encoded | `cb5-part20-remedies.l4`: `action within s 238` | Seat: Q53. Tests: cb5-tests-part20.l4. |
| s 238 "complainant" | src:3016-3020 | encoded | `cb5-part20-remedies.l4`: `complainant within s 238` | Seat: Q52. Tests: cb5-tests-part20.l4. |
| s 239(1) | src:3021-3022 | encoded | `cb5-part20-remedies.l4`: `a complainant may apply to a court for leave to act for the corporation within s 239(1)` | Marginal note: Commencing derivative action. Seat: Q54. Tests: cb5-tests-part20.l4. |
| s 239(2) | src:3023-3027 | fork | `cb5-part20-remedies.l4`: `the condition of notice to the directors is met within s 239(2)(a)`; `the condition of good faith is met within s 239(2)(b)`; `the condition of the interests of the corporation is met within s 239(2)(c)` (+1 more) | Marginal note: Conditions precedent. Fork F-239-1: the words `if the directors ... do not bring, diligently prosecute or defend or discontinue the action` are read as a further requirement of paragraph (a), so notice and the directors' inaction are both needed. Seat: Q55, Q56. Tests: cb5-tests-part20.l4. |
| s 240 | src:3028-3033 | encoded | `cb5-part20-remedies.l4`: `Kind of order in a derivative action (s 240)`; `the court may make an order of the kind within s 240` | Marginal note: Powers of court. Seat: Q57. Tests: cb5-tests-part20.l4. |
| s 241(1) | src:3034-3035 | encoded | `cb5-part20-remedies.l4`: `a complainant may apply to a court for an order within s 241(1)` | Marginal note: Application to court re oppression. Seat: Q58. Tests: cb5-tests-part20.l4. |
| s 241(2) | src:3036-3041 | encoded | `cb5-part20-remedies.l4`: `the court may make an order to rectify the matters complained of within s 241(2)` | Marginal note: Grounds. Seat: Q59. Tests: cb5-tests-part20.l4. |
| s 241(3) | src:3042-3057 | encoded | `cb5-part20-remedies.l4`: `Kind of order on an application for relief from oppression (s 241(3))`; `the court may make an order of the kind within s 241(3)` | Marginal note: Powers of court. Seat: Q60. Tests: cb5-tests-part20.l4. |
| s 241(4) | src:3058-3061 | encoded | `cb5-part20-remedies.l4`: `the directors must forthwith comply with subsection 191(4) within s 241(4)(a)`; `another amendment to the articles or by-laws is barred within s 241(4)(b)` | Marginal note: Duty of directors. Seat: Q61, Q62. Tests: cb5-tests-part20.l4. |
| s 241(5) | src:3062-3063 | encoded | `cb5-part20-remedies.l4`: `a shareholder is not entitled to dissent under section 190 within s 241(5)` | Marginal note: Exclusion. Seat: Q63. Tests: cb5-tests-part20.l4. |
| s 241(6) | src:3064-3067 | fork | `cb5-part20-remedies.l4`: `the corporation must not make the payment within s 241(6)` | Marginal note: Limitation. Fork F-241-1: the limit is worded for a payment `to a shareholder`; a payee who holds only debt obligations is not caught by the words. Seat: Q64. Tests: cb5-tests-part20.l4. |
| s 241(7) | src:3068-3069 | encoded | `cb5-part20-remedies.l4`: `the applicant may apply in the alternative for an order under section 214 within s 241(7)` | Marginal note: Alternative order. Seat: Q65. Tests: cb5-tests-part20.l4. |
| s 242(1) | src:3070-3071 | encoded | `cb5-part20-remedies.l4`: `an application or action under Part XX is stayed or dismissed by reason only of approval by the shareholders within s 242(1)`; `the court may take evidence of approval by the shareholders into account within s 242(1)` | Marginal note: Evidence of shareholder approval not decisive. Seat: Q66, Q67. Tests: cb5-tests-part20.l4. |
| s 242(2) | src:3072-3073 | encoded | `cb5-part20-remedies.l4`: `Step in an application or action under Part XX (s 242(2))`; `the approval of the court is required for the step within s 242(2)`; `the court may order a party to give notice to the complainant within s 242(2)` | Marginal note: Court approval to discontinue. Seat: Q68, Q69. Tests: cb5-tests-part20.l4. |
| s 242(3) | src:3074-3075 | encoded | `cb5-part20-remedies.l4`: `a complainant is required to give security for costs within s 242(3)` | Marginal note: No security for costs. Seat: Q70. Tests: cb5-tests-part20.l4. |
| s 242(4) | src:3076-3077 | encoded | `cb5-part20-remedies.l4`: `the court may order the corporation or its subsidiary to pay interim costs to the complainant within s 242(4)`; `the complainant may be held accountable for the interim costs within s 242(4)` | Marginal note: Interim costs. Seat: Q71, Q72. Tests: cb5-tests-part20.l4. |
| s 243(1) | src:3078-3079 | encoded | `cb5-part20-remedies.l4`: `may apply to a court for an order that the registers or records be rectified within s 243(1)` | Marginal note: Application to court to rectify records. Seat: Q73. Tests: cb5-tests-part20.l4. |
| s 243(2) | src:3080-3081 | encoded | `cb5-part20-remedies.l4`: `the applicant must give the Director notice within s 243(2)`; `the Director is entitled to appear and be heard within s 243(2)` | Marginal note: Notice to Director. Seat: Q74, Q75. Tests: cb5-tests-part20.l4. |
| s 243(3) | src:3082-3087 | encoded | `cb5-part20-remedies.l4`: `Kind of order on an application to rectify records (s 243(3))`; `the court may make an order of the kind within s 243(3)` | Marginal note: Powers of court. Seat: Q76. Tests: cb5-tests-part20.l4. |
| s 244 | src:3088-3089 | encoded | `cb5-part20-remedies.l4`: `the Director may apply to a court for directions within s 244` | Marginal note: Application for directions. Layer 1 only: the power is the Director's to ask the court for directions on the Director's own duties; the person has no fact to state and nothing to do. Tests: cb5-tests-part20.l4. |
| s 245(1) | src:3090-3091 | encoded | `cb5-part20-remedies.l4`: `the period for the Director to give notice of a refusal within s 245(1)`; `the last day for the Director to give written notice of the refusal within s 245(1)`; `the Director has complied with the duty to give notice of the refusal within s 245(1)` | Marginal note: Notice of refusal by Director. Seat: Q77, Q78. Tests: cb5-tests-part20.l4. |
| s 245(2) | src:3092-3093 | encoded | `cb5-part20-remedies.l4`: `the Director is deemed to have refused to file the document for the purposes of s 246 within s 245(2)` | Marginal note: Deemed refusal. Seat: Q79. Tests: cb5-tests-part20.l4. |
| s 246 | src:3094-3104 | encoded | `cb5-part20-remedies.l4`: `Kind of decision of the Director that may be appealed (s 246)`; `a person may apply to a court for an order on the decision within s 246` | Marginal note: Appeal from Director’s decision. Seat: Q80. Tests: cb5-tests-part20.l4. |
| s 246 closing words | src:3105 | encoded | `cb5-part20-remedies.l4`: `the court may make any order it thinks fit on the appeal within s 246` | Marginal note: The Court may make any order it thinks fit.. Seat: Q81. Tests: cb5-tests-part20.l4. |
| s 247 | src:3106-3107 | encoded | `cb5-part20-remedies.l4`: `may apply to a court for a compliance or restraining order within s 247` | Marginal note: Restraining or compliance order. Seat: Q82, Q83. Tests: cb5-tests-part20.l4. |
| s 248 | src:3108-3109 | encoded | `cb5-part20-remedies.l4`: `the application may be made in a summary manner within s 248` | Marginal note: Summary application to court. Seat: Q84. Tests: cb5-tests-part20.l4. |
| s 249(1) | src:3110-3111 | encoded | `cb5-part20-remedies.l4`: `Whether an appeal lies (s 249)`; `whether an appeal lies within s 249` | Marginal note: Appeal of final order. Seat: Q85. Tests: cb5-tests-part20.l4. |
| s 249(2) | src:3112-3113 | encoded | `cb5-part20-remedies.l4`: `Whether an appeal lies (s 249)`; `whether an appeal lies within s 249` | Marginal note: Appeal with leave. Seat: Q85. Tests: cb5-tests-part20.l4. |
| s 250(1) | src:3114-3118 | encoded | `cb5-nouns.l4`, `cb5-part20-offences.l4`: `Maximum punishment on summary conviction`; `the elements of the offence are met within s 250(1)`; `the person is guilty of an offence within s 250(1) and s 250(3)` (+1 more) | Marginal note: Offences with respect to reports. Seat: Q23, Q24, Q26, Q27, Q86, Q87.... |
| s 250(2) | src:3119-3120 | encoded | `cb5-part20-offences.l4`: `the director or officer is a party to and guilty of the offence within s 250(2)`; `the most the court may impose on a director or officer within s 250(2)` | Marginal note: Officers, etc., of bodies corporate. Seat: Q89, Q90, Q91. Tests: cb5-tests-part20-offences.l4. |
| s 250(3) | src:3121-3122 | encoded | `cb5-part20-offences.l4`: `the person has the immunity within s 250(3)` | Marginal note: Immunity. Seat: Q86, Q89. Tests: cb5-tests-part20-offences.l4. |
| s 250(4) | src:3123-3124 | encoded | `cb5-part20-offences.l4`: `the document is a report, return, notice or other document for the purposes of s 250 within s 250(4)` | Marginal note: Register of individuals with significant control. Seat: Q86. Tests: cb5-tests-part20-offences.l4. |
| s 251 | src:3125-3126 | encoded | `cb5-part20-offences.l4`: `the person is guilty of an offence within s 251`; `the most the court may impose within s 251` | Marginal note: Offence. Seat: Q92, Q93. Tests: cb5-tests-part20-offences.l4. |
| s 252(1) | src:3127-3128 | encoded | `cb5-part20-offences.l4`: `the court may order the person to comply within s 252(1)` | Marginal note: Order to comply. Seat: Q94. Tests: cb5-tests-part20-offences.l4. |
| s 252(2) | src:3129-3130 | encoded | `cb5-part20-offences.l4`: `the period for instituting a prosecution within s 252(2)`; `the last day to institute a prosecution within s 252(2)`; `the prosecution is instituted in time within s 252(2)` | Marginal note: Limitation period. Seat: Q95, Q96. Tests: cb5-tests-part20-offences.l4. |
| s 252(3) | src:3131-3132 | encoded | `cb5-part20-offences.l4`: `a civil remedy is suspended or affected by reason that the act or omission is an offence under this Act within s 252(3)` | Marginal note: Civil remedy not affected. Seat: Q97. Tests: cb5-tests-part20-offences.l4. |
| PART XX.1 Documents in Electronic or Other Form (heading) | src:3134 | inert | - | a title; decides nothing. The Part's text is encoded in the module of the same name, whose § heading repeats the title. |
| s 252.1 lead-in | src:3135-3136 | inert | - | Marginal note: Definitions. The lead-in only says that the definitions that follow apply in this Part: a pure citation of scope. Each definition is encoded on its own row. |
| s 252.1 "electronic document" | src:3137 | encoded | `cb5-part20-1-electronic.l4`: `electronic document within s 252.1` | Seat: Q98. Tests: cb5-tests-part20-1.l4. |
| s 252.1 "information system" | src:3138 | encoded | `cb5-part20-1-electronic.l4`: `information system within s 252.1` | Seat: Q99. Tests: cb5-tests-part20-1.l4. |
| s 252.2 | src:3139-3140 | encoded | `cb5-part20-1-electronic.l4`: `Part XX.1 applies within s 252.2` | Marginal note: Application. Seat: Q100. Tests: cb5-tests-part20-1.l4. |
| s 252.3(1) | src:3141-3142 | encoded | `cb5-part20-1-electronic.l4`: `this Act or the regulations require a person to create or provide an electronic document within s 252.3(1)` | Marginal note: Use not mandatory. Seat: Q101. Tests: cb5-tests-part20-1.l4. |
| s 252.3(2) | src:3143-3146 | encoded | `cb5-part20-1-electronic.l4`: `the provision of an electronic document satisfies the requirement to provide it to the addressee within s 252.3(2)`; `an electronic document satisfies a requirement to provide a notice to a person within s 252.3(2) and s 252.4` | Marginal note: Consent and other requirements. Seat: Q102, Q103. Tests: cb5-tests-part20-1.l4. |
| s 252.3(3) | src:3147-3148 | fork | `cb5-part20-1-electronic.l4`: `the revocation takes effect within s 252.3(3)` | Marginal note: Revocation of consent. Fork F-252.3-1: the text says a consent may be revoked but not what revocation does; a revoked consent is read as no longer a consent. Seat: Q104. Tests: cb5-tests-part20-1.l4. |
| s 252.4 | src:3149-3152 | encoded | `cb5-part20-1-electronic.l4`: `an electronic document satisfies the requirement to create or provide within s 252.4` | Marginal note: Creation and provision of information. Seat: Q103, Q105. Tests: cb5-tests-part20-1.l4. |
| s 252.5(1) | src:3153-3156 | encoded | `cb5-part20-1-electronic.l4`: `an electronic document satisfies the requirement to create in writing within s 252.5(1)` | Marginal note: Creation of information in writing. Seat: Q106. Tests: cb5-tests-part20-1.l4. |
| s 252.5(2) | src:3157-3160 | encoded | `cb5-part20-1-electronic.l4`: `an electronic document satisfies the requirement to provide in writing within s 252.5(2)` | Marginal note: Provision of information in writing. Seat: Q107. Tests: cb5-tests-part20-1.l4. |
| s 252.5(3) | src:3161-3162 | encoded | `cb5-part20-1-electronic.l4`: `a single version of an electronic document satisfies the requirement for copies within s 252.5(3)` | Marginal note: Copies. Seat: Q108. Tests: cb5-tests-part20-1.l4. |
| s 252.5(4) | src:3163-3164 | encoded | `cb5-part20-1-electronic.l4`: `sending an electronic document satisfies the requirement to provide by registered mail within s 252.5(4)` | Marginal note: Registered mail. Seat: Q109. Tests: cb5-tests-part20-1.l4. |
| s 252.6(1) | src:3165-3169 | encoded | `cb5-part20-1-electronic.l4`: `a statutory declaration or affidavit may be created or provided in an electronic document within s 252.6(1)` | Marginal note: Statutory declarations and affidavits. Seat: Q110. Tests: cb5-tests-part20-1.l4. |
| s 252.6(2) | src:3170-3171 | encoded | `cb5-part20-1-electronic.l4`: `electronic document within s 252.6` | Marginal note: Definitions. Seat: Q111. Tests: cb5-tests-part20-1.l4. |
| s 252.6(3) | src:3172-3173 | encoded | `cb5-part20-1-electronic.l4`: `electronic document within s 252.6` | Marginal note: Clarification. Seat: Q111. Tests: cb5-tests-part20-1.l4. |
| s 252.7 | src:3174-3178 | encoded | `cb5-part20-1-electronic.l4`: `a requirement for a signature or for a document to be executed is satisfied within s 252.7` | Marginal note: Signatures. Seat: Q112. Tests: cb5-tests-part20-1.l4. |
| PART XXI General (heading) | src:3180 | inert | - | a title; decides nothing. The Part's text is encoded in the module of the same name, whose § heading repeats the title. |
| s 253(1) | src:3181-3184 | encoded | `cb5-part21-notices.l4`: `Way of sending a notice (s 253(1))`; `a notice or document may be sent in the way within s 253(1)` | Marginal note: Notice to directors and shareholders. Seat: Q113. Tests: cb5-tests-part21-notices.l4. |
| s 253(2) | src:3185-3186 | encoded | `cb5-part21-notices.l4`: `the person is presumed to be a director of the corporation within s 253(2)` | Marginal note: Effect of notice. Seat: Q114. Tests: cb5-tests-part21-notices.l4. |
| s 253(3) | src:3187-3188 | encoded | `cb5-part21-notices.l4`: `the date the notice is deemed received within s 253(3)` | Marginal note: Deemed receipt. Seat: Q115. Tests: cb5-tests-part21-notices.l4. |
| s 253(4) | src:3189-3190 | encoded | `cb5-part21-notices.l4`: `the corporation is not required to send further notices to the shareholder within s 253(4)` | Marginal note: Undelivered notices. Seat: Q116. Tests: cb5-tests-part21-notices.l4. |
| s 254 | src:3191-3192 | encoded | `cb5-part21-notices.l4`: `a notice or document may be sent to or served on a corporation within s 254`; `the date the notice is deemed received or served within s 254` | Marginal note: Notice to and service on a corporation. Seat: Q117, Q118. Tests: cb5-tests-part21-notices.l4. |
| s 255 | src:3193-3194 | encoded | `cb5-part21-notices.l4`: `the sending or the time may be waived or abridged within s 255` | Marginal note: Waiver of notice. Seat: Q119. Tests: cb5-tests-part21-notices.l4. |
| s 256(1) | src:3195-3196 | encoded | `cb5-part21-notices.l4`: `the certificate of the Director is validly signed within s 256(1)` | Marginal note: Certificate of Director. Seat: Q120. Tests: cb5-tests-part21-notices.l4. |
| s 256(2) | src:3197-3198 | encoded | `cb5-part21-notices.l4`: `Strength of proof given by the Act (ss 256(2), 257(2))`; `the strength of proof of a certificate of the Director within s 256(2)` | Marginal note: Evidence. Seat: Q121, Q123. Tests: cb5-tests-part21-notices.l4. |
| s 257(1) | src:3199-3200 | encoded | `cb5-part21-notices.l4`: `a certificate issued on behalf of a corporation may be signed by the person within s 257(1)` | Marginal note: Certificate of corporation. Seat: Q122. Tests: cb5-tests-part21-notices.l4. |
| s 257(2) | src:3201-3206 | encoded | `cb5-part21-notices.l4`: `Strength of proof given by the Act (ss 256(2), 257(2))`; `the strength of proof of a corporation's certificate, extract or minutes within s 257(2)` | Marginal note: Proof. Seat: Q121, Q123. Tests: cb5-tests-part21-notices.l4. |
| s 257(3) | src:3207-3208 | encoded | `cb5-part21-notices.l4`: `the entry or certificate is proof that the registered person is the owner of the securities within s 257(3)` | Marginal note: Security certificate. Seat: Q124. Tests: cb5-tests-part21-notices.l4. |
| s 258 | src:3209-3210 | encoded | `cb5-part21-director.l4`: `the Director may accept a photostatic or photographic copy within s 258` | Marginal note: Copies. Seat: Q125. Tests: cb5-tests-part21-director.l4. |
| s 258.1 | src:3211-3216 | inert | - | Marginal note: Content and form of documents. Machinery: it gives the Director a power to establish, by an instrument that is not among the sources, the content and form of what is sent to or issued by the Director, including electronic forms, who may sign or transmit, how signing is done and when a document is taken as sent or received. Nothing in the text says what the Director has established, so no rule can be computed from it; the Director's form requirements are plain inputs where a rule needs them. |
| s 258.1(e) | src:3217 | repealed or blank in this text | - | Marginal note: (e) [Repealed, 2018, c. 8, s. 36]. The text shows `(e) [Repealed, 2018, c. 8, s. 36]`. |
| s 258.2 | src:3218-3219 | encoded | `cb5-part21-director.l4`: `the Director may exempt the notices or documents from being sent to the Director within s 258.2` | Marginal note: Exemption. Seat: Q126. Tests: cb5-tests-part21-director.l4. |
| s 259(1) | src:3220-3221 | encoded | `cb5-part21-director.l4`: `the Director may require verification within s 259(1)` | Marginal note: Proof required by Director. Seat: Q127. Tests: cb5-tests-part21-director.l4. |
| s 259(2) | src:3222-3223 | encoded | `cb5-part21-director.l4`: `the document or fact is verified within s 259(2)` | Marginal note: Form of proof. Seat: Q128. Tests: cb5-tests-part21-director.l4. |
| s 260 | src:3224-3225 | inert | - | Marginal note: Appointment of Director. Machinery: the Minister may appoint a Director and Deputy Directors. The appointment of an officer is not a rule about anyone's rights; the validity of a certificate signed by a Deputy Director authorized under it is encoded under s 256(1). |
| s 261(1) | src:3226-3243 | inert | - | Marginal note: Regulations. Machinery: the Governor in Council's regulation-making power (paragraphs (a) to (i), with (a.1), (a.2), (c.01), (c.02) and (c.1)). The regulations are not among the sources; every place the Act leaves a matter to the regulations is a plain input in the rule that needs it (for example the prescribed amount in s 237.5(1)(b) and the fees of s 261.1). |
| s 261(2) | src:3244-3245 | inert | - | Marginal note: Incorporation by reference. Machinery: regulations may incorporate material by reference, as it exists on a date or as amended. A rule about how a regulation is drafted, not about the rights of a person under the Act. |
| s 261(3) | src:3246-3247 | inert | - | Marginal note: Incorporated material is not a regulation. Machinery: it says incorporated material does not become a regulation for the purposes of the Statutory Instruments Act. A rule about the status of regulations, not about a person's rights under the Act. |
| s 261.1 | src:3248-3249 | encoded | `cb5-part21-director.l4`: `Step for which a fee is payable (s 261.1)`; `When a fee must be paid (s 261.1)`; `when the fee must be paid to the Director within s 261.1` | Marginal note: Payment of fees. Seat: Q129. Tests: cb5-tests-part21-director.l4. |
| s 262(1) | src:3250-3251 | encoded | `cb5-part21-director.l4`: `statement within s 262(1)` | Marginal note: Definition of statement. Seat: Q131. Tests: cb5-tests-part21-director.l4. |
| s 262(2) | src:3252-3257 | encoded | `cb5-part21-director.l4`: `Duty of the Director on receiving articles or a statement (s 262(2))`; `the duty is due within s 262(2)` | Marginal note: Sending of articles and statements. Seat: Q130. Tests: cb5-tests-part21-director.l4. |
| s 262(3) | src:3258-3259 | encoded | `cb5-part21-director.l4`: `a certificate may be dated as of the day within s 262(3)` | Marginal note: Date of certificate. Seat: Q132. Tests: cb5-tests-part21-director.l4. |
| s 262(4) | src:3260 | repealed or blank in this text | - | The text shows `(4) [Repealed, 1994, c. 24, s. 28]`. |
| s 262(5) | src:3261-3262 | encoded | `cb5-part21-director.l4`: `a certificate of discontinuance may be dated as of the day within s 262(5)` | Marginal note: Date of certificate. Seat: Q133. Tests: cb5-tests-part21-director.l4. |
| s 262.1(1) | src:3263-3264 | encoded | `cb5-part21-director.l4`: `a signature on a certificate issued by the Director is allowed within s 262.1(1)` | Marginal note: Signature. Seat: Q134. Tests: cb5-tests-part21-director.l4. |
| s 262.1(2) | src:3265 | repealed or blank in this text | - | The text shows `(2) [Repealed, 2018, c. 8, s. 41]`. |
| s 262.1(3) | src:3266-3267 | encoded | `cb5-part21-director.l4`: `the documents are deemed to constitute one document within s 262.1(3)` | Marginal note: Execution of documents. Seat: Q135. Tests: cb5-tests-part21-director.l4. |
| s 262.2 | src:3268-3269 | encoded | `cb5-part21-director.l4`: `Application whose grant the Director must publish (s 262.2)`; `the Director must publish a notice of the decision within s 262.2` | Marginal note: Publication. Seat: Q136. Tests: cb5-tests-part21-director.l4. |
| s 263 | src:3270-3271 | encoded | `cb5-part21-director.l4`: `the corporation has complied with the duty to send an annual return within s 263` | Marginal note: Annual return. Seat: Q137. Tests: cb5-tests-part21-director.l4. |
| s 263.1(1) | src:3272-3276 | encoded | `cb5-part21-director.l4`: `Statement the Director may certify about a corporation (s 263.1(1))`; `the Director may provide any person with a certificate of the statement within s 263.1(1)` | Marginal note: Certificate. Seat: Q138, Q139. Tests: cb5-tests-part21-director.l4. |
| s 263.1(2) | src:3277-3278 | encoded | `cb5-part21-director.l4`: `the Director may refuse to issue a certificate of existence within s 263.1(2)` | Marginal note: Director may refuse to issue certificate of existence. Seat: Q139. Tests: cb5-tests-part21-director.l4. |
| s 264 | src:3279-3280 | encoded | `cb5-part21-director.l4`: `the Director may alter a notice or document within s 264` | Marginal note: Alteration. Seat: Q140. Tests: cb5-tests-part21-director.l4. |
| s 265(1) | src:3281-3282 | encoded | `cb5-part21-director.l4`: `the directors or shareholders must pass the resolutions and take the steps within s 265(1)` | Marginal note: Corrections at request of Director. Seat: Q141. Tests: cb5-tests-part21-director.l4. |
| s 265(2) | src:3283-3284 | encoded | `cb5-part21-director.l4`: `the Director may proceed under subsection 265(1) within s 265(2)` | Marginal note: No prejudice. Seat: Q142. Tests: cb5-tests-part21-director.l4. |
| s 265(3) | src:3285-3288 | encoded | `cb5-part21-director.l4`: `the Director may accept the correction within s 265(3)` | Marginal note: Corrections at the request of the corporation. Seat: Q143. Tests: cb5-tests-part21-director.l4. |
| s 265(4) | src:3289-3290 | encoded | `cb5-part21-director.l4`: `the applicant may apply to the court for an order that the document be corrected within s 265(4)` | Marginal note: Application to court. Seat: Q144. Tests: cb5-tests-part21-director.l4. |
| s 265(5) | src:3291-3292 | encoded | `cb5-part21-director.l4`: `the applicant must give the Director notice within s 265(5)` | Marginal note: Notice to Director. Seat: Q145. Tests: cb5-tests-part21-director.l4. |
| s 265(6) | src:3293-3294 | encoded | `cb5-part21-director.l4`: `the Director may demand the surrender of the original document within s 265(6)` | Marginal note: Director may require surrender of document. Seat: Q146. Tests: cb5-tests-part21-director.l4. |
| s 265(7) | src:3295-3298 | fork | `cb5-part21-director.l4`: `the date the corrected document bears within s 265(7)` | Marginal note: Date of corrected document. Fork F-265(7)-1: if both exceptions apply, the court's decision is taken to prevail. Seat: Q147. Tests: cb5-tests-part21-director.l4. |
| s 265(8) | src:3299-3300 | encoded | `cb5-part21-director.l4`: `the Director must without delay give notice of the correction within s 265(8)` | Marginal note: Notice. Seat: Q148. Tests: cb5-tests-part21-director.l4. |
| s 265.1(1) | src:3301-3302 | encoded | `cb5-part21-director.l4`: `the Director may cancel the articles and related certificate within s 265.1(1)` | Marginal note: Cancellation of articles by Director. Seat: Q149. Tests: cb5-tests-part21-director.l4. |
| s 265.1(2) | src:3303-3304 | encoded | `cb5-part21-director.l4`: `the Director may proceed under subsection 265.1(1) within s 265.1(2)` | Marginal note: No prejudice. Seat: Q150. Tests: cb5-tests-part21-director.l4. |
| s 265.1(3) | src:3305-3308 | encoded | `cb5-part21-director.l4`: `the Director may cancel at the request of the corporation or an interested person within s 265.1(3)` | Marginal note: Request to Director to cancel articles. Seat: Q151. Tests: cb5-tests-part21-director.l4. |
| s 265.1(4) | src:3309-3310 | encoded | `cb5-part21-director.l4`: `the applicant may apply to the court for an order that the articles and certificate be cancelled within s 265.1(4)` | Marginal note: Application to court. Seat: Q152. Tests: cb5-tests-part21-director.l4. |
| s 265.1(5) | src:3311-3312 | encoded | `cb5-part21-director.l4`: `the applicant must give the Director notice within s 265.1(5)` | Marginal note: Notice to Director. Seat: Q153. Tests: cb5-tests-part21-director.l4. |
| s 265.1(6) | src:3313-3314 | encoded | `cb5-part21-director.l4`: `the Director may demand the surrender of the cancelled certificate within s 265.1(6)` | Marginal note: Return of certificate. Seat: Q154. Tests: cb5-tests-part21-director.l4. |
| s 266(1) | src:3315-3316 | encoded | `cb5-part21-director.l4`: `a person is entitled to examine and make copies or extracts within s 266(1)` | Marginal note: Examination. Seat: Q155. Tests: cb5-tests-part21-director.l4. |
| s 266(2) | src:3317-3318 | encoded | `cb5-part21-director.l4`: `the Director must provide the copy or extract within s 266(2)` | Marginal note: Copies or extracts. Seat: Q156. Tests: cb5-tests-part21-director.l4. |
| s 266.1(1) | src:3319-3320 | encoded | `cb5-part21-director.l4`: `the Director must not make the information available within s 266.1(1)` | Marginal note: Information not to be made available. Seat: Q158. Tests: cb5-tests-part21-director.l4. |
| s 266.1(2) | src:3321-3322 | encoded | `cb5-part21-director.l4`: `Recipient of protected information (s 266.1(2))`; `the Director may provide the information to the recipient within s 266.1(2)` | Marginal note: Exception — investigations. Seat: Q159. Tests: cb5-tests-part21-director.l4. |
| s 266.1(3) | src:3323-3327 | encoded | `cb5-part21-director.l4`: `wrongdoing within s 266.1(3)` | Marginal note: Definition of wrongdoing. Seat: Q157. Tests: cb5-tests-part21-director.l4. |
| s 267(1) | src:3328-3329 | encoded | `cb5-part21-director.l4`: `the Director must keep the document within s 267(1)` | Marginal note: Director’s obligation to keep documents. Seat: Q160. Tests: cb5-tests-part21-director.l4. |
| s 267(2) | src:3330-3333 | encoded | `cb5-part21-director.l4`: `the Director must furnish a copy in intelligible form within s 267(2)(a)`; `the report is admissible in evidence to the same extent as the originals within s 267(2)(b)` | Marginal note: Obligation to furnish. Seat: Q161, Q162. Tests: cb5-tests-part21-director.l4. |
| s 267(3) | src:3334-3335 | encoded | `cb5-part21-director.l4`: `the Director is required to keep or produce the document within s 267(3)` | Marginal note: Time period for keeping and producing documents. Seat: Q163. Tests: cb5-tests-part21-director.l4. |
| s 267.1 | src:3336-3337 | encoded | `cb5-part21-director.l4`: `information or notices may be made available or published by the system or device within s 267.1` | Marginal note: Form of publication. Seat: Q164. Tests: cb5-tests-part21-director.l4. |
| s 268(1) | src:3338-3341 | encoded | `cb5-part21-charter.l4`: `charter within s 268(1)` | Marginal note: Definition of charter. Seat: Q165. Tests: cb5-tests-part21-charter.l4. |
| s 268(2) | src:3342-3345 | encoded | `cb5-part21-charter.l4`: `the shareholders may authorize the directors and amend the charter by special resolution despite the charter within s 268(2)` | Marginal note: Amendment of charter — special Act. Seat: Q167. Tests: cb5-tests-part21-charter.l4. |
| s 268(2.1) | src:3346-3349 | encoded | `cb5-part21-charter.l4`: `the shareholders may authorize the directors and amend the charter by special resolution subject to any other Act and the charter within s 268(2.1)` | Marginal note: Amendment of charter — other Act. Seat: Q168. Tests: cb5-tests-part21-charter.l4. |
| s 268(3) | src:3350-3353 | encoded | `cb5-part21-charter.l4`: `the shareholders may make the change by special resolution under subsection 268(2) or (2.1) within s 268(3)` | Marginal note: Change of class rights. Seat: Q169. Tests: cb5-tests-part21-charter.l4. |
| s 268(4) | src:3354-3355 | fork | `cb5-part21-charter.l4`: `the directors may apply for a certificate of continuance despite the charter within s 268(4)` | Marginal note: Authorizing continuance. Fork F-268(4)-1: `Subject to subsection (6)` is given no effect: subsection (6) lets the Governor in Council require an application and does not limit the directors' power here. Seat: Q170. Tests: cb5-tests-part21-charter.l4. |
| s 268(4.1) | src:3356-3357 | encoded | `cb5-part21-charter.l4`: `the directors may apply for a certificate of continuance subject to any other Act and the charter within s 268(4.1)` | Marginal note: Authorizing continuance. Seat: Q171. Tests: cb5-tests-part21-charter.l4. |
| s 268(4.2) | src:3358-3359 | encoded | `cb5-part21-charter.l4`: `the body corporate is deemed to be incorporated or continued by or under an Act of Parliament other than this Act or a special Act within s 268(4.2)` | Marginal note: Financial institutions. Seat: Q166. Tests: cb5-tests-part21-charter.l4. |
| s 268(5) | src:3360-3361 | encoded | `cb5-part21-charter.l4`: `a shareholder is not entitled to dissent under section 190 within s 268(5)` | Marginal note: No dissent. Seat: Q172. Tests: cb5-tests-part21-charter.l4. |
| s 268(6) | src:3362-3367 | encoded | `cb5-part21-charter.l4`: `the Governor in Council may require the body corporate to apply for a certificate of continuance within s 268(6)` | Marginal note: Discretionary continuance. Seat: Q173. Tests: cb5-tests-part21-charter.l4. |
| s 268(7) | src:3368 | repealed or blank in this text | - | The text shows `(7) [Repealed, 2009, c. 23, s. 311]`. |
| s 268(8) | src:3369-3370 | encoded | `cb5-part21-charter.l4`: `the body corporate is not required to pay the fees otherwise payable for the continuance within s 268(8)` | Marginal note: Fees. Seat: Q175. Tests: cb5-tests-part21-charter.l4. |
| s 268(8.1) | src:3371-3372 | encoded | `cb5-part21-charter.l4`: `the special Act ceases to apply to the corporation within s 268(8.1)` | Marginal note: Special Act no longer applicable. Seat: Q176. Tests: cb5-tests-part21-charter.l4. |
| s 268(9) | src:3373-3374 | encoded | `cb5-part21-charter.l4`: `the body corporate is dissolved on the expiration of the period within s 268(9)` | Marginal note: Idem. Seat: Q174. Tests: cb5-tests-part21-charter.l4. |
| s 268(10) | src:3375-3376 | fork | `cb5-part21-charter.l4`: `the body corporate may not apply for a certificate of continuance under section 187 within s 268(10)`; `the body corporate may apply for a certificate of continuance within s 268(10) and s 268(11)` | Marginal note: Continuance prohibited. Fork F-268(10)-1: a body corporate within both s 268(10) and s 268(11) is read as allowed to apply: subsection (11) is the exception. Seat: Q177. Tests: cb5-tests-part21-charter.l4. |
| s 268(11) | src:3377-3378 | fork | `cb5-part21-charter.l4`: `the body corporate may apply for a certificate of continuance under section 187 within s 268(11)`; `the body corporate may apply for a certificate of continuance within s 268(10) and s 268(11)` | Marginal note: Exception for railway companies. Fork F-268(10)-1: a body corporate within both s 268(10) and s 268(11) is read as allowed to apply: subsection (11) is the exception. Seat: Q177. Tests: cb5-tests-part21-charter.l4. |
| Heading: SCHEDULE (Subsections 21.31(2), (3) and (6)) Offences | src:3380 | inert | - | A title and a citation: it names the Schedule and the subsections of the Act (21.31(2), (3) and (6), in another piece's range) that use it. The Schedule's rows are encoded on the item rows below. |
| Schedule item 1 | src:3381-3509 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 1 of the Schedule`; `an offence is listed in items 1 to 8 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 2 | src:3510 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 2 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 3 | src:3511-3514 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 3 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 4 | src:3515-3518 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 4 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 5 | src:3519-3522 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 5 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 6 | src:3523-3529 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 6 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 7 | src:3530-3533 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 7 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 8 | src:3534-3540 | encoded | `cb5-schedule-offences.l4`: `the offence provisions listed in item 8 of the Schedule` | Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Schedule item 9 | src:3541 | fork | `cb5-schedule-offences.l4`: `an offence is within item 9 of the Schedule`; `an offence is in the Schedule` | Fork F-sched-9-1: `for which` is read to attach to the offence: the offence's own maximum term of imprisonment must be five years or more. Seat: Q178. Tests: cb5-tests-schedule.l4. |
| Heading: RELATED PROVISIONS | src:3543 | inert | - | A title: the heading of the run of transitional and review provisions of amending Acts that follows. Each provision is encoded on its own row below. |
| RP R.S., 1985, c. 27 (2nd Supp.), s. 11 | src:3545-3547 | encoded | `cb5-related-provisions.l4`: `the proceeding is continued in accordance with the amended provisions within R.S. 1985, c. 27 (2nd Supp.), s. 11` | Seat: Q179. Tests: cb5-tests-related.l4. |
| RP 1990, c. 17, s. 45(1) | src:3549-3551 | encoded | `cb5-related-provisions.l4`: `the proceeding is taken up and continued under the amended provision within S.C. 1990, c. 17, s. 45(1)` | Seat: Q180. Tests: cb5-tests-related.l4. |
| RP 1994, c. 21, s. 125(2) | src:3553-3554 | fork | `cb5-related-provisions.l4`: `subsection 125(1) applies to the year within S.C. 1994, c. 21, s. 125(2)` | Fork F-125(2)-1: `after 1988` is read as the calendar years 1989 and later; subsection (1) is not in the text. Seat: Q182. Tests: cb5-tests-related.l4. |
| RP 1994, c. 24, s. 33(1) | src:3556-3558 | encoded | `cb5-related-provisions.l4`: `the period for the Minister to lay the report within S.C. 1994, c. 24, s. 33(1)`; `the Minister has laid the report in time within S.C. 1994, c. 24, s. 33(1)` | Layer 1 only: it fixes when the Minister reports on the Act to Parliament; no right or duty of a shareholder, director or officer. Tests: cb5-tests-related.l4. |
| RP 1994, c. 24, s. 33(2) | src:3559-3562 | encoded | `cb5-related-provisions.l4`: `the committee must review the report and the Act as soon as possible within S.C. 1994, c. 24, s. 33(2)(a)`; `the period for the committee to report within S.C. 1994, c. 24, s. 33(2)(b)`; `the last day for the committee to report within S.C. 1994, c. 24, s. 33(2)(b)` | Layer 1 only: it fixes how a parliamentary committee reviews the Minister's report; no right or duty of a shareholder, director or officer. Tests: cb5-tests-related.l4. |
| RP 1996, c. 10, s. 214 | src:3564-3566 | encoded | `cb5-related-provisions.l4`: `the continuance is not invalid because the company was incorporated by or under an Act of Parliament within S.C. 1996, c. 10, s. 214` | Seat: Q183. Tests: cb5-tests-related.l4. |
| RP 1998, c. 30, s. 10 | src:3568-3570 | encoded | `cb5-related-provisions.l4`: `the proceeding is taken up and continued under the amended provision within S.C. 1998, c. 30, s. 10` | Seat: Q181. Tests: cb5-tests-related.l4. |
| RP 2001, c. 14, s. 136 | src:3572-3574 | fork | `cb5-related-provisions.l4`: `the last day for the review within S.C. 2001, c. 14, s. 136`; `the committee must cause a report to be laid before each House within a reasonable period within S.C. 2001, c. 14, s. 136` | Fork F-136-1: the ten years run from the previous due day, not from the day the previous review was finished. Layer 1 only: it fixes when a parliamentary committee reviews the Act; no right or duty of a shareholder, director or officer. Tests: cb5-tests-related.l4. |
| RP 2001, c. 14, s. 233 | src:3576-3577 | encoded | `cb5-related-provisions.l4`: `Part XIX.1 applies to the proceeding within S.C. 2001, c. 14, s. 233`; `Part XIX.1 governs the apportionment of the damages` | Seat: Q34. Tests: cb5-tests-related.l4. |
| RP 2009, c. 23, s. 297(6) | src:3579-3581 | encoded | `cb5-related-provisions.l4`: `the period to apply for continuance within S.C. 2009, c. 23, s. 297(6)`; `the last day to apply for continuance within S.C. 2009, c. 23, s. 297(6)`; `the body corporate is dissolved on the expiry of the period within S.C. 2009, c. 23, s. 297(6)` | Seat: Q184, Q185. Tests: cb5-tests-related.l4. |
| RP 2011, c. 25, s. 42(1) | src:3583-3588 | encoded | `cb5-related-provisions.l4`: `Act of continuance (S.C. 2011, c. 25, s. 42(1))`; `the Corporation may submit an application for continuance under the Act for the Minister's approval within S.C. 2011, c. 25, s. 42(1)` | Layer 1 only: it concerns the continuance of the named Crown corporation, not of the person's corporation. Tests: cb5-tests-related.l4. |
| RP 2011, c. 25, s. 42(2) | src:3589-3590 | encoded | `cb5-related-provisions.l4`: `the period of four years within S.C. 2011, c. 25, s. 42(2)`; `the last day to submit the application to the Minister within S.C. 2011, c. 25, s. 42(2)` | Layer 1 only: it concerns the continuance of the named Crown corporation, not of the person's corporation. Tests: cb5-tests-related.l4. |
| RP 2011, c. 25, s. 42(3) | src:3591-3592 | encoded | `cb5-related-provisions.l4`: `the Corporation must submit the application to the applicable authorities within S.C. 2011, c. 25, s. 42(3)` | Layer 1 only: it concerns the continuance of the named Crown corporation, not of the person's corporation. Tests: cb5-tests-related.l4. |
| RP 2011, c. 25, s. 42(4) | src:3593-3594 | encoded | `cb5-related-provisions.l4`: `the application is invalid solely because the Corporation is incorporated by an Act of Parliament within S.C. 2011, c. 25, s. 42(4)` | Layer 1 only: it concerns the continuance of the named Crown corporation, not of the person's corporation. Tests: cb5-tests-related.l4. |
| RP 2012, c. 19, s. 210 | src:3596-3598 | encoded | `cb5-related-provisions.l4`: `PPP Canada Inc. is an agent of Her Majesty in right of Canada within S.C. 2012, c. 19, s. 210` | Layer 1 only: it concerns the status of PPP Canada Inc., a named Crown corporation, not the person's corporation. Tests: cb5-tests-related.l4. |
| RP 2018, c. 8, s. 107.1(1) | src:3600-3602 | encoded | `cb5-related-provisions.l4`: `the day Part XIV.1 is to be referred to a committee within S.C. 2018, c. 8, s. 107.1(1)` | Layer 1 only: it fixes when a parliamentary committee reviews Part XIV.1; no right or duty of a shareholder, director or officer. Tests: cb5-tests-related.l4. |
| RP 2018, c. 8, s. 107.1(2) | src:3603-3604 | encoded | `cb5-related-provisions.l4`: `the committee must submit a report within a reasonable time within S.C. 2018, c. 8, s. 107.1(2)` | Layer 1 only: it fixes when a parliamentary committee reports on its review; no right or duty of a shareholder, director or officer. Tests: cb5-tests-related.l4. |
| Heading: AMENDMENTS NOT IN FORCE | src:3606 | inert | - | A title: the heading of the run of amendments that the source shows as not in force. Each is an inert row below. |
| NIF 2018, c. 8, s. 17: new s 150(1) | src:3608-3613 | inert | - | An amendment that the source itself shows as not in force: it would replace s 150(1) (soliciting proxies: a proxy circular must be made available to the auditor, each shareholder solicited and each director). Section 150 is in another piece's range; the unamended text is encoded there. |
| NIF 2018, c. 8, s. 17: new s 150(1.1) | src:3614-3615 | inert | - | An amendment shown as not in force: it would add an exception to s 150(1) for solicitation, other than by management, to 15 or fewer shareholders. Section 150 is in another piece's range. |
| NIF 2018, c. 8, s. 17: new s 150(1.2) | src:3616-3617 | inert | - | An amendment shown as not in force: it would add an exception to s 150(1) for solicitation conveyed in the prescribed circumstances by public broadcast, speech or publication. Section 150 is in another piece's range. |
| NIF 2018, c. 8, s. 17: new s 150(2) | src:3618-3619 | inert | - | An amendment shown as not in force: it would replace s 150(2) (a copy of the circular, with a statement and the form of proxy, is sent concurrently to the Director). Section 150 is in another piece's range. |
| NIF 2018, c. 8, s. 19: new s 153(1) | src:3621-3624 | inert | - | An amendment shown as not in force: it would replace s 153(1) (shares registered in the name of an intermediary must not be voted unless the intermediary sends the prescribed documents to the beneficial owner). Section 153 is in another piece's range. |
| NIF 2018, c. 8, s. 22: new s 159(1) | src:3626-3629 | inert | - | An amendment shown as not in force: it would replace s 159(1) (a corporation sends the prescribed financial-disclosure documents to the prescribed shareholders within a prescribed period). Section 159 is in another piece's range. |
| NIF 2018, c. 8, s. 37: new s 258.3 | src:3631-3634 | inert | - | An amendment shown as not in force: it would add s 258.3 after s 258.2, a power of the Director to exempt a corporation or person, in the prescribed circumstances, from sending notices or documents required by ss 135(1), 149, 150(1), 153(1) or 159(1). It would sit in Part XXI beside s 258.2 and is encoded nowhere until it is in force. |
| NIF 2019, c. 29, s. 142: new s 125.1 | src:3636-3639 | inert | - | An amendment shown as not in force: it would add s 125.1 after s 125, requiring a prescribed corporation to develop an approach to the remuneration of its senior management. Section 125 is in another piece's range. |
| NIF 2019, c. 29, s. 143(1): new s 172.1 | src:3641-3644 | inert | - | An amendment shown as not in force: it would replace s 172.1 (the directors of a prescribed corporation place the prescribed diversity information before the shareholders at every annual meeting). Section 172.1 is in another piece's range. |
| NIF 2019, c. 29, s. 143(1): new s 172.2(1) | src:3645-3646 | inert | - | An amendment shown as not in force: it would add s 172.2(1) (the corporation provides the diversity information to each shareholder, with the notice of meeting or by making it available). Section 172.2 is in another piece's range. |
| NIF 2019, c. 29, s. 143(1): new s 172.2(2) | src:3647-3648 | inert | - | An amendment shown as not in force: it would add s 172.2(2) (the corporation concurrently sends the diversity information to the Director). Section 172.2 is in another piece's range. |
| NIF 2019, c. 29, s. 143(2): new heading before s 172.1 | src:3649-3651 | inert | - | An amendment shown as not in force: it would replace the heading before s 172.1 by `Disclosure Relating to Diversity, Well-being and Remuneration`. A heading of a Part of the Act that is in another piece's range. |
| NIF 2019, c. 29, s. 143(3): new s 172.2 | src:3652-3654 | inert | - | An amendment shown as not in force: it would replace s 172.2 (the directors of a prescribed corporation place the information on the well-being of employees, retirees and pensioners before the shareholders at every annual meeting). Section 172.2 is in another piece's range. |
| NIF 2019, c. 29, s. 143(3): new s 172.3 | src:3655-3656 | inert | - | An amendment shown as not in force: it would add s 172.3 (the directors of a prescribed corporation place the information on recovery of incentive benefits before the shareholders). Section 172.3 is in another piece's range. |
| NIF 2019, c. 29, s. 143(3): new s 172.4(1) | src:3657-3658 | inert | - | An amendment shown as not in force: it would add s 172.4(1) (the directors place the approach to remuneration of s 125.1 before the shareholders at every annual meeting). Section 172.4 is in another piece's range. |
| NIF 2019, c. 29, s. 143(3): new s 172.4(2) | src:3659-3660 | inert | - | An amendment shown as not in force: it would add s 172.4(2) (the shareholders vote on the approach; the result is not binding on the corporation). Section 172.4 is in another piece's range. |
| NIF 2019, c. 29, s. 143(3): new s 172.4(3) | src:3661-3662 | inert | - | An amendment shown as not in force: it would add s 172.4(3) (the corporation discloses the result of the vote to the shareholders). Section 172.4 is in another piece's range. |
| NIF 2019, c. 29, s. 143(3): new s 172.5(1) | src:3663-3664 | inert | - | An amendment shown as not in force: it would add s 172.5(1) (the corporation provides the information of ss 172.1 to 172.4 to each shareholder who has not opted out, with the notice of meeting or by making it available). Section 172.5 is in another piece's range. |
| NIF 2019, c. 29, s. 143(3): new s 172.5(2) | src:3665-3666 | inert | - | An amendment shown as not in force: it would add s 172.5(2) (the corporation concurrently sends that information to the Director). Section 172.5 is in another piece's range. |
| NIF 2019, c. 29, s. 144: new s 261(1)(j) and (k) | src:3668-3671 | inert | - | An amendment shown as not in force: it would add paragraphs (j) and (k) to the regulation-making power of s 261(1) (defining `retirees` and `pensioners` for s 172.2, and prescribing the time and manner of disclosing the vote result). Regulation-making machinery, and the section it amends (261(1)) is itself an inert row above. |

## Fork register

Where I looked.
I read every `if`, `unless`, `whichever`, `or as otherwise ordered`, `subject to`, `despite`, `not later than`, `within`, `shall`/`may` pair, every list joined by `and` or `or` at the end of a paragraph, every cross-reference to a subsection, and every place the text says `prescribed`, in the whole range.
The entries below are the places where two readings both survive.
A reading that the text settles (for example "whichever is later" in s 245(1)) is not a fork and is under `## What the text turns out to say`.
The keel's fork F1 (a time limit counted from a start date: the start day is allowed, the last day included) is relied on by ss 237.3(2), 239(2)(a), 245, 252(2), 265.1 and the Related Provisions; it is the keel's, not mine.

| id | provision | readings seen | reading taken, and the text that licenses it | where | effect |
| --- | --- | --- | --- | --- | --- |
| F-239-1 | s 239(2)(a) | (A) The trailing words `if the directors of the corporation or its subsidiary do not bring, diligently prosecute or defend or discontinue the action` qualify the notice requirement only: notice is needed only where the directors are not acting. (B) They are a second requirement of the paragraph: the complainant must have given the notice (not less than fourteen days before bringing the application, or as the court otherwise orders) and the directors must be failing to act. | B. Paragraph (a) is one sentence, one of three conditions the court must find, and the words follow the notice clause with no break; on A, a complainant would satisfy (a) trivially whenever the directors are acting, and the leave test would say nothing about an action the directors are already prosecuting. The text does not say which; this is the reading that gives the trailing words work to do. | `cb5-part20-remedies.l4`: `the condition of notice to the directors is met within s 239(2)(a)` | The seat asks both the date of the notice and whether the directors are failing to act (Q55). |
| F-241-1 | s 241(6) | (A) The limit on paying under (3)(f) or (g) is worded `a payment to a shareholder`, so it protects the corporation's solvency only where the payee is a shareholder. (B) It reaches any `security holder`, which is the word (3)(f) and (g) use. | A. The subsection says `shareholder`, and the drafter used `security holder` in (3)(f) and (g), so the choice of word looks deliberate; B would be a reading of the paragraphs and not of the subsection. | `cb5-part20-remedies.l4`: `the corporation must not make the payment within s 241(6)` | A payee who holds only debt obligations is not caught. |
| F-237.5-1 | s 237.5(1)(a) | (A) Both ends of `the period between the day that the error ... occurred and the day ... that it was generally disclosed` are in the period. (B) Neither end is. (C) Only the first end is. | A. The words do not say. The first limb separately covers a plaintiff who held an interest on the day of the error, so including that day in the second limb changes nothing; the day of disclosure is taken as in the period, which brings in more plaintiffs (assumed, not ruled). | `cb5-part19-1-damages.l4`: `the position is an acquisition in the period within s 237.5(1)(a)` | A plaintiff who acquired on the day of general disclosure is treated as acquiring in the period; both days are tested. |
| F-237.7-1 | s 237.7(1)(b), (c) | (A) The limbs are an ordered fallback: the closing price; else, if the security traded that day, the average of the highest and lowest prices; else (not traded) the average of the bid and ask prices. (B) (b) applies whenever `no closing price is given`, including a security that did not trade, and (c) is then never reached for that security. | A. A security that did not trade has no highest or lowest price for (b) to average, and (c) says `if the security was not traded`; reading (c) out of the text would leave it nothing to do. | `cb5-part19-1-damages.l4`: `the value of the security within s 237.7(1)` | A security with no closing price that did not trade takes the average of bid and ask. |
| F-252.3-1 | s 252.3(3) | (A) A revoked consent is no longer a consent. (B) Revocation takes effect only from a later step (the text does not say what step). | A. The text says only that `an addressee may revoke the consent ... in the manner prescribed`; the effect of revoking must be that the consent referred to in (2)(a) no longer exists. | `cb5-part20-1-electronic.l4`: `the provision of an electronic document satisfies the requirement to provide it to the addressee within s 252.3(2)` | A document provided after a revocation does not count. |
| F-268(4)-1 | s 268(4) | (A) `Subject to subsection (6)` limits the directors' power by the Governor in Council's power to require an application. (B) It has no bearing on whether the directors may apply. | B. Subsection (6) lets the Governor in Council require a body to apply; nothing in it removes the directors' power to apply of their own motion. | `cb5-part21-charter.l4`: `the directors may apply for a certificate of continuance despite the charter within s 268(4)` | The phrase is given no effect. |
| F-265(7)-1 | s 265(7) | (A) If the correction concerns the date and the court decides otherwise, the corrected date prevails. (B) The court's decision prevails. | B. Paragraph (b) says `the court decides otherwise` without qualification, and a court's decision is the last word. | `cb5-part21-director.l4`: `the date the corrected document bears within s 265(7)` | Tested. |
| F-sched-9-1 | Schedule item 9 | (A) `for which the maximum term of imprisonment is five years or more` attaches to the offence. (B) It attaches to the tax or duty. | A. A tax or duty has no term of imprisonment; the term belongs to an offence. | `cb5-schedule-offences.l4`: `an offence is within item 9 of the Schedule` | The offence's own maximum term is the input. |
| F-125(2)-1 | S.C. 1994, c. 21, s. 125(2) | (A) `after 1988` means the calendar years 1989 and later. (B) It means from some day after 1988 begins. | A. Subsection (1) is not in the text; the only thing the rule can say is whether the year is after 1988. | `cb5-related-provisions.l4`: `subsection 125(1) applies to the year within S.C. 1994, c. 21, s. 125(2)` | The question is asked of a year. |
| F-136-1 | S.C. 2001, c. 14, s. 136 | (A) Every ten years runs from the previous due day. (B) It runs from the day the previous review was finished. | A. The text says `within every ten years thereafter`, counted from the fixed starting day, not from an event that the text does not date. | `cb5-related-provisions.l4`: `the last day for the review within S.C. 2001, c. 14, s. 136` | The nth review is due five years plus ten times (n - 1) years after the section came into force. |
| F-268(10)-1 | s 268(10), (11) | (A) (11) is an exception that prevails over (10) for a body within both. (B) (10) prevails: `may not` is the stronger word, and (11) only permits what no other provision forbids. | A. (11) is headed `Exception for railway companies` (and (10) `Continuance prohibited`), and it says such a body `may apply`; an exception that did not prevail would have no work to do. Whether a body can be within both turns on the definition of Special Act in s 87 of the Canada Transportation Act, which is not among the sources, so the two are separate inputs. | `cb5-part21-charter.l4`: `the body corporate may apply for a certificate of continuance within s 268(10) and s 268(11)` | A body within both may apply. Asserted in the layer-1 tests (`cb5-tests-part21-charter.l4`). |

## Cross-references out of my ranges

Twelve places in the modules carry a `-- out of range:` comment; the other references below are carried in a rule's name or in the description of an input or constructor, and the last column says which.
The rows are the distinct references, grouped where several sections are used the same way; the pieces are the brief's table of pieces.

| reference | piece | used in | how taken |
| --- | --- | --- | --- |
| s 19 (notice of registered office) | cb1 | s 254 | input |
| s 21.1(1) (register of individuals with significant control) | cb1 | s 250(4) | input |
| s 21.21 | cb1 | s 266(1) | input |
| s 21.303(3) | cb1 | s 266(1), s 262.2 | input; constructor of the applications whose grant is published |
| s 21.31(2), (3), (6) | cb1 | the Schedule, s 266.1(2) | the Schedule is encoded as a list; the recipient is a constructor |
| s 2(6), s 10(2), s 82(3), s 151(1), s 156, s 171(2), s 187(11) | cb1 to cb4 | s 262.2 | constructors of the applications whose grant the Director publishes |
| s 12 (names), s 187(11), s 188, s 209, s 212, s 265, s 265.1 | cb1 to cb4 and this piece | s 246 | constructors of the decisions that may be appealed |
| ss 106 and 113 (notices of directors) | cb2 | s 253(1), s 253(2) | inputs |
| Parts XI, XIII, XVII and s 174 | other pieces | s 235(1) | one input |
| s 176(1) (class votes on amendments) | cb4 | s 268(3) | inputs |
| s 187 (continuance) | cb4 | s 268(10), (11); two Related Provisions; s 246 | named in rules, no input |
| s 190 (dissent) | cb4 | s 241(5), s 268(5) | the rule says the shareholder `is not entitled to dissent under section 190` |
| s 191(4) | cb4 | s 241(4)(a) | the rule's name carries it; its content is cb4's |
| s 211 (intent to dissolve) | cb4 | s 262(1) | inputs |
| s 213 (dissolution) | cb4 | s 256(2) | input |
| s 214 (dissolution by the court) | cb4 | s 241(7) | the rule's name carries it |
| s 261(1)(c.1) (regulations) | this piece (inert) | s 262.1(1) | input (see finding 13) |
| Criminal Code ss 132 and 136 | not among the sources | s 233 | inputs |
| Criminal Code offences listed in item 1 of the Schedule | not among the sources | the Schedule | list of sections |
| Canada Evidence Act | not among the sources | s 259(2) | input |
| Personal Information Protection and Electronic Documents Act s 31(1) | not among the sources | s 252.6(2) | input |
| Canada Transportation Act s 87 | not among the sources | s 268(11) | input |
| Income Tax Act s 149.1(1) | not among the sources | s 237.2(2)(c) | a constructor of the kinds of plaintiff |
| Bank Act, Cooperative Credit Associations Act, Insurance Companies Act, Trust and Loan Companies Act, Canada Not-for-profit Corporations Act | not among the sources | s 268(4.2), (6), (10) | inputs |
| Statutory Instruments Act | not among the sources | ss 237.6(3), 237.8(3), 261(3) | inert rows |

## Needs from the core

1. `Maximum punishment on summary conviction` (largest fine, longest imprisonment in months, whether both may be imposed) is declared in `cb5-nouns.l4`.
Parts XIV and the other Parts of the Act that state offences will want the same shape; it belongs in `cbca-core.l4` under the same name, and `cb5-nouns.l4` would then shrink to nothing.
2. `Party` has no constructor for an inspector, an interested person, an affiliate or the Governor in Council; this piece takes those as plain yes-or-no facts.
If the core adds them, the investigation rules could take a `Party` instead.
3. `Strength of proof given by the Act (ss 256(2), 257(2))` is needed by any piece that meets a rule of evidence (conclusive, prima facie, none); it is declared in `cb5-part21-notices.l4` and nothing else needs it so far.
4. A shared convention for the numbers and forms that the regulations fix (the prescribed amount, fees, periods, forms): this piece names each as a plain input; if the core fixes a naming convention, I would follow it.

## What the text turns out to say

1. Section 251 states no maximum: `punishable on summary conviction` and nothing more.
The rule returns `NOTHING` for the most the court may impose, never `0` and never a figure from another statute. Asserted.
2. The ceiling for a failure to report ownership (s 235(4)) and for a false or misleading document (s 250(1)) is the same, five thousand dollars or six months or both; s 235(5) and s 250(2) give a director or officer who knowingly authorized, permitted or acquiesced the same ceiling. Asserted.
3. Section 250(3) has two requirements: the person did not know, and in the exercise of reasonable diligence could not have known; one who did not know but could have known is not immune.
It applies to subsection (2) as well as subsection (1). Asserted.
4. Section 245(1) is the later of two twenty-day dates (twenty days after receiving the articles or document, or twenty days after receiving any approval required under another Act). Asserted.
5. Section 245(2) deems a refusal when the last day has passed and the Director has neither filed the document nor given written notice of the refusal by that day; a filing or a notice made after the last day does not undo the deeming. Asserted.
6. Section 237.3(4) caps what may be reallocated to each defendant at half of the amount originally awarded against that defendant, and subsection (3) multiplies the uncollectable amount by the percentage that corresponds to that defendant's degree of responsibility for the total financial loss. Asserted.
7. Section 237.5(1)(b) says `not more than the prescribed amount`, so a holding equal to the amount qualifies; s 237.6(1) says `greater than`, so the court's power starts above it. The two meet with no gap and no overlap. Asserted (in `cb5-tests-part19-1.l4`, and in the seat cases for Q41 and Q44, at 100000 against 100000).
8. Section 253(3) gives a day of deemed receipt only for a notice sent as s 253(1) allows to a shareholder or director where there are no reasonable grounds to believe it was not received; otherwise the Act fixes no day, and the rule returns `NOTHING`. Asserted.
9. Section 252(2) says `within but not later than` two years: the anniversary is in time and the day after is too late. Asserted.
10. Sections 241(5) and 268(5) take away the right to dissent under section 190 only for an amendment made under them; whether the right exists in any other case is section 190's. The seat therefore asks "am I barred from dissenting", not "can I dissent". Asserted.
11. Section 241(4)(b) bars another amendment to the articles or by-laws only after an order directing an amendment, and only until the court consents or otherwise orders. Asserted.
12. Subsection 268(11) is headed `Exception for railway companies` and says a body incorporated by or under a Special Act, as defined in section 87 of the Canada Transportation Act, `may apply` for a certificate of continuance; subsection 268(10) says a body to which the Canada Not-for-profit Corporations Act applies, or a similar body incorporated otherwise than by or under an Act of Parliament, `may not`.
The rule lets (11) prevail when a body is within both (fork F-268(10)-1), and whether any body is within both depends on a definition that is not among the sources; each is a separate input. Asserted.
13. Section 262.1(1) allows a signature `in accordance with the regulations made under paragraph 261(1)(c.1)`, but paragraph 261(1)(c.1) (src:3237) authorises regulations `prescribing, for the purposes of subsection 137(1.1), a manner of determining the number of shares required for a person to be eligible to submit a proposal`, which on its face does not concern signatures.
The rule takes `the signature is in accordance with the regulations` as a plain input and asserts nothing about the paragraph. Not asserted.
14. Section 233 does two things: nobody is excused from giving evidence to an inspector because it may incriminate them, and what they say may not be used against them in a later proceeding under an Act of Parliament, other than a prosecution for perjury (Criminal Code s 132) or under Criminal Code s 136 in respect of the evidence.
A proceeding under a provincial law is therefore not within the bar. Asserted.
15. Two provisions say an applicant need not give security for costs (s 229(4) for an applicant for an investigation, s 242(3) for a complainant); each is a rule that is constant `FALSE` (security is not required). Asserted.
16. Section 252.3(1) says nothing in the Act or the regulations requires a person to create or provide an electronic document; it is a constant `FALSE`. Asserted.
17. Section 239(2)(a) says the notice must be given `not less than fourteen days before bringing the application`, so fourteen days is enough. Asserted (`cb5-tests-part20.l4`).
18. Section 241(6) forbids a payment to a shareholder under paragraph (3)(f) or (g) where there are reasonable grounds for believing that the corporation is or would after the payment be unable to pay its liabilities as they become due, or that the realizable value of its assets would thereby be less than the aggregate of its liabilities.
Paragraphs (3)(f) and (g) are themselves worded `subject to subsection (6)`, so the seat's question whether the court may make such an order takes the forbidden payment as a fact. Asserted.
19. The Related Provisions of 2011, c. 25, s. 42 and 2012, c. 19, s. 210 concern named Crown corporations, and 1994, c. 24, s. 33, 2001, c. 14, s. 136 and 2018, c. 8, s. 107.1 concern Parliament's reviews; none gives a shareholder, director or officer a right or a duty. Asserted in layer 1 (`cb5-tests-related.l4`); the seat has no question on them.
20. Section 125(2) of 1994, c. 21 says `Subsection (1) applies after 1988` and subsection (1) is not in the text; no more than the year can be tested. Asserted.

## What the stable binary does not accept

The binary is `l4` 1.6.98 (the stable `main` dialect), and the check was `L4_TARGET=unstable` (one binary).
What I met, and what I did:

1. Loud: a chain of `ELSE IF` written on new lines at the same column is a parse error (`incorrect indentation (got 26, should be greater than 26)`); each nested `ELSE IF` is indented deeper than the previous `IF`.
2. Loud: a one-line `WITH` record and a `LIST` of one-line `WITH` records are rejected; the Schedule's 194 rows are built by a helper constructor function (`a listed offence provision`), and the seat's list of positions uses a multi-line `LIST ... WITH` inside `THEN`.
3. Loud: a multi-line body in `any (GIVEN row YIELD ...)` mis-parses; the body is a helper rule (`a row of the Schedule matches the offence`).
4. Loud: there is no `++` and no `LENGTH`; the prelude's lowercase `concat`, `append`, `count`, `any`, `all`, `elem`, `null` are used.
5. Loud: a `NOT` before a call must be parenthesised.
6. Not available, by choice of dialect: `REFUSE`, `BECAUSE`, section `GIVEN`, `TYPICALLY`, sets, `EVERY`, `WITHIN ... OF`, the ledger and a bodiless `DECLARE`; where the text does not answer, `MAYBE` and `NOTHING`, or a named constructor, stands in.
7. Assumption, not a limit: no `DEONTIC` rule is written. The Act's `shall` and `may` become yes-or-no rules in the person's or the official's mouth (`must give notice`, `may apply`), and a court's or the Director's judgment is a conditional input.
8. Silent: `Check succeeded` does not show that a module is complete. A module truncated while it was being written (a section missing) still checked clean, because nothing referred to the missing rule; only a test that named it failed. The coverage script therefore reads each module to confirm every `where` name exists.
9. Silent: positional arguments of the same type are order-dependent; a script lined up each seat question's arguments against the layer-1 rule's `GIVEN` and the cases were chosen so that a swap fails.
10. Enumeration constructors are global; every constructor carries its section.

## What check.sh prints

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
cb5-cases-seat.l4                              0       551       0        0         0
cb5-nouns.l4                                   0         0       0        0         0
cb5-part19-1-damages.l4                        0         0       0        0         0
cb5-part19-investigation.l4                    0         0       0        0         0
cb5-part20-1-electronic.l4                     0         0       0        0         0
cb5-part20-offences.l4                         0         0       0        0         0
cb5-part20-remedies.l4                         0         0       0        0         0
cb5-part21-charter.l4                          0         0       0        0         0
cb5-part21-director.l4                         0         0       0        0         0
cb5-part21-notices.l4                          0         0       0        0         0
cb5-related-provisions.l4                      0         0       0        0         0
cb5-schedule-offences.l4                       0         0       0        0         0
cb5-seat.l4                                    0         0       0        0         0
cb5-tests-part19-1.l4                          0       109       0        0         0
cb5-tests-part19.l4                            0       106       0        0         0
cb5-tests-part20-1.l4                          0        51       0        0         0
cb5-tests-part20-offences.l4                   0        43       0        0         0
cb5-tests-part20.l4                            0       146       0        0         0
cb5-tests-part21-charter.l4                    0        53       0        0         0
cb5-tests-part21-director.l4                   0       146       0        0         0
cb5-tests-part21-notices.l4                    0        52       0        0         0
cb5-tests-related.l4                           0        55       0        0         0
cb5-tests-schedule.l4                          0        87       0        0         0
cbca-core-control.l4                           0         0       0        0         0
cbca-core-definitions.l4                       0         0       0        0         0
cbca-core-isc.l4                               0         0       0        0         0
cbca-core.l4                                   0         0       0        0         0
TOTAL (27 modules)                             0      1399       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Layer 1 has 848 assertions in its ten test files, all included in the totals above; layer 2 has 551.
`python3 -I srcrefs.py check --refs ../../registers/source-bundle/R.S.C.-1985-c.-C-44.txt cb5-*.l4` reports 0 problems.

## Before this is worth relying on

1. The source is an unofficial plain-text rendering; the text of every section should be compared with the official consolidation.
2. The regulations are not among the sources: the prescribed amount (s 237.5(1)(b)), the fees and when they fall due (s 261.1), the prescribed periods (s 267(3)), the prescribed forms, and the regulations under s 261(1)(c.1) are inputs. The answers are only as good as the figures a user supplies.
3. Every judgment of a court, the Director or an inspector is an input. The layer says "if the court is satisfied, then ...", not whether it will be.
4. Eleven forks are taken (twelve `fork` rows in the coverage table, because s 268(10) and s 268(11) share F-268(10)-1); F-239-1 (the derivative-action notice), F-241-1 (shareholder or security holder) and F-237.7-1 (the valuation limbs) change answers and need a lawyer's reading.
5. The twelve `-- out of range:` places in the modules, and the 25 rows of the cross-reference table, depend on other pieces (cb1: ss 19, 21.1, 21.21, 21.303; cb2: ss 106, 113; cb4: ss 176, 187, 190, 191(4), 211, 213, 214); until those pieces are merged and checked, those inputs are plain facts.
6. The Related Provisions' commencement dates are unknown (they are in the amending Acts), so each is an input.
7. No real person has used the seat's questions; the wording of the `@desc` lines has not been tested on a first-time reader.
8. Rules about officials alone (the Director's power to apply for directions, the inspector's report to the Director, the Parliament reviews, the two named Crown corporations) are encoded in layer 1 and not asked.
