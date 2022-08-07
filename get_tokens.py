import os
import requests
import base64


CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')
AUTHORIZATION_CODE = "AQCx-E30_ZpvgMBJKdvOjSR2oNWDMlW-ZmcXmjpPEbyAY5FCJ1FV9T6AoGDjMdCqSxzCK-hgEAb8jv1UAY8T5kd9qzQgh-370YV_1xxbZAnEjYm8bu0-p4J9yObj59WFPTVvxP2JjzTfS-nO1-S1GmVI2CbhtC5AHIBPWgPNQzhRhTzbvv2q9qZ014TZ-Td7LPQ57ZAzLCr3sw-rPz0NcthyAkarIEBd18zNp3BWWgPZ-w"



scope = 'playlist-read-private playlist-modify-private'


base_url = "https://accounts.spotify.com"
endpoint = "/api/token"

query_params = {
    "grant_type": "authorization_code",
    "code": AUTHORIZATION_CODE,
    "redirect_uri": REDIRECT_URI
}

encoded_client = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('ascii')).decode('ascii')

headers = {
    "Authorization": f"Basic {encoded_client}",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(f"{base_url}{endpoint}", params=query_params, headers=headers)

print(response.text)