import spotipy
from spotipy import oauth2
import spotipy.util as util
from sptygenre import exceptions

def authorize(username):
    scope = 'playlist-read-private'
    token = util.prompt_for_user_token(username, scope)
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
