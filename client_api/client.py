from settings import CID, SECRET
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

class ClientConnection:
    def __init__(self) -> None:
        client_credentials_manager = SpotifyClientCredentials(client_id=CID, client_secret=SECRET)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)