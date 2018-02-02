import argparse
import sptygenre
from sptygenre.auth import auth
from sptygenre.fetch import fetch
from sptygenre.ui import draw, write
from sptygenre import exceptions
import sys


def main():
    parser = argparse.ArgumentParser(description='Analyse Spotify playlists for genres.', prog='sptygenre')
    parser.add_argument('username', help='Your Spotify username')
    parser.add_argument('uri', help='spotify playlist uri (Example: spotify:user:spotify:playlist:37i9dQZF1DXdPec7aLTmlC)')
    parser.add_argument('-f', '--file', help='Path to write png')
    parser.add_argument('--version', action='version', version="sptygenre {}".format(sptygenre.__version__))
    args = parser.parse_args()
    if not len(args.uri.split(':')) == 5:
        print("Please provide a valid spotify uri")
        sys.exit(1)
    try:
        s = auth.authorize(args.username)
    except exceptions.TokenException as e:
        print(e.msg)
        sys.exit(1)
    try:
        fetcher = fetch.Fetcher(args.uri, s)
        playlist_wordcloud = fetcher.fetch_wordcloud()
    except Exception as e:
        print(e.msg)
        sys.exit(1)
    if args.file is not None:
        write.cloud_to_file(args.file, playlist_wordcloud)
    else:
        draw.draw_wordcloud_with_matplot(playlist_wordcloud)

if __name__ == '__main__':
    main()
