import spotipy
import spotipy.util as util
from sptygenre import exceptions

def authorize(username):
	scope = 'playlist-read-private'
	token = util.prompt_for_user_token(username, scope)
	if token:
		return spotipy.Spotify(auth=token)
	else:
		raise exceptions.TokenException(username)