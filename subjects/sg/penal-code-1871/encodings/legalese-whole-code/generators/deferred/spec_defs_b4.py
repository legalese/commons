# Definitions, rules of reading and defences of ss 377BB-377C, for gen_defs.py (pass of 2026-11-04).
DEFS = []


def d(**k):
    DEFS.append(k)


# ------------------------------------------------------------------------------------------- 377C
d(sec="377C", ref='s 377C(1) "buttocks"', whole=True, lines=(9911, 9911), name='s 377C(1) the region is within "buttocks"',
  export='Whether a region is within "buttocks" in relation to a person, section 377C(1) of the Penal Code 1871: it includes the anal region',
  params=[("it is the anal region of the person", "Is the region the anal region of the person?")],
  expr="[it is the anal region of the person]", shape="includes", quote='"buttocks", in relation to a person, includes the anal region of the person')

d(sec="377C", ref='s 377C(1) "child abuse material"', lines=(9915, 9947), name='s 377C(1) the material is child abuse material',
  export='Whether material is "child abuse material" within section 377C(1) of the Penal Code 1871: material that depicts an image of a person who is, or appears to a reasonable observer to be, or is implied to be, below 16 years of age, as a victim of abuse, in a sexual pose or activity, or in the presence of another in one; or the sexual and offensive depiction of the genital region, buttocks or (if female) breasts of such a person',
  params=[("it is material within the definition in section 377C(1)", "Is the thing \"material\" - see `s 377C(1) the thing is material`?"),
          ("the person depicted is, or appears to a reasonable observer to be, or is implied to be, below 16 years of age", "Is the person depicted below 16 years of age, or does the person appear to a reasonable observer to be, or is the person implied to be, below 16?"),
          ("any child was involved in the production of the material", "Was any child involved in the production of the material? NOT relevant: the definition applies \"whether or not any child was involved\""),
          ("the image is of the person as a victim of torture, cruelty or physical abuse (whether or not the torture, cruelty or abuse is sexual)", "Is the image of the person as a victim of torture, cruelty or physical abuse, whether or not sexual? (s 377C(1) paragraph (a)(i))"),
          ("the image is of the person as a victim of sexual abuse", "Is the image of the person as a victim of sexual abuse? (paragraph (a)(ii))"),
          ("the image is of the person engaged in, or apparently engaging in, a sexual pose or sexual activity (whether or not in the presence of another person)", "Is the image of the person engaged in, or apparently engaging in, a sexual pose or sexual activity, whether or not in the presence of another person? (paragraph (a)(iii))"),
          ("the image is of the person in the presence of another person who is engaged in, or apparently engaged in, a sexual pose or sexual activity", "Is the image of the person in the presence of another person who is engaged in, or apparently engaged in, a sexual pose or sexual activity? (paragraph (a)(iv))"),
          ("the image is of the genital region or buttocks (whether exposed or covered) of the person", "Is the image of the genital region or buttocks (whether exposed or covered) of the person? (paragraph (b))"),
          ("the image is of the breasts (whether exposed or covered) of a female", "Is the image of the breasts (whether exposed or covered) of a female? (paragraph (c))"),
          ("the depiction is sexual", "Is the depiction sexual? See `s 377C(3)(d) the conduct is sexual`"),
          ("reasonable persons would regard the circumstances as offensive", "Are the circumstances (whether or not apparent from the depiction) such that reasonable persons would regard them as offensive?")],
  expr="[it is material within the definition in section 377C(1)] AND [the person depicted is, or appears to a reasonable observer to be, or is implied to be, below 16 years of age] AND ([the image is of the person as a victim of torture, cruelty or physical abuse (whether or not the torture, cruelty or abuse is sexual)] OR [the image is of the person as a victim of sexual abuse] OR [the image is of the person engaged in, or apparently engaging in, a sexual pose or sexual activity (whether or not in the presence of another person)] OR [the image is of the person in the presence of another person who is engaged in, or apparently engaged in, a sexual pose or sexual activity] OR ([the image is of the genital region or buttocks (whether exposed or covered) of the person] AND [the depiction is sexual] AND [reasonable persons would regard the circumstances as offensive]) OR ([the image is of the breasts (whether exposed or covered) of a female] AND [the depiction is sexual] AND [reasonable persons would regard the circumstances as offensive]))",
  shape="means", quote='"child abuse material" means material that depicts an image of any of the following (whether or not any child was involved in the production of the material)')

d(sec="377C", ref='s 377C(1) "distribute"', lines=(9952, 9958), name='s 377C(1) the conduct is distributing',
  export='Whether conduct is "distribute" within section 377C(1) of the Penal Code 1871: it includes sending, publishing, supplying, showing, exhibiting, transmitting or communicating to another person, and making available for viewing or access by another person',
  params=[("the conduct is to send, publish, supply, show, exhibit, transmit or communicate to another person", "Is the conduct to send, publish, supply, show, exhibit, transmit or communicate to another person, in person, electronically, digitally or in any other way?"),
          ("the conduct is to make available for viewing or access by another person", "Is the conduct to make available for viewing or access by another person?")],
  expr="[the conduct is to send, publish, supply, show, exhibit, transmit or communicate to another person] OR [the conduct is to make available for viewing or access by another person]",
  shape="includes", quote='"distribute" includes any of the following conduct')

d(sec="377C", ref='s 377C(2)', lines=(10006, 10008), name='s 377C(2) distributing requires that another person views or gains access to the image',
  export='Whether, under section 377C(2) of the Penal Code 1871, a person is treated as having distributed an image or recording only if another person views or gains access to it: no, whether or not',
  params=[("another person views or gains access to the image", "Did another person view or gain access to the image or recording? The answer changes nothing")],
  shape="flat", quote="a person is treated as having distributed an image or recording whether or not another person views or gains access to the image")

d(sec="377C", ref='s 377C(1) "image"', lines=(9960, 9962), name='s 377C(1) the thing is an image',
  export='Whether a thing is an "image" within section 377C(1) of the Penal Code 1871: a still, moving, recorded or unrecorded image, and any image produced by any means, and where the context requires, a three-dimensional image',
  params=[("it is a still, moving, recorded or unrecorded image", "Is it a still, moving, recorded or unrecorded image?"),
          ("it is an image produced by any means", "Is it an image produced by any means?"),
          ("it is a three-dimensional image and the context requires it to count", "Is it a three-dimensional image, where the context requires?")],
  expr="[it is a still, moving, recorded or unrecorded image] OR [it is an image produced by any means] OR [it is a three-dimensional image and the context requires it to count]",
  shape="includes", quote='"image" means a still, moving, recorded or unrecorded image and includes an image produced by any means and, where the context requires, a three-dimensional image')

d(sec="377C", ref='s 377C(1) "image", in relation to a person', lines=(9964, 9974), name='s 377C(1) the image is an image in relation to a person',
  export='Whether an image is an "image" in relation to a person, section 377C(1) of the Penal Code 1871: an image of a human being who is not fictional or imaginary, or of a fictional or imaginary human being so closely resembling one that an ordinary person would find it difficult to tell the two apart',
  params=[("it is an image of a human being who is not fictional or imaginary (whether identifiable or not)", "Is it an image of a human being who is not fictional or imaginary, whether identifiable or not?"),
          ("it is an image of a fictional or imaginary human being that so closely resembles an image of a human being who is not fictional or imaginary as to make it difficult for an ordinary person to distinguish the two", "Is it an image of a fictional or imaginary human being that so closely resembles an image of a real human being (identifiable or not) that an ordinary person would find it difficult to distinguish the two?")],
  expr="[it is an image of a human being who is not fictional or imaginary (whether identifiable or not)] OR [it is an image of a fictional or imaginary human being that so closely resembles an image of a human being who is not fictional or imaginary as to make it difficult for an ordinary person to distinguish the two]",
  shape="means", quote='"image", in relation to a person, means (a) an image of a human being who is not fictional or imaginary ...; or (b) an image of a fictional or imaginary human being that so closely resembles ...')

d(sec="377C", ref='s 377C(1) "material"', lines=(9978, 9985), name='s 377C(1) the thing is material',
  export='Whether a thing is "material" within section 377C(1) of the Penal Code 1871: a film, photograph, printed matter or computer game depicting an image, an electronic record depicting an image, or any other thing of any kind depicting an image',
  params=[("it is a film, photograph, printed matter or computer game depicting an image", "Is it a film, photograph, printed matter or computer game depicting an image?"),
          ("it is an electronic record depicting an image", "Is it an electronic record depicting an image? \"Electronic record\" has the meaning of the Electronic Transactions Act 2010 (s 29B)"),
          ("it is any other thing of any kind depicting an image", "Is it any other thing of any kind depicting an image?")],
  expr="[it is a film, photograph, printed matter or computer game depicting an image] OR [it is an electronic record depicting an image] OR [it is any other thing of any kind depicting an image]",
  shape="means", quote='"material" means (a) any film, photograph, printed matter or computer game depicting an image; (b) any electronic record depicting an image; or (c) any other thing of any kind depicting an image')

d(sec="377C", ref='s 377C(1) "structure"', lines=(9987, 9988), name='s 377C(1) the thing is a structure',
  export='Whether a thing is a "structure" within section 377C(1) of the Penal Code 1871: it includes a tent, vehicle or vessel or other temporary or movable structure',
  params=[("it is a tent, vehicle or vessel", "Is it a tent, vehicle or vessel?"), ("it is another temporary or movable structure", "Is it another temporary or movable structure?")],
  expr="[it is a tent, vehicle or vessel] OR [it is another temporary or movable structure]", shape="includes", quote='"structure" includes a tent, vehicle or vessel or other temporary or movable structure')

d(sec="377C", ref='s 377C(1) "touching"', lines=(9990, 9999), name='s 377C(1) the act is touching',
  export='Whether an act is "touching" within section 377C(1) of the Penal Code 1871: it includes touching with any part of the body, with anything else, or through anything, and penetration of the vagina or anus with a part of the body or anything else and of the mouth with the penis',
  params=[("it is touching with any part of the body", "Is it touching with any part of the body?"), ("it is touching with anything else", "Is it touching with anything else?"), ("it is touching through anything", "Is it touching through anything?"),
          ("it is penetration of the vagina or anus with a part of the body or anything else", "Is it penetration of the vagina or anus, as the case may be, with a part of the body or anything else?"),
          ("it is penetration of the mouth with the penis", "Is it penetration of the mouth with the penis?")],
  expr="[it is touching with any part of the body] OR [it is touching with anything else] OR [it is touching through anything] OR [it is penetration of the vagina or anus with a part of the body or anything else] OR [it is penetration of the mouth with the penis]",
  shape="includes", quote='"touching" includes touching (a) with any part of the body; (b) with anything else; or (c) through anything, and includes penetration of the vagina or anus ... and penetration of the mouth with the penis')

d(sec="377C", ref='s 377C(1) "vagina"', lines=(10001, 10001), name='s 377C(1) the part is within "vagina"',
  export='Whether a part is within "vagina" in section 377C(1) of the Penal Code 1871: it includes the vulva',
  params=[("it is the vulva", "Is the part the vulva?")], expr="[it is the vulva]", shape="includes", quote='"vagina" includes vulva')

d(sec="377C", ref='s 377C(3)(a)', lines=(10014, 10014), name='s 377C(3)(a) the penetration is continuing',
  export='Whether penetration is continuing at a point of time, section 377C(3)(a) of the Penal Code 1871: it is a continuing act from entry to withdrawal',
  params=[("entry has taken place", "Has entry taken place?"), ("withdrawal has taken place", "Has withdrawal taken place?")],
  expr="[entry has taken place] AND NOT [withdrawal has taken place]", shape="limited", quote="penetration is a continuing act from entry to withdrawal", why="limited by its own wording",
  note="the subsection says the act continues from entry to withdrawal; it does not say what the law is before entry or after withdrawal")

d(sec="377C", ref='s 377C(3)(b)', lines=(10016, 10018), name='s 377C(3)(b) the part is a part of the body',
  export='Whether a part is "a part of the body" in sections 375 to 377BO of the Penal Code 1871, section 377C(3)(b): it includes a part surgically constructed, in particular through a sex reassignment procedure',
  params=[("it is a part which is surgically constructed (in particular, through a sex reassignment procedure)", "Is the part surgically constructed, in particular through a sex reassignment procedure?")],
  expr="[it is a part which is surgically constructed (in particular, through a sex reassignment procedure)]", shape="includes", quote="a reference to a part of the body includes a reference to a part which is surgically constructed")

d(sec="377C", ref='s 377C(3)(d)', lines=(10031, 10037), name='s 377C(3)(d) the conduct is sexual',
  export='Whether penetration, touching, communication or other activity is "sexual" within section 377C(3)(d) of the Penal Code 1871: sexual by its nature whatever the circumstances or purpose, or of a nature that may be sexual and sexual because of the circumstances or the purpose of any person, or both',
  params=[("because of its nature it is sexual, whatever its circumstances or any person's purpose in relation to it may be", "Is it, because of its nature, sexual, whatever its circumstances or any person's purpose in relation to it may be? (s 377C(3)(d)(i))"),
          ("because of its nature it may be sexual", "Is it, because of its nature, something that may be sexual? (s 377C(3)(d)(ii))"),
          ("because of its circumstances or the purpose of any person in relation to it (or both) it is sexual", "Because of its circumstances or the purpose of any person in relation to it (or both), is it sexual? (s 377C(3)(d)(ii))")],
  expr="[because of its nature it is sexual, whatever its circumstances or any person's purpose in relation to it may be] OR ([because of its nature it may be sexual] AND [because of its circumstances or the purpose of any person in relation to it (or both) it is sexual])",
  shape="if", quote="penetration, touching, communication or other activity is \"sexual\" if (i) ...; or (ii) ...")

d(sec="377C", ref='s 377C(3)(e)', lines=(10039, 10040), name='s 377C(3)(e) the observation is observation within the sections',
  export='Whether an observation is "observation" in sections 375 to 377BO of the Penal Code 1871, section 377C(3)(e): observation whether direct or by looking at an image',
  params=[("the observation is direct", "Is the observation direct?"), ("the observation is by looking at an image", "Is the observation by looking at an image?")],
  expr="[the observation is direct] OR [the observation is by looking at an image]", shape="limited", quote="references to observation (however expressed) are to observation whether direct or by looking at an image", why="limited by its own wording",
  note="the subsection names two kinds of observation; it does not say that observation in any other way is not observation")

d(sec="377C", ref='s 377C(3)(f)', lines=(10042, 10053), name='s 377C(3)(f) the person is doing a private act',
  export='Whether a person is "doing a private act" within section 377C(3)(f) of the Penal Code 1871: in circumstances where the person has a reasonable expectation of privacy, the person is in a state of undress or covered only in underwear, is using a toilet, showering or bathing, or is doing a sexual act not ordinarily done in public',
  params=[("the person has a reasonable expectation of privacy in the circumstances", "Does the person have a reasonable expectation of privacy in the circumstances - against what was done? See the Illustration: in an open-concept shower the person cannot expect not to be casually observed, but can expect not to be surreptitiously recorded by a video camera"),
          ("the person is in a state where the person's genital region, buttocks or breasts (if the person is a female) are exposed or covered only in underwear", "Is the person in a state where the person's genital region, buttocks or breasts (if the person is a female) are exposed or covered only in underwear? (s 377C(3)(f)(i))"),
          ("the person is using a toilet, showering or bathing", "Is the person using a toilet, showering or bathing? (s 377C(3)(f)(ii))"),
          ("the person is doing a sexual act that is not of a kind ordinarily done in public", "Is the person doing a sexual act that is not of a kind ordinarily done in public? (s 377C(3)(f)(iii))")],
  expr="[the person has a reasonable expectation of privacy in the circumstances] AND ([the person is in a state where the person's genital region, buttocks or breasts (if the person is a female) are exposed or covered only in underwear] OR [the person is using a toilet, showering or bathing] OR [the person is doing a sexual act that is not of a kind ordinarily done in public])",
  shape="if", quote="a person is doing a private act if under circumstances in which the person has a reasonable expectation of privacy, the person (i) ...; (ii) ...; or (iii) ...")

# ----------------------------------------------------------------------------------------- 377BD
d(sec="377BD", ref='s 377BD(4)(a)', lines=(9238, 9241), name='s 377BD(4)(a) the person has the electronic image in his possession',
  export='Whether a person has in his possession an image or recording in electronic form, section 377BD(4)(a) of the Penal Code 1871: if he controls access to it, whether or not he has physical possession',
  params=[("the image or recording is in electronic form", "Is the image or recording in electronic form?"), ("the person controls access to the electronic image or recording", "Does the person control access to the electronic image or recording, whether or not he has physical possession of it?")],
  expr="[the image or recording is in electronic form] AND [the person controls access to the electronic image or recording]", shape="if",
  quote="a person has in his possession an image or recording of another person that is in electronic form if he controls access to the electronic image or recording")

d(sec="377BD", ref='s 377BD(4)(b)', lines=(9243, 9249), name='s 377BD(4)(b) the way is a way of gaining access',
  export='Whether a way is a way in which a person gains access to an image or recording, section 377BD(4)(b) of the Penal Code 1871: the ways may include viewing or displaying it by an electronic medium, or communicating, sending, supplying or transmitting it to himself or herself',
  params=[("the person views or displays it by an electronic medium, or by any other output of the image by an electronic medium", "Does the person view or display it by an electronic medium or any other output of the image by an electronic medium?"), ("the person communicates, sends, supplies or transmits the image to himself or herself", "Does the person communicate, send, supply or transmit the image to himself or herself?")],
  expr="[the person views or displays it by an electronic medium, or by any other output of the image by an electronic medium] OR [the person communicates, sends, supplies or transmits the image to himself or herself]", shape="includes",
  quote="the ways in which a person gains access to an image or recording may include", note="\"may include\": the ways are not limited to these")

d(sec="377BD", ref='s 377BD(8)', lines=(9276, 9284), name='s 377BD(8) the way is a way of producing material',
  export='Whether a way is a way in which material is produced, section 377BD(8) of the Penal Code 1871: it may include filming, printing, photographing, recording, writing, drawing or otherwise generating material, altering or manipulating material, or reproducing or copying material',
  params=[("the person films, prints, photographs, records, writes, draws or otherwise generates material", "Does the person film, print, photograph, record, write, draw or otherwise generate material?"), ("the person alters or manipulates material", "Does the person alter or manipulate material?"), ("the person reproduces or copies material", "Does the person reproduce or copy material?")],
  expr="[the person films, prints, photographs, records, writes, draws or otherwise generates material] OR [the person alters or manipulates material] OR [the person reproduces or copies material]", shape="includes",
  quote="the ways in which material is produced may include", note="\"may include\": the ways are not limited to these")

# ----------------------------------------------------------------------------------------- 377BE
d(sec="377BE", ref='s 377BE(6)(a)', lines=(9359, 9362), name='s 377BE(6)(a) the prosecution must prove that the image or recording mentioned in the threat exists',
  export='Whether, for an offence under section 377BE(2) of the Penal Code 1871 (a threat to distribute), the prosecution must prove that the image or recording mentioned in the threat exists: it need not',
  params=[("the image or recording mentioned in the threat exists", "Does the image or recording mentioned in the threat exist? The answer changes nothing")],
  shape="flat", quote="it is not necessary for the prosecution to prove (a) that the image or recording mentioned in the threat exists")

d(sec="377BE", ref='s 377BE(6)(b)', lines=(9359, 9365), name='s 377BE(6)(b) the prosecution must prove that the image or recording is in fact an intimate image or recording',
  export='Whether, for an offence under section 377BE(2) of the Penal Code 1871 (a threat to distribute), the prosecution must prove that an existing image or recording is in fact an intimate image or recording: it need not',
  params=[("the image or recording mentioned in the threat is in fact an intimate image or recording", "Is the image or recording mentioned in the threat, if it exists, in fact an intimate image or recording? The answer changes nothing")],
  shape="flat", quote="it is not necessary for the prosecution to prove (b) if the image or recording mentioned in the threat exists, that it is in fact an intimate image or recording")

# ----------------------------------------------------------------------------------------- 377BG
d(sec="377BG", ref='s 377BG(3)(a)', lines=(9431, 9432), name='s 377BG(3)(a) A has the care of the person below 16 years of age',
  export='Whether a person has "the care" of a person below 16 years of age, section 377BG(3)(a) of the Penal Code 1871: a person may have the care without necessarily being entitled by law to have the custody of the child',
  params=[("A in fact has the care of the person below 16 years of age", "Does A in fact have the care of the person below 16 years of age?"), ("A is entitled by law to have the custody of the child", "Is A entitled by law to have the custody of the child? NOT required for care")],
  expr="[A in fact has the care of the person below 16 years of age]", shape="limited", quote="a person may have the care of a person below 16 years of age without necessarily being entitled by law to have the custody of the child", why="limited by its own wording",
  note="the paragraph says care does not need legal custody; it does not say what else makes a person have the care")

d(sec="377BG", ref='s 377BG(3)(b)', lines=(9434, 9440), name='s 377BG(3)(b) the way is a way of producing material',
  export='Whether a way is a way in which material is produced, section 377BG(3)(b) of the Penal Code 1871: it may include filming, printing, photographing, recording, drawing or otherwise generating material, altering or manipulating material, or reproducing or copying material',
  params=[("the person films, prints, photographs, records, draws or otherwise generates material", "Does the person film, print, photograph, record, draw or otherwise generate material?"), ("the person alters or manipulates material", "Does the person alter or manipulate material?"), ("the person reproduces or copies material", "Does the person reproduce or copy material?")],
  expr="[the person films, prints, photographs, records, draws or otherwise generates material] OR [the person alters or manipulates material] OR [the person reproduces or copies material]", shape="includes",
  quote="the ways in which material is produced may include", note="\"may include\": the ways are not limited to these")

d(sec="377BG", ref='s 377BG(3)(c)', lines=(9442, 9444), name='s 377BG(3)(c) the way is a way of using a person in the production of material',
  export='Whether a way is a way in which a person is used in the production of material, section 377BG(3)(c) of the Penal Code 1871: the ways include inviting or encouraging the person to be involved, or offering the person to be involved',
  params=[("the person is invited or encouraged to be involved in the production of the material", "Is the person invited or encouraged to be involved in the production of the material?"), ("the person is offered to be involved in the production of the material", "Is the person offered to be involved in the production of the material?")],
  expr="[the person is invited or encouraged to be involved in the production of the material] OR [the person is offered to be involved in the production of the material]", shape="includes",
  quote="the ways in which a person may be used in the production of material include")

d(sec="377BH", ref='s 377BH(3)', lines=(9463, 9471), name='s 377BH(3) the way is a way of producing material',
  export='Whether a way is a way in which material is produced, section 377BH(3) of the Penal Code 1871: it may include filming, printing, photographing, recording, writing, drawing or otherwise generating material, altering or manipulating material, or reproducing or copying material',
  params=[("the person films, prints, photographs, records, writes, draws or otherwise generates material", "Does the person film, print, photograph, record, write, draw or otherwise generate material?"), ("the person alters or manipulates material", "Does the person alter or manipulate material?"), ("the person reproduces or copies material", "Does the person reproduce or copy material?")],
  expr="[the person films, prints, photographs, records, writes, draws or otherwise generates material] OR [the person alters or manipulates material] OR [the person reproduces or copies material]", shape="includes",
  quote="the ways in which material is produced may include", note="\"may include\": the ways are not limited to these")

d(sec="377BJ", ref='s 377BJ(4)', lines=(9519, 9526), name='s 377BJ(4) the conduct is advertising',
  export='Whether conduct is to "advertise" child abuse material within section 377BJ(4) of the Penal Code 1871: it includes exhibiting, displaying or supplying advertising material, announcing an offer to sell or distribute, or distributing or circulating an advertisement',
  params=[("the conduct is exhibiting, displaying or supplying any advertising material relating to the material", "Is the conduct exhibiting, displaying or supplying any advertising material relating to the material?"), ("the conduct is announcing by any means any offer to sell or distribute the material", "Is the conduct announcing by any means any offer to sell or distribute the material?"), ("the conduct is distributing or circulating any advertisement relating to the material", "Is the conduct distributing or circulating any advertisement relating to the material?")],
  expr="[the conduct is exhibiting, displaying or supplying any advertising material relating to the material] OR [the conduct is announcing by any means any offer to sell or distribute the material] OR [the conduct is distributing or circulating any advertisement relating to the material]", shape="includes",
  quote='"advertise", in relation to child abuse material, includes')

d(sec="377BK", ref='s 377BK(3)(a)', lines=(9549, 9551), name='s 377BK(3)(a) the person has the electronic child abuse material in his possession',
  export='Whether a person has in his possession child abuse material that is electronic material, section 377BK(3)(a) of the Penal Code 1871: if the person controls access to it, whether or not he has physical possession',
  params=[("the child abuse material is electronic material", "Is the child abuse material electronic material?"), ("the person controls access to the material", "Does the person control access to the material, whether or not he has physical possession of it? (See the Illustration: control of an online storage account)")],
  expr="[the child abuse material is electronic material] AND [the person controls access to the material]", shape="if",
  quote="a person has in the person's possession child abuse material that is electronic material if the person controls access to the material whether or not the person has physical possession")

d(sec="377BK", ref='s 377BK(3)(b)', lines=(9553, 9555), name='s 377BK(3)(b) the way is a way of gaining access to material',
  export='Whether a way is a way in which a person gains access to material, section 377BK(3)(b) of the Penal Code 1871: the ways may include viewing material or displaying it by an electronic medium or any other output of it by an electronic medium',
  params=[("the person views the material or displays it by an electronic medium or any other output of the material by an electronic medium", "Does the person view the material or display it by an electronic medium or any other output of the material by an electronic medium?")],
  expr="[the person views the material or displays it by an electronic medium or any other output of the material by an electronic medium]", shape="includes",
  quote="the ways in which a person gains access to material may include", note="\"may include\": the ways are not limited to this")

d(sec="377BL", ref='s 377BL(5)(a)', lines=(9600, 9606), name='s 377BL(5)(a) the way is a way of producing material',
  export='Whether a way is a way in which material is produced, section 377BL(5)(a) of the Penal Code 1871: it may include filming, printing, photographing, recording, writing, drawing or otherwise generating material, altering or manipulating material, or reproducing or copying material',
  params=[("the person films, prints, photographs, records, writes, draws or otherwise generates material", "Does the person film, print, photograph, record, write, draw or otherwise generate material?"), ("the person alters or manipulates material", "Does the person alter or manipulate material?"), ("the person reproduces or copies material", "Does the person reproduce or copy material?")],
  expr="[the person films, prints, photographs, records, writes, draws or otherwise generates material] OR [the person alters or manipulates material] OR [the person reproduces or copies material]", shape="includes",
  quote="the ways in which material is produced may include", note="\"may include\": the ways are not limited to these")

d(sec="377BL", ref='s 377BL(5)(b)', lines=(9608, 9610), name='s 377BL(5)(b) the way is a way of using a person in the production of material',
  export='Whether a way is a way in which a person is used in the production of material, section 377BL(5)(b) of the Penal Code 1871: the ways include inviting or encouraging the person to be involved, or offering the person to be involved',
  params=[("the person is invited or encouraged to be involved in the production of the material", "Is the person invited or encouraged to be involved in the production of the material?"), ("the person is offered to be involved in the production of the material", "Is the person offered to be involved in the production of the material?")],
  expr="[the person is invited or encouraged to be involved in the production of the material] OR [the person is offered to be involved in the production of the material]", shape="includes",
  quote="the ways in which a person may be used in the production of material include")

d(sec="377BL", ref='s 377BL(6)', lines=(9615, 9638), name='s 377BL(6) the material is abusive material',
  export='Whether material is "abusive material" in relation to B within section 377BL(6) of the Penal Code 1871: material depicting B as a victim of abuse, in a sexual pose or activity or in the presence of another in one, or the sexual and offensive depiction of B\'s genital region, buttocks or (if female) breasts',
  params=[("the image is of B as a victim of torture, cruelty or physical abuse (whether or not the torture, cruelty or abuse is sexual)", "Is the image of B as a victim of torture, cruelty or physical abuse, whether or not sexual? (s 377BL(6)(a)(i))"),
          ("the image is of B as a victim of sexual abuse", "Is the image of B as a victim of sexual abuse? (s 377BL(6)(a)(ii))"),
          ("the image is of B engaged in, or apparently engaging in, a sexual pose or sexual activity (whether or not in the presence of another person)", "Is the image of B engaged in, or apparently engaging in, a sexual pose or sexual activity, whether or not in the presence of another person? (s 377BL(6)(a)(iii))"),
          ("the image is of B in the presence of another person who is engaged in, or apparently engaged in, a sexual pose or sexual activity", "Is the image of B in the presence of another person who is engaged in, or apparently engaged in, a sexual pose or sexual activity? (s 377BL(6)(a)(iv))"),
          ("the material depicts the genital region or buttocks (whether exposed or covered) of B", "Does the material depict the genital region or buttocks (whether exposed or covered) of B? (s 377BL(6)(b))"),
          ("the material depicts the breasts (whether exposed or covered) of B, who is female", "Does the material depict the breasts (whether exposed or covered) of B, if B is female? (s 377BL(6)(c))"),
          ("the depiction is sexual", "Is the depiction sexual? See `s 377C(3)(d) the conduct is sexual`"),
          ("reasonable persons would regard the circumstances as offensive", "Are the circumstances (whether or not apparent from the depiction) such that reasonable persons would regard them as offensive?")],
  expr="[the image is of B as a victim of torture, cruelty or physical abuse (whether or not the torture, cruelty or abuse is sexual)] OR [the image is of B as a victim of sexual abuse] OR [the image is of B engaged in, or apparently engaging in, a sexual pose or sexual activity (whether or not in the presence of another person)] OR [the image is of B in the presence of another person who is engaged in, or apparently engaged in, a sexual pose or sexual activity] OR (([the material depicts the genital region or buttocks (whether exposed or covered) of B] OR [the material depicts the breasts (whether exposed or covered) of B, who is female]) AND [the depiction is sexual] AND [reasonable persons would regard the circumstances as offensive])",
  shape="means", quote='"abusive material", in relation to B, means material that depicts ...')

# ----------------------------------------------------------------------------------------- 377BM
PURP = [("the act was done for the prevention, detection, investigation or punishment of any offence", "Was the act done for the prevention, detection, investigation or punishment of any offence?"),
        ("the act was done for the conduct of contemplated or pending proceedings in any court or tribunal, or to obtain evidence for the purpose of contemplating such proceedings", "Was the act done for the conduct of contemplated or pending proceedings in any court or tribunal, or to obtain evidence for the purpose of contemplating such proceedings?"),
        ("the act was done for safety or national security", "Was the act done for safety or national security?")]
PURP_E = "([the act was done for the prevention, detection, investigation or punishment of any offence] OR [the act was done for the conduct of contemplated or pending proceedings in any court or tribunal, or to obtain evidence for the purpose of contemplating such proceedings] OR [the act was done for safety or national security])"

d(sec="377BM", ref='s 377BM(1)', whole=True, lines=(9645, 9657), name='s 377BM(1) the defence of unintended possession or access is made out',
  export='Whether the defence in section 377BM(1) of the Penal Code 1871 is made out for a charge under section 377BD of possession of or access to an image or recording obtained through an offence under 377BB or an intimate image or recording: the accused proves the possession or access was not intentional and, on becoming aware, all reasonable steps to cease it were taken as soon as practicable',
  params=[("the charge is under section 377BD of having possession of or gained access to an image or recording obtained through an offence under section 377BB or an intimate image or recording mentioned in section 377BD(1)(b)", "Is the charge one under s 377BD of having possession of or having gained access to such an image or recording?"),
          ("the accused person did not intentionally come into possession of or gain access to the image or recording", "Has the accused proved that he or she did not intentionally come into possession of or gain access to it? (s 377BM(1)(a))"),
          ("on becoming aware, as soon as it was practicable to do so, the accused person took all reasonable steps in the circumstances to cease possession of or access to the image or recording", "Has the accused proved that, on becoming aware, as soon as it was practicable, he or she took all reasonable steps in the circumstances to cease possession of or access to it? (s 377BM(1)(b))")],
  expr="[the charge is under section 377BD of having possession of or gained access to an image or recording obtained through an offence under section 377BB or an intimate image or recording mentioned in section 377BD(1)(b)] AND [the accused person did not intentionally come into possession of or gain access to the image or recording] AND [on becoming aware, as soon as it was practicable to do so, the accused person took all reasonable steps in the circumstances to cease possession of or access to the image or recording]",
  shape="limited", quote="It is a defence ... for the accused person to prove that the accused person (a) did not intentionally come into possession ...; and (b) on becoming aware ...", why="limited by its own wording",
  note="the subsection says what the accused can prove to have a defence; it does not say that an accused who cannot prove it has none")

d(sec="377BM", ref='s 377BM(2)', lines=(9661, 9687), name='s 377BM(2) the defence of a protected purpose is made out',
  export='Whether the defence in section 377BM(2) of the Penal Code 1871 is made out for a charge under section 377BB, 377BC, 377BD or 377BE(1): the act was done for the prevention, detection, investigation or punishment of an offence, proceedings, or safety or national security, without intent to cause injury and with reasonable cause, and the image or recording was not kept longer than reasonably necessary',
  params=[("the charge is under section 377BB, 377BC, 377BD or 377BE(1)", "Is the charge one under s 377BB, 377BC, 377BD or 377BE(1)?")] + PURP +
         [("the act was done without intent to cause injury to the person", "Was the act done without intent to cause injury to the person (B) or the person depicted?"), ("the act was done with reasonable cause", "Was the act done with reasonable cause?"),
          ("the image or recording was not kept for a period longer than what was reasonably necessary or required for the purposes", "Was the image or recording (if any) not kept for a period longer than what was reasonably necessary or required for those purposes? (s 377BM(2)(b))")],
  expr="[the charge is under section 377BB, 377BC, 377BD or 377BE(1)] AND " + PURP_E + " AND [the act was done without intent to cause injury to the person] AND [the act was done with reasonable cause] AND [the image or recording was not kept for a period longer than what was reasonably necessary or required for the purposes]",
  shape="if", quote="It is a defence to a charge for an offence under section 377BB, 377BC, 377BD or 377BE(1) if (a) the act ... was done for any of the following purposes without intent to cause injury ... and with reasonable cause ...; (b) the image or recording ... was not kept for a period longer than ...")

# ----------------------------------------------------------------------------------------- 377BN
d(sec="377BN", ref='s 377BN(1)', whole=True, lines=(9710, 9722), name='s 377BN(1) the defence of unintended possession or access is made out',
  export='Whether the defence in section 377BN(1) of the Penal Code 1871 is made out for a charge under section 377BK of possession of or access to child abuse material: the accused proves the possession or access was not intentional and, on becoming aware, all reasonable steps to cease it were taken as soon as practicable',
  params=[("the charge is under section 377BK of having possession of or gaining access to child abuse material", "Is the charge one under s 377BK of having possession of or gaining access to child abuse material?"),
          ("the accused person did not intentionally come into possession of or gain access to child abuse material", "Has the accused proved that he or she did not intentionally come into possession of or gain access to the material? (s 377BN(1)(a))"),
          ("on becoming aware, as soon as it was practicable to do so, the accused person took all reasonable steps in the circumstances to cease possession of or access to the material", "Has the accused proved that, on becoming aware, as soon as it was practicable, he or she took all reasonable steps in the circumstances to cease possession of or access to it? (s 377BN(1)(b))")],
  expr="[the charge is under section 377BK of having possession of or gaining access to child abuse material] AND [the accused person did not intentionally come into possession of or gain access to child abuse material] AND [on becoming aware, as soon as it was practicable to do so, the accused person took all reasonable steps in the circumstances to cease possession of or access to the material]",
  shape="limited", quote="It is a defence to a charge for an offence of having possession of or gaining access to child abuse material under section 377BK for the accused person to prove that the accused person (a) ...; and (b) ...", why="limited by its own wording",
  note="the subsection says what the accused can prove to have a defence; it does not say that an accused who cannot prove it has none")

d(sec="377BN", ref='s 377BN(2)', lines=(9726, 9744), name='s 377BN(2) the defence of a protected purpose is made out',
  export='Whether the defence in section 377BN(2) of the Penal Code 1871 is made out for a charge under sections 377BH to 377BK: the act was done for the prevention, detection, investigation or punishment of an offence, proceedings, or safety or national security, without intent to cause injury to the person depicted and with reasonable cause, and the material was not kept longer than reasonably necessary',
  params=[("the charge is under sections 377BH to 377BK", "Is the charge one under ss 377BH to 377BK?")] + PURP +
         [("the act was done without intent to cause injury to the person depicted in the child abuse material", "Was the act done without intent to cause injury to the person depicted in the child abuse material?"), ("the act was done with reasonable cause", "Was the act done with reasonable cause?"),
          ("the child abuse material was not kept for a period longer than what was reasonably necessary or required for the purposes", "Was the child abuse material not kept for a period longer than what was reasonably necessary or required for those purposes? (s 377BN(2)(b))")],
  expr="[the charge is under sections 377BH to 377BK] AND " + PURP_E + " AND [the act was done without intent to cause injury to the person depicted in the child abuse material] AND [the act was done with reasonable cause] AND [the child abuse material was not kept for a period longer than what was reasonably necessary or required for the purposes]",
  shape="if", quote="It is a defence to a charge for an offence under sections 377BH to 377BK if (a) the act ... was done for any of the following purposes ... and with reasonable cause ...; (b) the child abuse material was not kept for a period longer than ...")

d(sec="377BN", ref='s 377BN(3)', lines=(9749, 9757), name='s 377BN(3) the defence of a legitimate purpose is made out',
  export='Whether the defence in section 377BN(3) of the Penal Code 1871 is made out for a charge under sections 377BH to 377BK: the act has a legitimate purpose related to science, medicine, education or art, and did not pose an undue risk of harm to any person below 16 years of age',
  params=[("the charge is under sections 377BH to 377BK", "Is the charge one under ss 377BH to 377BK?"),
          ("the act has a legitimate purpose related to science, medicine, education or art", "Does the act have a legitimate purpose related to science, medicine, education or art? An act has a legitimate purpose related to art which reasonable persons would regard as art (Explanation)"),
          ("the act did not pose an undue risk of harm to any person below 16 years of age", "Did the act NOT pose an undue risk of harm to any person below 16 years of age?")],
  expr="[the charge is under sections 377BH to 377BK] AND [the act has a legitimate purpose related to science, medicine, education or art] AND [the act did not pose an undue risk of harm to any person below 16 years of age]",
  shape="if", quote="It is a defence to a charge for an offence under sections 377BH to 377BK if the act ... (a) has a legitimate purpose related to science, medicine, education or art; and (b) did not pose an undue risk of harm to any person below 16 years of age")

d(sec="377BN", ref='s 377BN(3) Explanation', lines=(9756, 9757), name='s 377BN(3) Explanation the act has a legitimate purpose related to art',
  export='Whether an act has a legitimate purpose related to art, section 377BN(3) Explanation of the Penal Code 1871: it has if reasonable persons would regard it as art',
  params=[("reasonable persons would regard the act as art", "Would reasonable persons regard the act as art?")],
  expr="[reasonable persons would regard the act as art]", shape="if", quote="An act has a legitimate purpose related to art which reasonable persons would regard as art")

d(sec="377BN", ref='s 377BN(4)', lines=(9773, 9778), name='s 377BN(4) the defence of the child\'s own image is made out',
  export='Whether the defence in section 377BN(4) of the Penal Code 1871 is made out for a charge under sections 377BH to 377BK: the accused is below 16 years of age and the child abuse material is an image of the accused alone',
  params=[("the charge is under sections 377BH to 377BK", "Is the charge one under ss 377BH to 377BK?"), ("the accused person is below 16 years of age", "Is the accused person below 16 years of age? Set from the helper `below 16 years of age` on the accused's age"), ("the child abuse material is an image of the accused person alone", "Is the child abuse material an image of the accused person alone?")],
  expr="[the charge is under sections 377BH to 377BK] AND [the accused person is below 16 years of age] AND [the child abuse material is an image of the accused person alone]",
  shape="if", quote="It is a defence to a charge for an offence under sections 377BH to 377BK if (a) the accused person (A) is below 16 years of age; and (b) the child abuse material that is alleged to constitute the offence is an image of A alone")

d(sec="377BN", ref='s 377BN(5)', lines=(9788, 9793), name='s 377BN(5) a mistaken belief that the material is not offensive is a defence',
  export='Whether it is a defence to a charge relating to child abuse material or abusive material under sections 377BG to 377BL that the accused honestly and reasonably, but mistakenly, believed that reasonable persons would not regard the material as offensive, section 377BN(5) of the Penal Code 1871: it is not',
  params=[("the accused mistakenly but honestly and reasonably believed that reasonable persons would not regard the material as offensive", "Did the accused hold a mistaken but honest and reasonable belief that reasonable persons would not regard the material as being, in the circumstances, offensive? The answer changes nothing")],
  shape="flat", quote="it is not a defence to a charge for an offence relating to child abuse material or abusive material (as the case may be) under sections 377BG to 377BL that, at the time of the conduct constituting the offence, the accused was under a mistaken but honest and reasonable belief that reasonable persons would not regard the child abuse material or abusive material ... as being, in the circumstances, offensive")

MARRIED = [("A and B are married", "Are the offender (A) and the person below 16 years of age (B) married?")]
d(sec="377BN", ref='s 377BN(6)(a)', lines=(9798, 9809), name='s 377BN(6)(a) the defence of marriage to a charge under section 377BG(1) or 377BH(1) is made out',
  export='Whether the defence in section 377BN(6)(a) of the Penal Code 1871 is made out for a charge under section 377BG(1) or 377BH(1) where the offender and the person below 16 years of age are married: the material involves only A and B in its production, depicts B only, A and B only, or A only if A is below 16, and was produced with B\'s consent',
  params=[("the charge is under section 377BG(1) or 377BH(1)", "Is the charge one under s 377BG(1) or 377BH(1)?")] + MARRIED +
         [("the child abuse material involves only A and B in its production", "Does the child abuse material involve only A and B in its production?"), ("the child abuse material depicts B only, A and B only, or A only if A is below 16 years of age", "Does the child abuse material depict B only, A and B only, or A only if A is below 16 years of age?"), ("the child abuse material was produced with B's consent", "Was the child abuse material produced with B's consent?")],
  expr="[the charge is under section 377BG(1) or 377BH(1)] AND [A and B are married] AND [the child abuse material involves only A and B in its production] AND [the child abuse material depicts B only, A and B only, or A only if A is below 16 years of age] AND [the child abuse material was produced with B's consent]",
  shape="if", quote="It is a defence to a charge for the following offences in circumstances where the offender (A) and the person below 16 years of age (B) are married and subject to the following respective conditions: (a) an offence under section 377BG(1) or 377BH(1) if the child abuse material (i) involves only A and B in its production; (ii) depicts B only, A and B only, or A only if A is below 16 years of age; and (iii) was produced with B's consent")

d(sec="377BN", ref='s 377BN(6)(b)', lines=(9811, 9820), name='s 377BN(6)(b) the defence of marriage to a charge under section 377BI is made out',
  export='Whether the defence in section 377BN(6)(b) of the Penal Code 1871 is made out for a charge under section 377BI where the offender and the person below 16 years of age are married: the distribution occurs between A and B only, involves material depicting B only, A and B only, or A only if A is below 16, and was with B\'s consent',
  params=[("the charge is under section 377BI", "Is the charge one under s 377BI?")] + MARRIED +
         [("the distribution occurs between A and B only", "Does the distribution occur between A and B only?"), ("the material depicts B only, A and B only, or A only if A is below 16 years of age", "Does the material depict B only, A and B only, or A only if A is below 16 years of age?"), ("the distribution was with B's consent", "Was the distribution with B's consent?")],
  expr="[the charge is under section 377BI] AND [A and B are married] AND [the distribution occurs between A and B only] AND [the material depicts B only, A and B only, or A only if A is below 16 years of age] AND [the distribution was with B's consent]",
  shape="if", quote="(b) an offence under section 377BI if the distribution of the child abuse material (i) occurs between A and B only; (ii) involves material depicting B only, A and B only, or A only if A is below 16 years of age; and (iii) was distributed with B's consent")

d(sec="377BN", ref='s 377BN(6)(c)', lines=(9822, 9827), name='s 377BN(6)(c) the defence of marriage to a charge under section 377BJ(2) is made out',
  export='Whether the defence in section 377BN(6)(c) of the Penal Code 1871 is made out for a charge under section 377BJ(2) where the offender and the person below 16 years of age are married: the offer occurs between A and B only and involves material depicting B only, A and B only, or A only if A is below 16',
  params=[("the charge is under section 377BJ(2)", "Is the charge one under s 377BJ(2)?")] + MARRIED +
         [("the offer to acquire, buy or gain access to the child abuse material occurs between A and B only", "Does the offer to acquire, buy or gain access to the child abuse material occur between A and B only?"), ("the material depicts B only, A and B only, or A only if A is below 16 years of age", "Does the material depict B only, A and B only, or A only if A is below 16 years of age?")],
  expr="[the charge is under section 377BJ(2)] AND [A and B are married] AND [the offer to acquire, buy or gain access to the child abuse material occurs between A and B only] AND [the material depicts B only, A and B only, or A only if A is below 16 years of age]",
  shape="if", quote="(c) an offence under section 377BJ(2) if the offer to acquire, buy, or gain access to the child abuse material (i) occurs between A and B only; and (ii) involves material depicting B only, A and B only, or A only if A is below 16 years of age")

d(sec="377BN", ref='s 377BN(6)(d)', lines=(9829, 9831), name='s 377BN(6)(d) the defence of marriage to a charge under section 377BK(1) is made out',
  export='Whether the defence in section 377BN(6)(d) of the Penal Code 1871 is made out for a charge under section 377BK(1) where the offender and the person below 16 years of age are married: the possession was with B\'s consent and the material depicts B only, A and B only, or A only if A is below 16',
  params=[("the charge is under section 377BK(1)", "Is the charge one under s 377BK(1)?")] + MARRIED +
         [("the possession of the child abuse material was with B's consent", "Was the possession of the child abuse material with B's consent?"), ("the material depicts B only, A and B only, or A only if A is below 16 years of age", "Does the material depict B only, A and B only, or A only if A is below 16 years of age?")],
  expr="[the charge is under section 377BK(1)] AND [A and B are married] AND [the possession of the child abuse material was with B's consent] AND [the material depicts B only, A and B only, or A only if A is below 16 years of age]",
  shape="if", quote="(d) an offence under section 377BK(1) if the possession of the child abuse material was with B's consent and the material depicts B only, A and B only, or A only if A is below 16 years of age")
