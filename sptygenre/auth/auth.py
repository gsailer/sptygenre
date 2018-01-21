import spotipy
import spotipy.util as util
from spotipy import oauth2
from sptygenre import exceptions

def authorize(username):
	scope = 'playlist-read-private'
	token = util.prompt_for_user_token(username, scope)
	if token:
		return spotipy.Spotify(auth=token)
	else:
		raise exceptions.TokenException(username)

# returns spotipy OAuth Object
def get_url_token(username):
	_client_id = ''
	_client_secret = ''
	_redirect_uri = ''
	scope = 'playlist-read-private'
	cache_path = ".cache-" + username
    sp_oauth = oauth2.SpotifyOAuth(_client_id, _client_secret, _redirect_uri, 
        scope=scope, cache_path=cache_path)
    token_info = sp_oauth.get_cached_token()
    return sp_oauth

