# louisiana/

Louisiana (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

Nothing is indexed, deposited or encoded here yet. This README records why.

## Register access, 24 October 2026: the official host did not answer

The Louisiana Revised Statutes are published by the Louisiana State Legislature at https://www.legis.la.gov/ (Law search). For the tax and benefits sample (personal income tax, La. R.S. Title 47; the Family Independence Temporary Assistance Program, La. R.S. Title 46) the register was tried on 2026-10-24 (UTC) with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`:

- 03:24 UTC, https://www.legis.la.gov/robots.txt: no TCP connection on port 443 after about 22 seconds;
- 03:24 UTC, https://www.legis.la.gov/legis/LawSearch.aspx: the same;
- 03:26 UTC, https://legis.la.gov/robots.txt: the same;
- 03:29 UTC, https://www.legis.la.gov/robots.txt: the same.

The name resolves (184.178.144.11), and other states' registers answered from the same machine at the same time, so the host itself was not reachable from here. Under the sourcing rules a site that hangs is treated as a no: no other user agent, proxy or mirror was tried, and nothing was fetched. Robots.txt and the site's terms could therefore not be read.

**To do when the host answers:** read robots.txt and the site's terms; then index and deposit La. R.S. 47:31 to 47:300 (the individual income tax, including the 47:297 credits) and the FITAP provisions of Title 46 (and the Department of Children and Family Services rules in LAC Title 67 that set the payment amounts), and encode them as the other states' baselines are.
