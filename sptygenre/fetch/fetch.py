from sptygenre import exceptions
from wordcloud import WordCloud

class Fetcher(object):
    def __init__(self, uri, spotipyAPI):
        self._spotipy = spotipyAPI
        self._uri = uri
    # fetches playlist from spotify
    def fetch_playlist(self):
        username = self._uri.split(':')[2]
        playlist_id = self._uri.split(':')[4]
        playlist = self._spotipy.user_playlist(username, playlist_id)["tracks"]
        if playlist:
            return playlist
        else:
            raise exceptions.FetchingException(playlist_id, "Failed fetching playlist with uri {}".format(self._uri))

    # gets all artists in playlist
    # and finds all returns all
    # genres as a list of lists of genres
    def get_genres_from_playlist(self, playlist):
        ids = []
        if playlist['total'] < 100:
            for i in range(0, playlist['total']):
                id = playlist["items"][i]["track"]["artists"][0]["id"]
                ids.append(id)
            if self._spotipy.next(playlist):
                playlist = self._spotipy.next(playlist)
        else:
            while playlist['next']:
                for i in range(0,playlist['total']):
                    id = playlist["items"][i]["track"]["artists"][0]["id"]
                    ids.append(id)
                playlist = self._spotipy.next(playlist)
        genres = []
        # only 50 artists max because api
        while ids:
            artists = self._spotipy.artists(ids[:49])
            if not artists:
                raise exceptions.FetchingException("artists", "Failed fetching artists: {}", ids[:49])
            for i in range(0,len(artists["artists"])):
                genre = artists["artists"][i]["genres"]
                if genre in genres:
                    continue
                genres.append(genre)
            ids = ids[49:]
        return genres

    # checks for duplicates in list of list of strings and writes
    # items into dict with weight as value
    def quantize_genres(self, genres):
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

    # returns wordcloud
    def fetch_wordcloud(self):
        quant_genres =  self.quantize_genres(self.get_genres_from_playlist(self.fetch_playlist()))
        return WordCloud(width=2400, height=1600, margin=2).generate_from_frequencies(quant_genres)