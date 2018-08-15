#server.py

import socket
import datetime

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cli_ip = "172.20.51.255"
port = 2020

servsock.bind(("", port))

servsock.listen(5)

'''
while True:
	c, addr = servsock.accept()
	print("got connection from ", addr)
	message = "hi " + str(addr)
	c.send( message.encode())
	c.close()
'''

while True:
	data, addr = serversock.recvfrom(1024)
	print( "recieved message: %s from %s"%(data, addr))

