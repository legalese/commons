# NEEDS-CORE (coa26)

Constructors and types that `coa-core.l4` lacks and that coa26 declared under its own prefix instead (the lead may hoist them at the merge).

| wanted in the core | used by | what coa26 declared instead |
| --- | --- | --- |
| `Party`: `Recognised supervisory body`, `Recognised qualifying body`, `Independent Supervisor`, `Auditor General`, `Approved third country competent authority` | ss 1223A, 1224A, 1225-1225G, 1227-1237 (the duties and powers of these parties; their duties are decision functions only, since `Auditor` is the only one of them the core has a constructor for) | nothing: the duties of these parties are asked as decision functions, and the regulative rules use the core `Auditor` (an Auditor General holding office is a statutory auditor) |
| `Fine limit`: a constructor for "one-tenth of the greater of an amount and the amount corresponding to a level on the standard scale, for each day" (2 uses in this Part: ss 1213(7) and 1215(6)) | ss 1213(7), 1215(6) | `s 1213(7) fine for continuing` IS ONE OF `s 1213(7) a fine without a stated limit`, `s 1213(7) a fine not exceeding a sum for each day on which the act or the failure continues` HAS `s 1213(7) pounds for each day` |
| a court type with `the High Court` and `the Court of Session` ("the court" means the High Court or, in Scotland, the Court of Session: ss 1225C(3), 1225F(10), 1236(3)) | those three subsections | `s 1225C(3) court`, `s 1225F(10) court`, `s 1236(3) court` (three identical two-constructor types, one per subsection, so that no name is shared) |
| `Mode of conviction`: "on summary conviction in England and Wales or Northern Ireland" as one mode (s 1224B(2)(b)(ii)) | s 1224B(2) | the core's separate modes for England and Wales and for Northern Ireland, with the same answer for each |
