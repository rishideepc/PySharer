from vidstream import ScreenShareClient
import threading

sender= ScreenShareClient('192.168.137.1', 9999)


tr= threading.Thread(target=sender.start_stream)
tr.start()

while input("") != 'STOP':
    continue

sender.stop_stream()