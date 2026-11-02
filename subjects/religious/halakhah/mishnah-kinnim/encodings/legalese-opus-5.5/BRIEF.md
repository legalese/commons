# Encoding brief: Mishnah Kinnim, whole, in L4 (main)

This brief was written down at the end of the work, from the requests it was built to; no separate brief was issued before it began.

## The request

Meng Wong, 2026-11-02, verbatim: "please run a solo encoding of the Kinnim (https://en.wikipedia.org/wiki/Kinnim), but first please review https://www.jstor.org/stable/40914641 and also consider any writings on the subject by Prof Moshe Koppel, and allow the encodings to be informed by all those sources".

Later the same day, through the `higayon` session, Meng added two instructions (checked by this session in that session's transcript):

- if Koppel's own text on *Seder Kinnim* cannot be found, substitute the gloss at `~/src/higayon/says-gemini.txt`, and build an encoding that can be extracted to the formal systems and backends for the treatments the gloss describes;
- brief this session on the higayon session's findings and have it proceed accordingly.

The higayon session asked, in addition, that any claim supportable only from the gloss be flagged to Meng, and set three constraints: the Higayon PDFs from the Asif library are for personal study and are never copied into this repository (cite journal, volume, article and pages); the gloss is labelled secondary and unverified, and where it disagrees with the Mishnah or the commentaries, they win; and its Tel Aviv relay was for asif.co.il only.

## What the row is

- **Solo**: one agent, one context, no subagents, no independent test pass.
- **Whole**: every unit of the three chapters has a row in the coverage table, with one disposition each (`encoded`, `inert` for aggadah, or a fork in the register).
- **Two layers**: the law as the text gives it (`kn-nouns`, `kn-ch1`, `kn-ch2`, `kn-majority`, `kn-ch3`), and a seat layer (`kn-seat`, `kn-cases-seat`) for the person who brought the birds; no seat for the priest.
- **Target**: the `main` compiler, checked with `check.sh` against a main build.
- **Sources**: the Hebrew text deposited from he.wikisource, with Bartenura, Tiferet Yisrael and Maimonides as aids; Reiss (the JSTOR article), Gewirtz, Beller and what could be found of Koppel's, cited by page and not deposited.
- **Formal shape**: the gloss's four treatments (partition, bounds, the worst case, deduction not probability) are stated as solver obligations in `prove/`, run with `l4 prove`, and tried on the Lean backend.

The results, the forks and what was not obtained are in `NOTES.md`.
