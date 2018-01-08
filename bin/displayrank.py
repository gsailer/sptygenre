#!/usr/bin/env python
import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
	
#print "Most emergent genres in playlist:"
wc_dict = {}
for x in rank:
	wc_dict[x[0]] = x[1]
#	print "{}  -  weight: {}".format(x[0], x[1])
print "Drawing wordcloud for generes"
wordcloud = WordCloud(width=2400, height=1600, margin=2).generate_from_frequencies(wc_dict)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

