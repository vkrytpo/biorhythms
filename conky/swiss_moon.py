#!/usr/bin/python
# Print current astrological sign of the Moon
# (needs PySwissEph)
# 2013-12-20

import datetime
import swisseph as s

t = ("Ari",
     "Tau",
     "Gem",
     "Can",
     "Leo",
     "Vir",
     "Lib",
     "Sco",
     "Sag",
     "Cap",
     "Aqu",
     "Pis"
     )

n = datetime.datetime.utcnow()

j = s.julday(n.year, n.month, n.day, n.hour + n.minute / 60.)

ra = (s.calc_ut(j, s.MOON))[0]

print(t[int(ra//30.)])
