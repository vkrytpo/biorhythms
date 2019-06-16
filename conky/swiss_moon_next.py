#!/usr/bin/python
# Print approx. hours until next Moon sign
# (needs PySwissEph)
# 2014-07-08

import datetime
import swisseph as s

n = datetime.datetime.utcnow()

j = s.julday(n.year, n.month, n.day, n.hour + n.minute / 60.)
j2 = j

ra = (s.calc_ut(j, s.MOON))[0]
next_ra = 30.*(1+(ra//30.))
diff = 100

for it in range(15):
	ra = (s.calc_ut(j2, s.MOON))[0]
	if next_ra == 360 and ra < 25:
		h = -ra
	else:
		h = next_ra - ra
	diff = 27.321582/360. * h
	if abs(diff*24*60*60) < 1:
		break
	j2 += diff

h = 24 * (j2-j)

def plur(x):
	if x > 1:
		return 'n'
	else:
		return ''

def nat(h):
	if h > 24:
		h2 = int(h)
		d = h2//24
		if d > 1:
			dh = "%u Tage" % d
		else:
			dh = "einen Tag"
		hh = h2%24
		if hh > 1:
			hhh = "%u Stunden" % hh
		else:
			hhh = "eine Stunde"
		print("noch %s und %s" % (dh, hhh))
	elif h >= 1:
		h3 = int(h)
		m = (60*h)%60
		print("noch %u Stunde%s und %u Minuten" % (h3, plur(h3), m))
	else:
		m = (60*h)%60
		print("noch %u Minuten" % m)

nat(h)
