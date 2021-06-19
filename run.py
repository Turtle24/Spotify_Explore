from data_capture.data_capture import DataCapture, NotificationHandler

if __name__ == "__main__":
    DataCapture().latestSong('Drake')
    NotificationHandler().notify()