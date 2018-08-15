import socket

udp_ip_address = "xxx"
udp_port_no = 2020

serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serversock.bind((udp_ip_address, udp_port_no))

while True:
	data, addr = serversock.recvfrom(1024)
	print( "message", data)
