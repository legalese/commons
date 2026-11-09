#!/usr/bin/env python3
# hebdate.py : the arithmetic Hebrew calendar (Calendrical Calculations), to check "Hebrew date (Gregorian date)" pairs printed in the Law.
# Month numbers: 1 Nisan 2 Iyyar 3 Sivan 4 Tammuz 5 Av 6 Elul 7 Tishri 8 Marheshvan 9 Kislev 10 Tevet 11 Shevat 12 Adar (13 Adar II in a leap year).
# This is computed arithmetic, NOT a reading of any source; the pairs it checks are claims in the sources.
import datetime,sys
def leap(y): return (7*y+1)%19<7
def elapsed(y):
    m=(235*y-234)//19; parts=12084+13753*m; d=29*m+parts//25920
    if (3*(d+1))%7<3: d+=1
    return d
def delay2(y):
    a,b,c=elapsed(y-1),elapsed(y),elapsed(y+1)
    if c-b==356: return 2
    if b-a==382: return 1
    return 0
EPOCH=-1373427   # R.D. of the Hebrew epoch (Calendrical Calculations, hebrew-epoch)
def new_year(y): return EPOCH+elapsed(y)+delay2(y)
def diy(y): return new_year(y+1)-new_year(y)
def last_month(y): return 13 if leap(y) else 12
def mlen(y,m):
    if m in (2,4,6,10,13): return 29
    if m==12 and not leap(y): return 29
    if m==8 and diy(y) not in (355,385): return 29
    if m==9 and diy(y) in (353,383): return 29
    return 30
def fixed(y,m,d):
    t=new_year(y)+d-1
    if m<7:
        for k in range(7,last_month(y)+1): t+=mlen(y,k)
        for k in range(1,m): t+=mlen(y,k)
    else:
        for k in range(7,m): t+=mlen(y,k)
    return t
def greg(y,m,d): return datetime.date.fromordinal(fixed(y,m,d))
if __name__=='__main__':
    tests=[(5786,5,5,'2026-07-19'),(5786,5,1,'2026-07-15'),(5786,4,28,'2026-07-13'),(5786,3,9,'2026-05-25'),(5786,3,16,'2026-06-01'),
           (5786,4,21,'2026-07-06'),(5787,10,22,'2027-01-01'),(5785,2,14,'2025-05-12'),(5786,8,7,'2025-10-29'),(5786,10,18,'2026-01-07'),(5785,2,7,'2025-05-05')]
    for y,m,d,want in tests:
        got=greg(y,m,d).isoformat(); print(y,m,d,'->',got,'claimed',want,'OK' if got==want else 'MISMATCH')
