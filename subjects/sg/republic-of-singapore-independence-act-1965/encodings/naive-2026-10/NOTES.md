# Republic of Singapore Independence Act 1965 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, which the deposit says "incorporates all
amendments up to and including 1 December 2021 and comes into operation on 31
December 2021" (`../../registers/source-bundle/RSIA1965.txt`). Its Legislative
History lists only Act 9 of 1965, Act 7 of 1972 (which deleted the 1985 Edition's
s 8(3)) and the 1985 Revised Edition. Section numbers follow the body (ss 1 to 14).
The arrangement of sections at the top of the deposit is printed one line out of
step with the body.

**Checks:** one case file, 55 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0258** in `subjects/sg/requirements.jsonl`: Tier 4 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked
a sharper question yet.

The Act is short and is mostly about the state's own machinery. This row takes the
parts that have tests: Singapore Day (s 1), executive authority (s 4), the
Malaysian constitutional provisions that ceased (s 6(3)) and who exercises the ones
that continue (s 6(4)), including the Legal Service Commission; languages (s 7);
clemency (s 8); public officers (s 10); appeals (s 11); Malaysian board members
(s 12); and existing laws (s 13). Not encoded: the vesting provisions as such
(ss 3, 5, 9), s 6(1), (2) and (5) beyond the s 6(3) list, the Prime Minister's
orders under s 13(5), and the saving in s 14. Which Articles of the Constitution of
Malaysia sit inside the Parts listed in s 6(3) is a flag, because the deposit does
not reproduce that Constitution.

## What the Act turns out to say

### 1. The 2020 Revised Edition still sends High Court appeals to Kuala Lumpur and the Privy Council

s 11: "Until other provision is made by the Legislature", appeals from the High
Court "shall continue to lie to the Federal Court of Malaysia and to the Privy
Council". The section is printed unchanged in the 2020 Revised Edition. Whether the
Legislature has made other provision is not in this deposit, so it is a flag. The
encoding gives the s 11 answer only when the flag is false. Asserted.

### 2. An accomplice can be pardoned without having been convicted

s 8(1)(a) lets the President, on the Cabinet's advice, pardon "any accomplice in any
offence who gives information which leads to the conviction of the principal
offender". It does not require the accomplice to have been convicted. A free or
conditional pardon, reprieve or respite under (b) does require a conviction "in any
court in Singapore". Remitting "any penalty or forfeiture imposed by law" under (c)
is read as not needing a conviction. That last point is the encoder's reading.
Everything under s 8 needs the Cabinet's advice. Asserted.

### 3. The death-sentence report route is written only for sentences confirmed on appeal

s 8(2) applies where a death sentence "in the event of an appeal ... has been
confirmed by the appellate court". The reports of the trial Judge and of the
appellate presiding Judge go to the Attorney-General. His opinion goes with them to
the Cabinet, and the Cabinet then advises the President. On its words the route
does not apply to a death sentence that was not appealed, and the text does not say
what happens in that case. Asserted.

### 4. Four official languages; Malay is the national language; no one may be stopped using any language

s 7(1) names Malay, Mandarin, Tamil and English. s 7(2) makes Malay, "in the Roman
script", the national language. The proviso protects using, teaching or learning
"any other language", not only the official ones. Asserted.

### 5. The Malaysian Police Force Commission's powers went to the Public Service Commission

s 6(4)(g) gives the Police Force Commission's powers to the Public Service
Commission. The Judicial and Legal Service Commission's powers go to a new Legal
Service Commission: the Chief Justice (as President), the Attorney-General, the
Chairman of the PSC, one High Court Judge nominated by the Chief Justice, and "not
more than 2" PSC members nominated by the Chairman. Counting that as at most six
members is the encoder's arithmetic. Asserted.

### 6. Old laws are read forward, and the President had three years to rewrite them, with no limit for local government

s 13(2) reads references to the Colony or State of Singapore as the Republic. The
Yang di-Pertuan Agong and the Yang di-Pertuan Negara both become the President, the
Legislative Assembly becomes the Parliament of Singapore, and the State
Advocate-General becomes the Attorney-General. The President's power to modify
written law by order lasted "3 years after the coming into operation of this Act"
(s 13(3)). An order cannot take effect before Singapore Day. The separate power for
the abolition of the City Council and Rural Board (s 13(4)) states no time limit;
reading that as no 3-year window is an inference. Asserted.

### 7. The Act was deemed in force months before it was passed

s 1 deems the Act in force from 9 August 1965. The Legislative History, which says it
"is not part of the Act", gives the Second Reading as 22 December 1965. Asserted
only as the deeming: the Act is in operation on 1 October 1965.

### 8. Returning officers and temporary staff were treated differently

Officers of the Singapore Government before 16 September 1963 who became Malaysian
officers became Singapore officers "once again" (s 10(1)). People Malaysia engaged
in former Singapore departments between those dates became only "temporarily
employed" (s 10(2)). The President could confirm or terminate their employment
within 24 months (s 10(3)). That power does not reach the s 10(1) returners.
Asserted. The 24-month and 3-year windows are taken to include their last day, and
no test sits on either boundary.

## What would need doing before this is worth anything

- The later Acts that dealt with appeals (finding 1) and that may have overtaken
  other transitional sections were not read. The Constitution of the Republic of
  Singapore was not read either.
- The Parts of the Constitution of Malaysia listed in s 6(3) were not resolved to
  Articles.
- No case law on s 8 clemency or on s 7 was searched.
