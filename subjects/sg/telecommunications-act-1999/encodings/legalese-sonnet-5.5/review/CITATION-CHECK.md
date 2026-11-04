# Citation check of the two encodings

Status: done on 2026-11-04 by the independent reviewer, in the copy VIEW, by three methods.
- **Mechanically, every quotation:** `srcrefs.py check --strict` was run over every module that quotes a source, plus an exact comparison of every quote line with its source line.
- **By hand, the decisive chain:** I read 263 `@ref`s on the chain (listed in part 2) against the source lines they point at.
- **By hand, a random sample:** I read 64 `@ref`s drawn by a seeded script (part 3), 62 of them not already read in part 2, the same way.
This was done after the encoders' preliminary answers had reached my context (REQUESTS.md R2); a citation check does not depend on the answer, so I did it anyway.
The modules named `sgta-tv-*` and `sgba-tv-*` were withheld from my copy, so nothing here covers them.

## 0. Result in one paragraph

All 15,530 quote lines in the 97 quoting modules are verbatim: each is an exact substring of the source line it names, after squeezing whitespace, with no case-folding, no Unicode normalisation and no punctuation collapse.
`srcrefs.py check --strict` reports 0 problems on every one of them.
By hand I found **17 locator-level mismatches, of 8 kinds**, and 2 coverage gaps, listed in part 4.
None is in a quotation's words, and none changes an answer to the question: every one is a range that starts or stops a line or two away from the provision its label names, a range that runs on into the next heading, a row of a table cut short, or a wrong word in a label.
Fifteen of the 17 are on the decisive chain; the random sample of 64 had 1 (about 1.6%), and 1 more turned up when I followed a decisive-chain mismatch into a second module.

## 1. Mechanical checks

### 1.1 `srcrefs.py check --strict`, every quoting module

The two encodings' `srcrefs.py` are the same file (466 lines each; `diff -q` printed nothing).
The TA encoding runs it through `srcrefs-all.sh`, which pairs each module with its deposit; the BA encoding names each instrument module's deposit in a `-- Deposit:` header and runs the Act modules against `BA1994.txt`.
I wrote my own driver, `review-out/tools/run_srcrefs.sh`, which reproduces `srcrefs-all.sh`'s pairing for the TA and reads the `-- Deposit:` header for the BA, and ran `python3 -I srcrefs.py check --strict RAW MODULE` once per module.

| encoding | modules with quote lines | quote lines | runs | locators | problems |
| --- | --- | --- | --- | --- | --- |
| TA (`sgta-*`) | 52 | 11,415 | 740 | 767 | 0 |
| BA Act modules (`sgba-p*`, `sgba-sched`, `sgba-versions`) | 16 | 2,896 | 443 | 443 | 0 |
| BA instrument modules (`sgba-i-*`) | 29 | 1,219 | 175 | 175 | 0 |
| **total** | **97** | **15,530** | **1,358** | **1,385** | **0** |

The TA row matches `encoding.json` `checks.srcrefs` exactly ("52 modules, 11415 quote lines, 740 runs, 767 locators, 0 problems").
The BA Act row matches BA `encoding.json` `checks.srcrefs` exactly ("2896 src: lines, 443 runs, 443 locators, 0 problems").
The BA instrument modules match the per-module lines in BA NOTES.md for each one I compared: `sgba-i-rg1.l4` 416/40/40, `sgba-i-s333-2004.l4` 170/16/16, `sgba-i-tvro-regs.l4` 31/24/24.
The three modules that quote the deposits added to my copy on 2026-11-04 pass: `sgba-i-s212-1999.l4` 11/1/1, `sgba-i-s354-2001.l4` 51/7/7 and `sgba-i-s496-2001.l4` 29/3/3.

### 1.2 Exact comparison, every quote line

srcrefs' rule R1 forgives case, Unicode form and punctuation, so I also compared each quote line exactly: whitespace squeezed to single spaces, nothing else changed (`review-out/tools/exact_quotes.py`).
Result: `quote lines 15530; exact substring after whitespace squeeze 15530; equal only after NFC 0; differ otherwise 0`.
So no quotation changes a quote mark, a hyphen, a dash, a digit or a letter of its source.

### 1.3 What neither check sees

srcrefs' own docstring says what it does not check: "that a locator names the right provision (a wrong but covered range passes), that the `@ref` sits above the right declaration, that a run quotes every raw line inside its locator, or that the encoding is right."
Parts 2 and 3 are the hand check of the first three.

## 2. The decisive chain, by hand

Method: for each `@ref`, I printed the label and the source lines at both ends of each locator (`review-out/tools/refshow.py`), and read the label against the provision those lines hold.
Where an end looked wrong, I read the source lines on either side.
**All 263 `@ref`s with locators in these modules were read:**
- **TA modules:** `sgta-s2-definitions` (18), `sgta-s3-5-privilege-licensing` (7), `sgta-part6-offences` (19), `sgta-part8-penalties` (6), `sgta-part9-general` (4), `sgta-ta-versions` (5, one of which carries 23 locators), `sgta-i-n1-exemption` (9), `sgta-i-rg3-class` (2), `sgta-i-rg5-radio` (8), `sgta-i-rg5-definitions` (1), `sgta-i-rg6-dealers` (7), `sgta-i-rg6-definitions` (5).
- **BA modules:** `sgba-p5-apparatus` (10), `sgba-sched` (5), `sgba-versions` (13), `sgba-i-s549-2012` (1), `sgba-i-s548-2012` (6), `sgba-i-s333-2004` (16), `sgba-i-tvro-regs` (24), `sgba-i-composition` (1), `sgba-i-s354-2001` (7), `sgba-i-s212-1999` (1), `sgba-i-rg1` (40).
- **Selected `@ref`s from larger modules:** `sgta-i-rg5-licences` regs 19(2)-22 (4), `sgta-i-rg6-licensing` regs 20, 21, 23, 24 and the Fifth Schedule (5), `sgba-p1-defs` "broadcasting apparatus", "broadcasting apparatus licence/licensee", "broadcasting licence", "broadcasting service", "free-to-air", "licensable" and "subscription broadcasting service" (8), `sgba-p11-offences` ss 47, 56 and 57 (14), `sgba-p12-misc` ss 64-66 (17).

The provisions the brief names, and what I found:

| provision | locator(s) | result |
| --- | --- | --- |
| TA s 2 "equipment", current | `TA1999.txt:325-329` | correct |
| TA s 2 "equipment", 2000 Ed. | `TA1999.20001230.txt:226-227` | correct: "used or intended to be used for telecommunication purposes;" |
| TA s 2 "equipment" amended by Act 19/2011 | `TA1999.ACT19-2011.txt:49-54`, Bill 20/2011 explanatory statement `TA1999.BILL20-2011.txt:2571-2574` | correct; label says "clause 2(b)" of the Act (M8) |
| TA s 2 "radio-communication" | `TA1999.txt:450-451` | correct |
| TA s 2 "broadcasting apparatus" and "broadcasting service" | `TA1999.txt:275-276` | correct |
| TA s 2 "broadcasting apparatus" inserted by Act 10/2005 | `TA1999.ACT10-2005.txt:42-47` | correct; label says "clause 2(a)" (M8) |
| TA s 5(1)-(2), (8), (10) | `TA1999.txt:607-618`, `705-706`, `713-715` | correct |
| TA s 33(1), 2000 Ed. | `TA1999.20001230.txt:1203-1206` | correct |
| TA ss 34-36, 2000 Ed. | none | **not quoted in any module in my copy** (G1) |
| TA s 33 amended by Act 30/2016 | `TA1999.ACT30-2016.txt:1063-1068` | correct; label says "clause 18" (M8) |
| TA s 53(1), (2), (5), (6) | `TA1999.txt:4831-4837`, `4844-4849`, `4864-4868`, `4870-4873` | correct |
| TA s 54(1)(a), (1)(b) with its exception, (2) | `TA1999.txt:4894-4897`, `4899-4902`, `4904-4905` | correct |
| TA s 55(1)-(4) | `TA1999.txt:4911-4916`, `4918-4920`, `4922-4924`, `4926-4929` | correct |
| TA s 56 | `TA1999.txt:4935-4947` | correct |
| TA s 65, 2000 Ed., and Act 10/2005 s 28 | `TA1999.20001230.txt:1916-1920`, `TA1999.ACT10-2005.txt:961-964` | correct; label says "clause 28" (M8) |
| TA s 85 | `TA1999.txt:5941-5950` | correct (line 5950 is the former-number note "[65") |
| TA s 72, 2000 Ed., and Act 10/2005 s 30 | `TA1999.20001230.txt:2030-2035`, `TA1999.ACT10-2005.txt:1188-1190` | correct; label says "clause 30" (M8) |
| TA s 95, s 96 | `TA1999.txt:6987-6992`, `7000-7001` | correct |
| BA s 2(1) "broadcasting apparatus", 2003, 2012 and 2024 texts | `BA1994.20030731.txt:198-200`, `BA1994.20120831.txt:191-193`, `BA1994.txt:277-279` | correct |
| BA s 20(1)-(4), three texts | `BA1994.20030731.txt:701-720`, `BA1994.20120831.txt:684-704`, `BA1994.txt:1425-1452` | correct |
| BA s 47 | `BA1994.txt:3676-3681` | correct |
| BA First Schedule, three texts | `BA1994.20030731.txt:2134-2154`, `BA1994.20120831.txt:2163-2178`, `BA1994.txt:4347-4357` | correct |
| S 549/2012 | `BA1994-S549-2012.txt:3-37` | correct |
| S 548/2012 regs 1, 2(1), 2(2)(a)-(c), 2(3) | `BA1994-S548-2012.txt:3-31`, `33-36`, `37-41`, `42-48`, `49-53`, `54-57` | correct |
| S 333/2004 paras 1-23 | 16 locators in `BA1994-S333-2004.txt:3-249` | correct |
| Rg 1 (TV and Radio Licensing Regs, 2004 Ed.) | 40 locators in `BA1994-RG1.txt:32-664` | 4 kinds of mismatch, 8 `@ref`s (M1-M4) |
| TVRO Regs, S 354/2001 | 24 locators in `BA1994-RG3.txt`, 7 in `BA1994-S354-2001.txt` | correct |
| BA Composition Regs reg 2 | `BA1994-RG2.txt:5` | correct |
| N 1 para 2 (2002 Ed. and as amended by S 726/2014) | `TA1999-N1.txt:24-31`, `TA1999-N1-S726-2014.txt:23-43` | correct |
| N 1 Schedule (2002 Ed., S 525/2001) | `TA1999-N1.txt:42-156`, `TA1999-N1-S525-2001.txt:21-158` | item 16 cut short (M6, M7) |
| Rg 5 reg 2 "station", reg 19, reg 65 (2002 Ed., S 263/2006, S 461/2009), reg 65A, reg 78 | `TA1999-RG5.txt:273-275`, `555-566`, `1094-1108`, `1260-1265`, and the amending texts | correct |
| Rg 3 (Class Licences) reg 3, 2002 Ed. and S 685/2011 | `TA1999-RG3.txt:78-81`, `TA1999-RG3-S685-2011.txt:63-67` | correct |
| Rg 6 (Dealers) reg 2, reg 20, reg 22 (2004 Ed. and S 478/2005), Fifth Schedule (2004 Ed. and S 251/2013 item 3) | `TA1999-RG6.txt:75-98`, `349-365`, `381-388`, `581-601`; `TA1999-RG6-S478-2005.txt:86-98`, `145-155`; `TA1999-RG6-S251-2013.txt:18-20`, `161-168` | correct |

## 3. The random sample

Script: `review-out/tools/sample_refs.py`, sha256 `aeed44487ef9c17dbd91df7fad9d9afdddf5fcdfc62567338c467b7d9060e5e4`.
Pool: every `@ref` carrying a `src:` locator in the 97 quoting modules, minus the 23 modules read in full in part 2 and the 39 `@ref`s read in part 2 from `sgba-p1-defs`, `sgba-p11-offences` and `sgba-p12-misc`; that is 1,126 `@ref`s in 78 modules.
The exclusion list missed the 9 `@ref`s read in part 2 from `sgta-i-rg5-licences` and `sgta-i-rg6-licensing`, and 2 of them were drawn (items [20] and [62]), so **62 of the 64 are further to part 2**.
Draw: `random.Random(20261104).sample(sorted(pool), 64)`; **seed 20261104**.
Output, with the source lines on both sides of each end: `review-out/tools/sample-20261104.txt`.
The 64 fall in 38 modules, 23 TA and 15 BA.
TA: ss 2, 5, 6-8, 9-10, 11-14 and Parts 3, 4, 5A, 5B-5C, 6, 8 and 9 of the Act; the N 1 bands, Rg 1 (ships), Rg 5 (four modules), Rg 6, and the Internal Wiring and Composition Regulations.
BA: Parts 1, 2, 4, 6-7, 8-9, 10, 10A and 11 of the Act; the class licence N 1, S 330/2013, S 674/2016, the digital display panels class licence and the Online Codes of Practice rules.

Result: 63 correct; 1 mismatch, item [21], `sgta-i-rg5-licences.l4:322` (M5).
Three items I checked further and found correct:
- item [18], S 179/2011, comes into operation "on 1 April 2011" (`TA1999-N1-S179-2011.txt:14-17`);
- item [32], Rg 5 First Schedule Part III, ends at item 3, as the source does (`TA1999-RG5.txt:1420-1422`);
- item [58], BA s 2(1) "access", whose "means" limb is quoted in the block above (`sgba-p1-defs.l4:27-30`, `src:257-259`).

## 4. Every mismatch found

| # | where | what the locator or label says | what the source shows |
| --- | --- | --- | --- |
| M1 | `sgba-i-rg1.l4:74` | `@ref reg 2(1) "vessel" (src:162-166)` | Line 162 is "vessel"; lines 163-166 are the first four lines of reg 2(2), "(2) Unless the context otherwise requires, the words ''licence'' and ''licensee'' shall, … be construed respectively as meaning a licence or the person to whom is granted a licence of the type specified against", which stops mid-sentence; reg 2(2)'s list (a)-(d) (`BA1994-RG1.txt:167-174`) is quoted nowhere in the module. |
| M2 | `sgba-i-rg1.l4:93` and `:111` | `@ref reg 4(1) and (2) (src:187-197)`, then `@ref reg 4(3) (src:201-205)` | Reg 4(2) runs from line 194 to line 202: its closing words, "supporting it, shall not exceed such height as may be approved by the chief executive officer of the Civil Aviation Authority of Singapore." (`BA1994-RG1.txt:201-202`), are quoted under the reg 4(3) `@ref`, while the reg 4(2) rule above uses them ("does not exceed the height approved by the chief executive officer"). Lines 198-200 are a page header, rightly skipped. |
| M3 | `sgba-i-rg1.l4:456` | `@ref reg 15 (RevEd 2004) (src:355-368)` | Line 368 is "Broadcasting system not to include TVRO system", the heading of reg 16. |
| M4 | `sgba-i-rg1.l4:569`, `:658`, `:852`, `:886` | reg 22 `(src:416-438)`, reg 26 `(src:469-478)`, reg 35 `(src:575-585)`, reg 37 `(src:596-609)` | Each range ends on the next Part's heading, "PART IV / BROADCAST SOUND RECEIVERS" (`437-438`), "PART V / BROADCAST TELEVISION RECEIVERS" (`477-478`), "BROADCAST SOUND RECEIVERS AND / BROADCAST TELEVISION RECEIVERS / IN HOTELS AND HOSPITALS" (`583-585`), "PART VII / MISCELLANEOUS" (`608-609`), which is quoted at the foot of the preceding regulation's block (`sgba-i-rg1.l4:567-568`, `656-657`, `850-851`, `884-885`). |
| M5 | `sgta-i-rg5-licences.l4:322` (random item [21]) | `@ref Rg 5 reg 30 (src:TA1999-RG5:741-743)` | Line 743 is "Compliance with Radio Regulations, Authority's requirements, etc.", the heading of reg 31 (`TA1999-RG5.txt:744` "31. A Ship Station licensee shall —"). |
| M6 | `sgta-i-n1-exemption.l4:96` | `@ref N 1 Schedule, 2002 Revised Edition (src:TA1999-N1:42-156)` | The range stops in the middle of item 16, "16. Short Range Radar 76.00 – 77.00 GHz 5W EIRP for vehicle in" (`TA1999-N1.txt:156`); the rest of the row, "System motion 250 mW EIRP for / stationary vehicle" (`157-158`), is not quoted in this module (it is quoted in `sgta-i-n1-bands.l4:112-114`). |
| M7 | `sgta-i-n1-exemption.l4:301` and `sgta-i-n1-bands.l4:340` | S 525/2001 Schedule, ending `src:TA1999-N1-S525-2001:158` | Line 158 ends "5W EIRP for"; the rest of item 16, "vehicle in motion / 250 mW EIRP for / stationary vehicle" (`TA1999-N1-S525-2001.txt:159-161`), is quoted in neither module. |
| M8 | `sgta-ta-versions.l4` (5 labels) | "Act 10 of 2005 clause 2(a)", "clause 28", "clause 30"; "Act 19 of 2011 clause 2(b)"; "Act 30 of 2016 clause 18" | These are sections of enacted Acts, not clauses of Bills; the Act texts print them as numbered sections, e.g. "28. Section 65 of the Telecommunications Act is amended by inserting," (`TA1999.ACT10-2005.txt:961`). The locators are right. |

Count: M1 1, M2 2, M3 1, M4 4, M5 1, M6 1, M7 2, M8 5, which is **17 `@ref`s in 8 kinds**.
Of those, 15 are on the decisive chain (M1-M4, M6, M7's first `@ref`, and M8) and 2 are outside it (M5, and M7's second `@ref`, in `sgta-i-n1-bands.l4`).

Coverage gaps (not mismatches, since nothing wrong is cited):
- **G1.** No module in my copy quotes the 2000 Edition's ss 34, 35 or 36 (`TA1999.20001230.txt:1244-1287`), the possession and operation offences as numbered and worded in that Edition.
  I read them against the current ss 54-55 (`TA1999.txt:4894-4929`).
  The words of s 34(1)(b) and its exception ("possess any radio-communication equipment, except and in accordance with a licence granted under section 5 or any regulations made under this Act") are the same.
  So are s 35(1), (3) and (4), apart from drafting form ("shall be deemed" against "is deemed"; "It shall be a defence" against "It is a defence").
  So no answer turns on G1; it matters only to a reader who wants the text in force at the conduct date.
  The `sgta-tv-*` modules, withheld from me, may quote them.
- **G2.** The encoder's own `srcrefs-all.sh` never checks the `sgta-tv-*` modules: its Act run takes `ls sgta-*.l4 | grep -vE '^sgta-(tests|tv|i-|nouns|ta-vintage)'`, and no other line of it names them.
  The modules that state the TA's answer to the question are therefore outside the quotation check its `encoding.json` reports.
  I could not run it on them myself, because they were withheld from my copy.

## 5. Files

Everything needed to repeat the mechanical checks is in `review-out/tools/`; run each from the root of the review copy.
- `run_srcrefs.sh VIEW` drives `srcrefs.py check --strict` over every quoting module; its output is `srcrefs-run.tsv` (one row per module: module, raw file, exit status, summary line).
- `exact_quotes.py refmap.tsv` is the exact comparison of part 1.2.
- `refshow.py RAW MODULE…` prints an `@ref` beside its source lines (part 2).
- `sample_refs.py 20261104 64 refmap.tsv` draws the sample of part 3; `refmap.tsv` maps each module to its source file, with paths relative to the copy's root, and `sample-20261104.txt` is the draw as I read it.
- `zz-review-pairs-ba.l4` and `zz-review-pairs-ta.l4` are the probes of `REVIEW.md` §3(f); each runs only when copied into its encoding's folder, because stable l4 cannot IMPORT across folders.
The hand reading itself is recorded in parts 2 to 4, not in a file a script can re-run.
