#!/usr/bin/python
# Print next moon quarter (requires PyEphem)
# 2017-10-29

import ephem

n = ephem.now()

p = [[ephem.next_full_moon(n),"🌕 Vollmond"],
[ephem.next_last_quarter_moon(n),"🌗 Letztes Viertel"],
[ephem.next_new_moon(n),"🌑 Neumond"],
[ephem.next_first_quarter_moon(n),"🌓 Erstes Viertel"]]

p.sort()

a = p[0]

h = 24*(a[0]-n)

def nat(h):
	h2 = round(h)
	if h > 24:
		d = h2//24
		if d > 1:
			dh = "%u Tagen" % d
		else:
			dh = "einem Tag"
		hh = h2 - 24*d
		if hh > 1:
			hhh = "%u Stunden" % hh
		else:
			hhh = "einer Stunde"
		return ("in %s und %s" % (dh, hhh))
	elif h >= 2:
		return ("in %u Stunden" % h2)
	elif h >= 1:
		m = 60*(h - 1)
		return ("in einer Stunde und %u Minuten" % m)
	else:
		m = 60*(h - int(h))
		return ("in %u Minuten" % m)

b = "${font Symbola:size=12}%s${font Droid Sans:size=11}%s\n${font Droid Sans:size=11}%s" % (a[1][:2], a[1][2:], nat(h))

print (b)
