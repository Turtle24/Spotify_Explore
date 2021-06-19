from settings import CID, SECRET
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

class ClientConnection:
        client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
        _client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)