from vidstream import StreamingServer
import threading

receiver= StreamingServer('192.168.137.1', 9999)

tr= threading.Thread(target=receiver.start_server)
tr.start()

while input("") != 'STOP':
    continue

receiver.stop_server()