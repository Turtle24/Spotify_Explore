from typing import OrderedDict
from client_api.client import ClientConnection
from plyer import notification
import csv
from datetime import time

class DataCapture:
    def __init__(self) -> None:
        self.spotifyData = None
        self.top_artists = ['Drake']
        self.latest_release = OrderedDict()
        self._client = ClientConnection.sp
    
    def addArtist(self, artist):
        res = self._client.search(q=artist, limit=1)
        if res and not self.latest_release.get(res['tracks']['items'][0]['artists'][0]['id']):
            self.top_artists.append(artist)
        return 

    def latestSong(self, artist):
        res = self._client.search(q=artist, limit=1)
        self.latest_release[res['tracks']['items'][0]['artists'][0]['id']] = f"{res['tracks']['items'][0]['artists'][0]['name']} - {res['tracks']['items'][0]['name']}"
        with open("artists.csv", "w", newline='') as csvfile:
            fieldnames = ['artist_id', 'new_song', 'status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'artist_id': res['tracks']['items'][0]['artists'][0]['id'], 'new_song': f"{res['tracks']['items'][0]['artists'][0]['name']} - {res['tracks']['items'][0]['name']}", 'status': 0})
        return f"{res['tracks']['items'][0]['artists'][0]['name']} - {res['tracks']['items'][0]['name']}"

    def updateStatus(self, id):
        with open("artists.csv", "w", newline='') as csvfile:
            fieldnames = ['artist_id', 'new_song', 'status']

class NotificationHandler:
    
    check_status = False
    # building logic
    def notification_check(self):
        if last != new:
            self.check_status = False

    def notify(self):
        if not self._client:
            print('No data was retrieved!')
        
        with open('artists.csv', newline='') as csvfile:
            check = csv.reader(csvfile, delimiter=',')
            check = [i for i in check][0]
            if check[-1] == 1:
                return 'No new songs'
            else:
                new_song = check[1]
                check[-1] = 0
        name = new_song.split("-")[0]
        try:
            notification.notify(
                
                title = f"New song from: {name}",
                    
                message = f"{new_song}",
                app_icon = "banner.ico",
                timeout  = 50
                ), time.sleep(60*60*4)
                    
        except Exception as e:
            print(f"Something {e}")
