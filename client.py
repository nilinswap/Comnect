import socket
import sys, datetime

udp_ip_address = "xxx"
udp_port_no = 3030
message = "hello, server"

clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientsock.send(message.encode(), (udp_id_address, udp_port_no))

