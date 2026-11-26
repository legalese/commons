#!/usr/bin/env python3
# notes/gen-seats.py -- writes the five seat-layer modules of K2 from the signatures of the layer-1 files.
# Run from the deposit folder:   python3 -I notes/gen-seats.py
# It reads gdpr-core.l4, gdpr-core-2.l4, gdpr-definitions-2.l4, K2-art-1.l4, K2-art-2b.l4, K2-art-3.l4 for the
# names, types and input order of every layer-1 function (so no input name is typed twice), and it writes
#   K2-seat-subject.l4  K2-cases-seat-subject.l4  K2-seat-controller.l4  K2-cases-seat-controller.l4  K2-cases-mirror.l4
# The EXPECTED VALUES are the ones in the case lists below.  They were written by hand from the text of the
# provision before the first run; the generator copies them and computes none of them.
import re, sys

LAYER1 = ["gdpr-definitions-2.l4", "K2-art-1.l4", "K2-art-2b.l4", "K2-art-3.l4"]
CORE = ["gdpr-core.l4", "gdpr-core-2.l4"]

# ---- reading the layer-1 signatures --------------------------------------------------------------
lines_by_file = {f: open(f, encoding="utf-8").read().split("\n") for f in LAYER1}
enums = {}
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


def find_fn(prefix):
    hits = []
    for f, ls in lines_by_file.items():
        for i, l in enumerate(ls):
            if l.startswith("`" + prefix):
                m = re.match(r"^`([^`]+)` MEANS\s*$", l)
                if m:
                    hits.append((f, i, m.group(1)))
    assert len(hits) == 1, (prefix, hits)
    f, i, full = hits[0]
    ls = lines_by_file[f]
    assert ls[i - 1].startswith("GIVETH A "), (full, ls[i - 1])
    result = ls[i - 1][len("GIVETH A "):].strip()
    j = i - 2
    ins = []
    while True:
        l = ls[j]
        m = re.match(r"^(?:GIVEN)?\s*(`[^`]+`|[A-Za-z]\w*)\s+IS\s+AN?\s+(.+?)\s*$", l)
        assert m, (full, l)
        ins.append((m.group(1).strip("`"), m.group(2)))
        if l.startswith("GIVEN"):
            break
        j -= 1
    ins.reverse()
    out = []
    for name, ty in ins:
        if ty == "BOOLEAN":
            out.append((name, "B", None))
        elif ty == "MAYBE BOOLEAN":
            out.append((name, "Y", None))
        elif re.match(r"^`[^`]+`$", ty):
            out.append((name, "C", ty.strip("`")))
        elif ty.startswith("LIST OF"):
            out.append((name, "L", re.search(r"`([^`]+)`", ty).group(1)))
        else:
            raise Exception(("unknown type", full, ty))
    return full, out, result


# ---- the questions: id, group, texts, layer-1 function, overrides, cases -----------------------------
T, F = "TRUE", "FALSE"
JT, JF, NO = "JUST TRUE", "JUST FALSE", "NOTHING"
Yes, No, Unsure = "yes", "no", "not sure"

A = "Art 4(16)(a) "
QS = []


def Q(**kw):
    QS.append(kw)


# S = in the data subject's seat, C = in the controller's seat.  `s` and `c` are the question texts.
Q(id="1(3)", group="Article 1", s="Under Article 1(3), as a data subject, is a restriction or prohibition of the free movement of my personal data within the Union barred when its reason is the protection of natural persons?",
  c="Under Article 1(3), as a controller, is a restriction or prohibition of the free movement of the personal data I process within the Union barred when its reason is the protection of natural persons?",
  fn="Art 1(3) the restriction",
  cases=[[T, T, T, JT],   # a national rule bans sending the data to another Member State for data protection reasons
         [T, T, F, NO],   # the ban is for another reason (public security): outside the provision
         [F, T, T, NO],   # the data are going outside the Union
         [T, F, T, NO]])  # there is no ban

Q(id="2(3)a", group="Article 2(3) and (4)", s="Under Article 2(3), as a data subject, does Regulation (EC) No 45/2001 apply to the processing of my personal data?",
  c="Under Article 2(3), as a controller, does Regulation (EC) No 45/2001 apply to my processing of personal data?",
  fn="Art 2(3) Regulation (EC) No 45/2001 applies",
  cases=[[T, JT], [F, NO]])
Q(id="2(3)b", group="Article 2(3) and (4)", s="Under Article 2(3), as a data subject, does this Regulation apply to the processing of my personal data by a Union institution, body, office or agency?",
  c="Under Article 2(3), as a controller, does this Regulation apply to my processing of personal data, where I am a Union institution, body, office or agency?",
  fn="Art 2(3) this Regulation applies to the processing, where",
  cases=[[T, JF], [F, NO]])
Q(id="2(4)", group="Article 2(3) and (4)", s="Under Article 2(4), as a data subject, is this Regulation without prejudice to the application of Directive 2000/31/EC?",
  c="Under Article 2(4), as a controller, is this Regulation without prejudice to the application of Directive 2000/31/EC?",
  fn="Art 2(4) this Regulation is without prejudice",
  cases=[[T, F, JT],   # a dispute about the Directive's application
         [F, T, JT],   # a claim against an intermediary service provider under Articles 12 to 15 of the Directive
         [F, F, NO]])  # some other instrument

Q(id="3(1)", group="Article 3", s="Under Article 3(1), as a data subject, is the establishment limb met for the processing of my personal data?",
  c="Under Article 3(1), as a controller, is the establishment limb met for my processing of personal data?",
  fn="Art 3(1) the territorial limb",
  cases=[[T, T, JT], [T, F, JT], [F, T, NO]])
Q(id="3(2)", group="Article 3", s="Under Article 3(2), as a data subject, is the limb of data subjects in the Union and a controller or processor not established there met for the processing of my personal data?",
  c="Under Article 3(2), as a controller, is the limb of data subjects in the Union and a controller or processor not established there met for my processing of personal data?",
  fn="Art 3(2) the territorial limb",
  cases=[[T, T, T, F, F, F, JT],   # (a) goods or services offered free
         [T, T, T, T, F, F, JT],   # (a) a payment is required
         [T, T, F, F, T, T, JT],   # (b) behaviour monitored in the Union
         [T, T, F, F, T, F, JF],   # monitoring of behaviour outside the Union only
         [F, T, T, F, T, T, NO],   # the data subject is not in the Union
         [T, F, T, F, T, T, NO]])  # the controller is established in the Union
Q(id="3(3)", group="Article 3", s="Under Article 3(3), as a data subject, is the limb of a place where Member State law applies by virtue of public international law met for the processing of my personal data?",
  c="Under Article 3(3), as a controller, is the limb of a place where Member State law applies by virtue of public international law met for my processing of personal data?",
  fn="Art 3(3) the territorial limb",
  cases=[[T, T, JT], [T, F, NO], [F, T, NO]])
Q(id="3", group="Article 3", s="Under Article 3, as a data subject, does this Regulation apply to the processing of my personal data?",
  c="Under Article 3, as a controller, does this Regulation apply to my processing of personal data?",
  fn="Art 3 this Regulation applies to the processing of personal data",
  # inputs: material (Y), unionBody, ctx1, takesPlace, dsIn, notEst2, offering, payment, monitoring, behaviourIn, notEst3, place3
  cases=[[Yes, F, T, T, F, F, F, F, F, F, F, F, JT],   # an establishment in the Union
         [Yes, F, F, F, T, T, T, F, F, F, F, F, JT],   # 3(2)(a)
         [Yes, F, F, F, T, T, F, F, T, T, F, F, JT],   # 3(2)(b)
         [Yes, F, F, F, F, F, F, F, F, F, T, T, JT],   # 3(3)
         [Yes, F, F, F, F, F, F, F, F, F, F, F, NO],   # none of the three limbs
         [Yes, T, T, T, F, F, F, F, F, F, F, F, JF],   # processing by a Union body
         [No, F, T, T, F, F, F, F, F, F, F, F, JF],    # outside the material scope
         [Unsure, F, T, T, F, F, F, F, F, F, F, F, NO]])

Q(id="4lead", group="Article 4", c="Under Article 4, as a controller, do the definitions of Article 4 apply to a term I use?",
  fn="Art 4 lead-in", cases=[[T, JT], [F, NO]])
Q(id="4(3)", group="Article 4", s="Under Article 4(3), as a data subject, is what was done to my stored personal data a restriction of processing?",
  c="Under Article 4(3), as a controller, is what I did to stored personal data a restriction of processing?",
  fn="Art 4(3) the act",
  cases=[[T, T, T, JT],   # the data are stored, marked, with the aim of limiting their processing in the future
         [T, F, T, JF],   # the data were erased, not marked
         [F, T, T, JF],   # the data were not stored
         [T, T, F, JF]])  # marked for another aim
Q(id="4(4)", group="Article 4", s="Under Article 4(4), as a data subject, was I profiled?",
  c="Under Article 4(4), as a controller, is my processing profiling?",
  fn="Art 4(4) the processing is profiling",
  args=["{0}", "{1}", "(IF {2} THEN (LIST {3}) ELSE EMPTY)", "{4}"],
  # seat inputs: processing of personal data, automated, evaluates aspects (yes/no), which aspect, aspects relate to a natural person
  seat_inputs=[("the processing is processing of personal data", "B", None),
               ("the processing is automated", "B", None),
               ("the personal data are used to evaluate personal aspects relating to a natural person", "B", None),
               ("the personal aspect that is evaluated", "C", "Art 4(4) personal aspect"),
               ("the aspects relate to a natural person", "B", None)],
  cases=[[T, T, T, "Art 4(4) economic situation", T, JT],
         [T, T, T, "Art 4(4) some other personal aspect", T, JT],
         [T, F, T, "Art 4(4) behaviour", T, JF],    # evaluated by hand
         [T, T, F, "Art 4(4) location", T, JF],     # nothing is evaluated
         [F, T, T, "Art 4(4) health", T, JF]])      # not personal data
Q(id="4(5)", group="Article 4", c="Under Article 4(5), as a controller, is my processing pseudonymisation?",
  fn="Art 4(5)",
  cases=[[T, T, T, T, JT], [T, T, F, T, JF], [T, T, T, F, JF], [T, F, T, T, JF]])
Q(id="4(9)a", group="Article 4", s="Under Article 4(9), as a data subject, is the body my personal data were disclosed to a recipient?",
  c="Under Article 4(9), as a controller, is the body I disclose personal data to a recipient?",
  fn="Art 4(9) the body is a recipient",
  cases=[["legal person", T, F, F, F, JT],
         ["public authority", T, F, T, T, JF],     # an authority receiving the data in a particular inquiry under law
         ["legal person", F, F, F, F, JF],         # not disclosed to it
         ["public authority", T, T, F, F, JT],
         ["agency", T, T, T, T, JT]])              # the exception names public authorities only
Q(id="4(9)b", group="Article 4", s="Under Article 4(9), as a data subject, is the processing by a public authority of my personal data that it received in a particular inquiry in compliance with the applicable data protection rules?",
  c="Under Article 4(9), as a controller, is the processing by a public authority of the personal data it received from me in a particular inquiry in compliance with the applicable data protection rules?",
  fn="Art 4(9) the processing by the public authority",
  cases=[["public authority", T, T, T, JT], ["public authority", T, T, F, JF], ["legal person", T, T, F, NO]])
Q(id="4(10)", group="Article 4", s="Under Article 4(10), as a data subject, is the body a third party?",
  c="Under Article 4(10), as a controller, is the body a third party?",
  fn="Art 4(10) the body is a third party",
  cases=[["legal person", F, F, F, F, JT],
         ["natural person", T, F, F, F, JF],     # the data subject
         ["legal person", F, T, F, F, JF],       # the controller
         ["legal person", F, F, T, F, JF],       # the processor
         ["natural person", F, F, F, T, JF]])    # an employee authorised to process under the controller's direct authority
Q(id="4(11)", group="Article 4", s="Under Article 4(11), as a data subject, did I give consent?",
  c="Under Article 4(11), as a controller, is what the data subject gave me consent?",
  fn="Art 4(11) the indication",
  cases=[[T, T, T, T, T, "Art 4(11) by a statement", T, JT],
         [T, T, T, T, T, "Art 4(11) by a clear affirmative action", T, JT],
         [T, T, T, T, T, "Art 4(11) in some other way, with no statement and no clear affirmative action", T, JF],   # silence or a pre-ticked box
         [T, T, F, T, T, "Art 4(11) by a clear affirmative action", T, JF],                                         # not informed
         [F, T, T, T, T, "Art 4(11) by a statement", T, JF],                                                        # not freely given
         [T, T, T, T, T, "Art 4(11) by a statement", F, JF]])                                                       # agreement not to the processing
Q(id="4(12)", group="Article 4", s="Under Article 4(12), as a data subject, is what happened to my personal data a personal data breach?",
  c="Under Article 4(12), as a controller, is the incident a personal data breach?",
  fn="Art 4(12) the incident",
  args=["{0}", "(LIST {1})", "{2}"],
  seat_inputs=[("there is a breach of security", "B", None),
               ("what the breach of security leads to", "C", "Art 4(12) consequence of a breach of security"),
               ("the personal data are transmitted, stored or otherwise processed", "B", None)],
  cases=[[T, "Art 4(12) unauthorised access to personal data", T, JT],
         [T, "Art 4(12) accidental loss of personal data", T, JT],
         [T, "Art 4(12) some other consequence", T, JF],
         [F, "Art 4(12) unauthorised disclosure of personal data", T, JF]])
Q(id="4(13)", group="Article 4", s="Under Article 4(13), as a data subject, are my personal data genetic data?",
  c="Under Article 4(13), as a controller, are the data genetic data?",
  fn="Art 4(13) the data are genetic data",
  cases=[[T, T, T, T, JT], [T, T, T, F, JT], [T, F, T, T, JF]])
Q(id="4(14)", group="Article 4", s="Under Article 4(14), as a data subject, are my personal data biometric data?",
  c="Under Article 4(14), as a controller, are the data biometric data?",
  fn="Art 4(14) the data are biometric data",
  cases=[[T, T, T, T, T, JT], [T, F, T, T, T, JF], [T, T, T, F, F, JF]])
Q(id="4(15)", group="Article 4", s="Under Article 4(15), as a data subject, are my personal data data concerning health?",
  c="Under Article 4(15), as a controller, are the data data concerning health?",
  fn="Art 4(15) the data are data concerning health",
  cases=[[T, T, F, T, JT], [T, F, T, T, JT], [T, T, T, F, JF]])
Q(id="4(13-15)", group="Article 4", s="Under Article 4(13) to (15), as a data subject, which category of Article 9(1) do my personal data fall in by the definitions of genetic data, biometric data and data concerning health?",
  c="Under Article 4(13) to (15), as a controller, which category of Article 9(1) do the data fall in by the definitions of genetic data, biometric data and data concerning health?",
  fn="Art 4(13) to (15) the category",
  result="MAYBE `Art 9(1) category of personal data`",
  cases=[[Yes, No, F, No, "J:Art 9(1) genetic data"],
         [No, Yes, T, No, "J:Art 9(1) biometric data for the purpose of uniquely identifying a natural person"],
         [No, Yes, F, No, "J:Art 9(1) biometric data not for the purpose of uniquely identifying a natural person"],
         [No, No, F, Yes, "J:Art 9(1) data concerning health"],
         [Yes, No, F, Yes, "J:Art 9(1) genetic data"],
         [No, No, F, No, NO],
         [Unsure, Unsure, F, Unsure, NO]])
Q(id="4(16)a", group="Article 4", c="Under Article 4(16)(a), as a controller, where is my main establishment?",
  fn="Art 4(16)(a) the main establishment",
  result="MAYBE `Art 4(16) which establishment is the main establishment`",
  cases=[[T, T, F, F, "J:Art 4(16)(a) the place of the controller's central administration in the Union"],
         [T, T, T, T, "J:Art 4(16)(a) the establishment of the controller that took the decisions on the purposes and means"],
         [F, T, F, F, NO]])
Q(id="4(16)b", group="Article 4", c="Under Article 4(16)(b), as a controller, where is the main establishment of my processor?",
  fn="Art 4(16)(b) the main establishment",
  result="MAYBE `Art 4(16) which establishment is the main establishment`",
  cases=[[T, T, F, F, "J:Art 4(16)(b) the place of the processor's central administration in the Union"],
         [T, F, T, T, "J:Art 4(16)(b) the establishment of the processor in the Union where the main processing activities take place"],
         [T, F, T, F, NO]])
Q(id="4(17)", group="Article 4", s="Under Article 4(17), as a data subject, is the person a representative?",
  c="Under Article 4(17), as a controller, is the person I designated a representative?",
  fn="Art 4(17) the person",
  cases=[["legal person", T, T, T, JT], ["legal person", F, T, T, JF], ["public authority", T, T, T, JF]])
Q(id="4(18)", group="Article 4", c="Under Article 4(18), as a controller, is my body an enterprise?",
  fn="Art 4(18) the body",
  cases=[["legal person", T, F, F, JT], ["natural person", F, F, F, JF], ["other body", F, T, T, JT], ["other body", T, F, F, NO]])
Q(id="4(19)", group="Article 4", c="Under Article 4(19), as a controller, is the set of undertakings I belong to a group of undertakings?",
  fn="Art 4(19) the set", cases=[[T, T, JT], [T, F, JF]])
Q(id="4(20)", group="Article 4", c="Under Article 4(20), as a controller, are my data protection policies binding corporate rules?",
  fn="Art 4(20) the policies", cases=[[T, T, T, T, T, F, JT], [T, T, T, T, F, F, JF]])
Q(id="4(21)", group="Article 4", s="Under Article 4(21), as a data subject, is the body a supervisory authority?",
  c="Under Article 4(21), as a controller, is the body a supervisory authority?",
  fn="Art 4(21) the body",
  cases=[["public authority", T, T, T, JT], ["public authority", F, T, T, JF], ["other body", T, T, T, JF]])
Q(id="4(22)", group="Article 4", s="Under Article 4(22), as a data subject, is the supervisory authority a supervisory authority concerned by the processing of my personal data?",
  c="Under Article 4(22), as a controller, is the supervisory authority a supervisory authority concerned by my processing?",
  fn="Art 4(22) the supervisory authority",
  cases=[[T, T, F, F, F, JT], [T, F, F, F, T, JT], [T, F, F, F, F, JF]])
Q(id="4(23)", group="Article 4", c="Under Article 4(23), as a controller, is my processing cross-border processing?",
  fn="Art 4(23) the processing",
  cases=[[T, T, T, F, F, F, JT], [T, F, F, T, T, F, JT], [T, F, F, T, F, F, JF]])
Q(id="4(24)", group="Article 4", c="Under Article 4(24), as a controller, is the objection to the draft decision about me a relevant and reasoned objection?",
  fn="Art 4(24) the objection",
  cases=[[T, T, T, F, F, JT], [T, T, T, T, F, JF], [F, T, T, F, F, JF]])
Q(id="4(25)", group="Article 4", s="Under Article 4(25), as a data subject, is the service an information society service?",
  c="Under Article 4(25), as a controller, is my service an information society service?",
  fn="Art 4(25) the service", cases=[[T, JT], [F, JF]])
Q(id="4(26)", group="Article 4", s="Under Article 4(26), as a data subject, is the body my personal data went to an international organisation?",
  c="Under Article 4(26), as a controller, is the body I transfer personal data to an international organisation?",
  fn="Art 4(26) the body", cases=[[T, F, JT], [F, T, JT], [F, F, JF]])

# ---- generation ------------------------------------------------------------------------------------
ROLES = {"s": ("subject", "a data subject", "As far as you can tell, is it the case that {fact}?"),
         "c": ("controller", "a controller", "Is it the case, for your processing, that {fact}?")}


def fact_of(name):
    m = re.match(r"^(Art [^ ]+(?: and \([^)]*\))?) (the .*)$", name)
    if m:
        return "%s (%s)" % (m.group(2), m.group(1))
    return name


def cap(s):
    return s[0].upper() + s[1:]


def arg_expr(i, name, kind, role):
    q = name if re.match(r"^[A-Za-z]\w*$", name) else "`%s`" % name
    if kind == "Y":
        return "(`K2 %s answer as a yes or no` %s)" % (role, q)
    return q


def value_expr(v, kind, role):
    if kind == "B":
        return v
    if kind == "Y":
        return "`K2 %s answer: %s`" % (role, v)
    if kind == "C":
        return "`%s`" % v
    raise Exception(kind)


def expect_expr(e):
    if e.startswith("J:"):
        return "JUST `%s`" % e[2:]
    return e


def decide_name(text):
    return text.rstrip("?")


files = {}
for key in ("s", "c"):
    role, phrase, bool_desc = ROLES[key]
    seat = []
    seat.append("IMPORT prelude\nIMPORT `gdpr-core`\nIMPORT `gdpr-core-2`\nIMPORT `gdpr-definitions-2`\nIMPORT `K2-art-1`\nIMPORT `K2-art-2b`\nIMPORT `K2-art-3`\n")
    if role == "subject":
        who = "A DATA SUBJECT, the natural person whose personal data are processed"
    else:
        who = "A CONTROLLER, the body that determines the purposes and means of the processing"
    seat.append("""-- ============================================================================
-- K2-seat-%(role)s.l4 -- THE SEAT LAYER OF K2 FOR %(who)s.
-- Written by K2 (Sonnet 5.5); produced from the layer-1 signatures by notes/gen-seats.py.
-- SEAT: %(who)s.  Every question is phrased as that person asks it and takes plain inputs: a yes or
-- no, a choice from a list, or yes, no or not sure where a combining rule takes a MAYBE (not sure is
-- treated as not covered).  Nothing here is new law, and no rule is restated: every answer is a call on a
-- layer-1 rule of gdpr-definitions-2.l4, K2-art-1.l4, K2-art-2b.l4 or K2-art-3.l4.
-- Questions are grouped under § headings in the Regulation's order.
-- HOW TO READ A RESULT.  JUST TRUE and JUST FALSE are answers the Regulation gives in its own words; NOTHING
-- means it does not answer on these facts (NOTES: Reading a result).  Never read NOTHING as no.
-- THERE IS NO SEAT FOR AN AUTHORITY.  Provisions that address only an authority or the lawmaker (Art 2(3)
-- second sentence, Art 4(24) for the objection's author) are encoded in layer 1 and reach this seat only through
-- the questions below, for what they mean to the person.
-- ============================================================================
""" % dict(role=role, who=who))
    seat.append("""-- Yes, no or not sure, for a fact that a combining rule takes as a MAYBE.
DECLARE `K2 %(role)s answer` IS ONE OF
    `K2 %(role)s answer: yes`
    `K2 %(role)s answer: no`
    `K2 %(role)s answer: not sure`

GIVEN answer IS A `K2 %(role)s answer`
GIVETH A MAYBE BOOLEAN
`K2 %(role)s answer as a yes or no` MEANS
    CONSIDER answer
    WHEN `K2 %(role)s answer: yes` THEN JUST TRUE -- input mapping
    WHEN `K2 %(role)s answer: no` THEN JUST FALSE -- input mapping
    WHEN `K2 %(role)s answer: not sure` THEN NOTHING -- input mapping
""" % dict(role=role))
    seat.append("§ `Regulation (EU) 2016/679, Chapter I -- my questions as %s`\n" % phrase)
    cases = []
    cases.append("IMPORT prelude\nIMPORT `gdpr-core`\nIMPORT `gdpr-core-2`\nIMPORT `K2-seat-%s`\n" % role)
    cases.append("""-- ============================================================================
-- K2-cases-seat-%(role)s.l4 -- cases for the questions of K2-seat-%(role)s.l4, with the facts a real person in the
-- seat would state.  Every expected value was written by hand from the text of the provision named in the
-- comment above its group of cases (notes/gen-seats.py holds them); none was copied from an output.
-- ============================================================================
""" % dict(role=role))
    last_group = None
    n_q = n_c = 0
    for q in QS:
        if key not in q:
            continue
        fname, fins, fres = find_fn(q["fn"])
        sins = q.get("seat_inputs", fins)
        if len(sins) != len(fins) and "args" not in q:
            raise Exception(("arity", q["id"]))
        kinds = [k for (_, k, _) in sins]
        names = [n for (n, _, _) in sins]
        if q["group"] != last_group:
            seat.append("")
            seat.append("§§ `%s`" % q["group"])
            seat.append("")
            cases.append("")
            cases.append("§§ `%s`" % q["group"])
            cases.append("")
            last_group = q["group"]
        text = q[key]
        n_q += 1
        # inputs
        gl = []
        for idx, (n, k, ty) in enumerate(sins):
            qn = n if re.match(r"^[A-Za-z]\w*$", n) else "`%s`" % n
            if k == "B":
                desc = bool_desc.format(fact=fact_of(n)) + " Answer true or false."
                tyexpr = "BOOLEAN"
            elif k == "Y":
                desc = bool_desc.format(fact=fact_of(n)) + " Answer K2 %s answer: yes, K2 %s answer: no or K2 %s answer: not sure (not sure is treated as not covered)." % (role, role, role)
                tyexpr = "A `K2 %s answer`" % role
            elif k == "C":
                desc = "%s: choose exactly one of: %s." % (cap(n), "; ".join(enums[ty]))
                tyexpr = "A `%s`" % ty
            else:
                raise Exception(("list input needs a seat_inputs override", q["id"], n))
            gl.append("%s%s IS %s @desc %s" % ("GIVEN " if idx == 0 else "      ", qn, tyexpr if tyexpr.startswith("A ") else "A " + tyexpr, desc))
        exprs = [arg_expr(i, n, k, role) for i, (n, k, _) in enumerate(sins)]
        if "args" in q:
            call_args = " ".join(a.format(*exprs) for a in q["args"])
        else:
            call_args = " ".join(exprs)
        result = q.get("result", "MAYBE BOOLEAN")
        dn = decide_name(text)
        seat.append("-- %s: %s" % (q["id"], fname))
        seat.append("@export %s" % text)
        seat.extend(gl)
        seat.append("GIVETH A %s" % result)
        seat.append("DECIDE `%s` IS" % dn)
        seat.append("    `%s` %s" % (fname, call_args))
        seat.append("")
        # cases
        cases.append("-- %s: %s" % (q["id"], fname))
        for c in q["cases"]:
            vals, exp = c[:-1], c[-1]
            assert len(vals) == len(sins), (q["id"], c, len(sins))
            vs = " ".join(value_expr(v, k, role) for v, k in zip(vals, kinds))
            cases.append("#ASSERT `%s` %s EQUALS %s" % (dn, vs, expect_expr(exp)))
            n_c += 1
        cases.append("")
    files["K2-seat-%s.l4" % role] = "\n".join(seat)
    files["K2-cases-seat-%s.l4" % role] = "\n".join(cases)
    print(role, n_q, "questions,", n_c, "cases")

# ---- the mirror file ------------------------------------------------------------------------------
mir = ["IMPORT prelude\nIMPORT `gdpr-core`\nIMPORT `gdpr-core-2`\nIMPORT `K2-seat-subject`\nIMPORT `K2-seat-controller`\n",
       """-- ============================================================================
-- K2-cases-mirror.l4 -- the same facts put to the data subject's seat and the controller's seat, asserting that
-- the two answers are equal.  Only the questions that both seats ask are mirrored; the facts of each case
-- are those of the questions' own cases (notes/gen-seats.py), and each case's value is also asserted in
-- the two cases files.  A seat asks yes, no or not sure in its own type, so the values are mapped.
-- ============================================================================
"""]
n_m = 0
for q in QS:
    if "s" not in q or "c" not in q:
        continue
    fname, fins, fres = find_fn(q["fn"])
    sins = q.get("seat_inputs", fins)
    kinds = [k for (_, k, _) in sins]
    mir.append("-- %s: %s" % (q["id"], fname))
    for c in q["cases"]:
        vals = c[:-1]
        vs_s = " ".join(value_expr(v, k, "subject") for v, k in zip(vals, kinds))
        vs_c = " ".join(value_expr(v, k, "controller") for v, k in zip(vals, kinds))
        mir.append("#ASSERT (`%s` %s) EQUALS (`%s` %s)" % (decide_name(q["s"]), vs_s, decide_name(q["c"]), vs_c))
        n_m += 1
    mir.append("")
files["K2-cases-mirror.l4"] = "\n".join(mir)
print("mirror", n_m, "assertions")

for f, s in files.items():
    open(f, "w", encoding="utf-8").write(s.rstrip("\n") + "\n")
