#!/usr/bin/python
# Computer partner compatibility like Kosmos Astro
# (needs PySwissEph)
# 2016-02-27

# See page 12 of the Tandy Astro manual.

# Shows if persons have similar (+) or dissimilar (-):

# Sun - life purposes
# Mercury - ways of thinking
# Venus - likes and dislikes
# Mars - styles of action

# Example (L. Taylor and R. Burton):

# $ python tandy_astro.py 1925 11 10 1932 2 27
# 1925 11 10 1932 2 27
# 8 12 +
# 9 12 -
# 10 1 -
# 7 12 -

# First two numbers are the signs for each planet: 1 = Aries,..., 12 = Pisces
# "+ - - -" -> The Sun matches, everything else not so much.

import sys
import swisseph as s

y1,m1,d1,y2,m2,d2 = [int(x) for x in sys.argv[1:]]

print(y1,m1,d1,y2,m2,d2)

for b in s.SUN, s.MERCURY, s.VENUS, s.MARS:
	j = s.julday(y1, m1, d1, 12)
	ra = (s.calc_ut(j, b))[0]
	x1 = int(ra//30.)+1
	j = s.julday(y2, m2, d2, 12)
	ra = (s.calc_ut(j, b))[0]
	x2 = int(ra//30.)+1
	d = x2-x1
	if d < 0:
		d += 12
	if d in (0,2,4,6,8,10):
		f = "+"
	else:
		f = "-"
	print(x1, x2, f)

