# ireland/

Ireland legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the electronic Irish Statute Book (eISB), Office of the Attorney General; Law Reform Commission Revised Acts (revisedacts.lawreform.ie); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. When the subjects were laid out, no statute text had been deposited and nothing was encoded; the last section says what has been added since.

**Licence category: open.** Statute text may be deposited and quoted in an encoding, subject to the attribution above.

## Topics with no legislation here

- **Passenger compensation**: Governed by directly applicable EU law: Regulation (EC) 261/2004 for air, plus the EU rail, bus/coach and maritime passenger rights Regulations. Ireland has no principal Act. Enforcement is set by S.I.s (e.g. S.I. No. 274 of 2005), with the Commission for Aviation Regulation (set up by the Aviation Regulation Act, 2001, No. 1 of 2001, whose eISB title was verified) and the NTA as national enforcement bodies. That Act only creates the regulator, so it is not listed.
- **Utility billing**: Only partly covered. The Electricity Regulation Act 1999 is listed as a weak fit. Billing rules for electricity, gas and telecoms come from CRU/ComReg decisions and EU-derived S.I.s. Domestic water charges were abolished (Water Services Act 2017).

## Interpretation Act 2005

`interpretation-act-2005/` holds the Interpretation Act 2005 (No. 23 of 2005) as enacted, from the electronic Irish Statute Book.
The eISB legislation directory lists no textual amendment, but this is the enacted text and not a revised consolidation.
The text is under the Oireachtas (Open Data) PSI Licence, which incorporates CC BY 4.0; each file that quotes the text carries the Oireachtas copyright notice.
Only the English text is deposited.
The first encoding is `interpretation-act-2005/encodings/legalese-sonnet-5.5/`, written by one Sonnet 5.5 agent against the `unstable` compiler.
It encodes the rules for counting periods, commencement, repeal, service and the defined time words, and refuses where the Act has no rule.
No one has read the encoding against the official text.
