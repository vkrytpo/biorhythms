#!/usr/bin/env python
"""
Compute biorhythm compatibility

2011-08-30

Inspired by http://www.biorhythmonline.com/comp.php
"""

from datetime import date
from math import sin, pi
from pylab import *

rc(('xtick.major','xtick.minor','ytick.major','ytick.minor'), pad=10)

dd,mm,yy=10,11,1925	# Richard Burton
dd2,mm2,yy2=27,2,1932	# Liz Taylor

# computation method:
method = 1	# 1: summed phase; 0: phase difference

# (See http://www.brianapps.net/palmbio/compatibilitycomparison.png for
#  the differences between computation methods.)

#----------------------------------------------------------------------

s1 = "%04u-%02u-%02u" % (yy,mm,dd)
s2 = "%04u-%02u-%02u" % (yy2,mm2,dd2)

print ("Compatibility between",s1,"and",s2)
print (47*'-')

t1 = date(yy,mm,dd).toordinal()
t2 = date(yy2,mm2,dd2).toordinal()

lag = abs(t2-t1)

lag_p = lag % 23
lag_e = lag % 28
lag_i = lag % 33

lag_int = lag % 38
lag_aes = lag % 43
lag_awa = lag % 48
lag_spi = lag % 53

print ("lags (PEI):", lag_p,lag_e,lag_i)

avg1, avg2 = 0,0
out = []

def ana_lag(s, l, t):
	global avg1, avg2

	# from http://www.brianapps.net/palmbio/compatibility.html:
	if method:
		qq = 100.*abs(cos(pi*l/t))	# summed maximum method
	else:
		qq = 200./t*abs(l-t/2.)		# phase difference
	print (s, round(qq), "%")
	avg1 += qq
	avg2 += qq
	out.append(qq)

ana_lag("compat physical:    ", lag_p, 23)
ana_lag("compat emotional:   ", lag_e, 28)
ana_lag("compat intellectual:", lag_i, 33)
avg1f = int(.5+avg1/3.)
print ("average: ", avg1f, "%")

ana_lag("compat intuitive: ", lag_int, 38)	# aka compassion
ana_lag("compat aesthetic: ", lag_aes, 43)
ana_lag("compat awareness: ", lag_awa, 48)
ana_lag("compat spiritual: ", lag_spi, 53)
avg2f = int(.5+avg2/7.)
print ("total average: ", avg2f, "%")

tnam = ('Emotional','Physical','Intellectual','Main Average','Spiritual','Awareness','Intuitive','Aesthetic','Total Average')

figure(figsize = (12,7))
barh(8.5, out[1], align='center', color='#990000')
barh(7.5, out[0], align='center', color='#008000')
barh(6.5, out[2], align='center', color='#0000aa')
barh(5.5, avg1f, color="k", align='center')
barh(4.5, out[6], align='center', height=0.6, color='#5900bd')
barh(3.5, out[5], align='center', height=0.6, color='#009aa0')
barh(2.5, out[3], align='center', height=0.6, color='#643c00')
barh(1.5, out[4], align='center', height=0.6, color='#ab008d')
barh(.5,  avg2f, color="k", align='center', height=0.6)

yticks(arange(8.5,-.5,-1), tnam)
xlim((0,100))
xlabel("%")

x = 102
text(x,8.5, "%u%%" % round(out[1]), va="center")
text(x,7.5, "%u%%" % round(out[0]), va="center")
text(x,6.5, "%u%%" % round(out[2]), va="center")
text(x,5.5, "%u%%" % round(avg1f), va="center")
text(x,4.5, "%u%%" % round(out[6]), va="center")
text(x,3.5, "%u%%" % round(out[5]), va="center")
text(x,2.5, "%u%%" % round(out[3]), va="center")
text(x,1.5, "%u%%" % round(out[4]), va="center")
text(x,.5,  "%u%%" % round(avg2f), va="center")

title("Compatibility between %04u-%02u-%02u and %04u-%02u-%02u" % (yy,mm,dd,yy2,mm2,dd2))

fn = "%04u-%02u-%02u_and_%04u-%02u-%02u.pdf" % (yy,mm,dd,yy2,mm2,dd2)
savefig(fn)

show()
