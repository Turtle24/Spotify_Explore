from typing import OrderedDict
from connection.client import ClientConnection
from plyer import notification
import csv
from time import sleep


class DataCapture:
    def __init__(self) -> None:
        self.spotifyData = None
        self.top_artists = ['Drake']
        self.latest_release = OrderedDict()
        self._client = ClientConnection._client
        self._status = False
    
    def addArtist(self, artist: str):
        res = self._client.search(q=artist, limit=1)
        if res and not self.latest_release.get(res['tracks']['items'][0]['artists'][0]['id']):
            self.top_artists.append(artist)
        return 

    def latestSong(self, artist: str):
        res = self._client.search(q=artist, limit=1)
        self.latest_release[res['tracks']['items'][0]['artists'][0]['id']] = f"{res['tracks']['items'][0]['artists'][0]['name']} - {res['tracks']['items'][0]['name']}"
        with open("artists.csv", "w", newline='') as csvfile:
            fieldnames = ['artist_id', 'new_song', 'status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'artist_id': res['tracks']['items'][0]['artists'][0]['id'], 'new_song': f"{res['tracks']['items'][0]['artists'][0]['name']} - {res['tracks']['items'][0]['name']}", 'status': 0})
        return f"{res['tracks']['items'][0]['artists'][0]['name']} - {res['tracks']['items'][0]['name']}"

    def checkStatus(self, id: str) -> bool:
        self._status = False
        with open("artists.csv", "w", newline='') as csvfile:
            read = csv.reader(csvfile)
            for row in read:
                if row[0] == id and row[-1] == 0:
                    return True
        return False

class NotificationHandler(DataCapture):
    def __init__(self) -> None:
        super().__init__()
        self.check_status = self._status

    def notification_check(self) -> bool:
        if not self.check_status:
            return False
        else:
            return True

    def new_song_check(self) -> tuple:
        with open('artists.csv', newline='') as csvfile:
            check = csv.reader(csvfile, delimiter=',')
            check = [i for i in check][0]
            if check[-1] == 1:
                return 'No new songs'
            else:
                new_song = check[1]
                check[-1] = 0
        name = new_song.split("-")[0]
        return (name, new_song)

    def notify(self) -> None:
        if not self.notification_check():
            notification.notify(
                title = "No new songs"
            )
        if not self._client:
            print('No data was retrieved!')
        name, new_song = self.new_song_check()
        try:
            notification.notify(
                title = f"New song from: {name}",
                message = f"{new_song}",
                app_icon = "banner.ico",
                timeout  = 50
                ), sleep(60*60*4)
                    
        except Exception as e:
            print(f"Something went wrong {e}")
