#!/usr/bin/env python

import subprocess, re

cmd = "bash /home/martin/bin/conkraw"

r = subprocess.check_output(cmd.split(), universal_newlines = True)


c = (
("${color red}", "\033[1;31;40m"),
("${color green}", "\033[1;32;40m"),
("${color yellow}", "\033[1;33;40m"),
("${color}", "\033[0m"),
)

for l in r.splitlines():
	for x in c:
		l = l.replace(x[0], x[1])
	l = re.sub(r"\$\{.+?\}", '', l)
	print(l)


