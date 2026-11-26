#!/usr/bin/env python3
# notes/gen-tests-p2.py -- writes P2-tests-art-12.l4 ... P2-tests-art-23.l4 from the cases below.
# Run from the deposit folder:   python3 -I notes/gen-tests-p2.py [12 13 ...]
# Every EXPECTED VALUE below was written by hand from the text of the provision named in the comment of the
# case, BEFORE the first run; the generator copies the values and computes none of them.
# A case is T(function, [arguments as L4 text], expected as L4 text, why).  A trace is TR(function, [arguments], "AT 0", [events], why).
import sys, re

JT, JF, NO = "JUST TRUE", "JUST FALSE", "NOTHING"
AJT, AJF = "(JUST TRUE)", "(JUST FALSE)"   # a MAYBE BOOLEAN used as an ARGUMENT needs brackets
T_, F_ = "TRUE", "FALSE"
MET = "JUST `the duty arises and is met`"
UNMET = "JUST `the duty arises and is not met`"
NOARISE = "JUST `the duty does not arise`"

def D(d, m, y):
    return "(Date %d %d %d)" % (d, m, y)

class Mod:
    def __init__(self, art, imports, title):
        self.art, self.imports, self.title, self.items = art, imports, title, []
    def S(self, heading):
        self.items.append(("S", heading))
    def T(self, fn, args, exp, why):
        self.items.append(("T", fn, args, exp, why))
    def TR(self, fn, args, start, events, why):
        self.items.append(("TR", fn, args, start, events, why))
    def C(self, text):
        self.items.append(("C", text))
    def write(self):
        out = []
        for i in self.imports:
            out.append("IMPORT %s" % i)
        out.append("")
        out.append("-- " + "=" * 76)
        out.append("-- P2-tests-art-%s.l4 -- tests of %s." % (self.art, self.title))
        out.append("-- Every expected value was written by hand from the text of the provision named in the comment above it,")
        out.append("-- before the first run, and none was copied from an output (notes/gen-tests-p2.py holds the cases).")
        out.append("-- A #TRACE result is not an assertion and check.sh does not count it; each trace comment gives the expected result.")
        out.append("-- " + "=" * 76)
        for it in self.items:
            if it[0] == "S":
                out.append("")
                out.append("§ `%s`" % it[1])
                out.append("")
            elif it[0] == "C":
                out.append("-- " + it[1])
            elif it[0] == "T":
                _, fn, args, exp, why = it
                out.append("-- " + why)
                a = (" " + " ".join(args)) if args else ""
                out.append("#ASSERT `%s`%s EQUALS %s" % (fn, a, exp))
            elif it[0] == "TR":
                _, fn, args, start, events, why = it
                out.append("-- " + why)
                a = (" " + " ".join(args)) if args else ""
                out.append("#TRACE `%s`%s %s WITH" % (fn, a, start))
                for e in events:
                    out.append("    " + e)
        open("P2-tests-art-%s.l4" % self.art, "w", encoding="utf-8").write("\n".join(out) + "\n")
        n = sum(1 for it in self.items if it[0] == "T"); t = sum(1 for it in self.items if it[0] == "TR")
        print("P2-tests-art-%s.l4: %d assertions, %d traces" % (self.art, n, t))

MODS = {}

# =============================================================================================== Article 12
m = Mod("12", ["prelude", "daydate", "`gdpr-core`", "`P2-art-12`"], "Article 12 (src:146-158)")
MODS["12"] = m
F121 = "Art 12(1) the controller takes appropriate measures to provide the information and communications in a concise, transparent, intelligible and easily accessible form, using clear and plain language"
m.S("Art 12(1) first sentence: appropriate measures, concise, transparent, intelligible, easily accessible, clear and plain")
m.T(F121, [T_]*6 + [F_], JT, "all six requirements met; not addressed to a child")
m.T(F121, [T_]*6 + [T_], JT, "all six met, and the information is addressed to a child: 'in particular' stresses a case and adds no test")
m.T(F121, [F_] + [T_]*5 + [F_], JF, "no appropriate measures taken: 'shall take appropriate measures'")
m.T(F121, [T_, F_] + [T_]*4 + [F_], JF, "not concise")
m.T(F121, [T_, T_, F_] + [T_]*3 + [F_], JF, "not transparent")
m.T(F121, [T_]*3 + [F_] + [T_]*2 + [F_], JF, "not intelligible")
m.T(F121, [T_]*4 + [F_] + [T_] + [F_], JF, "not easily accessible")
m.T(F121, [T_]*5 + [F_] + [F_], JF, "not clear and plain language")
m.T(F121, [T_]*5 + [F_] + [T_], JF, "not clear and plain language, information addressed to a child: still JUST FALSE")
m.T("Art 12(1) the controller has taken appropriate measures", [T_], JT, "measures taken")
m.T("Art 12(1) the controller has taken appropriate measures", [F_], JF, "no measures: 'shall take appropriate measures'")
F121b = "Art 12(1) the information is provided in writing, or by other means, including, where appropriate, by electronic means"
m.S("Art 12(1) second sentence: in writing, or by other means")
m.T(F121b, [T_, F_, F_, F_], JT, "in writing")
m.T(F121b, [F_, T_, F_, F_], JT, "by other means (oral, say)")
m.T(F121b, [F_, F_, T_, F_], JT, "by electronic means alone: an example of 'other means'")
m.T(F121b, [F_, F_, T_, T_], JT, "by electronic means, where appropriate")
m.T(F121b, [F_, F_, F_, F_], JF, "in no form at all: 'shall be provided in writing, or by other means'")
m.T(F121b, [F_, F_, F_, T_], JF, "that electronic means would be appropriate does not supply the information")
F121c = "Art 12(1) the information may be provided orally"
m.S("Art 12(1) third sentence: orally, when requested, provided that the identity is proven by other means")
m.T(F121c, [T_, T_], JT, "requested by the data subject and identity proven by other means")
m.T(F121c, [F_, T_], JF, "not requested by the data subject: 'When requested by the data subject' (a failed 'When', ruling (b))")
m.T(F121c, [T_, F_], JF, "identity not proven by other means: 'provided that'")
m.T(F121c, [F_, F_], JF, "neither")
R1 = "Art 12(1) the controller must take appropriate measures to provide the information and communications"
m.S("Art 12(1): the regulative rule (no time limit, no consequence: it can stand or be fulfilled, never be breached)")
m.TR(R1, [], "AT 0", ["PARTY controller DOES `Art 12(1) take appropriate measures to provide the information and communications in the form that paragraph 1 requires` AT 1"], "the controller takes the measures: FULFILLED")
m.TR(R1, [], "AT 0", ["(WAITUNTIL 1000)"], "no act, a long time later: the obligation still stands (a MUST with no WITHIN never breaches)")
F122a = "Art 12(2) the controller facilitates the exercise of data subject rights under Articles 15 to 22"
m.S("Art 12(2) first sentence: facilitate")
m.T(F122a, [T_], JT, "the controller has facilitated the exercise of the rights")
m.T(F122a, [F_], JF, "the controller has not: 'shall facilitate'")
R2a = "Art 12(2) the controller must facilitate the exercise of data subject rights under Articles 15 to 22"
m.TR(R2a, [], "AT 0", ["PARTY controller DOES `Art 12(2) facilitate the exercise of data subject rights under Articles 15 to 22` AT 1"], "the controller facilitates: FULFILLED")
m.TR(R2a, [], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands, no breach is possible (no time limit)")
F122b = "Art 12(2) the controller shall not refuse to act on the request of the data subject in the cases referred to in Article 11(2)"
m.S("Art 12(2) second sentence: in the cases referred to in Article 11(2), no refusal unless the controller demonstrates it cannot identify")
m.T(F122b, [NO, F_], NO, "P1 says the case is outside Article 11(2): 'In the cases referred to in Article 11(2)' is not met, the text is silent")
m.T(F122b, [NO, T_], NO, "outside Article 11(2), and the controller demonstrates it cannot identify: still not covered")
m.T(F122b, [AJT, F_], JT, "an Article 11(2) case, the controller has not demonstrated it cannot identify: it shall not refuse to act")
m.T(F122b, [AJT, T_], JF, "an Article 11(2) case, and the controller demonstrates it is not in a position to identify: 'unless'")
m.T(F122b, [AJF, F_], JT, "an Article 11(2) case in which the data subject provided identifying information: the controller shall not refuse")
m.T(F122b, [AJF, T_], JF, "the same, but the controller still demonstrates it cannot identify: 'unless'")
R2b = "Art 12(2) the controller shall not refuse to act on the request in the cases referred to in Article 11(2)"
m.TR(R2b, [AJT, F_], "AT 0", ["PARTY controller DOES `Art 12(2) refuse to act on the request of the data subject` AT 1"], "BREACH: refusing in an Article 11(2) case with no demonstration (the act is the breach)")
m.TR(R2b, [AJF, F_], "AT 0", ["PARTY controller DOES `Art 12(2) refuse to act on the request of the data subject` AT 1"], "BREACH: the data subject provided identifying information, the controller still refuses")
m.TR(R2b, [AJT, T_], "AT 0", ["PARTY controller DOES `Art 12(2) refuse to act on the request of the data subject` AT 1"], "FULFILLED: the controller demonstrates it cannot identify, so refusing is not barred")
m.TR(R2b, [NO, F_], "AT 0", ["PARTY controller DOES `Art 12(2) refuse to act on the request of the data subject` AT 1"], "FULFILLED: outside Article 11(2) this sentence does not bar")
m.TR(R2b, [AJT, F_], "AT 0", ["(WAITUNTIL 1000)"], "no refusal: the prohibition stands, unbroken")
FM = "Art 12(3) the months within which the information on action taken is to be provided"
m.S("Art 12(3) first and second sentences: one month, extended by two further months")
m.T(FM, [F_], "1", "one month")
m.T(FM, [T_], "3", "one month extended by two further months")
F123 = "Art 12(3) the controller provides information on action taken on the request without undue delay and within one month of receipt of the request"
m.T(F123, [D(15,3,2026), D(15,4,2026), T_, F_], JT, "provided on the last day of the month: 15 March to 15 April")
m.T(F123, [D(15,3,2026), D(16,4,2026), T_, F_], JF, "one day after the month: 'in any event within one month'")
m.T(F123, [D(15,3,2026), D(15,3,2026), T_, F_], JT, "provided on the day of receipt")
m.T(F123, [D(31,1,2026), D(28,2,2026), T_, F_], JT, "31 January plus one month ends on 28 February (the month is short)")
m.T(F123, [D(31,1,2026), D(1,3,2026), T_, F_], JF, "1 March is after the month that began on 31 January")
m.T(F123, [D(15,1,2026), D(15,4,2026), T_, T_], JT, "extended by two further months: three months in all, last day")
m.T(F123, [D(15,1,2026), D(16,4,2026), T_, T_], JF, "extended, one day after the three months")
m.T(F123, [D(15,1,2026), D(20,2,2026), T_, F_], JF, "no extension: 20 February is after one month from 15 January")
m.T(F123, [D(15,3,2026), D(20,3,2026), F_, F_], JF, "within the month but with undue delay: 'without undue delay'")
F123x = "Art 12(3) the period may be extended by two further months"
m.T(F123x, [T_], JT, "necessary, taking into account the complexity and number of the requests")
m.T(F123x, [F_], JF, "not necessary: 'where necessary' (a failed 'where', ruling (b))")
F123n = "Art 12(3) the controller informs the data subject of the extension within one month of receipt of the request, together with the reasons for the delay"
m.T(F123n, [F_, D(10,1,2026), D(10,2,2026), T_], NO, "no extension: 'any such extension' is not met, the text is silent")
m.T(F123n, [T_, D(10,1,2026), D(10,2,2026), T_], MET, "informed on the last day of the month with the reasons")
m.T(F123n, [T_, D(10,1,2026), D(11,2,2026), T_], UNMET, "informed one day after the month")
m.T(F123n, [T_, D(10,1,2026), D(20,1,2026), F_], UNMET, "informed in time but without the reasons for the delay")
R3 = "Art 12(3) the controller must provide the data subject with information on action taken on the request"
m.TR(R3, [F_], "AT 0", ["PARTY controller DOES `Art 12(3) provide the data subject with information on action taken on the request` AT 1"], "FULFILLED: provided at month 1, the last moment of the first month (the deadline is inclusive)")
m.TR(R3, [F_], "AT 0", ["PARTY controller DOES `Art 12(3) provide the data subject with information on action taken on the request` AT 2"], "BREACH: provided at month 2, after one month, with no extension")
m.TR(R3, [F_], "AT 0", ["(WAITUNTIL 2)"], "BREACH: nothing provided by month 2")
m.TR(R3, [T_], "AT 0", ["(WAITUNTIL 2)"], "extended by two further months: at month 2 the obligation still stands (residual)")
m.TR(R3, [T_], "AT 0", ["(WAITUNTIL 4)"], "BREACH: extended, nothing provided by month 4 (three months allowed)")
m.TR(R3, [T_], "AT 0", ["PARTY controller DOES `Art 12(3) provide the data subject with information on action taken on the request` AT 3"], "FULFILLED: extended, provided at month 3")
RN = "Art 12(3) the controller must inform the data subject of the extension within one month of receipt of the request"
m.TR(RN, [T_], "AT 0", ["PARTY controller DOES `Art 12(3) inform the data subject of the extension, with the reasons for the delay` AT 1"], "FULFILLED: the extension notified at month 1")
m.TR(RN, [T_], "AT 0", ["(WAITUNTIL 2)"], "BREACH: an extension and no notice within one month")
m.TR(RN, [F_], "AT 0", ["(WAITUNTIL 2)"], "FULFILLED: no extension, nothing to inform of")
FE = "Art 12(3) the information is provided by electronic means where the request is made by electronic form means"
m.S("Art 12(3) fourth sentence: by electronic means where the request is by electronic form means")
m.T(FE, [T_, T_, F_, T_], MET, "electronic request, possible, not requested otherwise, provided electronically")
m.T(FE, [T_, T_, F_, F_], UNMET, "electronic request, possible, not requested otherwise, but provided on paper")
m.T(FE, [F_, T_, F_, F_], NOARISE, "the request was not made by electronic form means: 'Where' fails")
m.T(FE, [T_, F_, F_, F_], NOARISE, "not possible: 'where possible'")
m.T(FE, [T_, T_, T_, F_], NOARISE, "the data subject requested otherwise: 'unless otherwise requested'")
F124 = "Art 12(4) the controller informs the data subject of the reasons for not taking action and of the possibilities of a complaint and a judicial remedy"
m.S("Art 12(4): the reasons for not taking action")
m.T(F124, [F_, D(1,2,2026), D(1,3,2026), T_, T_, T_, T_], NOARISE, "the controller does take action: 'If the controller does not take action' fails")
m.T(F124, [T_, D(1,2,2026), D(1,3,2026), T_, T_, T_, T_], MET, "no action; informed on the last day of the month, without delay, with the three contents")
m.T(F124, [T_, D(1,2,2026), D(2,3,2026), T_, T_, T_, T_], UNMET, "informed one day after the month")
m.T(F124, [T_, D(1,2,2026), D(5,2,2026), F_, T_, T_, T_], UNMET, "within the month but not 'without delay'")
m.T(F124, [T_, D(1,2,2026), D(5,2,2026), T_, F_, T_, T_], UNMET, "no reasons for not taking action")
m.T(F124, [T_, D(1,2,2026), D(5,2,2026), T_, T_, F_, T_], UNMET, "no mention of the possibility of lodging a complaint with a supervisory authority")
m.T(F124, [T_, D(1,2,2026), D(5,2,2026), T_, T_, T_, F_], UNMET, "no mention of the possibility of seeking a judicial remedy")
R4 = "Art 12(4) the controller must inform the data subject of the reasons for not taking action within one month of receipt of the request"
m.TR(R4, [T_], "AT 0", ["PARTY controller DOES `Art 12(4) inform the data subject of the reasons for not taking action and of the possibilities of a complaint and a judicial remedy` AT 1"], "FULFILLED: informed at month 1")
m.TR(R4, [T_], "AT 0", ["(WAITUNTIL 2)"], "BREACH: no action taken and no reasons given within one month")
m.TR(R4, [F_], "AT 0", ["(WAITUNTIL 2)"], "FULFILLED: the controller takes action, so this duty does not arise")
m.S("Art 12(5): free of charge, a reasonable fee, refusal, the burden")
m.T("Art 12(5) the information, communication or action is provided free of charge", [F_], JT, "no fee charged")
m.T("Art 12(5) the information, communication or action is provided free of charge", [T_], JF, "a fee is charged: 'shall be provided free of charge'")
FA = "Art 12(5)(a) the controller may charge a reasonable fee"
m.T(FA, [T_, T_, T_], JT, "manifestly unfounded or excessive, demonstrated, reasonable fee")
m.T(FA, [F_, T_, T_], JF, "the request is not manifestly unfounded or excessive: 'Where' fails")
m.T(FA, [T_, F_, T_], JF, "the controller has not borne the burden of demonstrating the character of the request")
m.T(FA, [T_, T_, F_], NO, "a fee that is not reasonable or not based on the administrative costs is outside the grant, which the text limits by its own wording")
m.T(FA, [F_, F_, F_], JF, "none of the three")
FB = "Art 12(5)(b) the controller may refuse to act on the request"
m.T(FB, [T_, T_], JT, "manifestly unfounded or excessive and demonstrated")
m.T(FB, [F_, T_], JF, "not manifestly unfounded or excessive")
m.T(FB, [T_, F_], JF, "the burden of demonstrating has not been borne")
FBu = "Art 12(5) the controller has borne the burden of demonstrating the manifestly unfounded or excessive character of the request"
m.T(FBu, [T_], JT, "demonstrated")
m.T(FBu, [F_], JF, "not demonstrated: 'shall bear the burden of demonstrating'")
F126 = "Art 12(6) the controller may request the provision of additional information necessary to confirm the identity of the data subject"
m.S("Art 12(6): additional information to confirm identity")
m.T(F126, [T_, T_], JT, "reasonable doubts, and the information is necessary to confirm identity")
m.T(F126, [F_, T_], JF, "no reasonable doubts: 'where' fails")
m.T(F126, [T_, F_], NO, "reasonable doubts, but the information asked for is not necessary to confirm identity: outside the grant")
m.T(F126, [F_, F_], JF, "no reasonable doubts and not necessary")
F127a = "Art 12(7) the information may be provided in combination with standardised icons"
m.S("Art 12(7): standardised icons")
m.T(F127a, [T_], JT, "information under Article 13 or 14")
m.T(F127a, [F_], NO, "information under another Article: outside the grant, and the text does not say no")
F127b = "Art 12(7) the icons presented electronically are machine-readable"
m.T(F127b, [T_, T_], MET, "presented electronically and machine-readable")
m.T(F127b, [T_, F_], UNMET, "presented electronically and not machine-readable: 'shall be machine-readable'")
m.T(F127b, [F_, T_], NOARISE, "not presented electronically: 'Where' fails")
m.T(F127b, [F_, F_], NOARISE, "not presented electronically, not machine-readable: the duty does not arise")

# =============================================================================================== Article 13
m = Mod("13", ["prelude", "`gdpr-core`", "`P2-art-13`"], "Article 13 (src:161-178)")
MODS["13"] = m
I1a = "`Art 13(1)(a) the identity and the contact details of the controller`"
I1ar = "`Art 13(1)(a) the identity and the contact details of the controller's representative`"
I1b = "`Art 13(1)(b) the contact details of the data protection officer`"
I1cp = "`Art 13(1)(c) the purposes of the processing for which the personal data are intended`"
I1cl = "`Art 13(1)(c) the legal basis for the processing`"
I1d = "`Art 13(1)(d) the legitimate interests pursued by the controller or by a third party`"
I1e = "`Art 13(1)(e) the recipients or categories of recipients of the personal data`"
I1f = "`Art 13(1)(f) the intended transfer to a third country or international organisation and the adequacy decision or the safeguards`"
def L(*xs):
    return "(LIST " + ", ".join(xs) + ")" if xs else "EMPTY"
BASE = [I1a, I1cp, I1cl]
F131 = "Art 13(1) the controller provides the data subject with all of the following information"
G6f = "`Art 6(1)(f) point (f) applies: the processing is necessary for legitimate interests that are not overridden`"
# arguments: collected, has representative, has DPO, (f) gate, recipients, transfer, provided, already has, provided at the time (R4)
def a131(coll=T_, rep=F_, dpo=F_, gate="(JUST FALSE)", rec=F_, tr=F_, prov=BASE, has=(), time=T_):
    return [coll, rep, dpo, gate, rec, tr, L(*prov), L(*has), time]
m.S("Art 13(1): the information at the time when the data are obtained")
m.T(F131, a131(coll=F_, prov=()), NOARISE, "the data are not collected from the data subject: 'Where personal data ... are collected from the data subject' fails")
m.T(F131, a131(), MET, "collected; no representative, officer, recipients or transfer; point (f) not relied on; points (a) and (c) provided")
m.T(F131, a131(prov=[I1cp, I1cl]), UNMET, "(a) the identity and contact details of the controller not provided")
m.T(F131, a131(prov=[I1a, I1cl]), UNMET, "(c) the purposes not provided")
m.T(F131, a131(prov=[I1a, I1cp]), UNMET, "(c) the legal basis not provided")
m.T(F131, a131(prov=()), UNMET, "nothing provided")
m.T(F131, a131(rep=T_), UNMET, "(a) 'where applicable, of the controller's representative': there is one and its identity was not provided")
m.T(F131, a131(rep=T_, prov=BASE + [I1ar]), MET, "the representative's identity and contact details provided too")
m.T(F131, a131(dpo=T_), UNMET, "(b) 'where applicable': there is an officer and the contact details were not provided")
m.T(F131, a131(dpo=T_, prov=BASE + [I1b]), MET, "(b) provided")
m.T(F131, a131(rec=T_), UNMET, "(e) 'if any': there are recipients and they were not named")
m.T(F131, a131(rec=T_, prov=BASE + [I1e]), MET, "(e) provided")
m.T(F131, a131(tr=T_), UNMET, "(f) 'where applicable': a transfer is intended and it was not disclosed")
m.T(F131, a131(tr=T_, prov=BASE + [I1f]), MET, "(f) provided")
m.T(F131, a131(gate="(JUST TRUE)"), UNMET, "(d) 'where the processing is based on point (f) of Article 6(1)': it is, and the legitimate interests were not provided")
m.T(F131, a131(gate="(JUST TRUE)", prov=BASE + [I1d]), MET, "(d) provided")
m.T(F131, a131(gate="(JUST FALSE)"), MET, "(d) not owed: point (f) does not apply")
m.T(F131, a131(gate="NOTHING"), NO, "whether point (f) applies is not answered (P1): item (d) is neither provided nor shown not to be owed")
m.T(F131, a131(gate="NOTHING", prov=BASE + [I1d]), MET, "point (f) not answered, but (d) was provided in any event")
m.T(F131, a131(gate="NOTHING", prov=[I1cp, I1cl]), UNMET, "point (f) not answered, but item (a) is missing: unmet whatever (d) is")
m.T(F131, a131(has=[I1cl]  , prov=[I1a, I1cp]), MET, "(c) the legal basis: not provided, but the data subject already has it ('where and insofar as', paragraph 4)")
m.T(F131, a131(has=[I1a, I1cp, I1cl], prov=()), MET, "the data subject already has everything")
m.T(F131, a131(has=[I1cl], prov=[I1a]), UNMET, "the data subject already has the legal basis, but not the purposes")
m.T(F131, a131(rep=T_, dpo=T_, gate="(JUST TRUE)", rec=T_, tr=T_, prov=BASE + [I1ar, I1b, I1d, I1e, I1f]), MET, "every point applies and every item is provided")
m.T(F131, a131(prov=BASE + [I1ar, I1b, I1d, I1e, I1f]), MET, "items provided that do not apply are harmless")
R131 = "Art 13(1) the controller must provide the data subject with all of the following information at the time when the personal data are obtained"
A131 = "PARTY controller DOES `Art 13(1) provide the data subject with all of the following information` AT %s"
m.TR(R131, [T_], "AT 0", [A131 % 0], "FULFILLED: provided at the time the data are obtained (the deadline, WITHIN 0, is inclusive)")
m.TR(R131, [T_], "AT 0", [A131 % 1], "BREACH: provided one instant after the data were obtained")
m.TR(R131, [T_], "AT 0", ["(WAITUNTIL 1)"], "BREACH: nothing provided when the time passes")
m.TR(R131, [F_], "AT 0", ["(WAITUNTIL 1)"], "FULFILLED: the data are not collected from the data subject, so Article 14 and not this paragraph")
I2a = "`Art 13(2)(a) the period for which the personal data will be stored, or the criteria used to determine that period`"
I2b = "`Art 13(2)(b) the existence of the rights of access, rectification, erasure, restriction, objection and data portability`"
I2c = "`Art 13(2)(c) the existence of the right to withdraw consent at any time, without affecting the lawfulness of processing before its withdrawal`"
I2d = "`Art 13(2)(d) the right to lodge a complaint with a supervisory authority`"
I2e = "`Art 13(2)(e) whether the provision of personal data is a statutory or contractual requirement, whether the data subject is obliged to provide the data and the possible consequences of failure`"
I2f = "`Art 13(2)(f) the existence of automated decision-making, including profiling, and meaningful information about the logic involved, the significance and the envisaged consequences`"
B2 = [I2a, I2b, I2d, I2e]
F132 = "Art 13(2) the controller provides the data subject with the following further information necessary to ensure fair and transparent processing"
def a132(coll=T_, cons=F_, adm=F_, prov=B2, has=(), time=T_):
    return [coll, cons, adm, L(*prov), L(*has), time]
m.S("Art 13(2): the further information")
m.T(F132, a132(coll=F_, prov=()), NO, "data not collected from the data subject: 'In addition to the information referred to in paragraph 1' is not met, the text is silent")
m.T(F132, a132(), MET, "(a), (b), (d), (e) provided; no consent basis and no automated decision-making")
m.T(F132, a132(prov=[I2b, I2d, I2e]), UNMET, "(a) the storage period or criteria not provided")
m.T(F132, a132(prov=[I2a, I2d, I2e]), UNMET, "(b) the existence of the rights not provided")
m.T(F132, a132(prov=[I2a, I2b, I2e]), UNMET, "(d) the right to lodge a complaint not provided")
m.T(F132, a132(prov=[I2a, I2b, I2d]), UNMET, "(e) statutory or contractual requirement not provided")
m.T(F132, a132(cons=T_), UNMET, "(c) 'where the processing is based on point (a) of Article 6(1) or point (a) of Article 9(2)': it is, and the right to withdraw consent was not provided")
m.T(F132, a132(cons=T_, prov=B2 + [I2c]), MET, "(c) provided")
m.T(F132, a132(adm=T_), UNMET, "(f) there is automated decision-making referred to in Article 22(1) and (4), and its existence and logic were not provided")
m.T(F132, a132(adm=T_, prov=B2 + [I2f]), MET, "(f) provided")
m.T(F132, a132(prov=B2 + [I2c, I2f]), MET, "items provided that do not apply are harmless")
m.T(F132, a132(prov=[I2a, I2b, I2d], has=[I2e]), MET, "(e) not provided but the data subject already has it (paragraph 4)")
m.T(F132, a132(cons=T_, adm=T_, prov=B2 + [I2c, I2f]), MET, "every point applies and every item is provided")
R132 = "Art 13(2) the controller must provide the data subject with the further information at the time when the personal data are obtained"
A132 = "PARTY controller DOES `Art 13(2) provide the data subject with the further information necessary to ensure fair and transparent processing` AT %s"
m.TR(R132, [T_], "AT 0", [A132 % 0], "FULFILLED: provided at the time the data are obtained")
m.TR(R132, [T_], "AT 0", ["(WAITUNTIL 1)"], "BREACH: not provided at the time")
m.TR(R132, [F_], "AT 0", ["(WAITUNTIL 1)"], "FULFILLED: the data are not collected from the data subject")
F133 = "Art 13(3) the controller provides the data subject, prior to the further processing, with information on the other purpose and any relevant further information"
# arguments: intends, provided purpose info, provided further info, prior, already has purpose info, already has further info
m.S("Art 13(3): further processing for another purpose")
m.T(F133, [F_, F_, F_, F_, F_, F_], NOARISE, "no further processing intended: 'Where' fails")
m.T(F133, [T_, T_, T_, T_, F_, F_], MET, "both kinds of information provided before the further processing")
m.T(F133, [T_, T_, T_, F_, F_, F_], UNMET, "provided, but not before the further processing: 'prior to that further processing'")
m.T(F133, [T_, F_, T_, T_, F_, F_], UNMET, "no information on the other purpose")
m.T(F133, [T_, T_, F_, T_, F_, F_], UNMET, "no relevant further information")
m.T(F133, [T_, F_, F_, F_, T_, T_], MET, "nothing provided, but the data subject already has both kinds of information (paragraph 4): the time is then immaterial")
m.T(F133, [T_, F_, T_, T_, T_, F_], MET, "the data subject already has the purpose information; the further information was provided before")
m.T(F133, [T_, F_, T_, F_, T_, F_], UNMET, "the further information was provided too late")
R133 = "Art 13(3) the controller must provide the data subject, prior to the further processing, with information on the other purpose and any relevant further information"
A133 = "PARTY controller DOES `Art 13(3) provide the data subject, prior to the further processing, with information on the other purpose and any relevant further information` AT %s"
m.TR(R133, [T_, "5"], "AT 0", [A133 % 4], "FULFILLED: provided before the further processing is to begin (at instant 5)")
m.TR(R133, [T_, "5"], "AT 0", [A133 % 5], "FULFILLED: provided at the instant the further processing begins (inclusive deadline: marginal reading F13-2)")
m.TR(R133, [T_, "5"], "AT 0", [A133 % 6], "BREACH: provided after the further processing began")
m.TR(R133, [T_, "5"], "AT 0", ["(WAITUNTIL 6)"], "BREACH: nothing provided by the time the further processing begins")
m.TR(R133, [F_, "5"], "AT 0", ["(WAITUNTIL 6)"], "FULFILLED: no further processing intended")
m.S("Art 13(4): where and insofar as the data subject already has the information")
m.T("Art 13(4) paragraphs 1, 2 and 3 do not apply where and insofar as the data subject already has the information", [T_], JT, "the data subject already has the information: the paragraphs 'shall not apply'")
m.T("Art 13(4) paragraphs 1, 2 and 3 do not apply where and insofar as the data subject already has the information", [F_], JF, "the data subject does not have the information: the 'where' fails, so the paragraphs apply")

# =============================================================================================== Article 14
m = Mod("14", ["prelude", "`gdpr-core`", "`P2-art-14`"], "Article 14 (src:179-205)")
MODS["14"] = m
J1a = "`Art 14(1)(a) the identity and the contact details of the controller`"
J1ar = "`Art 14(1)(a) the identity and the contact details of the controller's representative`"
J1b = "`Art 14(1)(b) the contact details of the data protection officer`"
J1cp = "`Art 14(1)(c) the purposes of the processing for which the personal data are intended`"
J1cl = "`Art 14(1)(c) the legal basis for the processing`"
J1d = "`Art 14(1)(d) the categories of personal data concerned`"
J1e = "`Art 14(1)(e) the recipients or categories of recipients of the personal data`"
J1f = "`Art 14(1)(f) the intended transfer to a recipient in a third country or international organisation and the adequacy decision or the safeguards`"
JB1 = [J1a, J1cp, J1cl, J1d]
F141 = "Art 14(1) the controller provides the data subject with the following information"
# arguments: not obtained from the data subject, paragraph 5 (b)-(d) answer, representative, officer, recipients, transfer, provided, already has
def a141(nobt=T_, exc="(JUST FALSE)", rep=F_, dpo=F_, rec=F_, tr=F_, prov=JB1, has=()):
    return [nobt, exc, rep, dpo, rec, tr, L(*prov), L(*has)]
m.S("Art 14(1): the information where the data have not been obtained from the data subject")
m.T(F141, a141(nobt=F_, prov=()), NOARISE, "the data were obtained from the data subject: 'Where personal data have not been obtained' fails")
m.T(F141, a141(exc="(JUST TRUE)", prov=()), NOARISE, "paragraph 5 (b), (c) or (d) disapplies paragraphs 1 to 4: 'shall not apply'")
m.T(F141, a141(), MET, "(a), (c), (d) provided; no representative, officer, recipients or transfer")
m.T(F141, a141(prov=[J1cp, J1cl, J1d]), UNMET, "(a) the identity and contact details of the controller not provided")
m.T(F141, a141(prov=[J1a, J1cl, J1d]), UNMET, "(c) the purposes not provided")
m.T(F141, a141(prov=[J1a, J1cp, J1d]), UNMET, "(c) the legal basis not provided")
m.T(F141, a141(prov=[J1a, J1cp, J1cl]), UNMET, "(d) the categories of personal data concerned not provided")
m.T(F141, a141(rep=T_), UNMET, "(a) 'where applicable, of the controller's representative': there is one and it was not provided")
m.T(F141, a141(rep=T_, prov=JB1 + [J1ar]), MET, "the representative provided")
m.T(F141, a141(dpo=T_), UNMET, "(b) 'where applicable': the officer's contact details not provided")
m.T(F141, a141(dpo=T_, prov=JB1 + [J1b]), MET, "(b) provided")
m.T(F141, a141(rec=T_), UNMET, "(e) 'if any': recipients exist and were not named")
m.T(F141, a141(rec=T_, prov=JB1 + [J1e]), MET, "(e) provided")
m.T(F141, a141(tr=T_), UNMET, "(f) 'where applicable': a transfer is intended and was not disclosed")
m.T(F141, a141(tr=T_, prov=JB1 + [J1f]), MET, "(f) provided")
m.T(F141, a141(has=[J1d], prov=[J1a, J1cp, J1cl]), MET, "(d) not provided but already held by the data subject (paragraph 5(a))")
m.T(F141, a141(exc="NOTHING"), MET, "paragraph 5 not answered, but every item was provided: the duty is met either way")
m.T(F141, a141(exc="NOTHING", prov=[J1a]), NO, "paragraph 5 not answered and items missing: the text does not say whether the duty was taken away")
m.T(F141, a141(exc="(JUST FALSE)", prov=[J1a]), UNMET, "paragraph 5 (b) to (d) do not apply and items are missing")
m.T(F141, a141(rep=T_, dpo=T_, rec=T_, tr=T_, prov=JB1 + [J1ar, J1b, J1e, J1f]), MET, "every point applies and every item is provided")
K2a = "`Art 14(2)(a) the period for which the personal data will be stored, or the criteria used to determine that period`"
K2b = "`Art 14(2)(b) the legitimate interests pursued by the controller or by a third party`"
K2c = "`Art 14(2)(c) the existence of the rights of access, rectification, erasure, restriction, objection and data portability`"
K2d = "`Art 14(2)(d) the existence of the right to withdraw consent at any time, without affecting the lawfulness of processing before its withdrawal`"
K2e = "`Art 14(2)(e) the right to lodge a complaint with a supervisory authority`"
K2f = "`Art 14(2)(f) the source from which the personal data originate and, if applicable, whether it came from publicly accessible sources`"
K2g = "`Art 14(2)(g) the existence of automated decision-making, including profiling, and meaningful information about the logic involved, the significance and the envisaged consequences`"
KB = [K2a, K2c, K2e, K2f]
F142 = "Art 14(2) the controller provides the data subject with the following information necessary to ensure fair and transparent processing"
# arguments: not obtained, paragraph 5 answer, point (f) of 6(1) answer, consent basis, automated decision-making, provided, already has
def a142(nobt=T_, exc="(JUST FALSE)", g6f="(JUST FALSE)", cons=F_, adm=F_, prov=KB, has=()):
    return [nobt, exc, g6f, cons, adm, L(*prov), L(*has)]
m.S("Art 14(2): the further information")
m.T(F142, a142(nobt=F_, prov=()), NO, "data obtained from the data subject: 'In addition to the information referred to in paragraph 1' is not met, the text is silent")
m.T(F142, a142(exc="(JUST TRUE)", prov=()), NOARISE, "paragraph 5 (b) to (d) disapplies paragraphs 1 to 4")
m.T(F142, a142(), MET, "(a), (c), (e), (f) provided; no point (f) basis, no consent basis, no automated decision-making")
m.T(F142, a142(prov=[K2c, K2e, K2f]), UNMET, "(a) the storage period not provided")
m.T(F142, a142(prov=[K2a, K2e, K2f]), UNMET, "(c) the existence of the rights not provided")
m.T(F142, a142(prov=[K2a, K2c, K2f]), UNMET, "(e) the right to lodge a complaint not provided")
m.T(F142, a142(prov=[K2a, K2c, K2e]), UNMET, "(f) the source not provided")
m.T(F142, a142(g6f="(JUST TRUE)"), UNMET, "(b) 'where the processing is based on point (f) of Article 6(1)': it is, and the legitimate interests were not provided")
m.T(F142, a142(g6f="(JUST TRUE)", prov=KB + [K2b]), MET, "(b) provided")
m.T(F142, a142(g6f="NOTHING"), NO, "whether point (f) applies is not answered: item (b) neither provided nor shown not to be owed")
m.T(F142, a142(g6f="NOTHING", prov=KB + [K2b]), MET, "point (f) not answered, (b) provided in any event")
m.T(F142, a142(cons=T_), UNMET, "(d) 'where processing is based on point (a) of Article 6(1) or point (a) of Article 9(2)': it is, and the right to withdraw consent was not provided")
m.T(F142, a142(cons=T_, prov=KB + [K2d]), MET, "(d) provided")
m.T(F142, a142(adm=T_), UNMET, "(g) automated decision-making referred to in Article 22(1) and (4): not provided")
m.T(F142, a142(adm=T_, prov=KB + [K2g]), MET, "(g) provided")
m.T(F142, a142(exc="NOTHING", prov=[K2a]), NO, "paragraph 5 not answered and items missing")
m.T(F142, a142(prov=[K2a, K2c, K2e], has=[K2f]), MET, "(f) not provided but already held")
m.T(F142, a142(g6f="(JUST TRUE)", cons=T_, adm=T_, prov=KB + [K2b, K2d, K2g]), MET, "every point applies and every item is provided")
FM3 = "Art 14(3) the months within which the information is to be provided"
# arguments: used for communication, months to first communication, disclosure envisaged, months to first disclosure
m.S("Art 14(3): the time limit, the earliest of the applicable limits")
m.T(FM3, [F_, "0", F_, "0"], "1", "(a) at the latest within one month: no communication and no disclosure")
m.T(FM3, [T_, "0.5", F_, "0"], "0.5", "(b) first communication after half a month: at the latest at the time of the first communication")
m.T(FM3, [T_, "2", F_, "0"], "1", "(b) first communication after two months: the limit of (a) is earlier, so one month")
m.T(FM3, [F_, "0", T_, "0.25"], "0.25", "(c) a disclosure envisaged after a quarter of a month: at the latest when first disclosed")
m.T(FM3, [T_, "0.5", T_, "0.25"], "0.25", "both: the disclosure is earlier")
m.T(FM3, [T_, "0.1", T_, "0.25"], "0.1", "both: the communication is earlier")
m.T(FM3, [T_, "0.5", T_, "3"], "0.5", "both: the disclosure is later than the communication and than one month")
m.T(FM3, [F_, "0.1", F_, "0.1"], "1", "the dates are not read where there is no communication and no disclosure")
F143 = "Art 14(3) the controller provides the information referred to in paragraphs 1 and 2 within the time that paragraph 3 requires"
# arguments: reasonable period, months to providing, used for communication, months to first communication, disclosure envisaged, months to first disclosure
m.T(F143, [T_, "1", F_, "0", F_, "0"], JT, "provided exactly one month after obtaining the data: 'at the latest within one month'")
m.T(F143, [T_, "1.5", F_, "0", F_, "0"], JF, "provided after one month and a half")
m.T(F143, [F_, "0.5", F_, "0", F_, "0"], JF, "within a month but not within 'a reasonable period ... having regard to the specific circumstances'")
m.T(F143, [T_, "0.5", T_, "0.5", F_, "0"], JT, "(b) provided at the time of the first communication")
m.T(F143, [T_, "0.6", T_, "0.5", F_, "0"], JF, "(b) provided after the first communication")
m.T(F143, [T_, "0.2", F_, "0", T_, "0.2"], JT, "(c) provided when the data are first disclosed")
m.T(F143, [T_, "0.3", F_, "0", T_, "0.2"], JF, "(c) provided after the first disclosure")
R143 = "Art 14(1) and (2) the controller must provide the data subject with the information within the time that Art 14(3) requires"
A143 = "PARTY controller DOES `Art 14(1) and (2) provide the data subject with the information that paragraphs 1 and 2 list` AT %s"
# arguments: not obtained, paragraph 5 answer, used for communication, months to first communication, disclosure envisaged, months to first disclosure
m.TR(R143, [T_, "(JUST FALSE)", F_, "0", F_, "0"], "AT 0", [A143 % 1], "FULFILLED: provided at month 1, within the month")
m.TR(R143, [T_, "(JUST FALSE)", F_, "0", F_, "0"], "AT 0", [A143 % 2], "BREACH: provided at month 2, after the month")
m.TR(R143, [T_, "(JUST FALSE)", F_, "0", F_, "0"], "AT 0", ["(WAITUNTIL 2)"], "BREACH: nothing provided within the month")
m.TR(R143, [T_, "(JUST FALSE)", T_, "0.5", F_, "0"], "AT 0", [A143 % 0.6], "BREACH: provided at month 0.6, after the first communication at 0.5")
m.TR(R143, [T_, "(JUST FALSE)", T_, "0.5", F_, "0"], "AT 0", [A143 % 0.5], "FULFILLED: provided at the time of the first communication")
m.TR(R143, [T_, "(JUST FALSE)", F_, "0", T_, "0.25"], "AT 0", ["(WAITUNTIL 0.5)"], "BREACH: a disclosure at 0.25 and nothing provided by then")
m.TR(R143, [T_, "(JUST TRUE)", F_, "0", F_, "0"], "AT 0", ["(WAITUNTIL 2)"], "FULFILLED: paragraph 5 (b) to (d) disapplies paragraphs 1 to 4")
m.TR(R143, [F_, "(JUST FALSE)", F_, "0", F_, "0"], "AT 0", ["(WAITUNTIL 2)"], "FULFILLED: the data were obtained from the data subject (Article 13)")
F144 = "Art 14(4) the controller provides the data subject, prior to the further processing, with information on the other purpose and any relevant further information"
# arguments: intends, paragraph 5 answer, provided purpose, provided further, prior, already has purpose, already has further
m.S("Art 14(4): further processing for another purpose")
m.T(F144, [F_, "(JUST FALSE)", F_, F_, F_, F_, F_], NOARISE, "no further processing intended: 'Where' fails")
m.T(F144, [T_, "(JUST TRUE)", F_, F_, F_, F_, F_], NOARISE, "paragraph 5 (b) to (d) disapplies paragraphs 1 to 4")
m.T(F144, [T_, "(JUST FALSE)", T_, T_, T_, F_, F_], MET, "both kinds provided before the further processing")
m.T(F144, [T_, "(JUST FALSE)", T_, T_, F_, F_, F_], UNMET, "provided too late")
m.T(F144, [T_, "(JUST FALSE)", F_, T_, T_, F_, F_], UNMET, "no information on the other purpose")
m.T(F144, [T_, "(JUST FALSE)", T_, F_, T_, F_, F_], UNMET, "no relevant further information")
m.T(F144, [T_, "(JUST FALSE)", F_, F_, F_, T_, T_], MET, "the data subject already has both kinds of information")
m.T(F144, [T_, "NOTHING", F_, F_, F_, F_, F_], NO, "unmet, and paragraph 5 is not answered: the text does not say")
m.T(F144, [T_, "NOTHING", T_, T_, T_, F_, F_], MET, "met whatever paragraph 5 says")
R144 = "Art 14(4) the controller must provide the data subject, prior to the further processing, with information on the other purpose and any relevant further information"
A144 = "PARTY controller DOES `Art 14(4) provide the data subject, prior to the further processing, with information on the other purpose and any relevant further information` AT %s"
m.TR(R144, [T_, "(JUST FALSE)", "5"], "AT 0", [A144 % 4], "FULFILLED: provided before the further processing begins at 5")
m.TR(R144, [T_, "(JUST FALSE)", "5"], "AT 0", [A144 % 6], "BREACH: provided after the further processing began")
m.TR(R144, [T_, "(JUST FALSE)", "5"], "AT 0", ["(WAITUNTIL 6)"], "BREACH: nothing provided by the time the further processing begins")
m.TR(R144, [T_, "(JUST TRUE)", "5"], "AT 0", ["(WAITUNTIL 6)"], "FULFILLED: paragraph 5 (b) to (d) disapplies paragraph 4")
m.TR(R144, [F_, "(JUST FALSE)", "5"], "AT 0", ["(WAITUNTIL 6)"], "FULFILLED: no further processing intended")
m.S("Art 14(5): where and insofar as paragraphs 1 to 4 do not apply")
m.T("Art 14(5)(a) paragraphs 1 to 4 do not apply where and insofar as the data subject already has the information", [T_], JT, "the data subject already has the information")
m.T("Art 14(5)(a) paragraphs 1 to 4 do not apply where and insofar as the data subject already has the information", [F_], JF, "the data subject does not have it: 'where' fails")
F145b = "Art 14(5)(b) paragraphs 1 to 4 do not apply where and insofar as the provision of the information proves impossible or would involve a disproportionate effort"
# arguments: impossible, disproportionate effort, likely to render impossible or seriously impair the objectives, research purposes subject to Article 89(1)
m.T(F145b, [T_, F_, F_, F_], JT, "the provision proves impossible")
m.T(F145b, [F_, T_, F_, F_], JT, "the provision would involve a disproportionate effort")
m.T(F145b, [F_, F_, T_, T_], JT, "the obligation is likely to render impossible or seriously impair the objectives of the processing")
m.T(F145b, [F_, F_, F_, T_], JF, "research purposes subject to Article 89(1) alone: 'in particular' gives an example, not a ground of its own")
m.T(F145b, [F_, F_, F_, F_], JF, "none of the grounds: 'where and insofar as' fails")
F145bm = "Art 14(5)(b) the controller takes appropriate measures to protect the data subject's rights and freedoms and legitimate interests, including making the information publicly available"
m.T(F145bm, ["(JUST TRUE)", T_], MET, "point (b) applies and the controller took appropriate measures")
m.T(F145bm, ["(JUST TRUE)", F_], UNMET, "point (b) applies and no measures were taken: 'In such cases the controller shall take appropriate measures'")
m.T(F145bm, ["(JUST FALSE)", T_], NO, "point (b) does not apply: 'In such cases' is not met, the text is silent")
m.T(F145bm, ["NOTHING", F_], NO, "point (b) not answered")
R145b = "Art 14(5)(b) the controller must take appropriate measures to protect the data subject's rights and freedoms and legitimate interests"
m.TR(R145b, ["(JUST TRUE)"], "AT 0", ["PARTY controller DOES `Art 14(5)(b) take appropriate measures to protect the data subject's rights and freedoms and legitimate interests, including making the information publicly available` AT 1"], "FULFILLED: the measures are taken")
m.TR(R145b, ["(JUST TRUE)"], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R145b, ["(JUST FALSE)"], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: point (b) does not apply")
F145c = "Art 14(5)(c) paragraphs 1 to 4 do not apply where and insofar as obtaining or disclosure is expressly laid down by Union or Member State law"
m.T(F145c, [T_, T_], JT, "expressly laid down by Union or Member State law to which the controller is subject, which provides appropriate measures")
m.T(F145c, [T_, F_], JF, "laid down, but the law does not provide appropriate measures: 'and which provides appropriate measures'")
m.T(F145c, [F_, T_], JF, "not laid down by such law")
m.T(F145c, [F_, F_], JF, "neither")
F145d = "Art 14(5)(d) paragraphs 1 to 4 do not apply where the personal data must remain confidential subject to an obligation of professional secrecy"
m.T(F145d, [T_], JT, "the data must remain confidential subject to professional secrecy")
m.T(F145d, [F_], JF, "no obligation of professional secrecy: 'where' fails")
F145 = "Art 14(5) points (b) to (d) disapply paragraphs 1 to 4"
m.T(F145, ["(JUST TRUE)", "(JUST FALSE)", "(JUST FALSE)"], JT, "point (b) holds")
m.T(F145, ["(JUST FALSE)", "(JUST TRUE)", "(JUST FALSE)"], JT, "point (c) holds")
m.T(F145, ["(JUST FALSE)", "(JUST FALSE)", "(JUST TRUE)"], JT, "point (d) holds")
m.T(F145, ["(JUST FALSE)", "(JUST FALSE)", "(JUST FALSE)"], JF, "none holds: 'where and insofar as' fails in each")
m.T(F145, ["(JUST FALSE)", "(JUST FALSE)", "NOTHING"], NO, "none holds and point (d) is not answered: not covered")
m.T(F145, ["NOTHING", "(JUST FALSE)", "(JUST FALSE)"], NO, "point (b) is not answered")
m.T(F145, ["NOTHING", "(JUST TRUE)", "NOTHING"], JT, "point (c) holds whatever the others are")

# =============================================================================================== Article 15
m = Mod("15", ["prelude", "`gdpr-core`", "`P2-art-15`"], "Article 15 (src:206-219)")
MODS["15"] = m
A11 = "`Art 11(2) Articles 15 to 20 are disapplied`"
F151c = "Art 15(1) the data subject has the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed"
m.S("Art 15(1): confirmation")
m.T(F151c, [T_, T_, NO], JT, "a data subject and the controller; Article 11(2) does not apply to the case")
m.T(F151c, [T_, T_, AJF], JT, "an Article 11(2) case in which the data subject provided identifying information: the articles apply again")
m.T(F151c, [T_, T_, AJT], JF, "Article 11(2) disapplies Articles 15 to 20: 'shall not apply'")
m.T(F151c, [F_, T_, NO], NO, "the person is not the data subject: the grant is to the data subject, and the text is silent about anyone else")
m.T(F151c, [T_, F_, NO], NO, "the body asked is not the controller: the right is against the controller")
F151a = "Art 15(1) the data subject has the right to obtain from the controller access to the personal data"
m.S("Art 15(1): access, 'where that is the case'")
m.T(F151a, [T_, T_, T_, NO], JT, "personal data concerning the data subject are being processed")
m.T(F151a, [T_, T_, F_, NO], JF, "no personal data are being processed: 'where that is the case' fails (ruling (b))")
m.T(F151a, [T_, T_, T_, AJT], JF, "Article 11(2) disapplies Articles 15 to 20")
m.T(F151a, [T_, T_, F_, AJT], JF, "both bars")
m.T(F151a, [F_, T_, T_, NO], NO, "not the data subject")
m.T(F151a, [T_, F_, T_, NO], NO, "not the controller")
F151i = "Art 15(1) the data subject has the right to obtain from the controller the following information"
IT = ["`Art 15(1)(a) the purposes of the processing`",
      "`Art 15(1)(b) the categories of personal data concerned`",
      "`Art 15(1)(c) the recipients or categories of recipient to whom the personal data have been or will be disclosed`",
      "`Art 15(1)(d) the envisaged period for which the personal data will be stored, or the criteria used to determine that period`",
      "`Art 15(1)(e) the existence of the right to request rectification or erasure of personal data or restriction of processing, or to object to such processing`",
      "`Art 15(1)(f) the right to lodge a complaint with a supervisory authority`",
      "`Art 15(1)(g) any available information as to the source of the personal data`",
      "`Art 15(1)(h) the existence of automated decision-making, including profiling, and meaningful information about the logic involved, the significance and the envisaged consequences`"]
# arguments: person, body, processed, item, personal data not collected from the data subject, automated decision-making exists, Article 11(2)
for i, nm in enumerate("abcdef"):
    m.T(F151i, [T_, T_, T_, IT[i], F_, F_, NO], JT, "point (%s) of paragraph 1: the right to the information, personal data being processed" % nm)
m.T(F151i, [T_, T_, T_, IT[6], T_, F_, NO], JT, "(g) the data are not collected from the data subject: any available information as to the source")
m.T(F151i, [T_, T_, T_, IT[6], F_, F_, NO], JF, "(g) the data are collected from the data subject: 'where the personal data are not collected from the data subject' fails")
m.T(F151i, [T_, T_, T_, IT[7], F_, T_, NO], JT, "(h) automated decision-making referred to in Article 22(1) and (4) exists")
m.T(F151i, [T_, T_, T_, IT[7], F_, F_, NO], NO, "(h) there is no such decision-making: nothing whose existence can be obtained; the text does not say no")
m.T(F151i, [T_, T_, F_, IT[0], F_, F_, NO], JF, "no personal data are being processed: 'where that is the case' fails, whatever the item")
m.T(F151i, [T_, T_, T_, IT[0], F_, F_, AJT], JF, "Article 11(2) disapplies Articles 15 to 20")
m.T(F151i, [F_, T_, T_, IT[0], F_, F_, NO], NO, "not the data subject")
m.T(F151i, [T_, F_, T_, IT[0], F_, F_, NO], NO, "not the controller")
F152 = "Art 15(2) the data subject has the right to be informed of the appropriate safeguards pursuant to Article 46 relating to the transfer"
m.S("Art 15(2): safeguards for a transfer")
m.T(F152, [T_, T_, T_, NO], JT, "personal data are transferred to a third country: the right to be informed of the Article 46 safeguards")
m.T(F152, [T_, T_, F_, NO], JF, "no transfer: 'Where personal data are transferred' fails (ruling (b))")
m.T(F152, [T_, T_, T_, AJT], JF, "Article 11(2) disapplies Articles 15 to 20")
m.T(F152, [F_, T_, T_, NO], NO, "not the data subject")
R151 = "Art 15(1) the controller must confirm whether personal data concerning the data subject are being processed and give access"
m.TR(R151, [NO], "AT 0", ["PARTY controller DOES `Art 15(1) confirm to the data subject whether or not personal data concerning him or her are being processed, and give access` AT 1"], "FULFILLED: the controller confirms and gives access")
m.TR(R151, [NO], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit in the text)")
m.TR(R151, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: Article 11(2) disapplies Articles 15 to 20")
F153 = "Art 15(3) the controller provides a copy of the personal data undergoing processing"
m.S("Art 15(3) and (4): the copy")
m.T(F153, [T_, T_, NO], MET, "personal data undergoing processing, copy provided")
m.T(F153, [T_, F_, NO], UNMET, "undergoing processing, no copy: 'shall provide a copy'")
m.T(F153, [F_, F_, NO], NO, "no personal data undergoing processing: nothing to copy; the text is silent")
m.T(F153, [T_, F_, AJT], NOARISE, "Article 11(2) disapplies Articles 15 to 20: 'shall not apply'")
m.T(F153, [T_, T_, AJF], MET, "an Article 11(2) case with identifying information: the article applies, and the copy was provided")
R153 = "Art 15(3) the controller must provide a copy of the personal data undergoing processing"
m.TR(R153, [T_, NO], "AT 0", ["PARTY controller DOES `Art 15(3) provide a copy of the personal data undergoing processing` AT 1"], "FULFILLED: the copy is provided")
m.TR(R153, [T_, NO], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit in the text)")
m.TR(R153, [F_, NO], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: nothing is undergoing processing")
m.TR(R153, [T_, AJT], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: Article 11(2) disapplies Articles 15 to 20")
F153f = "Art 15(3) the controller may charge a reasonable fee based on administrative costs for any further copies requested by the data subject"
m.T(F153f, [T_, T_], JT, "a further copy requested, a reasonable fee based on administrative costs")
m.T(F153f, [T_, F_], NO, "a further copy, but the fee is not reasonable or not based on costs: outside the grant")
m.T(F153f, [F_, T_], NO, "the first copy: 'any further copies' is not met; Article 12(5) answers it")
m.T(F153f, [F_, F_], NO, "neither")
F153e = "Art 15(3) the information is provided in a commonly used electronic form where the request is made by electronic means"
m.T(F153e, [T_, F_, T_], MET, "electronic request, not requested otherwise, provided in a commonly used electronic form")
m.T(F153e, [T_, F_, F_], UNMET, "electronic request, not requested otherwise, not provided electronically")
m.T(F153e, [F_, F_, F_], NOARISE, "the request is not by electronic means: 'Where' fails")
m.T(F153e, [T_, T_, F_], NOARISE, "the data subject requested otherwise: 'unless otherwise requested'")
F154 = "Art 15(4) the right to obtain a copy is limited because the copy would adversely affect the rights and freedoms of others"
m.T(F154, [T_], JT, "the copy would adversely affect the rights and freedoms of others: 'shall not adversely affect'")
m.T(F154, [F_], NO, "no adverse effect: the limit is not engaged and the paragraph is silent")

# =============================================================================================== Article 16
m = Mod("16", ["prelude", "`gdpr-core`", "`P2-art-16`"], "Article 16 (src:222-224)")
MODS["16"] = m
F16a = "Art 16 the data subject has the right to obtain from the controller the rectification of inaccurate personal data concerning him or her"
m.S("Art 16 first sentence: rectification of inaccurate data")
m.T(F16a, [T_, T_, T_, NO], JT, "inaccurate personal data, a data subject and the controller")
m.T(F16a, [T_, T_, F_, NO], NO, "the data are accurate: outside 'inaccurate personal data'; the text does not say no")
m.T(F16a, [T_, T_, T_, AJT], JF, "Article 11(2) disapplies Articles 15 to 20 (Article 16 is among them)")
m.T(F16a, [T_, T_, T_, AJF], JT, "an Article 11(2) case with identifying information: the right applies")
m.T(F16a, [F_, T_, T_, NO], NO, "not the data subject")
m.T(F16a, [T_, F_, T_, NO], NO, "not the controller")
F16b = "Art 16 the data subject has the right to have incomplete personal data completed"
# arguments: person, body, incomplete, completion called for by the purposes, supplementary statement provided, Article 11(2)
m.S("Art 16 second sentence: completion, taking into account the purposes")
m.T(F16b, [T_, T_, T_, T_, F_, NO], JT, "incomplete data, completion called for by the purposes")
m.T(F16b, [T_, T_, T_, T_, T_, NO], JT, "a supplementary statement is provided: 'including by means of providing a supplementary statement' is an example, not a condition")
m.T(F16b, [T_, T_, T_, F_, F_, NO], NO, "incomplete, but the purposes do not call for completion: outside the grant")
m.T(F16b, [T_, T_, F_, T_, F_, NO], NO, "the data are complete")
m.T(F16b, [T_, T_, T_, T_, F_, AJT], JF, "Article 11(2) disapplies Articles 15 to 20")
m.T(F16b, [F_, T_, T_, T_, F_, NO], NO, "not the data subject")
R16 = "Art 16 the controller must rectify the inaccurate personal data without undue delay"
m.TR(R16, [T_, NO], "AT 0", ["PARTY controller DOES `Art 16 rectify the inaccurate personal data concerning the data subject without undue delay` AT 1"], "FULFILLED: the controller rectifies")
m.TR(R16, [T_, NO], "AT 0", ["(WAITUNTIL 1000)"], "no act, a long time later: the obligation stands; 'without undue delay' is not a number, so nothing breaches")
m.TR(R16, [F_, NO], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: no inaccurate data")
m.TR(R16, [T_, AJT], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: Article 11(2) disapplies Articles 15 to 20")

# =============================================================================================== Article 17
m = Mod("17", ["prelude", "`gdpr-core`", "`P2-art-17`"], "Article 17 (src:225-240)")
MODS["17"] = m
P17 = {"a": "Art 17(1)(a) point (a) applies: the personal data are no longer necessary in relation to the purposes for which they were collected or otherwise processed",
       "b": "Art 17(1)(b) point (b) applies: the data subject withdraws consent and there is no other legal ground for the processing",
       "c": "Art 17(1)(c) point (c) applies: the data subject objects to the processing and there are no overriding legitimate grounds for it, or the objection is under Article 21(2)",
       "d": "Art 17(1)(d) point (d) applies: the personal data have been unlawfully processed",
       "e": "Art 17(1)(e) point (e) applies: the personal data have to be erased for compliance with a legal obligation in Union or Member State law",
       "f": "Art 17(1)(f) point (f) applies: the personal data have been collected in relation to the offer of information society services referred to in Article 8(1)"}
m.S("Art 17(1)(a) to (f): the six grounds")
m.T(P17["a"], [T_], JT, "(a) no longer necessary for the purposes")
m.T(P17["a"], [F_], JF, "(a) still necessary: 'where one of the following grounds applies' fails")
m.T(P17["b"], [T_, F_], JT, "(b) consent withdrawn, no other legal ground")
m.T(P17["b"], [T_, T_], JF, "(b) consent withdrawn but there is another legal ground: 'where there is no other legal ground' fails")
m.T(P17["b"], [F_, F_], JF, "(b) no withdrawal")
m.T(P17["b"], [F_, T_], JF, "(b) no withdrawal, another ground")
m.T(P17["c"], [T_, F_, F_], JT, "(c) objection under Article 21(1), no overriding legitimate grounds")
m.T(P17["c"], [T_, T_, F_], JF, "(c) objection under Article 21(1) but overriding legitimate grounds exist")
m.T(P17["c"], [F_, F_, T_], JT, "(c) objection under Article 21(2) (direct marketing): no test of overriding grounds")
m.T(P17["c"], [T_, T_, T_], JT, "(c) overriding grounds exist, but the objection is also under Article 21(2)")
m.T(P17["c"], [F_, F_, F_], JF, "(c) no objection")
m.T(P17["d"], [T_], JT, "(d) unlawfully processed")
m.T(P17["d"], [F_], JF, "(d) lawfully processed")
m.T(P17["e"], [T_], JT, "(e) erasure required by Union or Member State law")
m.T(P17["e"], [F_], JF, "(e) no such legal obligation")
m.T(P17["f"], [T_], JT, "(f) collected in relation to the offer of information society services to a child (Article 8(1))")
m.T(P17["f"], [F_], JF, "(f) not so collected")
X17 = {"a": "Art 17(3)(a) paragraphs 1 and 2 do not apply to the extent that processing is necessary for exercising the right of freedom of expression and information",
       "b": "Art 17(3)(b) paragraphs 1 and 2 do not apply to the extent that processing is necessary for compliance with a legal obligation or for a task in the public interest",
       "c": "Art 17(3)(c) paragraphs 1 and 2 do not apply to the extent that processing is necessary for reasons of public interest in the area of public health",
       "d": "Art 17(3)(d) paragraphs 1 and 2 do not apply to the extent that processing is necessary for archiving, research or statistical purposes",
       "e": "Art 17(3)(e) paragraphs 1 and 2 do not apply to the extent that processing is necessary for the establishment, exercise or defence of legal claims"}
m.S("Art 17(3)(a) to (e): the five exceptions")
m.T(X17["a"], [T_], JT, "(a) necessary for exercising freedom of expression and information")
m.T(X17["a"], [F_], JF, "(a) not necessary for that")
m.T(X17["b"], [T_, F_], JT, "(b) necessary for compliance with a legal obligation")
m.T(X17["b"], [F_, T_], JT, "(b) necessary for a task in the public interest or official authority")
m.T(X17["b"], [F_, F_], JF, "(b) neither")
X17c = [T_, AJT, AJT, AJT]
m.T(X17["c"], [T_, AJT, AJT, AJT], JT, "(c) public health reasons, in accordance with points (h) and (i) of Article 9(2) and Article 9(3)")
m.T(X17["c"], [T_, AJT, AJT, AJF], JF, "(c) Article 9(3) not met")
m.T(X17["c"], [T_, AJF, AJT, AJT], JF, "(c) point (h) not met")
m.T(X17["c"], [T_, AJT, AJF, AJT], JF, "(c) point (i) not met")
m.T(X17["c"], [T_, AJT, "NOTHING", AJT], NO, "(c) point (i) not decided, none failed: not covered")
m.T(X17["c"], [T_, AJF, "NOTHING", AJT], JF, "(c) point (h) fails: fails whatever (i) is")
m.T(X17["c"], [F_, AJT, AJT, AJT], JF, "(c) not necessary for public health reasons")
m.T(X17["d"], [T_, T_, T_], JT, "(d) archiving, research or statistical purposes in accordance with Article 89(1), and the right is likely to render impossible or seriously impair the objectives")
m.T(X17["d"], [T_, F_, T_], JF, "(d) not in accordance with Article 89(1)")
m.T(X17["d"], [T_, T_, F_], JF, "(d) the right would not impair the objectives: 'in so far as' fails")
m.T(X17["d"], [F_, T_, T_], JF, "(d) not for those purposes")
m.T(X17["e"], [T_], JT, "(e) legal claims")
m.T(X17["e"], [F_], JF, "(e) no legal claims")
F173 = "Art 17(3) paragraphs 1 and 2 do not apply"
m.T(F173, [AJT, AJF, AJF, AJF, AJF], JT, "exception (a) holds")
m.T(F173, [AJF, AJF, AJF, AJF, AJT], JT, "exception (e) holds")
m.T(F173, [AJF, AJF, AJF, AJF, AJF], JF, "no exception holds")
m.T(F173, [AJF, AJF, AJF, AJF, "NOTHING"], NO, "no exception holds and (e) is not decided")
m.T(F173, ["NOTHING", AJT, "NOTHING", AJF, AJF], JT, "one exception holds whatever the others are")
F171 = "Art 17(1) the data subject has the right to obtain from the controller the erasure of personal data concerning him or her and the controller has the obligation to erase them"
# arguments: person, body, grounds (a) to (f), Article 17(3), Article 11(2)
def a171(per=T_, bod=T_, g=(AJF,)*6, x3=AJF, a11=NO):
    return [per, bod] + list(g) + [x3, a11]
m.S("Art 17(1): the right to erasure and the obligation to erase")
m.T(F171, a171(g=(AJT, AJF, AJF, AJF, AJF, AJF)), JT, "ground (a) holds, no exception")
m.T(F171, a171(g=(AJF, AJF, AJF, AJT, AJF, AJF)), JT, "ground (d) holds, no exception")
m.T(F171, a171(g=(AJF, AJF, AJF, AJF, AJF, AJT)), JT, "ground (f) holds, no exception")
m.T(F171, a171(g=(AJT, AJT, AJT, AJT, AJT, AJT)), JT, "all six grounds hold")
m.T(F171, a171(), JF, "no ground holds: 'where one of the following grounds applies' fails")
m.T(F171, a171(g=(AJT, AJF, AJF, AJF, AJF, AJF), x3=AJT), JF, "a ground holds, but paragraph 3 disapplies paragraphs 1 and 2")
m.T(F171, a171(g=(AJT, AJF, AJF, AJF, AJF, AJF), x3="NOTHING"), NO, "a ground holds, and whether paragraph 3 applies is not decided: not covered")
m.T(F171, a171(g=(AJT, "NOTHING", AJF, AJF, AJF, AJF), x3=AJF), JT, "ground (a) holds, (b) is not decided, no exception: the right exists")
m.T(F171, a171(g=("NOTHING", AJF, AJF, AJF, AJF, AJF)), NO, "no ground holds, one is not decided: not covered")
m.T(F171, a171(g=(AJT, AJF, AJF, AJF, AJF, AJF), a11=AJT), JF, "Article 11(2) disapplies Articles 15 to 20 (Article 17 is among them)")
m.T(F171, a171(g=(AJT, AJF, AJF, AJF, AJF, AJF), a11=AJF), JT, "an Article 11(2) case with identifying information: the right applies")
m.T(F171, a171(per=F_, g=(AJT, AJF, AJF, AJF, AJF, AJF)), NO, "not the data subject")
m.T(F171, a171(bod=F_, g=(AJT, AJF, AJF, AJF, AJF, AJF)), NO, "not the controller")
R171 = "Art 17(1) the controller must erase the personal data without undue delay"
m.TR(R171, [AJT], "AT 0", ["PARTY controller DOES `Art 17(1) erase the personal data without undue delay` AT 1"], "FULFILLED: the controller erases")
m.TR(R171, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; 'without undue delay' is not a number, so nothing breaches")
m.TR(R171, [AJF], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: no right to erasure")
m.TR(R171, ["NOTHING"], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: the right is not established (not covered), so the rule creates no standing duty")
F172 = "Art 17(2) the controller takes reasonable steps, including technical measures, to inform controllers which are processing the personal data that the data subject has requested the erasure of any links to, or copy or replication of, those personal data"
# arguments: made public, obliged pursuant to paragraph 1, Article 17(3), reasonable steps taken
m.S("Art 17(2): informing the controllers that process the data")
m.T(F172, [T_, AJT, AJF, T_], MET, "made public, obliged to erase, reasonable steps taken")
m.T(F172, [T_, AJT, AJF, F_], UNMET, "made public, obliged to erase, no steps: 'shall take reasonable steps'")
m.T(F172, [F_, AJT, AJF, F_], NOARISE, "not made public: 'Where the controller has made the personal data public' fails")
m.T(F172, [T_, AJF, AJF, F_], NOARISE, "made public but not obliged to erase: 'and is obliged pursuant to paragraph 1' fails")
m.T(F172, [T_, AJT, AJT, F_], NOARISE, "paragraph 3 disapplies paragraphs 1 and 2")
m.T(F172, [T_, "NOTHING", AJF, F_], NO, "whether the controller is obliged is not decided")
m.T(F172, [T_, AJT, "NOTHING", F_], NO, "no steps and paragraph 3 is not decided: not covered")
m.T(F172, [T_, AJT, "NOTHING", T_], MET, "steps taken: met whatever paragraph 3 says")
R172 = "Art 17(2) the controller must take reasonable steps to inform the controllers which are processing the personal data"
m.TR(R172, [T_, AJT, AJF], "AT 0", ["PARTY controller DOES `Art 17(2) take reasonable steps, including technical measures, to inform the controllers which are processing the personal data of the erasure request` AT 1"], "FULFILLED: the steps are taken")
m.TR(R172, [T_, AJT, AJF], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R172, [F_, AJT, AJF], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: the data were not made public")

# =============================================================================================== Article 18
m = Mod("18", ["prelude", "`gdpr-core`", "`P2-art-18`"], "Article 18 (src:241-249)")
MODS["18"] = m
Q18 = {"a": "Art 18(1)(a) point (a) applies: the accuracy of the personal data is contested, for a period enabling the controller to verify the accuracy",
       "b": "Art 18(1)(b) point (b) applies: the processing is unlawful and the data subject opposes erasure and requests restriction instead",
       "c": "Art 18(1)(c) point (c) applies: the controller no longer needs the personal data but the data subject requires them for legal claims",
       "d": "Art 18(1)(d) point (d) applies: the data subject has objected pursuant to Article 21(1) pending the verification whether the controller's grounds override"}
m.S("Art 18(1)(a) to (d): the four points")
m.T(Q18["a"], [T_, T_], JT, "(a) accuracy contested, for a period enabling verification")
m.T(Q18["a"], [T_, F_], JF, "(a) contested, but the period enabling verification has ended")
m.T(Q18["a"], [F_, T_], JF, "(a) accuracy not contested")
m.T(Q18["b"], [T_, T_, T_], JT, "(b) unlawful, the data subject opposes erasure and requests restriction instead")
m.T(Q18["b"], [T_, T_, F_], JF, "(b) the data subject does not request restriction")
m.T(Q18["b"], [T_, F_, T_], JF, "(b) the data subject does not oppose erasure")
m.T(Q18["b"], [F_, T_, T_], JF, "(b) the processing is lawful")
m.T(Q18["c"], [T_, T_], JT, "(c) no longer needed by the controller, required by the data subject for legal claims")
m.T(Q18["c"], [T_, F_], JF, "(c) not required by the data subject for legal claims")
m.T(Q18["c"], [F_, T_], JF, "(c) the controller still needs the data")
m.T(Q18["d"], [T_, T_], JT, "(d) objected pursuant to Article 21(1), verification pending")
m.T(Q18["d"], [T_, F_], JF, "(d) objected, but the verification is complete")
m.T(Q18["d"], [F_, T_], JF, "(d) no objection")
F181 = "Art 18(1) the data subject has the right to obtain from the controller restriction of processing"
# arguments: person, body, points (a) to (d), Article 11(2)
m.T(F181, [T_, T_, AJT, AJF, AJF, AJF, NO], JT, "point (a) holds")
m.T(F181, [T_, T_, AJF, AJT, AJF, AJF, NO], JT, "point (b) holds")
m.T(F181, [T_, T_, AJF, AJF, AJT, AJF, NO], JT, "point (c) holds")
m.T(F181, [T_, T_, AJF, AJF, AJF, AJT, NO], JT, "point (d) holds")
m.T(F181, [T_, T_, AJF, AJF, AJF, AJF, NO], JF, "no point holds: 'where one of the following applies' fails")
m.T(F181, [T_, T_, AJF, AJF, AJF, "NOTHING", NO], NO, "no point holds and (d) is not decided: not covered")
m.T(F181, [T_, T_, "NOTHING", AJT, AJF, AJF, NO], JT, "(b) holds whatever (a) is")
m.T(F181, [T_, T_, AJT, AJF, AJF, AJF, AJT], JF, "Article 11(2) disapplies Articles 15 to 20 (Article 18 is among them)")
m.T(F181, [T_, T_, AJT, AJF, AJF, AJF, AJF], JT, "an Article 11(2) case with identifying information: the right applies")
m.T(F181, [F_, T_, AJT, AJF, AJF, AJF, NO], NO, "not the data subject")
m.T(F181, [T_, F_, AJT, AJF, AJF, AJF, NO], NO, "not the controller")
F182 = "Art 18(2) the restricted personal data are processed, with the exception of storage, only with the data subject's consent or for one of the three purposes that paragraph 2 names"
# arguments: restricted, storage, consent, legal claims, rights of another person, important public interest
m.S("Art 18(2): processing of restricted data")
m.T(F182, [T_, T_, F_, F_, F_, F_], MET, "restricted data, storage only: 'with the exception of storage'")
m.T(F182, [T_, F_, T_, F_, F_, F_], MET, "with the data subject's consent")
m.T(F182, [T_, F_, F_, T_, F_, F_], MET, "for the establishment, exercise or defence of legal claims")
m.T(F182, [T_, F_, F_, F_, T_, F_], MET, "for the protection of the rights of another natural or legal person")
m.T(F182, [T_, F_, F_, F_, F_, T_], MET, "for reasons of important public interest of the Union or of a Member State")
m.T(F182, [T_, F_, F_, F_, F_, F_], UNMET, "any other processing of restricted data: the list is closed with 'only'")
m.T(F182, [F_, F_, F_, F_, F_, F_], NOARISE, "the processing has not been restricted: 'Where processing has been restricted' fails")
F183 = "Art 18(3) the controller informs the data subject who has obtained restriction of processing before the restriction is lifted"
m.S("Art 18(3): informing the data subject before the restriction is lifted")
m.T(F183, [T_, T_], MET, "informed before the restriction was lifted")
m.T(F183, [T_, F_], UNMET, "not informed before: 'shall be informed by the controller before'")
m.T(F183, [F_, T_], NO, "no restriction obtained under paragraph 1: outside 'A data subject who has obtained restriction'")
R183 = "Art 18(3) the controller must inform the data subject before the restriction of processing is lifted"
A183 = "PARTY controller DOES `Art 18(3) inform the data subject before the restriction of processing is lifted` AT %s"
m.TR(R183, [T_, "5"], "AT 0", [A183 % 4], "FULFILLED: informed before the restriction is lifted at 5")
m.TR(R183, [T_, "5"], "AT 0", [A183 % 6], "BREACH: informed after the restriction was lifted")
m.TR(R183, [T_, "5"], "AT 0", ["(WAITUNTIL 6)"], "BREACH: not informed by the time the restriction is lifted")
m.TR(R183, [F_, "5"], "AT 0", ["(WAITUNTIL 6)"], "FULFILLED: no restriction obtained")

# =============================================================================================== Article 19
m = Mod("19", ["prelude", "`gdpr-core`", "`gdpr-core-2`", "`gdpr-definitions-2`", "`P2-art-19`"], "Article 19 (src:250-252)")
MODS["19"] = m
F191 = "Art 19 the controller communicates any rectification, erasure or restriction of processing to each recipient to whom the personal data have been disclosed"
# arguments: change carried out, body, disclosed to the body, the body is a third party, received in a particular inquiry, receipt in accordance with law, impossible or disproportionate, communicated, Article 11(2)
def a191(done=T_, body="`legal person`", disc=T_, third=F_, inq=F_, law=F_, imp=F_, comm=F_, a11=NO):
    return [done, body, disc, third, inq, law, imp, comm, a11]
m.S("Art 19, first sentence: communicate to each recipient, unless impossible or disproportionate")
m.T(F191, a191(comm=T_), MET, "a rectification carried out, a recipient (a legal person to whom the data were disclosed), communicated")
m.T(F191, a191(comm=F_), UNMET, "not communicated: 'shall communicate'")
m.T(F191, a191(third=T_), UNMET, "the recipient is a third party: 'whether a third party or not' (Article 4(9)), so still a recipient")
m.T(F191, a191(imp=T_), NOARISE, "communicating proves impossible or involves disproportionate effort: 'unless'")
m.T(F191, a191(done=F_), NO, "no rectification, erasure or restriction carried out: nothing to communicate; the text is silent")
m.T(F191, a191(disc=F_), NO, "the data were not disclosed to the body: it is not a recipient (Article 4(9)), outside 'each recipient'")
m.T(F191, a191(body="`public authority`", inq=T_, law=T_), NO, "a public authority that receives the data in a particular inquiry in accordance with law is 'not regarded as a recipient' (Article 4(9))")
m.T(F191, a191(body="`public authority`", inq=T_, law=F_), UNMET, "a public authority in an inquiry NOT in accordance with law is a recipient")
m.T(F191, a191(body="`not a person or body`"), NO, "a body that is not a natural or legal person, public authority, agency or other body is not a recipient")
m.T(F191, a191(a11=AJT), NOARISE, "Article 11(2) disapplies Articles 15 to 20 (Article 19 is among them)")
m.T(F191, a191(comm=T_, a11=AJF), MET, "an Article 11(2) case with identifying information: the article applies; communicated")
R191 = "Art 19 the controller must communicate the rectification, erasure or restriction of processing to each recipient"
m.TR(R191, [T_], "AT 0", ["PARTY controller DOES `Art 19 communicate the rectification, erasure or restriction of processing to each recipient to whom the personal data have been disclosed` AT 1"], "FULFILLED: the controller communicates")
m.TR(R191, [T_], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R191, [F_], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: no duty to communicate arises")
F192 = "Art 19 the controller informs the data subject about those recipients if the data subject requests it"
m.S("Art 19, second sentence: informing the data subject about the recipients")
m.T(F192, [T_, T_, NO], MET, "requested, and the controller informed the data subject")
m.T(F192, [T_, F_, NO], UNMET, "requested, and not informed: 'shall inform'")
m.T(F192, [F_, F_, NO], NOARISE, "not requested: 'if the data subject requests it' fails")
m.T(F192, [F_, T_, NO], NOARISE, "not requested, informed in any case: the duty did not arise")
m.T(F192, [T_, F_, AJT], NOARISE, "Article 11(2) disapplies Articles 15 to 20 (Article 19 is among them): no duty to inform, whatever the controller did (R9)")
m.T(F192, [T_, F_, AJF], UNMET, "an Article 11(2) case with identifying information: the article applies; requested and not informed")
m.T(F192, [T_, T_, AJF], MET, "an Article 11(2) case with identifying information: requested and informed")
R192 = "Art 19 the controller must inform the data subject about those recipients if the data subject requests it"
m.TR(R192, [T_, NO], "AT 0", ["PARTY controller DOES `Art 19 inform the data subject about those recipients` AT 1"], "FULFILLED: the controller informs")
m.TR(R192, [T_, NO], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R192, [F_, NO], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: no request")
m.TR(R192, [T_, AJT], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: Article 11(2) disapplies Articles 15 to 20, so there is no duty to inform (R9)")

# =============================================================================================== Article 20
m = Mod("20", ["prelude", "`gdpr-core`", "`P2-art-20`"], "Article 20 (src:253-260)")
MODS["20"] = m
F201 = "Art 20(1) the data subject has the right to receive the personal data concerning him or her which he or she has provided to a controller, in a structured, commonly used and machine-readable format"
F201t = "Art 20(1) the data subject has the right to transmit those data to another controller without hindrance from the controller to which the personal data have been provided"
# arguments: person, body, provided by the data subject, based on consent, Article 6(1)(b) answer, automated means, necessary for a public-interest task, Article 11(2)
def a201(per=T_, bod=T_, prov=T_, cons=T_, ctr=AJF, aut=T_, pub=F_, a11=NO):
    return [per, bod, prov, cons, ctr, aut, pub, a11]
m.S("Art 20(1): the right to receive and the right to transmit")
for fn, which in ((F201, "receive"), (F201t, "transmit")):
    m.T(fn, a201(), JT, "(%s) consent-based, automated, provided by the data subject" % which)
    m.T(fn, a201(cons=F_, ctr=AJT), JT, "(%s) based on a contract pursuant to point (b) of Article 6(1)" % which)
    m.T(fn, a201(cons=F_, ctr=AJF), JF, "(%s) based on neither consent nor contract: 'where: (a)' fails" % which)
    m.T(fn, a201(cons=F_, ctr="NOTHING"), NO, "(%s) not on consent and the contract basis is not decided: not covered" % which)
    m.T(fn, a201(cons=T_, ctr="NOTHING"), JT, "(%s) consent-based: the contract limb is not needed" % which)
    m.T(fn, a201(aut=F_), JF, "(%s) not carried out by automated means: 'where: ... (b)' fails" % which)
    m.T(fn, a201(pub=T_), JF, "(%s) the processing is necessary for a task in the public interest: 'That right shall not apply'" % which)
    m.T(fn, a201(prov=F_), NO, "(%s) data the data subject did not provide: outside the grant" % which)
    m.T(fn, a201(a11=AJT), JF, "(%s) Article 11(2) disapplies Articles 15 to 20" % which)
    m.T(fn, a201(a11=AJF), JT, "(%s) an Article 11(2) case with identifying information: the right applies" % which)
    m.T(fn, a201(per=F_), NO, "(%s) not the data subject" % which)
    m.T(fn, a201(bod=F_), NO, "(%s) not the controller" % which)
R201 = "Art 20(1) the controller shall not hinder the transmission of the personal data to another controller"
m.TR(R201, [AJT], "AT 0", ["PARTY controller DOES `Art 20(1) hinder the transmission of the personal data to another controller` AT 1"], "BREACH: the controller hinders a transmission the data subject has the right to make (the act is the breach)")
m.TR(R201, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no hindrance: the prohibition stands, unbroken")
m.TR(R201, [AJF], "AT 0", ["PARTY controller DOES `Art 20(1) hinder the transmission of the personal data to another controller` AT 1"], "FULFILLED: no right to transmit on these facts, so hindering is not barred by this paragraph")
m.TR(R201, ["NOTHING"], "AT 0", ["PARTY controller DOES `Art 20(1) hinder the transmission of the personal data to another controller` AT 1"], "FULFILLED: the right is not established (not covered), so the rule creates no bar")
F202 = "Art 20(2) the data subject has the right to have the personal data transmitted directly from one controller to another, where technically feasible"
# arguments: person, body, exercises the right under paragraph 1, technically feasible, Article 11(2)
m.S("Art 20(2): direct transmission, where technically feasible")
m.T(F202, [T_, T_, T_, T_, NO], JT, "in exercising the right of paragraph 1, technically feasible")
m.T(F202, [T_, T_, T_, F_, NO], JF, "not technically feasible: 'where technically feasible' fails")
m.T(F202, [T_, T_, F_, T_, NO], NO, "not in exercising the right of paragraph 1: outside the sentence")
m.T(F202, [T_, T_, T_, T_, AJT], JF, "Article 11(2) disapplies Articles 15 to 20")
m.T(F202, [F_, T_, T_, T_, NO], NO, "not the data subject")
m.S("Art 20(3) and (4): the limits")
F203a = "Art 20(3) the exercise of the right referred to in paragraph 1 prejudices the right to erasure under Article 17"
m.T(F203a, [T_], JF, "the exercise of the right is 'without prejudice to Article 17'")
m.T(F203a, [F_], NO, "no exercise of the right: outside the sentence")
F203b = "Art 20(3) the right to data portability does not apply to processing necessary for the performance of a task carried out in the public interest or in the exercise of official authority"
m.T(F203b, [T_], JT, "processing necessary for a task in the public interest or official authority: 'That right shall not apply'")
m.T(F203b, [F_], NO, "other processing: outside the sentence")
F204 = "Art 20(4) the right referred to in paragraph 1 is limited because its exercise would adversely affect the rights and freedoms of others"
m.T(F204, [T_], JT, "the exercise would adversely affect the rights and freedoms of others: 'shall not adversely affect'")
m.T(F204, [F_], NO, "no adverse effect: the limit is not engaged and the paragraph is silent")

# =============================================================================================== Article 21
m = Mod("21", ["prelude", "`gdpr-core`", "`P2-art-21`"], "Article 21 (src:263-270)")
MODS["21"] = m
G6e = "Art 6(1)(e) point (e) applies: the processing is necessary for a task in the public interest or in the exercise of official authority vested in the controller"
F211 = "Art 21(1) the data subject has the right to object, on grounds relating to his or her particular situation, to processing which is based on point (e) or (f) of Article 6(1)"
# arguments: person, body, grounds relating to the particular situation, point (e) answer, point (f) answer
m.S("Art 21(1): the right to object to processing based on point (e) or (f)")
m.T(F211, [T_, T_, T_, AJT, AJF], JT, "processing based on point (e), objection on grounds of the particular situation")
m.T(F211, [T_, T_, T_, AJF, AJT], JT, "processing based on point (f)")
m.T(F211, [T_, T_, T_, "NOTHING", AJT], JT, "point (f) holds whatever (e) is")
m.T(F211, [T_, T_, T_, AJF, AJF], NO, "processing on another basis: outside 'which is based on point (e) or (f)'; the text does not say no")
m.T(F211, [T_, T_, T_, "NOTHING", AJF], NO, "neither holds and (e) is not decided: not covered")
m.T(F211, [T_, T_, F_, AJT, AJF], NO, "an objection not on grounds relating to the particular situation: outside the grant")
m.T(F211, [F_, T_, T_, AJT, AJF], NO, "not the data subject")
m.T(F211, [T_, F_, T_, AJT, AJF], NO, "not the controller")
F211b = "Art 21(1) the controller shall no longer process the personal data unless the controller demonstrates compelling legitimate grounds"
# arguments: the data subject has objected, compelling legitimate grounds that override, compelling legitimate grounds for legal claims
m.T(F211b, [T_, F_, F_], JT, "objected, and the controller demonstrates no compelling grounds: it shall no longer process")
m.T(F211b, [T_, T_, F_], JF, "compelling legitimate grounds that override the interests of the data subject: 'unless'")
m.T(F211b, [T_, F_, T_], JF, "compelling legitimate grounds for legal claims: 'unless'")
m.T(F211b, [T_, T_, T_], JF, "both")
m.T(F211b, [F_, F_, F_], NO, "no objection: the sentence follows an objection and the text is silent otherwise")
R211 = "Art 21(1) the controller must no longer process the personal data after the objection"
m.TR(R211, [AJT], "AT 0", ["PARTY controller DOES `Art 21(1) process the personal data after the objection` AT 1"], "BREACH: processing after the objection, with no compelling grounds (the act is the breach)")
m.TR(R211, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no further processing: the prohibition stands, unbroken")
m.TR(R211, [AJF], "AT 0", ["PARTY controller DOES `Art 21(1) process the personal data after the objection` AT 1"], "FULFILLED: the controller demonstrates compelling grounds, so the bar does not stand")
m.TR(R211, ["NOTHING"], "AT 0", ["PARTY controller DOES `Art 21(1) process the personal data after the objection` AT 1"], "FULFILLED: no objection (not covered), so the rule creates no bar")
F212 = "Art 21(2) the data subject has the right to object at any time to processing of personal data concerning him or her for direct marketing"
m.S("Art 21(2) and (3): direct marketing")
m.T(F212, [T_, T_, T_], JT, "personal data processed for direct marketing purposes")
m.T(F212, [T_, T_, F_], JF, "not processed for direct marketing: 'Where' fails")
m.T(F212, [F_, T_, T_], NO, "not the data subject")
m.T(F212, [T_, F_, T_], NO, "not the controller")
F213 = "Art 21(3) the personal data shall no longer be processed for direct marketing purposes"
m.T(F213, [T_], JT, "the data subject objects to processing for direct marketing: the data shall no longer be processed for those purposes")
m.T(F213, [F_], JF, "no objection: 'Where the data subject objects' fails")
R213 = "Art 21(3) the controller must no longer process the personal data for direct marketing purposes after the objection"
m.TR(R213, [T_], "AT 0", ["PARTY controller DOES `Art 21(3) process the personal data for direct marketing purposes after the objection` AT 1"], "BREACH: direct marketing after the objection")
m.TR(R213, [T_], "AT 0", ["(WAITUNTIL 1000)"], "no direct marketing: the prohibition stands, unbroken")
m.TR(R213, [F_], "AT 0", ["PARTY controller DOES `Art 21(3) process the personal data for direct marketing purposes after the objection` AT 1"], "FULFILLED: no objection")
F214 = "Art 21(4) the right to object is explicitly brought to the attention of the data subject, clearly and separately, at the latest at the time of the first communication"
m.S("Art 21(4) to (6)")
m.T(F214, [T_, T_, T_], JT, "explicitly brought to the attention, presented clearly and separately, at the time of the first communication")
m.T(F214, [T_, T_, F_], JF, "not at the latest at the time of the first communication")
m.T(F214, [T_, F_, T_], JF, "not presented clearly and separately")
m.T(F214, [F_, T_, T_], JF, "not explicitly brought to the attention")
F215 = "Art 21(5) the data subject may exercise the right to object by automated means using technical specifications"
m.T(F215, [T_], JT, "in the context of the use of information society services")
m.T(F215, [F_], NO, "another context: outside the grant")
F216 = "Art 21(6) the data subject has the right to object to processing for scientific or historical research purposes or statistical purposes"
# arguments: person, body, purpose of the processing, pursuant to Article 89(1), grounds relating to the particular situation, necessary for a task for reasons of public interest
m.T(F216, [T_, T_, "`Art 5(1)(b) scientific research purposes`", T_, T_, F_], JT, "scientific research purposes pursuant to Article 89(1)")
m.T(F216, [T_, T_, "`Art 5(1)(b) historical research purposes`", T_, T_, F_], JT, "historical research purposes")
m.T(F216, [T_, T_, "`Art 5(1)(b) statistical purposes`", T_, T_, F_], JT, "statistical purposes")
m.T(F216, [T_, T_, "`Art 5(1)(b) archiving purposes in the public interest`", T_, T_, F_], JF, "archiving purposes in the public interest are not on the list: 'Where' fails")
m.T(F216, [T_, T_, "`Art 5(1)(b) some other purpose`", T_, T_, F_], JF, "another purpose: 'Where' fails")
m.T(F216, [T_, T_, "`Art 5(1)(b) scientific research purposes`", F_, T_, F_], JF, "research purposes but not pursuant to Article 89(1)")
m.T(F216, [T_, T_, "`Art 5(1)(b) scientific research purposes`", T_, F_, F_], NO, "an objection not on grounds relating to the particular situation: outside the grant")
m.T(F216, [T_, T_, "`Art 5(1)(b) scientific research purposes`", T_, T_, T_], JF, "the processing is necessary for a task for reasons of public interest: 'unless'")
m.T(F216, [F_, T_, "`Art 5(1)(b) scientific research purposes`", T_, T_, F_], NO, "not the data subject")

# =============================================================================================== Article 22
m = Mod("22", ["prelude", "`gdpr-core`", "`P2-art-22`"], "Article 22 (src:271-279)")
MODS["22"] = m
W22 = {"a": "Art 22(2)(a) point (a) applies: the decision is necessary for entering into, or performance of, a contract between the data subject and a data controller",
       "b": "Art 22(2)(b) point (b) applies: the decision is authorised by Union or Member State law which also lays down suitable measures",
       "c": "Art 22(2)(c) point (c) applies: the decision is based on the data subject's explicit consent"}
m.S("Art 22(2)(a) to (c): the three points")
m.T(W22["a"], [T_], JT, "(a) necessary for entering into or performing a contract between the data subject and a controller")
m.T(W22["a"], [F_], JF, "(a) not necessary: 'if' fails")
m.T(W22["b"], [T_, T_], JT, "(b) authorised by law which also lays down suitable measures")
m.T(W22["b"], [T_, F_], JF, "(b) authorised, but the law lays down no suitable measures: 'and which also lays down'")
m.T(W22["b"], [F_, T_], JF, "(b) not authorised by law")
m.T(W22["c"], [T_], JT, "(c) based on the data subject's explicit consent")
m.T(W22["c"], [F_], JF, "(c) no explicit consent")
F222 = "Art 22(2) paragraph 1 does not apply"
m.T(F222, [AJT, AJF, AJF], JT, "point (a) holds")
m.T(F222, [AJF, AJT, AJF], JT, "point (b) holds")
m.T(F222, [AJF, AJF, AJT], JT, "point (c) holds")
m.T(F222, [AJF, AJF, AJF], JF, "no point holds: 'if' fails in each")
m.T(F222, [AJF, AJF, "NOTHING"], NO, "no point holds and (c) is not decided: not covered")
F221 = "Art 22(1) the data subject has the right not to be subject to a decision based solely on automated processing which produces legal effects or similarly significantly affects him or her"
# arguments: person, based solely on automated processing, includes profiling, legal effects, similarly significant effect, Article 22(2)
m.S("Art 22(1): the right not to be subject to an automated decision")
m.T(F221, [T_, T_, F_, T_, F_, AJF], JT, "solely automated, legal effects, no exception")
m.T(F221, [T_, T_, T_, F_, T_, AJF], JT, "profiling (not read), a similarly significant effect, no exception")
m.T(F221, [T_, T_, F_, F_, F_, AJF], NO, "no legal effect and no similarly significant effect: outside the grant")
m.T(F221, [T_, F_, F_, T_, F_, AJF], NO, "not based solely on automated processing: outside the grant")
m.T(F221, [F_, T_, F_, T_, F_, AJF], NO, "not the data subject")
m.T(F221, [T_, T_, F_, T_, F_, AJT], JF, "paragraph 2 takes the decision out of paragraph 1: 'shall not apply'")
m.T(F221, [T_, T_, F_, T_, F_, "NOTHING"], NO, "whether paragraph 2 applies is not decided")
R221 = "Art 22(1) the controller shall not subject the data subject to a decision based solely on automated processing"
m.TR(R221, [AJT], "AT 0", ["PARTY controller DOES `Art 22(1) subject the data subject to a decision based solely on automated processing` AT 1"], "BREACH: the controller subjects the data subject to such a decision (the act is the breach)")
m.TR(R221, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no such decision: the prohibition stands, unbroken")
m.TR(R221, [AJF], "AT 0", ["PARTY controller DOES `Art 22(1) subject the data subject to a decision based solely on automated processing` AT 1"], "FULFILLED: paragraph 2 applies (or no right), so the decision is not barred by paragraph 1")
F223 = "Art 22(3) in the cases of points (a) and (c) of paragraph 2 the controller implements suitable measures, at least the right to human intervention, to express a point of view and to contest the decision"
# arguments: point (a) answer, point (c) answer, suitable measures implemented, human intervention, point of view, contest
m.S("Art 22(3): suitable measures in the cases of points (a) and (c)")
m.T(F223, [AJT, AJF, T_, T_, T_, T_], MET, "point (a) case, all three safeguards")
m.T(F223, [AJF, AJT, T_, T_, T_, T_], MET, "point (c) case, all three safeguards")
m.T(F223, [AJT, AJF, T_, F_, T_, T_], UNMET, "no right to obtain human intervention: 'at least'")
m.T(F223, [AJT, AJF, T_, T_, F_, T_], UNMET, "no right to express a point of view")
m.T(F223, [AJT, AJF, T_, T_, T_, F_], UNMET, "no right to contest the decision")
m.T(F223, [AJT, AJF, F_, T_, T_, T_], UNMET, "no suitable measures at all")
m.T(F223, [AJF, AJF, T_, T_, T_, T_], NO, "a point (b) decision, or none: outside 'the cases referred to in points (a) and (c)'")
m.T(F223, ["NOTHING", AJF, T_, T_, T_, T_], NO, "point (a) not decided and (c) not met: not covered")
R223 = "Art 22(3) the controller must implement suitable measures in the cases of points (a) and (c) of paragraph 2"
m.TR(R223, [AJT, AJF], "AT 0", ["PARTY controller DOES `Art 22(3) implement suitable measures to safeguard the data subject's rights and freedoms and legitimate interests` AT 1"], "FULFILLED: the measures are implemented")
m.TR(R223, [AJT, AJF], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R223, [AJF, AJF], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: not a point (a) or (c) case")
F224 = "Art 22(4) decisions referred to in paragraph 2 shall not be based on special categories of personal data referred to in Article 9(1)"
# arguments: decision referred to in paragraph 2, based on special categories, Article 9(2)(a), Article 9(2)(g), suitable measures in place
m.S("Art 22(4): special categories of personal data")
m.T(F224, [T_, T_, AJT, AJF, T_], JF, "point (a) of Article 9(2) applies and suitable measures are in place: 'unless'")
m.T(F224, [T_, T_, AJF, AJT, T_], JF, "point (g) applies and suitable measures are in place")
m.T(F224, [T_, T_, AJT, AJF, F_], JT, "point (a) applies but suitable measures are not in place: the bar stands")
m.T(F224, [T_, T_, AJF, AJF, T_], JT, "neither point applies: the bar stands")
m.T(F224, [T_, T_, AJF, AJF, F_], JT, "neither applies, no measures")
m.T(F224, [T_, T_, AJT, AJT, F_], JT, "(a) and (g) both apply, but no suitable measures are in place: the 'unless' needs point (a) or (g) AND the measures, so the bar stands (R2)")
m.T(F224, [T_, T_, AJT, "NOTHING", F_], JT, "(a) applies, (g) not decided, but no suitable measures are in place: the 'unless' needs point (a) or (g) AND the measures, so the bar stands (R2)")
m.T(F224, [T_, T_, AJF, AJT, F_], JT, "(a) fails, (g) applies, but no suitable measures are in place: the 'unless' needs point (a) or (g) AND the measures, so the bar stands (R2)")
m.T(F224, [T_, T_, AJF, "NOTHING", F_], JT, "(a) fails, (g) not decided, but no suitable measures are in place: the 'unless' needs point (a) or (g) AND the measures, so the bar stands (R2)")
m.T(F224, [T_, T_, "NOTHING", AJT, F_], JT, "(a) not decided, (g) applies, but no suitable measures are in place: the 'unless' needs point (a) or (g) AND the measures, so the bar stands (R2)")
m.T(F224, [T_, T_, "NOTHING", AJF, F_], JT, "(a) not decided, (g) fails, but no suitable measures are in place: the 'unless' needs point (a) or (g) AND the measures, so the bar stands (R2)")
m.T(F224, [T_, T_, "NOTHING", "NOTHING", F_], JT, "neither decided, but no suitable measures are in place: the 'unless' needs point (a) or (g) AND the measures, so the bar stands (R2)")
m.T(F224, [T_, T_, "NOTHING", AJF, T_], NO, "point (a) not decided, (g) fails: not covered")
m.T(F224, [T_, T_, "NOTHING", AJT, T_], JF, "point (g) applies with measures: lifts the bar whatever (a) is")
m.T(F224, [T_, F_, AJF, AJF, F_], NO, "not based on special categories: the bar is not engaged")
m.T(F224, [F_, T_, AJF, AJF, F_], NO, "not a decision referred to in paragraph 2: outside the paragraph")

# =============================================================================================== Article 23
m = Mod("23", ["prelude", "`gdpr-core`", "`P2-art-23`"], "Article 23 (src:282-303)")
MODS["23"] = m
P23 = {"12": "`Art 23(1) an obligation or a right provided for in Articles 12 to 22`",
       "34": "`Art 23(1) an obligation provided for in Article 34`",
       "5": "`Art 23(1) Article 5, in so far as its provisions correspond to the rights and obligations provided for in Articles 12 to 22`",
       "other": "`Art 23(1) some other provision of the Regulation`"}
O23 = {"a": "`Art 23(1)(a) national security`", "b": "`Art 23(1)(b) defence`", "c": "`Art 23(1)(c) public security`",
       "d": "`Art 23(1)(d) the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including the safeguarding against and the prevention of threats to public security`",
       "e": "`Art 23(1)(e) other important objectives of general public interest of the Union or of a Member State, in particular an important economic or financial interest, including monetary, budgetary and taxation matters, public health and social security`",
       "f": "`Art 23(1)(f) the protection of judicial independence and judicial proceedings`",
       "g": "`Art 23(1)(g) the prevention, investigation, detection and prosecution of breaches of ethics for regulated professions`",
       "h": "`Art 23(1)(h) a monitoring, inspection or regulatory function connected, even occasionally, to the exercise of official authority in the cases referred to in points (a) to (e) and (g)`",
       "i": "`Art 23(1)(i) the protection of the data subject or the rights and freedoms of others`",
       "j": "`Art 23(1)(j) the enforcement of civil law claims`",
       "other": "`Art 23(1) some other objective`"}
F231 = "Art 23(1) Union or Member State law may restrict by way of a legislative measure the scope of the obligations and rights"
# arguments: Union or Member State law, legislative measure, provision restricted, objective, connected to official authority (point (h)), respects the essence, necessary and proportionate
def a231(law=T_, leg=T_, prov=P23["12"], obj=O23["a"], con=F_, ess=T_, np_=T_):
    return [law, leg, prov, obj, con, ess, np_]
m.S("Art 23(1): what Union or Member State law may restrict")
for k in "abcdefgij":
    m.T(F231, a231(obj=O23[k]), JT, "objective (%s): a legislative measure of Union or Member State law that respects the essence and is necessary and proportionate" % k)
m.T(F231, a231(obj=O23["h"], con=T_), JT, "objective (h): a regulatory function connected to the exercise of official authority")
m.T(F231, a231(obj=O23["h"], con=F_), NO, "objective (h) with no such connection: not point (h)")
m.T(F231, a231(prov=P23["34"]), JT, "the obligation of Article 34")
m.T(F231, a231(prov=P23["5"]), JT, "Article 5 in so far as it corresponds to Articles 12 to 22")
m.T(F231, a231(prov=P23["other"]), NO, "another provision of the Regulation: outside the grant")
m.T(F231, a231(obj=O23["other"]), NO, "an objective outside points (a) to (j): the list is not closed with 'only'")
m.T(F231, a231(law=F_), NO, "not Union or Member State law to which the controller or processor is subject")
m.T(F231, a231(leg=F_), NO, "not by way of a legislative measure")
m.T(F231, a231(ess=F_), JF, "the restriction does not respect the essence of the fundamental rights and freedoms: 'when' fails")
m.T(F231, a231(np_=F_), JF, "not necessary and proportionate: 'when' fails")
m.T(F231, a231(ess=F_, np_=F_), JF, "neither")
F231b = "Art 23(1) the law is a necessary and proportionate measure in a democratic society to safeguard one of the objectives referred to in Article 23(1)"
m.T(F231b, [O23["a"], T_], JT, "national security, necessary and proportionate")
m.T(F231b, [O23["j"], T_], JT, "the enforcement of civil law claims, necessary and proportionate")
m.T(F231b, [O23["a"], F_], JF, "not necessary and proportionate: 'when' fails")
m.T(F231b, [O23["other"], T_], NO, "an objective outside points (a) to (j): not decided")
S2 = {k: "`Art 23(2)(%s) %s`" % (k, v) for k, v in (
    ("a", "the purposes of the processing or categories of processing"), ("b", "the categories of personal data"),
    ("c", "the scope of the restrictions introduced"), ("d", "the safeguards to prevent abuse or unlawful access or transfer"),
    ("e", "the specification of the controller or categories of controllers"),
    ("f", "the storage periods and the applicable safeguards taking into account the nature, scope and purposes of the processing or categories of processing"),
    ("g", "the risks to the rights and freedoms of data subjects"), ("h", "the right of data subjects to be informed about the restriction"))}
F232 = "Art 23(2) the legislative measure contains specific provisions at least, where relevant, as to the matters that paragraph 2 lists"
# arguments: the relevant provisions, the provisions the measure contains, informing the data subjects may be prejudicial
m.S("Art 23(2): what the legislative measure must contain")
m.T(F232, [L(S2["a"], S2["b"], S2["c"]), L(S2["a"], S2["b"], S2["c"]), F_], JT, "three relevant matters, all three provided for")
m.T(F232, [L(S2["a"], S2["b"], S2["c"]), L(S2["a"], S2["b"]), F_], JF, "one relevant matter (c) not provided for: 'shall contain ... at least, where relevant'")
m.T(F232, ["EMPTY", "EMPTY", F_], JT, "nothing is relevant: nothing is required")
m.T(F232, [L(S2["a"]), L(S2["a"], S2["d"]), F_], JT, "the measure also provides for an irrelevant matter: 'at least'")
m.T(F232, [L(S2["h"]), "EMPTY", T_], JT, "(h) informing the data subject may be prejudicial to the purpose of the restriction: not required ('unless')")
m.T(F232, [L(S2["h"]), "EMPTY", F_], JF, "(h) relevant, not prejudicial, and not provided for")
m.T(F232, [L(S2["h"]), L(S2["h"]), F_], JT, "(h) provided for")
m.T(F232, [L(S2["a"], S2["h"]), L(S2["a"]), T_], JT, "(a) provided for, (h) excused as prejudicial")
m.T(F232, [L(S2["a"], S2["h"]), L(S2["h"]), T_], JF, "(h) excused, but (a) is missing")


# =============================================================================================== the fix round of 2026-11-26 (R1 to R10)
# ---- Art 13: the time (R4) and one item at a time (R10)
m = MODS["13"]
m.S("Art 13(1): the information must be provided at the time when the data are obtained (R4)")
m.T(F131, a131(time=F_), UNMET, "every item provided, but not at the time when the data were obtained: 'at the time when personal data are obtained, provide'")
m.T(F131, a131(rep=T_, dpo=T_, gate="(JUST TRUE)", rec=T_, tr=T_, prov=BASE + [I1ar, I1b, I1d, I1e, I1f], time=F_), UNMET, "every point applies and every item is provided, late")
m.T(F131, a131(has=[I1a, I1cp, I1cl], prov=(), time=F_), MET, "the controller provided nothing, because the data subject already has everything: nothing is late")
m.T(F131, a131(has=[I1cl], prov=[I1a, I1cp], time=F_), UNMET, "the data subject already has the legal basis; the rest was provided late")
m.T(F131, a131(gate="NOTHING", time=F_), UNMET, "late, and point (f) is not answered: the lateness is decided whatever (d) is")
m.T(F131, a131(coll=F_, prov=(), time=F_), NOARISE, "data not collected from the data subject: the time does not matter")
m.T(F131, a131(prov=[I1cp, I1cl], time=F_), UNMET, "an item missing and late: unmet")
m.S("Art 13(2): the further information must be provided at the time when the data are obtained (R4)")
m.T(F132, a132(time=F_), UNMET, "every item provided, but not at the time when the data were obtained")
m.T(F132, a132(prov=(), has=B2, time=F_), MET, "the controller provided nothing, because the data subject already has everything: nothing is late")
m.T(F132, a132(coll=F_, prov=(), time=F_), NO, "data not collected from the data subject: outside the paragraph")
O131 = "Art 13(1) the controller owes the data subject the item of information"
# arguments: collected, item, has representative, has DPO, (f) gate, recipients, transfer, the data subject already has the item
def o131(item, coll=T_, rep=F_, dpo=F_, gate="(JUST FALSE)", rec=F_, tr=F_, has=F_):
    return [coll, item, rep, dpo, gate, rec, tr, has]
m.S("Art 13(1): is this item owed? (one item at a time, R10)")
for it, nm in ((I1a, "(a) the identity and contact details of the controller"), (I1cp, "(c) the purposes"), (I1cl, "(c) the legal basis")):
    m.T(O131, o131(it), JT, "%s: owed in every case" % nm)
m.T(O131, o131(I1ar), JF, "(a) the representative: 'where applicable', and the controller has none")
m.T(O131, o131(I1ar, rep=T_), JT, "(a) the representative: the controller has one")
m.T(O131, o131(I1b), JF, "(b) the officer's contact details: 'where applicable', and none was designated")
m.T(O131, o131(I1b, dpo=T_), JT, "(b) the officer's contact details: an officer was designated")
m.T(O131, o131(I1d, gate="(JUST TRUE)"), JT, "(d) 'where the processing is based on point (f) of Article 6(1)': it is")
m.T(O131, o131(I1d, gate="(JUST FALSE)"), JF, "(d) not owed: the processing is not based on point (f)")
m.T(O131, o131(I1d, gate="NOTHING"), NO, "(d): P1 does not answer whether the processing is based on point (f)")
m.T(O131, o131(I1d, gate="NOTHING", has=T_), JF, "(d), point (f) not answered, but the data subject already has it: paragraph 4 lifts the item whatever (f) says")
m.T(O131, o131(I1e), JF, "(e) 'if any': there are no recipients")
m.T(O131, o131(I1e, rec=T_), JT, "(e) there are recipients")
m.T(O131, o131(I1f), JF, "(f) 'where applicable': no transfer is intended")
m.T(O131, o131(I1f, tr=T_), JT, "(f) a transfer is intended")
m.T(O131, o131(I1a, coll=F_), JF, "the data are not collected from the data subject: 'Where personal data ... are collected from the data subject' fails")
m.T(O131, o131(I1cl, has=T_), JF, "the data subject already has the legal basis: paragraph 4, 'where and insofar as'")
O132 = "Art 13(2) the controller owes the data subject the item of further information"
# arguments: collected, item, consent basis, automated decision-making, the data subject already has the item
def o132(item, coll=T_, cons=F_, adm=F_, has=F_):
    return [coll, item, cons, adm, has]
m.S("Art 13(2): is this item owed? (one item at a time, R10)")
for it, nm in ((I2a, "(a) the storage period"), (I2b, "(b) the rights"), (I2d, "(d) the complaint"), (I2e, "(e) the statutory or contractual requirement")):
    m.T(O132, o132(it), JT, "%s: owed" % nm)
m.T(O132, o132(I2c), JF, "(c) the right to withdraw consent: 'where the processing is based on point (a) of Article 6(1) or point (a) of Article 9(2)', and it is not")
m.T(O132, o132(I2c, cons=T_), JT, "(c) the processing is based on consent")
m.T(O132, o132(I2f), JF, "(f) no automated decision-making referred to in Article 22(1) and (4)")
m.T(O132, o132(I2f, adm=T_), JT, "(f) there is such decision-making")
m.T(O132, o132(I2a, coll=F_), NO, "data not collected from the data subject: outside the paragraph")
m.T(O132, o132(I2a, has=T_), JF, "the data subject already has the storage period: paragraph 4")
m.T(O132, o132(I2c, cons=T_, has=T_), JF, "consent basis, but the data subject already has the information")

# ---- Art 14: one item at a time (R10)
m = MODS["14"]
J1a = "`Art 14(1)(a) the identity and the contact details of the controller`"
J1ar = "`Art 14(1)(a) the identity and the contact details of the controller's representative`"
J1b = "`Art 14(1)(b) the contact details of the data protection officer`"
J1cp = "`Art 14(1)(c) the purposes of the processing for which the personal data are intended`"
J1cl = "`Art 14(1)(c) the legal basis for the processing`"
J1d = "`Art 14(1)(d) the categories of personal data concerned`"
J1e = "`Art 14(1)(e) the recipients or categories of recipients of the personal data`"
J1f = "`Art 14(1)(f) the intended transfer to a recipient in a third country or international organisation and the adequacy decision or the safeguards`"
O141 = "Art 14(1) the controller owes the data subject the item of information"
# arguments: not obtained from the data subject, Article 14(5) points (b) to (d), item, representative, DPO, recipients, transfer, already has
def o141(item, nob=T_, g5="(JUST FALSE)", rep=F_, dpo=F_, rec=F_, tr=F_, has=F_):
    return [nob, g5, item, rep, dpo, rec, tr, has]
m.S("Art 14(1): is this item owed? (one item at a time, R10)")
for it, nm in ((J1a, "(a) the identity of the controller"), (J1cp, "(c) the purposes"), (J1cl, "(c) the legal basis"), (J1d, "(d) the categories of personal data")):
    m.T(O141, o141(it), JT, "%s: owed" % nm)
m.T(O141, o141(J1ar), JF, "(a) the representative: the controller has none")
m.T(O141, o141(J1ar, rep=T_), JT, "(a) the representative: there is one")
m.T(O141, o141(J1b), JF, "(b) no officer designated")
m.T(O141, o141(J1b, dpo=T_), JT, "(b) an officer was designated")
m.T(O141, o141(J1e), JF, "(e) 'if any': no recipients")
m.T(O141, o141(J1e, rec=T_), JT, "(e) there are recipients")
m.T(O141, o141(J1f), JF, "(f) 'where applicable': no transfer is intended")
m.T(O141, o141(J1f, tr=T_), JT, "(f) a transfer is intended")
m.T(O141, o141(J1a, nob=F_), JF, "the data were obtained from the data subject: 'Where personal data have not been obtained from the data subject' fails")
m.T(O141, o141(J1a, g5=AJT), JF, "paragraph 5 (b) to (d) disapplies paragraphs 1 to 4: 'shall not apply'")
m.T(O141, o141(J1a, g5="NOTHING"), NO, "paragraph 5 is not answered: it may take the duty away")
m.T(O141, o141(J1a, has=T_), JF, "the data subject already has the information: paragraph 5(a)")
m.T(O141, o141(J1b, g5="NOTHING"), JF, "(b) not owed whatever paragraph 5 says: no officer")
J2a = "`Art 14(2)(a) the period for which the personal data will be stored, or the criteria used to determine that period`"
J2b = "`Art 14(2)(b) the legitimate interests pursued by the controller or by a third party`"
J2c = "`Art 14(2)(c) the existence of the rights of access, rectification, erasure, restriction, objection and data portability`"
J2d = "`Art 14(2)(d) the existence of the right to withdraw consent at any time, without affecting the lawfulness of processing before its withdrawal`"
J2e = "`Art 14(2)(e) the right to lodge a complaint with a supervisory authority`"
J2f = "`Art 14(2)(f) the source from which the personal data originate and, if applicable, whether it came from publicly accessible sources`"
J2g = "`Art 14(2)(g) the existence of automated decision-making, including profiling, and meaningful information about the logic involved, the significance and the envisaged consequences`"
O142 = "Art 14(2) the controller owes the data subject the item of information"
# arguments: not obtained from the data subject, Article 14(5) points (b) to (d), Article 6(1)(f) gate, item, consent basis, automated decision-making, already has
def o142(item, nob=T_, g5="(JUST FALSE)", gate="(JUST FALSE)", cons=F_, adm=F_, has=F_):
    return [nob, g5, gate, item, cons, adm, has]
m.S("Art 14(2): is this item owed? (one item at a time, R10)")
for it, nm in ((J2a, "(a) the storage period"), (J2c, "(c) the rights"), (J2e, "(e) the complaint"), (J2f, "(f) the source")):
    m.T(O142, o142(it), JT, "%s: owed" % nm)
m.T(O142, o142(J2b, gate="(JUST TRUE)"), JT, "(b) 'where the processing is based on point (f) of Article 6(1)': it is")
m.T(O142, o142(J2b, gate="(JUST FALSE)"), JF, "(b) not owed: the processing is not based on point (f)")
m.T(O142, o142(J2b, gate="NOTHING"), NO, "(b): P1 does not answer whether the processing is based on point (f)")
m.T(O142, o142(J2d), JF, "(d) the processing is not based on consent")
m.T(O142, o142(J2d, cons=T_), JT, "(d) the processing is based on consent")
m.T(O142, o142(J2g), JF, "(g) no automated decision-making referred to in Article 22(1) and (4)")
m.T(O142, o142(J2g, adm=T_), JT, "(g) there is such decision-making")
m.T(O142, o142(J2a, nob=F_), NO, "the data were obtained from the data subject: outside the paragraph")
m.T(O142, o142(J2a, g5=AJT), JF, "paragraph 5 (b) to (d) disapplies paragraphs 1 to 4")
m.T(O142, o142(J2a, g5="NOTHING"), NO, "paragraph 5 is not answered")
m.T(O142, o142(J2a, has=T_), JF, "the data subject already has the information")

# ---- Art 12: the months allowed for the notice and for the reasons (R10)
m = MODS["12"]
m.S("Art 12(3) third sentence and Art 12(4): the months allowed (R10)")
m.T("Art 12(3) the months within which the data subject is to be informed of the extension", [], "1", "'within one month of receipt of the request': one month, with no extension of its own")
m.T("Art 12(4) the months within which the data subject is to be informed of the reasons for not taking action", [], "1", "'without delay and at the latest within one month of receipt of the request'")

# ---- Art 16: the duty to complete (R8)
m = MODS["16"]
R16c = "Art 16 the controller must complete the incomplete personal data"
A16c = "PARTY controller DOES `Art 16 complete the incomplete personal data concerning the data subject` AT 1"
m.S("Art 16, second sentence: the controller must complete incomplete data (R8)")
m.TR(R16c, [AJT], "AT 0", [A16c], "FULFILLED: the controller completes the data")
m.TR(R16c, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R16c, [AJF], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: there is no right to completion on these facts")
m.TR(R16c, ["NOTHING"], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: the right is not established (not covered), so the rule creates no standing duty")

# ---- Art 18: the duty to restrict (R8)
m = MODS["18"]
R18a = "Art 18(1) the controller must restrict the processing of the personal data"
A18a = "PARTY controller DOES `Art 18(1) restrict the processing of the personal data concerning the data subject` AT 1"
m.S("Art 18(1): the controller must restrict the processing (R8)")
m.TR(R18a, [AJT], "AT 0", [A18a], "FULFILLED: the controller restricts the processing")
m.TR(R18a, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R18a, [AJF], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: no ground applies, so there is no right to restriction")
m.TR(R18a, ["NOTHING"], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: the right is not established (not covered)")

# ---- Art 20: the duties to provide the data and to transmit directly (R8)
m = MODS["20"]
R201 = "Art 20(1) the controller must give the data subject the personal data in a structured, commonly used and machine-readable format"
A201 = "PARTY controller DOES `Art 20(1) provide the data subject with the personal data in a structured, commonly used and machine-readable format` AT 1"
R202 = "Art 20(2) the controller must transmit the personal data directly to another controller"
A202 = "PARTY controller DOES `Art 20(2) transmit the personal data directly to another controller` AT 1"
m.S("Art 20(1) and (2): the controller must provide the data and transmit them directly (R8)")
m.TR(R201, [AJT], "AT 0", [A201], "FULFILLED: the controller provides the data in the format")
m.TR(R201, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R201, [AJF], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: no right to receive on these facts")
m.TR(R202, [AJT], "AT 0", [A202], "FULFILLED: the controller transmits the data directly")
m.TR(R202, [AJT], "AT 0", ["(WAITUNTIL 1000)"], "no act: the obligation stands; no breach is possible (no time limit)")
m.TR(R202, [AJF], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: not technically feasible, or no exercise of portability: no right to direct transmission")
m.TR(R202, ["NOTHING"], "AT 0", ["(WAITUNTIL 1000)"], "FULFILLED: the right is not established (not covered)")

if __name__ == "__main__":
    want = sys.argv[1:] or sorted(MODS)
    for k in want:
        MODS[k].write()
