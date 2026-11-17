# NEEDS-CORE (ccc23: Part XX.1, ss 672.1 to 672.95)

What layer 1 of this part wanted from the core and did not find. Nothing here blocks the part: each item is asked as a plain boolean fact in the function that needs it, and the lead can hoist the type later and wrap the inputs.

1. Constructors for `Party` (the core's type for who takes part in a proceeding). The core already has `the accused`, `the offender`, `the victim`, `the prosecutor`, `a Review Board`, `a justice`, `a peace officer`, `a court of appeal`, `the Attorney General` and `a witness`, which this part's regulative rules use (`PARTY a Review Board`). The core lacks the people this Part names and no other part is likely to spell differently:
   - `an appellant` and `a respondent` (672.72 to 672.78: "the appellant must give notice of appeal within fifteen days", "the appellant must provide the court of appeal and the respondent with a certified transcript");
   - `the person in charge of a hospital` (672.56, 672.81(1.4), (2), 672.1(1) "hospital");
   - `a medical practitioner` (672.16(2), 672.2, 672.51(8));
   - `the Minister` of 672.68(1) (the Minister of Public Safety and Emergency Preparedness, or the minister of a province, in the dual status offender provisions);
   - `the chairperson of a Review Board` (672.43, 672.48(3), 672.85: layer 1 answers who is one through the seam `s 672.1(1) the issuer is the chairperson of a Review Board`).
   Layer 1 asks each of these as a plain boolean fact in the function that needs it.
2. A core record for "the days between two dates counted in months" is not needed: `add months` and `Day` cover it, and 672.81(1) is tested at the boundary on both sides. Noted only because 672.81 is the one place this part measures calendar months.

Nothing else was missing. The keel's `Provision of the Code` record (section number and subsection) was enough for the twelve sections of 672.81(1.3)(b) and s 163.1 of 672.501(2).
