#!/usr/bin/env python3
"""coverage.py -- the coverage table of the CRTPA 2001 encoding, built from the text.

usage:  python3 -I coverage.py <CRTPA2001.txt> <folder holding the crtpa-*.l4 files> [--md]

What it does
  1. Reads the raw text and enumerates the units it finds BY ITS OWN SCAN (sections, subsections, paragraphs,
     defined terms, table rows): the "text units counted".
  2. Holds the table ROWS (below): one per unit, with the lines it covers, a disposition and the rules that encode it.
  3. Checks (a) every non-blank line of the text falls in at least one row (page furniture and amendment marks fall in
     automatic furniture rows, and nothing else may); (b) every unit the scan found is claimed by some row, and every
     row's claimed unit was found by the scan; (c) every rule named in a row is defined in the folder.
  4. Prints the counts per disposition, and with --md the table in Markdown.
Exit status is 1 if any check fails."""
import re, sys, os, glob, collections

TEXT, DIR = sys.argv[1], sys.argv[2]
MD = "--md" in sys.argv
lines = open(TEXT, encoding="utf-8").read().split("\n")
N = len(lines)

# ----------------------------------------------------------------------------------------------- the scan
FURN = [r"^\s*31\.12\.2021\s*$", r"^\s*Contracts \(Rights of Third\s*$", r"^\s*Parties\) Act 2001\s*$", r"^\s*\d*\s*Parties\) Act 2001\s*(2020 Ed\.)?\s*$",
        r"^\s*2020 Ed\.\s*(Parties\) Act 2001)?\s*\d*\s*$", r"^\s*\d+\s*$", r"^\s*[ivx]+\s*$", r"^\s*\[\d+/\d+\]\s*$", r"^\s*Contracts \(Rights of Third\s*\d*\s*$",
        r"^\s*\d+\s+Parties\) Act 2001\s+2020 Ed\.\s*$"]
def furniture(s):
    return any(re.match(p, s) for p in FURN)

scan = collections.Counter()   # unit key -> occurrences
sec = sub = None
for i, s in enumerate(lines, 1):
    if furniture(s) or not s.strip():
        continue
    m = re.match(r"^\s*(\d+)\.—\((\d+)\)", s) or re.match(r"^\s*(\d+)\.\s", s)
    if m and 1 <= int(m.group(1)) <= 9 and 30 <= i < 394:
        sec = int(m.group(1)); sub = None
        scan[f"s{sec}"] += 1
        if m.lastindex and m.lastindex >= 2:
            sub = int(m.group(2)); scan[f"s{sec}({sub})"] += 1
        continue
    if i >= 394:
        break
    m = re.match(r"^\s*\((\d+)\)\s", s)
    if m and sec:
        sub = int(m.group(1)); scan[f"s{sec}({sub})"] += 1
        continue
    m = re.match(r"^\s*\(([a-c])\)\s", s)
    if m and sec:
        scan[f"s{sec}({sub})({m.group(1)})" if sub else f"s{sec}({m.group(1)})"] += 1
# sections 5 and 6 carry paragraphs (a), (b) without a subsection number: key them s6(a), s6(b) (done above with sub None)
body = re.sub(r"\s+", " ", " ".join(l for l in lines[:393] if not furniture(l)))
for t in re.findall(r"“([^”]+)”", body):
    scan["term:" + t.replace("’", "'")] += 1
for t in re.findall(r"\(called in this (?:Act|section) (?:a|the) ([^)]+)\)", body):
    scan["term:" + t] += 1
# the back matter: legislative history items, abbreviations, comparative table rows
for i, s in enumerate(lines, 1):
    if 394 <= i <= N and re.match(r"^\d\. (Act \d+ of \d+|2002 Revised Edition)", s):
        scan[f"hist:{s.split()[0]}"] += 1
    ma = re.match(r"^(C\.P\.|G\.N\. No\. S \(N\.S\.\)|G\.N\. No\. S|G\.N\. Sp\. No\. S|G\.N\. No\.|L\.A\.|L\.N\.|M\. Act|M\. Ordinance|Parl\.|S\.S\.G\.G\. \(E\) No\.|S\.S\.G\.G\. No\.)(?=\s)", s)
    if 456 < i < 484 and ma:
        scan["abbr:" + ma.group(1)] += 1
    if 491 < i < 499 and re.match(r"^\s*(7—)?\(\d\)\s+(7—)?\(?\d", s):
        scan["cmp:" + re.sub(r"\s+", " ", s.strip())] += 1

# ----------------------------------------------------------------------------------------------- the rows
# (id, first line, last line, provision, what, disposition, rules, keys)
# disposition: encoded | inert1 | inert2 | inert3 | fork:<label> | repealed
R = []
def row(id_, a, b, prov, what, disp, rules=(), keys=()):
    R.append(dict(id=id_, a=a, b=b, prov=prov, what=what, disp=disp, rules=list(rules), keys=list(keys)))

S1 = "crtpa-s1-application"
row("T01", 1, 18, "front matter", "title page, edition statement, publisher", "inert1")
row("T02", 19, 29, "arrangement of sections", "table of contents (headings of ss 1 to 9)", "inert1")
row("T03", 31, 32, "long title", "\"An Act to make provision for the enforcement of contractual terms by third parties.\"", "inert1")
row("T04", 34, 34, "commencement date", "\"[1 January 2002]\", the Act's own commencement", "inert2")
row("S01", 36, 36, "s 1 heading", "Short title and application", "inert1", keys=["s1"])
row("S01-1", 37, 39, "s 1(1)", "short title", "inert2", keys=["s1(1)"])
row("S01-2", 41, 43, "s 1(2)", "the Act does not apply to a contract entered into before the end of the 6 months from 1 January 2002", "fork:G1,G2",
    ["s 1(2) the last day of the period of 6 months from 1 January 2002, as the Interpretation Act counts it",
     "s 1(2) the contract was entered into before the end of the period of 6 months from 1 January 2002",
     "s 1(2) the restriction on the application of this Act applies to the contract",
     "s 1(2) this Act applies in relation to the contract"], ["s1(2)"])
row("S01-3", 45, 46, "s 1(3)", "the restriction does not apply to a contract which (a) and (b)", "encoded",
    ["s 1(3) the restriction in subsection (2) does not apply in relation to the contract"], ["s1(3)"])
row("S01-3a", 48, 48, "s 1(3)(a)", "entered into on or after 1 January 2002", "encoded", ["s 1(3)(a) the contract is entered into on or after 1 January 2002"], ["s1(3)(a)"])
row("S01-3b", 50, 50, "s 1(3)(b)", "expressly provides for the application of this Act", "encoded", ["s 1(3)(b) the contract expressly provides for the application of this Act"], ["s1(3)(b)"])

row("S02", 59, 59, "s 2 heading", "Right of third party to enforce contractual term", "inert1", keys=["s2"])
row("S02-1", 61, 63, "s 2(1)", "a person who is not a party may, in the third party's own right, enforce a term if (a) or (b); \"Subject to the provisions of this Act\"", "encoded",
    ["s 2(1) the third party may in the third party's own right enforce the term of the contract", "ss 1, 2 and 7 taken together the third party may enforce the term of the contract"], ["s2(1)"])
row("D01", 62, 62, "s 2(1) \"third party\"", "defined term: a person who is not a party to a contract", "encoded", ["s 2(1) the person is a third party"], ["term:third party"])
row("S02-1a", 65, 65, "s 2(1)(a)", "the contract expressly provides that the third party may", "encoded", ["s 2(1)(a) the contract expressly provides that the third party may enforce the term"], ["s2(1)(a)"])
row("S02-1b", 67, 68, "s 2(1)(b)", "subject to (2), the term purports to confer a benefit on the third party", "encoded (M1)", ["s 2(1)(b) the term purports to confer a benefit on the third party and subsection (2) does not take it out"], ["s2(1)(b)"])
row("S02-2", 70, 72, "s 2(2)", "(1)(b) does not apply if the parties did not intend the term to be enforceable", "encoded (M2)", ["s 2(2) subsection (1)(b) does not apply to the term"], ["s2(2)"])
row("S02-3a", 74, 75, "s 2(3) (first limb)", "the third party must be expressly identified by name, as a member of a class or as answering a particular description", "fork:QB",
    ["s 2(3) the third party is expressly identified in the contract by name, as a member of a class or as answering a particular description"], ["s2(3)"])
row("S02-3b", 76, 76, "s 2(3) (second limb)", "but need not be in existence when the contract is entered into", "encoded", ["s 2(3) the third party must be in existence when the contract is entered into"])
row("S02-4", 78, 80, "s 2(4)", "no right to enforce otherwise than subject to and in accordance with any other relevant terms", "encoded",
    ["s 2(4) section 2 confers a right on the third party to enforce the term otherwise than subject to and in accordance with the other relevant terms of the contract"], ["s2(4)"])
row("S02-5a", 82, 85, "s 2(5) (remedies)", "any remedy that would have been available in an action for breach of contract is available to the third party", "encoded",
    ["s 2(5) the remedy is available to the third party"], ["s2(5)"])
row("S02-5b", 86, 87, "s 2(5) (parenthesis)", "the rules relating to damages, injunctions, specific performance and other remedy apply accordingly", "encoded",
    ["s 2(5) the rules relating to damages, injunctions, specific performance and other remedy apply to the third party's remedy accordingly"])
row("S02-5c", 87, 89, "s 2(5) (volunteer)", "such remedy must not be refused on the ground that the third party is a volunteer", "encoded",
    ["s 2(5) the remedy may be refused on the ground that, as against the promisor, the third party is a volunteer"])
row("S02-6", 91, 94, "s 2(6)", "where a term excludes or limits liability, enforcing means availing of the exclusion or limitation", "encoded",
    ["s 2(6) references in this Act to the third party enforcing the term are to be construed as references to availing of the exclusion or limitation", "s 2(6) what a reference to the third party enforcing the term is construed as"], ["s2(6)"])
row("S02-7", 96, 97, "s 2(7)", "in relation to a term enforceable by a third party: promisee and promisor", "encoded", ["s 2(7) the party is the promisee", "s 2(7) the party is the promisor"], ["s2(7)"])
row("D02", 99, 100, "s 2(7) \"promisee\"", "defined term: the party by whom the term is enforceable against the promisor", "encoded", ["s 2(7) the party is the promisee"], ["term:promisee"])
row("D03", 102, 103, "s 2(7) \"promisor\"", "defined term: the party against whom the term is enforceable by the third party", "encoded", ["s 2(7) the party is the promisor"], ["term:promisor"])

row("S03", 108, 108, "s 3 heading", "Variation and rescission of contract", "inert1", keys=["s3"])
row("S03-1", 110, 115, "s 3(1)", "the parties may not, by agreement, rescind or vary so as to extinguish or alter the third party's entitlement without consent if (a), (b) or (c)", "encoded (M5)",
    ["s 3(1) the parties to the contract may not rescind or vary the contract without the third party's consent", "s 3(1) one of the circumstances in (a), (b) and (c) exists", "s 3(1) the parties to the contract SHANT rescind or vary the contract without the third party's consent"], ["s3(1)"])
row("S03-1a", 117, 118, "s 3(1)(a)", "the third party has communicated assent to the term to the promisor", "encoded", ["s 3(1)(a) the third party has communicated the third party's assent to the term to the promisor"], ["s3(1)(a)"])
row("S03-1b", 120, 122, "s 3(1)(b)", "the promisor is aware that the third party has relied on the term (knowledge of the precise terms no condition)", "encoded",
    ["s 3(1)(b) the promisor is aware that the third party has relied on the term", "s 3(1)(b) and (c) knowledge of the precise terms of the term is a condition"], ["s3(1)(b)"])
row("S03-1c", 124, 127, "s 3(1)(c)", "the promisor can reasonably be expected to have foreseen reliance, and the third party has in fact relied", "encoded",
    ["s 3(1)(c) the promisor can reasonably be expected to have foreseen that the third party would rely on the term and the third party has in fact relied on it"], ["s3(1)(c)"])
row("S03-2", 129, 129, "s 3(2)", "the assent mentioned in subsection (1)(a)", "encoded", ["s 3(2)(a) the assent may be by this form"], ["s3(2)"])
row("S03-2a", 131, 131, "s 3(2)(a)", "may be by words or conduct", "encoded", ["s 3(2)(a) the assent may be by this form"], ["s3(2)(a)"])
row("S03-2b", 133, 135, "s 3(2)(b)", "if sent by post or other means, is not regarded as communicated until received (an \"until\" bar, ruling (d))", "encoded (M6)",
    ["s 3(2)(b) the assent cannot yet be regarded as communicated to the promisor", "s 3(2)(b) the assent has been communicated to the promisor"], ["s3(2)(b)"])
row("S03-3", 137, 138, "s 3(3)", "subsection (1) is subject to any express term of the contract under which (a) or (b)", "fork:M3",
    ["s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account"], ["s3(3)"])
row("S03-3a", 140, 141, "s 3(3)(a)", "the parties may by agreement rescind or vary without the third party's consent", "fork:M3",
    ["s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account"], ["s3(3)(a)"])
row("S03-3b", 143, 145, "s 3(3)(b)", "the consent is required in circumstances specified in the contract instead of those in (1)(a), (b), (c)", "encoded",
    ["s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account"], ["s3(3)(b)"])
row("S03-4", 147, 150, "s 3(4)", "where consent is required under (1) or (3), the court or tribunal may, on the parties' application, dispense with it if satisfied that (a) or (b)", "encoded (M5, M7)",
    ["s 3(4) the court or arbitral tribunal may dispense with the third party's consent", "s 3(4) the court or arbitral tribunal MAY dispense with the third party's consent"], ["s3(4)"])
row("S03-4a", 152, 153, "s 3(4)(a)", "the consent cannot be obtained because the third party's whereabouts cannot reasonably be ascertained", "encoded", ["s 3(4) the court or arbitral tribunal may dispense with the third party's consent"], ["s3(4)(a)"])
row("S03-4b", 160, 161, "s 3(4)(b)", "the third party is mentally incapable of giving consent", "encoded", ["s 3(4) the court or arbitral tribunal may dispense with the third party's consent"], ["s3(4)(b)"])
row("S03-5", 163, 167, "s 3(5)", "the court or tribunal may dispense with a consent required under (1)(c) if satisfied reliance cannot reasonably be ascertained", "encoded (M5, M7)",
    ["s 3(5) the court or arbitral tribunal may dispense with a consent that may be required under subsection (1)(c)"], ["s3(5)"])
row("S03-6", 169, 171, "s 3(6)", "on dispensing with consent the court or tribunal may impose such conditions as it thinks fit, including compensation", "encoded (M5)",
    ["s 3(6) the court or arbitral tribunal may impose such conditions as it thinks fit", "s 3(6) the court or arbitral tribunal may impose a condition requiring the payment of compensation to the third party"], ["s3(6)"])
row("S03-7", 173, 175, "s 3(7)", "the jurisdiction is exercisable by both the General Division of the High Court and a District Court", "encoded",
    ["s 3(7) the jurisdiction conferred on the court by subsections (4), (5) and (6) is exercisable by this body"], ["s3(7)"])

row("S04", 179, 179, "s 4 heading", "Defences, etc., available to promisor", "inert1", keys=["s4"])
row("S04-1", 181, 183, "s 4(1)", "subsections (2) to (5) apply where proceedings are brought by a third party in reliance on section 2", "encoded", ["s 4(1) subsections (2) to (5) apply"], ["s4(1)"])
row("S04-2", 185, 186, "s 4(2)", "the promisor has available, by way of defence or set-off, any matter that (a) and (b)", "encoded (M8)",
    ["s 4(2) the matter is available to the promisor by way of defence or set-off", "s 4(2), (3) and (4)(a) taken together the matter is available to the promisor by way of defence or set-off"], ["s4(2)"])
row("S04-2a", 188, 189, "s 4(2)(a)", "arises from or in connection with the contract and is relevant to the term", "encoded (M8)", ["s 4(2) the matter is available to the promisor by way of defence or set-off"], ["s4(2)(a)"])
row("S04-2b", 191, 193, "s 4(2)(b)", "would have been available if the proceedings had been brought by the promisee", "encoded (M8)", ["s 4(2) the matter is available to the promisor by way of defence or set-off"], ["s4(2)(b)"])
row("S04-3", 195, 196, "s 4(3)", "the promisor also has available, by way of defence or set-off, any matter if (a) and (b)", "encoded (M5)",
    ["s 4(3) the matter is available to the promisor by way of defence or set-off because an express term provides for it"], ["s4(3)"])
row("S04-3a", 198, 200, "s 4(3)(a)", "an express term of the contract provides for it to be available in proceedings brought by the third party", "encoded", ["s 4(3) the matter is available to the promisor by way of defence or set-off because an express term provides for it"], ["s4(3)(a)"])
row("S04-3b", 202, 204, "s 4(3)(b)", "it would have been available if the proceedings had been brought by the promisee", "encoded", ["s 4(3) the matter is available to the promisor by way of defence or set-off because an express term provides for it"], ["s4(3)(b)"])
row("S04-4", 209, 209, "s 4(4)", "the promisor also has available (a) by way of defence or set-off and (b) by way of counterclaim", "encoded",
    ["s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party", "s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party"], ["s4(4)"])
row("S04-4a", 211, 211, "s 4(4)(a)", "by way of defence or set-off any matter", "encoded (M8)", ["s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party"], ["s4(4)(a)"])
row("S04-4b", 213, 214, "s 4(4)(b)", "by way of counterclaim any matter not arising from the contract", "encoded (M8)", ["s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party"], ["s4(4)(b)"])
row("S04-4c", 216, 218, "s 4(4) (tail)", "that would have been available against the third party if the third party had been a party to the contract", "encoded",
    ["s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party", "s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party"])
row("S04-5", 220, 222, "s 4(5)", "subsections (2) and (4) are subject to any express term as to the matters that are not to be available", "fork:M3",
    ["s 4(5) subsections (2) and (4) are subject to an express term of the contract that takes the matter away"], ["s4(5)"])
row("S04-6", 224, 230, "s 4(6)", "a third party sued may not enforce a term in reliance on section 2 if the third party could not have done so as a party", "encoded (M5)",
    ["s 4(6) the third party may not enforce the term in proceedings brought against the third party", "s 4(6) the third party SHANT enforce the term in proceedings brought against the third party"], ["s4(6)"])

row("S05", 232, 232, "s 5 heading", "Enforcement of contract by promisee", "inert1")
row("S05-0", 234, 235, "s 5", "section 2 does not affect any right of the promisee to enforce any term", "encoded", ["s 5 section 2 affects a right of the promisee to enforce a term of the contract"], ["s5"])
row("S06", 237, 237, "s 6 heading", "Protection of promisor from double liability", "inert1")
row("S06-0", 239, 241, "s 6 (lead-in)", "where under section 2 a term is enforceable by a third party and the promisee has recovered a sum in respect of (a) or (b)", "encoded",
    ["s 6 the court or arbitral tribunal must reduce any award to the third party"], ["s6"])
row("S06-a", 243, 243, "s 6(a)", "the third party's loss in respect of the term", "encoded", ["s 6(a) the promisee has recovered from the promisor a sum in respect of the third party's loss in respect of the term"], ["s6(a)"])
row("S06-b", 245, 246, "s 6(b)", "the expense to the promisee of making good to the third party the default of the promisor", "encoded", ["s 6(b) the promisee has recovered from the promisor a sum in respect of the expense to the promisee of making good to the third party the default of the promisor"], ["s6(b)"])
row("S06-t", 248, 251, "s 6 (tail)", "in any proceedings brought in reliance on that section by the third party the court or tribunal must reduce any award to such extent as it thinks appropriate", "encoded",
    ["s 6 the award to the third party after the reduction", "s 6 the court or arbitral tribunal MUST reduce any award to the third party"])

row("S07", 258, 258, "s 7 heading", "Exceptions", "inert1", keys=["s7"])
row("S07-1", 260, 262, "s 7(1)", "no right in the case of a contract on a bill of exchange, promissory note or other negotiable instrument", "encoded", ["s 7(1) section 2 confers a right on the third party in the case of the contract"], ["s7(1)"])
row("S07-2", 264, 266, "s 7(2)", "no right in the case of any contract binding on a company and its members under section 39 of the Companies Act 1967", "encoded", ["s 7(2) section 2 confers a right on the third party in the case of the contract"], ["s7(2)"])
row("S07-3", 268, 271, "s 7(3)", "no right in the case of a registration document of an LLP or an LLP agreement", "encoded", ["s 7(3) section 2 confers a right on the third party in the case of the contract"], ["s7(3)"])
row("S07-4", 275, 276, "s 7(4)", "no right to enforce a term of a contract of employment against an employee", "encoded", ["s 7(4) section 2 confers a right on the third party to enforce a term of the contract of employment against an employee"], ["s7(4)"])
row("S07-5", 278, 279, "s 7(5)", "section 2 confers no right in the case of (a) or (b), except that a third party may avail of an exclusion or limitation of liability", "fork:QA",
    ["s 7(5) section 2 confers a right on the third party in the case of the contract", "s 7(5) the third party may in reliance on section 2 avail of an exclusion or limitation of liability in the contract"], ["s7(5)"])
row("S07-5a", 281, 281, "s 7(5)(a)", "a contract for the carriage of goods by sea", "encoded", ["s 7(5)(a) the contract is a contract for the carriage of goods by sea"], ["s7(5)(a)"])
row("S07-5b", 283, 285, "s 7(5)(b)", "a contract for the carriage of goods by rail or road, or of cargo by air, subject to the rules of the appropriate international transport convention", "encoded",
    ["s 7(5)(b) the contract is a contract for the carriage of goods by rail or road, or for the carriage of cargo by air, which is subject to the rules of the appropriate international transport convention"], ["s7(5)(b)"])
row("S07-5c", 287, 288, "s 7(5) (exception)", "except that a third party may in reliance on that section avail the third party of an exclusion or limitation of liability in such a contract", "fork:QA",
    ["s 7(5) the third party may in reliance on section 2 avail of an exclusion or limitation of liability in the contract", "s 7(5) section 2 confers a right on the third party in the case of the contract"])
row("S07-6", 290, 290, "s 7(6)", "in subsection (5), the two definitions", "encoded", ["s 7(6) the Convention is the appropriate international transport convention for the contract", "s 7(6) the contract is a contract for the carriage of goods by sea"], ["s7(6)"])
row("D04", 292, 292, "s 7(6) \"appropriate international transport convention\"", "defined term: means (a) air, (b) rail, (c) road", "encoded", ["s 7(6) the Convention is the appropriate international transport convention for the contract"], ["term:appropriate international transport convention"])
row("S07-6a", 294, 297, "s 7(6) \"appropriate ...\" (a)", "air: the Convention with the force of law under section 3 of the Carriage by Air Act 1988", "encoded", ["s 7(6) the Convention is the appropriate international transport convention for the contract"], ["s7(6)(a)"])
row("S07-6b", 299, 302, "s 7(6) \"appropriate ...\" (b)", "rail: the Convention with the force of law under the written law the Minister may by order prescribe", "encoded", ["s 7(6) the Convention is the appropriate international transport convention for the contract"], ["s7(6)(b)"])
row("S07-6c", 307, 310, "s 7(6) \"appropriate ...\" (c)", "road: the Convention with the force of law under the written law the Minister may by order prescribe", "encoded", ["s 7(6) the Convention is the appropriate international transport convention for the contract"], ["s7(6)(c)"])
row("D05", 312, 313, "s 7(6) \"contract for the carriage of goods by sea\"", "defined term: means a contract of carriage (a) or (b)", "encoded", ["s 7(6) the contract is a contract for the carriage of goods by sea"], ["term:contract for the carriage of goods by sea"])
row("S07-6d", 315, 316, "s 7(6) \"contract ... by sea\" (a)", "contained in or evidenced by a bill of lading or sea waybill", "encoded", ["s 7(6) the contract is a contract for the carriage of goods by sea"], ["s7(6)(a)"])
row("S07-6e", 318, 320, "s 7(6) \"contract ... by sea\" (b)", "an undertaking contained in a ship's delivery order is given under or for its purposes", "encoded", ["s 7(6) the contract is a contract for the carriage of goods by sea"], ["s7(6)(b)"])
row("S07-7", 324, 326, "s 7(7)", "\"bill of lading\", \"sea waybill\" and \"ship's delivery order\" have the meanings given by the Bills of Lading Act 1992", "encoded", ["s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name"], ["s7(7)"])
row("D06", 324, 326, "s 7(7) \"bill of lading\"", "defined term (by reference to the Bills of Lading Act 1992)", "encoded", ["s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name"], ["term:bill of lading"])
row("D07", 324, 326, "s 7(7) \"sea waybill\"", "defined term (by reference to the Bills of Lading Act 1992)", "encoded", ["s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name"], ["term:sea waybill"])
row("D08", 324, 326, "s 7(7) \"ship's delivery order\"", "defined term (by reference to the Bills of Lading Act 1992)", "encoded", ["s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name"], ["term:ship's delivery order"])

row("S08", 330, 330, "s 8 heading", "Supplementary provisions relating to third party", "inert1", keys=["s8"])
row("S08-1", 332, 333, "s 8(1)", "section 2 does not affect any right or remedy of a third party that exists apart from this Act", "encoded", ["s 8(1) section 2 affects a right or remedy of the third party that exists or is available apart from this Act"], ["s8(1)"])
row("S08-2", 335, 339, "s 8(2)", "section 2(2) of the Unfair Contract Terms Act 1977 does not apply where the negligence consists of breach of an obligation arising from a term of a contract and the person enforcing is a third party relying on section 2", "encoded", ["s 8(2) section 2(2) of the Unfair Contract Terms Act 1977 does not apply"], ["s8(2)"])
row("S08-3", 341, 343, "s 8(3)", "in section 6 of the Limitation Act 1959 the references to an action founded on a contract include an action brought in reliance on section 2", "encoded", ["s 8(3) the action is one founded on a contract for the purposes of section 6 of the Limitation Act 1959", "s 8(3) the period that applies to the action, in years"], ["s8(3)"])
row("S08-4", 345, 347, "s 8(4)", "a third party is not, by virtue of section 2(5) or 4(4) or (6), treated as a party for the purposes of any other written law", "encoded", ["s 8(4) the third party is treated as a party to the contract for the purposes of any other written law"], ["s8(4)"])

row("S09", 354, 354, "s 9 heading", "Arbitration provisions", "inert1", keys=["s9"])
row("S09-1", 356, 356, "s 9(1) (lead-in)", "Where (a) and (b)", "encoded (M5)", ["s 9(1) the third party is treated as a party to the arbitration agreement"], ["s9(1)"])
row("S09-1a", 358, 361, "s 9(1)(a)", "a right under section 2 to enforce a term (the substantive term) is subject to a term providing for the submission of disputes to arbitration (the arbitration agreement)", "encoded", ["s 9(1) the third party is treated as a party to the arbitration agreement"], ["s9(1)(a)"])
row("D09", 358, 359, "s 9(1)(a) \"substantive term\"", "defined term: a term the third party has a right under section 2 to enforce, that is subject to an arbitration term", "encoded", ["s 9(1) the third party is treated as a party to the arbitration agreement"], ["term:substantive term"])
row("D10", 359, 361, "s 9(1)(a) \"arbitration agreement\"", "defined term: the term providing for the submission of disputes to arbitration", "encoded", ["s 9(1) the third party is treated as a party to the arbitration agreement"], ["term:arbitration agreement"])
row("S09-1b", 363, 365, "s 9(1)(b)", "the arbitration agreement is an agreement in writing for the purposes of the Arbitration Act 2001 or Part 2 of the International Arbitration Act 1994", "encoded", ["s 9(1) the third party is treated as a party to the arbitration agreement"], ["s9(1)(b)"])
row("S09-1t", 367, 371, "s 9(1) (tail)", "the third party is treated as a party to the arbitration agreement as regards disputes about the third party's enforcement of the substantive term", "encoded",
    ["s 9(1) the third party is treated as a party to the arbitration agreement", "s 9(1) the Act for the purposes of which the third party is treated as a party"])
row("S09-2", 373, 373, "s 9(2) (lead-in)", "Where (a), (b) and (c)", "encoded (M5)", ["s 9(2) the third party is treated as a party to the arbitration agreement"], ["s9(2)"])
row("S09-2a", 375, 379, "s 9(2)(a)", "a third party has a right under section 2 to enforce a term providing for disputes between the third party and the promisor to be submitted to arbitration", "encoded", ["s 9(2) the third party is treated as a party to the arbitration agreement"], ["s9(2)(a)"])
row("D11", 378, 379, "s 9(2)(a) \"arbitration agreement\"", "defined term for the purposes of s 9(2)", "encoded", ["s 9(2) the third party is treated as a party to the arbitration agreement"], ["term:arbitration agreement"])
row("S09-2b", 381, 383, "s 9(2)(b)", "the arbitration agreement is an agreement in writing for the purposes of either Act", "encoded", ["s 9(2) the third party is treated as a party to the arbitration agreement"], ["s9(2)(b)"])
row("S09-2c", 385, 386, "s 9(2)(c)", "the third party does not fall to be treated under subsection (1) as a party to the arbitration agreement", "encoded", ["s 9(2) the third party is treated as a party to the arbitration agreement"], ["s9(2)(c)"])
row("S09-2t", 388, 393, "s 9(2) (tail)", "the third party is, if the third party exercises the right, treated as a party, and as having been so immediately before the exercise", "encoded", ["s 9(2) the third party is treated as a party to the arbitration agreement"])

row("B01", 394, 398, "legislative history (heading and note)", "\"This Legislative History ... is not part of the Act.\"", "inert1")
row("B02", 400, 408, "legislative history 1", "Act 39 of 2001", "inert1", keys=["hist:1."])
row("B03", 410, 413, "legislative history 2", "2002 Revised Edition", "inert1", keys=["hist:2."])
row("B04", 415, 426, "legislative history 3", "Act 5 of 2005 (Limited Liability Partnerships Act 2005)", "inert1", keys=["hist:3."])
row("B05", 428, 443, "legislative history 4", "Act 40 of 2019 (Supreme Court of Judicature (Amendment) Act 2019)", "inert1", keys=["hist:4."])
row("B06", 445, 454, "legislative history 5", "Act 5 of 2021 (Electronic Transactions (Amendment) Act 2021)", "inert1", keys=["hist:5."])
row("B07", 456, 456, "abbreviations (heading)", "Abbreviations", "inert1")
for i, ab in [(458, "C.P."), (460, "G.N. No. S (N.S.)"), (462, "G.N. No."), (464, "G.N. No. S"), (466, "G.N. Sp. No. S"), (468, "L.A."), (470, "L.N."), (474, "M. Act"), (476, "M. Ordinance"), (478, "Parl."), (480, "S.S.G.G. (E) No."), (483, "S.S.G.G. No.")]:
    last = {470: 472, 480: 481}.get(i, i)
    row("X%03d" % i, i, last, "abbreviation \"%s\"" % ab, "abbreviations table row", "inert1", keys=["abbr:" + ab])
row("B08", 484, 489, "comparative table (heading and note)", "\"provided to help readers locate the corresponding provisions in the last Revised Edition\"", "inert1")
row("B09", 491, 491, "comparative table (column heads)", "2020 Ed. | 2002 Ed.", "inert1")
for i, k in [(493, "7—(3) 7—(2A)"), (494, "(4) (3)"), (495, "(5) (4)"), (496, "(6) (5)"), (497, "(7) (6)")]:
    row("C%03d" % i, i, i, "comparative table row", k.replace(" ", " <-> ", 1) if False else k, "inert1", keys=["cmp:" + k])

# ----------------------------------------------------------------------------------------------- checks
fail = []
covered = [0] * (N + 2)
for r in R:
    for l in range(r["a"], r["b"] + 1):
        covered[l] += 1
# furniture rows, automatic
F = []
cur = None
for l in range(1, N + 1):
    s = lines[l - 1]
    if not s.strip() or covered[l]:
        cur = None if covered[l] else cur
        continue
    if furniture(s):
        if cur and l - cur["b"] <= 3:
            cur["b"] = l
        else:
            cur = dict(id="P%02d" % (len(F) + 1), a=l, b=l)
            F.append(cur)
        covered[l] += 1
    else:
        fail.append("line %d is not blank, not in any row and not page furniture: %r" % (l, s))
        cur = None
uncov = [l for l in range(1, N + 1) if lines[l - 1].strip() and not covered[l]]
if uncov:
    fail.append("uncovered non-blank lines: %s" % uncov)

claimed = collections.Counter()
for r in R:
    for k in r["keys"]:
        claimed[k] += 1
for k, n in scan.items():
    if claimed[k] != n:
        fail.append("scan found %d x %s but the rows claim %d" % (n, k, claimed[k]))
for k, n in claimed.items():
    if k not in scan:
        fail.append("a row claims %s which the scan did not find" % k)

defs = set()
for f in glob.glob(os.path.join(DIR, "crtpa-*.l4")):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r"^`([^`]+)` (?:MEANS|IS)\b", t, flags=re.M):
        defs.add(m.group(1))
    for m in re.finditer(r"^DECIDE `([^`]+)` IS", t, flags=re.M):
        defs.add(m.group(1))
for r in R:
    for fn in r["rules"]:
        if fn not in defs:
            fail.append("row %s names a rule that is not defined in the folder: %s" % (r["id"], fn))

# every section-named rule in the folder (a name beginning "s <n>" or "ss ") is claimed by some row
named = {x for r in R for x in r["rules"]}
for d in sorted(defs):
    if re.match(r"^(s \d|ss \d)", d) and d not in named:
        fail.append("rule defined in the folder but cited by no row: %s" % d)

# ----------------------------------------------------------------------------------------------- report
def kind(d):
    d = d.split(" (")[0]
    return "inert (reason %s)" % d[-1] if d.startswith("inert") else d.split(":")[0]
cnt = collections.Counter(kind(r["disp"]) for r in R)
cnt["inert (reason 1)"] += len(F)
total = len(R) + len(F)

def disp_text(d):
    if d.startswith("inert"):
        return "inert, reason %s" % d[5]
    if d.startswith("fork:"):
        return "fork " + d[5:]
    return d

if MD:
    print("| Row | Lines | Provision | What the text says | Disposition | Encoded by |")
    print("| --- | --- | --- | --- | --- | --- |")
    allrows = sorted([(r["a"], r["id"], r) for r in R] + [(f["a"], f["id"], dict(f, prov="page furniture", what="page numbers, date stamps, running heads, amendment marks", disp="inert1", rules=[])) for f in F], key=lambda x: (x[0], x[1]))
    for _, _, r in allrows:
        rng = "%d" % r["a"] if r["a"] == r["b"] else "%d-%d" % (r["a"], r["b"])
        rules = "<br>".join("`%s`" % x for x in r["rules"]) if r["rules"] else ""
        print("| %s | %s | %s | %s | %s | %s |" % (r["id"], rng, r["prov"], r["what"].replace("|", "/"), disp_text(r["disp"]), rules))
else:
    print("coverage rows: %d hand rows + %d automatic page-furniture rows = %d" % (len(R), len(F), total))
    for k in sorted(cnt):
        print("  %-20s %d" % (k, cnt[k]))
    units = sum(scan.values())
    print("text units the scan counted: %d (sections %d, subsections+paragraphs %d, defined terms %d, history items %d, abbreviations %d, comparative-table rows %d)" % (
        units, sum(v for k, v in scan.items() if re.fullmatch(r"s\d", k)),
        sum(v for k, v in scan.items() if k.startswith("s") and not re.fullmatch(r"s\d", k)),
        sum(v for k, v in scan.items() if k.startswith("term:")), sum(v for k, v in scan.items() if k.startswith("hist:")),
        sum(v for k, v in scan.items() if k.startswith("abbr:")), sum(v for k, v in scan.items() if k.startswith("cmp:"))))
    nb = sum(1 for s in lines if s.strip())
    print("non-blank lines of the text: %d; covered by some row: %d" % (nb, sum(1 for l in range(1, N + 1) if lines[l - 1].strip() and covered[l])))
    print("rules named in the table: %d distinct, all defined" % len({x for r in R for x in r["rules"]}) if not fail else "")
if fail:
    for f in fail:
        print("FAIL:", f, file=sys.stderr)
    sys.exit(1)
