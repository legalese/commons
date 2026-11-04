# Bills read through lawplain (extrinsic material)

Retrieved 2026-11-04 through the lawplain MCP server (`mcp__lawplain__get_document`, corpus `bills`).
lawplain is a secondary source; each record names an SSO URL, which was not fetched (SSO refuses this fetcher).
A Bill as introduced is evidence of what the Bill proposed, not of the Act as passed; it is used here only to identify what a provision of the repealed Act was about.
Only the sentences relied on are copied, verbatim from lawplain's `body_text`.

## B6-1998: Telecommunication Authority of Singapore (Amendment) Bill

lawplain record: `bill_id` B6-1998, "Read the first time on 14th January 1998", long title "An Act to amend the Telecommunication Authority of Singapore Act (Chapter 323 of the 1993 Revised Edition).", `body_length` 20608, record URL `https://sso.agc.gov.sg/Bills-Supp/6-1998/Published/19980115?DocDate=19980115`.

> Amendment of section 30 6. Section 30(1) of the principal Act is amended by deleting the words “public telecommunication” and substituting the words “telecommunication system”.

> Amendment of section 74 12. Section 74 of the principal Act is amended — ( a ) by inserting, immediately after the words “section 30” in the ninth line of subsection (1), the words “or that the telecommunication equipment is imported in contravention of any provision of this Act or any regulations made thereunder”;

## B16-1992: Telecommunication Authority of Singapore Bill

lawplain record: `bill_id` B16-1992, "Read the first time on 27th February 1992", `body_length` 8876; the body ends after clause 2 (definitions), so no clause 30 is served.

> “telecommunications” means a transmission, emission or reception of signs, signals, writing, images, sounds or intelligence of any nature by wire, radio, optical or other electro-magnetic systems

## Searches that returned nothing usable

`bills`: "Telecommunications Bill Telecommunication Authority of Singapore repealed" (lists B33-1999, not fetched: it is the whole 1999 Bill); "section 30" with `year` 1998 and 1999 (the `year` parameter was ignored; no TAS Bill in the first 10); "Clause 9 approval of equipment re-enacts section 30 of the repealed Act" (nothing relevant).
`statutes`: "Telecommunication Authority of Singapore Act" (TASA1982 and TASA1992, both `act_repealed`; `get_document` TASA1992 returns no sections).
`hansard`: "Telecommunications Bill second reading 1999 Info-communications Development Authority" (only 2016 and 2026 records).
