# Specs of ss 376B-376EE for gen_offences.py (pass of 2026-11-04).  Raw line numbers are PC1871.txt's.
SECTIONS = []
FALSE_KIND = 'FALSE-kind (the text says no in its own words): '

# --------------------------------------------------------------------------------------------- 376B
O1 = "the accused obtains for consideration the sexual services of a person"
O2 = "the accused communicates with another person for the purpose of obtaining for consideration the sexual services of a person"
U18 = "the person whose sexual services are in question is below 18 years of age"
SS = "the services are sexual services within section 376B(4)"
SP = "the sexual services were obtained from the accused's spouse"
SECTIONS.append(dict(
    sec="376B", title="commercial sex with minor below 18 years of age", quote=(8359, 8385),
    notes=["Subsection (4) defines \"sexual services\" (a closed list, \"means\"): `s 376B(4) the services are sexual services`, below.",
           "Subsection (3) bars both offences for services obtained from the accused's spouse (\"an offence under this section\")."],
    record="Commercial Sex Facts",
    victim="The name of the person whose sexual services were obtained or sought, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by paying the said minor $200 for sexual intercourse\"",
    leaves=[
        (O1, "Did the accused obtain, for consideration, the sexual services of a person? (s 376B(1))"),
        (O2, "Did the accused communicate with another person for the purpose of obtaining, for consideration, the sexual services of a person? (s 376B(2))"),
        (U18, "Was the person whose sexual services were obtained or sought below 18 years of age? Set from the helper `below 18 years of age` on that person's age"),
        (SS, "Are the services \"sexual services\" as s 376B(4) gives the meaning - involving sexual penetration of the vagina or anus by a part of another person's body (other than the penis) or by anything else, penetration of the vagina, anus or mouth by a man's penis, or touching which is sexual? Set from `s 376B(4) the services are sexual services`"),
        (SP, "Were the sexual services obtained from the accused's own spouse? (s 376B(3): then there is no offence under the section)"),
    ],
    defs=[
        dict(name="obtains the sexual services of a person below 18 years of age within section 376B(1)", lines=(8361, 8363),
             export="Whether the accused commits the offence in section 376B(1) of the Penal Code 1871 (obtaining for consideration the sexual services of a person below 18 years of age)",
             conj=[("Any person who obtains for consideration the sexual services of a person, who is below 18 years of age", "[%s] AND [%s] AND [%s]" % (O1, SS, U18), "the accused obtains for consideration the sexual services of a person below 18 years of age"),
                   ("(3) No person shall be guilty of an offence under this section for any sexual services obtained from that person's spouse", "NOT [%s]" % SP, "the sexual services were not obtained from the accused's spouse (section 376B(3))", FALSE_KIND + '"No person shall be guilty of an offence under this section for any sexual services obtained from that person\'s spouse"')]),
        dict(name="communicates to obtain the sexual services of a person below 18 years of age within section 376B(2)", lines=(8365, 8368),
             export="Whether the accused commits the offence in section 376B(2) of the Penal Code 1871 (communicating for the purpose of obtaining for consideration the sexual services of a person below 18 years of age)",
             conj=[("Any person who communicates with another person for the purpose of obtaining for consideration, the sexual services of a person who is below 18 years of age", "[%s] AND [%s] AND [%s]" % (O2, SS, U18), "the accused communicates with another person for the purpose of obtaining for consideration the sexual services of a person below 18 years of age"),
                   ("(3) No person shall be guilty of an offence under this section for any sexual services obtained from that person's spouse", "NOT [%s]" % SP, "the sexual services were not obtained from the accused's spouse (section 376B(3))", FALSE_KIND + '"No person shall be guilty of an offence under this section for any sexual services obtained from that person\'s spouse"')]),
    ],
    offences=[
        dict(label="376B(1)", lines=(8361, 8363), punish=["376B(1)"],
             export_offence="Whether the accused has committed an offence punishable under section 376B(1) of the Penal Code 1871 (commercial sex with a minor below 18 years of age)",
             export_charge="Frame a charge under section 376B(1) of the Penal Code 1871 (commercial sex with a minor below 18 years of age), or say why none can be framed",
             offence_quote="shall be punished with imprisonment for a term which may extend to 7 years, or with fine, or with both",
             defn="`obtains the sexual services of a person below 18 years of age within section 376B(1)` f",
             punish_expr="`punishment prescribed by s 376B(1)`'s words", charge_name="commercial sex with minor below 18 years of age",
             miss_from=["obtains the sexual services of a person below 18 years of age within section 376B(1)"],
             charge_body='CONCAT "did obtain for consideration the sexual services of ", {v}, ", a person below 18 years of age, to wit, ", {m}'),
        dict(label="376B(2)", lines=(8365, 8368), punish=["376B(2)"],
             export_offence="Whether the accused has committed an offence punishable under section 376B(2) of the Penal Code 1871 (communicating to obtain commercial sex with a minor below 18 years of age)",
             export_charge="Frame a charge under section 376B(2) of the Penal Code 1871 (communicating to obtain commercial sex with a minor below 18 years of age), or say why none can be framed",
             offence_quote="shall be punished with imprisonment for a term which may extend to 2 years, or with fine, or with both",
             defn="`communicates to obtain the sexual services of a person below 18 years of age within section 376B(2)` f",
             punish_expr="`punishment prescribed by s 376B(2)`'s words", charge_name="communicating to obtain commercial sex with minor below 18 years of age",
             miss_from=["communicates to obtain the sexual services of a person below 18 years of age within section 376B(2)"],
             charge_body='CONCAT "did communicate with another person for the purpose of obtaining for consideration the sexual services of ", {v}, ", a person below 18 years of age, to wit, ", {m}'),
    ],
))

# --------------------------------------------------------------------------------------------- 376C
CIT = "the accused is a citizen or a permanent resident of Singapore"
OUT = "the accused does the act outside Singapore"
INS = "the accused does the act in Singapore"
B18 = "the act involves a person below 18 years of age"
BOUT = "the person below 18 years of age is outside Singapore"
BIN = "the person below 18 years of age is in Singapore"
ACT = "the act that would, if done in Singapore, constitute an offence under section 376B"
SECTIONS.append(dict(
    sec="376C", title="commercial sex with minor below 18 years of age outside Singapore", quote=(8387, 8409),
    notes=["The act \"that would, if done in Singapore, constitute an offence under section 376B\" is read over a nested",
           "`Commercial Sex Facts` for the same act, which the caller supplies (FORK DEF-B2). The punishment is borrowed from s 376B (subsection (2)):",
           "the charge states the words of s 376B(1) or s 376B(2), whichever offence the nested facts make out."],
    record="Commercial Sex Abroad Facts",
    victim="The name of the person below 18 years of age involved in the act, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by paying the said minor in Batam for sexual intercourse\"",
    leaves=[
        (CIT, "Is the accused a citizen or a permanent resident of Singapore? (s 376C(1))"),
        (OUT, "Did the accused do the act outside Singapore? (s 376C(1), (1B))"),
        (INS, "Did the accused do the act in Singapore? (s 376C(1A))"),
        (B18, "Does the act involve a person below 18 years of age? (s 376C(1A), (1B))"),
        (BOUT, "Is that person outside Singapore? (s 376C(1A))"),
        (BIN, "Is that person in Singapore? (s 376C(1B))"),
        (ACT, "The facts of the same act, read as if it were done in Singapore (or, in s 376C(1A), as if B were in Singapore): would they constitute an offence under s 376B? Supply them as `Commercial Sex Facts`", "Commercial Sex Facts"),
    ],
    defs=[dict(name="does an act that would be an offence under section 376B within section 376C", lines=(8389, 8401),
               export="Whether the accused commits the offence in section 376C of the Penal Code 1871 (an act that would constitute an offence under section 376B, done outside Singapore by a citizen or permanent resident; done in Singapore involving a minor who is outside it; or done outside Singapore involving a minor who is in it)",
               conj=[("(1) Any person, being a citizen or a permanent resident of Singapore, who does, outside Singapore, any act that would, if done in Singapore, constitute an offence under section 376B; (1A) any person (A) who does in Singapore, any act involving a person below 18 years of age (B) who is outside Singapore, that would if B were in Singapore constitute an offence under section 376B; (1B) any person who does outside Singapore, any act involving a person below 18 years of age who is in Singapore, that would if done in Singapore constitute an offence under section 376B, shall be guilty of an offence",
                      "([%s] AND [%s]) OR ([%s] AND [%s] AND [%s]) OR ([%s] AND [%s] AND [%s])" % (CIT, OUT, INS, B18, BOUT, OUT, B18, BIN), "the accused is a citizen or permanent resident who acts outside Singapore; or acts in Singapore involving a person below 18 who is outside Singapore; or acts outside Singapore involving a person below 18 who is in Singapore"),
                     (None, "(`offence under s 376B(1)` ([%s])) OR (`offence under s 376B(2)` ([%s]))" % (ACT, ACT), "the act would, if done in Singapore, constitute an offence under section 376B")])],
    offences=[dict(label="376C(2)", lines=(8405, 8407), punish=[],
                   export_offence="Whether the accused has committed an offence punishable under section 376C(2) of the Penal Code 1871 (commercial sex with a minor below 18 years of age, outside Singapore)",
                   export_charge="Frame a charge under section 376C(2) of the Penal Code 1871 (commercial sex with a minor below 18 years of age, outside Singapore), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under this section shall be punished with the same punishment with which he would have been punished had he been convicted of an offence under section 376B",
                   defn="`does an act that would be an offence under section 376B within section 376C` f",
                   punish_expr="IF (`offence under s 376B(1)` ([%s])) THEN `punishment prescribed by s 376B(1)`'s words ELSE `punishment prescribed by s 376B(2)`'s words" % ACT,
                   charge_name="commercial sex with minor below 18 years of age outside Singapore",
                   miss_from=["does an act that would be an offence under section 376B within section 376C"],
                   charge_body='CONCAT (IF [%s] THEN "being a citizen or a permanent resident of Singapore, did outside Singapore an act, to wit, " ELSE (IF [%s] THEN "did in Singapore an act involving " ELSE "did outside Singapore an act involving ")), (IF [%s] THEN "" ELSE CONCAT {v}, ", a person below 18 years of age, "), "which would, if done in Singapore, constitute an offence under section 376B of the Penal Code 1871, to wit, ", {m}' % (CIT, INS, CIT))],
))

# --------------------------------------------------------------------------------------------- 376D
TA = "the accused makes or organises travel arrangements for or on behalf of any other person"
TAI = "the accused makes or organises the travel arrangements with the intention of facilitating the commission by that other person of an offence under section 376C"
TT = "the accused transports any other person to a place outside Singapore"
TTI = "the accused transports that person with the intention of facilitating the commission by that other person of an offence under section 376C"
PI = "the accused prints, publishes or distributes information"
PP = "the information is intended to promote conduct that would constitute an offence under section 376C, or to assist any other person to engage in such conduct"
SECTIONS.append(dict(
    sec="376D", title="tour outside Singapore for commercial sex with minor below 18 years of age", quote=(8411, 8438),
    notes=["Whether the offence under s 376C is \"actually committed by that other person\" is immaterial: the ladder has no leaf for it."],
    record="Travel for Commercial Sex Facts",
    victim="The name of the other person for whom the arrangements were made or whom the accused transported (leave blank for information published to the public)",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by booking flights and a hotel in Phnom Penh for the said person\"",
    leaves=[
        (TA, "Did the accused make or organise travel arrangements for or on behalf of any other person? (s 376D(1)(a))"),
        (TAI, "Did the accused do so with the intention of facilitating the commission by that other person of an offence under s 376C, whether or not it is actually committed? (s 376D(1)(a))"),
        (TT, "Did the accused transport any other person to a place outside Singapore? (s 376D(1)(b))"),
        (TTI, "Did the accused do so with the intention of facilitating the commission by that other person of an offence under s 376C, whether or not it is actually committed? (s 376D(1)(b))"),
        (PI, "Did the accused print, publish or distribute information? Publication is by any means, whether written, electronic or other form of communication (s 376D(2); see `s 376D(2) the means of publication`) (s 376D(1)(c))"),
        (PP, "Was the information intended to promote conduct that would constitute an offence under s 376C, or to assist any other person to engage in such conduct? (s 376D(1)(c))"),
    ],
    defs=[dict(name="organises a tour for commercial sex with a minor within section 376D", lines=(8413, 8429),
               export="Whether the accused commits the offence in section 376D(1) of the Penal Code 1871 (making travel arrangements for, transporting, or publishing information to promote, an offence under section 376C)",
               conj=[("Any person who (a) makes or organises any travel arrangements for or on behalf of any other person with the intention of facilitating the commission by that other person of an offence under section 376C, whether or not such an offence is actually committed by that other person; (b) transports any other person to a place outside Singapore with the intention of facilitating the commission by that other person of an offence under section 376C; or (c) prints, publishes or distributes any information that is intended to promote conduct that would constitute an offence under section 376C, or to assist any other person to engage in such conduct, shall be guilty of an offence",
                      "([%s] AND [%s]) OR ([%s] AND [%s]) OR ([%s] AND [%s])" % (TA, TAI, TT, TTI, PI, PP), "the accused makes or organises travel arrangements with the intention of facilitating an offence under section 376C; or transports a person outside Singapore with that intention; or prints, publishes or distributes information intended to promote conduct that would constitute an offence under section 376C, or to assist another person to engage in it")])],
    offences=[dict(label="376D(3)", lines=(8437, 8438), punish=["376D(3)"],
                   export_offence="Whether the accused has committed an offence punishable under section 376D(3) of the Penal Code 1871 (tour outside Singapore for commercial sex with a minor below 18 years of age)",
                   export_charge="Frame a charge under section 376D(3) of the Penal Code 1871 (tour outside Singapore for commercial sex with a minor below 18 years of age), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 10 years, or with fine, or with both",
                   defn="`organises a tour for commercial sex with a minor within section 376D` f",
                   punish_expr="`punishment prescribed by s 376D(3)`'s words", charge_name="tour outside Singapore for commercial sex with minor below 18 years of age",
                   miss_from=["organises a tour for commercial sex with a minor within section 376D"],
                   charge_body='CONCAT (IF [%s] THEN CONCAT "did make or organise travel arrangements for or on behalf of ", (f\'s victim), " with the intention of facilitating the commission by that person of an offence under section 376C of the Penal Code 1871" ELSE (IF [%s] THEN CONCAT "did transport ", (f\'s victim), " to a place outside Singapore with the intention of facilitating the commission by that person of an offence under section 376C of the Penal Code 1871" ELSE "did print, publish or distribute information intended to promote conduct that would constitute an offence under section 376C of the Penal Code 1871, or to assist another person to engage in such conduct")), ", to wit, ", {m}' % (TA, TT))],
))

# -------------------------------------------------------------------------------- 376E and 376EA
A18 = "A is of or above 18 years of age"
PREV = "A has met or communicated with B on at least one previous occasion"
M1 = "A intentionally meets B in Singapore"
M2 = "A travels in Singapore with the intention of meeting B in Singapore"
M3 = "A travels from a location in Singapore with the intention of meeting B outside Singapore"
M4 = "B travels in Singapore to attend a meeting with A in Singapore which A has either initiated or agreed to whether expressly or by implication"
M5 = "B travels from a location in Singapore to attend a meeting with A outside Singapore which A has either initiated or agreed to whether expressly or by implication"
I1 = "A intends, during or after the meeting, to do in Singapore anything to or in respect of B which will involve the commission by A of a relevant offence"
I2 = "A intends, during or after the meeting, to do outside Singapore anything to or in respect of B which would, if done in Singapore, involve the commission by A of a relevant offence"
MEET = "([%s] OR [%s] OR [%s] OR [%s] OR [%s])" % (M1, M2, M3, M4, M5)
INTENT = "([%s] OR [%s])" % (I1, I2)
MEETS = [(M1, "Does A intentionally meet B in Singapore? (s %s(1)(a)(i))"), (M2, "Does A travel in Singapore with the intention of meeting B in Singapore? (s %s(1)(a)(ii))"),
         (M3, "Does A travel from a location in Singapore with the intention of meeting B outside Singapore? (s %s(1)(a)(iii))"),
         (M4, "Does B travel in Singapore to attend a meeting with A in Singapore which A has either initiated or agreed to, expressly or by implication? (s %s(1)(a)(iv))"),
         (M5, "Does B travel from a location in Singapore to attend a meeting with A outside Singapore which A has either initiated or agreed to, expressly or by implication? (s %s(1)(a)(v))")]


def grooming(sec, title, quote, def_lines, off_lines, record, bage, bage_desc, nb, nb_desc, extra, punish_ids, punish_expr, relevant_fn, charge_band):
    leaves = [(A18, "Is the accused (A) of or above 18 years of age? Set from NOT `below 18 years of age` on A's age"),
              (PREV, "Had A met or communicated with B on at least one previous occasion? It is immaterial whether that occasion was in or outside Singapore (s %s(3))" % sec)]
    leaves += [(a, b % sec) for (a, b) in MEETS]
    leaves += [(I1, "At the time of those acts, did A intend, during or after the meeting, to do (in Singapore) anything to or in respect of B which will involve A committing a relevant offence? The offence must be one of those `%s` lists (s %s(1)(b)(i)(A))" % (relevant_fn, sec)),
               (I2, "At the time of those acts, did A intend, during or after the meeting, to do (outside Singapore) anything to or in respect of B which would, if done in Singapore, involve A committing a relevant offence? (s %s(1)(b)(i)(B))" % sec),
               (bage, bage_desc), (nb, nb_desc)]
    leaves += extra
    conj = [(None, "[%s]" % A18, "A is of or above 18 years of age"),
            (None, "[%s]" % PREV, "A has met or communicated with B on at least one previous occasion"),
            ("(a) any of the following acts takes place: (i) A intentionally meets B in Singapore; (ii) A travels in Singapore with the intention of meeting B in Singapore; (iii) A travels from a location in Singapore with the intention of meeting B outside Singapore; (iv) B travels in Singapore to attend a meeting with A in Singapore which A has either initiated or agreed to whether expressly or by implication; (v) B travels from a location in Singapore to attend a meeting with A outside Singapore which A has either initiated or agreed to whether expressly or by implication", MEET, "one of the five meeting acts takes place"),
            ("(b)(i) A intends, during or after the meeting, (A) to do (in Singapore) anything to or in respect of B which will involve the commission by A of a relevant offence; or (B) to do (outside Singapore) anything to or in respect of B which would, if done in Singapore, involve the commission by A of a relevant offence", INTENT, "A intends, during or after the meeting, to do anything to or in respect of B which would involve A committing a relevant offence"),
            (None, "[%s]" % bage, bage_desc.split("?")[0] + "" if False else None),
            (None, "[%s]" % nb, None)]
    for e in extra:
        conj.append((None, "[%s]" % e[0], None))
    return leaves, conj


# 376E
L, C = grooming("376E", "sexual grooming of minor below 16 years of age", (8440, 8521), (8442, 8482), (8507, 8518), "Grooming Facts",
                "B is below 16 years of age", "Is B below 16 years of age at the time of the acts? Set from the helper `below 16 years of age` on B's age (s 376E(1)(b)(ii))",
                "A does not reasonably believe that B is of or above 16 years of age", "Does A NOT reasonably believe that B is of or above 16 years of age? (s 376E(1)(b)(iii))",
                [("B is below 14 years of age and A does not reasonably believe that B is of or above 14 years of age", "Is B below 14 years of age, and does A NOT reasonably believe B is of or above that age? NOT an element: it chooses which punishment s 376E(4) states (7 years, or 5 years)")],
                [], "", "s 376E(2) the offence is a relevant offence", "")
L = [l for l in L]
C = [(c[0], c[1], c[2] or c[1][1:-1]) for c in C]
# the last conjunct is the punishment-band leaf, which is not an element
C = C[:-1]
SECTIONS.append(dict(
    sec="376E", title="sexual grooming of minor below 16 years of age", quote=(8440, 8521),
    notes=["\"Relevant offence\" (subsection (2), a closed list) is `s 376E(2) the offence is a relevant offence`, below: the two intent leaves are set from it.",
           "Subsection (3) makes the place of the previous occasion immaterial; there is no leaf for it."],
    record="Grooming Facts",
    victim="The name of the child (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by travelling to a hotel to meet the said child, intending to have sexual intercourse with her\"",
    leaves=L,
    defs=[dict(name="sexually grooms a minor below 16 years of age within section 376E(1)", lines=(8442, 8482),
               export="Whether the accused commits the offence in section 376E(1) of the Penal Code 1871 (sexual grooming of a minor below 16 years of age)",
               conj=C)],
    offences=[dict(label="376E(4)", lines=(8507, 8518), punish=["376E(4)(a)", "376E(4)(b)"],
                   export_offence="Whether the accused has committed an offence punishable under section 376E(4) of the Penal Code 1871 (sexual grooming of a minor below 16 years of age)",
                   export_charge="Frame a charge under section 376E(4) of the Penal Code 1871 (sexual grooming of a minor below 16 years of age), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under this section shall on conviction be punished",
                   defn="`sexually grooms a minor below 16 years of age within section 376E(1)` f",
                   punish_expr="IF [B is below 14 years of age and A does not reasonably believe that B is of or above 14 years of age] THEN `punishment prescribed by s 376E(4)(a)`'s words ELSE `punishment prescribed by s 376E(4)(b)`'s words",
                   charge_name="sexual grooming of minor below 16 years of age",
                   miss_from=["sexually grooms a minor below 16 years of age within section 376E(1)"],
                   charge_body='CONCAT "being of or above 18 years of age, having met or communicated with ", {v}, ", a person below 16 years of age, on at least one previous occasion, did, with the intention of doing in respect of the said person something that would involve the commission by you of a relevant offence, and not reasonably believing the said person to be of or above 16 years of age, bring about a meeting between you and the said person, to wit, ", {m}')],
))

# 376EA
EXP = "A is in a relationship that is exploitative of B"
L, C = grooming("376EA", "exploitative sexual grooming of minor of or above 16 but below 18 years of age", (8523, 8602), (8525, 8568), (8598, 8599), "Exploitative Grooming Facts",
                "B is of or above 16 but below 18 years of age", "Is B of or above 16 but below 18 years of age at the time of the acts? Set from the helper `of or above 16 years of age but below 18 years of age` on B's age (s 376EA(1)(b)(ii))",
                "A does not reasonably believe that B is of or above 18 years of age", "Does A NOT reasonably believe that B is of or above 18 years of age? (s 376EA(1)(b)(iii))",
                [(EXP, "Is A in a relationship that is exploitative of B, as the court determines under s 377CA? (s 376EA(1)(b)(iv))")],
                [], "", "s 376EA(2) the offence is a relevant offence", "")
C = [(c[0], c[1], c[2] or c[1][1:-1]) for c in C]
SECTIONS.append(dict(
    sec="376EA", title="exploitative sexual grooming of minor of or above 16 but below 18 years of age", quote=(8523, 8602),
    notes=["\"Relevant offence\" (subsection (2), a closed list) is `s 376EA(2) the offence is a relevant offence`, below.",
           "Subsection (3) makes the place of the previous occasion immaterial; there is no leaf for it."],
    record="Exploitative Grooming Facts",
    victim="The name of the child (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by travelling to a flat to meet the said child, intending to have sexual intercourse with her\"",
    leaves=L,
    defs=[dict(name="exploitatively sexually grooms a minor within section 376EA(1)", lines=(8525, 8568),
               export="Whether the accused commits the offence in section 376EA(1) of the Penal Code 1871 (exploitative sexual grooming of a minor of or above 16 but below 18 years of age)",
               conj=C)],
    offences=[dict(label="376EA(4)", lines=(8598, 8599), punish=["376EA(4)"],
                   export_offence="Whether the accused has committed an offence punishable under section 376EA(4) of the Penal Code 1871 (exploitative sexual grooming of a minor of or above 16 but below 18 years of age)",
                   export_charge="Frame a charge under section 376EA(4) of the Penal Code 1871 (exploitative sexual grooming of a minor of or above 16 but below 18 years of age), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 5 years, or with fine, or with both",
                   defn="`exploitatively sexually grooms a minor within section 376EA(1)` f",
                   punish_expr="`punishment prescribed by s 376EA(4)`'s words",
                   charge_name="exploitative sexual grooming of minor of or above 16 but below 18 years of age",
                   miss_from=["exploitatively sexually grooms a minor within section 376EA(1)"],
                   charge_body='CONCAT "being of or above 18 years of age, in a relationship that is exploitative of ", {v}, ", a person of or above 16 but below 18 years of age, having met or communicated with the said person on at least one previous occasion, did, with the intention of doing in respect of the said person something that would involve the commission by you of a relevant offence, and not reasonably believing the said person to be of or above 18 years of age, bring about a meeting between you and the said person, to wit, ", {m}')],
))

# --------------------------------------------------------------------------------------------- 376EB
COMM = "A intentionally communicated with B"
GRAT = "A communicated for the purpose of obtaining sexual gratification"
HUM = "A communicated for the purpose of causing B humiliation, alarm or distress"
SEXC = "the communication is sexual"
B16 = "B is below 16 years of age"
NB16 = "A does not reasonably believe that B is of or above 16 years of age"
SGC = "either A or B was in Singapore at the time of the communication"
REPL = "B replied or responded to A's communication"
SPC = "the communication was with the accused's spouse with the consent of that spouse"
AGG14 = "B is below 14 years of age and A does not reasonably believe that B is of or above 14 years of age"
SECTIONS.append(dict(
    sec="376EB", title="sexual communication with minor below 16 years of age", quote=(8604, 8646),
    notes=["Subsection (2)(a): whether B replied is immaterial, so the leaf is carried and ignored (FORK DEF-B3).",
           "Subsection (2)(b): where the communication originated is immaterial \"provided that either A or B was in Singapore\", read as a condition (FORK DEF-B3)."],
    record="Sexual Communication Facts",
    victim="The name of the child (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by sending the said child messages describing sexual acts\"",
    leaves=[
        (A18, "Is the accused (A) of or above 18 years of age? Set from NOT `below 18 years of age` on A's age"),
        (COMM, "Did A intentionally communicate with B? (s 376EB(1)(a))"),
        (GRAT, "Was the purpose of the communication to obtain sexual gratification? (s 376EB(1)(a))"),
        (HUM, "Was the purpose of the communication to cause B humiliation, alarm or distress? (s 376EB(1)(a))"),
        (SEXC, "Is the communication sexual - as s 377C(3)(d) says when a communication is sexual? (s 376EB(1)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (B16, "Was B below 16 years of age at the time of the communication? Set from the helper `below 16 years of age` on B's age (s 376EB(1)(c))"),
        (NB16, "Does A NOT reasonably believe that B is of or above 16 years of age? (s 376EB(1)(d))"),
        (SGC, "Was either A or B in Singapore at the time of the communication? Where the communication originated is immaterial, provided that this is so (s 376EB(2)(b))"),
        (REPL, "Did B reply or respond to A's communication? NOT an element: s 376EB(2)(a) says it is immaterial, so the answer changes nothing"),
        (SPC, "Was the communication with A's spouse, with that spouse's consent? (s 376EB(4): then there is no offence under the section)"),
        (AGG14, "Is B below 14 years of age, and does A NOT reasonably believe B is of or above that age? NOT an element: it chooses which punishment s 376EB(3) states (3 years, or 2 years)"),
    ],
    defs=[dict(name="sexually communicates with a minor below 16 years of age within section 376EB(1)", lines=(8606, 8617),
               export="Whether the accused commits the offence in section 376EB(1) of the Penal Code 1871 (sexual communication with a minor below 16 years of age)",
               conj=[(None, "[%s]" % A18, "A is of or above 18 years of age"),
                     ("(a) for the purpose of obtaining sexual gratification or of causing another person (B) humiliation, alarm or distress, A intentionally communicated with B", "[%s] AND ([%s] OR [%s])" % (COMM, GRAT, HUM), "for the purpose of obtaining sexual gratification or of causing B humiliation, alarm or distress, A intentionally communicated with B"),
                     ("(b) the communication is sexual", "[%s]" % SEXC, "the communication is sexual"),
                     ("(c) at the time of the communication, B is below 16 years of age; and (d) A does not reasonably believe that B is of or above 16 years of age", "[%s] AND [%s]" % (B16, NB16), "at the time of the communication B is below 16 years of age and A does not reasonably believe that B is of or above 16 years of age"),
                     ("(2)(b) whether such communication originated in Singapore provided that either A or B was in Singapore at the time of such communication", "[%s]" % SGC, "either A or B was in Singapore at the time of the communication"),
                     ("(4) No person shall be guilty of an offence under this section for any communication with his or her spouse with the consent of that spouse", "NOT [%s]" % SPC, "the communication was not with the accused's spouse with that spouse's consent (section 376EB(4))", FALSE_KIND + '"No person shall be guilty of an offence under this section for any communication with his or her spouse with the consent of that spouse"')])],
    offences=[dict(label="376EB(3)", lines=(8631, 8639), punish=["376EB(3)(a)", "376EB(3)(b)"],
                   export_offence="Whether the accused has committed an offence punishable under section 376EB(3) of the Penal Code 1871 (sexual communication with a minor below 16 years of age)",
                   export_charge="Frame a charge under section 376EB(3) of the Penal Code 1871 (sexual communication with a minor below 16 years of age), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under this section shall be punished",
                   defn="`sexually communicates with a minor below 16 years of age within section 376EB(1)` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 376EB(3)(a)`'s words ELSE `punishment prescribed by s 376EB(3)(b)`'s words" % AGG14,
                   charge_name="sexual communication with minor below 16 years of age",
                   miss_from=["sexually communicates with a minor below 16 years of age within section 376EB(1)"],
                   charge_body='CONCAT "being of or above 18 years of age, for the purpose of obtaining sexual gratification or of causing humiliation, alarm or distress to ", {v}, ", a person below 16 years of age, did intentionally communicate with the said person in a sexual communication, not reasonably believing the said person to be of or above 16 years of age, to wit, ", {m}')],
))

# --------------------------------------------------------------------------------------------- 376EC
B1618 = "B is of or above 16 but below 18 years of age"
NB18 = "A does not reasonably believe that B is of or above 18 years of age"
EXPB = "B is in a relationship with A that is exploitative of B"
SECTIONS.append(dict(
    sec="376EC", title="exploitative sexual communication with minor of or above 16 but below 18 years of age", quote=(8649, 8683),
    notes=["Subsection (2) is carried as in s 376EB (FORK DEF-B3)."],
    record="Exploitative Sexual Communication Facts",
    victim="The name of the child (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by sending the said child messages describing sexual acts\"",
    leaves=[
        (A18, "Is the accused (A) of or above 18 years of age? Set from NOT `below 18 years of age` on A's age"),
        (COMM, "Did A intentionally communicate with B? (s 376EC(1)(a))"),
        (GRAT, "Was the purpose of the communication to obtain sexual gratification? (s 376EC(1)(a))"),
        (HUM, "Was the purpose of the communication to cause B humiliation, alarm or distress? (s 376EC(1)(a))"),
        (SEXC, "Is the communication sexual - as s 377C(3)(d) says when a communication is sexual? (s 376EC(1)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (B1618, "Was B of or above 16 but below 18 years of age at the time of the communication? Set from the helper `of or above 16 years of age but below 18 years of age` on B's age (s 376EC(1)(c))"),
        (NB18, "Does A NOT reasonably believe that B is of or above 18 years of age? (s 376EC(1)(d))"),
        (EXPB, "Is B in a relationship with A that is exploitative of B, as the court determines under s 377CA? (s 376EC(1)(e))"),
        (SGC, "Was either A or B in Singapore at the time of the communication? Where the communication originated is immaterial, provided that this is so (s 376EC(2)(b))"),
        (REPL, "Did B reply or respond to A's communication? NOT an element: s 376EC(2)(a) says it is immaterial, so the answer changes nothing"),
    ],
    defs=[dict(name="exploitatively sexually communicates with a minor within section 376EC(1)", lines=(8652, 8666),
               export="Whether the accused commits the offence in section 376EC(1) of the Penal Code 1871 (exploitative sexual communication with a minor of or above 16 but below 18 years of age)",
               conj=[(None, "[%s]" % A18, "A is of or above 18 years of age"),
                     ("(a) for the purpose of obtaining sexual gratification or of causing another person (B) humiliation, alarm or distress, A intentionally communicated with B", "[%s] AND ([%s] OR [%s])" % (COMM, GRAT, HUM), "for the purpose of obtaining sexual gratification or of causing B humiliation, alarm or distress, A intentionally communicated with B"),
                     ("(b) the communication is sexual", "[%s]" % SEXC, "the communication is sexual"),
                     ("(c) at the time of the communication, B is of or above 16 but below 18 years of age; (d) A does not reasonably believe that B is of or above 18 years of age; and (e) B is in a relationship with A that is exploitative of B", "[%s] AND [%s] AND [%s]" % (B1618, NB18, EXPB), "at the time of the communication B is of or above 16 but below 18 years of age, A does not reasonably believe B is of or above 18, and B is in a relationship with A that is exploitative of B"),
                     ("(2)(b) whether such communication originated in Singapore provided that either A or B was in Singapore at the time of such communication", "[%s]" % SGC, "either A or B was in Singapore at the time of the communication")])],
    offences=[dict(label="376EC(3)", lines=(8680, 8681), punish=["376EC(3)"],
                   export_offence="Whether the accused has committed an offence punishable under section 376EC(3) of the Penal Code 1871 (exploitative sexual communication with a minor of or above 16 but below 18 years of age)",
                   export_charge="Frame a charge under section 376EC(3) of the Penal Code 1871 (exploitative sexual communication with a minor of or above 16 but below 18 years of age), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 2 years, or with fine, or with both",
                   defn="`exploitatively sexually communicates with a minor within section 376EC(1)` f",
                   punish_expr="`punishment prescribed by s 376EC(3)`'s words",
                   charge_name="exploitative sexual communication with minor of or above 16 but below 18 years of age",
                   miss_from=["exploitatively sexually communicates with a minor within section 376EC(1)"],
                   charge_body='CONCAT "being of or above 18 years of age, in a relationship that is exploitative of ", {v}, ", a person of or above 16 but below 18 years of age, for the purpose of obtaining sexual gratification or of causing humiliation, alarm or distress to the said person, did intentionally communicate with the said person in a sexual communication, not reasonably believing the said person to be of or above 18 years of age, to wit, ", {m}')],
))

# --------------------------------------------------------------------------------------------- 376ED
ENG = "A intentionally engages in an activity"
ACTG = "A engaged in the activity for the purpose of obtaining sexual gratification"
ACTH = "A engaged in the activity for the purpose of causing B humiliation, alarm or distress"
SEXA = "the activity is sexual"
PRES = "B is present or is in a place from which A can be observed"
SGP = "either A or B is or both are in Singapore"
AWARE = "A knows or believes that B is aware, or intends that B should be aware, that A is engaging in it"
CAUSE = "A intentionally causes B to observe an image"
IMGG = "A caused B to observe the image for the purpose of obtaining sexual gratification"
IMGH = "A caused B to observe the image for the purpose of causing B humiliation, alarm or distress"
SEXI = "the image is sexual"
SPA = "B is the accused's spouse and consented to the activity"
SECTIONS.append(dict(
    sec="376ED", title="sexual activity or image in presence of minor below 16 years of age", quote=(8685, 8744),
    notes=["Two offences, (1) activity and (2) image, one punishment, (3) (FORK DEF-B4: subsection (4)'s spouse bar is read as covering both)."],
    record="Sexual Activity Facts",
    victim="The name of the child (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by masturbating in front of the said child\"",
    leaves=[
        (A18, "Is the accused (A) of or above 18 years of age? Set from NOT `below 18 years of age` on A's age"),
        (ENG, "Did A intentionally engage in an activity? (s 376ED(1)(a))"),
        (ACTG, "Was the purpose of A's engaging in the activity to obtain sexual gratification? (s 376ED(1)(a))"),
        (ACTH, "Was the purpose of A's engaging in the activity to cause B humiliation, alarm or distress? (s 376ED(1)(a))"),
        (SEXA, "Is the activity sexual - as s 377C(3)(d) says when an activity is sexual? (s 376ED(1)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (PRES, "Did A engage in it when B was present or in a place from which A could be observed? (s 376ED(1)(c)(i))"),
        (SGP, "Was either A or B, or were both, in Singapore? (s 376ED(1)(c)(ii), (2)(e))"),
        (AWARE, "Did A know or believe that B was aware, or intend that B should be aware, that A was engaging in it? (s 376ED(1)(c)(iii))"),
        (CAUSE, "Did A intentionally cause B to observe an image? (s 376ED(2)(a))"),
        (IMGG, "Was the purpose of A's causing B to observe the image to obtain sexual gratification? (s 376ED(2)(a))"),
        (IMGH, "Was the purpose of A's causing B to observe the image to cause B humiliation, alarm or distress? (s 376ED(2)(a))"),
        (SEXI, "Is the image sexual - as s 377C(3)(d) says when an image is sexual? (s 376ED(2)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (B16, "Is B below 16 years of age? Set from the helper `below 16 years of age` on B's age (s 376ED(1)(d), (2)(c))"),
        (NB16, "Does A NOT reasonably believe that B is of or above 16 years of age? (s 376ED(1)(e), (2)(d))"),
        (SPA, "Is B A's spouse, and did that spouse consent to the activity or to observing the image? (s 376ED(4): then there is no offence under the section against B)"),
        (AGG14, "Is B below 14 years of age, and does A NOT reasonably believe B is of or above that age? NOT an element: it chooses which punishment s 376ED(3) states (3 years, or 2 years)"),
    ],
    defs=[
        dict(name="engages in a sexual activity in the presence of a minor below 16 years of age within section 376ED(1)", lines=(8687, 8707),
             export="Whether the accused commits the offence in section 376ED(1) of the Penal Code 1871 (sexual activity in the presence of a minor below 16 years of age)",
             conj=[(None, "[%s]" % A18, "A is of or above 18 years of age"),
                   ("(a) for the purpose of obtaining sexual gratification or of causing another person (B) humiliation, alarm or distress, A intentionally engages in an activity", "[%s] AND ([%s] OR [%s])" % (ENG, ACTG, ACTH), "for the purpose of obtaining sexual gratification or of causing B humiliation, alarm or distress, A intentionally engages in an activity"),
                   ("(b) the activity is sexual", "[%s]" % SEXA, "the activity is sexual"),
                   ("(c) A engages in the activity (i) when B is present or is in a place from which A can be observed; (ii) when either A or B is or both are in Singapore; and (iii) knowing or believing that B is aware, or intending that B should be aware, that A is engaging in it", "[%s] AND [%s] AND [%s]" % (PRES, SGP, AWARE), "A engages in the activity when B is present or can observe A, when either or both are in Singapore, knowing or believing that B is aware, or intending that B should be aware"),
                   ("(d) B is below 16 years of age; and (e) A does not reasonably believe that B is of or above 16 years of age", "[%s] AND [%s]" % (B16, NB16), "B is below 16 years of age and A does not reasonably believe that B is of or above 16 years of age"),
                   ("(4) No person shall be guilty of an offence under this section against B if B is his or her spouse with the consent of that spouse", "NOT [%s]" % SPA, "B is not the accused's spouse consenting (section 376ED(4))", FALSE_KIND + '"No person shall be guilty of an offence under this section against B if B is his or her spouse with the consent of that spouse"')]),
        dict(name="causes a minor below 16 years of age to observe a sexual image within section 376ED(2)", lines=(8711, 8723),
             export="Whether the accused commits the offence in section 376ED(2) of the Penal Code 1871 (causing a minor below 16 years of age to observe a sexual image)",
             conj=[(None, "[%s]" % A18, "A is of or above 18 years of age"),
                   ("(a) for the purpose of obtaining sexual gratification or of causing another person (B) humiliation, alarm or distress, A intentionally causes B to observe an image", "[%s] AND ([%s] OR [%s])" % (CAUSE, IMGG, IMGH), "for the purpose of obtaining sexual gratification or of causing B humiliation, alarm or distress, A intentionally causes B to observe an image"),
                   ("(b) the image is sexual", "[%s]" % SEXI, "the image is sexual"),
                   ("(c) B is below 16 years of age; (d) A does not reasonably believe that B is of or above 16 years of age; and (e) either A or B is or both are in Singapore", "[%s] AND [%s] AND [%s]" % (B16, NB16, SGP), "B is below 16 years of age, A does not reasonably believe B is of or above 16, and either or both are in Singapore"),
                   ("(4) No person shall be guilty of an offence under this section against B if B is his or her spouse with the consent of that spouse", "NOT [%s]" % SPA, "B is not the accused's spouse consenting (section 376ED(4))", FALSE_KIND + '"No person shall be guilty of an offence under this section against B if B is his or her spouse with the consent of that spouse"')]),
    ],
    offences=[
        dict(label="376ED(1)", lines=(8727, 8736), punish=["376ED(3)(a)", "376ED(3)(b)"],
             export_offence="Whether the accused has committed an offence punishable under section 376ED(3) of the Penal Code 1871 by a sexual activity in the presence of a minor below 16 years of age",
             export_charge="Frame a charge under section 376ED(1) of the Penal Code 1871 (sexual activity in the presence of a minor below 16 years of age), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under this section shall be punished",
             defn="`engages in a sexual activity in the presence of a minor below 16 years of age within section 376ED(1)` f",
             punish_expr="IF [%s] THEN `punishment prescribed by s 376ED(3)(a)`'s words ELSE `punishment prescribed by s 376ED(3)(b)`'s words" % AGG14,
             charge_name="sexual activity in presence of minor below 16 years of age",
             miss_from=["engages in a sexual activity in the presence of a minor below 16 years of age within section 376ED(1)"],
             charge_body='CONCAT "being of or above 18 years of age, for the purpose of obtaining sexual gratification or of causing humiliation, alarm or distress to ", {v}, ", a person below 16 years of age, did intentionally engage in a sexual activity when the said person was present or in a place from which you could be observed, knowing or believing, or intending, that the said person was aware of it, not reasonably believing the said person to be of or above 16 years of age, to wit, ", {m}'),
        dict(label="376ED(2)", lines=(8727, 8736), punish=[],
             export_offence="Whether the accused has committed an offence punishable under section 376ED(3) of the Penal Code 1871 by causing a minor below 16 years of age to observe a sexual image",
             export_charge="Frame a charge under section 376ED(2) of the Penal Code 1871 (causing a minor below 16 years of age to observe a sexual image), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under this section shall be punished",
             defn="`causes a minor below 16 years of age to observe a sexual image within section 376ED(2)` f",
             punish_expr="IF [%s] THEN `punishment prescribed by s 376ED(3)(a)`'s words ELSE `punishment prescribed by s 376ED(3)(b)`'s words" % AGG14,
             charge_name="causing minor below 16 years of age to observe a sexual image",
             miss_from=["causes a minor below 16 years of age to observe a sexual image within section 376ED(2)"],
             charge_body='CONCAT "being of or above 18 years of age, for the purpose of obtaining sexual gratification or of causing humiliation, alarm or distress to ", {v}, ", a person below 16 years of age, did intentionally cause the said person to observe a sexual image, not reasonably believing the said person to be of or above 16 years of age, to wit, ", {m}'),
    ],
))

# --------------------------------------------------------------------------------------------- 376EE
SECTIONS.append(dict(
    sec="376EE", title="exploitative sexual activity or image in presence of minor of or above 16 but below 18 years of age", quote=(8746, 8798),
    notes=["Two offences, (1) activity and (2) image, one punishment, (3)."],
    record="Exploitative Sexual Activity Facts",
    victim="The name of the child (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by showing the said child a pornographic film\"",
    leaves=[
        (A18, "Is the accused (A) of or above 18 years of age? Set from NOT `below 18 years of age` on A's age"),
        (ENG, "Did A intentionally engage in an activity? (s 376EE(1)(a))"),
        (ACTG, "Was the purpose of A's engaging in the activity to obtain sexual gratification? (s 376EE(1)(a))"),
        (ACTH, "Was the purpose of A's engaging in the activity to cause B humiliation, alarm or distress? (s 376EE(1)(a))"),
        (SEXA, "Is the activity sexual - as s 377C(3)(d) says? (s 376EE(1)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (PRES, "Did A engage in it when B was present or in a place from which A could be observed? (s 376EE(1)(c)(i))"),
        (SGP, "Was either A or B, or were both, in Singapore? (s 376EE(1)(c)(ii), (2)(f))"),
        (AWARE, "Did A know or believe that B was aware, or intend that B should be aware, that A was engaging in it? (s 376EE(1)(c)(iii))"),
        (CAUSE, "Did A intentionally cause B to observe an image? (s 376EE(2)(a))"),
        (IMGG, "Was the purpose of A's causing B to observe the image to obtain sexual gratification? (s 376EE(2)(a))"),
        (IMGH, "Was the purpose of A's causing B to observe the image to cause B humiliation, alarm or distress? (s 376EE(2)(a))"),
        (SEXI, "Is the image sexual - as s 377C(3)(d) says? (s 376EE(2)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (B1618, "Is B of or above 16 but below 18 years of age? Set from the helper `of or above 16 years of age but below 18 years of age` on B's age (s 376EE(1)(d), (2)(c))"),
        (NB18, "Does A NOT reasonably believe that B is of or above 18 years of age? (s 376EE(1)(e), (2)(d))"),
        ("A is in a relationship with B that is exploitative of B", "Is A in a relationship with B that is exploitative of B, as the court determines under s 377CA? (s 376EE(1)(f), (2)(e))"),
    ],
    defs=[
        dict(name="engages in a sexual activity in the presence of a minor in an exploitative relationship within section 376EE(1)", lines=(8749, 8771),
             export="Whether the accused commits the offence in section 376EE(1) of the Penal Code 1871 (sexual activity in the presence of a minor of or above 16 but below 18 years of age in an exploitative relationship)",
             conj=[(None, "[%s]" % A18, "A is of or above 18 years of age"),
                   ("(a) for the purpose of obtaining sexual gratification or of causing another person (B) humiliation, alarm or distress, A intentionally engages in an activity", "[%s] AND ([%s] OR [%s])" % (ENG, ACTG, ACTH), "for the purpose of obtaining sexual gratification or of causing B humiliation, alarm or distress, A intentionally engages in an activity"),
                   ("(b) the activity is sexual", "[%s]" % SEXA, "the activity is sexual"),
                   ("(c) A engages in the activity (i) when B is present or is in a place from which A can be observed; (ii) when either A or B is or both are in Singapore; and (iii) knowing or believing that B is aware, or intending that B should be aware, that A is engaging in it", "[%s] AND [%s] AND [%s]" % (PRES, SGP, AWARE), "A engages in the activity when B is present or can observe A, when either or both are in Singapore, knowing or believing that B is aware, or intending that B should be aware"),
                   ("(d) B is of or above 16 but below 18 years of age; (e) A does not reasonably believe that B is of or above 18 years of age; and (f) A is in a relationship with B that is exploitative of B", "[%s] AND [%s] AND [A is in a relationship with B that is exploitative of B]" % (B1618, NB18), "B is of or above 16 but below 18 years of age, A does not reasonably believe B is of or above 18, and A is in a relationship with B that is exploitative of B")]),
        dict(name="causes a minor in an exploitative relationship to observe a sexual image within section 376EE(2)", lines=(8775, 8789),
             export="Whether the accused commits the offence in section 376EE(2) of the Penal Code 1871 (causing a minor of or above 16 but below 18 years of age in an exploitative relationship to observe a sexual image)",
             conj=[(None, "[%s]" % A18, "A is of or above 18 years of age"),
                   ("(a) for the purpose of obtaining sexual gratification or of causing another person (B) humiliation, alarm or distress, A intentionally causes B to observe an image", "[%s] AND ([%s] OR [%s])" % (CAUSE, IMGG, IMGH), "for the purpose of obtaining sexual gratification or of causing B humiliation, alarm or distress, A intentionally causes B to observe an image"),
                   ("(b) the image is sexual", "[%s]" % SEXI, "the image is sexual"),
                   ("(c) B is of or above 16 but below 18 years of age; (d) A does not reasonably believe that B is of or above 18 years of age; (e) A is in a relationship with B that is exploitative of B; and (f) either A or B is or both are in Singapore", "[%s] AND [%s] AND [A is in a relationship with B that is exploitative of B] AND [%s]" % (B1618, NB18, SGP), "B is of or above 16 but below 18 years of age, A does not reasonably believe B is of or above 18, A is in a relationship with B that is exploitative of B, and either or both are in Singapore")]),
    ],
    offences=[
        dict(label="376EE(1)", lines=(8793, 8795), punish=["376EE(3)"],
             export_offence="Whether the accused has committed an offence punishable under section 376EE(3) of the Penal Code 1871 by a sexual activity in the presence of a minor in an exploitative relationship",
             export_charge="Frame a charge under section 376EE(1) of the Penal Code 1871 (exploitative sexual activity in the presence of a minor of or above 16 but below 18 years of age), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 2 years, or with fine, or with both",
             defn="`engages in a sexual activity in the presence of a minor in an exploitative relationship within section 376EE(1)` f",
             punish_expr="`punishment prescribed by s 376EE(3)`'s words",
             charge_name="exploitative sexual activity in presence of minor of or above 16 but below 18 years of age",
             miss_from=["engages in a sexual activity in the presence of a minor in an exploitative relationship within section 376EE(1)"],
             charge_body='CONCAT "being of or above 18 years of age, in a relationship that is exploitative of ", {v}, ", a person of or above 16 but below 18 years of age, for the purpose of obtaining sexual gratification or of causing humiliation, alarm or distress to the said person, did intentionally engage in a sexual activity when the said person was present or in a place from which you could be observed, knowing or believing, or intending, that the said person was aware of it, not reasonably believing the said person to be of or above 18 years of age, to wit, ", {m}'),
        dict(label="376EE(2)", lines=(8793, 8795), punish=[],
             export_offence="Whether the accused has committed an offence punishable under section 376EE(3) of the Penal Code 1871 by causing a minor in an exploitative relationship to observe a sexual image",
             export_charge="Frame a charge under section 376EE(2) of the Penal Code 1871 (exploitative causing of a minor of or above 16 but below 18 years of age to observe a sexual image), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 2 years, or with fine, or with both",
             defn="`causes a minor in an exploitative relationship to observe a sexual image within section 376EE(2)` f",
             punish_expr="`punishment prescribed by s 376EE(3)`'s words",
             charge_name="exploitative causing of minor of or above 16 but below 18 years of age to observe a sexual image",
             miss_from=["causes a minor in an exploitative relationship to observe a sexual image within section 376EE(2)"],
             charge_body='CONCAT "being of or above 18 years of age, in a relationship that is exploitative of ", {v}, ", a person of or above 16 but below 18 years of age, for the purpose of obtaining sexual gratification or of causing humiliation, alarm or distress to the said person, did intentionally cause the said person to observe a sexual image, not reasonably believing the said person to be of or above 18 years of age, to wit, ", {m}'),
    ],
))
