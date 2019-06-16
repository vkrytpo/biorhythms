#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Show biorhythm warnings like the KOSMOS-1 calculator with Conky
P: physical
E: emotional
I: intellectual

2013-08-23

Red: critical days
Orange: mini-critical days
See http://decodesystems.com/kosmos-1.html

Dominant cycle is shown in parentheses.

argument 1: number of days in advance (today = 0)

"""

dd,mm,yy=1,1,1990

from datetime import date
from sys import argv
from math import sin,pi

t0 = date(yy,mm,dd).toordinal()
t1 = date.today().toordinal()

wa=(
((1,12,13),(7,18)),
((1,15),(8,22)),
((1,17,18),(9,26))
)

s = {'_': '${color green}●${color}', 'y': '${color yellow}●${color}', 'r': '${color red}●${color}'}

out = ""

t = t1 + int(argv[1])

w = ['_','_','_']
o = ['*','*','*']
perc = [0,0,0]
for c in range(3):
    p = 23+5*c
    perc[c] = 100.*sin(2*pi*(t-t0)/p)
    v = ((t-t0) % p)+1
    if (v-1) <= p/2:
        o[c] = 'H'
    if (v-1) >= p/2:
        o[c] = 'T'
    if v in wa[c][0]:
        w[c] = 'r'
        o[c] = 'K'
    if v in wa[c][1]:
        w[c] = 'y'
for x in w:
    out += s[x] + ' '
for x in o:
    out += x + ' '

if perc[0]>perc[1] and perc[0]>perc[2]:
    out += '(P)'
elif perc[1]>perc[0] and perc[1]>perc[2]:
    out += '(E)'
else:
    out += '(I)'

print(out)
