#!/usr/bin/env python3
# notes/gen-seats-p2.py -- writes the five seat-layer modules of P2 from the signatures of the layer-1 files and from the cases of
# notes/gen-tests-p2.py.  Run from the deposit folder, after `python3 -I notes/gen-tests-p2.py`:
#     python3 -I notes/gen-seats-p2.py
# It reads gdpr-core.l4, gdpr-core-2.l4 and P2-art-12.l4 ... P2-art-23.l4 for the name, type and order of every input of a layer-1
# function (so no input name is typed twice), and writes
#     P2-seat-subject.l4  P2-cases-seat-subject.l4  P2-seat-controller.l4  P2-cases-seat-controller.l4  P2-cases-mirror.l4
# THE QUESTIONS (the texts below) are written by hand, one for the data subject's seat and one for the controller's.
# THE CASES are the layer-1 cases of notes/gen-tests-p2.py (each with the expected value that was written by hand from the text
# before the first run), converted to the seat's inputs: a role fact the seat fixes ("the person is the data subject" in the data
# subject's seat, "the body is the controller" in the controller's) is dropped, a list of items becomes one yes/no input per item,
# a MAYBE BOOLEAN becomes yes, no or not sure.  A case that the seat cannot put (a role fact the seat fixes is the other way, or a
# partial list of items the data subject already has) is left out of that seat.  The generator copies the expected values and
# computes none of them.
import re, sys, importlib.util, collections

FILES = ["P2-art-%d.l4" % n for n in range(12, 24)]
CORE = ["gdpr-core.l4", "gdpr-core-2.l4"] + FILES

# ---- reading the signatures ----------------------------------------------------------------------------------------------
lines_by_file = {f: open(f, encoding="utf-8").read().split("\n") for f in FILES}
enums = collections.OrderedDict()
for f in CORE:
    ls = open(f, encoding="utf-8").read().split("\n")
    for i, l in enumerate(ls):
        m = re.match(r"^DECLARE `([^`]+)` IS ONE OF\s*$", l)
        if m:
            mem = []
            for l2 in ls[i + 1:]:
                m2 = re.match(r"^\s+`([^`]+)`\s*$", l2)
                if m2:
                    mem.append(m2.group(1))
                else:
                    break
            enums[m.group(1)] = mem

FUNCS = []   # (file, full name, inputs [(name, kind, type)], result)
for f, ls in lines_by_file.items():
    for i, l in enumerate(ls):
        m = re.match(r"^`([^`]+)` MEANS\s*$", l)
        if not m or not ls[i - 1].startswith("GIVETH A "):
            continue
        result = ls[i - 1][len("GIVETH A "):].strip()
        if result.startswith("DEONTIC"):
            continue
        j = i - 2
        ins = []
        while j >= 0:
            mm = re.match(r"^(?:GIVEN)?\s*(`[^`]+`|[A-Za-z]\w*)\s+IS\s+AN?\s+(.+?)\s*$", ls[j])
            if not mm:
                break
            ins.append((mm.group(1).strip("`"), mm.group(2)))
            if ls[j].startswith("GIVEN"):
                break
            j -= 1
        ins.reverse()
        out = []
        for name, ty in ins:
            if ty == "BOOLEAN": out.append((name, "B", None))
            elif ty == "MAYBE BOOLEAN": out.append((name, "Y", None))
            elif ty == "DATE": out.append((name, "D", None))
            elif ty == "NUMBER": out.append((name, "N", None))
            elif re.match(r"^`[^`]+`$", ty): out.append((name, "C", ty.strip("`")))
            elif ty.startswith("LIST OF"): out.append((name, "L", re.search(r"`([^`]+)`", ty).group(1)))
            else: raise Exception(("unknown type", m.group(1), ty))
        FUNCS.append((f, m.group(1), out, result))


def find_fn(key):
    hits = [x for x in FUNCS if x[1].startswith(key)]
    assert len(hits) == 1, (key, [h[1] for h in hits])
    return hits[0]


# ---- the cases of the layer-1 tests ---------------------------------------------------------------------------------------
spec = importlib.util.spec_from_file_location("gentests", "notes/gen-tests-p2.py")
gt = importlib.util.module_from_spec(spec); spec.loader.exec_module(gt)
CASES = collections.defaultdict(list)    # function full name -> [(args, expected, why)]
for mod in gt.MODS.values():
    for it in mod.items:
        if it[0] == "T":
            CASES[it[1]].append((it[2], it[3], it[4]))

# ---- seat vocabulary ------------------------------------------------------------------------------------------------------
JT, JF, NO = "JUST TRUE", "JUST FALSE", "NOTHING"
FIXED = {"the person is the data subject": "subject", "the body is the controller": "controller"}   # input -> the seat that fixes it TRUE
# the choice of an item is named by the Article it belongs to, so that two questions that share a name also share a type (R10)
ITEM_NAME = {"Art 15(1) item of information": "the item of information the data subject asks about",
             "Art 13(1) item of information": "the item of information the data subject asks about in Article 13(1)",
             "Art 13(2) item of further information": "the item of further information the data subject asks about in Article 13(2)",
             "Art 14(1) item of information": "the item of information the data subject asks about in Article 14(1)",
             "Art 14(2) item of information": "the item of information the data subject asks about in Article 14(2)"}
RENAME = {"item": "the item of information the data subject asks about",
          "body": "the kind of body the personal data were disclosed to"}
ALREADY = "the data subject already has the information"
# F-12 (2026-11-26), widened by R1 the same day: every function that takes P1's three-valued answer `Art 11(2) Articles 15 to 20 are
# disapplied` gets the two plain facts below in the seat, so a yes/no/not sure input remains nowhere for this seam.  The reason, first
# found at the Art 12(2) bar: there NOTHING
# means "not an Article 11(2) case" while JUST FALSE means "an Article 11(2) case in which the data subject provided identifying
# information" (fork F12-2).  A person who answers "no" to "Articles 15 to 20 are disapplied" about an ordinary request would be
# read as the second, so the seat asks two plain facts instead and builds the MAYBE itself (the seat helper `P2 <seat> Art 11(2)
# answer from the facts`).  The other functions test it only with EQUALS JUST TRUE, so there "no" and NOTHING make no difference to the
# layer-1 answer, but "not sure" was then answered as "no" while the @desc promised "not covered" (R1), so they take the two facts too.
ART11 = "Art 11(2) Articles 15 to 20 are disapplied"
ART11_FACTS = ("the request concerns a case referred to in Article 11(2): the controller is not in a position to identify the data subject",
               "the data subject has provided information enabling the controller to identify him or her")
BAR_MARK = "the controller demonstrates that it is not in a position to identify the data subject"


def is_bar(fn_inputs):
    return any(n == ART11 for (n, k, t) in fn_inputs) and any(n == BAR_MARK for (n, k, t) in fn_inputs)
LIST_NAMES = {"the items of information that the controller provides": "the information provided includes {s}",
              "the items of further information that the controller provides": "the information provided includes {s}",
              "the specific provisions that are relevant to the restriction": "the matter of {s} is relevant to the restriction",
              "the specific provisions that the legislative measure contains": "the legislative measure contains a specific provision as to {s}"}
ROLES = {"subject": ("a data subject", "As far as you can tell, is it the case that {fact}?"),
         "controller": ("a controller", "Is it the case, for your processing, that {fact}?")}


def suffix(c):
    return re.sub(r"^Art \d+(?:\(\d+\))?(?:\([a-z]\))? ", "", c)


def cap(s):
    return s[0].upper() + s[1:]


def fact_of(name):
    """A seat input's name as a clause for its @desc: `Art 11(2) Articles 15 to 20 are disapplied` becomes `Articles 15 to 20 are disapplied (Art 11(2))`."""
    m = re.match(r"^(Art [^ ]+(?: and \([^)]*\))?) (.*)$", name)
    if m:
        return "%s (%s)" % (m.group(2), m.group(1))
    return name


def q(name):
    return name if re.match(r"^[A-Za-z]\w*$", name) else "`%s`" % name


# ---- the questions ----------------------------------------------------------------------------------------------------------
QS = []
def Q(**kw):
    QS.append(kw)

G12 = "Article 12: transparent information, communication and modalities"
Q(id="12(1)a", group=G12, key="Art 12(1) the controller takes appropriate measures",
  s="Under Article 12(1), as a data subject, is the information and communication I am given in a concise, transparent, intelligible and easily accessible form, using clear and plain language?",
  c="Under Article 12(1), as a controller, have I taken appropriate measures to provide the information and communications in a concise, transparent, intelligible and easily accessible form, using clear and plain language?")
Q(id="12(1)b", group=G12, key="Art 12(1) the information is provided in writing",
  s="Under Article 12(1), as a data subject, has the information been provided to me in writing, or by other means?",
  c="Under Article 12(1), as a controller, have I provided the information in writing, or by other means, including by electronic means where appropriate?")
Q(id="12(1)c", group=G12, key="Art 12(1) the information may be provided orally",
  s="Under Article 12(1), as a data subject, may the information be provided to me orally?",
  c="Under Article 12(1), as a controller, may I provide the information orally?")
Q(id="12(2)a", group=G12, key="Art 12(2) the controller facilitates",
  s="Under Article 12(2), as a data subject, has the controller facilitated the exercise of my rights under Articles 15 to 22?",
  c="Under Article 12(2), as a controller, have I facilitated the exercise of data subject rights under Articles 15 to 22?")
Q(id="12(2)b", group=G12, key="Art 12(2) the controller shall not refuse",
  s="Under Article 12(2), as a data subject, is the controller barred from refusing to act on my request in the cases referred to in Article 11(2)?",
  c="Under Article 12(2), as a controller, am I barred from refusing to act on the data subject's request in the cases referred to in Article 11(2)?")
Q(id="12(3)m", group=G12, key="Art 12(3) the months within which the information on action taken",
  s="Under Article 12(3), as a data subject, within how many months must the controller provide me with information on action taken on my request?",
  c="Under Article 12(3), as a controller, within how many months must I provide the data subject with information on action taken on the request?")
Q(id="12(3)a", group=G12, key="Art 12(3) the controller provides information on action taken",
  s="Under Article 12(3), as a data subject, was I given information on action taken on my request without undue delay and within one month of receipt of the request?",
  c="Under Article 12(3), as a controller, did I provide information on action taken on the request without undue delay and within one month of its receipt?")
Q(id="12(3)b", group=G12, key="Art 12(3) the period may be extended",
  s="Under Article 12(3), as a data subject, may the period for acting on my request be extended by two further months?",
  c="Under Article 12(3), as a controller, may I extend the period by two further months?")
Q(id="12(3)c", group=G12, key="Art 12(3) the controller informs the data subject of the extension",
  s="Under Article 12(3), as a data subject, was I informed of the extension within one month of receipt of my request, together with the reasons for the delay?",
  c="Under Article 12(3), as a controller, have I informed the data subject of the extension within one month of receipt of the request, together with the reasons for the delay?")
Q(id="12(3)n", group=G12, key="Art 12(3) the months within which the data subject is to be informed of the extension",
  s="Under Article 12(3), as a data subject, within how many months must the controller inform me of any extension of the period?",
  c="Under Article 12(3), as a controller, within how many months must I inform the data subject of any extension of the period?")
Q(id="12(3)d", group=G12, key="Art 12(3) the information is provided by electronic means",
  s="Under Article 12(3), as a data subject, has the information been provided to me by electronic means, where I made my request by electronic form means?",
  c="Under Article 12(3), as a controller, have I provided the information by electronic means, where the request was made by electronic form means?")
Q(id="12(4)", group=G12, key="Art 12(4) the controller informs",
  s="Under Article 12(4), as a data subject, was I informed of the reasons for not taking action on my request and of the possibilities of a complaint and a judicial remedy?",
  c="Under Article 12(4), as a controller, where I do not take action on a request, have I informed the data subject of the reasons and of the possibilities of lodging a complaint and seeking a judicial remedy?")
Q(id="12(4)n", group=G12, key="Art 12(4) the months within which",
  s="Under Article 12(4), as a data subject, within how many months must the controller inform me of the reasons for not taking action on my request?",
  c="Under Article 12(4), as a controller, within how many months must I inform the data subject of the reasons for not taking action on the request?")
Q(id="12(5)a", group=G12, key="Art 12(5) the information, communication or action is provided free of charge",
  s="Under Article 12(5), as a data subject, was the information, communication or action provided to me free of charge?",
  c="Under Article 12(5), as a controller, have I provided the information, communication or action free of charge?")
Q(id="12(5)b", group=G12, key="Art 12(5)(a)",
  s="Under Article 12(5), as a data subject, may the controller charge me a reasonable fee for my request?",
  c="Under Article 12(5), as a controller, may I charge a reasonable fee for a request that is manifestly unfounded or excessive?")
Q(id="12(5)c", group=G12, key="Art 12(5)(b)",
  s="Under Article 12(5), as a data subject, may the controller refuse to act on my request?",
  c="Under Article 12(5), as a controller, may I refuse to act on a request that is manifestly unfounded or excessive?")
Q(id="12(5)d", group=G12, key="Art 12(5) the controller has borne the burden",
  s="Under Article 12(5), as a data subject, has the controller borne the burden of demonstrating that my request is manifestly unfounded or excessive?",
  c="Under Article 12(5), as a controller, have I borne the burden of demonstrating that the request is manifestly unfounded or excessive?")
Q(id="12(6)", group=G12, key="Art 12(6)",
  s="Under Article 12(6), as a data subject, may the controller ask me for additional information to confirm my identity?",
  c="Under Article 12(6), as a controller, may I request additional information necessary to confirm the identity of the data subject?")
Q(id="12(7)a", group=G12, key="Art 12(7) the information may be provided",
  s="Under Article 12(7), as a data subject, may the information I am entitled to under Article 13 or 14 be provided to me in combination with standardised icons?",
  c="Under Article 12(7), as a controller, may I provide the information required by Article 13 or 14 in combination with standardised icons?")
Q(id="12(7)b", group=G12, key="Art 12(7) the icons presented electronically",
  s="Under Article 12(7), as a data subject, are the icons presented to me electronically machine-readable?",
  c="Under Article 12(7), as a controller, are the icons I present electronically machine-readable?")

G13 = "Article 13: information where the personal data are collected from the data subject"
Q(id="13(1)", group=G13, key="Art 13(1) the controller provides",
  s="Under Article 13(1), as a data subject, has the controller, at the time it obtained my personal data from me, provided me with all of the following information?",
  c="Under Article 13(1), as a controller, where I collect personal data from the data subject, have I provided, at the time I obtain them, all of the information that paragraph 1 lists?")
Q(id="13(1)i", group=G13, key="Art 13(1) the controller owes the data subject the item",
  s="Under Article 13(1), as a data subject, where the controller collected my personal data from me, am I entitled to be given the item of information I name?",
  c="Under Article 13(1), as a controller, where I collect personal data from the data subject, must I give the data subject the item of information he or she names?")
Q(id="13(2)", group=G13, key="Art 13(2) the controller provides",
  s="Under Article 13(2), as a data subject, has the controller, at the time it obtained my personal data from me, provided me with the further information necessary to ensure fair and transparent processing?",
  c="Under Article 13(2), as a controller, where I collect personal data from the data subject, have I provided, at the time I obtain them, the further information that paragraph 2 lists?")
Q(id="13(2)i", group=G13, key="Art 13(2) the controller owes the data subject the item",
  s="Under Article 13(2), as a data subject, where the controller collected my personal data from me, am I entitled to be given the item of further information I name?",
  c="Under Article 13(2), as a controller, where I collect personal data from the data subject, must I give the data subject the item of further information he or she names?")
Q(id="13(3)", group=G13, key="Art 13(3) the controller provides",
  s="Under Article 13(3), as a data subject, was I given, before my personal data were further processed for another purpose, information on that purpose and any relevant further information?",
  c="Under Article 13(3), as a controller, where I intend to further process personal data for another purpose, have I provided, before the further processing, information on that purpose and any relevant further information?")
Q(id="13(4)", group=G13, key="Art 13(4)",
  s="Under Article 13(4), as a data subject, do paragraphs 1, 2 and 3 not apply because I already have the information?",
  c="Under Article 13(4), as a controller, do paragraphs 1, 2 and 3 not apply because the data subject already has the information?")

G14 = "Article 14: information where the personal data have not been obtained from the data subject"
Q(id="14(1)", group=G14, key="Art 14(1) the controller provides",
  s="Under Article 14(1), as a data subject, where the controller did not obtain my personal data from me, has it provided me with the following information?",
  c="Under Article 14(1), as a controller, where I have not obtained the personal data from the data subject, have I provided the information that paragraph 1 lists?")
Q(id="14(1)i", group=G14, key="Art 14(1) the controller owes the data subject the item",
  s="Under Article 14(1), as a data subject, where the controller did not obtain my personal data from me, am I entitled to be given the item of information I name?",
  c="Under Article 14(1), as a controller, where I have not obtained the personal data from the data subject, must I give the data subject the item of information he or she names?")
Q(id="14(2)", group=G14, key="Art 14(2) the controller provides",
  s="Under Article 14(2), as a data subject, where the controller did not obtain my personal data from me, has it provided me with the further information necessary to ensure fair and transparent processing?",
  c="Under Article 14(2), as a controller, where I have not obtained the personal data from the data subject, have I provided the further information that paragraph 2 lists?")
Q(id="14(2)i", group=G14, key="Art 14(2) the controller owes the data subject the item",
  s="Under Article 14(2), as a data subject, where the controller did not obtain my personal data from me, am I entitled to be given the item of further information I name?",
  c="Under Article 14(2), as a controller, where I have not obtained the personal data from the data subject, must I give the data subject the item of further information he or she names?")
Q(id="14(3)m", group=G14, key="Art 14(3) the months within which",
  s="Under Article 14(3), as a data subject, within how many months after the controller obtained my personal data must it provide me with the information?",
  c="Under Article 14(3), as a controller, within how many months after obtaining the personal data must I provide the information?")
Q(id="14(3)a", group=G14, key="Art 14(3) the controller provides the information",
  s="Under Article 14(3), as a data subject, was the information provided to me within the time that paragraph 3 requires?",
  c="Under Article 14(3), as a controller, have I provided the information within the time that paragraph 3 requires?")
Q(id="14(4)", group=G14, key="Art 14(4) the controller provides",
  s="Under Article 14(4), as a data subject, was I given, before my personal data were further processed for another purpose, information on that purpose and any relevant further information?",
  c="Under Article 14(4), as a controller, where I intend to further process personal data for another purpose, have I provided, before the further processing, information on that purpose and any relevant further information?")
Q(id="14(5)a", group=G14, key="Art 14(5)(a)",
  s="Under Article 14(5), as a data subject, do paragraphs 1 to 4 not apply because I already have the information?",
  c="Under Article 14(5), as a controller, do paragraphs 1 to 4 not apply because the data subject already has the information?")
Q(id="14(5)b", group=G14, key="Art 14(5)(b) paragraphs",
  s="Under Article 14(5), as a data subject, do paragraphs 1 to 4 not apply because providing the information to me proves impossible or would involve a disproportionate effort?",
  c="Under Article 14(5), as a controller, do paragraphs 1 to 4 not apply because providing the information proves impossible or would involve a disproportionate effort?")
Q(id="14(5)b2", group=G14, key="Art 14(5)(b) the controller takes",
  s="Under Article 14(5), as a data subject, has the controller taken appropriate measures to protect my rights and freedoms and legitimate interests, where it need not provide me with the information because that is impossible or disproportionate?",
  c="Under Article 14(5), as a controller, where I need not provide the information because that proves impossible or involves a disproportionate effort, have I taken appropriate measures to protect the data subject's rights and freedoms and legitimate interests?")
Q(id="14(5)c", group=G14, key="Art 14(5)(c)",
  s="Under Article 14(5), as a data subject, do paragraphs 1 to 4 not apply because Union or Member State law expressly lays down the obtaining or disclosure of my personal data?",
  c="Under Article 14(5), as a controller, do paragraphs 1 to 4 not apply because Union or Member State law to which I am subject expressly lays down the obtaining or disclosure?")
Q(id="14(5)d", group=G14, key="Art 14(5)(d)",
  s="Under Article 14(5), as a data subject, do paragraphs 1 to 4 not apply because my personal data must remain confidential under an obligation of professional secrecy?",
  c="Under Article 14(5), as a controller, do paragraphs 1 to 4 not apply because the personal data must remain confidential under an obligation of professional secrecy?")
Q(id="14(5)e", group=G14, key="Art 14(5) points (b) to (d)",
  s="Under Article 14(5), as a data subject, do points (b), (c) or (d) of paragraph 5 disapply paragraphs 1 to 4?",
  c="Under Article 14(5), as a controller, do points (b), (c) or (d) of paragraph 5 disapply paragraphs 1 to 4?")

G15 = "Article 15: right of access by the data subject"
Q(id="15(1)a", group=G15, key="Art 15(1) the data subject has the right to obtain from the controller confirmation",
  s="Under Article 15(1), as a data subject, am I entitled to obtain from the controller confirmation as to whether or not personal data concerning me are being processed?",
  c="Under Article 15(1), as a controller, must I confirm to the data subject whether or not personal data concerning him or her are being processed?")
Q(id="15(1)b", group=G15, key="Art 15(1) the data subject has the right to obtain from the controller access",
  s="Under Article 15(1), as a data subject, am I entitled to obtain from the controller access to the personal data concerning me?",
  c="Under Article 15(1), as a controller, must I give the data subject access to the personal data concerning him or her?")
Q(id="15(1)c", group=G15, key="Art 15(1) the data subject has the right to obtain from the controller the following information",
  s="Under Article 15(1), as a data subject, am I entitled to obtain from the controller the item of information I name?",
  c="Under Article 15(1), as a controller, must I give the data subject the item of information he or she names?")
Q(id="15(2)", group=G15, key="Art 15(2)",
  s="Under Article 15(2), as a data subject, am I entitled to be informed of the appropriate safeguards relating to the transfer of my personal data to a third country or international organisation?",
  c="Under Article 15(2), as a controller, must I inform the data subject of the appropriate safeguards relating to a transfer of his or her personal data to a third country or international organisation?")
Q(id="15(3)a", group=G15, key="Art 15(3) the controller provides a copy",
  s="Under Article 15(3), as a data subject, has the controller provided me with a copy of the personal data undergoing processing?",
  c="Under Article 15(3), as a controller, have I provided the data subject with a copy of the personal data undergoing processing?")
Q(id="15(3)b", group=G15, key="Art 15(3) the controller may charge",
  s="Under Article 15(3), as a data subject, may the controller charge me a reasonable fee for a further copy that I request?",
  c="Under Article 15(3), as a controller, may I charge a reasonable fee based on administrative costs for a further copy that the data subject requests?")
Q(id="15(3)c", group=G15, key="Art 15(3) the information is provided in a commonly used electronic form",
  s="Under Article 15(3), as a data subject, has the information been provided to me in a commonly used electronic form, where I made my request by electronic means?",
  c="Under Article 15(3), as a controller, have I provided the information in a commonly used electronic form, where the request was made by electronic means?")
Q(id="15(4)", group=G15, key="Art 15(4)",
  s="Under Article 15(4), as a data subject, is my right to obtain a copy limited because the copy would adversely affect the rights and freedoms of others?",
  c="Under Article 15(4), as a controller, is the data subject's right to obtain a copy limited because the copy would adversely affect the rights and freedoms of others?")

G16 = "Article 16: right to rectification"
Q(id="16a", group=G16, key="Art 16 the data subject has the right to obtain",
  s="Under Article 16, as a data subject, am I entitled to obtain from the controller the rectification of inaccurate personal data concerning me?",
  c="Under Article 16, as a controller, must I rectify inaccurate personal data concerning the data subject?")
Q(id="16b", group=G16, key="Art 16 the data subject has the right to have incomplete",
  s="Under Article 16, as a data subject, am I entitled to have incomplete personal data concerning me completed?",
  c="Under Article 16, as a controller, must I complete incomplete personal data concerning the data subject?")

G17 = "Article 17: right to erasure ('right to be forgotten')"
WHO17S = {"b": "I withdraw my consent and there is no other legal ground for the processing",
          "c": "I object to the processing and there are no overriding legitimate grounds for it, or I object to processing for direct marketing"}
WHO18S = {"a": "the accuracy of my personal data is contested, for a period enabling the controller to verify it",
          "b": "the processing is unlawful and I oppose erasure and request restriction instead",
          "c": "the controller no longer needs my personal data but I require them for legal claims",
          "d": "I have objected pursuant to Article 21(1), pending the verification whether the controller's grounds override"}
for k, who in (("a", "the personal data are no longer necessary in relation to the purposes for which they were collected or otherwise processed"),
               ("b", "the data subject withdraws consent and there is no other legal ground for the processing"),
               ("c", "the data subject objects to the processing and there are no overriding legitimate grounds for it, or objects to processing for direct marketing"),
               ("d", "the personal data have been unlawfully processed"),
               ("e", "the personal data have to be erased for compliance with a legal obligation in Union or Member State law"),
               ("f", "the personal data have been collected in relation to the offer of information society services referred to in Article 8(1)")):
    Q(id="17(1)(%s)" % k, group=G17, key="Art 17(1)(%s) point" % k,
      s="Under Article 17(1), as a data subject, does ground (%s) apply to my personal data: %s?" % (k, WHO17S.get(k, who.replace("the personal data", "my personal data"))),
      c="Under Article 17(1), as a controller, does ground (%s) apply: %s?" % (k, who))
Q(id="17(1)", group=G17, key="Art 17(1) the data subject has the right to obtain from the controller the erasure",
  s="Under Article 17(1), as a data subject, am I entitled to obtain from the controller the erasure of my personal data?",
  c="Under Article 17(1), as a controller, must I erase the data subject's personal data?")
Q(id="17(2)", group=G17, key="Art 17(2) the controller takes",
  s="Under Article 17(2), as a data subject, has the controller, having made my personal data public, taken reasonable steps to inform the controllers processing them that I have requested erasure?",
  c="Under Article 17(2), as a controller, having made the personal data public, have I taken reasonable steps, including technical measures, to inform the controllers processing them that the data subject has requested erasure?")
for k, who in (("a", "the processing is necessary for exercising the right of freedom of expression and information"),
               ("b", "the processing is necessary for compliance with a legal obligation or for a task in the public interest or in the exercise of official authority"),
               ("c", "the processing is necessary for reasons of public interest in the area of public health, in accordance with points (h) and (i) of Article 9(2) and Article 9(3)"),
               ("d", "the processing is necessary for archiving, research or statistical purposes, in accordance with Article 89(1) and in so far as erasure would seriously impair its objectives"),
               ("e", "the processing is necessary for the establishment, exercise or defence of legal claims")):
    Q(id="17(3)(%s)" % k, group=G17, key="Art 17(3)(%s) paragraphs" % k,
      s="Under Article 17(3), as a data subject, do paragraphs 1 and 2 not apply to my personal data because %s?" % who,
      c="Under Article 17(3), as a controller, do paragraphs 1 and 2 not apply because %s?" % who)
Q(id="17(3)", group=G17, key="Art 17(3) paragraphs 1 and 2 do not apply",
  s="Under Article 17(3), as a data subject, do paragraphs 1 and 2 not apply to my personal data?",
  c="Under Article 17(3), as a controller, do paragraphs 1 and 2 not apply to the personal data I process?")

G18 = "Article 18: right to restriction of processing"
for k, who in (("a", "the accuracy of the personal data is contested, for a period enabling the controller to verify it"),
               ("b", "the processing is unlawful and the data subject opposes erasure and requests restriction instead"),
               ("c", "the controller no longer needs the personal data but the data subject requires them for legal claims"),
               ("d", "the data subject has objected pursuant to Article 21(1), pending the verification whether the controller's grounds override")):
    Q(id="18(1)(%s)" % k, group=G18, key="Art 18(1)(%s) point" % k,
      s="Under Article 18(1), as a data subject, does ground (%s) apply to me: %s?" % (k, WHO18S[k]),
      c="Under Article 18(1), as a controller, does ground (%s) apply: %s?" % (k, who))
Q(id="18(1)", group=G18, key="Art 18(1) the data subject has the right",
  s="Under Article 18(1), as a data subject, am I entitled to obtain from the controller restriction of the processing of my personal data?",
  c="Under Article 18(1), as a controller, must I restrict the processing of the data subject's personal data?")
Q(id="18(2)", group=G18, key="Art 18(2)",
  s="Under Article 18(2), as a data subject, is the controller processing my restricted personal data only as paragraph 2 allows?",
  c="Under Article 18(2), as a controller, am I processing the restricted personal data, apart from storage, only with the data subject's consent or for one of the three purposes that paragraph 2 names?")
Q(id="18(3)", group=G18, key="Art 18(3) the controller informs",
  s="Under Article 18(3), as a data subject, was I informed by the controller before the restriction of the processing of my personal data was lifted?",
  c="Under Article 18(3), as a controller, have I informed the data subject, before lifting the restriction of processing, that I am lifting it?")

G19 = "Article 19: notification obligation regarding rectification or erasure or restriction"
Q(id="19a", group=G19, key="Art 19 the controller communicates",
  s="Under Article 19, as a data subject, has the controller communicated the rectification, erasure or restriction of processing of my personal data to a recipient to whom they were disclosed?",
  c="Under Article 19, as a controller, have I communicated the rectification, erasure or restriction of processing to a recipient to whom the personal data were disclosed?")
Q(id="19b", group=G19, key="Art 19 the controller informs",
  s="Under Article 19, as a data subject, where I asked, has the controller informed me about the recipients of my personal data?",
  c="Under Article 19, as a controller, where the data subject asks, have I informed the data subject about the recipients?")

G20 = "Article 20: right to data portability"
Q(id="20(1)a", group=G20, key="Art 20(1) the data subject has the right to receive",
  s="Under Article 20(1), as a data subject, am I entitled to receive the personal data I provided to the controller in a structured, commonly used and machine-readable format?",
  c="Under Article 20(1), as a controller, must I give the data subject the personal data he or she provided to me in a structured, commonly used and machine-readable format?")
Q(id="20(1)b", group=G20, key="Art 20(1) the data subject has the right to transmit",
  s="Under Article 20(1), as a data subject, am I entitled to transmit my personal data to another controller without hindrance from the controller to which I provided them?",
  c="Under Article 20(1), as a controller, must I allow the data subject to transmit his or her personal data to another controller without hindrance from me?")
Q(id="20(2)", group=G20, key="Art 20(2)",
  s="Under Article 20(2), as a data subject, am I entitled to have my personal data transmitted directly from one controller to another?",
  c="Under Article 20(2), as a controller, must I transmit the data subject's personal data directly to another controller, where technically feasible?")
Q(id="20(3)a", group=G20, key="Art 20(3) the exercise",
  s="Under Article 20(3), as a data subject, does my exercise of the right to data portability prejudice my right to erasure under Article 17?",
  c="Under Article 20(3), as a controller, does the data subject's exercise of the right to data portability prejudice his or her right to erasure under Article 17?")
Q(id="20(3)b", group=G20, key="Art 20(3) the right to data portability does not apply",
  s="Under Article 20(3), as a data subject, does the right to data portability not apply to processing necessary for a task in the public interest or in the exercise of official authority?",
  c="Under Article 20(3), as a controller, does the right to data portability not apply to my processing, which is necessary for a task in the public interest or in the exercise of official authority?")
Q(id="20(4)", group=G20, key="Art 20(4)",
  s="Under Article 20(4), as a data subject, is my right to data portability limited because its exercise would adversely affect the rights and freedoms of others?",
  c="Under Article 20(4), as a controller, is the data subject's right to data portability limited because its exercise would adversely affect the rights and freedoms of others?")

G21 = "Article 21: right to object"
Q(id="21(1)a", group=G21, key="Art 21(1) the data subject has the right to object",
  s="Under Article 21(1), as a data subject, am I entitled to object, on grounds relating to my particular situation, to processing of my personal data based on point (e) or (f) of Article 6(1)?",
  c="Under Article 21(1), as a controller, may the data subject object, on grounds relating to his or her particular situation, to my processing based on point (e) or (f) of Article 6(1)?")
Q(id="21(1)b", group=G21, key="Art 21(1) the controller shall no longer process",
  s="Under Article 21(1), as a data subject, after I objected, is the controller barred from processing my personal data any longer?",
  c="Under Article 21(1), as a controller, after the data subject objected, am I barred from processing his or her personal data any longer?")
Q(id="21(2)", group=G21, key="Art 21(2)",
  s="Under Article 21(2), as a data subject, am I entitled to object at any time to processing of my personal data for direct marketing?",
  c="Under Article 21(2), as a controller, may the data subject object at any time to my processing of his or her personal data for direct marketing?")
Q(id="21(3)", group=G21, key="Art 21(3)",
  s="Under Article 21(3), as a data subject, after I objected to direct marketing, are my personal data barred from being processed for that purpose any longer?",
  c="Under Article 21(3), as a controller, after the data subject objected to direct marketing, are the personal data barred from being processed by me for that purpose any longer?")
Q(id="21(4)", group=G21, key="Art 21(4)",
  s="Under Article 21(4), as a data subject, was my right to object explicitly brought to my attention, clearly and separately, at the latest at the time of the first communication with me?",
  c="Under Article 21(4), as a controller, have I explicitly brought the right to object to the data subject's attention, clearly and separately, at the latest at the time of the first communication?")
Q(id="21(5)", group=G21, key="Art 21(5)",
  s="Under Article 21(5), as a data subject, may I exercise my right to object by automated means using technical specifications?",
  c="Under Article 21(5), as a controller, may the data subject exercise the right to object by automated means using technical specifications?")
Q(id="21(6)", group=G21, key="Art 21(6)",
  s="Under Article 21(6), as a data subject, am I entitled to object to processing of my personal data for scientific or historical research or statistical purposes?",
  c="Under Article 21(6), as a controller, may the data subject object to my processing of his or her personal data for scientific or historical research or statistical purposes?")

G22 = "Article 22: automated individual decision-making, including profiling"
for k, who in (("a", "the decision is necessary for entering into, or performance of, a contract between the data subject and a controller"),
               ("b", "the decision is authorised by Union or Member State law which also lays down suitable measures"),
               ("c", "the decision is based on the data subject's explicit consent")):
    Q(id="22(2)(%s)" % k, group=G22, key="Art 22(2)(%s) point" % k,
      s="Under Article 22(2), as a data subject, does point (%s) apply to the decision about me: %s?" % (k, who.replace("the data subject's", "my").replace("the data subject", "me")),
      c="Under Article 22(2), as a controller, does point (%s) apply to my decision: %s?" % (k, who))
Q(id="22(2)", group=G22, key="Art 22(2) paragraph 1 does not apply",
  s="Under Article 22(2), as a data subject, does paragraph 1 not apply to the decision about me?",
  c="Under Article 22(2), as a controller, does paragraph 1 not apply to my decision?")
Q(id="22(1)", group=G22, key="Art 22(1) the data subject has the right",
  s="Under Article 22(1), as a data subject, am I entitled not to be subject to a decision based solely on automated processing that produces legal effects concerning me or similarly significantly affects me?",
  c="Under Article 22(1), as a controller, must I refrain from subjecting the data subject to a decision based solely on automated processing that produces legal effects or similarly significantly affects him or her?")
Q(id="22(3)", group=G22, key="Art 22(3) in the cases",
  s="Under Article 22(3), as a data subject, in a decision under point (a) or (c) of paragraph 2, has the controller implemented suitable measures, at least the right to human intervention, to express my point of view and to contest the decision?",
  c="Under Article 22(3), as a controller, in a decision under point (a) or (c) of paragraph 2, have I implemented suitable measures, at least the right to human intervention, to express a point of view and to contest the decision?")
Q(id="22(4)", group=G22, key="Art 22(4)",
  s="Under Article 22(4), as a data subject, is a decision referred to in paragraph 2 barred from being based on special categories of my personal data?",
  c="Under Article 22(4), as a controller, am I barred from basing a decision referred to in paragraph 2 on special categories of personal data?")

G23 = "Article 23: restrictions"
Q(id="23(1)a", group=G23, key="Art 23(1) Union or Member State law may restrict",
  s="Under Article 23(1), as a data subject, may Union or Member State law restrict by a legislative measure the scope of the rights I have under Articles 12 to 22?",
  c="Under Article 23(1), as a controller, may Union or Member State law restrict by a legislative measure the scope of my obligations under Articles 12 to 22?")
Q(id="23(1)b", group=G23, key="Art 23(1) the law is a necessary and proportionate",
  s="Under Article 23(1), as a data subject, is the law that restricts my rights a necessary and proportionate measure in a democratic society to safeguard one of the objectives that paragraph 1 names?",
  c="Under Article 23(1), as a controller, is the law that restricts my obligations a necessary and proportionate measure in a democratic society to safeguard one of the objectives that paragraph 1 names?")
Q(id="23(2)", group=G23, key="Art 23(2)",
  s="Under Article 23(2), as a data subject, does the legislative measure that restricts my rights contain specific provisions at least, where relevant, as to the matters that paragraph 2 lists?",
  c="Under Article 23(2), as a controller, does the legislative measure that restricts my obligations contain specific provisions at least, where relevant, as to the matters that paragraph 2 lists?")

# ---- conversion of cases ------------------------------------------------------------------------------------------------
def members_of(text):
    return re.findall(r"`([^`]+)`", text)


def seat_inputs(fn_inputs, seat):
    """The seat's inputs, in order: list of (kind, seat input name, source layer-1 input index or None, extra)."""
    out = []
    for idx, (name, kind, ty) in enumerate(fn_inputs):
        if name in FIXED:
            if FIXED[name] == seat:
                out.append(("fixed", name, idx, None))
                continue
        if kind == "L":
            if "already has" in name:
                out.append(("all", ALREADY, idx, ty))
            else:
                tmpl = LIST_NAMES[name]
                for c in enums[ty]:
                    out.append(("item", tmpl.format(s=suffix(c)), idx, c))
            continue
        if kind == "Y" and name == ART11:
            out.append(("E", ART11_FACTS[0], idx, 1))
            out.append(("E", ART11_FACTS[1], idx, 2))
            continue
        out.append((kind, ITEM_NAME.get(ty, RENAME.get(name, name)) if name == "item" else RENAME.get(name, name), idx, ty))
    return out


def convert_case(fn_inputs, seat, args):
    """The seat's argument expressions for a layer-1 case, or None if the seat cannot put the case."""
    vals = []
    for (kind, sname, idx, extra) in seat_inputs(fn_inputs, seat):
        a = args[idx]
        if kind == "fixed":
            if a != "TRUE":
                return None
            continue
        if kind == "E":
            vals.append("TRUE" if (a != "NOTHING" if extra == 1 else a == "(JUST FALSE)") else "FALSE")
        elif kind == "Y":
            vals.append({"(JUST TRUE)": "`P2 %s answer: yes`", "(JUST FALSE)": "`P2 %s answer: no`", "NOTHING": "`P2 %s answer: not sure`"}[a] % seat)
        elif kind == "all":
            mem = members_of(a)
            if a == "EMPTY":
                vals.append("FALSE")
            elif sorted(mem) == sorted(enums[extra]):
                vals.append("TRUE")
            else:
                return None
        elif kind == "item":
            vals.append("TRUE" if extra in members_of(a) else "FALSE")
        else:
            vals.append(a)
    return vals


def pick_cases(cases, fn_inputs, seat, limit=7):
    ok = []
    for (args, exp, why) in cases:
        v = convert_case(fn_inputs, seat, args)
        if v is not None:
            ok.append((args, v, exp, why))
    chosen, seen = [], set()
    for c in ok:
        if c[2] not in seen:
            seen.add(c[2]); chosen.append(c)
    for c in ok:
        if len(chosen) >= limit:
            break
        if c not in chosen:
            chosen.append(c)
    return [c for c in ok if c in chosen]


# ---- writing the files ---------------------------------------------------------------------------------------------------
def decide_name(text):
    return text.rstrip("?")


def call_expr(fn_inputs, seat):
    parts = []
    for (kind, sname, idx, extra) in seat_inputs(fn_inputs, seat):
        pass
    # arguments in layer-1 order
    args = []
    sin = seat_inputs(fn_inputs, seat)
    by_idx = collections.OrderedDict()
    for s in sin:
        by_idx.setdefault(s[2], []).append(s)
    for idx, (name, kind, ty) in enumerate(fn_inputs):
        group = by_idx[idx]
        if group[0][0] == "fixed":
            args.append("TRUE")
        elif group[0][0] == "E":
            args.append("(`P2 %s Art 11(2) answer from the facts` %s %s)" % (seat, q(group[0][1]), q(group[1][1])))
        elif kind == "Y":
            args.append("(`P2 %s answer as a yes or no` %s)" % (seat, q(group[0][1])))
        elif kind == "L" and group[0][0] == "all":
            allm = ", ".join("`%s`" % c for c in enums[ty])
            args.append("(IF %s THEN (LIST %s) ELSE EMPTY)" % (q(group[0][1]), allm))
        elif kind == "L":
            expr = "EMPTY"
            for (k2, sname, i2, c) in reversed(group):
                expr = "(append (IF %s THEN LIST `%s` ELSE EMPTY) %s)" % (q(sname), c, expr)
            args.append(expr)
        else:
            args.append(q(group[0][1]))
    return " ".join(args)


files = {}
counts = {}
mirror = ["IMPORT prelude\nIMPORT `gdpr-core`\nIMPORT `gdpr-definitions-2`\nIMPORT `P2-seat-subject`\nIMPORT `P2-seat-controller`\n",
          """-- ============================================================================
-- P2-cases-mirror.l4 -- the same facts put to the data subject's seat and the controller's seat, asserting that the two answers
-- are equal.  Only the questions that both seats ask are mirrored.  Each case is a layer-1 case of notes/gen-tests-p2.py (its
-- expected value was written by hand from the text); a role fact that one seat fixes is TRUE in the case (the data subject and
-- the controller are the two parties of one relation), and a seat that asks it is given TRUE.  A seat asks yes, no or not sure in
-- its own type, so the values are mapped.  The same cases are asserted against their expected values in the two cases files.
-- ============================================================================
"""]
n_m = 0
for seat in ("subject", "controller"):
    phrase, bool_desc = ROLES[seat]
    who = ("A DATA SUBJECT, the natural person whose personal data are processed" if seat == "subject"
           else "A CONTROLLER, the body that determines the purposes and means of the processing")
    seatf, casef = [], []
    seatf.append("IMPORT prelude\nIMPORT daydate\nIMPORT `gdpr-core`\nIMPORT `gdpr-core-2`\nIMPORT `gdpr-definitions-2`\n" + "".join("IMPORT `%s`\n" % f[:-3] for f in FILES))
    seatf.append("""-- ============================================================================
-- P2-seat-%(seat)s.l4 -- THE SEAT LAYER OF P2 (CHAPTER III, ARTICLES 12 TO 23) FOR %(who)s.
-- Written by P2 (Sonnet 5.5); produced from the layer-1 signatures by notes/gen-seats-p2.py.
-- SEAT: %(who)s.  Every question is phrased as that person asks it and takes plain inputs: a yes or no, a
-- date, a number, a choice from a list, one yes or no for each item of a list, or yes, no or not sure where a combining rule takes a
-- MAYBE (not sure is treated as not covered).  Nothing here is new law and no rule is restated: every answer is a call on a layer-1
-- rule of P2-art-12.l4 ... P2-art-23.l4 (or, through them, of the keel).
-- THE ROLE FACTS.  %(fixed)s
-- Questions are grouped under § headings in the Regulation's order.
-- HOW TO READ A RESULT.  JUST TRUE and JUST FALSE are answers the Regulation gives in its own words; NOTHING means it does not answer
-- on these facts (NOTES: Reading a result).  Never read NOTHING as no.  A `Duty outcome` is one of: the duty does not arise, the duty arises
-- and is met, the duty arises and is not met; NOTHING beside it is "not covered".  A NUMBER is a number of months.
-- THERE IS NO SEAT FOR AN AUTHORITY.  Article 23 is addressed to a lawmaker and reaches this seat only through the questions below,
-- for what it means to the person.
-- ============================================================================
""" % dict(seat=seat, who=who,
           fixed=("The question is asked as a data subject, so `the person is the data subject` is TRUE and is not asked." if seat == "subject"
                  else "The question is asked as a controller, so `the body is the controller` is TRUE and is not asked.")))
    seatf.append("""-- Yes, no or not sure, for a fact that a combining rule takes as a MAYBE.
DECLARE `P2 %(r)s answer` IS ONE OF
    `P2 %(r)s answer: yes`
    `P2 %(r)s answer: no`
    `P2 %(r)s answer: not sure`

GIVEN answer IS A `P2 %(r)s answer`
GIVETH A MAYBE BOOLEAN
`P2 %(r)s answer as a yes or no` MEANS
    CONSIDER answer
    WHEN `P2 %(r)s answer: yes` THEN JUST TRUE -- input mapping
    WHEN `P2 %(r)s answer: no` THEN JUST FALSE -- input mapping
    WHEN `P2 %(r)s answer: not sure` THEN NOTHING -- input mapping

-- The Article 12(2) bar takes P1's answer `Art 11(2) Articles 15 to 20 are disapplied`, which has three meanings there (JUST TRUE: an
-- Article 11(2) case; JUST FALSE: an Article 11(2) case in which the data subject provided identifying information; NOTHING: not an
-- Article 11(2) case).  A plain yes or no would read "no" as the second meaning for an ordinary request, so the seat asks two plain
-- facts and builds the three meanings from them (finding F-12 in notes/P2-NOTES.md).
GIVEN `%(f1)s` IS A BOOLEAN
      `%(f2)s` IS A BOOLEAN
GIVETH A MAYBE BOOLEAN
`P2 %(r)s Art 11(2) answer from the facts` MEANS
    BRANCH
        IF NOT (`%(f1)s`)
        THEN NOTHING -- input mapping: not an Article 11(2) case
        IF `%(f2)s`
        THEN JUST FALSE -- input mapping: an Article 11(2) case in which the data subject provided identifying information
        OTHERWISE JUST TRUE -- input mapping: an Article 11(2) case
""" % dict(r=seat, f1=ART11_FACTS[0], f2=ART11_FACTS[1]))
    seatf.append("§ `Regulation (EU) 2016/679, Chapter III -- my questions as %s`\n" % phrase)
    casef.append("IMPORT prelude\nIMPORT daydate\nIMPORT `gdpr-core`\nIMPORT `gdpr-core-2`\nIMPORT `P2-seat-%s`\n" % seat)
    casef.append("""-- ============================================================================
-- P2-cases-seat-%(seat)s.l4 -- cases for the questions of P2-seat-%(seat)s.l4, with the facts a real person in the seat would state.
-- Every case is a layer-1 case of notes/gen-tests-p2.py converted to the seat's inputs; its expected value was written by hand from the
-- text of the provision named in the comment above the group, before the first run, and none was copied from an output.  Where a
-- question has more cases in layer 1 than are shown here, the cases here cover every distinct expected answer.
-- ============================================================================
""" % dict(seat=seat))
    last, n_q, n_c = None, 0, 0
    for qd in QS:
        if seat not in ("subject", "controller") or ("s" if seat == "subject" else "c") not in qd:
            continue
        text = qd["s" if seat == "subject" else "c"]
        full, fname, fins, fres = find_fn(qd["key"])
        sin = seat_inputs(fins, seat)
        if qd["group"] != last:
            seatf.append("\n§§ `%s`\n" % qd["group"]); casef.append("\n§§ `%s`\n" % qd["group"]); last = qd["group"]
        n_q += 1
        gl = []
        first = True
        for (kind, sname, idx, extra) in sin:
            if kind == "fixed":
                continue
            fact = fact_of(sname)
            if kind == "B" or kind == "item" or kind == "all" or kind == "E":
                desc, ty = bool_desc.format(fact=fact) + " Answer true or false.", "BOOLEAN"
            elif kind == "Y":
                desc = bool_desc.format(fact=fact) + " Answer P2 %s answer: yes, P2 %s answer: no or P2 %s answer: not sure (not sure is treated as not covered)." % (seat, seat, seat)
                ty = "`P2 %s answer`" % seat
            elif kind == "D":
                desc, ty = "On what date: %s?" % fact, "DATE"
            elif kind == "N":
                desc, ty = "What is %s? Give a number." % fact, "NUMBER"
            elif kind == "C":
                desc, ty = "%s: choose exactly one of: %s." % (cap(fact), "; ".join(enums[extra])), "`%s`" % extra
            else:
                raise Exception(kind)
            gl.append("%s%s IS A %s @desc %s" % ("GIVEN " if first else "      ", q(sname), ty if not ty.startswith("`") else ty, desc))
            first = False
        dn = decide_name(text)
        seatf.append("-- %s: %s" % (qd["id"], fname))
        seatf.append("@export %s" % text)
        if gl:
            seatf.extend(gl)
        seatf.append("GIVETH A %s" % fres)
        seatf.append("DECIDE `%s` IS" % dn)
        seatf.append("    `%s` %s" % (fname, call_expr(fins, seat)))
        seatf.append("")
        casef.append("-- %s: %s" % (qd["id"], fname))
        chosen = pick_cases(CASES[fname], fins, seat)
        assert chosen, ("no case for", qd["id"], seat)
        for (args, vals, exp, why) in chosen:
            casef.append("-- %s" % why.replace("P1 says the case is outside Article 11(2): ", "an ordinary request, not in an Article 11(2) case (the two Article 11(2) facts are false): "))
            casef.append("#ASSERT `%s` %s EQUALS %s" % (dn, " ".join(vals), exp) if vals else "#ASSERT `%s` EQUALS %s" % (dn, exp))
            n_c += 1
        casef.append("")
    files["P2-seat-%s.l4" % seat] = "\n".join(seatf)
    files["P2-cases-seat-%s.l4" % seat] = "\n".join(casef)
    counts[seat] = (n_q, n_c)

# the mirror: the questions both seats ask, with the cases both seats can put
for qd in QS:
    if "s" not in qd or "c" not in qd:
        continue
    full, fname, fins, fres = find_fn(qd["key"])
    cs = []
    for (args, exp, why) in CASES[fname]:
        vs = convert_case(fins, "subject", args); vc = convert_case(fins, "controller", args)
        if vs is not None and vc is not None:
            cs.append((args, vs, vc, exp, why))
    seen, chosen = set(), []
    for c in cs:
        if c[3] not in seen:
            seen.add(c[3]); chosen.append(c)
    for c in cs:
        if len(chosen) >= 3: break
        if c not in chosen: chosen.append(c)
    if not chosen:
        continue
    mirror.append("-- %s: %s" % (qd["id"], fname))
    for (args, vs, vc, exp, why) in chosen:
        ds, dc = decide_name(qd["s"]), decide_name(qd["c"])
        mirror.append("#ASSERT (`%s` %s) EQUALS (`%s` %s)" % (ds, " ".join(vs), dc, " ".join(vc)) if vs else "#ASSERT (`%s`) EQUALS (`%s`)" % (ds, dc))
        n_m += 1
    mirror.append("")
files["P2-cases-mirror.l4"] = "\n".join(mirror)

for f, s in files.items():
    open(f, "w", encoding="utf-8").write(s.rstrip("\n") + "\n")
print("subject: %d questions, %d cases; controller: %d questions, %d cases; mirror: %d assertions" % (counts["subject"][0], counts["subject"][1], counts["controller"][0], counts["controller"][1], n_m))
