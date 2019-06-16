#!/usr/bin/env python
"""
Plot biorhythm for a whole year.

2011-08-30

Based on http://glowingpython.blogspot.com/2011/07/how-to-plot-biorhythm.html

Usage:
  python bioyear.py [year]

If year is not specified, the current year is used.

"""

dd,mm,yy=31,1,1956	# Guido van Rossum


from datetime import date
import matplotlib.dates
from pylab import *
from numpy import array,sin,pi
from sys import argv

if len(argv)<2:
	year = date.today().year	# current year
else:
	year = int(argv[1])		# read from command line

print ("Biorhythm for year", year)

def sig(q):
	if q>=0: return 1
	return 0

def isleap(x):
	if not (x%400): return True
	if not (x%100): return False
	if not (x%4): return True

if isleap(year):
	dur = 366
else:
	dur = 365

t0 = date(yy,mm,dd).toordinal()
t1 = date(year,1,1).toordinal()
t = array(range(t1,t1+dur+2)) # one year

y =     (sin(2*pi*(t-t0)/23),  # Physical
         sin(2*pi*(t-t0)/28),  # Emotional
         sin(2*pi*(t-t0)/33))  # Intellectual

av3 = (y[0]+y[1]+y[2])/3.

# converting ordinals to date
label = []
for p in t:
	label.append(date.fromordinal(p))

def f(x):
	return 50.*(x+1)

# print critical days:
for n in range(len(t)-1):
	#print "%s %3.1f %3.1f %3.1f" % (label[n], f(y[0][n]), f(y[1][n]), f(y[2][n]))
	if ( sig(y[0][n])!=sig(y[0][n+1]) or
	     sig(y[1][n])!=sig(y[1][n+1]) or
	     sig(y[2][n])!=sig(y[2][n+1]) ):
		print (label[n], "***")

fig = figure(figsize=(11,16))

seasname = ("January through March", "April through June", "July through September", "October through December")
start = array((0,90,181,273,365))
if isleap(year):
	start[1:] = start[1:]+1

for seas in range(4):
	subplot(411+seas)
	aa = start[seas]
	bb = start[seas+1]+1
	ax = fig.gca()
	plot(label[aa:bb],y[0][aa:bb], color="r", linewidth=4, alpha=.7)
	plot(label[aa:bb],y[1][aa:bb], color="b", linewidth=4, alpha=.7)
	plot(label[aa:bb],y[2][aa:bb], color="g", linewidth=4, alpha=.7)
	plot(label[aa:bb],av3[aa:bb], linewidth=2, linestyle="--", color="black")

	# formatting the dates on the x axis
	ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b'))
	axhline(0, color="black", linewidth=1.4)
	grid(True, linestyle="-", alpha=.5)
	xlim((t[aa],t[bb]))
	title("%04u-%02u-%02u (%s %u)" % (yy, mm, dd, seasname[seas],year))

fn = "%04u-%02u-%02u_year_%u.pdf" % (yy,mm,dd,year)
savefig(fn)

show()
