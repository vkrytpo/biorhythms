#!/usr/bin/env python
"""
Find upcoming biorhythmically-matching dates for a group of persons
(i.e. days without warnings for all persons involved).

2011-09-06

"""

b = ((1,1,1990),(31,1,1990),(15,1,1990))

print ("Matches for", b)
print (57*'-')

from datetime import date

t1 = date.today().toordinal()

wa=(
((1,12,13),(7,18)),
((1,15),(8,22)),
((1,17,18),(9,26))
)

tag = ('Mo.','Di.','Mi.','Do.','Fr.','Sa.','So.')

for t in range(t1,t1+120):
	m = 0
	for k in b:
		t0 = date(k[2],k[1],k[0]).toordinal()
		tm = 3
		for c in range(3):
			p = 23+5*c
			v = ((t-t0) % p)+1
			if v in wa[c][0] or v in wa[c][1]:
				tm -= 1
		if tm == 3:
			m += 1
	if m == len(b):
		a = date.fromordinal(t)
		print (a, tag[a.weekday()])

