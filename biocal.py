#!/usr/bin/env python3

"""
Print a whole-year biorhythm PEI calendar as a DIN-A4 PDF
with the ReportLab module

check mark = high
downward triangle = low
star = critical day

2017-07-08

"""

import sys, datetime

from reportlab.lib import colors
from reportlab.platypus import BaseDocTemplate, Table, TableStyle, Frame, PageTemplate
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm, mm, inch

try:
	year = int(sys.argv[1])
except:
	print("Please add a year on the commandline")
	sys.exit(1)

by, bm, bd = 1990, 1, 1

width, height = A4[1] * 127 / 360, A4[0] * 127 / 360	# A4 landscape frame,
							# converted from points to mm

pagesize = (width * mm, height * mm)
F=Frame(0, 0, width * mm, height * mm,
                  leftPadding =   .5 * inch,
                  bottomPadding = .5 * inch,
                  rightPadding =  .5 * inch,
                  topPadding =    .5 * inch,)
PT = PageTemplate(id = "calendar", frames = [F,])

doc = BaseDocTemplate("biocal_%4u–%02u–%02u_%u.pdf" % (by, bm, bd, year))
doc.pagesize = landscape(A4)
doc.addPageTemplates([PT,])
doc.title = "%u biorhythm calendar for %4u–%02u–%02u" % (year, by, bm, bd)
elements = []

dnamelist = 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'
mnamelist = [['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]

data =  list(mnamelist)

wa=(
((1,12,13),(7,18)),
((1,15),(8,22)),
((1,17,18),(9,26))
)

def getbr(y, m ,d):
	o = ['', '', '']
	t0 = datetime.date(by,bm,bd).toordinal()
	t1 = datetime.date(y, m, d).toordinal()

	for c in range(3):
		p = 23 + 5 * c
		v = ((t1 - t0) % p) + 1
		if (v - 1) <= p / 2:
			o[c] = '✔'
		if (v - 1) >= p / 2:
			o[c] = '▼'
		if v in wa[c][0]:
			o[c] = '★'
	return ''.join(o)

def getcell(y, m, d):
	try:
		t = datetime.date(y, m, d).toordinal()
	except:
		return ['']
	return ['%u %s %s' % (d, dnamelist[datetime.date(y, m, d).weekday()], getbr(y, m, d)  )]

def isweekend(y, m, d):
	try:
		t = datetime.date(y, m, d).toordinal()
	except:
		return False
	return datetime.date(y, m, d).weekday() > 4

we = []
for day in range(1, 32):
	d2 = []
	for month in range(1, 13):
		d2 += getcell(year, month, day)
		if isweekend(year, month, day):
			we.append((month - 1, day))
	data.append(d2)

data.append((year,) + ('%4u–%02u–%02u' % (by, bm, bd),)  + 10 * ('',))

t = Table(data, rowHeights=(.55 * cm))
t.setStyle(TableStyle([
        ('FONTSIZE', (0,0), (-1,1), 11),
        ('FONTSIZE', (0,1), (-1,-2), 8),
        ('FONTSIZE', (0,-1), (-1,-1), 12),
        ('ALIGN',(0,0),(-1,1),'CENTER'),
        ('ALIGN',(0,1),(-1,-1),'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-2), 0.25, colors.black),
        ('BOX', (0,0), (-1,-2), 1.50, colors.black),
        ('BOX', (0,1), (-1,-2), 1.50, colors.black),
         ]))

for a in range(12):
	t._argW[a]=2.2*cm
for wx, wy in we:
	t.setStyle(TableStyle([
		('BACKGROUND', (wx, wy), (wx, wy), '#aaaaaa'),
		]))
elements.append(t)
doc.build(elements)


