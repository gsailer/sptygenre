#!/usr/bin/env python
import matplotlib.pyplot as plt
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from wordcloud import WordCloud

# fetches playlist from spotify
def fetch_playlist(uri):
	username = uri.split(':')[2]
	playlist_id = uri.split(':')[4]

	client_credentials_manager = SpotifyClientCredentials()
	s = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	playlist = s.user_playlist(username, playlist_id)["tracks"]
	return playlist

# gets all artists in playlist
# and finds all returns all
# genres as a list of lists of genres
def get_genres_from_playlist(playlist):
	ids = []
	if playlist['total'] < 100:
		for i in range(0,len(playlist)):
			id = playlist["items"][i]["track"]["artists"][0]["id"]
			ids.append(id)
		playlist = s.next(playlist)
	else:
		while playlist['next']:
			for i in range(0,len(playlist)):
				id = playlist["items"][i]["track"]["artists"][0]["id"]
				ids.append(id)
			playlist = s.next(playlist)
		
	genres = []
	# only 50 artists max because api 
	while ids:
		artists = s.artists(ids[:49])
		for i in range(0,len(artists["artists"])):
			genre = artists["artists"][i]["genres"]
			if genre in genres:
				continue
			genres.append(genre)
		ids = ids[49:]
	return genres

# checks for duplicates in list of list of strings and writes
# items into dict with weight as value
def quantize_genres(genres):
	individual_genres = []
	weighted_genres = {}
	for list in genres:
		for item in list:
			if item in individual_genres:
				weighted_genres[item] += 1
			else:
				individual_genres.append(item)
				weighted_genres[item] = 1
	return weighted_genres

# draws wordcloud from dict[string] = int
def drawWordCloud(weighted_genres):
	print("drawing wordcloud")
	wordcloud = WordCloud(width=2400, height=1600, margin=2).generate_from_frequencies(weighted_genres)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.margins(x=0, y=0)
	plt.show()

if __name__ == "__main__":
	# virtual envs for Creds
	os.environ["SPOTIPY_CLIENT_ID"] = 'Your App ClientID'
	os.environ["SPOTIPY_CLIENT_SECRET"] = 'Your Client Secret'
	os.environ["SPOTIPY_REDIRECT_URI"] = 'Your redirect uri for auth flow'

	# check sysargs
	if len(sys.argv) != 2:
		print "Usage: fetchsptygenre.py [playlist uri]"
		print "Example: spotify:user:g051x7db:playlist:3eXwHXkwGQLDZkj0UuR2H6"
		sys.exit(2)
	uri = sys.argv[1]
	drawWordCloud(quantize_genres(get_genres_from_playlist(fetch_playlist(uri))))
	