#!/usr/bin/env python
import sys

with open("ranked_genres.data", "r") as f:
	raw = f.read()
try:
	rank = eval(raw)
except:
	print "Error: corrupted rank data?"
	sys.exit(1)
if len(rank) == 0:
	print "something didn't work as expected."
	sys.exit(1)
	
print "Most emergent genres in playlist:"
for x in rank:
	print "{}  -  weight: {}".format(x[0], x[1])