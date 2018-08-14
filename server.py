import socket
import datetime
import sys
import time
s = socket.socket()
print("socket successfully created")
port = int(sys.argv[1])
s.bind(("",port))
s.listen(5)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c, addr = s.accept()
print("Got connection from ", addr)
while True:
	#c, addr = s.accept()
	#print("Got connection from", addr)
	#print(addr, "sent: ", c.recv(1024))
	st = (str(datetime.datetime.now())+"\n").encode()
	c.send(st)
	#print(addr, "sent: ", c.recv(1024))
	st = "Thank you:)\n".encode()
	#print(addr, "sent: ", c.recv(1024))
	c.send(st)
	time.sleep(2)
c.close()
s.close()
