from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIFY_URI = os.environ["SPOTIFY_REDIRECT_URI"]
scope = "playlist-modify-private"


def create_song_list(user_input):
    user_url = f"https://www.billboard.com/charts/hot-100/{user_input}"
    response = requests.get(url=user_url)
    response.raise_for_status()

    song_data = response.text
    soup = BeautifulSoup(song_data, "html.parser")

    song_list = soup.select("li ul li h3")
    custom_list = []
    for item in song_list:
        custom_list.append(item.get_text().strip())

    return custom_list


def main():
    user_input = input("Enter a year you want to go back to YYYY-MM-DD: ")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri=SPOTIFY_URI,
                                                   scope=scope))
    song_list = create_song_list(user_input)
    playlist = sp.user_playlist_create(user=sp.me()['id'],
                                       name=f"Top tracks of {user_input}",
                                       public=False)
    playlist_id = playlist["id"]
    song_uris = []
    for item in song_list:
        results = sp.search(q=item, type='track')
        items = results['tracks']['items']
        if items:
            song_uris.append(items[0]['uri'])

    sp.playlist_add_items(playlist_id,
                          song_uris)


if __name__ == '__main__':
    main()
