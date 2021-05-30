from data_capture.data_capture import DataCapture
from client_api.client import ClientConnection

test = ClientConnection()

dc = DataCapture()

print(dc.topArtists('Drake'))