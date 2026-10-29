# Magna Carta (1297), extract from legislation.gov.uk

**Provenance.**
Read on 2026-10-29 by the pitch-Oct session ([7c2f85]) through Meng's Chrome (claude-in-chrome `get_page_text`), at Meng's instruction in that session ("use chrome plugin to reach uk legislation").
URL: https://www.legislation.gov.uk/aep/Edw1cc1929/25/9/data.xml
Chrome returned the XML in the browser's XML viewer with no bot challenge.
This file is a **transcription of that rendered output, not a byte-exact download**, and it is an extract: the `<Metadata>` link block and the three `<Resources>` image references (scans of the original) are left out.
The text below is copied verbatim from the `<Body>`; the status table and the variants table are my extraction from the `<Commentaries>` and marked as mine.
Licence (read 2026-10-29 through the same Chrome, from the footer of https://www.legislation.gov.uk/aep/Edw1cc1929/25/9, the HTML page of this document): "All content is available under the Open Government Licence v3.0 except where otherwise stated. This site additionally contains content derived from EUR-Lex, reused under the terms of the Commission Decision 2011/833/EU on the reuse of documents from the EU institutions. For more information see the EUR-Lex public statement on re-use. © Crown and database right" (the page text ends there).
What that read does not establish: (1) I read only the site-wide footer. I did not look for a notice specific to this document, and the `<Metadata>` block of its data.xml has no licence field (publisher is "Statute Law Database"). (2) The site's separate re-use page (https://www.legislation.gov.uk/re-use) returned HTTP 504 when I tried it, so I have not read it. (3) I did not open the OGL v3.0 text itself. (4) The site's editorial layer, namely the "traditional translation" with obsolete characters modernised and the commentaries, is the site's own; the footer says OGL applies to all content unless otherwise stated, but whether anything on this page is "otherwise stated" is not something I checked beyond the footer.
Re-read the XML in Chrome if you need byte-exactness.

**Metadata (as given).**
- Title: Magna Carta (1297). Number: 1297 c. 9. `AlternativeNumber` (Regnal): `25_Edw_1_cc_1_9_29`.
- `DocumentStatus` = `revised`. `RestrictExtent` = `E+W`. `RestrictStartDate` = 1991-02-01. `dc:valid` = 1991-02-01. `dc:modified` = 2026-08-27. `dc:date` = 1979-09-30. `NumberOfProvisions` = 26.
- Long title: THE GREAT CHARTER OF THE LIBERTIES OF ENGLAND, AND OF THE LIBERTIES OF THE FOREST; CONFIRMED BY KING EDWARD, IN THE TWENTY-FIFTH YEAR OF HIS REIGN.
- Editorial note on the site (commentary c918914): "The original text of this Act was not modern English. The traditional translation appears first with obsolete characters modernised. The original text (as an image) appears second. The full reference to the chapter numbers of this Statute includes cc. 1-37, c. 37 of which has been partly repealed."
- Editorial note (c918913): the Latin indorsement is on Membrane 38 of the Roll; the text is from *Statutes of the Realm*, vol. 1, p. 114 to p. 124; "The Various Readings marked L. are from the Charter of Inspeximus 25 Edw. I, under the Great Seal preserved among the Archives of the City of London."

## Text with no repeal annotation (verbatim from `<Body>`)

**Preamble, paragraph 1 (Edward I).**
EDWARD by the Grace of God King of England, Lord of Ireland, and Duke of Guyan, to all Archbishops, Bishops, &c. We have seen the Great Charter of the Lord Henry sometimes King of England, our Father, of the Liberties of England in these words:

**Preamble, paragraph 2 (Henry III's charter, recited).**
HENRY by the Grace of God King of England, Lord of Ireland, Duke of Normandy and Guyan, and Earl of Anjou, to all Archbishops, Bishops, Abbots, Priors, Earls, Barons, Sheriffs, Provosts, Officers, and to all Bailiffs, and other our faithful Subjects, which shall see this present Charter, Greeting: Know Ye, that We, unto the honour of Almighty God, and for the salvation of ( ) the souls of our Progenitors and Successors [Kings of England,] to the advancement of Holy Church and amendment of our Realm, of our meer and free will, have given and granted to all Archbishops, Bishops, Abbots, Priors, Earls, Barons, and to all [Freemen] of this our Realm, these Liberties following, to be kept in our Kingdom of England for ever.

**Heading: "Confirmation of Liberties." Chapter I (`section-I`).**
FIRST, We have granted to God, and by this our present Charter have confirmed, for Us and our Heirs for ever, that the Church of England shall be free, and shall have all her whole Rights and Liberties inviolable. We have granted also, and given to all the Freemen of our Realm, for Us and our Heirs for ever, these Liberties under-written, to have and to hold to them and their Heirs, of Us and our Heirs for ever.

**Heading: "Liberties of London, &c." Chapter IX (`section-IX`).**
THE City of London shall have all the old Liberties and Customs [which it hath been used to have]. Moreover We will and grant, that all other Cities, Boroughs, Towns, and the Barons of the Five Ports, and all other Ports, shall have all their Liberties and free Customs.

**Heading: "Imprisonment, &c. contrary to Law. Administration of Justice." Chapter XXIX (`section-XXIX`).**
NO Freeman shall be taken or imprisoned, or be disseised of his Freehold, or Liberties, or free Customs, or be outlawed, or exiled, or any other wise destroyed; nor will We not pass upon him, nor condemn him, but by lawful judgment of his Peers, or by the Law of the Land. We will sell to no man, we will not deny or defer to any man either Justice or Right.

**Heading: "General Saving. Observance of these Liberties. Subsidy, in respect of this Charter and Charter of the Forest."**
This heading follows the empty XXXVI–XXXVII provision. It holds three unnumbered paragraphs (`wrapper1`, `wrapper2`, `wrapper3`), which I read as the surviving part of c. 37 (see the table). Nothing marks them repealed.

`wrapper1`:
Reserving to all Archbishops, Bishops, Abbots, Priors, Templars, Hospitallers, Earls, Barons, and all Persons, as well Spiritual as Temporal, all their free Liberties and free Customs, which they have had in time passed. And all these Customs and Liberties aforesaid, which We have granted to be holden within this our Realm, as much as appertaineth to Us and our Heirs, we shall observe; and all Men of this our Realm, as well Spiritual as Temporal, as much as in them is, shall observe the same against all Persons, in like wise. And for this our Gift and Grant of these Liberties, and of other contained in our Charter of Liberties of our Forest, the Archbishops, Bishops, Abbots, Priors, Earls, Barons, Knights, Freeholders, and other our Subjects, have given unto Us the Fifteenth Part of all their Moveables. And We have granted unto them on the other part, ( ) that neither We nor our Heirs shall procure or do any thing whereby the Liberties in this Charter contained shall be infringed or broken. And if any thing be procured by any person contrary to the premises, it shall be had of no force nor effect. These being Witnesses; Lord B. Archbishop of Canterbury, E. Bishop of London, J. Bishop of Bathe, P. of Winchester, H. of Lincoln, R. of Salisbury, W. of Rochester, W. of Worcester, J. of Ely, H. of Hereford, R. of Chichester, W. of Exeter, Bishops; the Abbot of St. Edmonds, the Abbot of St. Albans, the Abbot of Bello, the Abbot of St. Augustine’s in Canterbury, the Abbot of Evesham, the Abbot of Westminster, the Abbot of Bourgh St. Peter, the Abbot of Reding, the Abbot of Abindon, the Abbot of Malmsbury, the Abbot of Winchcomb, the Abbot of Hyde, the Abbot of Certesey, the Abbot of Sherburn, the Abbot of Cerne, the Abbot of Abbotebir, the Abbot of Middleton, the Abbot of Seleby, the Abbot of Cirencester; H. de Burgh Justice, H. Earl of Chester and Lincoln, W. Earl of Salisbury, W. Earl of Warren, G. de Clare Earl of Gloucester and Hereford, W. de Ferrars Earl of Derby, W. de Mandeville Earl of Essex, H. de Bygod Earl of Norfolk, W. Earl of Albemarle, H. Earl of Hereford, J. Constable of Chester, R. de Ros, R. Fitzwalter, R. de Vyponte, W. de Bruer, R. de Muntefichet, P. Fitzherbert, W. de Aubenie, F. Gresly, F. de Breus, J. de Monemue, J. Fitzallen, H. de Mortimer, W. de Beauchamp, W. de St. John, P. de Mauly, Brian de Lisle, Thomas de Multon, R. de Argenteyn, G. de Nevil, W. de Mauduit, J. de Balun, and others. ( )

`wrapper2`:
We, Ratifying and approving these Gifts and Grants aforesaid, confirm and make strong all the same for Us and our Heirs perpetually, and by the Tenor of these Presents do renew the same: Willing and granting for Us and our Heirs, that this Charter and all and singular his Articles for ever shall be stedfastly, firmly, and inviolably observed; and if any Article in the same Charter contained yet hitherto peradventure hath not been kept We will and by authority royal command from henceforth firmly they be observed.

`wrapper3`:
In Witness whereof We have caused these our Letters Patents to be made. T. Edward our son at Westminster, the twenty-eighth day of March in the twenty-eighth year of our Reign.

(`wrapper3` is followed by three scan images of the original.)

## Per-chapter status (MY EXTRACTION from the F-type commentaries; check against the XML)

Each repealed chapter appears in `<Body>` as an empty provision. The text of the repeal comes from a commentary of Type="F". Short names are the site's own titles.

| Chapter(s) | Status per the site | Repealed by (as the commentary cites it) |
|---|---|---|
| Preamble (2 paras) | no annotation | none |
| 1 | text present, no annotation | none |
| 2–6 | repealed | Statute Law Revision Act 1863 (c. 125); Statute Law (Ireland) Revision Act 1872 (c. 98) |
| 7 | repealed | Administration of Estates Act 1925 (c. 23) s. 56, Sch. 2 Pt. I; Administration of Estates Act (Northern Ireland) 1955 (c. 24) s. 46, Sch. 3; Statute Law (Repeals) Act 1969 (c. 52) Sch. Pt. I |
| 8 | repealed | Statute Law (Repeals) Act 1969 (c. 52) Sch. Pt. I |
| 9 | text present, no annotation | none |
| 10 | repealed | Statute Law Revision Act 1948 (c. 62) |
| 11, 12 | repealed | Civil Procedure Acts Repeal Act 1879 (c. 59) Sch. |
| 13 | repealed | SLRA 1863; SL(I)RA 1872 |
| 14 | repealed | Criminal Law Act 1967 (c. 58) Sch. 3 Pt. I; Criminal Law Act (Northern Ireland) 1967 (c. 18) Sch. 2 Pt. I |
| 15, 16 | repealed | Statute Law (Repeals) Act 1969 Sch. Pt. I |
| 17 | repealed | Statute Law Revision Act 1892 (c. 19) |
| 18 | repealed | Crown Proceedings Act 1947 (c. 44) Sch. 2 |
| 19–21 | repealed | SLRA 1863; SL(I)RA 1872 |
| 22 | repealed | SLRA 1948 |
| 23 | repealed | Statute Law (Repeals) Act 1969 Sch. Pt. I |
| 24 | repealed | SLRA 1863; SL(I)RA 1872 |
| 25 | repealed | SLRA 1948 |
| 26 | repealed | Offences Against the Person Act 1828 (9 Geo. 4 c. 31) s. 1; Offences Against the Person (Ireland) Act 1829 (10 Geo. 4 c. 34) s. 1; Criminal Law (India) Act 1828 (9 Geo. 4 c. 74) s. 125 |
| 27, 28 | repealed | SLRA 1863; SL(I)RA 1872 |
| 29 | text present, no annotation | none |
| 30 | repealed | Statute Law (Repeals) Act 1969 Sch. Pt. I |
| 31 | repealed | SLRA 1863; SL(I)RA 1872 |
| 32 | repealed | Statute Law Revision Act 1887 (c. 59) |
| 33, 34 | repealed | SLRA 1863; SL(I)RA 1872 |
| 35 | repealed | Sheriffs Act 1887 (c. 55) s. 39, Sch. 3 |
| 36 | repealed | SLRA 1863; SL(I)RA 1872 |
| 37 | **repealed in part** | SLRA 1863; SL(I)RA 1872 (same commentary as c. 36). My reading: the unrepealed residue is the "General Saving" heading and its three unnumbered paragraphs above. The XML does not say this in so many words. |

Not in the XML at all, so not established by this read: whether "in force" holds for the preamble paragraphs and the three wrapper paragraphs. The site shows them without a repeal annotation. Do not treat that as a statement about in-force status.

## Variant readings from *Statutes of the Realm* (X-type commentaries; MY EXTRACTION)

The XML marks the text in the left column as an `Addition` (the bracketed-in text of the traditional translation) and the commentary gives the *Statutes of the Realm* reading in the right column.

| Where | Text as shown | *Statutes of the Realm* variant |
|---|---|---|
| Preamble 1 | to all Archbishops, Bishops, &c. | To All to whom these present Letters shall come; Greeting. |
| Preamble 2, after "salvation of" | (gap) | our Soul and |
| c. 29 | condemn him, | deal with him, |
| Wrapper 1 | free Liberties | Liberties |
| Wrapper 1 | as much as appertaineth to Us and our Heirs, we shall observe; and | on our part, towards our men, |
| Wrapper 1 | as much as in them is, shall observe the same against all Persons, in like wise. | shall observe on their part towards their men |
| Wrapper 1, after "on the other part," | (gap) | for us and our heirs, |
| Wrapper 1 witnesses | B. | S |
| | Bello, | Battel. |
| | Bourgh St. Peter, | Peterborough |
| | Abbotebir, | Abbotsbury |
| | Justice, | Chief Justicer |
| | Hereford, (after Gloucester and) | Hertford |
| | Monemue, | Monmouth |
| Wrapper 1, end | (gap) | Given at Westminster the eleventh day of February in the ninth year of our Reign. |
| Wrapper 2 | this Charter and | the Charter aforesaid in |
| Wrapper 2 | and if | even although |
| Wrapper 2 | We will and by authority royal command from henceforth firmly they be observed | Not in Original. |
| Wrapper 3 | T. Edward our son at Westminster, the twenty-eighth day of March in the twenty-eighth year of our Reign. | "The Old Translations read These Reverend Fathers being Witnesses; R. Archbishop of Canterbury Primate of England, A. Bishop of Duresme, and other; Given at Westminster, with our own hand, the twenty-eighth day of the month of March, the twenty-eighth year of our reign." Also: "Witness Edward our Son at Westminster, the Twelfth day of October in the Twenty-fifth Year of our Reign." |

## What this read shows for the 1225-versus-1297 question (MY OBSERVATION)

The statute does not merely resemble the 1225 reissue; it recites Henry III's charter "in these words" (Preamble 1) and then reproduces it (Preamble 2 onward), with a dating variant "the eleventh day of February in the ninth year of our Reign" (9 Hen. III). Edward I's own words are the Preamble 1 and the wrapper 2 and 3 paragraphs. Whether Edward's inspeximus changed any word of Henry's text is what the `Addition` and variant-reading markers above record, and this is only a partial answer: it covers the differences the editors flagged, not a diff against an independent 1225 text.
