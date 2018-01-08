#!/usr/bin/env python
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os, sys

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
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

client_credentials_manager = SpotifyClientCredentials()
s = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
playlist = s.user_playlist(username, playlist_id)["tracks"]

ids = []
# check playlist size, because of spotify paging object
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
	
names = []
# only 50 artists max because api 
while ids:
	artists = s.artists(ids[:49])
	for i in range(0,len(artists["artists"])):
		name = artists["artists"][i]["genres"]
		if name in names:
			continue
		names.append(name)
	ids = ids[49:]

with open("genres.json", "w") as f:
	f.write(json.dumps(names))
