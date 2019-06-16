#!/usr/bin/env python
"""
Plot biorhythm. Includes secondary pulses

2011-08-29

From http://glowingpython.blogspot.com/2011/07/how-to-plot-biorhythm.html
and http://www.spiritualplatform.org/library/biorhythms.html
"""

dd,mm,yy=31,1,1956	# Guido van Rossum


from datetime import date
import matplotlib.dates
from pylab import *
from numpy import array,sin,pi

def sig(q):
	if q>=0: return 1
	return 0

t0 = date(yy,mm,dd).toordinal()
t1 = date.today().toordinal()
t = array(range(t1-3,t1+31)) # range of 31 days

y =     (sin(2*pi*(t-t0)/23),  # Physical
         sin(2*pi*(t-t0)/28),  # Emotional
         sin(2*pi*(t-t0)/33),  # Intellectual
         sin(2*pi*(t-t0)/38),  # intuitive
         sin(2*pi*(t-t0)/43),  # aesthetic
         sin(2*pi*(t-t0)/48),  # awareness
         sin(2*pi*(t-t0)/53))  # spiritual

av3 = (y[0]+y[1]+y[2])/3.
av7 = (y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6])/7.

# converting ordinals to date
label = []
for p in t:
 label.append(date.fromordinal(p))

fig = figure(figsize=(14,7))
ax = fig.gca()
plot(label,y[0], color="r", linewidth=4, alpha=.7)
plot(label,y[1], color="b", linewidth=4, alpha=.7)
plot(label,y[2], color="g", linewidth=4, alpha=.7)
plot(label,av3, linewidth=2, linestyle="--", color="black")
plot(label,.5*(y[0]+y[1]),label,.5*(y[1]+y[2]),label,.5*(y[2]+y[0]), linewidth=2, alpha=.65)
plot(label,y[3],label,y[4],label,y[5],label,y[6], linewidth=2, alpha=.3)
plot(label,.5*(y[3]+y[1]),label,.5*(y[3]+y[2]),label,.5*(y[3]+y[0]), linewidth=4, alpha=.5, linestyle="dotted")
plot(label,av7, linewidth=4, linestyle="--", color="black")

def f(x):
	return 50.*(x+1)

for n in range(len(t)-1):
	print ("%s %3.1f %3.1f %3.1f" % (label[n], f(y[0][n]), f(y[1][n]), f(y[2][n])))
	if ( sig(y[0][n])!=sig(y[0][n+1]) or
	     sig(y[1][n])!=sig(y[1][n+1]) or
	     sig(y[2][n])!=sig(y[2][n+1]) ):
		print (label[n], "***")

# adding a legend
legend(['Physical', 'Emotional', 'Intellectual','AVERAGE-3',
		'Passion','Wisdom','Mastery',
		'Intuitive','Aesthetic','Awareness','Spiritual',
		'Psychic', 'Success', 'Perception'
		,'AVERAGE-7'])
# formatting the dates on the x axis
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b'))
axhline(0, color="black", linewidth=1.4)
grid(True, linestyle="-", alpha=.3)
xlim((t[0],t[-1]))
a = date.today()
title("%02u.%02u.%04u (Alter: %u Tage am %02u.%02u.%04u)" % (dd,mm,yy, t1-t0, a.day, a.month, a.year))

fn = "%04u-%02u-%02u.pdf" % (yy,mm,dd)
savefig(fn)

show()
