#!/bin/sh
# Re-fetch the Código Penal sources and print what each request cost.
# The LexML record names Planalto's "Texto Atualizado Multivigente"; its own
# link to Planalto (legislacao.planalto.gov.br/.../websearch?...) answered 302
# and then reset the connection on 2026-09-29, so the compiled text is fetched
# from its stable ccivil_03 URL directly.
set -eu
UA="Mozilla/5.0"
fetch() { # url outfile
  curl -sS -L -A "$UA" -o "$2" -w "%{http_code} %{num_redirects} %{size_download} %{time_total} $1\n" "$1"
}
fetch "https://www.lexml.gov.br/urn/urn:lex:br:federal:decreto.lei:1940-12-07;2848" lexml-record.html
fetch "https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm" del2848compilado.htm
python3 extract.py del2848compilado.htm > codigo-penal-1940.txt
shasum -a 256 lexml-record.html del2848compilado.htm codigo-penal-1940.txt extract.py > SHA256SUMS
cat SHA256SUMS
# The Senado's open-data record for the norm (id 527942): amendment METADATA, not text.
fetch "https://legis.senado.leg.br/dadosabertos/legislacao/527942" senado-dadosabertos-527942.xml
shasum -a 256 senado-dadosabertos-527942.xml >> SHA256SUMS
