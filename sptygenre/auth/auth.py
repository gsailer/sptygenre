import spotipy
import spotipy.util as util
from spotipy import oauth2
from sptygenre import exceptions

def authorize(username):
	scope = 'playlist-read-private'
	token = util.prompt_for_user_token(username, scope, client_id='3dab3c84034247168f7021f1f1128754', client_secret='d89c1072a0a84ae396998d08501a0b1c', redirect_uri='http://localhost:5000/callback/')
	if token:
		return spotipy.Spotify(auth=token)
	else:
		raise exceptions.TokenException(username)

# returns auth url
def get_auth_url(username):
    _client_id = ''
    _client_secret = ''
    _redirect_uri = ''
    scope = 'playlist-read-private'
    cache_path = ".cache-" + username
    sp_oauth = oauth2.SpotifyOAuth(_client_id, _client_secret, _redirect_uri, scope=scope, cache_path=cache_path)
    return sp_oauth.get_authorize_url()

# returns token for response url
def get_token(sp_oauth, response_url):
    code = oauth2.parse_response_code(response_url)
    token = sp_oauth.get_access_token(code)
    return token['access_token']