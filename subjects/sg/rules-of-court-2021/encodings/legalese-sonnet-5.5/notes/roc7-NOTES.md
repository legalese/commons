# NOTES: roc7, Rules of Court 2021 (Singapore), G.N. No. S 914/2021, Orders 28 to 33

Range: lines 4194 to 5050 of `SCJA1969-S914-2021.txt`: Order 28 (electronic filing service), Order 29 (referrals on issues of law), Order 29A (requests for opinions on questions of foreign law), Orders 30 and 31 (references under Article 100 of the Constitution for advisory opinion; constitutional case), Order 32 (administration and similar actions) and Order 33 (Admiralty proceedings and marine insurance claims).
Text: the version current as at 5 November 2026.
The source file is a plain-text rendering made by a converter script from Singapore Statutes Online.
It is not the official text, and nothing here has been checked against the official text.

Status, as run on 2026-11-05: every roc7 file runs with 0 errors and 0 warnings on main 1.6.109 and gives the same four counts on main 1.6.108; `check.sh` prints 20 modules and 3495 assertions satisfied, none failed, none refused (see the end); `srcrefs.py check --refs` and `--strict` report 0 problems on every roc7 file.
Nothing in this row is checked against the official text or by a lawyer.

Files (all in this folder): layer 1 is `roc7-order-28.l4`, `roc7-order-29.l4` (Orders 29 and 29A), `roc7-order-30.l4` (Orders 30 and 31), `roc7-order-32.l4`, `roc7-order-33a.l4` (rules 1 to 17), `roc7-order-33b.l4` (rules 18 to 28), `roc7-order-33c.l4` (rules 29 to 46) and `roc7-order-duties.l4` (eight duties with a time limit, written as regulative rules); their tests are `roc7-tests-28.l4`, `-29`, `-30`, `-32`, `-33a`, `-33b`, `-33c` and `-duties`; layer 2 is `roc7-seat.l4` and `roc7-cases-seat.l4`.
The layer-1 modules hold 629 decision and helper functions, each citing its source lines with `@ref` and quoting them.
The keel files `roc-core.l4` and `roc-definitions.l4` are imported and not edited.

## Coverage (roc7)

One row per unit of the text in lines 4194 to 5050: an Order or Part heading, a rule, a subsection, a paragraph, a sub-paragraph, a sub-sub-paragraph or a defined term.
The units were found by a script (`work/units.py`, not shipped) and its audit found every non-blank line of the range inside some unit and none outside.
Audit counts: text units counted 703; rows in the table before 107 (the rows of `inputs/RULE-INDEX.md` for this range: 100 rules and 7 Order headings), after 703.
Dispositions: encoded 695; inert reason 1 (not operative) 8; inert reason 2 (machinery) 0; inert reason 3 (shown repealed or blank) 0.
The 8 inert rows are the headings of Orders 28, 29, 29A, 30, 31, 32 and 33 and the heading of Part 2 (line 4478); each is a heading with no operative words.
There is no out-of-scope or deferred row.
A unit that has no function of its own is covered by the function of its nearest enclosing provision, which the cell then names (`covered with ...`), or it is a rule or subsection whose paragraphs have their own rows (`see the sub-rows`).
A cell lists at most five names; the rest are under the same provision label in the file.
The fork column names the forks of the register below whose text the unit carries.
The 167 Order 28 rows were typed by hand (the same typing feeds the jural table); the others were mapped by script from each function's provision label to the unit, because the labels (`o 33 r 4(2)(a) ...`) follow the text's own numbering.

| unit | lines | disposition | L4 name(s) | fork |
| --- | --- | --- | --- | --- |
| O28 | 4194-4195 | inert-1 | (heading: not operative) |  |
| O28 r1 | 4196-4207 | encoded | `o 28 r 1 a defined term has its defined meaning` |  |
| O28 r1 def “authorised user” | 4197 | encoded | `o 28 r 1 a person is an authorised user` |  |
| O28 r1 def “deemed” | 4198 | encoded | `o 28 r 1 a deeming under this Order stands` | F-28-3 |
| O28 r1 def “electronic filing service” | 4199 | encoded | `o 28 r 1 a service is the electronic filing service` |  |
| O28 r1 def “electronic filing service provider” | 4200 | encoded | `o 28 r 1 a provider is an electronic filing service provider` |  |
| O28 r1 def “electronic transmission” | 4201 | encoded | `o 28 r 1 a transmission is electronic transmission` |  |
| O28 r1 def “entity” | 4202 | encoded | `o 28 r 1 a body is an entity` |  |
| O28 r1 def “identification code” | 4203 | encoded | `o 28 r 1 a code is an identification code` |  |
| O28 r1 def “public authority” | 4204 | encoded | `o 28 r 1 a body is a public authority` |  |
| O28 r1 def “registered foreign lawyer” | 4205 | encoded | `o 28 r 1 a person is a registered foreign lawyer` |  |
| O28 r1 def “registered user” | 4206 | encoded | `o 28 r 1 a body is a registered user` |  |
| O28 r1 def “service bureau” | 4207 | encoded | `o 28 r 1 a bureau is a service bureau` |  |
| O28 r2 | 4208-4209 | encoded | `o 28 r 2 the Registrar may establish an electronic filing service` |  |
| O28 r3 | 4210-4211 | encoded | see the sub-rows |  |
| O28 r3(1) | 4211 | encoded | `o 28 r 3(1) the service is operated by a provider appointed as required` | F-28-4 |
| O28 r3(2) | 4211 | encoded | `o 28 r 3(2) a body is the superintendent of a provider` |  |
| O28 r4 | 4212-4213 | encoded | `o 28 r 4 equipment is part of the computer system of a provider` |  |
| O28 r5 | 4214-4216 | encoded | see the sub-rows |  |
| O28 r5(1) | 4215 | encoded | `o 28 r 5(1) the Registrar may establish or appoint agents to establish a service bureau` |  |
| O28 r5(2) | 4215 | encoded | `o 28 r 5(2) an appointed agent is treated as an agent for accepting payment of fees or service charges` |  |
| O28 r5(3) | 4216 | encoded | `o 28 r 5(3) a body is the superintendent of an appointed agent` |  |
| O28 r6 | 4217-4227 | encoded | see the sub-rows |  |
| O28 r6(1) | 4218 | encoded | `o 28 r 6(1) an entity may apply to be a registered user` |  |
| O28 r6(2) | 4218 | encoded | `o 28 r 6(2) a registered user may designate a person as an authorised user` |  |
| O28 r6(3) | 4219 | encoded | `o 28 r 6(3) the Registrar may allow a registered user or an authorised user on terms` |  |
| O28 r6(4) | 4220 | encoded | `o 28 r 6(4) the entity or person is deemed registered or designated under this Rule` |  |
| O28 r6(5) | 4221 | encoded | `o 28 r 6(5) the registered user is deemed to approve use of the identification code` |  |
| O28 r6(6) | 4222 | encoded | `o 28 r 6(6) the registered user has met the conditions for using the electronic filing service` | F-28-5 |
| O28 r6(6)(a) | 4222-4223 | encoded | `o 28 r 6(6) the registered user has met the conditions for using the electronic filing service` | F-28-5 |
| O28 r6(6)(b) | 4224-4225 | encoded | `o 28 r 6(6) the registered user has met the conditions for using the electronic filing service` | F-28-5 |
| O28 r6(7) | 4226 | encoded | `o 28 r 6(7) the Registrar may waive paragraph (6)` |  |
| O28 r6(8) | 4227 | encoded | `o 28 r 6(8) a service bureau is deemed to be a registered user`; `o 28 r 6(8) an employee of a service bureau is deemed to be an authorised user` |  |
| O28 r7 | 4228-4277 | encoded | see the sub-rows |  |
| O28 r7(1) | 4229 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(a) | 4229-4230 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(b) | 4231-4232 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(c) | 4233-4234 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(d) | 4235-4236 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(e) | 4237-4238 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(f) | 4239-4240 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(g) | 4241-4242 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(1)(h) | 4243-4244 | encoded | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` | F-28-6 |
| O28 r7(2) | 4245 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(2)(a) | 4245-4246 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(2)(b) | 4247-4248 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(2)(b)(i) | 4248-4249 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(2)(b)(ii) | 4250-4251 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(2)(c) | 4252-4253 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(2)(d) | 4254-4255 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(2)(e) | 4256-4257 | encoded | `o 28 r 7(2) paragraph (1) applies with a modification`; `o 28 r 7(2) the number counted in place of advocates and solicitors` |  |
| O28 r7(3) | 4258 | encoded | `o 28 r 7(3) no fee is payable by the registered user` |  |
| O28 r7(3)(a) | 4258-4259 | encoded | `o 28 r 7(3) no fee is payable by the registered user` |  |
| O28 r7(3)(b) | 4260-4261 | encoded | `o 28 r 7(3) no fee is payable by the registered user` |  |
| O28 r7(4) | 4262 | encoded | `o 28 r 7(4) the relevant time`; `o 28 r 7(4) a relevant time arises in this way` | F-28-1 |
| O28 r7(4) def “relevant time” | 4262 | encoded | `o 28 r 7(4) the relevant time`; `o 28 r 7(4) a relevant time arises in this way` | F-28-1 |
| O28 r7(4)(a) | 4262-4263 | encoded | `o 28 r 7(4) the relevant time`; `o 28 r 7(4) a relevant time arises in this way` | F-28-1 |
| O28 r7(4)(b) | 4264-4265 | encoded | `o 28 r 7(4) the relevant time`; `o 28 r 7(4) a relevant time arises in this way` | F-28-1 |
| O28 r7(4)(c) | 4266-4267 | encoded | `o 28 r 7(4) the relevant time`; `o 28 r 7(4) a relevant time arises in this way` | F-28-1 |
| O28 r7(4)(d) | 4268-4269 | encoded | `o 28 r 7(4) the relevant time`; `o 28 r 7(4) a relevant time arises in this way` | F-28-1 |
| O28 r7(5) | 4270 | encoded | `o 28 r 7(5) the fee is payable for the month` |  |
| O28 r7(6) | 4271 | encoded | `o 28 r 7(6) the day the fee for a month is due and payable`; `o 28 r 7(6) the fee for the month is due and payable on the day` |  |
| O28 r7(7) | 4272 | encoded | `o 28 r 7(7) the Registrar may waive, refund or defer the fee` |  |
| O28 r7(8) | 4273 | encoded | see the sub-rows |  |
| O28 r7(8)(a) | 4273-4274 | encoded | `o 28 r 7(8)(a) the Registrar must refund the amount paid in excess or error`; `o 28 r 7(8)(a) the claim is made in writing in time`; `o 28 r 7(8)(a) the act is done by the last day` | F-ALL-1 |
| O28 r7(8)(b) | 4275-4276 | encoded | `o 28 r 7(8)(b) the Registrar may refund in any other case` |  |
| O28 r7(9) | 4277 | encoded | `o 28 r 7(9) the manner of informing the Registrar is set out in practice directions` |  |
| O28 r8 | 4278-4299 | encoded | see the sub-rows |  |
| O28 r8(1) | 4279 | encoded | `o 28 r 8(1) the requirement to use the electronic filing service arises`; `o 28 r 8(1) the document is filed using the electronic filing service as required` | F-28-5 |
| O28 r8(2) | 4279 | encoded | `o 28 r 8(2) the requirement is satisfied by a single copy filed using the electronic filing service` |  |
| O28 r8(3) | 4280 | encoded | `o 28 r 8(3) the way of using the electronic filing service is one of the 2 ways` |  |
| O28 r8(3)(a) | 4280-4281 | encoded | `o 28 r 8(3) the way of using the electronic filing service is one of the 2 ways` |  |
| O28 r8(3)(b) | 4282-4283 | encoded | `o 28 r 8(3) the way of using the electronic filing service is one of the 2 ways` |  |
| O28 r8(4) | 4284 | encoded | `o 28 r 8(4) a document may be filed other than using the electronic filing service` | F-28-7 |
| O28 r8(5) | 4285 | encoded | `o 28 r 8(5) the form of the document is as required` | F-28-5 |
| O28 r8(5)(a) | 4285-4286 | encoded | `o 28 r 8(5) the form of the document is as required` | F-28-5 |
| O28 r8(5)(b) | 4287-4289 | encoded | `o 28 r 8(5) the form of the document is as required` | F-28-5 |
| O28 r8(6) | 4290 | encoded | `o 28 r 8(6) the document is deemed filed by the registered user with that user's intention` |  |
| O28 r8(7) | 4291 | encoded | `o 28 r 8(7)(a) the document is deemed conveyed by the authorised user on behalf and with the authority of the registered user`; `o 28 r 8(7)(b) the document is deemed conveyed with the intention of the registered user` |  |
| O28 r8(7)(a) | 4291-4292 | encoded | `o 28 r 8(7)(a) the document is deemed conveyed by the authorised user on behalf and with the authority of the registered user`; `o 28 r 8(7)(b) the document is deemed conveyed with the intention of the registered user` |  |
| O28 r8(7)(b) | 4293-4294 | encoded | `o 28 r 8(7)(a) the document is deemed conveyed by the authorised user on behalf and with the authority of the registered user`; `o 28 r 8(7)(b) the document is deemed conveyed with the intention of the registered user` |  |
| O28 r8(8) | 4295 | encoded | `o 28 r 8(8)(a) the document is deemed conveyed on behalf and with the authority of the person tendering it`; `o 28 r 8(8)(b) the document is deemed conveyed on behalf and with the authority of the principal` | F-28-8 |
| O28 r8(8)(a) | 4295-4296 | encoded | `o 28 r 8(8)(a) the document is deemed conveyed on behalf and with the authority of the person tendering it`; `o 28 r 8(8)(b) the document is deemed conveyed on behalf and with the authority of the principal` | F-28-8 |
| O28 r8(8)(b) | 4297-4298 | encoded | `o 28 r 8(8)(a) the document is deemed conveyed on behalf and with the authority of the person tendering it`; `o 28 r 8(8)(b) the document is deemed conveyed on behalf and with the authority of the principal` | F-28-8 |
| O28 r8(9) | 4299 | encoded | `o 28 r 8(9) the document is a secure electronic record` |  |
| O28 r9 | 4300-4317 | encoded | see the sub-rows |  |
| O28 r9(1) | 4301 | encoded | `o 28 r 9(1) a requirement of signing by an authorised user or a registered user is deemed complied with` |  |
| O28 r9(2) | 4301 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(a) | 4301-4302 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(a)(i) | 4302-4303 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(a)(ii) | 4304-4305 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(b) | 4306-4307 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(b)(i) | 4307-4308 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(b)(ii) | 4309-4310 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(c) | 4311-4312 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(c)(i) | 4312-4313 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(2)(c)(ii) | 4314-4315 | encoded | `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user`; `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user`; `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user`; `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it`; `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | F-28-8 |
| O28 r9(3) | 4316 | encoded | `o 28 r 9(3) the requirement for the signature of an advocate or solicitor is deemed met` |  |
| O28 r9(4) | 4317 | encoded | `o 28 r 9(4) the application of the identification code is a secure electronic signature` |  |
| O28 r10 | 4318-4343 | encoded | see the sub-rows |  |
| O28 r10(1) | 4319 | encoded | `o 28 r 10(1) the document is deemed filed, served, delivered or conveyed`; `o 28 r 10 the moment the document is deemed filed` | F-28-9 |
| O28 r10(1)(a) | 4319-4320 | encoded | `o 28 r 10(1) the document is deemed filed, served, delivered or conveyed`; `o 28 r 10 the moment the document is deemed filed` | F-28-9 |
| O28 r10(1)(b) | 4321-4322 | encoded | `o 28 r 10(1) the document is deemed filed, served, delivered or conveyed`; `o 28 r 10 the moment the document is deemed filed` | F-28-9 |
| O28 r10(1)(c) | 4323-4324 | encoded | `o 28 r 10(1) the document is deemed filed, served, delivered or conveyed`; `o 28 r 10 the moment the document is deemed filed` | F-28-9 |
| O28 r10(2) | 4325 | encoded | `o 28 r 10(2) paragraph (1) applies to the document` |  |
| O28 r10(2)(a) | 4325-4326 | encoded | `o 28 r 10(2) paragraph (1) applies to the document` |  |
| O28 r10(2)(b) | 4327-4328 | encoded | `o 28 r 10(2) paragraph (1) applies to the document` |  |
| O28 r10(3) | 4329 | encoded | `o 28 r 10(3) the caveat is deemed filed at the moment the Registrar accepts it`; `o 28 r 10 the moment the document is deemed filed` |  |
| O28 r10(3)(a) | 4329-4330 | encoded | `o 28 r 10(3) the caveat is deemed filed at the moment the Registrar accepts it`; `o 28 r 10 the moment the document is deemed filed` |  |
| O28 r10(3)(b) | 4331-4332 | encoded | `o 28 r 10(3) the caveat is deemed filed at the moment the Registrar accepts it`; `o 28 r 10 the moment the document is deemed filed` |  |
| O28 r10(4) | 4333 | encoded | `o 28 r 10(4) the originating process is deemed issued`; `o 28 r 10(4) the moment the originating process is deemed issued` |  |
| O28 r10(4)(a) | 4333-4334 | encoded | `o 28 r 10(4) the originating process is deemed issued`; `o 28 r 10(4) the moment the originating process is deemed issued` |  |
| O28 r10(4)(b) | 4335-4336 | encoded | `o 28 r 10(4) the originating process is deemed issued`; `o 28 r 10(4) the moment the originating process is deemed issued` |  |
| O28 r10(5) | 4337 | encoded | `o 28 r 10(5) the registered user may produce a record as evidence of filing or issuance` |  |
| O28 r10(5)(a) | 4337-4338 | encoded | `o 28 r 10(5) the registered user may produce a record as evidence of filing or issuance` |  |
| O28 r10(5)(b) | 4339-4340 | encoded | `o 28 r 10(5) the registered user may produce a record as evidence of filing or issuance` |  |
| O28 r10(5)(c) | 4341-4342 | encoded | `o 28 r 10(5) the registered user may produce a record as evidence of filing or issuance` |  |
| O28 r10(6) | 4343 | encoded | `o 28 r 10(6) the Registrar may cause an earlier date and time to be reflected`; `o 28 r 10 the moment the document is deemed filed` |  |
| O28 r11 | 4344-4346 | encoded | see the sub-rows |  |
| O28 r11(1) | 4345 | encoded | `o 28 r 11(1) time for service cannot yet begin to run`; `o 28 r 11(1) time for service has begun to run`; `o 28 r 11 the moment time for service begins to run` | F-28-10 |
| O28 r11(2) | 4345 | encoded | `o 28 r 11 the moment time for service begins to run` | F-28-10 |
| O28 r11(3) | 4346 | encoded | `o 28 r 11(3) the first working day on or after`; `o 28 r 11 the moment time for service begins to run` | F-28-2 |
| O28 r12 | 4347-4371 | encoded | see the sub-rows |  |
| O28 r12(1) | 4348 | encoded | `o 28 r 12(1) service may be effected using the electronic filing service` |  |
| O28 r12(1)(a) | 4348-4349 | encoded | `o 28 r 12(1) service may be effected using the electronic filing service` |  |
| O28 r12(1)(b) | 4350-4352 | encoded | `o 28 r 12(1) service may be effected using the electronic filing service` |  |
| O28 r12(2) | 4353 | encoded | `o 28 r 12(2) the party is deemed to have agreed to be served using the electronic filing service` |  |
| O28 r12(3) | 4354 | encoded | `o 28 r 12 the moment service is deemed effected`; `o 28 r 12(3)(a) the document is deemed served by electronic transmission`; `o 28 r 12(3)(b) the remotely composed document is deemed served` |  |
| O28 r12(3)(a) | 4354-4355 | encoded | `o 28 r 12 the moment service is deemed effected`; `o 28 r 12(3)(a) the document is deemed served by electronic transmission`; `o 28 r 12(3)(b) the remotely composed document is deemed served` |  |
| O28 r12(3)(b) | 4356-4357 | encoded | `o 28 r 12 the moment service is deemed effected`; `o 28 r 12(3)(a) the document is deemed served by electronic transmission`; `o 28 r 12(3)(b) the remotely composed document is deemed served` |  |
| O28 r12(4) | 4358 | encoded | `o 28 r 12(4) the person serving may produce a record of service as evidence` |  |
| O28 r12(5) | 4359 | encoded | `o 28 r 12(5) the person serving may file a Registrar's certificate of service in lieu of an affidavit`; `o 28 r 12(5) the certificate is regarded as prima facie evidence of service` |  |
| O28 r12(6) | 4360 | encoded | `o 28 r 12(6) service on more than one person may be effected using the electronic filing service on those who are users` |  |
| O28 r12(7) | 4361 | encoded | `o 28 r 12(7) the document is deemed served by the registered user with that user's intention` |  |
| O28 r12(8) | 4362 | encoded | `o 28 r 12(8)(a) the document is deemed served by the authorised user on behalf and with the authority of the registered user`; `o 28 r 12(8)(b) the document is deemed served with the intention of the registered user` |  |
| O28 r12(8)(a) | 4362-4363 | encoded | `o 28 r 12(8)(a) the document is deemed served by the authorised user on behalf and with the authority of the registered user`; `o 28 r 12(8)(b) the document is deemed served with the intention of the registered user` |  |
| O28 r12(8)(b) | 4364-4365 | encoded | `o 28 r 12(8)(a) the document is deemed served by the authorised user on behalf and with the authority of the registered user`; `o 28 r 12(8)(b) the document is deemed served with the intention of the registered user` |  |
| O28 r12(9) | 4366 | encoded | `o 28 r 12(9)(a) the document is deemed served on behalf and with the authority of the person tendering it`; `o 28 r 12(9)(b) the document is deemed served on behalf and with the authority of the principal` | F-28-8 |
| O28 r12(9)(a) | 4366-4367 | encoded | `o 28 r 12(9)(a) the document is deemed served on behalf and with the authority of the person tendering it`; `o 28 r 12(9)(b) the document is deemed served on behalf and with the authority of the principal` | F-28-8 |
| O28 r12(9)(b) | 4368-4369 | encoded | `o 28 r 12(9)(a) the document is deemed served on behalf and with the authority of the person tendering it`; `o 28 r 12(9)(b) the document is deemed served on behalf and with the authority of the principal` | F-28-8 |
| O28 r12(10) | 4370 | encoded | `o 28 r 12(10) the document is a secure electronic record` |  |
| O28 r12(11) | 4371 | encoded | `o 28 r 12(11) Order 7, Rule 8 applies to the service`; `o 28 r 12(11) the day service through the electronic filing service is deemed effected` |  |
| O28 r13 | 4372-4373 | encoded | `o 28 r 13 the Registrar may notify or deliver using the electronic filing service` |  |
| O28 r14 | 4374-4375 | encoded | `o 28 r 14 the amendment is effected in the manner prescribed in the practice directions` | F-28-5 |
| O28 r15 | 4376-4383 | encoded | see the sub-rows |  |
| O28 r15(1) | 4377 | encoded | `o 28 r 15(1) the affidavit may be used to the same extent as a paper affidavit` |  |
| O28 r15(2) | 4377 | encoded | `o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way`; `o 28 r 15(2)(b) a true and complete electronic image of the original is created`; `o 28 r 15(2)(c) the original paper affidavit is retained for 7 years` | F-28-5 |
| O28 r15(2)(a) | 4377-4378 | encoded | `o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way`; `o 28 r 15(2)(b) a true and complete electronic image of the original is created`; `o 28 r 15(2)(c) the original paper affidavit is retained for 7 years` | F-28-5 |
| O28 r15(2)(b) | 4379-4380 | encoded | `o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way`; `o 28 r 15(2)(b) a true and complete electronic image of the original is created`; `o 28 r 15(2)(c) the original paper affidavit is retained for 7 years` | F-28-5 |
| O28 r15(2)(c) | 4381-4382 | encoded | `o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way`; `o 28 r 15(2)(b) a true and complete electronic image of the original is created`; `o 28 r 15(2)(c) the original paper affidavit is retained for 7 years` | F-28-5, F-ALL-1 |
| O28 r15(3) | 4383 | encoded | `o 28 r 15(3) the Court may permit the electronic image to be used` |  |
| O28 r16 | 4384-4389 | encoded | `o 28 r 16 the information contained in the document prevails`; `o 28 r 16 the information entered into the electronic template prevails` |  |
| O28 r16(a) | 4385-4386 | encoded | `o 28 r 16 the information contained in the document prevails`; `o 28 r 16 the information entered into the electronic template prevails` |  |
| O28 r16(b) | 4387-4389 | encoded | `o 28 r 16 the information contained in the document prevails`; `o 28 r 16 the information entered into the electronic template prevails` |  |
| O28 r17 | 4390-4404 | encoded | see the sub-rows |  |
| O28 r17(1) | 4391 | encoded | `o 28 r 17(1) a user registered by the Registrar of the Supreme Court is treated as also registered by the other two Registrars` |  |
| O28 r17(2) | 4391 | encoded | `o 28 r 17(2) a user registered by the Registrar of the State Courts is treated as also registered by the other two Registrars` |  |
| O28 r17(3) | 4392 | encoded | `o 28 r 17(3) a user registered by the Registrar of the Family Justice Courts is treated as also registered by the other two Registrars` |  |
| O28 r17(4) | 4393 | encoded | `o 28 r 17(4)(a) a Supreme Court service bureau may be used for State Courts proceedings`; `o 28 r 17(4)(b) a Supreme Court service bureau may be used for Family Justice Courts proceedings` |  |
| O28 r17(4)(a) | 4393-4394 | encoded | `o 28 r 17(4)(a) a Supreme Court service bureau may be used for State Courts proceedings`; `o 28 r 17(4)(b) a Supreme Court service bureau may be used for Family Justice Courts proceedings` |  |
| O28 r17(4)(b) | 4395-4396 | encoded | `o 28 r 17(4)(a) a Supreme Court service bureau may be used for State Courts proceedings`; `o 28 r 17(4)(b) a Supreme Court service bureau may be used for Family Justice Courts proceedings` |  |
| O28 r17(5) | 4397 | encoded | `o 28 r 17(5)(a) a State Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(5)(b) a State Courts service bureau may be used for Family Justice Courts proceedings` |  |
| O28 r17(5)(a) | 4397-4398 | encoded | `o 28 r 17(5)(a) a State Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(5)(b) a State Courts service bureau may be used for Family Justice Courts proceedings` |  |
| O28 r17(5)(b) | 4399-4400 | encoded | `o 28 r 17(5)(a) a State Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(5)(b) a State Courts service bureau may be used for Family Justice Courts proceedings` |  |
| O28 r17(6) | 4401 | encoded | `o 28 r 17(6)(a) a Family Justice Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(6)(b) a Family Justice Courts service bureau may be used for State Courts proceedings` |  |
| O28 r17(6)(a) | 4401-4402 | encoded | `o 28 r 17(6)(a) a Family Justice Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(6)(b) a Family Justice Courts service bureau may be used for State Courts proceedings` |  |
| O28 r17(6)(b) | 4403-4404 | encoded | `o 28 r 17(6)(a) a Family Justice Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(6)(b) a Family Justice Courts service bureau may be used for State Courts proceedings` |  |
| O29 | 4405-4406 | inert-1 | (heading: not operative) |  |
| O29 r1 | 4407-4411 | encoded | `o 29 r 1 a defined term has its defined meaning`; `o 29 r 1 a court is the Court`; `o 29 r 1 a place is a foreign country`; `o 29 r 1 a court is a specified court`; `o 29 r 1 a place is a specified foreign country` |  |
| O29 r1 def “Court” | 4408 | encoded | `o 29 r 1 a court is the Court` |  |
| O29 r1 def “foreign country” | 4409 | encoded | `o 29 r 1 a place is a foreign country` |  |
| O29 r1 def “specified court” | 4410 | encoded | `o 29 r 1 a court is a specified court`; `o 29 r 7 a court is a specified court` | F-29-1 |
| O29 r1 def “specified foreign country” | 4411 | encoded | `o 29 r 1 a place is a specified foreign country`; `o 29 r 6 a place is a specified foreign country` | F-29-1 |
| O29 r2 | 4412-4414 | encoded | see the sub-rows (4 functions under this provision) |  |
| O29 r2(1) | 4413 | encoded | `o 29 r 2(1) the Court may order proceedings in a specified court in a specified foreign country` |  |
| O29 r2(2) | 4413 | encoded | `o 29 r 2(2) the application is made by summons and supported by an affidavit`; `o 29 r 2(2) the application is made by summons and supported by an affidavit (the duty arises)` |  |
| O29 r2(3) | 4414 | encoded | `o 29 r 2(3) the Court may give directions for a statement of the issue` |  |
| O29 r3 | 4415-4416 | encoded | `o 29 r 3 this Order does not prevent the Court ordering proceedings in another foreign country on its own motion` |  |
| O29 r4 | 4417-4425 | encoded | `o 29 r 4 the order states what it must state`; `o 29 r 4 the order states what it must state (the duty arises)` |  |
| O29 r4(a) | 4418-4419 | encoded | `o 29 r 4 the order states what it must state`; `o 29 r 4 the order states what it must state (the duty arises)` (covered with O 29 r 4) |  |
| O29 r4(b) | 4420-4421 | encoded | `o 29 r 4 the order states what it must state`; `o 29 r 4 the order states what it must state (the duty arises)` (covered with O 29 r 4) |  |
| O29 r4(c) | 4422-4423 | encoded | `o 29 r 4 the order states what it must state`; `o 29 r 4 the order states what it must state (the duty arises)` (covered with O 29 r 4) |  |
| O29 r4(d) | 4424-4425 | encoded | `o 29 r 4 the order states what it must state`; `o 29 r 4 the order states what it must state (the duty arises)` (covered with O 29 r 4) |  |
| O29 r5 | 4426-4434 | encoded | see the sub-rows (3 functions under this provision) |  |
| O29 r5(1) | 4427 | encoded | `o 29 r 5(1) proceedings on an issue of Singapore law may be commenced by originating application` |  |
| O29 r5(2) | 4427 | encoded | `o 29 r 5(2) the originating application or affidavit states what it must state`; `o 29 r 5(2) the originating application or affidavit states what it must state (the duty arises)` |  |
| O29 r5(2)(a) | 4427-4428 | encoded | `o 29 r 5(2) the originating application or affidavit states what it must state`; `o 29 r 5(2) the originating application or affidavit states what it must state (the duty arises)` (covered with O 29 r 5(2)) |  |
| O29 r5(2)(b) | 4429-4430 | encoded | `o 29 r 5(2) the originating application or affidavit states what it must state`; `o 29 r 5(2) the originating application or affidavit states what it must state (the duty arises)` (covered with O 29 r 5(2)) |  |
| O29 r5(2)(c) | 4431-4432 | encoded | `o 29 r 5(2) the originating application or affidavit states what it must state`; `o 29 r 5(2) the originating application or affidavit states what it must state (the duty arises)` (covered with O 29 r 5(2)) |  |
| O29 r5(2)(d) | 4433-4434 | encoded | `o 29 r 5(2) the originating application or affidavit states what it must state`; `o 29 r 5(2) the originating application or affidavit states what it must state (the duty arises)` (covered with O 29 r 5(2)) |  |
| O29 r6 | 4435-4441 | encoded | `o 29 r 6 a place is a specified foreign country` | F-29-1 |
| O29 r6(a) | 4436-4437 | encoded | `o 29 r 6 a place is a specified foreign country` (covered with O 29 r 6) | F-29-1 |
| O29 r6(b) | 4438-4439 | encoded | `o 29 r 6 a place is a specified foreign country` (covered with O 29 r 6) | F-29-1 |
| O29 r6(c) | 4440-4441 | encoded | `o 29 r 6 a place is a specified foreign country` (covered with O 29 r 6) | F-29-1 |
| O29 r7 | 4442-4448 | encoded | `o 29 r 7 a court is a specified court` | F-29-1 |
| O29 r7(a) | 4443-4444 | encoded | `o 29 r 7 a court is a specified court` (covered with O 29 r 7) | F-29-1 |
| O29 r7(b) | 4445-4446 | encoded | `o 29 r 7 a court is a specified court` (covered with O 29 r 7) | F-29-1 |
| O29 r7(c) | 4447-4448 | encoded | `o 29 r 7 a court is a specified court` (covered with O 29 r 7) | F-29-1 |
| O29A | 4449-4450 | inert-1 | (heading: not operative) |  |
| O29A r1 | 4451-4455 | encoded | `o 29A r 1 a defined term has its defined meaning`; `o 29A r 1 a court is the Court`; `o 29A r 1 a place is a foreign country`; `o 29A r 1 a court is a specified court`; `o 29A r 1 a place is a specified foreign country` |  |
| O29A r1 def “Court” | 4452 | encoded | `o 29A r 1 a court is the Court` |  |
| O29A r1 def “foreign country” | 4453 | encoded | `o 29A r 1 a place is a foreign country` |  |
| O29A r1 def “specified court” | 4454 | encoded | `o 29A r 1 a court is a specified court`; `o 29A r 5 a court is a specified court` | F-29-1 |
| O29A r1 def “specified foreign country” | 4455 | encoded | `o 29A r 1 a place is a specified foreign country`; `o 29A r 4 a place is a specified foreign country` | F-29-1 |
| O29A r2 | 4456-4463 | encoded | see the sub-rows (3 functions under this provision) |  |
| O29A r2(1) | 4457 | encoded | `o 29A r 2(1) the Court may transmit a request for an opinion to a specified court` |  |
| O29A r2(1)(a) | 4457-4458 | encoded | `o 29A r 2(1) the Court may transmit a request for an opinion to a specified court` (covered with O 29A r 2(1)) |  |
| O29A r2(1)(b) | 4459-4460 | encoded | `o 29A r 2(1) the Court may transmit a request for an opinion to a specified court` (covered with O 29A r 2(1)) |  |
| O29A r2(1)(c) | 4461-4462 | encoded | `o 29A r 2(1) the Court may transmit a request for an opinion to a specified court` (covered with O 29A r 2(1)) |  |
| O29A r2(2) | 4463 | encoded | `o 29A r 2(2) the application is made by summons`; `o 29A r 2(2) the application is made by summons (the duty arises)` |  |
| O29A r3 | 4464-4473 | encoded | see the sub-rows (3 functions under this provision) |  |
| O29A r3(1) | 4465 | encoded | `o 29A r 3(1) the initial request states what it must state`; `o 29A r 3(1) the initial request states what it must state (the duty arises)` |  |
| O29A r3(1)(a) | 4465-4466 | encoded | `o 29A r 3(1) the initial request states what it must state`; `o 29A r 3(1) the initial request states what it must state (the duty arises)` (covered with O 29A r 3(1)) |  |
| O29A r3(1)(b) | 4467-4468 | encoded | `o 29A r 3(1) the initial request states what it must state`; `o 29A r 3(1) the initial request states what it must state (the duty arises)` (covered with O 29A r 3(1)) |  |
| O29A r3(1)(c) | 4469-4470 | encoded | `o 29A r 3(1) the initial request states what it must state`; `o 29A r 3(1) the initial request states what it must state (the duty arises)` (covered with O 29A r 3(1)) |  |
| O29A r3(1)(d) | 4471-4472 | encoded | `o 29A r 3(1) the initial request states what it must state`; `o 29A r 3(1) the initial request states what it must state (the duty arises)` (covered with O 29A r 3(1)) |  |
| O29A r3(2) | 4473 | encoded | `o 29A r 3(2) a request may identify the proceedings or the parties` |  |
| O29A r4 | 4474-4475 | encoded | `o 29A r 4 a place is a specified foreign country` | F-29-1 |
| O29A r5 | 4476-4477 | encoded | `o 29A r 5 a court is a specified court` | F-29-1 |
| PART2 | 4478-4479 | inert-1 | (heading: not operative) |  |
| O30 | 4480-4481 | inert-1 | (heading: not operative) |  |
| O30 r1 | 4482-4484 | encoded | see the sub-rows (3 functions under this provision) |  |
| O30 r1(1) | 4483 | encoded | `o 30 r 1(1) this Order applies to the Reference` |  |
| O30 r1(2) | 4483 | encoded | `o 30 r 1(2) a reference is a Reference`; `o 30 r 1(2) a tribunal is the Tribunal` |  |
| O30 r1(2) def “Reference” | 4483 | encoded | `o 30 r 1(2) a reference is a Reference` |  |
| O30 r1(2) def “Tribunal” | 4484 | encoded | `o 30 r 1(2) a tribunal is the Tribunal` |  |
| O30 r2 | 4485-4487 | encoded | see the sub-rows (3 functions under this provision) |  |
| O30 r2(1) | 4486 | encoded | `o 30 r 2(1) the Reference is brought by filing it in Form 47` |  |
| O30 r2(2) | 4486 | encoded | `o 30 r 2(2) the Reference is made under the hand of the President of Singapore` |  |
| O30 r2(3) | 4487 | encoded | `o 30 r 2(3) the Registrar causes a copy of the Reference to be served on the Attorney-General` |  |
| O30 r3 | 4488-4489 | encoded | see the sub-rows (2 functions under this provision) |  |
| O30 r3(1) | 4489 | encoded | `o 30 r 3(1) the Reference states the questions in a form which can be answered yes or no` |  |
| O30 r3(2) | 4489 | encoded | `o 30 r 3(2) the Reference is divided into paragraphs and states what is necessary` |  |
| O30 r4 | 4490-4492 | encoded | see the sub-rows (5 functions under this provision) |  |
| O30 r4(1) | 4491 | encoded | `o 30 r 4(1) the Tribunal consists of the Chief Justice and the other Judges` |  |
| O30 r4(2) | 4491 | encoded | `o 30 r 4(2) the Tribunal consists of Judges appointed by the Chief Justice`; `o 30 r 4(2) the Tribunal consists of Judges appointed by the Chief Justice (the duty arises)` |  |
| O30 r4(3) | 4492 | encoded | `o 30 r 4(3) the Chief Justice is the President of the Tribunal`; `o 30 r 4(3) the presidency may be determined by the order of precedence` |  |
| O30 r5 | 4493-4494 | encoded | see the sub-rows (7 functions under this provision) |  |
| O30 r5(1) | 4494 | encoded | `o 30 r 5(1) the Tribunal may direct that a person interested be notified`; `o 30 r 5(1) a person notified is entitled to be heard` |  |
| O30 r5(2) | 4494 | encoded | `o 30 r 5(2) the person informs the Tribunal in writing of the intention to be heard`; `o 30 r 5(2) the person informs the Tribunal in writing of the intention to be heard (the duty arises)`; `o 30 r 5(2) the period for informing the Tribunal`; `o 30 r 5(2) the person informs the Tribunal in time`; `o 30 r 5(2) duty` | F-ALL-1 |
| O30 r6 | 4495-4496 | encoded | see the sub-rows (2 functions under this provision) |  |
| O30 r6(1) | 4496 | encoded | `o 30 r 6(1) the Attorney-General assists the Tribunal` |  |
| O30 r6(2) | 4496 | encoded | `o 30 r 6(2) the Presidency may be represented by counsel the Tribunal appoints` |  |
| O30 r7 | 4497-4498 | encoded | `o 30 r 7 the Tribunal may request counsel to argue the case` |  |
| O30 r8 | 4499-4502 | encoded | see the sub-rows (5 functions under this provision) |  |
| O30 r8(1) | 4500 | encoded | `o 30 r 8(1) the Reference is regarded as an appeal to the Court of Appeal` |  |
| O30 r8(2) | 4500 | encoded | `o 30 r 8(2) the Reference is treated as the record of appeal` |  |
| O30 r8(3) | 4501 | encoded | `o 30 r 8(3) the President of Singapore is treated as the appellant`; `o 30 r 8(3) a party is treated as a respondent` |  |
| O30 r8(4) | 4502 | encoded | `o 30 r 8(4) the steps required before filing the record of appeal are taken` |  |
| O30 r9 | 4503-4504 | encoded | `o 30 r 9 the procedure follows the procedure before the Court of Appeal`; `o 30 r 9 the Tribunal is bound by the strict rules of evidence` |  |
| O30 r10 | 4505-4506 | encoded | `o 30 r 10 the requirement to hold the proceeding in open court applies`; `o 30 r 10 the proceeding is held in open court`; `o 30 r 10 the proceeding is held in open court (the duty arises)` |  |
| O30 r11 | 4507-4508 | encoded | `o 30 r 11 the Registrar serves a notice to attend a hearing for directions` |  |
| O30 r12 | 4509-4515 | encoded | `o 30 r 12 the directions may include` |  |
| O30 r12(a) | 4510-4511 | encoded | `o 30 r 12 the directions may include` (covered with O 30 r 12) |  |
| O30 r12(b) | 4512-4513 | encoded | `o 30 r 12 the directions may include` (covered with O 30 r 12) |  |
| O30 r12(c) | 4514-4515 | encoded | `o 30 r 12 the directions may include` (covered with O 30 r 12) |  |
| O30 r13 | 4516-4517 | encoded | see the sub-rows (2 functions under this provision) |  |
| O30 r13(1) | 4517 | encoded | `o 30 r 13(1) the report is in the form of an answer to the questions` |  |
| O30 r13(2) | 4517 | encoded | `o 30 r 13(2) the Registrar delivers the report to the President of Singapore and the Attorney-General` |  |
| O30 r14 | 4518-4519 | encoded | `o 30 r 14 a party may be ordered to pay costs` |  |
| O30 r15 | 4520-4521 | encoded | `o 30 r 15 a fee is payable in respect of the proceedings` |  |
| O31 | 4522-4523 | inert-1 | (heading: not operative) |  |
| O31 r1 | 4524-4527 | encoded | see the sub-rows (7 functions under this provision) |  |
| O31 r1(1) | 4525 | encoded | `o 31 r 1(1) this Order applies despite Order 1, Rule 2` |  |
| O31 r1(2) | 4525 | encoded | `o 31 r 1(2) the Case states what it must state`; `o 31 r 1(2) the Case states what it must state (the duty arises)` |  |
| O31 r1(3) | 4526 | encoded | `o 31 r 1(3) the Registrar of the Supreme Court lays the Case before a Judge and serves a copy on the Attorney-General`; `o 31 r 1(3) the Registrar of the Supreme Court lays the Case before a Judge and serves a copy on the Attorney-General (the duty arises)` |  |
| O31 r1(4) | 4527 | encoded | `o 31 r 1(4) the Judge deals with the Case as if it were a case in the original jurisdiction`; `o 31 r 1(4) the Judge deals with the Case as if it were a case in the original jurisdiction (the duty arises)` |  |
| O31 r2 | 4528-4532 | encoded | see the sub-rows (8 functions under this provision) |  |
| O31 r2(1) | 4529 | encoded | `o 31 r 2(1) the Case is regarded as an application to the General Division` |  |
| O31 r2(2) | 4529 | encoded | `o 31 r 2(2) the Case is treated as the record of proceedings` |  |
| O31 r2(3) | 4530 | encoded | `o 31 r 2(3) the claimant or the prosecution is treated as the applicant`; `o 31 r 2(3) a party is treated as a respondent` |  |
| O31 r2(4) | 4531 | encoded | `o 31 r 2(4) the judgment of the General Division is in the form of an answer to the question`; `o 31 r 2(4) the judgment of the General Division is in the form of an answer to the question (the duty arises)` |  |
| O31 r2(5) | 4532 | encoded | `o 31 r 2(5) the Registrar of the Supreme Court serves notice of the hearing`; `o 31 r 2(5) the Registrar of the Supreme Court serves notice of the hearing (the duty arises)` |  |
| O31 r3 | 4533-4534 | encoded | `o 31 r 3 the Registrar of the Supreme Court delivers a copy of the judgment` |  |
| O31 r4 | 4535-4536 | encoded | see the sub-rows (4 functions under this provision) |  |
| O31 r4(1) | 4536 | encoded | `o 31 r 4(1) the State Court continues and disposes of the proceedings according to law`; `o 31 r 4(1) the State Court continues and disposes of the proceedings according to law (the duty arises)` |  |
| O31 r4(2) | 4536 | encoded | `o 31 r 4(2) the State Court determines all questions and makes the orders regarding costs`; `o 31 r 4(2) an order for costs incurred in the General Division may be made` |  |
| O32 | 4537-4538 | inert-1 | (heading: not operative) |  |
| O32 r1 | 4539-4541 | encoded | `o 32 r 1 an action is an administration action`; `o 32 r 1 a person is a personal representative` |  |
| O32 r1 def “administration action” | 4540 | encoded | `o 32 r 1 an action is an administration action` |  |
| O32 r1 def “personal representatives” | 4541 | encoded | `o 32 r 1 a person is a personal representative` | F-32-1 |
| O32 r2 | 4542-4558 | encoded | see the sub-rows (4 functions under this provision) |  |
| O32 r2(1) | 4543 | encoded | `o 32 r 2(1) an action may be brought for a question or relief which could be had in an administration action`; `o 32 r 2(1) a claim for administration or execution must be made in the action` |  |
| O32 r2(2) | 4543 | encoded | `o 32 r 2(2) an action may be brought for the determination of the question` |  |
| O32 r2(2)(a) | 4543-4544 | encoded | `o 32 r 2(2) an action may be brought for the determination of the question` (covered with O 32 r 2(2)) |  |
| O32 r2(2)(b) | 4545-4546 | encoded | `o 32 r 2(2) an action may be brought for the determination of the question` (covered with O 32 r 2(2)) |  |
| O32 r2(2)(c) | 4547-4548 | encoded | `o 32 r 2(2) an action may be brought for the determination of the question` (covered with O 32 r 2(2)) |  |
| O32 r2(3) | 4549 | encoded | `o 32 r 2(3) an action may be brought for the relief` |  |
| O32 r2(3)(a) | 4549-4550 | encoded | `o 32 r 2(3) an action may be brought for the relief` (covered with O 32 r 2(3)) |  |
| O32 r2(3)(b) | 4551-4552 | encoded | `o 32 r 2(3) an action may be brought for the relief` (covered with O 32 r 2(3)) |  |
| O32 r2(3)(c) | 4553-4554 | encoded | `o 32 r 2(3) an action may be brought for the relief` (covered with O 32 r 2(3)) |  |
| O32 r2(3)(d) | 4555-4556 | encoded | `o 32 r 2(3) an action may be brought for the relief` (covered with O 32 r 2(3)) |  |
| O32 r2(3)(e) | 4557-4558 | encoded | `o 32 r 2(3) an action may be brought for the relief` (covered with O 32 r 2(3)) |  |
| O32 r3 | 4559-4561 | encoded | see the sub-rows (8 functions under this provision) |  |
| O32 r3(1) | 4560 | encoded | `o 32 r 3(1) all the personal representatives are parties to the action`; `o 32 r 3(1) all the personal representatives are parties to the action (the duty arises)`; `o 32 r 3(1) a personal representative who does not consent is made a defendant`; `o 32 r 3(1) a personal representative who does not consent is made a defendant (the duty arises)` |  |
| O32 r3(2) | 4560 | encoded | `o 32 r 3(2) a person having a beneficial interest or claim must be a party`; `o 32 r 3(2) the claimant may make a person with a beneficial interest or claim a party` |  |
| O32 r3(3) | 4561 | encoded | `o 32 r 3(3) a party other than the executors or administrators is entitled to appear`; `o 32 r 3(3) the Court may direct or allow another party to appear` |  |
| O32 r4 | 4562-4563 | encoded | `o 32 r 4 the Court may grant relief for breach of trust even though the action began by originating application`; `o 32 r 4 the Court may order that the originating application be converted into an originating claim` |  |
| O32 r5 | 4564-4568 | encoded | see the sub-rows (3 functions under this provision) |  |
| O32 r5(1) | 4565 | encoded | `o 32 r 5(1) a judgment or order for administration or execution need be given or made` |  |
| O32 r5(2) | 4565 | encoded | see the sub-rows (2 functions under this provision) |  |
| O32 r5(2)(a) | 4565-4566 | encoded | `o 32 r 5(2)(a) the Court may stay the action and order the personal representatives to provide accounts` |  |
| O32 r5(2)(b) | 4567-4568 | encoded | `o 32 r 5(2)(b) the Court may give judgment or make an order for administration` |  |
| O32 r6 | 4569-4570 | encoded | `o 32 r 6 the personal representatives have the conduct of the sale` |  |
| O33 | 4571-4572 | inert-1 | (heading: not operative) |  |
| O33 r1 | 4573-4582 | encoded | see the sub-rows (10 functions under this provision) |  |
| O33 r1(1) | 4574 | encoded | `o 33 r 1(1) this Order applies to the cause or matter` |  |
| O33 r1(2) | 4574 | encoded | `o 33 r 1(2) an action is an action in rem`; `o 33 r 1(2) a caveat is a caveat against arrest`; `o 33 r 1(2) a caveat is a caveat against release and payment`; `o 33 r 1(2) a recording is electronic track data`; `o 33 r 1(2) an action is a limitation action`; and 3 more under the same provision label |  |
| O33 r1(2) def “action in rem” | 4574 | encoded | `o 33 r 1(2) an action is an action in rem` |  |
| O33 r1(2) def “caveat against arrest” | 4575 | encoded | `o 33 r 1(2) a caveat is a caveat against arrest` |  |
| O33 r1(2) def “caveat against release and payment” | 4576 | encoded | `o 33 r 1(2) a caveat is a caveat against release and payment` |  |
| O33 r1(2) def “electronic track data” | 4577 | encoded | `o 33 r 1(2) a recording is electronic track data` |  |
| O33 r1(2) def “limitation action” | 4578 | encoded | `o 33 r 1(2) an action is a limitation action` |  |
| O33 r1(2) def “record of caveats” | 4579 | encoded | `o 33 r 1(2) information is the record of caveats` |  |
| O33 r1(2) def “Sheriff’s account” | 4580 | encoded | `o 33 r 1(2) an account is the Sheriff's account` |  |
| O33 r1(2) def “ship” | 4581 | encoded | `o 33 r 1(2) a craft is a ship` |  |
| O33 r1(3) | 4582 | encoded | `o 33 r 1(3) a reference to payment into Court of proceeds of sale means payment into the Sheriff's account` |  |
| O33 r2 | 4583-4592 | encoded | see the sub-rows (22 functions under this provision) |  |
| O33 r2(1) | 4584 | encoded | `o 33 r 2(1) an action in rem is begun by originating claim in Form 48`; `o 33 r 2(1) an action in rem is begun by originating claim in Form 48 (the duty arises)` |  |
| O33 r2(2) | 4584 | encoded | `o 33 r 2(2) the originating claim in an Admiralty action in personam is in Form 8 with the words inserted`; `o 33 r 2(2) the originating claim in an Admiralty action in personam is in Form 8 with the words inserted (the duty arises)` |  |
| O33 r2(3) | 4585 | encoded | `o 33 r 2(3) Order 6 Rules 5(4) and (6) and 6(1), (2), (3), (4) and (7) apply to the action` |  |
| O33 r2(4) | 4586 | encoded | `o 33 r 2(4) the defendant served in Singapore files and serves the notice`; `o 33 r 2(4) the defendant served in Singapore files and serves the notice (the duty arises)`; `o 33 r 2(4) the period for the notice`; `o 33 r 2(4) the defendant served in Singapore files and serves the notice in time`; `o 33 r 2(4) duty` | F-ALL-1 |
| O33 r2(5) | 4587 | encoded | `o 33 r 2(5) the defendant served out of Singapore files and serves the notice`; `o 33 r 2(5) the defendant served out of Singapore files and serves the notice (the duty arises)`; `o 33 r 2(5) the period for the notice`; `o 33 r 2(5) the defendant served out of Singapore files and serves the notice in time`; `o 33 r 2(5) duty` | F-ALL-1 |
| O33 r2(6) | 4588 | encoded | `o 33 r 2(6) the notice is in Form 49`; `o 33 r 2(6) the notice is in Form 49 (the duty arises)` |  |
| O33 r2(7) | 4589 | encoded | `o 33 r 2(7) the filing and service of the notice is treated as a submission to jurisdiction or a waiver of any improper service` |  |
| O33 r2(8) | 4590 | encoded | `o 33 r 2(8) the claimant may apply for judgment in Form 50` |  |
| O33 r2(9) | 4591 | encoded | `o 33 r 2(9) the period of validity of the originating claim for service`; `o 33 r 2(9) the originating claim is valid for service on the date` | F-33-8, F-ALL-1 |
| O33 r2(10) | 4592 | encoded | `o 33 r 2(10) Order 6 Rule 6(5) and (6) and Order 16 Rule 2(6) and (7) apply to the originating claim` |  |
| O33 r3 | 4593-4610 | encoded | see the sub-rows (5 functions under this provision) |  |
| O33 r3(1) | 4594 | encoded | `o 33 r 3(1) this Rule applies to the action` |  |
| O33 r3(1)(a) | 4594-4595 | encoded | `o 33 r 3(1) this Rule applies to the action` (covered with O 33 r 3(1)) |  |
| O33 r3(1)(b) | 4596-4597 | encoded | `o 33 r 3(1) this Rule applies to the action` (covered with O 33 r 3(1)) |  |
| O33 r3(1)(c) | 4598-4599 | encoded | `o 33 r 3(1) this Rule applies to the action` (covered with O 33 r 3(1)) |  |
| O33 r3(2) | 4600 | encoded | `o 33 r 3(2) service out of Singapore is permissible` |  |
| O33 r3(2)(a) | 4600-4601 | encoded | `o 33 r 3(2) service out of Singapore is permissible` (covered with O 33 r 3(2)) |  |
| O33 r3(2)(b) | 4602-4603 | encoded | `o 33 r 3(2) service out of Singapore is permissible` (covered with O 33 r 3(2)) |  |
| O33 r3(2)(c) | 4604-4605 | encoded | `o 33 r 3(2) service out of Singapore is permissible` (covered with O 33 r 3(2)) |  |
| O33 r3(2)(d) | 4606-4607 | encoded | `o 33 r 3(2) service out of Singapore is permissible` (covered with O 33 r 3(2)) |  |
| O33 r3(3) | 4608 | encoded | `o 33 r 3(3) this Rule applies to the action` |  |
| O33 r3(4) | 4609 | encoded | `o 33 r 3(4) Order 8 other than Rule 4 applies to the service out of Singapore` |  |
| O33 r3(5) | 4610 | encoded | `o 33 r 3(5) a term has the meaning given by the High Court (Admiralty Jurisdiction) Act` |  |
| O33 r4 | 4611-4632 | encoded | `o 33 r 4 a warrant of arrest is issued under this Rule` |  |
| O33 r4(1) | 4612 | encoded | `o 33 r 4(1) the claimant or defendant may apply for a warrant of arrest` |  |
| O33 r4(2) | 4612 | encoded | `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats`; `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats (the duty arises)` |  |
| O33 r4(2)(a) | 4612-4613 | encoded | `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats`; `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats (the duty arises)` (covered with O 33 r 4(2)) |  |
| O33 r4(2)(b) | 4614-4615 | encoded | `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats`; `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats (the duty arises)` (covered with O 33 r 4(2)) |  |
| O33 r4(3) | 4616 | encoded | `o 33 r 4(3) the warrant of arrest cannot yet be issued for want of the affidavit`; `o 33 r 4(3) the Court may allow the warrant to issue although the affidavit lacks particulars`; `o 33 r 4(3) a warrant of arrest may be issued` |  |
| O33 r4(4) | 4617 | encoded | `o 33 r 4(4) the warrant of arrest cannot yet be issued for want of notice to the consul`; `o 33 r 4(4) a warrant of arrest may be issued against the foreign ship` |  |
| O33 r4(5) | 4618 | encoded | `o 33 r 4(5) a warrant of arrest is issued` |  |
| O33 r4(6) | 4619 | encoded | `o 33 r 4(6) the affidavit states what paragraph (6) requires`; `o 33 r 4(6) the affidavit states what paragraph (6) requires (the duty arises)` |  |
| O33 r4(6)(a) | 4619-4620 | encoded | `o 33 r 4(6) the affidavit states what paragraph (6) requires`; `o 33 r 4(6) the affidavit states what paragraph (6) requires (the duty arises)` (covered with O 33 r 4(6)) |  |
| O33 r4(6)(b) | 4621-4622 | encoded | `o 33 r 4(6) the affidavit states what paragraph (6) requires`; `o 33 r 4(6) the affidavit states what paragraph (6) requires (the duty arises)` (covered with O 33 r 4(6)) |  |
| O33 r4(6)(c) | 4623-4624 | encoded | `o 33 r 4(6) the affidavit states what paragraph (6) requires`; `o 33 r 4(6) the affidavit states what paragraph (6) requires (the duty arises)` (covered with O 33 r 4(6)) |  |
| O33 r4(7) | 4625 | encoded | `o 33 r 4(7) the affidavit states what paragraph (7) requires`; `o 33 r 4(7) the affidavit states what paragraph (7) requires (the duty arises)` | F-33-6 |
| O33 r4(7)(a) | 4625-4626 | encoded | `o 33 r 4(7) the affidavit states what paragraph (7) requires`; `o 33 r 4(7) the affidavit states what paragraph (7) requires (the duty arises)` (covered with O 33 r 4(7)) | F-33-6 |
| O33 r4(7)(b) | 4627-4628 | encoded | `o 33 r 4(7) the affidavit states what paragraph (7) requires`; `o 33 r 4(7) the affidavit states what paragraph (7) requires (the duty arises)` (covered with O 33 r 4(7)) | F-33-6 |
| O33 r4(7)(c) | 4629-4630 | encoded | `o 33 r 4(7) the affidavit states what paragraph (7) requires`; `o 33 r 4(7) the affidavit states what paragraph (7) requires (the duty arises)` (covered with O 33 r 4(7)) | F-33-6 |
| O33 r4(7)(d) | 4631-4632 | encoded | `o 33 r 4(7) the affidavit states what paragraph (7) requires`; `o 33 r 4(7) the affidavit states what paragraph (7) requires (the duty arises)` (covered with O 33 r 4(7)) | F-33-6 |
| O33 r5 | 4633-4639 | encoded | `o 33 r 5 a caveat against arrest is issued under this Rule` |  |
| O33 r5(1) | 4634 | encoded | `o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats`; `o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats (the duty arises)` |  |
| O33 r5(1)(a) | 4634-4635 | encoded | `o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats`; `o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats (the duty arises)` (covered with O 33 r 5(1)) |  |
| O33 r5(1)(b) | 4636-4638 | encoded | `o 33 r 5(1)(b) the period for giving bail or paying into Court`; `o 33 r 5(1)(b) bail is given or the amount is paid into Court in time`; `o 33 r 5(1)(b) duty` | F-ALL-1 |
| O33 r5(2) | 4639 | encoded | `o 33 r 5(2) a caveat against arrest in force prevents the issue of a warrant to arrest the property` |  |
| O33 r6 | 4640-4641 | encoded | `o 33 r 6 the Court may discharge the warrant`; `o 33 r 6 the Court may order the party procuring the arrest to pay damages` | F-33-2 |
| O33 r7 | 4642-4666 | encoded | see the sub-rows (33 functions under this provision) |  |
| O33 r7(1) | 4643 | encoded | `o 33 r 7(1) the originating claim is served on the property against which the action is brought`; `o 33 r 7(1) the originating claim is served on the property against which the action is brought (the duty arises)` |  |
| O33 r7(1)(a) | 4643-4644 | encoded | `o 33 r 7(1)(a) where the property is freight the originating claim is served on the cargo or the ship`; `o 33 r 7(1)(a) where the property is freight the originating claim is served on the cargo or the ship (the duty arises)` |  |
| O33 r7(1)(b) | 4645-4646 | encoded | `o 33 r 7(1)(b) where the property has been sold by the Sheriff a sealed copy is filed and served on the Sheriff`; `o 33 r 7(1)(b) where the property has been sold by the Sheriff a sealed copy is filed and served on the Sheriff (the duty arises)`; `o 33 r 7(1)(b) the originating claim may be served on the property sold by the Sheriff`; `o 33 r 7(1)(b) the originating claim is deemed served on the day the copy was filed` |  |
| O33 r7(2) | 4647 | encoded | `o 33 r 7(2) the originating claim must be served as mentioned in paragraph (1)` |  |
| O33 r7(3) | 4648 | encoded | `o 33 r 7(3) the day the originating claim is deemed duly served` | F-33-3 |
| O33 r7(3)(a) | 4648-4649 | encoded | `o 33 r 7(3)(a) the originating claim is deemed duly served on acceptance by the defendant's solicitor` | F-33-3 |
| O33 r7(3)(b) | 4650-4651 | encoded | `o 33 r 7(3)(b) the originating claim is deemed duly served when the defendant files the notice` | F-33-3 |
| O33 r7(4) | 4652 | encoded | `o 33 r 7(4) service on the property may be effected by the Sheriff or a notified solicitor or clerk` |  |
| O33 r7(5) | 4653 | encoded | `o 33 r 7(5) the Registrar may allow service to be effected by any other named person`; `o 33 r 7(5) the Registrar causes a memorandum to be marked on the originating claim`; `o 33 r 7(5) the Registrar causes a memorandum to be marked on the originating claim (the duty arises)` |  |
| O33 r7(6) | 4654 | encoded | `o 33 r 7(6) the claimant leaves a copy at the Registry and files a request in Form 53`; `o 33 r 7(6) the claimant leaves a copy at the Registry and files a request in Form 53 (the duty arises)`; `o 33 r 7(6) the Sheriff serves the originating claim on the property described in the request`; `o 33 r 7(6) the Sheriff serves the originating claim on the property described in the request (the duty arises)` |  |
| O33 r7(7) | 4655 | encoded | `o 33 r 7(7) the expenses of service are paid to the Sheriff on demand`; `o 33 r 7(7) the expenses of service are paid to the Sheriff on demand (the duty arises)` |  |
| O33 r7(8) | 4656 | encoded | `o 33 r 7(8) the person effecting service endorses the particulars on the originating claim`; `o 33 r 7(8) the person effecting service endorses the particulars on the originating claim (the duty arises)`; `o 33 r 7(8) the endorsement is evidence of the facts stated in it` |  |
| O33 r7(9) | 4657 | encoded | `o 33 r 7(9) the Sheriff gives the claimant written notice of the fact and manner of service`; `o 33 r 7(9) the Sheriff gives the claimant written notice of the fact and manner of service (the duty arises)` |  |
| O33 r7(10) | 4658 | encoded | `o 33 r 7(10) the claimant serves the originating claim forthwith on the person who entered the caveat`; `o 33 r 7(10) the claimant serves the originating claim forthwith on the person who entered the caveat (the duty arises)` | F-33-9 |
| O33 r7(11) | 4659 | encoded | `o 33 r 7(11) the originating claim may be amended once without permission to delete defendant vessels`; `o 33 r 7(11) the amended originating claim is served as required`; `o 33 r 7(11) the amended originating claim is served as required (the duty arises)` |  |
| O33 r7(12) | 4660 | encoded | `o 33 r 7(12) permission of the Court is required for the amendment` |  |
| O33 r7(12)(a) | 4660-4661 | encoded | `o 33 r 7(12) permission of the Court is required for the amendment` (covered with O 33 r 7(12)) |  |
| O33 r7(12)(b) | 4662-4663 | encoded | `o 33 r 7(12) permission of the Court is required for the amendment` (covered with O 33 r 7(12)) |  |
| O33 r7(12)(c) | 4664-4666 | encoded | `o 33 r 7(12) permission of the Court is required for the amendment` (covered with O 33 r 7(12)) |  |
| O33 r8 | 4667-4668 | encoded | `o 33 r 8 the solicitor is liable to committal` |  |
| O33 r9 | 4669-4679 | encoded | see the sub-rows (15 functions under this provision) |  |
| O33 r9(1) | 4670 | encoded | `o 33 r 9(1) the period of validity of the warrant of arrest`; `o 33 r 9(1) the warrant of arrest is valid on the date` | F-33-8, F-ALL-1 |
| O33 r9(2) | 4670 | encoded | `o 33 r 9(2) the warrant may be executed by the Sheriff or a notified solicitor or clerk` |  |
| O33 r9(3) | 4671 | encoded | `o 33 r 9(3) the Registrar may allow the warrant to be executed by any other named person`; `o 33 r 9(3) the Registrar causes a memorandum to be marked on the warrant`; `o 33 r 9(3) the Registrar causes a memorandum to be marked on the warrant (the duty arises)` |  |
| O33 r9(4) | 4672 | encoded | `o 33 r 9(4) the warrant of arrest cannot yet be executed by the Sheriff for want of the undertaking` |  |
| O33 r9(5) | 4673 | encoded | `o 33 r 9(5) the warrant of arrest may be executed` |  |
| O33 r9(6) | 4674 | encoded | `o 33 r 9(6) a warrant issued against freight may be executed by serving it on the cargo or the ship or both` |  |
| O33 r9(7) | 4675 | encoded | `o 33 r 9(7) the warrant of arrest is served on the property against which it is issued`; `o 33 r 9(7) the warrant of arrest is served on the property against which it is issued (the duty arises)` |  |
| O33 r9(8) | 4676 | encoded | `o 33 r 9(8) the report of the arrest is made by the person required`; `o 33 r 9(8) the report of the arrest is made by the person required (the duty arises)`; `o 33 r 9(8) the period for the report of the arrest`; `o 33 r 9(8) the report of the arrest is made in time` | F-ALL-1 |
| O33 r9(8)(a) | 4676-4677 | encoded | `o 33 r 9(8) the report of the arrest is made by the person required`; `o 33 r 9(8) the report of the arrest is made by the person required (the duty arises)`; `o 33 r 9(8) the period for the report of the arrest`; `o 33 r 9(8) the report of the arrest is made in time` (covered with O 33 r 9(8)) | F-ALL-1 |
| O33 r9(8)(b) | 4678-4679 | encoded | `o 33 r 9(8) the report of the arrest is made by the person required`; `o 33 r 9(8) the report of the arrest is made by the person required (the duty arises)`; `o 33 r 9(8) the period for the report of the arrest`; `o 33 r 9(8) the report of the arrest is made in time` (covered with O 33 r 9(8)) | F-ALL-1 |
| O33 r10 | 4680-4688 | encoded | see the sub-rows (4 functions under this provision) |  |
| O33 r10(1) | 4681 | encoded | `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy`; `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy (the duty arises)` |  |
| O33 r10(1)(a) | 4681-4682 | encoded | `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy`; `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy (the duty arises)` (covered with O 33 r 10(1)) |  |
| O33 r10(1)(b) | 4683-4684 | encoded | `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy`; `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy (the duty arises)` (covered with O 33 r 10(1)) |  |
| O33 r10(2) | 4685 | encoded | `o 33 r 10(2) service on landed or transhipped cargo is effected as required`; `o 33 r 10(2) service on landed or transhipped cargo is effected as required (the duty arises)` |  |
| O33 r10(2)(a) | 4685-4686 | encoded | `o 33 r 10(2) service on landed or transhipped cargo is effected as required`; `o 33 r 10(2) service on landed or transhipped cargo is effected as required (the duty arises)` (covered with O 33 r 10(2)) |  |
| O33 r10(2)(b) | 4687-4688 | encoded | `o 33 r 10(2) service on landed or transhipped cargo is effected as required`; `o 33 r 10(2) service on landed or transhipped cargo is effected as required (the duty arises)` (covered with O 33 r 10(2)) |  |
| O33 r11 | 4689-4733 | encoded | see the sub-rows (12 functions under this provision) |  |
| O33 r11(1) | 4690 | encoded | `o 33 r 11(1) service may be effected on the agent of the ship during the relevant period` | F-33-1 |
| O33 r11(1)(a) | 4690-4691 | encoded | `o 33 r 11(1) service may be effected on the agent of the ship during the relevant period` (covered with O 33 r 11(1)) | F-33-1 |
| O33 r11(1)(b) | 4692-4693 | encoded | `o 33 r 11(1) service may be effected on the agent of the ship during the relevant period` (covered with O 33 r 11(1)) | F-33-1 |
| O33 r11(1)(b)(i) | 4693-4694 | encoded | `o 33 r 11(1) service may be effected on the agent of the ship during the relevant period` (covered with O 33 r 11(1)) | F-33-1 |
| O33 r11(1)(b)(ii) | 4695-4696 | encoded | `o 33 r 11(1) service may be effected on the agent of the ship during the relevant period` (covered with O 33 r 11(1)) | F-33-1 |
| O33 r11(2) | 4697 | encoded | see the sub-rows (2 functions under this provision) |  |
| O33 r11(2)(a) | 4697-4698 | encoded | `o 33 r 11(2)(a) the warrant or originating claim is deemed served on the property` |  |
| O33 r11(2)(b) | 4699-4700 | encoded | `o 33 r 11(2)(b) the time of service` |  |
| O33 r11(2)(b)(i) | 4700-4701 | encoded | `o 33 r 11(2)(b) the time of service` (covered with O 33 r 11(2)(b)) |  |
| O33 r11(2)(b)(ii) | 4702-4703 | encoded | `o 33 r 11(2)(b) the time of service` (covered with O 33 r 11(2)(b)) |  |
| O33 r11(3) | 4704 | encoded | `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search`; `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search (the duty arises)` |  |
| O33 r11(3)(a) | 4704-4705 | encoded | `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search`; `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search (the duty arises)` (covered with O 33 r 11(3)) |  |
| O33 r11(3)(a)(i) | 4705-4706 | encoded | `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search`; `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search (the duty arises)` (covered with O 33 r 11(3)) |  |
| O33 r11(3)(a)(ii) | 4707-4708 | encoded | `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search`; `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search (the duty arises)` (covered with O 33 r 11(3)) |  |
| O33 r11(3)(b) | 4709-4710 | encoded | `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search`; `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search (the duty arises)` (covered with O 33 r 11(3)) |  |
| O33 r11(4) | 4711 | encoded | `o 33 r 11(4) Order 6 Rule 6(5) and (6) applies to the originating claim`; `o 33 r 11(4) the claimant is entitled to enter final or interlocutory judgment in default` |  |
| O33 r11(4)(a) | 4711-4712 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` | F-ALL-1 |
| O33 r11(4)(a)(i) | 4712-4713 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(i)(A) | 4713-4714 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(i)(B) | 4715-4716 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(i)(C) | 4717-4718 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(i)(D) | 4719-4720 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(ii) | 4721-4722 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(ii)(A) | 4722-4723 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(ii)(B) | 4724-4725 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(a)(iii) | 4726-4727 | encoded | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service`; `o 33 r 11(4)(a) the claimant files the memorandum of service in time` (covered with O 33 r 11(4)(a)) | F-ALL-1 |
| O33 r11(4)(b) | 4728-4729 | encoded | `o 33 r 11(4) Order 6 Rule 6(5) and (6) applies to the originating claim`; `o 33 r 11(4) the claimant is entitled to enter final or interlocutory judgment in default` (covered with O 33 r 11(4)) |  |
| O33 r11(5) | 4730 | encoded | `o 33 r 11(5) it is the relevant period`; `o 33 r 11(5) it is the relevant period by (a) or (b)` |  |
| O33 r11(5) def “relevant period” | 4730 | encoded | `o 33 r 11(5) it is the relevant period`; `o 33 r 11(5) it is the relevant period by (a) or (b)` |  |
| O33 r11(5)(a) | 4730-4731 | encoded | `o 33 r 11(5) it is the relevant period`; `o 33 r 11(5) it is the relevant period by (a) or (b)` (covered with O 33 r 11(5)) |  |
| O33 r11(5)(b) | 4732-4733 | encoded | `o 33 r 11(5) it is the relevant period`; `o 33 r 11(5) it is the relevant period by (a) or (b)` (covered with O 33 r 11(5)) |  |
| O33 r12 | 4734-4744 | encoded | see the sub-rows (9 functions under this provision) |  |
| O33 r12(1) | 4735 | encoded | `o 33 r 12(1) the Sheriff may apply to the Court for directions`; `o 33 r 12(1) the Sheriff gives notice of the application to the persons referred to in paragraph (2)`; `o 33 r 12(1) the Sheriff gives notice of the application to the persons referred to in paragraph (2) (the duty arises)` |  |
| O33 r12(2) | 4735 | encoded | `o 33 r 12(2) the Sheriff must send the person a copy of the order`; `o 33 r 12(2) the Sheriff must send the person a copy of the order (the duty arises)` |  |
| O33 r12(2)(a) | 4735-4736 | encoded | `o 33 r 12(2) the Sheriff must send the person a copy of the order`; `o 33 r 12(2) the Sheriff must send the person a copy of the order (the duty arises)` (covered with O 33 r 12(2)) |  |
| O33 r12(2)(b) | 4737-4738 | encoded | `o 33 r 12(2) the Sheriff must send the person a copy of the order`; `o 33 r 12(2) the Sheriff must send the person a copy of the order (the duty arises)` (covered with O 33 r 12(2)) |  |
| O33 r12(2)(c) | 4739-4740 | encoded | `o 33 r 12(2) the Sheriff must send the person a copy of the order`; `o 33 r 12(2) the Sheriff must send the person a copy of the order (the duty arises)` (covered with O 33 r 12(2)) |  |
| O33 r12(2)(d) | 4741-4742 | encoded | `o 33 r 12(2) the Sheriff must send the person a copy of the order`; `o 33 r 12(2) the Sheriff must send the person a copy of the order (the duty arises)` (covered with O 33 r 12(2)) |  |
| O33 r12(3) | 4743 | encoded | `o 33 r 12(3) the summons and copies of affidavits are served on the Sheriff and the persons referred to in paragraph (2)`; `o 33 r 12(3) the summons and copies of affidavits are served on the Sheriff and the persons referred to in paragraph (2) (the duty arises)` |  |
| O33 r12(4) | 4744 | encoded | `o 33 r 12(4) the Sheriff sends a copy of the order to all the parties to every action against the property`; `o 33 r 12(4) the Sheriff sends a copy of the order to all the parties to every action against the property (the duty arises)` |  |
| O33 r13 | 4745-4759 | encoded | `o 33 r 13 an instrument of release is issued under this Rule` |  |
| O33 r13(1) | 4746 | encoded | `o 33 r 13(1) the property is released only under an instrument of release in Form 54`; `o 33 r 13(1) the property is released only under an instrument of release in Form 54 (the duty arises)` |  |
| O33 r13(2) | 4746 | encoded | `o 33 r 13(2) a release may be issued` |  |
| O33 r13(2)(a) | 4746-4747 | encoded | `o 33 r 13(2) a release may be issued` (covered with O 33 r 13(2)) |  |
| O33 r13(2)(b) | 4748-4749 | encoded | `o 33 r 13(2) a release may be issued` (covered with O 33 r 13(2)) |  |
| O33 r13(3) | 4750 | encoded | `o 33 r 13(3) a release may be issued on the application` | F-33-4 |
| O33 r13(4) | 4751 | encoded | `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued`; `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued (the duty arises)` |  |
| O33 r13(4)(a) | 4751-4752 | encoded | `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued`; `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued (the duty arises)` (covered with O 33 r 13(4)) |  |
| O33 r13(4)(b) | 4753-4754 | encoded | `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued`; `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued (the duty arises)` (covered with O 33 r 13(4)) |  |
| O33 r13(5) | 4755 | encoded | `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released`; `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released (the duty arises)` |  |
| O33 r13(5)(a) | 4755-4756 | encoded | `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released`; `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released (the duty arises)` (covered with O 33 r 13(5)) |  |
| O33 r13(5)(b) | 4757-4758 | encoded | `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released`; `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released (the duty arises)` (covered with O 33 r 13(5)) |  |
| O33 r13(6) | 4759 | encoded | `o 33 r 13(6) the Court may vary or revoke the Sheriff's directions` |  |
| O33 r14 | 4760-4761 | encoded | see the sub-rows (3 functions under this provision) |  |
| O33 r14(1) | 4761 | encoded | `o 33 r 14(1) the caveat against release and payment is filed in Form 55 and entered in the record of caveats`; `o 33 r 14(1) the caveat against release and payment is filed in Form 55 and entered in the record of caveats (the duty arises)` |  |
| O33 r14(2) | 4761 | encoded | `o 33 r 14(2) the Court may order the person who procured the caveat to pay damages` | F-33-2 |
| O33 r15 | 4762-4763 | encoded | see the sub-rows (5 functions under this provision) |  |
| O33 r15(1) | 4763 | encoded | `o 33 r 15(1) the period of validity of the caveat`; `o 33 r 15(1) the caveat is valid on the date`; `o 33 r 15(1) the person at whose instance a caveat was entered may withdraw it` | F-33-8, F-ALL-1 |
| O33 r15(2) | 4763 | encoded | `o 33 r 15(2) the period of validity of a caveat may be extended`; `o 33 r 15(2) the bar on extension prevents the entry of successive caveats` |  |
| O33 r16 | 4764-4767 | encoded | see the sub-rows (11 functions under this provision) |  |
| O33 r16(1) | 4765 | encoded | `o 33 r 16(1) bail is given by bond in Form 57 entered into before a commissioner for oaths or the Registrar`; `o 33 r 16(1) bail is given by bond in Form 57 entered into before a commissioner for oaths or the Registrar (the duty arises)` |  |
| O33 r16(2) | 4765 | encoded | `o 33 r 16(2) the surety makes an affidavit that the surety is able to pay`; `o 33 r 16(2) the surety makes an affidavit that the surety is able to pay (the duty arises)` |  |
| O33 r16(3) | 4766 | encoded | `o 33 r 16(3) an affidavit is to be made on behalf of the corporation`; `o 33 r 16(3) the affidavit required of a corporation is made by an officer`; `o 33 r 16(3) the affidavit required of a corporation is made by an officer (the duty arises)` |  |
| O33 r16(4) | 4767 | encoded | `o 33 r 16(4) the party giving bail serves a notice of bail and files the bond, the affidavits and the proof of service`; `o 33 r 16(4) the party giving bail serves a notice of bail and files the bond, the affidavits and the proof of service (the duty arises)`; `o 33 r 16(4) the bond may be filed at the moment`; `o 33 r 16(4) the earliest moment the bond may be filed without consent` | F-33-7 |
| O33 r17 | 4768-4771 | encoded | see the sub-rows (7 functions under this provision) |  |
| O33 r17(1) | 4769 | encoded | `o 33 r 17(1) a person with an interest may intervene with the permission of the Court` |  |
| O33 r17(2) | 4769 | encoded | `o 33 r 17(2) the application for permission to intervene is made by summons without notice with an affidavit`; `o 33 r 17(2) the application for permission to intervene is made by summons without notice with an affidavit (the duty arises)` |  |
| O33 r17(3) | 4770 | encoded | `o 33 r 17(3) the intervener files and serves a notice of intention to contest or not contest`; `o 33 r 17(3) the intervener files and serves a notice of intention to contest or not contest (the duty arises)`; `o 33 r 17(3) Rule 2(3) to (6) applies to the intervener's notice with the necessary modifications` |  |
| O33 r17(4) | 4771 | encoded | `o 33 r 17(4) the Court may order the intervener to serve a pleading` |  |
| O33 r18 | 4772-4828 | encoded | see the sub-rows (32 functions under this provision) |  |
| O33 r18(1) | 4773 | encoded | `o 33 r 18(1) the provisions of this Rule apply to the action` |  |
| O33 r18(2) | 4773 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label | F-ALL-1 |
| O33 r18(2)Part One | 4773 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)` |  |
| O33 r18(2)(a) | 4774-4775 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(b) | 4776-4777 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(c) | 4778-4779 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(d) | 4780-4781 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(e) | 4782-4783 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(f) | 4784-4785 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(g) | 4786-4787 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(h) | 4788-4789 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(i) | 4790-4791 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(j) | 4792-4793 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(k) | 4794-4795 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(l) | 4796-4797 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(m) | 4798-4799 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(n) | 4800-4801 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(o) | 4802-4803 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(p) | 4804-4805 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(q) | 4806-4807 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)Part Two | 4808 | encoded | `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)` |  |
| O33 r18(2)(r) | 4809-4810 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(s) | 4811-4812 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(t) | 4813-4814 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(2)(u) | 4815-4816 | encoded | `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)`; `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)`; `o 33 r 18(2) the claimant files a preliminary act`; `o 33 r 18(2) the claimant files a preliminary act (the duty arises)`; `o 33 r 18(2) the period for the claimant's preliminary act`; and 5 more under the same provision label (covered with O 33 r 18(2)) | F-ALL-1 |
| O33 r18(3) | 4817 | encoded | `o 33 r 18(3) Part Two of the preliminary act is deemed to be the pleading of the person filing it`; `o 33 r 18(3) the provisions of these Rules relating to pleadings apply to Part Two` |  |
| O33 r18(4) | 4818 | encoded | `o 33 r 18(4) the Court may order that Part Two need not be filed` |  |
| O33 r18(5) | 4819 | encoded | `o 33 r 18(5) the preliminary act is sealed by the Registrar`; `o 33 r 18(5) the preliminary act is sealed by the Registrar (the duty arises)`; `o 33 r 18(5) a preliminary act may be inspected` |  |
| O33 r18(6) | 4820 | encoded | `o 33 r 18(6) the claimant serves notice of filing the claimant's preliminary act`; `o 33 r 18(6) the claimant serves notice of filing the claimant's preliminary act (the duty arises)`; `o 33 r 18(6) the period for the notice of filing`; `o 33 r 18(6) the claimant serves the notice of filing in time` | F-ALL-1 |
| O33 r18(7) | 4821 | encoded | `o 33 r 18(7) the defendant serves notice that the defendant has filed a preliminary act`; `o 33 r 18(7) the defendant serves notice that the defendant has filed a preliminary act (the duty arises)` |  |
| O33 r18(8) | 4822 | encoded | `o 33 r 18(8) a party may inspect and bespeak a copy of another party's preliminary act` |  |
| O33 r18(9) | 4823 | encoded | `o 33 r 18(9) each party serves a copy of the party's preliminary act on every other party`; `o 33 r 18(9) each party serves a copy of the party's preliminary act on every other party (the duty arises)`; `o 33 r 18(9) the period for serving the copy`; `o 33 r 18(9) the party serves the copy in time`; `o 33 r 18(9) duty` | F-ALL-1 |
| O33 r18(10) | 4824 | encoded | `o 33 r 18(10) a party may apply for an order for particulars of damages and assessment` |  |
| O33 r18(10)(a) | 4824-4825 | encoded | `o 33 r 18(10) a party may apply for an order for particulars of damages and assessment` (covered with O 33 r 18(10)) |  |
| O33 r18(10)(b) | 4826-4827 | encoded | `o 33 r 18(10) a party may apply for an order for particulars of damages and assessment` (covered with O 33 r 18(10)) |  |
| O33 r18(11) | 4828 | encoded | `o 33 r 18(11) the claim is treated as referred for assessment`; `o 33 r 18(11) Rules 41 and 42 apply to the claim referred for assessment` |  |
| O33 r19 | 4829-4835 | encoded | see the sub-rows (13 functions under this provision) |  |
| O33 r19(1) | 4830 | encoded | `o 33 r 19(1) a defendant who has filed a preliminary act may apply for the action to be dismissed`; `o 33 r 19(1) the Court may dismiss the action or make such other order` |  |
| O33 r19(2) | 4830 | encoded | `o 33 r 19(2) the claimant may enter judgment against a defendant in default in an action in personam` |  |
| O33 r19(3) | 4831 | encoded | `o 33 r 19(3) the claimant may apply by summons for judgment against a defendant in default in an action in rem`; `o 33 r 19(3) the claimant must file or serve a statement of claim or an affidavit before the hearing of the summons` |  |
| O33 r19(4) | 4832 | encoded | `o 33 r 19(4) the Court may make such order as it thinks just on the hearing of the summons`; `o 33 r 19(4) the Court orders the claimant's preliminary act to be opened and requires the claimant to satisfy the Court`; `o 33 r 19(4) the Court orders the claimant's preliminary act to be opened and requires the claimant to satisfy the Court (the duty arises)`; `o 33 r 19(4) the claimant's evidence may be given by affidavit` |  |
| O33 r19(5) | 4833 | encoded | `o 33 r 19(5) the Court may give judgment for the claim with or without a reference to the Registrar`; `o 33 r 19(5) the Court may order the property to be appraised and sold and the proceeds paid into Court` |  |
| O33 r19(6) | 4834 | encoded | `o 33 r 19(6) the Court may set aside a judgment entered in pursuance of this Rule` |  |
| O33 r19(7) | 4835 | encoded | `o 33 r 19(7) a period is the prescribed period` |  |
| O33 r20 | 4836-4841 | encoded | see the sub-rows (12 functions under this provision) |  |
| O33 r20(1) | 4837 | encoded | `o 33 r 20(1) the claimant may serve a reply or a defence to counterclaim on the defendant` |  |
| O33 r20(2) | 4837 | encoded | `o 33 r 20(2) the party gives production of electronic track data`; `o 33 r 20(2) the party gives production of electronic track data (the duty arises)` | F-ALL-1 |
| O33 r20(2)(a) | 4837-4838 | encoded | `o 33 r 20(2)(a) the period after the disposal of the application`; `o 33 r 20(2)(a) the party gives production in time after the disposal of the jurisdiction application` | F-ALL-1 |
| O33 r20(2)(b) | 4839-4840 | encoded | `o 33 r 20(2)(b) the period after the notice`; `o 33 r 20(2)(b) the party gives production in time after the notice of intention to contest or not contest` | F-ALL-1 |
| O33 r20(3) | 4841 | encoded | `o 33 r 20(3) the party allows another party to inspect and copy the electronic track data`; `o 33 r 20(3) the party allows another party to inspect and copy the electronic track data (the duty arises)`; `o 33 r 20(3) the period for allowing inspection`; `o 33 r 20(3) the party allows the inspection in time`; `o 33 r 20(3) duty` | F-ALL-1 |
| O33 r21 | 4842-4871 | encoded | see the sub-rows (25 functions under this provision) |  |
| O33 r21(1) | 4843 | encoded | `o 33 r 21(1) the claimant may apply for judgment by default against the party who gave a caveat undertaking` |  |
| O33 r21(1)(a) | 4843-4844 | encoded | `o 33 r 21(1) the claimant may apply for judgment by default against the party who gave a caveat undertaking` (covered with O 33 r 21(1)) |  |
| O33 r21(1)(b) | 4845-4847 | encoded | `o 33 r 21(1)(b) the period for fulfilling the undertaking`; `o 33 r 21(1)(b) the party fulfils the undertaking in time` | F-ALL-1 |
| O33 r21(2) | 4848 | encoded | `o 33 r 21(2) judgment given under paragraph (1) may be enforced by arrest and committal` |  |
| O33 r21(3) | 4849 | encoded | `o 33 r 21(3) the claimant may apply to the Court for judgment by default` |  |
| O33 r21(4) | 4850 | encoded | `o 33 r 21(4) an affidavit proving due service of the originating claim must be filed under paragraph (3)`; `o 33 r 21(4) the required exhibit is exhibited in the affidavit verifying the facts`; `o 33 r 21(4) the required exhibit is exhibited in the affidavit verifying the facts (the duty arises)` |  |
| O33 r21(5) | 4851 | encoded | `o 33 r 21(5) the claimant may apply to the Court for judgment by default against a defendant who served no defence` |  |
| O33 r21(5)(a) | 4851-4852 | encoded | `o 33 r 21(5) the claimant may apply to the Court for judgment by default against a defendant who served no defence` (covered with O 33 r 21(5)) |  |
| O33 r21(5)(b) | 4853-4854 | encoded | `o 33 r 21(5) the claimant may apply to the Court for judgment by default against a defendant who served no defence` (covered with O 33 r 21(5)) |  |
| O33 r21(5)(c) | 4855-4857 | encoded | `o 33 r 21(5) the claimant may apply to the Court for judgment by default against a defendant who served no defence` (covered with O 33 r 21(5)) |  |
| O33 r21(6) | 4858 | encoded | `o 33 r 21(6) the defendant making the counterclaim may apply to the Court for judgment by default` |  |
| O33 r21(6)(a) | 4858-4859 | encoded | `o 33 r 21(6) the defendant making the counterclaim may apply to the Court for judgment by default` (covered with O 33 r 21(6)) |  |
| O33 r21(6)(b) | 4860-4861 | encoded | `o 33 r 21(6) the defendant making the counterclaim may apply to the Court for judgment by default` (covered with O 33 r 21(6)) |  |
| O33 r21(6)(c) | 4862-4864 | encoded | `o 33 r 21(6) the defendant making the counterclaim may apply to the Court for judgment by default` (covered with O 33 r 21(6)) |  |
| O33 r21(7) | 4865 | encoded | `o 33 r 21(7) an application may be made under paragraph (6) against the claimant` |  |
| O33 r21(8) | 4866 | encoded | `o 33 r 21(8) an application under this Rule is made by summons`; `o 33 r 21(8) an application under this Rule is made by summons (the duty arises)`; `o 33 r 21(8) the Court may give judgment for the claim with or without a reference to the Registrar`; `o 33 r 21(8) the Court may order the property to be appraised and sold or make such other order` |  |
| O33 r21(9) | 4867 | encoded | `o 33 r 21(9) a copy of the summons and the affidavit is served on each person mentioned in Rule 12(2)`; `o 33 r 21(9) a copy of the summons and the affidavit is served on each person mentioned in Rule 12(2) (the duty arises)`; `o 33 r 21(9) the period before the hearing`; `o 33 r 21(9) the copies are served in time` | F-ALL-1 |
| O33 r21(10) | 4868 | encoded | `o 33 r 21(10) the rate of interest per year, in percent`; `o 33 r 21(10) the Court may direct the payment of interest on the judgment`; `o 33 r 21(10) the interest on the sum` | F-33-5 |
| O33 r21(11) | 4869 | encoded | `o 33 r 21(11) evidence may be given by affidavit in default actions in rem` |  |
| O33 r21(12) | 4870 | encoded | `o 33 r 21(12) the Court may set aside or vary a judgment entered pursuant to this Rule` |  |
| O33 r21(13) | 4871 | encoded | `o 33 r 21(13) Order 6 Rules 6(5), 7(7) and 9(3) apply to the action` |  |
| O33 r22 | 4872-4895 | encoded | see the sub-rows (17 functions under this provision) |  |
| O33 r22(1) | 4873 | encoded | `o 33 r 22(1) the party may apply for an order determining the order of priority` |  |
| O33 r22(1)(a) | 4873-4874 | encoded | `o 33 r 22(1) the party may apply for an order determining the order of priority` (covered with O 33 r 22(1)) |  |
| O33 r22(1)(b) | 4875-4877 | encoded | `o 33 r 22(1) the party may apply for an order determining the order of priority` (covered with O 33 r 22(1)) |  |
| O33 r22(2) | 4878 | encoded | `o 33 r 22(2) the Court may further order` |  |
| O33 r22(2)(a) | 4878-4879 | encoded | `o 33 r 22(2)(a) the period before the order of priority is determined` | F-ALL-1 |
| O33 r22(2)(b) | 4880-4881 | encoded | `o 33 r 22(2) the Court may further order` (covered with O 33 r 22(2)) |  |
| O33 r22(2)(c) | 4882-4883 | encoded | `o 33 r 22(2)(c) the period for sending the notice`; `o 33 r 22(2)(c) the Sheriff sends the notice for publication in time`; `o 33 r 22(2)(c) duty` | F-ALL-1 |
| O33 r22(3) | 4884 | encoded | `o 33 r 22(3) the notice states what it must state`; `o 33 r 22(3) the notice states what it must state (the duty arises)` |  |
| O33 r22(3)(a) | 4884-4885 | encoded | `o 33 r 22(3) the notice states what it must state`; `o 33 r 22(3) the notice states what it must state (the duty arises)` (covered with O 33 r 22(3)) |  |
| O33 r22(3)(b) | 4886-4887 | encoded | `o 33 r 22(3) the notice states what it must state`; `o 33 r 22(3) the notice states what it must state (the duty arises)` (covered with O 33 r 22(3)) |  |
| O33 r22(3)(c) | 4888-4889 | encoded | `o 33 r 22(3) the notice states what it must state`; `o 33 r 22(3) the notice states what it must state (the duty arises)` (covered with O 33 r 22(3)) |  |
| O33 r22(3)(d) | 4890-4891 | encoded | `o 33 r 22(3) the notice states what it must state`; `o 33 r 22(3) the notice states what it must state (the duty arises)` (covered with O 33 r 22(3)) |  |
| O33 r22(4) | 4892 | encoded | `o 33 r 22(4) the Sheriff lodges in the Registry a copy of each newspaper or publication`; `o 33 r 22(4) the Sheriff lodges in the Registry a copy of each newspaper or publication (the duty arises)` |  |
| O33 r22(5) | 4893 | encoded | `o 33 r 22(5) the Sheriff's expenses of complying with the order are included in the expenses relating to the sale`; `o 33 r 22(5) the Sheriff's expenses of complying with the order are included in the expenses relating to the sale (the duty arises)` |  |
| O33 r22(6) | 4894 | encoded | `o 33 r 22(6) the application to extend the period is made by summons and a copy served on each party`; `o 33 r 22(6) the application to extend the period is made by summons and a copy served on each party (the duty arises)`; `o 33 r 22(6) the period before the hearing`; `o 33 r 22(6) the copy of the summons is served in time` | F-ALL-1 |
| O33 r22(7) | 4895 | encoded | `o 33 r 22(7) a court is the Court in this Rule` |  |
| O33 r22(7) def “Court” | 4895 | encoded | `o 33 r 22(7) a court is the Court in this Rule` |  |
| O33 r23 | 4896-4900 | encoded | see the sub-rows (9 functions under this provision) |  |
| O33 r23(1) | 4897 | encoded | `o 33 r 23(1) the party requesting a commission for appraisement and sale files a commission in Form 58`; `o 33 r 23(1) the party requesting a commission for appraisement and sale files a commission in Form 58 (the duty arises)` |  |
| O33 r23(2) | 4897 | encoded | `o 33 r 23(2) the commission is executed by the Sheriff`; `o 33 r 23(2) the commission is executed by the Sheriff (the duty arises)` |  |
| O33 r23(3) | 4898 | encoded | `o 33 r 23(3) the commission for appraisement and sale cannot yet be executed for want of the undertaking` |  |
| O33 r23(4) | 4899 | encoded | `o 33 r 23(4) the Sheriff pays the gross proceeds into Court and brings the accounts into Court`; `o 33 r 23(4) the Sheriff pays the gross proceeds into Court and brings the accounts into Court (the duty arises)` |  |
| O33 r23(5) | 4900 | encoded | `o 33 r 23(5) a person interested in the proceeds of the sale is entitled to be heard on the assessment`; `o 33 r 23(5) a decision of the Registrar on the assessment may be reviewed` |  |
| O33 r24 | 4901-4903 | encoded | see the sub-rows (4 functions under this provision) |  |
| O33 r24(1) | 4902 | encoded | `o 33 r 24(1) every undertaking under this Order is given in writing to the satisfaction of the Sheriff`; `o 33 r 24(1) every undertaking under this Order is given in writing to the satisfaction of the Sheriff (the duty arises)` |  |
| O33 r24(2) | 4902 | encoded | `o 33 r 24(2) the Sheriff may accept a deposit instead of an undertaking` |  |
| O33 r24(3) | 4903 | encoded | `o 33 r 24(3) the Court may vary or revoke a direction or determination of the Sheriff` |  |
| O33 r25 | 4904-4912 | encoded | see the sub-rows (4 functions under this provision) |  |
| O33 r25(1) | 4905 | encoded | `o 33 r 25(1) a Rule of Order 14 applies to the Admiralty action` |  |
| O33 r25(2) | 4905 | encoded | `o 33 r 25(2) the money paid into Court may be paid out` |  |
| O33 r25(3) | 4906 | encoded | `o 33 r 25(3) the Registrar may order the money to be paid out with the consent of the interested parties` |  |
| O33 r25(3)(a) | 4906-4907 | encoded | `o 33 r 25(3) the Registrar may order the money to be paid out with the consent of the interested parties` (covered with O 33 r 25(3)) |  |
| O33 r25(3)(b) | 4908-4909 | encoded | `o 33 r 25(3) the Registrar may order the money to be paid out with the consent of the interested parties` (covered with O 33 r 25(3)) |  |
| O33 r25(3)(c) | 4910-4911 | encoded | `o 33 r 25(3) the Registrar may order the money to be paid out with the consent of the interested parties` (covered with O 33 r 25(3)) |  |
| O33 r25(4) | 4912 | encoded | `o 33 r 25(4) the Registrar may order the money paid into Court under Order 13 Rule 8 to be paid out` |  |
| O33 r26 | 4913-4916 | encoded | see the sub-rows (5 functions under this provision) |  |
| O33 r26(1) | 4914 | encoded | `o 33 r 26(1) Order 9 Rules 8 and 9 apply to the Admiralty action` |  |
| O33 r26(2) | 4914 | encoded | `o 33 r 26(2) the order or application under Order 9 Rule 9 determines whether the trial is with assessors`; `o 33 r 26(2) the order or application under Order 9 Rule 9 determines whether the trial is with assessors (the duty arises)` |  |
| O33 r26(3) | 4915 | encoded | `o 33 r 26(3) an order or direction may limit the witnesses who may be called at the trial` |  |
| O33 r26(4) | 4916 | encoded | `o 33 r 26(4) an order or direction mentioned in paragraphs (2) and (3) may be varied or revoked` |  |
| O33 r27 | 4917-4922 | encoded | see the sub-rows (6 functions under this provision) |  |
| O33 r27(1) | 4918 | encoded | `o 33 r 27(1) Order 9 Rule 25 applies to the Admiralty action` |  |
| O33 r27(2) | 4918 | encoded | `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts`; `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts (the duty arises)`; `o 33 r 27(2) the period before the trial`; `o 33 r 27(2) the party files in time before the trial` | F-ALL-1 |
| O33 r27(2)(a) | 4918-4919 | encoded | `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts`; `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts (the duty arises)`; `o 33 r 27(2) the period before the trial`; `o 33 r 27(2) the party files in time before the trial` (covered with O 33 r 27(2)) | F-ALL-1 |
| O33 r27(2)(b) | 4920-4921 | encoded | `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts`; `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts (the duty arises)`; `o 33 r 27(2) the period before the trial`; `o 33 r 27(2) the party files in time before the trial` (covered with O 33 r 27(2)) | F-ALL-1 |
| O33 r27(3) | 4922 | encoded | `o 33 r 27(3) Order 16 Rule 2(5) applies to the Admiralty action` |  |
| O33 r28 | 4923-4928 | encoded | `o 33 r 28 the Court may stay proceedings in the firstmentioned action until security is given` |  |
| O33 r28(a) | 4924-4925 | encoded | `o 33 r 28 the Court may stay proceedings in the firstmentioned action until security is given` (covered with O 33 r 28) |  |
| O33 r28(b) | 4926-4928 | encoded | `o 33 r 28 the Court may stay proceedings in the firstmentioned action until security is given` (covered with O 33 r 28) |  |
| O33 r29 | 4929-4930 | encoded | `o 33 r 29 the Court may order the inspection of a ship or other property` |  |
| O33 r30 | 4931-4942 | encoded | see the sub-rows (13 functions under this provision) |  |
| O33 r30(1) | 4932 | encoded | `o 33 r 30(1) the power under Order 9 Rule 24 extends to an examination on oath before a Judge` |  |
| O33 r30(2) | 4932 | encoded | `o 33 r 30(2) the power under Order 9 Rule 24 extends to evidence taken as if before an examiner` |  |
| O33 r30(3) | 4933 | encoded | `o 33 r 30(3) the order may make provision for consequential matters` |  |
| O33 r30(3)(a) | 4933-4934 | encoded | `o 33 r 30(3)(a) the party whose witness is to be examined provides a shorthand writer`; `o 33 r 30(3)(a) the party whose witness is to be examined provides a shorthand writer (the duty arises)` |  |
| O33 r30(3)(b) | 4935-4936 | encoded | `o 33 r 30(3)(b) a representative of either party has authority to administer the oath` |  |
| O33 r30(3)(c) | 4937-4938 | encoded | `o 33 r 30(3)(c) the shorthand writer certifies the transcript and the solicitor files it`; `o 33 r 30(3)(c) the shorthand writer certifies the transcript and the solicitor files it (the duty arises)` |  |
| O33 r30(3)(d) | 4939-4940 | encoded | `o 33 r 30(3)(d) the transcript is made available to counsel and any certificate of corrections is filed with it`; `o 33 r 30(3)(d) the transcript is made available to counsel and any certificate of corrections is filed with it (the duty arises)` |  |
| O33 r30(4) | 4941 | encoded | `o 33 r 30(4) an order authorising an examination of a witness cannot yet be made for want of the preliminary acts`; `o 33 r 30(4) an order may be made under Order 9 Rule 24 authorising an examination of a witness` |  |
| O33 r30(5) | 4942 | encoded | `o 33 r 30(5) Order 9 Rule 24 applies to the Admiralty cause or matter` |  |
| O33 r31 | 4943-4944 | encoded | `o 33 r 31 Order 15 Rule 4(1) to (6) applies to the order to attend court` |  |
| O33 r32 | 4945-4947 | encoded | see the sub-rows (7 functions under this provision) |  |
| O33 r32(1) | 4946 | encoded | `o 33 r 32(1) the proceedings for the apportionment of salvage are begun in the way required`; `o 33 r 32(1) the proceedings for the apportionment of salvage are begun in the way required (the duty arises)` |  |
| O33 r32(2) | 4946 | encoded | `o 33 r 32(2) the originating application or summons and the supporting affidavit are filed and served`; `o 33 r 32(2) the originating application or summons and the supporting affidavit are filed and served (the duty arises)`; `o 33 r 32(2) the period before the hearing`; `o 33 r 32(2) the filing and service are in time before the hearing` | F-ALL-1 |
| O33 r32(3) | 4947 | encoded | `o 33 r 32(3) the Judge may exercise the powers conferred by section 175 of the Merchant Shipping Act` |  |
| O33 r33 | 4948-4950 | encoded | see the sub-rows (7 functions under this provision) |  |
| O33 r33(1) | 4949 | encoded | `o 33 r 33(1) a summons and the affidavits in support are filed in the Registry`; `o 33 r 33(1) a summons and the affidavits in support are filed in the Registry (the duty arises)`; `o 33 r 33(1) the period before the hearing`; `o 33 r 33(1) the summons is filed in time before the hearing` | F-ALL-1 |
| O33 r33(2) | 4949 | encoded | `o 33 r 33(2) a copy of the summons and affidavits is served on all the other parties`; `o 33 r 33(2) a copy of the summons and affidavits is served on all the other parties (the duty arises)` |  |
| O33 r33(3) | 4950 | encoded | `o 33 r 33(3) paragraph (2) applies to the summons` |  |
| O33 r34 | 4951-4952 | encoded | `o 33 r 34 the Registrar may allow an agreement between solicitors to be filed`; `o 33 r 34 the filed agreement becomes an order of court` |  |
| O33 r35 | 4953-4954 | encoded | see the sub-rows (2 functions under this provision) |  |
| O33 r35(1) | 4954 | encoded | `o 33 r 35(1) Order 15 Rule 1(1) applies to Admiralty proceedings begun by originating application` |  |
| O33 r35(2) | 4954 | encoded | `o 33 r 35(2) a provision of Rule 27 applies to the Admiralty cause or matter` |  |
| O33 r36 | 4955-4959 | encoded | see the sub-rows (14 functions under this provision) |  |
| O33 r36(1) | 4956 | encoded | `o 33 r 36(1) the person seeking relief is the claimant in a limitation action`; `o 33 r 36(1) the claimant is named in the originating claim by the claimant's name`; `o 33 r 36(1) the claimant is named in the originating claim by the claimant's name (the duty arises)` |  |
| O33 r36(2) | 4956 | encoded | `o 33 r 36(2) the claimant makes one of the persons with claims a defendant`; `o 33 r 36(2) the claimant makes one of the persons with claims a defendant (the duty arises)`; `o 33 r 36(2) the claimant may make all or any of the others defendants also` |  |
| O33 r36(3) | 4957 | encoded | `o 33 r 36(3) at least one defendant is named in the originating claim by the defendant's name`; `o 33 r 36(3) at least one defendant is named in the originating claim by the defendant's name (the duty arises)`; `o 33 r 36(3) the other defendants may be described generally` |  |
| O33 r36(4) | 4958 | encoded | `o 33 r 36(4) the originating claim is served on one or more of the defendants named by their names`; `o 33 r 36(4) the originating claim is served on one or more of the defendants named by their names (the duty arises)`; `o 33 r 36(4) the originating claim must be served on a defendant not named by name` |  |
| O33 r36(5) | 4959 | encoded | `o 33 r 36(5) “name” includes a firm name or the name under which a person carries on business`; `o 33 r 36(5) a person described merely as owner is deemed to have been named by name` |  |
| O33 r36(5) def “name” | 4959 | encoded | `o 33 r 36(5) “name” includes a firm name or the name under which a person carries on business`; `o 33 r 36(5) a person described merely as owner is deemed to have been named by name` |  |
| O33 r37 | 4960-4970 | encoded | see the sub-rows (7 functions under this provision) |  |
| O33 r37(1) | 4961 | encoded | `o 33 r 37(1) the Court may allow the person to constitute a limitation fund in the way` |  |
| O33 r37(1)(a) | 4961-4962 | encoded | `o 33 r 37(1) the Court may allow the person to constitute a limitation fund in the way` (covered with O 33 r 37(1)) |  |
| O33 r37(1)(b) | 4963-4964 | encoded | `o 33 r 37(1) the Court may allow the person to constitute a limitation fund in the way` (covered with O 33 r 37(1)) |  |
| O33 r37(2) | 4965 | encoded | `o 33 r 37(2) a limitation fund may be established before or after the commencement of a limitation action` |  |
| O33 r37(3) | 4966 | encoded | `o 33 r 37(3) the period for commencing the limitation action`; `o 33 r 37(3) the limitation action is commenced in time` | F-ALL-1 |
| O33 r37(3)(a) | 4966-4967 | encoded | `o 33 r 37(3)(a) the limitation fund lapses` | F-ALL-1 |
| O33 r37(3)(b) | 4968-4969 | encoded | `o 33 r 37(3)(b) the money paid into Court is repaid to the person who paid it` | F-ALL-1 |
| O33 r37(4) | 4970 | encoded | `o 33 r 37(4) the money paid into Court under paragraph (1) may be paid out` |  |
| O33 r38 | 4971-4985 | encoded | see the sub-rows (21 functions under this provision) |  |
| O33 r38(1) | 4972 | encoded | `o 33 r 38(1) the claimant takes out a summons before the Registrar for a decree limiting liability`; `o 33 r 38(1) the claimant takes out a summons before the Registrar for a decree limiting liability (the duty arises)`; `o 33 r 38(1) the period for the summons`; `o 33 r 38(1) the claimant takes out the summons in time` | F-ALL-1 |
| O33 r38(2) | 4972 | encoded | `o 33 r 38(2) the summons is supported by the affidavits required`; `o 33 r 38(2) the summons is supported by the affidavits required (the duty arises)` |  |
| O33 r38(2)(a) | 4972-4973 | encoded | `o 33 r 38(2) the summons is supported by the affidavits required`; `o 33 r 38(2) the summons is supported by the affidavits required (the duty arises)` (covered with O 33 r 38(2)) |  |
| O33 r38(2)(b) | 4974-4975 | encoded | `o 33 r 38(2) the summons is supported by the affidavits required`; `o 33 r 38(2) the summons is supported by the affidavits required (the duty arises)` (covered with O 33 r 38(2)) |  |
| O33 r38(3) | 4976 | encoded | `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims`; `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims (the duty arises)` |  |
| O33 r38(3)(a) | 4976-4977 | encoded | `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims`; `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims (the duty arises)` (covered with O 33 r 38(3)) |  |
| O33 r38(3)(b) | 4978-4979 | encoded | `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims`; `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims (the duty arises)` (covered with O 33 r 38(3)) |  |
| O33 r38(4) | 4980 | encoded | `o 33 r 38(4) the summons and every affidavit in support are served on any defendant who has filed a notice`; `o 33 r 38(4) the summons and every affidavit in support are served on any defendant who has filed a notice (the duty arises)`; `o 33 r 38(4) the period before the hearing`; `o 33 r 38(4) the summons and affidavits are served in time before the hearing` | F-ALL-1 |
| O33 r38(5) | 4981 | encoded | `o 33 r 38(5) the Court makes a decree limiting the claimant's liability`; `o 33 r 38(5) the Court makes a decree limiting the claimant's liability (the duty arises)` |  |
| O33 r38(6) | 4982 | encoded | `o 33 r 38(6) the Court gives directions for the defendant to obtain information and adjourns`; `o 33 r 38(6) the Court gives directions for the defendant to obtain information and adjourns (the duty arises)` |  |
| O33 r38(7) | 4983 | encoded | `o 33 r 38(7) the Court gives directions as to the further proceedings`; `o 33 r 38(7) the Court gives directions as to the further proceedings (the duty arises)` |  |
| O33 r38(8) | 4984 | encoded | `o 33 r 38(8) a defendant who ceases to dispute the right to limit files and serves a notice forthwith`; `o 33 r 38(8) a defendant who ceases to dispute the right to limit files and serves a notice forthwith (the duty arises)` | F-33-9 |
| O33 r38(9) | 4985 | encoded | `o 33 r 38(9) the claimant may take out a summons before the Court for a decree` |  |
| O33 r39 | 4986-5003 | encoded | see the sub-rows (15 functions under this provision) |  |
| O33 r39(1) | 4987 | encoded | see the sub-rows (2 functions under this provision) |  |
| O33 r39(1)(a) | 4987-4988 | encoded | `o 33 r 39(1)(a) the decree must be advertised` |  |
| O33 r39(1)(b) | 4989-4990 | encoded | `o 33 r 39(1)(b) the decree protects the claimant against the claim` |  |
| O33 r39(2) | 4991 | encoded | see the sub-rows (4 functions under this provision) |  |
| O33 r39(2)(a) | 4991-4992 | encoded | `o 33 r 39(2)(a) the claimant advertises the decree in the manner and within the time the decree provides`; `o 33 r 39(2)(a) the claimant advertises the decree in the manner and within the time the decree provides (the duty arises)` |  |
| O33 r39(2)(b) | 4993-4994 | encoded | `o 33 r 39(2)(b) the decree fixes a time for notices, claims and summonses`; `o 33 r 39(2)(b) the decree fixes a time for notices, claims and summonses (the duty arises)` |  |
| O33 r39(3) | 4995 | encoded | `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers`; `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers (the duty arises)` |  |
| O33 r39(3)(a) | 4995-4996 | encoded | `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers`; `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers (the duty arises)` (covered with O 33 r 39(3)) |  |
| O33 r39(3)(b) | 4997-4998 | encoded | `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers`; `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers (the duty arises)` (covered with O 33 r 39(3)) |  |
| O33 r39(3)(c) | 4999-5000 | encoded | `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers`; `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers (the duty arises)` (covered with O 33 r 39(3)) |  |
| O33 r39(4) | 5001 | encoded | `o 33 r 39(4) the claimant files the copies of the newspapers in time`; `o 33 r 39(4) the claimant files a copy of each newspaper in which the advertisement appears`; `o 33 r 39(4) the claimant files a copy of each newspaper in which the advertisement appears (the duty arises)` | F-ALL-1 |
| O33 r39(5) | 5002 | encoded | `o 33 r 39(5) the time allowed is not less than 2 months from the latest date allowed for the advertisements`; `o 33 r 39(5) the time allowed is not less than 2 months from the latest date allowed for the advertisements (the duty arises)`; `o 33 r 39(5) the step may be taken after the time allowed has expired` |  |
| O33 r39(6) | 5003 | encoded | `o 33 r 39(6) the decree may make any provision authorised by the Merchant Shipping Act` |  |
| O33 r40 | 5004-5012 | encoded | see the sub-rows (10 functions under this provision) |  |
| O33 r40(1) | 5005 | encoded | `o 33 r 40(1) a person with a claim may take out a summons to set the decree aside`; `o 33 r 40(1) the person takes out the summons within the time fixed by the decree` | F-ALL-1 |
| O33 r40(1)(a) | 5005-5006 | encoded | `o 33 r 40(1) a person with a claim may take out a summons to set the decree aside`; `o 33 r 40(1) the person takes out the summons within the time fixed by the decree` (covered with O 33 r 40(1)) | F-ALL-1 |
| O33 r40(1)(b) | 5007-5009 | encoded | `o 33 r 40(1) a person with a claim may take out a summons to set the decree aside`; `o 33 r 40(1) the person takes out the summons within the time fixed by the decree` (covered with O 33 r 40(1)) | F-ALL-1 |
| O33 r40(2) | 5010 | encoded | `o 33 r 40(2) the summons is supported by an affidavit showing a bona fide claim and prima facie grounds`; `o 33 r 40(2) the summons is supported by an affidavit showing a bona fide claim and prima facie grounds (the duty arises)` |  |
| O33 r40(3) | 5011 | encoded | `o 33 r 40(3) the summons and every affidavit in support are served on the claimant and any defendant who has filed a notice`; `o 33 r 40(3) the summons and every affidavit in support are served on the claimant and any defendant who has filed a notice (the duty arises)`; `o 33 r 40(3) the period before the hearing`; `o 33 r 40(3) the summons and affidavits are served in time before the hearing` | F-ALL-1 |
| O33 r40(4) | 5012 | encoded | `o 33 r 40(4) the Registrar sets the decree aside and gives directions`; `o 33 r 40(4) the Registrar sets the decree aside and gives directions (the duty arises)` |  |
| O33 r41 | 5013-5027 | encoded | see the sub-rows (24 functions under this provision) |  |
| O33 r41(1) | 5014 | encoded | `o 33 r 41(1) the claiming party files the claim`; `o 33 r 41(1) the claiming party files the claim (the duty arises)`; `o 33 r 41(1) the claiming party serves a copy of the claim on every other party`; `o 33 r 41(1) the claiming party serves a copy of the claim on every other party (the duty arises)`; `o 33 r 41(1) the period for filing the claim`; and 1 more under the same provision label | F-ALL-1 |
| O33 r41(2) | 5014 | encoded | `o 33 r 41(2) a party may apply to the Registrar under Order 9 Rule 9 as to the proceedings on the reference`; `o 33 r 41(2) the period before the hearing`; `o 33 r 41(2) the application is made in time before the hearing`; `o 33 r 41(2) the Registrar gives directions on the application`; `o 33 r 41(2) the Registrar gives directions on the application (the duty arises)` | F-ALL-1 |
| O33 r41(2)(a) | 5014-5015 | encoded | `o 33 r 41(2) a party may apply to the Registrar under Order 9 Rule 9 as to the proceedings on the reference`; `o 33 r 41(2) the period before the hearing`; `o 33 r 41(2) the application is made in time before the hearing`; `o 33 r 41(2) the Registrar gives directions on the application`; `o 33 r 41(2) the Registrar gives directions on the application (the duty arises)` (covered with O 33 r 41(2)) | F-ALL-1 |
| O33 r41(2)(b) | 5016-5018 | encoded | `o 33 r 41(2) a party may apply to the Registrar under Order 9 Rule 9 as to the proceedings on the reference`; `o 33 r 41(2) the period before the hearing`; `o 33 r 41(2) the application is made in time before the hearing`; `o 33 r 41(2) the Registrar gives directions on the application`; `o 33 r 41(2) the Registrar gives directions on the application (the duty arises)` (covered with O 33 r 41(2)) | F-ALL-1 |
| O33 r41(3) | 5019 | encoded | `o 33 r 41(3) the appointment of the day for the hearing is made in the way required`; `o 33 r 41(3) the appointment of the day for the hearing is made in the way required (the duty arises)` |  |
| O33 r41(4) | 5020 | encoded | `o 33 r 41(4) an appointment for the hearing of the reference cannot yet be made` |  |
| O33 r41(5) | 5021 | encoded | `o 33 r 41(5) the claiming party or the claimant enters the reference for hearing`; `o 33 r 41(5) the claiming party or the claimant enters the reference for hearing (the duty arises)`; `o 33 r 41(5) the period for lodging the Request`; `o 33 r 41(5) the Request is lodged in time`; `o 33 r 41(5) duty` | F-ALL-1 |
| O33 r41(6) | 5022 | encoded | `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies`; `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies (the duty arises)`; `o 33 r 41(6) the period before the hearing`; `o 33 r 41(6) the list and affidavits are filed in time before the hearing` | F-ALL-1 |
| O33 r41(6)(a) | 5022-5023 | encoded | `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies`; `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies (the duty arises)`; `o 33 r 41(6) the period before the hearing`; `o 33 r 41(6) the list and affidavits are filed in time before the hearing` (covered with O 33 r 41(6)) | F-ALL-1 |
| O33 r41(6)(b) | 5024-5026 | encoded | `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies`; `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies (the duty arises)`; `o 33 r 41(6) the period before the hearing`; `o 33 r 41(6) the list and affidavits are filed in time before the hearing` (covered with O 33 r 41(6)) | F-ALL-1 |
| O33 r41(7) | 5027 | encoded | `o 33 r 41(7) the Court may dismiss the claim` |  |
| O33 r42 | 5028-5037 | encoded | `o 33 r 42 a reference is heard under this Rule` |  |
| O33 r42(1) | 5029 | encoded | `o 33 r 42(1) the Registrar may adjourn the hearing of a reference` |  |
| O33 r42(2) | 5029 | encoded | `o 33 r 42(2) the Registrar may give a direction limiting the witnesses`; `o 33 r 42(2) the direction may be revoked or varied on sufficient cause` |  |
| O33 r42(3) | 5030 | encoded | `o 33 r 42(3) evidence may be given in the manner`; `o 33 r 42(3) the evidence is recorded under Order 15 Rule 11(5), (6) and (7)`; `o 33 r 42(3) the evidence is recorded under Order 15 Rule 11(5), (6) and (7) (the duty arises)` |  |
| O33 r42(4) | 5031 | encoded | `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice`; `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice (the duty arises)` |  |
| O33 r42(4)(a) | 5031-5032 | encoded | `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice`; `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice (the duty arises)` (covered with O 33 r 42(4)) |  |
| O33 r42(4)(b) | 5033-5034 | encoded | `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice`; `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice (the duty arises)` (covered with O 33 r 42(4)) |  |
| O33 r42(4)(c) | 5035-5036 | encoded | `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice`; `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice (the duty arises)` (covered with O 33 r 42(4)) |  |
| O33 r42(5) | 5037 | encoded | `o 33 r 42(5) a party may request a statement of the grounds of the decision`; `o 33 r 42(5) the period for the request`; `o 33 r 42(5) the party makes the written request in time` | F-ALL-1 |
| O33 r43 | 5038-5044 | encoded | see the sub-rows (10 functions under this provision) |  |
| O33 r43(1) | 5039 | encoded | `o 33 r 43(1) a party to a reference may apply to a Judge to set aside or vary the decision` | F-ALL-1 |
| O33 r43(1)(a) | 5039-5040 | encoded | `o 33 r 43(1)(a) the period after the notice of the decision`; `o 33 r 43(1)(a) the summons is filed in time after the notice of the filing of the decision` | F-ALL-1 |
| O33 r43(1)(b) | 5041-5042 | encoded | `o 33 r 43(1)(b) the period after the notice of the statement of the grounds`; `o 33 r 43(1)(b) the summons is filed in time after the notice of the statement of the grounds` | F-ALL-1 |
| O33 r43(2) | 5043 | encoded | `o 33 r 43(2) the decision is deemed to be given on the date on which it is filed`; `o 33 r 43(2) the decision cannot yet be acted upon`; `o 33 r 43(2) the decision may be acted upon` |  |
| O33 r43(3) | 5044 | encoded | `o 33 r 43(3) a direction may be given under paragraph (2) without the parties being given an opportunity of being heard`; `o 33 r 43(3) the direction may be incorporated in the Registrar's decision` |  |
| O33 r44 | 5045-5046 | encoded | `o 33 r 44 Order 26 Rule 3 applies to documents filed in the Registry` |  |
| O33 r45 | 5047-5048 | encoded | `o 33 r 45 Rules 35 to 40 limit the right to rely by way of defence on the Merchant Shipping Act` |  |
| O33 r46 | 5049-5050 | encoded | see the sub-rows (2 functions under this provision) |  |
| O33 r46(1) | 5050 | encoded | `o 33 r 46(1) the Court may order the production of documents in a marine insurance action` |  |
| O33 r46(2) | 5050 | encoded | `o 33 r 46(2) the order may be made on terms as to staying proceedings or otherwise` |  |

## Fork register (roc7)

The rulings of 2026-11-04 and 2026-11-05 that bind this row, word for word as printed in the brief:


- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

The brief governs over PLAN.md where the two differ on periods: PLAN.md section 2 would have answered NOTHING outside a period, and the brief's periods ruling (a) of 2026-11-05 answers JUST FALSE; this row follows the brief (fork F-ALL-1).
Where several sections give one legal effect, each section's answer is its own function (option C of E1).
By hand and in plain L4 (option B as guidance for hand-gathering only) three Moment-valued functions gather the routes of Order 28: `o 28 r 10 the moment the document is deemed filed`, `o 28 r 11 the moment time for service begins to run` and `o 28 r 12 the moment service is deemed effected`; they are the seams S-F1, S-F2 and S-S2 of PLAN.md, and each route also has its own section function.
The source is a converter rendering, not the official text: a reading that turns on punctuation (the "and" of O 33 r 11(1), the "(b) and (c)" of O 28 r 7(4)(a)) is the first to check against the official text.

### Judgment calls

The corpus owner's instruction of 2026-11-05 (relayed by the lead): the six open convention questions are decided case by case, at encoding time, by my best judgment of what the text says, and human review catches an error.
The defaults printed in the brief were starting points; where the text pointed the other way I did not follow them.
Each line below is one site, so that a human reviewer can find it and overrule it: question | provision | function name | file and line of the function | the answer taken | the other reading.
A site is found by the marker `(open convention question QX)` in the comment of the branch that raises it; no function name and no `@desc` mentions the questions.
No twin function was added for any reading; the companions "(the duty arises)" of QD are kept because a party plainly asks "does this duty apply to me?" before "did I comply?".
Where a site is decided the same way as the others of its question the line says so in the same words, so the lines can be sorted by "answer taken".


**QA** (14 sites):

```
QA | O 32 r 3(3) | o 32 r 3(3) a party other than the executors or administrators is entitled to appear | roc7-order-32.l4:194 | JUST TRUE once the exception is met: the permission, order or direction the sentence names is what permits the act, and the sentence says so in its own words | NOTHING (a lifted bar grants nothing), or NOTHING plus a yes/no "is it barred under this rule?" twin
QA | O 32 r 5(1) | o 32 r 5(1) a judgment or order for administration or execution need be given or made | roc7-order-32.l4:245 | NOTHING once the "unless" is met: it lifts the exemption ("need not") on the Court's opinion and does not say that a judgment or order must then be given | JUST TRUE (the exemption is lifted, so one need be given)
QA | O 33 r 4(3) | o 33 r 4(3) a warrant of arrest may be issued | roc7-order-33a.l4:441 | two exceptions, answered differently: JUST TRUE where the exception is the Court's (or Registrar's) permission, order or direction; NOTHING where it is a fact that only ends the bar (a filing, a notice, the lapse of time, another action) because the sentence is then silent about the act | NOTHING for both limbs (a lifted bar grants nothing), or JUST TRUE for both (the exception permits it)
QA | O 33 r 4(4) | o 33 r 4(4) a warrant of arrest may be issued against the foreign ship | roc7-order-33a.l4:468 | two exceptions, answered differently: JUST TRUE where the exception is the Court's (or Registrar's) permission, order or direction; NOTHING where it is a fact that only ends the bar (a filing, a notice, the lapse of time, another action) because the sentence is then silent about the act | NOTHING for both limbs (a lifted bar grants nothing), or JUST TRUE for both (the exception permits it)
QA | O 33 r 11(4) | o 33 r 11(4) the claimant is entitled to enter final or interlocutory judgment in default | roc7-order-33a.l4:1414 | two exceptions, answered differently: JUST TRUE where the exception is the Court's (or Registrar's) permission, order or direction; NOTHING where it is a fact that only ends the bar (a filing, a notice, the lapse of time, another action) because the sentence is then silent about the act | NOTHING for both limbs (a lifted bar grants nothing), or JUST TRUE for both (the exception permits it)
QA | O 33 r 13(2) | o 33 r 13(2) a release may be issued | roc7-order-33a.l4:1563 | two exceptions, answered differently: JUST TRUE where the exception is the Court's (or Registrar's) permission, order or direction; NOTHING where it is a fact that only ends the bar (a filing, a notice, the lapse of time, another action) because the sentence is then silent about the act | NOTHING for both limbs (a lifted bar grants nothing), or JUST TRUE for both (the exception permits it)
QA | O 33 r 16(3) | o 33 r 16(3) an affidavit is to be made on behalf of the corporation | roc7-order-33a.l4:1784 | JUST TRUE once the exception is met: the permission, order or direction the sentence names is what permits the act, and the sentence says so in its own words | NOTHING (a lifted bar grants nothing), or NOTHING plus a yes/no "is it barred under this rule?" twin
QA | O 33 r 18(5) | o 33 r 18(5) a preliminary act may be inspected | roc7-order-33b.l4:254 | JUST TRUE once the exception is met: the permission, order or direction the sentence names is what permits the act, and the sentence says so in its own words | NOTHING (a lifted bar grants nothing), or NOTHING plus a yes/no "is it barred under this rule?" twin
QA | O 33 r 20(1) | o 33 r 20(1) the claimant may serve a reply or a defence to counterclaim on the defendant | roc7-order-33b.l4:546 | JUST TRUE once the exception is met: the permission, order or direction the sentence names is what permits the act, and the sentence says so in its own words | NOTHING (a lifted bar grants nothing), or NOTHING plus a yes/no "is it barred under this rule?" twin
QA | O 33 r 25(2) | o 33 r 25(2) the money paid into Court may be paid out | roc7-order-33b.l4:1259 | JUST TRUE once the exception is met: the permission, order or direction the sentence names is what permits the act, and the sentence says so in its own words | NOTHING (a lifted bar grants nothing), or NOTHING plus a yes/no "is it barred under this rule?" twin
QA | O 33 r 30(4) | o 33 r 30(4) an order may be made under Order 9 Rule 24 authorising an examination of a witness | roc7-order-33c.l4:184 | two exceptions, answered differently: JUST TRUE where the exception is the Court's (or Registrar's) permission, order or direction; NOTHING where it is a fact that only ends the bar (a filing, a notice, the lapse of time, another action) because the sentence is then silent about the act | NOTHING for both limbs (a lifted bar grants nothing), or JUST TRUE for both (the exception permits it)
QA | O 33 r 37(4) | o 33 r 37(4) the money paid into Court under paragraph (1) may be paid out | roc7-order-33c.l4:600 | JUST TRUE once the exception is met: the permission, order or direction the sentence names is what permits the act, and the sentence says so in its own words | NOTHING (a lifted bar grants nothing), or NOTHING plus a yes/no "is it barred under this rule?" twin
QA | O 33 r 39(5) | o 33 r 39(5) the step may be taken after the time allowed has expired | roc7-order-33c.l4:964 | JUST TRUE once the exception is met: the permission, order or direction the sentence names is what permits the act, and the sentence says so in its own words | NOTHING (a lifted bar grants nothing), or NOTHING plus a yes/no "is it barred under this rule?" twin
QA | O 33 r 43(2) | o 33 r 43(2) the decision may be acted upon | roc7-order-33c.l4:1505 | two exceptions, answered differently: JUST TRUE where the exception is the Court's (or Registrar's) permission, order or direction; NOTHING where it is a fact that only ends the bar (a filing, a notice, the lapse of time, another action) because the sentence is then silent about the act | NOTHING for both limbs (a lifted bar grants nothing), or JUST TRUE for both (the exception permits it)
```

The test I applied: an exception that is somebody's permission, order or direction for the very act the bar forbids permits it (JUST TRUE); an exception that is only a fact ending the bar leaves the sentence silent about the act (NOTHING).

**QB** (134 sites):

```
QB | O 28 r 3(1) | o 28 r 3(1) the service is operated by a provider appointed as required | roc7-order-28.l4:180 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 28 r 6(6) | o 28 r 6(6) the registered user has met the conditions for using the electronic filing service | roc7-order-28.l4:288 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 28 r 7(8)(a) | o 28 r 7(8)(a) the Registrar must refund the amount paid in excess or error | roc7-order-28.l4:555 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 28 r 8(1) | o 28 r 8(1) the document is filed using the electronic filing service as required | roc7-order-28.l4:638 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 28 r 8(5) | o 28 r 8(5) the form of the document is as required | roc7-order-28.l4:687 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 28 r 14 | o 28 r 14 the amendment is effected in the manner prescribed in the practice directions | roc7-order-28.l4:1283 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 28 r 15(2)(a) | o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way | roc7-order-28.l4:1301 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 28 r 15(2)(b) | o 28 r 15(2)(b) a true and complete electronic image of the original is created | roc7-order-28.l4:1320 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 29 r 2(2) | o 29 r 2(2) the application is made by summons and supported by an affidavit | roc7-order-29.l4:149 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 29 r 4 | o 29 r 4 the order states what it must state | roc7-order-29.l4:196 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 29 r 5(2) | o 29 r 5(2) the originating application or affidavit states what it must state | roc7-order-29.l4:241 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 29A r 2(2) | o 29A r 2(2) the application is made by summons | roc7-order-29.l4:358 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 29A r 3(1) | o 29A r 3(1) the initial request states what it must state | roc7-order-29.l4:386 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 2(1) | o 30 r 2(1) the Reference is brought by filing it in Form 47 | roc7-order-30.l4:67 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 2(2) | o 30 r 2(2) the Reference is made under the hand of the President of Singapore | roc7-order-30.l4:75 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 2(3) | o 30 r 2(3) the Registrar causes a copy of the Reference to be served on the Attorney-General | roc7-order-30.l4:83 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 3(1) | o 30 r 3(1) the Reference states the questions in a form which can be answered yes or no | roc7-order-30.l4:91 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 3(2) | o 30 r 3(2) the Reference is divided into paragraphs and states what is necessary | roc7-order-30.l4:101 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 4(1) | o 30 r 4(1) the Tribunal consists of the Chief Justice and the other Judges | roc7-order-30.l4:115 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 4(2) | o 30 r 4(2) the Tribunal consists of Judges appointed by the Chief Justice | roc7-order-30.l4:124 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 5(2) | o 30 r 5(2) the person informs the Tribunal in writing of the intention to be heard | roc7-order-30.l4:177 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 6(1) | o 30 r 6(1) the Attorney-General assists the Tribunal | roc7-order-30.l4:207 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 10 | o 30 r 10 the proceeding is held in open court | roc7-order-30.l4:326 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 11 | o 30 r 11 the Registrar serves a notice to attend a hearing for directions | roc7-order-30.l4:349 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 13(1) | o 30 r 13(1) the report is in the form of an answer to the questions | roc7-order-30.l4:378 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 30 r 13(2) | o 30 r 13(2) the Registrar delivers the report to the President of Singapore and the Attorney-General | roc7-order-30.l4:387 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 1(2) | o 31 r 1(2) the Case states what it must state | roc7-order-30.l4:440 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 1(3) | o 31 r 1(3) the Registrar of the Supreme Court lays the Case before a Judge and serves a copy on the Attorney-General | roc7-order-30.l4:459 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 1(4) | o 31 r 1(4) the Judge deals with the Case as if it were a case in the original jurisdiction | roc7-order-30.l4:477 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 2(4) | o 31 r 2(4) the judgment of the General Division is in the form of an answer to the question | roc7-order-30.l4:538 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 2(5) | o 31 r 2(5) the Registrar of the Supreme Court serves notice of the hearing | roc7-order-30.l4:557 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 3 | o 31 r 3 the Registrar of the Supreme Court delivers a copy of the judgment | roc7-order-30.l4:576 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 4(1) | o 31 r 4(1) the State Court continues and disposes of the proceedings according to law | roc7-order-30.l4:586 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 31 r 4(2) | o 31 r 4(2) the State Court determines all questions and makes the orders regarding costs | roc7-order-30.l4:605 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 32 r 3(1) | o 32 r 3(1) all the personal representatives are parties to the action | roc7-order-32.l4:131 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 32 r 3(1) | o 32 r 3(1) a personal representative who does not consent is made a defendant | roc7-order-32.l4:150 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 2(1) | o 33 r 2(1) an action in rem is begun by originating claim in Form 48 | roc7-order-33a.l4:131 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 2(2) | o 33 r 2(2) the originating claim in an Admiralty action in personam is in Form 8 with the words inserted | roc7-order-33a.l4:150 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 2(4) | o 33 r 2(4) the defendant served in Singapore files and serves the notice | roc7-order-33a.l4:177 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 2(5) | o 33 r 2(5) the defendant served out of Singapore files and serves the notice | roc7-order-33a.l4:208 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 2(6) | o 33 r 2(6) the notice is in Form 49 | roc7-order-33a.l4:239 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 4(2) | o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats | roc7-order-33a.l4:399 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 4(6) | o 33 r 4(6) the affidavit states what paragraph (6) requires | roc7-order-33a.l4:509 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 4(7) | o 33 r 4(7) the affidavit states what paragraph (7) requires | roc7-order-33a.l4:540 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 5(1) | o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats | roc7-order-33a.l4:571 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(1) | o 33 r 7(1) the originating claim is served on the property against which the action is brought | roc7-order-33a.l4:664 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(1)(a) | o 33 r 7(1)(a) where the property is freight the originating claim is served on the cargo or the ship | roc7-order-33a.l4:688 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(1)(b) | o 33 r 7(1)(b) where the property has been sold by the Sheriff a sealed copy is filed and served on the Sheriff | roc7-order-33a.l4:710 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(5) | o 33 r 7(5) the Registrar causes a memorandum to be marked on the originating claim | roc7-order-33a.l4:815 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(6) | o 33 r 7(6) the claimant leaves a copy at the Registry and files a request in Form 53 | roc7-order-33a.l4:834 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(6) | o 33 r 7(6) the Sheriff serves the originating claim on the property described in the request | roc7-order-33a.l4:852 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(7) | o 33 r 7(7) the expenses of service are paid to the Sheriff on demand | roc7-order-33a.l4:871 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(8) | o 33 r 7(8) the person effecting service endorses the particulars on the originating claim | roc7-order-33a.l4:890 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(9) | o 33 r 7(9) the Sheriff gives the claimant written notice of the fact and manner of service | roc7-order-33a.l4:916 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(10) | o 33 r 7(10) the claimant serves the originating claim forthwith on the person who entered the caveat | roc7-order-33a.l4:934 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 7(11) | o 33 r 7(11) the amended originating claim is served as required | roc7-order-33a.l4:970 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 9(3) | o 33 r 9(3) the Registrar causes a memorandum to be marked on the warrant | roc7-order-33a.l4:1067 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 9(7) | o 33 r 9(7) the warrant of arrest is served on the property against which it is issued | roc7-order-33a.l4:1119 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 9(8) | o 33 r 9(8) the report of the arrest is made by the person required | roc7-order-33a.l4:1147 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 10(1) | o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy | roc7-order-33a.l4:1190 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 10(2) | o 33 r 10(2) service on landed or transhipped cargo is effected as required | roc7-order-33a.l4:1218 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 11(3) | o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search | roc7-order-33a.l4:1321 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 12(1) | o 33 r 12(1) the Sheriff gives notice of the application to the persons referred to in paragraph (2) | roc7-order-33a.l4:1444 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 12(3) | o 33 r 12(3) the summons and copies of affidavits are served on the Sheriff and the persons referred to in paragraph (2) | roc7-order-33a.l4:1496 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 12(4) | o 33 r 12(4) the Sheriff sends a copy of the order to all the parties to every action against the property | roc7-order-33a.l4:1517 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 13(1) | o 33 r 13(1) the property is released only under an instrument of release in Form 54 | roc7-order-33a.l4:1537 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 13(4) | o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued | roc7-order-33a.l4:1597 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 13(5) | o 33 r 13(5) the party has done what paragraph (5) requires before the property is released | roc7-order-33a.l4:1623 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 14(1) | o 33 r 14(1) the caveat against release and payment is filed in Form 55 and entered in the record of caveats | roc7-order-33a.l4:1671 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 16(1) | o 33 r 16(1) bail is given by bond in Form 57 entered into before a commissioner for oaths or the Registrar | roc7-order-33a.l4:1744 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 16(2) | o 33 r 16(2) the surety makes an affidavit that the surety is able to pay | roc7-order-33a.l4:1763 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 16(3) | o 33 r 16(3) the affidavit required of a corporation is made by an officer | roc7-order-33a.l4:1797 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 16(4) | o 33 r 16(4) the party giving bail serves a notice of bail and files the bond, the affidavits and the proof of service | roc7-order-33a.l4:1819 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 17(2) | o 33 r 17(2) the application for permission to intervene is made by summons without notice with an affidavit | roc7-order-33a.l4:1877 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 17(3) | o 33 r 17(3) the intervener files and serves a notice of intention to contest or not contest | roc7-order-33a.l4:1895 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(2) | o 33 r 18(2) Part One states every matter in paragraphs (a) to (q) | roc7-order-33b.l4:94 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(2) | o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u) | roc7-order-33b.l4:111 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(2) | o 33 r 18(2) the claimant files a preliminary act | roc7-order-33b.l4:136 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(2) | o 33 r 18(2) the defendant files a preliminary act | roc7-order-33b.l4:172 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(5) | o 33 r 18(5) the preliminary act is sealed by the Registrar | roc7-order-33b.l4:233 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(6) | o 33 r 18(6) the claimant serves notice of filing the claimant's preliminary act | roc7-order-33b.l4:267 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(7) | o 33 r 18(7) the defendant serves notice that the defendant has filed a preliminary act | roc7-order-33b.l4:299 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 18(9) | o 33 r 18(9) each party serves a copy of the party's preliminary act on every other party | roc7-order-33b.l4:328 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 19(4) | o 33 r 19(4) the Court orders the claimant's preliminary act to be opened and requires the claimant to satisfy the Court | roc7-order-33b.l4:471 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 20(2) | o 33 r 20(2) the party gives production of electronic track data | roc7-order-33b.l4:564 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 20(3) | o 33 r 20(3) the party allows another party to inspect and copy the electronic track data | roc7-order-33b.l4:612 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 21(4) | o 33 r 21(4) the required exhibit is exhibited in the affidavit verifying the facts | roc7-order-33b.l4:719 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 21(8) | o 33 r 21(8) an application under this Rule is made by summons | roc7-order-33b.l4:794 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 21(9) | o 33 r 21(9) a copy of the summons and the affidavit is served on each person mentioned in Rule 12(2) | roc7-order-33b.l4:837 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 22(3) | o 33 r 22(3) the notice states what it must state | roc7-order-33b.l4:1004 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 22(4) | o 33 r 22(4) the Sheriff lodges in the Registry a copy of each newspaper or publication | roc7-order-33b.l4:1022 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 22(5) | o 33 r 22(5) the Sheriff's expenses of complying with the order are included in the expenses relating to the sale | roc7-order-33b.l4:1040 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 22(6) | o 33 r 22(6) the application to extend the period is made by summons and a copy served on each party | roc7-order-33b.l4:1059 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 23(1) | o 33 r 23(1) the party requesting a commission for appraisement and sale files a commission in Form 58 | roc7-order-33b.l4:1099 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 23(2) | o 33 r 23(2) the commission is executed by the Sheriff | roc7-order-33b.l4:1118 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 23(4) | o 33 r 23(4) the Sheriff pays the gross proceeds into Court and brings the accounts into Court | roc7-order-33b.l4:1150 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 24(1) | o 33 r 24(1) every undertaking under this Order is given in writing to the satisfaction of the Sheriff | roc7-order-33b.l4:1191 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 26(2) | o 33 r 26(2) the order or application under Order 9 Rule 9 determines whether the trial is with assessors | roc7-order-33b.l4:1314 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 27(2) | o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts | roc7-order-33b.l4:1370 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 30(3)(a) | o 33 r 30(3)(a) the party whose witness is to be examined provides a shorthand writer | roc7-order-33c.l4:86 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 30(3)(c) | o 33 r 30(3)(c) the shorthand writer certifies the transcript and the solicitor files it | roc7-order-33c.l4:122 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 30(3)(d) | o 33 r 30(3)(d) the transcript is made available to counsel and any certificate of corrections is filed with it | roc7-order-33c.l4:147 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 32(1) | o 33 r 32(1) the proceedings for the apportionment of salvage are begun in the way required | roc7-order-33c.l4:219 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 32(2) | o 33 r 32(2) the originating application or summons and the supporting affidavit are filed and served | roc7-order-33c.l4:241 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 33(1) | o 33 r 33(1) a summons and the affidavits in support are filed in the Registry | roc7-order-33c.l4:288 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 33(2) | o 33 r 33(2) a copy of the summons and affidavits is served on all the other parties | roc7-order-33c.l4:323 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 36(1) | o 33 r 36(1) the claimant is named in the originating claim by the claimant's name | roc7-order-33c.l4:409 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 36(2) | o 33 r 36(2) the claimant makes one of the persons with claims a defendant | roc7-order-33c.l4:427 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 36(3) | o 33 r 36(3) at least one defendant is named in the originating claim by the defendant's name | roc7-order-33c.l4:457 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 36(4) | o 33 r 36(4) the originating claim is served on one or more of the defendants named by their names | roc7-order-33c.l4:487 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(1) | o 33 r 38(1) the claimant takes out a summons before the Registrar for a decree limiting liability | roc7-order-33c.l4:614 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(2) | o 33 r 38(2) the summons is supported by the affidavits required | roc7-order-33c.l4:651 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(3) | o 33 r 38(3) the affidavit states the names and addresses of the persons with claims | roc7-order-33c.l4:675 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(4) | o 33 r 38(4) the summons and every affidavit in support are served on any defendant who has filed a notice | roc7-order-33c.l4:694 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(5) | o 33 r 38(5) the Court makes a decree limiting the claimant's liability | roc7-order-33c.l4:729 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(6) | o 33 r 38(6) the Court gives directions for the defendant to obtain information and adjourns | roc7-order-33c.l4:748 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(7) | o 33 r 38(7) the Court gives directions as to the further proceedings | roc7-order-33c.l4:766 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 38(8) | o 33 r 38(8) a defendant who ceases to dispute the right to limit files and serves a notice forthwith | roc7-order-33c.l4:786 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 39(2)(a) | o 33 r 39(2)(a) the claimant advertises the decree in the manner and within the time the decree provides | roc7-order-33c.l4:844 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 39(2)(b) | o 33 r 39(2)(b) the decree fixes a time for notices, claims and summonses | roc7-order-33c.l4:863 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 39(3) | o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers | roc7-order-33c.l4:890 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 39(4) | o 33 r 39(4) the claimant files a copy of each newspaper in which the advertisement appears | roc7-order-33c.l4:922 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 39(5) | o 33 r 39(5) the time allowed is not less than 2 months from the latest date allowed for the advertisements | roc7-order-33c.l4:941 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 40(2) | o 33 r 40(2) the summons is supported by an affidavit showing a bona fide claim and prima facie grounds | roc7-order-33c.l4:1018 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 40(3) | o 33 r 40(3) the summons and every affidavit in support are served on the claimant and any defendant who has filed a notice | roc7-order-33c.l4:1037 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 40(4) | o 33 r 40(4) the Registrar sets the decree aside and gives directions | roc7-order-33c.l4:1072 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 41(1) | o 33 r 41(1) the claiming party files the claim | roc7-order-33c.l4:1095 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 41(1) | o 33 r 41(1) the claiming party serves a copy of the claim on every other party | roc7-order-33c.l4:1114 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 41(2) | o 33 r 41(2) the Registrar gives directions on the application | roc7-order-33c.l4:1177 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 41(3) | o 33 r 41(3) the appointment of the day for the hearing is made in the way required | roc7-order-33c.l4:1199 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 41(5) | o 33 r 41(5) the claiming party or the claimant enters the reference for hearing | roc7-order-33c.l4:1233 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 41(6) | o 33 r 41(6) the claiming party files the list and the affidavits and serves copies | roc7-order-33c.l4:1270 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 42(3) | o 33 r 42(3) the evidence is recorded under Order 15 Rule 11(5), (6) and (7) | roc7-order-33c.l4:1368 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
QB | O 33 r 42(4) | o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice | roc7-order-33c.l4:1393 | NOTHING for the compliance question when the facts do not meet a bare "must" (Order 3, Rule 2(1) and (4)(a)); a consequence of non-compliance stays NOTHING | JUST FALSE (the facts show the requirement was not done)
```

All sites alike, and the same as the other parts of the Rules (Orders 20 to 27 and 34 to 70): the compliance function asks whether what the text requires was done; when the facts say it was not, the answer is NOTHING, with a NOTHING-kind comment naming Order 3, Rule 2(1) (every requirement is subject to the Court's discretion to order otherwise) and saying the text does not itself say no. A consequence of non-compliance stays NOTHING, because no function here derives one. The other reading at each site is JUST FALSE, which would make this row differ from the other parts at the same kind of site.

**QC** (10 sites):

```
QC | O 29 r 6 | o 29 r 6 a place is a specified foreign country | roc7-order-29.l4:79 | JUST FALSE for a thing not on the list: Rule 1 defines the term as one "specified in" this Rule, so the list is the whole class (delegated-definitions ruling (a)) | NOTHING (a bare list is not closed)
QC | O 29 r 7 | o 29 r 7 a court is a specified court | roc7-order-29.l4:94 | JUST FALSE for a court not on the list: Rule 1 defines the term as one "specified in" this Rule, so the list is the whole class (delegated-definitions ruling (a)); the three arms that pair a listed court with another country are also JUST FALSE, because "where the specified foreign country is X" is not met (ruling (b)) | NOTHING (a bare list is not closed; a "where" that fails is silence)
QC | O 29A r 4 | o 29A r 4 a place is a specified foreign country | roc7-order-29.l4:297 | JUST FALSE for a thing not on the list: Rule 1 defines the term as one "specified in" this Rule, so the list is the whole class (delegated-definitions ruling (a)) | NOTHING (a bare list is not closed)
QC | O 29A r 5 | o 29A r 5 a court is a specified court | roc7-order-29.l4:306 | JUST FALSE for a thing not on the list: Rule 1 defines the term as one "specified in" this Rule, so the list is the whole class (delegated-definitions ruling (a)) | NOTHING (a bare list is not closed)
QC | O 32 r 2(2) | o 32 r 2(2) an action may be brought for the determination of the question | roc7-order-32.l4:91 | NOTHING for a thing not on the list: "Without limiting paragraph (1)" says in its own words that the list does not close the class | JUST FALSE (the list is the whole class)
QC | O 32 r 2(3) | o 32 r 2(3) an action may be brought for the relief | roc7-order-32.l4:117 | NOTHING for a thing not on the list: "Without limiting paragraph (1)" says in its own words that the list does not close the class | JUST FALSE (the list is the whole class)
QC | O 33 r 12(2) | o 33 r 12(2) the Sheriff must send the person a copy of the order | roc7-order-33a.l4:1474 | NOTHING for a thing not on the list: the paragraph names the persons to whom the Sheriff must send a copy and does not say that a copy may go to no other | JUST FALSE (the list is the whole class)
QC | O 33 r 22(2) | o 33 r 22(2) the Court may further order | roc7-order-33b.l4:962 | NOTHING for a thing not on the list: a "may" over three orders with no "only" or "no other" | JUST FALSE (the list is the whole class)
QC | O 33 r 37(1) | o 33 r 37(1) the Court may allow the person to constitute a limitation fund in the way | roc7-order-33c.l4:544 | NOTHING for a thing not on the list: a "may" over two ways with no "only" or "in no other way" | JUST FALSE (the list is the whole class)
QC | O 33 r 42(3) | o 33 r 42(3) evidence may be given in the manner | roc7-order-33c.l4:1356 | NOTHING for a thing not on the list: a "may" over three manners with no "only" | JUST FALSE (the list is the whole class)
```

The test I applied: a list is closed where the text defines the term as one "specified in" the list; it is open where the text says "without limiting", or says "may" with no "only".

**QD** (116 sites):

```
QD | O 28 r 7(8)(a) | o 28 r 7(8)(a) the Registrar must refund the amount paid in excess or error | roc7-order-28.l4:555 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 28 r 15(2)(a) | o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way | roc7-order-28.l4:1301 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 28 r 15(2)(b) | o 28 r 15(2)(b) a true and complete electronic image of the original is created | roc7-order-28.l4:1320 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 29 r 2(2) | o 29 r 2(2) the application is made by summons and supported by an affidavit | roc7-order-29.l4:149 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 29 r 4 | o 29 r 4 the order states what it must state | roc7-order-29.l4:196 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 29 r 5(2) | o 29 r 5(2) the originating application or affidavit states what it must state | roc7-order-29.l4:241 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 29A r 2(2) | o 29A r 2(2) the application is made by summons | roc7-order-29.l4:358 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 29A r 3(1) | o 29A r 3(1) the initial request states what it must state | roc7-order-29.l4:386 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 30 r 4(2) | o 30 r 4(2) the Tribunal consists of Judges appointed by the Chief Justice | roc7-order-30.l4:124 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 30 r 5(2) | o 30 r 5(2) the person informs the Tribunal in writing of the intention to be heard | roc7-order-30.l4:177 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 30 r 10 | o 30 r 10 the proceeding is held in open court | roc7-order-30.l4:326 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 31 r 1(2) | o 31 r 1(2) the Case states what it must state | roc7-order-30.l4:440 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 31 r 1(3) | o 31 r 1(3) the Registrar of the Supreme Court lays the Case before a Judge and serves a copy on the Attorney-General | roc7-order-30.l4:459 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 31 r 1(4) | o 31 r 1(4) the Judge deals with the Case as if it were a case in the original jurisdiction | roc7-order-30.l4:477 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 31 r 2(4) | o 31 r 2(4) the judgment of the General Division is in the form of an answer to the question | roc7-order-30.l4:538 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 31 r 2(5) | o 31 r 2(5) the Registrar of the Supreme Court serves notice of the hearing | roc7-order-30.l4:557 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 31 r 4(1) | o 31 r 4(1) the State Court continues and disposes of the proceedings according to law | roc7-order-30.l4:586 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 32 r 3(1) | o 32 r 3(1) all the personal representatives are parties to the action | roc7-order-32.l4:131 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 32 r 3(1) | o 32 r 3(1) a personal representative who does not consent is made a defendant | roc7-order-32.l4:150 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 2(1) | o 33 r 2(1) an action in rem is begun by originating claim in Form 48 | roc7-order-33a.l4:131 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 2(2) | o 33 r 2(2) the originating claim in an Admiralty action in personam is in Form 8 with the words inserted | roc7-order-33a.l4:150 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 2(4) | o 33 r 2(4) the defendant served in Singapore files and serves the notice | roc7-order-33a.l4:177 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 2(5) | o 33 r 2(5) the defendant served out of Singapore files and serves the notice | roc7-order-33a.l4:208 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 2(6) | o 33 r 2(6) the notice is in Form 49 | roc7-order-33a.l4:239 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 4(2) | o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats | roc7-order-33a.l4:399 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 4(6) | o 33 r 4(6) the affidavit states what paragraph (6) requires | roc7-order-33a.l4:509 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 4(7) | o 33 r 4(7) the affidavit states what paragraph (7) requires | roc7-order-33a.l4:540 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 5(1) | o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats | roc7-order-33a.l4:571 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(1) | o 33 r 7(1) the originating claim is served on the property against which the action is brought | roc7-order-33a.l4:664 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(1)(a) | o 33 r 7(1)(a) where the property is freight the originating claim is served on the cargo or the ship | roc7-order-33a.l4:688 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(1)(b) | o 33 r 7(1)(b) where the property has been sold by the Sheriff a sealed copy is filed and served on the Sheriff | roc7-order-33a.l4:710 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(5) | o 33 r 7(5) the Registrar causes a memorandum to be marked on the originating claim | roc7-order-33a.l4:815 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(6) | o 33 r 7(6) the claimant leaves a copy at the Registry and files a request in Form 53 | roc7-order-33a.l4:834 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(6) | o 33 r 7(6) the Sheriff serves the originating claim on the property described in the request | roc7-order-33a.l4:852 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(7) | o 33 r 7(7) the expenses of service are paid to the Sheriff on demand | roc7-order-33a.l4:871 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(8) | o 33 r 7(8) the person effecting service endorses the particulars on the originating claim | roc7-order-33a.l4:890 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(9) | o 33 r 7(9) the Sheriff gives the claimant written notice of the fact and manner of service | roc7-order-33a.l4:916 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(10) | o 33 r 7(10) the claimant serves the originating claim forthwith on the person who entered the caveat | roc7-order-33a.l4:934 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 7(11) | o 33 r 7(11) the amended originating claim is served as required | roc7-order-33a.l4:970 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 9(3) | o 33 r 9(3) the Registrar causes a memorandum to be marked on the warrant | roc7-order-33a.l4:1067 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 9(7) | o 33 r 9(7) the warrant of arrest is served on the property against which it is issued | roc7-order-33a.l4:1119 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 9(8) | o 33 r 9(8) the report of the arrest is made by the person required | roc7-order-33a.l4:1147 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 10(1) | o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy | roc7-order-33a.l4:1190 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 10(2) | o 33 r 10(2) service on landed or transhipped cargo is effected as required | roc7-order-33a.l4:1218 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 11(3) | o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search | roc7-order-33a.l4:1321 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 12(1) | o 33 r 12(1) the Sheriff gives notice of the application to the persons referred to in paragraph (2) | roc7-order-33a.l4:1444 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 12(2) | o 33 r 12(2) the Sheriff must send the person a copy of the order | roc7-order-33a.l4:1474 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 12(3) | o 33 r 12(3) the summons and copies of affidavits are served on the Sheriff and the persons referred to in paragraph (2) | roc7-order-33a.l4:1496 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 12(4) | o 33 r 12(4) the Sheriff sends a copy of the order to all the parties to every action against the property | roc7-order-33a.l4:1517 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 13(1) | o 33 r 13(1) the property is released only under an instrument of release in Form 54 | roc7-order-33a.l4:1537 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 13(4) | o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued | roc7-order-33a.l4:1597 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 13(5) | o 33 r 13(5) the party has done what paragraph (5) requires before the property is released | roc7-order-33a.l4:1623 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 14(1) | o 33 r 14(1) the caveat against release and payment is filed in Form 55 and entered in the record of caveats | roc7-order-33a.l4:1671 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 16(1) | o 33 r 16(1) bail is given by bond in Form 57 entered into before a commissioner for oaths or the Registrar | roc7-order-33a.l4:1744 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 16(2) | o 33 r 16(2) the surety makes an affidavit that the surety is able to pay | roc7-order-33a.l4:1763 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 16(3) | o 33 r 16(3) the affidavit required of a corporation is made by an officer | roc7-order-33a.l4:1797 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 16(4) | o 33 r 16(4) the party giving bail serves a notice of bail and files the bond, the affidavits and the proof of service | roc7-order-33a.l4:1819 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 17(2) | o 33 r 17(2) the application for permission to intervene is made by summons without notice with an affidavit | roc7-order-33a.l4:1877 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 17(3) | o 33 r 17(3) the intervener files and serves a notice of intention to contest or not contest | roc7-order-33a.l4:1895 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 18(2) | o 33 r 18(2) the claimant files a preliminary act | roc7-order-33b.l4:136 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 18(2) | o 33 r 18(2) the defendant files a preliminary act | roc7-order-33b.l4:172 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 18(5) | o 33 r 18(5) the preliminary act is sealed by the Registrar | roc7-order-33b.l4:233 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 18(6) | o 33 r 18(6) the claimant serves notice of filing the claimant's preliminary act | roc7-order-33b.l4:267 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 18(7) | o 33 r 18(7) the defendant serves notice that the defendant has filed a preliminary act | roc7-order-33b.l4:299 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 18(9) | o 33 r 18(9) each party serves a copy of the party's preliminary act on every other party | roc7-order-33b.l4:328 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 19(4) | o 33 r 19(4) the Court orders the claimant's preliminary act to be opened and requires the claimant to satisfy the Court | roc7-order-33b.l4:471 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 20(2) | o 33 r 20(2) the party gives production of electronic track data | roc7-order-33b.l4:564 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 20(3) | o 33 r 20(3) the party allows another party to inspect and copy the electronic track data | roc7-order-33b.l4:612 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 21(4) | o 33 r 21(4) the required exhibit is exhibited in the affidavit verifying the facts | roc7-order-33b.l4:719 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 21(8) | o 33 r 21(8) an application under this Rule is made by summons | roc7-order-33b.l4:794 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 21(9) | o 33 r 21(9) a copy of the summons and the affidavit is served on each person mentioned in Rule 12(2) | roc7-order-33b.l4:837 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 22(3) | o 33 r 22(3) the notice states what it must state | roc7-order-33b.l4:1004 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 22(4) | o 33 r 22(4) the Sheriff lodges in the Registry a copy of each newspaper or publication | roc7-order-33b.l4:1022 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 22(5) | o 33 r 22(5) the Sheriff's expenses of complying with the order are included in the expenses relating to the sale | roc7-order-33b.l4:1040 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 22(6) | o 33 r 22(6) the application to extend the period is made by summons and a copy served on each party | roc7-order-33b.l4:1059 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 23(1) | o 33 r 23(1) the party requesting a commission for appraisement and sale files a commission in Form 58 | roc7-order-33b.l4:1099 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 23(2) | o 33 r 23(2) the commission is executed by the Sheriff | roc7-order-33b.l4:1118 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 23(4) | o 33 r 23(4) the Sheriff pays the gross proceeds into Court and brings the accounts into Court | roc7-order-33b.l4:1150 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 24(1) | o 33 r 24(1) every undertaking under this Order is given in writing to the satisfaction of the Sheriff | roc7-order-33b.l4:1191 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 26(2) | o 33 r 26(2) the order or application under Order 9 Rule 9 determines whether the trial is with assessors | roc7-order-33b.l4:1314 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 27(2) | o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts | roc7-order-33b.l4:1370 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 30(3)(a) | o 33 r 30(3)(a) the party whose witness is to be examined provides a shorthand writer | roc7-order-33c.l4:86 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 30(3)(c) | o 33 r 30(3)(c) the shorthand writer certifies the transcript and the solicitor files it | roc7-order-33c.l4:122 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 30(3)(d) | o 33 r 30(3)(d) the transcript is made available to counsel and any certificate of corrections is filed with it | roc7-order-33c.l4:147 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 32(1) | o 33 r 32(1) the proceedings for the apportionment of salvage are begun in the way required | roc7-order-33c.l4:219 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 32(2) | o 33 r 32(2) the originating application or summons and the supporting affidavit are filed and served | roc7-order-33c.l4:241 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 33(1) | o 33 r 33(1) a summons and the affidavits in support are filed in the Registry | roc7-order-33c.l4:288 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 33(2) | o 33 r 33(2) a copy of the summons and affidavits is served on all the other parties | roc7-order-33c.l4:323 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 36(1) | o 33 r 36(1) the claimant is named in the originating claim by the claimant's name | roc7-order-33c.l4:409 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 36(2) | o 33 r 36(2) the claimant makes one of the persons with claims a defendant | roc7-order-33c.l4:427 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 36(3) | o 33 r 36(3) at least one defendant is named in the originating claim by the defendant's name | roc7-order-33c.l4:457 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 36(4) | o 33 r 36(4) the originating claim is served on one or more of the defendants named by their names | roc7-order-33c.l4:487 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(1) | o 33 r 38(1) the claimant takes out a summons before the Registrar for a decree limiting liability | roc7-order-33c.l4:614 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(2) | o 33 r 38(2) the summons is supported by the affidavits required | roc7-order-33c.l4:651 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(3) | o 33 r 38(3) the affidavit states the names and addresses of the persons with claims | roc7-order-33c.l4:675 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(4) | o 33 r 38(4) the summons and every affidavit in support are served on any defendant who has filed a notice | roc7-order-33c.l4:694 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(5) | o 33 r 38(5) the Court makes a decree limiting the claimant's liability | roc7-order-33c.l4:729 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(6) | o 33 r 38(6) the Court gives directions for the defendant to obtain information and adjourns | roc7-order-33c.l4:748 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(7) | o 33 r 38(7) the Court gives directions as to the further proceedings | roc7-order-33c.l4:766 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 38(8) | o 33 r 38(8) a defendant who ceases to dispute the right to limit files and serves a notice forthwith | roc7-order-33c.l4:786 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 39(2)(a) | o 33 r 39(2)(a) the claimant advertises the decree in the manner and within the time the decree provides | roc7-order-33c.l4:844 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 39(2)(b) | o 33 r 39(2)(b) the decree fixes a time for notices, claims and summonses | roc7-order-33c.l4:863 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 39(3) | o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers | roc7-order-33c.l4:890 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 39(4) | o 33 r 39(4) the claimant files a copy of each newspaper in which the advertisement appears | roc7-order-33c.l4:922 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 39(5) | o 33 r 39(5) the time allowed is not less than 2 months from the latest date allowed for the advertisements | roc7-order-33c.l4:941 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 40(2) | o 33 r 40(2) the summons is supported by an affidavit showing a bona fide claim and prima facie grounds | roc7-order-33c.l4:1018 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 40(3) | o 33 r 40(3) the summons and every affidavit in support are served on the claimant and any defendant who has filed a notice | roc7-order-33c.l4:1037 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 40(4) | o 33 r 40(4) the Registrar sets the decree aside and gives directions | roc7-order-33c.l4:1072 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 41(1) | o 33 r 41(1) the claiming party files the claim | roc7-order-33c.l4:1095 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 41(1) | o 33 r 41(1) the claiming party serves a copy of the claim on every other party | roc7-order-33c.l4:1114 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 41(2) | o 33 r 41(2) the Registrar gives directions on the application | roc7-order-33c.l4:1177 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 41(3) | o 33 r 41(3) the appointment of the day for the hearing is made in the way required | roc7-order-33c.l4:1199 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 41(5) | o 33 r 41(5) the claiming party or the claimant enters the reference for hearing | roc7-order-33c.l4:1233 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 41(6) | o 33 r 41(6) the claiming party files the list and the affidavits and serves copies | roc7-order-33c.l4:1270 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 42(3) | o 33 r 42(3) the evidence is recorded under Order 15 Rule 11(5), (6) and (7) | roc7-order-33c.l4:1368 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
QD | O 33 r 42(4) | o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice | roc7-order-33c.l4:1393 | compliance function NOTHING when the duty does not arise, with the companion "(the duty arises)" JUST FALSE | JUST TRUE ("nothing is unmet"), or JUST FALSE read as "the Rule requires nothing here" with no separate compliance function
```

All sites alike: the text states the duty only for its trigger, so it says nothing of compliance outside it (NOTHING), and the companion answers whether the duty arises (JUST FALSE when the trigger is unmet, by the "where" ruling (b)).

**QE** (10 sites):

```
QE | O 28 r 7(1) | o 28 r 7(1) the fee is payable by the registered user | roc7-order-28.l4:329 | NOTHING for X: the parenthesis limits what the charge, deeming or grant covers and is not inside a "where" or "if" (scope-limit ruling (c)) | JUST FALSE (as "except")
QE | O 28 r 8(7)(a) | o 28 r 8(7)(a) the document is deemed conveyed by the authorised user on behalf and with the authority of the registered user | roc7-order-28.l4:711 | NOTHING for X: the parenthesis limits what the charge, deeming or grant covers and is not inside a "where" or "if" (scope-limit ruling (c)) | JUST FALSE (as "except")
QE | O 28 r 8(7)(b) | o 28 r 8(7)(b) the document is deemed conveyed with the intention of the registered user | roc7-order-28.l4:723 | NOTHING for X: the parenthesis limits what the charge, deeming or grant covers and is not inside a "where" or "if" (scope-limit ruling (c)) | JUST FALSE (as "except")
QE | O 28 r 9(2)(b)(i) | o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user | roc7-order-28.l4:807 | JUST FALSE for X: the parenthesis sits inside a "where" condition that X does not meet (ruling (b)) | NOTHING (a scope limit)
QE | O 28 r 9(2)(b)(ii) | o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user | roc7-order-28.l4:818 | JUST FALSE for X: the parenthesis sits inside a "where" condition that X does not meet (ruling (b)) | NOTHING (a scope limit)
QE | O 28 r 12(8)(a) | o 28 r 12(8)(a) the document is deemed served by the authorised user on behalf and with the authority of the registered user | roc7-order-28.l4:1197 | NOTHING for X: the parenthesis limits what the charge, deeming or grant covers and is not inside a "where" or "if" (scope-limit ruling (c)) | JUST FALSE (as "except")
QE | O 28 r 12(8)(b) | o 28 r 12(8)(b) the document is deemed served with the intention of the registered user | roc7-order-28.l4:1208 | NOTHING for X: the parenthesis limits what the charge, deeming or grant covers and is not inside a "where" or "if" (scope-limit ruling (c)) | JUST FALSE (as "except")
QE | O 33 r 25(1) | o 33 r 25(1) a Rule of Order 14 applies to the Admiralty action | roc7-order-33b.l4:1245 | JUST FALSE for the excepted Rules: "except" says in its own words that they do not apply | NOTHING (X is only taken out of what a grant covers)
QE | O 33 r 26(1) | o 33 r 26(1) Order 9 Rules 8 and 9 apply to the Admiralty action | roc7-order-33b.l4:1302 | NOTHING for X: the parenthesis limits what the charge, deeming or grant covers and is not inside a "where" or "if" (scope-limit ruling (c)) | JUST FALSE (as "except")
QE | O 33 r 35(2) | o 33 r 35(2) a provision of Rule 27 applies to the Admiralty cause or matter | roc7-order-33c.l4:382 | JUST FALSE for the excepted Rules: "except" says in its own words that they do not apply | NOTHING (X is only taken out of what a grant covers)
```

Three kinds of "other than" or "except" arise in this range, and I answered them differently.
A parenthesis that limits what a charge, a deeming or a grant covers, with no "where" or "if" around it (O 28 r 7(1), r 8(7), r 12(8), O 33 r 26(1)), answers NOTHING for X: it is a scope limit under ruling (c).
A parenthesis inside a "where" condition (O 28 r 9(2)(b)(i) and (ii)) answers JUST FALSE for X, because the "where" is not met (ruling (b)).
An "except" that names what does not apply (O 33 r 25(1), "except Rules 3, 4, 5 and 12 of that Order"; O 33 r 35(2), "except paragraph (3) of that Rule") answers JUST FALSE for the excepted thing, because the text says in its own words that it does not apply.
No "other than" or "except" of this range takes X out of a defined class in a "means" or "includes" definition (I searched lines 4194 to 5050 for "other than", "except", "save" and "excluding").
O 33 r 13(3), "(except any defendant who has not filed a notice of intention to contest or not contest)", takes a defendant out of the class of parties whose consent is needed; it is folded into one yes/no input, so no branch answers for X, and it is not listed as a site.

**QF** (a missing event in a ledger): not applicable. This encoding writes no events to a state ledger.

### Forks taken

```
F-28-1 | O 28 r 7(4)(a) "1 May in any year unless sub-paragraphs (b) and (c) apply" | the date function `o 28 r 7(4) the relevant time` takes the way a relevant time arises as an input, so the "(b) and (c)" is never evaluated there. The yes/no twin `o 28 r 7(4) a relevant time arises in this way` has to evaluate it: (i) unless EITHER (b) or (c) applies [taken: a 1 May relevant time is displaced by a first registration in that year or by a deemed pre-1 April 2022 registration]; (ii) unless BOTH apply [the literal "and"; makes (a) displaced only where an entity is at once newly registered and registered before 1 April 2022, which cannot be]; (iii) unless (b), (c) or (d) applies [the text names (b) and (c) only; (d) is worded as a relevant time of its own ("the day on which the Registrar is so informed"), so it is not taken as displacing 1 May] | (i)
F-28-2 | O 28 r 11(3) "deemed ... to have been received on the next working day" | the text gives the day, not the time of day. (i) the next working day from 0 minutes after midnight [taken]; (ii) the same minutes after midnight as the real receipt | (i)
F-28-3 | O 28 r 1 "“deemed” means deemed until the contrary is proved" | (i) the deeming stands (JUST TRUE) until the contrary is proved and ends (JUST FALSE) once it is [taken; the until-bar of the ruling of 2026-11-05 (d)]; (ii) once the contrary is proved the deeming gives no answer (NOTHING) | (i)
F-28-4 | O 28 r 3(1) "must be operated by an electronic filing service provider appointed by the Registrar with the approval of the Chief Justice" | a duty on the Registrar's side, with no stated bearer of a breach; encoded as the compliance question, a bare "must" (QB), answering NOTHING when the appointment or the approval is not shown (O 3 r 2(1): every requirement is subject to the Court's discretion to order otherwise); the other reading is JUST FALSE | NOTHING
F-28-5 | bare "must" with no "if", "only" or "shall not", at every QB site listed under Judgment calls (for example r 6(6), r 8(1), r 8(5), r 14, r 15(2)) | NOTHING for the compliance question when the facts do not meet it [taken, and the same as the other parts of the Rules (Orders 20 to 27 and 34 to 70): O 3 r 2(1) (l.296) subjects "all requirements in these Rules" to the Court's discretion "even if they are expressed using imperative words such as “must”", and r 2(4)(a) lets the Court waive non-compliance, so the text does not itself say no]; the other reading is JUST FALSE (the facts show it was not done), which would make this row answer differently from the rest of the Rules at the same kind of site. O 28 r 14 (no practice direction found) is one such site | NOTHING
F-28-6 | O 28 r 7(1) "other than a service bureau" | (i) NOTHING for a service bureau [taken: a parenthesis that limits a charge is a scope limit, ruling (c); listed under QE]; (ii) JUST FALSE ("except") | (i)
F-28-7 | O 28 r 8(4) "Despite anything in paragraph (1), the Registrar may allow ..." | an exception clause to the bar of paragraph (1)? (i) a grant of power, answering JUST TRUE where the Registrar has allowed [taken]; (ii) a lifted bar that grants nothing, NOTHING (the QA reading I did not take here) | (i)
F-28-8 | O 28 r 8(8), r 9(2)(c), r 12(9) (a) "...or (b) where the person tendering ... is acting as agent for his or her principal" | (i) (a) and (b) both stand where there is an agent [taken: two deemings, each its own function]; (ii) (b) displaces (a) where there is an agent | (i)
F-28-9 | O 28 r 10 the moment | the Moment-valued seam answers only where its twin deeming is JUST TRUE; a Moment cannot carry JUST FALSE (yes/no twin added, assumed, not ruled) | twin
F-28-10 | O 28 r 11(1) "only begins to run from the time that" | the bar of the ruling of 2026-11-05 (d): "time for service cannot yet begin to run" is JUST TRUE before the notification is received and JUST FALSE after; "time for service has begun to run" is JUST FALSE before and JUST TRUE after (the text states the beginning positively, so not NOTHING after) | as stated
F-28-11 | O 28 r 12(1) "If a document — (a) other than a document ... required ... to be served personally; or (b) being such a document ... which the party to be served has agreed may be served using the electronic filing service — is required ... to be served ..., and that person is an authorised user or a registered user or is represented by a solicitor who is ..., such service ... may be effected by using the electronic filing service" | the "If" is either the text's own condition or a limit inside a grant. (i) the text's own condition: a personal-service document with no agreement, and a person served who is neither a user nor represented by one, answer JUST FALSE [taken: the module headers (ruling (b)) read an unmet "if" as the text's no; the sentence has the shape "If A, B may be done", A being a condition of the permission; the same reading as r 8(1) whose companion `o 28 r 8(1) the requirement to use the electronic filing service arises` answers JUST FALSE when the document is not required to be filed]; (ii) a limit on a grant, NOTHING: the text does not forbid service by another route, which other provisions of the Rules govern. r 8(4) is not the same shape ("Despite anything in paragraph (1), the Registrar may allow ..." has no "if"): `o 28 r 8(4) a document may be filed other than using the electronic filing service` stays a grant that answers NOTHING until the Registrar has allowed | (i)
F-28-12 | O 28 r 8(3) "may be done in one of 2 ways — (a) by electronic transmission; or (b) via a service bureau" (A10) | (i) the list closes: a way that is neither answers JUST FALSE [taken: "one of 2 ways" counts the ways, so the number closes the list in the text's own words]; (ii) "may" permits two ways and forbids no other: NOTHING | (i)
F-28-13 | O 28 r 15(3) "if the original paper affidavit subsequently becomes unavailable within 7 years after it was filed, the Court may grant permission" (A5) | (i) the "if" is the condition of the power: an affidavit not unavailable within the 7 years answers JUST FALSE for the Court's permission [taken: ruling (b)]; (ii) the grant is limited by its own wording and the text does not say the Court may never permit the electronic image otherwise: NOTHING. The 7 years of r 15(2)(c) is a duty to retain and is its own function; the 7 years here is the window of the power, and the caller states whether the affidavit became unavailable inside it, as a yes/no | (i)
F-ALL-1 | every period of O 28 r 7(8)(a), O 30 r 5(2) and O 33 (one working day, 2 days, 2 clear days, 3 days, 7, 8, 14, 21, 28 and 75 days, 2 and 3 months, and the validity periods of 6 and 12 months) | PLAN.md would have answered NOTHING outside a period; the brief's periods ruling (a) of 2026-11-05 answers JUST FALSE outside a period the text fixes in its own words. The brief governs over PLAN.md. Taken: JUST FALSE outside the period; NOTHING while the period is still running and the act is not yet done. The last day is an input (`o 3 r 3 the last day for doing the act`), because the Rules of Court count their own periods in Order 3, Rule 3 (another part) | JUST FALSE outside the period [taken]
F-ALL-2 | every duty macro in O 28, O 29, O 30, O 32, O 33 ("must", "shall") | a duty whose trigger is unmet: the compliance function answers NOTHING and a companion "(the duty arises)" answers JUST FALSE (QD, a judgment call kept at every site); a duty whose trigger is met and whose act is not done: NOTHING for the compliance function (QB, a judgment call, the same as the other parts of the Rules, F-28-5) | the two judgment calls QB and QD, listed site by site
F-ALL-3 | every "at least N days before" / "not less than N days before" provision: O 33 r 21(9), r 22(6), r 27(2), r 32(2), r 33(1), r 38(4), r 40(3), r 41(2), r 41(6) (A7) | whether the first day of the period is in time (the Nth day before is in time or is not) is not decided by any function: the last day for doing the act is an input that the caller counts under O 3 r 3(4), or r 3(5) for clear days, and each function answers JUST TRUE on or before it and JUST FALSE after it. The reading that day H minus N is in time and the reading that H minus N minus 1 is the last day differ only in what the caller supplies | the caller's last day
F-ALL-4 | the "limited by its own wording" NOTHING branches, checked against the module headers | the rule applied at each: an "if", "where", "when", "unless" or "upon" that sets a condition of the sentence's own answer is the text's no when unmet (JUST FALSE), and an input that is the exercise of a power or grant, a relative clause that limits what a charge or deeming covers, a discretion formula ("as the Court thinks fit") or a count ("once") stays NOTHING. Six inputs moved to JUST FALSE under it: O 28 r 12(1) (F-28-11), O 28 r 8(8)(b) and r 12(9)(b) (the agent for a principal, "where"), O 32 r 5(2)(b) ("if necessary to prevent proceedings by other creditors"), O 33 r 18(8) ("upon filing ... a consent") and O 33 r 41(2) ("at least 28 days before", a window); one moved to NOTHING, O 33 r 7(11) (F-33-11) | as stated
F-29-1 | O 29 r 1 and O 29A r 1 "specified court", "specified foreign country" | the definitions hand their meaning to the lists in Rules 6 and 7 (O 29) and Rules 4 and 5 (O 29A). (i) the definition says JUST FALSE when no entry of the list holds, and so do the lists, because "specified in Rule N" makes the list the whole class [taken: delegated-definitions ruling (a); the four list functions are QC judgment calls, and the arms of Rule 7 that pair a listed court with the wrong country are JUST FALSE because "where the specified foreign country is ..." is not met, ruling (b)]; (ii) NOTHING because the lists are not closed with "only" | (i)
F-29-2 | O 29A r 4 "the People's Republic of China is a specified foreign country" (A8) | whether Hong Kong or Macao is "within" the People's Republic of China for this list is not answered by the text: Rule 1 defines "foreign country" as "a country or territory outside Singapore" and r 4 names only the People's Republic of China. The function takes the caller's yes/no for "the country is the People's Republic of China" and decides nothing about the special administrative regions: (i) a caller who answers FALSE for Hong Kong or Macao gets JUST FALSE (not on the list) [taken: the list is the whole class, delegated-definitions ruling (a)]; (ii) a caller who answers TRUE gets JUST TRUE. Which answer is right for those territories is for a lawyer | the caller's input
F-32-1 | O 32 r 1 "personal representatives" includes executors, administrators and trustees | "includes" does not close the class: a member answers JUST TRUE, a non-member NOTHING [taken]; JUST FALSE for a non-member would treat "includes" as "means" | NOTHING
F-33-1 | O 33 r 11(1) "(a) leaving a copy with the agent; and (b) transmitting by fax or email" | (i) both (a) and (b) are required [taken: the "and" joins them]; (ii) either suffices | (i)
F-33-2 | O 33 r 6 and r 14(2) "unless it is satisfied that the party had a good and sufficient reason" | a power to order damages (or to discharge the warrant) that the Court has "unless" it is satisfied. (i) when the Court is satisfied the power is not there: JUST FALSE [taken: an "unless" the text introduces, on a power rather than a bar]; (ii) NOTHING (the exception lifts the power and says nothing more) | (i)
F-33-3 | O 33 r 7(3) two deemings of due service (acceptance by the defendant's solicitor; filing of a notice of intention to contest or not contest) | where both occurred, (i) the claim is deemed duly served on the earlier of the two days [taken: once duly served it is not served again]; (ii) on the later; (iii) both days stand and the text does not choose | (i)
F-33-4 | O 33 r 13(3) "if the Court so orders, or ... if all the other parties consent" | where neither limb holds: (i) JUST FALSE [taken: an "if" the text sets, unmet]; (ii) NOTHING, because the paragraph says when a release may be issued and does not say that it may not be issued otherwise | (i)
F-33-5 | O 33 r 21(10) interest "at 5.33% per year" from the date of the originating claim to the date of judgment | the text does not say how a year is counted. (i) simple interest on a 365-day year [taken]; (ii) a 366-day year in a leap year; (iii) compound interest. The rate is a constant of the text (5.33), the Court "may" direct it, so the question of power is separate (POWER function). The text states the rate for a judgment given "under this Rule" and names no figure for any other: `o 33 r 21(10) the interest on the sum` takes `the judgment is given under this Rule` and answers NOTHING outside it (a scope limit with no "only"; an amount cannot carry JUST FALSE), while the yes/no power function answers JUST FALSE outside it ("when giving judgment under this Rule" is a "when" condition, ruling (b)); the other reading is that 5.33% applies to any judgment of the Court in an Admiralty action. The paragraph states no in rem or in personam limit, so none is encoded | (i)
F-33-6 | O 33 r 4(7)(d) | the affidavit that paragraph (7) requires in an action in rem against a ship by virtue of section 4(4) of the High Court (Admiralty Jurisdiction) Act must state (a) to (d), and (d) bites only in a claim for possession or wages; encoded as a condition on that kind of claim [taken]; the alternative is to require (d) of every affidavit under paragraph (7) | conditional on the kind of claim
F-33-7 | O 33 r 16(4) "after the expiration of 24 hours after service of the notice of bail" | the text counts hours, not days; encoded on Moments (a day and minutes after midnight), 24 hours being 1440 minutes [taken]; the alternative is to count one calendar day. `o 33 r 16(4) the earliest moment the bond may be filed without consent` is the same time of day on the next day | 1440 minutes
F-33-8 | O 33 r 2(9), r 9(1), r 15(1) validity of an originating claim for 12 months, a warrant for 12 months, a caveat for 6 months | the last day of validity is an input (`o 3 r 3 the last day of the validity`); valid on or before that day and not valid after it. (i) the last day counts as valid [taken: the validity period runs through its last day]; (ii) the period ends the day before. For r 2(9) ("valid in the first instance for 12 months", "for the purpose of service") the text does not say from what date the 12 months run; the function does not choose, because the last day is an input that the caller counts under O 3 r 3(3) (the period begins immediately after the date, whether that is issue or filing) | (i)
F-33-9 | O 33 r 7(10) and r 38(8) "forthwith" | the text gives no number of days or hours, so there is no period to count: encoded as a bare duty with its companion and no timeliness function [taken]; the alternative is an invented outer limit, which would be a number from nowhere | no period
F-33-10 | O 33 r 21(1) "Where an originating claim is served under Rule 7(8) on a party at whose instance a caveat against arrest was issued" (A2) | the printed cross-reference does not match the text of Rule 7: r 7(8) is the Sheriff's endorsement of service on property, and the rule that has the claimant serve the originating claim on the person at whose instance a caveat was entered is r 7(10). (i) keep the citation as printed in the input name and the seat question, since the function quotes the Rule as it stands [taken]; (ii) rename the input to say what it asks ("served on the caveator under Rule 7(10)"). Which paragraph the drafter meant is for a lawyer; the answers do not depend on it, because the caller states the fact as a yes/no | (i)
F-33-11 | O 33 r 7(11) "may, without permission of the Court, be amended once at any time after service ... where the amendment is solely to delete defendant vessels" (A6) | a second amendment of that kind after service: (i) NOTHING [taken: "once" limits the grant that dispenses with permission and is not a flat negative; the text does not say that a second amendment is barred, only that this paragraph does not dispense with permission for it; the same reading as a scope limit with no "only", ruling (c)]; (ii) JUST FALSE ("once" read as a closed count in the text's own words). The "where the amendment is solely to delete defendant vessels" and "after service" limbs are "where" conditions and answer JUST FALSE when unmet (ruling (b)) | (i)
F-33-12 | O 33 r 19(1) "Where, in an action mentioned in Rule 18(1), the claimant fails to file a preliminary act within the prescribed period, any defendant who has filed such an act may apply ... and the Court may by order dismiss the action or make such other order on such terms as the Court thinks just" (A9) | the two powers are two functions. (i) the defendant's application and the Court's order each carry the "where" conditions (an action mentioned in Rule 18(1), a claimant's failure within the prescribed period, a defendant who has filed such an act, and for the Court's order a defendant's application by summons), JUST FALSE when one is unmet [taken: ruling (b)]; the prescribed period is the one r 19(7) gives, and the caller states whether the claimant failed within it; (ii) "such an act" read as a preliminary act filed in time: the text says "has filed" and not "has filed in time", so the defendant's filing is not tested against the period. The question the reviewer put is whether a defendant that has not filed its own preliminary act may apply to dismiss: the input `the defendant has filed such an act` answers that case JUST FALSE, reading "any defendant who has filed such an act" as a condition of the power (ruling (b)); the other reading is NOTHING, the clause being a relative clause that limits who holds the power, the kind F-ALL-4 leaves at NOTHING | (i)
F-33-13 | O 33 r 18(6) "within 3 days of the service of the notice of intention to contest or not contest or upon filing the claimant's preliminary act, whichever is the later" (A11) | (i) calendar days, with the last day an input counted by the caller under O 3 r 3: a period of 6 days or less excludes non-court days by O 3 r 3(6), so the caller's last day already leaves them out [taken: the Rules' own counting rule does the work]; (ii) "Working days", as O 33 r 9(8) says "one working day" in the text's own words, which are not the same days as non-court days | (i)
F-33-14 | O 33 r 41(1) "must, within 2 months after the order is made, or, in a limitation action, within such other period as the Court may direct, file that party's claim and (unless the reference is in such an action) serve a copy of the claim on every other party" | the filing and the service are two duties with two inputs: `o 33 r 41(1) the claiming party files the claim` (no exception) and `o 33 r 41(1) the claiming party serves a copy of the claim on every other party` (the exception "unless the reference is in such an action" is its own input, so "must I serve copies?" can be asked, with its "(the duty arises)" companion). The other reading is one duty with the exception merged in, which cannot say whether service is owed | two functions
```

## Jural relations (roc7)

Hohfeld's correlatives: a claim of one party is the duty of another; a privilege is the other's no-right; a power is the other's liability; an immunity is the other's disability.
The table has 248 rows, one for each provision label that creates a relation; 119 further provision labels create none (listed under the table).
How the rows were typed: the Order 28 rows by hand, reading each rule.
For Orders 29 to 33 the holder and bearer are read off the encoded function: where its name begins with the acting party or officer and "may" or "must" (for example `the Court may ...`, `the Sheriff must ...`, `the claimant ...`), that actor is the bearer of a duty or the holder of a power or privilege; a procedural duty on a party is shown as owed to "the Court and the other parties" and a duty on an officer as owed to "the parties to the action", which is an inference from the nature of these Orders and not a quotation; where the rule lays a requirement on a document and names no actor, the bearer is shown as "the person who must file, serve or state it (the text names no actor)"; the rows the rule above gave no or a wrong party for were typed by hand, reading the provision; in several of them (for example O 33 r 25(2) and r 37(4), money paid into Court) the text names no holder and I inferred one from the nature of the provision.
Flat negatives are recorded here as immunity / disability or claim / duty and answered JUST FALSE in layer 1 (ruling N2); no SHANT (prohibition) function is derived in this row, so the derivation that N2 allows where the text names the bearer is left to the reader of this table.
The kinds are recorded here only and are not typed into any answer.
All of this is for a lawyer to confirm.


| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| O 28 r 2 | the Registrar (with the Chief Justice's approval) | persons who file or serve documents | power / liability | `o 28 r 2 the Registrar may establish an electronic filing service` |
| O 28 r 3(1) | the Registrar and Chief Justice (appointment) | the provider appointed | power / liability | `o 28 r 3(1) the service is operated by a provider appointed as required` |
| O 28 r 3(2) | the Singapore Academy of Law (superintendence) | the provider | power / liability | `o 28 r 3(2) a body is the superintendent of a provider` |
| O 28 r 5(1) | the Registrar | persons who use a service bureau | power / liability | `o 28 r 5(1) the Registrar may establish or appoint agents to establish a service bureau` |
| O 28 r 5(2) | the appointed agent | the Registrar | immunity / disability | `o 28 r 5(2) an appointed agent is treated as an agent for accepting payment of fees or service charges` |
| O 28 r 5(3) | the Singapore Academy of Law | the appointed agent | power / liability | `o 28 r 5(3) a body is the superintendent of an appointed agent` |
| O 28 r 6(1) | an entity | the Registrar (who must receive the application) | privilege / no-right | `o 28 r 6(1) an entity may apply to be a registered user` |
| O 28 r 6(2) | a registered user | the partner, director, officer or employee designated | power / liability | `o 28 r 6(2) a registered user may designate a person as an authorised user` |
| O 28 r 6(3) | the Registrar | the entity or person | power / liability | `o 28 r 6(3) the Registrar may allow a registered user or an authorised user on terms` |
| O 28 r 6(4) | the entity or person registered under the revoked Rules | the Registrar | immunity / disability | `o 28 r 6(4) the entity or person is deemed registered or designated under this Rule` |
| O 28 r 6(5) | the authorised user | the registered user (bound by the approval) | power / liability | `o 28 r 6(5) the registered user is deemed to approve use of the identification code` |
| O 28 r 6(6) | the Registrar and the provider | the registered user | claim / duty | `o 28 r 6(6) the registered user has met the conditions for using the electronic filing service` |
| O 28 r 6(7) | the Registrar | registered users | power / liability | `o 28 r 6(7) the Registrar may waive paragraph (6)` |
| O 28 r 6(8) | the service bureau and its employees | the Registrar | immunity / disability | `o 28 r 6(8) a service bureau is deemed to be a registered user`; `o 28 r 6(8) an employee of a service bureau is deemed to be an authorised user` |
| O 28 r 7(1) | the Registrar | each registered user other than a service bureau | claim / duty | `o 28 r 7(1) the fee is payable by the registered user`; `o 28 r 7(1) the monthly fee for a registered user`; `o 28 r 7(1) the fee for a number of months or parts of a month` |
| O 28 r 7(3) | the registered user (an entity registered solely for the two applications) | the Registrar | immunity / disability | `o 28 r 7(3) no fee is payable by the registered user` |
| O 28 r 7(5) | the Registrar | the registered user | claim / duty | `o 28 r 7(5) the fee is payable for the month` |
| O 28 r 7(6) | the Registrar | the registered user | claim / duty | `o 28 r 7(6) the day the fee for a month is due and payable`; `o 28 r 7(6) the fee for the month is due and payable on the day` |
| O 28 r 7(7) | the Registrar | registered users | power / liability | `o 28 r 7(7) the Registrar may waive, refund or defer the fee` |
| O 28 r 7(8)(a) | the registered user | the Registrar | claim / duty | `o 28 r 7(8)(a) the Registrar must refund the amount paid in excess or error`; `o 28 r 7(8)(a) the claim is made in writing in time`; `o 28 r 7(8)(a) the act is done by the last day` |
| O 28 r 7(8)(b) | the Registrar | the registered user | power / liability | `o 28 r 7(8)(b) the Registrar may refund in any other case` |
| O 28 r 7(9) | the Registrar | registered users | power / liability | `o 28 r 7(9) the manner of informing the Registrar is set out in practice directions` |
| O 28 r 8(1) | the Registrar | the person who must file, serve or convey | claim / duty | `o 28 r 8(1) the requirement to use the electronic filing service arises`; `o 28 r 8(1) the document is filed using the electronic filing service as required` |
| O 28 r 8(2) | the person filing | the Registrar | privilege / no-right | `o 28 r 8(2) the requirement is satisfied by a single copy filed using the electronic filing service` |
| O 28 r 8(3) | the person filing | the Registrar | privilege / no-right | `o 28 r 8(3) the way of using the electronic filing service is one of the 2 ways` |
| O 28 r 8(4) | the Registrar | the person who must otherwise use the service | power / liability | `o 28 r 8(4) a document may be filed other than using the electronic filing service` |
| O 28 r 8(5) | the Registrar | the person filing | claim / duty | `o 28 r 8(5) the form of the document is as required` |
| O 28 r 8(7) | the registered user | the Registrar (bound by the deeming) | power / liability | `o 28 r 8(7)(a) the document is deemed conveyed by the authorised user on behalf and with the authority of the registered user`; `o 28 r 8(7)(b) the document is deemed conveyed with the intention of the registered user` |
| O 28 r 8(8) | the person tendering (or the principal) | the service bureau | power / liability | `o 28 r 8(8)(a) the document is deemed conveyed on behalf and with the authority of the person tendering it`; `o 28 r 8(8)(b) the document is deemed conveyed on behalf and with the authority of the principal` |
| O 28 r 10(5) | the registered user | the court receiving the evidence | privilege / no-right | `o 28 r 10(5) the registered user may produce a record as evidence of filing or issuance` |
| O 28 r 10(6) | the Registrar | the party relying on the later time | power / liability | `o 28 r 10(6) the Registrar may cause an earlier date and time to be reflected`; `o 28 r 10 the moment the document is deemed filed` |
| O 28 r 11(1) | the party served | the serving party (time does not run) | immunity / disability | `o 28 r 11(1) time for service cannot yet begin to run`; `o 28 r 11(1) time for service has begun to run`; `o 28 r 11 the moment time for service begins to run` |
| O 28 r 11(2) | the party served | the serving party | immunity / disability | `o 28 r 11 the moment time for service begins to run` |
| O 28 r 12(1) | the party serving | the person on whom the document is served | power / liability | `o 28 r 12(1) service may be effected using the electronic filing service` |
| O 28 r 12(2) | the party serving | the party served | power / liability | `o 28 r 12(2) the party is deemed to have agreed to be served using the electronic filing service` |
| O 28 r 12(4) | the person serving | the court | privilege / no-right | `o 28 r 12(4) the person serving may produce a record of service as evidence` |
| O 28 r 12(5) | the person serving | the person served | privilege / no-right | `o 28 r 12(5) the person serving may file a Registrar's certificate of service in lieu of an affidavit`; `o 28 r 12(5) the certificate is regarded as prima facie evidence of service` |
| O 28 r 12(6) | the person serving | those served | power / liability | `o 28 r 12(6) service on more than one person may be effected using the electronic filing service on those who are users` |
| O 28 r 13 | the Registrar | the registered user | power / liability | `o 28 r 13 the Registrar may notify or deliver using the electronic filing service` |
| O 28 r 14 | the Registrar | the party amending | claim / duty | `o 28 r 14 the amendment is effected in the manner prescribed in the practice directions` |
| O 28 r 15(1) | the party filing | other parties and the Court | privilege / no-right | `o 28 r 15(1) the affidavit may be used to the same extent as a paper affidavit` |
| O 28 r 15(2) | the Court | the party filing | claim / duty | `o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way`; `o 28 r 15(2)(b) a true and complete electronic image of the original is created`; `o 28 r 15(2)(c) the original paper affidavit is retained for 7 years` |
| O 28 r 15(3) | the Court | the party | power / liability | `o 28 r 15(3) the Court may permit the electronic image to be used` |
| O 28 r 17(1) | the registered user or authorised user | the other two Registrars | immunity / disability | `o 28 r 17(1) a user registered by the Registrar of the Supreme Court is treated as also registered by the other two Registrars` |
| O 28 r 17(2) | the registered user or authorised user | the other two Registrars | immunity / disability | `o 28 r 17(2) a user registered by the Registrar of the State Courts is treated as also registered by the other two Registrars` |
| O 28 r 17(3) | the registered user or authorised user | the other two Registrars | immunity / disability | `o 28 r 17(3) a user registered by the Registrar of the Family Justice Courts is treated as also registered by the other two Registrars` |
| O 28 r 17(4) | the Registrar of the Supreme Court | users of the service bureau | power / liability | `o 28 r 17(4)(a) a Supreme Court service bureau may be used for State Courts proceedings`; `o 28 r 17(4)(b) a Supreme Court service bureau may be used for Family Justice Courts proceedings` |
| O 28 r 17(5) | the Registrar of the State Courts | users of the service bureau | power / liability | `o 28 r 17(5)(a) a State Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(5)(b) a State Courts service bureau may be used for Family Justice Courts proceedings` |
| O 28 r 17(6) | the Registrar of the Family Justice Courts | users of the service bureau | power / liability | `o 28 r 17(6)(a) a Family Justice Courts service bureau may be used for Supreme Court proceedings`; `o 28 r 17(6)(b) a Family Justice Courts service bureau may be used for State Courts proceedings` |
| O 29 r 2(1) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 29 r 2(1) the Court may order proceedings in a specified court in a specified foreign country` |
| O 29 r 2(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 29 r 2(2) the application is made by summons and supported by an affidavit` |
| O 29 r 2(3) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 29 r 2(3) the Court may give directions for a statement of the issue` |
| O 29 r 3 | the Court | the parties to the proceedings | power / liability | `o 29 r 3 this Order does not prevent the Court ordering proceedings in another foreign country on its own motion` |
| O 29 r 4 | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 29 r 4 the order states what it must state` |
| O 29 r 5(1) | the person who commences the proceedings | the other parties | privilege / no-right | `o 29 r 5(1) proceedings on an issue of Singapore law may be commenced by originating application` |
| O 29 r 5(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 29 r 5(2) the originating application or affidavit states what it must state` |
| O 29A r 2(1) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 29A r 2(1) the Court may transmit a request for an opinion to a specified court` |
| O 29A r 2(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 29A r 2(2) the application is made by summons` |
| O 29A r 3(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 29A r 3(1) the initial request states what it must state` |
| O 29A r 3(2) | the parties to the proceedings | the Court making the request | claim / duty | `o 29A r 3(2) a request may identify the proceedings or the parties` |
| O 30 r 2(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 30 r 2(1) the Reference is brought by filing it in Form 47` |
| O 30 r 2(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 30 r 2(2) the Reference is made under the hand of the President of Singapore` |
| O 30 r 2(3) | the parties to the action | the Registrar | claim / duty | `o 30 r 2(3) the Registrar causes a copy of the Reference to be served on the Attorney-General` |
| O 30 r 3(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 30 r 3(1) the Reference states the questions in a form which can be answered yes or no` |
| O 30 r 3(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 30 r 3(2) the Reference is divided into paragraphs and states what is necessary` |
| O 30 r 5(1) | the Tribunal | the party or person affected by what is allowed or ordered | power / liability | `o 30 r 5(1) the Tribunal may direct that a person interested be notified`; `o 30 r 5(1) a person notified is entitled to be heard` |
| O 30 r 5(2) | the Court and the other parties | the person | claim / duty | `o 30 r 5(2) the person informs the Tribunal in writing of the intention to be heard`; `o 30 r 5(2) the period for informing the Tribunal`; `o 30 r 5(2) duty`; regulative rule `o 30 r 5(2) duty` in roc7-order-duties.l4 |
| O 30 r 6(1) | the parties to the action | the Attorney-General | claim / duty | `o 30 r 6(1) the Attorney-General assists the Tribunal` |
| O 30 r 6(2) | the Presidency | the other parties and the Court | privilege / no-right | `o 30 r 6(2) the Presidency may be represented by counsel the Tribunal appoints` |
| O 30 r 7 | the Tribunal | the party or person affected by what is allowed or ordered | power / liability | `o 30 r 7 the Tribunal may request counsel to argue the case` |
| O 30 r 10 | (the text names no right-holder) | the Tribunal | claim / duty | `o 30 r 10 the requirement to hold the proceeding in open court applies`; `o 30 r 10 the proceeding is held in open court` |
| O 30 r 11 | the parties to the action | the Registrar | claim / duty | `o 30 r 11 the Registrar serves a notice to attend a hearing for directions` |
| O 30 r 12 | the Tribunal | the persons interested in the Reference | power / liability | `o 30 r 12 the directions may include` |
| O 30 r 13(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 30 r 13(1) the report is in the form of an answer to the questions` |
| O 30 r 13(2) | the parties to the action | the Registrar | claim / duty | `o 30 r 13(2) the Registrar delivers the report to the President of Singapore and the Attorney-General` |
| O 30 r 14 | a party to the proceedings | the Tribunal | immunity / disability | `o 30 r 14 a party may be ordered to pay costs` |
| O 30 r 15 | a party to the proceedings | the Registrar | immunity / disability | `o 30 r 15 a fee is payable in respect of the proceedings` |
| O 31 r 1(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 31 r 1(2) the Case states what it must state` |
| O 31 r 1(3) | the parties to the action | the Registrar of the Supreme Court | claim / duty | `o 31 r 1(3) the Registrar of the Supreme Court lays the Case before a Judge and serves a copy on the Attorney-General` |
| O 31 r 1(4) | the parties to the action | a Judge | claim / duty | `o 31 r 1(4) the Judge deals with the Case as if it were a case in the original jurisdiction` |
| O 31 r 2(4) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 31 r 2(4) the judgment of the General Division is in the form of an answer to the question` |
| O 31 r 2(5) | the parties to the action | the Registrar of the Supreme Court | claim / duty | `o 31 r 2(5) the Registrar of the Supreme Court serves notice of the hearing` |
| O 31 r 3 | the parties to the action | the Registrar of the Supreme Court | claim / duty | `o 31 r 3 the Registrar of the Supreme Court delivers a copy of the judgment` |
| O 31 r 4(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 31 r 4(1) the State Court continues and disposes of the proceedings according to law` |
| O 31 r 4(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 31 r 4(2) the State Court determines all questions and makes the orders regarding costs`; `o 31 r 4(2) an order for costs incurred in the General Division may be made` |
| O 32 r 2(1) | the person who may bring the action | the other parties to the action | privilege / no-right | `o 32 r 2(1) an action may be brought for a question or relief which could be had in an administration action`; `o 32 r 2(1) a claim for administration or execution must be made in the action` |
| O 32 r 2(2) | the person who may bring the action | the other parties to the action | privilege / no-right | `o 32 r 2(2) an action may be brought for the determination of the question` |
| O 32 r 2(3) | the person who may bring the action | the other parties to the action | privilege / no-right | `o 32 r 2(3) an action may be brought for the relief` |
| O 32 r 3(1) | the Court and the other parties | the claimant | claim / duty | `o 32 r 3(1) all the personal representatives are parties to the action`; `o 32 r 3(1) a personal representative who does not consent is made a defendant` |
| O 32 r 3(2) | the person with a beneficial interest or claim and the Court | the claimant | claim / duty | `o 32 r 3(2) a person having a beneficial interest or claim must be a party`; `o 32 r 3(2) the claimant may make a person with a beneficial interest or claim a party` |
| O 32 r 3(3) | a party other than the executors or administrators | the Court | claim / duty | `o 32 r 3(3) a party other than the executors or administrators is entitled to appear`; `o 32 r 3(3) the Court may direct or allow another party to appear` |
| O 32 r 4 | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 32 r 4 the Court may grant relief for breach of trust even though the action began by originating application`; `o 32 r 4 the Court may order that the originating application be converted into an originating claim` |
| O 32 r 5(2)(a) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 32 r 5(2)(a) the Court may stay the action and order the personal representatives to provide accounts` |
| O 32 r 5(2)(b) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 32 r 5(2)(b) the Court may give judgment or make an order for administration` |
| O 32 r 6 | the personal representatives | the persons interested in the property sold | power / liability | `o 32 r 6 the personal representatives have the conduct of the sale` |
| O 33 r 2(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 2(1) an action in rem is begun by originating claim in Form 48` |
| O 33 r 2(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 2(2) the originating claim in an Admiralty action in personam is in Form 8 with the words inserted` |
| O 33 r 2(4) | the Court and the other parties | the defendant | claim / duty | `o 33 r 2(4) the defendant served in Singapore files and serves the notice`; `o 33 r 2(4) the period for the notice`; `o 33 r 2(4) duty`; regulative rule `o 33 r 2(4) duty` in roc7-order-duties.l4 |
| O 33 r 2(5) | the Court and the other parties | the defendant | claim / duty | `o 33 r 2(5) the defendant served out of Singapore files and serves the notice`; `o 33 r 2(5) the period for the notice`; `o 33 r 2(5) duty`; regulative rule `o 33 r 2(5) duty` in roc7-order-duties.l4 |
| O 33 r 2(6) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 2(6) the notice is in Form 49` |
| O 33 r 2(7) | the defendant who files and serves the notice | the claimant and the Court | immunity / disability | `o 33 r 2(7) the filing and service of the notice is treated as a submission to jurisdiction or a waiver of any improper service` |
| O 33 r 2(8) | the claimant | the defendant | privilege / no-right | `o 33 r 2(8) the claimant may apply for judgment in Form 50` |
| O 33 r 4(1) | the claimant | the other parties and the Court | privilege / no-right | `o 33 r 4(1) the claimant or defendant may apply for a warrant of arrest` |
| O 33 r 4(2) | the Court and the other parties | the party | claim / duty | `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats` |
| O 33 r 4(3) | the person whose property is to be arrested | the Court or Registrar that issues the warrant | immunity / disability | `o 33 r 4(3) the warrant of arrest cannot yet be issued for want of the affidavit`; `o 33 r 4(3) the Court may allow the warrant to issue although the affidavit lacks particulars`; `o 33 r 4(3) a warrant of arrest may be issued` |
| O 33 r 4(4) | the foreign ship concerned and its owner | the Court or Registrar that issues the warrant | immunity / disability | `o 33 r 4(4) the warrant of arrest cannot yet be issued for want of notice to the consul`; `o 33 r 4(4) a warrant of arrest may be issued against the foreign ship` |
| O 33 r 4(6) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 4(6) the affidavit states what paragraph (6) requires` |
| O 33 r 4(7) | the Court | the party applying for a warrant | claim / duty | `o 33 r 4(7) the affidavit states what paragraph (7) requires` |
| O 33 r 5(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats` |
| O 33 r 5(2) | the person at whose instance the caveat against arrest was entered | the Court or Registrar that would issue a warrant | immunity / disability | `o 33 r 5(2) a caveat against arrest in force prevents the issue of a warrant to arrest the property` |
| O 33 r 6 | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 6 the Court may discharge the warrant`; `o 33 r 6 the Court may order the party procuring the arrest to pay damages` |
| O 33 r 7(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 7(1) the originating claim is served on the property against which the action is brought` |
| O 33 r 7(1)(a) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 7(1)(a) where the property is freight the originating claim is served on the cargo or the ship` |
| O 33 r 7(1)(b) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 7(1)(b) where the property has been sold by the Sheriff a sealed copy is filed and served on the Sheriff`; `o 33 r 7(1)(b) the originating claim may be served on the property sold by the Sheriff`; `o 33 r 7(1)(b) the originating claim is deemed served on the day the copy was filed` |
| O 33 r 7(4) | the Sheriff, or a solicitor or clerk notified to the Registrar | the owner of the property served | power / liability | `o 33 r 7(4) service on the property may be effected by the Sheriff or a notified solicitor or clerk` |
| O 33 r 7(5) | the Registrar | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 7(5) the Registrar may allow service to be effected by any other named person`; `o 33 r 7(5) the Registrar causes a memorandum to be marked on the originating claim` |
| O 33 r 7(6) | the Court and the other parties | the claimant | claim / duty | `o 33 r 7(6) the claimant leaves a copy at the Registry and files a request in Form 53`; `o 33 r 7(6) the Sheriff serves the originating claim on the property described in the request` |
| O 33 r 7(7) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 7(7) the expenses of service are paid to the Sheriff on demand` |
| O 33 r 7(8) | the Court and the other parties | the person | claim / duty | `o 33 r 7(8) the person effecting service endorses the particulars on the originating claim`; `o 33 r 7(8) the endorsement is evidence of the facts stated in it` |
| O 33 r 7(9) | the parties to the action | the Sheriff | claim / duty | `o 33 r 7(9) the Sheriff gives the claimant written notice of the fact and manner of service` |
| O 33 r 7(10) | the Court and the other parties | the claimant | claim / duty | `o 33 r 7(10) the claimant serves the originating claim forthwith on the person who entered the caveat` |
| O 33 r 7(11) | the claimant | the interveners and the defendants who have filed a notice | privilege / no-right | `o 33 r 7(11) the originating claim may be amended once without permission to delete defendant vessels`; `o 33 r 7(11) the amended originating claim is served as required` |
| O 33 r 7(12) | the Court | the party amending the originating claim | claim / duty | `o 33 r 7(12) permission of the Court is required for the amendment` |
| O 33 r 8 | the Court | the solicitor who failed to comply with an undertaking | power / liability | `o 33 r 8 the solicitor is liable to committal` |
| O 33 r 9(2) | the Sheriff, or a solicitor or clerk notified to the Registrar | the owner of the property arrested | power / liability | `o 33 r 9(2) the warrant may be executed by the Sheriff or a notified solicitor or clerk` |
| O 33 r 9(3) | the Registrar | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 9(3) the Registrar may allow the warrant to be executed by any other named person`; `o 33 r 9(3) the Registrar causes a memorandum to be marked on the warrant` |
| O 33 r 9(4) | the Sheriff | the solicitor or party who must give the undertaking | claim / duty | `o 33 r 9(4) the warrant of arrest cannot yet be executed by the Sheriff for want of the undertaking` |
| O 33 r 9(5) | the party at whose instance the warrant was issued | the Sheriff | claim / duty | `o 33 r 9(5) the warrant of arrest may be executed` |
| O 33 r 9(6) | the Sheriff | the owner of the cargo or the ship | power / liability | `o 33 r 9(6) a warrant issued against freight may be executed by serving it on the cargo or the ship or both` |
| O 33 r 9(7) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 9(7) the warrant of arrest is served on the property against which it is issued` |
| O 33 r 9(8) | the Court | the person required by the Rule to report the arrest | claim / duty | `o 33 r 9(8) the report of the arrest is made by the person required`; `o 33 r 9(8) the period for the report of the arrest` |
| O 33 r 10(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy` |
| O 33 r 10(2) | the Court and the other parties | the person effecting service | claim / duty | `o 33 r 10(2) service on landed or transhipped cargo is effected as required` |
| O 33 r 11(1) | the person serving | the agent of the ship | privilege / no-right | `o 33 r 11(1) service may be effected on the agent of the ship during the relevant period` |
| O 33 r 11(3) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search` |
| O 33 r 11(4)(a) | the claimant | the defendant | privilege / no-right | `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars`; `o 33 r 11(4)(a) the period for the memorandum of service` |
| O 33 r 12(1) | the Sheriff | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 12(1) the Sheriff may apply to the Court for directions`; `o 33 r 12(1) the Sheriff gives notice of the application to the persons referred to in paragraph (2)` |
| O 33 r 12(2) | each person referred to in paragraph (2) | the Sheriff | claim / duty | `o 33 r 12(2) the Sheriff must send the person a copy of the order` |
| O 33 r 12(3) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 12(3) the summons and copies of affidavits are served on the Sheriff and the persons referred to in paragraph (2)` |
| O 33 r 12(4) | the parties to the action | the Sheriff | claim / duty | `o 33 r 12(4) the Sheriff sends a copy of the order to all the parties to every action against the property` |
| O 33 r 13(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 13(1) the property is released only under an instrument of release in Form 54` |
| O 33 r 13(2) | the person at whose instance a caveat against release is in force | the Registry that issues the release | immunity / disability | `o 33 r 13(2) a release may be issued` |
| O 33 r 13(3) | a party to the action in which the warrant of arrest was issued | the other parties to the action | power / liability | `o 33 r 13(3) a release may be issued on the application` |
| O 33 r 13(4) | the Sheriff | the applicant for the release | claim / duty | `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued` |
| O 33 r 13(5) | the Sheriff | the party seeking the release of the property | claim / duty | `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released` |
| O 33 r 13(6) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 13(6) the Court may vary or revoke the Sheriff's directions` |
| O 33 r 14(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 14(1) the caveat against release and payment is filed in Form 55 and entered in the record of caveats` |
| O 33 r 14(2) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 14(2) the Court may order the person who procured the caveat to pay damages` |
| O 33 r 15(2) | the person affected by the caveat | the person at whose instance the caveat was entered (no power to extend its validity) | immunity / disability | `o 33 r 15(2) the period of validity of a caveat may be extended`; `o 33 r 15(2) the bar on extension prevents the entry of successive caveats` |
| O 33 r 16(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 16(1) bail is given by bond in Form 57 entered into before a commissioner for oaths or the Registrar` |
| O 33 r 16(2) | the Court and the other parties | the surety | claim / duty | `o 33 r 16(2) the surety makes an affidavit that the surety is able to pay` |
| O 33 r 16(3) | the Court and the other parties | the corporation that is a surety | claim / duty | `o 33 r 16(3) an affidavit is to be made on behalf of the corporation`; `o 33 r 16(3) the affidavit required of a corporation is made by an officer` |
| O 33 r 16(4) | the Court and the other parties | the party | claim / duty | `o 33 r 16(4) the party giving bail serves a notice of bail and files the bond, the affidavits and the proof of service`; `o 33 r 16(4) the bond may be filed at the moment`; `o 33 r 16(4) the earliest moment the bond may be filed without consent` |
| O 33 r 17(1) | the person | the other parties and the Court | privilege / no-right | `o 33 r 17(1) a person with an interest may intervene with the permission of the Court` |
| O 33 r 17(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 17(2) the application for permission to intervene is made by summons without notice with an affidavit` |
| O 33 r 17(3) | the Court and the other parties | the intervener | claim / duty | `o 33 r 17(3) the intervener files and serves a notice of intention to contest or not contest`; `o 33 r 17(3) Rule 2(3) to (6) applies to the intervener's notice with the necessary modifications` |
| O 33 r 17(4) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 17(4) the Court may order the intervener to serve a pleading` |
| O 33 r 18(4) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 18(4) the Court may order that Part Two need not be filed` |
| O 33 r 18(5) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 18(5) the preliminary act is sealed by the Registrar`; `o 33 r 18(5) a preliminary act may be inspected` |
| O 33 r 18(6) | the Court and the other parties | the claimant | claim / duty | `o 33 r 18(6) the claimant serves notice of filing the claimant's preliminary act`; `o 33 r 18(6) the period for the notice of filing` |
| O 33 r 18(7) | the Court and the other parties | the defendant | claim / duty | `o 33 r 18(7) the defendant serves notice that the defendant has filed a preliminary act` |
| O 33 r 18(8) | the party | the other parties and the Court | privilege / no-right | `o 33 r 18(8) a party may inspect and bespeak a copy of another party's preliminary act` |
| O 33 r 18(9) | the Court and the other parties | each party | claim / duty | `o 33 r 18(9) each party serves a copy of the party's preliminary act on every other party`; `o 33 r 18(9) the period for serving the copy`; `o 33 r 18(9) duty`; regulative rule `o 33 r 18(9) duty` in roc7-order-duties.l4 |
| O 33 r 18(10) | the party | the other parties and the Court | privilege / no-right | `o 33 r 18(10) a party may apply for an order for particulars of damages and assessment` |
| O 33 r 19(1) | the defendant | the other parties and the Court | privilege / no-right | `o 33 r 19(1) a defendant who has filed a preliminary act may apply for the action to be dismissed`; `o 33 r 19(1) the Court may dismiss the action or make such other order` |
| O 33 r 19(2) | the claimant | the other parties and the Court | privilege / no-right | `o 33 r 19(2) the claimant may enter judgment against a defendant in default in an action in personam` |
| O 33 r 19(3) | the claimant | the other parties and the Court | privilege / no-right | `o 33 r 19(3) the claimant may apply by summons for judgment against a defendant in default in an action in rem`; `o 33 r 19(3) the claimant must file or serve a statement of claim or an affidavit before the hearing of the summons` |
| O 33 r 19(4) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 19(4) the Court may make such order as it thinks just on the hearing of the summons`; `o 33 r 19(4) the Court orders the claimant's preliminary act to be opened and requires the claimant to satisfy the Court`; `o 33 r 19(4) the claimant's evidence may be given by affidavit` |
| O 33 r 19(5) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 19(5) the Court may give judgment for the claim with or without a reference to the Registrar`; `o 33 r 19(5) the Court may order the property to be appraised and sold and the proceeds paid into Court` |
| O 33 r 19(6) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 19(6) the Court may set aside a judgment entered in pursuance of this Rule` |
| O 33 r 20(1) | the claimant | the defendant | privilege / no-right | `o 33 r 20(1) the claimant may serve a reply or a defence to counterclaim on the defendant` |
| O 33 r 20(2) | the Court and the other parties | the party | claim / duty | `o 33 r 20(2) the party gives production of electronic track data` |
| O 33 r 20(3) | the Court and the other parties | the party | claim / duty | `o 33 r 20(3) the party allows another party to inspect and copy the electronic track data`; `o 33 r 20(3) the period for allowing inspection`; `o 33 r 20(3) duty`; regulative rule `o 33 r 20(3) duty` in roc7-order-duties.l4 |
| O 33 r 21(1) | the claimant | the other parties and the Court | privilege / no-right | `o 33 r 21(1) the claimant may apply for judgment by default against the party who gave a caveat undertaking` |
| O 33 r 21(3) | the claimant | the defendant in default | privilege / no-right | `o 33 r 21(3) the claimant may apply to the Court for judgment by default` |
| O 33 r 21(4) | the Court | the claimant | claim / duty | `o 33 r 21(4) an affidavit proving due service of the originating claim must be filed under paragraph (3)`; `o 33 r 21(4) the required exhibit is exhibited in the affidavit verifying the facts` |
| O 33 r 21(5) | the claimant | the defendant in default | privilege / no-right | `o 33 r 21(5) the claimant may apply to the Court for judgment by default against a defendant who served no defence` |
| O 33 r 21(6) | the defendant making the counterclaim | the claimant in default | privilege / no-right | `o 33 r 21(6) the defendant making the counterclaim may apply to the Court for judgment by default` |
| O 33 r 21(7) | the claimant in an action mentioned in Rule 3(1) | the defendant making the counterclaim | immunity / disability | `o 33 r 21(7) an application may be made under paragraph (6) against the claimant` |
| O 33 r 21(8) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 21(8) an application under this Rule is made by summons`; `o 33 r 21(8) the Court may give judgment for the claim with or without a reference to the Registrar`; `o 33 r 21(8) the Court may order the property to be appraised and sold or make such other order` |
| O 33 r 21(9) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 21(9) a copy of the summons and the affidavit is served on each person mentioned in Rule 12(2)`; `o 33 r 21(9) the period before the hearing` |
| O 33 r 21(12) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 21(12) the Court may set aside or vary a judgment entered pursuant to this Rule` |
| O 33 r 22(1) | the party | the other parties to the action | privilege / no-right | `o 33 r 22(1) the party may apply for an order determining the order of priority` |
| O 33 r 22(2) | the Court | the parties and the persons with claims | power / liability | `o 33 r 22(2) the Court may further order` |
| O 33 r 22(3) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 22(3) the notice states what it must state` |
| O 33 r 22(4) | the parties to the action | the Sheriff | claim / duty | `o 33 r 22(4) the Sheriff lodges in the Registry a copy of each newspaper or publication` |
| O 33 r 22(5) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 22(5) the Sheriff's expenses of complying with the order are included in the expenses relating to the sale` |
| O 33 r 22(6) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 22(6) the application to extend the period is made by summons and a copy served on each party`; `o 33 r 22(6) the period before the hearing` |
| O 33 r 23(1) | the Court and the other parties | the party | claim / duty | `o 33 r 23(1) the party requesting a commission for appraisement and sale files a commission in Form 58` |
| O 33 r 23(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 23(2) the commission is executed by the Sheriff` |
| O 33 r 23(3) | the Sheriff | the party requesting the commission | claim / duty | `o 33 r 23(3) the commission for appraisement and sale cannot yet be executed for want of the undertaking` |
| O 33 r 23(4) | the parties to the action | the Sheriff | claim / duty | `o 33 r 23(4) the Sheriff pays the gross proceeds into Court and brings the accounts into Court` |
| O 33 r 23(5) | a person interested in the proceeds of the sale | the Registrar | claim / duty | `o 33 r 23(5) a person interested in the proceeds of the sale is entitled to be heard on the assessment`; `o 33 r 23(5) a decision of the Registrar on the assessment may be reviewed` |
| O 33 r 24(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 24(1) every undertaking under this Order is given in writing to the satisfaction of the Sheriff` |
| O 33 r 24(2) | the Sheriff | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 24(2) the Sheriff may accept a deposit instead of an undertaking` |
| O 33 r 24(3) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 24(3) the Court may vary or revoke a direction or determination of the Sheriff` |
| O 33 r 25(2) | the persons interested in the money paid into Court | whoever holds the money in Court | immunity / disability | `o 33 r 25(2) the money paid into Court may be paid out` |
| O 33 r 25(3) | the Registrar | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 25(3) the Registrar may order the money to be paid out with the consent of the interested parties` |
| O 33 r 25(4) | the Registrar | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 25(4) the Registrar may order the money paid into Court under Order 13 Rule 8 to be paid out` |
| O 33 r 26(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 26(2) the order or application under Order 9 Rule 9 determines whether the trial is with assessors` |
| O 33 r 26(3) | the Court | the parties | power / liability | `o 33 r 26(3) an order or direction may limit the witnesses who may be called at the trial` |
| O 33 r 26(4) | the Court | the parties | power / liability | `o 33 r 26(4) an order or direction mentioned in paragraphs (2) and (3) may be varied or revoked` |
| O 33 r 27(2) | the Court and the other parties | the party | claim / duty | `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts`; `o 33 r 27(2) the period before the trial` |
| O 33 r 28 | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 28 the Court may stay proceedings in the firstmentioned action until security is given` |
| O 33 r 29 | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 29 the Court may order the inspection of a ship or other property` |
| O 33 r 30(3)(a) | the Court and the other parties | the party | claim / duty | `o 33 r 30(3)(a) the party whose witness is to be examined provides a shorthand writer` |
| O 33 r 30(3)(c) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 30(3)(c) the shorthand writer certifies the transcript and the solicitor files it` |
| O 33 r 30(3)(d) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 30(3)(d) the transcript is made available to counsel and any certificate of corrections is filed with it` |
| O 33 r 30(4) | the Court | the party seeking the order | claim / duty | `o 33 r 30(4) an order authorising an examination of a witness cannot yet be made for want of the preliminary acts`; `o 33 r 30(4) an order may be made under Order 9 Rule 24 authorising an examination of a witness` |
| O 33 r 32(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 32(2) the originating application or summons and the supporting affidavit are filed and served`; `o 33 r 32(2) the period before the hearing` |
| O 33 r 32(3) | a Judge | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 32(3) the Judge may exercise the powers conferred by section 175 of the Merchant Shipping Act` |
| O 33 r 33(1) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 33(1) a summons and the affidavits in support are filed in the Registry`; `o 33 r 33(1) the period before the hearing` |
| O 33 r 33(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 33(2) a copy of the summons and affidavits is served on all the other parties` |
| O 33 r 34 | the Registrar | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 34 the Registrar may allow an agreement between solicitors to be filed`; `o 33 r 34 the filed agreement becomes an order of court` |
| O 33 r 36(2) | the Court and the other parties | the claimant | claim / duty | `o 33 r 36(2) the claimant makes one of the persons with claims a defendant`; `o 33 r 36(2) the claimant may make all or any of the others defendants also` |
| O 33 r 36(3) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 36(3) at least one defendant is named in the originating claim by the defendant's name`; `o 33 r 36(3) the other defendants may be described generally` |
| O 33 r 36(4) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 36(4) the originating claim is served on one or more of the defendants named by their names`; `o 33 r 36(4) the originating claim must be served on a defendant not named by name` |
| O 33 r 37(4) | the persons interested in the money paid into Court | whoever holds the money in Court | immunity / disability | `o 33 r 37(4) the money paid into Court under paragraph (1) may be paid out` |
| O 33 r 38(1) | the Court and the other parties | the claimant | claim / duty | `o 33 r 38(1) the claimant takes out a summons before the Registrar for a decree limiting liability`; `o 33 r 38(1) the period for the summons` |
| O 33 r 38(3) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims` |
| O 33 r 38(4) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 38(4) the summons and every affidavit in support are served on any defendant who has filed a notice`; `o 33 r 38(4) the period before the hearing` |
| O 33 r 38(5) | the parties to the action | the Court | claim / duty | `o 33 r 38(5) the Court makes a decree limiting the claimant's liability` |
| O 33 r 38(6) | the parties to the action | the Court | claim / duty | `o 33 r 38(6) the Court gives directions for the defendant to obtain information and adjourns` |
| O 33 r 38(7) | the parties to the action | the Court | claim / duty | `o 33 r 38(7) the Court gives directions as to the further proceedings` |
| O 33 r 38(8) | the Court and the other parties | the defendant | claim / duty | `o 33 r 38(8) a defendant who ceases to dispute the right to limit files and serves a notice forthwith` |
| O 33 r 38(9) | the claimant | the other parties and the Court | privilege / no-right | `o 33 r 38(9) the claimant may take out a summons before the Court for a decree` |
| O 33 r 39(1)(a) | the claimant | the persons with claims against the claimant (no right to have the decree advertised) | privilege / no-right | `o 33 r 39(1)(a) the decree must be advertised` |
| O 33 r 39(2)(a) | the Court and the other parties | the claimant | claim / duty | `o 33 r 39(2)(a) the claimant advertises the decree in the manner and within the time the decree provides` |
| O 33 r 39(2)(b) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 39(2)(b) the decree fixes a time for notices, claims and summonses` |
| O 33 r 39(3) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers` |
| O 33 r 39(5) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 39(5) the time allowed is not less than 2 months from the latest date allowed for the advertisements`; `o 33 r 39(5) the step may be taken after the time allowed has expired` |
| O 33 r 40(1) | the person | the other parties and the Court | privilege / no-right | `o 33 r 40(1) a person with a claim may take out a summons to set the decree aside`; `o 33 r 40(1) the person takes out the summons within the time fixed by the decree` |
| O 33 r 40(2) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 40(2) the summons is supported by an affidavit showing a bona fide claim and prima facie grounds` |
| O 33 r 40(3) | the Court and the other parties | the person who must file, serve or state it (the text names no actor) | claim / duty | `o 33 r 40(3) the summons and every affidavit in support are served on the claimant and any defendant who has filed a notice`; `o 33 r 40(3) the period before the hearing` |
| O 33 r 40(4) | the parties to the action | the Registrar | claim / duty | `o 33 r 40(4) the Registrar sets the decree aside and gives directions` |
| O 33 r 41(1) | the Court and the other parties | the claiming party | claim / duty | `o 33 r 41(1) the claiming party files the claim`; `o 33 r 41(1) the claiming party serves a copy of the claim on every other party`; `o 33 r 41(1) the period for filing the claim` |
| O 33 r 41(2) | the party | the other parties and the Court | privilege / no-right | `o 33 r 41(2) a party may apply to the Registrar under Order 9 Rule 9 as to the proceedings on the reference`; `o 33 r 41(2) the period before the hearing`; `o 33 r 41(2) the Registrar gives directions on the application` |
| O 33 r 41(5) | the Court and the other parties | the claiming party | claim / duty | `o 33 r 41(5) the claiming party or the claimant enters the reference for hearing`; `o 33 r 41(5) the period for lodging the Request`; `o 33 r 41(5) duty`; regulative rule `o 33 r 41(5) duty` in roc7-order-duties.l4 |
| O 33 r 41(6) | the Court and the other parties | the claiming party | claim / duty | `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies`; `o 33 r 41(6) the period before the hearing` |
| O 33 r 41(7) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 41(7) the Court may dismiss the claim` |
| O 33 r 42(1) | the Registrar | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 42(1) the Registrar may adjourn the hearing of a reference` |
| O 33 r 42(2) | the Registrar | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 42(2) the Registrar may give a direction limiting the witnesses`; `o 33 r 42(2) the direction may be revoked or varied on sufficient cause` |
| O 33 r 42(4) | the parties to the action | the Registrar | claim / duty | `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice` |
| O 33 r 42(5) | the party | the other parties and the Court | privilege / no-right | `o 33 r 42(5) a party may request a statement of the grounds of the decision`; `o 33 r 42(5) the period for the request` |
| O 33 r 43(1) | the party | the other parties and the Court | privilege / no-right | `o 33 r 43(1) a party to a reference may apply to a Judge to set aside or vary the decision` |
| O 33 r 43(3) | the parties | the Registrar or Judge giving the direction | claim / duty | `o 33 r 43(3) a direction may be given under paragraph (2) without the parties being given an opportunity of being heard`; `o 33 r 43(3) the direction may be incorporated in the Registrar's decision` |
| O 33 r 45 | a shipowner or other person relying on the Merchant Shipping Act by way of defence | the claimant | immunity / disability | `o 33 r 45 Rules 35 to 40 limit the right to rely by way of defence on the Merchant Shipping Act` |
| O 33 r 46(1) | the Court | the party or person affected by what is allowed or ordered | power / liability | `o 33 r 46(1) the Court may order the production of documents in a marine insurance action` |

Provisions that create no relation (definitions, counting rules, scopes, deemings, forms and lists), listed once: O 28 r 1, O 28 r 4, O 28 r 7(2), O 28 r 7(4), O 28 r 8(6), O 28 r 8(9), O 28 r 9(1), O 28 r 9(2), O 28 r 9(3), O 28 r 9(4), O 28 r 10(1), O 28 r 10(2), O 28 r 10(3), O 28 r 10(4), O 28 r 11(3), O 28 r 12(3), O 28 r 12(7), O 28 r 12(8), O 28 r 12(9), O 28 r 12(10), O 28 r 12(11), O 28 r 16, O 29 r 1, O 29 r 6, O 29 r 7, O 29A r 1, O 29A r 4, O 29A r 5, O 30 r 1(1), O 30 r 1(2), O 30 r 4(1), O 30 r 4(2), O 30 r 4(3), O 30 r 8(1), O 30 r 8(2), O 30 r 8(3), O 30 r 8(4), O 30 r 9, O 31 r 1(1), O 31 r 2(1), O 31 r 2(2), O 31 r 2(3), O 32 r 1, O 32 r 5(1), O 33 r 1(1), O 33 r 1(2), O 33 r 1(3), O 33 r 2(3), O 33 r 2(9), O 33 r 2(10), O 33 r 3(1), O 33 r 3(2), O 33 r 3(3), O 33 r 3(4), O 33 r 3(5), O 33 r 4, O 33 r 4(5), O 33 r 5, O 33 r 5(1)(b), O 33 r 7(2), O 33 r 7(3), O 33 r 7(3)(a), O 33 r 7(3)(b), O 33 r 9(1), O 33 r 11(2)(a), O 33 r 11(2)(b), O 33 r 11(4), O 33 r 11(5), O 33 r 13, O 33 r 15(1), O 33 r 18(1), O 33 r 18(2), O 33 r 18(3), O 33 r 18(11), O 33 r 19(7), O 33 r 20(2)(a), O 33 r 20(2)(b), O 33 r 21(1)(b), O 33 r 21(2), O 33 r 21(10), O 33 r 21(11), O 33 r 21(13), O 33 r 22(2)(a), O 33 r 22(2)(c), O 33 r 22(7), O 33 r 25(1), O 33 r 26(1), O 33 r 27(1), O 33 r 27(3), O 33 r 30(1), O 33 r 30(2), O 33 r 30(3), O 33 r 30(3)(b), O 33 r 30(5), O 33 r 31, O 33 r 32(1), O 33 r 33(3), O 33 r 35(1), O 33 r 35(2), O 33 r 36(1), O 33 r 36(5), O 33 r 37(1), O 33 r 37(2), O 33 r 37(3), O 33 r 37(3)(a), O 33 r 37(3)(b), O 33 r 38(2), O 33 r 39(1)(b), O 33 r 39(4), O 33 r 39(6), O 33 r 41(3), O 33 r 41(4), O 33 r 42, O 33 r 42(3), O 33 r 43(1)(a), O 33 r 43(1)(b), O 33 r 43(2), O 33 r 44, O 33 r 46(2).

## Marginal readings for a lawyer (roc7)

The brief names two readings that are for a lawyer, not for me, and asks that every branch resting on one be listed with the other reading stated:
(a) a failed "if" (and "where", "when", "unless") counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and a flat negative counts as the text saying no;
(b) a prohibition or grant limited by its own wording does not (the case outside the limit answers NOTHING);
(c) added by the judgment calls of 2026-11-05 and aligned with the other parts of the Rules at the review round (see Judgment calls, QB): a requirement the text states with a bare "must", where the facts show it was not done, answers NOTHING for the compliance question, because Order 3, Rule 2(1) makes "all requirements in these Rules" subject to "the Court’s discretion to order otherwise in the interests of justice, even if they are expressed using imperative words such as “must”, “is to” or “shall”", and Order 3, Rule 2(4)(a) lets the Court "waive the non‑compliance of the Rule", so the text does not itself say that a requirement not met means "no".
The other reading of (a): a failed "if" is silence and answers NOTHING.
The other reading of (b): the limit is itself a no and answers JUST FALSE.
The other reading of (c): the facts show the requirement was not done, so the compliance question answers JUST FALSE (the answer follows from the facts, not from a negative the text states).
Every branch that answers JUST FALSE carries a comment `FALSE-kind (...)` and rests on (a), on a period fixed in the text's own words (the periods ruling), or on a definition that hands its meaning to a list (delegated-definitions ruling (a)); every branch that answers NOTHING because the text limits itself carries `NOTHING-kind (limited by its own wording)` and rests on (b); every branch that answers NOTHING because a requirement was not met carries `NOTHING-kind (a requirement not met; ...)` and rests on (c).
I assigned the class from the kind of comment on the branch, not by re-reading each branch, so the lawyer should read the quoted words in the comment.


| module | functions with a FALSE-kind branch | FALSE-kind branches (reading a) | functions with a NOTHING-kind (limited by its own wording) branch | such branches (reading b) | functions with a requirement-not-met branch | such branches (reading c) |
| --- | --- | --- | --- | --- | --- | --- |
| roc7-order-28.l4 | 50 | 52 | 48 | 48 | 8 | 8 |
| roc7-order-29.l4 | 22 | 25 | 11 | 11 | 5 | 5 |
| roc7-order-30.l4 | 28 | 28 | 21 | 21 | 21 | 21 |
| roc7-order-32.l4 | 12 | 13 | 10 | 10 | 2 | 2 |
| roc7-order-33a.l4 | 111 | 112 | 72 | 74 | 39 | 41 |
| roc7-order-33b.l4 | 74 | 74 | 58 | 59 | 24 | 24 |
| roc7-order-33c.l4 | 93 | 94 | 65 | 66 | 35 | 35 |
| total | 390 | 398 | 285 | 289 | 134 | 136 |

Specific readings the lawyer should look at first, each with the other reading:

1. O 28 r 7(4)(a), "unless sub-paragraphs (b) and (c) apply": read as "unless either applies"; the literal "and" would displace (a) only where an entity is at once newly registered and registered before 1 April 2022 (fork F-28-1).
2. O 28 r 1, "deemed means deemed until the contrary is proved": the deeming stands (JUST TRUE) until the contrary is proved and ends (JUST FALSE) once it is; the other reading answers NOTHING once the contrary is proved (F-28-3).
3. O 33 r 6 and r 14(2), "unless it is satisfied that ... a good and sufficient reason": when the Court is satisfied the power is not there (JUST FALSE); the other reading is NOTHING (F-33-2).
4. O 33 r 13(3): where neither "the Court so orders" nor consent holds, JUST FALSE; the other reading is NOTHING (F-33-4).
5. O 33 r 11(1), "(a) ...; and (b) ...": both required (F-33-1).
6. Every JUST FALSE given after a period has run out rests on the periods ruling (a) of 2026-11-05 and not on a negative in the text (F-ALL-1); PLAN.md would have answered NOTHING.
7. Every JUST FALSE given for a duty or deeming "lifted by an exception" (for example O 33 r 18(1), r 23(2), r 27(2) "unless the Court otherwise orders") rests on the brief's rule that a duty lifted by an exception does not apply; the permission questions on a lifted bar (QA sites) are judgment calls, one line each under Judgment calls: JUST TRUE where the exception is a permission, order or direction, NOTHING where it is only a fact that ends the bar.


8. Check of the branches commented `NOTHING-kind (limited by its own wording)` against the headers of the modules, which say that an unmet "if" or "where" answers JUST FALSE (fork F-ALL-4).
After the changes below, 285 functions carry such a branch (289 branches in all, counted from the files).
I read the quoted words and the sentence round the branch for 161 of those functions, one by one; 159 of the 161 still carry the branch after the changes below.
The other 126 were not part of this check, each having its own line under Judgment calls: 116 are the compliance functions of a duty whose trigger is unmet (QD), 5 are QE sites, 4 are QA sites (all listed under Judgment calls), and one is `o 33 r 21(10) the interest on the sum`, which was added in this round (fork F-33-5).
A branch stays NOTHING where the unmet thing is the exercise of the grant itself (the Registrar has allowed, the Court orders, the party applies), a relative clause or parenthesis that limits what a charge, a deeming or a grant covers, a discretion formula ("as the Court thinks fit"), or a count ("once").
It becomes JUST FALSE where the sentence is "If", "Where", "When", "Upon" or "Unless" followed by a condition that the facts can meet or miss.
Seven branches changed: O 28 r 12(1), O 28 r 8(8)(b), O 28 r 12(9)(b), O 32 r 5(2)(b), O 33 r 18(8) and O 33 r 41(2) now answer JUST FALSE, and O 33 r 7(11) (a second amendment) now answers NOTHING.
Checked, no change: O 28 r 8(1), whose companion `o 28 r 8(1) the requirement to use the electronic filing service arises` already answers JUST FALSE when the document is not required to be filed and whose compliance question answers NOTHING (a bare "must", QB); and O 28 r 8(4), a grant with no "if" that answers NOTHING until the Registrar has allowed.


### Every function that rests on reading (a), (b) or (c)

Each row is one function; "a" counts its FALSE-kind branches, "b" its NOTHING-kind (limited by its own wording) branches, "c" its NOTHING-kind (a requirement not met) branches. `grep -n "FALSE-kind"` in the file lists each branch with the words quoted.

| function | file:line | a | b | c |
| --- | --- | --- | --- | --- |
| `o 28 r 1 a defined term has its defined meaning` | roc7-order-28.l4:44 | 0 | 1 | 0 |
| `o 28 r 1 a person is an authorised user` | roc7-order-28.l4:53 | 1 | 0 | 0 |
| `o 28 r 1 a deeming under this Order stands` | roc7-order-28.l4:65 | 1 | 0 | 0 |
| `o 28 r 1 a service is the electronic filing service` | roc7-order-28.l4:74 | 1 | 0 | 0 |
| `o 28 r 1 a provider is an electronic filing service provider` | roc7-order-28.l4:82 | 1 | 0 | 0 |
| `o 28 r 1 a transmission is electronic transmission` | roc7-order-28.l4:91 | 1 | 0 | 0 |
| `o 28 r 1 a body is an entity` | roc7-order-28.l4:113 | 1 | 0 | 0 |
| `o 28 r 1 a code is an identification code` | roc7-order-28.l4:123 | 1 | 0 | 0 |
| `o 28 r 1 a body is a public authority` | roc7-order-28.l4:132 | 1 | 0 | 0 |
| `o 28 r 1 a person is a registered foreign lawyer` | roc7-order-28.l4:141 | 1 | 0 | 0 |
| `o 28 r 1 a body is a registered user` | roc7-order-28.l4:150 | 1 | 0 | 0 |
| `o 28 r 1 a bureau is a service bureau` | roc7-order-28.l4:158 | 1 | 0 | 0 |
| `o 28 r 2 the Registrar may establish an electronic filing service` | roc7-order-28.l4:171 | 0 | 1 | 0 |
| `o 28 r 3(1) the service is operated by a provider appointed as required` | roc7-order-28.l4:180 | 0 | 0 | 1 |
| `o 28 r 4 equipment is part of the computer system of a provider` | roc7-order-28.l4:198 | 1 | 0 | 0 |
| `o 28 r 5(1) the Registrar may establish or appoint agents to establish a service bureau` | roc7-order-28.l4:206 | 0 | 1 | 0 |
| `o 28 r 5(2) an appointed agent is treated as an agent for accepting payment of fees or service charges` | roc7-order-28.l4:216 | 1 | 0 | 0 |
| `o 28 r 6(1) an entity may apply to be a registered user` | roc7-order-28.l4:239 | 0 | 1 | 0 |
| `o 28 r 6(2) a registered user may designate a person as an authorised user` | roc7-order-28.l4:248 | 0 | 1 | 0 |
| `o 28 r 6(3) the Registrar may allow a registered user or an authorised user on terms` | roc7-order-28.l4:256 | 0 | 1 | 0 |
| `o 28 r 6(4) the entity or person is deemed registered or designated under this Rule` | roc7-order-28.l4:266 | 0 | 1 | 0 |
| `o 28 r 6(5) the registered user is deemed to approve use of the identification code` | roc7-order-28.l4:276 | 0 | 1 | 0 |
| `o 28 r 6(6) the registered user has met the conditions for using the electronic filing service` | roc7-order-28.l4:288 | 0 | 0 | 1 |
| `o 28 r 6(7) the Registrar may waive paragraph (6)` | roc7-order-28.l4:296 | 0 | 1 | 0 |
| `o 28 r 6(8) a service bureau is deemed to be a registered user` | roc7-order-28.l4:305 | 0 | 1 | 0 |
| `o 28 r 6(8) an employee of a service bureau is deemed to be an authorised user` | roc7-order-28.l4:314 | 0 | 1 | 0 |
| `o 28 r 7(1) the fee is payable by the registered user` | roc7-order-28.l4:329 | 0 | 1 | 0 |
| `o 28 r 7(2) paragraph (1) applies with a modification` | roc7-order-28.l4:411 | 1 | 0 | 0 |
| `o 28 r 7(3) no fee is payable by the registered user` | roc7-order-28.l4:438 | 1 | 0 | 0 |
| `o 28 r 7(4) the relevant time` | roc7-order-28.l4:464 | 0 | 1 | 0 |
| `o 28 r 7(4) a relevant time arises in this way` | roc7-order-28.l4:483 | 2 | 0 | 0 |
| `o 28 r 7(5) the fee is payable for the month` | roc7-order-28.l4:502 | 1 | 0 | 0 |
| `o 28 r 7(6) the fee for the month is due and payable on the day` | roc7-order-28.l4:520 | 1 | 0 | 0 |
| `o 28 r 7(7) the Registrar may waive, refund or defer the fee` | roc7-order-28.l4:530 | 0 | 1 | 0 |
| `o 28 r 7(8)(a) the Registrar must refund the amount paid in excess or error (the duty arises)` | roc7-order-28.l4:544 | 1 | 0 | 0 |
| `o 28 r 7(8)(a) the Registrar must refund the amount paid in excess or error` | roc7-order-28.l4:555 | 0 | 1 | 1 |
| `o 28 r 7(8)(a) the act is done by the last day` | roc7-order-28.l4:574 | 2 | 0 | 0 |
| `o 28 r 7(8)(b) the Registrar may refund in any other case` | roc7-order-28.l4:606 | 0 | 1 | 0 |
| `o 28 r 8(1) the requirement to use the electronic filing service arises` | roc7-order-28.l4:628 | 1 | 0 | 0 |
| `o 28 r 8(1) the document is filed using the electronic filing service as required` | roc7-order-28.l4:638 | 0 | 0 | 1 |
| `o 28 r 8(2) the requirement is satisfied by a single copy filed using the electronic filing service` | roc7-order-28.l4:647 | 0 | 1 | 0 |
| `o 28 r 8(3) the way of using the electronic filing service is one of the 2 ways` | roc7-order-28.l4:661 | 1 | 0 | 0 |
| `o 28 r 8(4) a document may be filed other than using the electronic filing service` | roc7-order-28.l4:670 | 0 | 1 | 0 |
| `o 28 r 8(5) the form of the document is as required` | roc7-order-28.l4:687 | 0 | 0 | 1 |
| `o 28 r 8(6) the document is deemed filed by the registered user with that user's intention` | roc7-order-28.l4:699 | 0 | 1 | 0 |
| `o 28 r 8(7)(a) the document is deemed conveyed by the authorised user on behalf and with the authority of the registered user` | roc7-order-28.l4:711 | 0 | 1 | 0 |
| `o 28 r 8(7)(b) the document is deemed conveyed with the intention of the registered user` | roc7-order-28.l4:723 | 0 | 1 | 0 |
| `o 28 r 8(8)(a) the document is deemed conveyed on behalf and with the authority of the person tendering it` | roc7-order-28.l4:735 | 0 | 1 | 0 |
| `o 28 r 8(8)(b) the document is deemed conveyed on behalf and with the authority of the principal` | roc7-order-28.l4:748 | 1 | 1 | 0 |
| `o 28 r 9(1) a requirement of signing by an authorised user or a registered user is deemed complied with` | roc7-order-28.l4:774 | 1 | 0 | 0 |
| `o 28 r 9(2)(a)(i) the document is deemed signed by the registered user` | roc7-order-28.l4:785 | 1 | 0 | 0 |
| `o 28 r 9(2)(a)(ii) the contents are deemed endorsed by the registered user` | roc7-order-28.l4:796 | 1 | 0 | 0 |
| `o 28 r 9(2)(b)(i) the document is deemed signed by the authorised user on behalf of the registered user` | roc7-order-28.l4:807 | 1 | 0 | 0 |
| `o 28 r 9(2)(b)(ii) the contents are deemed endorsed by the registered user` | roc7-order-28.l4:818 | 1 | 0 | 0 |
| `o 28 r 9(2)(c)(i) the document is deemed signed on behalf of the person tendering it` | roc7-order-28.l4:829 | 1 | 0 | 0 |
| `o 28 r 9(2)(c)(ii) the document is deemed signed on behalf of the principal` | roc7-order-28.l4:841 | 1 | 0 | 0 |
| `o 28 r 9(3) the requirement for the signature of an advocate or solicitor is deemed met` | roc7-order-28.l4:852 | 1 | 0 | 0 |
| `o 28 r 10(1) the document is deemed filed, served, delivered or conveyed` | roc7-order-28.l4:887 | 1 | 0 | 0 |
| `o 28 r 10(2) paragraph (1) applies to the document` | roc7-order-28.l4:901 | 1 | 0 | 0 |
| `o 28 r 10(3) the caveat is deemed filed at the moment the Registrar accepts it` | roc7-order-28.l4:965 | 1 | 0 | 0 |
| `o 28 r 10(4) the originating process is deemed issued` | roc7-order-28.l4:978 | 1 | 0 | 0 |
| `o 28 r 10(5) the registered user may produce a record as evidence of filing or issuance` | roc7-order-28.l4:1005 | 0 | 1 | 0 |
| `o 28 r 10(6) the Registrar may cause an earlier date and time to be reflected` | roc7-order-28.l4:1013 | 1 | 0 | 0 |
| `o 28 r 11(1) time for service cannot yet begin to run` | roc7-order-28.l4:1028 | 1 | 0 | 0 |
| `o 28 r 11(1) time for service has begun to run` | roc7-order-28.l4:1036 | 1 | 0 | 0 |
| `o 28 r 12(1) service may be effected using the electronic filing service` | roc7-order-28.l4:1096 | 1 | 0 | 0 |
| `o 28 r 12(2) the party is deemed to have agreed to be served using the electronic filing service` | roc7-order-28.l4:1107 | 0 | 1 | 0 |
| `o 28 r 12(3)(a) the document is deemed served by electronic transmission` | roc7-order-28.l4:1130 | 1 | 0 | 0 |
| `o 28 r 12(3)(b) the remotely composed document is deemed served` | roc7-order-28.l4:1140 | 1 | 0 | 0 |
| `o 28 r 12(4) the person serving may produce a record of service as evidence` | roc7-order-28.l4:1148 | 0 | 1 | 0 |
| `o 28 r 12(5) the person serving may file a Registrar's certificate of service in lieu of an affidavit` | roc7-order-28.l4:1156 | 0 | 1 | 0 |
| `o 28 r 12(5) the certificate is regarded as prima facie evidence of service` | roc7-order-28.l4:1165 | 0 | 1 | 0 |
| `o 28 r 12(6) service on more than one person may be effected using the electronic filing service on those who are users` | roc7-order-28.l4:1174 | 1 | 1 | 0 |
| `o 28 r 12(7) the document is deemed served by the registered user with that user's intention` | roc7-order-28.l4:1186 | 0 | 1 | 0 |
| `o 28 r 12(8)(a) the document is deemed served by the authorised user on behalf and with the authority of the registered user` | roc7-order-28.l4:1197 | 0 | 1 | 0 |
| `o 28 r 12(8)(b) the document is deemed served with the intention of the registered user` | roc7-order-28.l4:1208 | 0 | 1 | 0 |
| `o 28 r 12(9)(a) the document is deemed served on behalf and with the authority of the person tendering it` | roc7-order-28.l4:1218 | 0 | 1 | 0 |
| `o 28 r 12(9)(b) the document is deemed served on behalf and with the authority of the principal` | roc7-order-28.l4:1229 | 1 | 1 | 0 |
| `o 28 r 12(11) Order 7, Rule 8 applies to the service` | roc7-order-28.l4:1251 | 0 | 1 | 0 |
| `o 28 r 12(11) the day service through the electronic filing service is deemed effected` | roc7-order-28.l4:1260 | 0 | 1 | 0 |
| `o 28 r 13 the Registrar may notify or deliver using the electronic filing service` | roc7-order-28.l4:1274 | 1 | 0 | 0 |
| `o 28 r 14 the amendment is effected in the manner prescribed in the practice directions` | roc7-order-28.l4:1283 | 0 | 0 | 1 |
| `o 28 r 15(1) the affidavit may be used to the same extent as a paper affidavit` | roc7-order-28.l4:1291 | 0 | 1 | 0 |
| `o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way` | roc7-order-28.l4:1301 | 0 | 1 | 1 |
| `o 28 r 15(2)(a) the affidavit is sworn or affirmed in the usual way (the duty arises)` | roc7-order-28.l4:1310 | 1 | 0 | 0 |
| `o 28 r 15(2)(b) a true and complete electronic image of the original is created` | roc7-order-28.l4:1320 | 0 | 1 | 1 |
| `o 28 r 15(2)(b) a true and complete electronic image of the original is created (the duty arises)` | roc7-order-28.l4:1329 | 1 | 0 | 0 |
| `o 28 r 15(2)(c) the original paper affidavit is retained for 7 years` | roc7-order-28.l4:1344 | 1 | 0 | 0 |
| `o 28 r 15(3) the Court may permit the electronic image to be used` | roc7-order-28.l4:1366 | 1 | 0 | 0 |
| `o 28 r 16 the information contained in the document prevails` | roc7-order-28.l4:1382 | 1 | 0 | 0 |
| `o 28 r 16 the information entered into the electronic template prevails` | roc7-order-28.l4:1392 | 1 | 0 | 0 |
| `o 28 r 17(1) a user registered by the Registrar of the Supreme Court is treated as also registered by the other two Registrars` | roc7-order-28.l4:1406 | 0 | 1 | 0 |
| `o 28 r 17(2) a user registered by the Registrar of the State Courts is treated as also registered by the other two Registrars` | roc7-order-28.l4:1415 | 0 | 1 | 0 |
| `o 28 r 17(3) a user registered by the Registrar of the Family Justice Courts is treated as also registered by the other two Registrars` | roc7-order-28.l4:1424 | 0 | 1 | 0 |
| `o 28 r 17(4)(a) a Supreme Court service bureau may be used for State Courts proceedings` | roc7-order-28.l4:1435 | 0 | 1 | 0 |
| `o 28 r 17(4)(b) a Supreme Court service bureau may be used for Family Justice Courts proceedings` | roc7-order-28.l4:1446 | 0 | 1 | 0 |
| `o 28 r 17(5)(a) a State Courts service bureau may be used for Supreme Court proceedings` | roc7-order-28.l4:1457 | 0 | 1 | 0 |
| `o 28 r 17(5)(b) a State Courts service bureau may be used for Family Justice Courts proceedings` | roc7-order-28.l4:1468 | 0 | 1 | 0 |
| `o 28 r 17(6)(a) a Family Justice Courts service bureau may be used for Supreme Court proceedings` | roc7-order-28.l4:1479 | 0 | 1 | 0 |
| `o 28 r 17(6)(b) a Family Justice Courts service bureau may be used for State Courts proceedings` | roc7-order-28.l4:1490 | 0 | 1 | 0 |
| `o 29 r 1 a defined term has its defined meaning` | roc7-order-29.l4:31 | 0 | 1 | 0 |
| `o 29 r 1 a court is the Court` | roc7-order-29.l4:40 | 1 | 0 | 0 |
| `o 29 r 1 a place is a foreign country` | roc7-order-29.l4:52 | 1 | 0 | 0 |
| `o 29 r 6 a place is a specified foreign country` | roc7-order-29.l4:79 | 1 | 0 | 0 |
| `o 29 r 7 a court is a specified court` | roc7-order-29.l4:94 | 4 | 0 | 0 |
| `o 29 r 1 a court is a specified court` | roc7-order-29.l4:112 | 1 | 0 | 0 |
| `o 29 r 1 a place is a specified foreign country` | roc7-order-29.l4:121 | 1 | 0 | 0 |
| `o 29 r 2(1) the Court may order proceedings in a specified court in a specified foreign country` | roc7-order-29.l4:137 | 1 | 1 | 0 |
| `o 29 r 2(2) the application is made by summons and supported by an affidavit` | roc7-order-29.l4:149 | 0 | 1 | 1 |
| `o 29 r 2(2) the application is made by summons and supported by an affidavit (the duty arises)` | roc7-order-29.l4:158 | 1 | 0 | 0 |
| `o 29 r 2(3) the Court may give directions for a statement of the issue` | roc7-order-29.l4:166 | 1 | 0 | 0 |
| `o 29 r 3 this Order does not prevent the Court ordering proceedings in another foreign country on its own motion` | roc7-order-29.l4:177 | 0 | 1 | 0 |
| `o 29 r 4 the order states what it must state` | roc7-order-29.l4:196 | 0 | 1 | 1 |
| `o 29 r 4 the order states what it must state (the duty arises)` | roc7-order-29.l4:205 | 1 | 0 | 0 |
| `o 29 r 5(1) proceedings on an issue of Singapore law may be commenced by originating application` | roc7-order-29.l4:220 | 1 | 1 | 0 |
| `o 29 r 5(2) the originating application or affidavit states what it must state` | roc7-order-29.l4:241 | 0 | 1 | 1 |
| `o 29 r 5(2) the originating application or affidavit states what it must state (the duty arises)` | roc7-order-29.l4:250 | 1 | 0 | 0 |
| `o 29A r 1 a defined term has its defined meaning` | roc7-order-29.l4:267 | 0 | 1 | 0 |
| `o 29A r 1 a court is the Court` | roc7-order-29.l4:275 | 1 | 0 | 0 |
| `o 29A r 1 a place is a foreign country` | roc7-order-29.l4:287 | 1 | 0 | 0 |
| `o 29A r 4 a place is a specified foreign country` | roc7-order-29.l4:297 | 1 | 0 | 0 |
| `o 29A r 5 a court is a specified court` | roc7-order-29.l4:306 | 1 | 0 | 0 |
| `o 29A r 1 a court is a specified court` | roc7-order-29.l4:315 | 1 | 0 | 0 |
| `o 29A r 1 a place is a specified foreign country` | roc7-order-29.l4:324 | 1 | 0 | 0 |
| `o 29A r 2(1) the Court may transmit a request for an opinion to a specified court` | roc7-order-29.l4:347 | 1 | 1 | 0 |
| `o 29A r 2(2) the application is made by summons` | roc7-order-29.l4:358 | 0 | 1 | 1 |
| `o 29A r 2(2) the application is made by summons (the duty arises)` | roc7-order-29.l4:367 | 1 | 0 | 0 |
| `o 29A r 3(1) the initial request states what it must state` | roc7-order-29.l4:386 | 0 | 1 | 1 |
| `o 29A r 3(1) the initial request states what it must state (the duty arises)` | roc7-order-29.l4:395 | 1 | 0 | 0 |
| `o 29A r 3(2) a request may identify the proceedings or the parties` | roc7-order-29.l4:405 | 1 | 0 | 0 |
| `o 30 r 1(1) this Order applies to the Reference` | roc7-order-30.l4:35 | 0 | 1 | 0 |
| `o 30 r 1(2) a reference is a Reference` | roc7-order-30.l4:44 | 1 | 0 | 0 |
| `o 30 r 1(2) a tribunal is the Tribunal` | roc7-order-30.l4:53 | 1 | 0 | 0 |
| `o 30 r 2(1) the Reference is brought by filing it in Form 47` | roc7-order-30.l4:67 | 0 | 0 | 1 |
| `o 30 r 2(2) the Reference is made under the hand of the President of Singapore` | roc7-order-30.l4:75 | 0 | 0 | 1 |
| `o 30 r 2(3) the Registrar causes a copy of the Reference to be served on the Attorney-General` | roc7-order-30.l4:83 | 0 | 0 | 1 |
| `o 30 r 3(1) the Reference states the questions in a form which can be answered yes or no` | roc7-order-30.l4:91 | 0 | 0 | 1 |
| `o 30 r 3(2) the Reference is divided into paragraphs and states what is necessary` | roc7-order-30.l4:101 | 0 | 0 | 1 |
| `o 30 r 4(1) the Tribunal consists of the Chief Justice and the other Judges` | roc7-order-30.l4:115 | 0 | 0 | 1 |
| `o 30 r 4(2) the Tribunal consists of Judges appointed by the Chief Justice` | roc7-order-30.l4:124 | 0 | 1 | 1 |
| `o 30 r 4(2) the Tribunal consists of Judges appointed by the Chief Justice (the duty arises)` | roc7-order-30.l4:133 | 1 | 0 | 0 |
| `o 30 r 4(3) the presidency may be determined by the order of precedence` | roc7-order-30.l4:150 | 1 | 1 | 0 |
| `o 30 r 5(1) the Tribunal may direct that a person interested be notified` | roc7-order-30.l4:160 | 0 | 1 | 0 |
| `o 30 r 5(2) the person informs the Tribunal in writing of the intention to be heard` | roc7-order-30.l4:177 | 0 | 1 | 1 |
| `o 30 r 5(2) the person informs the Tribunal in writing of the intention to be heard (the duty arises)` | roc7-order-30.l4:186 | 1 | 0 | 0 |
| `o 30 r 6(1) the Attorney-General assists the Tribunal` | roc7-order-30.l4:207 | 0 | 0 | 1 |
| `o 30 r 6(2) the Presidency may be represented by counsel the Tribunal appoints` | roc7-order-30.l4:216 | 0 | 1 | 0 |
| `o 30 r 7 the Tribunal may request counsel to argue the case` | roc7-order-30.l4:225 | 0 | 1 | 0 |
| `o 30 r 8(1) the Reference is regarded as an appeal to the Court of Appeal` | roc7-order-30.l4:239 | 1 | 1 | 0 |
| `o 30 r 8(2) the Reference is treated as the record of appeal` | roc7-order-30.l4:249 | 1 | 0 | 0 |
| `o 30 r 8(3) the President of Singapore is treated as the appellant` | roc7-order-30.l4:258 | 1 | 1 | 0 |
| `o 30 r 8(3) a party is treated as a respondent` | roc7-order-30.l4:269 | 1 | 1 | 0 |
| `o 30 r 8(4) the steps required before filing the record of appeal are taken` | roc7-order-30.l4:280 | 1 | 1 | 0 |
| `o 30 r 9 the procedure follows the procedure before the Court of Appeal` | roc7-order-30.l4:291 | 0 | 1 | 0 |
| `o 30 r 9 the Tribunal is bound by the strict rules of evidence` | roc7-order-30.l4:301 | 1 | 0 | 0 |
| `o 30 r 10 the requirement to hold the proceeding in open court applies` | roc7-order-30.l4:315 | 1 | 0 | 0 |
| `o 30 r 10 the proceeding is held in open court` | roc7-order-30.l4:326 | 1 | 1 | 1 |
| `o 30 r 10 the proceeding is held in open court (the duty arises)` | roc7-order-30.l4:338 | 1 | 0 | 0 |
| `o 30 r 11 the Registrar serves a notice to attend a hearing for directions` | roc7-order-30.l4:349 | 0 | 0 | 1 |
| `o 30 r 13(1) the report is in the form of an answer to the questions` | roc7-order-30.l4:378 | 0 | 0 | 1 |
| `o 30 r 13(2) the Registrar delivers the report to the President of Singapore and the Attorney-General` | roc7-order-30.l4:387 | 0 | 0 | 1 |
| `o 30 r 14 a party may be ordered to pay costs` | roc7-order-30.l4:397 | 1 | 0 | 0 |
| `o 30 r 15 a fee is payable in respect of the proceedings` | roc7-order-30.l4:406 | 1 | 0 | 0 |
| `o 31 r 1(1) this Order applies despite Order 1, Rule 2` | roc7-order-30.l4:428 | 1 | 0 | 0 |
| `o 31 r 1(2) the Case states what it must state` | roc7-order-30.l4:440 | 0 | 1 | 1 |
| `o 31 r 1(2) the Case states what it must state (the duty arises)` | roc7-order-30.l4:449 | 1 | 0 | 0 |
| `o 31 r 1(3) the Registrar of the Supreme Court lays the Case before a Judge and serves a copy on the Attorney-General` | roc7-order-30.l4:459 | 0 | 1 | 1 |
| `o 31 r 1(3) the Registrar of the Supreme Court lays the Case before a Judge and serves a copy on the Attorney-General (the duty arises)` | roc7-order-30.l4:468 | 1 | 0 | 0 |
| `o 31 r 1(4) the Judge deals with the Case as if it were a case in the original jurisdiction` | roc7-order-30.l4:477 | 0 | 1 | 1 |
| `o 31 r 1(4) the Judge deals with the Case as if it were a case in the original jurisdiction (the duty arises)` | roc7-order-30.l4:486 | 1 | 0 | 0 |
| `o 31 r 2(1) the Case is regarded as an application to the General Division` | roc7-order-30.l4:499 | 1 | 0 | 0 |
| `o 31 r 2(2) the Case is treated as the record of proceedings` | roc7-order-30.l4:507 | 1 | 0 | 0 |
| `o 31 r 2(3) the claimant or the prosecution is treated as the applicant` | roc7-order-30.l4:516 | 1 | 1 | 0 |
| `o 31 r 2(3) a party is treated as a respondent` | roc7-order-30.l4:527 | 1 | 1 | 0 |
| `o 31 r 2(4) the judgment of the General Division is in the form of an answer to the question` | roc7-order-30.l4:538 | 0 | 1 | 1 |
| `o 31 r 2(4) the judgment of the General Division is in the form of an answer to the question (the duty arises)` | roc7-order-30.l4:547 | 1 | 0 | 0 |
| `o 31 r 2(5) the Registrar of the Supreme Court serves notice of the hearing` | roc7-order-30.l4:557 | 0 | 1 | 1 |
| `o 31 r 2(5) the Registrar of the Supreme Court serves notice of the hearing (the duty arises)` | roc7-order-30.l4:566 | 1 | 0 | 0 |
| `o 31 r 3 the Registrar of the Supreme Court delivers a copy of the judgment` | roc7-order-30.l4:576 | 0 | 0 | 1 |
| `o 31 r 4(1) the State Court continues and disposes of the proceedings according to law` | roc7-order-30.l4:586 | 0 | 1 | 1 |
| `o 31 r 4(1) the State Court continues and disposes of the proceedings according to law (the duty arises)` | roc7-order-30.l4:596 | 1 | 0 | 0 |
| `o 31 r 4(2) the State Court determines all questions and makes the orders regarding costs` | roc7-order-30.l4:605 | 0 | 0 | 1 |
| `o 31 r 4(2) an order for costs incurred in the General Division may be made` | roc7-order-30.l4:615 | 1 | 0 | 0 |
| `o 32 r 1 an action is an administration action` | roc7-order-32.l4:32 | 1 | 0 | 0 |
| `o 32 r 2(1) an action may be brought for a question or relief which could be had in an administration action` | roc7-order-32.l4:61 | 0 | 1 | 0 |
| `o 32 r 2(1) a claim for administration or execution must be made in the action` | roc7-order-32.l4:71 | 1 | 0 | 0 |
| `o 32 r 3(1) all the personal representatives are parties to the action` | roc7-order-32.l4:131 | 0 | 1 | 1 |
| `o 32 r 3(1) all the personal representatives are parties to the action (the duty arises)` | roc7-order-32.l4:140 | 1 | 0 | 0 |
| `o 32 r 3(1) a personal representative who does not consent is made a defendant` | roc7-order-32.l4:150 | 0 | 1 | 1 |
| `o 32 r 3(1) a personal representative who does not consent is made a defendant (the duty arises)` | roc7-order-32.l4:160 | 1 | 0 | 0 |
| `o 32 r 3(2) a person having a beneficial interest or claim must be a party` | roc7-order-32.l4:169 | 1 | 0 | 0 |
| `o 32 r 3(2) the claimant may make a person with a beneficial interest or claim a party` | roc7-order-32.l4:179 | 0 | 1 | 0 |
| `o 32 r 3(3) a party other than the executors or administrators is entitled to appear` | roc7-order-32.l4:194 | 1 | 1 | 0 |
| `o 32 r 3(3) the Court may direct or allow another party to appear` | roc7-order-32.l4:207 | 1 | 1 | 0 |
| `o 32 r 4 the Court may grant relief for breach of trust even though the action began by originating application` | roc7-order-32.l4:223 | 1 | 1 | 0 |
| `o 32 r 4 the Court may order that the originating application be converted into an originating claim` | roc7-order-32.l4:234 | 0 | 1 | 0 |
| `o 32 r 5(1) a judgment or order for administration or execution need be given or made` | roc7-order-32.l4:245 | 1 | 1 | 0 |
| `o 32 r 5(2)(a) the Court may stay the action and order the personal representatives to provide accounts` | roc7-order-32.l4:257 | 1 | 1 | 0 |
| `o 32 r 5(2)(b) the Court may give judgment or make an order for administration` | roc7-order-32.l4:270 | 1 | 0 | 0 |
| `o 32 r 6 the personal representatives have the conduct of the sale` | roc7-order-32.l4:281 | 2 | 0 | 0 |
| `o 33 r 1(1) this Order applies to the cause or matter` | roc7-order-33a.l4:39 | 0 | 1 | 0 |
| `o 33 r 1(2) an action is an action in rem` | roc7-order-33a.l4:47 | 1 | 0 | 0 |
| `o 33 r 1(2) a caveat is a caveat against arrest` | roc7-order-33a.l4:56 | 1 | 0 | 0 |
| `o 33 r 1(2) a caveat is a caveat against release and payment` | roc7-order-33a.l4:65 | 1 | 0 | 0 |
| `o 33 r 1(2) a recording is electronic track data` | roc7-order-33a.l4:74 | 1 | 0 | 0 |
| `o 33 r 1(2) an action is a limitation action` | roc7-order-33a.l4:83 | 1 | 0 | 0 |
| `o 33 r 1(2) information is the record of caveats` | roc7-order-33a.l4:91 | 1 | 0 | 0 |
| `o 33 r 1(2) an account is the Sheriff's account` | roc7-order-33a.l4:99 | 1 | 0 | 0 |
| `o 33 r 1(3) a reference to payment into Court of proceeds of sale means payment into the Sheriff's account` | roc7-order-33a.l4:116 | 1 | 0 | 0 |
| `o 33 r 2(1) an action in rem is begun by originating claim in Form 48` | roc7-order-33a.l4:131 | 0 | 1 | 1 |
| `o 33 r 2(1) an action in rem is begun by originating claim in Form 48 (the duty arises)` | roc7-order-33a.l4:140 | 1 | 0 | 0 |
| `o 33 r 2(2) the originating claim in an Admiralty action in personam is in Form 8 with the words inserted` | roc7-order-33a.l4:150 | 0 | 1 | 1 |
| `o 33 r 2(2) the originating claim in an Admiralty action in personam is in Form 8 with the words inserted (the duty arises)` | roc7-order-33a.l4:159 | 1 | 0 | 0 |
| `o 33 r 2(3) Order 6 Rules 5(4) and (6) and 6(1), (2), (3), (4) and (7) apply to the action` | roc7-order-33a.l4:167 | 1 | 0 | 0 |
| `o 33 r 2(4) the defendant served in Singapore files and serves the notice` | roc7-order-33a.l4:177 | 0 | 1 | 1 |
| `o 33 r 2(4) the defendant served in Singapore files and serves the notice (the duty arises)` | roc7-order-33a.l4:186 | 1 | 0 | 0 |
| `o 33 r 2(5) the defendant served out of Singapore files and serves the notice` | roc7-order-33a.l4:208 | 0 | 1 | 1 |
| `o 33 r 2(5) the defendant served out of Singapore files and serves the notice (the duty arises)` | roc7-order-33a.l4:217 | 1 | 0 | 0 |
| `o 33 r 2(6) the notice is in Form 49` | roc7-order-33a.l4:239 | 0 | 1 | 1 |
| `o 33 r 2(6) the notice is in Form 49 (the duty arises)` | roc7-order-33a.l4:248 | 1 | 0 | 0 |
| `o 33 r 2(7) the filing and service of the notice is treated as a submission to jurisdiction or a waiver of any improper service` | roc7-order-33a.l4:256 | 1 | 0 | 0 |
| `o 33 r 2(8) the claimant may apply for judgment in Form 50` | roc7-order-33a.l4:270 | 1 | 1 | 0 |
| `o 33 r 2(9) the originating claim is valid for service on the date` | roc7-order-33a.l4:287 | 1 | 0 | 0 |
| `o 33 r 2(10) Order 6 Rule 6(5) and (6) and Order 16 Rule 2(6) and (7) apply to the originating claim` | roc7-order-33a.l4:295 | 1 | 0 | 0 |
| `o 33 r 3(1) this Rule applies to the action` | roc7-order-33a.l4:319 | 0 | 1 | 0 |
| `o 33 r 3(2) service out of Singapore is permissible` | roc7-order-33a.l4:341 | 1 | 1 | 0 |
| `o 33 r 3(3) this Rule applies to the action` | roc7-order-33a.l4:352 | 1 | 0 | 0 |
| `o 33 r 3(4) Order 8 other than Rule 4 applies to the service out of Singapore` | roc7-order-33a.l4:360 | 1 | 0 | 0 |
| `o 33 r 3(5) a term has the meaning given by the High Court (Admiralty Jurisdiction) Act` | roc7-order-33a.l4:369 | 1 | 0 | 0 |
| `o 33 r 4(1) the claimant or defendant may apply for a warrant of arrest` | roc7-order-33a.l4:384 | 1 | 1 | 0 |
| `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats` | roc7-order-33a.l4:399 | 0 | 1 | 1 |
| `o 33 r 4(2) the party applying for a warrant files it and procures a search of the record of caveats (the duty arises)` | roc7-order-33a.l4:408 | 1 | 0 | 0 |
| `o 33 r 4(3) the warrant of arrest cannot yet be issued for want of the affidavit` | roc7-order-33a.l4:418 | 1 | 0 | 0 |
| `o 33 r 4(3) the Court may allow the warrant to issue although the affidavit lacks particulars` | roc7-order-33a.l4:429 | 1 | 1 | 0 |
| `o 33 r 4(3) a warrant of arrest may be issued` | roc7-order-33a.l4:441 | 1 | 1 | 0 |
| `o 33 r 4(4) the warrant of arrest cannot yet be issued for want of notice to the consul` | roc7-order-33a.l4:455 | 1 | 1 | 0 |
| `o 33 r 4(4) a warrant of arrest may be issued against the foreign ship` | roc7-order-33a.l4:468 | 1 | 2 | 0 |
| `o 33 r 4(5) a warrant of arrest is issued` | roc7-order-33a.l4:481 | 1 | 0 | 0 |
| `o 33 r 4 a warrant of arrest is issued under this Rule` | roc7-order-33a.l4:492 | 1 | 0 | 0 |
| `o 33 r 4(6) the affidavit states what paragraph (6) requires` | roc7-order-33a.l4:509 | 0 | 1 | 1 |
| `o 33 r 4(6) the affidavit states what paragraph (6) requires (the duty arises)` | roc7-order-33a.l4:518 | 1 | 0 | 0 |
| `o 33 r 4(7) the affidavit states what paragraph (7) requires` | roc7-order-33a.l4:540 | 0 | 1 | 1 |
| `o 33 r 4(7) the affidavit states what paragraph (7) requires (the duty arises)` | roc7-order-33a.l4:550 | 1 | 0 | 0 |
| `o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats` | roc7-order-33a.l4:571 | 0 | 1 | 1 |
| `o 33 r 5(1) the caveat against arrest is filed in Form 52 and entered in the record of caveats (the duty arises)` | roc7-order-33a.l4:580 | 1 | 0 | 0 |
| `o 33 r 5(2) a caveat against arrest in force prevents the issue of a warrant to arrest the property` | roc7-order-33a.l4:603 | 1 | 0 | 0 |
| `o 33 r 5 a caveat against arrest is issued under this Rule` | roc7-order-33a.l4:618 | 0 | 1 | 0 |
| `o 33 r 6 the Court may discharge the warrant` | roc7-order-33a.l4:630 | 1 | 1 | 0 |
| `o 33 r 6 the Court may order the party procuring the arrest to pay damages` | roc7-order-33a.l4:643 | 1 | 1 | 0 |
| `o 33 r 7(1) the originating claim is served on the property against which the action is brought` | roc7-order-33a.l4:664 | 1 | 1 | 1 |
| `o 33 r 7(1) the originating claim is served on the property against which the action is brought (the duty arises)` | roc7-order-33a.l4:677 | 1 | 0 | 0 |
| `o 33 r 7(1)(a) where the property is freight the originating claim is served on the cargo or the ship` | roc7-order-33a.l4:688 | 0 | 1 | 1 |
| `o 33 r 7(1)(a) where the property is freight the originating claim is served on the cargo or the ship (the duty arises)` | roc7-order-33a.l4:698 | 1 | 0 | 0 |
| `o 33 r 7(1)(b) where the property has been sold by the Sheriff a sealed copy is filed and served on the Sheriff` | roc7-order-33a.l4:710 | 0 | 1 | 1 |
| `o 33 r 7(1)(b) where the property has been sold by the Sheriff a sealed copy is filed and served on the Sheriff (the duty arises)` | roc7-order-33a.l4:720 | 1 | 0 | 0 |
| `o 33 r 7(1)(b) the originating claim may be served on the property sold by the Sheriff` | roc7-order-33a.l4:729 | 1 | 0 | 0 |
| `o 33 r 7(1)(b) the originating claim is deemed served on the day the copy was filed` | roc7-order-33a.l4:739 | 1 | 0 | 0 |
| `o 33 r 7(2) the originating claim must be served as mentioned in paragraph (1)` | roc7-order-33a.l4:747 | 1 | 0 | 0 |
| `o 33 r 7(3)(a) the originating claim is deemed duly served on acceptance by the defendant's solicitor` | roc7-order-33a.l4:756 | 1 | 0 | 0 |
| `o 33 r 7(3)(b) the originating claim is deemed duly served when the defendant files the notice` | roc7-order-33a.l4:766 | 1 | 0 | 0 |
| `o 33 r 7(4) service on the property may be effected by the Sheriff or a notified solicitor or clerk` | roc7-order-33a.l4:793 | 1 | 1 | 0 |
| `o 33 r 7(5) the Registrar may allow service to be effected by any other named person` | roc7-order-33a.l4:804 | 1 | 1 | 0 |
| `o 33 r 7(5) the Registrar causes a memorandum to be marked on the originating claim` | roc7-order-33a.l4:815 | 0 | 1 | 1 |
| `o 33 r 7(5) the Registrar causes a memorandum to be marked on the originating claim (the duty arises)` | roc7-order-33a.l4:824 | 1 | 0 | 0 |
| `o 33 r 7(6) the claimant leaves a copy at the Registry and files a request in Form 53` | roc7-order-33a.l4:834 | 0 | 1 | 1 |
| `o 33 r 7(6) the claimant leaves a copy at the Registry and files a request in Form 53 (the duty arises)` | roc7-order-33a.l4:843 | 1 | 0 | 0 |
| `o 33 r 7(6) the Sheriff serves the originating claim on the property described in the request` | roc7-order-33a.l4:852 | 0 | 1 | 1 |
| `o 33 r 7(6) the Sheriff serves the originating claim on the property described in the request (the duty arises)` | roc7-order-33a.l4:861 | 1 | 0 | 0 |
| `o 33 r 7(7) the expenses of service are paid to the Sheriff on demand` | roc7-order-33a.l4:871 | 0 | 1 | 1 |
| `o 33 r 7(7) the expenses of service are paid to the Sheriff on demand (the duty arises)` | roc7-order-33a.l4:881 | 1 | 0 | 0 |
| `o 33 r 7(8) the person effecting service endorses the particulars on the originating claim` | roc7-order-33a.l4:890 | 0 | 1 | 1 |
| `o 33 r 7(8) the person effecting service endorses the particulars on the originating claim (the duty arises)` | roc7-order-33a.l4:899 | 1 | 0 | 0 |
| `o 33 r 7(8) the endorsement is evidence of the facts stated in it` | roc7-order-33a.l4:907 | 1 | 0 | 0 |
| `o 33 r 7(9) the Sheriff gives the claimant written notice of the fact and manner of service` | roc7-order-33a.l4:916 | 0 | 1 | 1 |
| `o 33 r 7(9) the Sheriff gives the claimant written notice of the fact and manner of service (the duty arises)` | roc7-order-33a.l4:925 | 1 | 0 | 0 |
| `o 33 r 7(10) the claimant serves the originating claim forthwith on the person who entered the caveat` | roc7-order-33a.l4:934 | 0 | 1 | 1 |
| `o 33 r 7(10) the claimant serves the originating claim forthwith on the person who entered the caveat (the duty arises)` | roc7-order-33a.l4:943 | 1 | 0 | 0 |
| `o 33 r 7(11) the originating claim may be amended once without permission to delete defendant vessels` | roc7-order-33a.l4:955 | 1 | 1 | 0 |
| `o 33 r 7(11) the amended originating claim is served as required` | roc7-order-33a.l4:970 | 1 | 1 | 2 |
| `o 33 r 7(11) the amended originating claim is served as required (the duty arises)` | roc7-order-33a.l4:983 | 1 | 0 | 0 |
| `o 33 r 7(12) permission of the Court is required for the amendment` | roc7-order-33a.l4:1003 | 1 | 1 | 0 |
| `o 33 r 8 the solicitor is liable to committal` | roc7-order-33a.l4:1020 | 1 | 0 | 0 |
| `o 33 r 9(1) the warrant of arrest is valid on the date` | roc7-order-33a.l4:1039 | 1 | 0 | 0 |
| `o 33 r 9(2) the warrant may be executed by the Sheriff or a notified solicitor or clerk` | roc7-order-33a.l4:1047 | 0 | 1 | 0 |
| `o 33 r 9(3) the Registrar may allow the warrant to be executed by any other named person` | roc7-order-33a.l4:1056 | 1 | 1 | 0 |
| `o 33 r 9(3) the Registrar causes a memorandum to be marked on the warrant` | roc7-order-33a.l4:1067 | 0 | 1 | 1 |
| `o 33 r 9(3) the Registrar causes a memorandum to be marked on the warrant (the duty arises)` | roc7-order-33a.l4:1076 | 1 | 0 | 0 |
| `o 33 r 9(4) the warrant of arrest cannot yet be executed by the Sheriff for want of the undertaking` | roc7-order-33a.l4:1087 | 1 | 1 | 0 |
| `o 33 r 9(5) the warrant of arrest may be executed` | roc7-order-33a.l4:1098 | 1 | 0 | 0 |
| `o 33 r 9(6) a warrant issued against freight may be executed by serving it on the cargo or the ship or both` | roc7-order-33a.l4:1107 | 1 | 1 | 0 |
| `o 33 r 9(7) the warrant of arrest is served on the property against which it is issued` | roc7-order-33a.l4:1119 | 1 | 1 | 1 |
| `o 33 r 9(7) the warrant of arrest is served on the property against which it is issued (the duty arises)` | roc7-order-33a.l4:1131 | 1 | 0 | 0 |
| `o 33 r 9(8) the report of the arrest is made by the person required` | roc7-order-33a.l4:1147 | 0 | 1 | 2 |
| `o 33 r 9(8) the report of the arrest is made by the person required (the duty arises)` | roc7-order-33a.l4:1157 | 1 | 0 | 0 |
| `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy` | roc7-order-33a.l4:1190 | 1 | 1 | 1 |
| `o 33 r 10(1) service on a ship, freight or cargo is effected by affixing and leaving a copy (the duty arises)` | roc7-order-33a.l4:1202 | 1 | 0 | 0 |
| `o 33 r 10(2) service on landed or transhipped cargo is effected as required` | roc7-order-33a.l4:1218 | 0 | 1 | 1 |
| `o 33 r 10(2) service on landed or transhipped cargo is effected as required (the duty arises)` | roc7-order-33a.l4:1229 | 1 | 0 | 0 |
| `o 33 r 11(5) it is the relevant period` | roc7-order-33a.l4:1239 | 1 | 0 | 0 |
| `o 33 r 11(5) it is the relevant period by (a) or (b)` | roc7-order-33a.l4:1251 | 1 | 0 | 0 |
| `o 33 r 11(1) service may be effected on the agent of the ship during the relevant period` | roc7-order-33a.l4:1271 | 1 | 1 | 0 |
| `o 33 r 11(2)(a) the warrant or originating claim is deemed served on the property` | roc7-order-33a.l4:1282 | 1 | 0 | 0 |
| `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search` | roc7-order-33a.l4:1321 | 0 | 1 | 1 |
| `o 33 r 11(3) the report of the arrest annexes the search results and states the date and time of the search (the duty arises)` | roc7-order-33a.l4:1330 | 1 | 0 | 0 |
| `o 33 r 11(4) Order 6 Rule 6(5) and (6) applies to the originating claim` | roc7-order-33a.l4:1341 | 1 | 0 | 0 |
| `o 33 r 11(4)(a) the claimant files a memorandum of service in Form 12 with the particulars` | roc7-order-33a.l4:1369 | 1 | 1 | 0 |
| `o 33 r 11(4) the claimant is entitled to enter final or interlocutory judgment in default` | roc7-order-33a.l4:1414 | 1 | 2 | 0 |
| `o 33 r 12(1) the Sheriff may apply to the Court for directions` | roc7-order-33a.l4:1432 | 1 | 1 | 0 |
| `o 33 r 12(1) the Sheriff gives notice of the application to the persons referred to in paragraph (2)` | roc7-order-33a.l4:1444 | 0 | 1 | 1 |
| `o 33 r 12(1) the Sheriff gives notice of the application to the persons referred to in paragraph (2) (the duty arises)` | roc7-order-33a.l4:1454 | 1 | 0 | 0 |
| `o 33 r 12(2) the Sheriff must send the person a copy of the order` | roc7-order-33a.l4:1474 | 0 | 1 | 0 |
| `o 33 r 12(2) the Sheriff must send the person a copy of the order (the duty arises)` | roc7-order-33a.l4:1484 | 1 | 0 | 0 |
| `o 33 r 12(3) the summons and copies of affidavits are served on the Sheriff and the persons referred to in paragraph (2)` | roc7-order-33a.l4:1496 | 1 | 1 | 1 |
| `o 33 r 12(3) the summons and copies of affidavits are served on the Sheriff and the persons referred to in paragraph (2) (the duty arises)` | roc7-order-33a.l4:1508 | 1 | 0 | 0 |
| `o 33 r 12(4) the Sheriff sends a copy of the order to all the parties to every action against the property` | roc7-order-33a.l4:1517 | 0 | 1 | 1 |
| `o 33 r 12(4) the Sheriff sends a copy of the order to all the parties to every action against the property (the duty arises)` | roc7-order-33a.l4:1526 | 1 | 0 | 0 |
| `o 33 r 13(1) the property is released only under an instrument of release in Form 54` | roc7-order-33a.l4:1537 | 1 | 1 | 1 |
| `o 33 r 13(1) the property is released only under an instrument of release in Form 54 (the duty arises)` | roc7-order-33a.l4:1549 | 1 | 0 | 0 |
| `o 33 r 13(2) a release may be issued` | roc7-order-33a.l4:1563 | 1 | 1 | 0 |
| `o 33 r 13(3) a release may be issued on the application` | roc7-order-33a.l4:1581 | 1 | 0 | 0 |
| `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued` | roc7-order-33a.l4:1597 | 0 | 1 | 1 |
| `o 33 r 13(4) the applicant has done what paragraph (4) requires before the release is issued (the duty arises)` | roc7-order-33a.l4:1607 | 1 | 0 | 0 |
| `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released` | roc7-order-33a.l4:1623 | 0 | 1 | 1 |
| `o 33 r 13(5) the party has done what paragraph (5) requires before the property is released (the duty arises)` | roc7-order-33a.l4:1633 | 1 | 0 | 0 |
| `o 33 r 13(6) the Court may vary or revoke the Sheriff's directions` | roc7-order-33a.l4:1644 | 1 | 1 | 0 |
| `o 33 r 13 an instrument of release is issued under this Rule` | roc7-order-33a.l4:1656 | 0 | 1 | 0 |
| `o 33 r 14(1) the caveat against release and payment is filed in Form 55 and entered in the record of caveats` | roc7-order-33a.l4:1671 | 0 | 1 | 1 |
| `o 33 r 14(1) the caveat against release and payment is filed in Form 55 and entered in the record of caveats (the duty arises)` | roc7-order-33a.l4:1680 | 1 | 0 | 0 |
| `o 33 r 14(2) the Court may order the person who procured the caveat to pay damages` | roc7-order-33a.l4:1691 | 1 | 1 | 0 |
| `o 33 r 15(1) the caveat is valid on the date` | roc7-order-33a.l4:1708 | 1 | 0 | 0 |
| `o 33 r 15(1) the person at whose instance a caveat was entered may withdraw it` | roc7-order-33a.l4:1717 | 0 | 1 | 0 |
| `o 33 r 15(2) the period of validity of a caveat may be extended` | roc7-order-33a.l4:1725 | 1 | 0 | 0 |
| `o 33 r 15(2) the bar on extension prevents the entry of successive caveats` | roc7-order-33a.l4:1733 | 1 | 0 | 0 |
| `o 33 r 16(1) bail is given by bond in Form 57 entered into before a commissioner for oaths or the Registrar` | roc7-order-33a.l4:1744 | 0 | 1 | 1 |
| `o 33 r 16(1) bail is given by bond in Form 57 entered into before a commissioner for oaths or the Registrar (the duty arises)` | roc7-order-33a.l4:1753 | 1 | 0 | 0 |
| `o 33 r 16(2) the surety makes an affidavit that the surety is able to pay` | roc7-order-33a.l4:1763 | 1 | 1 | 1 |
| `o 33 r 16(2) the surety makes an affidavit that the surety is able to pay (the duty arises)` | roc7-order-33a.l4:1775 | 1 | 0 | 0 |
| `o 33 r 16(3) an affidavit is to be made on behalf of the corporation` | roc7-order-33a.l4:1784 | 1 | 1 | 0 |
| `o 33 r 16(3) the affidavit required of a corporation is made by an officer` | roc7-order-33a.l4:1797 | 0 | 1 | 1 |
| `o 33 r 16(3) the affidavit required of a corporation is made by an officer (the duty arises)` | roc7-order-33a.l4:1807 | 1 | 0 | 0 |
| `o 33 r 16(4) the party giving bail serves a notice of bail and files the bond, the affidavits and the proof of service` | roc7-order-33a.l4:1819 | 0 | 1 | 1 |
| `o 33 r 16(4) the party giving bail serves a notice of bail and files the bond, the affidavits and the proof of service (the duty arises)` | roc7-order-33a.l4:1828 | 1 | 0 | 0 |
| `o 33 r 16(4) the bond may be filed at the moment` | roc7-order-33a.l4:1840 | 2 | 0 | 0 |
| `o 33 r 17(1) a person with an interest may intervene with the permission of the Court` | roc7-order-33a.l4:1865 | 1 | 1 | 0 |
| `o 33 r 17(2) the application for permission to intervene is made by summons without notice with an affidavit` | roc7-order-33a.l4:1877 | 0 | 1 | 1 |
| `o 33 r 17(2) the application for permission to intervene is made by summons without notice with an affidavit (the duty arises)` | roc7-order-33a.l4:1886 | 1 | 0 | 0 |
| `o 33 r 17(3) the intervener files and serves a notice of intention to contest or not contest` | roc7-order-33a.l4:1895 | 0 | 1 | 1 |
| `o 33 r 17(3) the intervener files and serves a notice of intention to contest or not contest (the duty arises)` | roc7-order-33a.l4:1904 | 1 | 0 | 0 |
| `o 33 r 17(3) Rule 2(3) to (6) applies to the intervener's notice with the necessary modifications` | roc7-order-33a.l4:1913 | 1 | 0 | 0 |
| `o 33 r 17(4) the Court may order the intervener to serve a pleading` | roc7-order-33a.l4:1924 | 1 | 1 | 0 |
| `o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)` | roc7-order-33b.l4:94 | 0 | 0 | 1 |
| `o 33 r 18(2) Part Two states every matter in paragraphs (r) to (u)` | roc7-order-33b.l4:111 | 0 | 0 | 1 |
| `o 33 r 18(1) the provisions of this Rule apply to the action` | roc7-order-33b.l4:122 | 1 | 1 | 0 |
| `o 33 r 18(2) the claimant files a preliminary act` | roc7-order-33b.l4:136 | 1 | 1 | 1 |
| `o 33 r 18(2) the claimant files a preliminary act (the duty arises)` | roc7-order-33b.l4:148 | 1 | 0 | 0 |
| `o 33 r 18(2) the defendant files a preliminary act` | roc7-order-33b.l4:172 | 1 | 1 | 1 |
| `o 33 r 18(2) the defendant files a preliminary act (the duty arises)` | roc7-order-33b.l4:184 | 1 | 0 | 0 |
| `o 33 r 18(3) Part Two of the preliminary act is deemed to be the pleading of the person filing it` | roc7-order-33b.l4:206 | 1 | 0 | 0 |
| `o 33 r 18(3) the provisions of these Rules relating to pleadings apply to Part Two` | roc7-order-33b.l4:215 | 1 | 0 | 0 |
| `o 33 r 18(4) the Court may order that Part Two need not be filed` | roc7-order-33b.l4:224 | 0 | 1 | 0 |
| `o 33 r 18(5) the preliminary act is sealed by the Registrar` | roc7-order-33b.l4:233 | 0 | 1 | 1 |
| `o 33 r 18(5) the preliminary act is sealed by the Registrar (the duty arises)` | roc7-order-33b.l4:242 | 1 | 0 | 0 |
| `o 33 r 18(5) a preliminary act may be inspected` | roc7-order-33b.l4:254 | 1 | 1 | 0 |
| `o 33 r 18(6) the claimant serves notice of filing the claimant's preliminary act` | roc7-order-33b.l4:267 | 0 | 1 | 1 |
| `o 33 r 18(6) the claimant serves notice of filing the claimant's preliminary act (the duty arises)` | roc7-order-33b.l4:277 | 1 | 0 | 0 |
| `o 33 r 18(7) the defendant serves notice that the defendant has filed a preliminary act` | roc7-order-33b.l4:299 | 0 | 1 | 1 |
| `o 33 r 18(7) the defendant serves notice that the defendant has filed a preliminary act (the duty arises)` | roc7-order-33b.l4:308 | 1 | 0 | 0 |
| `o 33 r 18(8) a party may inspect and bespeak a copy of another party's preliminary act` | roc7-order-33b.l4:317 | 1 | 1 | 0 |
| `o 33 r 18(9) each party serves a copy of the party's preliminary act on every other party` | roc7-order-33b.l4:328 | 0 | 1 | 1 |
| `o 33 r 18(9) each party serves a copy of the party's preliminary act on every other party (the duty arises)` | roc7-order-33b.l4:337 | 1 | 0 | 0 |
| `o 33 r 18(10) a party may apply for an order for particulars of damages and assessment` | roc7-order-33b.l4:364 | 1 | 1 | 0 |
| `o 33 r 18(11) the claim is treated as referred for assessment` | roc7-order-33b.l4:374 | 1 | 0 | 0 |
| `o 33 r 18(11) Rules 41 and 42 apply to the claim referred for assessment` | roc7-order-33b.l4:383 | 1 | 0 | 0 |
| `o 33 r 19(1) a defendant who has filed a preliminary act may apply for the action to be dismissed` | roc7-order-33b.l4:399 | 1 | 1 | 0 |
| `o 33 r 19(1) the Court may dismiss the action or make such other order` | roc7-order-33b.l4:412 | 1 | 1 | 0 |
| `o 33 r 19(2) the claimant may enter judgment against a defendant in default in an action in personam` | roc7-order-33b.l4:426 | 1 | 1 | 0 |
| `o 33 r 19(3) the claimant may apply by summons for judgment against a defendant in default in an action in rem` | roc7-order-33b.l4:439 | 1 | 1 | 0 |
| `o 33 r 19(3) the claimant must file or serve a statement of claim or an affidavit before the hearing of the summons` | roc7-order-33b.l4:449 | 1 | 0 | 0 |
| `o 33 r 19(4) the Court may make such order as it thinks just on the hearing of the summons` | roc7-order-33b.l4:458 | 1 | 1 | 0 |
| `o 33 r 19(4) the Court orders the claimant's preliminary act to be opened and requires the claimant to satisfy the Court` | roc7-order-33b.l4:471 | 0 | 1 | 1 |
| `o 33 r 19(4) the Court orders the claimant's preliminary act to be opened and requires the claimant to satisfy the Court (the duty arises)` | roc7-order-33b.l4:482 | 1 | 0 | 0 |
| `o 33 r 19(4) the claimant's evidence may be given by affidavit` | roc7-order-33b.l4:491 | 1 | 0 | 0 |
| `o 33 r 19(5) the Court may give judgment for the claim with or without a reference to the Registrar` | roc7-order-33b.l4:500 | 1 | 1 | 0 |
| `o 33 r 19(5) the Court may order the property to be appraised and sold and the proceeds paid into Court` | roc7-order-33b.l4:511 | 1 | 1 | 0 |
| `o 33 r 19(6) the Court may set aside a judgment entered in pursuance of this Rule` | roc7-order-33b.l4:522 | 0 | 1 | 0 |
| `o 33 r 19(7) a period is the prescribed period` | roc7-order-33b.l4:530 | 1 | 0 | 0 |
| `o 33 r 20(1) the claimant may serve a reply or a defence to counterclaim on the defendant` | roc7-order-33b.l4:546 | 1 | 1 | 0 |
| `o 33 r 20(2) the party gives production of electronic track data` | roc7-order-33b.l4:564 | 0 | 1 | 1 |
| `o 33 r 20(2) the party gives production of electronic track data (the duty arises)` | roc7-order-33b.l4:574 | 1 | 0 | 0 |
| `o 33 r 20(3) the party allows another party to inspect and copy the electronic track data` | roc7-order-33b.l4:612 | 0 | 1 | 1 |
| `o 33 r 20(3) the party allows another party to inspect and copy the electronic track data (the duty arises)` | roc7-order-33b.l4:622 | 1 | 0 | 0 |
| `o 33 r 21(1) the claimant may apply for judgment by default against the party who gave a caveat undertaking` | roc7-order-33b.l4:655 | 1 | 1 | 0 |
| `o 33 r 21(2) judgment given under paragraph (1) may be enforced by arrest and committal` | roc7-order-33b.l4:679 | 1 | 0 | 0 |
| `o 33 r 21(3) the claimant may apply to the Court for judgment by default` | roc7-order-33b.l4:697 | 1 | 1 | 0 |
| `o 33 r 21(4) an affidavit proving due service of the originating claim must be filed under paragraph (3)` | roc7-order-33b.l4:708 | 1 | 0 | 0 |
| `o 33 r 21(4) the required exhibit is exhibited in the affidavit verifying the facts` | roc7-order-33b.l4:719 | 0 | 1 | 1 |
| `o 33 r 21(4) the required exhibit is exhibited in the affidavit verifying the facts (the duty arises)` | roc7-order-33b.l4:730 | 1 | 0 | 0 |
| `o 33 r 21(5) the claimant may apply to the Court for judgment by default against a defendant who served no defence` | roc7-order-33b.l4:751 | 1 | 1 | 0 |
| `o 33 r 21(6) the defendant making the counterclaim may apply to the Court for judgment by default` | roc7-order-33b.l4:774 | 1 | 1 | 0 |
| `o 33 r 21(7) an application may be made under paragraph (6) against the claimant` | roc7-order-33b.l4:785 | 1 | 0 | 0 |
| `o 33 r 21(8) an application under this Rule is made by summons` | roc7-order-33b.l4:794 | 0 | 1 | 1 |
| `o 33 r 21(8) an application under this Rule is made by summons (the duty arises)` | roc7-order-33b.l4:803 | 1 | 0 | 0 |
| `o 33 r 21(8) the Court may give judgment for the claim with or without a reference to the Registrar` | roc7-order-33b.l4:813 | 1 | 1 | 0 |
| `o 33 r 21(8) the Court may order the property to be appraised and sold or make such other order` | roc7-order-33b.l4:825 | 1 | 1 | 0 |
| `o 33 r 21(9) a copy of the summons and the affidavit is served on each person mentioned in Rule 12(2)` | roc7-order-33b.l4:837 | 0 | 1 | 1 |
| `o 33 r 21(9) a copy of the summons and the affidavit is served on each person mentioned in Rule 12(2) (the duty arises)` | roc7-order-33b.l4:846 | 1 | 0 | 0 |
| `o 33 r 21(10) the Court may direct the payment of interest on the judgment` | roc7-order-33b.l4:874 | 1 | 1 | 0 |
| `o 33 r 21(10) the interest on the sum` | roc7-order-33b.l4:887 | 0 | 1 | 0 |
| `o 33 r 21(11) evidence may be given by affidavit in default actions in rem` | roc7-order-33b.l4:898 | 1 | 1 | 0 |
| `o 33 r 21(12) the Court may set aside or vary a judgment entered pursuant to this Rule` | roc7-order-33b.l4:909 | 0 | 1 | 0 |
| `o 33 r 21(13) Order 6 Rules 6(5), 7(7) and 9(3) apply to the action` | roc7-order-33b.l4:917 | 1 | 0 | 0 |
| `o 33 r 22(1) the party may apply for an order determining the order of priority` | roc7-order-33b.l4:939 | 1 | 1 | 0 |
| `o 33 r 22(2) the Court may further order` | roc7-order-33b.l4:962 | 1 | 0 | 0 |
| `o 33 r 22(3) the notice states what it must state` | roc7-order-33b.l4:1004 | 0 | 1 | 1 |
| `o 33 r 22(3) the notice states what it must state (the duty arises)` | roc7-order-33b.l4:1013 | 1 | 0 | 0 |
| `o 33 r 22(4) the Sheriff lodges in the Registry a copy of each newspaper or publication` | roc7-order-33b.l4:1022 | 0 | 1 | 1 |
| `o 33 r 22(4) the Sheriff lodges in the Registry a copy of each newspaper or publication (the duty arises)` | roc7-order-33b.l4:1031 | 1 | 0 | 0 |
| `o 33 r 22(5) the Sheriff's expenses of complying with the order are included in the expenses relating to the sale` | roc7-order-33b.l4:1040 | 0 | 1 | 1 |
| `o 33 r 22(5) the Sheriff's expenses of complying with the order are included in the expenses relating to the sale (the duty arises)` | roc7-order-33b.l4:1049 | 1 | 0 | 0 |
| `o 33 r 22(6) the application to extend the period is made by summons and a copy served on each party` | roc7-order-33b.l4:1059 | 0 | 1 | 1 |
| `o 33 r 22(6) the application to extend the period is made by summons and a copy served on each party (the duty arises)` | roc7-order-33b.l4:1068 | 1 | 0 | 0 |
| `o 33 r 22(7) a court is the Court in this Rule` | roc7-order-33b.l4:1089 | 1 | 0 | 0 |
| `o 33 r 23(1) the party requesting a commission for appraisement and sale files a commission in Form 58` | roc7-order-33b.l4:1099 | 0 | 1 | 1 |
| `o 33 r 23(1) the party requesting a commission for appraisement and sale files a commission in Form 58 (the duty arises)` | roc7-order-33b.l4:1108 | 1 | 0 | 0 |
| `o 33 r 23(2) the commission is executed by the Sheriff` | roc7-order-33b.l4:1118 | 1 | 1 | 1 |
| `o 33 r 23(2) the commission is executed by the Sheriff (the duty arises)` | roc7-order-33b.l4:1130 | 1 | 0 | 0 |
| `o 33 r 23(3) the commission for appraisement and sale cannot yet be executed for want of the undertaking` | roc7-order-33b.l4:1139 | 1 | 0 | 0 |
| `o 33 r 23(4) the Sheriff pays the gross proceeds into Court and brings the accounts into Court` | roc7-order-33b.l4:1150 | 0 | 1 | 1 |
| `o 33 r 23(4) the Sheriff pays the gross proceeds into Court and brings the accounts into Court (the duty arises)` | roc7-order-33b.l4:1159 | 1 | 0 | 0 |
| `o 33 r 23(5) a person interested in the proceeds of the sale is entitled to be heard on the assessment` | roc7-order-33b.l4:1168 | 1 | 0 | 0 |
| `o 33 r 23(5) a decision of the Registrar on the assessment may be reviewed` | roc7-order-33b.l4:1178 | 1 | 1 | 0 |
| `o 33 r 24(1) every undertaking under this Order is given in writing to the satisfaction of the Sheriff` | roc7-order-33b.l4:1191 | 0 | 1 | 1 |
| `o 33 r 24(1) every undertaking under this Order is given in writing to the satisfaction of the Sheriff (the duty arises)` | roc7-order-33b.l4:1200 | 1 | 0 | 0 |
| `o 33 r 24(2) the Sheriff may accept a deposit instead of an undertaking` | roc7-order-33b.l4:1209 | 1 | 1 | 0 |
| `o 33 r 24(3) the Court may vary or revoke a direction or determination of the Sheriff` | roc7-order-33b.l4:1221 | 1 | 1 | 0 |
| `o 33 r 25(1) a Rule of Order 14 applies to the Admiralty action` | roc7-order-33b.l4:1245 | 1 | 1 | 0 |
| `o 33 r 25(2) the money paid into Court may be paid out` | roc7-order-33b.l4:1259 | 1 | 1 | 0 |
| `o 33 r 25(3) the Registrar may order the money to be paid out with the consent of the interested parties` | roc7-order-33b.l4:1278 | 1 | 1 | 0 |
| `o 33 r 25(4) the Registrar may order the money paid into Court under Order 13 Rule 8 to be paid out` | roc7-order-33b.l4:1289 | 1 | 1 | 0 |
| `o 33 r 26(1) Order 9 Rules 8 and 9 apply to the Admiralty action` | roc7-order-33b.l4:1302 | 0 | 2 | 0 |
| `o 33 r 26(2) the order or application under Order 9 Rule 9 determines whether the trial is with assessors` | roc7-order-33b.l4:1314 | 0 | 1 | 1 |
| `o 33 r 26(2) the order or application under Order 9 Rule 9 determines whether the trial is with assessors (the duty arises)` | roc7-order-33b.l4:1323 | 1 | 0 | 0 |
| `o 33 r 26(3) an order or direction may limit the witnesses who may be called at the trial` | roc7-order-33b.l4:1332 | 1 | 1 | 0 |
| `o 33 r 26(4) an order or direction mentioned in paragraphs (2) and (3) may be varied or revoked` | roc7-order-33b.l4:1343 | 1 | 1 | 0 |
| `o 33 r 27(1) Order 9 Rule 25 applies to the Admiralty action` | roc7-order-33b.l4:1355 | 1 | 0 | 0 |
| `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts` | roc7-order-33b.l4:1370 | 1 | 1 | 1 |
| `o 33 r 27(2) the party who set the action down for trial files a Request for assessors and any preliminary acts (the duty arises)` | roc7-order-33b.l4:1383 | 1 | 0 | 0 |
| `o 33 r 27(3) Order 16 Rule 2(5) applies to the Admiralty action` | roc7-order-33b.l4:1404 | 1 | 0 | 0 |
| `o 33 r 28 the Court may stay proceedings in the firstmentioned action until security is given` | roc7-order-33b.l4:1421 | 1 | 1 | 0 |
| `o 33 r 29 the Court may order the inspection of a ship or other property` | roc7-order-33c.l4:40 | 0 | 1 | 0 |
| `o 33 r 30(1) the power under Order 9 Rule 24 extends to an examination on oath before a Judge` | roc7-order-33c.l4:50 | 1 | 1 | 0 |
| `o 33 r 30(2) the power under Order 9 Rule 24 extends to evidence taken as if before an examiner` | roc7-order-33c.l4:62 | 1 | 1 | 0 |
| `o 33 r 30(3) the order may make provision for consequential matters` | roc7-order-33c.l4:73 | 1 | 1 | 0 |
| `o 33 r 30(3)(a) the party whose witness is to be examined provides a shorthand writer` | roc7-order-33c.l4:86 | 1 | 1 | 1 |
| `o 33 r 30(3)(a) the party whose witness is to be examined provides a shorthand writer (the duty arises)` | roc7-order-33c.l4:98 | 1 | 0 | 0 |
| `o 33 r 30(3)(b) a representative of either party has authority to administer the oath` | roc7-order-33c.l4:109 | 1 | 0 | 0 |
| `o 33 r 30(3)(c) the shorthand writer certifies the transcript and the solicitor files it` | roc7-order-33c.l4:122 | 1 | 1 | 1 |
| `o 33 r 30(3)(c) the shorthand writer certifies the transcript and the solicitor files it (the duty arises)` | roc7-order-33c.l4:134 | 1 | 0 | 0 |
| `o 33 r 30(3)(d) the transcript is made available to counsel and any certificate of corrections is filed with it` | roc7-order-33c.l4:147 | 1 | 1 | 1 |
| `o 33 r 30(3)(d) the transcript is made available to counsel and any certificate of corrections is filed with it (the duty arises)` | roc7-order-33c.l4:160 | 1 | 0 | 0 |
| `o 33 r 30(4) an order authorising an examination of a witness cannot yet be made for want of the preliminary acts` | roc7-order-33c.l4:172 | 1 | 1 | 0 |
| `o 33 r 30(4) an order may be made under Order 9 Rule 24 authorising an examination of a witness` | roc7-order-33c.l4:184 | 1 | 2 | 0 |
| `o 33 r 30(5) Order 9 Rule 24 applies to the Admiralty cause or matter` | roc7-order-33c.l4:197 | 1 | 0 | 0 |
| `o 33 r 31 Order 15 Rule 4(1) to (6) applies to the order to attend court` | roc7-order-33c.l4:206 | 1 | 0 | 0 |
| `o 33 r 32(1) the proceedings for the apportionment of salvage are begun in the way required` | roc7-order-33c.l4:219 | 0 | 1 | 1 |
| `o 33 r 32(1) the proceedings for the apportionment of salvage are begun in the way required (the duty arises)` | roc7-order-33c.l4:229 | 1 | 0 | 0 |
| `o 33 r 32(2) the originating application or summons and the supporting affidavit are filed and served` | roc7-order-33c.l4:241 | 1 | 1 | 1 |
| `o 33 r 32(2) the originating application or summons and the supporting affidavit are filed and served (the duty arises)` | roc7-order-33c.l4:253 | 1 | 0 | 0 |
| `o 33 r 32(3) the Judge may exercise the powers conferred by section 175 of the Merchant Shipping Act` | roc7-order-33c.l4:275 | 1 | 1 | 0 |
| `o 33 r 33(1) a summons and the affidavits in support are filed in the Registry` | roc7-order-33c.l4:288 | 1 | 1 | 1 |
| `o 33 r 33(1) a summons and the affidavits in support are filed in the Registry (the duty arises)` | roc7-order-33c.l4:300 | 1 | 0 | 0 |
| `o 33 r 33(2) a copy of the summons and affidavits is served on all the other parties` | roc7-order-33c.l4:323 | 1 | 1 | 1 |
| `o 33 r 33(2) a copy of the summons and affidavits is served on all the other parties (the duty arises)` | roc7-order-33c.l4:335 | 1 | 0 | 0 |
| `o 33 r 33(3) paragraph (2) applies to the summons` | roc7-order-33c.l4:343 | 1 | 0 | 0 |
| `o 33 r 34 the Registrar may allow an agreement between solicitors to be filed` | roc7-order-33c.l4:355 | 0 | 1 | 0 |
| `o 33 r 34 the filed agreement becomes an order of court` | roc7-order-33c.l4:363 | 1 | 0 | 0 |
| `o 33 r 35(1) Order 15 Rule 1(1) applies to Admiralty proceedings begun by originating application` | roc7-order-33c.l4:371 | 1 | 0 | 0 |
| `o 33 r 35(2) a provision of Rule 27 applies to the Admiralty cause or matter` | roc7-order-33c.l4:382 | 1 | 1 | 0 |
| `o 33 r 36(1) the person seeking relief is the claimant in a limitation action` | roc7-order-33c.l4:399 | 1 | 0 | 0 |
| `o 33 r 36(1) the claimant is named in the originating claim by the claimant's name` | roc7-order-33c.l4:409 | 0 | 1 | 1 |
| `o 33 r 36(1) the claimant is named in the originating claim by the claimant's name (the duty arises)` | roc7-order-33c.l4:418 | 1 | 0 | 0 |
| `o 33 r 36(2) the claimant makes one of the persons with claims a defendant` | roc7-order-33c.l4:427 | 0 | 1 | 1 |
| `o 33 r 36(2) the claimant makes one of the persons with claims a defendant (the duty arises)` | roc7-order-33c.l4:436 | 1 | 0 | 0 |
| `o 33 r 36(2) the claimant may make all or any of the others defendants also` | roc7-order-33c.l4:446 | 1 | 1 | 0 |
| `o 33 r 36(3) at least one defendant is named in the originating claim by the defendant's name` | roc7-order-33c.l4:457 | 0 | 1 | 1 |
| `o 33 r 36(3) at least one defendant is named in the originating claim by the defendant's name (the duty arises)` | roc7-order-33c.l4:466 | 1 | 0 | 0 |
| `o 33 r 36(3) the other defendants may be described generally` | roc7-order-33c.l4:476 | 1 | 1 | 0 |
| `o 33 r 36(4) the originating claim is served on one or more of the defendants named by their names` | roc7-order-33c.l4:487 | 0 | 1 | 1 |
| `o 33 r 36(4) the originating claim is served on one or more of the defendants named by their names (the duty arises)` | roc7-order-33c.l4:496 | 1 | 0 | 0 |
| `o 33 r 36(4) the originating claim must be served on a defendant not named by name` | roc7-order-33c.l4:505 | 1 | 0 | 0 |
| `o 33 r 36(5) “name” includes a firm name or the name under which a person carries on business` | roc7-order-33c.l4:514 | 1 | 0 | 0 |
| `o 33 r 36(5) a person described merely as owner is deemed to have been named by name` | roc7-order-33c.l4:525 | 1 | 0 | 0 |
| `o 33 r 37(1) the Court may allow the person to constitute a limitation fund in the way` | roc7-order-33c.l4:544 | 1 | 1 | 0 |
| `o 33 r 37(3)(a) the limitation fund lapses` | roc7-order-33c.l4:578 | 1 | 0 | 0 |
| `o 33 r 37(3)(b) the money paid into Court is repaid to the person who paid it` | roc7-order-33c.l4:590 | 1 | 0 | 0 |
| `o 33 r 37(4) the money paid into Court under paragraph (1) may be paid out` | roc7-order-33c.l4:600 | 1 | 1 | 0 |
| `o 33 r 38(1) the claimant takes out a summons before the Registrar for a decree limiting liability` | roc7-order-33c.l4:614 | 0 | 1 | 1 |
| `o 33 r 38(1) the claimant takes out a summons before the Registrar for a decree limiting liability (the duty arises)` | roc7-order-33c.l4:623 | 1 | 0 | 0 |
| `o 33 r 38(2) the summons is supported by the affidavits required` | roc7-order-33c.l4:651 | 0 | 1 | 1 |
| `o 33 r 38(2) the summons is supported by the affidavits required (the duty arises)` | roc7-order-33c.l4:661 | 1 | 0 | 0 |
| `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims` | roc7-order-33c.l4:675 | 0 | 1 | 1 |
| `o 33 r 38(3) the affidavit states the names and addresses of the persons with claims (the duty arises)` | roc7-order-33c.l4:684 | 1 | 0 | 0 |
| `o 33 r 38(4) the summons and every affidavit in support are served on any defendant who has filed a notice` | roc7-order-33c.l4:694 | 1 | 1 | 1 |
| `o 33 r 38(4) the summons and every affidavit in support are served on any defendant who has filed a notice (the duty arises)` | roc7-order-33c.l4:706 | 1 | 0 | 0 |
| `o 33 r 38(5) the Court makes a decree limiting the claimant's liability` | roc7-order-33c.l4:729 | 0 | 1 | 1 |
| `o 33 r 38(5) the Court makes a decree limiting the claimant's liability (the duty arises)` | roc7-order-33c.l4:738 | 1 | 0 | 0 |
| `o 33 r 38(6) the Court gives directions for the defendant to obtain information and adjourns` | roc7-order-33c.l4:748 | 0 | 1 | 1 |
| `o 33 r 38(6) the Court gives directions for the defendant to obtain information and adjourns (the duty arises)` | roc7-order-33c.l4:757 | 1 | 0 | 0 |
| `o 33 r 38(7) the Court gives directions as to the further proceedings` | roc7-order-33c.l4:766 | 0 | 1 | 1 |
| `o 33 r 38(7) the Court gives directions as to the further proceedings (the duty arises)` | roc7-order-33c.l4:775 | 1 | 0 | 0 |
| `o 33 r 38(8) a defendant who ceases to dispute the right to limit files and serves a notice forthwith` | roc7-order-33c.l4:786 | 0 | 1 | 1 |
| `o 33 r 38(8) a defendant who ceases to dispute the right to limit files and serves a notice forthwith (the duty arises)` | roc7-order-33c.l4:796 | 1 | 0 | 0 |
| `o 33 r 38(9) the claimant may take out a summons before the Court for a decree` | roc7-order-33c.l4:805 | 1 | 1 | 0 |
| `o 33 r 39(1)(a) the decree must be advertised` | roc7-order-33c.l4:819 | 1 | 0 | 0 |
| `o 33 r 39(1)(b) the decree protects the claimant against the claim` | roc7-order-33c.l4:831 | 1 | 1 | 0 |
| `o 33 r 39(2)(a) the claimant advertises the decree in the manner and within the time the decree provides` | roc7-order-33c.l4:844 | 0 | 1 | 1 |
| `o 33 r 39(2)(a) the claimant advertises the decree in the manner and within the time the decree provides (the duty arises)` | roc7-order-33c.l4:853 | 1 | 0 | 0 |
| `o 33 r 39(2)(b) the decree fixes a time for notices, claims and summonses` | roc7-order-33c.l4:863 | 0 | 1 | 1 |
| `o 33 r 39(2)(b) the decree fixes a time for notices, claims and summonses (the duty arises)` | roc7-order-33c.l4:872 | 1 | 0 | 0 |
| `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers` | roc7-order-33c.l4:890 | 1 | 1 | 1 |
| `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers (the duty arises)` | roc7-order-33c.l4:902 | 1 | 0 | 0 |
| `o 33 r 39(4) the claimant files a copy of each newspaper in which the advertisement appears` | roc7-order-33c.l4:922 | 0 | 1 | 1 |
| `o 33 r 39(4) the claimant files a copy of each newspaper in which the advertisement appears (the duty arises)` | roc7-order-33c.l4:931 | 1 | 0 | 0 |
| `o 33 r 39(5) the time allowed is not less than 2 months from the latest date allowed for the advertisements` | roc7-order-33c.l4:941 | 1 | 1 | 1 |
| `o 33 r 39(5) the time allowed is not less than 2 months from the latest date allowed for the advertisements (the duty arises)` | roc7-order-33c.l4:953 | 1 | 0 | 0 |
| `o 33 r 39(5) the step may be taken after the time allowed has expired` | roc7-order-33c.l4:964 | 1 | 1 | 0 |
| `o 33 r 39(6) the decree may make any provision authorised by the Merchant Shipping Act` | roc7-order-33c.l4:977 | 1 | 1 | 0 |
| `o 33 r 40(1) a person with a claim may take out a summons to set the decree aside` | roc7-order-33c.l4:996 | 1 | 1 | 0 |
| `o 33 r 40(2) the summons is supported by an affidavit showing a bona fide claim and prima facie grounds` | roc7-order-33c.l4:1018 | 0 | 1 | 1 |
| `o 33 r 40(2) the summons is supported by an affidavit showing a bona fide claim and prima facie grounds (the duty arises)` | roc7-order-33c.l4:1027 | 1 | 0 | 0 |
| `o 33 r 40(3) the summons and every affidavit in support are served on the claimant and any defendant who has filed a notice` | roc7-order-33c.l4:1037 | 1 | 1 | 1 |
| `o 33 r 40(3) the summons and every affidavit in support are served on the claimant and any defendant who has filed a notice (the duty arises)` | roc7-order-33c.l4:1049 | 1 | 0 | 0 |
| `o 33 r 40(4) the Registrar sets the decree aside and gives directions` | roc7-order-33c.l4:1072 | 0 | 1 | 1 |
| `o 33 r 40(4) the Registrar sets the decree aside and gives directions (the duty arises)` | roc7-order-33c.l4:1081 | 1 | 0 | 0 |
| `o 33 r 41(1) the claiming party files the claim` | roc7-order-33c.l4:1095 | 0 | 1 | 1 |
| `o 33 r 41(1) the claiming party files the claim (the duty arises)` | roc7-order-33c.l4:1104 | 1 | 0 | 0 |
| `o 33 r 41(1) the claiming party serves a copy of the claim on every other party` | roc7-order-33c.l4:1114 | 1 | 1 | 1 |
| `o 33 r 41(1) the claiming party serves a copy of the claim on every other party (the duty arises)` | roc7-order-33c.l4:1126 | 1 | 0 | 0 |
| `o 33 r 41(2) a party may apply to the Registrar under Order 9 Rule 9 as to the proceedings on the reference` | roc7-order-33c.l4:1153 | 1 | 1 | 0 |
| `o 33 r 41(2) the Registrar gives directions on the application` | roc7-order-33c.l4:1177 | 0 | 1 | 1 |
| `o 33 r 41(2) the Registrar gives directions on the application (the duty arises)` | roc7-order-33c.l4:1186 | 1 | 0 | 0 |
| `o 33 r 41(3) the appointment of the day for the hearing is made in the way required` | roc7-order-33c.l4:1199 | 0 | 1 | 1 |
| `o 33 r 41(3) the appointment of the day for the hearing is made in the way required (the duty arises)` | roc7-order-33c.l4:1209 | 1 | 0 | 0 |
| `o 33 r 41(4) an appointment for the hearing of the reference cannot yet be made` | roc7-order-33c.l4:1221 | 2 | 0 | 0 |
| `o 33 r 41(5) the claiming party or the claimant enters the reference for hearing` | roc7-order-33c.l4:1233 | 0 | 1 | 1 |
| `o 33 r 41(5) the claiming party or the claimant enters the reference for hearing (the duty arises)` | roc7-order-33c.l4:1242 | 1 | 0 | 0 |
| `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies` | roc7-order-33c.l4:1270 | 0 | 1 | 1 |
| `o 33 r 41(6) the claiming party files the list and the affidavits and serves copies (the duty arises)` | roc7-order-33c.l4:1279 | 1 | 0 | 0 |
| `o 33 r 41(7) the Court may dismiss the claim` | roc7-order-33c.l4:1302 | 1 | 1 | 0 |
| `o 33 r 42(1) the Registrar may adjourn the hearing of a reference` | roc7-order-33c.l4:1314 | 1 | 1 | 0 |
| `o 33 r 42(2) the Registrar may give a direction limiting the witnesses` | roc7-order-33c.l4:1325 | 1 | 1 | 0 |
| `o 33 r 42(2) the direction may be revoked or varied on sufficient cause` | roc7-order-33c.l4:1337 | 1 | 1 | 0 |
| `o 33 r 42(3) evidence may be given in the manner` | roc7-order-33c.l4:1356 | 1 | 0 | 0 |
| `o 33 r 42(3) the evidence is recorded under Order 15 Rule 11(5), (6) and (7)` | roc7-order-33c.l4:1368 | 0 | 1 | 1 |
| `o 33 r 42(3) the evidence is recorded under Order 15 Rule 11(5), (6) and (7) (the duty arises)` | roc7-order-33c.l4:1377 | 1 | 0 | 0 |
| `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice` | roc7-order-33c.l4:1393 | 0 | 1 | 1 |
| `o 33 r 42(4) the Registrar reduces the decision to writing, causes it to be filed and sends notice (the duty arises)` | roc7-order-33c.l4:1402 | 1 | 0 | 0 |
| `o 33 r 42(5) a party may request a statement of the grounds of the decision` | roc7-order-33c.l4:1412 | 1 | 1 | 0 |
| `o 33 r 42 a reference is heard under this Rule` | roc7-order-33c.l4:1438 | 0 | 1 | 0 |
| `o 33 r 43(1) a party to a reference may apply to a Judge to set aside or vary the decision` | roc7-order-33c.l4:1449 | 1 | 1 | 0 |
| `o 33 r 43(2) the decision is deemed to be given on the date on which it is filed` | roc7-order-33c.l4:1487 | 1 | 0 | 0 |
| `o 33 r 43(2) the decision cannot yet be acted upon` | roc7-order-33c.l4:1496 | 1 | 0 | 0 |
| `o 33 r 43(2) the decision may be acted upon` | roc7-order-33c.l4:1505 | 1 | 1 | 0 |
| `o 33 r 43(3) a direction may be given under paragraph (2) without the parties being given an opportunity of being heard` | roc7-order-33c.l4:1516 | 1 | 0 | 0 |
| `o 33 r 43(3) the direction may be incorporated in the Registrar's decision` | roc7-order-33c.l4:1525 | 1 | 1 | 0 |
| `o 33 r 44 Order 26 Rule 3 applies to documents filed in the Registry` | roc7-order-33c.l4:1536 | 1 | 0 | 0 |
| `o 33 r 45 Rules 35 to 40 limit the right to rely by way of defence on the Merchant Shipping Act` | roc7-order-33c.l4:1545 | 1 | 0 | 0 |
| `o 33 r 46(1) the Court may order the production of documents in a marine insurance action` | roc7-order-33c.l4:1557 | 1 | 1 | 0 |
| `o 33 r 46(2) the order may be made on terms as to staying proceedings or otherwise` | roc7-order-33c.l4:1568 | 1 | 1 | 0 |

### Reading a result: FALSE and NOTHING (roc7)

Every decision function in this row answers a `MAYBE BOOLEAN`.
`JUST TRUE` is the Rules' own yes.
`JUST FALSE` is the Rules' own no, and in this row it is one of five things: a definition that says "means" (for example O 28 r 1 "entity", O 29 r 1 "specified court"), and the list that definition hands the term to (O 29 r 7); a flat negative (O 30 r 14, "No party ... may be ordered to pay any costs", answers JUST FALSE for a party in proceedings under that Order); an "if", "where", "when" or "unless" the Rules set that the facts do not meet; or a period the Rules fix in their own words that has run out (O 33 r 2(4), a notice filed on the 15th day of 14 days, answers JUST FALSE); or an "except" that names what does not apply (O 33 r 25(1), Rule 3 of Order 14).
`NOTHING` is "the Rules do not answer on these facts", and in this row it is: a bare "must" that the facts show was not done, for the compliance question (O 28 r 8(1); Order 3, Rule 2(1) subjects every requirement to the Court's discretion, so the text does not itself say no; a judgment call, see QB); a power or grant limited by its own wording once the case falls outside the limit, or an "until" bar that has ended (O 33 r 4(3): once the affidavit is filed the sentence says nothing about issuing the warrant); a duty whose trigger is unmet, where the compliance function answers NOTHING and a companion "(the duty arises)" answers JUST FALSE; a list the text does not close ("Without limiting paragraph (1), an action may be brought for the determination of any of the following questions", O 32 r 2(2)); a scope limit with no "only" ("other than a service bureau"); a silence; and a period still running with the act not yet done (O 33 r 2(4) on day 10 of 14).
A caller must never turn NOTHING into FALSE.
A question that returns NOTHING means "the Rules do not say", and the party should look to the practice directions, the Court's directions or the other Order the rule points to; it never means "no".


## Seams (roc7)

PLAN.md section 8 lists what this range asks of other parts and what other parts ask of it.
In every case below the other part's rule is not called: no import crosses parts.
The cross-reference is kept as a function, or as a BOOLEAN input named after the cross-reference, in the provision that makes it, so that the merged seat can connect it.
The one input taken from another part's answer that is not a yes/no is `o 3 r 3 the last day for doing the act` (and its variants `o 3 r 3 the last day of the validity` and `o 3 r 3 the last day of the 7 years`), a DATE (seam S-T1); `the date asked about` is the second DATE every timeliness function takes.

You ask (the answer is in another part's range):

| line | cross-reference | what roc7 does |
| --- | --- | --- |
| O 28 l 4253 | O 26 r 3 [roc6] | `o 28 r 7(3) no fee is payable by the registered user` takes the BOOLEAN "the registered user is an entity registered solely for the purpose of" the searches that O 26 r 3(1) mentions |
| O 28 l 4289 | O 3 r 6 [roc1] | `o 28 r 8(5) the form of the document is as required` takes the BOOLEAN "there is no such prescription and the document is in the form prescribed" |
| O 28 l 4371 | O 7 r 8 [roc1] | `o 28 r 12(11) the day service through the electronic filing service is deemed effected` takes the DATE `o 7 r 8 the day service is deemed effected` |
| O 30 l 4500, 4502, 4511 | O 19 whole [roc4] | `o 30 r 8(1)` to `(4)` and the directions of r 12 take BOOLEAN inputs "it is dealt with in accordance with Division 3 of Order 19 ..."; Division 3 of Order 19 is not called |
| O 31 l 4525 | O 1 r 2 [keel] | `o 31 r 1(1) this Order applies despite Order 1, Rule 2` (an override, S-L2): a flat statement about this Order that the keel's O 1 r 2 function does not thread |
| O 33 l 4580 | O 27 r 15 [roc6] | `o 33 r 1(2) an account is the Sheriff's account` (a definition over a BOOLEAN) |
| O 33 ll 4585 to 4871 | O 6 r 5, r 6, r 7, r 9 [roc1] | `o 33 r 2(3)`, `o 33 r 2(10)`, `o 33 r 11(4)`, `o 33 r 21(13)`: the statements that those Rules do or do not apply; the Rules are not called |
| O 33 l 4592, 4922 | O 16 r 2 [roc3] | `o 33 r 2(10)` and `o 33 r 27(3)`, the same way |
| O 33 l 4609 | O 8 whole [roc1] | `o 33 r 3(4) Order 8 other than Rule 4 applies to the service out of Singapore` |
| O 33 l 4830 | O 59 r 7 [roc11] | `o 33 r 19(7) a period is the prescribed period` takes a BOOLEAN naming the period fixed by r 18(2) or by the Court |
| O 33 ll 4838 to 5018 | O 9 r 7, r 8, r 9, r 25, r 24 [roc2] | `o 33 r 26(1)`, `o 33 r 27(1)`, `o 33 r 30(1)` to `(5)`, `o 33 r 41(2)`: the statements that those Rules apply; the Rules are not called |
| O 33 l 4900 | O 21 whole [roc5] | `o 33 r 23(5)` takes the BOOLEAN "the Sheriff's accounts relating to a sale are being assessed" |
| O 33 l 4905 | O 14 whole [roc2] | `o 33 r 25(1) a Rule of Order 14 applies to the Admiralty action`, over an enum of the Rules of Order 14 (the four excepted Rules answer JUST FALSE: QE) |
| O 33 l 4912, 4930 | O 13 r 8, r 2 [roc2] | `o 33 r 25(4)` and `o 33 r 29`, over BOOLEAN conditions |
| O 33 l 4930, 4944, 4954, 5030 | O 15 r 10, r 4, r 1, r 11 [roc3] | `o 33 r 31`, `o 33 r 35(1)`, `o 33 r 42(3) the evidence is recorded under Order 15 Rule 11(5), (6) and (7)` |
| O 33 l 5046 | O 26 r 3 [roc6] | `o 33 r 44 Order 26 Rule 3 applies to documents filed in the Registry` |
| O 33 l 5050 | O 11 r 2 [roc2] | `o 33 r 46(1)` takes the BOOLEAN "an application for production of documents is made by the insurer under Order 11, Rule 2" |

You are asked (another part's text cites your sections), with the names this row offers:

| citing text | asks for | roc7 offers |
| --- | --- | --- |
| O 1 [keel] l 50 | O 29A whole | the functions of `roc7-order-29.l4` named `o 29A r ...` |
| O 1 [keel] l 71, 75, 79, 83 | O 28 whole | the functions of `roc7-order-28.l4` |
| O 7 [roc1] l 635 | O 28 whole | `o 28 r 12 the moment service is deemed effected` and the `o 28 r 12(...)` functions (S-S2) |
| O 22 [roc5] l 3448 | O 33 r 25 | `o 33 r 25(1)`, `o 33 r 25(2)`, `o 33 r 25(3)`, `o 33 r 25(4)` |
| O 27 [roc6] l 4135, 4166, 4167 | O 33 whole | the functions of `roc7-order-33a.l4`, `-33b.l4` and `-33c.l4` |
| O 44 [roc9] l 6056 | O 33 r 36 | `o 33 r 36(1) the person seeking relief is the claimant in a limitation action` |
| First Schedule [roc12] l 7760 | O 33 r 5 | `o 33 r 5 a caveat against arrest is issued under this Rule` |
| Fourth Schedule [roc12] l 8385, 8408 | O 28 whole | `o 28 r 7(1) the monthly fee for a registered user`, `o 28 r 7(1) the fee for a number of months or parts of a month` |
| Fourth Schedule [roc12] ll 8462 to 8780 | O 33 r 42, r 4, r 13 | `o 33 r 42 a reference is heard under this Rule`, `o 33 r 4 a warrant of arrest is issued under this Rule`, `o 33 r 13 an instrument of release is issued under this Rule` |

Seams answered here for other parts: S-F1 `o 28 r 10 the moment the document is deemed filed`, S-F2 `o 28 r 11 the moment time for service begins to run`, S-S2 `o 28 r 12 the moment service is deemed effected` (each a Moment, with yes/no twins; fork F-28-9).
Seams found that PLAN.md does not list: none beyond the rows above; the pointer of O 22 to O 33 r 25 and the Fourth Schedule's pointers are in its "you are asked" list.


## Seat layer (roc7)

`roc7-seat.l4` asks the Orders' questions as a party to a civil action in the Singapore courts (a claimant, a defendant, a third party or an appellant) would, on facts that party can state.
It has 397 `@export` questions, each beginning "Under Order N, rule M," with the Rules' own numbering, grouped under `§` headings (one per Order) and `§§` headings (one per rule, with the rule's own heading).
Each question takes plain inputs with an `@desc`, and calls exactly one layer-1 function; no rule is restated.
A date of doing something is asked as a year, a month and a day with 0 meaning "not done yet"; the last day allowed is a DATE the party takes from Order 3, Rule 3.
Every compliance question that has a "(the duty arises)" companion (open convention question QD) is exported next to it, companion first.
There is no seat for an official: the Registrar's, the Sheriff's, the Tribunal's and the Court's own powers appear only as questions about what the party may expect or ask for.
`roc7-cases-seat.l4` has 1300 cases covering every question; each is lifted from an assertion of the called function's layer-1 tests, whose expected value was written from the text and not from output, so the seat is checked against the same expectations.
Of the cases, 449 expect JUST TRUE, 418 expect JUST FALSE, 411 expect NOTHING (the Rules do not cover the facts) and 22 expect an amount or a day.
Eight of the questions ask for an amount, a day or a time and not a yes/no (the monthly fee, the fee for a number of months, the monthly fee of an entity registered only to search or inspect, the day a fee is due, the day service through the electronic filing service is deemed effected, the day an originating claim is deemed duly served, the interest on a sum, and the time from which a bond may be filed without consent); the questions about a time of day (O 33 r 16(4)) take the day, the hour and the minute and build a `Moment` in a wiring function; the three Moment-valued seams of Order 28 (`o 28 r 10 the moment the document is deemed filed`, `o 28 r 11 the moment time for service begins to run`, `o 28 r 12 the moment service is deemed effected`) stay in layer 1, because they are inputs to other parts and a party reaches them through the yes/no questions of rules 10 to 12.
Of the 1034 `@desc` lines, 742 are the mechanical form "Is it the case that <the rule's own words>?", in the third person (for example "Is it the case that the person is designated as an authorised user under Rule 6?"), not worded as that party would be asked; a fix round can personalise them.
The seat does not expose the two functions that take the 21-matter preliminary-act record (`o 33 r 18(2) Part One states every matter in paragraphs (a) to (q)` and `... Part Two ... (r) to (u)`): the seat's rule 18(2) questions take "the document states every matter in Part One and Part Two" as one yes/no, and the checklist is in layer 1.


## Dependencies

None copied and none needed.
The staged Interpretation Act time module (`sgia-interpretation-time.l4`) is not used, because the Rules of Court count their own periods in Order 3, Rule 3, which is another part of the Rules; every period in this range is a Period constant plus a function over the last day the party states (`o 3 r 3 the last day for doing the act`), so a refreshed Order 3 can supply that DATE later.
For `encoding.json`: `"dependencies": []`.


## Unstable dialect

I looked at time (every period and validity function, and the 24-hour count of O 33 r 16(4)), versions (this range has no in-force dates and no amendments by date) and workarounds (the 84 months for 7 years in O 28 r 15(2)(c), the 21-matter record of O 33 r 18(2), the Moment functions of Order 28) in `roc7-order-28.l4`, `roc7-order-33a.l4`, `roc7-order-33b.l4` and `roc7-order-duties.l4`, and found no shape that the unstable dialect would express better, so there is no second encoding.


## Regulative rules and their traces (roc7)

Eight duties with a fixed time limit are written as regulative rules in `roc7-order-duties.l4` (PARTY ... MUST ... WITHIN ... HENCE FULFILLED LEST BREACH).
The text names no consequence of breach for any of them, so the consequence is the bare BREACH with the text's own words as the reason; no actor, deadline or remedy is invented.
Each rule has a decision-function twin in the module that holds its Order (`... in time`, over the last day the party states), which is asserted in `roc7-tests-duties.l4`.
A `#TRACE` result is an Information diagnostic, not an assertion, on both main builds, so the outcomes are recorded here, from running each trace on 1.6.109 and on 1.6.108 (`work/traces.py`, not shipped), and not asserted.
Result: all 32 outcomes are identical on the two builds; each rule is FULFILLED when the act is done at day 1 and at day n, and BREACHED at day n+1 and when the trace waits past day n.


| rule | trace | file:line | main 1.6.109 | main 1.6.108 |
| --- | --- | --- | --- | --- |
| o 33 r 2(4) | the act is done at day 1 | roc7-order-duties.l4:53 | FULFILLED | FULFILLED |
| o 33 r 2(4) | the act is done at day 14 | roc7-order-duties.l4:56 | FULFILLED | FULFILLED |
| o 33 r 2(4) | the act is done at day 15 | roc7-order-duties.l4:59 | BREACHED | BREACHED |
| o 33 r 2(4) | no act, waiting until day 15 | roc7-order-duties.l4:62 | BREACHED | BREACHED |
| o 33 r 2(5) | the act is done at day 1 | roc7-order-duties.l4:75 | FULFILLED | FULFILLED |
| o 33 r 2(5) | the act is done at day 21 | roc7-order-duties.l4:78 | FULFILLED | FULFILLED |
| o 33 r 2(5) | the act is done at day 22 | roc7-order-duties.l4:81 | BREACHED | BREACHED |
| o 33 r 2(5) | no act, waiting until day 22 | roc7-order-duties.l4:84 | BREACHED | BREACHED |
| o 33 r 5(1)(b) | the act is done at day 1 | roc7-order-duties.l4:99 | FULFILLED | FULFILLED |
| o 33 r 5(1)(b) | the act is done at day 3 | roc7-order-duties.l4:102 | FULFILLED | FULFILLED |
| o 33 r 5(1)(b) | the act is done at day 4 | roc7-order-duties.l4:105 | BREACHED | BREACHED |
| o 33 r 5(1)(b) | no act, waiting until day 4 | roc7-order-duties.l4:108 | BREACHED | BREACHED |
| o 33 r 18(9) | the act is done at day 1 | roc7-order-duties.l4:121 | FULFILLED | FULFILLED |
| o 33 r 18(9) | the act is done at day 14 | roc7-order-duties.l4:124 | FULFILLED | FULFILLED |
| o 33 r 18(9) | the act is done at day 15 | roc7-order-duties.l4:127 | BREACHED | BREACHED |
| o 33 r 18(9) | no act, waiting until day 15 | roc7-order-duties.l4:130 | BREACHED | BREACHED |
| o 33 r 20(3) | the act is done at day 1 | roc7-order-duties.l4:143 | FULFILLED | FULFILLED |
| o 33 r 20(3) | the act is done at day 14 | roc7-order-duties.l4:146 | FULFILLED | FULFILLED |
| o 33 r 20(3) | the act is done at day 15 | roc7-order-duties.l4:149 | BREACHED | BREACHED |
| o 33 r 20(3) | no act, waiting until day 15 | roc7-order-duties.l4:152 | BREACHED | BREACHED |
| o 30 r 5(2) | the act is done at day 1 | roc7-order-duties.l4:165 | FULFILLED | FULFILLED |
| o 30 r 5(2) | the act is done at day 7 | roc7-order-duties.l4:168 | FULFILLED | FULFILLED |
| o 30 r 5(2) | the act is done at day 8 | roc7-order-duties.l4:171 | BREACHED | BREACHED |
| o 30 r 5(2) | no act, waiting until day 8 | roc7-order-duties.l4:174 | BREACHED | BREACHED |
| o 33 r 41(5) | the act is done at day 1 | roc7-order-duties.l4:187 | FULFILLED | FULFILLED |
| o 33 r 41(5) | the act is done at day 14 | roc7-order-duties.l4:190 | FULFILLED | FULFILLED |
| o 33 r 41(5) | the act is done at day 15 | roc7-order-duties.l4:193 | BREACHED | BREACHED |
| o 33 r 41(5) | no act, waiting until day 15 | roc7-order-duties.l4:196 | BREACHED | BREACHED |
| o 33 r 22(2)(c) | the act is done at day 1 | roc7-order-duties.l4:209 | FULFILLED | FULFILLED |
| o 33 r 22(2)(c) | the act is done at day 14 | roc7-order-duties.l4:212 | FULFILLED | FULFILLED |
| o 33 r 22(2)(c) | the act is done at day 15 | roc7-order-duties.l4:215 | BREACHED | BREACHED |
| o 33 r 22(2)(c) | no act, waiting until day 15 | roc7-order-duties.l4:218 | BREACHED | BREACHED |

## What the text turns out to say (roc7)

1. "Deemed" is defined only for Order 28 ("deemed" means deemed until the contrary is proved, O 28 r 1, "In this Order"); the deemings of Order 33 (r 7(3)(a) and (b), r 11(2)(a), r 18(3), r 43(2)) carry no such meaning in the text, and are plain gates here.
2. The Rules count their own periods in Order 3, Rule 3, in another part; the text of Order 33 says nothing on how to count. Every period function in this range (37 timeliness or validity questions in the seat) therefore takes the last day as an input.
3. O 28 r 15(2)(c) requires the original paper affidavit to be retained for 7 years; the core's `Time unit` has Days, Clear days, Working days, Weeks, Months and Hours and no years, so the period is 84 months (NEEDS-CORE.md).
4. O 33 r 21(10) fixes interest at 5.33% per year and does not say how a year is counted (fork F-33-5); the same rate is written in O 6 r 6(7) and r 7(8), O 17 r 5 and O 21 r 29, each part in its own rule (PLAN.md).
5. O 33 r 11(5) defines the "relevant period" by whether two instruments outside the Rules are in force (regulations 61A, 61B and 61C of the Maritime and Port Authority of Singapore (Port) Regulations, and Part 3 of the Second Schedule to the COVID-19 (Temporary Measures) (Control Order) Regulations 2020); the function takes the two as yes/no inputs and does not answer whether they are in force on a date.
6. Orders 30 and 31 are addressed almost wholly to officials (the Tribunal, a Judge, the Registrar, the Attorney-General). What they say to a party: O 30 r 5 (a person notified may be heard if the person tells the Tribunal in writing within 7 days), r 14 (no costs) and r 15 (no fees); O 31 r 2(3) (who is the applicant and who a respondent) and r 4(2) (no order for costs incurred in the General Division).
7. Orders 29 and 29A name their specified countries and courts in lists: New South Wales, Dubai and Bermuda in O 29 r 6, with their courts in r 7; the People's Republic of China and the Supreme People's Court in O 29A r 4 and r 5. Rule 1 of each Order defines "specified foreign country" and "specified court" as one "specified in" the list, so a place or court not named answers JUST FALSE both at the list and at the definition (F-29-1; a judgment call, listed under QC).
8. O 33 r 18(2) requires a preliminary act of two Parts: 17 matters in Part One (paragraphs (a) to (q)) and 4 in Part Two ((r) to (u)); the record of 21 yes/no fields in `roc7-order-33b.l4` lets a party check a draft matter by matter.
9. Several rules bar something "until" an event; each bar is its own yes/no function, JUST TRUE before the event and JUST FALSE after, and none claims the event has happened: O 33 r 4(3), r 4(4), r 9(4), r 23(3), r 30(4), r 41(4) and r 43(2) (delegated-definitions ruling (d)).
10. Of the 100 rules, the ones the text gives a time limit but no consequence for missing it are eight in the regulative module (O 33 r 2(4), r 2(5), r 5(1)(b), r 18(9), r 20(3), r 22(2)(c), r 41(5) and O 30 r 5(2)); the Rules leave the consequence to the Court.

## What the text does not answer (roc7)

- The amounts, manners and forms the Rules leave to other instruments: the manner of informing the Registrar (O 28 r 7(9)) and the form of an electronic document (r 8(5)) are "set out in the practice directions"; the terms on which the Registrar may allow a user (r 6(3)); the other period the Court may specify (O 33 r 22(2)(a)); the time the decree fixes (r 39(2)(b)).
- What follows a breach of any of the eight duties with a time limit (see the regulative section): the text names none.
- How long "forthwith" is (O 33 r 7(10), r 38(8)).
- How to count any period, which is Order 3, Rule 3 (another part).
- Whether the instruments named in O 33 r 11(5) are in force on a given date.
- Whether a document served through a service bureau is "served by electronic transmission from the computer system of the authorised user or registered user" (O 28 r 12(3)(a)) or a document "remotely composed" on the provider's system (r 12(3)(b)): neither limb names a service bureau's own system, so the deemed time for that route is not stated; the functions take the two route facts as the caller's yes/no and have no input for a service-bureau route.
- O 28 r 10(6): the Registrar's power is stated for an earlier date and time only; the text grants nothing for a later one, and a caller who asks about a later date gets JUST FALSE from the unmet "earlier" condition of `o 28 r 10(6) the Registrar may cause an earlier date and time to be reflected`, which is the sentence's own "if" and not a statement by the Rules about later dates.
- O 29 (referrals on issues of law): the text states no fee payable on a referral, so no function answers one.
- O 31: whether the General Division may order the costs of the Case in its own judgment on the Case; rules 1 to 3 mention no costs, and r 4(2) says only that, in the State Court's proceedings, "no order for costs incurred in the General Division is to be made", which `o 31 r 4(2) an order for costs incurred in the General Division may be made` answers (JUST FALSE for that case, NOTHING outside it).
- O 32 r 5(2)(b): the order the Court may include, that no proceedings are to be taken under the judgment "without the permission of the Judge in person", is in the quoted words of the power; no function asks whose permission later proceedings need.
- O 33 r 3(4): whether Order 8 Rule 4 itself applies to service out of Singapore under this Rule; the text says "Order 8 (except Rule 4)", the exclusion is in the name of `o 33 r 3(4) Order 8 other than Rule 4 applies to the service out of Singapore`, and no function asks about Order 8 Rule 4.
- O 33 r 6 and r 14(2): what counts as a good and sufficient reason; it is an input (r 6: "the Court is not satisfied that the party procuring the arrest had a good and sufficient reason"; r 14(2): the same words about the person procuring the entry of the caveat) and the text gives no test.
- O 33 r 21(10): the interest runs from the date of the originating claim to the date of judgment, and the number of days between them is an input (`the number of days from the date of the originating claim to the date on which judgment is given`), not a count from two dates.
- O 33 r 24(2): the amount of a deposit the Sheriff may accept is "such sum as the Sheriff considers reasonable", an input; no function gives an amount.
- O 33 r 39(3): the number of newspapers (3) is in the name of `o 33 r 39(3) the advertisement is a single advertisement in each of 3 newspapers`; which newspapers is "specified in the decree", an input.
- Asked of this row and answered by a constant or a record, so not gaps: how long and by whom the original affidavit is kept (O 28 r 15(2)(c): the 7 years are the 84 months of `o 28 r 15(2)(c) the period of retention in months`, and the party who filed it is the bearer in the Jural relations table), and the 17 matters of Part One and 4 of Part Two of a preliminary act (O 33 r 18(2): the fields of the record).
- Every case a list the text does not close, or a grant limited by its own wording, does not describe: the QA, QC and QE sites that answer NOTHING (see Judgment calls).


## What the main binary does not accept

Measured while writing this row on main 1.6.109 and cross-checked on 1.6.108 by `check.sh` (the two builds give the same counts for every file):

- A regulative rule's `#TRACE` result is printed as an Information diagnostic and is not an assertion, so a trace cannot be asserted; the outcomes are recorded under "Regulative rules and their traces", and each duty has a decision-function twin that is asserted. An act pattern with a numeric field did not match in a trace; the acts are fieldless constructors.
- An unbracketed `NOT a OR b` did not read as I meant, so every NOT in these files is bracketed.
- The files use only the constructs the brief says main reads: no `REFUSE`, no `BECAUSE` except after `LEST BREACH BY`, no section-level `GIVEN`, no `TYPICALLY`, no sets, no `YMD` of my own, no `@lang`; constructor patterns are positional.
- A record field is read as `x's \`field\`` with a plain identifier before `'s`; a backticked name before `'s` is unproven on this build, so Moment parameters have plain names (`left`, `received`, `served`, `filed`).
- A `§§` heading must have all its text inside the backticks.
- The core has no years unit in `Time unit` (NEEDS-CORE.md).


## What check.sh prints

Run on 2026-11-05 as `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` (with the temporary directory set to the scratchpad):


```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
roc7-cases-seat.l4                             0      1300       0        0         0 |      0      1300       0        0  same
roc7-order-28.l4                               0         0       0        0         0 |      0         0       0        0  same
roc7-order-29.l4                               0         0       0        0         0 |      0         0       0        0  same
roc7-order-30.l4                               0         0       0        0         0 |      0         0       0        0  same
roc7-order-32.l4                               0         0       0        0         0 |      0         0       0        0  same
roc7-order-33a.l4                              0         0       0        0         0 |      0         0       0        0  same
roc7-order-33b.l4                              0         0       0        0         0 |      0         0       0        0  same
roc7-order-33c.l4                              0         0       0        0         0 |      0         0       0        0  same
roc7-order-duties.l4                           0         0       0        0         0 |      0         0       0        0  same
roc7-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
roc7-tests-28.l4                               0       396       0        0         0 |      0       396       0        0  same
roc7-tests-29.l4                               0       100       0        0         0 |      0       100       0        0  same
roc7-tests-30.l4                               0       164       0        0         0 |      0       164       0        0  same
roc7-tests-32.l4                               0        66       0        0         0 |      0        66       0        0  same
roc7-tests-33a.l4                              0       527       0        0         0 |      0       527       0        0  same
roc7-tests-33b.l4                              0       441       0        0         0 |      0       441       0        0  same
roc7-tests-33c.l4                              0       469       0        0         0 |      0       469       0        0  same
roc7-tests-duties.l4                           0        32       0        0         0 |      0        32       0        0  same
TOTAL (20 modules)                             0      3495       0        0           |      0      3495       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Baseline it replaced (the same script on the keel alone, `roc-core.l4` and `roc-definitions.l4`, before any roc7 file existed):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (2 modules)                              0         0       0        0           |      0         0       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

