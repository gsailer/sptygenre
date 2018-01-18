import sys
import sptygenre
from sptygenre.auth import auth
from sptygenre.fetch import fetch
from sptygenre.ui import draw
from sptygenre import exceptions

def main():
	if len(sys.argv) != 3:
		print("Usage: sptygenre [playlist username uri]")
		print("Example: spotify:user:spotify:playlist:37i9dQZF1DXdPec7aLTmlC")
		print("Version: {}".format(sptygenre.__version__))
		sys.exit(2)
	username = sys.argv[1]
	uri = sys.argv[2]

	try:
		s = auth.authorize(username)
	except exceptions.TokenException as e:
		print(e.msg)
		sys.exit(1)
	try:
		fetcher = fetch.Fetcher(uri, s)
		playlist_wordcloud = fetcher.fetch_wordcloud()
	except Exception as e:
		print(e.msg)
		sys.exit(1)
	draw.draw_wordcloud_with_matplot(playlist_wordcloud)

if __name__ == '__main__':
	main()