# Source licence

The terms the quoted source text carries are recorded once, at the subject level, in `../../SOURCE-LICENSE.md` (in a deposit, the subject's own `SOURCE-LICENSE.md`); this file does not repeat them.

In short, and only to point at that file: the text of the State Pension Credit Act 2002 comes from legislation.gov.uk, is Crown copyright, and is available under the Open Government Licence v3.0, with the attribution line that file gives.

What this encoding adds to that record:

- Every module quotes the text line by line (`-- src:N | ...`, copied by `srcrefs.py quote` from `../../registers/source-bundle/ukpga-2002-16.txt`), so the encoding reproduces the text and carries those terms with it.
- The quoted file is a plain-text rendering made by a converter script from the legislation.gov.uk XML. It is not the official text, and nothing in this encoding is verified against the official text. The converter's own caveats, and the one outstanding effect it lists, are in `NOTES.md` and in `inputs/ukpga-2002-16.meta.json`.
- The licence of the encoding itself (the L4 code and the notes) is Apache-2.0, like the rest of Commons.
