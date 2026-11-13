# NEEDS-CORE (coa29: Schedules 2 to 9)

Things the shared core `coa-core.l4` would need for this part's modules to use it instead of declaring their own copies.
None of them blocks anything: each module declares its own types under its own prefix and compiles and passes on 1.6.110 and 1.6.109.
The core is read-only for this part, so these are requests to the lead, to be decided at the merge.

1. **`Form of document` has two constructors; the Schedules need four.**
   `coa-core.l4:160` declares `hard copy form` and `electronic form` (from s 1168(2) and (3)).
   Schedule 4 para 8 speaks of a communication "otherwise than in hard copy form or electronic form", Schedule 5 para 15 of one "otherwise than in hard copy or electronic form or by means of a website", and Schedule 5 para 8 of a document "made available on a website".
   Own copies: `sch 4 form of the document or information` (hard copy form, electronic form, neither hard copy form nor electronic form; `coa29-sch4.l4`) and `sch 5 form of the document or information` (hard copy form, electronic form, made available on a website, none of those forms; `coa29-sch5.l4`).
   Wanted in the core: two more constructors (`made available on a website`, `neither of those forms`); the two copies would then be deleted.
2. **There is no core type for how a document is sent.**
   Section 1168(3)(a) names "electronic means (for example, by e-mail or fax)" and Schedules 4 and 5 add "by hand", "by post" and (Schedule 5) "handed to the intended recipient".
   Own copies: `sch 4 means of sending or supplying` (by hand, by post, by electronic means, by some other means) and `sch 5 means of sending or supplying` (handed to the intended recipient, by hand to an address, by post, by electronic means, by some other means).
   Wanted in the core: one type with these constructors, if another part needs it.
3. **The core's `Period` has a length but no first and last day.**
   `coa-core.l4:176` is `Period` (number of units, unit).
   Schedule 5 para 14(1) needs "the period throughout which" a document must be on a website, by its first and last day (the period specified by another provision, or the 28 days beginning with the notification date).
   Own copy: the record `sch 5 period of availability` (first day of the period, last day of the period; `coa29-sch5.l4`).
   Wanted in the core: a `Dated period` (first day, last day), if other parts count periods by their days.
4. **Nothing is needed for the penalties of Schedule 3.**
   Schedule 3 is inert here (fork F12).
   If it is encoded later, the core's `Penalty` (`coa-core.l4:210`) and `Fine limit` (`coa-core.l4:200`) fit its text: `on conviction on indictment`, `on summary conviction in England and Wales`, `on summary conviction in Scotland` and `on summary conviction in Northern Ireland` (two constructors), the fraction of the statutory maximum for the daily default fine.
   The pounds the statutory maximum stands for would be an input, as the core says.
