from client_api.client import ClientConnection
import json

class DataCapture:
    def __init__(self) -> None:
        self.spotifyData = None
        self.top_artists = []
        self.name_track_dict = {}
        self.old_name_track_dict = {}
        self.sp = ClientConnection().sp
    
    def topArtists(self, artist):
        res = self.sp.search(q=artist, limit=1)
        # print(res['tracks'])
        return json.dumps(res['tracks']['items'], indent=2)

    # # get artist data
    # def getArtistAndSongs(self, name):
    #     if name in top_artists:
    #         return sp.search(q=name, limit=1)

    # # insert artist data into dictionary 
    # def artistAndTrack(self, artistlst):
    #     for artist in top_artists:
    #         artist_data = getArtistAndSongs(artist)
    #         name = artist_data['tracks']['items'][0]['album']['artists'][0]['name']
    #         track_name = artist_data['tracks']['items'][0]['name']
    #         if name not in name_track_dict:
    #             name_track_dict[name] = track_name
    #         elif name in name_track_dict:
    #             old_name_track_dict = name_track_dict
    #     return name_track_dict


    # # if we fetched data
    # if (sp == None):
    #     print('No data was retrieved!')

    # # Get the latest song
    # for song in top_artists:
    #     current_artist_data = artistAndTrack(song)
    # # repeating the loop for multiple times
    # # try and except is here to test different data structures
    # try:
    #     while True:
    #         if name_track_dict == old_name_track_dict:
    #             break
    #         for artist in current_artist_data.items():
    #             notification.notify(
    #             #title of the notification,
    #             title = "New Song From Favourite Artsit {}".format(datetime.date.today()),
    #             #the body of the notification
    #             message = f"Artist Name: {artist[0]}\nTrack Title: {artist[1]}",
    #             app_icon = "C:/Users/Aidan/Documents/Python_Master/Projects/Spotify Notification App/logo-app.ico",
    #             timeout  = 50
    #             ), time.sleep(60*60*4)
    #             #sleep for 4 hrs => 60*60*4 sec
    #             #notification repeats after every 4hrs
    # except KeyError:
    #     print("keyerror")
