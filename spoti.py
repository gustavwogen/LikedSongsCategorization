import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from collections import defaultdict
from pprint import pprint

scope = 'playlist-read-private playlist-modify-private user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
artist_set = set()
genre_songs = defaultdict(list)
artist_genres = defaultdict(list)
song_data = {}

def add_song_to_playlist(song_id, playlist_id):
    return


for i in range(10):
    results = sp.current_user_saved_tracks(limit=50, offset=50*i, market='SE')
    for idx, item in enumerate(results['items']):
        track = item['track']
        album = track['album']
        album_name = album['name']
        album_id = album['id']
        album_info = sp.album(album_id)
        album_upc = album_info['external_ids']['upc']
        total_tracks_on_album = album['total_tracks']
        track_id = track['id']
        artists = track['artists']
        main_artist_data = artists[0]
        main_artist_name = main_artist_data['name']
        artist_set.add(main_artist_name)
        main_artist_id = main_artist_data['id']
        main_artist_genres = sp.artist(main_artist_id)['genres']
        song_data[track['name']] = {
                                   'track_id': track_id,
                                   'duration_ms': track['duration_ms'],
                                   'track_number': track['track_number'],
                                   'artist': main_artist_name,
                                   'artist_id': main_artist_id,
                                   'album_name': album_name,
                                   'album_id': album_id,
                                   'album_upc': album_upc,
                                   'album_release_date': album['release_date'],
                                   'num_tracks_on_album': total_tracks_on_album
                                }
        # for genre in main_artist_genres:
        #     genre_songs[genre].append({track['name']: track_id})
        #     artist_genres[main_artist_name].append(genre)


# popular_genres = dict(sorted(genre_songs.items(), key=lambda item: len(item[1]), reverse=True))


# with open('genres_songs.json', 'w') as outfile:
#     json.dump(popular_genres, outfile)

# with open('artists_genres.json', 'w') as outfile:
#     json.dump(artist_genres, outfile)

with open('song_data.json', 'w') as song_file:
    json.dump(song_data, song_file)

