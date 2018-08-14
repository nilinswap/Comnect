import socket
import time
import sys
s = socket.socket()

port = int(sys.argv[1]) #2020 for server being behind router( mine)

s.connect(("172.40.71.15", port)) 
'''this is router's Ip. Further the 'port' is not the port of this process; it is the port at which server is to be requested. The port of this process (which is printed in first line of server.py) is arbitrary.'''
while True:
	st = s.recv(1024)
	print(st)
	#s.send("ok then".encode())
	time.sleep(5)
s.close()


