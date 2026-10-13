# Source licence: Decree 67/2023/NĐ-CP, Decree 220/2026/NĐ-CP, and the earlier Decree 03/2021/NĐ-CP and Circular 04/2021/TT-BTC

**Terms: not established by us.**

The sources are a decree of the Government of Vietnam and its amending decree, normative legal documents published in the Government gazette (Công báo); and, since 2026-10-13, the decree it replaced, Decree 03/2021, also from the gazette, with the Ministry of Finance's Circular 04/2021, from the Government's document portal.
Legal normative documents are generally outside copyright in Vietnam, but this file does not rely on that and has not verified the provision, so no grant is written here.

What this repository does about it: the PDFs are **not held** here; `source/fetch.sh` fetches them from the government's servers and checks their sha256 (ruling of 2026-10-01). The encodings quote the provisions they encode one `-- src:N |` line at a time.

The encodings are Apache-2.0.

## Hosting

- `nd67-congbao-1017-1018`: congbaocdn.chinhphu.vn, the Government gazette (Công báo) issue 1017+1018, 20 September 2023: the decree's body and Phụ lục I-III. The server wants a Referer.
- `nd67-congbao-1019-1020`: congbaocdn.chinhphu.vn, the Government gazette (Công báo) issue 1019+1020: the decree's remaining annexes (Phụ lục III continued to X, including Phụ lục VI). The server wants a Referer.
- `nd220-2026-congbao-367`: congbaocdn.chinhphu.vn, the Government gazette (Công báo) no. 367, 3 July 2026: Decree 220/2026/NĐ-CP, which amends Decree 67/2023. The server wants a Referer.
- `nd03-congbao-125-126`: congbaocdn.chinhphu.vn, the Government gazette (Công báo) issue 125+126, 28 January 2021: Decree 03/2021/NĐ-CP, which Decree 67/2023 replaced and whose rules its Article 76(1) continues for earlier contracts. The server wants a Referer.
- `tt04-2021-btc`: datafiles.chinhphu.vn, the Government's document portal: Circular 04/2021/TT-BTC, the limits and premiums under Decree 03/2021. A scan with no text layer, read by OCR in `source/fetch.sh`.
