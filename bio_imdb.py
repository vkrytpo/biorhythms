#!/usr/bin/env python
"""
Get birthdays and compute biorhythm compatibility

2014-01-13

Accepts (either one or two) IMDb ids, 'pers' list names, or dates (in YYYY-M-D format)

Examples:
	python bio_imdb.py nm0000093
	python bio_imdb.py nm0006683 nm0290556
	python bio_imdb.py Test2 nm0000093
	python bio_imdb.py nm0290556 Test
	python bio_imdb.py 1993-11-3 Test

Any other string as an argument performs a local database search (case is insignificant),
e.g. "python bio_imdb.py tom" will show all names in the database that contain "tom".
(This is useful for looking up IMDb ids of existing database entries.)

Calling the script without an argument lists all existing database entries.
"""

imp = True	# Save retrieved IMDb birthdays into local database?

import pickle, sys
assert sys.version >= '3', "*** Python 3 is required!"

try:
	imdb_cache = pickle.load(open("imdb_cache.dat", 'rb'))
	print(len(imdb_cache),"entries in database")
except:
	print("Creating empty IMDb cache...")
	imdb_cache = {}

pers=(
 ((1990,1,1),"You"),   
 ((1991,10,1),"Test"),   
 ((1991,12,1),"Test2"),
)
# Default partner is first 'pers' list entry:
yy,mm,dd = pers[0][0]
n1 = pers[0][1]

import sys, shutil
from datetime import date
from math import sin, cos, pi
import urllib.request

k = []
for x in imdb_cache.keys():
	k.append((imdb_cache[x][0], x))
k.sort()

if len(sys.argv) < 2:
	# print database contents and exit if there are no arguments
	for name, imdb in k:
		print(name, imdb)
	sys.exit(0)

if len(sys.argv) > 3:
	print("*** Please supply one or two arguments!")
	sys.exit(2)

dirty = False

def under(t):
	print(t)
	print(len(t) * '-')

def getdate(id):
	global imdb_cache, dirty

	# is the name in the list?
	for n in range(len(pers)):
		if pers[n][1].lower() == id.lower():
			yy2,mm2,dd2 = pers[n][0]
			return pers[n][1],yy2,mm2,dd2
	# is it a date?
	if "-" in id:
		yy2,mm2,dd2 = [int(x) for x in id.split("-")]
		return "X",yy2,mm2,dd2
	# Print cache name search results and exit if not a valid IMDb id
	if id[:2] != "nm":
		under('Search results for "%s":' % id)

		for name, imdb in k:
			if id.lower() in name.lower():
				print(name, imdb)
		sys.exit(0)
	try:
		return imdb_cache[id]
	except:
		dirty = True
	url = "http://www.imdb.com/name/%s/" % id
	response = urllib.request.urlopen(url)
	html = response.read()
	html = html.decode('utf-8')

	n2 = ''
	for l in html.split("\n"):
		if "<title" in l and not n2:
			s = l.split(" - ")[0]
			n2 = s.split(">")[1]
		if "<time datetime=" in l:
			dat = l.split('"')[1]
			yy2,mm2,dd2 = [int(x) for x in dat.split("-")]
			break
	try:
		imdb_cache[id] = (n2,yy2,mm2,dd2)
		return n2,yy2,mm2,dd2
	except:
		print("*** No birthdate available! ***")
		sys.exit(1)

n2,yy2,mm2,dd2 = getdate(sys.argv[1])
if len(sys.argv) > 2:
	n1,yy,mm,dd = getdate(sys.argv[2])

# computation method:
method = 1	# 1: summed phase; 0: phase difference

s1 = "%04u-%02u-%02u" % (yy,mm,dd)
s2 = "%04u-%02u-%02u" % (yy2,mm2,dd2)

under("Compatibility between %s (%s) and %s (%s)" % (n1,s1,n2,s2))

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

print("lags (PEI):", lag_p,lag_e,lag_i)

avg1, avg2 = 0,0
out = []

def ana_lag(s, l, t):
	global avg1, avg2

	# from http://www.brianapps.net/palmbio/compatibility.html:
	if method:
		qq = 100.*abs(cos(pi*l/t))	# summed maximum method
	else:
		qq = 200./t*abs(l-t/2.)		# phase difference
	print(s, round(qq), "%")
	avg1 += qq
	avg2 += qq
	out.append(qq)

ana_lag("compat physical:    ", lag_p, 23)
ana_lag("compat emotional:   ", lag_e, 28)
ana_lag("compat intellectual:", lag_i, 33)
avg1f = int(.5+avg1/3.)
print("average: ", avg1f, "%")

ana_lag("compat intuitive: ", lag_int, 38)	# aka compassion
ana_lag("compat aesthetic: ", lag_aes, 43)
ana_lag("compat awareness: ", lag_awa, 48)
ana_lag("compat spiritual: ", lag_spi, 53)
avg2f = int(.5+avg2/7.)
print("total average: ", avg2f, "%")

if dirty and imp:
	try:
		shutil.move("imdb_cache.dat", "imdb_cache.dat.bak")
	except:
		print("(Failed to create backup of old database file.)")
	pickle.dump(imdb_cache, open("imdb_cache.dat", 'wb'), 1)

# Print likely nature of relationship:
m = 70
m2 = 50
if out[0] > m and out[1] > m and out[0] > out[2] and out[1] > out[2]:
	print("==> LOVERS")
	if out[2] < m2:
		print("    with problems")
elif out[1] > m and out[2] > m and out[1] > out[0] and out[2] > out[0]:
	print("==> FRIENDS")
	if out[0] < m2:
		print("    with problems")
elif out[0] > m and out[2] > m and out[0] > out[1] and out[2] > out[1]:
	print("==> COLLEAGUES")
	if out[1] < m2:
		print("    with problems")
