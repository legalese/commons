# NEEDS-CORE.md -- part ccc31: what the core (`ccc-core.l4`) lacks for Forms 24 to 54

The keel's files are read-only here, so none of these was added; each was met by the workaround named, and the lead may hoist the constructor into the core at the merge (the workaround is then a one-word change in the part's module).

## `Party` (the regulative actor)

- `the sheriff` (Forms 27 and 34: the warrant and the writ are addressed "To the sheriff of (territorial division)"). Workaround: `a peace officer` (a sheriff is a peace officer by paragraph (a) of the definition in s 2, line 140). Used in `form 27 the duties of the sheriff and the keeper` and `form 34 the duties of the sheriff`.
- `the keeper, administrator or warden of a prison, hospital or other place` (Forms 49 and 50: "the keeper (administrator, warden) of the (prison, hospital or other appropriate place)"). Workaround: `the keeper of a prison`. Used in `form 49 the duties of the peace officers and the keeper` and `form 50 the duty of the keeper`.
- `the addressee of an order to disclose income tax information` (Form 47, "To A.B., of , (office or occupation)"). Workaround: `a public officer`. Used in `form 47 the duty of the addressee`.
- `the chairperson of a Review Board` (the signatory of Forms 48.1, 49 and 50). Not used in a rule (the signature lines are wording).
- `a fingerprint examiner` (Forms 44 and 45, "a fingerprint examiner designated as such for the purposes of section 667"). Not used (the Forms are certificates: inert).
- `a person who collects information at a registration centre` and `the Canadian Forces Provost Marshal` (Forms 52 and 53, paragraph 5; Forms 52 to 54, paragraph 3). Not used (the functions take "the person is subject to the order" as the fact).

## A helper for counting a period

- `forms 24-54 the first day after a period that begins on a day` and `forms 24-54 the day falls within a period that begins on a day`, in `ccc31-forms-periods.l4`, count a `Length of time` from a day (fork F16 of NOTES.md). Other parts that count a term of years, months and days from a date will need the same; the lead may hoist it into the core (or a library module) under a name without the `forms 24-54` prefix.

## Nothing else

No type or constructor beyond these was needed: the `Provision of the Code` record carried the section tests of Forms 29, 29.1 and 32, and `Length of time` carried every period.
