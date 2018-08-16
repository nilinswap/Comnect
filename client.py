import socket
import time
import sys
import random
cli_s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)

serv_port = 2020
serv_adr = "172.20.51.18"

cli_s.connect(( serv_adr, serv_port))
req_lis = ["sun", "black", "yin", "batman"]
while True:
	req_msg = random.choice(req_lis)
	print("sent request: ", req_msg)
	req_msg = req_msg.encode()
	result  = cli_s.send(req_msg)
	
	if not result:
		print("connection broken")
		exit()
	st = cli_s.recv(1024)
	if st == b'':
		print("connection broken")
		exit()

	print("\t\tgot reply: ", st)

	#s.send("ok then".encode())
	time.sleep(5)
cli_s.close()


