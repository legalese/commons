# subjects/religious/

**Proposed, not ruled (2026-11-02).** `docs/directory-conventions.md` has not been amended, and no ruling covers this tree.
It exists because its first subject, `halakhah/mishnah-kinnim`, fits neither of the ruled grammars.

- §2 of the conventions files **enacted law by the authority that enacted it**, under an ISO 3166 code.
  The Mishnah was enacted by no state; filing it under `il/` would misstate it as Israeli law, which it is not.
- §3 files **contract forms by genre**, and `doctrine/` (itself a proposal) files **judge-made doctrine compared across authorities**.
  Neither describes a body of religious law.

The grammar proposed here is `subjects/religious/<tradition>/<leaf>/`, with the tradition named in its own term for its law (`halakhah` for Jewish law; `canon-law` or `fiqh` would be peers).
The leaf is a single work or tractate, as a statute is under §2.
Its `subject.json` records the authority in prose, the extent, and whether any of it is practised today.

If the grammar is not adopted, the cheapest alternative is a top-level leaf such as `subjects/halakhah-mishnah-kinnim/`, which loses nothing but grouping; a reviewer who rules otherwise should move the subject and say why in the conventions document.
