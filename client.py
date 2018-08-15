import socket
import time
import sys
s = socket.socket()

port = int(sys.argv[1])

s.connect(("172.20.51.18", port))

while True:
	st = s.recv(1024)
	print(st)
	#s.send("ok then".encode())
	time.sleep(5)
s.close()


