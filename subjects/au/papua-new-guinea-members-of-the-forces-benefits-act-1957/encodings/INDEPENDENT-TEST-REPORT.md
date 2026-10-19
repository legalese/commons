# Independent test report: Papua New Guinea (Members of the Forces Benefits) Act 1957

`tests-independent.l4`: **24 assertions, 23 satisfied, 1 failed**, no other errors. (`L4=~/.local/bin/l4 ./check.sh`)

## Failure

- **L38, scenario 22: enlisted before the war, served on into it.** A man who enlisted on 1 Aug 1939 and served through 1942 is "a member of the Forces" under s 3, which asks whether he "served during the war". The module decides membership on `served in the Defence Force from` alone, which must fall between 3 Sep 1939 and 2 Sep 1945, so a pre-war enlistee is shut out. **Finding against the code.** The fix is to test whether the service *period* overlaps the war (start before 3 Sep 1945 and end on or after 3 Sep 1939), which needs an end date or a "served on or after 3 Sep 1939" input.

## Reading differences (not code defects)

- **End of the war.** The brief and module take the war to end before 3 Sep 1945. The Act does not set an end date. The 1945 date only limits which *other* wars "the war" includes. I tested on the brief's reading (service starting 1 Oct 1945 is not a member, which passes), but this is a matter of reading the Act.
- **The start date as a proxy for service.** Because the module uses the start date, a man who enlisted on 2 Sep 1945 is counted as a member even if he served one day in the war. That is consistent with the Act. A man who enlisted in, say, 1944 is a member however long he served afterwards, which is also fine.

## Gaps

- Sex, indigeneity and the "not part of a State" island test are folded into one boolean, so scenarios 2, 5, 6 and 7 test only that boolean.
- s 4 and s 8 are outputs that just copy the membership answer. They cannot show that a benefit from "any other" law is excluded, or that a particular dealing (sale, assignment, execution, bankruptcy) fails. I asserted only that they are TRUE for a member.
- s 8 says "a pension is absolutely inalienable" with no membership condition. The module returns FALSE for a non-member. That is harmless, since a non-member has no pension under the Act, but it is not what the words say. Not asserted.
- Dependants are not modelled separately. Death and incapacity share the same booleans.
- s 6 (other prescribed benefits) and the regulation conditions in s 5(1) are not encoded.

## Change after the pass (encoder)

- **Service begun before the war (scenario 22).** Accepted: service that continued into the war counts (F1).
- **Line 31 (service beginning 2 September 1939).** Left failing: it follows the brief's original start-date reading and contradicts scenario 22; without an end date both cannot hold.
- The gaps are recorded as known limits in NOTES.md.
