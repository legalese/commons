# NOTES.md -- part agent ccc20: Criminal Code (Canada), R.S.C. 1985, c. C-46, Part XVI (ss 493 to 529.5)

Status: written 2026-11-16 (resumed after the weekly-limit stop of about 2026-11-12T21:20Z); every count below was produced by a script run over the files in this folder on that day, and check.sh was run on both builds after the last edit to a `.l4` file.
The state of the work is in PROGRESS.md; the types the core lacks are in NEEDS-CORE.md.

## What this is

The range is lines 11032 to 11828 of `inputs/R.S.C.-1985-c.-C-46.txt`: PART XVI, "Compelling Appearance of Accused Before a Justice and Interim Release" (arrest with and without warrant, appearance notices, undertakings, taking before a justice, information and process, interim release and its reverse onuses, review, failure to comply, delay, prisoners, endorsement of warrants, entry of a dwelling-house to arrest).
The text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation (current to 2026-09-30, last amended 2026-07-18, per `inputs/R.S.C.-1985-c.-C-46.meta.json`) under the Open Government Licence - Canada; it is NOT the official text and nothing here is claimed to have been verified against the official text.
The French version is equally authoritative and was not among the sources; the French equivalents in parentheses after a defined term are quoted, not encoded.
Where the brief and PLAN.md differ, the brief governs; the differences found are under Seams (the s 553 seam, the s 679 and s 673 inputs).

Two layers: layer 1 is the law, objectively, in eleven modules `ccc20-part16-*.l4` with tests `ccc20-tests-*.l4`; layer 2 is the seat, `ccc20-seat.l4` with `ccc20-cases-seat.l4`: a person who is, or may be, accused of an offence, asking what Part XVI says about arrest, release and detention.
The seat layer calls layer 1 and restates no rule.

| module | sections |
| --- | --- |
| `ccc20-part16-interpretation.l4` | 493, 493.01 (definitions; the reference to an indictable offence) |
| `ccc20-part16-principles.l4` | 493.1, 493.11, 493.2 (restraint, Aboriginal and vulnerable accused) |
| `ccc20-part16-arrest.l4` | 494 to 499 (arrest, appearance notice, release from custody) |
| `ccc20-part16-notices.l4` | 500 to 502.1 (appearance notices, undertakings, variation, remote attendance) |
| `ccc20-part16-taking-before-justice.l4` | 503 |
| `ccc20-part16-process.l4` | 504 to 514 (information, summons, warrant) |
| `ccc20-part16-reverse-onus.l4` | 515(4.1) to (4.4), (6), (6.1), (7), (10) (the additional conditions, the reverse onuses and the grounds of detention) |
| `ccc20-part16-interim-release.l4` | 515(1) to (5), (9), (11) to (14.1) (the order, conditions, sureties, the interim release outcome), 515.01, 515.1, 516 to 519.1 |
| `ccc20-part16-review.l4` | 520 to 523 (review, release by a judge, continuation) |
| `ccc20-part16-failure-and-delay.l4` | 523.1 to 526 (judicial referral hearing, cancellation, 90-day hearing) |
| `ccc20-part16-prisoners-and-entry.l4` | 527 to 529.5 (prisoners, endorsement of warrants, entry to arrest) |

## Coverage (ccc20)

Audit counts (script `work/units.py` and `work/cov.py`, run 2026-11-16): the range holds 797 lines, 785 of them non-blank; the units are 540 (sections 23, defined terms 9, subsections 209, paragraphs 239, subparagraphs 60); every non-blank line lies in exactly one unit (checked line by line: 0 lines missing, 0 in two units).
Rows: 0 before the table was generated (the table was not written before this run), 540 after; one row per unit.
Heading and marginal-note lines (230 of the 785) are carried inside the unit they head; they are inert for reason 1 (not operative) and have no row of their own, so no row is `inert`.

Dispositions: encoded 333; fork 190; inert 0; repealed or blank in this text 17; total 540.
A `fork` row names every fork-register entry that applies to it; the other columns say where the encoding is.
"within" means the unit is a limb or paragraph encoded inside the named function of the same section.

| unit | text lines | disposition | L4 name [module] |
| --- | --- | --- | --- |
| 493 | 11032-11036 | encoded | within `s 493 the person is an accused within the definition` [part16-interpretation] |
| 493 "accused" | 11037 | encoded | `s 493 the person is an accused within the definition` [part16-interpretation] |
| 493 "accused"(a) | 11038 | encoded | within `s 493 the person is an accused within the definition` [part16-interpretation] |
| 493 "accused"(b) | 11039 | encoded | within `s 493 the person is an accused within the definition` [part16-interpretation] |
| 493 "appearance notice" | 11040 | repealed or blank in this text | the text shows: "appearance notice [Repealed, 2019, c. 25, s. 209]" |
| 493 "judge" | 11041 | encoded | `s 493 the office the person holds` [part16-interpretation] |
| 493 "judge"(a) | 11042 | encoded | within `s 493 ordinary province` [part16-interpretation] |
| 493 "judge"(b) | 11043 | encoded | within `s 493 the office the person holds` [part16-interpretation] |
| 493 "judge"(c) | 11044 | repealed or blank in this text | the text shows: "(c) [Repealed, 1992, c. 51, s. 37]" |
| 493 "judge"(d) | 11045 | encoded | within `s 493 the office the person holds` [part16-interpretation] |
| 493 "judge"(e) | 11046 | encoded | within `s 493 territory with a Supreme Court` [part16-interpretation] |
| 493 "judge"(f) | 11047 | encoded | within `s 493 the office the person holds` [part16-interpretation] |
| 493 "officer in charge" | 11048 | repealed or blank in this text | the text shows: "officer in charge [Repealed, 2019, c. 25, s. 209]" |
| 493 "promise to appear" | 11049 | repealed or blank in this text | the text shows: "promise to appear [Repealed, 2019, c. 25, s. 209]" |
| 493 "recognizance" | 11050 | repealed or blank in this text | the text shows: "recognizance [Repealed, 2019, c. 25, s. 209]" |
| 493 "summons" | 11051 | repealed or blank in this text | the text shows: "summons [Repealed, 2019, c. 25, s. 209]" |
| 493 "undertaking" | 11052 | repealed or blank in this text | the text shows: "undertaking [Repealed, 2019, c. 25, s. 209]" |
| 493 "warrant" | 11053 | encoded | `s 493 what the warrant is for` [part16-interpretation] |
| 493.01 | 11054-11055 | fork (F-493.01-scope, F-unless-493.01) | `s 493.01 the offence charged` [part16-interpretation] |
| 493.1 | 11057-11059 | fork (F-493.1-with-493.11-2-c, F-duty-493.1, F-dutyN-493.1) | `s 493.1 the peace officer, justice or judge must give primary consideration to the release of the accused at the earliest reasonable opportunity and on the least onerous conditions that are appropriate in the circumstances` [part16-principles] |
| 493.11(1) | 11060-11061 | encoded | `s 493.11(1) section 493.1 requires the accused to be released` [part16-principles] |
| 493.11(2) | 11062-11063 | encoded | within `s 493.11(2)(a) the peace officer is barred from releasing the accused` [part16-principles] |
| 493.11(2)(a) | 11064 | fork (F-duty-493.11(2)(a), F-dutyN-493.11(2)(a)) | `s 493.11(2)(a) the peace officer is barred from releasing the accused` [part16-principles] |
| 493.11(2)(b) | 11065 | fork (F-duty-493.11(2)(b), F-dutyN-493.11(2)(b)) | `s 493.11(2)(b) the peace officer must impose the least onerous conditions that are appropriate in the circumstances` [part16-principles] |
| 493.11(2)(c) | 11066 | fork (F-493.1-with-493.11-2-c, F-duty-493.11(2)(c), F-dutyN-493.11(2)(c)) | `s 493.11(2)(c) the justice or judge is barred from giving primary consideration to the release of the accused at the earliest reasonable opportunity` [part16-principles] |
| 493.11(2)(d) | 11067 | fork (F-duty-493.11(2)(d), F-dutyN-493.11(2)(d)) | `s 493.11(2)(d) the justice or judge must impose the least onerous conditions that are appropriate in the circumstances` [part16-principles] |
| 493.11(2)(e) | 11068 | fork (F-duty-493.11(2)(e), F-dutyN-493.11(2)(e)) | `s 493.11(2)(e) the justice or judge is barred from ordering that the accused be released` [part16-principles] |
| 493.2 | 11069-11070 | fork (F-duty-493.2, F-dutyN-493.2) | `s 493.2(a) the accused is an Aboriginal accused, to whose circumstances particular attention must be given` [part16-principles] |
| 493.2(a) | 11071 | fork (F-duty-493.2(a)) | within `s 493.2(a) the accused is an Aboriginal accused, to whose circumstances particular attention must be given` [part16-principles] |
| 493.2(b) | 11072 | fork (F-duty-493.2(b)) | `s 493.2(b) the accused belongs to a vulnerable population, to whose circumstances particular attention must be given` [part16-principles] |
| 494(1) | 11074-11076 | encoded | `s 494(1) any one may arrest the person without warrant` [part16-arrest] |
| 494(1)(a) | 11077 | encoded | within `s 494(1) any one may arrest the person without warrant` [part16-arrest] |
| 494(1)(b) | 11078 | encoded | within `s 494(1) any one may arrest the person without warrant` [part16-arrest] |
| 494(1)(b)(i) | 11079 | encoded | within `s 494(1) any one may arrest the person without warrant` [part16-arrest] |
| 494(1)(b)(ii) | 11080 | encoded | within `s 494(1) any one may arrest the person without warrant` [part16-arrest] |
| 494(2) | 11081-11082 | fork (F-may-494(2)) | `s 494(2) the owner of property, or a person acting for the owner, may arrest the person without a warrant` [part16-arrest] |
| 494(2)(a) | 11083 | encoded | within `s 494(2) the owner of property, or a person acting for the owner, may arrest the person without a warrant` [part16-arrest] |
| 494(2)(b) | 11084 | encoded | within `s 494(2) the owner of property, or a person acting for the owner, may arrest the person without a warrant` [part16-arrest] |
| 494(3) | 11085-11086 | fork (F-duty-494(3), F-other-494(3)) | `s 494(3) the arrester must forthwith deliver the person to a peace officer` [part16-arrest] |
| 494(4) | 11087-11088 | encoded | `s 494(4) the person is authorized by law to make the arrest for the purposes of section 25` [part16-arrest] |
| 495(1) | 11089-11090 | encoded | `s 495(1) the peace officer may arrest the person without warrant` [part16-arrest] |
| 495(1)(a) | 11091 | encoded | within `s 495(1) the peace officer may arrest the person without warrant` [part16-arrest] |
| 495(1)(b) | 11092 | encoded | within `s 495(1) the peace officer may arrest the person without warrant` [part16-arrest] |
| 495(1)(c) | 11093 | encoded | within `s 495(1) the peace officer may arrest the person without warrant` [part16-arrest] |
| 495(2) | 11094-11095 | fork (F-duty-495(2), F-dutyN-495(2)) | `s 495(2)(d) a circumstance the text names` [part16-arrest] |
| 495(2)(a) | 11096 | encoded | within `s 495(2)(d) a circumstance the text names` [part16-arrest] |
| 495(2)(b) | 11097 | encoded | within `s 495(2)(d) a circumstance the text names` [part16-arrest] |
| 495(2)(c) | 11098-11099 | encoded | within `s 495(2)(d) a circumstance the text names` [part16-arrest] |
| 495(2)(d) | 11100 | encoded | within `s 495(2)(d) a circumstance the text names` [part16-arrest] |
| 495(2)(d)(i) | 11101 | encoded | within `s 495(2)(d) the circumstance is a need the text names` [part16-arrest] |
| 495(2)(d)(ii) | 11102 | encoded | within `s 495(2)(d) the circumstance is a need the text names` [part16-arrest] |
| 495(2)(d)(iii) | 11103-11104 | encoded | within `s 495(2)(d) the circumstance is a need the text names` [part16-arrest] |
| 495(2)(e) | 11105 | encoded | within `s 495(2)(d) a circumstance the text names` [part16-arrest] |
| 495(3) | 11106-11107 | fork (F-unless-495(3)) | `s 495(3) the peace officer is deemed to be acting lawfully and in the execution of their duty` [part16-arrest] |
| 495(3)(a) | 11108 | encoded | within `s 495(3) the peace officer is deemed to be acting lawfully and in the execution of their duty` [part16-arrest] |
| 495(3)(b) | 11109 | encoded | within `s 495(3) the peace officer is deemed to be acting lawfully and in the execution of their duty` [part16-arrest] |
| 495.1 | 11110-11111 | fork (F-may-495.1) | `s 495.1 the peace officer may arrest the accused without a warrant to take them before a judge or justice under section 524` [part16-arrest] |
| 496 | 11112-11113 | fork (F-may-496) | `s 496 the peace officer may, without laying a charge, issue an appearance notice to attend a judicial referral hearing` [part16-arrest] |
| 497 | 11114-11115 | fork (F-may-497) | `s 497 the peace officer may issue an appearance notice to the person` [part16-arrest] |
| 497(a) | 11116 | encoded | within `s 497 the peace officer may issue an appearance notice to the person` [part16-arrest] |
| 497(b) | 11117 | encoded | within `s 497 the peace officer may issue an appearance notice to the person` [part16-arrest] |
| 497(c) | 11118 | encoded | within `s 497 the peace officer may issue an appearance notice to the person` [part16-arrest] |
| 498(1) | 11119-11120 | fork (F-duty-498(1), F-other-498(1)) | within `s 498(1) how the release is to be effected` [part16-arrest] |
| 498(1)(a) | 11121 | encoded | within `s 498(1) how the release is to be effected` [part16-arrest] |
| 498(1)(b) | 11122 | encoded | within `s 498(1) how the release is to be effected` [part16-arrest] |
| 498(1)(c) | 11123 | encoded | within `s 498(1) how the release is to be effected` [part16-arrest] |
| 498(1.01) | 11124-11125 | encoded | within `s 498(1) how the release is to be effected` [part16-arrest] |
| 498(1.1) | 11126-11127 | fork (F-duty-498(1.1)) | `s 498(1.1)(a) a circumstance the text names` [part16-arrest] |
| 498(1.1)(a) | 11128 | encoded | within `s 498(1.1)(a) a circumstance the text names` [part16-arrest] |
| 498(1.1)(a)(i) | 11129 | encoded | within `s 498(1.1)(a) the circumstance is a need the text names` [part16-arrest] |
| 498(1.1)(a)(ii) | 11130 | encoded | within `s 498(1.1)(a) the circumstance is a need the text names` [part16-arrest] |
| 498(1.1)(a)(iii) | 11131 | encoded | within `s 498(1.1)(a) the circumstance is a need the text names` [part16-arrest] |
| 498(1.1)(a)(iv) | 11132 | encoded | within `s 498(1.1)(a) the circumstance is a need the text names` [part16-arrest] |
| 498(1.1)(b) | 11133 | encoded | within `s 498(1.1)(a) a circumstance the text names` [part16-arrest] |
| 498(2) | 11134-11135 | encoded | within `s 498(3) the peace officer is deemed to be acting lawfully and in the execution of the officer's duty` [part16-arrest] |
| 498(3) | 11136-11137 | fork (F-unless-498(3)) | within `s 498(3) the peace officer is deemed to be acting lawfully and in the execution of the officer's duty` [part16-arrest] |
| 498(3)(a) | 11138 | encoded | within `s 498(3) the peace officer is deemed to be acting lawfully and in the execution of the officer's duty` [part16-arrest] |
| 498(3)(b) | 11139 | encoded | within `s 498(3) the peace officer is deemed to be acting lawfully and in the execution of the officer's duty` [part16-arrest] |
| 499 | 11140-11141 | fork (F-may-499) | `s 499 a peace officer may release the person arrested with a warrant` [part16-arrest] |
| 499(a) | 11142 | encoded | within `s 499 a peace officer may release the person arrested with a warrant` [part16-arrest] |
| 499(b) | 11143 | encoded | within `s 499 a peace officer may release the person arrested with a warrant` [part16-arrest] |
| 500(1) | 11144-11145 | encoded | `s 500(1) the appearance notice meets the requirements of paragraphs (a) to (d)` [part16-notices] |
| 500(1)(a) | 11146 | encoded | within `s 500(1) the appearance notice meets the requirements of paragraphs (a) to (d)` [part16-notices] |
| 500(1)(b) | 11147 | encoded | within `s 500(1) the appearance notice meets the requirements of paragraphs (a) to (d)` [part16-notices] |
| 500(1)(c) | 11148 | encoded | within `s 500(1) the appearance notice meets the requirements of paragraphs (a) to (d)` [part16-notices] |
| 500(1)(d) | 11149 | encoded | within `s 500(1) the appearance notice meets the requirements of paragraphs (a) to (d)` [part16-notices] |
| 500(2) | 11150-11151 | encoded | `s 500(2) the appearance notice sets out the required summary` [part16-notices] |
| 500(3) | 11152-11153 | fork (F-may-500(3)) | `s 500(3) the appearance notice may require the accused to appear for the purposes of the Identification of Criminals Act` [part16-notices] |
| 500(4) | 11154-11155 | encoded | `s 500(4) the officer has done what subsection (4) requires about the signature` [part16-notices] |
| 501(1) | 11156-11157 | encoded | `s 501(1) the undertaking sets out the required contents` [part16-notices] |
| 501(1)(a) | 11158 | encoded | within `s 501(1) the undertaking sets out the required contents` [part16-notices] |
| 501(1)(b) | 11159 | encoded | within `s 501(1) the undertaking sets out the required contents` [part16-notices] |
| 501(1)(c) | 11160 | encoded | within `s 501(1) the undertaking sets out the required contents` [part16-notices] |
| 501(2) | 11161-11162 | encoded | `s 501(2) the undertaking contains the mandatory condition` [part16-notices] |
| 501(3) | 11163-11164 | fork (F-may-501(3)) | `s 501(3) the condition` [part16-notices] |
| 501(3)(a) | 11165 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(b) | 11166 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(c) | 11167 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(d) | 11168 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(e) | 11169 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(f) | 11170 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(g) | 11171 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(h) | 11172 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(i) | 11173 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(j) | 11174 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(3)(k) | 11175 | encoded | within `s 501(3) the condition` [part16-notices] |
| 501(4) | 11176-11177 | fork (F-may-501(4)) | `s 501(4) the undertaking may require the accused to appear for the purposes of the Identification of Criminals Act` [part16-notices] |
| 501(5) | 11178-11179 | encoded | `s 501(5) the officer has delivered the deposit to a justice as required` [part16-notices] |
| 501(6) | 11180-11181 | encoded | `s 501(6) the officer has done what subsection (6) requires about the signature` [part16-notices] |
| 502(1) | 11182-11183 | encoded | `s 502(1) the undertaking may be varied` [part16-notices] |
| 502(2) | 11184-11185 | fork (F-may-502(2)) | `s 502(2) the accused or the prosecutor may apply to a justice` [part16-notices] |
| 502(2)(a) | 11186 | encoded | within `s 502(2) the accused or the prosecutor may apply to a justice` [part16-notices] |
| 502(2)(b) | 11187-11188 | encoded | within `s 502(2) the accused or the prosecutor may apply to a justice` [part16-notices] |
| 502.1(1) | 11190-11192 | fork (F-may-502.1(1), F-unless-502.1(1)) | `s 502.1(1) the accused must appear in person` [part16-notices] |
| 502.1(2) | 11193-11194 | fork (F-may-502.1(2)) | `s 502.1(2) the witness in Canada may give evidence by audioconference or videoconference` [part16-notices] |
| 502.1(3) | 11195-11196 | encoded | `s 502.1(3) sections 714.2 to 714.8 apply` [part16-notices] |
| 502.1(4) | 11197-11198 | fork (F-may-502.1(4)) | `s 502.1(4) the participant may participate by audioconference or videoconference` [part16-notices] |
| 502.1(5) | 11199-11200 | fork (F-may-502.1(5)) | `s 502.1(5) the justice may preside by audioconference or videoconference` [part16-notices] |
| 503(1) | 11201-11202 | fork (F-duty-503(1)) | `s 503(1) the peace officer must cause the person to be taken before a justice` [part16-taking-before-justice] |
| 503(1)(a) | 11203 | encoded | within `s 503(1) the person was taken before a justice as paragraph (a) or (b) requires` [part16-taking-before-justice] |
| 503(1)(b) | 11204 | encoded | within `s 503(1) the person was taken before a justice as paragraph (a) or (b) requires` [part16-taking-before-justice] |
| 503(1.1) | 11205-11206 | fork (F-duty-503(1.1)) | `s 503(1.1) the peace officer must release the person` [part16-taking-before-justice] |
| 503(1.1)(a) | 11207 | encoded | within `s 503(1.1) the peace officer must release the person` [part16-taking-before-justice] |
| 503(1.1)(b) | 11208 | encoded | within `s 503(1.1) the peace officer must release the person` [part16-taking-before-justice] |
| 503(2) | 11209-11210 | encoded | `s 503(2) the hours that run against the 24-hour period` [part16-taking-before-justice] |
| 503(2.1) | 11211 | repealed or blank in this text | the text shows: "(2.1) [Repealed, 2019, c. 25, s. 217]" |
| 503(2.2) | 11212 | repealed or blank in this text | the text shows: "(2.2) [Repealed, 2019, c. 25, s. 217]" |
| 503(2.3) | 11213 | repealed or blank in this text | the text shows: "(2.3) [Repealed, 2019, c. 25, s. 217]" |
| 503(3) | 11214-11215 | fork (F-duty-503(3), F-unless-503(3)) | within `s 503(3) the person must, within the time prescribed in paragraph (1)(a) or (b), be taken before a justice within whose jurisdiction the person was arrested` [part16-taking-before-justice] |
| 503(3)(a) | 11216 | fork (F-duty-503(3)(a)) | `s 503(3)(a) the justice must release the person` (+1 more) [part16-taking-before-justice] |
| 503(3)(b) | 11217 | fork (F-may-503(3)(b), F-where-503(3)(b)) | `s 503(3)(b) the justice may take that step` [part16-taking-before-justice] |
| 503(3)(b)(i) | 11218 | fork (F-duty-503(3)(b)(i)) | `s 503(3)(b)(i) the person in whose custody the person then is must release them` [part16-taking-before-justice] |
| 503(3)(b)(ii) | 11219 | encoded | within `s 503(3)(b) the justice may take that step` [part16-taking-before-justice] |
| 503(3.1) | 11220-11221 | encoded | `s 503(3.1) the release ordered` [part16-taking-before-justice] |
| 503(3.1)(a) | 11222 | encoded | within `s 503(3.1) the justice may order the person released` [part16-taking-before-justice] |
| 503(3.1)(b) | 11223 | encoded | within `s 503(3.1) the justice may order the person released` [part16-taking-before-justice] |
| 503(4) | 11224-11225 | fork (F-duty-503(4)) | `s 503(4) the peace officer must release the person as soon as practicable` [part16-taking-before-justice] |
| 503(5) | 11226-11227 | fork (F-unless-503(5)) | `s 503(5) the peace officer is deemed to be acting lawfully and in the execution of the peace officer's duty` [part16-taking-before-justice] |
| 503(5)(a) | 11228 | encoded | within `s 503(5) the peace officer is deemed to be acting lawfully and in the execution of the peace officer's duty` [part16-taking-before-justice] |
| 503(5)(b) | 11229 | encoded | within `s 503(5) the peace officer is deemed to be acting lawfully and in the execution of the peace officer's duty` [part16-taking-before-justice] |
| 504 | 11231-11233 | fork (F-may-504, F-duty-504) | `s 504 any one may lay an information in writing and under oath before a justice` [part16-process] |
| 504(a) | 11234 | encoded | within `s 504 the justice must receive the information` [part16-process] |
| 504(a)(i) | 11235 | encoded | within `s 504 the justice must receive the information` [part16-process] |
| 504(a)(ii) | 11236-11237 | encoded | within `s 504 the justice must receive the information` [part16-process] |
| 504(b) | 11238 | encoded | within `s 504 the justice must receive the information` [part16-process] |
| 504(c) | 11239 | encoded | within `s 504 the justice must receive the information` [part16-process] |
| 504(d) | 11240 | encoded | within `s 504 the justice must receive the information` [part16-process] |
| 505 | 11241-11242 | fork (F-duty-505) | `s 505 an information must be laid before a justice` [part16-process] |
| 506 | 11243-11244 | encoded | `s 506 the information may be in Form 2` [part16-process] |
| 507(1) | 11245-11246 | fork (F-duty-507(1), F-other-507(1), F-unless-507(1)) | `s 507(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 507(1)(a) | 11247 | encoded | within `s 507(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 507(1)(a)(i) | 11248 | encoded | within `s 507(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 507(1)(a)(ii) | 11249 | encoded | within `s 507(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 507(1)(a.1) | 11250 | fork (F-duty-507(1)(a.1)) | `s 507(1)(a.1) the hearing must be held in camera` [part16-process] |
| 507(1)(b) | 11251 | fork (F-duty-507(1)(b)) | `s 507(1)(b) the justice must issue a summons or a warrant for the arrest of the accused` [part16-process] |
| 507(2) | 11252-11253 | fork (F-dutyN-507(2)) | `s 507(2) the justice must not refuse to issue a summons or warrant` [part16-process] |
| 507(3) | 11254-11255 | fork (F-duty-507(3)) | `s 507(3) the justice must take the evidence on oath and in accordance with section 540` [part16-process] |
| 507(3)(a) | 11256 | encoded | within `s 507(3) the justice must take the evidence on oath and in accordance with section 540` [part16-process] |
| 507(3)(b) | 11257 | encoded | within `s 507(3) the justice must take the evidence on oath and in accordance with section 540` [part16-process] |
| 507(4) | 11258-11259 | fork (F-duty-507(4), F-unless-507(4)) | `s 507(4) the justice must issue a summons to the accused` [part16-process] |
| 507(5) | 11260-11261 | fork (F-duty-507(5)) | `s 507(5) the justice is barred from signing the summons or warrant` [part16-process] |
| 507(6) | 11262-11263 | encoded | `s 507(6) the justice may authorize the release of the accused under section 499 by endorsing the warrant in Form 29` [part16-process] |
| 507(7) | 11264-11265 | encoded | `s 507(7) the appearance notice or undertaking is deemed to have been confirmed by a justice under section 508` [part16-process] |
| 507(8) | 11266-11267 | fork (F-where-507(8)) | `s 507(8) a justice may issue a summons or a warrant for the arrest of the accused to compel attendance` [part16-process] |
| 507.1(1) | 11268-11269 | fork (F-other-507.1(1)) | `s 507.1(1) the justice must refer the information to a provincial court judge, a judge of the Court of Quebec or a designated justice` [part16-process] |
| 507.1(2) | 11270-11271 | fork (F-duty-507.1(2)) | `s 507.1(2) the judge or designated justice must issue a summons or warrant for the arrest of the accused` [part16-process] |
| 507.1(3) | 11272-11273 | encoded | `s 507.1(3) the conditions for issuing a summons or warrant are all met` [part16-process] |
| 507.1(3)(a) | 11274 | encoded | within `s 507.1(3) the conditions for issuing a summons or warrant are all met` [part16-process] |
| 507.1(3)(b) | 11275 | encoded | within `s 507.1(3) the conditions for issuing a summons or warrant are all met` [part16-process] |
| 507.1(3)(c) | 11276 | encoded | within `s 507.1(3) the conditions for issuing a summons or warrant are all met` [part16-process] |
| 507.1(3)(d) | 11277 | encoded | within `s 507.1(3) the conditions for issuing a summons or warrant are all met` [part16-process] |
| 507.1(4) | 11278-11279 | encoded | `s 507.1(4) the Attorney General is deemed to intervene in the proceeding by appearing at the hearing` [part16-process] |
| 507.1(5) | 11280-11281 | fork (F-month-end, F-duty-507.1(5), F-unless-507.1(5)) | `s 507.1(5) the judge or designated justice must endorse the information with a statement to that effect` [part16-process] |
| 507.1(6) | 11282-11283 | encoded | `s 507.1(6) the information is deemed never to have been laid after the proceedings` [part16-process] |
| 507.1(7) | 11284-11285 | fork (F-duty-507.1(7), F-unless-507.1(7)) | `s 507.1(7) another hearing under paragraph (3)(a) on the offence or an included offence is barred` [part16-process] |
| 507.1(8) | 11286-11287 | encoded | `s 507.1(8) subsections 507(2) to (8) apply` [part16-process] |
| 507.1(9) | 11288-11289 | encoded | `s 507.1(9) subsections (1) to (8) apply to the information` [part16-process] |
| 507.1(10) | 11290-11291 | encoded | `s 507.1(10) the justice is a designated justice` [part16-process] |
| 507.1(11) | 11292-11293 | encoded | `s 507.1(11) the person is the Attorney General for the purposes of section 507.1` [part16-process] |
| 508(1) | 11294-11295 | fork (F-duty-508(1)) | within `s 508(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 508(1)(a) | 11296 | encoded | within `s 508(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 508(1)(a)(i) | 11297 | encoded | within `s 508(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 508(1)(a)(ii) | 11298 | encoded | within `s 508(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` [part16-process] |
| 508(1)(a.1) | 11299 | fork (F-duty-508(1)(a.1)) | `s 508(1)(a.1) the hearing must be held in camera` [part16-process] |
| 508(1)(b) | 11300 | fork (F-duty-508(1)(b), F-dutyN-508(1)(b)) | `s 508(1)(b) the justice must take that step` [part16-process] |
| 508(1)(b)(i) | 11301 | encoded | within `s 508(1)(b) the justice must take that step` [part16-process] |
| 508(1)(b)(ii) | 11302 | encoded | within `s 508(1)(b) the justice must take that step` [part16-process] |
| 508(1)(b)(iii) | 11303 | encoded | within `s 508(1)(b) the justice must take that step` [part16-process] |
| 508(1)(c) | 11304 | fork (F-duty-508(1)(c)) | `s 508(1)(c) the justice must cancel the appearance notice or undertaking and cause the accused to be immediately notified` [part16-process] |
| 508(2) | 11305-11306 | fork (F-duty-508(2)) | `s 508(2) the justice must take the evidence on oath and in accordance with section 540` [part16-process] |
| 508(2)(a) | 11307 | encoded | within `s 508(2) the justice must take the evidence on oath and in accordance with section 540` [part16-process] |
| 508(2)(b) | 11308 | encoded | within `s 508(2) the justice must take the evidence on oath and in accordance with section 540` [part16-process] |
| 508.1(1) | 11309-11310 | encoded | within `s 508.1(1) the peace officer may lay the information by a means of telecommunication` [part16-process] |
| 508.1(2) | 11311-11312 | encoded | within `s 508.1(1) the peace officer may lay the information by a means of telecommunication` [part16-process] |
| 509(1) | 11313-11314 | encoded | `s 509(1) the summons meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 509(1)(a) | 11315 | encoded | within `s 509(1) the summons meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 509(1)(b) | 11316 | encoded | within `s 509(1) the summons meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 509(1)(c) | 11317 | encoded | within `s 509(1) the summons meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 509(2) | 11318-11319 | encoded | `s 509(2) the summons has been served as the subsection requires` [part16-process] |
| 509(3) | 11320 | repealed or blank in this text | the text shows: "(3) [Repealed, 2008, c. 18, s. 17]" |
| 509(4) | 11321-11322 | encoded | `s 509(4) the summons sets out the required summary` [part16-process] |
| 509(5) | 11323-11324 | fork (F-may-509(5)) | `s 509(5) the summons may require the accused to appear for the purposes of the Identification of Criminals Act` [part16-process] |
| 510 | 11325 | repealed or blank in this text | the text shows: "510 [Repealed, 2019, c. 25, s. 222]" |
| 511(1) | 11326-11327 | encoded | `s 511(1) the warrant meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 511(1)(a) | 11328 | encoded | within `s 511(1) the warrant meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 511(1)(b) | 11329 | encoded | within `s 511(1) the warrant meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 511(1)(c) | 11330 | encoded | within `s 511(1) the warrant meets the requirements of paragraphs (a) to (c)` [part16-process] |
| 511(2) | 11331-11332 | encoded | `s 511(2) the warrant remains in force` [part16-process] |
| 511(2.1) | 11333-11334 | fork (F-may-511(2.1), F-where-511(2.1)) | `s 511(2.1) the judge or justice may cancel the warrant` [part16-process] |
| 511(3) | 11335-11336 | encoded | `s 511(3) the judge or justice may specify a period before which the warrant shall not be executed` [part16-process] |
| 511(4) | 11337-11338 | encoded | `s 511(4) the warrant is deemed to be executed` [part16-process] |
| 512(1) | 11339-11340 | fork (F-where-512(1)) | `s 512(1) a prior step` [part16-process] |
| 512(1)(a) | 11341 | encoded | within `s 512(1) the justice may issue a summons or warrant notwithstanding the prior step` [part16-process] |
| 512(1)(b) | 11342 | encoded | within `s 512(1) the justice may issue a summons or warrant notwithstanding the prior step` [part16-process] |
| 512(1)(c) | 11343 | encoded | within `s 512(1) the justice may issue a summons or warrant notwithstanding the prior step` [part16-process] |
| 512(2) | 11344-11345 | fork (F-where-512(2)) | `s 512(2) a justice may issue a warrant for the arrest of the accused` [part16-process] |
| 512(2)(a) | 11346 | encoded | within `s 512(2) a justice may issue a warrant for the arrest of the accused` [part16-process] |
| 512(2)(b) | 11347 | encoded | within `s 512(2) a justice may issue a warrant for the arrest of the accused` [part16-process] |
| 512(2)(c) | 11348-11350 | encoded | within `s 512.1 a justice may issue a warrant for the arrest of the accused for the offence` [part16-process] |
| 512.1 | 11351 | fork (F-may-512.1) | `s 512.1 a justice may issue a warrant for the arrest of the accused for the offence` [part16-process] |
| 512.2 | 11352-11353 | fork (F-may-512.2) | `s 512.2 a justice may issue a warrant for the arrest of the accused for the offence` [part16-process] |
| 512.3 | 11354-11355 | fork (F-may-512.3) | `s 512.3 a justice may issue a warrant to take the accused before a justice under section 524` [part16-process] |
| 513 | 11356-11357 | encoded | `s 513 the warrant is directed as the section requires` [part16-process] |
| 514(1) | 11358-11359 | encoded | `s 514(1) the warrant may be executed by arresting the accused where the accused is found` [part16-process] |
| 514(1)(a) | 11360 | encoded | within `s 514(1) the warrant may be executed by arresting the accused where the accused is found` [part16-process] |
| 514(1)(b) | 11361 | encoded | within `s 514(1) the warrant may be executed by arresting the accused where the accused is found` [part16-process] |
| 514(2) | 11362-11363 | encoded | `s 514(2) the person may execute the warrant, whether or not the place is within the territory for which the person is a peace officer` [part16-process] |
| 515(1) | 11365-11367 | fork (F-duty-515(1), F-other-515(1), F-unless-515(1)) | within `s 515 the accused is bound by a release order` [part16-interim-release] |
| 515(2) | 11368-11369 | fork (F-unless-515(2)) | `s 515(2) the justice must make a release order that sets out the conditions directed under subsection (4)` [part16-interim-release] |
| 515(2)(a) | 11370 | encoded | within `s 515(2) the financial term of the release order` [part16-interim-release] |
| 515(2)(b) | 11371 | encoded | within `s 515(2) the financial term of the release order` [part16-interim-release] |
| 515(2)(c) | 11372 | encoded | within `s 515(2) the financial term of the release order` [part16-interim-release] |
| 515(2)(d) | 11373 | encoded | within `s 515(2) the financial term of the release order` [part16-interim-release] |
| 515(2)(e) | 11374 | encoded | within `s 515(2) the financial term of the release order` [part16-interim-release] |
| 515(2.01) | 11375-11376 | fork (F-duty-515(2.01), F-dutyN-515(2.01), F-unless-515(2.01)) | within `s 515(2.01) the justice is barred from making an order containing the term` [part16-interim-release] |
| 515(2.02) | 11377-11378 | fork (F-duty-515(2.02)) | `s 515(2.02) the justice must favour a promise to pay an amount over the deposit of an amount of money` [part16-interim-release] |
| 515(2.03) | 11379-11380 | fork (F-duty-515(2.03)) | `s 515(2.03) the justice must be satisfied that a surety is the least onerous form of release possible for the accused` [part16-interim-release] |
| 515(2.04) | 11381-11382 | encoded | `s 515(2.04) subsection (2.01) applies to the accused` [part16-interim-release] |
| 515(2.1) | 11383-11384 | fork (F-may-515(2.1)) | `s 515(2.1) the judge, justice or court may name particular persons as sureties` [part16-interim-release] |
| 515(2.11) | 11385-11386 | fork (F-ten-years, F-duty-515(2.11), F-unless-515(2.11)) | `s 515(2.11) the judge, justice or court is barred from naming the person as surety` [part16-interim-release] |
| 515(2.12) | 11387-11388 | fork (F-duty-515(2.12)) | `s 515(2.12) the judge, justice or court must include in the record a statement of the reasons for naming the person` [part16-interim-release] |
| 515(2.2) | 11389-11390 | fork (F-may-515(2.2), F-duty-515(2.2)) | within `s 515(2.2) the accused must appear in person` [part16-interim-release] |
| 515(2.3) | 11391-11392 | encoded | `s 515(2.3) the consent of the prosecutor and the accused is required for the appearance of the accused by audioconference` [part16-interim-release] |
| 515(3) | 11393-11394 | fork (F-dutyN-515(3)) | `s 515(3) a factor` [part16-interim-release] |
| 515(3)(a) | 11395 | encoded | within `s 515(3) the justice must consider the factor` [part16-interim-release] |
| 515(3)(a.1) | 11396 | encoded | within `s 515(3) the justice must consider the factor` [part16-interim-release] |
| 515(3)(b) | 11397 | encoded | within `s 515(3) the justice must consider the factor` [part16-interim-release] |
| 515(4) | 11398-11399 | fork (F-where-515(4)) | `s 515(4) the justice may direct the accused to comply with the condition` [part16-interim-release] |
| 515(4)(a) | 11400 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4)(b) | 11401 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4)(c) | 11402 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4)(d) | 11403 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4)(e) | 11404 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4)(f) | 11405 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4)(g) | 11406 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4)(h) | 11407-11408 | encoded | within `s 515(4) the condition` [part16-interim-release] |
| 515(4.1) | 11409 | fork (F-duty-515(4.1), F-unless-515(4.1)) | `s 515(4.1) the justice must add a condition prohibiting the accused from possessing a firearm and the other things` [part16-reverse-onus] |
| 515(4.1)(a) | 11410 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(b) | 11411 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(c) | 11412 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(d) | 11413 | repealed or blank in this text | the text shows: "(d) [Repealed, 2026, c. 19, s. 48]" |
| 515(4.1)(e) | 11414 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(f) | 11415 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(g) | 11416 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(g.1) | 11417 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(h) | 11418 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(i) | 11419 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(j) | 11420 | encoded | within `s 515(4.1) the accused is charged with one of the offences listed in paragraphs (a) to (k)` [part16-reverse-onus] |
| 515(4.1)(k) | 11421-11422 | encoded | within `s 515(4.11) the justice must specify in the order the manner and method of surrender, disposal, detention or storage` [part16-reverse-onus] |
| 515(4.11) | 11423 | fork (F-duty-515(4.11)) | `s 515(4.11) the justice must specify in the order the manner and method of surrender, disposal, detention or storage` [part16-reverse-onus] |
| 515(4.11)(a) | 11424 | encoded | within `s 515(4.11) the justice must specify in the order the manner and method of surrender, disposal, detention or storage` [part16-reverse-onus] |
| 515(4.11)(b) | 11425 | encoded | within `s 515(4.11) the justice must specify in the order the manner and method of surrender, disposal, detention or storage` [part16-reverse-onus] |
| 515(4.12) | 11426-11427 | fork (F-duty-515(4.12)) | `s 515(4.12) the justice must include in the record a statement of the reasons for not adding the condition` [part16-reverse-onus] |
| 515(4.2) | 11428-11429 | fork (F-duty-515(4.2)) | `s 515(4.2) the justice must consider whether it is desirable to include the condition` [part16-reverse-onus] |
| 515(4.2)(a) | 11430 | encoded | within `s 515(4.2) the additional condition` [part16-reverse-onus] |
| 515(4.2)(a.1) | 11431 | encoded | within `s 515(4.2) the additional condition` [part16-reverse-onus] |
| 515(4.2)(a.2) | 11432 | encoded | within `s 515(4.2) the additional condition` [part16-reverse-onus] |
| 515(4.2)(b) | 11433 | encoded | within `s 515(4.2) the additional condition` [part16-reverse-onus] |
| 515(4.3) | 11434-11435 | fork (F-are-the-following) | within `s 515(4.3) the charge` [part16-reverse-onus] |
| 515(4.3)(a) | 11436 | fork (F-are-the-following) | within `s 515(4.3) the offence is one of the offences for the purposes of subsection (4.2)` [part16-reverse-onus] |
| 515(4.3)(a.1) | 11437 | fork (F-are-the-following) | within `s 515(4.3) the offence is one of the offences for the purposes of subsection (4.2)` [part16-reverse-onus] |
| 515(4.3)(b) | 11438 | fork (F-are-the-following) | within `s 515(4.3) the offence is one of the offences for the purposes of subsection (4.2)` [part16-reverse-onus] |
| 515(4.3)(c) | 11439 | fork (F-are-the-following) | within `s 515(4.3) the offence is one of the offences for the purposes of subsection (4.2)` [part16-reverse-onus] |
| 515(4.3)(d) | 11440 | fork (F-are-the-following) | within `s 515(4.3) the offence is one of the offences for the purposes of subsection (4.2)` [part16-reverse-onus] |
| 515(4.4) | 11441-11442 | fork (F-duty-515(4.4)) | `s 515(4.4) the condition` [part16-reverse-onus] |
| 515(4.4)(a) | 11443 | encoded | within `s 515(4.4) the condition` [part16-reverse-onus] |
| 515(4.4)(b) | 11444 | encoded | within `s 515(4.4) the condition` [part16-reverse-onus] |
| 515(4.4)(c) | 11445 | encoded | within `s 515(4.4) the condition` [part16-reverse-onus] |
| 515(5) | 11446-11447 | fork (F-duty-515(5)) | `s 515(5) the justice must order that the accused be detained in custody and state the reasons in the record` [part16-interim-release] |
| 515(6) | 11448-11449 | fork (F-duty-515(6), F-unless-515(6)) | `s 515(6)(a) the charge` [part16-reverse-onus] |
| 515(6)(a) | 11450 | fork (F-other-515(6)(a)) | `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(i) | 11451 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(ii) | 11452 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(iii) | 11453 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(iv) | 11454 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(v) | 11455 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(vi) | 11456 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(vii) | 11457 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(viii) | 11458 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(ix) | 11459 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(x) | 11460 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(xi) | 11461 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(xii) | 11462 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(xii.1) | 11463 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(xiii) | 11464 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(a)(xiv) | 11465 | encoded | within `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` [part16-reverse-onus] |
| 515(6)(b) | 11466 | fork (F-other-515(6)(b)) | `s 515(6)(b) the accused is charged with an indictable offence, other than an offence listed in section 469, and is not ordinarily resident in Canada` [part16-reverse-onus] |
| 515(6)(b.1) | 11467 | encoded | `s 515(6)(b.1) the accused is charged with an offence of violence against their intimate partner and has a prior conviction, discharge or recognizance` [part16-reverse-onus] |
| 515(6)(b.1)(i) | 11468 | encoded | within `s 515(6)(b.1) the accused is charged with an offence of violence against their intimate partner and has a prior conviction, discharge or recognizance` [part16-reverse-onus] |
| 515(6)(b.1)(ii) | 11469 | encoded | within `s 515(6)(b.1) the accused is charged with an offence of violence against their intimate partner and has a prior conviction, discharge or recognizance` [part16-reverse-onus] |
| 515(6)(b.2) | 11470 | fork (F-ten-years) | `s 515(6)(b.2) the accused is charged with an offence of violence with a weapon and was convicted within 10 years of another such offence` [part16-reverse-onus] |
| 515(6)(c) | 11471 | encoded | within `s 515(6)(c) and (d) the accused is charged with an offence at large after release, or a life-imprisonment drug offence` [part16-reverse-onus] |
| 515(6)(d) | 11472 | encoded | within `s 515(6)(c) and (d) the accused is charged with an offence at large after release, or a life-imprisonment drug offence` [part16-reverse-onus] |
| 515(6.1) | 11473-11474 | fork (F-duty-515(6.1)) | `s 515(6.1) the justice must include in the record a statement of the reasons for ordering the release` [part16-reverse-onus] |
| 515(7) | 11475-11476 | fork (F-may-515(7), F-duty-515(7)) | `s 515(7) the justice must make a release order under section 515` [part16-reverse-onus] |
| 515(8) | 11477 | repealed or blank in this text | the text shows: "(8) [Repealed, 2019, c. 25, s. 225]" |
| 515(9) | 11478-11479 | fork (F-515-9-sufficient) | within `s 515(9) it is sufficient for the purposes of subsections (5) and (6) that a record is made in accordance with Part XVIII` [part16-interim-release] |
| 515(9.1) | 11480-11481 | fork (F-duty-515(9.1)) | `s 515(9.1) the justice must state in writing, in the record, that the detention is ordered primarily because of a previous conviction` [part16-interim-release] |
| 515(10) | 11482-11483 | encoded | `s 515(10) the detention of the accused in custody can be justified on one of the three grounds` (+1 more) [part16-reverse-onus] |
| 515(10)(a) | 11484 | encoded | within `s 515(10) the detention of the accused in custody can be justified on one of the three grounds` (+1 more) [part16-reverse-onus] |
| 515(10)(b) | 11485 | encoded | within `s 515(10) the detention of the accused in custody can be justified on one of the three grounds` (+1 more) [part16-reverse-onus] |
| 515(10)(c) | 11486 | encoded | within `s 515(10)(c) the circumstance is one the text names for the third ground` [part16-reverse-onus] |
| 515(10)(c)(i) | 11487 | encoded | within `s 515(10)(c) the circumstance is one the text names for the third ground` [part16-reverse-onus] |
| 515(10)(c)(ii) | 11488 | encoded | within `s 515(10)(c) the circumstance is one the text names for the third ground` [part16-reverse-onus] |
| 515(10)(c)(iii) | 11489 | encoded | within `s 515(10)(c) the circumstance is one the text names for the third ground` [part16-reverse-onus] |
| 515(10)(c)(iv) | 11490 | encoded | within `s 515(10)(c) the circumstance is one the text names for the third ground` [part16-reverse-onus] |
| 515(10)(c)(v) | 11491 | encoded | within `s 515(10)(c) the circumstance is one the text names for the third ground` [part16-reverse-onus] |
| 515(11) | 11492-11493 | fork (F-duty-515(11)) | `s 515(11) the justice must order that the accused be detained in custody and issue a warrant in Form 8 for the committal` [part16-interim-release] |
| 515(12) | 11494-11495 | encoded | `s 515(12) the justice may include in the order a direction that the accused abstain from communicating with any victim, witness or other person` [part16-interim-release] |
| 515(13) | 11496-11497 | fork (F-duty-515(13)) | `s 515(13) the justice must include in the record a statement that the justice considered the safety and security of every victim and of the community` [part16-interim-release] |
| 515(13.1) | 11498-11499 | fork (F-duty-515(13.1), F-duty-515(13.1)-2) | `s 515(13.1) the justice must include in the record a statement of how the justice determined whether the accused is an accused referred to in section 493.2, and the determination` [part16-interim-release] |
| 515(14) | 11500-11501 | fork (F-duty-515(14)) | `s 515(14) the justice must cause a copy of the order to be given to the victim` [part16-interim-release] |
| 515(14.1) | 11502-11503 | fork (F-duty-515(14.1)) | `s 515(14.1) the justice must ask the prosecutor whether victims of the offence have been informed of their right to request a copy` [part16-interim-release] |
| 515.01 | 11504-11505 | fork (F-may-515.01, F-where-515.01) | `s 515.01 the judge or justice may make an order in Form 11.1 requiring the accused to appear for the purposes of the Identification of Criminals Act` [part16-interim-release] |
| 515.1(1) | 11506-11507 | encoded | `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(a) | 11508 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(b) | 11509 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(c) | 11510 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(d) | 11511 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(e) | 11512 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(f) | 11513 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(g) | 11514 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(1)(h) | 11515 | encoded | within `s 515.1(1) the person has provided the declaration the subsection requires before being named as a surety` [part16-interim-release] |
| 515.1(2) | 11516-11517 | fork (F-may-515.1(2)) | `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` [part16-interim-release] |
| 515.1(2)(a) | 11518 | encoded | within `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` [part16-interim-release] |
| 515.1(2)(b) | 11519 | encoded | within `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` [part16-interim-release] |
| 515.1(2)(b)(i) | 11520 | encoded | within `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` [part16-interim-release] |
| 515.1(2)(b)(ii) | 11521 | encoded | within `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` [part16-interim-release] |
| 515.1(2)(b)(iii) | 11522 | encoded | within `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` [part16-interim-release] |
| 515.1(3) | 11523-11524 | encoded | `s 515.1(3) the person may provide the declaration by a means of telecommunication` [part16-interim-release] |
| 516 | 11525-11526 | fork (F-where-516) | `s 516 the justice may adjourn the proceedings and remand the accused to custody in prison by warrant in Form 19` [part16-interim-release] |
| 516.1(1) | 11527-11528 | encoded | within `s 516.1(1) the justice may order that the accused abstain from communicating with any victim, witness or other person identified in the order` [part16-interim-release] |
| 516.1(2) | 11529-11530 | encoded | within `s 516.1(1) the justice may order that the accused abstain from communicating with any victim, witness or other person identified in the order` [part16-interim-release] |
| 516.1(2)(a) | 11531 | encoded | within `s 516.1(2) the order remains in force` [part16-interim-release] |
| 516.1(2)(b) | 11532 | encoded | within `s 516.1(2) the order remains in force` [part16-interim-release] |
| 516.1(2)(c) | 11533 | encoded | within `s 516.1(2) the order remains in force` [part16-interim-release] |
| 516.1(2)(d) | 11534 | encoded | within `s 516.1(2) the order remains in force` [part16-interim-release] |
| 517(1) | 11535-11536 | fork (F-may-517(1), F-duty-517(1)) | `s 517(1) the justice may make an order directing that the evidence, information, representations and reasons shall not be published` [part16-interim-release] |
| 517(1)(a) | 11537 | encoded | within `s 517(1) the order against publication remains in force` [part16-interim-release] |
| 517(1)(b) | 11538 | encoded | within `s 517(1) the order against publication remains in force` [part16-interim-release] |
| 517(2) | 11539-11540 | encoded | `s 517(2) the person is guilty of an offence punishable on summary conviction` [part16-interim-release] |
| 517(3) | 11541 | repealed or blank in this text | the text shows: "(3) [Repealed, 2005, c. 32, s. 17]" |
| 518(1) | 11542-11543 | encoded | `s 518(1)(a) the justice may make inquiries, on oath or otherwise, of and concerning the accused` [part16-interim-release] |
| 518(1)(a) | 11544 | encoded | within `s 518(1)(a) the justice may make inquiries, on oath or otherwise, of and concerning the accused` [part16-interim-release] |
| 518(1)(b) | 11545 | fork (F-unless-518(1)(b), F-unless-518(1)(b)-2) | `s 518(1)(b) the accused is barred from being examined by the justice or any other person except counsel for the accused` [part16-interim-release] |
| 518(1)(c) | 11546 | encoded | `s 518(1)(c) the prosecutor may lead the evidence` [part16-interim-release] |
| 518(1)(c)(i) | 11547 | encoded | within `s 518(1)(c) the prosecutor may lead the evidence` [part16-interim-release] |
| 518(1)(c)(ii) | 11548 | encoded | within `s 518(1)(c) the prosecutor may lead the evidence` [part16-interim-release] |
| 518(1)(c)(iii) | 11549 | encoded | within `s 518(1)(c) the prosecutor may lead the evidence` [part16-interim-release] |
| 518(1)(c)(iv) | 11550 | encoded | within `s 518(1)(c) the prosecutor may lead the evidence` [part16-interim-release] |
| 518(1)(d) | 11551 | encoded | `s 518(1)(d) the justice may take the matters into consideration` [part16-interim-release] |
| 518(1)(d.1) | 11552 | encoded | `s 518(1)(d.1) the justice may receive the evidence in writing, orally or as a recording` [part16-interim-release] |
| 518(1)(d.2) | 11553 | fork (F-duty-518(1)(d.2)) | `s 518(1)(d.2) the justice must take the evidence into consideration` [part16-interim-release] |
| 518(1)(e) | 11554 | encoded | `s 518(1)(e) the justice may receive the evidence and base the decision on it` [part16-interim-release] |
| 518(2) | 11555-11556 | fork (F-where-518(2)) | `s 518(2) the justice may make any order provided for in this Part for the release of the accused until sentence` [part16-interim-release] |
| 519(1) | 11557-11558 | encoded | within `s 519(1)(a) the justice must direct that the accused be released forthwith` [part16-interim-release] |
| 519(1)(a) | 11559 | fork (F-duty-519(1)(a), F-duty-519(1)(a)-2) | within `s 519(1)(a) the justice must direct that the accused be released forthwith` [part16-interim-release] |
| 519(1)(a)(i) | 11560 | encoded | within `s 519(1)(a) the justice must direct that the accused be released forthwith` [part16-interim-release] |
| 519(1)(a)(ii) | 11561 | encoded | `s 519(1)(a) the justice must direct that the accused be released as soon as the accused is no longer required to be detained in respect of another matter` [part16-interim-release] |
| 519(1)(b) | 11562 | fork (F-duty-519(1)(b), F-duty-519(1)(b)-2) | `s 519(1)(b) the justice who made the order or another justice having jurisdiction must issue a warrant for the committal of the accused` [part16-interim-release] |
| 519(1)(b)(i) | 11563 | encoded | within `s 519(1)(b) the justice who made the order or another justice having jurisdiction must issue a warrant for the committal of the accused` [part16-interim-release] |
| 519(1)(b)(ii) | 11564-11565 | encoded | within `s 519(1)(b) the justice who made the order or another justice having jurisdiction must issue a warrant for the committal of the accused` [part16-interim-release] |
| 519(1)(c) | 11566 | encoded | `s 519(1)(c) the no-communication condition is effective from the moment it is made, whether or not the accused has been released from custody` [part16-interim-release] |
| 519(2) | 11567-11568 | fork (F-unless-519(2)) | `s 519(2) the justice must issue an order for discharge in Form 39` [part16-interim-release] |
| 519(3) | 11569-11570 | fork (F-duty-519(3)) | `s 519(3) the justice must issue a warrant for the committal of the accused` [part16-interim-release] |
| 519.1 | 11571-11572 | encoded | `s 519.1 the release order may be varied` [part16-interim-release] |
| 520(1) | 11573-11574 | fork (F-may-520(1), F-where-520(1)) | `s 520(1) the accused may apply to a judge for a review of the order` [part16-review] |
| 520(2) | 11575-11576 | encoded | `s 520(2) the application may be heard by a judge` [part16-review] |
| 520(3) | 11577-11578 | fork (F-where-520(3), F-duty-520(3)) | `s 520(3) the accused must be present at the hearing` [part16-review] |
| 520(4) | 11579-11580 | fork (F-where-520(4)) | `s 520(4) the judge may adjourn the proceedings` [part16-review] |
| 520(5) | 11581-11582 | fork (F-where-520(5)) | within `s 520(5) the judge may issue a warrant for the arrest of the accused` [part16-review] |
| 520(6) | 11583-11584 | encoded | `s 520(6) the warrant may be executed anywhere in Canada` [part16-review] |
| 520(7) | 11585-11586 | fork (F-duty-520(7), F-dutyN-520(7)) | `s 520(7) the judge may consider the material` [part16-review] |
| 520(7)(a) | 11587 | encoded | within `s 520(7) the judge may consider the material` [part16-review] |
| 520(7)(b) | 11588 | encoded | within `s 520(7) the judge may consider the material` [part16-review] |
| 520(7)(c) | 11589-11590 | encoded | within `s 520(7) what the judge may consider` [part16-review] |
| 520(7)(d) | 11591 | fork (F-cause-shown-choice) | within `s 520(7) the judge must dismiss the application` [part16-review] |
| 520(7)(e) | 11592 | fork (F-cause-shown-choice, F-may-520(7)(e)) | `s 520(7)(e) the judge may allow the application, vacate or vary the order and make any other order provided for in section 515` [part16-review] |
| 520(8) | 11593-11594 | fork (F-30-days, F-duty-520(8), F-unless-520(8)) | `s 520(8) the further application is barred` [part16-review] |
| 520(9) | 11595-11596 | encoded | `s 520(9) sections 517, 518 and 519 apply with such modifications as the circumstances require` [part16-review] |
| 521(1) | 11597-11598 | fork (F-may-521(1), F-where-521(1)) | `s 521(1) the prosecutor may apply to a judge for a review of the order` [part16-review] |
| 521(2) | 11599-11600 | encoded | `s 521(2) the application may be heard by a judge` [part16-review] |
| 521(3) | 11601-11602 | fork (F-where-521(3), F-duty-521(3)) | `s 521(3) the accused must be present at the hearing` [part16-review] |
| 521(4) | 11603-11604 | encoded | `s 521(4) the adjournment of an accused in custody is within the limit of three clear days, or the accused consents` [part16-review] |
| 521(5) | 11605-11606 | fork (F-where-521(5)) | within `s 521(5) the judge may issue a warrant for the arrest of the accused` [part16-review] |
| 521(6) | 11607-11608 | fork (F-duty-521(6)) | `s 521(6) the judge must issue a warrant for the committal of the accused` [part16-review] |
| 521(7) | 11609-11610 | encoded | `s 521(7) the warrant may be executed anywhere in Canada` [part16-review] |
| 521(8) | 11611-11612 | fork (F-duty-521(8), F-dutyN-521(8)) | `s 521(8) the judge may consider the material` [part16-review] |
| 521(8)(a) | 11613 | encoded | within `s 521(8) the judge may consider the material` [part16-review] |
| 521(8)(b) | 11614 | encoded | within `s 521(8) the judge may consider the material` [part16-review] |
| 521(8)(c) | 11615-11616 | encoded | within `s 521(8) the judge may consider the material` [part16-review] |
| 521(8)(d) | 11617 | fork (F-cause-shown-choice) | within `s 521(8) the judge must dismiss the application` [part16-review] |
| 521(8)(e) | 11618 | fork (F-cause-shown-choice, F-may-521(8)(e)) | `s 521(8)(e) the judge may allow the application, vacate or vary the order and make any other order provided for in section 515` [part16-review] |
| 521(9) | 11619-11620 | fork (F-30-days, F-duty-521(9), F-unless-521(9)) | `s 521(9) the further application is barred` [part16-review] |
| 521(10) | 11621-11622 | encoded | `s 521(10) sections 517, 518 and 519 apply with such modifications as the circumstances require` [part16-review] |
| 522(1) | 11623-11624 | fork (F-duty-522(1), F-other-522(1)) | `s 522(1) the court, judge or justice is barred from releasing the accused` [part16-review] |
| 522(2) | 11625-11626 | fork (F-duty-522(2), F-unless-522(2)) | `s 522(2) the judge must order that the accused be detained in custody` [part16-review] |
| 522(2.1) | 11627-11628 | encoded | `s 522(2.1) the judge may include in the order a direction that the accused abstain from communicating with any victim, witness or other person` [part16-review] |
| 522(3) | 11629-11630 | fork (F-may-522(3)) | `s 522(3) the judge may make a release order referred to in section 515` [part16-review] |
| 522(3.1) | 11631-11632 | encoded | `s 522(3.1) subsection 515(2.01) applies to the accused` [part16-review] |
| 522(4) | 11633-11634 | encoded | `s 522(4) the order is subject to review other than under section 680` [part16-review] |
| 522(5) | 11635-11636 | fork (F-unless-522(5)) | `s 522(5) subsection 518(2) applies to the application` [part16-review] |
| 522(6) | 11637-11638 | fork (F-where-522(6)) | `s 522(6) the judge may apply the provisions of this Part respecting judicial interim release to the other offence` [part16-review] |
| 523(1) | 11639-11640 | encoded | `s 523(1) how the accused is determined at trial` [part16-review] |
| 523(1)(a) | 11641 | encoded | within `s 523(1) how the accused is determined at trial` [part16-review] |
| 523(1)(b) | 11642 | encoded | within `s 523(1) how the accused is determined at trial` [part16-review] |
| 523(1)(c) | 11643 | encoded | within `s 523(1) how the accused is determined at trial` [part16-review] |
| 523(1.1) | 11644-11645 | encoded | within `s 523(1.1) section 507 or 508 applies to the new information` [part16-review] |
| 523(1.2) | 11646-11647 | encoded | `s 523(1.2) the order for detention, release order, appearance notice, summons or undertaking applies in respect of the indictment` [part16-review] |
| 523(2) | 11648-11649 | fork (F-where-523(2)) | `s 523(2) who may act and when` [part16-review] |
| 523(2)(a) | 11650 | encoded | within `s 523(2) who may act and when` [part16-review] |
| 523(2)(a.1) | 11651 | encoded | within `s 523(2) who may act and when` [part16-review] |
| 523(2)(b) | 11652 | encoded | within `s 523(2) who may act and when` [part16-review] |
| 523(2)(c) | 11653 | encoded | within `s 523(2) who may act and when` [part16-review] |
| 523(2)(c)(i) | 11654 | encoded | within `s 523(2) who may act and when` [part16-review] |
| 523(2)(c)(ii) | 11655 | encoded | within `s 523(2) who may act and when` [part16-review] |
| 523(2)(c)(iii) | 11656-11658 | encoded | within `s 523(2.1) the court, judge or justice must order that the accused be detained in custody` [part16-review] |
| 523(2.1) | 11659 | fork (F-duty-523(2.1), F-other-523(2.1), F-unless-523(2.1)) | `s 523(2.1) the court, judge or justice must order that the accused be detained in custody` [part16-review] |
| 523(2.2) | 11660-11661 | encoded | `s 523(2.2) the accused is deemed to have been charged with an offence other than an offence listed in section 469` [part16-review] |
| 523(2.3) | 11662-11663 | encoded | `s 523(2.3) subsection 515(2.01) applies to the accused` [part16-review] |
| 523(3) | 11664-11665 | fork (F-unless-523(3)) | `s 523(3) subsection 518(2) applies to the proceedings under subsection (2)` [part16-review] |
| 523.1(1) | 11667-11669 | encoded | `s 523.1(1)(a) the justice must order that the accused appear before a judge of the superior court of criminal jurisdiction so that the judge may hear the matter` [part16-failure-and-delay] |
| 523.1(1)(a) | 11670 | encoded | within `s 523.1(1)(a) the justice must order that the accused appear before a judge of the superior court of criminal jurisdiction so that the judge may hear the matter` [part16-failure-and-delay] |
| 523.1(1)(b) | 11671 | fork (F-duty-523.1(1)(b)) | `s 523.1(1)(b) the justice must hear the matter` [part16-failure-and-delay] |
| 523.1(2) | 11672-11673 | fork (F-are-the-following) | `s 523.1(2)(a) an appearance notice has been issued for the failure and the prosecutor seeks a decision under this section` [part16-failure-and-delay] |
| 523.1(2)(a) | 11674 | fork (F-are-the-following) | within `s 523.1(2)(a) an appearance notice has been issued for the failure and the prosecutor seeks a decision under this section` [part16-failure-and-delay] |
| 523.1(2)(b) | 11675 | fork (F-are-the-following) | `s 523.1(2)(b) a charge has been laid for the contravention and the prosecutor seeks a decision under this section` [part16-failure-and-delay] |
| 523.1(3) | 11676-11677 | fork (F-duty-523.1(3)) | `s 523.1(3) the judge or justice must review any conditions of release that have been imposed on the accused` [part16-failure-and-delay] |
| 523.1(3)(a) | 11678 | fork (F-may-523.1(3)(a)) | `s 523.1(3)(a) the judge or justice may take no action` [part16-failure-and-delay] |
| 523.1(3)(b) | 11679 | fork (F-may-523.1(3)(b)) | `s 523.1(3)(b) the judge or justice may cancel any other summons, appearance notice, undertaking or release order in respect of the accused` [part16-failure-and-delay] |
| 523.1(3)(b)(i) | 11680 | fork (F-may-523.1(3)(b)(i)) | `s 523.1(3)(b)(i) the judge or justice may make a release order under section 515` [part16-failure-and-delay] |
| 523.1(3)(b)(ii) | 11681 | fork (F-may-523.1(3)(b)(ii), F-duty-523.1(3)(b)(ii)) | `s 523.1(3)(b)(ii) the judge or justice may make an order that the accused be detained in custody until the accused is dealt with according to law` [part16-failure-and-delay] |
| 523.1(3)(c) | 11682 | fork (F-may-523.1(3)(c)) | `s 523.1(3)(c) the judge or justice may remand the accused to custody for the purposes of the Identification of Criminals Act` [part16-failure-and-delay] |
| 523.1(4) | 11683-11684 | fork (F-duty-523.1(4)) | `s 523.1(4) the judge or justice must dismiss the charge` [part16-failure-and-delay] |
| 523.1(5) | 11685-11686 | fork (F-duty-523.1(5)) | `s 523.1(5) the laying of an information or the preferring of an indictment against the accused for the failure referred to in paragraph (2)(a) is barred` [part16-failure-and-delay] |
| 524(1) | 11687-11688 | encoded | `s 524(1)(a) the justice must order that the accused be taken before a judge of the superior court of criminal jurisdiction so that the judge may hear the matter` [part16-failure-and-delay] |
| 524(1)(a) | 11689 | encoded | within `s 524(1)(a) the justice must order that the accused be taken before a judge of the superior court of criminal jurisdiction so that the judge may hear the matter` [part16-failure-and-delay] |
| 524(1)(b) | 11690 | fork (F-duty-524(1)(b)) | `s 524(1)(b) the justice must hear the matter` [part16-failure-and-delay] |
| 524(2) | 11691-11692 | fork (F-are-the-following) | `s 524(2)(a) the accused has been arrested for a contravention and the prosecutor seeks to have the document cancelled under this section` [part16-failure-and-delay] |
| 524(2)(a) | 11693 | fork (F-are-the-following) | within `s 524(2)(a) the accused has been arrested for a contravention and the prosecutor seeks to have the document cancelled under this section` [part16-failure-and-delay] |
| 524(2)(b) | 11694 | fork (F-are-the-following) | `s 524(2)(b) the accused has been arrested for an offence committed while subject to the document and the prosecutor seeks to have it cancelled under this section` [part16-failure-and-delay] |
| 524(3) | 11695-11696 | fork (F-duty-524(3)) | `s 524(3) the judge or justice must cancel the summons, appearance notice, undertaking or release order` [part16-failure-and-delay] |
| 524(3)(a) | 11697 | encoded | within `s 524(3) the judge or justice must cancel the summons, appearance notice, undertaking or release order` [part16-failure-and-delay] |
| 524(3)(b) | 11698 | encoded | within `s 524(3) the judge or justice must cancel the summons, appearance notice, undertaking or release order` [part16-failure-and-delay] |
| 524(4) | 11699-11700 | fork (F-duty-524(4), F-unless-524(4)) | within `s 524(4) the judge or justice must order that the accused be detained in custody` [part16-failure-and-delay] |
| 524(4)(a) | 11701 | encoded | `s 524(4)(a) the judge or justice found under paragraph (3)(a) that the accused has contravened or had been about to contravene the summons, appearance notice, undertaking or release order` [part16-failure-and-delay] |
| 524(4)(b) | 11702 | encoded | `s 524(4)(b) the judge or justice found under paragraph (3)(b) that there are reasonable grounds to believe that the accused has committed an indictable offence while being subject to the summons, appearance notice, undertaking or release order` [part16-failure-and-delay] |
| 524(4)(c) | 11703 | encoded | `s 524(4)(c) any of the outstanding charges against the accused include charges for an offence referred to in subsection 515(6) or 522(2)` [part16-failure-and-delay] |
| 524(5) | 11704-11705 | fork (F-524-5-6.2, F-duty-524(5), F-dutyN-524(5)) | `s 524(5) the judge or justice must make a release order referred to in section 515` [part16-failure-and-delay] |
| 524(5.1) | 11706-11707 | encoded | `s 524(5.1) subsection 515(2.01) applies to the accused for the purposes of subsection (5)` [part16-failure-and-delay] |
| 524(6) | 11708-11709 | fork (F-duty-524(6)) | `s 524(6) the judge or justice must include in the record a statement of the reasons for making the release order` [part16-failure-and-delay] |
| 524(6.1) | 11710-11711 | fork (F-duty-524(6.1), F-unless-524(6.1)) | `s 524(6.1) the judge or justice must make a release order referred to in section 515` [part16-failure-and-delay] |
| 524(6.2) | 11712-11713 | fork (F-524-5-6.2, F-duty-524(6.2), F-dutyN-524(6.2)) | `s 524(6.2) the judge or justice must make a detention order referred to in section 515` [part16-failure-and-delay] |
| 524(7) | 11714-11715 | fork (F-duty-524(7)) | `s 524(7) the judge or justice must order that the accused be released from custody` [part16-failure-and-delay] |
| 524(8) | 11716-11717 | fork (F-unless-524(8)) | `s 524(8) subsection 518(2) applies to the proceedings under this section` [part16-failure-and-delay] |
| 524(9) | 11718-11719 | encoded | `s 524(9) the order is subject to review other than under section 680` [part16-failure-and-delay] |
| 524(10) | 11720-11721 | encoded | `s 524(10) the order is subject to review under sections 520 and 521 as if the order were made under section 515` [part16-failure-and-delay] |
| 525(1) | 11723-11725 | fork (F-90-days, F-525-1-ab, F-duty-525(1), F-other-525(1)) | within `s 525(1) the trial has not commenced within 90 days from the day` [part16-failure-and-delay] |
| 525(1)(a) | 11726 | fork (F-90-days, F-525-1-ab) | within `s 525(1) the day from which the 90 days are counted` [part16-failure-and-delay] |
| 525(1)(b) | 11727-11729 | fork (F-90-days, F-525-1-ab) | within `s 525(1) the application is made immediately after the expiry of those 90 days` [part16-failure-and-delay] |
| 525(1.1) | 11730 | fork (F-90-days, F-duty-525(1.1)) | `s 525(1.1) the person having the custody of the accused is not required to make the application` [part16-failure-and-delay] |
| 525(2) | 11731-11732 | encoded | `s 525(2)(a) the judge must fix a date for the hearing described in subsection (1)` [part16-failure-and-delay] |
| 525(2)(a) | 11733 | fork (F-duty-525(2)(a)) | within `s 525(2)(a) the place of the hearing is one the paragraph names` [part16-failure-and-delay] |
| 525(2)(a)(i) | 11734 | encoded | within `s 525(2)(a) the place of the hearing is one the paragraph names` [part16-failure-and-delay] |
| 525(2)(a)(ii) | 11735 | encoded | within `s 525(2)(a) the place of the hearing is one the paragraph names` [part16-failure-and-delay] |
| 525(2)(b) | 11736 | fork (F-duty-525(2)(b), F-dutyN-525(2)(b)) | `s 525(2)(b) the judge must direct that notice of the hearing be given` [part16-failure-and-delay] |
| 525(3) | 11737-11738 | fork (F-may-525(3)) | `s 525(3) the judge may cancel the hearing` [part16-failure-and-delay] |
| 525(4) | 11739-11740 | fork (F-duty-525(4)) | `s 525(4) the judge must consider whether the prosecutor or the accused has been responsible for any delay` [part16-failure-and-delay] |
| 525(4)(a) | 11741 | fork (F-may-525(4)(a), F-where-525(4)(a)) | `s 525(4)(a) the judge may give directions for expediting the proceedings` [part16-failure-and-delay] |
| 525(4)(b) | 11742 | fork (F-90-days, F-may-525(4)(b), F-where-525(4)(b)) | `s 525(4)(b) the judge may require a further hearing under this section` [part16-failure-and-delay] |
| 525(4.1) | 11743-11744 | fork (F-duty-525(4.1)) | `s 525(4.1) the judge must order the release or detention of the accused on cause being shown in accordance with section 515` [part16-failure-and-delay] |
| 525(5) | 11745-11746 | fork (F-duty-525(5)) | `s 525(5) the judge must make a release order referred to in section 515` [part16-failure-and-delay] |
| 525(5.1) | 11747-11748 | fork (F-duty-525(5.1)) | `s 525(5.1) the judge must make an order that the accused continue to be detained` [part16-failure-and-delay] |
| 525(5.2) | 11749-11750 | fork (F-duty-525(5.2), F-unless-525(5.2)) | `s 525(5.2) a further hearing under this section is barred` [part16-failure-and-delay] |
| 525(6) | 11751-11752 | encoded | `s 525(6) the section applies, with any modifications that the circumstances require, in respect of proceedings under this section` [part16-failure-and-delay] |
| 525(7) | 11753-11754 | encoded | `s 525(7) the office the person holds` [part16-failure-and-delay] |
| 525(7)(a) | 11755 | encoded | within `s 525(7)(a) the office as section 493 knows it` [part16-failure-and-delay] |
| 525(7)(b) | 11756 | encoded | within `s 525(7) the office the person holds` [part16-failure-and-delay] |
| 525(8) | 11757 | repealed or blank in this text | the text shows: "(8) [Repealed, 2019, c. 25, s. 235]" |
| 525(9) | 11758 | repealed or blank in this text | the text shows: "(9) [Repealed, 2019, c. 25, s. 235]" |
| 526 | 11759-11760 | encoded | `s 526 the court, judge or justice may give directions for expediting any proceedings in respect of the accused` [part16-failure-and-delay] |
| 527(1) | 11762-11764 | fork (F-may-527(1)) | `s 527(1) the judge may order in writing that a person who is confined in a prison be brought before the court, judge, justice or provincial court judge` [part16-prisoners-and-entry] |
| 527(1)(a) | 11765 | encoded | within `s 527(1) the judge may order in writing that a person who is confined in a prison be brought before the court, judge, justice or provincial court judge` [part16-prisoners-and-entry] |
| 527(1)(b) | 11766 | encoded | within `s 527(1) the judge may order in writing that a person who is confined in a prison be brought before the court, judge, justice or provincial court judge` [part16-prisoners-and-entry] |
| 527(2) | 11767-11768 | fork (F-where-527(2)) | `s 527(2) a provincial court judge has the same powers for the purposes of subsection (1) or (7) as a judge has under that subsection` [part16-prisoners-and-entry] |
| 527(3) | 11769-11770 | fork (F-duty-527(3)) | `s 527(3) the order must be addressed to the person who has custody of the prisoner` [part16-prisoners-and-entry] |
| 527(3)(a) | 11771 | fork (F-duty-527(3)(a)) | `s 527(3)(a) the person who has custody of the prisoner must deliver the prisoner to the person named in the order to receive the prisoner, or do what paragraph (b) requires` [part16-prisoners-and-entry] |
| 527(3)(b) | 11772 | fork (F-duty-527(3)(b)) | `s 527(3)(b) the person who has custody of the prisoner must bring the prisoner before the court, judge, justice or provincial court judge, or do what paragraph (a) requires` [part16-prisoners-and-entry] |
| 527(4) | 11773-11774 | fork (F-duty-527(4)) | `s 527(4) the judge or provincial court judge must direct in the order the manner in which the prisoner is to be kept in custody and returned to the prison` [part16-prisoners-and-entry] |
| 527(5) | 11775-11776 | fork (F-duty-527(5)) | `s 527(5) the judge or provincial court judge must give appropriate directions in the order with respect to the manner in which the prisoner is to be kept in custody or returned` [part16-prisoners-and-entry] |
| 527(5)(a) | 11777 | encoded | within `s 527(5) the direction the order must give` [part16-prisoners-and-entry] |
| 527(5)(b) | 11778 | encoded | within `s 527(5) the direction the order must give` [part16-prisoners-and-entry] |
| 527(6) | 11779-11780 | encoded | `s 527(6) the section applies where the prisoner is convicted and sentenced to imprisonment` [part16-prisoners-and-entry] |
| 527(7) | 11781-11782 | fork (F-527-7-three-gates, F-may-527(7), F-where-527(7)) | `s 527(7) the judge may order the transfer of the prisoner or other person to the custody of a peace officer named in the order for a period specified in the order` [part16-prisoners-and-entry] |
| 527(8) | 11783-11784 | fork (F-duty-527(8), F-duty-527(8)-2) | `s 527(8) the order must be addressed to the person who has custody of the prisoner` [part16-prisoners-and-entry] |
| 527(9) | 11785-11786 | fork (F-duty-527(9)) | `s 527(9) the prisoner must be returned to the place where the prisoner was confined at the time the order was made` [part16-prisoners-and-entry] |
| 528(1) | 11788-11790 | fork (F-duty-528(1)) | `s 528(1) the justice must authorize the arrest of the accused within the justice's jurisdiction by making an endorsement on the warrant` [part16-prisoners-and-entry] |
| 528(1.1) | 11791-11792 | encoded | `s 528(1.1) the copy has the same probative force as the original for the purposes of subsection (1)` [part16-prisoners-and-entry] |
| 528(2) | 11793-11794 | encoded | `s 528(2) the endorsement is sufficient authority to the peace officer to execute the warrant and to take the accused before a justice` [part16-prisoners-and-entry] |
| 529(1) | 11796-11798 | fork (F-may-529(1)) | `s 529(1) the warrant may authorize a peace officer to enter a dwelling-house described in the warrant for the purpose of arresting or apprehending the person` [part16-prisoners-and-entry] |
| 529(2) | 11799-11800 | fork (F-dutyN-529(2), F-unless-529(2)) | `s 529(2) the peace officer is barred from entering the dwelling-house` [part16-prisoners-and-entry] |
| 529.1 | 11801-11802 | fork (F-may-529.1) | `s 529.1 the judge or justice may issue a warrant in Form 7.1 authorizing a peace officer to enter a dwelling-house described in the warrant` [part16-prisoners-and-entry] |
| 529.1(a) | 11803 | encoded | within `s 529.1 the judge or justice may issue a warrant in Form 7.1 authorizing a peace officer to enter a dwelling-house described in the warrant` [part16-prisoners-and-entry] |
| 529.1(b) | 11804 | encoded | within `s 529.1 the judge or justice may issue a warrant in Form 7.1 authorizing a peace officer to enter a dwelling-house described in the warrant` [part16-prisoners-and-entry] |
| 529.1(c) | 11805 | encoded | within `s 529.1 the judge or justice may issue a warrant in Form 7.1 authorizing a peace officer to enter a dwelling-house described in the warrant` [part16-prisoners-and-entry] |
| 529.2 | 11806-11807 | fork (F-duty-529.2) | `s 529.2 the judge or justice must include the term or condition in the warrant` [part16-prisoners-and-entry] |
| 529.3(1) | 11808-11809 | fork (F-may-529.3(1)) | `s 529.3(1) the peace officer may enter the dwelling-house for the purpose of arresting or apprehending a person without a warrant` [part16-prisoners-and-entry] |
| 529.3(2) | 11810-11811 | encoded | `s 529.3(2) the circumstances are exigent circumstances` [part16-prisoners-and-entry] |
| 529.3(2)(a) | 11812 | encoded | within `s 529.3(2) the circumstances are exigent circumstances` [part16-prisoners-and-entry] |
| 529.3(2)(b) | 11813 | encoded | within `s 529.3(2) the circumstances are exigent circumstances` [part16-prisoners-and-entry] |
| 529.4(1) | 11814-11815 | fork (F-may-529.4(1)) | `s 529.4(1) the judge or justice may authorize the peace officer to enter the dwelling-house without prior announcement` [part16-prisoners-and-entry] |
| 529.4(1)(a) | 11816 | encoded | within `s 529.4(1) the judge or justice may authorize the peace officer to enter the dwelling-house without prior announcement` [part16-prisoners-and-entry] |
| 529.4(1)(b) | 11817 | encoded | within `s 529.4(1) the judge or justice may authorize the peace officer to enter the dwelling-house without prior announcement` [part16-prisoners-and-entry] |
| 529.4(2) | 11818-11819 | encoded | `s 529.4(2) the peace officer is barred from entering the dwelling-house without prior announcement despite being authorized to do so` [part16-prisoners-and-entry] |
| 529.4(2)(a) | 11820 | encoded | within `s 529.4(2) the peace officer is barred from entering the dwelling-house without prior announcement despite being authorized to do so` [part16-prisoners-and-entry] |
| 529.4(2)(b) | 11821 | encoded | within `s 529.4(2) the peace officer is barred from entering the dwelling-house without prior announcement despite being authorized to do so` [part16-prisoners-and-entry] |
| 529.4(3) | 11822-11823 | fork (F-dutyN-529.4(3), F-unless-529.4(3)) | `s 529.4(3) the peace officer is barred from entering the dwelling-house without prior announcement` [part16-prisoners-and-entry] |
| 529.4(3)(a) | 11824 | encoded | within `s 529.4(3) the peace officer is barred from entering the dwelling-house without prior announcement` [part16-prisoners-and-entry] |
| 529.4(3)(b) | 11825 | encoded | within `s 529.4(3) the peace officer is barred from entering the dwelling-house without prior announcement` [part16-prisoners-and-entry] |
| 529.5 | 11826-11827 | encoded | `s 529.5 the application may be submitted, and the warrant or authorization may be issued, by a means of telecommunication` [part16-prisoners-and-entry] |

## Fork register (ccc20)

Each entry: the provision, the readings seen, the one taken, the text that licenses each, the module.
The first block holds the readings of the text; the second holds the grant-named ("may") functions whose failed "if" gate answers NOTHING (rule of 2026-11-12, point 1), one row per function, each naming the other reading; the third LISTS, one row per function, the "may" functions whose gate is "where", "when", "upon" or an equivalent of that kind, which answer the guide's own JUST FALSE (ruling (b)) and are left for a lawyer (rule of 2026-11-12, point 3); the fourth holds the case-by-case sites of the brief (2026-11-05), one row per function and kind, each with the answer taken and the other reading.

### Readings of the text

| id | provision | readings seen | taken | text | module |
| --- | --- | --- | --- | --- | --- |
| F-90-days | s 525(1), (1.1), (4)(b) | (1) The day of the event is day 0, so the 90 days are days 1 to 90 and expire at the end of day 90; a trial that commences on day 90 has commenced "within 90 days". (2) The day of the event is day 1, so the period expires at the end of day 89. | (1), by `Date to days` difference: at most 90 is within, more than 90 is not. | "if the trial has not commenced within 90 days from (a) the day on which the accused was taken before a justice": "from" a day does not say whether that day is counted. The same convention is used for the 30 days of ss 520(8) and 521(9). | ccc20-part16-failure-and-delay.l4 |
| F-30-days | s 520(8), s 521(9) | (1) The day of the decision is day 0: an application on the 30th day after it is before the expiry and one on the 31st is not. (2) The day of the decision is day 1. | (1), as for F-90-days. | "before the expiry of 30 days from the date of the decision of the judge who heard the previous application". | ccc20-part16-review.l4 |
| F-are-the-following | s 523.1(2), s 524(2), s 515(4.3) | (1) "are the following" and "are" close the list: a case in none of the paragraphs is the text's own no (JUST FALSE). (2) The list is not closed because the text does not say "only": such a case is NOTHING. | (1) for ss 523.1(2) and 524(2); for s 515(4.3), (1) as the keel read "are" in s 2.3(1). | s 523.1(2) and s 524(2) "The circumstances referred to in subsection (1) are the following"; s 515(4.3) "The offences for the purposes of subsection (4.2) are" followed by its paragraphs. | ccc20-part16-failure-and-delay.l4; ccc20-part16-reverse-onus.l4 |
| F-524-5-6.2 | s 524(5), s 524(6.2) | (1) Subsection (5) is the consequence of subsection (4) and subsection (6.2) the consequence of (6.1): each applies only where the document was cancelled and its predecessor was engaged. (2) Read literally, (5) applies whenever the judge or justice "does not order that the accused be detained in custody under subsection (4)" and (6.2) whenever the judge or justice "does not make a release order under subsection (6.1)", even where (4) or (6.1) was never engaged. | (1). | s 524(5) "If the judge or justice does not order that the accused be detained in custody under subsection (4), the judge or justice shall make a release order referred to in section 515"; s 524(6.2) "If the judge or justice does not make a release order under subsection (6.1), they shall make a detention order referred to in section 515"; s 524(5.1) speaks of "an accused referred to in subsection (4)" and s 524(6.1) of "an accused to whom subsection (4) does not apply", which tie the pairs to the cancellation of s 524(4). | ccc20-part16-failure-and-delay.l4 |
| F-525-1-ab | s 525(1)(a), (b) | (1) Where an order or review decision of paragraph (b) exists, the 90 days run from the later of the two days it names; otherwise from the day the accused was taken before a justice (paragraph (a)). (2) The 90 days also run from paragraph (a), so that the period expires at the first of the two. | (1). | "(a) the day on which the accused was taken before a justice under section 503; or (b) in the case where an order ... has been made ... the later of the day on which the accused was taken into custody under that order and the day of the decision": (b) is introduced by "in the case where" and names its own day. | ccc20-part16-failure-and-delay.l4 |
| F-527-7-three-gates | s 527(7) | (1) The consent gate ("if a prisoner ... consents in writing") fails: NOTHING, whatever the other two gates say; the "on application by the prosecutor" and "where the judge is satisfied" gates fail: JUST FALSE (guide rulings (c) and (b)). (2) Every gate that fails gives NOTHING. (3) Every gate that fails gives JUST FALSE. | (1). | "On application by the prosecutor, a judge of a superior court of criminal jurisdiction may, if a prisoner or a person in the custody of a peace officer consents in writing, order the transfer ..., where the judge is satisfied that". | ccc20-part16-prisoners-and-entry.l4 |
| F-493.1-with-493.11-2-c | s 493.1, s 493.11(2)(c) | (1) The duty of s 493.1 takes the answer of s 493.11(2)(c) as its input, because s 493.11(2) says it applies "for the purposes of section 493.1": a justice or judge faced with a reverse-onus case is not to give primary consideration to release. (2) The two sections answer separately and the caller combines them. | (1). | s 493.11(2) "For the purposes of section 493.1, ... (c) a justice or judge, as the case may be, shall not give primary consideration to the release of the accused at the earliest reasonable opportunity if the accused is one to whom subsection 515(6), 522(2), 523(2.1) or 524(4) applies". | ccc20-part16-principles.l4 |
| F-ten-years | s 515(2.11), s 515(6)(b.2) | (1) "within ten years" is a closed period whose first day is the day ten years before (that day is within). (2) The period is ten years less a day. | (1). | s 515(2.11) "within ten years before the day on which the release order is made"; s 515(6)(b.2) "within 10 years of the day on which they were charged for that offence". | ccc20-part16-interim-release.l4; ccc20-part16-reverse-onus.l4 |
| F-month-end | s 507.1(5) | (1) Six months after the endorsement are counted by calendar month with `Date`, which rolls an impossible day forward (31 August 2026 gives 3 March 2027). (2) The last day is the last day of the sixth month (28 February 2027). | (1). | "not later than six months after the endorsement" names no rule for a month that is shorter. | ccc20-part16-process.l4 |
| F-493.01-scope | s 493.01 | (1) "a reference to an indictable offence includes an offence that may be punishable on summary conviction if it is also an offence that may be prosecuted by indictment, unless the prosecutor has elected" applies to every reference to an indictable offence in Part XVI. (2) It applies to the whole Code, because it sits in Part XVI only for the Part's own references. | (1), through one function `s 493.01 the reference to an indictable offence includes the offence` that every "indictable offence" test in the range calls. | The section stands at the head of Part XVI and the text does not say whether it reaches outside the Part. | ccc20-part16-interpretation.l4 |
| F-cause-shown-choice | s 520(7)(d), (e); s 521(8)(d), (e) | (1) Where the accused (or the prosecutor, in s 521) shows cause, the text leaves the judge a choice between (d) dismiss and (e) allow: the function `must dismiss` answers NOTHING there. (2) Showing cause obliges the judge to allow the application. | (1). | "shall either (d) dismiss the application, or (e) if the accused shows cause, allow the application". | ccc20-part16-review.l4 |
| F-515-9-sufficient | s 515(9) | (1) A record made of the reasons in accordance with Part XVIII is sufficient; a record made another way is NOT COVERED (NOTHING). (2) A record made another way is not sufficient (JUST FALSE). | (1). | "it is sufficient if a record is made of the reasons in accordance with the provisions of Part XVIII": the text says what suffices and does not say that nothing else does. | ccc20-part16-interim-release.l4 |

### Grant-named functions whose failed "if" gate answers NOTHING (45)

The other reading for every row is JUST FALSE: a failed "if" read as the text's own "no", so that a grant turned into "may not".

| id | function | the gate in the text | module |
| --- | --- | --- | --- |
| F-may-494(2) | `s 494(2) the owner of property, or a person acting for the owner, may arrest the person without a warrant` | "may arrest a person without a warrant if they find them committing a criminal offence on or in relation to that property" | part16-arrest |
| F-may-495.1 | `s 495.1 the peace officer may arrest the accused without a warrant to take them before a judge or justice under section 524` | "if a peace officer has reasonable grounds to believe" | part16-arrest |
| F-may-496 | `s 496 the peace officer may, without laying a charge, issue an appearance notice to attend a judicial referral hearing` | "If a peace officer has reasonable grounds to believe" | part16-arrest |
| F-may-497 | `s 497 the peace officer may issue an appearance notice to the person` | "If, by virtue of subsection 495(2), a peace officer does not arrest a person, they may issue" | part16-arrest |
| F-may-499 | `s 499 a peace officer may release the person arrested with a warrant` | "If a person who has been arrested with a warrant by a peace officer is taken into custody" | part16-arrest |
| F-may-500(3) | `s 500(3) the appearance notice may require the accused to appear for the purposes of the Identification of Criminals Act` | "if the accused is alleged to have committed an offence referred to in paragraph 2(1)(c) of that Act" | part16-notices |
| F-may-501(3) | `s 501(3) the undertaking may contain the condition` | "if the condition is reasonable in the circumstances of the offence and necessary, to ensure the accused’s attendance in court or the safety and security of any victim of or witness to the offence, or to prevent the continuation or" | part16-notices |
| F-may-501(4) | `s 501(4) the undertaking may require the accused to appear for the purposes of the Identification of Criminals Act` | "if the accused is alleged to have committed an offence referred to in paragraph 2(1)(c) of that Act" | part16-notices |
| F-may-502(2) | `s 502(2) the accused or the prosecutor may apply to a justice` | "may, in the absence of consent between them, (a) apply to a justice ...; or (b) apply to a justice to vary the undertaking" | part16-notices |
| F-may-502.1(1) | `s 502.1(1) the accused may appear by audioconference or videoconference` | "may appear by audioconference or videoconference, if arrangements are made with the court in advance and those arrangements are satisfactory to the justice" | part16-notices |
| F-may-502.1(2) | `s 502.1(2) the witness in Canada may give evidence by audioconference or videoconference` | "may do so by audioconference or videoconference, if it is satisfactory to the justice" | part16-notices |
| F-may-502.1(4) | `s 502.1(4) the participant may participate by audioconference or videoconference` | "may participate by audioconference or videoconference, if it is satisfactory to the justice" | part16-notices |
| F-may-502.1(5) | `s 502.1(5) the justice may preside by audioconference or videoconference` | "may preside by audioconference or videoconference, if the justice considers it necessary in the circumstances" | part16-notices |
| F-may-503(3)(b) | `s 503(3)(b) the justice may take that step` | "(b) if the justice is satisfied that there are reasonable grounds to believe that the person arrested is the person alleged to have committed the offence, may" | part16-taking-before-justice |
| F-may-504 | `s 504 any one may lay an information in writing and under oath before a justice` | "Any one who, on reasonable grounds, believes that a person has committed an indictable offence may lay an information" | part16-process |
| F-may-509(5) | `s 509(5) the summons may require the accused to appear for the purposes of the Identification of Criminals Act` | "if the accused is alleged to have committed an offence referred to in paragraph 2(1)(c) of that Act" | part16-process |
| F-may-511(2.1) | `s 511(2.1) the judge or justice may cancel the warrant` | "a judge or justice having jurisdiction in the territorial division in which the warrant was issued may cancel the warrant on application by the prosecutor, ... if the judge or justice is satisfied that it is in the interests of ju" | part16-process |
| F-may-512.1 | `s 512.1 a justice may issue a warrant for the arrest of the accused for the offence` | "If an accused who is required by a summons to appear ... does not appear at that time and place and, in the case of an offence designated as a contravention under the Contraventions Act, the Attorney General ... has not made an el" | part16-process |
| F-may-512.2 | `s 512.2 a justice may issue a warrant for the arrest of the accused for the offence` | "If an accused who is required by an appearance notice or undertaking to appear ... does not appear at that time and place, a justice may, if the appearance notice or undertaking has been confirmed by a justice under section 508, i" | part16-process |
| F-may-512.3 | `s 512.3 a justice may issue a warrant to take the accused before a justice under section 524` | "If a justice is satisfied that there are reasonable grounds to believe ... the justice may issue a warrant" | part16-process |
| F-may-515(2.1) | `s 515(2.1) the judge, justice or court may name particular persons as sureties` | "If, under subsection (2) or any other provision of this Act, a judge, justice or court makes a release order with a requirement for sureties, the judge, justice or court may name particular persons as sureties" | part16-interim-release |
| F-may-515(2.2) | `s 515(2.2) the justice may allow the accused to appear by videoconference or audioconference` | "If, by this Act, the appearance of an accused is required for the purposes of judicial interim release" | part16-interim-release |
| F-may-515(7) | `s 515(7) the new release order may include additional conditions described in subsections (4) to (4.2)` | "If the accused was already at large on a release order, the new release order may include any additional conditions described in subsections (4) to (4.2) that the justice considers desirable" | part16-reverse-onus |
| F-may-515.01 | `s 515.01 the judge or justice may make an order in Form 11.1 requiring the accused to appear for the purposes of the Identification of Criminals Act` | "if the accused is charged with an offence referred to in paragraph 2(1)(c) of that Act" | part16-interim-release |
| F-may-515.1(2) | `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` | "a judge, justice or court may name a person as a surety without a declaration if (a) the prosecutor consents to it; or (b) ..." | part16-interim-release |
| F-may-517(1) | `s 517(1) the justice may make an order directing that the evidence, information, representations and reasons shall not be published` | "If the prosecutor or the accused intends to show cause under section 515, he or she shall so state to the justice and the justice may" | part16-interim-release |
| F-may-520(1) | `s 520(1) the accused may apply to a judge for a review of the order` | "If a judge or justice makes an order under subsection 515(2), (5), (6), (7) or (12) or vacates, varies or makes any order under paragraph 523(2)(b), the accused may" | part16-review |
| F-may-520(7)(e) | `s 520(7)(e) the judge may allow the application, vacate or vary the order and make any other order provided for in section 515` | "(e) if the accused shows cause, allow the application, vacate or vary the order previously made by the justice and make any other order provided for in section 515 that the judge considers is warranted" | part16-review |
| F-may-521(1) | `s 521(1) the prosecutor may apply to a judge for a review of the order` | "If a judge or justice makes an order under subsection 515(1), (2), (7) or (12) or vacates, varies or makes any order under paragraph 523(2)(b), the prosecutor may" | part16-review |
| F-may-521(8)(e) | `s 521(8)(e) the judge may allow the application, vacate or vary the order and make any other order provided for in section 515` | "(e) if the prosecutor shows cause, allow the application, vacate or vary the order previously made by the justice and make any other order provided for in section 515 that the judge considers to be warranted" | part16-review |
| F-may-522(3) | `s 522(3) the judge may make a release order referred to in section 515` | "If the judge does not order that the accused be detained in custody under subsection (2), the judge may make a release order referred to in section 515" | part16-review |
| F-may-523.1(3)(a) | `s 523.1(3)(a) the judge or justice may take no action` | "If the judge or justice ... is satisfied that ..., the judge or justice shall review any conditions of release ... and may, as the case may be, (a) take no action" | part16-failure-and-delay |
| F-may-523.1(3)(b) | `s 523.1(3)(b) the judge or justice may cancel any other summons, appearance notice, undertaking or release order in respect of the accused` | "If the judge or justice ... is satisfied that ..., ... may, as the case may be, ... (b) cancel any other summons, appearance notice, undertaking or release order in respect of the accused" | part16-failure-and-delay |
| F-may-523.1(3)(b)(i) | `s 523.1(3)(b)(i) the judge or justice may make a release order under section 515` | "... (b) cancel any other summons ... and, as the case may be, (i) make a release order under section 515" | part16-failure-and-delay |
| F-may-523.1(3)(b)(ii) | `s 523.1(3)(b)(ii) the judge or justice may make an order that the accused be detained in custody until the accused is dealt with according to law` | "(ii) if the prosecutor shows cause why the detention of the accused in custody is justified under subsection 515(10), make an order that the accused be detained in custody until the accused is dealt with according to law" | part16-failure-and-delay |
| F-may-523.1(3)(c) | `s 523.1(3)(c) the judge or justice may remand the accused to custody for the purposes of the Identification of Criminals Act` | "If the judge or justice ... is satisfied that ..., ... may, as the case may be, ... (c) remand the accused to custody for the purposes of the Identification of Criminals Act" | part16-failure-and-delay |
| F-may-525(3) | `s 525(3) the judge may cancel the hearing` | "The judge may cancel the hearing if the judge receives the accused's waiver before the hearing" | part16-failure-and-delay |
| F-may-525(4)(a) | `s 525(4)(a) the judge may give directions for expediting the proceedings` | "if the judge is concerned that the proceedings are progressing slowly and that an unreasonable delay may result, the judge may (a) give directions for expediting the proceedings" | part16-failure-and-delay |
| F-may-525(4)(b) | `s 525(4)(b) the judge may require a further hearing under this section` | "if the judge is concerned that the proceedings are progressing slowly and that an unreasonable delay may result, the judge may ... (b) require a further hearing under this section" | part16-failure-and-delay |
| F-may-527(1) | `s 527(1) the judge may order in writing that a person who is confined in a prison be brought before the court, judge, justice or provincial court judge` | "may order in writing ... if (a) the applicant ... sets out the facts of the case in an affidavit and produces the warrant, if any; and (b) the judge is satisfied that the ends of justice require that an order be made" | part16-prisoners-and-entry |
| F-may-527(7) | `s 527(7) the judge may order the transfer of the prisoner or other person to the custody of a peace officer named in the order for a period specified in the order` | "may, if a prisoner or a person in the custody of a peace officer consents in writing, order the transfer" | part16-prisoners-and-entry |
| F-may-529(1) | `s 529(1) the warrant may authorize a peace officer to enter a dwelling-house described in the warrant for the purpose of arresting or apprehending the person` | "may authorize a peace officer ... to enter a dwelling-house described in the warrant ... if the judge or justice is satisfied by information on oath in writing that there are reasonable grounds to believe that the person is or wil" | part16-prisoners-and-entry |
| F-may-529.1 | `s 529.1 the judge or justice may issue a warrant in Form 7.1 authorizing a peace officer to enter a dwelling-house described in the warrant` | "may issue a warrant in Form 7.1 ... if the judge or justice is satisfied by information on oath that there are reasonable grounds to believe that the person is or will be present in the dwelling-house and that (a) ...; (b) ...; or" | part16-prisoners-and-entry |
| F-may-529.3(1) | `s 529.3(1) the peace officer may enter the dwelling-house for the purpose of arresting or apprehending a person without a warrant` | "the peace officer may enter the dwelling-house ... without a warrant ... if the peace officer has reasonable grounds to believe that the person is present in the dwelling-house, and the conditions for obtaining a warrant under sec" | part16-prisoners-and-entry |
| F-may-529.4(1) | `s 529.4(1) the judge or justice may authorize the peace officer to enter the dwelling-house without prior announcement` | "may authorize the peace officer to enter the dwelling-house without prior announcement if the judge or justice is satisfied by information on oath that there are reasonable grounds to believe that prior announcement of the entry w" | part16-prisoners-and-entry |

### Listed, not flipped: "may" functions with a "where", "when", "upon" or equivalent gate (22)

Assumed, not ruled, that "on", "on application", "on cause being shown" and "when" go with "upon" (delegated ruling (c) counts "upon" as "where"), and that a period ("at any time before the trial") goes with them.
The answer is the guide's JUST FALSE (ruling (b)); the guide's line on grants points the other way (NOTHING); that is a question for the maintainer or a lawyer and is not settled by this sweep.

| id | function | gate | module |
| --- | --- | --- | --- |
| F-where-503(3)(b) | `s 503(3)(b) the justice may take that step` | "(ii) where the offence was alleged to have been committed within the province in which the person was arrested, order the person to be taken before a justice having jurisdiction with respect to the of" | part16-taking-before-justice |
| F-where-507(8) | `s 507(8) a justice may issue a summons or a warrant for the arrest of the accused to compel attendance` | "Where, on an appeal from or review of any decision or matter of jurisdiction, a new trial or hearing ... is ordered, a justice may issue" | part16-process |
| F-where-511(2.1) | `s 511(2.1) the judge or justice may cancel the warrant` | "may cancel the warrant on application by the prosecutor" | part16-process |
| F-where-512(1) | `s 512(1) the justice may issue a summons or warrant notwithstanding the prior step` | "A justice may, where the justice has reasonable and probable grounds to believe that it is necessary in the public interest to issue a summons or a warrant for the arrest of the accused, issue a summo" | part16-process |
| F-where-512(2) | `s 512(2) a justice may issue a warrant for the arrest of the accused` | "Where (a) service of a summons is proved and the accused fails to attend ..., (b) ..., or (c) ..., a justice may issue a warrant" | part16-process |
| F-where-515(4) | `s 515(4) the justice may direct the accused to comply with the condition` | "When making an order under subsection (2), the justice may direct the accused to comply with one or more of the following conditions" | part16-interim-release |
| F-where-515.01 | `s 515.01 the judge or justice may make an order in Form 11.1 requiring the accused to appear for the purposes of the Identification of Criminals Act` | "When a release order is made under section 515, the judge or justice may also make an order, in Form 11.1" | part16-interim-release |
| F-where-516 | `s 516 the justice may adjourn the proceedings and remand the accused to custody in prison by warrant in Form 19` | "on application by the prosecutor or the accused, adjourn the proceedings" | part16-interim-release |
| F-where-518(2) | `s 518(2) the justice may make any order provided for in this Part for the release of the accused until sentence` | "Where, before or at any time during the course of any proceedings under section 515, the accused pleads guilty and that plea is accepted, the justice may make any order" | part16-interim-release |
| F-where-520(1) | `s 520(1) the accused may apply to a judge for a review of the order` | "the accused may, at any time before the trial of the charge, apply to a judge for a review of the order" | part16-review |
| F-where-520(3) | `s 520(3) the judge may order in writing the person having custody of the accused to bring the accused before the court` | "where the accused is in custody, the judge may order, in writing, the person having the custody of the accused to bring him before the court" | part16-review |
| F-where-520(4) | `s 520(4) the judge may adjourn the proceedings` | "on application by the prosecutor or the accused, adjourn the proceedings" | part16-review |
| F-where-520(5) | `s 520(5) the judge may issue a warrant for the arrest of the accused` | "Where an accused, other than an accused who is in custody, has been ordered by a judge to be present at the hearing of an application under this section and does not attend the hearing, the judge may " | part16-review |
| F-where-521(1) | `s 521(1) the prosecutor may apply to a judge for a review of the order` | "the prosecutor may, at any time before the trial of the charge, apply to a judge for a review of the order" | part16-review |
| F-where-521(3) | `s 521(3) the judge may order in writing the person having custody of the accused to bring the accused before the court` | "where the accused is in custody, the judge may order, in writing, the person having the custody of the accused to bring him before the court" | part16-review |
| F-where-521(5) | `s 521(5) the judge may issue a warrant for the arrest of the accused` | "Where an accused, other than an accused who is in custody, has been ordered by a judge to be present at the hearing of an application under this section and does not attend the hearing, the judge may " | part16-review |
| F-where-522(6) | `s 522(6) the judge may apply the provisions of this Part respecting judicial interim release to the other offence` | "Where an accused is charged with an offence mentioned in section 469 and with any other offence, a judge acting under this section may apply the provisions of this Part" | part16-review |
| F-where-523(2) | `s 523(2) the court, judge or justice may vacate or vary the order previously made and make any other order for the detention or release of the accused` | "may, on cause being shown, vacate or vary any order previously made under this Part" | part16-review |
| F-where-525(4)(a) | `s 525(4)(a) the judge may give directions for expediting the proceedings` | "On the hearing described in subsection (1), the judge shall consider" | part16-failure-and-delay |
| F-where-525(4)(b) | `s 525(4)(b) the judge may require a further hearing under this section` | "On the hearing described in subsection (1), the judge shall consider" | part16-failure-and-delay |
| F-where-527(2) | `s 527(2) a provincial court judge has the same powers for the purposes of subsection (1) or (7) as a judge has under that subsection` | "where the person whose attendance is required is within the province in which the provincial court judge has jurisdiction" | part16-prisoners-and-entry |
| F-where-527(7) | `s 527(7) the judge may order the transfer of the prisoner or other person to the custody of a peace officer named in the order for a period specified in the order` | "On application by the prosecutor, a judge of a superior court of criminal jurisdiction may" | part16-prisoners-and-entry |

### "In any proceedings under section 515": borderline, not counted above

`s 518(1)(a)`, `s 518(1)(c)`, `s 518(1)(d)`, `s 518(1)(d.1)` and `s 518(1)(e)` are "may" functions that begin "In any proceedings under section 515".
They answer NOTHING outside those proceedings, read as a scope limit (guide ruling (c) of the periods ruling).
If a lawyer reads "In any proceedings" as a "where" gate the answer is JUST FALSE; this reading is assumed, not ruled.

### Case-by-case sites: duties and bars, "(other than X)", "unless" and "except" once met (167)

The brief (the maintainer, 2026-11-05) leaves these to the encoder, site by site, with one fork line each for a reviewer to overrule.
The kinds: **duty** is a function named for a duty or a bar ("must", "barred", "not required") whose "if", "where" or similar gate is unmet, taken as "no duty on these facts" or "not barred" (JUST FALSE, on the text's own words; the other reading is NOTHING, the text being silent on a case outside its gate); **other** is an "other than X" carve-out, taken as the text's own exclusion of X (JUST FALSE; the other reading is NOTHING); **unless** is an "unless" or "except" that is met, taken as the text taking the case out in its own words (JUST FALSE; the other reading is NOTHING); **dutyN** is the opposite direction: a duty or a bar whose gate is unmet and which answers NOTHING because the text limits it to a class (or leaves a choice, or does not close a list) and says nothing of the case outside (taken NOTHING; the other reading is JUST FALSE).
A function appears once per kind, the first matching text only; a function's own question ("the circumstances ... exist", a definition) is not a duty and is listed only for an "unless", "except" or "other than" in its text; the seam inputs that carry NOTHING from a section outside this range (s 469, s 3.01 and the like) are not sites and are not listed.
Five "unless" candidates were read and dropped, because the function's own name carries the exception, so that its JUST FALSE is the main rule and not the exception met: the three adjournment limits (`s 516 the adjournment is not for more than three clear days, or the accused consents`, `s 520(4) ...` and `s 521(4) ...`) and the two "subject to review other than under section 680" functions (`s 522(4)`, `s 524(9)`).
Counts: duty 107, other 10, unless 31, dutyN 19.
The other three kinds the brief names do not arise as separate sites: a bare "must" not done is the regulative rules (ss 494(3), 498(1), 503(1), 525(1)), whose breach is a `BREACH` trace outcome and not an answer; "listed in Schedule N" does not occur in this Part (the only lists of offences are in the Code's own sections, s 469 and s 553, which are seams); and Part XVI keeps no state ledger.

| id | kind | function | text | taken | other reading | module |
| --- | --- | --- | --- | --- | --- | --- |
| F-unless-493.01 | unless | `s 493.01 the reference to an indictable offence includes the offence` | "unless the prosecutor has elected to proceed by way of summary conviction" | JUST FALSE | NOTHING | part16-interpretation |
| F-duty-493.1 | duty | `s 493.1 the peace officer, justice or judge must give primary consideration to the release of the accused at the earliest reasonable opportunity and on the least onerous conditions that are appropriate in the circumstances` | "In making a decision under this Part, a peace officer, justice or judge shall give primary consideration" | JUST FALSE | NOTHING | part16-principles |
| F-dutyN-493.1 | dutyN | `s 493.1 the peace officer, justice or judge must give primary consideration to the release of the accused at the earliest reasonable opportunity and on the least onerous conditions that are appropriate in the circumstances` | (limited by its own wording) "a peace officer, justice or judge shall give primary consideration" (the duty is for the three named) | NOTHING | JUST FALSE | part16-principles |
| F-duty-493.11(2)(a) | duty | `s 493.11(2)(a) the peace officer is barred from releasing the accused` | "a peace officer shall not release the accused if the peace officer believes on reasonable grounds that it is necessary in the public interest for the accused to be detained in custody under subsection" | JUST FALSE | NOTHING | part16-principles |
| F-dutyN-493.11(2)(a) | dutyN | `s 493.11(2)(a) the peace officer is barred from releasing the accused` | (limited by its own wording) "(a) a peace officer shall not release the accused" | NOTHING | JUST FALSE | part16-principles |
| F-duty-493.11(2)(b) | duty | `s 493.11(2)(b) the peace officer must impose the least onerous conditions that are appropriate in the circumstances` | "a peace officer shall, if they release the accused, impose the least onerous conditions that are appropriate in the circumstances" | JUST FALSE | NOTHING | part16-principles |
| F-dutyN-493.11(2)(b) | dutyN | `s 493.11(2)(b) the peace officer must impose the least onerous conditions that are appropriate in the circumstances` | (limited by its own wording) "(b) a peace officer shall, if they release the accused, impose the least onerous conditions" | NOTHING | JUST FALSE | part16-principles |
| F-duty-493.11(2)(c) | duty | `s 493.11(2)(c) the justice or judge is barred from giving primary consideration to the release of the accused at the earliest reasonable opportunity` | "shall not give primary consideration to the release of the accused at the earliest reasonable opportunity if the accused is one to whom subsection 515(6), 522(2), 523(2.1) or 524(4) applies" | JUST FALSE | NOTHING | part16-principles |
| F-dutyN-493.11(2)(c) | dutyN | `s 493.11(2)(c) the justice or judge is barred from giving primary consideration to the release of the accused at the earliest reasonable opportunity` | (limited by its own wording) "(c) a justice or judge, as the case may be, shall not give primary consideration" | NOTHING | JUST FALSE | part16-principles |
| F-duty-493.11(2)(d) | duty | `s 493.11(2)(d) the justice or judge must impose the least onerous conditions that are appropriate in the circumstances` | "a justice or judge shall, if they release the accused, impose the least onerous conditions that are appropriate in the circumstances" | JUST FALSE | NOTHING | part16-principles |
| F-dutyN-493.11(2)(d) | dutyN | `s 493.11(2)(d) the justice or judge must impose the least onerous conditions that are appropriate in the circumstances` | (limited by its own wording) "(d) a justice or judge shall, if they release the accused, impose the least onerous conditions" | NOTHING | JUST FALSE | part16-principles |
| F-duty-493.11(2)(e) | duty | `s 493.11(2)(e) the justice or judge is barred from ordering that the accused be released` | "shall not order that the accused be released if the detention of the accused is justified under subsection 515(10)" | JUST FALSE | NOTHING | part16-principles |
| F-dutyN-493.11(2)(e) | dutyN | `s 493.11(2)(e) the justice or judge is barred from ordering that the accused be released` | (limited by its own wording) "(e) a justice or judge shall not order that the accused be released" | NOTHING | JUST FALSE | part16-principles |
| F-duty-493.2 | duty | `s 493.2 the peace officer, justice or judge must give particular attention to the circumstances of the accused` | "In making a decision under this Part, a peace officer, justice or judge shall give particular attention" | JUST FALSE | NOTHING | part16-principles |
| F-dutyN-493.2 | dutyN | `s 493.2 the peace officer, justice or judge must give particular attention to the circumstances of the accused` | (limited by its own wording) "a peace officer, justice or judge shall give particular attention" (the duty is for the three named) | NOTHING | JUST FALSE | part16-principles |
| F-duty-493.2(a) | duty | `s 493.2(a) the accused is an Aboriginal accused, to whose circumstances particular attention must be given` | "(a) Aboriginal accused" | JUST FALSE | NOTHING | part16-principles |
| F-duty-493.2(b) | duty | `s 493.2(b) the accused belongs to a vulnerable population, to whose circumstances particular attention must be given` | "(b) accused who belong to a vulnerable population that is overrepresented in the criminal justice system and that is disadvantaged in obtaining release under this Part" | JUST FALSE | NOTHING | part16-principles |
| F-duty-494(3) | duty | `s 494(3) the arrester must forthwith deliver the person to a peace officer` | "who arrests a person without warrant shall" | JUST FALSE | NOTHING | part16-arrest |
| F-other-494(3) | other | `s 494(3) the arrester must forthwith deliver the person to a peace officer` | "Any one other than a peace officer who arrests a person without warrant shall" | JUST FALSE | NOTHING | part16-arrest |
| F-duty-495(2) | duty | `s 495(2) the peace officer is barred from arresting the person without warrant` | "in any case where (d) he believes on reasonable grounds that the public interest" | JUST FALSE | NOTHING | part16-arrest |
| F-dutyN-495(2) | dutyN | `s 495(2) the peace officer is barred from arresting the person without warrant` | (limited by its own wording) "shall not arrest a person without warrant for (a) an indictable offence mentioned in section 553" (an indictable offence not mentioned there is outside the bar's three limbs) | NOTHING | JUST FALSE | part16-arrest |
| F-unless-495(3) | unless | `s 495(3) the peace officer is deemed to be acting lawfully and in the execution of their duty` | "(b) any other proceedings, unless in any such proceedings it is alleged and established" | JUST FALSE | NOTHING | part16-arrest |
| F-duty-498(1) | duty | `s 498(1) a peace officer must, as soon as practicable, release the person, subject to subsection (1.1)` | "(2) Subsections (1) and (1.01) do not apply in respect of a person who has been arrested without warrant by a peace officer for an offence described in subsection 503(3)" | JUST FALSE | NOTHING | part16-arrest |
| F-other-498(1) | other | `s 498(1) a peace officer must, as soon as practicable, release the person, subject to subsection (1.1)` | "for an offence, other than one listed in section 469" | JUST FALSE | NOTHING | part16-arrest |
| F-duty-498(1.1) | duty | `s 498(1.1) the peace officer must not release the person` | "shall not release the person if the peace officer believes, on reasonable grounds" | JUST FALSE | NOTHING | part16-arrest |
| F-unless-498(3) | unless | `s 498(3) the peace officer is deemed to be acting lawfully and in the execution of the officer's duty` | "(b) any other proceedings, unless in any such proceedings it is alleged and established" | JUST FALSE | NOTHING | part16-arrest |
| F-unless-502.1(1) | unless | `s 502.1(1) the accused must appear in person` | "Except as otherwise provided in this Part, an accused who is required to appear in a proceeding under this Part shall appear in person" | JUST FALSE | NOTHING | part16-notices |
| F-duty-503(1) | duty | `s 503(1) the peace officer must cause the person to be taken before a justice` | "a peace officer who arrests a person with or without warrant" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-duty-503(1.1) | duty | `s 503(1.1) the peace officer must release the person` | "At any time before the expiry of the time referred to in paragraph (1)(a) or (b)" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-duty-503(3) | duty | `s 503(3) the person must, within the time prescribed in paragraph (1)(a) or (b), be taken before a justice within whose jurisdiction the person was arrested` | "Where a person has been arrested without warrant for an indictable offence alleged to have been committed in Canada outside the territorial division where the arrest took place" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-unless-503(3) | unless | `s 503(3) the person must, within the time prescribed in paragraph (1)(a) or (b), be taken before a justice within whose jurisdiction the person was arrested` | "unless, where the offence was alleged to have been committed within the province in which the person was arrested, the person was taken before a justice within whose jurisdiction the offence was alleg" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-duty-503(3)(a) | duty | `s 503(3)(a) the justice must release the person` | "(a) if the justice is not satisfied that there are reasonable grounds to believe that the person arrested is the person alleged to have committed the offence, shall release that person" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-duty-503(3)(b)(i) | duty | `s 503(3)(b)(i) the person in whose custody the person then is must release them` | "(i) remand the person to the custody of a peace officer to await execution of a warrant for his or her arrest in accordance with section 528, but if no warrant is so executed" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-duty-503(4) | duty | `s 503(4) the peace officer must release the person as soon as practicable` | "shall release that person as soon as practicable after the officer is satisfied that the continued detention of that person is no longer necessary" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-unless-503(5) | unless | `s 503(5) the peace officer is deemed to be acting lawfully and in the execution of the peace officer's duty` | "(b) any other proceedings, unless in those proceedings it is alleged and established by the person making the allegation" | JUST FALSE | NOTHING | part16-taking-before-justice |
| F-duty-504 | duty | `s 504 the justice must receive the information` | "the justice shall receive the information, where it is alleged (a) ... (b) ... (c) ... or (d) ..." | JUST FALSE | NOTHING | part16-process |
| F-duty-505 | duty | `s 505 an information must be laid before a justice` | "If an appearance notice has been issued to an accused under section 497, or if an accused has been released from custody under section 498 or 503, an information ... shall be laid" | JUST FALSE | NOTHING | part16-process |
| F-duty-507(1) | duty | `s 507(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` | "Subject to subsection 523(1.1)" | JUST FALSE | NOTHING | part16-process |
| F-other-507(1) | other | `s 507(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` | "other than an information laid before the justice under section 505" | JUST FALSE | NOTHING | part16-process |
| F-unless-507(1) | unless | `s 507(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` | "except if an accused has already been arrested with or without a warrant" | JUST FALSE | NOTHING | part16-process |
| F-duty-507(1)(a.1) | duty | `s 507(1)(a.1) the hearing must be held in camera` | "(a.1) if a hearing is held, hold it in camera" | JUST FALSE | NOTHING | part16-process |
| F-duty-507(1)(b) | duty | `s 507(1)(b) the justice must issue a summons or a warrant for the arrest of the accused` | "(b) where he considers that a case for so doing is made out, issue, in accordance with this section, either a summons or a warrant" | JUST FALSE | NOTHING | part16-process |
| F-dutyN-507(2) | dutyN | `s 507(2) the justice must not refuse to issue a summons or warrant` | (limited by its own wording) "No justice shall refuse to issue a summons or warrant by reason only that the alleged offence is one for which a person may be arrested without warrant" (the bar is limited to that one reason) | NOTHING | JUST FALSE | part16-process |
| F-duty-507(3) | duty | `s 507(3) the justice must take the evidence on oath and in accordance with section 540` | "A justice who hears the evidence of a witness pursuant to subsection (1) shall (a) take the evidence on oath; and (b) cause the evidence to be taken in accordance with section 540" | JUST FALSE | NOTHING | part16-process |
| F-duty-507(4) | duty | `s 507(4) the justice must issue a summons to the accused` | "Where a justice considers that a case is made out for compelling an accused to attend before him to answer to a charge of an offence, he shall issue a summons" | JUST FALSE | NOTHING | part16-process |
| F-unless-507(4) | unless | `s 507(4) the justice must issue a summons to the accused` | "unless the allegations of the informant or the evidence of any witness or witnesses ... discloses reasonable grounds to believe that it is necessary in the public interest to issue a warrant" | JUST FALSE | NOTHING | part16-process |
| F-duty-507(5) | duty | `s 507(5) the justice is barred from signing the summons or warrant` | "A justice shall not sign a summons or warrant in blank" | JUST FALSE | NOTHING | part16-process |
| F-other-507.1(1) | other | `s 507.1(1) the justice must refer the information to a provincial court judge, a judge of the Court of Quebec or a designated justice` | "A justice who receives an information laid under section 504, other than an information referred to in subsection 507(1), shall refer it" | JUST FALSE | NOTHING | part16-process |
| F-duty-507.1(2) | duty | `s 507.1(2) the judge or designated justice must issue a summons or warrant for the arrest of the accused` | "A judge or designated justice to whom an information is referred under subsection (1) and who considers that a case for doing so is made out shall issue" | JUST FALSE | NOTHING | part16-process |
| F-duty-507.1(5) | duty | `s 507.1(5) the judge or designated justice must endorse the information with a statement to that effect` | "If the judge or designated justice does not issue a summons or warrant under subsection (2), he or she shall endorse the information" | JUST FALSE | NOTHING | part16-process |
| F-unless-507.1(5) | unless | `s 507.1(5) the information is deemed never to have been laid` | "Unless the informant, not later than six months after the endorsement, commences proceedings to compel the judge or designated justice to issue a summons or warrant" | JUST FALSE | NOTHING | part16-process |
| F-duty-507.1(7) | duty | `s 507.1(7) another hearing under paragraph (3)(a) on the offence or an included offence is barred` | "If a hearing in respect of an offence has been held under paragraph (3)(a) and the judge or designated justice has not issued a summons or a warrant, no other hearings may be held" | JUST FALSE | NOTHING | part16-process |
| F-unless-507.1(7) | unless | `s 507.1(7) another hearing under paragraph (3)(a) on the offence or an included offence is barred` | "unless there is new evidence in support of the allegation in respect of which the hearing is sought to be held" | JUST FALSE | NOTHING | part16-process |
| F-duty-508(1) | duty | `s 508(1) the justice must hear and consider the allegations of the informant and any evidence of witnesses, ex parte` | "A justice who receives an information laid before him under section 505 shall" | JUST FALSE | NOTHING | part16-process |
| F-duty-508(1)(a.1) | duty | `s 508(1)(a.1) the hearing must be held in camera` | "(a.1) if a hearing is held, hold it in camera" | JUST FALSE | NOTHING | part16-process |
| F-duty-508(1)(b) | duty | `s 508(1)(b) the justice must take that step` | "(b) if the justice considers that a case for so doing is made out" | JUST FALSE | NOTHING | part16-process |
| F-dutyN-508(1)(b) | dutyN | `s 508(1)(b) the justice must take that step` | (limited by its own wording) "(iii) in the case of the undertaking, amend it" | NOTHING | JUST FALSE | part16-process |
| F-duty-508(1)(c) | duty | `s 508(1)(c) the justice must cancel the appearance notice or undertaking and cause the accused to be immediately notified` | "(c) if the justice considers that a case is not made out for the purposes of paragraph (b), cancel the appearance notice or undertaking" | JUST FALSE | NOTHING | part16-process |
| F-duty-508(2) | duty | `s 508(2) the justice must take the evidence on oath and in accordance with section 540` | "A justice who hears the evidence of a witness pursuant to subsection (1) shall (a) take the evidence on oath" | JUST FALSE | NOTHING | part16-process |
| F-duty-515(1) | duty | `s 515(1) the justice must make a release order without conditions` | "when an accused ... is taken before a justice, the justice shall" | JUST FALSE | NOTHING | part16-interim-release |
| F-other-515(1) | other | `s 515(1) the justice must make a release order without conditions` | "an accused who is charged with an offence other than an offence listed in section 469" | JUST FALSE | NOTHING | part16-interim-release |
| F-unless-515(1) | unless | `s 515(1) the justice must make a release order without conditions` | "unless a plea of guilty by the accused is accepted" | JUST FALSE | NOTHING | part16-interim-release |
| F-unless-515(2) | unless | `s 515(2) the justice must make a release order that sets out the conditions directed under subsection (4)` | "If the justice does not make an order under subsection (1), the justice shall, unless the prosecutor shows cause why the detention of the accused is justified, make a release order" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(2.01) | duty | `s 515(2.01) the justice is barred from making an order containing the term` | "(2.04) Subsection (2.01) does not apply to an accused to whom subsection (6) applies" | JUST FALSE | NOTHING | part16-interim-release |
| F-dutyN-515(2.01) | dutyN | `s 515(2.01) the justice is barred from making an order containing the term` | (limited by its own wording) "shall not make an order containing the conditions referred to in one of the paragraphs (2)(b) to (e)" (paragraph (a) is outside the bar) | NOTHING | JUST FALSE | part16-interim-release |
| F-unless-515(2.01) | unless | `s 515(2.01) the justice is barred from making an order containing the term` | "unless the prosecution shows cause why an order containing the conditions referred to in the preceding paragraphs for any less onerous form of release would be inadequate" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(2.02) | duty | `s 515(2.02) the justice must favour a promise to pay an amount over the deposit of an amount of money` | "The justice shall favour a promise to pay an amount over the deposit of an amount of money if the accused or the surety, if applicable, has reasonably recoverable assets" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(2.03) | duty | `s 515(2.03) the justice must be satisfied that a surety is the least onerous form of release possible for the accused` | "before making an order requiring that the accused have a surety, the justice shall be satisfied that this requirement is the least onerous form of release possible" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(2.11) | duty | `s 515(2.11) the judge, justice or court is barred from naming the person as surety` | "if the person was convicted of an indictable offence" | JUST FALSE | NOTHING | part16-interim-release |
| F-unless-515(2.11) | unless | `s 515(2.11) the judge, justice or court is barred from naming the person as surety` | "unless the judge, justice or court is satisfied that no other suitable surety is available and that doing so is in the interests of justice" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(2.12) | duty | `s 515(2.12) the judge, justice or court must include in the record a statement of the reasons for naming the person` | "If a judge, justice or court names a person described in subsection (2.11) as a surety, the judge, justice or court shall include in the record a statement of the reasons" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(2.2) | duty | `s 515(2.2) the accused must appear in person` | "If, by this Act, the appearance of an accused is required for the purposes of judicial interim release, the accused shall appear in person" | JUST FALSE | NOTHING | part16-interim-release |
| F-dutyN-515(3) | dutyN | `s 515(3) the justice must consider the factor` | (silent) "the justice shall consider any relevant factors, including" names three factors and says nothing of a factor that is not relevant | NOTHING | JUST FALSE | part16-interim-release |
| F-duty-515(4.1) | duty | `s 515(4.1) the justice must add a condition prohibiting the accused from possessing a firearm and the other things` | "When the justice makes an order under subsection (2) in respect of an accused who is charged with any of the following offences, the justice shall add" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-unless-515(4.1) | unless | `s 515(4.1) the justice must add a condition prohibiting the accused from possessing a firearm and the other things` | "unless the justice considers that such a condition is not required" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(4.11) | duty | `s 515(4.11) the justice must specify in the order the manner and method of surrender, disposal, detention or storage` | "Where the justice adds a condition described in subsection (4.1) to an order made under subsection (2), the justice shall specify in the order the manner and method" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(4.12) | duty | `s 515(4.12) the justice must include in the record a statement of the reasons for not adding the condition` | "Where the justice does not add a condition described in subsection (4.1) to an order made under subsection (2), the justice shall include in the record a statement of the reasons" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(4.2) | duty | `s 515(4.2) the justice must consider whether it is desirable to include the condition` | "Before making an order under subsection (2), in the case of an accused who is charged with an offence referred to in subsection (4.3), the justice shall consider" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(4.4) | duty | `s 515(4.4) the justice must consider whether it is desirable to include the condition` | "Before making an order under subsection (2) in respect of an accused who is charged with an offence described in subsection 333.1(1), (3) or (4) or paragraph 348(1)(d), the justice shall consider" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(5) | duty | `s 515(5) the justice must order that the accused be detained in custody and state the reasons in the record` | "Where the prosecutor shows cause why the detention of the accused in custody is justified, the justice shall order that the accused be detained in custody" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(6) | duty | `s 515(6) the justice must order that the accused be detained in custody` | "the justice shall order ... that the accused be detained in custody ... if the accused is charged" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-unless-515(6) | unless | `s 515(6) the justice must order that the accused be detained in custody` | "Unless the accused, having been given a reasonable opportunity to do so, shows cause why the accused’s detention in custody is not justified" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-other-515(6)(a) | other | `s 515(6)(a) the accused is charged with an indictable offence, other than an offence listed in section 469, of the kind described in subparagraphs (i) to (xiv)` | "with an indictable offence, other than an offence listed in section 469" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-other-515(6)(b) | other | `s 515(6)(b) the accused is charged with an indictable offence, other than an offence listed in section 469, and is not ordinarily resident in Canada` | "(b) with an indictable offence, other than an offence listed in section 469" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(6.1) | duty | `s 515(6.1) the justice must include in the record a statement of the reasons for ordering the release` | "If the justice orders that an accused to whom subsection (6) applies be released, the justice shall include in the record a statement of the justice’s reasons" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(7) | duty | `s 515(7) the justice must make a release order under section 515` | "If an accused to whom subsection (6) applies shows cause why their detention in custody is not justified, the justice shall make a release order under this section" | JUST FALSE | NOTHING | part16-reverse-onus |
| F-duty-515(9.1) | duty | `s 515(9.1) the justice must state in writing, in the record, that the detention is ordered primarily because of a previous conviction` | "if the justice orders that the accused be detained in custody primarily because of a previous conviction of the accused, the justice shall state that reason, in writing, in the record" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(11) | duty | `s 515(11) the justice must order that the accused be detained in custody and issue a warrant in Form 8 for the committal` | "Where an accused who is charged with an offence mentioned in section 469 is taken before a justice, the justice shall order that the accused be detained in custody" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(13) | duty | `s 515(13) the justice must include in the record a statement that the justice considered the safety and security of every victim and of the community` | "A justice who makes an order under this section shall include in the record of the proceedings a statement that the justice considered the safety and security of every victim of the offence and the sa" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(13.1) | duty | `s 515(13.1) the justice must include in the record a statement of how the justice determined whether the accused is an accused referred to in section 493.2, and the determination` | "A justice who makes an order under this section shall include in the record of proceedings a statement that sets out both how they determined whether the accused is an accused referred to in section 4" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(13.1)-2 | duty | `s 515(13.1) the justice must also include a statement of how the justice considered the accused's particular circumstances` | "If the justice determines that the accused is an accused referred to in section 493.2, they shall also include a statement indicating how they considered their particular circumstances" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(14) | duty | `s 515(14) the justice must cause a copy of the order to be given to the victim` | "If an order is made under this section, the justice shall, on request by a victim of the offence, cause a copy of the order to be given to the victim" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-515(14.1) | duty | `s 515(14.1) the justice must ask the prosecutor whether victims of the offence have been informed of their right to request a copy` | "Upon making an order under subsection (2), the justice must ask the prosecutor whether victims of the offence have been informed of their right to request a copy of the order" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-517(1) | duty | `s 517(1) the justice must make the order on the application of the accused` | "the justice may, and shall on application by the accused" | JUST FALSE | NOTHING | part16-interim-release |
| F-unless-518(1)(b) | unless | `s 518(1)(b) the accused is barred from being examined by the justice or any other person except counsel for the accused` | "the accused shall not be examined by the justice or any other person except counsel for the accused respecting the offence with which the accused is charged" | JUST FALSE | NOTHING | part16-interim-release |
| F-unless-518(1)(b)-2 | unless | `s 518(1)(b) the accused is barred from being cross-examined on the offence` | "no inquiry shall be made of the accused respecting that offence by way of cross-examination unless the accused has testified respecting the offence" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-518(1)(d.2) | duty | `s 518(1)(d.2) the justice must take the evidence into consideration` | "the justice shall take into consideration any evidence submitted regarding the need to ensure the safety or security of any victim of or witness to an offence" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-519(1)(a) | duty | `s 519(1)(a) the justice must direct that the accused be released forthwith` | "(a) if the accused thereupon complies with the order, the justice shall direct that the accused be released (i) forthwith, if the accused is not required to be detained in custody in respect of any ot" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-519(1)(a)-2 | duty | `s 519(1)(a) the justice must direct that the accused be released as soon as the accused is no longer required to be detained in respect of another matter` | "(ii) as soon thereafter as the accused is no longer required to be detained in custody in respect of any other matter" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-519(1)(b) | duty | `s 519(1)(b) the justice who made the order or another justice having jurisdiction must issue a warrant for the committal of the accused` | "(b) if the accused does not thereupon comply with the order, the justice who made the order or another justice having jurisdiction shall issue a warrant for the committal of the accused" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-519(1)(b)-2 | duty | `s 519(1)(b) the justice must attach a copy of the order to the warrant` | "and if the justice so endorses the warrant, he shall attach to it a copy of the order" | JUST FALSE | NOTHING | part16-interim-release |
| F-unless-519(2) | unless | `s 519(2) the justice must issue an order for discharge in Form 39` | "Where the accused complies with an order referred to in paragraph (1)(b) and is not required to be detained in custody in respect of any other matter, the justice ... shall, unless the accused has bee" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-519(3) | duty | `s 519(3) the justice must issue a warrant for the committal of the accused` | "Where the justice makes an order under subsection 515(5) or (6) for the detention of the accused, he shall issue a warrant for the committal of the accused" | JUST FALSE | NOTHING | part16-interim-release |
| F-duty-520(3) | duty | `s 520(3) the accused must be present at the hearing` | "If the judge so orders or the prosecutor or the accused or his counsel so requests, the accused shall be present at the hearing" | JUST FALSE | NOTHING | part16-review |
| F-duty-520(7) | duty | `s 520(7) the judge must dismiss the application` | "On the hearing of an application under this section, the judge ... shall either (d) dismiss the application, or (e) ..." | JUST FALSE | NOTHING | part16-review |
| F-dutyN-520(7) | dutyN | `s 520(7) the judge must dismiss the application` | (silent) "shall either (d) dismiss the application, or (e) if the accused shows cause, allow the application": where cause is shown the text leaves the choice between (d) and (e) to the judge | NOTHING | JUST FALSE | part16-review |
| F-duty-520(8) | duty | `s 520(8) the further application is barred` | "If an application under this section or section 521 or 525 has been heard, a further or other application ... shall not be made" | JUST FALSE | NOTHING | part16-review |
| F-unless-520(8) | unless | `s 520(8) the further application is barred` | "except with leave of a judge" | JUST FALSE | NOTHING | part16-review |
| F-duty-521(3) | duty | `s 521(3) the accused must be present at the hearing` | "If the judge so orders or the prosecutor or the accused or his counsel so requests, the accused shall be present at the hearing" | JUST FALSE | NOTHING | part16-review |
| F-duty-521(6) | duty | `s 521(6) the judge must issue a warrant for the committal of the accused` | "Where, pursuant to paragraph (8)(e), the judge makes an order that the accused be detained in custody until he is dealt with according to law, he shall, if the accused is not in custody, issue a warra" | JUST FALSE | NOTHING | part16-review |
| F-duty-521(8) | duty | `s 521(8) the judge must dismiss the application` | "On the hearing of an application under this section, the judge ... shall either (d) dismiss the application, or (e) ..." | JUST FALSE | NOTHING | part16-review |
| F-dutyN-521(8) | dutyN | `s 521(8) the judge must dismiss the application` | (silent) "shall either (d) dismiss the application, or (e) if the prosecutor shows cause, allow the application": where cause is shown the text leaves the choice between (d) and (e) to the judge | NOTHING | JUST FALSE | part16-review |
| F-duty-521(9) | duty | `s 521(9) the further application is barred` | "If an application under this section or section 520 or 525 has been heard, a further or other application ... shall not be made" | JUST FALSE | NOTHING | part16-review |
| F-unless-521(9) | unless | `s 521(9) the further application is barred` | "except with leave of a judge" | JUST FALSE | NOTHING | part16-review |
| F-duty-522(1) | duty | `s 522(1) the court, judge or justice is barred from releasing the accused` | "Where an accused is charged with an offence listed in section 469, no court, judge or justice ... may release the accused" | JUST FALSE | NOTHING | part16-review |
| F-other-522(1) | other | `s 522(1) the court, judge or justice is barred from releasing the accused` | "no court, judge or justice, other than a judge of or a judge presiding in a superior court of criminal jurisdiction for the province in which the accused is so charged, may release the accused" | JUST FALSE | NOTHING | part16-review |
| F-duty-522(2) | duty | `s 522(2) the judge must order that the accused be detained in custody` | "Where an accused is charged with an offence listed in section 469, a judge of or a judge presiding in a superior court of criminal jurisdiction ... shall order that the accused be detained in custody" | JUST FALSE | NOTHING | part16-review |
| F-unless-522(2) | unless | `s 522(2) the judge must order that the accused be detained in custody` | "unless the accused, having been given a reasonable opportunity to do so, shows cause why their detention in custody is not justified" | JUST FALSE | NOTHING | part16-review |
| F-unless-522(5) | unless | `s 522(5) subsection 518(2) applies to the application` | "The provisions of sections 517, 518 except subsection (2) thereof, and 519 apply with such modifications as the circumstances require in respect of an application for an order under subsection (2)" | JUST FALSE | NOTHING | part16-review |
| F-duty-523(2.1) | duty | `s 523(2.1) the court, judge or justice must order that the accused be detained in custody` | "if the prosecutor brings an application to vacate an order for the interim release of the accused after the accused is, at their trial, determined to be guilty ..., the court, judge or justice shall o" | JUST FALSE | NOTHING | part16-review |
| F-other-523(2.1) | other | `s 523(2.1) the court, judge or justice must order that the accused be detained in custody` | "after the accused is, at their trial, determined to be guilty of an offence other than an offence listed in section 469 and before a sentence within the meaning of section 673 is imposed" | JUST FALSE | NOTHING | part16-review |
| F-unless-523(2.1) | unless | `s 523(2.1) the court, judge or justice must order that the accused be detained in custody` | "unless the accused, having been given a reasonable opportunity to do so, shows cause why their detention in custody is not justified" | JUST FALSE | NOTHING | part16-review |
| F-unless-523(3) | unless | `s 523(3) subsection 518(2) applies to the proceedings under subsection (2)` | "except that subsection 518(2) does not apply in respect of an accused who is charged with an offence listed in section 469" | JUST FALSE | NOTHING | part16-review |
| F-duty-523.1(1)(b) | duty | `s 523.1(1)(b) the justice must hear the matter` | "When an accused appears before a justice in any of the circumstances described in subsection (2), the justice shall" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-523.1(3) | duty | `s 523.1(3) the judge or justice must review any conditions of release that have been imposed on the accused` | "If the judge or justice who hears the matter is satisfied that the accused failed to comply ... and that the failure did not cause a victim physical or emotional harm, property damage or economic loss" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-523.1(3)(b)(ii) | duty | `s 523.1(3)(b)(ii) the judge or justice must include in the record a statement of the reasons for making the order` | "and if so detained, the judge or justice shall include in the record a statement of the judge's or justice's reasons for making the order" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-523.1(4) | duty | `s 523.1(4) the judge or justice must dismiss the charge` | "If a charge has been laid against the accused for the failure referred to in paragraph (2)(a) and the judge or justice, as the case may be, makes a decision under subsection (3), the judge or justice " | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-523.1(5) | duty | `s 523.1(5) the laying of an information or the preferring of an indictment against the accused for the failure referred to in paragraph (2)(a) is barred` | "If the judge or justice makes a decision under subsection (3), no information may be laid nor indictment be preferred against the accused for the failure referred to in paragraph (2)(a)" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-524(1)(b) | duty | `s 524(1)(b) the justice must hear the matter` | "When an accused is taken before a justice in any of the circumstances described in subsection (2), the justice shall" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-524(3) | duty | `s 524(3) the judge or justice must cancel the summons, appearance notice, undertaking or release order` | "shall cancel a summons, appearance notice, undertaking or release order in respect of the accused if the judge or justice finds that (a) ... or (b) ..." | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-524(4) | duty | `s 524(4) the judge or justice must order that the accused be detained in custody` | "If the judge or justice cancels the summons, appearance notice, undertaking or release order, the judge or justice shall, in the following circumstances, order that the accused be detained in custody" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-unless-524(4) | unless | `s 524(4) the judge or justice must order that the accused be detained in custody` | "unless the accused, having been given a reasonable opportunity to do so, shows cause why their detention in custody is not justified under subsection 515(10)" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-524(5) | duty | `s 524(5) the judge or justice must make a release order referred to in section 515` | "If the judge or justice does not order that the accused be detained in custody under subsection (4), the judge or justice shall make a release order" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-dutyN-524(5) | dutyN | `s 524(5) the judge or justice must make a release order referred to in section 515` | (silent) subsection (5) says what follows when the judge or justice "does not order that the accused be detained in custody under subsection (4)"; for an accused to whom (4) does not apply, (6.1) and (6.2) speak | NOTHING | JUST FALSE | part16-failure-and-delay |
| F-duty-524(6) | duty | `s 524(6) the judge or justice must include in the record a statement of the reasons for making the release order` | "If the judge or justice makes a release order under subsection (5), the judge or justice shall include in the record a statement of the reasons for making the order" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-524(6.1) | duty | `s 524(6.1) the judge or justice must make a release order referred to in section 515` | "If the judge or justice cancels the summons, appearance notice, undertaking or release order in respect of an accused to whom subsection (4) does not apply" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-unless-524(6.1) | unless | `s 524(6.1) the judge or justice must make a release order referred to in section 515` | "unless the prosecutor shows cause why the detention of the accused is justified" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-524(6.2) | duty | `s 524(6.2) the judge or justice must make a detention order referred to in section 515` | "If the judge or justice does not make a release order under subsection (6.1), they shall make a detention order referred to in section 515" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-dutyN-524(6.2) | dutyN | `s 524(6.2) the judge or justice must make a detention order referred to in section 515` | (silent) subsection (6.2) says what follows when the judge or justice "does not make a release order under subsection (6.1)"; it is read with (6.1) and says nothing where (6.1) is not engaged | NOTHING | JUST FALSE | part16-failure-and-delay |
| F-duty-524(7) | duty | `s 524(7) the judge or justice must order that the accused be released from custody` | "If the judge or justice does not cancel the summons, appearance notice, undertaking or release order under subsection (3), the judge or justice shall order that the accused be released from custody" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-unless-524(8) | unless | `s 524(8) subsection 518(2) applies to the proceedings under this section` | "except that subsection 518(2) does not apply in respect of an accused who is charged with an offence mentioned in section 469" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(1) | duty | `s 525(1) the person having the custody of the accused must apply to a judge to fix a date for a hearing` | "who is being detained in custody pending their trial for that offence" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-other-525(1) | other | `s 525(1) the person having the custody of the accused must apply to a judge to fix a date for a hearing` | "who has been charged with an offence other than an offence listed in section 469" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(1.1) | duty | `s 525(1.1) the person having the custody of the accused is not required to make the application` | "is not required to make the application if the accused has waived in writing their right to a hearing and the judge has received the waiver before the expiry of the 90-day period referred to in subsec" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(2)(a) | duty | `s 525(2)(a) the judge must fix a date for the hearing described in subsection (1)` | "On receiving an application under subsection (1), the judge shall (a) fix a date for the hearing" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(2)(b) | duty | `s 525(2)(b) the judge must direct that notice of the hearing be given` | "On receiving an application under subsection (1), the judge shall ... (b) direct that notice of the hearing be given" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-dutyN-525(2)(b) | dutyN | `s 525(2)(b) the person is one to whom notice of the hearing must be given` | (includes) "to such persons, including the prosecutor and the accused" (other persons are those the judge specifies) | NOTHING | JUST FALSE | part16-failure-and-delay |
| F-duty-525(4) | duty | `s 525(4) the judge must consider whether the prosecutor or the accused has been responsible for any delay` | "On the hearing described in subsection (1), the judge shall consider whether the prosecutor or the accused has been responsible for any delay" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(4.1) | duty | `s 525(4.1) the judge must order the release or detention of the accused on cause being shown in accordance with section 515` | "if in conducting the hearing referred to in subsection (1) the judge conducts a proceeding under section 515, they shall order the release or detention of the accused on cause being shown in accordanc" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(5) | duty | `s 525(5) the judge must make a release order referred to in section 515` | "If, following the hearing, the judge is not satisfied that the continued detention of the accused in custody is justified within the meaning of subsection 515(10), the judge shall make a release order" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(5.1) | duty | `s 525(5.1) the judge must make an order that the accused continue to be detained` | "If the judge does not make a release order under subsection (5), the judge shall make an order that the accused continue to be detained" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-525(5.2) | duty | `s 525(5.2) a further hearing under this section is barred` | "after an order is made under subsection (5.1), no further hearing under this section shall be held" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-unless-525(5.2) | unless | `s 525(5.2) a further hearing under this section is barred` | "unless required by the judge under paragraph (4)(b)" | JUST FALSE | NOTHING | part16-failure-and-delay |
| F-duty-527(3) | duty | `s 527(3) the order must be addressed to the person who has custody of the prisoner` | "An order that is made under subsection (1) or (2) shall be addressed to the person who has custody of the prisoner" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-527(3)(a) | duty | `s 527(3)(a) the person who has custody of the prisoner must deliver the prisoner to the person named in the order to receive the prisoner, or do what paragraph (b) requires` | "on receipt thereof that person shall (a) deliver the prisoner to any person who is named in the order to receive him" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-527(3)(b) | duty | `s 527(3)(b) the person who has custody of the prisoner must bring the prisoner before the court, judge, justice or provincial court judge, or do what paragraph (a) requires` | "on receipt thereof that person shall ... (b) bring the prisoner before the court, judge, justice or provincial court judge, as the case may be, on payment of his reasonable charges in respect thereof" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-527(4) | duty | `s 527(4) the judge or provincial court judge must direct in the order the manner in which the prisoner is to be kept in custody and returned to the prison` | "Where a prisoner is required as a witness, the judge or provincial court judge shall direct, in the order, the manner in which the prisoner shall be kept in custody and returned to the prison from whi" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-527(5) | duty | `s 527(5) the judge or provincial court judge must give appropriate directions in the order with respect to the manner in which the prisoner is to be kept in custody or returned` | "If the appearance of a prisoner is required for the purposes of subsection (1), the judge or provincial court judge shall give appropriate directions in the order" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-527(8) | duty | `s 527(8) the order must be addressed to the person who has custody of the prisoner` | "An order under subsection (7) shall be addressed to the person who has custody of the prisoner" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-527(8)-2 | duty | `s 527(8) the person who has custody of the prisoner must deliver the prisoner to the peace officer who is named in the order to receive the prisoner` | "on receipt thereof that person shall deliver the prisoner to the peace officer who is named in the order to receive him" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-527(9) | duty | `s 527(9) the prisoner must be returned to the place where the prisoner was confined at the time the order was made` | "When the purposes of any order made under this section have been carried out, the prisoner shall be returned to the place where he was confined at the time the order was made" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-528(1) | duty | `s 528(1) the justice must authorize the arrest of the accused within the justice's jurisdiction by making an endorsement on the warrant` | "Where a warrant for the arrest or committal of an accused, in any form set out in Part XXVIII in relation thereto, cannot be executed in accordance with section 514 or 703, a justice within whose juri" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-dutyN-529(2) | dutyN | `s 529(2) the peace officer is barred from entering the dwelling-house` | (limited by its own wording) "An authorization to enter a dwelling-house granted under subsection (1) is subject to the condition" (the bar is for an authorization granted under subsection (1)) | NOTHING | JUST FALSE | part16-prisoners-and-entry |
| F-unless-529(2) | unless | `s 529(2) the peace officer is barred from entering the dwelling-house` | "the peace officer may not enter the dwelling-house unless the peace officer has, immediately before entering the dwelling-house, reasonable grounds to believe that the person to be arrested or apprehe" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-duty-529.2 | duty | `s 529.2 the judge or justice must include the term or condition in the warrant` | "the judge or justice shall include in a warrant referred to in section 529 or 529.1 any terms and conditions that the judge or justice considers advisable to ensure that the entry into the dwelling-ho" | JUST FALSE | NOTHING | part16-prisoners-and-entry |
| F-dutyN-529.4(3) | dutyN | `s 529.4(3) the peace officer is barred from entering the dwelling-house without prior announcement` | (limited by its own wording) "A peace officer who enters a dwelling-house without a warrant under section 529.3 may not enter the dwelling-house without prior announcement" (the bar is for an entry under section 529.3) | NOTHING | JUST FALSE | part16-prisoners-and-entry |
| F-unless-529.4(3) | unless | `s 529.4(3) the peace officer is barred from entering the dwelling-house without prior announcement` | "may not enter the dwelling-house without prior announcement unless the peace officer has, immediately before entering the dwelling-house, (a) reasonable grounds to suspect that prior announcement of t" | JUST FALSE | NOTHING | part16-prisoners-and-entry |

## Jural relations (ccc20)

Kinds follow Hohfeld; the person in the seat is the accused.
A bar on an official is a disability of the official and an immunity of the accused; a duty of an official is a claim of the accused.

| provision | holder | kind | against | content |
| --- | --- | --- | --- | --- |
| 494(1), (2) | any one; an owner of property | privilege (liberty) | the person arrested | to arrest without warrant in the cases listed; the arrested person has no claim that they not be arrested then |
| 494(3) | a person other than a peace officer who arrests | duty | the person arrested (claim: to be delivered forthwith to a peace officer) | to deliver the person forthwith to a peace officer |
| 495(1) | a peace officer | power | the person arrested (liability) | to arrest without warrant in the three cases |
| 495(2) | a peace officer | disability | the person (immunity) | may not arrest for the three kinds of offence where the public interest is satisfied without it and attendance is not in doubt |
| 495.1, 496, 497 | a peace officer | power | the accused | to arrest on a failure to comply; to issue an appearance notice |
| 498(1) | a peace officer | duty | the accused (claim to release) | to release as soon as practicable on summons, appearance notice or undertaking |
| 498(1.1) | a peace officer | disability | the accused | may not release where detention is necessary in the public interest or attendance in doubt |
| 499 | a peace officer | power | the accused | to release a person arrested with a warrant that a justice has endorsed |
| 500 to 502 | a peace officer; the accused; the prosecutor | power; privilege | each other | contents of notices and undertakings; variation by consent or application |
| 502.1 | the accused; a witness; a justice | privilege | - | to take part by audioconference or videoconference where the justice allows |
| 503(1), (1.1) | a peace officer | duty | the accused (claim to be taken before a justice within 24 hours, or released) | to take before a justice; to release when detention is no longer necessary |
| 503(3), (3.1) | a justice | duty; power | the person arrested | to release or remand a person arrested for an offence elsewhere |
| 504 to 514 | any one; a justice; a judge | power | the accused (liability to process) | to lay an information; to issue a summons or warrant; to cancel; to execute |
| 507.1(5) | the informant | power with a time limit | the accused | six months to compel issue; then the information is deemed never laid |
| 515(1), (2) | a justice | duty | the accused (claim to release) | to make a release order without conditions, or with conditions, unless the prosecutor shows cause |
| 515(5), (6) | a justice | duty | the accused | to detain unless the accused shows cause where the reverse onus applies; the accused carries a burden |
| 515(10) | the prosecutor; the accused | limit on a power | the accused | detention is justified only on the three grounds |
| 516 to 519.1 | a justice | power | the accused | adjourn and remand; direct non-publication; take evidence; vary by consent |
| 520, 521 | the accused; the prosecutor | power with limits (period, two clear days' notice) | each other; the judge | to apply to a judge for review |
| 520(8) | the accused; the prosecutor | disability | - | no further application for 30 days without leave |
| 522 | a court, judge or justice other than a superior court judge | disability | an accused charged under s 469 | may not release |
| 523 | the court, judge or justice | power | the accused | to vacate or vary on cause being shown; the earlier order continues |
| 523.1, 524 | a judge or justice | duty; power | the accused | to review conditions; to cancel; to detain in the three circumstances unless cause is shown |
| 525(1) | the person having custody of the accused | duty | the accused (claim to a hearing) | to apply to fix a date for a hearing when the trial has not commenced within 90 days |
| 525(1.1) | the accused | power | the custodian | to waive the hearing in writing, received in time |
| 527 | a judge of a superior court | power | a prisoner | to order a prisoner brought before a court; to order transfer with consent |
| 528 | a justice | duty | the accused (liability to arrest elsewhere) | to endorse the warrant on application and proof of the signature |
| 529, 529.1, 529.3, 529.4 | a judge or justice; a peace officer | power | the occupier; the accused | to authorize entry; to enter without a warrant where exigent; to enter without announcement |
| 529(2), 529.4(2), (3) | a peace officer | disability | the occupier (immunity) | may not enter unless there are reasonable grounds to believe the person is present; may not enter without announcement unless harm or loss of evidence is feared |
| 493.1, 493.2 | a peace officer, justice or judge | duty | the accused (claim) | primary consideration to release; particular attention to Aboriginal and vulnerable accused |

## Marginal readings for a lawyer (ccc20)

The readings a lawyer should confirm or overrule, most consequential first.
Each hand-written fork of the register is one line here; the 45 grant-named functions whose failed "if" answers NOTHING follow as a table (the "where/when/upon" group is in the fork register only).

- F-90-days (s 525(1), (1.1), (4)(b)): readings: (1) The day of the event is day 0, so the 90 days are days 1 to 90 and expire at the end of day 90; a trial that commences on day 90 has commenced "within 90 days". (2) The day of the event is day 1, so the period expires at the end of day 89. Taken: (1), by `Date to days` difference: at most 90 is within, more than 90 is not.
- F-30-days (s 520(8), s 521(9)): readings: (1) The day of the decision is day 0: an application on the 30th day after it is before the expiry and one on the 31st is not. (2) The day of the decision is day 1. Taken: (1), as for F-90-days.
- F-are-the-following (s 523.1(2), s 524(2), s 515(4.3)): readings: (1) "are the following" and "are" close the list: a case in none of the paragraphs is the text's own no (JUST FALSE). (2) The list is not closed because the text does not say "only": such a case is NOTHING. Taken: (1) for ss 523.1(2) and 524(2); for s 515(4.3), (1) as the keel read "are" in s 2.3(1).
- F-524-5-6.2 (s 524(5), s 524(6.2)): readings: (1) Subsection (5) is the consequence of subsection (4) and subsection (6.2) the consequence of (6.1): each applies only where the document was cancelled and its predecessor was engaged. (2) Read literally, (5) applies whenever the judge or justice "does not order that the accused be detained in custody under subsection (4)" and (6.2) whenever the judge or justice "does not make a release order under subsection (6.1)", even where (4) or (6.1) was never engaged. Taken: (1).
- F-525-1-ab (s 525(1)(a), (b)): readings: (1) Where an order or review decision of paragraph (b) exists, the 90 days run from the later of the two days it names; otherwise from the day the accused was taken before a justice (paragraph (a)). (2) The 90 days also run from paragraph (a), so that the period expires at the first of the two. Taken: (1).
- F-527-7-three-gates (s 527(7)): readings: (1) The consent gate ("if a prisoner ... consents in writing") fails: NOTHING, whatever the other two gates say; the "on application by the prosecutor" and "where the judge is satisfied" gates fail: JUST FALSE (guide rulings (c) and (b)). (2) Every gate that fails gives NOTHING. (3) Every gate that fails gives JUST FALSE. Taken: (1).
- F-493.1-with-493.11-2-c (s 493.1, s 493.11(2)(c)): readings: (1) The duty of s 493.1 takes the answer of s 493.11(2)(c) as its input, because s 493.11(2) says it applies "for the purposes of section 493.1": a justice or judge faced with a reverse-onus case is not to give primary consideration to release. (2) The two sections answer separately and the caller combines them. Taken: (1).
- F-ten-years (s 515(2.11), s 515(6)(b.2)): readings: (1) "within ten years" is a closed period whose first day is the day ten years before (that day is within). (2) The period is ten years less a day. Taken: (1).
- F-month-end (s 507.1(5)): readings: (1) Six months after the endorsement are counted by calendar month with `Date`, which rolls an impossible day forward (31 August 2026 gives 3 March 2027). (2) The last day is the last day of the sixth month (28 February 2027). Taken: (1).
- F-493.01-scope (s 493.01): readings: (1) "a reference to an indictable offence includes an offence that may be punishable on summary conviction if it is also an offence that may be prosecuted by indictment, unless the prosecutor has elected" applies to every reference to an indictable offence in Part XVI. (2) It applies to the whole Code, because it sits in Part XVI only for the Part's own references. Taken: (1), through one function `s 493.01 the reference to an indictable offence includes the offence` that every "indictable offence" test in the range calls.
- F-cause-shown-choice (s 520(7)(d), (e); s 521(8)(d), (e)): readings: (1) Where the accused (or the prosecutor, in s 521) shows cause, the text leaves the judge a choice between (d) dismiss and (e) allow: the function `must dismiss` answers NOTHING there. (2) Showing cause obliges the judge to allow the application. Taken: (1).
- F-515-9-sufficient (s 515(9)): readings: (1) A record made of the reasons in accordance with Part XVIII is sufficient; a record made another way is NOT COVERED (NOTHING). (2) A record made another way is not sufficient (JUST FALSE). Taken: (1).
- F-duty-*, F-other-*, F-unless-*, F-dutyN-*: the 167 case-by-case sites of the brief (a duty or a bar whose gate is unmet; "(other than X)"; "unless" or "except" once met): the first three kinds answer JUST FALSE on the text's own words and the other reading is NOTHING; F-dutyN answers NOTHING (the text limits the duty to a class) and the other reading is JUST FALSE; the rows are in the fork register, fourth block.
- F-may-*: a "may" whose failed "if" gate is read as the text's own "no" (JUST FALSE) rather than as outside the limit of the grant (NOTHING); the guide's own "In short" sentence and the ruling of 2026-11-12 give NOTHING; the 45 functions are:

| function | other reading |
| --- | --- |
| `s 494(2) the owner of property, or a person acting for the owner, may arrest the person without a warrant` | JUST FALSE when the "if" gate fails (F-may-494(2)) |
| `s 495.1 the peace officer may arrest the accused without a warrant to take them before a judge or justice under section 524` | JUST FALSE when the "if" gate fails (F-may-495.1) |
| `s 496 the peace officer may, without laying a charge, issue an appearance notice to attend a judicial referral hearing` | JUST FALSE when the "if" gate fails (F-may-496) |
| `s 497 the peace officer may issue an appearance notice to the person` | JUST FALSE when the "if" gate fails (F-may-497) |
| `s 499 a peace officer may release the person arrested with a warrant` | JUST FALSE when the "if" gate fails (F-may-499) |
| `s 500(3) the appearance notice may require the accused to appear for the purposes of the Identification of Criminals Act` | JUST FALSE when the "if" gate fails (F-may-500(3)) |
| `s 501(3) the undertaking may contain the condition` | JUST FALSE when the "if" gate fails (F-may-501(3)) |
| `s 501(4) the undertaking may require the accused to appear for the purposes of the Identification of Criminals Act` | JUST FALSE when the "if" gate fails (F-may-501(4)) |
| `s 502(2) the accused or the prosecutor may apply to a justice` | JUST FALSE when the "if" gate fails (F-may-502(2)) |
| `s 502.1(1) the accused may appear by audioconference or videoconference` | JUST FALSE when the "if" gate fails (F-may-502.1(1)) |
| `s 502.1(2) the witness in Canada may give evidence by audioconference or videoconference` | JUST FALSE when the "if" gate fails (F-may-502.1(2)) |
| `s 502.1(4) the participant may participate by audioconference or videoconference` | JUST FALSE when the "if" gate fails (F-may-502.1(4)) |
| `s 502.1(5) the justice may preside by audioconference or videoconference` | JUST FALSE when the "if" gate fails (F-may-502.1(5)) |
| `s 503(3)(b) the justice may take that step` | JUST FALSE when the "if" gate fails (F-may-503(3)(b)) |
| `s 504 any one may lay an information in writing and under oath before a justice` | JUST FALSE when the "if" gate fails (F-may-504) |
| `s 509(5) the summons may require the accused to appear for the purposes of the Identification of Criminals Act` | JUST FALSE when the "if" gate fails (F-may-509(5)) |
| `s 511(2.1) the judge or justice may cancel the warrant` | JUST FALSE when the "if" gate fails (F-may-511(2.1)) |
| `s 512.1 a justice may issue a warrant for the arrest of the accused for the offence` | JUST FALSE when the "if" gate fails (F-may-512.1) |
| `s 512.2 a justice may issue a warrant for the arrest of the accused for the offence` | JUST FALSE when the "if" gate fails (F-may-512.2) |
| `s 512.3 a justice may issue a warrant to take the accused before a justice under section 524` | JUST FALSE when the "if" gate fails (F-may-512.3) |
| `s 515(2.1) the judge, justice or court may name particular persons as sureties` | JUST FALSE when the "if" gate fails (F-may-515(2.1)) |
| `s 515(2.2) the justice may allow the accused to appear by videoconference or audioconference` | JUST FALSE when the "if" gate fails (F-may-515(2.2)) |
| `s 515(7) the new release order may include additional conditions described in subsections (4) to (4.2)` | JUST FALSE when the "if" gate fails (F-may-515(7)) |
| `s 515.01 the judge or justice may make an order in Form 11.1 requiring the accused to appear for the purposes of the Identification of Criminals Act` | JUST FALSE when the "if" gate fails (F-may-515.01) |
| `s 515.1(2) the judge, justice or court may name the person as a surety without a declaration` | JUST FALSE when the "if" gate fails (F-may-515.1(2)) |
| `s 517(1) the justice may make an order directing that the evidence, information, representations and reasons shall not be published` | JUST FALSE when the "if" gate fails (F-may-517(1)) |
| `s 520(1) the accused may apply to a judge for a review of the order` | JUST FALSE when the "if" gate fails (F-may-520(1)) |
| `s 520(7)(e) the judge may allow the application, vacate or vary the order and make any other order provided for in section 515` | JUST FALSE when the "if" gate fails (F-may-520(7)(e)) |
| `s 521(1) the prosecutor may apply to a judge for a review of the order` | JUST FALSE when the "if" gate fails (F-may-521(1)) |
| `s 521(8)(e) the judge may allow the application, vacate or vary the order and make any other order provided for in section 515` | JUST FALSE when the "if" gate fails (F-may-521(8)(e)) |
| `s 522(3) the judge may make a release order referred to in section 515` | JUST FALSE when the "if" gate fails (F-may-522(3)) |
| `s 523.1(3)(a) the judge or justice may take no action` | JUST FALSE when the "if" gate fails (F-may-523.1(3)(a)) |
| `s 523.1(3)(b) the judge or justice may cancel any other summons, appearance notice, undertaking or release order in respect of the accused` | JUST FALSE when the "if" gate fails (F-may-523.1(3)(b)) |
| `s 523.1(3)(b)(i) the judge or justice may make a release order under section 515` | JUST FALSE when the "if" gate fails (F-may-523.1(3)(b)(i)) |
| `s 523.1(3)(b)(ii) the judge or justice may make an order that the accused be detained in custody until the accused is dealt with according to law` | JUST FALSE when the "if" gate fails (F-may-523.1(3)(b)(ii)) |
| `s 523.1(3)(c) the judge or justice may remand the accused to custody for the purposes of the Identification of Criminals Act` | JUST FALSE when the "if" gate fails (F-may-523.1(3)(c)) |
| `s 525(3) the judge may cancel the hearing` | JUST FALSE when the "if" gate fails (F-may-525(3)) |
| `s 525(4)(a) the judge may give directions for expediting the proceedings` | JUST FALSE when the "if" gate fails (F-may-525(4)(a)) |
| `s 525(4)(b) the judge may require a further hearing under this section` | JUST FALSE when the "if" gate fails (F-may-525(4)(b)) |
| `s 527(1) the judge may order in writing that a person who is confined in a prison be brought before the court, judge, justice or provincial court judge` | JUST FALSE when the "if" gate fails (F-may-527(1)) |
| `s 527(7) the judge may order the transfer of the prisoner or other person to the custody of a peace officer named in the order for a period specified in the order` | JUST FALSE when the "if" gate fails (F-may-527(7)) |
| `s 529(1) the warrant may authorize a peace officer to enter a dwelling-house described in the warrant for the purpose of arresting or apprehending the person` | JUST FALSE when the "if" gate fails (F-may-529(1)) |
| `s 529.1 the judge or justice may issue a warrant in Form 7.1 authorizing a peace officer to enter a dwelling-house described in the warrant` | JUST FALSE when the "if" gate fails (F-may-529.1) |
| `s 529.3(1) the peace officer may enter the dwelling-house for the purpose of arresting or apprehending a person without a warrant` | JUST FALSE when the "if" gate fails (F-may-529.3(1)) |
| `s 529.4(1) the judge or justice may authorize the peace officer to enter the dwelling-house without prior announcement` | JUST FALSE when the "if" gate fails (F-may-529.4(1)) |

### Reading a result: FALSE and NOTHING (ccc20)

A function answers `JUST TRUE` (the rule applies or the permission exists), `JUST FALSE` (the text says no in its own words) or `NOTHING` (the text does not cover the case); a caller never turns NOTHING into "no".
Every JUST FALSE branch in layer 1 carries `-- FALSE-kind (the text says no in its own words): "<quote>"` and every NOTHING branch `-- NOTHING-kind (<silent|list not closed|includes|undefined term|points outside the text|limited by its own wording>)`; `work/lint.py` checks that each quoted fragment occurs in the text (run 2026-11-16: JUST FALSE branches 300, NOTHING branches 208, quoted fragments 474, 0 problems).
The rules in force are those of the brief: the rule of 2026-10-29; E1 and N2 (2026-11-04); periods, "where" and scope limits (2026-11-05); delegated definitions, defences and "until" bars (2026-11-05); case by case (2026-11-05); and the ruling of 2026-11-12 on grants (an "if" gate that fails gives NOTHING; "only if", "unless" and a flat "may not" give JUST FALSE; where/when/upon gates are listed).
In particular for this Part: a duty or a bar whose gate fails answers JUST FALSE; a bar whose subject is an authorization or order that does not exist (ss 529(2), 529.4(2), 529.4(3)) answers NOTHING (a scope limit); a section 2 term the keel can answer NOTHING for is taken as a `MAYBE BOOLEAN` input and NOTHING is carried through.
In the seat layer: JUST TRUE is yes, JUST FALSE is "the text says no", NOTHING is "not covered"; a question about a bar is titled as the bar (JUST TRUE means barred).

## Seams (ccc20)

Inputs taken from other parts or from the keel (the input is named for the section that answers it):

| input | type | used by | note |
| --- | --- | --- | --- |
| `s 469 the offence charged is one listed in section 469` | MAYBE BOOLEAN | ss 498(1), 503(1.1), 507(6), 515, 522, 523, 525 | PLAN.md seam; NOTHING is carried through |
| `s 3.01 the offence counts as one in which violence against a person was used, threatened or attempted` (two forms) | MAYBE BOOLEAN | ccc20-part16-reverse-onus.l4 | PLAN.md seam (it lists ss 515(3), (4.1), (4.3), (6)) |
| `s 553 the offence charged is an indictable offence mentioned in section 553` | MAYBE BOOLEAN | ss 495(2), 497 | FOUND BY THIS PART: not in PLAN.md; the sections name the offences listed in s 553, which is outside this range |
| `s 673 a sentence within the meaning of section 673 is imposed on the accused` | BOOLEAN | s 523 | PLAN.md asks `ss 673, 679, 680`; the fact is a plain yes or no, so BOOLEAN, not MAYBE BOOLEAN |
| `s 679`, `s 680` | not taken | s 515(6)(a)(i), (c) | PLAN.md lists `s 679 the person has been released pending determination of an appeal`; the paragraphs ask a fact about the charge ("released ... pursuant to the provisions of this Part or section 679 or 680"), taken as a BOOLEAN of the charge; ss 522(4) and 524(9) say "other than under section 680" and that review is not given here |
| `s 715.25 the person is a participant as defined in subsection 715.25(1)` | MAYBE BOOLEAN | s 502.1(4) | the definition is in Part XVII |
| `s 2 terrorism offence`, `s 2 serious offence`, `s 2 prison`, `s 2 dwelling-house` | MAYBE BOOLEAN (dwelling-house: BOOLEAN) | ss 515(6), 527(1), 529 | section 2 terms the keel answers |
| `s 2 justice` | the keel's function, called directly (`ccc-definitions.l4` is imported by ccc20-part16-taking-before-justice.l4 only) | s 503 | the person the accused is taken before must be "a justice" as section 2 says |

Seams provided by this part for others: `s 493 the maker of the order is a judge as defined in section 493` (BOOLEAN; PLAN.md: s 2 "release order"), `s 515 the interim release outcome the accused was given` (`Outcome of interim release`; PLAN.md: ss 679, 680) and `s 515 the accused is bound by a release order` (BOOLEAN; PLAN.md: s 145).

## What the text turns out to say (numbered findings)

1. Subsections 524(5) and 524(6.2) begin "If the judge or justice does not order that the accused be detained in custody under subsection (4)" and "If the judge or justice does not make a release order under subsection (6.1)": read literally each applies even where its predecessor was never engaged; read as the consequences of (4) and (6.1), which s 524(5.1) and (6.1) support (F-524-5-6.2).
2. Subsection 525(1)(b) names its own day ("the later of the day on which the accused was taken into custody under that order and the day of the decision") and is introduced by "in the case where"; paragraph (a) is the day taken before a justice under s 503 (F-525-1-ab).
3. Subsection 525(6) applies "Sections 495.1, 512.3, 517 to 519 and 524"; the range "517 to 519" does not reach s 519.1, and the test `s 525(6)` asserts NOTHING for 519.1.
4. Subsection 520(2) lets the prosecutor consent to shorter notice ("unless the prosecutor otherwise consents"); subsection 521(2) has no such exception.
5. Subsection 520(1) lists orders under s 515(2), (5), (6), (7) or (12); subsection 521(1) lists orders under s 515(1), (2), (7) or (12).
6. The public-interest circumstances of s 495(2)(d) are three (identity, evidence, prevention of repetition); those of s 498(1.1)(a) are four, adding the safety and security of a victim or witness.
7. Subsection 527(7) has three gates of three kinds: "on application by the prosecutor", "if a prisoner ... consents in writing" and "where the judge is satisfied" (F-527-7-three-gates).
8. Subsection 497 lets a peace officer issue an appearance notice only "by virtue of subsection 495(2)": the permission depends on the bar of s 495(2) having engaged.
9. Section 515(10) is a closed list ("justified only on one or more of the following grounds") of three grounds; its ground (c) is the confidence ground.
10. The text shows 17 units repealed or blank: the `appearance notice`, `officer in charge`, `promise to appear`, `recognizance`, `summons` and `undertaking` definitions and para (c) of `judge` in s 493, ss 503(2.1) to (2.3), 509(3), 510, 515(4.1)(d), 515(8), 517(3), 525(8) and 525(9).

## What the stable binary does not accept

Measured 2026-11-16 with one-line probe files (`work/probe/`) on `l4 1.6.110 (main, e51181d, 2026-11-11)` and on `1.6.109 (main, 4c887e0, 2026-11-04)`; the two builds gave the same result for every probe.
Where `references/dialects.md` of the writing-l4-rules skill (written for build 98) differs from the build in hand, the build governs.

| construct | result on 1.6.110 and 1.6.109 |
| --- | --- |
| `TYPICALLY 2` on a record field | rejected (parse error at the value) |
| `SET OF NUMBER` and `setSize` | rejected: `I could not find a definition for the identifier` |
| `` `IS INTEGER` `` | rejected: `I could not find a definition for the identifier` |
| `IMPORT hierarchy` | rejected: `I could not find a module with this name` |
| an `@nonexhaustive` line | rejected (parse error at `@`) |
| an opaque `DECLARE Applicant` followed by a `GIVEN` | rejected (parse error at the `GIVEN`) |
| `YMD 2026 10 19`, `REFUSE`, `#ASSERT REFUSED`, `@lang pt` | ACCEPTED here although dialects.md lists them as rejected on build 98; the brief nevertheless forbids `YMD` (collision with unstable's daydate), `REFUSE` and `BECAUSE`, so none is used |
| comparing a regulative rule's `DEONTIC` value in an `#ASSERT` | not possible; the four regulative rules (ss 494(3), 498(1), 503(1), 525(1)) are tested with 13 `#TRACE`s, whose outcomes are identical on both builds (checked 2026-11-16: ccc20-tests-arrest 6 traces, ccc20-tests-failure-and-delay 3, ccc20-tests-taking-before-justice 4; one ends `DEONTIC BREACHED`) |

## Seat question audit of 2026-11-12 (second pass, written 2026-11-16)

Task: read the title of every seat question against the BODY of the layer-1 function it calls, and retitle only for (1) a different limb, route or scope, (2) a premise or qualifier the function does not compute, (3) a wrong polarity or modal, (4) a different answer type.
Counts: seat questions read 36; retitled 3; read and left 33; assertions restated by this audit 10 (the assertions of the retitled questions, each carrying `-- RECONCILED 2026-11-12: was <the original assertion>; <reason>` in ccc20-cases-seat.l4); mismatches of direction or subject found: 0 (the three retitles are of limb, premise and qualifier).
A first reading of each title against its own wording found none; the second reading, of each title against the body of the function it calls, found the three below.
The new question names, written out exactly:

- `Under section 493.1, must the peace officer, justice or judge give primary consideration to my release at the earliest reasonable opportunity and on the least onerous conditions that are appropriate in the circumstances`
- `Under section 497, may a peace officer who is barred by section 495(2) from arresting me issue me an appearance notice`
- `Under section 498(1), must a peace officer release me as soon as practicable, subject to subsection 498(1.1)`

| # | question | verdict | reason |
| --- | --- | --- | --- |
| 1 | `Under section 493, am I an accused within the meaning of Part XVI` | read, left | title and body agree: JUST TRUE for the two limbs, NOTHING because the definition says "includes" |
| 2 | `Under section 493.1, must the peace officer, justice or judge give primary consideration to my release at the earliest reasonable opportunity and on the least onerous conditions that are appropriate in the circumstances` | retitled | was `Under section 493.1, must the peace officer, justice or judge give primary consideration to my release at the earliest reasonable opportunity`: the title named one limb (release at the earliest reasonable opportunity) where the function answers the whole duty, which adds "and on the least onerous conditions that are appropriate" |
| 3 | `Under section 493.11(2)(e), is the justice or judge barred from ordering that I be released` | read, left | agree: titled as the bar (JUST TRUE = barred); NOTHING for a peace officer |
| 4 | `Under section 493.2, must the peace officer, justice or judge give particular attention to my circumstances` | read, left | agree: the duty owed to the Aboriginal and the vulnerable accused; NOTHING for an accused in neither group |
| 5 | `Under section 494(1), may any one arrest me without a warrant` | read, left | agree: a permission, JUST TRUE = may; NOTHING outside the two limbs |
| 6 | `Under section 495(1), may a peace officer arrest me without a warrant` | read, left | agree: a permission; NOTHING outside the three limbs |
| 7 | `Under section 495(2), is the peace officer barred from arresting me without a warrant` | read, left | agree: titled as the bar (JUST TRUE = barred) |
| 8 | `Under section 497, may a peace officer who is barred by section 495(2) from arresting me issue me an appearance notice` | retitled | was `Under section 497, may a peace officer who does not arrest me issue me an appearance notice`: the title carried the premise "who does not arrest me", which the function does not compute: it computes the gate "by virtue of subsection 495(2)", that is, that s 495(2) bars the arrest |
| 9 | `Under section 498(1), must a peace officer release me as soon as practicable, subject to subsection 498(1.1)` | retitled | was `Under section 498(1), must a peace officer release me as soon as practicable`: the title asked the duty without its qualifier; the function answers the duty of s 498(1) "subject to subsection (1.1)", which has its own question |
| 10 | `Under section 498(1.1), must the peace officer not release me` | read, left | agree: titled "must ... not release", JUST TRUE = barred from releasing |
| 11 | `Under section 503(1), must the peace officer cause me to be taken before a justice` | read, left | agree: a duty |
| 12 | `Under section 503(1), was I taken before a justice within the time the subsection requires` | read, left | agree: a yes-or-no on compliance with paragraph (a) or (b) |
| 13 | `Under section 503(1.1), must the peace officer release me` | read, left | agree: a duty |
| 14 | `Under section 503(2), how many hours of the 24-hour period have run against me` | read, left | agree in answer type (a NUMBER of hours); the title repeats the function's own wording and the number may exceed 24 |
| 15 | `Under section 507.1(5), what is the last day for commencing proceedings to compel the issue of a summons or warrant` | read, left | agree in answer type (a DATE) |
| 16 | `Under section 515(1), must the justice make a release order without conditions` | read, left | agree: a duty (a release order without conditions) |
| 17 | `Under section 515(6), must the justice order that I be detained in custody` | read, left | agree: a duty to detain; NOTHING when the reverse onus is not known |
| 18 | `Under section 515(6)(b), am I charged with an indictable offence, other than one listed in section 469, and not ordinarily resident in Canada` | read, left | agree: the limb of the reverse onus |
| 19 | `Under section 515(10), can my detention in custody be justified on one of the three grounds` | read, left | agree: the closed list of grounds |
| 20 | `Under section 520(1), may I apply to a judge for a review of the order` | read, left | agree: a permission; JUST FALSE for the period, NOTHING for an order of another kind |
| 21 | `Under section 520(2), may my application be heard by a judge` | read, left | agree: "may be heard", JUST FALSE where the text says it shall not |
| 22 | `Under section 520(8), is a further application by me barred` | read, left | agree: titled as the bar (JUST TRUE = barred) |
| 23 | `Under section 522(1), is the court, judge or justice barred from releasing me` | read, left | agree: titled as the bar |
| 24 | `Under section 523.1(3), must the judge or justice review the conditions of my release` | read, left | agree: a duty to review |
| 25 | `Under section 523.1(5), is the laying of an information or the preferring of an indictment against me for the failure barred` | read, left | agree: titled as the bar |
| 26 | `Under section 524(3), must the judge or justice cancel my summons, appearance notice, undertaking or release order` | read, left | agree: a duty to cancel |
| 27 | `Under section 524(4), must the judge or justice order that I be detained in custody` | read, left | agree: a duty to detain unless cause is shown |
| 28 | `Under section 525(1), must the person having my custody apply to a judge to fix a date for a hearing` | read, left | agree: a duty of the custodian |
| 29 | `Under section 525(1), from which day are the 90 days counted` | read, left | agree in answer type (a DATE) |
| 30 | `Under section 525(1.1), is the person having my custody not required to make the application` | read, left | agree: "not required", JUST TRUE = excused |
| 31 | `Under section 527(1), may a judge order that I, confined in a prison, be brought before the court` | read, left | agree: a permission; the title's "I, confined in a prison" is the prison gate the function computes |
| 32 | `Under section 528(1), must a justice authorize my arrest within the justice's jurisdiction by endorsing the warrant` | read, left | agree: a duty of the justice |
| 33 | `Under section 529(1), may a warrant authorize a peace officer to enter a dwelling-house to arrest or apprehend me` | read, left | agree: a permission |
| 34 | `Under section 529(2), is the peace officer barred from entering the dwelling-house` | read, left | agree: titled as the bar; NOTHING when no authorization exists |
| 35 | `Under section 529.3(1), may a peace officer enter the dwelling-house without a warrant to arrest or apprehend me` | read, left | agree: a permission |
| 36 | `Under section 529.4(3), is the peace officer barred from entering the dwelling-house without prior announcement` | read, left | agree: titled as the bar |

### Name-test sweep of 2026-11-12

Scope: the 94 top-level functions of layer 1 whose name contains "may", "permitted", "power", "entitled" or "authorized" (script `work/sweep.py`).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 0 | 4 | 22 | 0 |

**Flipped to NOTHING (0).**
No grant-named function answered JUST FALSE for a failed "if" gate: the part was written under the ruling of 2026-11-12 and every such function already answers NOTHING (45 functions with an "if" gate, each with one row in the fork register and in the marginal readings).

**Kept JUST FALSE, gate closed by the text (4):**
- `s 501(3) the undertaking may contain the condition`: "which shall not be more than $500" and "whose value does not exceed $500"
- `s 507(6) the justice may authorize the release of the accused under section 499 by endorsing the warrant in Form 29`: "may, unless the offence is one listed in section 469"
- `s 520(2) the application may be heard by a judge`: "shall not, unless the prosecutor otherwise consents, be heard ... unless the accused has given"
- `s 521(2) the application may be heard by a judge`: "shall not be heard by a judge unless the prosecutor has given"

Also JUST FALSE and left alone, because they are a duty or a bar whose name contains "may" (4): `s 523.1(1)(a) the justice must order that the accused appear before a judge of the superior court of criminal jurisdiction so that the judge may hear the matter`; `s 524(1)(a) the justice must order that the accused be taken before a judge of the superior court of criminal jurisdiction so that the judge may hear the matter`; `s 493.1 the decision-maker must take into account the grounds referred to in subsection 498(1.1) or 515(10), as the case may be`; `s 529.4(2) the peace officer is barred from entering the dwelling-house without prior announcement despite being authorized to do so`.

**Listed: "may" with where/when/upon or an equivalent gate (22), answer the guide's JUST FALSE:**
- `s 503(3)(b) the justice may take that step`
- `s 507(8) a justice may issue a summons or a warrant for the arrest of the accused to compel attendance`
- `s 511(2.1) the judge or justice may cancel the warrant`
- `s 512(1) the justice may issue a summons or warrant notwithstanding the prior step`
- `s 512(2) a justice may issue a warrant for the arrest of the accused`
- `s 515(4) the justice may direct the accused to comply with the condition`
- `s 515.01 the judge or justice may make an order in Form 11.1 requiring the accused to appear for the purposes of the Identification of Criminals Act`
- `s 516 the justice may adjourn the proceedings and remand the accused to custody in prison by warrant in Form 19`
- `s 518(2) the justice may make any order provided for in this Part for the release of the accused until sentence`
- `s 520(1) the accused may apply to a judge for a review of the order`
- `s 520(3) the judge may order in writing the person having custody of the accused to bring the accused before the court`
- `s 520(4) the judge may adjourn the proceedings`
- `s 520(5) the judge may issue a warrant for the arrest of the accused`
- `s 521(1) the prosecutor may apply to a judge for a review of the order`
- `s 521(3) the judge may order in writing the person having custody of the accused to bring the accused before the court`
- `s 521(5) the judge may issue a warrant for the arrest of the accused`
- `s 522(6) the judge may apply the provisions of this Part respecting judicial interim release to the other offence`
- `s 523(2) the court, judge or justice may vacate or vary the order previously made and make any other order for the detention or release of the accused`
- `s 525(4)(a) the judge may give directions for expediting the proceedings`
- `s 525(4)(b) the judge may require a further hearing under this section`
- `s 527(2) a provincial court judge has the same powers for the purposes of subsection (1) or (7) as a judge has under that subsection`
- `s 527(7) the judge may order the transfer of the prisoner or other person to the custody of a peace officer named in the order for a period specified in the order`

Nine of these (ss 503(3)(b)(ii), 511(2.1), 515(4), 515.01, 516, 520(4), 523(2), 525(4)(a) and 525(4)(b)) had answered NOTHING for their "when", "where" or "on" gate before this sweep; the sweep set them to the guide's own answer, JUST FALSE, because the rule of 2026-11-12 (point 3) leaves the answer "as the guide's rulings give it" and lists them; the "if" gates of ss 511(2.1), 515.01 and 525(4) still answer NOTHING.
Two gate words are outside the instruction's list and were left with the answers they had: "in the absence of consent" (s 502(2); read like the "with consent" gates of ss 502(1), 503(3.1), 519.1 and 523(2)(c), so NOTHING, listed in the "if" table as F-may-502(2)) and "during the course of any proceedings under section 515" (s 516; read as the scope limit of s 518(1), so NOTHING; the "on application" gate of s 516 is the one listed).
9 assertions were restated in place with `-- RECONCILED 2026-11-12: was <the original assertion>; <reason>`: ccc20-tests-failure-and-delay.l4 (2), ccc20-tests-interim-release.l4 (3), ccc20-tests-process.l4 (1), ccc20-tests-review.l4 (2), ccc20-tests-taking-before-justice.l4 (1).

**Layer-1 answers this sweep changed: 9 functions went from NOTHING to JUST FALSE** (the nine named above, each for a "when", "where", "on" or "on application" gate, to the guide's own answer), **and none went the other way**; the four-count table has no column for them, so "flipped to NOTHING: 0" does not mean that no answer changed.

**Listed: "entitled" (0).** No function name contains "entitled".

**"It is lawful ..." functions.** No function is named "it is lawful ..."; the three whose names say "is deemed to be acting lawfully" are `s 495(3)`, `s 498(3)` and `s 503(5)`, each named with its section label, so each is scoped and keeps JUST FALSE.
It is lawful, scoped: 3. It is lawful, unscoped and retitled: 0.

## What check.sh prints

Run on 2026-11-16 as `L4=<scratchpad>/bin/l4-main-110 L4_MAIN=<scratchpad>/bin/l4-main-109 ./check.sh` (stable 1.6.110 and the second stable build 1.6.109).
Baseline on resume, before any edit this session: TOTAL 20 modules, 976 satisfied, 0 failed, 0 refused, the same on main.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc20-cases-seat.l4                            0       121       0        0         0 |      0       121       0        0  same
ccc20-part16-arrest.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-failure-and-delay.l4              0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-interim-release.l4                0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-interpretation.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-notices.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-principles.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-prisoners-and-entry.l4            0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-process.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-reverse-onus.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-review.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc20-part16-taking-before-justice.l4          0         0       0        0         0 |      0         0       0        0  same
ccc20-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc20-tests-arrest.l4                          0        85       0        0         0 |      0        85       0        0  same
ccc20-tests-failure-and-delay.l4               0       224       0        0         0 |      0       224       0        0  same
ccc20-tests-fixtures.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc20-tests-interim-release.l4                 0       218       0        0         0 |      0       218       0        0  same
ccc20-tests-interpretation.l4                  0        45       0        0         0 |      0        45       0        0  same
ccc20-tests-notices.l4                         0        85       0        0         0 |      0        85       0        0  same
ccc20-tests-principles.l4                      0        52       0        0         0 |      0        52       0        0  same
ccc20-tests-prisoners-and-entry.l4             0       117       0        0         0 |      0       117       0        0  same
ccc20-tests-process.l4                         0       160       0        0         0 |      0       160       0        0  same
ccc20-tests-reverse-onus.l4                    0       205       0        0         0 |      0       205       0        0  same
ccc20-tests-review.l4                          0       140       0        0         0 |      0       140       0        0  same
ccc20-tests-taking-before-justice.l4           0        52       0        0         0 |      0        52       0        0  same
TOTAL (28 modules)                             0      1504       0        0           |      0      1504       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` and `--strict` over every `ccc20-*.l4`: 700 src: lines, 214 runs, 367 locators, 0 problems (both modes).
The #TRACE outcomes of the two builds are identical (see above).
