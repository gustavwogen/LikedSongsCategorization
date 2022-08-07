import os
import requests
import base64
import json


CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')



with open('tokens.json') as f:
    data = json.load(f)
    access_token = data['access_token']
    refresh_token = data['refresh_token']


base_url = "https://accounts.spotify.com"
endpoint = "/api/token"

query_params = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token
}

encoded_client = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('ascii')).decode('ascii')
headers = {
    "Authorization": f"Basic {encoded_client}",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(f"{base_url}{endpoint}", params=query_params, headers=headers)
print(response.text)