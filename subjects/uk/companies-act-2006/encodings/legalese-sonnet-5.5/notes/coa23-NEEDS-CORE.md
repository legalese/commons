# NEEDS-CORE (coa23)

Constructors and types the core lacks, which the coa23 modules declare under their own prefix (`coa23-nouns.l4`); the lead may hoist them into `coa-core.l4` at the merge.

| wanted in the core | declared now as | sections that need it |
| --- | --- | --- |
| `Party`: `Any person` | `s 1065 any person` (type `s 1065 person dealing with the registrar`) | ss 1065, 1085(1), 1086(1): "Any person may ..." |
| `Party`: `Individual who delivers a document to the registrar` | `s 1067A an individual who delivers a document to the registrar` (same type) | ss 1067A, 1067B |
| a registrar-for-a-place type | `s 1060 registrar of companies` with `s 1060(1)(a)`, `(b)`, `(c)` | ss 1060(3), 1060(4) |
| `Penalty`: a constructor for "imprisonment for a term not exceeding the general limit in a magistrates' court" | not needed: `s 1092B(3) the penalty for the offence` takes the limit as an input in months and builds the core's `Period OF n, Months` | s 1092B(3) |

No type or constructor of the core was missing for the rest of the range: `Place of registration`, `Form of document`, `Period`, `Unit of time`, `Penalty`, `Mode of conviction`, `Fine limit`, `Party` (Registrar, Company, Director) and `Action of a party` are used as they are.
