#!/usr/bin/env python

# Score-based network analysis of biorhythms. Higher scores mean more compatibility.
# (Matching primary cycles net two points. 50%-65% compatibility is considered neutral.)

# Usage:
#     python2 compattable.py | sort -g

from math import cos, pi
from datetime import date

# "Star Trek: The Next Generation" male cast example data:
pers=(
 ((1940,7,13),  "Patrick Stewart"),
 ((1949,2,2),   "Brent Spiner"),
 ((1952,8,19),  "Jonathan Frakes"),
 ((1957,2,16),  "LeVar Burton"),
 ((1952,12,9),  "Michael Dorn"),
)

nn = ("P","E","I")

def f(a):
    if a < -3:
        return "(-)"    # bad compatibility
    elif a > 3:
        return "(+)"    # good   "   "
    else:
        return "(0)"    # neutral

for n1, d1 in enumerate(pers):
    for n2, d2 in enumerate(pers):
        if n1 >= n2: continue
        yy,mm,dd = d1[0]
        yy2,mm2,dd2 = d2[0]
        t1 = date(yy,mm,dd).toordinal()
        t2 = date(yy2,mm2,dd2).toordinal()

        lag = abs(t2 - t1)
        score = 0
        mat = ''
        for p in range(0,7):
            ld = 23 + 5 * p
            l_lag = lag % ld
            qq = 100. * abs(cos(pi * l_lag / ld))
            if qq < 50:
                if p < 3:
                    score -= 2
                else:
                    score -= 1
            elif qq > 65:
                if p < 3:
                    score += 2
                    mat += nn[p]
                else:
                    score += 1
        print (score, d1[1],d2[1], f(score),mat)

