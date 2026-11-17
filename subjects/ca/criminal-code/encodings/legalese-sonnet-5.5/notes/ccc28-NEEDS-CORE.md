# NEEDS-CORE -- ccc28 (Criminal Code (Canada), lines 16296-16683)

Each item below is something the core (`ccc-core.l4`) does not declare and the range needed.
Each is declared in this part's own modules under the section label, as the brief requires, so that the lead can hoist it or leave it.
Checked against `ccc-core.l4` on 2026-11-17: it has no constructor for a sheriff, a person remanded, an applicant, a subject of habeas corpus or any writ, and no comparison of two `Length of time` values.

1. **Parties missing from `Party`** (a regulative rule needs a `Party` type, and each of these acts or bears a duty in the text):
   - the person to whom the offender is remanded for assessment (ss 752.1(2) and 753.01(2): "shall file a report"): declared as `s 752.1(2) party` with the constructor `s 752.1(2) the person to whom the offender is remanded`;
   - the applicant for an order reducing or terminating long-term supervision (s 753.2(4): "must give notice ... to the Attorney General"): `s 753.2(4) party`, `s 753.2(4) the applicant`;
   - the sheriff to whom a writ of fieri facias is delivered (s 772(1): "shall execute the writ"; also named in ss 766(3) and 773): `s 772 party`, `s 772 the sheriff to whom the writ is delivered`;
   - the person who is the subject of a writ of habeas corpus (s 774.1: "must appear in court in person"): `s 774.1 party`, `s 774.1 the person who is the subject of a writ of habeas corpus`.
2. **The extraordinary writs** (s 774 and s 784): a type with `certiorari`, `habeas corpus`, `mandamus`, `procedendo` and `prohibition`.
   Declared as `s 774 writ`, with a sixth constructor `s 774 another writ` for a case outside the five.
3. **A comparison of two `Length of time` values** (ss 752, 753.1(3), 755(2), 777(2)): the core declares the type and its constants but no "at least".
   Written as `s 752 the length of time is at least` in `ccc28-part24-s752.l4` and written again as `s 777(2) the length of time is at least` in `ccc28-part26-extraordinary-remedies.l4`, because every module of this part imports the core only.
4. **A `one year` constant** (`Length of time OF 1, 0, 0, FALSE`): the core has `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years` and `fourteen years` and no `one year`; this part writes the record inline where it needs a year.
