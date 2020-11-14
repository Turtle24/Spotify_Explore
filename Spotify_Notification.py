import datetime  # for reading present date
import time
import requests  
from plyer import notification  # for getting notification on your PC
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
# let there be no data initially
spotifyData = None

# Spotify Credentials and Secret
cid = 'CLIENT_ID_GOES_HERE'
secret = 'CLIENT_SECRET_GOES_HERE'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
                     =
                     client_credentials_manager)

# Artist list. Can use artist() and use IDs, URIs or URLS

top_artists = ['tom macdonald']

# dictionary for artist and song


name_track_dict = {}
# get artist function

def getArtistAndSongs(name):
    if name in top_artists:
        return sp.search(q=name, limit=1)

# search multiple artists and get the results *only saves the last artist...
def artistAndTrack(artistlst):
	for artist in top_artists:
		artist_data = getArtistAndSongs(artist)
		name = artist_data['tracks']['items'][0]['album']['artists'][0]['name']
		track_name = artist_data['tracks']['items'][0]['name']
		if name not in name_track_dict:
			name_track_dict[name] = track_name		
	return name_track_dict


# if we fetched data
if (sp == None):
	print('No data was retrieved!')

current_artist_data = artistAndTrack(top_artists)
for name in current_artist_data.items():
		artist_and_track = (name[0], name[1])

# repeating the loop for multiple times
try:
	while(True):
		for artist in artist_and_track:

			notification.notify(
			#title of the notification,
			title = "New Song From Favourite Artsit {}".format(datetime.date.today()),
			#the body of the notification
			message = f"Artist Name: {artist_and_track[0]}\nTrack Title: {artist_and_track[1]}",
        	app_icon = "C:/Users/Admin/Documents/CompSci/Projects/DesktopNotifierApp/logologo.ico",
        	timeout  = 50
        	), time.sleep(60*60*4)
 			#sleep for 4 hrs => 60*60*4 sec
 			#notification repeats after every 4hrs
except KeyError:
	print("keyerror")
