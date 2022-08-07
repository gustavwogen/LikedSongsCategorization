import os
import requests


CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')



scope = 'playlist-read-private playlist-modify-private'


base_url = "https://accounts.spotify.com"
endpoint = "/authorize"

query_params = {
    "response_type": "code",
    "client_id": CLIENT_ID,
    "redirect_uri": REDIRECT_URI,
    "scope": scope
}


response = requests.get(f"{base_url}{endpoint}", params=query_params)

print(response.url)